# Navheim Implementation Plan

Status: planning document

Crate name: `navheim`

1.0 target: a serious, security-first, independently tested Rust GNSS/PNT
platform supporting every publicly documented, legally implementable civil/open
signal and service in the frozen 1.0 standards baseline.

## Core Position

Navheim is not a GPS-only parser, an SDR demonstration, or a receiver SDK
wrapper. It is one layered platform whose canonical observation and time model
can be fed by RF samples, FPGA/DSP outputs, raw receiver measurements, decoded
messages, corrections, OS location providers, or archived data.

The facade must remain simple without hiding allocation, device access,
networking, degraded capability, authentication state, integrity state,
uncertainty, or provenance.

## Non-Negotiable Engineering Rules

- Publishable crates use edition 2024, resolver 3, MSRV Rust `1.90.0`, and
  remain compatible through pinned stable Rust `1.97.1`.
- Repository-only tools may require Rust `1.97.1`.
- The pinned stable toolchain, cargo security tools, dependencies, and GitHub
  Actions are checked for current versions before releases and dependency
  changes.
- Foundational, constellation, signal, solver, integrity, and format behavior
  is first-party and must not depend on another GNSS implementation.
- Navheim owns GNSS-derived time behavior and exposes it through its own
  dependency-free API. It never depends on Mundilfari or another generic clock
  framework; consumer-owned companion crates depend on Navheim.
- TLS and modern cryptographic primitives use reviewed adapter crates; Navheim
  does not implement them from scratch.
- Foundation and protocol crates are `no_std` by default and expose allocation
  only through explicit features.
- No core crate starts threads, selects an async runtime, opens devices, or
  uses networking.
- Side-effecting builders must first return an immutable reviewed plan receipt;
  device, credential, network and thread authority begins only after acceptance.
- Raw facts, normalized facts, corrections, assessments, evidence and policy
  decisions are immutable, separately typed and connected by bounded artifact
  identifiers. Later evidence never mutates an earlier fact.
- Protocol, constellation, solver, and format crates forbid unsafe code.
- Unsafe is isolated to reviewed FFI, DMA, or SIMD/platform modules with a
  safety contract, Miri evidence where applicable, and independent review.
- Hand-maintained code files must stay at or below 500 lines.
- Generated code records generator provenance and reproducibility; review also
  limits function/state-machine complexity rather than relying on file length.
- Every input length, offset, epoch, capacity, and resource calculation is
  checked.
- No input-dependent panic is permitted under declared resource limits.
- Untrusted input cannot select allocations, thread/channel counts, FFT plans,
  FEC iterations, candidate counts, queue growth or other work bounds.
- Every untrusted parser is bounded and receives unit, negative, property,
  conformance, and fuzz coverage.
- Standards constants cite authoritative sections or tables.
- Every implemented feature maps to `standards/manifest.toml`.
- Every release ends at an exact-commit pentest handoff before tagging.

## Capability Tiers

| Tier | Contract |
| --- | --- |
| 0 | `core` only, no heap, OS, hidden floating-point requirement, or unsafe code |
| 1 | explicit `alloc`, still no OS |
| 2 | explicit `std` for files, sockets, threads, serial, USB, and clocks |
| 3 | external integrations such as TLS, cryptography, platform APIs, and vendor stacks |

Each crate documents its default tier, optional promotions, exact structural
resource needs, target/toolchain/profile-specific stack evidence, measured
envelopes, caller assumptions, unavailable estimates, and floating-point
assumptions.
Enabling `std` must not change protocol/wire behavior. Tier 0 uses caller
buffers, explicit work budgets and allocator-free target evidence. Tier 1
documents every allocation point. Tier 2 documents threads, clocks, devices,
files, sockets, cancellation and authority. Tier 3 documents dependencies,
unsafe code, credentials, trust roots and platform guarantees.

A checked machine-readable crate/capability DAG records normal, optional,
build and development edges; feature unification; tier; `alloc`/`std`; unsafe;
TLS; cryptography; publication; and platform scope. CI rejects cycles,
undeclared edges and silent privilege or tier escalation.

## Crate Architecture

### Facade and foundation

