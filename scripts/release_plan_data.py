"""Technical acceptance data used by the Navheim release-plan generator."""

PHASE_CHECKS = {
    "A": "MSRV and pinned-stable builds, no_std checks, high-precision math references, boundary tests, metadata checks, and deterministic policy tests",
    "B": "official format examples, malformed/truncated/adversarial streams, exact-consumption and round-trip properties, recovery tests, and parser fuzz smoke",
    "C": "independent numerical references, fixed-point and floating comparisons, deterministic replay, resource bounds, and scalar/optimized equivalence",
    "D": "official GPS vectors, generated baseband, recorded independent captures, receiver comparison, malformed navigation data, and end-to-end replay",
    "E": "official Galileo vectors, generated and recorded signals, receiver comparison, FEC/page faults, time checks, and end-to-end replay",
    "F": "official GLONASS vectors, FDMA/CDMA channel cases, generated and recorded signals, bias/time faults, and independent receiver comparison",
    "G": "official BeiDou vectors, GEO/IGSO/MEO cases, generated and recorded signals, time/correction faults, and independent receiver comparison",
    "H": "official QZSS/NavIC/SBAS vectors, provider/profile cases, generated and recorded signals, integrity timeouts, and independent receiver comparison",
    "I": "independent high-precision and DGPS references, randomized geometry, degenerate/rank-deficient inputs, cross-architecture tolerances, and fault exclusion cases",
    "J": "independent RTK/PPP references, baseline and product replays, ambiguity/slip/freshness faults, frame validation, and receiver/software comparisons",
    "K": "official authentication vectors, delayed/reordered/missing/expired data, trust-root transitions, spoof/jam evidence scenarios, and policy-state tests",
    "L": "independent timing/fusion/navigation references, rollover and clock faults, delayed/out-of-sequence data, freshness expiry, outage invalidation, foreign-adapter round trips, sensor comparisons, and geodesic edge cases",
    "M": "target builds, device/OS fault injection, permission and disconnect handling, bounded discovery/PER/protocol inputs, transport security, and platform/hardware smoke evidence",
    "N": "cross-constellation replay, fuzz coverage, long-duration and rollover tests, numerical/unsafe/API audits, platform matrices, live-sky and shielded-simulator evidence",
}

PHASE_DELIVERABLES = {
    "A": "Use private checked representations, explicit availability/failure states, deterministic no_std math, bounded provenance, and executable capacity/resource contracts.",
    "B": "Separate borrowed raw records, correctness assessment, semantic conversion, and transactional state updates; preserve unknown and original fields.",
    "C": "Accept only immutable validated plan receipts, keep untrusted data inside predeclared work/state limits, and define bit-exact or numerical replay honestly.",
    "D": "Preserve raw GPS artifacts and targeted assessments through navigation-state transactions, observations, solutions, and explicit unavailable results.",
    "E": "Apply the canonical artifact, health, time, authentication, resource, and transaction contracts to every admitted Galileo surface.",
    "F": "Apply the canonical artifact, channel, health, time, bias, resource, and transaction contracts to every admitted GLONASS surface.",
    "G": "Apply the canonical artifact, orbit class, health, time, correction, resource, and transaction contracts to every admitted BeiDou surface.",
    "H": "Bind augmentation/provider/profile state explicitly and preserve integrity timeout, regional applicability, and future identifiers.",
    "I": "Name solver and DGPS state ordering, units, frames, epochs, covariance meaning, numerical backend, rank/condition checks, and unavailable outcomes.",
    "J": "Bind every correction and precise product to an immutable session, provider, station, frame, issue, epoch, validity, and provenance context.",
    "K": "Produce immutable targeted assessments and evidence; keep authentication, signal authenticity, integrity, and versioned policy decisions separate.",
    "L": "Use explicit capture domains, bounded event slots, targeted invalidation, asymmetric correlated uncertainty, deterministic fusion queues, and bounded navigation models.",
    "M": "Plan before side effects, isolate probes/unsafe/FFI, bound PER/protocol work, validate every device report, expose platform limitations, and redact sensitive data.",
    "N": "Close traceability, privacy, resource, numerical, unsafe, platform, interoperability, and reproducibility evidence without weakening non-claims.",
}

