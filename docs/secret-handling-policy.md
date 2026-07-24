# Secret and Sensitive Data Policy

Navheim may handle NTRIP/SUPL credentials, trust-store material, device
identifiers, precise positions, tracks, antenna/station coordinates, timing
data, and forensic captures.

- Core protocol types do not own credentials.
- Credential storage and TLS live in explicit integration crates.
- Debug and Display output redact secrets and precise location by default.
- Authorization headers, passwords, tokens, private keys, raw location
  histories, and full forensic captures are never logged by default.
- Configuration export is secret-free unless the caller explicitly selects an
  encrypted export path.
- Tests use synthetic credentials and locations.
- Reports minimize, encrypt, and access-control sensitive evidence.

If secret-bearing owned buffers are introduced, the release must review an
appropriate audited sanitization boundary rather than inventing wiping or
constant-time primitives.
