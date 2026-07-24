# Navheim Release Plan To 1.0

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

## Phase A: Foundation and contracts

### v0.1.0 - Workspace, licenses, security policy, MSRV, CI and `standards/manifest.toml`

Status: in implementation; exact-commit pentest pending.

Goal: deliver workspace, licenses, security policy, MSRV, CI and `standards/manifest.toml` as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- workspace, licenses, security policy, MSRV, CI and `standards/manifest.toml`.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.1.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.1.0 implementation stop reached. Run pentest for this exact commit.`

### v0.2.0 - Bounded collections, fixed-capacity strings and core error model

Status: planned.

Goal: deliver bounded collections, fixed-capacity strings and core error model as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- bounded collections, fixed-capacity strings and core error model.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.2.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.2.0 implementation stop reached. Run pentest for this exact commit.`

### v0.3.0 - Physical unit types and checked conversions

Status: planned.

Goal: deliver physical unit types and checked conversions as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- physical unit types and checked conversions.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.3.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.3.0 implementation stop reached. Run pentest for this exact commit.`

### v0.4.0 - GNSS/system time representation with no leap-second conversion yet

Status: planned.

Goal: deliver gNSS/system time representation with no leap-second conversion yet as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- GNSS/system time representation with no leap-second conversion yet.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.4.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.4.0 implementation stop reached. Run pentest for this exact commit.`

### v0.5.0 - Leap-second/UTC realization model and explicit rollover ambiguity

Status: planned.

Goal: deliver leap-second/UTC realization model and explicit rollover ambiguity as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- leap-second/UTC realization model and explicit rollover ambiguity.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.5.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.5.0 implementation stop reached. Run pentest for this exact commit.`

### v0.6.0 - Coordinate types: geodetic, ECEF, ENU and NED

Status: planned.

Goal: deliver coordinate types: geodetic, ECEF, ENU and NED as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- coordinate types: geodetic, ECEF, ENU and NED.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.6.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.6.0 implementation stop reached. Run pentest for this exact commit.`

### v0.7.0 - Geodesic, ellipsoid and reference-frame primitives

Status: planned.

Goal: deliver geodesic, ellipsoid and reference-frame primitives as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- geodesic, ellipsoid and reference-frame primitives.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.7.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.7.0 implementation stop reached. Run pentest for this exact commit.`

### v0.8.0 - Bit readers/writers, sign extension and reserved-bit preservation

Status: planned.

Goal: deliver bit readers/writers, sign extension and reserved-bit preservation as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- bit readers/writers, sign extension and reserved-bit preservation.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.8.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.8.0 implementation stop reached. Run pentest for this exact commit.`

### v0.9.0 - Checksums, CRC framework and GNSS parity primitives

Status: planned.

Goal: deliver checksums, CRC framework and GNSS parity primitives as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- checksums, CRC framework and GNSS parity primitives.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.9.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.9.0 implementation stop reached. Run pentest for this exact commit.`

### v0.10.0 - Convolutional, BCH, Reed–Solomon and interleaving primitives required by the selected...

Status: planned.

Goal: deliver convolutional, BCH, Reed–Solomon and interleaving primitives required by the selected ICDs as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- convolutional, BCH, Reed–Solomon and interleaving primitives required by the selected ICDs.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.10.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.10.0 implementation stop reached. Run pentest for this exact commit.`

### v0.11.0 - LDPC/polar or other modern FEC kernels required by public signals, one verified famil...

Status: planned.

Goal: deliver lDPC/polar or other modern FEC kernels required by public signals, one verified family at a time as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- LDPC/polar or other modern FEC kernels required by public signals, one verified family at a time.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.11.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.11.0 implementation stop reached. Run pentest for this exact commit.`

### v0.12.0 - Extensible system/satellite/signal identifiers and registry versioning

Status: planned.

Goal: deliver extensible system/satellite/signal identifiers and registry versioning as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- extensible system/satellite/signal identifiers and registry versioning.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.12.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.12.0 implementation stop reached. Run pentest for this exact commit.`

### v0.13.0 - Canonical observation/epoch model

Status: planned.

Goal: deliver canonical observation/epoch model as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- canonical observation/epoch model.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.13.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.13.0 implementation stop reached. Run pentest for this exact commit.`

### v0.14.0 - Ephemeris, almanac, health and clock model traits

Status: planned.

Goal: deliver ephemeris, almanac, health and clock model traits as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- ephemeris, almanac, health and clock model traits.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.14.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.14.0 implementation stop reached. Run pentest for this exact commit.`

### v0.15.0 - Correction and provenance models

Status: planned.

Goal: deliver correction and provenance models as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- correction and provenance models.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.15.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.15.0 implementation stop reached. Run pentest for this exact commit.`

### v0.16.0 - Event, source, sink and deterministic polling traits

Status: planned.

Goal: deliver event, source, sink and deterministic polling traits as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- event, source, sink and deterministic polling traits.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.16.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.16.0 implementation stop reached. Run pentest for this exact commit.`

### v0.17.0 - Capability negotiation and resource-planning contracts

Status: planned.

Goal: deliver capability negotiation and resource-planning contracts as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- capability negotiation and resource-planning contracts.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.17.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.17.0 implementation stop reached. Run pentest for this exact commit.`

### v0.18.0 - Canonical configuration serialization without external serialization crates

Status: planned.

Goal: deliver canonical configuration serialization without external serialization crates as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- canonical configuration serialization without external serialization crates.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.18.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.18.0 implementation stop reached. Run pentest for this exact commit.`

### v0.19.0 - Allocated convenience layer

Status: planned.

Goal: deliver allocated convenience layer as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- allocated convenience layer.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.19.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.19.0 implementation stop reached. Run pentest for this exact commit.`

### v0.20.0 - Initial `navheim` facade and `Profile::Replay`

Status: planned.

Goal: deliver initial `navheim` facade and `Profile::Replay` as one bounded,
reviewable release in Phase A (Foundation and contracts).

Deliverables:

- initial `navheim` facade and `Profile::Replay`.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.20.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform MSRV and pinned-stable builds, no_std checks, boundary tests, metadata checks, and deterministic policy tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.20.0 implementation stop reached. Run pentest for this exact commit.`

## Phase B: File and byte-stream interoperability

### v0.21.0 - NMEA 0183 framing, checksum and bounded recovery

Status: planned.

Goal: deliver nMEA 0183 framing, checksum and bounded recovery as one bounded,
reviewable release in Phase B (File and byte-stream interoperability).

Deliverables:

- NMEA 0183 framing, checksum and bounded recovery.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.21.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official format examples, malformed/truncated/adversarial streams, exact-consumption and round-trip properties, recovery tests, and parser fuzz smoke;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.21.0 implementation stop reached. Run pentest for this exact commit.`

### v0.22.0 - GNSS-relevant NMEA 0183 sentence models for the licensed baseline

Status: planned.

Goal: deliver gNSS-relevant NMEA 0183 sentence models for the licensed baseline as one bounded,
reviewable release in Phase B (File and byte-stream interoperability).

Deliverables:

- GNSS-relevant NMEA 0183 sentence models for the licensed baseline.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.22.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official format examples, malformed/truncated/adversarial streams, exact-consumption and round-trip properties, recovery tests, and parser fuzz smoke;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.22.0 implementation stop reached. Run pentest for this exact commit.`

### v0.23.0 - RTCM 3 framing and CRC

Status: planned.

Goal: deliver rTCM 3 framing and CRC as one bounded,
reviewable release in Phase B (File and byte-stream interoperability).

Deliverables:

- RTCM 3 framing and CRC.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.23.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official format examples, malformed/truncated/adversarial streams, exact-consumption and round-trip properties, recovery tests, and parser fuzz smoke;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.23.0 implementation stop reached. Run pentest for this exact commit.`

### v0.24.0 - RTCM station/antenna descriptor messages

Status: planned.

Goal: deliver rTCM station/antenna descriptor messages as one bounded,
reviewable release in Phase B (File and byte-stream interoperability).

Deliverables:

- RTCM station/antenna descriptor messages.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.24.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official format examples, malformed/truncated/adversarial streams, exact-consumption and round-trip properties, recovery tests, and parser fuzz smoke;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.24.0 implementation stop reached. Run pentest for this exact commit.`

### v0.25.0 - RTCM MSM observation decoding/encoding

Status: planned.

Goal: deliver rTCM MSM observation decoding/encoding as one bounded,
reviewable release in Phase B (File and byte-stream interoperability).

Deliverables:

- RTCM MSM observation decoding/encoding.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.25.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official format examples, malformed/truncated/adversarial streams, exact-consumption and round-trip properties, recovery tests, and parser fuzz smoke;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.25.0 implementation stop reached. Run pentest for this exact commit.`

### v0.26.0 - RTCM constellation ephemeris messages

Status: planned.

Goal: deliver rTCM constellation ephemeris messages as one bounded,
reviewable release in Phase B (File and byte-stream interoperability).

Deliverables:

- RTCM constellation ephemeris messages.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.26.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official format examples, malformed/truncated/adversarial streams, exact-consumption and round-trip properties, recovery tests, and parser fuzz smoke;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.26.0 implementation stop reached. Run pentest for this exact commit.`

### v0.27.0 - NTRIP source table and version 1 client

Status: planned.

Goal: deliver nTRIP source table and version 1 client as one bounded,
reviewable release in Phase B (File and byte-stream interoperability).

Deliverables:

- NTRIP source table and version 1 client.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.27.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official format examples, malformed/truncated/adversarial streams, exact-consumption and round-trip properties, recovery tests, and parser fuzz smoke;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.27.0 implementation stop reached. Run pentest for this exact commit.`

### v0.28.0 - NTRIP version 2 client/server/caster protocol core

Status: planned.

Goal: deliver nTRIP version 2 client/server/caster protocol core as one bounded,
reviewable release in Phase B (File and byte-stream interoperability).

Deliverables:

- NTRIP version 2 client/server/caster protocol core.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.28.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official format examples, malformed/truncated/adversarial streams, exact-consumption and round-trip properties, recovery tests, and parser fuzz smoke;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.28.0 implementation stop reached. Run pentest for this exact commit.`

### v0.29.0 - RINEX 2 observation streaming parser/writer

Status: planned.

Goal: deliver rINEX 2 observation streaming parser/writer as one bounded,
reviewable release in Phase B (File and byte-stream interoperability).

Deliverables:

- RINEX 2 observation streaming parser/writer.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.29.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official format examples, malformed/truncated/adversarial streams, exact-consumption and round-trip properties, recovery tests, and parser fuzz smoke;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.29.0 implementation stop reached. Run pentest for this exact commit.`

### v0.30.0 - RINEX 3 observation and navigation support

Status: planned.

Goal: deliver rINEX 3 observation and navigation support as one bounded,
reviewable release in Phase B (File and byte-stream interoperability).

Deliverables:

- RINEX 3 observation and navigation support.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.30.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official format examples, malformed/truncated/adversarial streams, exact-consumption and round-trip properties, recovery tests, and parser fuzz smoke;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.30.0 implementation stop reached. Run pentest for this exact commit.`

