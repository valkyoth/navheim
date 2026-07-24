#!/usr/bin/env sh
set -eu

for crate in crates/navheim crates/navheim-core; do
    grep -q '^#!\[no_std\]' "$crate/src/lib.rs"
    grep -q '^#!\[forbid(unsafe_code)\]' "$crate/src/lib.rs"
done

grep -q 'unknown-git = "deny"' deny.toml
grep -q 'unknown-registry = "deny"' deny.toml
grep -q 'wildcards = "deny"' deny.toml
grep -q 'panic = "abort"' Cargo.toml
grep -q 'overflow-checks = true' Cargo.toml
grep -q 'CodeQL default setup' SECURITY.md
grep -q 'CodeQL analysis default setup is active' docs/github-security-settings.md
test -f docs/secret-handling-policy.md
test -f docs/threat-model.md
test -f docs/GNSS_TIMING_API.md
test -f standards/manifest.toml
test -f standards/licensing.md
test ! -f .github/workflows/codeql.yml
test ! -f PENTEST.md

echo "security policy passed"
