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
