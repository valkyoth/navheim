#!/usr/bin/env sh
set -eu

fixture="$(mktemp -d)"
trap 'rm -rf "$fixture"' EXIT HUP INT TERM

mkdir -p "$fixture/scripts"

cat >"$fixture/scripts/valid-sh.sh" <<'EOF'
#!/usr/bin/env sh
set -eu
value="valid"
test "$value" = "valid"
EOF

cat >"$fixture/scripts/valid-bash.sh" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
diff <(printf '%s\n' "valid") <(printf '%s\n' "valid")
EOF

scripts/check_shell_syntax.sh "$fixture"

cat >"$fixture/scripts/invalid-bash.sh" <<'EOF'
#!/usr/bin/env bash
if [[; then
    exit 0
fi
EOF
if scripts/check_shell_syntax.sh "$fixture" >/dev/null 2>&1; then
    echo "shell checker accepted invalid Bash syntax" >&2
    exit 1
fi
rm "$fixture/scripts/invalid-bash.sh"

cat >"$fixture/scripts/invalid-sh.sh" <<'EOF'
#!/usr/bin/env sh
if (; then
    exit 0
fi
EOF
if scripts/check_shell_syntax.sh "$fixture" >/dev/null 2>&1; then
    echo "shell checker accepted invalid POSIX shell syntax" >&2
    exit 1
fi

echo "shell syntax checker tests passed"
