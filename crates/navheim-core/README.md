<p align="center">
  <b>Dependency-free no_std GNSS/PNT foundations for Navheim.</b><br>
  Bounded, unit-safe, provenance-aware types and traits built in small audited releases.
</p>

<div align="center">
  <a href="https://crates.io/crates/navheim">Navheim crate</a>
  |
  <a href="https://docs.rs/navheim-core">Docs.rs</a>
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

# navheim-core

Dependency-free Tier 0 foundation for Navheim.

Most users should depend on the facade crate:

```toml
[dependencies]
navheim = "0.1.0"
```

Version `0.1.0` establishes the crate and policy boundary only. Public GNSS
types arrive in their individually tested roadmap milestones; this crate does
not claim protocol, signal, positioning, or timing functionality yet.

The crate is `no_std`, has no default features or third-party dependencies, and
forbids unsafe code. Its future public values must make units, time scales,
reference frames, uncertainty, validity, capacity, and provenance explicit.

Licensed under `MIT OR Apache-2.0`.