PHASE_EXIT_CHECKS = {
    "A": "invalid states, undeclared resource use, and unavailable math capabilities are rejected before state mutation",
    "B": "all chunk boundaries, unknown fields, recovery paths, and original/canonical round trips have deterministic evidence",
    "C": "execution cannot exceed the accepted plan and every optimized result is checked against the normative scalar contract",
    "D": "GPS outputs remain traceable to immutable raw artifacts and independent signal/receiver references",
    "E": "Galileo outputs remain traceable to immutable raw artifacts and official plus independent references",
    "F": "GLONASS outputs preserve channel/time/bias context and pass official plus independent references",
    "G": "BeiDou outputs preserve orbit/time/correction context and pass official plus independent references",
    "H": "regional/provider/integrity applicability and expiry are explicit and independently verified",
    "I": "non-finite, singular, ill-conditioned, unavailable, and excluded cases are explicit and never reported as valid solutions",
    "J": "stale, incomplete, replayed, or cross-session corrections cannot enter or partially update solver state",
    "K": "delayed or changed evidence never mutates facts and can trigger ordered withdrawal or versioned policy reevaluation",
    "L": "clock-domain changes, queue pressure, stale evidence, invalidation, fusion discontinuities, and navigation boundary cases remain explicit",
    "M": "permission, reset, disconnect, probe/PER exhaustion, hostile metadata, unsafe boundary, and sensitive-data failures remain bounded and visible",
    "N": "the milestone closes its named evidence gap with reproducible artifacts and no unsupported production or certification claim",
}

DESCRIPTION_OVERRIDES = {
    "0.217.0": "first complete production-candidate evidence rehearsal",
    "0.218.0": "second production-candidate rehearsal with blocker-only fixes",
}

