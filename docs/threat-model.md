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

## Threat-to-Invariant Matrix

| Threat | Required invariant | Required evidence |
| --- | --- | --- |
| RF spoofing/meaconing | RF facts begin untrusted; authenticated data is not origin proof | conducted/shielded replay, gradual time drift, common-clock and multi-source scenarios |
| Jamming/interference | loss and degradation cannot become stale valid output | CW, chirp, pulse, broadband, AGC saturation and partial-band tests |
| Time rollback | GNSS, host wall, capture, persisted watermark and trust-root time stay separate | cold boot, storage rollback, truncated week, stale leap and delayed-key tests |
| Correction mixing | provider/station/frame/antenna/peer/issue/epoch stay session-bound | cross-session injection, replay, incomplete-group and atomic-transition tests |
| Correction duplication | physical target, convention and application stage remain ledger-bound | translated TGD/BGD/bias/PCO/PCV/atmosphere duplicate and wrong-sign tests |
| Parser differential | progress, exact consumption, normalization and recovery are deterministic | independent corpora, chunk variations, unknowns, duplicates and overlong inputs |
| Decompression expansion | compact codecs cannot bypass parser resource receipts | CRINEX/Hatanaka byte, record, line and expansion-ratio boundary tests |
| ASN.1 expansion | PER lengths, open types, extensions and nesting stay within a bit/work receipt | boundary integers/lengths, recursive extensions, unknown open types and malformed canonical encodings |
| Resource exhaustion | accepted plans bound all state, work, queues and output | false acquisition, worst-case FEC, queue pressure and reconnect-storm tests |
| Device-probe side effects | discovery cannot open devices or share corrupted probe state | hostile descriptors/responses, probe budget, permission, hotplug and identity-reuse tests |
| Evidence rollback | later assessment or invalidation cannot be ignored silently | reordered/replayed events, acknowledgement loss and forced-resynchronization tests |
| Integrity-model omission | missing fault hypotheses or assumptions yield unavailable protection | satellite/constellation/provider/common-mode faults, exclusion exhaustion and alert-timing tests |
| Sensor miscalibration | calibration validity, frame, clock, temperature and observability remain explicit | biased/expired calibration, lever-arm, time-offset, thermal and unobservable-motion tests |
| Credential/location leak | routine errors and telemetry exclude secrets and sensitive location/time | sentinel-secret and sensitive-diagnostic snapshot tests |
| FFI/DMA/SIMD fault | unsafe code only transfers validated bounded values into safe ownership | hostile length/alignment, disconnect/reset, model-check and sanitizer evidence |
| Math backend drift | scalar domains/error bounds and optimized equivalence remain explicit | high-precision corpus, exceptional/subnormal inputs, MSRV/no_std and scalar/backend differential tests |

## Mandatory Mitigations

- bounded parsing, collections, recursion, work, state, and output;
- checked arithmetic and exact-consumption decoding;
- no panics or partial commits across untrusted boundaries;
- explicit freshness, validity, time-scale, frame, provider, and station checks;
- staged/transactional navigation state updates;
- immutable artifact IDs and separately targeted correctness, authentication,
  signal-authenticity, integrity and policy-decision objects;
- immutable correction sessions binding peer, provider, station, frame, datum,
  antenna, issue, epoch and generation;
- a physical correction ledger rejecting duplicate or mutually exclusive bias,
  antenna, wind-up and atmosphere applications;
- independently sourced signal/message vectors admitted alongside each
  constellation feature rather than after implementation;
- explicit capability planning before hardware is opened;
- deterministic discovery explanations, isolated bounded probes and explicit
  open authority;
- canonical assistance before Android/SUPL/LPP translation and independently
  bounded PER decoding;
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

Time rollback protection consumes untrusted measurement time, boot-relative
capture time, trusted configuration/model versions and an optional
platform-provided high-water authority. Secure storage, TPMs or monotonic
counters are never implied by `no_std`; their presence and failure are explicit
capabilities.

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
