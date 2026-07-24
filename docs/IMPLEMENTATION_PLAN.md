# Navheim Implementation Plan

Status: planning document

Crate name: `navheim`

1.0 target: a serious, security-first, independently tested Rust GNSS/PNT
platform supporting every publicly documented, legally implementable civil/open
signal and service in the frozen 1.0 standards baseline.

## Core Position

Navheim is not a GPS-only parser, an SDR demonstration, or a receiver SDK
wrapper. It is one layered platform whose canonical observation and time model
can be fed by RF samples, FPGA/DSP outputs, raw receiver measurements, decoded
messages, corrections, OS location providers, or archived data.

The facade must remain simple without hiding allocation, device access,
networking, degraded capability, authentication state, integrity state,
uncertainty, or provenance.

## Non-Negotiable Engineering Rules

- Publishable crates use edition 2024, resolver 3, MSRV Rust `1.90.0`, and
  remain compatible through pinned stable Rust `1.97.1`.
- Repository-only tools may require Rust `1.97.1`.
- The pinned stable toolchain, cargo security tools, dependencies, and GitHub
  Actions are checked for current versions before releases and dependency
  changes.
- Foundational, constellation, signal, solver, integrity, and format behavior
  is first-party and must not depend on another GNSS implementation.
- Navheim owns GNSS-derived time behavior and exposes it through its own
  dependency-free API. It never depends on Mundilfari or another generic clock
  framework; consumer-owned companion crates depend on Navheim.
- TLS and modern cryptographic primitives use reviewed adapter crates; Navheim
  does not implement them from scratch.
- Foundation and protocol crates are `no_std` by default and expose allocation
  only through explicit features.
- No core crate starts threads, selects an async runtime, opens devices, or
  uses networking.
- Side-effecting builders must first return an immutable reviewed plan receipt;
  device, credential, network and thread authority begins only after acceptance.
- Raw facts, normalized facts, corrections, assessments, evidence and policy
  decisions are immutable, separately typed and connected by bounded artifact
  identifiers. Later evidence never mutates an earlier fact.
- Protocol, constellation, solver, and format crates forbid unsafe code.
- Unsafe is isolated to reviewed FFI, DMA, or SIMD/platform modules with a
  safety contract, Miri evidence where applicable, and independent review.
- Hand-maintained code files must stay at or below 500 lines.
- Generated code records generator provenance and reproducibility; review also
  limits function/state-machine complexity rather than relying on file length.
- Every input length, offset, epoch, capacity, and resource calculation is
  checked.
- No input-dependent panic is permitted under declared resource limits.
- Untrusted input cannot select allocations, thread/channel counts, FFT plans,
  FEC iterations, candidate counts, queue growth or other work bounds.
- Every untrusted parser is bounded and receives unit, negative, property,
  conformance, and fuzz coverage.
- Standards constants cite authoritative sections or tables.
- Every implemented feature maps to `standards/manifest.toml`.
- Every release ends at an exact-commit pentest handoff before tagging.

## Capability Tiers

| Tier | Contract |
| --- | --- |
| 0 | `core` only, no heap, OS, hidden floating-point requirement, or unsafe code |
| 1 | explicit `alloc`, still no OS |
| 2 | explicit `std` for files, sockets, threads, serial, USB, and clocks |
| 3 | external integrations such as TLS, cryptography, platform APIs, and vendor stacks |

Each crate documents its default tier, optional promotions, exact structural
resource needs, target/toolchain/profile-specific stack evidence, measured
envelopes, caller assumptions, unavailable estimates, and floating-point
assumptions.
Enabling `std` must not change protocol/wire behavior. Tier 0 uses caller
buffers, explicit work budgets and allocator-free target evidence. Tier 1
documents every allocation point. Tier 2 documents threads, clocks, devices,
files, sockets, cancellation and authority. Tier 3 documents dependencies,
unsafe code, credentials, trust roots and platform guarantees.

A checked machine-readable crate/capability DAG records normal, optional,
build and development edges; feature unification; tier; `alloc`/`std`; unsafe;
TLS; cryptography; publication; and platform scope. CI rejects cycles,
undeclared edges and silent privilege or tier escalation.

## Crate Architecture

### Facade and foundation

- `navheim`: profiles, prelude, stable re-exports, source/solver composition,
  and capability planning.
- `navheim-core`: bounded collections, units, time, coordinates, identifiers,
  bit/FEC/checksum primitives, observations, ephemerides, corrections, events,
  errors, provenance, resource planning, and stable traits.
- `navheim-math`: dependency-free `no_std` deterministic elementary floating
  math, admitted conservative statistical kernels and narrowly scoped backend
  capabilities.
- `navheim-linalg`: zero-third-party-dependency `no_std` bounded
  fixed-capacity and caller-scratch linear algebra depending only on
  `navheim-math`, with narrow solver-facing APIs.
- `navheim-geo`: zero-third-party-dependency `no_std` mathematical coordinate
  transformations, projections, ellipsoidal geodesics, great-circle/rhumb
  primitives and ENU/NED/body/frame transformations depending on
  representation-only `navheim-core` plus `navheim-math`.
- `navheim-dsp`: zero-third-party-dependency `no_std` complex/fixed-point
  values, filters, resampling, FFT, acquisition, tracking, synchronization and
  estimators, depending on `navheim-math` for all admitted scalar functions.
- `navheim-sdr`: front-end traits, sample metadata, coherent arrays, band
  planning, deployment validation, and device adapter boundaries.
- `navheim-executor`: optional Tier 2 `std` worker, cancellation and
  bounded-queue adapter over canonical scalar work units; never a
  `navheim-dsp` dependency.

### Constellations and augmentation

- `navheim-gps`
- `navheim-galileo`
- `navheim-glonass`
- `navheim-beidou`
- `navheim-qzss`
- `navheim-navic`
- `navheim-sbas`

Each constellation crate owns code generation, acquisition hints, tracking
configuration, FEC/framing, raw and semantic message models, ephemeris
conversion, signal corrections, and relevant conformance vectors. One crate
per signal is explicitly rejected to avoid version and dependency
fragmentation.

### Solving and application primitives

- `navheim-pvt`: typed solution, DOP, age, contributing/excluded satellite,
  residual, convergence, vertical-datum and availability outputs.
- `navheim-rtk`
- `navheim-ppp`
- `navheim-integrity`: implementable RAIM/ARAIM hypotheses, risk allocation,
  alert/continuity/availability, protection-level and exclusion contracts.
