#!/usr/bin/env python3
"""Regression tests for Navheim's locked RFC source baseline."""

from __future__ import annotations

import hashlib
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RFC = ROOT / "standards/rfc"
SOURCE_PATTERN = re.compile(
    r"^(\d+) https://www\.rfc-editor\.org/rfc/rfc(\d+)\.txt "
    r"([a-z0-9-]+)$"
)
CHECKSUM_PATTERN = re.compile(r"^([0-9a-f]{64})  (rfc(\d+)\.txt)$")
REQUIRED = {
    1945,
    2104,
    2119,
    2616,
    2617,
    3339,
    3629,
    3986,
    4648,
    5234,
    5280,
    5480,
    5758,
    6066,
    7468,
    7617,
    8174,
    8259,
    8446,
    9110,
    9111,
    9112,
    9205,
    9325,
    9525,
}
LEGACY = {1945, 2616, 2617}


def parse_sources() -> dict[int, str]:
    sources: dict[int, str] = {}
    for line in (RFC / "SOURCES").read_text(encoding="ascii").splitlines():
        if not line or line.startswith("#"):
            continue
        match = SOURCE_PATTERN.fullmatch(line)
        assert match is not None, f"invalid RFC source line: {line!r}"
        number, repeated, role = match.groups()
        assert number == repeated
        key = int(number)
        assert key not in sources
        assert role != "reference", f"RFC {key} needs a precise role"
        sources[key] = role
    return sources


def parse_checksums() -> dict[int, str]:
    checksums: dict[int, str] = {}
    for line in (RFC / "SHA256SUMS").read_text(encoding="ascii").splitlines():
        match = CHECKSUM_PATTERN.fullmatch(line)
        assert match is not None, f"invalid RFC checksum line: {line!r}"
        digest, filename, number = match.groups()
        path = RFC / filename
        assert path.is_file() and path.stat().st_size > 0
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest
        key = int(number)
        assert key not in checksums
        checksums[key] = digest
    return checksums


def verify_lifecycle(sources: dict[int, str]) -> None:
    for number in LEGACY:
        assert "legacy" in sources[number], (
            f"obsolete RFC {number} must be visibly legacy-only"
        )
    for number, role in sources.items():
        if number not in LEGACY:
            assert "legacy" not in role


def main() -> None:
    sources = parse_sources()
    checksums = parse_checksums()
    assert set(sources) == REQUIRED
    assert set(checksums) == REQUIRED
    verify_lifecycle(sources)
    subprocess.run(["scripts/verify-rfcs.sh"], cwd=ROOT, check=True)
    print(f"RFC source baseline tests passed ({len(REQUIRED)} documents)")


if __name__ == "__main__":
    main()
