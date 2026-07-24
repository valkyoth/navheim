# Navheim 0.1.0 Release Notes

Status: implementation candidate; not tagged or published.

## Scope

This release initializes the security-first Navheim workspace. It provides the
dependency-free `navheim-core` crate, the dependency-free `navheim` facade, the
standards inventory policy, repository security controls, cross-version Rust
policy, CI, documentation, and audited publication tooling.

The architecture now defines a stable direction for timing integration:
Navheim will own GNSS time decoding, resolution, PPS/time-mark meaning,
uncertainty, health, authentication, integrity, and provenance. Downstream
clock frameworks may consume that API, but Navheim will not depend on them or
perform generic clock discipline and holdover.

The implementation and release plans also incorporate the initial
architecture/security gap review without replacing Navheim's broader roadmap.
They add explicit future stops for immutable artifacts and assessments, safe
bounded storage, executable preflight receipts, deterministic DSP, correction
anti-mixing, privacy/unsafe/platform evidence, strict release provenance, and
exact standards traceability.

The standards foundation now includes 25 exact, immutable RFC Editor
references for Navheim's HTTP, encoding, certificate, JSON and TLS boundaries,
plus a live-checked errata drift snapshot. Legacy NTRIP HTTP references are
explicitly separated from current secure behavior.

RFC integrity is enforced through exact source lists and SHA-256 bytes. Git
does not preserve general read-only permission bits, so CI does not require
mode `0444`; developers may still apply the optional local read-only guard.

The broader acquisition inventory covers 36 authoritative source families.
Seventeen freely downloadable GPS, Galileo, NavIC and IGS documents can be
fetched into an ignored local vault and protected by a local SHA-256 lock.
Paid, licensed, consent-gated, registration-gated and vendor-profile material
is metadata-tracked but must be acquired lawfully and remains outside Git and
crate archives.

A second coverage pass preserves that sequence while closing promised-scope
gaps with named releases for the navigation crate; RTCM, RINEX and
Earth-orientation products; typed PVT/orthometric outputs; SDR conditioning;
full inertial/fusion calibration and vector tracking; canonical assistance;
implementable RAIM/ARAIM contracts; a concrete RustCrypto adapter; CAN I/O;
independent signal vectors; and exact timing arithmetic, mapping and slot
state machines.

The third coverage pass resolves acknowledgement and CAN address-claim
ownership contradictions and makes the stable-Rust numerical strategy
explicit. It adds future stops for first-party deterministic `no_std` math,
bounded extension registration, all facade profiles, DGPS and ordered
degradation, solver/integrity separation, platform-complete Android support,
isolated discovery probes, bounded ASN.1 PER, exact SUPL/LPP matrices and
post-protocol RustCrypto integration.

The fourth coverage pass keeps all earlier work and adds 14 bounded releases
for a crate/capability DAG, honest resource-evidence categories, projected
coordinates, typed kinematics, safe processing extensions, conditional NavIC
messaging, complete DFMC/network-RTK/PPP matrices, optional GNSS science,
fixed-rate fusion, calibrated native AoA, SouthPAN coverage, and full
FPGA/GPU/external-DSP stage equivalence.

The fifth coverage pass adds five foundation releases without replacing later
solver or assistance work: bounded first-party linear algebra, conservative
statistical kernels, canonical signal definitions, deterministic
navigation/correction/product selection, and early acquisition hints.
Artifact-ID lifecycle stays in its existing owning milestone, while late
SUPL/LPP/mobile/receiver assistance translates into the early hint contract.

The sixth coverage pass corrects the linalg and signal-registry dependency
directions, then adds 11 bounded releases for UTC civil and precision-geodesy
time, runtime acquisition-decision receipts, deterministic multicore and
source supervision, capability-gated receiver control, and an opt-in snapshot
envelope with separate acquisition, tracking/navigation-store, PPP and fusion
restore profiles.

The seventh coverage pass corrects DSP/geo/executor dependency authority,
distinguishes snapshot corruption detection from authenticated sealing,
defines role-aware source composition, narrows parallel determinism to logical
ordering plus captured runtime traces, moves executable acquisition receipts
and snapshots after their state exists, separates raw and semantic store
restore, and adds receiver-configuration generation barriers.