- `navheim-fusion`: calibrated IMU models, mechanization, bounded real-time
  filters, optional allocated factor graph and observable reacquisition.
- `navheim-timing`: GNSS time resolution, time-only solutions, receiver clock
  estimates, time transfer, external PPS/time-mark semantic correlation,
  10 MHz/frequency-output status, calibrated delay, uncertainty, health,
  authentication, integrity, and adapter-facing events.
- `navheim-security`
- `navheim-navigation`: bounded waypoint/route/track models, geofences,
  segment policies and navigation-facing wrappers over `navheim-geo`; it
  depends on `navheim-geo`, does not reimplement mathematical primitives and
  does not claim road-network routing.
- `navheim-science`: optional calibrated scintillation, reflectometry,
  space-weather and remote-sensing artifacts with explicit product maturity.

Authentication, signal authenticity, message correctness, and solution
integrity remain separate types and policies.

`navheim-timing` does not implement generic PPS device capture, NTP/PTP,
cross-family clock consensus, local oscillator discipline, generic holdover,
or privileged clock adjustment. Those belong to consumers such as Mundilfari.

### Formats and interoperability

- `navheim-nmea`
- `navheim-nmea2000`: protocol/PGN semantics separated from CAN frame I/O.
- `navheim-rtcm`: frozen legacy and modern observation, ephemeris,
  correction, transformation and projection profiles.
- `navheim-ntrip`
- `navheim-rinex`: observation, navigation, meteorological and clock profiles
  with separately bounded compact/Hatanaka integration.
- `navheim-products`: precise products plus Earth-orientation/reference-frame
  inputs.
- `navheim-receiver`: read-only adapters by default; admitted control profiles
  use side-effect-free allowlisted command plans, ACK/NAK correlation,
  transition recovery, configuration generations, targeted invalidation,
  persistent-write authority, receiver-asserted read-back and separate
  behavior-based configuration assessments.
- `navheim-assist`: canonical trust/freshness/session model before SUPL, LPP,
  Android or receiver translations.
- `navheim-io`

### External adapters

- `navheim-tls-rustls`
- `navheim-crypto-rustcrypto`
- `navheim-snapshot-protection`: optional `std` external AEAD and
  platform-keystore authority bridge with a common protection lifecycle and
  separately admitted platform modules; canonical crates retain format/policy
  ownership and never hold platform keys.
- `navheim-uhd`
- `navheim-bladerf`
- `navheim-lime`
- `navheim-android`

These crates are optional and may carry reviewed external dependencies. They
must not redefine canonical GNSS behavior.

`navheim-crypto-rustcrypto` is the reviewed concrete conformance backend for
end-to-end OSNMA/QZNMA testing. Cryptographic policy and protocol behavior
remain in first-party canonical crates.

### GitHub-only tools

CLI, daemons, caster/station/survey services, inspectors, viewers, labs,
simulation, conformance, benchmarks, fuzz targets, capture tooling, FPGA
artifacts, packaging, service units, and deployments remain under `tools/`,
`fuzz/`, or other repository-only paths until separately admitted. They set
`publish = false` and may use Rust `1.97.1`.

Their named implementation stops are v0.36.3 (`navheim-capture`), v0.175.1
(`navheim-fpga`), v0.190.3-v0.190.11 (tool foundation, CLI, daemon,
caster/station/survey, inspector/viewer and lab), v0.196.1-v0.196.2
(`navheim-sim` and external data), v0.198.2-v0.198.3 (fuzz and conformance),
v0.201.1 (benchmarks), and v0.219.1 (packaging/deployment). A tool may reuse
published crates; it may not introduce a parallel GNSS implementation or
bypass canonical validation, evidence, privacy, or policy.

## Canonical Model Order

Implementation proceeds in this dependency order:

1. bounded collections, errors, and checked arithmetic;
2. physical units, exact atomic/civil/precision-geodesy time, deterministic
   `no_std` math, bounded linear algebra and admitted conservative statistical
   kernels;
3. core coordinate/reference-frame representations, then `navheim-geo`
   algorithms through `navheim-math`;
4. bit, checksum, parity, and FEC primitives;
5. extensible identifiers, canonical signal definitions and registries;
6. observations, ephemerides, corrections, provenance, events and the opt-in
   snapshot envelope;
7. capabilities, resource plans, deterministic source/sink polling and source
   supervision;
8. formats and deterministic replay;
9. scalar native DSP through `navheim-math`, dependency-free acquisition hints,
   separate deterministic Tier 2 execution and timestamp correctness;
10. independent signal/message vector admission, then GPS L1 C/A end-to-end
    as the first observable-to-fix path;
11. remaining GPS and constellations;
12. multi-GNSS solution quality, RTK, PPP, integrity, and authentication;
13. complete the stable GNSS timing observation/event API, then fusion,
    navigation, state-specific restore profiles, hardware, receiver control,
    OS, canonical assistance, and NMEA 2000;
14. optional calibrated science outputs and accelerator integrations only
    after their canonical observations, resource evidence and scalar paths;
15. simulation, fuzzing, audits, conformance, standards freeze, and release
    candidates.

RTK, PPP, and authentication do not become trusted surfaces until observation
time/phase correctness is independently proven.

## Canonical Artifact and Assessment Pipeline

The public type graph follows this non-destructive order:

```text
ingress and capture facts
  -> tracking estimates or raw protocol records
  -> raw observations and raw navigation messages
  -> validated messages and normalized observations
  -> corrected epochs and transactional navigation state
  -> solver input epochs
  -> position/time/attitude solution artifacts
       + targeted correctness assessments
       + navigation-authentication assessments
       + signal-authenticity evidence
       + integrity assessments
       + versioned policy decisions
```

Every derived value has an immutable artifact ID, bounded parent IDs and
derivation algorithm/version. Authentication, signal-source authenticity,
message correctness and solution integrity never collapse into one boolean.
Delayed authentication creates a new assessment targeting the original
artifact. No-fix/unavailable, convergence, rollback, withdrawal and coasting
are explicit events or lifecycle artifacts rather than valid solution modes.

Artifact/provenance IDs contain source namespace, reset generation and a
non-wrapping local sequence with explicit exhaustion/renewal. Reset never
reuses identity. Import/replay remaps untrusted namespaces while preserving
parents; identity is distinct from an optional content digest. Canonical
serialization, duplicate/collision handling and privacy-safe formatting are
part of the lifecycle contract.

