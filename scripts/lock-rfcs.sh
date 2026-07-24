#!/usr/bin/env sh
set -eu

root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$root"

find standards/rfc -maxdepth 1 -type f -name 'rfc*.txt' -exec chmod a-w {} +
scripts/verify-rfcs.sh
