#!/usr/bin/env sh
set -eu

test ! -f PENTEST.md
test -f LICENSE-MIT
test -f LICENSE-APACHE
test -f SECURITY.md
test -f CHANGELOG.md
test -f release-crates.toml
test -f release-notes/RELEASE_NOTES_0.1.0.md
test -f sbom/navheim.spdx.json
test -f .github/CODEOWNERS
test -f .github/FUNDING.yml
test -f .github/CONTRIBUTING.md
test -f .github/PULL_REQUEST_TEMPLATE.md
test -f .github/ISSUE_TEMPLATE/bug_report.yml
test -f .github/dependabot.yml
test -f .github/workflows/ci.yml
test -f .github/workflows/release.yml
test -f .github/images/navheim.webp
test -f docs/initial-idea.md
test -f docs/IMPLEMENTATION_PLAN.md
test -f docs/RELEASE_PLAN.md
test -f docs/current-status.md
test -f docs/CRATE_VERSION_MATRIX.md
test -f docs/release-checklist.md
test -f docs/implementation-evidence-policy.md
test -f standards/manifest.toml
test -f standards/coverage.md
test -f standards/licensing.md

for script in \
    scripts/checks.sh \
    scripts/check_latest_tools.sh \
    scripts/check_release_plan.sh \
    scripts/generate_release_plan.py \
    scripts/release_crates.py \
    scripts/release_0_1_gate.sh \
    scripts/validate-implementation-evidence-policy.sh \
    scripts/validate_implementation_evidence.py \
    scripts/validate-release-readiness.sh; do
    test -x "$script"
done

release_version="$(
    python3 -c 'import tomllib; print(tomllib.load(open("release-crates.toml", "rb"))["release"]["version"])'
)"
facade_version="$(
    python3 -c 'import tomllib; print(tomllib.load(open("crates/navheim/Cargo.toml", "rb"))["package"]["version"]["workspace"])'
)"
core_version="$(
    python3 -c 'import tomllib; print(tomllib.load(open("crates/navheim-core/Cargo.toml", "rb"))["package"]["version"]["workspace"])'
)"

test "$facade_version" = "True"
test "$core_version" = "True"
test "$release_version" = "0.1.0"
grep -q '^version = "0.1.0"$' Cargo.toml
grep -q '^license = "MIT OR Apache-2.0"$' Cargo.toml
grep -q '^rust-version = "1.90"$' Cargo.toml
grep -q '^channel = "1.97.1"$' rust-toolchain.toml
grep -q 'repository = "https://github.com/valkyoth/navheim"' Cargo.toml

grep -q 'workflow_dispatch:' .github/workflows/release.yml
grep -q 'fetch-depth: 0' .github/workflows/release.yml
! grep -q 'tags:' .github/workflows/release.yml
! find .github/workflows -type f -iname '*codeql*' | grep .

scripts/release_crates.py --check
echo "release metadata passed"