Observation stages are separately typed: `TrackingEstimate`,
`RawReceiverObservation`, `RawSdrObservation`, normalized `Observation`,
`CorrectedObservation`, `ObservationEpoch` and `SolverInputEpoch`. Correction
ledgers and navigation-store transactions preserve issue, provider, station,
frame, session, generation, validity, uncertainty and provenance.
`navheim-core` owns canonical signal-definition/registry contracts;
constellation crates contribute physical fragments; RINEX/RTCM crates own
version-specific wire-ID mappings; and the facade composes selected fragments.
No constellation crate knows a later format standard, and no format crate
duplicates physical frequency, wavelength, rate, component, modulation or
native-time tables.
Navigation models, corrections and products are selected through explicit
epoch/applicability queries returning considered-candidate evidence and
`Selected`, `Ambiguous`, `Unavailable` or `Rejected`, never ambient latest-wins.

UTC civil labels preserve positive leap second `60` and hypothetical
negative-leap deletion semantics. Ordering/arithmetic resolves through an
identified UTC model to TAI. POSIX mappings are explicit ambiguous/lossy
adapters; leap smear is a non-claim. Gregorian/ordinal/Julian/MJD conversions
name their scale and precision; Julian/MJD uses integer day plus exact bounded
fraction/rational under a frozen proleptic-Gregorian/BCE convention. TT and
EOP-derived UT1 are typed
precision-geodesy arguments with product/revision/validity/uncertainty, not
ordinary GNSS scales.

## Resource, Progress, and Numerical Contracts

Tier 0 uses a small caller-driven vocabulary: bounded `Push`, `Poll`,
`Transform`, `Plan` and `Reset` contracts. Snapshot/restore is opt-in only
through a minimal versioned bounded envelope carrying algorithm/schema,
source/generation, validity, provenance, model/calibration/product identities,
capabilities, byte/work limits and corruption digest. Authenticity is
`Untrusted`, `IntegrityChecked` or `Authenticated`; confidentiality is
independently `Plaintext` or `ExternallyEncrypted`; freshness is independently
`Unchecked`, `CounterChecked` or `RollbackResistant`. Unkeyed digests provide
no authenticity. Authentication requires an injected external MAC/signature
authority but establishes no freshness; confidentiality requires external
AEAD/platform-keystore authority; rollback resistance requires trusted
external monotonic comparison/update. `CounterChecked` only proves that an
authenticated structurally valid counter was compared with named local state
that is not qualified as rollback-resistant; it cannot satisfy guaranteed-
freshness policy. Profiles classify sensitive fields, minimize included state,
require storage/export consent and retention, exclude contents from ordinary
debug/error output and document owned-plaintext zeroization limits. Restore
treats bytes as untrusted, checks compatibility, remaps provenance, validates
invariants and commits atomically.
The protection envelope has opaque extensible scheme/suite, authority,
key/version, nonce-allocation, associated-data schema, rollback counter,
ciphertext/tag length, creation/expiry and rotation fields. Associated data
authenticates every interpretive outer field. Unknown/downgraded suites fail
closed. `SnapshotTransactionBinding` is a distinct opaque type created by the
external authority using a suite-approved collision-resistant hash or MAC over
the exact canonical protected envelope, including ciphertext/tag and
authenticated metadata. It domain-separates purpose, authority, namespace,
suite/version and counter; noncanonical encodings fail and corruption/artifact
digests cannot convert into it. The binding is an authority record/sidecar
excluded from its own input and is computed only after the protected envelope
is final.

The normative transaction durably records `Pending` authority reservation
(namespace/counter/nonce/transaction/authority-expiry/boot generation), seals
and binds the envelope, durably stages the candidate, atomically advances to
`AuthorityCommitted`, durably promotes exactly that candidate, then finalizes
`Committed` before returning rollback-resistant evidence. Recovery is defined
at every boundary. Authority commit followed by failed promotion is pending or
fail-closed availability loss, never success. Recovery and a new writer cannot
both commit; cancellation is pre-authority-commit only; reboot, rotation and
migration must resolve/carry pending state. Reservation expiry uses authority
monotonic state/boot generation, never UTC/wall/caller time. Counter
exhaustion, cloned/restored authority state and every crash boundary fail
closed. Outer resource validation precedes decryption into caller buffers; and
authentication failure is uniform.

The common bridge freezes one recovery matrix: `Committed` restores only the
exact active binding and permits a new writer; `Pending` permits only the
previous committed restore under the same namespace lock/pre-commit
linearization while blocking writers until resume/cancel; `AuthorityCommitted`
forbids older restore and blocks writers until verified promotion/finalization
or unavailability; `PromotedUnfinalized` is usable only after synchronous
verification/finalization; and `CorruptOrUnknown` blocks restore and writers
pending a separately enabled Tier 3 repair capability. Repair may only verify
and recover the exact current authority-bound candidate through the normal
state machine, or durably retire the namespace/key/counter and establish a
fresh identity/key/nonce domain with an explicit continuity break. It cannot
reset an in-namespace counter, accept older state, reuse reserved nonces,
discard unresolved authority evidence or downgrade to `CounterChecked`;
missing durable anti-revival proof makes repair unavailable. Repair emits
security/invalidation evidence, invalidates restored assessments and requires
affected algorithm reacquisition/reconvergence. Receipts and profiles bound
active namespaces, one writer transaction per namespace, pending records,
staged/retained candidates,
retained bytes, retries and recovery work. Cancellation and supersession have
deterministic cleanup rules, while ordinary cleanup cannot remove an
authority-committed, promoted-unfinalized, corrupt or unknown candidate.
Concrete Linux/BSD, Windows, Apple and Android authority profiles are separate
milestones behind the common bridge. Authorities report separate cryptographic
verification, durable commit, monotonic compare/update, crash recovery and
key/counter migration evidence. Atomic file replacement plus AEAD is only
crash-consistent; it is not rollback-resistant against old-file restoration.
Missing qualified monotonic state remains `Unchecked` or `CounterChecked`.
Prior authentication, signal-authenticity, correctness, integrity and policy
assessments are invalidated or reverified rather than restored as authoritative.
Parsers report consumed length and
either make progress or request more input. Large events use borrowed views or
caller-provided bounded slots.

Every execution pipeline is created from a checked immutable `PlanReceipt`.
Each field is classified as an exact structural amount, a
target/toolchain/profile-specific static upper bound, a deterministic work
bound, a measured envelope, a caller assumption, or an unavailable estimate.
Portable plans never overstate stack, throughput, or latency certainty. Each
input block is checked against the applicable receipt bounds.
Invalidation and security events have sequence, source generation, target
artifact, effective interval and mandatory-withdrawal semantics. Queue
pressure cannot silently discard them: the source stops, explicitly coalesces,
or requires resynchronization.

