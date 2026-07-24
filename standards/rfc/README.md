# RFC Reference Copies

This directory contains exact, unmodified plain-text publications downloaded
from the [RFC Editor](https://www.rfc-editor.org/). Navheim uses them only for
Internet transport, encoding, certificate, and security boundaries around its
GNSS protocols. NTRIP's historical HTTP profiles are retained for
interoperability review; current RFCs govern new secure behavior.

Navheim and its maintainers claim no copyright in these documents. Each RFC
retains its own notices and legal terms and is not covered by Navheim's
MIT/Apache-2.0 software license. The RFC Editor permits unmodified
reproduction. Never edit, reformat, annotate, normalize line endings, or
remove notices from these files.

GNSS signal, correction, exchange, aviation, telecom, geodesy, and vendor
specifications are not RFCs. Their metadata lives in
[`../sources.toml`](../sources.toml), while document bytes stay in the ignored
`standards/private/` vault unless a later legal review explicitly approves
redistribution.

## Integrity and Review

- `SOURCES` is the reviewed exact-URL and role allowlist.
- `SHA256SUMS` pins every byte of every tracked RFC.
- `scripts/fetch-rfcs.sh` downloads only missing allowlisted RFC Editor text.
- `scripts/verify-rfcs.sh` rejects changed, missing, extra, empty, or writable
  RFC copies.
- `scripts/lock-rfcs.sh` reapplies the local read-only guard.
- `scripts/test-rfc-sources.py` verifies the complete expected baseline.
- `scripts/rfc_errata.py` validates the reviewed errata snapshot and can
  compare it with the RFC Editor.
- `.gitattributes` prevents line-ending normalization.

Checksums and review are authoritative because Git does not portably preserve
read-only file permissions.

## Scope

The baseline covers:

- BCP 14 requirement language and ABNF;
- NTRIP v1/v2's legacy HTTP and authentication references;
- current URI, HTTP/1.1, HTTP caching, Basic authentication, and
  protocols-over-HTTP guidance;
- UTF-8, JSON, Base64, and Internet timestamps used at network/receiver
  boundaries;
- TLS 1.3, deployment policy, SNI, service identity, PKIX, and EC certificate
  encodings needed by optional transport and cryptography adapters.

It deliberately excludes NTP, NTS, PTP, STUN/TURN, QUIC, and generic
clock-discipline RFCs. Those are not Navheim protocol responsibilities.

The set is not a ceiling. A source is added when a planned or implemented
Navheim surface proves it is normative, security-relevant, or needed to
interpret a legacy profile.

## Update Procedure

1. Add the exact RFC Editor URL and a precise role to `SOURCES`.
2. Review whether the RFC is current, obsolete-but-required, or out of scope.
3. Fetch the untouched publication and add its checksum.
4. Review all RFC Editor errata; record applicability and security impact
   without changing RFC bytes.
5. Update standards mappings, tests, plans, and release notes together.
6. Run the full repository checks.

Published RFCs are immutable. Corrections are separate errata decisions or
new RFCs.

## crates.io Exclusion

Publishable crates use strict package allowlists. RFC text and the private
standards vault must never enter a crates.io archive.
