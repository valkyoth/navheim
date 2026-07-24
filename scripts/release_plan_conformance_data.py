"""Acceptance data added by the repository-wide requirements audit."""

CONFORMANCE_MILESTONE_DETAILS = {
    "0.1.4": (
        "Generate an acyclic crate/capability DAG covering normal, optional, build, and development edges plus features, tiers, alloc/std, unsafe, TLS, crypto, publication, and platforms.",
        "Test Cargo metadata equivalence, feature unification, cycles, undeclared edges, tier escalation, adapter isolation, and every supported feature combination.",
    ),
    "0.3.4": (
        "Implement narrow no_std fixed-capacity and caller-scratch vectors/matrices, symmetric storage, QR, Cholesky/LDLT, triangular solves, rank updates/downdates, square-root updates, and rank/condition estimates.",
        "Compare arbitrary-precision and independent references for dimension/scratch limits, aliasing, deterministic pivots, singular/indefinite/non-finite inputs, bad scaling, downdate failure, and prohibition of unqualified normal-equation inversion.",
    ),
    "0.3.5": (
        "Implement only admitted normal and chi-square tails/CDFs/quantiles with degrees-of-freedom, confidence, log-probability, validated range, monotonicity, bounded error, and conservative rounding semantics.",
        "Compare arbitrary-precision tables across central/extreme tails and domain boundaries; prove integrity/protection rounding never underestimates risk or permits a looser threshold.",
    ),
    "0.7.2": (
        "Implement bounded UTM/UPS and selected Transverse Mercator profiles with explicit zone/hemisphere, false offsets, datum, frame, epoch, convergence, distortion, and unknown IDs.",
        "Cross-check independent references and test forward/inverse round trips, polar and zone boundaries, antimeridian, invalid coordinates, and unsupported EPSG-database requests.",
    ),
    "0.12.3": (
        "Define static Tier 0 and isolated host extension contracts declaring capabilities, numerical backend, determinism, resources, artifacts, provenance, trust, reset, and invalidation.",
        "Test limit lies, nondeterminism, prohibited trust/correctness bypass, stale output, panic/failure isolation, reset, unregister, and canonical fallback.",
    ),
    "0.12.4": (
        "Define versioned canonical signal metadata for nominal/channel frequency, GLONASS FDMA context, wavelength, chip/code/symbol rates, components, modulation, secondary codes, native time, applicability, and frozen RINEX/RTCM mappings.",
        "Cross-check every admitted constellation/format table and test unknown/partial definitions, FDMA channel bounds, revision conflicts, unit/rounding errors, format round trips, and rejection of duplicate private tables.",
    ),
    "0.13.3": (
        "Define typed horizontal and three-dimensional speed, course over ground, and climb rate with frame, epoch, covariance, derivation, and reason-bearing availability.",
        "Test stationary/low-speed course, vertical-only motion, frame and epoch mismatch, covariance propagation, discontinuities, overflow, and independent trajectories.",
    ),
    "0.14.2": (
        "Select navigation models, corrections, and products by named query epoch, satellite/signal/kind, issue, health, fit/validity, discontinuity, source/session/generation, and separate authentication assessment.",
        "Test future/stale/expired models, equivalent/conflicting healthy sources, issue transitions, session mixing, late authentication, every Selected/Ambiguous/Unavailable/Rejected outcome, considered-candidate evidence, and no latest-wins path.",
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
        "Test plan-reduction receipts, poisoned/conflicting/stale hints, bounded blind fallback, search equivalence, expiry/reset, work limits, and compile/runtime proof that hints cannot resolve canonical time, position, or trust.",
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