- `navheim`: profiles, prelude, stable re-exports, source/solver composition,
  and capability planning.
- `navheim-core`: bounded collections, units, time, coordinates, identifiers,
  bit/FEC/checksum primitives, observations, ephemerides, corrections, events,
  errors, provenance, resource planning, and stable traits.
- `navheim-math`: dependency-free `no_std` deterministic elementary floating
  math, admitted conservative statistical kernels and narrowly scoped backend
  capabilities.
- `navheim-linalg`: dependency-free `no_std` bounded fixed-capacity and
  caller-scratch linear algebra with narrow solver-facing APIs.
- `navheim-dsp`: complex/fixed-point values, filters, resampling, FFT,
  acquisition, tracking, synchronization, and estimators.
- `navheim-sdr`: front-end traits, sample metadata, coherent arrays, band
  planning, deployment validation, and device adapter boundaries.

### Constellations and augmentation

- `navheim-gps`
- `navheim-galileo`
- `navheim-glonass`
- `navheim-beidou`
- `navheim-qzss`
- `navheim-navic`
- `navheim-sbas`

Each constellation crate owns code generation, acquisition hints, tracking
configuration, FEC/framing, raw and semantic message models, ephemeris
conversion, signal corrections, and relevant conformance vectors. One crate
per signal is explicitly rejected to avoid version and dependency
fragmentation.

### Solving and application primitives

- `navheim-pvt`: typed solution, DOP, age, contributing/excluded satellite,
  residual, convergence, vertical-datum and availability outputs.
- `navheim-rtk`
- `navheim-ppp`
- `navheim-integrity`: implementable RAIM/ARAIM hypotheses, risk allocation,
  alert/continuity/availability, protection-level and exclusion contracts.
- `navheim-fusion`: calibrated IMU models, mechanization, bounded real-time
  filters, optional allocated factor graph and observable reacquisition.
- `navheim-timing`: GNSS time resolution, time-only solutions, receiver clock
  estimates, time transfer, external PPS/time-mark semantic correlation,
  10 MHz/frequency-output status, calibrated delay, uncertainty, health,
  authentication, integrity, and adapter-facing events.
- `navheim-security`
- `navheim-navigation`: geodesic/rhumb calculations, bounded
  waypoint/route/track models, geofences and local-frame navigation; it does
  not claim road-network routing.
- `navheim-science`: optional calibrated scintillation, reflectometry,
  space-weather and remote-sensing artifacts with explicit product maturity.

Authentication, signal authenticity, message correctness, and solution
integrity remain separate types and policies.

`navheim-timing` does not implement generic PPS device capture, NTP/PTP,
cross-family clock consensus, local oscillator discipline, generic holdover,
or privileged clock adjustment. Those belong to consumers such as Mundilfari.

### Formats and interoperability

- `navheim-nmea`
- `navheim-nmea2000`: protocol/PGN semantics separated from CAN frame I/O.
- `navheim-rtcm`: frozen legacy and modern observation, ephemeris,
  correction, transformation and projection profiles.
- `navheim-ntrip`
- `navheim-rinex`: observation, navigation, meteorological and clock profiles
  with separately bounded compact/Hatanaka integration.
- `navheim-products`: precise products plus Earth-orientation/reference-frame
  inputs.
- `navheim-receiver`
- `navheim-assist`: canonical trust/freshness/session model before SUPL, LPP,
  Android or receiver translations.
- `navheim-io`

### External adapters

- `navheim-tls-rustls`
- `navheim-crypto-rustcrypto`
- `navheim-uhd`
- `navheim-bladerf`
- `navheim-lime`
- `navheim-android`

These crates are optional and may carry reviewed external dependencies. They
must not redefine canonical GNSS behavior.

`navheim-crypto-rustcrypto` is the reviewed concrete conformance backend for
end-to-end OSNMA/QZNMA testing. Cryptographic policy and protocol behavior
remain in first-party canonical crates.

### GitHub-only tools

CLI, daemons, caster/station/survey services, inspectors, viewers, labs,
simulation, conformance, benchmarks, fuzz targets, capture tooling, FPGA
artifacts, packaging, service units, and deployments remain under `tools/`,
`fuzz/`, or other repository-only paths until separately admitted. They set
`publish = false` and may use Rust `1.97.1`.

