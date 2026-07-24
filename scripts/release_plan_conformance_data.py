"""Acceptance data added by the repository-wide requirements audit."""

CONFORMANCE_MILESTONE_DETAILS = {
    "0.1.4": (
        "Generate an acyclic crate/capability DAG covering normal, optional, build, and development edges plus features, tiers, alloc/std, unsafe, TLS, crypto, publication, and platforms.",
        "Test Cargo metadata equivalence, feature unification, cycles, undeclared edges, tier escalation, adapter isolation, and every supported feature combination.",
    ),
    "0.3.4": (
        "Implement narrow no_std fixed/caller-scratch QR, Cholesky/LDLT, triangular solves, rank updates/downdates, square-root updates, and rank/condition estimates, depending only on navheim-math with no private sqrt/hypot or platform math.",
        "Compare arbitrary-precision and independent references for dependency edges, dimension/scratch limits, aliasing, pivots, singular/indefinite/non-finite inputs, bad scaling, downdate failure, and prohibited normal-equation inversion.",
    ),
    "0.3.5": (
        "Implement only admitted normal and chi-square tails/CDFs/quantiles with degrees-of-freedom, confidence, log-probability, validated range, monotonicity, bounded error, and conservative rounding semantics.",
        "Compare arbitrary-precision tables across central/extreme tails and domain boundaries; prove integrity/protection rounding never underestimates risk or permits a looser threshold.",
    ),
    "0.7.2": (
        "Implement navheim-geo over navheim-core representations and navheim-math operations for bounded UTM/UPS and selected Transverse Mercator profiles with explicit provenance and no platform/private math.",
        "Cross-check independent references and test dependency direction, forward/inverse round trips, polar/zone boundaries, antimeridian, invalid coordinates, and unsupported EPSG-database requests.",
    ),
    "0.12.3": (
        "Define static Tier 0 and isolated host extension contracts declaring capabilities, numerical backend, determinism, resources, artifacts, provenance, trust, reset, and invalidation.",
        "Test limit lies, nondeterminism, prohibited trust/correctness bypass, stale output, panic/failure isolation, reset, unregister, and canonical fallback.",
    ),
    "0.12.4": (
        "Put SignalDefinition/registry contracts in navheim-core, physical fragments in constellation crates, format-version wire mappings in RINEX/RTCM crates, and fragment composition in the facade.",
        "Test dependency direction, selected-fragment composition, unknown/partial definitions, FDMA bounds, revision conflicts, units, format round trips, and rejection of duplicate physical tables.",
    ),
    "0.13.3": (
        "Define typed horizontal and three-dimensional speed, course over ground, and climb rate with frame, epoch, covariance, derivation, and reason-bearing availability.",
        "Test stationary/low-speed course, vertical-only motion, frame and epoch mismatch, covariance propagation, discontinuities, overflow, and independent trajectories.",
    ),
    "0.14.2": (
        "Select navigation models, corrections, and products by named query epoch, satellite/signal/kind, issue, health, fit/validity, discontinuity, source/session/generation, and separate authentication assessment.",
        "Test future/stale/expired models, equivalent/conflicting healthy sources, issue transitions, session mixing, late authentication, every Selected/Ambiguous/Unavailable/Rejected outcome, considered-candidate evidence, and no latest-wins path.",
    ),
    "0.5.5": (
        "Define checked UTC civil labels, TAI-mediated arithmetic, UTC-model lifecycle, POSIX ambiguity, and Gregorian/ordinal/Julian/MJD conversions using integer day plus exact fraction/rational under frozen range/BCE/year-zero rules.",
        "Test positive/hypothetical negative leaps, model lifecycle, calendar/BCE/range boundaries, Julian/MJD epochs/fractions, precision/rounding, POSIX ambiguity, and the leap-smear non-claim.",
    ),
    "0.7.3": (
        "Define TT and EOP-derived UT1 time arguments with exact derivation, product/series revision, interpolation, validity, uncertainty, provenance, and separation from GnssTimeScale.",
        "Cross-check IERS/IAU references and test EOP gaps/expiry, interpolation boundaries, leap transitions, precision, wrong-scale use, unavailable evidence, and Earth-rotation/tide call-site typing.",
    ),
    "0.18.1": (
        "Define an opt-in versioned bounded snapshot envelope with algorithm/schema, source/generation, validity, provenance, model/calibration/product IDs, capability needs, byte/work limits, corruption digest, and optional external freshness evidence.",
        "Test hostile bytes, versions, sizes, corruption checks, provenance remap, expired/rolled-back state, missing capabilities, incompatible identities, invariant failure, partial restore, atomic commit, and unsupported-state non-claims.",
    ),
    "0.18.2": (
        "Define orthogonal SnapshotAuthenticity, SnapshotConfidentiality and SnapshotFreshness. CounterChecked means an authenticated valid counter was compared with named non-rollback-resistant local state and never satisfies guaranteed-freshness policy; only qualified transactional monotonic evidence yields RollbackResistant.",
        "Test every evidence combination, CounterChecked policy rejection, mismatched authority/namespace/local state, stale authenticated replay, absent/lying authority, freshness downgrade/unavailable, consent/retention, sensitive formatting, plaintext limits, reconvergence and restored-assessment invalidation.",
    ),
    "0.20.3": (
        "Supervise only explicitly opened sources through deterministic health, withdrawal, gaps, generation-safe reselection, and bounded caller-authorized retry/failover policies without trust/accuracy downgrade.",
        "Test source/provider loss and return, flapping, retry exhaustion, same-role generation replacement, policy changes, simultaneous failures, ordering, cancellation, backpressure, recovery, and explicit no-fallback outcomes.",
    ),
    "0.20.4": (
        "Define logical source roles and a composition graph; same-role replacement invalidates dependent clock/bias, calibration, ambiguity/slip, correction, smoothing, PPS/timing, integrity and authenticity state unless an explicit evidenced handover transform preserves it.",
        "Test clock mapping, uncertainty growth, calibration, provenance, epochs and generations; default invalidation, transformed survival, gaps/discontinuities/reconvergence/coasting, legitimate cross-role composition, role confusion, reset and deterministic rejection reasons.",
    ),
    "0.1.3": (
        "Create a bidirectional ledger from architecture requirements and public claims to owners, milestones, sources, tests, status, and non-claims; make authored-file scope explicit.",
        "Reject missing, duplicate, stale, circular, aggregate, ownerless, testless, or unsupported mappings and scan every repository path covered by the source-size and documentation policies.",
    ),
    "0.36.3": (
        "Keep navheim-capture publish-disabled and route every import/export through the frozen replay model with explicit consent and minimized metadata.",
        "Test malformed streams, interruption, overwrite refusal, path traversal, device reset, disk exhaustion, metadata redaction, deterministic output, and round trips.",
    ),
    "0.103.1": (
        "Freeze the exact lawful public BeiDou SAR/short-message documents and either implement their interoperable profile or publish an explicit unsupported/unavailable matrix.",
        "Test unknown identifiers, malformed content, regional/service applicability, privacy-sensitive payload handling, expiry, and the no-specification non-claim path.",
    ),
    "0.114.2": (
        "Freeze exact lawful public NavIC messaging documents and either implement interoperable message profiles or preserve identifiers with explicit unavailable and privacy-sensitive outcomes.",
        "Test absent or ambiguous specifications, malformed and unknown messages, service/region applicability, sensitive payload handling, expiry, and unsupported-profile non-claims.",
    ),
    "0.118.1": (
        "Freeze DFMC code, acquisition, tracking, symbol/FEC, framing, correction, GEO mode, message, validity, and unsupported-cell matrices before claiming complete DFMC.",
        "Use licensed official and independent vectors for each admitted cell; test FEC limits, unknown messages, mode transitions, stale corrections, GEO confusion, and unavailable cells.",
    ),
    "0.119.2": (
        "Name WAAS, EGNOS, MSAS, GAGAN, SDCM, BDSBAS, KASS, SouthPAN, and current African SBAS profiles with exact service definitions, regions, signals, messages, validity, and limitations.",
        "Use provider and independent vectors for every admitted matrix cell; test region/profile confusion, future GEO IDs, expiry, conflicting providers, and unsupported profiles.",
    ),
    "0.124.1": (
        "Establish optional navheim-science artifacts with calibration, lock attribution, sample cadence, windows, gaps, batch identity, provenance, uncertainty, and explicit product maturity.",
        "Test missing/expired calibration, irregular sampling, window edges, gaps, batch mixing, provenance loss, bounded storage/work, and research-versus-operational labels.",
    ),
    "0.124.2": (
        "Implement amplitude and phase scintillation metrics including admitted S4-style profiles with named detrending, bandwidth, lock, sampling, uncertainty, and validity assumptions.",
        "Compare independent scientific references and test saturation, loss of lock, gaps, low CN0, detrending/window choices, finite arithmetic, and unavailable prerequisites.",
    ),
    "0.124.3": (
        "Represent direct/reflected observables, bistatic geometry, reflection points, path/surface delay, calibration, coherence, uncertainty, and validity without hiding model assumptions.",
        "Compare selected GNSS-R references and test geometry degeneracy, multipath ambiguity, surface/model mismatch, gaps, calibration expiry, and unsupported retrieval products.",
    ),
    "0.124.4": (
        "Expose calibrated GNSS space-weather and remote-sensing artifacts only for frozen authoritative methods, with cadence, region, model, uncertainty, provenance, and maturity labels.",
        "Compare admitted reference datasets and test sparse coverage, storms/outliers, stale models, calibration changes, batch reproducibility, and explicit non-product outcomes.",
    ),
    "0.138.1": (
        "Freeze exact standardized VRS, FKP, MAC, and MAX message/session profiles and label every proprietary or undocumented extension separately.",
        "Use independent network-RTK cases for each admitted profile and test mount/session/station mixing, datum/cell mismatch, handover, expiry, partial sets, and rejected proprietary variants.",
    ),
    "0.144.2": (
        "Freeze PPP state layouts, uncombined/ionosphere-free modes, clock/troposphere/ambiguity/bias states, product interpolation, discontinuity, convergence, rollback, and unavailable matrices.",
        "Compare independent PPP engines and datasets across every admitted mode; test state transitions, product/bias gaps, frame and epoch mismatch, resets, false convergence, and rollback.",
    ),
    "0.155.0": (
        "Accept caller-provided receiver, antenna, baseline, angle, coherence, calibration, and clock evidence as typed inputs without claiming Navheim produced direction estimates.",
        "Test missing calibration, frame/clock mismatch, ambiguous direction, stale evidence, conflicting arrays, expiry, provenance, and input-versus-native-producer labels.",
    ),
    "0.163.1": (
        "Produce common-view and all-in-view comparison artifacts and bounded CGGTTS V2E original/canonical records, including frozen BDS-3 conventions, calibration, schedule, uncertainty, and provenance.",
        "Cross-check independent BIPM-compatible results and test missing common satellites, mixed scales, station/calibration errors, malformed records, track boundaries, leap events, and explicit exclusion of discipline/consensus.",
    ),
    "0.168.2": (
        "Emit fusion solutions at caller-selected epochs using bounded interpolation or propagation with explicit extrapolation limit, deadline/latency evidence, covariance growth, freshness, and lifecycle.",
        "Compare independent trajectories and test irregular inputs, deadline misses, extrapolation boundaries, outages, reset, stale/coasting/unavailable transitions, and no invented GNSS freshness.",
    ),
    "0.169.5": (
        "Produce calibrated multi-antenna angle-of-arrival and direction-consistency evidence with array geometry, phase bias, ambiguity set, coherence, clock, frame, validity, uncertainty, and expiry.",
        "Use surveyed/simulated arrays and test integer ambiguities, reflections, weak signals, incoherent clocks, geometry degeneracy, calibration expiry, spoof cases, reset, and unavailable output.",
    ),
    "0.42.1": (
        "Define dependency-free SearchAid/AcquisitionHint artifacts for approximate time/location/velocity/orbit and Doppler windows, source/generation, validity, uncertainty, trust, cross-signal aiding, and reacquisition identity/expiry.",
        "Test immutable maximum PlanReceipt bounds, poisoned/conflicting/stale hints, bounded blind fallback, search equivalence, expiry/reset, work limits, and proof that hints cannot resolve canonical time, position, or trust.",
    ),
    "0.42.2": (
        "Define and serialize the bounded immutable SearchExecutionReceipt schema for hint IDs, windows, actual work, fallback, decision order, plan/source identity and outcome without claiming executable acquisition integration.",
        "Test canonical/original serialization, capacity/size bounds, unknown fields, hostile receipts, schema versions, no PlanReceipt mutation, stale identities, and explicit pre-acquisition non-claim.",
    ),
    "0.43.2": (
        "Integrate acquisition with SearchExecutionReceipt production for runtime hint acceptance/rejection, actual bounded work, fallback reason, deterministic decision order and outcome.",
        "Test dynamic hint arrival/loss, conflicting windows, deterministic ties/order, budget exhaustion, blind fallback, stale plans/generations, receipt completeness, and executable replay equivalence.",
    ),
    "0.48.3": (
        "Define must-use/non-cloneable CleanupScheduler<Running> with request_cleanup, drive, ready-token/claim and consuming begin_shutdown(self) -> CleanupScheduler<Draining>. Draining permanently disables admission but retains ready-token/claim APIs; bounded drive_shutdown returns recorded aggregate ShutdownProgress with checked ShutdownTurnId, and consuming finish_shutdown succeeds with a generation-bound ShutdownReport only after requests/completions/traces/lanes/driver/executor cleanup are finalized. Failure returns private-construction/must-use/non-Copy/non-cloneable/non-serializable ShutdownNotDrained<Self> owning the complete drainer and bounded blockers. Use safe Option-owned internals for consuming transitions; unfinished scheduler/error Drop aborts without allocation/unwind, while forget only leaks. Preserve IDs/tokens and original completed results across begin_shutdown; atomically resolve completion versus cancellation, materialize CancelledByShutdown with partial evidence only for queued/active work, and retain/claim or deterministically retire completions. The explicit Tier 2 scheduler-thread adapter stops intake, enters the same drainer and joins only after finish. Admission still atomically reserves bounded request+completion slots and issues non-reusing generation-bearing CleanupRequestId; normal drive remains bounded/nonblocking with aggregate recorded SchedulerProgress and checked SchedulerTurnId. ReadyCleanup remains private/must-use/non-clone and consumed for correlated completion. Move low-level supervised polling off ExecutionSupervisor to ReplayDriver::poll_cleanup(&self, &ExecutionSupervisor, &mut CleanupLane, &Executor, budget) -> SupervisedCleanupPoll. ReplayDriver remains must-use/non-Copy/non-Clone/non-serializable, has no public constructor/deserializer, and is privately created exactly once per scheduler generation by consuming a sealed must-use/non-Copy/non-Clone/non-serializable SchedulerPermit from validated PlanReceipt with supervisor/executor/plan/trace/scheduler binding. Shared driver calls preserve distinct-lane concurrency; mutable lanes exclude same-lane concurrency. Facade signatures expose no driver/lane/permit/poll type, completion has no Pending, and custom schedulers require a reviewed permit/profile. Preserve every prior lane, reservation, grant/result, replay, lifecycle and fail-stop guarantee.",
        "Use visibility/compile/API, Miri, Loom, Kani/model and subprocess tests for exact Running/Draining method availability and private state constructors; safe consuming Option transfer; permanent admission rejection after begin; preserved IDs/tokens and original ready results; queued/active cancellation with partial evidence; every completion/cancellation race; bounded nonblocking shutdown turns, phase/order/budget/progress recording and replay; claims and deterministic retirement during drain; finish rejection for every pending request, completion, trace, lane, driver and executor-cleanup condition; ShutdownNotDrained construction/clone/Copy/serialization rejection and sole-owner recovery; exact report binding/counts; unfinished Running/Draining/error Drop abort; forget/leak non-reuse; and thread-adapter intake stop, drain and join ordering. Retain exact normal facade signatures; mutable ordering/internal distinct-lane concurrency; dual-slot reservation and backpressure; request state/non-reuse/exhaustion/forgotten-ID cases; bounded normal drive and SchedulerTurnId replay; no per-call Pending; ReadyCleanup correlation and unknown/forged/duplicate/stale/cross-generation/already-claimed cases; retirement/tombstones/reuse; no supervisor poll; facade type exclusion; permit/driver constructors, authenticity, consumption, forget and binding; same/distinct-lane rules; ready-only completion; custom-extension rejection; side-effect-free repeated/permuted Pending; active-call binding; poll invisibility; driver budgets; no base block/spin; atomic reservation/failure; read-only replay; Busy/Granted capacity/receipts/order/results; incomplete/inverted/mismatch; lane exhaustion; raw boundary; trace failure; inert Busy; handles/cleaners/work/lifecycle/dispatch/publication/ABA/exactly-once/orphan/panic/reentrancy/unresponsive; and exact-API tests.",
    ),
    "0.50.3": (
        "Issue a framework-private linear PreSubmissionToken; acquiring exclusive Navheim command transport consumes it and makes RejectedNoMutation impossible. No-command proof is narrow; prior-generation preservation also requires exclusive control lease plus a frozen no-autonomous-change profile.",
        "Compile-fail third-party proof minting and post-transport no-mutation construction; test token consumption, no-command semantics, other controller, lease loss, reset/hotplug/identity/autonomous changes to StateUnknown, complete success evidence, overflow, coherent devices, invalidation/reprobe and safe reads.",
    ),
    "0.48.4": (
        "Implement the acquisition/reacquisition-memory snapshot profile after scheduler integration with search/source identity, expiry, authenticity/confidentiality/freshness, provenance remap, sensitivity and explicit monotonic-authority evidence.",
        "Test cold/warm/hot restore, all three evidence dimensions, stale authenticated/encrypted replay, unavailable monotonic state, expired/poisoned hints, mismatch/reset, corrupt/forged state, privacy, equivalence, invalidation, atomic failure and safe cold start.",
    ),
    "0.54.2": (
        "Implement minimal tracking-channel/raw-page snapshot profiles with source/generation, clock, calibration, partial-page issue, validity, parents, authenticity/confidentiality/freshness, sensitivity and monotonic-authority evidence.",
        "Test mid-symbol/page state, compatibility, calibration/reset, stale authenticated/encrypted replay, unavailable monotonic state, corruption/forgery, privacy, provenance remap, assessment invalidation, atomic restore, reacquisition and cold reconstruction.",
    ),
    "0.55.1": (
        "Implement the minimal semantic navigation-store/ephemeris snapshot after GPS models with issue, model, health, validity, source, parents, authenticity/confidentiality/freshness, sensitivity, provenance and monotonic-authority evidence.",
        "Test stale/conflicting/future ephemerides, issue/model/health/reset, stale authenticated/encrypted replay, unavailable monotonic state, corruption/forgery, privacy, provenance remap, restored-assessment invalidation, atomic restore and reconstruction.",
    ),
    "0.144.3": (
        "Implement admitted PPP snapshot profiles for named state layouts with products, biases, frame, clocks, ambiguity/troposphere state, covariance, convergence, calibration, expiry, trust, provenance, and independent authenticity/confidentiality/freshness evidence.",
        "Compare uninterrupted/restored solutions and test product/bias/frame changes, stale convergence, covariance invalidity, authenticity/confidentiality/freshness, stale authenticated replay, unavailable monotonic state, privacy, forgery, version mismatch, reconvergence, atomic rejection and unavailable restore.",
    ),
    "0.168.3": (
        "Implement admitted fusion snapshot profiles with named state/covariance layout, sensor clocks/generations, calibration/model identity, delayed queues, validity, expiry, trust, provenance, and independent authenticity/confidentiality/freshness evidence.",
        "Compare uninterrupted/restored trajectories and test sensor reset, calibration/model changes, invalid covariance/queues, authenticity/confidentiality/freshness, stale authenticated replay, unavailable monotonic state, privacy, forgery, version mismatch, reconvergence, atomic rejection and unavailable restore.",
    ),
    "0.185.4": (
        "Distinguish read-only/control-capable receiver profiles and execute only side-effect-free planned, typed, allowlisted commands with firmware capabilities, ACK/NAK correlation, timeouts, idempotency and transitions; record command, ACK/NAK, read-back and timing facts in ControlTransaction.",
        "Test arbitrary-byte rejection, unsupported firmware, NAK/timeout/reorder, duplicate commands, partial application, baud/protocol reconnect, power loss, read-back mismatch, receiver assertions, retry limits, redaction and recovery to known state.",
    ),
    "0.185.5": (
        "Create ReceiverConfigurationGeneration bound to device/firmware and effective epoch/interval; drain or stale queues, invalidate affected mappings/calibrations/observations, rebind corrections, and classify volatile/persistent/destructive commands.",
        "Test buffered old/new semantics, transition intervals, queue drain failure, targeted invalidation order, correction rebinding, device replacement, persistent authorization, flash-wear exhaustion, reset/destructive consent, rollback, and recovery.",
    ),
    "0.185.6": (
        "Create ConfigurationAssessment separately from ControlTransaction; target one generation and carry interval, evidence sources, coverage, uncertainty and unverifiable fields, using ReceiverAsserted or interval-scoped ObservedConsistent without claiming internal configuration or signal authenticity.",
        "Test false ACK/read-back, delayed/contradictory streams, partial coverage, uncertainty, unverifiable fields, independent timing/rate/protocol evidence, reset, firmware/device replacement, invalidation, stale generations and refusal to broaden ObservedConsistent.",
    ),
    "0.189.2": (
        "Normatively order durable Pending reservation -> complete canonical seal -> sidecar/authority binding -> durable candidate stage -> atomic AuthorityCommitted counter+binding -> durable promotion -> Committed finalization. Freeze the bounded recovery matrix and a separate Tier 3 repair capability limited to exact current-candidate recovery or durable namespace/key/counter retirement plus fresh-domain continuity break. Only finalization returns RollbackResistant evidence.",
        "Test binding self-exclusion, every state and crash edge, authority-commit/promotion/finalization failure as pending or unavailable, exclusive recovery versus new writer, pre-commit-only cancellation, deterministic cancelled/superseded cleanup and interruption, resource exhaustion, reboot, reservation expiry, key rotation/counter migration with pending state, staged-candidate mismatch/loss and no older fallback. Also test repair authorization, exact-current-candidate verification, permanent anti-revival retirement, fresh key/nonce/counter domains, continuity/security/invalidation artifacts and reacquisition; reject same-namespace reset, older state, nonce reuse, unresolved-evidence deletion, CounterChecked downgrade and repair without durable platform proof.",
    ),
    "0.189.3": (
        "Freeze Linux/BSD binding, staging, promotion, recovery and optional repair primitives sufficient for the exact v0.189.2 matrix, bounds, cleanup and anti-revival continuity-break contract; otherwise report CounterChecked/Unchecked and repair unavailable.",
        "Test fsync/rename/directory and authority durability boundaries, every recovery state, staged loss/mismatch, commit-before-promotion and promoted-before-finalization recovery, competing writer, cleanup interruption, reboot, pre-commit cancellation, old-file restoration, namespace/exhaustion/migration and bounded records/candidates/retries/bytes. Also test current-candidate repair, authorization denial, durable old-namespace retirement, fresh domains, backup/old-file anti-revival and honest repair/freshness unavailability.",
    ),
    "0.189.4": (
        "Freeze Windows binding, staging, promotion, recovery and optional repair primitives sufficient for the exact v0.189.2 matrix, bounds, cleanup and anti-revival continuity-break contract; otherwise report weaker freshness and repair unavailable.",
        "Test Windows storage/authority durability, every recovery state, staged loss/mismatch, commit-before-promotion and promoted-before-finalization recovery, competing writer, cleanup interruption, reboot, pre-commit cancellation, user/machine scope, old-state restoration, namespace/exhaustion/migration, bounded retention/retries and CounterChecked rejection. Also test current-candidate repair, authorization/scope denial, durable old-namespace retirement, fresh domains, backup/old-state anti-revival and honest repair unavailability.",
    ),
    "0.189.5": (
        "Freeze Apple binding, staging, promotion, recovery and optional repair primitives sufficient for the exact v0.189.2 matrix, bounds, cleanup and anti-revival continuity-break contract; preserve access/background semantics and report repair/freshness unavailable when any required transition is absent.",
        "Test storage/Keychain durability, every recovery state, staged loss/mismatch, commit-before-promotion and promoted-before-finalization recovery, competing writer, cleanup/background interruption, reboot, pre-commit cancellation, lock/entitlement denial, backup restoration, bounded retention/retries, exhaustion/migration and unavailable hardware. Also test current-candidate repair, explicit authorization denial, durable old-namespace retirement, fresh domains, backup anti-revival and honest repair unavailability.",
    ),
    "0.189.6": (
        "Freeze Android binding, staging, promotion, recovery and optional repair primitives sufficient for the exact v0.189.2 matrix, bounds, cleanup and anti-revival continuity-break contract; keep API/hardware/StrongBox/invalidation evidence explicit and report repair/freshness unavailable when required transitions are absent.",
        "Test storage/Keystore durability, every recovery state, staged loss/mismatch, commit-before-promotion and promoted-before-finalization recovery, competing writer, cleanup interruption, reboot/process death, pre-commit cancellation, software/hardware keys, backup/reinstall restoration, bounded retention/retries, exhaustion/migration/invalidation and CounterChecked rejection. Also test current-candidate repair, authorization/key-invalidation denial, durable old-namespace retirement, fresh domains, backup/reinstall anti-revival and honest repair unavailability.",
    ),
    "0.170.0": (
        "Implement recorded-I/Q and virtual sources against the v0.50.3 prepare/apply/generation/read contract, with deterministic transition simulation and no invented hardware acknowledgement or observed calibration.",
        "Test plan rejection, generation changes, partial reads, initialized counts, gaps/overruns/end/would-block, stale blocks, mapping/DSP invalidation, deterministic replay and honest unavailable device assessments.",
    ),
    "0.171.0": (
        "Implement the frozen RTL2832U/E4000 profile through v0.50.3 prepared plans, configuration generations, initialized-count reads and separate device-asserted versus observed sample behavior.",
        "Test hardware/recorded retune, rate, gain, AGC and bias transitions; stale USB buffers, timestamp limits, overruns, short reads, detach/reset, read-back disagreement, observed rate/calibration and sequential-band gaps.",
    ),
    "0.172.0": (
        "Implement each admitted bladeRF hardware/firmware/FPGA profile through the v0.50.3 plan, transition, generation, read and assessment contract.",
        "Test exact profile mismatch, tuning/rate/bandwidth/gain/clock/port transitions, coherent channels, stale transfers, timestamps, short reads, overruns, disconnect/reset, device assertions and observed consistency.",
    ),
    "0.173.0": (
        "Implement each admitted USRP/UHD device/firmware/FPGA profile through the v0.50.3 plan, transition, generation, read and assessment contract.",
        "Test property/profile mismatch, tuning/rate/bandwidth/gain/clock/antenna transitions, timed/coherent operation, stale packets, timestamps, short reads, overruns, disconnect/reset, device assertions and observed consistency.",
    ),
    "0.174.0": (
        "Implement each admitted LimeSDR/LimeSuite hardware/firmware/FPGA profile through the v0.50.3 plan, transition, generation, read and assessment contract.",
        "Test profile mismatch, tuning/rate/bandwidth/gain/clock/port transitions, calibration changes, stale transfers, timestamps, short reads, overruns, disconnect/reset, device assertions and observed consistency.",
    ),
    "0.37.0": (
        "Make navheim-dsp depend only on navheim-math for runtime twiddles, coefficients, thresholds, CN0/estimators and admitted scalar functions; prohibit private duplicates and platform math.",
        "Test Cargo/DAG edges, no_std/MSRV builds, normative scalar equivalence, fixed-table provenance, backend identity, feature combinations, and scans/reviews for duplicate or platform math paths.",
    ),
    "0.175.1": (
        "Version and bound FPGA/GPU/external-DSP FFT, channelizer, acquisition, candidate, correlator, and tracking artifacts with quantization, scaling, identity, clocks, calibration, build, reset, work, and trust provenance.",
        "Compare every accelerated stage with scalar vectors and test hostile metadata, quantization limits, stale/partial outputs, overruns, firmware mismatch, disconnect, reset, and fallback.",
    ),
    "0.185.2": (
        "Adapt NMEA-only, RTCM, RINEX, and canonical raw-observation sources without inventing receiver health, timing precision, or raw measurements that the source does not expose.",
        "Replay each source independently and test capability absence, mixed sessions, reset, duplicate data, stale epochs, provenance loss, backpressure, and canonical equivalence.",
    ),
    "0.185.3": (
        "Freeze exact official-document and hardware/firmware matrices for SkyTraq, SiRF, MediaTek/PMTK, Trimble, and other candidates; implement only independently testable admitted profiles.",
        "Test every admitted profile on named hardware plus recorded vectors and prove undocumented, reverse-engineered-only, stale-firmware, ambiguous, and untested profiles remain rejected or experimental.",
    ),
    "0.190.3": (
        "Create the publish-disabled Rust 1.97.1 tool workspace with common privilege, configuration, secret, consent, logging, cancellation, update, and local-data policies.",
        "Inspect Cargo metadata and packages and test accidental publication, privilege escalation, unsafe defaults, secret/location logging, config expansion, cancellation, and library-boundary bypass.",
    ),
    "0.190.4": (
        "Implement navheim-cli inspection, conversion, solving, recording, and replay only through public canonical APIs and explicit side-effect plans.",
        "Test every command and output mode, hostile paths/stdin, overwrite consent, broken pipes, redaction, deterministic replay, unavailable capabilities, and non-zero failure status.",
    ),
    "0.190.5": (
        "Implement navheimd with authenticated bounded local IPC/management, least-privilege device access, explicit configuration expansion, cancellation, and lifecycle reporting.",
        "Test unauthorized peers, socket/path races, request/queue limits, slow clients, restart/reset, revoked permissions, secret redaction, and clean shutdown.",
    ),
    "0.190.6": (
        "Implement navheim-caster with tenant, mountpoint, credential, correction-session, rate, and resource isolation over the frozen NTRIP/TLS cores.",
        "Test cross-tenant leakage, replay, downgrade, redirect, slowloris, reconnect storms, stale corrections, credential logs, load limits, and atomic configuration reload.",
    ),
    "0.190.7": (
        "Implement navheim-station with explicit survey state, antenna/frame identity, correction generation, continuity, authority, monitoring, and fail-closed service lifecycle.",
        "Test bad coordinates/antenna metadata, survey rollback, source loss, stale epochs, clock reset, correction interruption, permission loss, and restart continuity.",
    ),
    "0.190.8": (
        "Implement navheim-survey field and post-processing workflows with typed datum/frame/height, provenance, uncertainty, project separation, and reproducible reports.",
        "Compare independent survey results and test mixed projects/frames, stale products, interrupted writes, privacy exports, unavailable quality, and audit reconstruction.",
    ),
    "0.190.9": (
        "Implement navheim-inspector as a bounded diagnostic TUI that preserves raw/canonical distinctions and redacts sensitive fields by default.",
        "Test hostile streams, terminal escapes, high-rate backpressure, resize/input races, disconnect, bounded history, export consent, and redacted snapshots.",
    ),
    "0.190.10": (
        "Implement navheim-viewer desktop/web visualization with explicit local/network mode, data minimization, scoped sharing, uncertainty display, and no hidden telemetry.",
        "Test malicious labels/files, browser boundaries, location/time leakage, stale views, unavailable state, large tracks, export consent, and deterministic rendering data.",
    ),
    "0.190.11": (
        "Implement navheim-lab only for conducted or shielded experiments, with hardware identity, physical interlocks, authorization, power/frequency limits, audit logs, and emergency stop.",
        "Test absent/bypassed interlocks, unauthorized transmit requests, region/config errors, stale devices, limit overflow, disconnect, emergency stop, and receive-only safe default.",
    ),
    "0.196.1": (
        "Compose navheim-sim from the admitted message, signal, dynamics, atmosphere, interference, spoofing, receiver, and replay components without a second implementation.",
        "Test seeded reproducibility, scenario-schema limits, impossible states, cross-constellation time, resource exhaustion, safety labeling, and scalar component equivalence.",
    ),
    "0.196.2": (
        "Define content-addressed external navheim-data manifests with source/license/consent, sensitivity, encryption, retention, access, derivation, and test-vector identity.",
        "Test checksum substitution, partial downloads, unauthorized sensitive data, license mismatch, corpus drift, deletion/retention policy, offline replay, and provenance closure.",
    ),
    "0.198.2": (
        "Keep navheim-fuzz publish-disabled and bind every parser/state-machine target to bounded dictionaries, seed provenance, corpus minimization, sanitizer setup, and reproducible crash artifacts.",
        "Test target discovery, stale corpora, nondeterministic reproducers, secret/location scrubbing, timeout/memory limits, malformed artifacts, and fixed-crash regression promotion.",
    ),
    "0.198.3": (
        "Implement navheim-conformance as a read-only-by-default runner over exact manifest sections, vectors, profiles, expected failures, implementations, and evidence receipts.",
        "Test missing/licensed vectors, wrong revisions, false pass, skipped cells, corrupt evidence, tool/version drift, offline mode, and complete machine-readable reports.",
    ),
    "0.201.1": (
        "Implement navheim-bench with pinned inputs, warmup/statistics policy, CPU/toolchain/feature metadata, correctness prechecks, resource ceilings, and regression thresholds.",
        "Test scalar/optimized selection, noisy and throttled hosts, changed inputs, false improvements, threshold edges, output reproducibility, and no benchmark-only unsafe shortcut.",
    ),
    "0.210.2": (
        "Close the bidirectional ledger for every architecture requirement, public claim, published crate, GitHub-only component, conditional profile, source, milestone, test, status, and non-claim.",
        "Machine-check all frozen records and reject orphaned requirements, unowned tools, unsupported claims, incomplete conditional decisions, stale statuses, and evidence outside the reviewed baseline.",
    ),
    "0.219.1": (
        "Freeze publish-disabled packages, service users/permissions, units, containers, images, deployment defaults, upgrade/rollback, secrets, network exposure, and artifact provenance.",
        "Build from clean environments and test non-root operation, read-only filesystems, dropped capabilities, secret injection, hostile configuration, rollback, shutdown, SBOM/signature identity, and default-deny exposure.",
    ),
}
