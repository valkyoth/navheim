# Standards Source Workspace

Navheim separates four different things:

1. `rfc/` contains immutable, checksum-locked RFC Editor text that may be
   reproduced unmodified.
2. `sources.toml` is the reviewed acquisition inventory for every external
   source family needed by the 1.0 plan.
3. `manifest.toml` becomes the conformance ledger: exact revision, section,
   implementation, test, errata, and migration evidence.
4. ignored `private/` contains developer-local PDFs, archives, licensed
   standards, registration-gated material, and vendor documents.

Run:

```text
scripts/standards-sources.py check
scripts/standards-sources.py fetch
scripts/standards-sources.py verify-local --require-downloads
scripts/standards-sources.py review-current
```

`check` is offline and runs in CI. `fetch` downloads only explicitly
allowlisted public HTTPS files into `private/`, locks them read-only, and
records local SHA-256 values. It never fetches paid, membership-only,
registration-gated, consent-gated, or hardware-profile-specific material.
Those documents are acquired manually and remain local.

`review-current` is a networked freshness aid. It checks expected revision
markers on official landing pages, but cannot prove conformance or replace
human review of revision history, errata, service notices, licensing, and
scope. Before an implementation milestone starts, its source records must be
frozen into `manifest.toml`.

The latest human acquisition review is
[`reviews/2026-07-24.md`](reviews/2026-07-24.md).

The inventory is complete for the present 1.0 roadmap, not for every possible
future GNSS-related standard. Newly accepted scope adds its authoritative
source before code.
