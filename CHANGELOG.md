# Changelog

All notable changes to `navheim` are documented here.

## Unreleased

- Initialized the Rust workspace with dependency-free `navheim-core` and
  `navheim` facade crates.
- Added the standards, security, release, supply-chain, CI, and documentation
  foundations for the v0.1.0 implementation stop.
- Established Rust `1.90.0` through `1.97.1` compatibility policy and pinned
  release development to Rust `1.97.1`.
- Defined a one-way GNSS timing integration boundary: Navheim exposes complete
  dependency-free timing evidence, while downstream clock frameworks own their
  adapters, discipline, consensus, and holdover.
- Integrated the architecture/security gap review into the existing roadmap as
  targeted patch milestones, phase-specific technical acceptance criteria,
  stronger canonical/timing contracts, and unambiguous RC/package provenance.
- Closed the second planning coverage review with explicit implementation
  stops for `navheim-navigation`, complete RTCM/RINEX/product profiles, typed
  PVT and vertical-datum outputs, front-end conditioning, fusion calibration
  and vector tracking, assistance, integrity, RustCrypto, CAN I/O, independent
  conformance vectors, and exact timing state machines.
- Closed the third coverage review by repairing timing-slot and CAN ownership,
  adding deterministic `no_std` math, DGPS, profiles/discovery, full Android
  platform work, bounded PER and post-protocol crypto milestones, and
  separating PVT facts from integrity assessments.
- Integrated the fourth gap review without shrinking existing scope: 14
  bounded milestones now own the crate/capability DAG, honest resource
  evidence, projections, kinematics, safe extensions, NavIC messaging, DFMC,
  GNSS science, network RTK, PPP, fixed-rate fusion, native AoA, SouthPAN and
  complete FPGA/GPU/external-DSP stage contracts.
- Integrated the fifth foundation review as five bounded milestones plus
  strengthened existing ownership for artifact IDs and assistance translation:
  first-party bounded linear algebra, conservative statistics, canonical
  signal definitions, deterministic model selection, and early acquisition
  hints now precede the solvers and adapters that consume them.
- Integrated the sixth review as 11 bounded stops: corrected
  `navheim-linalg -> navheim-math` and signal/format dependency ownership,
  added civil UTC and TT/UT1/EOP contracts, separated immutable maximum plans
  from runtime search decisions, and assigned deterministic multicore, source
  failover, receiver control and staged snapshot/restore profiles.
- Integrated the seventh review as five net-new stops plus one moved
  milestone: explicit DSP/geo/executor dependencies, snapshot trust/sealing,
  source-role composition, correctly ordered acquisition and semantic-store
  persistence, receiver-configuration generations, captured parallel runtime
  traces and exact Julian/MJD representation.
- Integrated the eighth review without replacing earlier scope: geo owns all
  coordinate mathematics while navigation composes it; executor work has
  scoped exclusive ownership and lossless bounded traces; snapshot
  authenticity, confidentiality and privacy are separate; source handover
  invalidates dependent solver state by default; and receiver transactions,
  observed configuration assessments and optional external snapshot
  protection have explicit implementation stops.
- Integrated the ninth review as five additional bounded stops plus stronger
  existing milestones: SDRs now use prepared immutable transition plans and
  configuration generations; executor deadlines expose cooperative,
  unresponsive and terminal states; snapshot protection authenticates all
  interpretive metadata with crash-safe nonce/counter/key lifecycle and
  separate platform adapters; receiver assessments are interval-scoped
  `ObservedConsistent`; and local-frame mathematics remains geo-owned.
- Integrated the tenth review without inflating or replacing the roadmap:
  executor milestones now separate non-escaping borrowed scopes from owned
  lease handles and define exact ownership states; front-end application has
  mutation-aware and coherent-group outcomes; and snapshot authenticity,
  confidentiality and freshness are independent. Rollback resistance requires
  trusted external monotonic comparison/update evidence, while atomic
  encrypted file replacement is documented only as crash-consistent.
- Integrated the eleventh review into existing owning releases: nonterminal
  `ExecutionHandle` destruction is explicitly fail-stop with normal completion
  through terminal-result/join APIs; SDR partial and unknown outcomes preserve
  causes and bounded evidence; and `CounterChecked` cannot satisfy freshness
  policy. Rollback-resistant sealing now requires an atomic digest-bound
  compare-and-advance or exclusive writer reservation with concurrent-writer
  and crash-boundary verification.
- Integrated the twelfth review without adding parallel releases: executor
  accounting is authoritative even across `mem::forget`, `ManuallyDrop` and
  leaks, with explicit orphan shutdown and concrete abort behavior; SDR apply
  success and no-mutation results now carry structural evidence; and snapshot
  freshness transactions use a distinct suite-approved binding over the exact
  canonical protected envelope with authority-owned reservation time.
