"""Acceptance data added by the repository-wide requirements audit."""

from release_plan_tool_conformance_data import TOOL_CONFORMANCE_MILESTONE_DETAILS

CONFORMANCE_MILESTONE_DETAILS = {
    "0.1.4": (
        "Generate an acyclic crate/capability DAG covering normal, optional, build, and development edges plus features, tiers, alloc/std, unsafe, TLS, crypto, publication, and platforms.",
        "Test Cargo metadata equivalence, feature unification, cycles, undeclared edges, tier escalation, adapter isolation, and every supported feature combination.",
    ),
    "0.3.4": (
        "Implement no_std fixed/caller-scratch vector and matrix views, checked indexing/layout, transpose/permutation, dot/norm and multiply kernels, depending only on navheim-math.",
        "Test every zero/maximum dimension and scratch boundary, layout/alias rejection, overflow, non-finite input, deterministic operation order, independent scalar references and absence of platform/private math.",
    ),
    "0.3.5": (
        "Implement bounded QR, Cholesky/LDLT, triangular solves, rank updates/downdates and square-root updates with explicit pivot, rank, condition and definiteness evidence.",
        "Compare arbitrary-precision and independent references for singular, indefinite, non-finite, badly scaled and downdate-failure cases; prove no unqualified normal-equation inversion.",
    ),
    "0.3.6": (
        "Expose narrow solver-facing linear solve and least-squares operations that choose only qualified decompositions and return reason-bearing unavailable evidence.",
        "Test dimension/scratch mismatch, rank loss, condition thresholds, decomposition selection, covariance/state ordering and equivalence with independent least-squares references.",
    ),
    "0.3.7": (
        "Implement only admitted normal and chi-square tails/CDFs/quantiles with degrees-of-freedom, confidence, log-probability, validated range, monotonicity, bounded error, and conservative rounding semantics.",
        "Compare arbitrary-precision tables across central/extreme tails and domain boundaries; prove integrity/protection rounding never underestimates risk or permits a looser threshold.",
    ),
    "0.7.2": (
        "Implement the bounded Transverse Mercator forward/inverse kernel in navheim-geo over navheim-core/navheim-math with explicit series/profile provenance.",
        "Cross-check independent references and test convergence/scale/distortion, range boundaries, antimeridian behavior, invalid coordinates, numerical error and no platform/private math.",
    ),
    "0.7.3": (
        "Build reviewed UTM and UPS zone/hemisphere/frame/epoch profiles over admitted projection kernels without embedding an EPSG database.",
        "Test zone edges/overlap, Norway/Svalbard exceptions, equator/poles, false origins, forward/inverse round trips, invalid zones and unsupported database requests.",
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
    "0.14.3": (
        "Define immutable operator advisory/service-status artifacts targeting constellation, satellite, signal, service, region and interval with source/revision, publication, validity, supersession and withdrawal evidence.",
        "Test NANU/NAGU/operator-notice updates, conflicting/stale/future notices, target ambiguity, missing lawful source, replay, withdrawal, model-selection interaction and no mutation of underlying navigation facts.",
    ),
    "0.5.5": (
        "Define checked UTC civil labels and TAI-mediated arithmetic across positive/hypothetical negative leaps; make POSIX conversion explicitly lossy or ambiguous.",
        "Test UTC-model lifecycle, leap boundaries, invalid labels, fold/gap alternatives, POSIX round trips and the leap-smear non-claim.",
    ),
    "0.5.6": (
        "Implement exact-range proleptic Gregorian and ordinal-date conversion with frozen BCE/year-zero and supported-range rules.",
        "Cross-check independent calendar references and test leap-year cycles, BCE/CE boundary, ordinal edges, overflow and exact round trips.",
    ),
    "0.5.7": (
        "Represent Julian Date and Modified Julian Date as integer day plus exact fraction/rational and define explicit UTC/TAI/TT argument requirements.",
        "Cross-check reference epochs/fractions and test noon/midnight conventions, negative days, precision/rounding, scale mismatch, range edges and exact JD/MJD conversion.",
    ),
    "0.7.4": (
        "Define TT and EOP-derived UT1 time arguments with exact derivation, product/series revision, interpolation, validity, uncertainty, provenance, and separation from GnssTimeScale.",
        "Cross-check IERS/IAU references and test EOP gaps/expiry, interpolation boundaries, leap transitions, precision, wrong-scale use, unavailable evidence, and Earth-rotation/tide call-site typing.",
    ),
    "0.18.1": (
        "Define an opt-in versioned bounded snapshot envelope with algorithm/schema, source/generation, validity, provenance, model/calibration/product IDs, capability needs, byte/work limits, corruption digest, and optional external freshness evidence.",
        "Test hostile bytes, versions, sizes, corruption checks, provenance remap, expired/rolled-back state, missing capabilities, incompatible identities, invariant failure, partial restore, atomic commit, and unsupported-state non-claims.",
    ),
    "0.18.2": (
        "Define independent snapshot corruption, authenticity and confidentiality evidence bound to the exact canonical envelope, suite, key identity and associated metadata.",
        "Test every evidence combination, binding/suite/key mismatch, forgery, ciphertext corruption, plaintext limits, downgrade, unavailable primitive and refusal to infer freshness.",
    ),
    "0.18.3": (
        "Define SnapshotFreshness separately: CounterChecked names authenticated non-monotonic local state and cannot satisfy guaranteed freshness; only qualified transactional monotonic evidence yields RollbackResistant.",
        "Test stale authenticated replay, authority/namespace mismatch, absent/lying authority, counter rollback, reservation races, freshness downgrade/unavailable and CounterChecked policy rejection.",
    ),
    "0.18.4": (
        "Freeze minimum protected profiles for sensitive state with consent, retention, privacy-safe diagnostics and mandatory invalidation of restored assessments.",
        "Test plaintext refusal, consent withdrawal, retention expiry, sensitive formatting, provenance remap, restored-assessment invalidation, reconvergence and unavailable protection.",
    ),
    "0.20.3": (
        "Supervise only explicitly opened sources through deterministic health, withdrawal, gaps, generation-safe reselection, and bounded caller-authorized retry/failover policies without trust/accuracy downgrade.",
        "Test source/provider loss and return, flapping, retry exhaustion, same-role generation replacement, policy changes, simultaneous failures, ordering, cancellation, backpressure, recovery, and explicit no-fallback outcomes.",
    ),
    "0.20.4": (
        "Define logical source roles and a compatibility/composition graph that admits valid cross-role mixing and rejects circular, duplicate or semantically incompatible compositions.",
        "Test legitimate and invalid cross-role graphs, role confusion, epoch/generation mismatch, capability changes, deterministic ordering and reason-bearing rejection.",
    ),
    "0.20.5": (
        "Implement same-role handover generations; replacement invalidates dependent clock/bias, calibration, ambiguity/slip, correction, smoothing, PPS/timing, integrity and authenticity state unless an evidenced transform preserves it.",
        "Test default invalidation, clock mapping, uncertainty growth, transformed survival, gaps/discontinuities, withdrawal, reconvergence/coasting, reset and stale-generation rejection.",
    ),
    "0.1.3": (
        "Create a bidirectional ledger from architecture requirements and public claims to owners, milestones, sources, tests, status, and non-claims; make authored-file scope explicit.",
        "Reject missing, duplicate, stale, circular, aggregate, ownerless, testless, or unsupported mappings and scan every repository path covered by the source-size and documentation policies.",
    ),
    "0.36.3": (
        "Keep navheim-capture publish-disabled and route every import/export through the frozen replay model with explicit consent and minimized metadata.",
        "Test malformed streams, interruption, overwrite refusal, path traversal, device reset, disk exhaustion, metadata redaction, deterministic output, and round trips.",
    ),
    "0.35.2": (
        "Implement bounded streaming SINEX-TRO 2.00 headers, site/receiver/antenna/coordinate/eccentricity metadata and zenith/slant solution records with original preservation.",
        "Test official examples, mandatory/optional blocks, fixed columns, epochs, units, unknown blocks, duplicates, truncation, chunk boundaries, semantic conversion and exact/canonical round trips.",
    ),
    "0.35.3": (
        "Implement bounded streaming ORBEX attitude quaternion products with satellite, frame, epoch, convention, validity and provenance identities.",
        "Test official/independent products, quaternion normalization/sign equivalence, frame/order mismatch, gaps, duplicate epochs, unknown records, chunk boundaries and SP3/bias product alignment.",
    ),
    "0.35.4": (
        "Implement the current IGS long product filename grammar as a typed identity carrying project, solution, start, span, sampling, content and format codes.",
        "Test every official example, legacy/long ambiguity, optional station identity, unknown future codes, invalid intervals, path traversal, canonical formatting and filename/content disagreement.",
    ),
    "0.35.5": (
        "Implement bounded IGS site-log 2.0 station, monument, receiver, antenna and equipment-history records with nine-character IDs and explicit effective intervals.",
        "Test official templates, repeated/history sections, unknown fields, malformed dates, overlaps/gaps, equipment replacement, country-code transitions, privacy-sensitive contacts and metadata/product mismatch.",
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
        "Freeze DFMC code, bounded GEO acquisition, tracking and symbol/FEC acceptance matrices before claiming a signal path.",
        "Use licensed official and independent vectors for every admitted cell; test acquisition bounds, FEC limits, mode transitions, GEO confusion and unavailable cells.",
    ),
    "0.118.2": (
        "Freeze DFMC framing, message, correction, integrity, GEO-mode, validity and unsupported-cell matrices independently of the signal path.",
        "Use licensed official and independent vectors; test unknown messages, incomplete sets, stale corrections, integrity transitions, GEO-mode confusion and unavailable cells.",
    ),
    "0.119.2": (
        "Freeze the exact WAAS service definition, region, signals, messages, GEO registry, validity and limitations.",
        "Use WAAS provider and independent vectors; test region/profile confusion, future GEO IDs, expiry, conflicting data and unsupported service states.",
    ),
    "0.119.3": (
        "Freeze the exact EGNOS service definition, region, signals, messages, GEO registry, validity and limitations.",
        "Use EGNOS provider and independent vectors; test region/profile confusion, future GEO IDs, expiry, conflicting data and unsupported service states.",
    ),
    "0.119.4": (
        "Freeze the exact MSAS service definition, region, signals, messages, GEO registry, validity and limitations.",
        "Use MSAS provider and independent vectors; test region/profile confusion, future GEO IDs, expiry, conflicting data and unsupported service states.",
    ),
    "0.119.5": (
        "Freeze the exact GAGAN service definition, region, signals, messages, GEO registry, validity and limitations.",
        "Use GAGAN provider and independent vectors; test region/profile confusion, future GEO IDs, expiry, conflicting data and unsupported service states.",
    ),
    "0.119.6": (
        "Freeze the exact SDCM service definition, region, signals, messages, GEO registry, validity and limitations.",
        "Use SDCM provider and independent vectors; test region/profile confusion, future GEO IDs, expiry, conflicting data and unsupported service states.",
    ),
    "0.119.7": (
        "Freeze the exact BDSBAS service definition, region, signals, messages, GEO registry, validity and limitations.",
        "Use BDSBAS provider and independent vectors; test region/profile confusion, future GEO IDs, expiry, conflicting data and unsupported service states.",
    ),
    "0.119.8": (
        "Freeze the exact KASS service definition, region, signals, messages, GEO registry, validity and limitations.",
        "Use KASS provider and independent vectors; test region/profile confusion, future GEO IDs, expiry, conflicting data and unsupported service states.",
    ),
    "0.119.9": (
        "Freeze the exact SouthPAN service definition, region, signals, messages, GEO registry, validity and limitations.",
        "Use SouthPAN provider and independent vectors; test region/profile confusion, future GEO IDs, expiry, conflicting data and unsupported service states.",
    ),
    "0.119.10": (
        "Admit each named African SBAS provider only from an exact public operational service definition, with region, signal, message, validity and limitation evidence.",
        "Test every admitted provider independently and prove planned, ambiguous, unavailable and unsupported profiles remain explicit non-claims.",
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
    "0.140.1": (
        "Implement bounded SPARTN 2.0.3 framing, header, CRC and opaque protected-payload envelopes without interpreting ciphertext or claiming authenticity.",
        "Use official vectors and test chunk boundaries, lengths, unknown versions/types, CRC failure, truncation, concatenation, resource bounds and opaque protected round trips.",
    ),
    "0.140.2": (
        "Implement admitted SPARTN orbit, clock, code/phase bias, atmosphere and geographic-area correction semantics with issue, applicability, validity and atomic-group identity.",
        "Use official and independent vectors; test unknown subtypes, incomplete groups, grid/area edges, epoch and datum mismatch, expiry, conflicting corrections and unsupported cells.",
    ),
    "0.140.3": (
        "Implement SPARTN encryption/authentication-support message semantics behind audited key and primitive adapter traits, keeping decryption, authentication and correction validity separate.",
        "Use official protected vectors; test wrong/missing/rotated keys, nonce and replay rules, tag failure, unsupported suites, redaction, zeroization boundary and no unauthenticated promotion.",
    ),
    "0.144.2": (
        "Freeze named PPP state layouts and admitted uncombined, ionosphere-free and other observation-combination matrices.",
        "Compare independent PPP engines and datasets; test absent observations, state-layout mismatch, rank loss, frame/epoch mismatch and unavailable combinations.",
    ),
    "0.144.3": (
        "Freeze clock, troposphere, ambiguity and bias states plus product interpolation, issue, validity and discontinuity behavior.",
        "Compare independent products and engines; test product/bias gaps, interpolation edges, frame/epoch mismatch, issue changes, resets and discontinuities.",
    ),
    "0.144.4": (
        "Freeze PPP convergence, mode-transition, invalidation, reconvergence and rollback rules without turning estimator confidence into integrity evidence.",
        "Compare independent datasets; test false convergence, product withdrawal, mode changes, state reset, supersession, rollback and unavailable output.",
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
    "0.169.6": (
        "Represent calibrated antenna-array geometry, element identity, steering vectors, spatial covariance, clock/frame/generation, validity, uncertainty and provenance as bounded evidence.",
        "Use surveyed and simulated arrays; test element permutation/loss, phase/calibration error, covariance defects, aliasing, stale generations, hostile dimensions and unavailable prerequisites.",
    ),
    "0.169.7": (
        "Produce bounded civil adaptive-beamforming and null-steering plans/results with exact objective, constraints, work, scalar fallback, continuity and explicit non-certified anti-jam status.",
        "Compare scalar references and test ill-conditioning, insufficient elements, moving interferers, stale covariance, calibration loss, saturation, fallback, reset and honest unavailability.",
    ),
    "0.42.1": (
        "Define dependency-free SearchAid/AcquisitionHint artifacts for approximate time/location/velocity/orbit and Doppler windows, source/generation, validity, uncertainty, trust, cross-signal aiding and reacquisition identity/expiry.",
        "Test construction bounds, poisoned/conflicting/stale hints, expiry/reset, untrusted sources, privacy-safe formatting and proof that hints cannot resolve canonical time, position or trust.",
    ),
    "0.42.2": (
        "Validate hint sets against immutable maximum PlanReceipt bounds and produce a separate deterministic reduced search plan or bounded blind-fallback decision.",
        "Test conflicting/lost hints, work limits, empty intersections, deterministic ties, no bound expansion, fallback equivalence and no mutation of the maximum receipt.",
    ),
    "0.42.3": (
        "Define and serialize the bounded immutable SearchExecutionReceipt schema for hint IDs, windows, actual work, fallback, decision order, plan/source identity and outcome without claiming executable acquisition integration.",
        "Test canonical/original serialization, capacity/size bounds, unknown fields, hostile receipts, schema versions, no PlanReceipt mutation, stale identities, and explicit pre-acquisition non-claim.",
    ),
    "0.43.2": (
        "Integrate acquisition with SearchExecutionReceipt production for runtime hint acceptance/rejection, actual bounded work, fallback reason, deterministic decision order and outcome.",
        "Test dynamic hint arrival/loss, conflicting windows, deterministic ties/order, budget exhaustion, blind fallback, stale plans/generations, receipt completeness, and executable replay equivalence.",
    ),
    "0.48.3": (
        "Implement separate non-escaping ExecutionScope/ScopedJob and owned asynchronous ExecutionHandle modes over an authoritative bounded registry. Registry/worker ownership, not handle destruction, owns every payload/result/lease slot; generation-bearing JobId never reuses.",
        "Use compile-fail, Miri and model tests for borrow escape, owned lease transfer, registry states, forgotten/leaked handles, exact payload initialization/extraction/destruction, ABA/exhaustion, panic/reentrancy and no hidden Arc/allocation/worker.",
    ),
    "0.48.4": (
        "Linearize Registered dispatch versus pre-dispatch cancellation on one CAS; publish terminal results before claim. Define observing status, consuming try-terminal/join/cancel-and-join and destructor-free handle retirement; nonterminal Drop is allocation-free process abort.",
        "Use Loom/subprocess tests for every dispatch/cancel, completion/claim/Drop and shutdown race; terminal publication ordering, returned handle on not-ready, orphan ownership, unresponsive work, abort/no-unwind and exact API availability.",
    ),
    "0.48.5": (
        "Implement caller-driven shared-borrow cleanup with planned per-call/total budgets, private single-cleaner CAS, deterministic lowest-JobId selection, CleanupRequired admission backpressure and slot reuse only after payload/lease/trace finalization and checked generation increment.",
        "Use Miri/Loom/Kani for cleanup versus completion/claim/drop/admission/shutdown, concurrent Busy before mutation, bounded work/progress, live-handle compatibility, exactly-once cleanup, forgotten entries, generation exhaustion and no hidden reaper.",
    ),
    "0.48.6": (
        "Keep the receipt-producing cleanup primitive crate-private. A must-use ExecutionSupervisor binds executor/plan/trace generation, turns failed-CAS contention into a bounded receipt and records it before Busy becomes observable; trace failure stops or reports unavailable.",
        "Test visibility/forgery/forget, invalid-request mutation freedom, failed-CAS linearization, supervisor mismatch, reservation failure, trace overflow, replay-before-live-CAS, inert-Busy profiles and no raw receipt/guard escape.",
    ),
    "0.48.7": (
        "Have PlanReceipt privately issue bounded must-use/non-cloneable CleanupLane capabilities with deterministic CleanupLaneId and checked non-wrapping CallSequence bound to supervisor/executor/plan/trace generation.",
        "Compile-test private construction and mutable same-lane exclusion; test distinct-lane concurrency, stale/cross-boundary lanes, sequence exhaustion/renewal, forgotten lanes and replay identity independent of arrival/CAS/thread/task order.",
    ),
    "0.48.8": (
        "Reserve worst-case call-event capacity before cleaner CAS. Finalize Busy or a checked global CleanupOrder grant plus exact selected/retired JobIds, work and progress; replay gates successful grants in recorded global order without live CAS ownership.",
        "Test reservation atomicity, Busy/Granted capacity, publication ordering, exact results, incomplete/inverted/duplicate/missing events, global-order exhaustion, permuted concurrent calls, read-only replay and mismatch fail-stop.",
    ),
    "0.48.9": (
        "Move low-level polling to a must-use/non-Copy/non-cloneable/non-serializable ReplayDriver created once per scheduler generation by consuming a sealed SchedulerPermit. SupervisedCleanupPoll::Pending retains one active call and is scheduler-only, side-effect-free control flow.",
        "Compile-test constructors/deserialization/forgery/duplicate/forget and facade type exclusion; test shared-driver distinct-lane concurrency, repeated/permuted Pending, same-call binding, semantic poll invisibility, explicit budgets and no base blocking/spinning.",
    ),
    "0.48.10": (
        "Define CleanupScheduler<Running> request_cleanup, bounded drive, next_ready_cleanup and consuming completion claim. Admission reserves request+completion slots; generation-bearing IDs and turn IDs never reuse; ReadyCleanup is private/must-use/non-clone and completion persists to claim or recorded retirement.",
        "Test exact facade signatures, queue/ID backpressure, request state transitions, deterministic turn selection/record/replay, forgotten IDs/tokens, correlation, forged/duplicate/stale claims, retention/retirement/tombstones and optional declared worker channels.",
    ),
    "0.48.11": (
        "Define consuming Running->Draining begin_shutdown, bounded drive_shutdown and ownership-preserving finish_shutdown. Preserve IDs/tokens/original completed results; atomically cancel only queued/active work; finish only after completions/traces/lanes/driver/executor cleanup, otherwise return private linear ShutdownNotDrained<Self>.",
        "Compile/model/subprocess test typestate methods and safe Option transfer, permanent admission stop, completion/cancellation races, shutdown phases/turn replay, every finish blocker, error recovery, exact report, unfinished scheduler/error abort, forget leak and thread join ordering.",
    ),
    "0.50.3": (
        "Prepare side-effect-free typed front-end plans and issue a framework-private linear PreSubmissionToken; acquiring exclusive command transport consumes it and makes a no-command outcome impossible.",
        "Compile-fail plan/token forgery, clone and post-transport no-mutation construction; test preflight rejection, exact device/profile binding, token consumption, transport exclusivity, timeout and no side effect before acquisition.",
    ),
    "0.50.4": (
        "Define apply outcomes as complete success, proved no-mutation, partial mutation or state unknown. Prior-generation preservation requires exclusive control lease plus a frozen no-autonomous-change profile; every other outcome advances or invalidates generation.",
        "Test command/ACK/read-back evidence, NAK/timeout/reorder, other controller, lease loss, reset/hotplug/autonomous change, rollback/reprobe, cause preservation and no control-flow proof overstated as physical state.",
    ),
    "0.50.5": (
        "Apply coherent multi-device/group plans transactionally and expose reads as initialized-count slices with configuration/capture generation and explicit partial/end/would-block outcomes.",
        "Test every group partial/unknown outcome, rollback limits, coherent generation barrier, short/uninitialized reads, stale buffers, overflow, disconnect, concurrent access, invalidation and safe retry.",
    ),
    "0.48.12": (
        "Implement the acquisition/reacquisition-memory snapshot profile after scheduler integration with search/source identity, expiry, authenticity/confidentiality/freshness, provenance remap, sensitivity and explicit monotonic-authority evidence.",
        "Test cold/warm/hot restore, all three evidence dimensions, stale authenticated/encrypted replay, unavailable monotonic state, expired/poisoned hints, mismatch/reset, corrupt/forged state, privacy, equivalence, invalidation, atomic failure and safe cold start.",
    ),
    "0.54.2": (
        "Implement the minimal tracking-channel snapshot with source/generation, code/carrier/loop state, clock, calibration, validity, provenance and independent authenticity/confidentiality/freshness evidence.",
        "Test mid-symbol/loop restore, compatibility, calibration/reset, stale protected replay, corruption/forgery, privacy, provenance remap, invalidation, atomic restore, reacquisition and cold reconstruction.",
    ),
    "0.54.3": (
        "Implement the minimal raw page-assembly snapshot with source/generation, partial bits/symbols, issue/completeness, timing, parents, validity, provenance and protection evidence.",
        "Test every partial-page boundary, issue transition, duplicate/conflicting fragments, compatibility, stale protected replay, corruption, remap, assessment invalidation, atomic restore and cold reconstruction.",
    ),
    "0.55.1": (
        "Implement the minimal semantic navigation-store/ephemeris snapshot after GPS models with issue, model, health, validity, source, parents, authenticity/confidentiality/freshness, sensitivity, provenance and monotonic-authority evidence.",
        "Test stale/conflicting/future ephemerides, issue/model/health/reset, stale authenticated/encrypted replay, unavailable monotonic state, corruption/forgery, privacy, provenance remap, restored-assessment invalidation, atomic restore and reconstruction.",
    ),
    "0.76.1": (
        "Ingest Galileo HAS Internet Data Distribution corrections and service state while preserving exact source, transport, issue, validity, authentication and signal-in-space equivalence evidence.",
        "Use official IDD and SIS vectors; test registration/transport failure, source mixing, duplicates, delay, issue changes, stale status, equivalence mismatch and explicit unavailable network service.",
    ),
    "0.144.5": (
        "Implement admitted PPP snapshot profiles for named state layouts with products, biases, frame, clocks, ambiguity/troposphere state, covariance, convergence, calibration, expiry, trust, provenance, and independent authenticity/confidentiality/freshness evidence.",
        "Compare uninterrupted/restored solutions and test product/bias/frame changes, stale convergence, covariance invalidity, authenticity/confidentiality/freshness, stale authenticated replay, unavailable monotonic state, privacy, forgery, version mismatch, reconvergence, atomic rejection and unavailable restore.",
    ),
    "0.149.2": (
        "Ingest OSNMA Internet Data Distribution trust material, PKI policy and in-force service state with source, generation, validity, revocation and trusted-time evidence.",
        "Use official IDD/PKI/service vectors; test chain and policy failure, rollover, revocation, stale or conflicting state, transport loss, trust-generation changes and offline unavailability.",
    ),
    "0.150.2": (
        "Define a conditional GPS civil-authentication admission gate: stable lawful public interfaces receive named future milestones while CHIMERA/NTS-3 experimental material remains unavailable and unclaimed.",
        "Review official publications and test capability reporting, experimental/stable distinction, unknown data, absent specifications, policy refusal and proof no inferred decoder or authentication claim exists.",
    ),
    "0.168.3": (
        "Implement admitted fusion snapshot profiles with named state/covariance layout, sensor clocks/generations, calibration/model identity, delayed queues, validity, expiry, trust, provenance, and independent authenticity/confidentiality/freshness evidence.",
        "Compare uninterrupted/restored trajectories and test sensor reset, calibration/model changes, invalid covariance/queues, authenticity/confidentiality/freshness, stale authenticated replay, unavailable monotonic state, privacy, forgery, version mismatch, reconvergence, atomic rejection and unavailable restore.",
    ),
    "0.185.8": (
        "Distinguish read-only/control-capable receiver profiles and execute only side-effect-free planned, typed, allowlisted commands with firmware capabilities, ACK/NAK correlation, timeouts, idempotency and transitions; record command, ACK/NAK, read-back and timing facts in ControlTransaction.",
        "Test arbitrary-byte rejection, unsupported firmware, NAK/timeout/reorder, duplicate commands, partial application, baud/protocol reconnect, power loss, read-back mismatch, receiver assertions, retry limits, redaction and recovery to known state.",
    ),
    "0.185.9": (
        "Create ReceiverConfigurationGeneration bound to device/firmware and effective epoch/interval; drain or stale queues, invalidate affected mappings/calibrations/observations, rebind corrections, and classify volatile/persistent/destructive commands.",
        "Test buffered old/new semantics, transition intervals, queue drain failure, targeted invalidation order, correction rebinding, device replacement, persistent authorization, flash-wear exhaustion, reset/destructive consent, rollback, and recovery.",
    ),
    "0.185.10": (
        "Create ConfigurationAssessment separately from ControlTransaction; target one generation and carry interval, evidence sources, coverage, uncertainty and unverifiable fields, using ReceiverAsserted or interval-scoped ObservedConsistent without claiming internal configuration or signal authenticity.",
        "Test false ACK/read-back, delayed/contradictory streams, partial coverage, uncertainty, unverifiable fields, independent timing/rate/protocol evidence, reset, firmware/device replacement, invalidation, stale generations and refusal to broaden ObservedConsistent.",
    ),
    "0.189.2": (
        "Freeze the canonical domain-separated protected-snapshot binding, suite/version negotiation, self-exclusion and independent authenticity/confidentiality/freshness evidence contract.",
        "Test canonicalization, binding self-exclusion, suite/version mismatch, key/nonce domains, corruption, forgery, redaction and proof that encryption or authentication alone never implies freshness.",
    ),
    "0.189.3": (
        "Order durable Pending reservation, complete seal, authority binding, candidate stage, atomic authority commit, promotion and finalization with a bounded recovery matrix. Only finalization returns RollbackResistant evidence.",
        "Test every state/crash edge, competing writers, pre-commit cancellation, interrupted cleanup, exhaustion, reboot, expiry, key/counter migration, staged loss/mismatch and no older fallback.",
    ),
    "0.189.4": (
        "Define a separate Tier 3 repair capability limited to exact-current-candidate recovery or durable namespace/key/counter retirement plus a fresh-domain continuity break.",
        "Test authorization, candidate verification, anti-revival retirement, fresh domains and continuity artifacts; reject older state, same-namespace reset, nonce reuse and repair without durable proof.",
    ),
    "0.189.5": (
        "Freeze Linux binding, staging, promotion, recovery and optional repair primitives for the v0.189.2-v0.189.4 contract; otherwise report weaker freshness or repair unavailable.",
        "Test fsync/rename/directory boundaries, every recovery state, competing writers, reboot, old-file restoration, namespace migration, bounded retention and anti-revival repair.",
    ),
    "0.189.6": (
        "Freeze distinct FreeBSD, OpenBSD and NetBSD binding, persistence, recovery and optional repair profiles without assuming Linux filesystem or authority guarantees.",
        "Test each supported OS profile, durability boundaries, recovery states, reboot, restoration, namespace migration, unavailable authorities and anti-revival repair.",
    ),
    "0.189.7": (
        "Freeze Windows binding, staging, promotion, recovery and optional repair primitives with exact user/machine scope and honest weaker-capability evidence.",
        "Test every recovery state, competing writers, reboot, scope denial, backup restoration, migration, bounded retention and anti-revival repair.",
    ),
    "0.189.8": (
        "Freeze macOS storage, Keychain binding, recovery and optional repair primitives with access, entitlement and backup semantics.",
        "Test crash states, lock/entitlement denial, reboot, background interruption, backup restoration, migration and honest repair/freshness unavailability.",
    ),
    "0.189.9": (
        "Freeze iOS storage, Keychain binding, recovery and optional repair primitives with data-protection, entitlement, lifecycle and backup semantics.",
        "Test crash states, locked-device/background termination, entitlement denial, reboot, backup restoration, migration and honest repair/freshness unavailability.",
    ),
    "0.189.10": (
        "Freeze Android storage/Keystore binding, recovery and optional repair primitives with API, hardware, StrongBox and invalidation evidence.",
        "Test crash states, process death, software/hardware keys, backup/reinstall restoration, migration, invalidation and honest repair/freshness unavailability.",
    ),
    "0.170.0": (
        "Implement recorded-I/Q and virtual sources against the v0.50.3-v0.50.5 prepare/apply/generation/read contract, with deterministic transition simulation and no invented hardware acknowledgement or observed calibration.",
        "Test plan rejection, generation changes, partial reads, initialized counts, gaps/overruns/end/would-block, stale blocks, mapping/DSP invalidation, deterministic replay and honest unavailable device assessments.",
    ),
    "0.171.0": (
        "Implement the frozen RTL2832U/E4000 profile through the v0.50.3-v0.50.5 prepared-plan, generation, safe-read and assessment contract.",
        "Test hardware/recorded retune, rate, gain, AGC and bias transitions; stale USB buffers, timestamp limits, overruns, short reads, detach/reset, read-back disagreement, observed rate/calibration and sequential-band gaps.",
    ),
    "0.172.0": (
        "Implement each admitted bladeRF hardware/firmware/FPGA profile through the v0.50.3-v0.50.5 plan, transition, generation, read and assessment contract.",
        "Test exact profile mismatch, tuning/rate/bandwidth/gain/clock/port transitions, coherent channels, stale transfers, timestamps, short reads, overruns, disconnect/reset, device assertions and observed consistency.",
    ),
    "0.173.0": (
        "Implement each admitted USRP/UHD device/firmware/FPGA profile through the v0.50.3-v0.50.5 plan, transition, generation, read and assessment contract.",
        "Test property/profile mismatch, tuning/rate/bandwidth/gain/clock/antenna transitions, timed/coherent operation, stale packets, timestamps, short reads, overruns, disconnect/reset, device assertions and observed consistency.",
    ),
    "0.174.0": (
        "Implement each admitted LimeSDR/LimeSuite hardware/firmware/FPGA profile through the v0.50.3-v0.50.5 plan, transition, generation, read and assessment contract.",
        "Test profile mismatch, tuning/rate/bandwidth/gain/clock/port transitions, calibration changes, stale transfers, timestamps, short reads, overruns, disconnect/reset, device assertions and observed consistency.",
    ),
    "0.37.0": (
        "Make navheim-dsp depend only on navheim-math for runtime twiddles, coefficients, thresholds, CN0/estimators and admitted scalar functions; prohibit private duplicates and platform math.",
        "Test Cargo/DAG edges, no_std/MSRV builds, normative scalar equivalence, fixed-table provenance, backend identity, feature combinations, and scans/reviews for duplicate or platform math paths.",
    ),
    "0.175.1": (
        "Freeze a common bounded FPGA/GPU/external-DSP capability, immutable plan, buffer ownership, timestamp, calibration, build, reset, work and scalar-equivalence boundary.",
        "Test capability mismatch, hostile metadata, stale generations, buffer aliasing, quantization declarations, disconnect, reset, resource bounds and deterministic scalar fallback.",
    ),
    "0.175.2": (
        "Version external FFT and channelizer inputs/results with exact scaling, windows, bin/channel mapping, initialized extents, timestamp and work evidence.",
        "Compare scalar vectors and test quantization limits, short/partial outputs, overruns, stale results, firmware mismatch, disconnect, reset and fallback.",
    ),
    "0.175.3": (
        "Version external acquisition and candidate-selection inputs/results with search bounds, deterministic ordering, thresholds, confidence non-claims and scalar fallback.",
        "Compare scalar vectors and test ties, candidate truncation, poisoned metadata, stale/partial results, overruns, reset, disconnect and replay equivalence.",
    ),
    "0.175.4": (
        "Version external correlator and tracking inputs/results with loop identity, ownership, timestamps, discontinuities, validity, initialized extents and scalar fallback.",
        "Compare scalar vectors and test quantization, missing epochs, stale/partial outputs, ownership violation, overrun, reset, disconnect and reacquisition.",
    ),
    "0.175.5": (
        "Define the publish-disabled navheim-fpga host/artifact contract for bitstream, firmware, toolchain, board, interface, signature, provenance and safe-load authority.",
        "Test artifact substitution, incompatible boards/interfaces, unsigned or stale builds, interrupted load, rollback, reset, permission denial, redaction and receive-only safe failure.",
    ),
    "0.185.2": (
        "Adapt NMEA-only, RTCM, RINEX, and canonical raw-observation sources without inventing receiver health, timing precision, or raw measurements that the source does not expose.",
        "Replay each source independently and test capability absence, mixed sessions, reset, duplicate data, stale epochs, provenance loss, backpressure, and canonical equivalence.",
    ),
    "0.185.3": (
        "Freeze the official-document, lawful-access, hardware/firmware, capability and independent-evidence admission contract shared by every optional receiver profile.",
        "Test rejection of undocumented, reverse-engineered-only, ambiguous, stale-firmware and untested candidates; require a separate named patch before implementation.",
    ),
    "0.185.4": (
        "Freeze and implement exact admitted SkyTraq receiver/firmware profiles through the common adapter contract.",
        "Test named hardware and recorded vectors, framing, reset, timing, capability absence, hostile data, backpressure and profile mismatch.",
    ),
    "0.185.5": (
        "Freeze and implement exact admitted SiRF receiver/firmware profiles through the common adapter contract.",
        "Test named hardware and recorded vectors, framing, reset, timing, capability absence, hostile data, backpressure and profile mismatch.",
    ),
    "0.185.6": (
        "Freeze and implement exact admitted MediaTek/PMTK receiver/firmware profiles through the common adapter contract.",
        "Test named hardware and recorded vectors, framing, reset, timing, capability absence, hostile data, backpressure and profile mismatch.",
    ),
    "0.185.7": (
        "Freeze and implement exact admitted Trimble public receiver/firmware profiles; every other vendor remains unavailable until a named patch passes admission.",
        "Test named hardware and recorded vectors, framing, reset, timing, capability absence, hostile data, backpressure, mismatch and vendor non-claims.",
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
        "Freeze publish-disabled native packages, archives and install layouts with reproducible inputs, ownership, permissions, upgrade/rollback and artifact provenance.",
        "Build from clean environments and test reproducibility, hostile paths, install/uninstall, upgrade/rollback, ownership, permissions, SBOM and signature identity.",
    ),
    "0.219.2": (
        "Freeze service users, groups and init/service units with least authority, sandboxing, device access, lifecycle, logging and explicit network exposure.",
        "Test non-root operation, permission loss, dropped capabilities, read-only filesystems, restart, shutdown, log redaction and default-deny exposure.",
    ),
    "0.219.3": (
        "Freeze container images and runtime profiles with pinned bases, non-root identity, read-only roots, device/network boundaries, health, shutdown and provenance.",
        "Build from clean environments and test reproducibility, capabilities, mounts, secrets, network isolation, resource limits, shutdown, SBOM and signatures.",
    ),
    "0.219.4": (
        "Freeze deploy-time configuration expansion, secret injection, permissions, secure defaults, atomic reload and rollback independently of package or container form.",
        "Test hostile configuration, missing/revoked secrets, environment leakage, permission errors, partial reload, rollback and no implicit network/device authority.",
    ),
}

CONFORMANCE_MILESTONE_DETAILS.update(TOOL_CONFORMANCE_MILESTONE_DETAILS)
