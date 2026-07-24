#!/usr/bin/env python3
"""Regression tests for the Navheim crates.io publication helper."""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "release_crates.py"


def load_helper():
    spec = importlib.util.spec_from_file_location("release_crates", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load release_crates.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


helper = load_helper()


def package(name: str, version: str, dependencies: tuple[str, ...] = ()) -> dict:
    return {
        "name": name,
        "version": version,
        "dependencies": [{"name": item} for item in dependencies],
    }


def current_plan() -> dict:
    return helper.release_plan(ROOT / "release-crates.toml")


def current_packages() -> dict[str, dict]:
    return {
        "navheim-core": package("navheim-core", "0.1.0"),
        "navheim": package("navheim", "0.1.0", ("navheim-core",)),
    }


def expect_failure(expected: str, function, *args) -> None:
    try:
        function(*args)
    except RuntimeError as error:
        if expected not in str(error):
            raise AssertionError(f"expected {expected!r} in {error!r}") from error
        return
    raise AssertionError("expected RuntimeError")


def main() -> int:
    plan = current_plan()
    helper.verify_publish_order(current_packages(), plan)
    assert helper.publish_plan(plan) == ("navheim-core", "navheim")

    wrong_order = {
        "navheim": current_packages()["navheim"],
        "navheim-core": current_packages()["navheim-core"],
    }
    # Dictionary order cannot override the helper's explicit safe order.
    helper.verify_publish_order(wrong_order, plan)

    missing = current_packages()
    del missing["navheim-core"]
    expect_failure(
        "not in sync with workspace packages",
        helper.verify_publish_order,
        missing,
        plan,
    )

    wrong_version = current_packages()
    wrong_version["navheim"] = package("navheim", "0.2.0", ("navheim-core",))
    expect_failure(
        "expected 0.1.0",
        helper.verify_publish_order,
        wrong_version,
        plan,
    )

    unpublished = copy.deepcopy(plan)
    unpublished["crates"]["navheim"]["publish"] = False
    expect_failure(
        "code changes but publish is false",
        helper.validate_plan_entry,
        "navheim",
        unpublished["crates"]["navheim"],
        "0.1.0",
    )

    print("release crate helper tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
