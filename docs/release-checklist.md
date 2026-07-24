# Release Checklist

1. Confirm the milestone's Goal, Deliverables, Verification, and Exit criteria
   in `docs/RELEASE_PLAN.md`.
2. Run the offline RFC/source gates and networked RFC errata and official-page
   freshness reviews; verify standards revisions, amendments, notices,
   licenses, local checksums, citations, coverage mappings, and test vectors
   for changed behavior.
3. Before code, map exact document sections/tables/algorithms and independent
   evidence to the implementation; stop if required material is unavailable,
   ambiguous, unofficial, or legally unusable.
4. Add applicable positive, negative, boundary, malformed, adversarial,
   conformance, differential, resource, fuzz and regression tests in the same
   milestone; document every not-applicable class.
5. Update code, tests, fuzz targets, docs, current status, changelog, crate
   READMEs, version matrix, release plan metadata, and release notes.
6. Check newest stable Rust, cargo tools, GitHub Actions, and every changed
   dependency.
7. Run `scripts/checks.sh`, Cargo deny/audit, SBOM validation, compatibility,
   MSRV behavioral tests once behavior exists, and milestone-specific gates.
8. Stop at the exact implementation/pentest sentence. Do not tag.
9. Use ignored root `PENTEST.md` only for temporary findings.
10. Fix findings, remove `PENTEST.md`, rerun all gates, and commit.
11. Confirm GitHub CI and CodeQL default setup.
12. Pentest/retest the exact implementation commit.
13. Commit only the permanent `security/pentest/vX.Y.Z.md` PASS report as the
    direct child of the reviewed commit.
14. Verify the report-only child and reviewed implementation parent produce
    identical package file lists, bytes and checksums.
15. Run `scripts/validate-release-readiness.sh vX.Y.Z`.
16. For `v1.0.0-rc.N`, confirm manifests already declare package version
    `1.0.0`; the RC is an unpublished repository tag.
17. Confirm final `v1.0.0` points to the exact approved RC commit and uses the
    retained archives without rebuilding or metadata changes.
18. Tag and publish only when explicitly requested.
19. Publish through `scripts/release_crates.py --require-tag`; wait for each
    dependency to index before publishing dependents.