Their named implementation stops are v0.36.3 (`navheim-capture`), v0.175.1
(`navheim-fpga`), v0.190.3-v0.190.11 (tool foundation, CLI, daemon,
caster/station/survey, inspector/viewer and lab), v0.196.1-v0.196.2
(`navheim-sim` and external data), v0.198.2-v0.198.3 (fuzz and conformance),
v0.201.1 (benchmarks), and v0.219.1 (packaging/deployment). A tool may reuse
published crates; it may not introduce a parallel GNSS implementation or
bypass canonical validation, evidence, privacy, or policy.

## Canonical Model Order

Implementation proceeds in this dependency order:

1. bounded collections, errors, and checked arithmetic;
2. physical units, exact integer time, deterministic `no_std` math, bounded
   linear algebra and admitted conservative statistical kernels;
3. coordinates and reference frames;
4. bit, checksum, parity, and FEC primitives;
5. extensible identifiers, canonical signal definitions and registries;
6. observations, ephemerides, corrections, provenance, and events;
7. capabilities, resource plans, and deterministic source/sink polling;
8. formats and deterministic replay;
9. scalar native DSP, dependency-free acquisition hints and timestamp
   correctness;
10. independent signal/message vector admission, then GPS L1 C/A end-to-end
    as the first observable-to-fix path;
11. remaining GPS and constellations;
12. multi-GNSS solution quality, RTK, PPP, integrity, and authentication;
13. complete the stable GNSS timing observation/event API, then fusion,
    navigation, hardware, OS, canonical assistance, and NMEA 2000;
14. optional calibrated science outputs and accelerator integrations only
    after their canonical observations, resource evidence and scalar paths;
15. simulation, fuzzing, audits, conformance, standards freeze, and release
    candidates.

RTK, PPP, and authentication do not become trusted surfaces until observation
time/phase correctness is independently proven.

## Canonical Artifact and Assessment Pipeline

The public type graph follows this non-destructive order:

```text
ingress and capture facts
  -> tracking estimates or raw protocol records
  -> raw observations and raw navigation messages
  -> validated messages and normalized observations
  -> corrected epochs and transactional navigation state
  -> solver input epochs
  -> position/time/attitude solution artifacts
       + targeted correctness assessments
       + navigation-authentication assessments
       + signal-authenticity evidence
       + integrity assessments
       + versioned policy decisions
```

Every derived value has an immutable artifact ID, bounded parent IDs and
derivation algorithm/version. Authentication, signal-source authenticity,
message correctness and solution integrity never collapse into one boolean.
Delayed authentication creates a new assessment targeting the original
artifact. No-fix/unavailable, convergence, rollback, withdrawal and coasting
are explicit events or lifecycle artifacts rather than valid solution modes.

Artifact/provenance IDs contain source namespace, reset generation and a
non-wrapping local sequence with explicit exhaustion/renewal. Reset never
reuses identity. Import/replay remaps untrusted namespaces while preserving
parents; identity is distinct from an optional content digest. Canonical
serialization, duplicate/collision handling and privacy-safe formatting are
part of the lifecycle contract.

Observation stages are separately typed: `TrackingEstimate`,
`RawReceiverObservation`, `RawSdrObservation`, normalized `Observation`,
`CorrectedObservation`, `ObservationEpoch` and `SolverInputEpoch`. Correction
ledgers and navigation-store transactions preserve issue, provider, station,
frame, session, generation, validity, uncertainty and provenance.
Constellation crates provide the canonical versioned signal definitions;
format crates translate through them instead of duplicating frequency,
wavelength, rate, component, modulation, native-time or identifier tables.
Navigation models, corrections and products are selected through explicit
epoch/applicability queries returning considered-candidate evidence and
`Selected`, `Ambiguous`, `Unavailable` or `Rejected`, never ambient latest-wins.

## Resource, Progress, and Numerical Contracts

Tier 0 uses a small caller-driven vocabulary: bounded `Push`, `Poll`,
`Transform`, `Plan` and `Reset` contracts, with snapshot/restore only when the
state format is explicitly versioned. Parsers report consumed length and
either make progress or request more input. Large events use borrowed views or
caller-provided bounded slots.

