# Release Checklist

1. Confirm the milestone's Goal, Deliverables, Verification, and Exit criteria
   in `docs/RELEASE_PLAN.md`.
2. Run the offline RFC/source gates and networked RFC errata and official-page
   freshness reviews; verify standards revisions, amendments, notices,
   licenses, local checksums, citations, coverage mappings, and test vectors
   for changed behavior.
3. Update code, tests, fuzz targets, docs, current status, changelog, crate
   READMEs, version matrix, release plan metadata, and release notes.
4. Check newest stable Rust, cargo tools, GitHub Actions, and every changed
   dependency.
5. Run `scripts/checks.sh`, Cargo deny/audit, SBOM validation, compatibility,
   MSRV behavioral tests once behavior exists, and milestone-specific gates.
6. Stop at the exact implementation/pentest sentence. Do not tag.
7. Use ignored root `PENTEST.md` only for temporary findings.
8. Fix findings, remove `PENTEST.md`, rerun all gates, and commit.
9. Confirm GitHub CI and CodeQL default setup.
10. Pentest/retest the exact implementation commit.
11. Commit only the permanent `security/pentest/vX.Y.Z.md` PASS report as the
    direct child of the reviewed commit.
12. Verify the report-only child and reviewed implementation parent produce
    identical package file lists, bytes and checksums.
13. Run `scripts/validate-release-readiness.sh vX.Y.Z`.
14. For `v1.0.0-rc.N`, confirm manifests already declare package version
    `1.0.0`; the RC is an unpublished repository tag.
15. Confirm final `v1.0.0` points to the exact approved RC commit and uses the
    retained archives without rebuilding or metadata changes.
16. Tag and publish only when explicitly requested.
17. Publish through `scripts/release_crates.py --require-tag`; wait for each
    dependency to index before publishing dependents.