### v0.31.0 - RINEX 4 generic navigation records and current additions

Status: planned.

Goal: deliver rINEX 4 generic navigation records and current additions as one bounded,
reviewable release in Phase B (File and byte-stream interoperability).

Deliverables:

- RINEX 4 generic navigation records and current additions.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.31.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official format examples, malformed/truncated/adversarial streams, exact-consumption and round-trip properties, recovery tests, and parser fuzz smoke;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.31.0 implementation stop reached. Run pentest for this exact commit.`

### v0.32.0 - SP3 orbit and precise clock products

Status: planned.

Goal: deliver sP3 orbit and precise clock products as one bounded,
reviewable release in Phase B (File and byte-stream interoperability).

Deliverables:

- SP3 orbit and precise clock products.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.32.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official format examples, malformed/truncated/adversarial streams, exact-consumption and round-trip properties, recovery tests, and parser fuzz smoke;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.32.0 implementation stop reached. Run pentest for this exact commit.`

### v0.33.0 - IONEX

Status: planned.

Goal: deliver iONEX as one bounded,
reviewable release in Phase B (File and byte-stream interoperability).

Deliverables:

- IONEX.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.33.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official format examples, malformed/truncated/adversarial streams, exact-consumption and round-trip properties, recovery tests, and parser fuzz smoke;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.33.0 implementation stop reached. Run pentest for this exact commit.`

### v0.34.0 - ANTEX

Status: planned.

Goal: deliver aNTEX as one bounded,
reviewable release in Phase B (File and byte-stream interoperability).

Deliverables:

- ANTEX.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.34.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official format examples, malformed/truncated/adversarial streams, exact-consumption and round-trip properties, recovery tests, and parser fuzz smoke;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.34.0 implementation stop reached. Run pentest for this exact commit.`

### v0.35.0 - SINEX and Bias-SINEX foundations

Status: planned.

Goal: deliver sINEX and Bias-SINEX foundations as one bounded,
reviewable release in Phase B (File and byte-stream interoperability).

Deliverables:

- SINEX and Bias-SINEX foundations.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.35.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official format examples, malformed/truncated/adversarial streams, exact-consumption and round-trip properties, recovery tests, and parser fuzz smoke;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.35.0 implementation stop reached. Run pentest for this exact commit.`

### v0.36.0 - Deterministic raw-I/Q and observation replay container v0

Status: planned.

Goal: deliver deterministic raw-I/Q and observation replay container v0 as one bounded,
reviewable release in Phase B (File and byte-stream interoperability).

Deliverables:

- deterministic raw-I/Q and observation replay container v0.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.36.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official format examples, malformed/truncated/adversarial streams, exact-consumption and round-trip properties, recovery tests, and parser fuzz smoke;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.36.0 implementation stop reached. Run pentest for this exact commit.`

## Phase C: Native DSP reference implementation

### v0.37.0 - Complex/fixed-point types, NCO and oscillators

Status: planned.

Goal: deliver complex/fixed-point types, NCO and oscillators as one bounded,
reviewable release in Phase C (Native DSP reference implementation).

Deliverables:

- complex/fixed-point types, NCO and oscillators.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.37.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent numerical references, fixed-point and floating comparisons, deterministic replay, resource bounds, and scalar/optimized equivalence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.37.0 implementation stop reached. Run pentest for this exact commit.`

### v0.38.0 - FIR/IIR and decimation primitives

Status: planned.

Goal: deliver fIR/IIR and decimation primitives as one bounded,
reviewable release in Phase C (Native DSP reference implementation).

Deliverables:

- FIR/IIR and decimation primitives.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.38.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent numerical references, fixed-point and floating comparisons, deterministic replay, resource bounds, and scalar/optimized equivalence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.38.0 implementation stop reached. Run pentest for this exact commit.`

### v0.39.0 - Polyphase resampling

Status: planned.

Goal: deliver polyphase resampling as one bounded,
reviewable release in Phase C (Native DSP reference implementation).

Deliverables:

- polyphase resampling.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.39.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent numerical references, fixed-point and floating comparisons, deterministic replay, resource bounds, and scalar/optimized equivalence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.39.0 implementation stop reached. Run pentest for this exact commit.`

### v0.40.0 - Scalar radix-2/radix-4 FFT

Status: planned.

Goal: deliver scalar radix-2/radix-4 FFT as one bounded,
reviewable release in Phase C (Native DSP reference implementation).

Deliverables:

- scalar radix-2/radix-4 FFT.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.40.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent numerical references, fixed-point and floating comparisons, deterministic replay, resource bounds, and scalar/optimized equivalence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.40.0 implementation stop reached. Run pentest for this exact commit.`

### v0.41.0 - Mixed-radix FFT and convolution

Status: planned.

Goal: deliver mixed-radix FFT and convolution as one bounded,
reviewable release in Phase C (Native DSP reference implementation).

Deliverables:

- mixed-radix FFT and convolution.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.41.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent numerical references, fixed-point and floating comparisons, deterministic replay, resource bounds, and scalar/optimized equivalence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.41.0 implementation stop reached. Run pentest for this exact commit.`

### v0.42.0 - Polyphase channelizer

Status: planned.

Goal: deliver polyphase channelizer as one bounded,
reviewable release in Phase C (Native DSP reference implementation).

Deliverables:

- polyphase channelizer.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.42.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent numerical references, fixed-point and floating comparisons, deterministic replay, resource bounds, and scalar/optimized equivalence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.42.0 implementation stop reached. Run pentest for this exact commit.`

### v0.43.0 - Acquisition search framework and peak statistics

Status: planned.

Goal: deliver acquisition search framework and peak statistics as one bounded,
reviewable release in Phase C (Native DSP reference implementation).

Deliverables:

- acquisition search framework and peak statistics.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.43.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent numerical references, fixed-point and floating comparisons, deterministic replay, resource bounds, and scalar/optimized equivalence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.43.0 implementation stop reached. Run pentest for this exact commit.`

### v0.44.0 - DLL/FLL/PLL tracking-loop primitives

Status: planned.

Goal: deliver dLL/FLL/PLL tracking-loop primitives as one bounded,
reviewable release in Phase C (Native DSP reference implementation).

Deliverables:

- DLL/FLL/PLL tracking-loop primitives.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.44.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent numerical references, fixed-point and floating comparisons, deterministic replay, resource bounds, and scalar/optimized equivalence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.44.0 implementation stop reached. Run pentest for this exact commit.`

### v0.45.0 - Correlator banks, CN0 and lock estimators

Status: planned.

Goal: deliver correlator banks, CN0 and lock estimators as one bounded,
reviewable release in Phase C (Native DSP reference implementation).

Deliverables:

- correlator banks, CN0 and lock estimators.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.45.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent numerical references, fixed-point and floating comparisons, deterministic replay, resource bounds, and scalar/optimized equivalence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.45.0 implementation stop reached. Run pentest for this exact commit.`

### v0.46.0 - Bit/symbol/secondary-code synchronization

Status: planned.

Goal: deliver bit/symbol/secondary-code synchronization as one bounded,
reviewable release in Phase C (Native DSP reference implementation).

Deliverables:

- bit/symbol/secondary-code synchronization.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.46.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent numerical references, fixed-point and floating comparisons, deterministic replay, resource bounds, and scalar/optimized equivalence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.46.0 implementation stop reached. Run pentest for this exact commit.`

### v0.47.0 - Sample timestamp, gap and overrun model

Status: planned.

Goal: deliver sample timestamp, gap and overrun model as one bounded,
reviewable release in Phase C (Native DSP reference implementation).

Deliverables:

- sample timestamp, gap and overrun model.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.47.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent numerical references, fixed-point and floating comparisons, deterministic replay, resource bounds, and scalar/optimized equivalence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.47.0 implementation stop reached. Run pentest for this exact commit.`

### v0.48.0 - Scalar real-time scheduler and channel lifecycle

Status: planned.

Goal: deliver scalar real-time scheduler and channel lifecycle as one bounded,
reviewable release in Phase C (Native DSP reference implementation).

Deliverables:

- scalar real-time scheduler and channel lifecycle.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.48.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent numerical references, fixed-point and floating comparisons, deterministic replay, resource bounds, and scalar/optimized equivalence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.48.0 implementation stop reached. Run pentest for this exact commit.`

### v0.49.0 - SIMD dispatch boundary with reference equivalence tests

Status: planned.

Goal: deliver sIMD dispatch boundary with reference equivalence tests as one bounded,
reviewable release in Phase C (Native DSP reference implementation).

Deliverables:

- SIMD dispatch boundary with reference equivalence tests.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.49.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent numerical references, fixed-point and floating comparisons, deterministic replay, resource bounds, and scalar/optimized equivalence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.49.0 implementation stop reached. Run pentest for this exact commit.`

### v0.50.0 - SDR deployment/band planner and complete capability errors

Status: planned.

Goal: deliver sDR deployment/band planner and complete capability errors as one bounded,
reviewable release in Phase C (Native DSP reference implementation).

Deliverables:

- SDR deployment/band planner and complete capability errors.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.50.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent numerical references, fixed-point and floating comparisons, deterministic replay, resource bounds, and scalar/optimized equivalence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.50.0 implementation stop reached. Run pentest for this exact commit.`

## Phase D: GPS end-to-end

### v0.51.0 - GPS L1 C/A code generation and test vectors

Status: planned.

Goal: deliver gPS L1 C/A code generation and test vectors as one bounded,
reviewable release in Phase D (GPS end-to-end).

Deliverables:

- GPS L1 C/A code generation and test vectors.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.51.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GPS vectors, generated baseband, recorded independent captures, receiver comparison, malformed navigation data, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.51.0 implementation stop reached. Run pentest for this exact commit.`

### v0.52.0 - GPS L1 C/A acquisition

Status: planned.

Goal: deliver gPS L1 C/A acquisition as one bounded,
reviewable release in Phase D (GPS end-to-end).

Deliverables:

- GPS L1 C/A acquisition.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.52.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GPS vectors, generated baseband, recorded independent captures, receiver comparison, malformed navigation data, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.52.0 implementation stop reached. Run pentest for this exact commit.`

### v0.53.0 - GPS L1 C/A tracking and observables

Status: planned.

Goal: deliver gPS L1 C/A tracking and observables as one bounded,
reviewable release in Phase D (GPS end-to-end).

Deliverables:

- GPS L1 C/A tracking and observables.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.53.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GPS vectors, generated baseband, recorded independent captures, receiver comparison, malformed navigation data, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.53.0 implementation stop reached. Run pentest for this exact commit.`

### v0.54.0 - GPS LNAV parity/frame/subframe decode

Status: planned.

Goal: deliver gPS LNAV parity/frame/subframe decode as one bounded,
reviewable release in Phase D (GPS end-to-end).

Deliverables:

- GPS LNAV parity/frame/subframe decode.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.54.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GPS vectors, generated baseband, recorded independent captures, receiver comparison, malformed navigation data, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.54.0 implementation stop reached. Run pentest for this exact commit.`

