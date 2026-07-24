<p align="center">
  <b>Security-first, no_std-first GNSS/PNT infrastructure in Rust.</b><br>
  Built from scratch in small audited releases, from bounded protocol foundations to full civil/open positioning, navigation, and timing.
</p>

<div align="center">
  <a href="https://crates.io/crates/navheim">Crates.io</a>
  |
  <a href="https://docs.rs/navheim">Docs.rs</a>
  |
  <a href="https://github.com/valkyoth/navheim/blob/main/docs/RELEASE_PLAN.md">Release Plan</a>
  |
  <a href="https://github.com/valkyoth/navheim/blob/main/docs/threat-model.md">Threat Model</a>
  |
  <a href="https://github.com/valkyoth/navheim/blob/main/SECURITY.md">Security</a>
</div>

<br>

<p align="center">
  <a href="https://github.com/valkyoth/navheim">
    <img src="https://raw.githubusercontent.com/valkyoth/navheim/main/.github/images/navheim.webp" alt="Navheim Rust GNSS/PNT platform overview">
  </a>
</p>

# Navheim

Navheim is a security-first, `no_std`-first Rust platform for Global Navigation
Satellite Systems and positioning, navigation, and timing. Its production goal
is one canonical observation and time model spanning raw RF/I/Q samples,
receiver observations, correction streams, precise products, operating-system
providers, archived files, and final position/time/integrity results.

The project is built in small, independently reviewable milestones. Version
`0.1.0` establishes repository policy and the first crate boundaries only. It
does not yet decode GNSS data, access receivers, process RF, or produce a
position or time solution.

## Install

After the first release is published:

```toml
[dependencies]
navheim = "0.1.0"
```

The default feature set is dependency-free and `no_std`.

## Capability Status

Legend: 🟢 available for the stated scope, 🟡 established but incomplete,
🔴 planned.

| Capability | Status | Current scope |
| --- | --- | --- |
| Security and release foundation | 🟢 Available | Pinned toolchain, MSRV matrix, dependency policy, SBOM, exact-commit pentest gate, CI, and release tooling |
| `no_std` crate boundary | 🟢 Available | Dependency-free `navheim-core` and `navheim` facade with unsafe code forbidden |
| Standards evidence model | 🟢 Available | Candidate standards inventory, licensing policy, and coverage matrix; no protocol conformance claimed |
| Canonical GNSS types | 🔴 Planned | Units, bounded values, time, coordinates, identifiers, observations, ephemerides, corrections, provenance, and events |
| Formats and corrections | 🔴 Planned | NMEA, RTCM, NTRIP, RINEX, IGS products, SUPL/LPP, and NMEA 2000 boundaries |
| Native SDR/DSP | 🔴 Planned | Sample sources, acquisition, tracking, FEC, observables, deterministic replay, and resource planning |
| Civil/open constellations | 🔴 Planned | GPS, Galileo, GLONASS, BeiDou, QZSS, NavIC, and provider-neutral SBAS |
| Positioning and timing | 🔴 Planned | PVT, RTK, PPP, integrity, authentication, timing, fusion, attitude, and navigation |
| Platform I/O | 🔴 Planned | Linux, Windows, macOS, BSD, Android, iOS, WASM, bare metal, and a future Aesynx adapter |
| Production admission | 🔴 Planned | Standards freeze, full coverage audit, independent GNSS review, external security audit, release candidates, and unchanged 1.0 promotion |