Tier 0 and `navheim-dsp` remain thread-free. Separate `navheim-executor` takes
a caller-chosen worker count and bounded queues. Validated partitions create
deterministically identified ordered work units with immutable inputs,
exclusive output/scratch, checked non-overlapping regions, scoped caller-buffer
lifetimes, explicit `Send`, no hidden shared mutation and single-worker
stateful-channel ownership until deterministic handback. Cancellation cannot
detach work retaining borrowed storage; result slots and merge failures are
bounded. `CancellationRequested`, `Cancelled`, `DeadlineMissed`,
`WorkerUnresponsive` and `WorkerFailed` are distinct states. Deadlines do not
kill threads or release/reuse borrowed buffers. Only bounded first-party work
or admitted cooperative extensions may run; blocking I/O/external stages need
caller-owned process isolation for hard termination. Logical partition/merge
and event/invalidation order are deterministic. `PlanReceipt` fixes trace
capacity and only semantics-affecting nondeterministic facts enter replay.
Overflow stops/resynchronizes or marks replay unavailable, never drops facts.
Panic is recoverable only for admitted unwind profiles; abort or permanently
stuck work is process-terminal. Floating reductions are bit-exact only where
specified, otherwise tolerance-bounded. Scalar equivalence is verification
evidence, not mandatory duplicate production computation.

`ExecutionScope<'scope>`/`ScopedJob<'scope, ...>` represent borrowed work:
unresponsive status is pollable inside the scope, but jobs/borrows cannot
escape and scope exit waits for ownership. `#[must_use] ExecutionHandle`
is a lifetime-bound claim token for an authoritative executor registry entry;
the registry/worker, not the handle, owns planned buffers, result and slot.
Non-reusing generation-bearing job IDs prevent ABA. Registry state is
`Vacant(g) -> Registered -> {Running,
TerminalUnclaimed(CancelledBeforeDispatch)}`, then
`Running -> TerminalUnclaimed -> {Claimed, Discarded, ShutdownReclaimed} ->
Cleaning -> {Vacant(g+1), Retired}` with release/acquire publication of
results and leases. Dispatch and pre-dispatch cancellation compete on one CAS;
a cancellation winner proves the worker cannot execute. Generation exhaustion
retires the slot or requires a whole-executor namespace renewal after every
entry is reconciled; it never wraps.
`status(&self)` only observes; consuming `try_terminal_result` claims or
returns the handle; `join`/`cancel_and_join` wait and claim. Drop succeeds only
by atomically retiring `TerminalUnclaimed -> Discarded` and never runs caller
or generic destructors, returns leases or finalizes traces; observing
registered/running state aborts. Completion/drop ordering is determined by
their atomic linearization. Shutdown uses the same registered CAS for
cancel-before-dispatch; running work must cancel/join and publish terminal
before shutdown reclaims it. Claimed/discarded/shutdown entries are recycled
only by a separate bounded cleanup path after result transfer/destruction,
lease return, trace finalization and checked generation increment.
No quarantine/reaper or executor-ownership-transfer profile is admitted for
1.0.

Cleanup is caller-driven through public
`ExecutionSupervisor::poll_cleanup(&self, &mut CleanupLane, &Executor,
CleanupBudget)`, returning
`Result<CleanupProgress, SupervisedCleanupError>`. Progress distinguishes
complete from more-required and reports bounded counts/work without a hidden
wakeup contract. The non-cloneable, must-use supervisor is bound to one
executor namespace, `PlanReceipt` and trace generation; mismatched/duplicate
authority fails. Safe synchronized trace state supports concurrent shared
calls without unsafe `Sync`. `PlanReceipt` privately creates a bounded set of
must-use, non-`Copy`, non-cloneable `CleanupLane` capabilities before
execution, with no public constructor or serialization/deserialization path.
Each lane has a deterministic `CleanupLaneId`, checked non-wrapping per-lane
sequence and binding to the supervisor, executor namespace, plan and trace
generation. Mutable borrowing prevents concurrent reuse of one lane; separate
planned lanes admit concurrency. Lane identity never comes from call arrival,
CAS order, OS thread IDs or async-runtime task identities. No hidden worker/
reaper exists.

After mutation-free lane/supervisor/executor/generation and budget validation,
the supervisor forms the next `(CleanupLaneId, CallSequence)`. Live mode
atomically reserves the worst-case bounded call-event record and moves the
lane to that active call before CAS. Reservation covers either `Busy` or a
successful grant and the maximum exact result evidence permitted by that
budget. Reservation failure leaves the sequence unadvanced and returns
`TraceUnavailable` before executor CAS/mutation. Replay mode instead retains
the active key while reading the finalized event without trace mutation.
Only completed `Busy`/`Granted` handling advances the sequence;
`ReplayPending` does not. Stale, duplicate, exhausted and cross-supervisor
lanes likewise fail before executor mutation.

The supervisor then invokes a crate-private executor primitive in live mode.
The shared executor borrow keeps cleanup usable while unrelated lifetime-bound
handles remain live. An internal atomic single-cleaner CAS serializes cleanup;
a loser returns `CleanupStartError::Busy(CleanupContentionReceipt)` before
registry, payload, cleanup or admission mutation, and the raw primitive never
mutates trace state. The failed CAS is its linearization point. A winner
assigns the next checked non-wrapping global `CleanupOrder` and returns a
private `CleanupGrantReceipt` while the sealed guard remains owned inside the
supervisor call. The grant header is written into the reserved event before
cleanup mutation. Neither receipt nor guard crosses the public boundary.
Every normal return releases the guard explicitly. Safe `std` synchronization
and automatic trait bounds are required; no handwritten unsafe `Sync`
implementation is admitted.

`PlanReceipt` bounds cleaning entries, lane count, calls per lane, successful-
grant count/global order, lane/order exhaustion and fresh supervisor/lane/
trace-generation renewal, total/per-poll work, exact selected/retired identity
evidence, every replay-required call-event record and trace capacity.
Forgetting a lane only forfeits its bounded remaining calls; the executor
primitive retains no receipt registration/count state, while the supervisor
and lane capabilities own bounded logical-call/trace state.
Admission never cleans implicitly and returns
`CleanupRequired` when only dirty slots remain. Consuming shutdown reconciles
jobs and then drains bounded cleanup. Cleanup ordering, retirement and
semantics-affecting outcomes enter the deterministic trace; each poll scans
within its bound and chooses the lowest eligible generation-bearing `JobId`.
Every replay-relevant call finalizes one bounded `CleanupCallEvent` whose
`Busy` or `Granted` disposition binds the lane/call key, normalized budget and
executor/trace generations. `Granted` also binds global `CleanupOrder`, exact
bounded selected/retired `JobId` lists, work used and `CleanupProgress`; a
digest cannot replace exact identities. Selected entries remain non-reusable
`Cleaning` until the reserved event is finalized, after which states/progress
may be published and the guard released. Incomplete records are never
replayable; post-grant recording corruption is fail-stop or makes the
executor/trace generation unavailable, never ordinary unrecorded progress.