The eighth coverage pass preserves those boundaries while making them
implementation-safe: `navheim-geo` exclusively owns coordinate mathematics
and `navheim-navigation` composes it; executor work units have scoped,
non-overlapping ownership and lossless bounded traces; snapshot authenticity,
confidentiality and privacy policy are orthogonal; same-role handover
invalidates dependent solver state unless an evidenced transform preserves it;
and receiver transactions are distinct from independently observed
configuration assessments. Two bounded stops add behavioral receiver
assessment and optional external AEAD/platform-keystore snapshot protection.

The ninth coverage pass removes direct SDR hardware mutation in favor of
side-effect-free preparation, reviewed immutable application plans,
configuration generations, transition invalidation and initialized-count
reads. Executor deadlines now distinguish requested/acknowledged cancellation,
deadline misses, unresponsive ownership and failures without pretending Rust
can kill a stuck borrowed thread. Snapshot protection gains authenticated
interpretive metadata, crash-safe nonce/counter/key rotation and four separate
platform adapter stops. Receiver assessments become interval-scoped
`ObservedConsistent`, while local-frame transformations remain exclusively in
`navheim-geo`.

The tenth coverage pass strengthens existing releases rather than adding
parallel subsystems. Borrowed executor jobs are confined to a scope that
cannot return before storage does, while owned asynchronous handles transfer
explicit planned leases and cannot recover them from unresponsive work.
Front-end application reports applied, rejected-without-mutation, partially
applied and state-unknown outcomes; partial or unknown coherent-array
transitions retire prior generations and block reads until reprobe and
revalidation. Snapshot authenticity, confidentiality and freshness are now
three independent dimensions. Rollback resistance requires trusted external
monotonic comparison and update, so authenticated counters and crash-consistent
encrypted file replacement cannot silently imply freshness.

The eleventh coverage pass resolves the remaining edge contracts inside those
same releases. `ExecutionHandle` is must-use; explicit terminal-result,
`join`, and `cancel_and_join` paths return ownership, while destruction of
nonterminal work—including during unwinding—invokes a non-panicking fail-stop
policy instead of joining or detaching. Front-end partial and state-unknown
outcomes preserve their original cause plus bounded command, rollback and
reprobe evidence; post-submission uncertainty or evidence overflow cannot be
reported as no-mutation. `CounterChecked` is only diagnostic comparison with
named non-rollback-resistant local state. Rollback-resistant sealing requires
an atomic digest-bound compare-and-advance or an exclusive expiring writer
reservation across seal, durable commit and monotonic advancement, with
concurrent writers and every crash boundary tested.

The twelfth coverage pass makes those contracts sound even when Rust
destructors do not run. Executor registration, not a handle, owns every
submitted lease, result and capacity slot; forgotten or manually suppressed
handles remain accounted and non-reusable until explicit shutdown. Invalid
handle/executor destruction uses allocation-free, non-unwinding
`std::process::abort()`, and memory soundness never relies on `Drop`.
Front-end `Applied` and `RejectedNoMutation` results structurally carry bounded
transaction evidence or private-construction proof, while remaining distinct
from observed consistency. Snapshot rollback transactions use a separate
suite-approved, domain-separated `SnapshotTransactionBinding` over the exact
canonical protected envelope; corruption/artifact digests cannot substitute,
and reservation expiry/reboot recovery uses authority monotonic and boot-
generation evidence rather than caller time.

The thirteenth coverage pass closes the remaining races and evidence limits.
Executor registry entries move atomically through registered, running,
terminal-unclaimed and exactly one claimed/discarded/shutdown-reclaimed state;
generation-bearing job IDs prevent ABA, and observing status never consumes a
result. An SDR no-command proof comes only from an unconsumed framework-issued
pre-submission token; preserving prior configuration also requires exclusive
device control and a frozen no-autonomous-change profile. Snapshot protection
now has a normative durable sequence from pending reservation through complete
envelope binding, candidate staging, authority commit, candidate promotion and
finalization. Every crash point has exclusive recovery, and an authority-
committed but unpromoted candidate is pending or unavailable—never a successful
rollback-resistant snapshot.

The fourteenth coverage pass resolves further lifecycle details in those
same milestones. Dispatch and cancellation-before-dispatch contend on one CAS,
so a cancellation winner proves the job cannot execute. Handle `Drop` performs
only terminal retirement; sealed, bounded cleanup separately destroys or
transfers results, returns leases, finalizes traces and advances a non-wrapping
generation before slot reuse. Snapshot recovery now freezes the restore,
writer-blocking and recovery action for committed, pending, authority-
committed, promoted-unfinalized and corrupt/unknown state, together with
bounded candidates, retained bytes, retries and deterministic cleanup.

