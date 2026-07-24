#!/usr/bin/env sh
set -eu

fixture="$(mktemp -d)"
trap 'rm -rf "$fixture"' EXIT HUP INT TERM

mkdir -p "$fixture/.github" "$fixture/crates/example" "$fixture/docs"

cat >"$fixture/README.md" <<'EOF'
[Architecture](docs/architecture.md)
EOF
cat >"$fixture/docs/architecture.md" <<'EOF'
[Root](../README.md)
EOF
cat >"$fixture/.github/CONTRIBUTING.md" <<'EOF'
[Architecture](../docs/architecture.md)
EOF
cat >"$fixture/crates/example/README.md" <<'EOF'
[Root](../../README.md) and [Architecture](../../docs/architecture.md#scope)
EOF

scripts/check_doc_links.sh "$fixture"

cat >"$fixture/crates/example/README.md" <<'EOF'
[Root](../../README.md) and [Missing](../../docs/missing.md)
EOF
if scripts/check_doc_links.sh "$fixture" >/dev/null 2>&1; then
    echo "documentation link checker missed a crate README link" >&2
    exit 1
fi

echo "documentation link checker tests passed"