Every execution pipeline is created from a checked immutable `PlanReceipt`.
Each field is classified as an exact structural amount, a
target/toolchain/profile-specific static upper bound, a deterministic work
bound, a measured envelope, a caller assumption, or an unavailable estimate.
Portable plans never overstate stack, throughput, or latency certainty. Each
input block is checked against the applicable receipt bounds.
Invalidation and security events have sequence, source generation, target
artifact, effective interval and mandatory-withdrawal semantics. Queue
pressure cannot silently discard them: the source stops, explicitly coalesces,
or requires resynchronization.

Because canonical crates forbid unsafe code, bounded collections use an honest
safe representation such as initialized storage, `[Option<T>; N]`,
caller-owned slices or domain-specific arrays. The API documents representation
cost and does not promise a zero-overhead general `FixedVec` that its safety
policy cannot implement.

Tier 0 interchange values use exact scaled integers or reduced rationals.
Floating APIs reject non-finite values. Each numerical algorithm names its
backend, rounding/overflow behavior, state ordering and units, rank/condition
tests, convergence, tolerance and failure behavior. Fixed-point kernels define
bit-exact replay; floating kernels define numerical replay with explicit FMA,
denormal and platform policy. Optimized kernels are compared against the
normative scalar implementation. A broad public `Scalar` abstraction is not
stabilized before concrete algorithms prove the required operations.

`navheim-math` is the normative pure-Rust scalar source for `sqrt`/`hypot`,
trigonometry, `atan2`, logarithm/exponential and admitted derived functions.
It specifies domains, exceptional values, subnormals, argument reduction,
rounding and error bounds against high-precision references. Runtime
twiddles/coefficients are planned into caller storage; audited fixed tables are
versioned evidence. Platform math and target-specific `core::arch` paths are
optional reviewed backends with scalar equivalence. Nightly
`core::simd`/`std::simd`, OS `libm` assumptions and post-MSRV APIs are forbidden
from the baseline.

`navheim-linalg` admits only bounded solver-required storage, QR,
Cholesky/LDLT, triangular solves, rank updates/downdates, square-root updates
and rank/condition estimates. It rejects dimension/scratch overflow, aliasing,
singular, indefinite, non-finite and badly scaled cases explicitly. Production
least squares cannot silently use unqualified normal-equation inversion.

Statistical kernels are limited to admitted normal and chi-square
tails/CDFs/quantiles with explicit confidence/degrees-of-freedom domains,
log-probability paths, monotonicity and approximation bounds. Integrity and
protection thresholds round conservatively, so approximation error cannot
understate risk or make acceptance more permissive.

An early dependency-free `SearchAid`/`AcquisitionHint` carries bounded,
expiring approximate time/location/velocity/orbit and Doppler windows with
source, generation, uncertainty and trust class. Plan receipts record every
search reduction; poisoned/conflicting hints fall back to bounded blind
search. Late assistance protocols translate into this artifact and never use
it to resolve canonical time, position or trust.

Format profiles are not aggregate claims. RTCM legacy observations and
surveying transforms/projections, each RINEX observation/navigation/
meteorological/clock generation, RINEX 4 picosecond fields, compact codecs and
Earth-orientation products have separate versioned stops. Decompression
receipts bound bytes, records, lines and expansion ratio before decoded data
enters an ordinary parser.

PVT exposes DOP families, solution age, contributing/excluded satellites,
fix/convergence taxonomy, residuals and exclusions as typed results.
Orthometric height requires an identified geoid/vertical-datum artifact and
cannot be confused with ellipsoidal height. The sequential GNSS-only estimator
is independent from multi-sensor fusion and has explicit initialization,
convergence, reset and unavailable states.

Native front-end conditioning validates encoding, byte/IQ order, scaling,
clipping, quantization, calibration and AGC state before DC/IQ correction or
bounded mitigation. Every blanking/notching action creates distortion
evidence. SIMD is prohibited until its alignment, aliasing, feature-detection,
fallback and unsafe contract is independently reviewed.

