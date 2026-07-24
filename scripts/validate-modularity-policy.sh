#!/usr/bin/env sh
set -eu

mode="${1:-check}"
if [ "$mode" != "check" ]; then
    echo "usage: scripts/validate-modularity-policy.sh check" >&2
    exit 2
fi

violations="$(
    find crates tools scripts -type f \
        \( -name '*.rs' -o -name '*.py' -o -name '*.sh' \) \
        -not -path '*/generated/*' \
        -exec wc -l {} \; |
        awk '$1 > 500 { print }'
)"
if [ -n "$violations" ]; then
    echo "Hand-maintained code files exceed 500 lines:" >&2
    echo "$violations" >&2
    exit 1
fi

grep -q '"crates/navheim"' Cargo.toml
grep -q '"crates/navheim-core"' Cargo.toml
grep -q 'navheim-core.workspace = true' crates/navheim/Cargo.toml

if find tools -mindepth 2 -name Cargo.toml -type f -exec \
    grep -L '^publish = false$' {} + | grep .; then
    echo "GitHub-only tool crates must set publish = false" >&2
    exit 1
fi

echo "modularity policy passed"
