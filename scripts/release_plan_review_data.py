"""Acceptance data added by the third Navheim architecture coverage review."""

REVIEW_MILESTONE_DETAILS = {
    "0.3.3": (
        "Implement first-party deterministic no_std scalar sqrt/hypot, trigonometry, atan2, logarithm/exponential, and narrow backend capabilities.",
        "Compare high-precision references across domains, argument reduction, signed zero, subnormal, exceptional, rounding, MSRV, and no_std cases.",
    ),
    "0.12.2": (
        "Register bounded namespaced user decoders without overriding standards, accessing I/O, or directly mutating canonical state.",
        "Test duplicate/unknown IDs, capacity/work/output limits, progress, opaque artifacts, prohibited trust claims, isolation, and unregister/reset.",
    ),
    "0.20.2": (
        "Expand every named profile from versioned defaults into one printable canonical configuration before planning or side effects.",
        "Prove profile/explicit equivalence, deterministic output, structured capability failure, no silent fallback, and no alternative hidden algorithm.",
    ),
    "0.120.4": (
        "Cover Bancroft/equivalent initialization, position/time/velocity state modes, and elevation/CN0/variance weighting explicitly.",
        "Compare independent solvers for every mode and test initialization failure, mixed weighting, rank loss, state transitions, and unavailable outputs.",
    ),
    "0.129.3": (
        "Model code-differential base observations/corrections, station geometry, issue/signal identity, and common-view epoch matching.",
        "Test station/session mismatch, satellite/frequency mismatch, stale/reordered corrections, base uncertainty, partial views, and atomic expiry.",
    ),
    "0.129.4": (
        "Produce a separately typed DGPS solution with correction age, covariance, quality, provenance, and contributing-station evidence.",
        "Compare independent DGPS references and test age limits, covariance propagation, degraded geometry, unavailable base, and label separation from RTK float.",
    ),
    "0.129.5": (
        "Keep PVT measurement admission separate from post-solution integrity assumptions, policy, and targeted assessment.",
        "Compile-fail coupled APIs and test fact stability, residual/exclusion linkage, late integrity, unavailable assumptions, reassessment, and withdrawal.",
    ),
    "0.135.2": (
        "Implement explicit RtkFixed-to-RtkFloat-to-Dgps-to-Standalone-to-Unavailable degradation, recovery, and supersession artifacts.",
        "Test stale base/phase/code data, ambiguity loss, correction return, hysteresis, rollback, consumer ordering, and no RTK-float-as-DGPS relabeling.",
    ),
    "0.135.3": (
        "Close pivot switching, fix-and-hold rollback, ambiguity ratio/success probability, residual, partial-fix, and re-admission contracts.",
        "Use independent RTK cases for pivot loss, false fix, correlated ambiguities, rollback, threshold boundaries, and deterministic candidate limits.",
    ),
    "0.144.1": (
        "Close pole-tide/ocean-loading hooks, tropospheric wet delay/gradients, and provenance-rich meteorological input contracts.",
        "Compare scientific references and test absent/stale loading, frame/site mismatch, met units/age, gradient observability, and model double application.",
    ),
    "0.150.1": (
        "Run complete OSNMA and QZNMA protocol flows through the reviewed RustCrypto backend after both protocol engines exist.",
        "Replay official/independent end-to-end vectors, delayed keys, malformed tags/signatures, algorithm mismatch, revocation, and backend failure.",
    ),
    "0.155.1": (
        "Close multi-frequency, common-mode code/carrier, AGC/CN0, terrain/visibility, interference, and insufficient-data evidence profiles.",
        "Test every prerequisite absence, benign/adversarial scenario, confidence bound, targeted artifact, false alarm, expiry, and unavailable state.",
    ),
    "0.180.4": (
        "Enumerate bounded candidates, isolate budgeted probes, rank deterministically with explanations, and require explicit opening.",
        "Test permissions, disabled discovery, allowlists, malicious probes, time/work/byte limits, hotplug/removal, identity reuse, ties, and no implicit open.",
    ),
    "0.186.1": (
        "Adapt Android fused/location-provider fixes with provider, permission, mock, elapsed-realtime, accuracy, and reset provenance.",
        "Test provider changes, mock state, denied/revoked permission, stale fixes, capture resets, throttling, and raw-observation non-claims.",
    ),
    "0.186.2": (
        "Implement Android USB-host permission, attach/detach, endpoint, cancellation, transfer, and device-generation lifecycle.",
        "Test permission races, denial, short/stale transfers, detach/reset, identity reuse, cancellation, hostile descriptors, and bounded ownership.",
    ),
    "0.186.3": (
        "Expose Android network/connectivity, background restriction, throttling, cancellation, and provider-reset behavior without hidden retries.",
        "Test network loss/change, background transitions, throttling, captive failure, reset, cancellation, credential redaction, and bounded reconnect policy.",
    ),
    "0.186.4": (
        "Translate Android assistance only after canonical assistance exists, preserving origin, trust, generation, freshness, confidence, and validity.",
        "Test raw-observation separation, untrusted search hints, rollback, cross-session mixing, expiry, unknown fields, and canonical round trips.",
    ),
    "0.186.5": (
        "Implement bounded first-party aligned/unaligned PER primitives, extensions, open types, streaming progress, and canonical encoding.",
        "Test integer/length boundaries, unknown extensions, recursion/nesting/record/bit limits, truncation, alternate encodings, and generated provenance.",
    ),
    "0.187.1": (
        "Freeze exact SUPL/ULP roles, messages, transactions, extensions, aligned/unaligned PER use, transport inputs, and explicit non-claims.",
        "Use licensed/independent interoperability cases for every matrix cell, unknown extensions, state order, timeout, malformed PER, and resource limits.",
    ),
    "0.188.1": (
        "Freeze exact LPP messages, assistance families, transactions, extensions, PER use, translation rules, and explicit non-claims.",
        "Use standards/independent vectors for every matrix cell, unknown extensions, partial assistance, state order, malformed PER, and resource limits.",
    ),
    "0.190.1": (
        "Keep J1939 NAME ordering, address conflicts, commanded address, state transitions, and outgoing decisions pure and bounded in navheim-nmea2000.",
        "Test simultaneous claims, equal/invalid NAME, address exhaustion, commanded changes, reset, lost/reordered frames, and deterministic decisions.",
    ),
    "0.201.0": (
        "Optimize through stable target-specific core::arch or auto-vectorization with scalar fallback; never require nightly portable SIMD.",
        "Test MSRV builds, feature detection, unsupported CPUs, subnormal policy, every fallback, scalar equivalence, and cross-architecture tolerances.",
    ),
}