RAIM/ARAIM contracts name fault hypotheses, integrity-risk allocation, alert
limits, time-to-alert, continuity, availability, correlation assumptions,
solution separation, exclusion exhaustion and re-admission. Missing required
inputs produce unavailable protection levels. SBAS evidence stays a separate
targeted input.

The PVT solver emits solution, residual and exclusion facts under measurement
admission policy. A separate integrity assessor consumes those immutable
artifacts and emits targeted assessments; solver configuration never makes an
ordinary solution integrity-approved. Code DGPS is a distinct typed solution
and cannot be inferred from RTK-float state.

Profiles expand to versioned printable canonical configuration and fail on
missing capability. Discovery enumerates bounded candidates, isolates probes,
ranks deterministically with explanations and never opens devices. Assistance
is canonical before Android/SUPL/LPP translation; PER parsing has independent
bit/work/nesting receipts. NMEA 2000 owns pure address-claim decisions while
platform I/O only executes frames and lifecycle actions.

## GNSS Timing and Consumer APIs

Navheim owns every step required to determine time from GNSS: native system
times, transmitted UTC/leap models, rollover resolution, satellite and
receiver clock corrections, receiver protocols, time-only solutions,
PPS/time-mark and frequency-output meaning, delay calibration, uncertainty,
health, authentication, integrity, and provenance.

Navheim exposes dependency-free `no_std` timing types and a deterministic
`GnssTimingSource`-style event boundary. Events include observations, model
changes, ambiguity, gaps, discontinuities, invalidations, and security
transitions. A valid sample can therefore be withdrawn without a consumer
having to reinterpret GNSS protocols.

Generic clock behavior stays outside Navheim: physical PPS capture, NTP/NTS,
PTP, clock-family consensus, system/PHC adjustment, oscillator servos, and
holdover after GNSS evidence expires. A consumer-owned companion crate, such
as `mundilfari-navheim`, may depend on Navheim and map its exact timing evidence
into the consumer's clock types. Navheim never depends on that adapter or
consumer.

One consumer adapter covers every constellation exposed by Navheim. Consumers
must not recreate separate GPS, Galileo, GLONASS, BeiDou, QZSS, or NavIC time
decoders around the same clock framework.

The normative architectural contract, provisional type shapes, correlation
model, security invariants, and adapter verification requirements are in
[GNSS_TIMING_API.md](GNSS_TIMING_API.md).

## Standards Discipline

`standards/sources.toml` is the reviewed acquisition inventory;
`standards/manifest.toml` is the machine-readable conformance source of truth.
Exact RFC Editor text is immutable and checksum-locked under
`standards/rfc/`; other external document bytes default to the ignored local
vault. Candidate documents are not implementation claims. Before a feature
starts:

1. run the networked source/errata freshness reviews and confirm the current
   official or legally licensed revision;
2. verify the local byte lock and record publisher, revision,
   publication/retrieval dates, license class, and
   local-copy policy;
3. review amendments, errata, service notices, registries, replacement
   relationships, and legacy conflicts;
4. cite sections/tables in code;
5. map implementation crates and tests;
6. add official, independent, generated, and adversarial evidence;
7. preserve unknown/reserved fields where the standard permits;
8. update coverage and known limitations.

Aggregate families are inventory leads, not implementation records. Before
code begins, split them into exact documents, revisions, amendments, notices,
assignment snapshots and legally retained vectors. Each implemented record
maps crate/module, sections/tables/constants, official and independent vectors,
adversarial tests, feature/profile, known limitations and legal-access class.

Tests ship in the same milestone as behavior. Every applicable positive,
negative, boundary, malformed, adversarial, conformance, differential,
resource, fuzz, platform and regression class is mapped to the implementation;
a not-applicable class requires a recorded reason. Missing or ambiguous
authoritative material blocks implementation and support claims. The
fail-closed rule is normative in
[implementation-evidence-policy.md](implementation-evidence-policy.md).

Paid, consent-gated, registration-gated, personalized, or redistribution-
unclear standards are never committed. Builds and tests never download
standards. New revisions create versioned conformance profiles rather than
silently changing behavior.

## Testing Program

Every release adds evidence at the lowest relevant layer:

