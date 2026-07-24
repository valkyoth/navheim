# Security Policy

Navheim is security-sensitive GNSS/PNT infrastructure. Treat RF input,
receiver output, network corrections, assistance data, archived files,
position/time results, device adapters, FFI, CI, release scripts, and
dependency updates as hostile or high risk until reviewed and tested.

## Supported Versions

No production-ready version exists yet. Security fixes target the active
development line until a stable support policy is published before 1.0.0.

## Reporting

Do not disclose exploitable details in a public issue. Use GitHub private
vulnerability reporting or a private security advisory once enabled for the
repository. If those channels are unavailable, contact the repository owner
privately and include:

- affected version or commit;
- affected crate, protocol, platform, or tool;
- reproduction conditions;
- security impact;
- whether RF transmission or sensitive location data is involved.

Do not transmit GNSS-like RF outside a conducted or shielded environment.

## Routine Checks

Run regularly and before releases:

```bash
scripts/checks.sh
scripts/check_latest_tools.sh
scripts/release_0_1_gate.sh
cargo deny check
cargo audit
scripts/generate-sbom.sh --check
```

GitHub Actions run CI. GitHub CodeQL default setup should be enabled in the
repository security settings. Do not add an advanced CodeQL workflow while
default setup is active. See
[GitHub Security Settings](docs/github-security-settings.md).

## Release Gate

Every tag must point at a final pentest-report commit. The matching
`security/pentest/vX.Y.Z.md` report must have `Status: PASS`, name the exact
reviewed implementation commit, and be the only change in its commit.
`scripts/validate-release-readiness.sh vX.Y.Z` must pass before tagging.

The temporary root `PENTEST.md` file is scratch input for findings. It must
never be committed and must be removed before the final implementation commit.

## Dependency Policy

GNSS correctness is first-party. New third-party crates require:

- a current crates.io version check;
- license, maintenance, advisory, MSRV, and feature review;
- a documented reason the boundary cannot reasonably stay dependency-free;
- confirmation that core wire, signal, correction, solver, or integrity
  behavior is not delegated;
- tests for the admitted behavior;
- `cargo deny check`, `cargo audit`, and SBOM evidence.

TLS and modern cryptographic primitives must use explicit, reviewed adapters;
Navheim must not invent its own TLS or modern signature/hash primitives.

## Coordinated Disclosure

Maintain confidentiality until a fix and release plan exist. Security reports
may contain precise locations, receiver identities, RF characteristics,
credentials, captures, or timing data; minimize and encrypt that evidence.
