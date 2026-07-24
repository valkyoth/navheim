#!/usr/bin/env python3
"""Generate the initial detailed release plan from the archived idea roadmap."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from release_plan_data import (
    DESCRIPTION_OVERRIDES,
    MILESTONE_DETAILS,
    PHASE_CHECKS,
    PHASE_DELIVERABLES,
    PHASE_EXIT_CHECKS,
)
from release_plan_conformance_data import CONFORMANCE_MILESTONE_DETAILS
from release_plan_review_data import REVIEW_MILESTONE_DETAILS

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "initial-idea.md"
TARGET = ROOT / "docs" / "RELEASE_PLAN.md"
EXPECTED_MILESTONES = 484
MAX_ROADMAP_DESCRIPTION_CHARS = 200
MAX_SPECIFIC_ACCEPTANCE_CHARS = 650


def clean_sentence(text: str) -> str:
    text = text.strip()
    return text if text.endswith(".") else f"{text}."


def parse_milestones() -> list[tuple[str, str, str, str]]:
    text = SOURCE.read_text(encoding="utf-8")
    roadmap = text.split("## 26. Version and implementation roadmap", 1)[1]
    roadmap = roadmap.split("## 27. Definition of done for 1.0.0", 1)[0]
    phase = ""
    phase_title = ""
    milestones: list[tuple[str, str, str, str]] = []
    for line in roadmap.splitlines():
        phase_match = re.match(r"### Phase ([A-N]) — (.+)", line)
        if phase_match:
            phase, phase_title = phase_match.groups()
            continue
        release_match = re.match(r"- \*\*([0-9]+\.[0-9]+\.[0-9]+)\*\* — (.+)", line)
        if release_match:
            version, description = release_match.groups()
            description = DESCRIPTION_OVERRIDES.get(version, description)
            milestones.append((phase, phase_title, version, description))
    if len(milestones) != EXPECTED_MILESTONES:
        raise RuntimeError(
            f"expected {EXPECTED_MILESTONES} roadmap milestones, "
            f"found {len(milestones)}"
        )
    versions = [version for _, _, version, _ in milestones]
    if len(versions) != len(set(versions)):
        raise RuntimeError("roadmap milestone versions must be unique")
    for _, _, version, description in milestones:
        if len(description) > MAX_ROADMAP_DESCRIPTION_CHARS:
            raise RuntimeError(
                f"{version} roadmap description has {len(description)} characters; "
                "split the release or shorten it"
            )
        specific = (
            MILESTONE_DETAILS.get(version, ())
            + CONFORMANCE_MILESTONE_DETAILS.get(version, ())
            + REVIEW_MILESTONE_DETAILS.get(version, ())
        )
        specific_chars = sum(len(item) for item in specific)
        if specific_chars > MAX_SPECIFIC_ACCEPTANCE_CHARS:
            raise RuntimeError(
                f"{version} has {specific_chars} characters of specific acceptance; "
                "perform a semantic scope review and split independent concerns"
            )
    return milestones


def heading_title(description: str) -> str:
    title = description.rstrip(".")
    if len(title) > 88:
        title = title[:85].rstrip() + "..."
    if title.startswith(("gpsd", "iOS", "macOS", "no_std", "u-blox")):
        return title
    return title[0].upper() + title[1:]


def goal_text(description: str) -> str:
    text = description.rstrip(".")
    preserved = (
        "3GPP",
        "ARAIM",
        "ASN.1",
        "BeiDou",
        "CAN",
        "CRINEX",
        "DGPS",
        "FreeBSD",
        "Galileo",
        "GLONASS",
        "GNSS",
        "GPS",
        "GitHub",
        "IMU",
        "iOS",
        "J1939",
        "LPP",
        "macOS",
        "NavIC",
        "NetBSD",
        "NMEA",
        "NTRIP",
        "OpenBSD",
        "OSNMA",
        "PPP",
        "PVT",
        "QZSS",
        "RAIM",
        "RINEX",
        "RTCM",
        "RTK",
        "RustCrypto",
        "SBAS",
        "SIMD",
        "SUPL",
        "TAI",
        "UTC",
        "WASM",
    )
    if text.startswith(preserved):
        return text
    return text[0].lower() + text[1:]


def introduction() -> str:
    return """# Navheim Release Plan To 1.0

Status: planning document

This plan is intentionally granular. Navheim processes adversarial RF, device,
file, network, correction, time, and sensor inputs, so every milestone must be
small enough to implement, review, test, fuzz where relevant, pentest, and stop
cleanly before tagging.

The list is not a maximum. Split a milestone or add patch releases whenever
one safe review pass is no longer enough. Production-scope work is completed
before 1.0.0; post-1.0 releases may add newly published standards and optional
ecosystem extensions, not defer the stated 1.0 baseline.

