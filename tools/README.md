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

Named pre-1.0 stops cover:

- `navheim-capture` at v0.36.3 and `navheim-fpga` at v0.175.1;
- the tool foundation, `navheim-cli`, `navheimd`, caster, station, survey,
  inspector, viewer and lab at v0.190.3-v0.190.11;
- simulator/data, fuzz, conformance and benchmark tooling at
  v0.196.1-v0.201.1;
- packages, service units, containers and deployments at v0.219.1.

Each tool reuses canonical library APIs, declares its authority and side
effects, protects precise location/time and secrets, and has its own
adversarial verification. No tool may become a second GNSS implementation.
