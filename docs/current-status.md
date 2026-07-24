# Navheim Current Status

Status: v0.1.0 implementation candidate

Navheim currently provides repository and crate foundations only.

## Implemented

- Cargo workspace with resolver 3 and edition 2024.
- Dependency-free, `no_std`, unsafe-forbidden `navheim-core`.
- Dependency-free, `no_std`, unsafe-forbidden `navheim` facade over
  `navheim-core`.
- Rust 1.90.0 MSRV and Rust 1.97.1 pinned release toolchain.
- CI compatibility checks across every stable release in the supported range.
- Linux, Windows, and macOS host checks.
- Dependency, advisory, license, source, SBOM, modularity, documentation, and
  release-metadata gates.
- Exact-commit pentest-before-tag release process.
- Initial standards inventory, licensing policy, architecture discussion,
  implementation plan, and complete pre-1.0 release plan.
- Checksum-locked local copies of 25 applicable IETF RFCs, an RFC errata drift
  snapshot, and a reviewed acquisition inventory spanning 36 GNSS, correction,
  exchange, aviation, telecom, geodesy, security, timing, receiver, SDR,
  numerical/scientific, Rust, and platform
  source families.
- An ignored, locally checksum-locked standards vault with safe allowlisted
  fetching for public documents; paid, licensed, consent-gated,
  registration-gated, and vendor-profile documents remain manual/local-only.
- One-way GNSS timing API boundary: Navheim will produce complete satellite
  timing evidence without depending on generic clock frameworks.
- Repository-wide requirements audit covering every tracked artifact class,
  correcting the MIT donor notice and expanding code-size/document-link gates
  to all applicable repository paths.
- Fail-closed implementation evidence policy: exact authoritative documents
  and sections are reviewed before code, and mapped tests ship in the same
  milestone; missing or ambiguous evidence blocks implementation.
- Audit-strengthened roadmap with 424 pre-1.0 implementation milestones plus
  the explicit production candidate and final release: targeted
  artifact/assessment, complete format/navigation/PVT/DGPS/fusion coverage,
  deterministic `no_std` math, bounded preflight/discovery/PER, explicit
  GNSS time transfer, SBAS provider, receiver/FPGA, GitHub-only tool, platform,
  correction/security/provenance and traceability stops are integrated without
  reducing the original civil/open scope.
- Fourth gap review integrated as bounded milestones for the dependency DAG,
  honest resource-evidence classes, projected coordinates, typed kinematics,
  safe processing extensions, conditional NavIC messaging, complete DFMC/
  network-RTK/PPP matrices, optional GNSS science, fixed-rate fusion, native
  calibrated AoA, and full accelerator-stage equivalence.
- Fifth gap review integrated without duplicating later solvers or assistance:
  bounded linear algebra, conservative statistical kernels, canonical signal
  definitions, artifact-ID lifecycle, deterministic model selection, and
  early acquisition hints now have explicit foundation ownership.
- Sixth gap review corrected the linalg and signal-registry dependency graph
  and added explicit civil/precision time, runtime search receipts,
  deterministic multicore/source supervision, safe receiver control and
  staged state snapshot/restore ownership without weakening immutable planning
  or Tier 0 thread-free behavior.
- Seventh gap review corrected DSP/coordinate/executor dependency ownership,
  snapshot authenticity versus corruption detection, role-aware source
  composition and lifecycle ordering; it added post-acquisition receipt/
  snapshot integration, semantic-store restore and receiver-configuration
  generation barriers with narrower replayable parallel guarantees.
- Eighth gap review makes geo/navigation ownership non-overlapping, specifies
  borrow-safe executor work units and lossless trace overflow behavior,
  separates snapshot authenticity from confidentiality/privacy, invalidates
  solver state during source handover by default, distinguishes receiver
  transactions from observed behavior, and adds bounded receiver-assessment
  and external snapshot-protection adapter stops.