A release should own one primary state machine, provider profile, platform
adapter, artifact layer, or independently reviewable algorithm family. Split
work when parts can fail, roll back, freeze standards, or complete their test
matrices independently. A split never weakens earlier requirements: guarantees
accumulate through the sequence. The generator enforces coarse description and
specific-acceptance size ceilings as a regression alarm; passing those limits
does not replace semantic scope review.

Tags use:

```text
v0.N.0        milestone release
v0.N.P        bounded compatible implementation/remediation release
v1.0.0-rc.N   exact production candidate
v1.0.0        unchanged promotion of the approved candidate
```

## Release Principles

Every release requires:

- one bounded outcome and explicit non-claims;
- source-first implementation: review and freeze exact authoritative
  revisions, amendments, errata, sections/tables, legal access, and independent
  references before code; stop rather than guess when evidence is missing;
- bidirectional source/requirement-to-implementation-and-test mappings;
- unit, negative, adversarial, conformance, and fuzz evidence appropriate to
  the surface;
- MSRV behavioral tests once behavior exists, plus `no_std`, platform,
  numerical, and resource evidence as applicable;
- updated docs, current status, coverage, changelog, and release notes;
- current dependency/tool/action review, Cargo policy, RustSec, and SBOM;
- no hand-maintained code file above 500 lines;
- changed-code security review and exact-commit pentest;
- a clean implementation stop before any tag or publication.

Core GNSS correctness stays first-party. TLS, modern cryptographic primitives,
platform APIs, and vendor stacks enter only through explicit reviewed adapters.
Deterministic elementary math is first-party and `no_std`; published crates use
stable Rust only and never disguise a nightly portable-SIMD requirement as a
portable implementation.

## Required Milestone Format

Every milestone below has exactly:

- `Status`;
- `Goal`;
- `Deliverables`;
- `Verification`;
- `Exit criteria`.

Release-specific verification is additive to `scripts/checks.sh`,
`cargo deny check`, `cargo audit`, semantic SBOM validation, package checks,
CI, CodeQL default setup review, and exact-commit pentesting.

## Pentest Before Tags

Every version, including patch and prerelease tags, follows this handoff:

1. Complete only the milestone scope.
2. Update standards evidence, documentation, tests, and release notes.
3. Run local, dependency, advisory, package, SBOM, and compatibility gates.
4. Stop at the milestone's exact-commit pentest sentence.
5. Record temporary findings only in ignored root `PENTEST.md`.
6. Remediate findings, remove `PENTEST.md`, rerun all gates, and commit.
7. Check GitHub CI and CodeQL default setup.
8. Pentest/retest that exact full implementation commit.
9. Commit only `security/pentest/vX.Y.Z.md`, with `Status: PASS`,
   `Reviewed-Commit: <40 hex>`, `Tester`, `Scope`, and `Date`.
10. Require the report commit to be the direct child of the reviewed commit
    and to change no other path.
11. Prove package file lists and checksums are identical at the reviewed
    implementation commit and its report-only child.
12. Run `scripts/validate-release-readiness.sh vX.Y.Z`.
13. Tag or publish only on explicit maintainer request.

For the production candidate, all Cargo manifests already declare package
version `1.0.0`. `v1.0.0-rc.N` is a repository candidate tag over those
unpublished final-version sources, not a differently versioned crates.io
package. The final `v1.0.0` tag points to the same approved commit and publishes
the retained archives byte-for-byte. Any source, metadata, documentation, or
archive change requires another RC.

## Crate Publication Policy

Published libraries use independent versions. `release-crates.toml` marks each
crate as code, bugfix, dependency, metadata, or unchanged. The release helper
validates Cargo metadata and publishes only selected crates in dependency
order, waiting for crates.io indexing before dependents.

Repository-only tools under `tools/`, fuzzing, labs, simulator/deployment
artifacts, and large capture data are never included in the crates.io publish
order unless a later milestone explicitly admits a stable library package.

## GNSS Timing Consumer Boundary

Navheim owns GNSS time decoding, resolution, satellite/receiver clock models,
time-only solutions, PPS/time-mark meaning, uncertainty, health,
authentication, integrity, and provenance. It exposes those results through
its own dependency-free `no_std` API.

Generic PPS capture, NTP/NTS/PTP, clock-family consensus, oscillator
discipline, system/PHC adjustment, and holdover belong to consumers. A
consumer-owned adapter may depend on Navheim; Navheim never depends on that
adapter or consumer. Every affected milestone follows
[GNSS_TIMING_API.md](GNSS_TIMING_API.md).

"""


def milestone_block(
    phase: str,
    phase_title: str,
    version: str,
    description: str,
) -> str:
    status = (
        "in implementation; exact-commit pentest pending."
        if version == "0.1.0"
        else "planned."
    )
    sentence = clean_sentence(description)
    goal = goal_text(description)
    phase_checks = PHASE_CHECKS[phase]
    phase_deliverable = clean_sentence(PHASE_DELIVERABLES[phase])
    phase_exit = PHASE_EXIT_CHECKS[phase]
    detail = MILESTONE_DETAILS.get(version)
    if detail is None:
        detail = REVIEW_MILESTONE_DETAILS.get(version)
    if detail is None:
        detail = CONFORMANCE_MILESTONE_DETAILS.get(version)
    detail_deliverable = f"- {detail[0]}\n" if detail else ""
    detail_verification = f"- {detail[1]}\n" if detail else ""
    return f"""### v{version} - {heading_title(description)}

