#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

test -s standards/rfc/README.md
test -s standards/rfc/SOURCES
test -s standards/rfc/SHA256SUMS

expected="$(sed -n 's/^[0-9a-f]\{64\}  \(rfc[0-9][0-9]*\.txt\)$/\1/p' \
    standards/rfc/SHA256SUMS | sort)"
actual="$(find standards/rfc -maxdepth 1 -type f -name 'rfc*.txt' \
    -printf '%f\n' | sort)"
sources="$(sed -n \
    's/^\([0-9][0-9]*\) https:\/\/www\.rfc-editor\.org\/rfc\/rfc[0-9][0-9]*\.txt [a-z0-9-][a-z0-9-]*$/rfc\1.txt/p' \
    standards/rfc/SOURCES | sort)"

if [[ -z "$expected" || "$expected" != "$actual" || "$expected" != "$sources" ]]; then
    echo "RFC sources, checksums, and local files differ" >&2
    diff <(printf '%s\n' "$sources") <(printf '%s\n' "$expected") || true
    diff <(printf '%s\n' "$expected") <(printf '%s\n' "$actual") || true
    exit 1
fi

(
    cd standards/rfc
    sha256sum --check --strict SHA256SUMS
)
