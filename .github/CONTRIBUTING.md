# Contributing To Navheim

Navheim is security-sensitive GNSS/PNT infrastructure. Contributions must keep
the workspace bounded, explicit, tested, and honest about supported signals,
standards, platforms, integrity, and authentication.

## License

Navheim is licensed under `MIT OR Apache-2.0`. Unless explicitly stated
otherwise, contributions are provided under those same terms.

## Development Setup

Use the pinned Rust toolchain from `rust-toolchain.toml`.

```bash
cargo check --workspace --all-features
cargo test --workspace --all-features
scripts/checks.sh
```

## Engineering Requirements

- Keep hand-maintained code files at or below 500 lines.
- Keep foundational and protocol crates `no_std` by default.
- Do not add unsafe code to core, constellation, solver, or format crates.
- Do not add a third-party crate without the dependency review required by
  `SECURITY.md` and `docs/supply-chain-security.md`.
- Cite the normative document section/table for protocol constants.
- Add negative and adversarial tests for every untrusted input surface.
- Do not claim support until standards mapping and independent evidence exist.
- Never radiate generated or replayed GNSS-like RF outside a shielded or
  conducted test environment.

## Security-Sensitive Changes

Treat parsers, length arithmetic, time conversion, correction freshness,
authentication, integrity, solvers, device/OS adapters, FFI, RF generation,
release scripts, CI, and dependency updates as high risk. Follow
[SECURITY.md](../SECURITY.md) for private reports.
