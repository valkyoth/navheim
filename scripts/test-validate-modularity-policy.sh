#!/usr/bin/env sh
set -eu

fixture="$(mktemp -d)"
trap 'rm -rf "$fixture"' EXIT HUP INT TERM

mkdir -p \
    "$fixture/crates/navheim/src" \
    "$fixture/crates/navheim-core/src" \
    "$fixture/tools/helper/src" \
    "$fixture/scripts" \
    "$fixture/tests"

cat >"$fixture/Cargo.toml" <<'EOF'
[workspace]
members = [
    "crates/navheim",
    "crates/navheim-core",
]
EOF

cat >"$fixture/crates/navheim/Cargo.toml" <<'EOF'
[package]
name = "navheim"
readme = "README.md"

[dependencies]
navheim-core.workspace = true
EOF

cat >"$fixture/crates/navheim-core/Cargo.toml" <<'EOF'
[package]
name = "navheim-core"
readme = "README.md"
EOF

cat >"$fixture/tools/helper/Cargo.toml" <<'EOF'
[package]
name = "navheim-helper"
publish = false
rust-version = "1.97.1"
EOF

: >"$fixture/crates/navheim/README.md"
: >"$fixture/crates/navheim-core/README.md"
: >"$fixture/crates/navheim/src/lib.rs"
: >"$fixture/crates/navheim-core/src/lib.rs"
: >"$fixture/tools/helper/src/main.rs"
: >"$fixture/tests/conformance.rs"

scripts/validate-modularity-policy.sh check "$fixture" >/dev/null

cp "$fixture/Cargo.toml" "$fixture/Cargo.toml.clean"
cat >>"$fixture/Cargo.toml" <<'EOF'

[workspace.dependencies]
mundilfari = "0.1.0"
EOF
if scripts/validate-modularity-policy.sh check "$fixture" >/dev/null 2>&1; then
    echo "modularity policy accepted a Mundilfari dependency" >&2
    exit 1
fi
mv "$fixture/Cargo.toml.clean" "$fixture/Cargo.toml"

awk 'BEGIN { for (i = 0; i < 501; i++) print "#" }' \
    >"$fixture/tests/conformance.rs"
if scripts/validate-modularity-policy.sh check "$fixture" >/dev/null 2>&1; then
    echo "modularity policy accepted an oversized test source outside crates/tools/scripts" >&2
    exit 1
fi
: >"$fixture/tests/conformance.rs"

rm "$fixture/crates/navheim-core/README.md"
if scripts/validate-modularity-policy.sh check "$fixture" >/dev/null 2>&1; then
    echo "modularity policy accepted a missing published-crate README" >&2
    exit 1
fi

echo "modularity policy checker tests passed"
