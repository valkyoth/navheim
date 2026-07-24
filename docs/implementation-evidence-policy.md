# Implementation Evidence Policy

Status: mandatory, fail closed

No Navheim behavior is implemented from memory, an unofficial summary, an
unversioned web page, or a test written only to match the implementation.
Documentation review and testing are part of implementation, not follow-up
work.

## Source-First Rule

Before implementation begins, the milestone must:

1. identify every applicable authoritative document, exact revision,
   amendment, erratum, service notice, registry snapshot and legal-access
   class;
2. acquire and checksum-lock the exact document locally when permitted, while
   keeping restricted bytes outside Git and crates.io archives;
3. record the applicable sections, tables, figures, constants, algorithms,
   validity rules, unknown/reserved behavior and known limitations;
4. resolve conflicts between revisions and legacy profiles explicitly;
5. define the implementation owner, public claim and explicit non-claims in
   the standards/requirements evidence ledger.

If the required authoritative material is unavailable, legally inaccessible,
ambiguous, or cannot support interoperable implementation, work stops. The
capability remains unsupported, opaque, experimental, or represented only by
identifiers. Navheim does not guess.

For behavior not governed by an external standard, the milestone records the
owning architecture contract, reference algorithm/model, assumptions,
numerical limits and independent comparison source before implementation.

## Same-Milestone Test Rule

Every behavioral implementation includes tests in the same milestone and maps
them to the implementation and governing evidence. Applicable test classes
are:

- official or publisher-provided conformance vectors;
- independently produced vectors, receivers, implementations or numerical
  references;
- positive examples and exact boundary values;
- malformed, truncated, duplicated, reordered and unknown/future inputs;
- negative, adversarial, rollback, stale, replay and partial-commit cases;
- round-trip, chunk-boundary, differential and deterministic replay tests;
- resource, capacity, timing, cancellation and fault-injection limits;
- fuzzing for untrusted parsers/state machines;
- `no_std`, MSRV, platform, feature and scalar/optimized equivalence checks;
- regression tests for every fixed defect.

A test class may be marked not applicable only with a recorded reason. Ignored
tests, placeholder assertions, implementation-derived expected values and
self-generated-only conformance evidence do not close a requirement.

## Claim and Review Gate

A capability may change to `implemented` only when:

- exact source and section mappings are current;
- `implemented_by` and `tests` mappings are non-empty and machine-valid;
- independent evidence exists where correctness or interoperability requires
  it;
- all applicable positive, negative, boundary, adversarial and conformance
  tests pass;
- fuzz/resource/platform/security evidence required by the milestone passes;
- documentation, limitations, current status and release notes are updated;
- changed-code review and the exact-commit pentest stop are complete.

Any missing item is a release blocker. A passing build alone is not evidence
that behavior matches its specification.
