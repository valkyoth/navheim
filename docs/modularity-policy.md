# Modularity Policy

## Source Size

Hand-maintained Rust, Python, and shell source files must not exceed 500 lines.
Generated files require a documented exception and are excluded only by
explicit validation logic.

## Crate Boundaries

Create a focused crate when a domain has an independently testable contract,
different capability tier, different dependency/unsafe policy, separate
publication value, or a reason to remain GitHub-only.

Do not create one crate per signal or tiny helper. Constellation crates group
their public signals so versions and dependency graphs remain manageable.

## README Scope

Every package published to crates.io has its own package README with the shared
Navheim header style and package-specific purpose, features, compatibility, and
usage documentation. The `navheim` facade README remains identical to the
repository README.

GitHub-only packages and tools do not require separate crate-style READMEs.
They use normal repository documentation and may rely on the repository README
when that is clearer. Add a local README only when it helps explain that
component; do not duplicate documentation merely to mirror crates.io packages.

## Dependency Direction

Foundation crates cannot depend on constellation, format, solver, I/O, TLS,
crypto-backend, device, OS, daemon, or tool crates. Adapter and tool crates may
depend inward; canonical crates never depend outward.

The `navheim` facade depends on focused stable libraries. Focused libraries do
not depend on the facade.

GNSS timing consumers depend on Navheim, never the reverse. An adapter whose
purpose is to convert Navheim timing evidence into Mundilfari or another
generic clock framework belongs to that consumer's repository and publication
graph. No Navheim manifest may depend on such a framework.

## GitHub-Only Code

CLI, daemons, deployables, labs, simulators, conformance runners, fuzz
packages, benchmarks, capture tools, FPGA artifacts, and packaging stay
unpublished until an explicit release admits them.
