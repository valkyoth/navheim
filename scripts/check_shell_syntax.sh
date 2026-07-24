#!/usr/bin/env sh
set -eu

repository="${1:-.}"
cd "$repository"

files="$(find scripts -type f -name '*.sh' -print | sort)"
for file in $files; do
    shebang="$(sed -n '1p' "$file")"
    case "$shebang" in
        '#!/usr/bin/env bash'|'#!/bin/bash')
            bash -n "$file"
            ;;
        '#!/usr/bin/env sh'|'#!/bin/sh')
            sh -n "$file"
            ;;
        *)
            echo "unsupported or missing shell shebang: $file" >&2
            exit 1
            ;;
    esac
done
