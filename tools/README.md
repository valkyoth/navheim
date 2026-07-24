# Navheim Repository-Only Tools

This directory is reserved for CLI, daemon, caster, station, survey,
inspection, visualization, laboratory, simulation, conformance, benchmark,
capture, FPGA, packaging, and deployment packages.

Every Cargo package here must set:

```toml
publish = false
rust-version = "1.97.1"
```

Repository-only tools may use `std` and reviewed integration dependencies.
They must not leak those dependencies into published canonical crates. Moving a
tool or library to crates.io requires an explicit release-plan milestone,
stable public API, package README, dependency review, tests, security review,
and publish-order update.

GitHub-only packages use ordinary repository documentation. They need a local
README only when it adds useful component-specific guidance; the shared
crates.io package header is reserved for packages that are actually published.