### v0.55.0 - GPS LNAV ephemeris, almanac, UTC and ionosphere

Status: planned.

Goal: deliver gPS LNAV ephemeris, almanac, UTC and ionosphere as one bounded,
reviewable release in Phase D (GPS end-to-end).

Deliverables:

- GPS LNAV ephemeris, almanac, UTC and ionosphere.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.55.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GPS vectors, generated baseband, recorded independent captures, receiver comparison, malformed navigation data, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.55.0 implementation stop reached. Run pentest for this exact commit.`

### v0.56.0 - Satellite state and clock computation

Status: planned.

Goal: deliver satellite state and clock computation as one bounded,
reviewable release in Phase D (GPS end-to-end).

Deliverables:

- satellite state and clock computation.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.56.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GPS vectors, generated baseband, recorded independent captures, receiver comparison, malformed navigation data, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.56.0 implementation stop reached. Run pentest for this exact commit.`

### v0.57.0 - Pseudorange formation and transmit-time iteration

Status: planned.

Goal: deliver pseudorange formation and transmit-time iteration as one bounded,
reviewable release in Phase D (GPS end-to-end).

Deliverables:

- pseudorange formation and transmit-time iteration.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.57.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GPS vectors, generated baseband, recorded independent captures, receiver comparison, malformed navigation data, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.57.0 implementation stop reached. Run pentest for this exact commit.`

### v0.58.0 - Standalone GPS weighted least-squares PVT

Status: planned.

Goal: deliver standalone GPS weighted least-squares PVT as one bounded,
reviewable release in Phase D (GPS end-to-end).

Deliverables:

- standalone GPS weighted least-squares PVT.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.58.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GPS vectors, generated baseband, recorded independent captures, receiver comparison, malformed navigation data, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.58.0 implementation stop reached. Run pentest for this exact commit.`

### v0.59.0 - Doppler velocity and receiver clock drift

Status: planned.

Goal: deliver doppler velocity and receiver clock drift as one bounded,
reviewable release in Phase D (GPS end-to-end).

Deliverables:

- Doppler velocity and receiver clock drift.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.59.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GPS vectors, generated baseband, recorded independent captures, receiver comparison, malformed navigation data, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.59.0 implementation stop reached. Run pentest for this exact commit.`

### v0.60.0 - GPS L2C codes, acquisition and tracking

Status: planned.

Goal: deliver gPS L2C codes, acquisition and tracking as one bounded,
reviewable release in Phase D (GPS end-to-end).

Deliverables:

- GPS L2C codes, acquisition and tracking.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.60.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GPS vectors, generated baseband, recorded independent captures, receiver comparison, malformed navigation data, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.60.0 implementation stop reached. Run pentest for this exact commit.`

### v0.61.0 - GPS CNAV decode

Status: planned.

Goal: deliver gPS CNAV decode as one bounded,
reviewable release in Phase D (GPS end-to-end).

Deliverables:

- GPS CNAV decode.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.61.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GPS vectors, generated baseband, recorded independent captures, receiver comparison, malformed navigation data, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.61.0 implementation stop reached. Run pentest for this exact commit.`

### v0.62.0 - GPS L5 acquisition/tracking

Status: planned.

Goal: deliver gPS L5 acquisition/tracking as one bounded,
reviewable release in Phase D (GPS end-to-end).

Deliverables:

- GPS L5 acquisition/tracking.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.62.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GPS vectors, generated baseband, recorded independent captures, receiver comparison, malformed navigation data, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.62.0 implementation stop reached. Run pentest for this exact commit.`

### v0.63.0 - GPS L5 CNAV and signal corrections

Status: planned.

Goal: deliver gPS L5 CNAV and signal corrections as one bounded,
reviewable release in Phase D (GPS end-to-end).

Deliverables:

- GPS L5 CNAV and signal corrections.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.63.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GPS vectors, generated baseband, recorded independent captures, receiver comparison, malformed navigation data, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.63.0 implementation stop reached. Run pentest for this exact commit.`

### v0.64.0 - GPS L1C acquisition/tracking

Status: planned.

Goal: deliver gPS L1C acquisition/tracking as one bounded,
reviewable release in Phase D (GPS end-to-end).

Deliverables:

- GPS L1C acquisition/tracking.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.64.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GPS vectors, generated baseband, recorded independent captures, receiver comparison, malformed navigation data, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.64.0 implementation stop reached. Run pentest for this exact commit.`

### v0.65.0 - GPS CNAV-2

Status: planned.

Goal: deliver gPS CNAV-2 as one bounded,
reviewable release in Phase D (GPS end-to-end).

Deliverables:

- GPS CNAV-2.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.65.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GPS vectors, generated baseband, recorded independent captures, receiver comparison, malformed navigation data, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.65.0 implementation stop reached. Run pentest for this exact commit.`

### v0.66.0 - GPS multi-frequency combinations and consistency

Status: planned.

Goal: deliver gPS multi-frequency combinations and consistency as one bounded,
reviewable release in Phase D (GPS end-to-end).

Deliverables:

- GPS multi-frequency combinations and consistency.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.66.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GPS vectors, generated baseband, recorded independent captures, receiver comparison, malformed navigation data, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.66.0 implementation stop reached. Run pentest for this exact commit.`

## Phase E: Galileo

### v0.67.0 - Galileo E1 code generation/acquisition

Status: planned.

Goal: deliver galileo E1 code generation/acquisition as one bounded,
reviewable release in Phase E (Galileo).

Deliverables:

- Galileo E1 code generation/acquisition.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.67.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official Galileo vectors, generated and recorded signals, receiver comparison, FEC/page faults, time checks, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.67.0 implementation stop reached. Run pentest for this exact commit.`

### v0.68.0 - Galileo E1 tracking and secondary-code synchronization

Status: planned.

Goal: deliver galileo E1 tracking and secondary-code synchronization as one bounded,
reviewable release in Phase E (Galileo).

Deliverables:

- Galileo E1 tracking and secondary-code synchronization.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.68.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official Galileo vectors, generated and recorded signals, receiver comparison, FEC/page faults, time checks, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.68.0 implementation stop reached. Run pentest for this exact commit.`

### v0.69.0 - Galileo I/NAV page/FEC decode

Status: planned.

Goal: deliver galileo I/NAV page/FEC decode as one bounded,
reviewable release in Phase E (Galileo).

Deliverables:

- Galileo I/NAV page/FEC decode.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.69.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official Galileo vectors, generated and recorded signals, receiver comparison, FEC/page faults, time checks, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.69.0 implementation stop reached. Run pentest for this exact commit.`

### v0.70.0 - Galileo ephemeris, clock, health, GST/UTC

Status: planned.

Goal: deliver galileo ephemeris, clock, health, GST/UTC as one bounded,
reviewable release in Phase E (Galileo).

Deliverables:

- Galileo ephemeris, clock, health, GST/UTC.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.70.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official Galileo vectors, generated and recorded signals, receiver comparison, FEC/page faults, time checks, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.70.0 implementation stop reached. Run pentest for this exact commit.`

### v0.71.0 - Galileo E5a acquisition/tracking

Status: planned.

Goal: deliver galileo E5a acquisition/tracking as one bounded,
reviewable release in Phase E (Galileo).

Deliverables:

- Galileo E5a acquisition/tracking.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.71.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official Galileo vectors, generated and recorded signals, receiver comparison, FEC/page faults, time checks, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.71.0 implementation stop reached. Run pentest for this exact commit.`

### v0.72.0 - Galileo F/NAV

Status: planned.

Goal: deliver galileo F/NAV as one bounded,
reviewable release in Phase E (Galileo).

Deliverables:

- Galileo F/NAV.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.72.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official Galileo vectors, generated and recorded signals, receiver comparison, FEC/page faults, time checks, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.72.0 implementation stop reached. Run pentest for this exact commit.`

### v0.73.0 - Galileo E5b acquisition/tracking and I/NAV path

Status: planned.

Goal: deliver galileo E5b acquisition/tracking and I/NAV path as one bounded,
reviewable release in Phase E (Galileo).

Deliverables:

- Galileo E5b acquisition/tracking and I/NAV path.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.73.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official Galileo vectors, generated and recorded signals, receiver comparison, FEC/page faults, time checks, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.73.0 implementation stop reached. Run pentest for this exact commit.`

### v0.74.0 - Galileo AltBOC component and full-band processing

Status: planned.

Goal: deliver galileo AltBOC component and full-band processing as one bounded,
reviewable release in Phase E (Galileo).

Deliverables:

- Galileo AltBOC component and full-band processing.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.74.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official Galileo vectors, generated and recorded signals, receiver comparison, FEC/page faults, time checks, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.74.0 implementation stop reached. Run pentest for this exact commit.`

### v0.75.0 - Galileo E6 acquisition/tracking

Status: planned.

Goal: deliver galileo E6 acquisition/tracking as one bounded,
reviewable release in Phase E (Galileo).

Deliverables:

- Galileo E6 acquisition/tracking.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.75.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official Galileo vectors, generated and recorded signals, receiver comparison, FEC/page faults, time checks, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.75.0 implementation stop reached. Run pentest for this exact commit.`

### v0.76.0 - Galileo HAS message and correction model

Status: planned.

Goal: deliver galileo HAS message and correction model as one bounded,
reviewable release in Phase E (Galileo).

Deliverables:

- Galileo HAS message and correction model.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.76.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official Galileo vectors, generated and recorded signals, receiver comparison, FEC/page faults, time checks, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.76.0 implementation stop reached. Run pentest for this exact commit.`

### v0.77.0 - Galileo SAR/RLS public message support

Status: planned.

Goal: deliver galileo SAR/RLS public message support as one bounded,
reviewable release in Phase E (Galileo).

Deliverables:

- Galileo SAR/RLS public message support.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.77.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official Galileo vectors, generated and recorded signals, receiver comparison, FEC/page faults, time checks, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.77.0 implementation stop reached. Run pentest for this exact commit.`

### v0.78.0 - Galileo Timing Service Message

Status: planned.

Goal: deliver galileo Timing Service Message as one bounded,
reviewable release in Phase E (Galileo).

Deliverables:

- Galileo Timing Service Message.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.78.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official Galileo vectors, generated and recorded signals, receiver comparison, FEC/page faults, time checks, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.78.0 implementation stop reached. Run pentest for this exact commit.`

### v0.79.0 - Galileo EWSS/public emergency-message support

Status: planned.

Goal: deliver galileo EWSS/public emergency-message support as one bounded,
reviewable release in Phase E (Galileo).

Deliverables:

