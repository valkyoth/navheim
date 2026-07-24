#!/usr/bin/env sh
set -eu

fixture="$(mktemp -d)"
trap 'rm -rf "$fixture"' EXIT HUP INT TERM

mkdir -p \
    "$fixture/.github" \
    "$fixture/docs" \
    "$fixture/scripts" \
    "$fixture/standards"

cp .github/CONTRIBUTING.md "$fixture/.github/"
cp .github/PULL_REQUEST_TEMPLATE.md "$fixture/.github/"
cp docs/IMPLEMENTATION_PLAN.md "$fixture/docs/"
cp docs/RELEASE_PLAN.md "$fixture/docs/"
cp docs/implementation-evidence-policy.md "$fixture/docs/"
cp docs/initial-idea.md "$fixture/docs/"
cp docs/release-checklist.md "$fixture/docs/"
cp scripts/generate_release_plan.py "$fixture/scripts/"
cp scripts/validate_implementation_evidence.py "$fixture/scripts/"
cp standards/manifest.toml "$fixture/standards/"

scripts/validate-implementation-evidence-policy.sh "$fixture" >/dev/null

sed \
    's/implementation_requires_tests_in_same_milestone = true/implementation_requires_tests_in_same_milestone = false/' \
    "$fixture/standards/manifest.toml" \
    >"$fixture/standards/manifest.toml.changed"
mv "$fixture/standards/manifest.toml.changed" "$fixture/standards/manifest.toml"

if scripts/validate-implementation-evidence-policy.sh "$fixture" \
    >/dev/null 2>&1; then
    echo "implementation evidence checker accepted a weakened test policy" >&2
    exit 1
fi

cp standards/manifest.toml "$fixture/standards/manifest.toml"
sed '0,/^status = "candidate"$/s//status = "implemented"/' \
    "$fixture/standards/manifest.toml" \
    >"$fixture/standards/manifest.toml.changed"
mv "$fixture/standards/manifest.toml.changed" "$fixture/standards/manifest.toml"

if scripts/validate-implementation-evidence-policy.sh "$fixture" \
    >/dev/null 2>&1; then
    echo "implementation evidence checker accepted an unmapped implemented record" >&2
    exit 1
fi

echo "implementation evidence policy tests passed"
