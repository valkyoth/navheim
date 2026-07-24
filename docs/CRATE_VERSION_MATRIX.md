# Navheim Crate Version Matrix

Navheim crates use independent versions after the foundation release. A
workspace milestone does not force unchanged support crates to be republished.
Roadmap tags are program checkpoints, not a demand that every crate adopt the
same version. A `v0.N.P` roadmap milestone is a bounded compatible
implementation or remediation pass within that program train; any affected
crate receives the independently reviewed SemVer change required by its own
public API.

## v0.1.0 Candidate

| Package | Previous | Candidate | Change | Publish order | crates.io |
| --- | --- | --- | --- | --- | --- |
| `navheim-core` | none | `0.1.0` | Initial dependency-free foundation | 1 | yes, after pentest/tag approval |
| `navheim` | none | `0.1.0` | Initial facade over `navheim-core` | 2 | yes, after core indexing |

`release-crates.toml` is the machine-readable source of truth.
`scripts/release_crates.py --check` validates it against Cargo metadata.

Future releases classify each crate as:

- `code`: implementation/API/docs changed; use the reviewed independent
  version bump;
- `bugfix`: compatible correction; patch bump;
- `dependency`: dependency-only adjustment; patch bump on its existing line;
- `metadata`: immutable package metadata correction;
- `unchanged`: no publish.