- unit and boundary tests;
- checked-arithmetic and capacity tests;
- property and round-trip tests;
- official and operator-provided vectors;
- independent receiver and implementation comparisons;
- fuzz targets and committed small regression seeds;
- numerical reference and near-singular tests;
- deterministic replay;
- live-sky and multi-day tests;
- shielded or conducted RF fault scenarios;
- platform, `no_std`, MSRV, Miri, sanitizer, Kani/model-checking, and
  performance evidence where applicable.

Once behavioral core code exists, its tests run at the MSRV rather than only
compiling there. Miri validates safe wrappers and ownership models, Kani
validates bounded arithmetic/state machines, Loom validates concurrency and
invalidation ordering, and sanitizers/hardware tests validate native adapters.
No tool is credited for a boundary it cannot execute.

Generated GNSS-like RF must never be radiated into an open environment.

## Platform Strategy

The canonical crates avoid assumptions that prevent Linux, Windows, macOS,
FreeBSD, OpenBSD, NetBSD, Android, iOS, WASM, bare metal, or future Aesynx
support. Platform adapters are independently feature-gated and tested.

iOS support must not claim raw measurements unless the platform actually
provides them. WASM does not claim direct hardware access. Aesynx remains a
future adapter target and does not alter core types.

## Security Program

The threat model covers malicious RF, receivers, correction/assistance
servers, files, local devices, time rollback, correction mixing, resource
exhaustion, differential parsing, supply-chain compromise, FFI/DMA, credential
exposure, and location privacy.

Mandatory controls include bounded work, no input-dependent panic under
declared resource limits, freshness and issue-of-data validation, explicit
trust, credential redaction, location-minimizing logs, network allowlists,
reproducible inputs, locked tooling, SBOMs, fuzzing, changed-code pentests, and
periodic full external security and GNSS-domain audits.

Correction caches bind transport peer, provider/mountpoint, station/solution,
frame/datum, antenna, authenticated peer and generation. Secret types are not
ordinarily cloneable, displayable or serializable; routine telemetry excludes
precise position/time and globally correlatable provenance. Time rollback uses
an explicit platform persistence authority rather than pretending `no_std`
can provide rollback-resistant storage.

## Gap-Driven Version Integration

The architecture review has been incorporated without replacing the existing
broader 1.0 roadmap:

| Gap | Versioned implementation stops |
| --- | --- |
| Repository policy, strict tags, report-parent/package provenance | v0.1.1 |
| Machine-readable crate/capability DAG and feature/tier escalation checks | v0.1.4 |
| Exact standards, requirements, claims and test traceability | v0.1.2-v0.1.3 and v0.210.1-v0.210.2 |
| Honest safe bounded storage and caller scratch | v0.2.0-v0.2.3 |
| Exact units, uncertainty and typed covariance | v0.3.0-v0.3.2 and v0.6.2 |
| Deterministic `no_std` math and stable SIMD/backend policy | v0.3.3, v0.48.2-v0.49.0 and v0.201.0 |
| Bounded solver linear algebra and conservative statistical kernels | v0.3.4-v0.3.5 |
| Raw/resolved/atomic/UTC time, exact arithmetic, capture identity and rollback | v0.4.0-v0.5.4 |
| Namespaced IDs, opaque restricted/future records, safe extensions, staged artifacts and assessments | v0.12.0-v0.13.2 |
| External algorithm/stage capability, resource, trust and reset contract | v0.12.3 |
| Canonical versioned signal definitions shared by constellation and format crates | v0.12.4 |
| Projected coordinates and typed derived kinematics | v0.7.2 and v0.13.3 |
| Non-reusing artifact/provenance ID lifecycle and replay remapping | v0.13.1 |
| Deterministic navigation/correction/product model selection evidence | v0.14.2 |
| Correction taxonomy, duplicate prevention, sessions and anti-mixing | v0.15.1-v0.15.2, v0.139.1 and v0.142.1 |
| Borrowed progress, targeted invalidation, counter exhaustion and preflight receipts | v0.16.0-v0.17.2 |
| Honest exact/static/measured/assumed/unavailable resource evidence | v0.17.1 and v0.50.1 |
| Tiered facade, versioned profiles and plan-before-side-effects | v0.20.1-v0.20.2 |
| Complete RTCM/RINEX/product profiles and bounded compact decoding | v0.26.1-v0.35.1 |
| Capture utility and external data artifact governance | v0.36.3 and v0.196.2 |
| Fail-closed streaming/original-preserving format APIs | v0.21.1-v0.36.2 |
| Front-end conditioning, capture mapping, SIMD safety and independent vectors | v0.37.2, v0.47.2-v0.50.2 |
| Early bounded acquisition hints and late assistance translation | v0.42.1 and v0.185.1 |
| Typed PVT/vertical-datum outputs and sequential GNSS estimator | v0.58.1 and v0.120.1-v0.126.1 |
| PVT mode matrix, DGPS and PVT/integrity separation | v0.120.4 and v0.129.3-v0.135.3 |
| Implementable RAIM/ARAIM/SBAS integrity contracts | v0.127.0-v0.129.5 |
| RTK validation, exact network profiles and complete PPP acceptance matrices | v0.135.3, v0.138.1 and v0.144.1-v0.144.2 |
| Public GBAS/ABAS applicability and integrity boundary | v0.119.1 |
| DFMC implementation matrix and exact named SBAS provider/service profiles including SouthPAN | v0.118.1-v0.119.2 |
| Conditional public BeiDou SAR/short-message boundary | v0.103.1 |
| Conditional public NavIC messaging boundary | v0.114.2 |
| Calibrated science artifacts, scintillation, reflectometry and space weather | v0.124.1-v0.124.4 |
| Concrete crypto backend and immutable authentication/evidence/policy decisions | v0.146.1-v0.157.1 |
| Post-protocol crypto and complete resilience evidence matrices | v0.150.1 and v0.155.1 |
| Caller-provided direction evidence versus native calibrated AoA production | v0.155.0 and v0.169.5 |
| Exact bounded GNSS timing slot/mapping/withdrawal contract | v0.158.1-v0.162.1 |
| Common-view/all-in-view time transfer and CGGTTS V2E | v0.163.1 |
| Full fusion calibration/mechanization, vector tracking, reacquisition and fixed-rate output | v0.164.1-v0.168.2 |
| Navigation crate implementation, road-routing non-claim and native AoA producer | v0.169.1-v0.169.5 |
| FPGA/GPU/external-DSP stage, scalar-equivalence and provenance boundary | v0.175.1 |
| Generic sources and evidence-gated receiver families | v0.185.2-v0.185.3 |
| Discovery, Android, canonical assistance, bounded PER and CAN ownership | v0.180.4-v0.190.2 |
| Publish-disabled CLI, services, inspection, visualization and lab tools | v0.190.3-v0.190.11 |
| Simulator, fuzz, conformance and benchmark tools | v0.196.1, v0.198.2-v0.198.3 and v0.201.1 |
| Unsafe/platform/mobile/privacy boundaries | v0.177.1-v0.190.2 |
| Differential, numerical, unsafe, MSRV and Aesynx audits | v0.198.1-v0.207.1 |
| Capability/resource/privacy documentation closure | v0.214.1 |
| Packaging, service and deployment security freeze | v0.219.1 |

These patch milestones are planned compatible implementation passes, not
permission to bundle unrelated work. A breaking correction moves to the next
minor milestone or inserts a new explicitly reviewed minor release.

## Release Discipline

The detailed sequence is in [RELEASE_PLAN.md](RELEASE_PLAN.md). A release can
be split or receive patch milestones at any time. It cannot absorb unrelated
work merely to reach 1.0 faster.

Every milestone contains Status, Goal, Deliverables, Verification, and Exit
criteria. Exit criteria end with the exact-commit pentest stop. No feature is
postponed beyond 1.0 if it is part of the production claim.

Before the first production candidate, all publishable manifests already
declare `1.0.0`. The `v1.0.0-rc.N` repository tag and final `v1.0.0` tag point
to the same approved source/package commit; crates.io publishes only the
retained final-version archives. Report-only pentest commits must prove package
file lists and checksums are identical to the reviewed implementation parent.