The fifteenth coverage pass supplies the missing progress and privilege
boundaries without creating parallel releases. Executor cleanup is explicitly
caller-driven and bounded per poll and in total; admission reports
`CleanupRequired` instead of doing surprising work, shutdown drains cleanup,
and the executor is must-use. Safe state-owning payload storage is preferred;
`ManuallyDrop` may only use safe extraction in the 1.0 executor, with Miri,
Loom and Kani exactly-once evidence. Corrupt snapshot repair is a
separate Tier 3 capability limited to exact-current recovery or durable
namespace retirement followed by a fresh key/nonce/counter domain and explicit
continuity break. It cannot revive old state or silently weaken freshness.

The sixteenth coverage pass corrects a Rust borrowing conflict in v0.48.3
without weakening the lifetime-bound handle model. `poll_cleanup` takes a
shared executor borrow, allowing cleanup while unrelated handles remain live.
A private atomic guard admits one cleaner; concurrent calls return
pre-mutation `Busy`, callers cannot leak the guard, and each bounded poll
selects the lowest eligible generation-bearing job ID. Loom covers cleanup
against completion, result claims, handle drop, admission, another cleanup
caller and shutdown.

The seventeenth coverage pass separates cleanup mutation from trace mutation.
Invalid requests remain wholly mutation-free. A failed single-cleaner CAS
returns `Busy` with a bounded private contention receipt but changes no
registry, payload, cleanup, admission or trace state. In replayable profiles,
the supervisor must bind that receipt to a caller lane and logical call in the
bounded trace before reacting. Trace exhaustion follows the existing
fail-closed policy, and replay produces `Busy` from recorded evidence rather
than live contention.

The eighteenth coverage pass makes that ordering enforceable in safe Rust.
Replayable applications call only `ExecutionSupervisor::poll_cleanup`; the raw
executor primitive and contention receipt are crate-private, so callers cannot
ignore or forget an unrecorded receipt. The supervisor binds one executor,
plan and trace generation, allocates the logical call, records contention
before returning observable `Busy`, and reports trace unavailability or stops
if recording fails. Replay is consulted before any live cleaner CAS.

A repository-wide requirements pass then checked every tracked artifact class,
corrected the copied MIT donor identity, widened the source-size and
documentation-link gates to the whole applicable repository, and assigned
previously aggregate promises to bounded releases. Those stops now cover
CGGTTS common-view/all-in-view timing, exact SBAS providers, conditional
BeiDou messaging, FPGA/external-DSP inputs, generic and conditional receiver
families, all named GitHub-only tools, external evidence data, deployment
artifacts, and final requirement/claim traceability.

The standards acquisition catalog now also names the missing primary-source
families for BIPM/CCTF/ITU-R time transfer, Rust contracts, SDR/FPGA stacks,
Linux/BSD, Microsoft and Apple platform I/O, NovAtel, and conditional receiver
protocols. Their bytes remain local-only and exact profiles must be frozen
before implementation.

Behavioral implementation is now governed by a fail-closed evidence policy.
Exact authoritative revisions, amendments, errata and sections are reviewed
before code; implementation and test mappings are mandatory; applicable
positive, negative, boundary, malformed, adversarial, conformance,
differential, resource, fuzz, platform and regression tests ship in the same
milestone. Missing or ambiguous evidence stops implementation rather than
being guessed.

## Security

- Both published crates are `no_std`, dependency-free, and forbid unsafe code.
- Unknown registries, unknown Git sources, wildcard dependencies, yanked
  releases, and unreviewed advisory classes are denied.
- Release tagging requires exact-commit pentest evidence and a matching SBOM.
- GitHub CodeQL default setup is expected; no advanced CodeQL workflow is
  committed.

## Compatibility

- MSRV: Rust `1.90.0`.
- Pinned stable release toolchain: Rust `1.97.1`.
- Intended operating-system scope: Linux, Windows, macOS, FreeBSD, OpenBSD,
  NetBSD, Android, iOS, WASM, bare metal, and future Aesynx adapters.

## Non-Claims

This release does not decode signals or files, process RF, solve position or
time, access devices, use networking, or provide production GNSS/PNT behavior.
