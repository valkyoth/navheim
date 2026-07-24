# Navheim Threat Model

Status: foundation baseline; expand with every new input or authority boundary.

## Protected Properties

Navheim protects correctness, availability, integrity evidence, authentication
state, time continuity, bounded resource use, credential secrecy, location
privacy, provenance, reproducibility, and honest capability reporting.

## Adversaries and Faults

- malicious, spoofed, replayed, meaconed, jammed, or malformed RF;
- malformed or compromised receiver firmware output;
- hostile RTCM/NTRIP/SUPL/LPP/product servers;
- malicious NMEA, RTCM, RINEX, IGS, capture, or vendor-protocol data;
- compromised devices, drivers, FFI, DMA, clocks, or OS location providers;
- stale ephemerides, leap tables, corrections, trust roots, or issue-of-data;
- correction/provider/station/reference-frame mixing;
- degenerate geometry, numerical instability, and adversarial solver inputs;
- capacity, CPU, memory, disk, network, decompression, and event-queue
  exhaustion;
- differential parser behavior and ambiguous standards;
- supply-chain, CI, build, release, and dependency compromise;
- logs, captures, credentials, or diagnostics leaking precise location/time.

## Trust Boundaries

RF, receiver bytes, files, network data, OS providers, wall clocks, device
descriptors, user configuration, standards fixtures, external libraries, and
accelerators are untrusted until validated for their specific role.

CRC/FEC correctness does not imply authentication. Navigation-message
authentication does not prove signal-source authenticity. Neither implies
solution integrity.

## Mandatory Mitigations

- bounded parsing, collections, recursion, work, state, and output;
- checked arithmetic and exact-consumption decoding;
- no panics or partial commits across untrusted boundaries;
- explicit freshness, validity, time-scale, frame, provider, and station checks;
- staged/transactional navigation state updates;
- explicit capability planning before hardware is opened;
- caller-visible degradation, exclusion, uncertainty, and authentication state;
- explicit timing invalidation/withdrawal events after stale models, receiver
  resets, discontinuities, authentication failures, or new spoofing evidence;
- separate navigation health, message authentication, signal-source evidence,
  and solution integrity rather than one trusted-time boolean;
- fail-closed policy options and forensic evidence;
- no secret or precise-location logging by default;
- first-party GNSS correctness with isolated reviewed TLS/crypto/FFI adapters;
- fuzzing, independent differential evidence, live-sky evidence, shielded RF
  testing, pentests, and external audits.

## Out of Scope

Navheim does not claim to defeat a fully compromised host, privileged physical
attacker, receiver silicon backdoor, or every sophisticated coordinated
multi-antenna RF attack. It does not provide safety certification merely
because it exposes aviation or integrity research primitives.

Generic PPS capture, NTP/NTS/PTP, local oscillator discipline, clock-family
consensus, holdover after GNSS evidence expires, and privileged system/PHC
adjustment are consumer responsibilities. Navheim provides GNSS timing
evidence and never grants authority to steer a clock.

## Review Triggers

Update this model before adding an input format, network role, device/OS
adapter, unsafe/FFI module, cryptographic trust root, persistent format,
automatic source selection, timing observation/withdrawal contract, RF
generation, or a new solution/integrity claim.