- Galileo EWSS/public emergency-message support.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.79.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official Galileo vectors, generated and recorded signals, receiver comparison, FEC/page faults, time checks, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.79.0 implementation stop reached. Run pentest for this exact commit.`

### v0.80.0 - Galileo E5 quasi-pilot/current new-signal additions

Status: planned.

Goal: deliver galileo E5 quasi-pilot/current new-signal additions as one bounded,
reviewable release in Phase E (Galileo).

Deliverables:

- Galileo E5 quasi-pilot/current new-signal additions.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.80.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official Galileo vectors, generated and recorded signals, receiver comparison, FEC/page faults, time checks, and end-to-end replay;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.80.0 implementation stop reached. Run pentest for this exact commit.`

## Phase F: GLONASS

### v0.81.0 - GLONASS FDMA band/channel planner

Status: planned.

Goal: deliver gLONASS FDMA band/channel planner as one bounded,
reviewable release in Phase F (GLONASS).

Deliverables:

- GLONASS FDMA band/channel planner.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.81.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GLONASS vectors, FDMA/CDMA channel cases, generated and recorded signals, bias/time faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.81.0 implementation stop reached. Run pentest for this exact commit.`

### v0.82.0 - GLONASS L1OF acquisition/tracking

Status: planned.

Goal: deliver gLONASS L1OF acquisition/tracking as one bounded,
reviewable release in Phase F (GLONASS).

Deliverables:

- GLONASS L1OF acquisition/tracking.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.82.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GLONASS vectors, FDMA/CDMA channel cases, generated and recorded signals, bias/time faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.82.0 implementation stop reached. Run pentest for this exact commit.`

### v0.83.0 - GLONASS L1OF navigation strings and time

Status: planned.

Goal: deliver gLONASS L1OF navigation strings and time as one bounded,
reviewable release in Phase F (GLONASS).

Deliverables:

- GLONASS L1OF navigation strings and time.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.83.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GLONASS vectors, FDMA/CDMA channel cases, generated and recorded signals, bias/time faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.83.0 implementation stop reached. Run pentest for this exact commit.`

### v0.84.0 - GLONASS orbit/clock computation

Status: planned.

Goal: deliver gLONASS orbit/clock computation as one bounded,
reviewable release in Phase F (GLONASS).

Deliverables:

- GLONASS orbit/clock computation.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.84.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GLONASS vectors, FDMA/CDMA channel cases, generated and recorded signals, bias/time faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.84.0 implementation stop reached. Run pentest for this exact commit.`

### v0.85.0 - GLONASS L2OF acquisition/tracking and navigation

Status: planned.

Goal: deliver gLONASS L2OF acquisition/tracking and navigation as one bounded,
reviewable release in Phase F (GLONASS).

Deliverables:

- GLONASS L2OF acquisition/tracking and navigation.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.85.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GLONASS vectors, FDMA/CDMA channel cases, generated and recorded signals, bias/time faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.85.0 implementation stop reached. Run pentest for this exact commit.`

### v0.86.0 - GLONASS FDMA observation/bias model

Status: planned.

Goal: deliver gLONASS FDMA observation/bias model as one bounded,
reviewable release in Phase F (GLONASS).

Deliverables:

- GLONASS FDMA observation/bias model.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.86.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GLONASS vectors, FDMA/CDMA channel cases, generated and recorded signals, bias/time faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.86.0 implementation stop reached. Run pentest for this exact commit.`

### v0.87.0 - GLONASS L1OC public CDMA signal

Status: planned.

Goal: deliver gLONASS L1OC public CDMA signal as one bounded,
reviewable release in Phase F (GLONASS).

Deliverables:

- GLONASS L1OC public CDMA signal.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.87.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GLONASS vectors, FDMA/CDMA channel cases, generated and recorded signals, bias/time faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.87.0 implementation stop reached. Run pentest for this exact commit.`

### v0.88.0 - GLONASS L2OC public CDMA signal

Status: planned.

Goal: deliver gLONASS L2OC public CDMA signal as one bounded,
reviewable release in Phase F (GLONASS).

Deliverables:

- GLONASS L2OC public CDMA signal.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.88.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GLONASS vectors, FDMA/CDMA channel cases, generated and recorded signals, bias/time faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.88.0 implementation stop reached. Run pentest for this exact commit.`

### v0.89.0 - GLONASS L3OC public CDMA signal

Status: planned.

Goal: deliver gLONASS L3OC public CDMA signal as one bounded,
reviewable release in Phase F (GLONASS).

Deliverables:

- GLONASS L3OC public CDMA signal.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.89.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GLONASS vectors, FDMA/CDMA channel cases, generated and recorded signals, bias/time faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.89.0 implementation stop reached. Run pentest for this exact commit.`

### v0.90.0 - Mixed FDMA/CDMA solution validation

Status: planned.

Goal: deliver mixed FDMA/CDMA solution validation as one bounded,
reviewable release in Phase F (GLONASS).

Deliverables:

- mixed FDMA/CDMA solution validation.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.90.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official GLONASS vectors, FDMA/CDMA channel cases, generated and recorded signals, bias/time faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.90.0 implementation stop reached. Run pentest for this exact commit.`

## Phase G: BeiDou

### v0.91.0 - BeiDou B1I acquisition/tracking

Status: planned.

Goal: deliver beiDou B1I acquisition/tracking as one bounded,
reviewable release in Phase G (BeiDou).

Deliverables:

- BeiDou B1I acquisition/tracking.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.91.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official BeiDou vectors, GEO/IGSO/MEO cases, generated and recorded signals, time/correction faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.91.0 implementation stop reached. Run pentest for this exact commit.`

### v0.92.0 - BeiDou D1/D2 navigation and GEO/IGSO/MEO handling

Status: planned.

Goal: deliver beiDou D1/D2 navigation and GEO/IGSO/MEO handling as one bounded,
reviewable release in Phase G (BeiDou).

Deliverables:

- BeiDou D1/D2 navigation and GEO/IGSO/MEO handling.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.92.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official BeiDou vectors, GEO/IGSO/MEO cases, generated and recorded signals, time/correction faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.92.0 implementation stop reached. Run pentest for this exact commit.`

### v0.93.0 - BeiDou time, orbit and clock computation

Status: planned.

Goal: deliver beiDou time, orbit and clock computation as one bounded,
reviewable release in Phase G (BeiDou).

Deliverables:

- BeiDou time, orbit and clock computation.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.93.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official BeiDou vectors, GEO/IGSO/MEO cases, generated and recorded signals, time/correction faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.93.0 implementation stop reached. Run pentest for this exact commit.`

### v0.94.0 - BeiDou B2I and B3I public signal paths

Status: planned.

Goal: deliver beiDou B2I and B3I public signal paths as one bounded,
reviewable release in Phase G (BeiDou).

Deliverables:

- BeiDou B2I and B3I public signal paths.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.94.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official BeiDou vectors, GEO/IGSO/MEO cases, generated and recorded signals, time/correction faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.94.0 implementation stop reached. Run pentest for this exact commit.`

### v0.95.0 - BeiDou B1C acquisition/tracking

Status: planned.

Goal: deliver beiDou B1C acquisition/tracking as one bounded,
reviewable release in Phase G (BeiDou).

Deliverables:

- BeiDou B1C acquisition/tracking.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.95.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official BeiDou vectors, GEO/IGSO/MEO cases, generated and recorded signals, time/correction faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.95.0 implementation stop reached. Run pentest for this exact commit.`

### v0.96.0 - BeiDou B-CNAV1

Status: planned.

Goal: deliver beiDou B-CNAV1 as one bounded,
reviewable release in Phase G (BeiDou).

Deliverables:

- BeiDou B-CNAV1.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.96.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official BeiDou vectors, GEO/IGSO/MEO cases, generated and recorded signals, time/correction faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.96.0 implementation stop reached. Run pentest for this exact commit.`

### v0.97.0 - BeiDou B2a acquisition/tracking

Status: planned.

Goal: deliver beiDou B2a acquisition/tracking as one bounded,
reviewable release in Phase G (BeiDou).

Deliverables:

- BeiDou B2a acquisition/tracking.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.97.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official BeiDou vectors, GEO/IGSO/MEO cases, generated and recorded signals, time/correction faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.97.0 implementation stop reached. Run pentest for this exact commit.`

### v0.98.0 - BeiDou B-CNAV2

Status: planned.

Goal: deliver beiDou B-CNAV2 as one bounded,
reviewable release in Phase G (BeiDou).

Deliverables:

- BeiDou B-CNAV2.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.98.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official BeiDou vectors, GEO/IGSO/MEO cases, generated and recorded signals, time/correction faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.98.0 implementation stop reached. Run pentest for this exact commit.`

### v0.99.0 - BeiDou B2b acquisition/tracking

Status: planned.

Goal: deliver beiDou B2b acquisition/tracking as one bounded,
reviewable release in Phase G (BeiDou).

Deliverables:

- BeiDou B2b acquisition/tracking.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.99.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official BeiDou vectors, GEO/IGSO/MEO cases, generated and recorded signals, time/correction faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.99.0 implementation stop reached. Run pentest for this exact commit.`

### v0.100.0 - BeiDou B-CNAV3/basic navigation

Status: planned.

Goal: deliver beiDou B-CNAV3/basic navigation as one bounded,
reviewable release in Phase G (BeiDou).

Deliverables:

- BeiDou B-CNAV3/basic navigation.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.100.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official BeiDou vectors, GEO/IGSO/MEO cases, generated and recorded signals, time/correction faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.100.0 implementation stop reached. Run pentest for this exact commit.`

### v0.101.0 - BeiDou B2ab combined processing

Status: planned.

Goal: deliver beiDou B2ab combined processing as one bounded,
reviewable release in Phase G (BeiDou).

Deliverables:

- BeiDou B2ab combined processing.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.101.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official BeiDou vectors, GEO/IGSO/MEO cases, generated and recorded signals, time/correction faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.101.0 implementation stop reached. Run pentest for this exact commit.`

### v0.102.0 - BeiDou PPP-B2b correction service

Status: planned.

Goal: deliver beiDou PPP-B2b correction service as one bounded,
reviewable release in Phase G (BeiDou).

Deliverables:

- BeiDou PPP-B2b correction service.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.102.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official BeiDou vectors, GEO/IGSO/MEO cases, generated and recorded signals, time/correction faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.102.0 implementation stop reached. Run pentest for this exact commit.`

### v0.103.0 - Public BDSBAS interfaces

Status: planned.

Goal: deliver public BDSBAS interfaces as one bounded,
reviewable release in Phase G (BeiDou).

Deliverables:

- public BDSBAS interfaces.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.103.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official BeiDou vectors, GEO/IGSO/MEO cases, generated and recorded signals, time/correction faults, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.103.0 implementation stop reached. Run pentest for this exact commit.`

## Phase H: QZSS, NavIC and SBAS

### v0.104.0 - QZSS L1 family and regional geometry

Status: planned.

Goal: deliver qZSS L1 family and regional geometry as one bounded,
reviewable release in Phase H (QZSS, NavIC and SBAS).

Deliverables:

- QZSS L1 family and regional geometry.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.104.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official QZSS/NavIC/SBAS vectors, provider/profile cases, generated and recorded signals, integrity timeouts, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.104.0 implementation stop reached. Run pentest for this exact commit.`