- Integrated the thirteenth review into the existing owners: executor job
  retirement is atomic and generation-safe across completion, drop, claim and
  shutdown; SDR no-command proof is linear and bounded by exclusive physical-
  control evidence; and protected snapshots have a normative durable staging,
  authority-commit, promotion, finalization and crash-recovery sequence.
- Integrated the fourteenth review without adding releases: executor dispatch
  races cancellation-before-dispatch on one CAS, handle `Drop` performs no
  arbitrary destruction, sealed bounded cleanup gates generation-safe slot
  reuse, and exhausted generations cannot wrap. Protected snapshots now share
  an explicit restore/writer matrix across all durable states, with bounded
  pending artifacts, retention, retries and deterministic cleanup.
- Integrated the fifteenth review into the same owners: executor cleanup is
  caller-driven, budgeted and visible through admission backpressure, with no
  hidden reaper; safe payload ownership is required and unsafe extraction is
  excluded from the 1.0 executor. Snapshot repair is separately
  authorized and cannot reset an in-namespace counter, accept older state,
  reuse nonces or bypass a durable continuity break.
- Integrated the sixteenth review into v0.48.3: `poll_cleanup` uses a shared
  executor borrow so live handles do not prevent reclamation. An internal
  non-exported single-cleaner CAS returns pre-mutation `Busy` on contention,
  selects the lowest eligible generation-bearing job ID within bounded work,
  and is tested against completion, claim, drop, admission and shutdown.
- Integrated the seventeenth review into v0.48.3 by separating mutation
  domains: the raw primitive creates a bounded contention receipt at the
  failed-CAS linearization point without changing cleanup or trace state. The
  supervisor records `Busy` against a logical call before semantic reaction,
  and replay uses that fact instead of observing live contention.
- Integrated the eighteenth review into v0.48.3 by making the supervisor the
  only public cleanup boundary. The receipt-producing executor primitive is
  crate-private, so application code cannot ignore or forget an unrecorded
  receipt; recording succeeds before `Busy` is observable, and replay is
  consulted before a live CAS.
- Integrated the nineteenth review into v0.48.3 by replacing ambient
  concurrent-call identity with plan-issued `CleanupLane` capabilities. Each
  lane has a deterministic ID and checked non-wrapping sequence, so replay
  keys exact lane/call pairs and cannot swap outcomes when call arrival or CAS
  order changes.
- Integrated the twentieth review into v0.48.3 by recording successful cleanup
  grants and results as well as contention. Worst-case event capacity is
  reserved before the cleaner CAS, successful grants receive a checked global
  order, and replay follows that order without using live CAS timing.
- Integrated the twenty-first review into v0.48.3 by making early replay order
  a scheduler-only `SupervisedCleanupPoll::Pending`, not an application error.
  Pending preserves the same active call without state/result transitions;
  controlled drivers hide it and the base executor never blocks or busy-spins.
- Integrated the twenty-second review into v0.48.3 by moving low-level polling
  from `ExecutionSupervisor` to a `ReplayDriver` created by consuming a sealed
  plan-bound permit. The application facade is ready-only and cannot expose
  driver, lane, permit or poll types, while shared driver calls retain
  distinct-lane concurrency.
- Integrated the twenty-third review into v0.48.3 by defining the public
  `CleanupScheduler` request/drive/ready-token/completion lifecycle. Caller-
  invoked drive is bounded and nonblocking; request and turn IDs never reuse,
  queues reserve explicit capacity, completions persist until claim or
  deterministic retirement, and shutdown reconciles every request state.
- Added a Gjallarbru-style immutable RFC workflow with 25 exact RFC Editor
  publications, checksum/line-ending gates, an optional local read-only guard,
  lifecycle roles, and a live-checked 210-errata drift snapshot.
- Made shell syntax checks honor Bash versus POSIX-shell shebangs and replaced
  the non-portable CI read-only-mode assertion with checksum/source identity.
- Added the external standards acquisition inventory and secure local-only
  vault workflow: 36 authoritative source families, 17 allowlisted public
  downloads, local SHA-256 locking, official-page revision-marker review, and
  enforced exclusion of restricted document bytes from Git and crates.
- Completed a repository-wide requirement/specification audit, corrected the
  copied MIT donor notice, and expanded source-size and Markdown-link checks
  across all applicable repository paths.
- Added bounded pre-1.0 releases for CGGTTS common-view/all-in-view timing,
  exact SBAS providers, conditional BeiDou messaging, FPGA/external DSP,
  generic and conditional receiver families, every named GitHub-only tool,
  external evidence data, deployment artifacts, and full requirement/claim
  traceability.
- Made source-first review and same-milestone testing a fail-closed,
  repository-validated rule for every behavioral implementation.
