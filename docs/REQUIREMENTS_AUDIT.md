# Repository Requirements Audit

Status: completed planning and foundation audit, 2026-07-24

This audit classifies every tracked repository artifact against the project
requirements and the architecture in `initial-idea.md`. It does not claim that
planned GNSS behavior already exists. Exact RFC publications are reviewed by
source identity, checksum, line-ending, immutability and errata gates rather
than edited or summarized as project-authored prose. The Navheim image was
also inspected for repository/README consistency.

## Foundation Conformance

| Requirement | Evidence and result |
| --- | --- |
| Name and license | Cargo metadata, READMEs and documentation use Navheim and `MIT OR Apache-2.0`. The copied donor name in `LICENSE-MIT` was corrected. |
| Rust support | Publishable crates declare Rust 1.90 MSRV; CI checks every stable 1.90.0-1.97.1 release; repository tools may use pinned 1.97.1. |
| `no_std` | Both current publishable crates are dependency-free `no_std` crates with unsafe code forbidden. Future tiers and adapters are explicit. |
| Dependency policy | Core GNSS behavior remains first-party. TLS, modern cryptography, platform APIs and vendor stacks are isolated adapters. Navheim never depends on Mundilfari or another GNSS implementation. |
| Crate/readme policy | Every publishable crate has a package README; the facade README is identical to the GitHub README. GitHub-only components use normal documentation and remain `publish = false`. |
| Source size | The 500-line gate now scans hand-maintained Rust, Python and shell files across the whole repository, including tests, fuzzing and future paths, while excluding only explicit generated/private/build paths. |
| Testing and security | CI, deny/audit/SBOM gates, negative checker tests, exact-commit pentest stops, threat/security/unsafe/secrets/supply-chain policies and CodeQL default-setup guidance are present. |
| Documentation | Architecture, implementation/release plans, current status, release notes, security policies, standards coverage and publication tooling are present. Markdown-link validation now covers every tracked documentation path, including crates and `.github`. |
| Platforms | The plan has explicit Linux, Windows, macOS, FreeBSD, OpenBSD, NetBSD, Android, iOS, WASM, bare-metal and future Aesynx stops or contracts. |
| Standards storage | Exact redistributable RFC text is immutable and checksum locked. All other external documents default to an ignored local-only vault with legal/access metadata. |

## Scope-to-Version Findings

The earlier roadmap was technically broad but left some architecture promises
inside aggregate milestones. The following releases make each one auditable:

| Architecture promise | Bounded release stops |
| --- | --- |
| Requirement/public-claim ownership and traceability | v0.1.3 and final closure v0.210.2 |
| Capture utility and external evidence-data governance | v0.36.3 and v0.196.2 |
| Conditional public BeiDou SAR/short-message support | v0.103.1 |
| Exact named SBAS provider/service profiles | v0.119.2 |
| Common-view/all-in-view GNSS time transfer and CGGTTS V2E | v0.163.1 |
| FPGA/external-DSP inputs and GitHub-only host/artifact boundary | v0.175.1 |
| Generic receiver sources and conditional vendor families | v0.185.2-v0.185.3 |
| GitHub-only tool foundation, CLI, daemon, caster, station, survey, inspector, viewer and lab | v0.190.3-v0.190.11 |
| Simulator, fuzz, conformance and benchmark harnesses | v0.196.1, v0.198.2-v0.198.3 and v0.201.1 |
| Packages, service units, containers and deployments | v0.219.1 |

These stops augment the existing constellation, formats, DSP, PVT, DGPS, RTK,
PPP, integrity, authentication, timing, fusion, navigation, platform,
assistance, simulation and audit sequence. They do not replace or postpone
existing work.

## External Source Findings

The acquisition inventory previously concentrated on GNSS protocols and
correction formats. Eight missing primary-source families are now represented:

- BIPM/CCTF/ITU-R GNSS time transfer and CGGTTS;
- stable Rust and target/platform language contracts;
- RTL-SDR, bladeRF, UHD/USRP, LimeSuite and FPGA/device-stack contracts;
- Linux/BSD operating-system I/O contracts;
- Microsoft Windows I/O and location contracts;
- Apple macOS/iOS I/O and location contracts;
- NovAtel OEM public receiver material;
- conditionally admitted public receiver protocols.

The catalog now covers 34 source families. It remains an acquisition inventory,
not a conformance claim. Every implementation release must freeze exact lawful
documents, amendments, sections, vectors, hardware/firmware profiles and
limitations in `standards/manifest.toml`.

## Remaining Planned Work

No GNSS behavioral capability exists at v0.1.0. All feature rows remain
planned until their milestone passes its own tests, standards mapping,
security review and exact-commit pentest. The complete final gate requires a
bidirectional mapping for every architecture requirement, public claim,
component, source, test, status and non-claim before 1.0.0.
