#!/usr/bin/env sh
set -eu

cargo fmt --all --check
scripts/check_shell_syntax.sh
scripts/check_doc_links.sh
scripts/check_release_plan.sh
scripts/test-release-plan.sh
scripts/generate_release_plan.py --check
scripts/test-check-latest-tools.sh

if ! cmp -s README.md crates/navheim/README.md; then
    echo "README.md and crates/navheim/README.md must remain identical" >&2
    diff -u README.md crates/navheim/README.md >&2 || true
    exit 1
fi

scripts/validate-release-metadata.sh
scripts/validate-modularity-policy.sh check
scripts/validate-security-policy.sh
scripts/check_dependency_policy.sh
scripts/release_crates.py --check
python3 scripts/test-release-crates.py
python3 scripts/test-sbom-compare.py
scripts/generate-sbom.sh --check
scripts/test-release-readiness.sh

cargo check --workspace
cargo check --workspace --all-features
cargo clippy --workspace --all-targets --all-features -- -D warnings
cargo test --workspace --all-features
cargo doc --workspace --all-features --no-deps

cargo package -p navheim-core --allow-dirty
cargo package -p navheim --allow-dirty \
    --config 'patch.crates-io.navheim-core.path="crates/navheim-core"'