### v0.105.0 - QZSS L2C/L5

Status: planned.

Goal: deliver qZSS L2C/L5 as one bounded,
reviewable release in Phase H (QZSS, NavIC and SBAS).

Deliverables:

- QZSS L2C/L5.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.105.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official QZSS/NavIC/SBAS vectors, provider/profile cases, generated and recorded signals, integrity timeouts, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.105.0 implementation stop reached. Run pentest for this exact commit.`

### v0.106.0 - QZSS L1S and SLAS

Status: planned.

Goal: deliver qZSS L1S and SLAS as one bounded,
reviewable release in Phase H (QZSS, NavIC and SBAS).

Deliverables:

- QZSS L1S and SLAS.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.106.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official QZSS/NavIC/SBAS vectors, provider/profile cases, generated and recorded signals, integrity timeouts, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.106.0 implementation stop reached. Run pentest for this exact commit.`

### v0.107.0 - QZSS L5S public augmentation path

Status: planned.

Goal: deliver qZSS L5S public augmentation path as one bounded,
reviewable release in Phase H (QZSS, NavIC and SBAS).

Deliverables:

- QZSS L5S public augmentation path.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.107.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official QZSS/NavIC/SBAS vectors, provider/profile cases, generated and recorded signals, integrity timeouts, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.107.0 implementation stop reached. Run pentest for this exact commit.`

### v0.108.0 - QZSS L6 acquisition/tracking

Status: planned.

Goal: deliver qZSS L6 acquisition/tracking as one bounded,
reviewable release in Phase H (QZSS, NavIC and SBAS).

Deliverables:

- QZSS L6 acquisition/tracking.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.108.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official QZSS/NavIC/SBAS vectors, provider/profile cases, generated and recorded signals, integrity timeouts, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.108.0 implementation stop reached. Run pentest for this exact commit.`

### v0.109.0 - QZSS CLAS correction decode

Status: planned.

Goal: deliver qZSS CLAS correction decode as one bounded,
reviewable release in Phase H (QZSS, NavIC and SBAS).

Deliverables:

- QZSS CLAS correction decode.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.109.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official QZSS/NavIC/SBAS vectors, provider/profile cases, generated and recorded signals, integrity timeouts, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.109.0 implementation stop reached. Run pentest for this exact commit.`

### v0.110.0 - QZSS MADOCA/MADOCA-PPP public profiles

Status: planned.

Goal: deliver qZSS MADOCA/MADOCA-PPP public profiles as one bounded,
reviewable release in Phase H (QZSS, NavIC and SBAS).

Deliverables:

- QZSS MADOCA/MADOCA-PPP public profiles.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.110.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official QZSS/NavIC/SBAS vectors, provider/profile cases, generated and recorded signals, integrity timeouts, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.110.0 implementation stop reached. Run pentest for this exact commit.`

### v0.111.0 - NavIC L5 SPS

Status: planned.

Goal: deliver navIC L5 SPS as one bounded,
reviewable release in Phase H (QZSS, NavIC and SBAS).

Deliverables:

- NavIC L5 SPS.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.111.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official QZSS/NavIC/SBAS vectors, provider/profile cases, generated and recorded signals, integrity timeouts, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.111.0 implementation stop reached. Run pentest for this exact commit.`

### v0.112.0 - NavIC S-band SPS

Status: planned.

Goal: deliver navIC S-band SPS as one bounded,
reviewable release in Phase H (QZSS, NavIC and SBAS).

Deliverables:

- NavIC S-band SPS.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.112.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official QZSS/NavIC/SBAS vectors, provider/profile cases, generated and recorded signals, integrity timeouts, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.112.0 implementation stop reached. Run pentest for this exact commit.`

### v0.113.0 - NavIC L1 SPS

Status: planned.

Goal: deliver navIC L1 SPS as one bounded,
reviewable release in Phase H (QZSS, NavIC and SBAS).

Deliverables:

- NavIC L1 SPS.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.113.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official QZSS/NavIC/SBAS vectors, provider/profile cases, generated and recorded signals, integrity timeouts, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.113.0 implementation stop reached. Run pentest for this exact commit.`

### v0.114.0 - NavIC time/orbit/clock and multi-band solution

Status: planned.

Goal: deliver navIC time/orbit/clock and multi-band solution as one bounded,
reviewable release in Phase H (QZSS, NavIC and SBAS).

Deliverables:

- NavIC time/orbit/clock and multi-band solution.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.114.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official QZSS/NavIC/SBAS vectors, provider/profile cases, generated and recorded signals, integrity timeouts, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.114.0 implementation stop reached. Run pentest for this exact commit.`

### v0.115.0 - Generic legacy SBAS L1 framing/messages

Status: planned.

Goal: deliver generic legacy SBAS L1 framing/messages as one bounded,
reviewable release in Phase H (QZSS, NavIC and SBAS).

Deliverables:

- generic legacy SBAS L1 framing/messages.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.115.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official QZSS/NavIC/SBAS vectors, provider/profile cases, generated and recorded signals, integrity timeouts, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.115.0 implementation stop reached. Run pentest for this exact commit.`

### v0.116.0 - SBAS correction/degradation state machine

Status: planned.

Goal: deliver sBAS correction/degradation state machine as one bounded,
reviewable release in Phase H (QZSS, NavIC and SBAS).

Deliverables:

- SBAS correction/degradation state machine.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.116.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official QZSS/NavIC/SBAS vectors, provider/profile cases, generated and recorded signals, integrity timeouts, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.116.0 implementation stop reached. Run pentest for this exact commit.`

### v0.117.0 - SBAS integrity and protection-level inputs

Status: planned.

Goal: deliver sBAS integrity and protection-level inputs as one bounded,
reviewable release in Phase H (QZSS, NavIC and SBAS).

Deliverables:

- SBAS integrity and protection-level inputs.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.117.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official QZSS/NavIC/SBAS vectors, provider/profile cases, generated and recorded signals, integrity timeouts, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.117.0 implementation stop reached. Run pentest for this exact commit.`

### v0.118.0 - DFMC SBAS signal/messages

Status: planned.

Goal: deliver dFMC SBAS signal/messages as one bounded,
reviewable release in Phase H (QZSS, NavIC and SBAS).

Deliverables:

- DFMC SBAS signal/messages.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.118.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official QZSS/NavIC/SBAS vectors, provider/profile cases, generated and recorded signals, integrity timeouts, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.118.0 implementation stop reached. Run pentest for this exact commit.`

### v0.119.0 - Provider profiles and future-ID registry

Status: planned.

Goal: deliver provider profiles and future-ID registry as one bounded,
reviewable release in Phase H (QZSS, NavIC and SBAS).

Deliverables:

- provider profiles and future-ID registry.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.119.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official QZSS/NavIC/SBAS vectors, provider/profile cases, generated and recorded signals, integrity timeouts, and independent receiver comparison;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.119.0 implementation stop reached. Run pentest for this exact commit.`

## Phase I: Multi-GNSS solution quality

### v0.120.0 - Multi-constellation PVT and inter-system biases

Status: planned.

Goal: deliver multi-constellation PVT and inter-system biases as one bounded,
reviewable release in Phase I (Multi-GNSS solution quality).

Deliverables:

- multi-constellation PVT and inter-system biases.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.120.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent high-precision references, randomized geometry, degenerate/rank-deficient inputs, cross-architecture tolerances, and fault exclusion cases;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.120.0 implementation stop reached. Run pentest for this exact commit.`

### v0.121.0 - Robust estimation and fault exclusion

Status: planned.

Goal: deliver robust estimation and fault exclusion as one bounded,
reviewable release in Phase I (Multi-GNSS solution quality).

Deliverables:

- robust estimation and fault exclusion.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.121.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent high-precision references, randomized geometry, degenerate/rank-deficient inputs, cross-architecture tolerances, and fault exclusion cases;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.121.0 implementation stop reached. Run pentest for this exact commit.`

### v0.122.0 - Broadcast ionosphere/troposphere model suite

Status: planned.

Goal: deliver broadcast ionosphere/troposphere model suite as one bounded,
reviewable release in Phase I (Multi-GNSS solution quality).

Deliverables:

- broadcast ionosphere/troposphere model suite.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.122.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent high-precision references, randomized geometry, degenerate/rank-deficient inputs, cross-architecture tolerances, and fault exclusion cases;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.122.0 implementation stop reached. Run pentest for this exact commit.`

### v0.123.0 - Dual/multi-frequency combinations and TEC

Status: planned.

Goal: deliver dual/multi-frequency combinations and TEC as one bounded,
reviewable release in Phase I (Multi-GNSS solution quality).

Deliverables:

- dual/multi-frequency combinations and TEC.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.123.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent high-precision references, randomized geometry, degenerate/rank-deficient inputs, cross-architecture tolerances, and fault exclusion cases;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.123.0 implementation stop reached. Run pentest for this exact commit.`

### v0.124.0 - Carrier smoothing and multipath metrics

Status: planned.

Goal: deliver carrier smoothing and multipath metrics as one bounded,
reviewable release in Phase I (Multi-GNSS solution quality).

Deliverables:

- carrier smoothing and multipath metrics.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.124.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent high-precision references, randomized geometry, degenerate/rank-deficient inputs, cross-architecture tolerances, and fault exclusion cases;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.124.0 implementation stop reached. Run pentest for this exact commit.`

### v0.125.0 - Antenna phase-center and phase-wind-up models

Status: planned.

Goal: deliver antenna phase-center and phase-wind-up models as one bounded,
reviewable release in Phase I (Multi-GNSS solution quality).

Deliverables:

- antenna phase-center and phase-wind-up models.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.125.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent high-precision references, randomized geometry, degenerate/rank-deficient inputs, cross-architecture tolerances, and fault exclusion cases;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.125.0 implementation stop reached. Run pentest for this exact commit.`

### v0.126.0 - Earth rotation, tides and reference-frame transforms

Status: planned.

Goal: deliver earth rotation, tides and reference-frame transforms as one bounded,
reviewable release in Phase I (Multi-GNSS solution quality).

Deliverables:

- Earth rotation, tides and reference-frame transforms.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.126.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent high-precision references, randomized geometry, degenerate/rank-deficient inputs, cross-architecture tolerances, and fault exclusion cases;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.126.0 implementation stop reached. Run pentest for this exact commit.`

### v0.127.0 - RAIM

Status: planned.

Goal: deliver rAIM as one bounded,
reviewable release in Phase I (Multi-GNSS solution quality).

Deliverables:

- RAIM.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.127.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent high-precision references, randomized geometry, degenerate/rank-deficient inputs, cross-architecture tolerances, and fault exclusion cases;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.127.0 implementation stop reached. Run pentest for this exact commit.`

### v0.128.0 - ARAIM building blocks and assumptions API

Status: planned.

Goal: deliver aRAIM building blocks and assumptions API as one bounded,
reviewable release in Phase I (Multi-GNSS solution quality).

Deliverables:

- ARAIM building blocks and assumptions API.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.128.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent high-precision references, randomized geometry, degenerate/rank-deficient inputs, cross-architecture tolerances, and fault exclusion cases;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.128.0 implementation stop reached. Run pentest for this exact commit.`

