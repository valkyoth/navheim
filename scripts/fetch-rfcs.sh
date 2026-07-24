#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

test -s standards/rfc/SOURCES
mkdir -p standards/rfc

while read -r number url role; do
    [[ -n "${number:-}" ]] || continue
    [[ "$number" != \#* ]] || continue
    expected="https://www.rfc-editor.org/rfc/rfc${number}.txt"
    if [[ "$url" != "$expected" || -z "${role:-}" ]]; then
        echo "invalid RFC source entry for ${number}" >&2
        exit 1
    fi
    destination="standards/rfc/rfc${number}.txt"
    [[ ! -e "$destination" ]] || continue
    temporary="${destination}.tmp"
    rm -f "$temporary"
    curl --fail --location --silent --show-error --proto '=https' --tlsv1.2 \
        --connect-timeout 10 --max-time 90 "$url" --output "$temporary"
    test -s "$temporary"
    mv "$temporary" "$destination"
done < standards/rfc/SOURCES

(
    cd standards/rfc
    sha256sum rfc*.txt > SHA256SUMS
)
scripts/lock-rfcs.sh
scripts/verify-rfcs.sh
