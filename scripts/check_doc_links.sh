#!/usr/bin/env sh
set -eu

repository="${1:-.}"
cd "$repository"

missing=0
find . -type f -name '*.md' \
    -not -path './.git/*' \
    -not -path './.agents/*' \
    -not -path './.codex/*' \
    -not -path './.cargo-deny-advisory-dbs/*' \
    -not -path './target/*' \
    -not -path './standards/private/*' \
    -not -path './tmp/*' \
    -not -path './temp/*' \
    -not -path './dist/*' \
    -print | sort | while IFS= read -r file; do
    grep -oE '\]\([^)]*\.md(#[^)]*)?\)' "$file" 2>/dev/null |
        sed 's/^](//; s/)$//; s/#.*$//' |
        while IFS= read -r link; do
        case "$link" in
            http://*|https://*) continue ;;
            /*) target=".$link" ;;
            *) target="$(dirname "$file")/$link" ;;
        esac
        if [ ! -f "$target" ]; then
            echo "missing markdown link target: $file -> $link" >&2
            exit 1
        fi
        done || exit 1
done || missing=1

if [ "$missing" -ne 0 ]; then
    exit 1
fi
