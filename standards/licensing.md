# Standards Licensing Policy

Navheim follows constellation-operator ICDs, RTCM, NMEA, 3GPP, OMA,
ICAO/RTCA/EUROCAE, IGS, IETF, and public receiver specifications as appropriate.

- Do not commit paid, membership-only, classified, export-controlled, or
  redistribution-restricted documents.
- A local licensed copy stays outside Git. When lawful and useful, record only
  its title, revision, publisher, retrieval date, legal classification, and
  checksum. Checksums of licensed, personalized, or access-controlled bytes
  stay in the ignored local vault unless legal review approves publishing
  them.
- Public documents may be mirrored only when their terms explicitly permit it.
- Until that permission is reviewed, even freely downloadable non-RFC
  documents default to local-only storage under `standards/private/`.
- Do not reconstruct protected tables from unofficial copies.
- Source comments cite sections/tables without copying excessive protected
  text.
- Test vectors are committed only when their license permits redistribution.
- A new document revision creates a reviewed conformance profile and migration
  note; it never silently changes established behavior.
- Restricted civil/commercial and military services are represented honestly
  and are not decoded without public specifications and authorization.

The standards manifest is metadata and implementation evidence, not a
substitute for obtaining lawful access to a normative document.

Exact RFC Editor plain-text publications follow
[`docs/rfc-source-policy.md`](../docs/rfc-source-policy.md). They are the only
external standards bytes currently admitted to Git, remain under their own
notices, and are excluded from crate packages.
