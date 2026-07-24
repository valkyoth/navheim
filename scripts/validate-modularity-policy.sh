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

for manifest in crates/*/Cargo.toml; do
    [ -f "$manifest" ] || continue
    if grep -q '^publish = false$' "$manifest"; then
        continue
    fi

    package_dir="${manifest%/Cargo.toml}"
    if ! grep -q '^readme = "README.md"$' "$manifest"; then
        echo "Published crate must declare its package README: $manifest" >&2
        exit 1
    fi
    if [ ! -f "$package_dir/README.md" ]; then
        echo "Published crate package README is missing: $package_dir/README.md" >&2
        exit 1
    fi
done

echo "modularity policy passed"
