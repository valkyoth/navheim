#!/usr/bin/env python3
"""Regression tests for roadmap uniqueness and coarse scope alarms."""

from __future__ import annotations

import tempfile
from pathlib import Path

import generate_release_plan as plan


PREFIX = """## 26. Version and implementation roadmap

### Phase A — Test

"""
SUFFIX = """

## 27. Definition of done for 1.0.0
"""


def expect_failure(body: str, expected_count: int, message: str) -> None:
    with tempfile.TemporaryDirectory() as directory:
        source = Path(directory) / "idea.md"
        source.write_text(PREFIX + body + SUFFIX, encoding="utf-8")
        old_source = plan.SOURCE
        old_count = plan.EXPECTED_MILESTONES
        try:
            plan.SOURCE = source
            plan.EXPECTED_MILESTONES = expected_count
            try:
                plan.parse_milestones()
            except RuntimeError as error:
                assert message in str(error), error
            else:
                raise AssertionError(f"roadmap unexpectedly passed: {message}")
        finally:
            plan.SOURCE = old_source
            plan.EXPECTED_MILESTONES = old_count


def main() -> None:
    long_description = "x" * (plan.MAX_ROADMAP_DESCRIPTION_CHARS + 1)
    expect_failure(
        f"- **9.9.9** — {long_description}\n",
        1,
        "split the release or shorten it",
    )

    duplicate = "- **9.9.9** — first\n- **9.9.9** — second\n"
    expect_failure(duplicate, 2, "versions must be unique")

    plan.CONFORMANCE_MILESTONE_DETAILS["9.9.9"] = (
        "x" * (plan.MAX_SPECIFIC_ACCEPTANCE_CHARS + 1),
    )
    try:
        expect_failure(
            "- **9.9.9** — bounded description\n",
            1,
            "perform a semantic scope review",
        )
    finally:
        del plan.CONFORMANCE_MILESTONE_DETAILS["9.9.9"]

    print("release plan scope tests passed")


if __name__ == "__main__":
    main()
