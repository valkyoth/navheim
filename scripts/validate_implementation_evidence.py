#!/usr/bin/env python3
"""Validate fail-closed implementation evidence in the standards manifest."""

from __future__ import annotations

import sys
import tomllib
from pathlib import Path


REQUIRED_POLICY = {
    "implementation_requires_verified_revision",
    "implementation_requires_source_review_before_code",
    "implementation_requires_section_mapping",
    "implementation_requires_tests_in_same_milestone",
    "implementation_requires_negative_and_adversarial_tests",
    "implementation_requires_independent_evidence",
}
IMPLEMENTED_FIELDS = {
    "implemented_by",
    "tests",
    "sections",
    "vectors",
    "limitations",
}
ALLOWED_STATUSES = {"candidate", "verified", "implemented", "retired"}


def validate(path: Path) -> None:
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    policy = data.get("policy")
    if not isinstance(policy, dict):
        raise ValueError("standards manifest has no policy table")
    for name in sorted(REQUIRED_POLICY):
        if policy.get(name) is not True:
            raise ValueError(f"standards manifest must set {name} = true")

    documents = data.get("document")
    if not isinstance(documents, list) or not documents:
        raise ValueError("standards manifest has no document records")

    seen: set[str] = set()
    for index, document in enumerate(documents):
        if not isinstance(document, dict):
            raise ValueError(f"document {index} is not a table")
        identifier = document.get("id")
        if not isinstance(identifier, str) or not identifier:
            raise ValueError(f"document {index} has no id")
        if identifier in seen:
            raise ValueError(f"duplicate document id: {identifier}")
        seen.add(identifier)

        status = document.get("status")
        if status not in ALLOWED_STATUSES:
            raise ValueError(f"{identifier}: unsupported status {status!r}")
        if status != "implemented":
            continue

        revision = document.get("revision")
        if not isinstance(revision, str) or not revision:
            raise ValueError(f"{identifier}: implemented record has no revision")
        if "candidate" in revision.lower() or "verify" in revision.lower():
            raise ValueError(f"{identifier}: implemented revision is not frozen")
        for field in sorted(IMPLEMENTED_FIELDS):
            value = document.get(field)
            if not isinstance(value, list) or not value:
                raise ValueError(
                    f"{identifier}: implemented record requires non-empty {field}"
                )


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) == 2 else Path("standards/manifest.toml")
    try:
        validate(path)
    except (OSError, tomllib.TOMLDecodeError, ValueError) as error:
        print(f"implementation evidence invalid: {error}", file=sys.stderr)
        return 1
    print("machine-readable implementation evidence passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
