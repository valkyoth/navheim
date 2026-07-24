#!/usr/bin/env sh
set -eu

repository="${1:-.}"
cd "$repository"

policy="docs/implementation-evidence-policy.md"
manifest="standards/manifest.toml"
plan="docs/RELEASE_PLAN.md"

test -f "$policy"
grep -Fq 'No Navheim behavior is implemented from memory' "$policy"
grep -Fq 'Documentation review and testing are part of implementation' "$policy"
grep -Fq 'If the required authoritative material is unavailable' "$policy"
grep -Fq 'Every behavioral implementation includes tests in the same milestone' "$policy"
grep -Fq 'Any missing item is a release blocker' "$policy"

for required in \
    'implementation_requires_verified_revision = true' \
    'implementation_requires_source_review_before_code = true' \
    'implementation_requires_section_mapping = true' \
    'implementation_requires_tests_in_same_milestone = true' \
    'implementation_requires_negative_and_adversarial_tests = true' \
    'implementation_requires_independent_evidence = true'; do
    grep -Fq "$required" "$manifest"
done
python3 scripts/validate_implementation_evidence.py "$manifest"

grep -Fq 'Before implementation, review and freeze every applicable' \
    .github/CONTRIBUTING.md
grep -Fq '## Standards And Evidence' .github/PULL_REQUEST_TEMPLATE.md
grep -Fq 'I added applicable positive, negative, boundary, malformed, adversarial' \
    .github/PULL_REQUEST_TEMPLATE.md
grep -Fq 'Before code, map exact document sections/tables/algorithms' \
    docs/release-checklist.md
grep -Fq 'source-first review of exact authoritative revisions' \
    docs/initial-idea.md
grep -Fq 'Tests ship in the same milestone as behavior.' \
    docs/IMPLEMENTATION_PLAN.md

grep -Fq 'Before implementation, review and freeze every applicable authoritative' \
    scripts/generate_release_plan.py
grep -Fq 'run and map all applicable positive, negative, boundary, malformed' \
    scripts/generate_release_plan.py

milestones="$(grep -c '^### v' "$plan")"
if [ "$milestones" -lt 3 ]; then
    echo "release plan has too few milestones to validate evidence rules" >&2
    exit 1
fi
regular_milestones=$((milestones - 2))
source_rules="$(
    grep -c '^- Before implementation, review and freeze every applicable authoritative' \
        "$plan"
)"
test_rules="$(
    grep -c '^- run and map all applicable positive, negative, boundary, malformed' \
        "$plan"
)"

if [ "$source_rules" -ne "$regular_milestones" ]; then
    echo "not every implementation milestone has the source-first rule" >&2
    exit 1
fi
if [ "$test_rules" -ne "$regular_milestones" ]; then
    echo "not every implementation milestone has the same-milestone test rule" >&2
    exit 1
fi

echo "implementation evidence policy passed ($regular_milestones implementation milestones)"