See [Current Status](https://github.com/valkyoth/navheim/blob/main/docs/current-status.md)
for the exact implementation snapshot and
[Release Plan](https://github.com/valkyoth/navheim/blob/main/docs/RELEASE_PLAN.md)
for the complete pre-1.0 sequence.

## Design Commitments

- One canonical observation and time model, with independent sources and
  explicit solver/security policies.
- First-party implementation of GNSS wire formats, signal processing,
  navigation messages, correction behavior, and solution algorithms.
- Reviewed external crates only for boundaries such as TLS, cryptographic
  primitives, platform APIs, and vendor device stacks.
- No hidden allocation, threads, networking, device opening, or degraded
  capability in core APIs.
- Unknown future signal and system identifiers are preserved.
- Authentication, signal-source authenticity, message correctness, and
  solution integrity remain distinct.
- Every result eventually carries units, time scale, reference frame,
  uncertainty, validity, and provenance.
- Restricted or classified services are cataloged honestly, never represented
  as decoded without public specifications and authorization.
- Every untrusted parser is bounded, fuzzed, and covered by adversarial tests.
- Hand-maintained code files remain at or below 500 lines.

## Workspace Shape

Most users should depend on `navheim`. Focused crates are published only when
their assigned release has an implemented, tested, and documented public API.

| Crate | crates.io | Capability tier | Purpose |
| --- | --- | --- | --- |
| `navheim` | Publishable | Tier 0 by default | Stable facade over admitted Navheim capabilities |
| `navheim-core` | Publishable | Tier 0 | Dependency-free common types and traits |
| Future focused libraries | Planned | Tier 0–3 | DSP, constellations, solvers, formats, security, adapters, and platform I/O |
| `tools/*` | GitHub only | `std`, Rust 1.97.1 allowed | CLI, daemons, labs, conformance, capture, simulation, and deployment tools |

Capability tiers:

| Tier | Allowed environment |
| --- | --- |
| Tier 0 | `core` only; no heap or operating-system dependency |
| Tier 1 | Explicit `alloc`; no operating-system dependency |
| Tier 2 | Explicit `std` for files, sockets, devices, threads, and clocks |
| Tier 3 | External integration adapters such as TLS, crypto, platform, or vendor stacks |

## Trust Dashboard

| Area | Policy |
| --- | --- |
| License | `MIT OR Apache-2.0` |
| MSRV | Rust `1.90.0` |
| Pinned stable toolchain | Rust `1.97.1` |
| Default target | `no_std` |
| Default external dependencies | zero |
| Core unsafe policy | forbidden |
| Core GNSS implementation dependencies | none |
| Release evidence | tests, dependency policy, SBOM, CI, CodeQL default setup, exact-commit pentest |
| Safety claims | no safety-of-life or certification claim without independent certification evidence |

## Rust Version Support

Publishable crates have MSRV Rust `1.90.0`. Release development is pinned to
Rust `1.97.1`; repository-only tools may require that pinned version. The
release gate checks every installed stable release in the supported range and
the networked preflight verifies that the pin and CI tooling remain current.

| Rust | Required evidence |
| --- | --- |
| `1.90.0`–`1.97.0` | `cargo check --workspace --all-features` on each supported stable toolchain |
| `1.97.1` | Full format, lint, test, documentation, packaging, policy, SBOM, and release gate |

Increasing the pinned stable toolchain does not automatically increase the
published crates' MSRV.

## Operating-System Direction

The core architecture is designed for Linux, Windows, macOS, FreeBSD, OpenBSD,
NetBSD, Android, iOS, WASM, and bare-metal systems from day one. Platform
support is admitted only with target-specific evidence. Aesynx integration is
reserved as a future adapter and must not require redesigning the canonical
core.

## Checks

```bash
scripts/checks.sh
scripts/release_0_1_gate.sh
cargo deny check
cargo audit
```

The networked release gate also checks current Rust, cargo security tools, and
GitHub Action pins. GitHub CodeQL uses default setup rather than an advanced
workflow committed in this repository.

## Documentation

- [Current Status](https://github.com/valkyoth/navheim/blob/main/docs/current-status.md)
- [Implementation Plan](https://github.com/valkyoth/navheim/blob/main/docs/IMPLEMENTATION_PLAN.md)
- [GNSS Timing API](https://github.com/valkyoth/navheim/blob/main/docs/GNSS_TIMING_API.md)
- [Release Plan](https://github.com/valkyoth/navheim/blob/main/docs/RELEASE_PLAN.md)
- [Release Checklist](https://github.com/valkyoth/navheim/blob/main/docs/release-checklist.md)
- [Crate Version Matrix](https://github.com/valkyoth/navheim/blob/main/docs/CRATE_VERSION_MATRIX.md)
- [Initial Architecture Discussion](https://github.com/valkyoth/navheim/blob/main/docs/initial-idea.md)
- [Threat Model](https://github.com/valkyoth/navheim/blob/main/docs/threat-model.md)
- [Security Controls](https://github.com/valkyoth/navheim/blob/main/docs/security-controls.md)
- [Standards Source Workspace](https://github.com/valkyoth/navheim/blob/main/standards/README.md)
- [Standards Coverage](https://github.com/valkyoth/navheim/blob/main/standards/coverage.md)
- [Standards Licensing](https://github.com/valkyoth/navheim/blob/main/standards/licensing.md)
- [RFC Source Policy](https://github.com/valkyoth/navheim/blob/main/docs/rfc-source-policy.md)
- [Modularity Policy](https://github.com/valkyoth/navheim/blob/main/docs/modularity-policy.md)
- [Supply-Chain Security](https://github.com/valkyoth/navheim/blob/main/docs/supply-chain-security.md)
- [Toolchain Policy](https://github.com/valkyoth/navheim/blob/main/docs/toolchain-policy.md)
- [Unsafe Policy](https://github.com/valkyoth/navheim/blob/main/docs/unsafe-policy.md)

## License

Licensed under either of Apache License, Version 2.0 or MIT license at your
option.