Status: {status}

Goal: deliver {goal} as one bounded,
reviewable release in Phase {phase} ({phase_title}).

Deliverables:

- {sentence}
{detail_deliverable}- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Before implementation, review and freeze every applicable authoritative
  document, revision, amendment, erratum, section/table, legal condition, and
  independent reference; stop rather than guess when evidence is missing or
  ambiguous.
- Phase {phase} contract: {phase_deliverable}
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_{version}.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
{detail_verification}- perform {phase_checks};
- run and map all applicable positive, negative, boundary, malformed,
  adversarial, conformance, differential, resource, fuzz, platform, and
  regression tests; document every not-applicable class;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- Phase {phase} acceptance is demonstrated: {phase_exit};
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v{version} implementation stop reached. Run pentest for this exact commit.`

"""


def rc_block() -> str:
    return """## Production Candidate

### v1.0.0-rc.1 - Exact production candidate

Status: planned.

Goal: create the exact versioned production candidate after every v0.x
implementation, coverage, standards, platform, documentation, security,
GNSS-domain, and remediation milestone has passed.

Deliverables:

- Set every publishable Cargo package version to `1.0.0` before creating the
  first candidate tag; do not publish a crates.io prerelease.
- Freeze all 1.0 public APIs, crate versions, features, standards profiles,
  supported platforms, non-claims, migration policy, and package archives.
- Produce signed checksums, semantic SBOM, provenance, conformance inventory,
  independent receiver/simulator/live-sky evidence, audit references, and the
  complete crates.io publish plan.
- Build the candidate archives once and retain them for unchanged final
  promotion.

Verification:

- run every repository, MSRV, no_std, platform, fuzz, Miri, sanitizer, formal,
  numerical, performance, long-duration, live-sky, shielded-simulator,
  interoperability, and standards gate assigned before this point;
- complete independent external security and GNSS-domain audits, remediation,
  and clean retest;
- verify package contents, checksums, SBOM, provenance, publish order, docs,
  examples, and current capability tables against the frozen baseline;
- prove the reviewed implementation commit and its report-only child produce
  identical package file lists, bytes, and checksums;
- run `scripts/validate-release-readiness.sh v1.0.0-rc.1`.

Exit criteria:

- every frozen civil/open 1.0 claim is implemented, independently evidenced,
  documented, and free of unresolved critical/high findings;
- all publishable manifests already declare `1.0.0`;
- all candidate archives and checksums are retained without regeneration;
- `v1.0.0-rc.1 implementation stop reached. Run pentest for this exact commit.`

"""


def final_block() -> str:
    return """### v1.0.0 - Serious production release

Status: planned.

Goal: promote the exact approved production candidate to Navheim 1.0.0
without changing source, dependencies, metadata, archives, SBOM, or provenance.

Deliverables:

- Point `v1.0.0` at the exact commit already tagged as the approved
  `v1.0.0-rc.N`.
- Publish the exact retained and audited candidate crate archives.
- Publish final release notes, checksums, SBOM, provenance, audit references,
  frozen standards matrix, platform matrix, and support policy without
  rebuilding artifacts.

Verification:

- verify the final tag target equals the approved RC commit;
- verify archive and crates.io checksums equal the approved candidate manifest;
- verify no source, dependency, feature, metadata, standards, documentation,
  SBOM, provenance, or package-content drift;
- run final release-readiness validation in unchanged-candidate promotion mode.

Exit criteria:

- final tag and published archives are identical to the approved RC;
- all 1.0 support, security, migration, and standards policies are public;
- `v1.0.0 implementation stop reached. Run pentest for this exact commit.`
"""


def render() -> str:
    parts = [introduction()]
    previous_phase = ""
    milestones = parse_milestones()
    for phase, phase_title, version, description in milestones:
        if version == "1.0.0":
            continue
        if phase != previous_phase:
            parts.append(f"## Phase {phase}: {phase_title}\n\n")
            previous_phase = phase
        parts.append(milestone_block(phase, phase_title, version, description))
    parts.append(rc_block())
    parts.append(final_block())
    return "".join(parts)


def main() -> int:
    generated = render()
    if sys.argv[1:] == ["--check"]:
        if TARGET.read_text(encoding="utf-8") != generated:
            print(
                "release plan is stale; run scripts/generate_release_plan.py",
                file=sys.stderr,
            )
            return 1
        print("release plan matches the archived roadmap")
        return 0
    if sys.argv[1:]:
        print(
            "usage: scripts/generate_release_plan.py [--check]",
            file=sys.stderr,
        )
        return 2
    TARGET.write_text(generated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