- Ninth gap review closes direct SDR mutation with prepared plans,
  configuration generations, transition invalidation and initialized-count
  reads; distinguishes cooperative cancellation from missed/unresponsive
  workers; completes the snapshot cryptographic lifecycle with separately
  admitted platform adapters; narrows receiver evidence to
  `ObservedConsistent`; and preserves geo ownership of local-frame math.
- Tenth gap review makes those contracts representable and fail-closed:
  borrowed scoped jobs cannot escape or release storage while stuck, owned
  handles transfer explicit buffer/arena leases, front-end application reports
  no-mutation/partial/unknown outcomes including coherent-group evidence, and
  snapshot freshness is independent from authentication and encryption.
  Rollback resistance now requires a separately evidenced trusted monotonic
  compare/update authority; crash-consistent encrypted storage alone cannot
  claim it.
- Eleventh gap review closes the remaining lifecycle ambiguity without adding
  milestones: nonterminal owned executor handles now fail-stop on destruction
  instead of blocking or detaching, SDR apply failures retain their cause and
  bounded transition/rollback/reprobe evidence, and `CounterChecked` is
  explicitly non-fresh diagnostic evidence. Rollback-resistant snapshot
  sealing requires an atomic digest-bound compare-and-advance or exclusive
  expiring reservation across seal, durable commit and monotonic advancement.
- Twelfth gap review removes destructor-dependent assumptions: executor
  registration owns forgotten/leaked jobs and capacity until explicit
  shutdown, invalid executor destruction uses concrete `std::process::abort()`,
  and soundness survives destructor elision. SDR results structurally carry
  success/no-mutation proof or failure cause/evidence. Protected-snapshot
  transactions use their own suite-approved, domain-separated canonical
  binding and authority-monotonic/boot-generation reservation expiry.
- Thirteenth gap review completes those state machines without new milestones:
  executor completion/drop/claim/shutdown uses generation-safe atomic
  retirement, SDR no-command proof requires an unconsumed framework token plus
  exclusive control/no-autonomous-change evidence to preserve a generation,
  and rollback-resistant snapshots follow a durable pending, authority commit,
  candidate promotion and finalization sequence with exclusive crash recovery.
- Fourteenth gap review closes the remaining recycling and recovery ambiguity
  inside the same releases: executor dispatch and pre-dispatch cancellation
  share one CAS, handle `Drop` cannot run arbitrary destructors, bounded sealed
  cleanup precedes slot reuse and exhausted generations never wrap. Snapshot
  recovery now has an explicit restore/writer/action matrix for every durable
  state plus bounded transaction, candidate, retention, retry and deterministic
  cleanup rules.
- Fifteenth gap review makes those paths operable and privilege-bounded without
  adding releases: v0.48.3 now owns caller-driven budgeted cleanup,
  `CleanupRequired` admission backpressure, must-use shutdown and formally
  coupled safe-only exactly-once payload storage with Miri/Loom/Kani evidence.
  v0.189.2-v0.189.6 restrict corrupt-state repair to exact-current recovery or
  durable namespace retirement plus a fresh-domain continuity break, with
  anti-revival, security/invalidation and reacquisition requirements.
- Sixteenth gap review corrects the v0.48.3 cleanup API without weakening
  lifetime-bound handles: cleanup uses a shared executor borrow, remains
  available beside unrelated live jobs, and is serialized by an internal
  non-exported single-cleaner CAS. Concurrent attempts return pre-mutation
  `Busy`, selection is bounded and lowest-`JobId` deterministic, and Loom
  covers cleanup against every competing executor transition.

## Not Implemented

No GNSS/PNT behavioral capability is implemented. In particular, Navheim
cannot yet parse receiver/file/network data, process samples, decode a
constellation, compute satellite state, solve position or time, validate
integrity, authenticate navigation messages, or access platform devices.

## Next Stop

After the v0.1.0 exact-commit pentest/report stop, the next planned release is
v0.1.1: metadata-driven crate/tier/unsafe, strict SemVer, tag,
pentest-parent and package-provenance enforcement.