### v0.129.0 - Protection levels and integrity event model

Status: planned.

Goal: deliver protection levels and integrity event model as one bounded,
reviewable release in Phase I (Multi-GNSS solution quality).

Deliverables:

- protection levels and integrity event model.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.129.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent high-precision references, randomized geometry, degenerate/rank-deficient inputs, cross-architecture tolerances, and fault exclusion cases;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.129.0 implementation stop reached. Run pentest for this exact commit.`

## Phase J: RTK and precise positioning

### v0.130.0 - Carrier-phase epoch model and slip detectors

Status: planned.

Goal: deliver carrier-phase epoch model and slip detectors as one bounded,
reviewable release in Phase J (RTK and precise positioning).

Deliverables:

- carrier-phase epoch model and slip detectors.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.130.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent RTK/PPP references, baseline and product replays, ambiguity/slip/freshness faults, frame validation, and receiver/software comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.130.0 implementation stop reached. Run pentest for this exact commit.`

### v0.131.0 - Base/rover synchronization and single differences

Status: planned.

Goal: deliver base/rover synchronization and single differences as one bounded,
reviewable release in Phase J (RTK and precise positioning).

Deliverables:

- base/rover synchronization and single differences.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.131.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent RTK/PPP references, baseline and product replays, ambiguity/slip/freshness faults, frame validation, and receiver/software comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.131.0 implementation stop reached. Run pentest for this exact commit.`

### v0.132.0 - Double-difference baseline filter

Status: planned.

Goal: deliver double-difference baseline filter as one bounded,
reviewable release in Phase J (RTK and precise positioning).

Deliverables:

- double-difference baseline filter.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.132.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent RTK/PPP references, baseline and product replays, ambiguity/slip/freshness faults, frame validation, and receiver/software comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.132.0 implementation stop reached. Run pentest for this exact commit.`

### v0.133.0 - Native integer ambiguity search

Status: planned.

Goal: deliver native integer ambiguity search as one bounded,
reviewable release in Phase J (RTK and precise positioning).

Deliverables:

- native integer ambiguity search.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.133.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent RTK/PPP references, baseline and product replays, ambiguity/slip/freshness faults, frame validation, and receiver/software comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.133.0 implementation stop reached. Run pentest for this exact commit.`

### v0.134.0 - Ambiguity validation and partial fixing

Status: planned.

Goal: deliver ambiguity validation and partial fixing as one bounded,
reviewable release in Phase J (RTK and precise positioning).

Deliverables:

- ambiguity validation and partial fixing.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.134.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent RTK/PPP references, baseline and product replays, ambiguity/slip/freshness faults, frame validation, and receiver/software comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.134.0 implementation stop reached. Run pentest for this exact commit.`

### v0.135.0 - RTK fixed/float lifecycle and rollback

Status: planned.

Goal: deliver rTK fixed/float lifecycle and rollback as one bounded,
reviewable release in Phase J (RTK and precise positioning).

Deliverables:

- RTK fixed/float lifecycle and rollback.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.135.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent RTK/PPP references, baseline and product replays, ambiguity/slip/freshness faults, frame validation, and receiver/software comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.135.0 implementation stop reached. Run pentest for this exact commit.`

### v0.136.0 - GLONASS FDMA RTK biases

Status: planned.

Goal: deliver gLONASS FDMA RTK biases as one bounded,
reviewable release in Phase J (RTK and precise positioning).

Deliverables:

- GLONASS FDMA RTK biases.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.136.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent RTK/PPP references, baseline and product replays, ambiguity/slip/freshness faults, frame validation, and receiver/software comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.136.0 implementation stop reached. Run pentest for this exact commit.`

### v0.137.0 - Moving-base and dual-antenna heading

Status: planned.

Goal: deliver moving-base and dual-antenna heading as one bounded,
reviewable release in Phase J (RTK and precise positioning).

Deliverables:

- moving-base and dual-antenna heading.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.137.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent RTK/PPP references, baseline and product replays, ambiguity/slip/freshness faults, frame validation, and receiver/software comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.137.0 implementation stop reached. Run pentest for this exact commit.`

### v0.138.0 - Network RTK standardized inputs

Status: planned.

Goal: deliver network RTK standardized inputs as one bounded,
reviewable release in Phase J (RTK and precise positioning).

Deliverables:

- network RTK standardized inputs.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.138.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent RTK/PPP references, baseline and product replays, ambiguity/slip/freshness faults, frame validation, and receiver/software comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.138.0 implementation stop reached. Run pentest for this exact commit.`

### v0.139.0 - RTCM SSR complete public baseline

Status: planned.

Goal: deliver rTCM SSR complete public baseline as one bounded,
reviewable release in Phase J (RTK and precise positioning).

Deliverables:

- RTCM SSR complete public baseline.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.139.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent RTK/PPP references, baseline and product replays, ambiguity/slip/freshness faults, frame validation, and receiver/software comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.139.0 implementation stop reached. Run pentest for this exact commit.`

### v0.140.0 - IGS SSR profile

Status: planned.

Goal: deliver iGS SSR profile as one bounded,
reviewable release in Phase J (RTK and precise positioning).

Deliverables:

- IGS SSR profile.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.140.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent RTK/PPP references, baseline and product replays, ambiguity/slip/freshness faults, frame validation, and receiver/software comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.140.0 implementation stop reached. Run pentest for this exact commit.`

### v0.141.0 - Post-processed PPP

Status: planned.

Goal: deliver post-processed PPP as one bounded,
reviewable release in Phase J (RTK and precise positioning).

Deliverables:

- post-processed PPP.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.141.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent RTK/PPP references, baseline and product replays, ambiguity/slip/freshness faults, frame validation, and receiver/software comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.141.0 implementation stop reached. Run pentest for this exact commit.`

### v0.142.0 - Real-time PPP

Status: planned.

Goal: deliver real-time PPP as one bounded,
reviewable release in Phase J (RTK and precise positioning).

Deliverables:

- real-time PPP.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.142.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent RTK/PPP references, baseline and product replays, ambiguity/slip/freshness faults, frame validation, and receiver/software comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.142.0 implementation stop reached. Run pentest for this exact commit.`

### v0.143.0 - PPP ambiguity resolution

Status: planned.

Goal: deliver pPP ambiguity resolution as one bounded,
reviewable release in Phase J (RTK and precise positioning).

Deliverables:

- PPP ambiguity resolution.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.143.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent RTK/PPP references, baseline and product replays, ambiguity/slip/freshness faults, frame validation, and receiver/software comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.143.0 implementation stop reached. Run pentest for this exact commit.`

### v0.144.0 - PPP-RTK regional atmosphere/bias models

Status: planned.

Goal: deliver pPP-RTK regional atmosphere/bias models as one bounded,
reviewable release in Phase J (RTK and precise positioning).

Deliverables:

- PPP-RTK regional atmosphere/bias models.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.144.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent RTK/PPP references, baseline and product replays, ambiguity/slip/freshness faults, frame validation, and receiver/software comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.144.0 implementation stop reached. Run pentest for this exact commit.`

### v0.145.0 - Static/rapid-static survey workflow

Status: planned.

Goal: deliver static/rapid-static survey workflow as one bounded,
reviewable release in Phase J (RTK and precise positioning).

Deliverables:

- static/rapid-static survey workflow.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.145.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent RTK/PPP references, baseline and product replays, ambiguity/slip/freshness faults, frame validation, and receiver/software comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.145.0 implementation stop reached. Run pentest for this exact commit.`

## Phase K: Authentication and resilience

### v0.146.0 - Cryptographic backend traits and trust-store model

Status: planned.

Goal: deliver cryptographic backend traits and trust-store model as one bounded,
reviewable release in Phase K (Authentication and resilience).

Deliverables:

- cryptographic backend traits and trust-store model.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.146.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official authentication vectors, delayed/reordered/missing/expired data, trust-root transitions, spoof/jam evidence scenarios, and policy-state tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.146.0 implementation stop reached. Run pentest for this exact commit.`

### v0.147.0 - Galileo OSNMA framing/assembly

Status: planned.

Goal: deliver galileo OSNMA framing/assembly as one bounded,
reviewable release in Phase K (Authentication and resilience).

Deliverables:

- Galileo OSNMA framing/assembly.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.147.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official authentication vectors, delayed/reordered/missing/expired data, trust-root transitions, spoof/jam evidence scenarios, and policy-state tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.147.0 implementation stop reached. Run pentest for this exact commit.`

### v0.148.0 - OSNMA key-chain and tag verification

Status: planned.

Goal: deliver oSNMA key-chain and tag verification as one bounded,
reviewable release in Phase K (Authentication and resilience).

Deliverables:

- OSNMA key-chain and tag verification.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.148.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official authentication vectors, delayed/reordered/missing/expired data, trust-root transitions, spoof/jam evidence scenarios, and policy-state tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.148.0 implementation stop reached. Run pentest for this exact commit.`

### v0.149.0 - OSNMA policy, renewal/revocation and evidence

Status: planned.

Goal: deliver oSNMA policy, renewal/revocation and evidence as one bounded,
reviewable release in Phase K (Authentication and resilience).

Deliverables:

- OSNMA policy, renewal/revocation and evidence.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.149.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official authentication vectors, delayed/reordered/missing/expired data, trust-root transitions, spoof/jam evidence scenarios, and policy-state tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.149.0 implementation stop reached. Run pentest for this exact commit.`

### v0.150.0 - QZSS QZNMA decode and verification

Status: planned.

Goal: deliver qZSS QZNMA decode and verification as one bounded,
reviewable release in Phase K (Authentication and resilience).

Deliverables:

- QZSS QZNMA decode and verification.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.150.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official authentication vectors, delayed/reordered/missing/expired data, trust-root transitions, spoof/jam evidence scenarios, and policy-state tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.150.0 implementation stop reached. Run pentest for this exact commit.`

### v0.151.0 - Multi-constellation navigation conflict detector

Status: planned.

Goal: deliver multi-constellation navigation conflict detector as one bounded,
reviewable release in Phase K (Authentication and resilience).

Deliverables:

- multi-constellation navigation conflict detector.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.151.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official authentication vectors, delayed/reordered/missing/expired data, trust-root transitions, spoof/jam evidence scenarios, and policy-state tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.151.0 implementation stop reached. Run pentest for this exact commit.`

### v0.152.0 - Doppler/motion/clock spoofing evidence

Status: planned.

Goal: deliver doppler/motion/clock spoofing evidence as one bounded,
reviewable release in Phase K (Authentication and resilience).

Deliverables:

- Doppler/motion/clock spoofing evidence.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.152.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official authentication vectors, delayed/reordered/missing/expired data, trust-root transitions, spoof/jam evidence scenarios, and policy-state tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.152.0 implementation stop reached. Run pentest for this exact commit.`

