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