MILESTONE_DETAILS = {
    "0.1.1": (
        "Derive crate/tier/unsafe checks from Cargo metadata or an architecture "
        "manifest and parse release versions with strict SemVer.",
        "Test malformed tags, future workspace crates, tier violations, stale "
        "pentest parents, and package drift across report-only commits.",
    ),
    "0.1.2": (
        "Define exact document/amendment/vector records and require module, "
        "section, feature, limitation, legal, and test mappings.",
        "Reject aggregate implemented claims, missing revisions, unmapped "
        "tests, silent revision changes, and disallowed retained documents.",
    ),
    "0.2.2": (
        "Choose safe bounded representations honestly; record size/alignment "
        "overhead and do not promise zero-overhead generic storage.",
        "Test zero/full capacity, drop behavior, wraparound, large element "
        "alignment, and representation-size contracts without unsafe code.",
    ),
    "0.4.0": (
        "Define checked, exact, `no_std` native-scale types; preserve unknown "
        "scales and keep raw, ambiguous, and resolved time in different types.",
        "Test every constructor boundary, native epoch, invalid subsecond, "
        "unknown scale, and forbidden implicit Unix/wall-clock conversion.",
    ),
    "0.4.1": (
        "Make all resolved fields private and retain method, anchor, alternatives, "
        "model identity, validity, freshness, and untrusted hints.",
        "Prove equivalent instants have one canonical representation and no "
        "ambiguous or invalid native value can use the resolved type.",
    ),
    "0.4.2": (
        "Wrap foreign capture values with clock-domain and reset-generation "
        "identity while preserving dependency direction.",
        "Prove cross-domain/generation values cannot be ordered or subtracted "
        "without an explicit mapping and reset invalidates comparability.",
    ),
    "0.5.0": (
        "Model continuous atomic time and explicit GNSS-scale conversion "
        "without consulting host wall time.",
        "Test every epoch, offset boundary, out-of-range value, and forbidden "
        "implicit Unix/wall-clock conversion.",
    ),
    "0.5.3": (
        "Use reason-bearing availability for trust-relevant absence and define "
        "target artifact/model, sequence, generation, interval, and withdrawal.",
        "Test pending, unsupported, ambiguous, stale, rejected, failed, replayed, "
        "reordered, replaced, and mandatory-withdrawal states.",
    ),
    "0.13.0": (
        "Keep satellite transmit time, receiver observation time, and caller "
        "capture time distinct and attach uncertainty plus provenance to each.",
        "Test that missing or incomparable clock domains cannot be silently "
        "ordered, subtracted, or promoted to a resolved observation.",
    ),
    "0.13.1": (
        "Separate facts, correctness, authentication, signal authenticity, "
        "integrity, and policy decisions through immutable target IDs.",
        "Prove delayed assessments never mutate facts and bounded parent graphs "
        "reject cycles, overflow, unknown derivations, and stale generations.",
    ),
    "0.13.2": (
        "Make every observation derivation stage a distinct type and preserve "
        "protocol/sample offsets, clocks, corrections, exclusions, and parents.",
        "Compile-fail impossible stage mixing and test raw-to-solver provenance, "
        "unavailable solutions, correction order, and epoch consistency.",
    ),
    "0.16.0": (
        "Define allocation-free progress traits for observations, model "
        "changes, gaps, invalidations, and alerts.",
        "Build a foreign capture-timestamp newtype adapter and prove reset, "
        "withdrawal, backpressure, and error paths are deterministic.",
    ),
    "0.16.2": (
        "Sequence events per source generation and require explicit behavior "
        "for mandatory invalidation under queue pressure.",
        "Model event replay/reorder/loss, acknowledgement failure, coalescing, "
        "producer stop, consumer lag, reset, and forced resynchronization.",
    ),
    "0.17.1": (
        "Classify receipt fields as exact structure, target/profile static "
        "upper bound, work bound, measured envelope, caller assumption, or unavailable estimate.",
        "Test arithmetic overflow, evidence misclassification, target/profile "
        "mismatch, hostile metadata, maximum plans, and execution beyond bounds.",
    ),
    "0.36.2": (
        "Compare semantic artifacts across formats and independent parsers "
        "without discarding raw/original representations.",
        "Vary every chunk boundary and test duplicate, unknown, malformed, "
        "overlong, reordered, recovery, and differential-result cases.",
    ),
    "0.50.1": (
        "Seal exact DSP structure/work separately from measured throughput, "
        "latency and target-specific stack evidence; revalidate every sample block.",
        "Exercise maximum channels/candidates/FEC/FFT/scratch/work, evidence "
        "class errors, gap/overrun, metadata lies, and deterministic eviction.",
    ),
    "0.129.1": (
        "Target integrity bounds, assumptions, risk models, exclusions, validity, "
        "and recovery at immutable epoch/solution artifacts.",
        "Test unavailable assumptions, exclusion exhaustion, late evidence, "
        "withdrawal, recovery, and independence from authentication state.",
    ),
    "0.139.1": (
        "Bind SSR state to peer/provider/station/solution/frame/datum/antenna/"
        "issue/epoch/generation and commit complete groups atomically.",
        "Inject cross-session, incomplete, stale, replayed, conflicting, and "
        "issue-transition groups and prove no partial solver update.",
    ),
    "0.149.1": (
        "Add delayed OSNMA assessments to immutable message/field-set artifacts "
        "with trust-root, key-chain, time-context, renewal and revocation IDs.",
        "Test delayed/reordered keys, root transitions, persistence rollback, "
        "expiry, revocation, reassessment, and meaconed authentic signals.",
    ),
    "0.158.0": (
        "Return native GNSS, exact TAI, and explicit UTC results with model, "
        "leap, era, freshness, uncertainty, and provenance evidence.",
        "Cross-check every constellation conversion and disagreement path "
        "against independent timing references and frozen boundary vectors.",
    ),
    "0.159.0": (
        "Accept caller-captured pulse events and correlate receiver time marks, "
        "edge convention, sequence, frequency-output status, calibrated delay, "
        "and uncertainty.",
        "Test missing, duplicate, reordered, wrapped, reset, early/late, and "
        "leap-boundary pulse/message combinations, frequency lock loss, and "
        "signed delays.",
    ),
    "0.160.0": (
        "Freeze the GNSS timing observation/event API with time-only solution, "
        "capture identity, reason-bearing states, and targeted invalidation.",
        "Implement a separate consumer fixture that maps the public API "
        "without decoding GNSS fields or depending back into Navheim.",
    ),
    "0.160.1": (
        "Use caller-provided bounded event storage with declared maximum event "
        "size, queue depth, outstanding acknowledgements, and progress behavior.",
        "Test undersized slots, consumer stalls, maximum events, assessment "
        "bursts, invalidation priority, no allocation, and resynchronization.",
    ),
    "0.161.0": (
        "Expose satellite and receiver clock bias, drift, covariance, reference "
        "epoch, discontinuity, and a named GNSS timing error budget.",
        "Validate covariance and uncertainty composition without emitting "
        "oscillator steering, servo, PHC, or system-clock actions.",
    ),
    "0.162.0": (
        "Expire or invalidate GNSS evidence on stale models, gaps, resets, "
        "outages, backward steps, and unresolved discontinuities.",
        "Prove Navheim never manufactures holdover observations after GNSS "
        "evidence expires and always emits the withdrawal transition.",
    ),
    "0.162.1": (
        "Make withdrawal target-specific, ordered, acknowledged, replay-resistant, "
        "and mandatory when its reason requires fail-closed behavior.",
        "Test lost/reordered/replayed withdrawal, replacement races, source "
        "generation reset, queue exhaustion, and consumer disagreement.",
    ),
    "0.163.0": (
        "Expose authentication, navigation health, signal-source evidence, "
        "solution integrity, freshness, and policy reasons as separate states.",
        "Test fail-closed consumer policies without collapsing evidence into a "
        "trusted boolean or treating authentication as anti-meaconing proof.",
    ),
    "0.177.1": (
        "Keep parsers safe; isolate bindings and unsafe transfers behind one "
        "reviewed module with ownership, alignment, length, and unplug contracts.",
        "Reproduce bindings and run wrapper models, sanitizers, short/stale "
        "transfer, alignment, cancellation, disconnect, and reset cases.",
    ),
    "0.189.1": (
        "Keep secrets out of Clone, ordinary serialization, Display, URLs, "
        "errors, and routine telemetry; expose them only through guarded access.",
        "Send sentinel secrets through every redirect, TLS, reconnect, parse, "
        "debug, error, and logging path and verify reviewed zeroization claims.",
    ),
    "0.200.1": (
        "Assign Miri, Kani, Loom, sanitizers and hardware fault injection only "
        "to boundaries they can actually execute and record generated provenance.",
        "Audit each unsafe module's evidence matrix and reject unsupported "
        "claims such as treating mocked Miri tests as real driver evidence.",
    ),
    "0.210.1": (
        "Close exact revision/amendment/module/section/constant/feature/vector/"
        "adversarial-test/limitation mappings for every frozen claim.",
        "Machine-check full bidirectional traceability and reject aggregate, "
        "orphaned, stale, legally ambiguous, or evidence-free records.",
    ),
    "0.213.0": (
        "Audit the complete GNSS timing boundary against "
        "`docs/GNSS_TIMING_API.md` and verify dependency direction.",
        "Use an independently implemented external consumer adapter in the "
        "security/timing audit and retain disagreement/invalidation evidence.",
    ),
    "0.214.0": (
        "Document stable consumer integration without adding a Mundilfari or "
        "other clock-framework dependency to any Navheim crate.",
        "Compile and test the published timing examples with a foreign "
        "capture-time newtype and lossless observation mapping.",
    ),
    "0.214.1": (
        "Document every public API's tier, allocation, floating behavior, side "
        "effects, authority, capacities, sensitivity, failures, and non-claims.",
        "Audit rustdoc/examples/config expansion for silent fallback, hidden "
        "authority, precision inflation, sensitive output, and missing limits.",
    ),
}