### v0.153.0 - Correlation/power/interference evidence

Status: planned.

Goal: deliver correlation/power/interference evidence as one bounded,
reviewable release in Phase K (Authentication and resilience).

Deliverables:

- correlation/power/interference evidence.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.153.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official authentication vectors, delayed/reordered/missing/expired data, trust-root transitions, spoof/jam evidence scenarios, and policy-state tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.153.0 implementation stop reached. Run pentest for this exact commit.`

### v0.154.0 - Meaconing/time-replay evidence

Status: planned.

Goal: deliver meaconing/time-replay evidence as one bounded,
reviewable release in Phase K (Authentication and resilience).

Deliverables:

- meaconing/time-replay evidence.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.154.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official authentication vectors, delayed/reordered/missing/expired data, trust-root transitions, spoof/jam evidence scenarios, and policy-state tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.154.0 implementation stop reached. Run pentest for this exact commit.`

### v0.155.0 - Multi-receiver and multi-antenna security inputs

Status: planned.

Goal: deliver multi-receiver and multi-antenna security inputs as one bounded,
reviewable release in Phase K (Authentication and resilience).

Deliverables:

- multi-receiver and multi-antenna security inputs.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.155.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official authentication vectors, delayed/reordered/missing/expired data, trust-root transitions, spoof/jam evidence scenarios, and policy-state tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.155.0 implementation stop reached. Run pentest for this exact commit.`

### v0.156.0 - Security policy engine and fail/degrade reactions

Status: planned.

Goal: deliver security policy engine and fail/degrade reactions as one bounded,
reviewable release in Phase K (Authentication and resilience).

Deliverables:

- security policy engine and fail/degrade reactions.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.156.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official authentication vectors, delayed/reordered/missing/expired data, trust-root transitions, spoof/jam evidence scenarios, and policy-state tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.156.0 implementation stop reached. Run pentest for this exact commit.`

### v0.157.0 - Signed forensic provenance stream

Status: planned.

Goal: deliver signed forensic provenance stream as one bounded,
reviewable release in Phase K (Authentication and resilience).

Deliverables:

- signed forensic provenance stream.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.157.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform official authentication vectors, delayed/reordered/missing/expired data, trust-root transitions, spoof/jam evidence scenarios, and policy-state tests;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.157.0 implementation stop reached. Run pentest for this exact commit.`

## Phase L: Timing and fusion

### v0.158.0 - All GNSS time-scale conversions and leap provenance

Status: planned.

Goal: deliver all GNSS time-scale conversions and leap provenance as one bounded,
reviewable release in Phase L (Timing and fusion).

Deliverables:

- all GNSS time-scale conversions and leap provenance.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.158.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent timing/fusion references, rollover and clock faults, delayed/out-of-sequence data, holdover growth, outage replay, and sensor comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.158.0 implementation stop reached. Run pentest for this exact commit.`

### v0.159.0 - PPS/time-mark pairing and cable-delay model

Status: planned.

Goal: deliver pPS/time-mark pairing and cable-delay model as one bounded,
reviewable release in Phase L (Timing and fusion).

Deliverables:

- PPS/time-mark pairing and cable-delay model.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.159.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent timing/fusion references, rollover and clock faults, delayed/out-of-sequence data, holdover growth, outage replay, and sensor comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.159.0 implementation stop reached. Run pentest for this exact commit.`

### v0.160.0 - Time-only solution and multi-source voting

Status: planned.

Goal: deliver time-only solution and multi-source voting as one bounded,
reviewable release in Phase L (Timing and fusion).

Deliverables:

- time-only solution and multi-source voting.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.160.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent timing/fusion references, rollover and clock faults, delayed/out-of-sequence data, holdover growth, outage replay, and sensor comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.160.0 implementation stop reached. Run pentest for this exact commit.`

### v0.161.0 - Oscillator model and clock steering estimates

Status: planned.

Goal: deliver oscillator model and clock steering estimates as one bounded,
reviewable release in Phase L (Timing and fusion).

Deliverables:

- oscillator model and clock steering estimates.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.161.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent timing/fusion references, rollover and clock faults, delayed/out-of-sequence data, holdover growth, outage replay, and sensor comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.161.0 implementation stop reached. Run pentest for this exact commit.`

### v0.162.0 - Holdover and uncertainty growth

Status: planned.

Goal: deliver holdover and uncertainty growth as one bounded,
reviewable release in Phase L (Timing and fusion).

Deliverables:

- holdover and uncertainty growth.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.162.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent timing/fusion references, rollover and clock faults, delayed/out-of-sequence data, holdover growth, outage replay, and sensor comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.162.0 implementation stop reached. Run pentest for this exact commit.`

### v0.163.0 - Authenticated/integrity-aware time policy

Status: planned.

Goal: deliver authenticated/integrity-aware time policy as one bounded,
reviewable release in Phase L (Timing and fusion).

Deliverables:

- authenticated/integrity-aware time policy.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.163.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent timing/fusion references, rollover and clock faults, delayed/out-of-sequence data, holdover growth, outage replay, and sensor comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.163.0 implementation stop reached. Run pentest for this exact commit.`

### v0.164.0 - Inertial mechanization

Status: planned.

Goal: deliver inertial mechanization as one bounded,
reviewable release in Phase L (Timing and fusion).

Deliverables:

- inertial mechanization.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.164.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent timing/fusion references, rollover and clock faults, delayed/out-of-sequence data, holdover growth, outage replay, and sensor comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.164.0 implementation stop reached. Run pentest for this exact commit.`

### v0.165.0 - Error-state EKF

Status: planned.

Goal: deliver error-state EKF as one bounded,
reviewable release in Phase L (Timing and fusion).

Deliverables:

- error-state EKF.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.165.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent timing/fusion references, rollover and clock faults, delayed/out-of-sequence data, holdover growth, outage replay, and sensor comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.165.0 implementation stop reached. Run pentest for this exact commit.`

### v0.166.0 - Wheel/barometer/magnetometer inputs

Status: planned.

Goal: deliver wheel/barometer/magnetometer inputs as one bounded,
reviewable release in Phase L (Timing and fusion).

Deliverables:

- wheel/barometer/magnetometer inputs.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.166.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent timing/fusion references, rollover and clock faults, delayed/out-of-sequence data, holdover growth, outage replay, and sensor comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.166.0 implementation stop reached. Run pentest for this exact commit.`

### v0.167.0 - Delayed/out-of-sequence fusion

Status: planned.

Goal: deliver delayed/out-of-sequence fusion as one bounded,
reviewable release in Phase L (Timing and fusion).

Deliverables:

- delayed/out-of-sequence fusion.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.167.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent timing/fusion references, rollover and clock faults, delayed/out-of-sequence data, holdover growth, outage replay, and sensor comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.167.0 implementation stop reached. Run pentest for this exact commit.`

### v0.168.0 - GNSS outage/dead-reckoning lifecycle

Status: planned.

Goal: deliver gNSS outage/dead-reckoning lifecycle as one bounded,
reviewable release in Phase L (Timing and fusion).

Deliverables:

- GNSS outage/dead-reckoning lifecycle.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.168.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent timing/fusion references, rollover and clock faults, delayed/out-of-sequence data, holdover growth, outage replay, and sensor comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.168.0 implementation stop reached. Run pentest for this exact commit.`

### v0.169.0 - Multi-antenna attitude

Status: planned.

Goal: deliver multi-antenna attitude as one bounded,
reviewable release in Phase L (Timing and fusion).

Deliverables:

- multi-antenna attitude.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.169.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform independent timing/fusion references, rollover and clock faults, delayed/out-of-sequence data, holdover growth, outage replay, and sensor comparisons;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.169.0 implementation stop reached. Run pentest for this exact commit.`

## Phase M: Hardware, OS and assistance

### v0.170.0 - Recorded-I/Q and virtual SDR source

Status: planned.

Goal: deliver recorded-I/Q and virtual SDR source as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- recorded-I/Q and virtual SDR source.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.170.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.170.0 implementation stop reached. Run pentest for this exact commit.`

### v0.171.0 - Linux RTL2832U/E4000 reference backend

Status: planned.

Goal: deliver linux RTL2832U/E4000 reference backend as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- Linux RTL2832U/E4000 reference backend.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.171.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.171.0 implementation stop reached. Run pentest for this exact commit.`

### v0.172.0 - BladeRF adapter

Status: planned.

Goal: deliver bladeRF adapter as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- bladeRF adapter.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.172.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.172.0 implementation stop reached. Run pentest for this exact commit.`

### v0.173.0 - USRP/UHD adapter

Status: planned.

Goal: deliver uSRP/UHD adapter as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- USRP/UHD adapter.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.173.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.173.0 implementation stop reached. Run pentest for this exact commit.`

### v0.174.0 - LimeSDR adapter

Status: planned.

Goal: deliver limeSDR adapter as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- LimeSDR adapter.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.174.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.174.0 implementation stop reached. Run pentest for this exact commit.`

### v0.175.0 - Coherent multi-device clock/timestamp calibration

Status: planned.

Goal: deliver coherent multi-device clock/timestamp calibration as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- coherent multi-device clock/timestamp calibration.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.175.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.175.0 implementation stop reached. Run pentest for this exact commit.`

### v0.176.0 - Portable serial backend

Status: planned.

Goal: deliver portable serial backend as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- portable serial backend.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.176.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.176.0 implementation stop reached. Run pentest for this exact commit.`

### v0.177.0 - Native USB backend contracts and Linux implementation

Status: planned.

Goal: deliver native USB backend contracts and Linux implementation as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- native USB backend contracts and Linux implementation.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.177.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.177.0 implementation stop reached. Run pentest for this exact commit.`

### v0.178.0 - Windows WinUSB/COM/location implementation

Status: planned.

Goal: deliver windows WinUSB/COM/location implementation as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- Windows WinUSB/COM/location implementation.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.178.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.178.0 implementation stop reached. Run pentest for this exact commit.`

### v0.179.0 - MacOS IOKit/serial/Core Location implementation

Status: planned.

Goal: deliver macOS IOKit/serial/Core Location implementation as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- macOS IOKit/serial/Core Location implementation.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.179.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.179.0 implementation stop reached. Run pentest for this exact commit.`

### v0.180.0 - FreeBSD/OpenBSD/NetBSD I/O and PPS implementation

Status: planned.

Goal: deliver freeBSD/OpenBSD/NetBSD I/O and PPS implementation as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- FreeBSD/OpenBSD/NetBSD I/O and PPS implementation.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.180.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.180.0 implementation stop reached. Run pentest for this exact commit.`

### v0.181.0 - Gpsd protocol adapter

Status: planned.

