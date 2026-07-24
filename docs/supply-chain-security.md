# Supply-Chain Security

## Default Position

The v0.1 published graph contains no third-party crates. Core GNSS correctness
must remain first-party.

## Admission Checklist

Before adding or updating a dependency:

1. verify the newest crates.io release and its declared MSRV;
2. inspect default and optional features;
3. inspect runtime, build, proc-macro, native, network, and transitive impact;
4. review maintenance, advisories, yanks, provenance, and license;
5. document the security boundary and why a standard-library implementation is
   not appropriate;
6. disable default features unless explicitly required;
7. add behavior, negative, and feature-matrix tests;
8. run Cargo policy, advisory, packaging, MSRV, and SBOM checks.

Git dependencies are denied. An exceptional Git dependency must be exact-rev
pinned, documented, isolated, and removed or replaced through a named release.

## Accepted Dependency Classes

- TLS backends;
- modern cryptographic primitives;
- OS/platform and mobile bindings;
- vendor device/FPGA stacks where unavoidable;
- test-only independent references and tooling.

These classes are not pre-approved. Each instance still needs review.

## Release Evidence

Every release refreshes Cargo.lock, dependency policy, RustSec results, SBOM,
tool/action versions, crate archives, and exact publish order. Only crates
marked changed in `release-crates.toml` are published.
