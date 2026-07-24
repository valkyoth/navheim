#!/usr/bin/env python3
"""Generate the initial detailed release plan from the archived idea roadmap."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "initial-idea.md"
TARGET = ROOT / "docs" / "RELEASE_PLAN.md"

PHASE_CHECKS = {
    "A": "MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests",
    "B": "official format examples, malformed/truncated/adversarial streams, exact-consumption and round-trip properties, recovery tests, and parser fuzz smoke",
    "C": "independent numerical references, fixed-point and floating comparisons, deterministic replay, resource bounds, and scalar/optimized equivalence",
    "D": "official GPS vectors, generated baseband, recorded independent captures, receiver comparison, malformed navigation data, and end-to-end replay",
    "E": "official Galileo vectors, generated and recorded signals, receiver comparison, FEC/page faults, time checks, and end-to-end replay",
    "F": "official GLONASS vectors, FDMA/CDMA channel cases, generated and recorded signals, bias/time faults, and independent receiver comparison",
    "G": "official BeiDou vectors, GEO/IGSO/MEO cases, generated and recorded signals, time/correction faults, and independent receiver comparison",
    "H": "official QZSS/NavIC/SBAS vectors, provider/profile cases, generated and recorded signals, integrity timeouts, and independent receiver comparison",
    "I": "independent high-precision references, randomized geometry, degenerate/rank-deficient inputs, cross-architecture tolerances, and fault exclusion cases",
    "J": "independent RTK/PPP references, baseline and product replays, ambiguity/slip/freshness faults, frame validation, and receiver/software comparisons",
    "K": "official authentication vectors, delayed/reordered/missing/expired data, trust-root transitions, spoof/jam evidence scenarios, and policy-state tests",
    "L": "independent timing/fusion references, rollover and clock faults, delayed/out-of-sequence data, holdover growth, outage replay, and sensor comparisons",
    "M": "target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence",
    "N": "cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence",
}

DESCRIPTION_OVERRIDES = {
    "0.217.0": "first complete production-candidate evidence rehearsal",
    "0.218.0": "second production-candidate rehearsal with blocker-only fixes",
}


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
    if len(milestones) != 220:
        raise RuntimeError(f"expected 220 roadmap milestones, found {len(milestones)}")
    return milestones


def heading_title(description: str) -> str:
    title = description.rstrip(".")
    if len(title) > 88:
        title = title[:85].rstrip() + "..."
    return title[0].upper() + title[1:]


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

Tags use:

```text
v0.N.0        milestone release
v0.N.P        bounded fix/remediation release
v1.0.0-rc.N   exact production candidate
v1.0.0        unchanged promotion of the approved candidate
```

## Release Principles

Every release requires:

- one bounded outcome and explicit non-claims;
- authoritative standards/source evidence for affected behavior;
- unit, negative, adversarial, conformance, and fuzz evidence appropriate to
  the surface;
- MSRV, `no_std`, platform, numerical, and resource evidence as applicable;
- updated docs, current status, coverage, changelog, and release notes;
- current dependency/tool/action review, Cargo policy, RustSec, and SBOM;
- no hand-maintained code file above 500 lines;
- changed-code security review and exact-commit pentest;
- a clean implementation stop before any tag or publication.

Core GNSS correctness stays first-party. TLS, modern cryptographic primitives,
platform APIs, and vendor stacks enter only through explicit reviewed adapters.

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
11. Run `scripts/validate-release-readiness.sh vX.Y.Z`.
12. Tag or publish only on explicit maintainer request.

The final `v1.0.0` tag and crate archives must be byte-for-byte the approved
`v1.0.0-rc.N` candidate. Any change requires another RC.

## Crate Publication Policy

Published libraries use independent versions. `release-crates.toml` marks each
crate as code, bugfix, dependency, metadata, or unchanged. The release helper
validates Cargo metadata and publishes only selected crates in dependency
order, waiting for crates.io indexing before dependents.

Repository-only tools under `tools/`, fuzzing, labs, simulator/deployment
artifacts, and large capture data are never included in the crates.io publish
order unless a later milestone explicitly admits a stable library package.

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
    goal_text = description.rstrip(".")
    phase_checks = PHASE_CHECKS[phase]
    return f"""### v{version} - {heading_title(description)}

Status: {status}

Goal: deliver {goal_text[0].lower() + goal_text[1:]} as one bounded,
reviewable release in Phase {phase} ({phase_title}).

Deliverables:

- {sentence}
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_{version}.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform {phase_checks};
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
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
- run `scripts/validate-release-readiness.sh v1.0.0-rc.1`.

Exit criteria:

- every frozen civil/open 1.0 claim is implemented, independently evidenced,
  documented, and free of unresolved critical/high findings;
- all candidate archives and checksums are retained without regeneration;
- `v1.0.0-rc.1 implementation stop reached. Run pentest for this exact commit.`

"""


def final_block() -> str:
    return """### v1.0.0 - Serious production release

Status: planned.

Goal: promote the exact approved production candidate to Navheim 1.0.0
without changing source, dependencies, metadata, archives, SBOM, or provenance.

Deliverables:

- Point `v1.0.0` at the unchanged approved `v1.0.0-rc.N` commit.
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