The opaque, must-use, non-cloneable, non-deserializable contention/grant
receipts bind executor namespace, plan/trace generation and their CAS
observations. The primitive and receipts remain crate-private. A loser
finalizes the reservation as `Busy` before returning observable `Busy`; stale,
duplicate or misbound lanes, receipts and orders fail. Replay looks up the
exact `(CleanupLaneId, CallSequence)` before any live CAS. `Busy` returns
directly. `Granted` executes only at its recorded next global order under an
ordered replay gate; an early call returns non-semantic `ReplayPending` while
the lane retains the same active call for its next poll. Replay checks budget,
predicted selection, exact selected/retired identities, work and progress
before advancing its cursor. Missing, duplicate, exhausted, incomplete or
contradictory events/orders make replay unavailable; post-mutation mismatch is
fail-stop. Thus callers cannot exchange results under a different schedule.
Only `Busy` may be omitted by a `PlanReceipt`-proved inert policy; successful
grants/results remain recorded for replayable concurrency. Every profile still
uses the supervisor and planned lane; no public raw escape exists. `Executor`
is `#[must_use]`; dropping it with any non-vacant payload-owning/cleaning entry
uses the same fail-stop abort rule.

Registry storage uses safe state-owning enums/`Option<T>`. `ManuallyDrop`, if
retained for layout, may use safe `into_inner`; unsafe take/manual-drop payload
extraction is excluded from the 1.0 executor. Any future unsafe layout requires
a separate milestone and unsafe-policy amendment. Lifecycle and payload-
initialization state cannot diverge and exactly one path
extracts or destroys each payload. Only sealed first-party cleanup may destroy
in-process payloads; arbitrary extension cleanup needs isolation. Admitted
unwind builds catch cleanup panic and immediately abort without unwinding
through registry invariants. Miri covers extraction/destruction/panic; Loom
covers cleanup versus completion, claim, drop, admission, cleanup and shutdown;
and Kani proves bounded exactly-once ownership. Handle `Drop` remains only the
retirement CAS.

Forgetting/leaking a handle forfeits its result but leaves the entry, leases
and capacity registered; completed unclaimed entries cannot be reused.
Consuming executor shutdown cancels/joins every registered job, including
forgotten handles, owns all remaining `ShutdownReclaimed` transitions, drains
cleanup, and an unresponsive job traps shutdown. Executor drop with any
unreconciled or uncleaned entry calls
`std::process::abort()` without allocation, formatting, panic or unwind;
pre-abort in-memory reason is best-effort and not durable/emitted evidence.
Forgetting the executor leaks all registered capacity until process
termination. Soundness never depends on a destructor running, and no hidden
`Arc`, allocation, worker or lease bypasses planning. Lease state is
`CallerOwned -> Submitted -> WorkerOwned -> Returned`; cancellation requests,
deadline misses and unresponsive reports do not change ownership.

The facade source supervisor operates only on explicitly opened sources.
Loss/change emits gap and withdrawal before bounded caller-authorized retry or
reselection. Same-role replacement generations cannot overlap without a
declared transition. Different roles compose only through the checked
role/clock/session/calibration/provenance/epoch compatibility graph. Failover
cannot silently lower accuracy, integrity, authentication or trust policy.
Same-role replacement invalidates receiver/inter-system clock biases,
antenna/lever-arm calibration, carrier ambiguities/cycle-slip continuity,
correction ledgers, smoothing filters, timing/PPS mappings and integrity/
authenticity assessments by default. Survival requires an explicit calibrated
handover transform with clock mapping, uncertainty growth and provenance;
outputs expose gap, discontinuity, reconvergence or bounded coasting.

Receiver control records command bytes, ACK/NAK, read-back and timing only in
a `ControlTransaction`. A separate `ConfigurationAssessment` compares
observable rate, signal, protocol, time-pulse and correction-ingestion behavior
against the requested generation. It carries interval, evidence sources,
coverage, uncertainty and unverifiable fields. Read-back alone is
`ReceiverAsserted`; `ObservedConsistent` is limited to evidenced behavior and
does not prove internal configuration or signal authenticity. Reset,
firmware/device identity change and contradictory stream evidence invalidate
the assessment.

SDR configuration follows `capabilities -> prepare -> apply`; preparation is
side-effect free and application accepts only an immutable reviewed plan.
Every transition creates a non-reused front-end generation binding device/
firmware, clocks, RF ports/groups, tuning/bandwidth/rate, encoding/IQ/scaling,
gain/AGC/power, calibration and effective interval. Retune/change drains or
invalidates prior sample blocks and capture mappings, resets affected DSP/
tracking and emits gaps/discontinuities. Reads report initialized count,
block/configuration generations, mappings, gaps, overruns and explicit
data/end/would-block state. Device assertions remain separate from observed
sample-rate/timing/calibration consistency.
Apply returns proof-carrying `Applied { configuration, evidence }`,
`RejectedNoMutation { cause, proof }`, `PartiallyApplied { cause, evidence }`
or `StateUnknown { cause, evidence }`. The framework privately issues a linear
pre-submission token; acquiring exclusive Navheim command transport consumes
it, making no-mutation proof structurally impossible thereafter. Third-party
adapters cannot mint proof. The proof means only no command crossed Navheim's
boundary. Prior-generation preservation also requires a live exclusive
device-control lease and frozen no-autonomous-change profile; another
controller, reset/identity change, lease loss or possible autonomous mutation
is `StateUnknown`. Applied evidence binds the new configuration and required
per-device commands/ACK/read-back, but remains only an adapter/device
transaction assertion—not independently observed consistency. Timeout,
disconnect, lost acknowledgement, post-submission transport failure, uncertain
rollback or required proof/evidence-capacity exhaustion is `StateUnknown`;
overflow is recorded rather than discarded.
Partial/unknown outcomes retire the prior generation without activating the
intended one, invalidate samples/mappings/calibration/DSP/tracking, prohibit
reads and require reprobe plus a new plan. Coherent arrays use a prepared group
transaction with bounded per-device evidence; coherence is unavailable until
every device succeeds and shared clock/timestamp calibration is independently
revalidated. Rollback attempts are evidence, not assumed success.

