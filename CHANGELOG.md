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
