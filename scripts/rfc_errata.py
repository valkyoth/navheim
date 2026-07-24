#!/usr/bin/env python3
"""Validate or live-check Navheim's RFC Editor errata drift snapshot."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import urllib.parse
import urllib.request
from datetime import date
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "standards/rfc/SOURCES"
SNAPSHOT = ROOT / "standards/rfc/ERRATA.json"
ENDPOINT = "https://errata.rfc-editor.org/search/"
STATUSES = ("Verified", "Reported", "Held for Document Update", "Rejected")
LIFECYCLES = ("pre-implementation", "legacy-reference-only")


class ErrataError(RuntimeError):
    """Malformed or drifting RFC errata metadata."""


class ErrataTableParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.heading = False
        self.heading_text: list[str] = []
        self.status: str | None = None
        self.in_row = False
        self.in_cell = False
        self.cell_text: list[str] = []
        self.cells: list[str] = []
        self.records: list[dict] = []

    def handle_starttag(self, tag: str, _attrs) -> None:
        if tag == "h2":
            self.heading = True
            self.heading_text = []
        elif tag == "tr":
            self.in_row = True
            self.cells = []
        elif tag == "td" and self.in_row:
            self.in_cell = True
            self.cell_text = []

    def handle_data(self, data: str) -> None:
        if self.heading:
            self.heading_text.append(data)
        if self.in_cell:
            self.cell_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "h2" and self.heading:
            heading = "".join(self.heading_text).strip()
            self.status = next(
                (status for status in STATUSES if heading.startswith(status)), None
            )
            self.heading = False
        elif tag == "td" and self.in_cell:
            self.cells.append(" ".join("".join(self.cell_text).split()))
            self.in_cell = False
        elif tag == "tr" and self.in_row:
            self.in_row = False
            if self.cells and self.status is not None:
                self._record()

    def _record(self) -> None:
        match = re.fullmatch(r"RFC([0-9]+) \(([0-9]+)\)", self.cells[0])
        if match is None or len(self.cells) != 7:
            raise ErrataError(f"unrecognized errata row: {self.cells}")
        identifier = int(match.group(2))
        self.records.append(
            {
                "rfc": int(match.group(1)),
                "id": identifier,
                "source": f"https://errata.rfc-editor.org/eid{identifier}/",
                "status": self.status,
                "section": self.cells[1],
                "type": self.cells[2],
                "reported": self.cells[6],
            }
        )


def source_lifecycles() -> dict[int, str]:
    result: dict[int, str] = {}
    pattern = re.compile(
        r"^(\d+) https://www\.rfc-editor\.org/rfc/rfc\d+\.txt ([a-z0-9-]+)$"
    )
    for line in SOURCES.read_text(encoding="ascii").splitlines():
        if not line or line.startswith("#"):
            continue
        match = pattern.fullmatch(line)
        if match is None:
            raise ErrataError(f"invalid RFC source line: {line!r}")
        number = int(match.group(1))
        lifecycle = (
            "legacy-reference-only"
            if "legacy" in match.group(2)
            else "pre-implementation"
        )
        result[number] = lifecycle
    return result


def fetch_rfc(number: int) -> list[dict]:
    query = urllib.parse.urlencode(
        {"rfc_number": number, "status": "any", "presentation": "table"}
    )
    request = urllib.request.Request(
        f"{ENDPOINT}?{query}",
        headers={"User-Agent": "navheim-rfc-review/0.1"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            html = response.read().decode("utf-8")
    except OSError as error:
        raise ErrataError(f"cannot fetch RFC {number} errata: {error}") from error
    parser = ErrataTableParser()
    parser.feed(html)
    if any(record["rfc"] != number for record in parser.records):
        raise ErrataError(f"RFC {number} response contained another RFC")
    return sorted(parser.records, key=lambda record: record["id"])


def fingerprint(records: list[dict]) -> str:
    encoded = json.dumps(records, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def current_record(number: int, lifecycle: str) -> dict:
    records = fetch_rfc(number)
    return {
        "rfc": number,
        "lifecycle": lifecycle,
        "errata_ids": [record["id"] for record in records],
        "official_sha256": fingerprint(records),
    }


def validate(snapshot: dict) -> dict[int, dict]:
    if set(snapshot) != {"schema", "checked_at", "source", "rfcs"}:
        raise ErrataError("errata snapshot top-level fields are invalid")
    if snapshot["schema"] != 1 or snapshot["source"] != ENDPOINT:
        raise ErrataError("errata snapshot schema or source is invalid")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", snapshot["checked_at"]):
        raise ErrataError("errata snapshot date is invalid")
    expected = source_lifecycles()
    records: dict[int, dict] = {}
    previous = 0
    for record in snapshot["rfcs"]:
        if set(record) != {
            "rfc",
            "lifecycle",
            "errata_ids",
            "official_sha256",
        }:
            raise ErrataError("errata RFC fields are invalid")
        number = record["rfc"]
        if not isinstance(number, int) or number <= previous or number in records:
            raise ErrataError("errata RFCs are duplicated or unordered")
        previous = number
        if record["lifecycle"] not in LIFECYCLES:
            raise ErrataError(f"invalid lifecycle for RFC {number}")
        identifiers = record["errata_ids"]
        if (
            not isinstance(identifiers, list)
            or any(not isinstance(item, int) for item in identifiers)
            or identifiers != sorted(set(identifiers))
        ):
            raise ErrataError(f"invalid errata IDs for RFC {number}")
        if not re.fullmatch(r"[0-9a-f]{64}", record["official_sha256"]):
            raise ErrataError(f"invalid errata digest for RFC {number}")
        records[number] = record
    if set(records) != set(expected):
        raise ErrataError("errata snapshot and RFC source baseline differ")
    for number, lifecycle in expected.items():
        if records[number]["lifecycle"] != lifecycle:
            raise ErrataError(f"RFC {number} lifecycle differs from SOURCES")
    return records


def load() -> tuple[dict, dict[int, dict]]:
    try:
        snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ErrataError(f"cannot load errata snapshot: {error}") from error
    return snapshot, validate(snapshot)


def live_check(records: dict[int, dict]) -> None:
    for number, saved in records.items():
        current = current_record(number, saved["lifecycle"])
        if current != saved:
            raise ErrataError(f"official RFC {number} errata changed")


def print_current() -> None:
    lifecycles = source_lifecycles()
    snapshot = {
        "schema": 1,
        "checked_at": date.today().isoformat(),
        "source": ENDPOINT,
        "rfcs": [
            current_record(number, lifecycle)
            for number, lifecycle in sorted(lifecycles.items())
        ],
    }
    print(json.dumps(snapshot, indent=2))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true")
    parser.add_argument("--print-current", action="store_true")
    args = parser.parse_args()
    try:
        if args.print_current:
            print_current()
        else:
            snapshot, records = load()
            if args.live:
                live_check(records)
                print("official RFC errata match the reviewed drift snapshot")
            else:
                count = sum(len(record["errata_ids"]) for record in records.values())
                print(
                    f"RFC errata snapshot valid "
                    f"({len(records)} RFCs, {count} errata)"
                )
                assert snapshot["checked_at"]
    except ErrataError as error:
        print(f"RFC errata error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
