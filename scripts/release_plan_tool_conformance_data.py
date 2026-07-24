"""Acceptance details for repository-only tools and deployment."""

TOOL_CONFORMANCE_MILESTONE_DETAILS = {
    "0.190.3": (
        "Create the publish-disabled Rust 1.97.1 tool workspace with common privilege, configuration, secret, consent, logging, cancellation, update, and local-data policies.",
        "Test accidental publication, privilege escalation, unsafe defaults, sensitive logging, configuration expansion, cancellation, and library-boundary bypass.",
    ),
    "0.190.4": (
        "Implement navheim-cli inspection, conversion, solving, recording, and replay only through public canonical APIs and explicit side-effect plans.",
        "Test commands, output modes, hostile paths/stdin, overwrite consent, broken pipes, redaction, replay, unavailable capabilities, and failure status.",
    ),
    "0.190.5": (
        "Implement navheimd with authenticated bounded local IPC/management, least-privilege device access, explicit configuration expansion, cancellation, and lifecycle reporting.",
        "Test unauthorized peers, path races, request limits, slow clients, restart, revoked permissions, redaction, and shutdown.",
    ),
    "0.190.6": (
        "Implement navheim-caster with tenant, mountpoint, credential, correction-session, rate, and resource isolation over the frozen NTRIP/TLS cores.",
        "Test cross-tenant leakage, replay, downgrade, redirects, slowloris, reconnect storms, stale corrections, credential logs, load limits, and reload.",
    ),
    "0.190.7": (
        "Implement navheim-station with explicit survey state, antenna/frame identity, correction generation, continuity, authority, monitoring, and fail-closed lifecycle.",
        "Test bad metadata, survey rollback, source loss, stale epochs, clock reset, correction interruption, permission loss, and restart continuity.",
    ),
    "0.190.8": (
        "Implement navheim-survey workflows with typed datum/frame/height, provenance, uncertainty, project separation, and reproducible reports.",
        "Compare independent results and test mixed projects/frames, stale products, interrupted writes, privacy exports, unavailable quality, and audit reconstruction.",
    ),
    "0.190.9": (
        "Implement navheim-inspector as a bounded diagnostic TUI preserving raw/canonical distinctions and redacting sensitive fields by default.",
        "Test hostile streams, terminal escapes, backpressure, resize/input races, disconnect, bounded history, export consent, and redacted snapshots.",
    ),
    "0.190.10": (
        "Implement navheim-viewer desktop/web visualization with explicit local/network mode, data minimization, scoped sharing, uncertainty display, and no telemetry.",
        "Test malicious labels/files, browser boundaries, location/time leakage, stale views, unavailable state, large tracks, consent, and deterministic rendering data.",
    ),
    "0.190.11": (
        "Implement navheim-lab only for conducted or shielded experiments, with hardware identity, interlocks, authorization, limits, audit logs, and emergency stop.",
        "Test absent interlocks, unauthorized transmit, region errors, stale devices, limit overflow, disconnect, emergency stop, and receive-only safe default.",
    ),
    "0.196.1": (
        "Compose navheim-sim from admitted message, signal, dynamics, atmosphere, interference, spoofing, receiver, and replay components without a second implementation.",
        "Test seeded reproducibility, schema limits, impossible states, cross-constellation time, exhaustion, safety labels, and scalar equivalence.",
    ),
    "0.196.2": (
        "Define content-addressed external navheim-data manifests with source/license/consent, sensitivity, encryption, retention, access, derivation, and vector identity.",
        "Test checksum substitution, partial downloads, unauthorized data, license mismatch, drift, deletion/retention, offline replay, and provenance closure.",
    ),
    "0.198.2": (
        "Keep navheim-fuzz publish-disabled and bind parser/state-machine targets to bounded dictionaries, seed provenance, corpus minimization, sanitizers, and reproducible crashes.",
        "Test discovery, stale corpora, nondeterministic reproducers, sensitive-data scrubbing, resource limits, malformed artifacts, and regression promotion.",
    ),
    "0.198.3": (
        "Implement navheim-conformance as a read-only-by-default runner over exact manifest sections, vectors, profiles, expected failures, implementations, and receipts.",
        "Test missing/licensed vectors, wrong revisions, false passes, skipped cells, corrupt evidence, tool drift, offline mode, and complete reports.",
    ),
    "0.201.1": (
        "Implement navheim-bench with pinned inputs, statistics policy, CPU/toolchain/feature metadata, correctness prechecks, ceilings, and regression thresholds.",
        "Test scalar/optimized selection, noisy hosts, changed inputs, false improvements, threshold edges, reproducibility, and no benchmark-only unsafe shortcut.",
    ),
    "0.210.2": (
        "Close the bidirectional ledger for every architecture requirement, claim, crate/tool, conditional profile, source, milestone, test, status, and non-claim.",
        "Reject orphaned requirements, unowned tools, unsupported claims, incomplete decisions, stale statuses, and evidence outside the baseline.",
    ),
    "0.219.1": (
        "Freeze publish-disabled native packages, archives and install layouts with reproducible inputs, ownership, permissions, upgrade/rollback and provenance.",
        "Test reproducibility, hostile paths, install/uninstall, upgrade/rollback, ownership, permissions, SBOM and signature identity.",
    ),
    "0.219.2": (
        "Freeze service identities and service units with least authority, sandboxing, device access, lifecycle, logging and explicit network exposure.",
        "Test non-root operation, permission loss, dropped capabilities, read-only filesystems, restart, shutdown, redaction and default-deny exposure.",
    ),
    "0.219.3": (
        "Freeze container images and runtime profiles with pinned bases, non-root identity, read-only roots, device/network boundaries, health, shutdown and provenance.",
        "Test reproducibility, capabilities, mounts, secrets, network isolation, resource limits, shutdown, SBOM and signatures.",
    ),
    "0.219.4": (
        "Freeze deployment configuration expansion, secret injection, permissions, secure defaults, atomic reload and rollback independently of packaging form.",
        "Test hostile configuration, missing secrets, environment leakage, permission errors, partial reload, rollback and no implicit authority.",
    ),
}
