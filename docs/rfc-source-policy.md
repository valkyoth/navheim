# RFC Source Policy

Status: policy

Navheim keeps exact RFC Editor text as local references only for IETF-governed
boundaries. GNSS protocols remain governed by their operator, industry,
aviation, telecom, geodesy, or vendor specifications.

Requirements:

- fetch only exact HTTPS RFC Editor URLs allowlisted in
  `standards/rfc/SOURCES`;
- keep tracked RFC text byte-for-byte unmodified and checksum-locked;
- reject missing, extra, changed, empty, normalized, or locally writable RFC
  text;
- distinguish obsolete NTRIP interoperability references from the current
  HTTP and security rules that govern new behavior;
- record errata separately and never patch RFC text;
- review source, checksum, lifecycle, requirements, errata, implementation
  mapping, tests, and security impact together;
- consult current IANA registries where a protocol consumes registered values;
- perform no build-time or test-time downloads;
- never include RFC text in a crate package or claim it under Navheim's
  software license.

RFC review is intentionally narrower than Gjallarbru's STUN/TURN requirement
ledger: no RFC is a Navheim core GNSS protocol. Before an RFC-backed Navheim
surface is implemented, its owning release must still extract every applicable
normative rule, review verified and unresolved errata, map tests, and document
legacy conflicts. Supporting RFCs cannot be treated as “read once” references.

See [`standards/rfc/README.md`](../standards/rfc/README.md) for the exact
baseline and update procedure. External GNSS document handling is governed by
[`standards/licensing.md`](../standards/licensing.md) and
[`standards/sources.toml`](../standards/sources.toml).
