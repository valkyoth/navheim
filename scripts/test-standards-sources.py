#!/usr/bin/env python3
"""Regression tests for the external standards acquisition inventory."""

from __future__ import annotations

import copy
import importlib.util
import subprocess
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "standards/sources.toml"
REQUIRED = {
    "gps-sis",
    "gps-service",
    "galileo-open-service",
    "galileo-osnma",
    "galileo-has",
    "galileo-timing-sar",
    "glonass-open-service",
    "beidou-open-service",
    "qzss-open-services",
    "navic-open-service",
    "sbas-aviation",
    "rtcm-corrections",
    "rtcm-ntrip",
    "nmea-0183",
    "nmea-2000-j1939",
    "igs-rinex",
    "igs-products",
    "spartn-corrections",
    "iers-iau-geodesy",
    "oma-supl",
    "3gpp-lpp",
    "itu-asn1",
    "nist-gnss-crypto",
    "gpsd-json",
    "ublox-ubx",
    "septentrio-sbf",
    "android-gnss",
    "gnss-time-transfer",
    "rust-platform-contracts",
    "sdr-device-stacks",
    "linux-bsd-io",
    "microsoft-platform-io",
    "apple-platform-io",
    "novatel-oem",
    "conditional-receiver-protocols",
    "gnss-science-methods",
    "numerical-methods",
}


def load_tool():
    path = ROOT / "scripts/standards-sources.py"
    spec = importlib.util.spec_from_file_location("standards_sources", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def expect_invalid(tool, data: dict) -> None:
    try:
        tool.validate_catalog(data)
    except tool.SourceError:
        return
    raise AssertionError("malformed standards catalog was accepted")


def main() -> None:
    data = tomllib.loads(CATALOG.read_text(encoding="utf-8"))
    sources = {source["id"]: source for source in data["source"]}
    assert set(sources) == REQUIRED
    assert all(source["redistribution"] == "local-only" for source in sources.values())
    assert all(source["documents"] for source in sources.values())
    assert all(download["source_id"] in sources for download in data["download"])
    tool = load_tool()

    broken = copy.deepcopy(data)
    broken["source"][0]["redistribution"] = "tracked"
    expect_invalid(tool, broken)

    broken = copy.deepcopy(data)
    broken["source"][0]["landing_url"] = "http://example.invalid/"
    expect_invalid(tool, broken)

    broken = copy.deepcopy(data)
    broken["download"][1]["filename"] = broken["download"][0]["filename"]
    expect_invalid(tool, broken)

    broken = copy.deepcopy(data)
    broken["source"][0]["first_release"] = "v999.0.0"
    expect_invalid(tool, broken)

    try:
        tool.validate_document("document.pdf", b"<html>not a PDF</html>")
    except tool.SourceError:
        pass
    else:
        raise AssertionError("HTML masquerading as a PDF was accepted")

    subprocess.run(
        ["python3", "scripts/standards-sources.py", "check"],
        cwd=ROOT,
        check=True,
    )
    print(f"standards source inventory tests passed ({len(REQUIRED)} families)")


if __name__ == "__main__":
    main()