Because canonical crates forbid unsafe code, bounded collections use an honest
safe representation such as initialized storage, `[Option<T>; N]`,
caller-owned slices or domain-specific arrays. The API documents representation
cost and does not promise a zero-overhead general `FixedVec` that its safety
policy cannot implement.

Tier 0 interchange values use exact scaled integers or reduced rationals.
Floating APIs reject non-finite values. Each numerical algorithm names its
backend, rounding/overflow behavior, state ordering and units, rank/condition
tests, convergence, tolerance and failure behavior. Fixed-point kernels define
bit-exact replay; floating kernels define numerical replay with explicit FMA,
denormal and platform policy. Optimized kernels are compared against the
normative scalar implementation. A broad public `Scalar` abstraction is not
stabilized before concrete algorithms prove the required operations.

`navheim-math` is the normative pure-Rust scalar source for `sqrt`/`hypot`,
trigonometry, `atan2`, logarithm/exponential and admitted derived functions.
It specifies domains, exceptional values, subnormals, argument reduction,
rounding and error bounds against high-precision references. Runtime
twiddles/coefficients are planned into caller storage; audited fixed tables are
versioned evidence. Platform math and target-specific `core::arch` paths are
optional reviewed backends with scalar equivalence. Nightly
`core::simd`/`std::simd`, OS `libm` assumptions and post-MSRV APIs are forbidden
from the baseline.

`navheim-linalg` admits only bounded solver-required storage, QR,
Cholesky/LDLT, triangular solves, rank updates/downdates, square-root updates
and rank/condition estimates. It depends only on `navheim-math` for admitted
scalar operations and cannot reimplement them or call platform math. It
rejects dimension/scratch overflow, aliasing,
singular, indefinite, non-finite and badly scaled cases explicitly. Production
least squares cannot silently use unqualified normal-equation inversion.

Statistical kernels are limited to admitted normal and chi-square
tails/CDFs/quantiles with explicit confidence/degrees-of-freedom domains,
log-probability paths, monotonicity and approximation bounds. Integrity and
protection thresholds round conservatively, so approximation error cannot
understate risk or make acceptance more permissive.

An early dependency-free `SearchAid`/`AcquisitionHint` carries bounded,
expiring approximate time/location/velocity/orbit and Doppler windows with
source, generation, uncertainty and trust class. The immutable `PlanReceipt`
bounds maximum blind-search work, channels and scratch. A distinct immutable
`SearchExecutionReceipt` records runtime hint decisions, accepted/rejected
windows, actual work, fallback and deterministic order. Poisoned/conflicting
hints fall back to bounded blind search. Late assistance protocols translate
into this artifact and never use it to resolve canonical time, position or
trust.

Format profiles are not aggregate claims. RTCM legacy observations and
surveying transforms/projections, each RINEX observation/navigation/
meteorological/clock generation, RINEX 4 picosecond fields, compact codecs and
Earth-orientation products have separate versioned stops. Decompression
receipts bound bytes, records, lines and expansion ratio before decoded data
enters an ordinary parser.

PVT exposes DOP families, solution age, contributing/excluded satellites,
fix/convergence taxonomy, residuals and exclusions as typed results.
Orthometric height requires an identified geoid/vertical-datum artifact and
cannot be confused with ellipsoidal height. The sequential GNSS-only estimator
is independent from multi-sensor fusion and has explicit initialization,
convergence, reset and unavailable states.

Native front-end conditioning validates encoding, byte/IQ order, scaling,
clipping, quantization, calibration and AGC state before DC/IQ correction or
bounded mitigation. Every blanking/notching action creates distortion
evidence. SIMD is prohibited until its alignment, aliasing, feature-detection,
fallback and unsafe contract is independently reviewed.

RAIM/ARAIM contracts name fault hypotheses, integrity-risk allocation, alert
limits, time-to-alert, continuity, availability, correlation assumptions,
solution separation, exclusion exhaustion and re-admission. Missing required
inputs produce unavailable protection levels. SBAS evidence stays a separate
targeted input.

The PVT solver emits solution, residual and exclusion facts under measurement
admission policy. A separate integrity assessor consumes those immutable
artifacts and emits targeted assessments; solver configuration never makes an
ordinary solution integrity-approved. Code DGPS is a distinct typed solution
and cannot be inferred from RTK-float state.

Profiles expand to versioned printable canonical configuration and fail on
missing capability. Discovery enumerates bounded candidates, isolates probes,
ranks deterministically with explanations and never opens devices. Assistance
is canonical before Android/SUPL/LPP translation; PER parsing has independent
bit/work/nesting receipts. NMEA 2000 owns pure address-claim decisions while
platform I/O only executes frames and lifecycle actions.

## GNSS Timing and Consumer APIs

Navheim owns every step required to determine time from GNSS: native system
times, transmitted UTC/leap models, rollover resolution, satellite and
receiver clock corrections, receiver protocols, time-only solutions,
PPS/time-mark and frequency-output meaning, delay calibration, uncertainty,
health, authentication, integrity, and provenance.

Navheim exposes dependency-free `no_std` timing types and a deterministic
`GnssTimingSource`-style event boundary. Events include observations, model
changes, ambiguity, gaps, discontinuities, invalidations, and security
transitions. A valid sample can therefore be withdrawn without a consumer
having to reinterpret GNSS protocols.

Generic clock behavior stays outside Navheim: physical PPS capture, NTP/NTS,
PTP, clock-family consensus, system/PHC adjustment, oscillator servos, and
holdover after GNSS evidence expires. A consumer-owned companion crate, such
as `mundilfari-navheim`, may depend on Navheim and map its exact timing evidence
into the consumer's clock types. Navheim never depends on that adapter or
consumer.

One consumer adapter covers every constellation exposed by Navheim. Consumers
must not recreate separate GPS, Galileo, GLONASS, BeiDou, QZSS, or NavIC time
decoders around the same clock framework.

The normative architectural contract, provisional type shapes, correlation
model, security invariants, and adapter verification requirements are in
[GNSS_TIMING_API.md](GNSS_TIMING_API.md).

## Standards Discipline

