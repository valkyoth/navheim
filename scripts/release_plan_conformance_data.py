"""Acceptance data added by the repository-wide requirements audit."""

CONFORMANCE_MILESTONE_DETAILS = {
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
    "0.119.2": (
        "Name WAAS, EGNOS, MSAS, GAGAN, SDCM, BDSBAS, KASS, and current African SBAS profiles with exact service definitions, regions, signals, messages, validity, and limitations.",
        "Use provider and independent vectors for every admitted matrix cell; test region/profile confusion, future GEO IDs, expiry, conflicting providers, and unsupported profiles.",
    ),
    "0.163.1": (
        "Produce common-view and all-in-view comparison artifacts and bounded CGGTTS V2E original/canonical records, including frozen BDS-3 conventions, calibration, schedule, uncertainty, and provenance.",
        "Cross-check independent BIPM-compatible results and test missing common satellites, mixed scales, station/calibration errors, malformed records, track boundaries, leap events, and explicit exclusion of discipline/consensus.",
    ),
    "0.175.1": (
        "Version and bound FPGA/external-DSP correlator and tracking outputs with clock domain, calibration, device, firmware/bitstream, build/toolchain, reset, work, and trust provenance.",
        "Compare every accepted accelerated artifact with scalar vectors and test hostile lengths/metadata, stale generations, overruns, firmware mismatch, partial transfer, disconnect, and fallback.",
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
