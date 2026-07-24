# Toolchain Policy

## Published Crates

Published libraries declare `rust-version = "1.90"` and must compile on every
stable Rust release from `1.90.0` through pinned stable `1.97.1`.

The pinned stable version can move without raising MSRV. Raising MSRV requires
a planned release, compatibility rationale, documentation, and downstream
notice.

## Repository Tools

GitHub-only tools may require Rust `1.97.1`. They must be `publish = false` and
must not leak that requirement into published libraries.

## Release Checks

`rust-toolchain.toml` pins Rust `1.97.1`, rustfmt, and clippy.
`scripts/check_latest_tools.sh` verifies the live stable manifest, cargo-deny,
cargo-audit, cargo-sbom, and GitHub Action pins. Compatibility checks use
explicit `cargo +VERSION` commands.

The full release gate runs on `1.97.1`; earlier supported releases run
`cargo check --workspace --all-features`.
