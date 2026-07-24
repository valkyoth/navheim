# Changelog

All notable changes to `navheim` are documented here.

## Unreleased

- Initialized the Rust workspace with dependency-free `navheim-core` and
  `navheim` facade crates.
- Added the standards, security, release, supply-chain, CI, and documentation
  foundations for the v0.1.0 implementation stop.
- Established Rust `1.90.0` through `1.97.1` compatibility policy and pinned
  release development to Rust `1.97.1`.
- Defined a one-way GNSS timing integration boundary: Navheim exposes complete
  dependency-free timing evidence, while downstream clock frameworks own their
  adapters, discipline, consensus, and holdover.
- Integrated the architecture/security gap review into the existing roadmap as
  targeted patch milestones, phase-specific technical acceptance criteria,
  stronger canonical/timing contracts, and unambiguous RC/package provenance.
- Closed the second planning coverage review with explicit implementation
  stops for `navheim-navigation`, complete RTCM/RINEX/product profiles, typed
  PVT and vertical-datum outputs, front-end conditioning, fusion calibration
  and vector tracking, assistance, integrity, RustCrypto, CAN I/O, independent
  conformance vectors, and exact timing state machines.
- Closed the third coverage review by repairing timing-slot and CAN ownership,
  adding deterministic `no_std` math, DGPS, profiles/discovery, full Android
  platform work, bounded PER and post-protocol crypto milestones, and
  separating PVT facts from integrity assessments.
- Added a Gjallarbru-style immutable RFC workflow with 25 exact RFC Editor
  publications, checksum/line-ending gates, an optional local read-only guard,
  lifecycle roles, and a live-checked 210-errata drift snapshot.
- Made shell syntax checks honor Bash versus POSIX-shell shebangs and replaced
  the non-portable CI read-only-mode assertion with checksum/source identity.
- Added the external standards acquisition inventory and secure local-only
  vault workflow: 34 authoritative source families, 17 allowlisted public
  downloads, local SHA-256 locking, official-page revision-marker review, and
  enforced exclusion of restricted document bytes from Git and crates.
- Completed a repository-wide requirement/specification audit, corrected the
  copied MIT donor notice, and expanded source-size and Markdown-link checks
  across all applicable repository paths.
- Added bounded pre-1.0 releases for CGGTTS common-view/all-in-view timing,
  exact SBAS providers, conditional BeiDou messaging, FPGA/external DSP,
  generic and conditional receiver families, every named GitHub-only tool,
  external evidence data, deployment artifacts, and full requirement/claim
  traceability.
- Made source-first review and same-milestone testing a fail-closed,
  repository-validated rule for every behavioral implementation.
