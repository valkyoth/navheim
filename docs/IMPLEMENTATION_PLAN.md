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
- Protocol, constellation, solver, and format crates forbid unsafe code.
- Unsafe is isolated to reviewed FFI, DMA, or SIMD/platform modules with a
  safety contract, Miri evidence where applicable, and independent review.
- Hand-maintained code files must stay at or below 500 lines.
- Every input length, offset, epoch, capacity, and resource calculation is
  checked.
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

Each crate documents its default tier, optional promotions, worst-case stack,
heap, scratch, input, and state capacity, and any floating-point assumptions.

## Crate Architecture

### Facade and foundation

- `navheim`: profiles, prelude, stable re-exports, source/solver composition,
  and capability planning.
- `navheim-core`: bounded collections, units, time, coordinates, identifiers,
  bit/FEC/checksum primitives, observations, ephemerides, corrections, events,
  errors, provenance, resource planning, and stable traits.
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

- `navheim-pvt`
- `navheim-rtk`
- `navheim-ppp`
- `navheim-integrity`
- `navheim-fusion`
- `navheim-timing`: GNSS time resolution, time-only solutions, receiver clock
  estimates, time transfer, external PPS/time-mark semantic correlation,
  10 MHz/frequency-output status, calibrated delay, uncertainty, health,
  authentication, integrity, and adapter-facing events.
- `navheim-security`
- `navheim-navigation`

Authentication, signal authenticity, message correctness, and solution
integrity remain separate types and policies.

`navheim-timing` does not implement generic PPS device capture, NTP/PTP,
cross-family clock consensus, local oscillator discipline, generic holdover,
or privileged clock adjustment. Those belong to consumers such as Mundilfari.

### Formats and interoperability

- `navheim-nmea`
- `navheim-nmea2000`
- `navheim-rtcm`
- `navheim-ntrip`
- `navheim-rinex`
- `navheim-products`
- `navheim-receiver`
- `navheim-assist`
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

### GitHub-only tools

CLI, daemons, caster/station/survey services, inspectors, viewers, labs,
simulation, conformance, benchmarks, fuzz targets, capture tooling, FPGA
artifacts, packaging, service units, and deployments remain under `tools/`,
`fuzz/`, or other repository-only paths until separately admitted. They set
`publish = false` and may use Rust `1.97.1`.

## Canonical Model Order

Implementation proceeds in this dependency order:

1. bounded collections, errors, and checked arithmetic;
2. physical units and exact integer time;
3. coordinates and reference frames;
4. bit, checksum, parity, and FEC primitives;
5. extensible identifiers and registries;
6. observations, ephemerides, corrections, provenance, and events;
7. capabilities, resource plans, and deterministic source/sink polling;
8. formats and deterministic replay;
9. scalar native DSP and timestamp correctness;
10. GPS L1 C/A end-to-end as the first observable-to-fix path;
11. remaining GPS and constellations;
12. multi-GNSS solution quality, RTK, PPP, integrity, and authentication;
13. complete the stable GNSS timing observation/event API, then fusion,
    hardware, OS, assistance, and NMEA 2000;
14. simulation, fuzzing, audits, conformance, standards freeze, and release
    candidates.

RTK, PPP, and authentication do not become trusted surfaces until observation
time/phase correctness is independently proven.

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

`standards/manifest.toml` is the machine-readable source of truth. Candidate
documents are not implementation claims. Before a feature starts:

1. confirm the current official or legally licensed revision;
2. record publisher, revision, publication/retrieval dates, license class, and
   local-copy policy;
3. cite sections/tables in code;
4. map implementation crates and tests;
5. add official, independent, generated, and adversarial evidence;
6. preserve unknown/reserved fields where the standard permits;
7. update coverage and known limitations.

Paid or restricted standards are never committed. New revisions create
versioned conformance profiles rather than silently changing behavior.

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

Mandatory controls include bounded work, panic-free untrusted boundaries,
freshness and issue-of-data validation, explicit trust, credential redaction,
location-minimizing logs, network allowlists, reproducible inputs, locked
tooling, SBOMs, fuzzing, changed-code pentests, and periodic full external
security and GNSS-domain audits.

## Release Discipline

The detailed sequence is in [RELEASE_PLAN.md](RELEASE_PLAN.md). A release can
be split or receive patch milestones at any time. It cannot absorb unrelated
work merely to reach 1.0 faster.

Every milestone contains Status, Goal, Deliverables, Verification, and Exit
criteria. Exit criteria end with the exact-commit pentest stop. No feature is
postponed beyond 1.0 if it is part of the production claim.