`standards/sources.toml` is the reviewed acquisition inventory;
`standards/manifest.toml` is the machine-readable conformance source of truth.
Exact RFC Editor text is immutable and checksum-locked under
`standards/rfc/`; other external document bytes default to the ignored local
vault. Candidate documents are not implementation claims. Before a feature
starts:

1. run the networked source/errata freshness reviews and confirm the current
   official or legally licensed revision;
2. verify the local byte lock and record publisher, revision,
   publication/retrieval dates, license class, and
   local-copy policy;
3. review amendments, errata, service notices, registries, replacement
   relationships, and legacy conflicts;
4. cite sections/tables in code;
5. map implementation crates and tests;
6. add official, independent, generated, and adversarial evidence;
7. preserve unknown/reserved fields where the standard permits;
8. update coverage and known limitations.

Aggregate families are inventory leads, not implementation records. Before
code begins, split them into exact documents, revisions, amendments, notices,
assignment snapshots and legally retained vectors. Each implemented record
maps crate/module, sections/tables/constants, official and independent vectors,
adversarial tests, feature/profile, known limitations and legal-access class.

Tests ship in the same milestone as behavior. Every applicable positive,
negative, boundary, malformed, adversarial, conformance, differential,
resource, fuzz, platform and regression class is mapped to the implementation;
a not-applicable class requires a recorded reason. Missing or ambiguous
authoritative material blocks implementation and support claims. The
fail-closed rule is normative in
[implementation-evidence-policy.md](implementation-evidence-policy.md).

Paid, consent-gated, registration-gated, personalized, or redistribution-
unclear standards are never committed. Builds and tests never download
standards. New revisions create versioned conformance profiles rather than
silently changing behavior.

## Testing Program

Every release adds evidence at the lowest relevant layer:

- unit and boundary tests;
- checked-arithmetic and capacity tests;
- property and round-trip tests;
- official and operator-provided vectors;
- independent receiver and implementation comparisons;
- fuzz targets and committed small regression seeds;
- numerical reference and near-singular tests;
- deterministic replay;
- live-sky and multi-day tests;
- shielded or conducted RF fault scenarios;
- platform, `no_std`, MSRV, Miri, sanitizer, Kani/model-checking, and
  performance evidence where applicable.

Once behavioral core code exists, its tests run at the MSRV rather than only
compiling there. Miri validates safe wrappers and ownership models, Kani
validates bounded arithmetic/state machines, Loom validates concurrency and
invalidation ordering, and sanitizers/hardware tests validate native adapters.
No tool is credited for a boundary it cannot execute.

Generated GNSS-like RF must never be radiated into an open environment.

## Platform Strategy

The canonical crates avoid assumptions that prevent Linux, Windows, macOS,
FreeBSD, OpenBSD, NetBSD, Android, iOS, WASM, bare metal, or future Aesynx
support. Platform adapters are independently feature-gated and tested.

iOS support must not claim raw measurements unless the platform actually
provides them. WASM does not claim direct hardware access. Aesynx remains a
future adapter target and does not alter core types.

## Security Program

The threat model covers malicious RF, receivers, correction/assistance
servers, files, local devices, time rollback, correction mixing, resource
exhaustion, differential parsing, stale/hostile or privacy-exposing algorithm
snapshots, source role/failover and solver-handover confusion, forged
digest-valid, authenticated-plaintext or authenticated/encrypted but
freshness-unchecked state, counter-checked state misrepresented as fresh,
digest-type/noncanonical binding confusion, caller-time reservation expiry,
partial cross-authority promotion/finalization, ambiguous restore eligibility,
unbounded pending candidates/retries/retention, cleanup of authoritative state,
unauthorized repair, old-namespace revival, same-namespace counter reset,
nonce reuse or silent freshness downgrade, competing recovery,
nonce/suite/counter/
keystore lifecycle failures, receiver-asserted configuration/partial-
application errors, no-command proof overstated as hardware stability, lost
control lease/other-controller/autonomous changes, lost failure evidence,
unplanned/unknown transitions, stale samples or false coherence, escaped
borrowed work, forgotten/leaked handles or executors, dispatch/cancel and
completion/drop/cleanup races, arbitrary or reentrant destructors in handle
Drop, hidden/unbounded cleanup, admission starvation, lifecycle/payload-state
divergence, exclusive cleanup blocked by live handles, overlapping cleaners,
leaked cleanup authority, unrecorded/misbound contention, forged contention
receipts, public raw-receipt escape, ignored/forgotten receipts, duplicate or
mismatched supervisors, implicit/arrival-ordered lanes, OS thread/task replay
identity, cross-supervisor or concurrent same-lane use, lane sequence wrap/
exhaustion, unrecorded grants, reversed successful-cleanup order, live-CAS
replay ownership, under-reserved/incomplete events, global-order wrap/
exhaustion, grant/result mismatch, replay consulting live contention,
contention-trace exhaustion, nondeterministic entry selection, duplicate
extraction/destruction, stale/ABA/exhausted job IDs, detached registry entries,
hidden owned leases, unresponsive parallel work, premature capacity/buffer
reuse, overstated pre-abort diagnostics, trace overflow, uncaptured runtime
outcomes, supply-chain compromise, FFI/DMA, credential exposure, and location
privacy.

Mandatory controls include bounded work, no input-dependent panic under
declared resource limits, freshness and issue-of-data validation, explicit
trust, credential redaction, location-minimizing logs, network allowlists,
reproducible inputs, locked tooling, SBOMs, fuzzing, changed-code pentests, and
periodic full external security and GNSS-domain audits.

Correction caches bind transport peer, provider/mountpoint, station/solution,
frame/datum, antenna, authenticated peer and generation. Secret types are not
ordinarily cloneable, displayable or serializable; routine telemetry excludes
precise position/time and globally correlatable provenance. Time rollback uses
an explicit platform persistence authority rather than pretending `no_std`
can provide rollback-resistant storage.

## Gap-Driven Version Integration

The architecture review has been incorporated without replacing the existing
broader 1.0 roadmap:

