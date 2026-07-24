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
- Checksum-locked local copies of 25 applicable IETF RFCs, an RFC errata drift
  snapshot, and a reviewed acquisition inventory spanning 34 GNSS, correction,
  exchange, aviation, telecom, geodesy, security, timing, receiver, SDR, Rust,
  and platform
  source families.
- An ignored, locally checksum-locked standards vault with safe allowlisted
  fetching for public documents; paid, licensed, consent-gated,
  registration-gated, and vendor-profile documents remain manual/local-only.
- One-way GNSS timing API boundary: Navheim will produce complete satellite
  timing evidence without depending on generic clock frameworks.
- Repository-wide requirements audit covering every tracked artifact class,
  correcting the MIT donor notice and expanding code-size/document-link gates
  to all applicable repository paths.
- Fail-closed implementation evidence policy: exact authoritative documents
  and sections are reviewed before code, and mapped tests ship in the same
  milestone; missing or ambiguous evidence blocks implementation.
- Audit-strengthened roadmap with 382 pre-1.0 implementation milestones plus
  the explicit production candidate and final release: targeted
  artifact/assessment, complete format/navigation/PVT/DGPS/fusion coverage,
  deterministic `no_std` math, bounded preflight/discovery/PER, explicit
  GNSS time transfer, SBAS provider, receiver/FPGA, GitHub-only tool, platform,
  correction/security/provenance and traceability stops are integrated without
  reducing the original civil/open scope.

## Not Implemented

No GNSS/PNT behavioral capability is implemented. In particular, Navheim
cannot yet parse receiver/file/network data, process samples, decode a
constellation, compute satellite state, solve position or time, validate
integrity, authenticate navigation messages, or access platform devices.

## Next Stop

After the v0.1.0 exact-commit pentest/report stop, the next planned release is
v0.1.1: metadata-driven crate/tier/unsafe, strict SemVer, tag,
pentest-parent and package-provenance enforcement.