Goal: deliver gpsd protocol adapter as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- gpsd protocol adapter.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.181.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.181.0 implementation stop reached. Run pentest for this exact commit.`

### v0.182.0 - U-blox UBX adapter

Status: planned.

Goal: deliver u-blox UBX adapter as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- u-blox UBX adapter.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.182.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.182.0 implementation stop reached. Run pentest for this exact commit.`

### v0.183.0 - Septentrio SBF adapter

Status: planned.

Goal: deliver septentrio SBF adapter as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- Septentrio SBF adapter.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.183.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.183.0 implementation stop reached. Run pentest for this exact commit.`

### v0.184.0 - NovAtel/public receiver adapter baseline

Status: planned.

Goal: deliver novAtel/public receiver adapter baseline as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- NovAtel/public receiver adapter baseline.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.184.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.184.0 implementation stop reached. Run pentest for this exact commit.`

### v0.185.0 - Additional stable public receiver protocols

Status: planned.

Goal: deliver additional stable public receiver protocols as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- additional stable public receiver protocols.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.185.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.185.0 implementation stop reached. Run pentest for this exact commit.`

### v0.186.0 - Android raw GNSS measurement adapter

Status: planned.

Goal: deliver android raw GNSS measurement adapter as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- Android raw GNSS measurement adapter.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.186.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.186.0 implementation stop reached. Run pentest for this exact commit.`

### v0.187.0 - OMA SUPL/ULP core

Status: planned.

Goal: deliver oMA SUPL/ULP core as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- OMA SUPL/ULP core.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.187.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.187.0 implementation stop reached. Run pentest for this exact commit.`

### v0.188.0 - 3GPP LPP assistance core

Status: planned.

Goal: deliver 3GPP LPP assistance core as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- 3GPP LPP assistance core.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.188.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.188.0 implementation stop reached. Run pentest for this exact commit.`

### v0.189.0 - Rustls network adapter and secure credential policy

Status: planned.

Goal: deliver rustls network adapter and secure credential policy as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- Rustls network adapter and secure credential policy.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.189.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.189.0 implementation stop reached. Run pentest for this exact commit.`

### v0.190.0 - NMEA 2000 transport/legal PGN baseline

Status: planned.

Goal: deliver nMEA 2000 transport/legal PGN baseline as one bounded,
reviewable release in Phase M (Hardware, OS and assistance).

Deliverables:

- NMEA 2000 transport/legal PGN baseline.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.190.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform target builds, device/OS fault injection, permission and disconnect handling, bounded probes, transport security, and platform/hardware smoke evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.190.0 implementation stop reached. Run pentest for this exact commit.`

## Phase N: Simulation, hardening and 1.0 stabilization

### v0.191.0 - Synthetic navigation-message generators

Status: planned.

Goal: deliver synthetic navigation-message generators as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- synthetic navigation-message generators.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.191.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.191.0 implementation stop reached. Run pentest for this exact commit.`

### v0.192.0 - Scalar baseband signal generator for all implemented open signals

Status: planned.

Goal: deliver scalar baseband signal generator for all implemented open signals as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- scalar baseband signal generator for all implemented open signals.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.192.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.192.0 implementation stop reached. Run pentest for this exact commit.`

### v0.193.0 - Dynamics, atmosphere, multipath and clock scenario engine

Status: planned.

Goal: deliver dynamics, atmosphere, multipath and clock scenario engine as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- dynamics, atmosphere, multipath and clock scenario engine.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.193.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.193.0 implementation stop reached. Run pentest for this exact commit.`

### v0.194.0 - Controlled interference/jamming scenario generation

Status: planned.

Goal: deliver controlled interference/jamming scenario generation as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- controlled interference/jamming scenario generation.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.194.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.194.0 implementation stop reached. Run pentest for this exact commit.`

### v0.195.0 - Controlled spoofing/meaconing scenario generation

Status: planned.

Goal: deliver controlled spoofing/meaconing scenario generation as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- controlled spoofing/meaconing scenario generation.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.195.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.195.0 implementation stop reached. Run pentest for this exact commit.`

### v0.196.0 - Cross-constellation full replay suite

Status: planned.

Goal: deliver cross-constellation full replay suite as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- cross-constellation full replay suite.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.196.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.196.0 implementation stop reached. Run pentest for this exact commit.`

### v0.197.0 - Long-duration resource-leak and rollover suite

Status: planned.

Goal: deliver long-duration resource-leak and rollover suite as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- long-duration resource-leak and rollover suite.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.197.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.197.0 implementation stop reached. Run pentest for this exact commit.`

### v0.198.0 - Full parser fuzz corpus and coverage audit

Status: planned.

Goal: deliver full parser fuzz corpus and coverage audit as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- full parser fuzz corpus and coverage audit.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.198.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.198.0 implementation stop reached. Run pentest for this exact commit.`

### v0.199.0 - Numerical condition/precision audit

Status: planned.

Goal: deliver numerical condition/precision audit as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- numerical condition/precision audit.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.199.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.199.0 implementation stop reached. Run pentest for this exact commit.`

### v0.200.0 - Unsafe/FFI audit and device fault injection

Status: planned.

Goal: deliver unsafe/FFI audit and device fault injection as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- unsafe/FFI audit and device fault injection.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.200.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.200.0 implementation stop reached. Run pentest for this exact commit.`

### v0.201.0 - Portable SIMD performance release

Status: planned.

Goal: deliver portable SIMD performance release as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- portable SIMD performance release.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.201.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.201.0 implementation stop reached. Run pentest for this exact commit.`

### v0.202.0 - Fixed-point/embedded performance release

Status: planned.

Goal: deliver fixed-point/embedded performance release as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- fixed-point/embedded performance release.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.202.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.202.0 implementation stop reached. Run pentest for this exact commit.`

### v0.203.0 - WASM decoding/post-processing profile

Status: planned.

Goal: deliver wASM decoding/post-processing profile as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- WASM decoding/post-processing profile.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.203.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.203.0 implementation stop reached. Run pentest for this exact commit.`

### v0.204.0 - API naming and visibility freeze

Status: planned.

Goal: deliver aPI naming and visibility freeze as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- API naming and visibility freeze.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.204.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.204.0 implementation stop reached. Run pentest for this exact commit.`

### v0.205.0 - Configuration/profile freeze

Status: planned.

Goal: deliver configuration/profile freeze as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- configuration/profile freeze.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.205.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.205.0 implementation stop reached. Run pentest for this exact commit.`

### v0.206.0 - File/wire round-trip compatibility freeze

Status: planned.

Goal: deliver file/wire round-trip compatibility freeze as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- file/wire round-trip compatibility freeze.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.206.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.206.0 implementation stop reached. Run pentest for this exact commit.`

### v0.207.0 - All-platform CI and hardware farm release

Status: planned.

Goal: deliver all-platform CI and hardware farm release as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- all-platform CI and hardware farm release.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.207.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.207.0 implementation stop reached. Run pentest for this exact commit.`

### v0.208.0 - Independent receiver comparison campaign

Status: planned.

Goal: deliver independent receiver comparison campaign as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- independent receiver comparison campaign.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.208.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.208.0 implementation stop reached. Run pentest for this exact commit.`

### v0.209.0 - Multi-band live-sky and simulator evidence release

Status: planned.

Goal: deliver multi-band live-sky and simulator evidence release as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- multi-band live-sky and simulator evidence release.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.209.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.209.0 implementation stop reached. Run pentest for this exact commit.`

### v0.210.0 - Standards inventory refresh and 1.0 baseline freeze

Status: planned.

Goal: deliver standards inventory refresh and 1.0 baseline freeze as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- standards inventory refresh and 1.0 baseline freeze.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.210.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.210.0 implementation stop reached. Run pentest for this exact commit.`

### v0.211.0 - Complete public-signal coverage audit

Status: planned.

Goal: deliver complete public-signal coverage audit as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- complete public-signal coverage audit.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.211.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.211.0 implementation stop reached. Run pentest for this exact commit.`

### v0.212.0 - Complete correction/format/assistance coverage audit

Status: planned.

Goal: deliver complete correction/format/assistance coverage audit as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- complete correction/format/assistance coverage audit.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.212.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.212.0 implementation stop reached. Run pentest for this exact commit.`

### v0.213.0 - Complete security/integrity/timing audit

Status: planned.

Goal: deliver complete security/integrity/timing audit as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- complete security/integrity/timing audit.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.213.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.213.0 implementation stop reached. Run pentest for this exact commit.`

### v0.214.0 - Documentation, examples and migration audit

Status: planned.

Goal: deliver documentation, examples and migration audit as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- documentation, examples and migration audit.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.214.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.214.0 implementation stop reached. Run pentest for this exact commit.`

### v0.215.0 - External security audit fixes

Status: planned.

Goal: deliver external security audit fixes as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- external security audit fixes.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.215.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.215.0 implementation stop reached. Run pentest for this exact commit.`

### v0.216.0 - External GNSS/domain review fixes

Status: planned.

Goal: deliver external GNSS/domain review fixes as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- external GNSS/domain review fixes.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.216.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.216.0 implementation stop reached. Run pentest for this exact commit.`

### v0.217.0 - First complete production-candidate evidence rehearsal

Status: planned.

Goal: deliver first complete production-candidate evidence rehearsal as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- first complete production-candidate evidence rehearsal.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.217.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.217.0 implementation stop reached. Run pentest for this exact commit.`

### v0.218.0 - Second production-candidate rehearsal with blocker-only fixes

Status: planned.

Goal: deliver second production-candidate rehearsal with blocker-only fixes as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- second production-candidate rehearsal with blocker-only fixes.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.218.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.218.0 implementation stop reached. Run pentest for this exact commit.`

### v0.219.0 - Final reproducibility, packaging and provenance rehearsal

Status: planned.

Goal: deliver final reproducibility, packaging and provenance rehearsal as one bounded,
reviewable release in Phase N (Simulation, hardening and 1.0 stabilization).

Deliverables:

- final reproducibility, packaging and provenance rehearsal.
- Add or update only the focused crates and modules required by this outcome;
  preserve `no_std`, allocation, dependency, unsafe, and GitHub-only
  boundaries.
- Update standards mappings, capability/coverage status, security analysis,
  public documentation, migration notes, and `RELEASE_NOTES_0.219.0.md`.
- Add failure-state and resource-limit behavior; do not imply any adjacent
  planned capability is complete.

Verification:

- run the repository-wide format, lint, test, docs, package, dependency,
  advisory, SBOM, MSRV, and applicable platform gates;
- perform cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence;
- add at least one negative or adversarial regression for every new untrusted
  boundary and confirm no input can panic or partially commit state;
- review changed code, standards provenance, claims, resource bounds, and
  dependency/tool currency before the pentest handoff.

Exit criteria:

- the stated deliverable is implemented, independently testable, documented,
  mapped to evidence, and contains no hidden degradation or unsupported claim;
- all release-specific and repository-wide gates pass with no unresolved
  critical/high finding and known limitations are explicit;
- `v0.219.0 implementation stop reached. Run pentest for this exact commit.`

## Production Candidate

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

### v1.0.0 - Serious production release

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