| Gap | Versioned implementation stops |
| --- | --- |
| Repository policy, strict tags, report-parent/package provenance | v0.1.1 |
| Machine-readable crate/capability DAG and feature/tier escalation checks | v0.1.4 |
| Exact standards, requirements, claims and test traceability | v0.1.2-v0.1.3 and v0.210.1-v0.210.2 |
| Honest safe bounded storage and caller scratch | v0.2.0-v0.2.3 |
| Exact units, uncertainty and typed covariance | v0.3.0-v0.3.2 and v0.6.2 |
| Deterministic `no_std` math and stable SIMD/backend policy | v0.3.3, v0.48.2-v0.49.0 and v0.201.0 |
| Bounded solver linear algebra and conservative statistical kernels | v0.3.4-v0.3.5 |
| Explicit linalg/DSP/geo/navigation math dependencies and executor isolation | v0.3.4, v0.7.2, v0.37.0, v0.48.3 and v0.169.1-v0.169.4 |
| Raw/resolved/atomic/UTC time, exact arithmetic, capture identity and rollback | v0.4.0-v0.5.4 |
| UTC civil/POSIX/calendar and TT/UT1/EOP precision-time contracts | v0.5.5 and v0.7.3 |
| Namespaced IDs, opaque restricted/future records, safe extensions, staged artifacts and assessments | v0.12.0-v0.13.2 |
| External algorithm/stage capability, resource, trust and reset contract | v0.12.3 |
| Core signal contracts, constellation physical fragments and format-owned mappings | v0.12.4 |
| Projected coordinates and typed derived kinematics | v0.7.2 and v0.13.3 |
| Non-reusing artifact/provenance ID lifecycle and replay remapping | v0.13.1 |
| Deterministic navigation/correction/product model selection evidence | v0.14.2 |
| Correction taxonomy, duplicate prevention, sessions and anti-mixing | v0.15.1-v0.15.2, v0.139.1 and v0.142.1 |
| Borrowed progress, targeted invalidation, counter exhaustion and preflight receipts | v0.16.0-v0.17.2 |
| Honest exact/static/measured/assumed/unavailable resource evidence | v0.17.1 and v0.50.1 |
| Snapshot envelope, canonical binding, bounded restore/writer matrix, narrow repair authority, deterministic cleanup and platform protection | v0.18.1-v0.18.2, v0.48.4, v0.54.2-v0.55.1, v0.144.3, v0.168.3 and v0.189.2-v0.189.6 |
| Tiered facade, versioned profiles and plan-before-side-effects | v0.20.1-v0.20.2 |
| Runtime source withdrawal, supervision and authorized failover | v0.20.3 |
| Logical source-role composition and solver-state-safe same-role handover | v0.20.4 |
| Complete RTCM/RINEX/product profiles and bounded compact decoding | v0.26.1-v0.35.1 |
| Capture utility and external data artifact governance | v0.36.3 and v0.196.2 |
| Fail-closed streaming/original-preserving format APIs | v0.21.1-v0.36.2 |
| Front-end conditioning, capture mapping, linear transport/control-lease proofs and adapter conformance | v0.37.2, v0.47.2-v0.50.3 and v0.170.0-v0.174.0 |
| Early hints, receipt schema, post-acquisition receipt integration and late assistance translation | v0.42.1-v0.43.2 and v0.185.1 |
| Tier 2 dispatch/cancel linearization, supervisor-enforced deterministic cleanup lanes and globally ordered grant/result replay, live-handle serialization, proved payload ownership, generation-safe reuse and lossless traces | v0.48.3 |
| Typed PVT/vertical-datum outputs and sequential GNSS estimator | v0.58.1 and v0.120.1-v0.126.1 |
| PVT mode matrix, DGPS and PVT/integrity separation | v0.120.4 and v0.129.3-v0.135.3 |
| Implementable RAIM/ARAIM/SBAS integrity contracts | v0.127.0-v0.129.5 |
| RTK validation, exact network profiles and complete PPP acceptance matrices | v0.135.3, v0.138.1 and v0.144.1-v0.144.2 |
| Public GBAS/ABAS applicability and integrity boundary | v0.119.1 |
| DFMC implementation matrix and exact named SBAS provider/service profiles including SouthPAN | v0.118.1-v0.119.2 |
| Conditional public BeiDou SAR/short-message boundary | v0.103.1 |
| Conditional public NavIC messaging boundary | v0.114.2 |
| Calibrated science artifacts, scintillation, reflectometry and space weather | v0.124.1-v0.124.4 |
| Concrete crypto backend and immutable authentication/evidence/policy decisions | v0.146.1-v0.157.1 |
| Post-protocol crypto and complete resilience evidence matrices | v0.150.1 and v0.155.1 |
| Caller-provided direction evidence versus native calibrated AoA production | v0.155.0 and v0.169.5 |
| Exact bounded GNSS timing slot/mapping/withdrawal contract | v0.158.1-v0.162.1 |
| Common-view/all-in-view time transfer and CGGTTS V2E | v0.163.1 |
| Full fusion calibration/mechanization, vector tracking, reacquisition and fixed-rate output | v0.164.1-v0.168.2 |
| Geo-owned transformations/mathematics, navigation-only composition, road-routing non-claim and native AoA | v0.169.1-v0.169.5 |
| FPGA/GPU/external-DSP stage, scalar-equivalence and provenance boundary | v0.175.1 |
| Generic sources, evidence-gated receivers, safe control, configuration generations and interval-scoped behavioral assessments | v0.185.2-v0.185.6 |
| Discovery, Android, canonical assistance, bounded PER and CAN ownership | v0.180.4-v0.190.2 |
| Publish-disabled CLI, services, inspection, visualization and lab tools | v0.190.3-v0.190.11 |
| Simulator, fuzz, conformance and benchmark tools | v0.196.1, v0.198.2-v0.198.3 and v0.201.1 |
| Unsafe/platform/mobile/privacy and separately admitted snapshot-protection adapters | v0.177.1-v0.190.2 |
| Differential, numerical, unsafe, MSRV and Aesynx audits | v0.198.1-v0.207.1 |
| Capability/resource/privacy documentation closure | v0.214.1 |
| Packaging, service and deployment security freeze | v0.219.1 |

These patch milestones are planned compatible implementation passes, not
permission to bundle unrelated work. A breaking correction moves to the next
minor milestone or inserts a new explicitly reviewed minor release.

## Release Discipline

The detailed sequence is in [RELEASE_PLAN.md](RELEASE_PLAN.md). A release can
be split or receive patch milestones at any time. It cannot absorb unrelated
work merely to reach 1.0 faster.

Every milestone contains Status, Goal, Deliverables, Verification, and Exit
criteria. Exit criteria end with the exact-commit pentest stop. No feature is
postponed beyond 1.0 if it is part of the production claim.

Before the first production candidate, all publishable manifests already
declare `1.0.0`. The `v1.0.0-rc.N` repository tag and final `v1.0.0` tag point
to the same approved source/package commit; crates.io publishes only the
retained final-version archives. Report-only pentest commits must prove package
file lists and checksums are identical to the reviewed implementation parent.
