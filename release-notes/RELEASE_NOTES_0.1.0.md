# Navheim 0.1.0 Release Notes

Status: implementation candidate; not tagged or published.

## Scope

This release initializes the security-first Navheim workspace. It provides the
dependency-free `navheim-core` crate, the dependency-free `navheim` facade, the
standards inventory policy, repository security controls, cross-version Rust
policy, CI, documentation, and audited publication tooling.

The architecture now defines a stable direction for timing integration:
Navheim will own GNSS time decoding, resolution, PPS/time-mark meaning,
uncertainty, health, authentication, integrity, and provenance. Downstream
clock frameworks may consume that API, but Navheim will not depend on them or
perform generic clock discipline and holdover.

The implementation and release plans also incorporate the initial
architecture/security gap review without replacing Navheim's broader roadmap.
They add explicit future stops for immutable artifacts and assessments, safe
bounded storage, executable preflight receipts, deterministic DSP, correction
anti-mixing, privacy/unsafe/platform evidence, strict release provenance, and
exact standards traceability.

The standards foundation now includes 25 exact, immutable RFC Editor
references for Navheim's HTTP, encoding, certificate, JSON and TLS boundaries,
plus a live-checked errata drift snapshot. Legacy NTRIP HTTP references are
explicitly separated from current secure behavior.

RFC integrity is enforced through exact source lists and SHA-256 bytes. Git
does not preserve general read-only permission bits, so CI does not require
mode `0444`; developers may still apply the optional local read-only guard.

The broader acquisition inventory covers 36 authoritative source families.
Seventeen freely downloadable GPS, Galileo, NavIC and IGS documents can be
fetched into an ignored local vault and protected by a local SHA-256 lock.
Paid, licensed, consent-gated, registration-gated and vendor-profile material
is metadata-tracked but must be acquired lawfully and remains outside Git and
crate archives.

A second coverage pass preserves that sequence while closing promised-scope
gaps with named releases for the navigation crate; RTCM, RINEX and
Earth-orientation products; typed PVT/orthometric outputs; SDR conditioning;
full inertial/fusion calibration and vector tracking; canonical assistance;
implementable RAIM/ARAIM contracts; a concrete RustCrypto adapter; CAN I/O;
independent signal vectors; and exact timing arithmetic, mapping and slot
state machines.

The third coverage pass resolves acknowledgement and CAN address-claim
ownership contradictions and makes the stable-Rust numerical strategy
explicit. It adds future stops for first-party deterministic `no_std` math,
bounded extension registration, all facade profiles, DGPS and ordered
degradation, solver/integrity separation, platform-complete Android support,
isolated discovery probes, bounded ASN.1 PER, exact SUPL/LPP matrices and
post-protocol RustCrypto integration.

The fourth coverage pass keeps all earlier work and adds 14 bounded releases
for a crate/capability DAG, honest resource-evidence categories, projected
coordinates, typed kinematics, safe processing extensions, conditional NavIC
messaging, complete DFMC/network-RTK/PPP matrices, optional GNSS science,
fixed-rate fusion, calibrated native AoA, SouthPAN coverage, and full
FPGA/GPU/external-DSP stage equivalence.

The fifth coverage pass adds five foundation releases without replacing later
solver or assistance work: bounded first-party linear algebra, conservative
statistical kernels, canonical signal definitions, deterministic
navigation/correction/product selection, and early acquisition hints.
Artifact-ID lifecycle stays in its existing owning milestone, while late
SUPL/LPP/mobile/receiver assistance translates into the early hint contract.

The sixth coverage pass corrects the linalg and signal-registry dependency
directions, then adds 11 bounded releases for UTC civil and precision-geodesy
time, runtime acquisition-decision receipts, deterministic multicore and
source supervision, capability-gated receiver control, and an opt-in snapshot
envelope with separate acquisition, tracking/navigation-store, PPP and fusion
restore profiles.

The seventh coverage pass corrects DSP/geo/executor dependency authority,
distinguishes snapshot corruption detection from authenticated sealing,
defines role-aware source composition, narrows parallel determinism to logical
ordering plus captured runtime traces, moves executable acquisition receipts
and snapshots after their state exists, separates raw and semantic store
restore, and adds receiver-configuration generation barriers.

The eighth coverage pass preserves those boundaries while making them
implementation-safe: `navheim-geo` exclusively owns coordinate mathematics
and `navheim-navigation` composes it; executor work units have scoped,
non-overlapping ownership and lossless bounded traces; snapshot authenticity,
confidentiality and privacy policy are orthogonal; same-role handover
invalidates dependent solver state unless an evidenced transform preserves it;
and receiver transactions are distinct from independently observed
configuration assessments. Two bounded stops add behavioral receiver
assessment and optional external AEAD/platform-keystore snapshot protection.

The ninth coverage pass removes direct SDR hardware mutation in favor of
side-effect-free preparation, reviewed immutable application plans,
configuration generations, transition invalidation and initialized-count
reads. Executor deadlines now distinguish requested/acknowledged cancellation,
deadline misses, unresponsive ownership and failures without pretending Rust
can kill a stuck borrowed thread. Snapshot protection gains authenticated
interpretive metadata, crash-safe nonce/counter/key rotation and four separate
platform adapter stops. Receiver assessments become interval-scoped
`ObservedConsistent`, while local-frame transformations remain exclusively in
`navheim-geo`.

A repository-wide requirements pass then checked every tracked artifact class,
corrected the copied MIT donor identity, widened the source-size and
documentation-link gates to the whole applicable repository, and assigned
previously aggregate promises to bounded releases. Those stops now cover
CGGTTS common-view/all-in-view timing, exact SBAS providers, conditional
BeiDou messaging, FPGA/external-DSP inputs, generic and conditional receiver
families, all named GitHub-only tools, external evidence data, deployment
artifacts, and final requirement/claim traceability.

The standards acquisition catalog now also names the missing primary-source
families for BIPM/CCTF/ITU-R time transfer, Rust contracts, SDR/FPGA stacks,
Linux/BSD, Microsoft and Apple platform I/O, NovAtel, and conditional receiver
protocols. Their bytes remain local-only and exact profiles must be frozen
before implementation.

Behavioral implementation is now governed by a fail-closed evidence policy.
Exact authoritative revisions, amendments, errata and sections are reviewed
before code; implementation and test mappings are mandatory; applicable
positive, negative, boundary, malformed, adversarial, conformance,
differential, resource, fuzz, platform and regression tests ship in the same
milestone. Missing or ambiguous evidence stops implementation rather than
being guessed.

## Security

- Both published crates are `no_std`, dependency-free, and forbid unsafe code.
- Unknown registries, unknown Git sources, wildcard dependencies, yanked
  releases, and unreviewed advisory classes are denied.
- Release tagging requires exact-commit pentest evidence and a matching SBOM.
- GitHub CodeQL default setup is expected; no advanced CodeQL workflow is
  committed.

## Compatibility

- MSRV: Rust `1.90.0`.
- Pinned stable release toolchain: Rust `1.97.1`.
- Intended operating-system scope: Linux, Windows, macOS, FreeBSD, OpenBSD,
  NetBSD, Android, iOS, WASM, bare metal, and future Aesynx adapters.

## Non-Claims

This release does not decode signals or files, process RF, solve position or
time, access devices, use networking, or provide production GNSS/PNT behavior.
