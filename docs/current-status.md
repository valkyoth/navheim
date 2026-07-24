# Navheim Current Status

Status: v0.1.0 implementation candidate

Navheim currently provides repository and crate foundations only.

## Implemented

- Cargo workspace with resolver 3 and edition 2024.
- Dependency-free, `no_std`, unsafe-forbidden `navheim-core`.
- Dependency-free, `no_std`, unsafe-forbidden `navheim` facade over
  `navheim-core`.
- Rust 1.90.0 MSRV and Rust 1.97.1 pinned release toolchain.
- CI compatibility checks across every stable release in the supported range.
- Linux, Windows, and macOS host checks.
- Dependency, advisory, license, source, SBOM, modularity, documentation, and
  release-metadata gates.
- Exact-commit pentest-before-tag release process.
- Initial standards inventory, licensing policy, architecture discussion,
  implementation plan, and complete pre-1.0 release plan.

## Not Implemented

No GNSS/PNT behavioral capability is implemented. In particular, Navheim
cannot yet parse receiver/file/network data, process samples, decode a
constellation, compute satellite state, solve position or time, validate
integrity, authenticate navigation messages, or access platform devices.

## Next Stop

The next planned release is v0.2.0: bounded collections, fixed-capacity
strings, capacity errors, and adversarial boundary tests in `navheim-core`.
