#!/usr/bin/env sh
set -eu

metadata="$(cargo metadata --format-version 1 --locked)"

python3 -c '
import json
import sys

metadata = json.load(sys.stdin)
workspace = set(metadata["workspace_members"])
external = [
    package["name"]
    for package in metadata["packages"]
    if package["id"] not in workspace
]
if external:
    raise SystemExit(
        "v0.1.0 dependency-free policy violated by: " + ", ".join(sorted(external))
    )
print("v0.1.0 dependency-free policy passed")
' <<EOF
$metadata
EOF
