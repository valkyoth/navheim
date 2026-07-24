#!/usr/bin/env python3
"""Validate, fetch, lock, and review Navheim's external standards sources."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import subprocess
import sys
import tomllib
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "standards/sources.toml"
PRIVATE = ROOT / "standards/private"
LOCK = PRIVATE / "SHA256SUMS.local"
MAX_DOCUMENT_BYTES = 64 * 1024 * 1024
STATUS = {
    "verified-current",
    "verify-before-implementation",
    "licensed-baseline-required",
    "profile-freeze-required",
    "hardware-profile-freeze-required",
}
ACQUISITION = {"automatic", "manual", "portal"}
SOURCE_FIELDS = {
    "id",
    "publisher",
    "scope",
    "status",
    "acquisition",
    "redistribution",
    "landing_url",
    "documents",
    "first_release",
}
SOURCE_OPTIONAL = {"review_markers"}
DOWNLOAD_FIELDS = {"source_id", "filename", "url"}
ID_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
HASH_PATTERN = re.compile(r"([0-9a-f]{64})  ([A-Za-z0-9][A-Za-z0-9._+-]*)")


class SourceError(RuntimeError):
    """Invalid, unsafe, missing, or drifting source data."""


def load_catalog() -> dict:
    try:
        data = tomllib.loads(CATALOG.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise SourceError(f"cannot load source catalog: {error}") from error
    validate_catalog(data)
    return data


def require_https(url: object, label: str) -> urllib.parse.ParseResult:
    if not isinstance(url, str):
        raise SourceError(f"{label} URL is missing")
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username:
        raise SourceError(f"{label} must use an ordinary HTTPS URL")
    if parsed.fragment:
        raise SourceError(f"{label} URL must not contain a fragment")
    return parsed


def validate_catalog(data: dict) -> None:
    top = {
        "schema_version",
        "project",
        "reviewed",
        "private_directory",
        "default_redistribution",
        "source",
        "download",
    }
    if set(data) != top:
        raise SourceError("source catalog top-level fields differ from schema")
    if data["schema_version"] != 1 or data["project"] != "navheim":
        raise SourceError("source catalog identity or schema is invalid")
    if data["private_directory"] != "standards/private":
        raise SourceError("private standards path must remain standards/private")
    if data["default_redistribution"] != "local-only":
        raise SourceError("external documents must default to local-only")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(data["reviewed"])):
        raise SourceError("catalog review date is invalid")

    releases = (ROOT / "docs/RELEASE_PLAN.md").read_text(encoding="utf-8")
    sources: dict[str, dict] = {}
    for source in data["source"]:
        fields = set(source)
        if not SOURCE_FIELDS <= fields or not fields <= SOURCE_FIELDS | SOURCE_OPTIONAL:
            raise SourceError(f"invalid source fields for {source.get('id')}")
        source_id = source["id"]
        if not isinstance(source_id, str) or not ID_PATTERN.fullmatch(source_id):
            raise SourceError(f"invalid source ID: {source_id!r}")
        if source_id in sources:
            raise SourceError(f"duplicate source ID: {source_id}")
        sources[source_id] = source
        if source["status"] not in STATUS:
            raise SourceError(f"invalid status for {source_id}")
        if source["acquisition"] not in ACQUISITION:
            raise SourceError(f"invalid acquisition for {source_id}")
        if source["redistribution"] != "local-only":
            raise SourceError(f"{source_id} is not local-only")
        require_https(source["landing_url"], source_id)
        documents = source["documents"]
        if not isinstance(documents, list) or not documents:
            raise SourceError(f"{source_id} has no document inventory")
        if any(not isinstance(item, str) or not item.strip() for item in documents):
            raise SourceError(f"{source_id} has an invalid document")
        markers = source.get("review_markers", [])
        if not isinstance(markers, list) or any(
            not isinstance(item, str) or not item.strip() for item in markers
        ):
            raise SourceError(f"{source_id} has invalid review markers")
        release = source["first_release"]
        if not isinstance(release, str) or f"### {release} -" not in releases:
            raise SourceError(f"{source_id} names unknown release {release!r}")

    filenames: set[str] = set()
    urls: set[str] = set()
    for download in data["download"]:
        if set(download) != DOWNLOAD_FIELDS:
            raise SourceError("download entry fields differ from schema")
        source_id = download["source_id"]
        if source_id not in sources:
            raise SourceError(f"download names unknown source {source_id}")
        filename = download["filename"]
        if (
            not isinstance(filename, str)
            or filename in filenames
            or Path(filename).name != filename
            or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._+-]*", filename)
        ):
            raise SourceError(f"unsafe or duplicate filename: {filename!r}")
        filenames.add(filename)
        parsed = require_https(download["url"], filename)
        canonical_url = parsed.geturl()
        if canonical_url in urls:
            raise SourceError(f"duplicate download URL: {canonical_url}")
        urls.add(canonical_url)

    ignored = subprocess.run(
        ["git", "check-ignore", "-q", "standards/private/probe"],
        cwd=ROOT,
        check=False,
    )
    if ignored.returncode != 0:
        raise SourceError("standards/private is not ignored by Git")
    tracked = subprocess.run(
        ["git", "ls-files", "--", "standards/private"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    if tracked.stdout.strip():
        raise SourceError("private standards files are tracked by Git")


def safe_request(url: str, limit: int) -> bytes:
    requested = require_https(url, "download")
    request = urllib.request.Request(
        url, headers={"User-Agent": "navheim-standards/0.1"}
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            final = require_https(response.geturl(), "redirect")
            if final.hostname != requested.hostname:
                raise SourceError(
                    f"cross-host redirect rejected: {requested.hostname} -> "
                    f"{final.hostname}"
                )
            length = response.headers.get("Content-Length")
            if length is not None and int(length) > limit:
                raise SourceError(f"document exceeds {limit} bytes")
            body = response.read(limit + 1)
    except (OSError, ValueError) as error:
        raise SourceError(f"cannot download {url}: {error}") from error
    if not body or len(body) > limit:
        raise SourceError(f"empty or oversized response from {url}")
    return body


def validate_document(filename: str, body: bytes) -> None:
    suffix = Path(filename).suffix.lower()
    if suffix == ".pdf" and not body.startswith(b"%PDF-"):
        raise SourceError(f"{filename} is not a PDF")
    if suffix == ".zip" and not body.startswith(b"PK"):
        raise SourceError(f"{filename} is not a ZIP archive")
    if body.lstrip().lower().startswith((b"<!doctype html", b"<html")):
        raise SourceError(f"{filename} is an HTML response")


def lock_downloads(data: dict) -> None:
    lines = []
    for download in sorted(data["download"], key=lambda item: item["filename"]):
        path = PRIVATE / download["filename"]
        if not path.exists():
            continue
        if path.is_symlink() or not path.is_file():
            raise SourceError(f"unsafe local document path: {path.name}")
        body = path.read_bytes()
        validate_document(path.name, body)
        lines.append(f"{hashlib.sha256(body).hexdigest()}  {path.name}\n")
        path.chmod(0o444)
    temporary = PRIVATE / ".SHA256SUMS.local.tmp"
    temporary.write_text("".join(lines), encoding="ascii")
    os.replace(temporary, LOCK)
    LOCK.chmod(0o444)


def fetch(data: dict) -> None:
    PRIVATE.mkdir(mode=0o700, parents=True, exist_ok=True)
    if PRIVATE.is_symlink():
        raise SourceError("private standards directory must not be a symlink")
    fetched = 0
    for download in data["download"]:
        destination = PRIVATE / download["filename"]
        if destination.exists():
            continue
        body = safe_request(download["url"], MAX_DOCUMENT_BYTES)
        validate_document(destination.name, body)
        temporary = PRIVATE / f".{destination.name}.partial"
        temporary.write_bytes(body)
        os.replace(temporary, destination)
        destination.chmod(0o444)
        fetched += 1
        print(f"fetched {destination.name}")
    if LOCK.exists():
        LOCK.chmod(0o644)
    lock_downloads(data)
    print(f"local standards vault locked ({fetched} new documents)")


def parse_lock() -> dict[str, str]:
    if not LOCK.is_file() or LOCK.is_symlink():
        raise SourceError("local checksum lock is missing or unsafe")
    locked: dict[str, str] = {}
    for line in LOCK.read_text(encoding="ascii").splitlines():
        match = HASH_PATTERN.fullmatch(line)
        if match is None:
            raise SourceError(f"invalid local checksum line: {line!r}")
        digest, filename = match.groups()
        if filename in locked:
            raise SourceError(f"duplicate local checksum: {filename}")
        locked[filename] = digest
    return locked


def verify_local(data: dict, require_downloads: bool) -> None:
    locked = parse_lock()
    known = {item["filename"] for item in data["download"]}
    if not set(locked) <= known:
        raise SourceError("local lock contains a file outside the download allowlist")
    if require_downloads and set(locked) != known:
        missing = ", ".join(sorted(known - set(locked)))
        raise SourceError(f"allowlisted downloads are missing: {missing}")
    for filename, expected in locked.items():
        path = PRIVATE / filename
        if not path.is_file() or path.is_symlink():
            raise SourceError(f"locked document is missing or unsafe: {filename}")
        body = path.read_bytes()
        validate_document(filename, body)
        if hashlib.sha256(body).hexdigest() != expected:
            raise SourceError(f"local document changed: {filename}")
        if path.stat().st_mode & 0o222:
            raise SourceError(f"local document is writable: {filename}")
    print(f"local standards vault verified ({len(locked)} documents)")


def review_current(data: dict) -> None:
    reviewed = 0
    for source in data["source"]:
        markers = source.get("review_markers", [])
        if not markers:
            continue
        body = safe_request(source["landing_url"], 8 * 1024 * 1024)
        text = body.decode("utf-8", errors="replace")
        missing = [marker for marker in markers if marker not in text]
        if missing:
            raise SourceError(
                f"{source['id']} no longer exposes markers: {', '.join(missing)}"
            )
        reviewed += 1
        print(f"reviewed {source['id']}")
    print(f"official source freshness markers matched ({reviewed} families)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subcommands = parser.add_subparsers(dest="command", required=True)
    subcommands.add_parser("check", help="validate tracked metadata offline")
    subcommands.add_parser("fetch", help="fetch public allowlisted local copies")
    verify = subcommands.add_parser(
        "verify-local", help="verify installed local documents"
    )
    verify.add_argument("--require-downloads", action="store_true")
    subcommands.add_parser(
        "review-current", help="check revision markers on official pages"
    )
    args = parser.parse_args()
    try:
        data = load_catalog()
        if args.command == "check":
            print(
                f"standards catalog valid "
                f"({len(data['source'])} families, {len(data['download'])} downloads)"
            )
        elif args.command == "fetch":
            fetch(data)
        elif args.command == "verify-local":
            verify_local(data, args.require_downloads)
        elif args.command == "review-current":
            review_current(data)
    except SourceError as error:
        print(f"standards source error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