# Compatible implementation stops added by the second architecture coverage
# review. They augment the established sequence instead of renumbering it.
MILESTONE_DETAILS.update(
    {
        "0.5.4": (
            "Freeze the TAI epoch, canonical attosecond representation, full range, and checked duration arithmetic.",
            "Test range endpoints, non-canonical fractions, every overflow path, serialization, rounding, and forbidden implicit POSIX conversion.",
        ),
        "0.15.2": (
            "Classify every correction by physical target, convention, source, and application stage in an ordered ledger.",
            "Test mutually exclusive alternatives, translated duplicates, wrong signs, stale models, and double-application rejection.",
        ),
        "0.16.3": (
            "Define non-wrapping source-generation, mapping-generation, and event-sequence exhaustion and renewal.",
            "Model terminal counters, mandatory generation-end delivery, acknowledgement loss, identity reuse, replay, and fail-closed resynchronization.",
        ),
        "0.26.1": (
            "Implement each frozen RTCM legacy observation profile with raw/original and canonical forms.",
            "Use official and independent vectors for every admitted message and reject malformed scale, lock, ambiguity, and station contexts.",
        ),
        "0.26.2": (
            "Implement frozen RTCM transformation and projection records without hiding frame, datum, epoch, or validity.",
            "Compare forward/reverse examples, unknown methods, parameter ranges, unit errors, and unsupported transformations.",
        ),
        "0.29.1": (
            "Stream RINEX 2 navigation records while preserving headers, raw fields, constellation/profile limits, and provenance.",
            "Test frozen examples, mixed line endings, truncation, unknown records, exponent/range faults, chunk boundaries, and round trips.",
        ),
        "0.31.2": (
            "Add separately typed RINEX meteorological and clock files for each frozen supported revision.",
            "Test record families, epochs, units, missing/unknown values, ordering, chunk boundaries, and original/canonical output.",
        ),
        "0.31.3": (
            "Implement RINEX 4 observation records and exact picosecond timing fields without precision loss.",
            "Cross-check official examples and test sub-nanosecond round trips, range failures, unknown signals, and mixed-system epochs.",
        ),
        "0.31.4": (
            "Integrate optional CRINEX/Hatanaka only through a receipt bounding bytes, records, lines, and expansion ratio.",
            "Test compression bombs, truncated states, hostile deltas, limit edges, chunking, provenance, and parity with ordinary RINEX parsing.",
        ),
        "0.35.1": (
            "Parse frozen Earth-orientation and reference-frame products with agency, epoch, validity, units, uncertainty, and provenance.",
            "Compare independent products and test stale/missing epochs, frame mismatch, interpolation bounds, unknown fields, and malformed covariance.",
        ),
        "0.37.2": (
            "Normalize sample format and calibration before DC/IQ correction or bounded blanking/notching, retaining distortion evidence.",
            "Test encoding/order/scale variants, clipping, quantization, gain changes, imbalance, hostile metadata, mitigation limits, and replay.",
        ),
        "0.47.2": (
            "Map capture domains only through explicit identities, reset generations, validity intervals, transforms, uncertainty, and discontinuities.",
            "Test endpoints, stale mappings, reset races, discontinuities, composition, precision loss, and forbidden raw cross-domain comparison.",
        ),
        "0.48.2": (
            "Specify SIMD alignment, aliasing, feature detection, fallback, ownership, and unsafe preconditions before dispatch exists.",
            "Test misalignment, overlap, unsupported features, forced fallback, length tails, scalar equivalence, Miri-safe wrappers, and sanitizers.",
        ),
        "0.50.2": (
            "Require official plus independent or externally sourced signal/message vectors before each constellation feature is admitted.",
            "Reject self-generated-only evidence and test vector identity, provenance, corruption, negative cases, scalar replay, and receiver agreement.",
        ),
        "0.114.1": (
            "Implement SBAS L1 codes, acquisition, tracking, symbol evidence, and bounded regional GEO search before message framing.",
            "Use official and independent captures for GEO IDs, Doppler/code search limits, weak signals, false peaks, tracking loss, and reacquisition.",
        ),
        "0.120.2": (
            "Expose typed GDOP/PDOP/HDOP/VDOP/TDOP, solution age, satellite summaries, fix kind, and convergence state.",
            "Compare independent solvers and test rank loss, excluded satellites, stale epochs, unavailable DOP, transitions, and serialization.",
        ),
        "0.120.3": (
            "Expose typed prefit/postfit residual, weighting, contribution, rejection, and exclusion diagnostics targeting solver artifacts.",
            "Test bounded diagnostic capacity, redaction, reweighting, exclusion/re-admission, unavailable causes, and exact artifact linkage.",
        ),
        "0.121.2": (
            "Implement a sequential GNSS-only estimator with named state/process model, initialization, convergence, reset, and unavailable lifecycle.",
            "Compare batch/reference solutions and test outages, time gaps, clock jumps, state resets, singular covariance, and deterministic replay.",
        ),
        "0.126.1": (
            "Return orthometric height only through an identified geoid or vertical-datum model, epoch, interpolation, validity, and uncertainty.",
            "Test model boundaries, missing cells, datum mismatch, stale epochs, poles/seams, independent benchmarks, and ellipsoid/orthometric type separation.",
        ),
        "0.127.1": (
            "Specify RAIM hypotheses, risk allocation, alert limits, time-to-alert, continuity, solution separation, exclusion, recovery, and re-admission.",
            "Test satellite/common-mode faults, exhaustion, delayed detection, unavailable assumptions, alert timing, and independent reference cases.",
        ),
        "0.128.1": (
            "Specify ARAIM constellation/common-mode hypotheses, correlations, URA/SISA/service health, risk allocation, continuity, and availability.",
            "Exercise assumption withdrawal, constellation faults, correlation changes, service-health expiry, allocation bounds, and unavailable outcomes.",
        ),
        "0.129.2": (
            "Consume SBAS integrity as separate targeted evidence and define when protection levels are unavailable rather than merely large.",
            "Test SBAS expiry/conflict, missing hypotheses, alert-limit breach, RAIM/ARAIM separation, withdrawal ordering, and recovery.",
        ),
        "0.146.2": (
            "Conform the optional RustCrypto adapter's primitives, algorithm negotiation, key parsing, feature minima, and secret handling.",
            "Run primitive/backend vectors, algorithm mismatch, malformed keys/signatures, dependency audit, feature combinations, and zeroization review.",
        ),
        "0.160.2": (
            "Acknowledge with exclusive source and slot references after the event borrow ends; retain no hidden slot pointer or shared state.",
            "Model every slot transition, wrong sequence/generation, repeat acknowledgement, cancellation, source reset, mandatory invalidation, and recovery.",
        ),
        "0.164.1": (
            "Model IMU bias, scale factor, axis misalignment, noise, temperature, calibration validity, and uncertainty explicitly.",
            "Use independent sensor references and test calibration expiry, unit/frame mistakes, saturation, temperature sweeps, and unavailable parameters.",
        ),
        "0.164.2": (
            "Implement coning/sculling compensation and named gravity, Earth-rate, and transport-rate models in ECEF and local frames.",
            "Compare independent trajectories and test stationary/rotating/high-dynamic cases, poles, frame transitions, step size, and numerical drift.",
        ),
        "0.165.1": (
            "Add observable lever-arm and sensor time-offset calibration states with priors, bounds, covariance, and lifecycle.",
            "Test unobservable geometries, wrong clocks/frames, delayed data, reset, convergence, cross-correlation, and independent trajectories.",
        ),
        "0.165.2": (
            "Implement a square-root real-time fusion variant preserving the same named states, evidence, and failure semantics.",
            "Compare covariance-form results and test ill-conditioning, positive-definiteness, downdates, long runs, cross-architecture tolerance, and reset.",
        ),
        "0.165.3": (
            "Implement bounded vector tracking across solver and channel loops with scalar-loop fallback and visible aiding/discontinuity artifacts.",
            "Test weak-signal gains, bad-aid rejection, divergence, channel loss, fallback, reacquisition, spoof evidence, and deterministic work bounds.",
        ),
        "0.166.1": (
            "Implement zero-velocity, known-motion, and non-holonomic updates with explicit detectors, assumptions, validity, and targeted residuals.",
            "Test false constraints, slip/skid, stationary motion, detector hysteresis, delayed timestamps, rejection, and recovery.",
        ),
        "0.167.2": (
            "Expose an allocated factor-graph interface reusing canonical measurements, clocks, calibration states, residuals, and provenance.",
            "Compare real-time filters on frozen graphs and test malformed topology, duplicate factors, rank loss, robust loss, and bounded import.",
        ),
        "0.168.1": (
            "Smooth GNSS reacquisition without hiding the correction, state jump, covariance change, source interval, or discontinuity.",
            "Test short/long outages, biased return, clock reset, spoofed return, gating, rollback, monotonic evidence, and consumer visibility.",
        ),
        "0.169.1": (
            "Implement ellipsoid-aware distance, initial/final bearing, destination, cross-track, and along-track calculations.",
            "Compare GeographicLib-class references and test antipodes, poles, dateline, coincident points, invalid ellipsoids, and convergence failure.",
        ),
        "0.169.2": (
            "Define bounded Tier 0 waypoint, route, segment, and track models with explicit great-circle versus rhumb semantics.",
            "Test zero/full capacity, segment transitions, dateline/poles, timestamps, simplification non-claims, serialization, and no-allocation operation.",
        ),
        "0.169.3": (
            "Evaluate geofences with explicit boundary inclusion, horizontal model, altitude datum, time window, uncertainty, and hysteresis.",
            "Test boundary equality, holes, dateline/poles, altitude/time limits, uncertain positions, entry/exit ordering, and resource exhaustion.",
        ),
        "0.169.4": (
            "Provide local-frame navigation and progress primitives while explicitly excluding road-network search, maps, and turn-by-turn routing.",
            "Test frame origins/resets, route-relative geometry, stale solutions, unsupported routing requests, non-claims, and bounded Tier 0 behavior.",
        ),
        "0.185.1": (
            "Define canonical assistance artifacts for approximate time/location/orbit with source, generation, freshness, confidence, trust, and validity.",
            "Test untrusted hints, rollback, cross-session mixing, expiry, receiver/application origins, translation round trips, and search-only restrictions.",
        ),
        "0.190.2": (
            "Execute NMEA 2000/J1939 outgoing decisions through CAN I/O owning timestamps, bus errors, permissions, backpressure, and hardware lifecycle.",
            "Use virtual/hardware CAN tests for reset, timestamp domains, loss/reorder, bus-off, permissions, decision execution, and bounded queues.",
        ),
    }
)
