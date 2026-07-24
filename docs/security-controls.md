# Security Controls

## Repository Controls

- full-SHA GitHub Action pins;
- least-privilege workflow permissions;
- CodeQL default setup, not advanced setup;
- weekly Cargo and GitHub Actions dependency monitoring;
- locked Rust and Cargo tool versions;
- dependency allowlist and unknown-source denial;
- committed SPDX SBOM with semantic drift validation;
- release metadata and exact-commit pentest validation.

## Code Controls

- `#![forbid(unsafe_code)]` in current crates;
- `no_std` default and zero external dependencies;
- release overflow checks and aborting production panics;
- workspace lints against panic/unwrap/expect/indexing/arithmetic hazards;
- 500-line normal Rust source limit;
- package and documentation verification.

## Protocol Controls

Protocol implementation is not yet present. Before admission it must provide
bounded exact parsing, adversarial tests, fuzzing, official and independent
vectors, standards citations, freshness/validity policy, no partial state
commit, and explicit provenance/error reporting.

## Operational Controls

Generated GNSS-like RF is restricted to conducted or shielded environments.
Credentials and precise position are redacted by default. Device opening and
network access are explicit policy actions. Privileged clock changes remain
outside Navheim. GNSS timing APIs expose bounded uncertainty, freshness,
health, authentication, integrity, provenance, and invalidation so downstream
clock frameworks can enforce their own policy without re-decoding GNSS.
