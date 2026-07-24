# Navheim
## A security-first, `no_std`-first, from-scratch Rust GNSS/PNT platform

**Architecture and implementation plan**

**Standards research baseline:** 23 July 2026

**Target:** Navheim 1.0.0 supports every publicly documented, legally implementable civil/open GNSS signal and service in the frozen 1.0 standards baseline.

---

## 1. Executive decision

Navheim should not be designed as “a GPS parser,” “an SDR demo,” or “a wrapper around receiver vendor SDKs.” It should be a layered **GNSS/PNT platform** that can be used at any point in the positioning chain:

1. raw RF/I/Q samples from one or more SDR front ends;
2. correlator/tracking outputs from an FPGA or external DSP;
3. raw code, carrier-phase, Doppler, AGC and clock measurements from a GNSS chipset;
4. decoded navigation messages from a hardware receiver;
5. correction streams and precise orbit/clock products;
6. operating-system location providers;
7. archived RINEX, RTCM, NMEA, IGS and Navheim capture files;
8. final position, velocity, time, attitude, integrity, authentication and navigation results.

The same core should therefore serve:

- a bare-metal flight controller;
- a Linux GNSS daemon;
- a Windows or macOS desktop application;
- a BSD timing appliance;
- an Android raw-measurement application;
- a browser-based WASM post-processor;
- a datacenter timing service;
- an RTK base station or rover;
- a scientific SDR receiver;
- a survey tool;
- an anti-spoofing monitor;
- a maritime, aviation, automotive, rail, agricultural or robotic system;
- a file-conversion or inspection utility;
- a test laboratory and signal simulator.

The main design rule is:

> **One canonical observation and time model, many independent sources, and multiple solvers and policies.**

A user must never be forced to run the SDR pipeline when a receiver already supplies raw observations, and an SDR researcher must never be forced through an operating-system location API.

---

## 2. Honest meaning of “support everything”

“Every GNSS solution” needs a precise definition. Otherwise 1.0.0 can never have a defensible completion criterion.

### 2.1 Included in the Navheim 1.0 commitment

Navheim 1.0 should support, for the standards snapshot frozen before release:

- every publicly documented civil/open signal of GPS, Galileo, GLONASS, BeiDou, QZSS and NavIC;
- legacy and modern open navigation messages carried by those signals;
- single-, dual-, triple- and full-band operation;
- CDMA, FDMA and multiplexed GNSS signal structures;
- publicly documented open signal-authentication services;
- SBAS and DFMC SBAS through a provider-neutral implementation;
- GBAS/ABAS data models and integrity interfaces where public standards are available;
- standalone, differential, RTK, network RTK, PPP, PPP-AR and PPP-RTK workflows;
- OSR and SSR corrections, including open RTCM and IGS SSR profiles;
- NMEA 0183, NMEA 2000 integration boundaries, RTCM 3.x, NTRIP, RINEX 2/3/4 and principal IGS exchange products;
- public assistance interfaces such as SUPL and 3GPP LPP, subject to protocol licensing and transport constraints;
- raw Android GNSS measurements and desktop/mobile OS location adapters;
- public receiver protocols for which maintainable documentation is available;
- raw I/Q playback and live SDR reception;
- PVT, timing, attitude, integrity, authentication, sensor fusion, surveying and navigation primitives;
- Linux, Windows, macOS, FreeBSD, OpenBSD, NetBSD, Android and bare-metal-compatible core operation;
- WASM decoding, processing and solving where direct hardware access is not required.

### 2.2 Represented, but not falsely promised as decoded

Navheim must catalog, identify and safely preserve metadata for restricted or closed services, but must not claim to decode classified, encrypted or contract-only content without specifications and authorization. Examples include:

- GPS P(Y) and M-code protected content;
- Galileo PRS;
- restricted GLONASS services;
- BeiDou authorized services;
- NavIC Restricted Service;
- closed commercial correction payloads;
- receiver protocols available only under incompatible agreements;
- proprietary LEO-PNT, terrestrial beacon or indoor-location waveforms without public specifications.

For these, Navheim may provide:

- RF-energy and modulation-family detection;
- interference and coexistence measurements;
- raw sample capture;
- opaque frame transport;
- signal identifiers and capability metadata;
- user-supplied decoder/plugin boundaries.

It must not publish speculative decoders or imply military capability.

User decoders register only through a bounded, namespaced extension contract
that declares identifiers, accepted framing, maximum input/output, scratch,
work and progress behavior. Registration cannot override a standard decoder,
claim authentication/integrity, access devices or networking, or mutate
canonical state directly. It returns opaque or separately namespaced artifacts
until an explicit caller policy translates them.

The same rule applies to external algorithms and processing stages. A Tier 0
extension is a statically bound generic implementation with declared
capabilities, numerical backend, determinism, resources, artifact types,
provenance, reset and invalidation behavior. Dynamically loaded host
extensions are isolated to Tier 2/3 adapters. Neither form may bypass
canonical correctness, trust, resource or policy checks.

### 2.3 Future and experimental PNT

The architecture must reserve identifiers and plugin points for:

- LEO navigation and opportunistic PNT;
- pseudolites and local GNSS-like transmitters;
- eLoran and terrestrial timing sources;
- signals of opportunity;
- lunar navigation systems;
- new civil signals added after the 1.0 baseline.

These are not all part of the initial 1.0 decoding promise unless they become public, stable and testable before the standards freeze.

---

## 3. Standards baseline and evidence policy

GNSS does not primarily use IETF RFCs. Navheim should follow the authoritative document class for each surface:

1. constellation operator SIS ICDs and service definitions;
2. RTCM standards for correction protocols and NTRIP;
3. NMEA standards for marine/device sentences and CAN integration;
4. 3GPP and OMA specifications for assisted GNSS;
5. ICAO, RTCA and EUROCAE material for aviation augmentation and integrity;
6. IGS formats and conventions for precise products;
7. IETF RFCs for underlying Internet transports and security where applicable;
8. vendor protocol specifications only for vendor adapters.

Create a repository file named `standards/manifest.toml`. Every implemented feature must map to a record containing:

```toml
[[document]]
id = "galileo-os-sis-icd"
title = "Galileo Open Service Signal-in-Space Interface Control Document"
revision = "2.2"
publisher = "EUSPA / European Union"
published = "2025-11"
status = "normative"
license_class = "public-reference"
local_copy = false
sha256 = "...only when a legally retained copy exists..."
implemented_by = ["navheim-galileo"]
tests = ["galileo_e1_inav_vectors", "galileo_e5a_fnav_vectors"]
```

Rules:

- Do not commit paid NMEA, RTCM, RTCA, EUROCAE or other copyrighted standards merely because the project is open source.
- Public documents may be mirrored only when their publication terms clearly permit it.
- Otherwise store title, version, publisher, retrieval date, checksum of the developer’s local copy and implementation/test mapping.
- Normative constants must cite a section/table identifier in source comments.
- Every release candidate reruns the document inventory; 1.0 freezes exact revisions.
- A new standard revision never silently changes behavior. It creates a new conformance profile and a deprecation/migration note.

Important 2026 baseline examples include Galileo OS SIS ICD 2.2, RTCM 10403.4, NTRIP 10410.1, NMEA 0183 4.30, NMEA 2000 3.000 and RINEX 4.02. The release team must verify that these remain current at the final standards freeze.

---

## 4. Complete use-case inventory

The API and crate boundaries should be justified by real user jobs, not by protocol names alone.

### 4.1 Basic positioning and application development

- Obtain latitude, longitude, ellipsoidal height and orthometric height.
- Obtain ECEF, ENU/NED and projected coordinates.
- Obtain ground speed, 3D velocity, course over ground and climb rate.
- Query accuracy, covariance, DOP, age, satellite count and fix type.
- Subscribe to fixes or poll deterministically without async.
- Record routes, waypoints and tracks.
- Compute distance, bearing, destination, cross-track error and geofences.
- Detect stale, impossible or low-integrity fixes.
- Automatically use the best available receiver, OS provider or replay source.

### 4.2 Embedded and robotics

- Operate without `std` or a heap.
- Feed UART/SPI/CAN bytes into bounded parsers.
- Use caller-provided buffers.
- Fuse GNSS with IMU, odometry, wheel ticks, magnetometer and barometer.
- Survive temporary GNSS outages through dead reckoning and explicit coasting
  state without inventing fresh GNSS evidence.
- Produce fixed-rate state estimates.
- Control computational budgets, memory use and signal selection.
- Use deterministic fixed-point DSP on MCUs or FPGAs.

### 4.3 SDR and signal research

- Acquire and track signals from raw complex samples.
- Use real integer sample formats without immediately converting to `f32`.
- Plan multiple front ends, center frequencies, bandwidths and coherent clocks.
- Run acquisition offline, in real time or hardware accelerated.
- Inspect correlation surfaces, Doppler, CN0, lock indicators and loop state.
- Inject custom acquisition/tracking algorithms.
- Generate and replay reproducible captures.
- Compare front ends, antennas, filters and interference environments.

### 4.4 Surveying and geodesy

- Log complete code, phase and Doppler observations.
- Operate base/rover and network RTK.
- Resolve integer ambiguities and report validation evidence.
- Apply antenna phase-center, Earth tide, ocean loading and atmospheric models.
- Consume precise orbit, clock, bias and ionosphere products.
- Run static, rapid-static and kinematic post-processing.
- Export RINEX and survey reports.
- Maintain station monuments, reference frames and coordinate epochs.

### 4.5 Precision machine control

- Centimeter-level positioning for agriculture, drones, construction, mining and robotics.
- Low-latency corrections and age monitoring.
- Dual-antenna heading and multi-antenna attitude.
- Fail-safe transitions among RTK fixed, float, DGPS and standalone modes.
- Integrity limits and control-system-safe outputs.

### 4.6 Timing and frequency

- Recover and validate GNSS system time.
- Translate among GPS, GST, BDT, GLONASS time, UTC variants, TAI and Unix time.
- Interpret receiver PPS, 10 MHz and time marks using caller-provided capture
  timestamps.
- Expose clock-error, uncertainty, health, authentication and integrity
  evidence without disciplining a local clock.
- Detect leap-second, rollover, week ambiguity and time-spoofing conditions.
- Feed consumer-owned NTP/PTP/time frameworks without embedding those
  protocols or depending on those frameworks in the GNSS core.
- Measure time-transfer uncertainty and cable/antenna delays.
- Build Stratum-0/primary-reference appliances.

### 4.7 Cybersecurity and resilience

- Verify Galileo OSNMA and QZSS QZNMA when applicable.
- Enforce authentication policies per signal and solution.
- Compare independent constellations, frequencies, antennas and receivers.
- Detect inconsistent time, Doppler, angle, ephemeris and navigation data.
- Detect jamming, meaconing, spoofing, replay, impossible motion and clock manipulation.
- Preserve a signed provenance chain from raw observation to final fix.
- Run in “fail closed,” “degrade with warning” or “availability first” modes.
- Export evidence suitable for incident response.

### 4.8 Aviation, maritime, rail and safety-oriented systems

- Decode augmentation and integrity data.
- Calculate protection levels separately from estimated accuracy.
- Support RAIM/ARAIM inputs and exclusion evidence.
- Preserve service-volume, alert-limit and timeout semantics.
- Expose all assumptions needed for independent certification.
- Never label an uncertified build as safety-of-life certified.

### 4.9 Atmospheric and scientific research

- Total electron content and ionospheric delay studies.
- Tropospheric delay and water-vapor estimation.
- Scintillation and multipath metrics.
- Reflectometry and remote sensing from direct/reflected GNSS signals.
- Space-weather observation.
- Precise time/frequency comparison.
- Reproducible batch processing from archived observations.

### 4.10 Test, education and conformance

- Decode known vectors one layer at a time.
- Generate synthetic navigation messages and baseband signals.
- Perturb bits, timing, Doppler, multipath and interference.
- Differentially compare with known receivers and independent software.
- Inspect every intermediate state without modifying production algorithms.
- Fuzz all file, network and over-the-air parsers.

---

## 5. Constellation and signal coverage target

The following is the required 1.0 catalog. Exact channel/component names must be verified against the frozen ICD revisions.

### 5.1 GPS — `navheim-gps`

Open/civil targets:

- L1 C/A acquisition, tracking and LNAV;
- L1C data/pilot components and CNAV-2;
- L2C CM/CL and CNAV;
- L5 I/Q and CNAV;
- legacy almanac, ephemeris, UTC and ionosphere parameters;
- modernized clock, ephemeris, integrity and inter-signal corrections;
- navigation-message parity/FEC as specified;
- week rollover and fit-interval handling;
- current and historical PRN assignments through versioned registries.

Restricted signals are represented as identifiers and measurable RF components only.

### 5.2 Galileo — `navheim-galileo`

Open targets:

- E1 B/C and I/NAV;
- E5a I/Q and F/NAV;
- E5b I/Q and I/NAV;
- E5 AltBOC processing and component processing;
- E6 B/C and HAS;
- Galileo System Time and UTC conversion;
- OSNMA protocol, trust chain and delayed-key processing;
- High Accuracy Service corrections;
- Signal-in-Space accuracy/status/integrity fields;
- Search and Rescue data needed for return-link-service applications;
- Timing Service Message support;
- Emergency Warning Satellite Service messages as the public service stabilizes;
- new publicly documented signal components such as the E5 quasi-pilot mode;
- forward-compatible page and reserved-field preservation.

Galileo PRS is cataloged but not decoded.

### 5.3 GLONASS — `navheim-glonass`

Open targets:

- L1OF and L2OF FDMA acquisition, channelization, tracking and navigation strings;
- frequency-channel number handling;
- GLONASS time and UTC(SU) conversion;
- legacy almanac and ephemeris models;
- public CDMA signals such as L1OC, L2OC and L3OC where official ICDs are available;
- inter-frequency and inter-system bias metadata;
- FDMA-specific ambiguity and receiver-channel calibration support.

Restricted services are cataloged only.

### 5.4 BeiDou — `navheim-beidou`

Open targets:

- B1I and legacy D1/D2 navigation;
- B1C and B-CNAV1;
- B2I where publicly documented;
- B2a and B-CNAV2;
- B2b and B-CNAV3/basic navigation;
- B2ab combined processing;
- B3I;
- GEO, IGSO and MEO orbit-class handling;
- BeiDou Time conversion;
- PPP-B2b corrections;
- public BDSBAS interfaces;
- public short-message/SAR-related interfaces only where a stable open specification permits interoperable implementation.

Authorized services are cataloged only.

### 5.5 QZSS — `navheim-qzss`

Targets:

- L1 C/A, L1C, L1C/B and relevant modern components;
- L2C;
- L5;
- L1S sub-meter-level augmentation/disaster messaging;
- L5S augmentation/test services where public;
- L6D CLAS and MADOCA-family correction services;
- L6E/QZNMA authentication content;
- SLAS, CLAS and MADOCA-PPP service profiles;
- QZSS system status, health and regional geometry;
- QZNMA authentication of applicable QZSS/GPS/Galileo content according to the current interface specification.

### 5.6 NavIC — `navheim-navic`

Targets:

- L5 SPS;
- S-band SPS;
- new L1 SPS signal and navigation message;
- GEO/IGSO constellation geometry;
- NavIC system time conversion;
- public ionosphere, clock and ephemeris content;
- public messaging interfaces in the current ICD.

Restricted Service is cataloged only.

### 5.7 SBAS and augmentation — `navheim-sbas`

Implement the protocol generically first, then provider profiles:

- L1 legacy SBAS;
- dual-frequency multi-constellation SBAS on L5/E5a-class signals;
- fast, long-term, ionosphere and integrity corrections;
- GEO ranging and non-ranging modes;
- service regions, issue-of-data tracking, degradation and timeout rules;
- protection-level inputs and alert semantics.

Provider profiles should include, as public documentation becomes available and independently testable:

- WAAS;
- EGNOS;
- MSAS;
- GAGAN;
- SDCM;
- BDSBAS;
- KASS;
- SouthPAN;
- ASECNA/ANGA and successor African SBAS profiles;
- future provider IDs without core enum breakage.

A provider’s current operational certification status is deployment metadata, not hard-coded protocol behavior.

---

## 6. Correction, assistance and exchange ecosystem

### 6.1 RTCM and NTRIP

`navheim-rtcm` should implement from scratch:

- RTCM 3 framing and CRC;
- station, antenna and receiver descriptors;
- legacy observations where still required;
- MSM1–MSM7 generic observation messages;
- ephemeris messages for all supported constellations;
- network RTK messages;
- SSR orbit, clock, code bias, phase bias, atmosphere and integrity content covered by the standard;
- transformation and projection messages needed by surveying workflows;
- strict and permissive decoding modes;
- zero-copy message views and owned forms;
- round-trip encoding with reserved bits preserved when safe.

`navheim-ntrip` should implement:

- NTRIP client, server and caster roles;
- source-table parsing;
- version 1 and version 2 behavior;
- HTTP transport through a tiny internal adapter;
- optional TLS via `navheim-tls-rustls`;
- certificate/hostname validation with no TLS downgrade;
- redirects disabled or constrained to the approved host/mountpoint policy;
- bounded request/status/header/source-table/chunk sizes and reconnect rate;
- compression disabled unless a separately bounded profile admits it;
- explicit host/mountpoint allowlists and GGA-upload consent;
- credentials outside URLs/errors with redacted diagnostics;
- reconnect/backoff policy supplied by the application, not hidden threads.

RTCM/correction caches use immutable session identities binding transport peer,
provider/mountpoint, station/solution, frame/datum, antenna, authenticated peer,
issue/epoch and generation. Incomplete SSR groups, stale data and cross-session
mixing are rejected atomically.

### 6.2 Precise products

`navheim-products` should cover:

- SP3 precise orbit files;
- precise clock products;
- SINEX and Bias-SINEX;
- IONEX;
- ANTEX;
- earth-orientation and reference-frame inputs;
- IGS SSR profiles;
- product validity, interpolation and provenance.

The crate must preserve source agency, creation epoch, solution center, update interval and quality metadata.

### 6.3 RINEX

`navheim-rinex` should support:

- RINEX 2 observation and navigation files for legacy archives;
- RINEX 3 multi-GNSS observations/navigation;
- RINEX 4 observations, picosecond timing fields, generic navigation records
  and current constellation additions;
- observation, navigation, meteorological and clock files where applicable;
- Hatanaka/compact integration via a separate optional codec if legally and technically appropriate;
- streaming parsing and writing;
- lossless unknown-header preservation;
- bounded line handling and explicit non-UTF-8 policy;
- canonical output and original-format output modes.

Any compact/Hatanaka adapter is bounded before admission: decompressed bytes,
records, line length and expansion ratio are planned and enforced. A compact
stream cannot bypass the ordinary RINEX parser's progress, resource and
provenance contracts.

### 6.4 NMEA

`navheim-nmea` should support:

- NMEA 0183 framing, checksums, talker IDs and all GNSS-relevant standard sentences in the licensed implementation baseline;
- manufacturer/proprietary sentence registration without putting vendor logic in the core;
- strict numeric, coordinate and time validation;
- partial-line and noisy-serial recovery;
- no allocation operation.

NMEA 2000 uses CAN and licensed parameter-group definitions. Implement
transport and a legal, versioned PGN layer in `navheim-nmea2000`; do not copy
protected tables from unofficial sources. CAN frame sources/sinks and platform
adapters own bus I/O, timestamp domains, permissions, backpressure, bus-off
recovery and hardware lifecycle. The protocol crate owns bounded
frame/fast-packet assembly, legal PGN semantics and the pure J1939
address-claim state machine: NAME ordering, conflicts, commanded addresses and
outgoing-frame decisions. An adapter executes those decisions but never
defines address-claim semantics.

### 6.5 Assistance

`navheim-assist` should expose a common assistance model and adapters for:

- OMA SUPL, including ULP messages;
- 3GPP LPP positioning assistance;
- Android raw measurement inputs;
- receiver-provided aiding data;
- application-injected approximate time, location and orbit assistance.

The canonical model precedes every protocol adapter. Time, location, orbit and
other assistance are immutable artifacts carrying source, generation,
freshness, confidence, validity and whether they are receiver-provided or
application-injected. Untrusted hints can narrow a search but cannot silently
resolve time, position or trust. Rollback and cross-session mixing are rejected
before SUPL, LPP, Android or receiver-specific translation.

Transport security belongs in optional TLS/network adapters. ASN.1 PER encoding/decoding is a core protocol concern and should be implemented in a small reusable internal module rather than delegated to a GNSS library.

The first-party PER core admits only the aligned/unaligned profiles required
by the frozen SUPL/LPP matrices. It bounds constrained/semi-constrained
integers, length determinants, extension bitmaps, open types, recursion,
nesting, allocation, records and bit work; preserves unknown extensions; and
provides partial streaming, exact consumption and canonical encoding.
Generated schemas record source revision, generator version and reproducible
output provenance.

---

## 7. Repository and crate architecture

Use one monorepo until well after 1.0. This provides atomic changes, a single security policy, coordinated CI and lockstep compatibility. Do not create one Git repository per receiver or signal.

### 7.1 Published crates

The following crates have independently useful public APIs and should be published to crates.io.

#### Facade and foundation

- **`navheim`** — ergonomic facade, profiles, prelude, auto source selection and feature bundles.
- **`navheim-core`** — zero-dependency common types: units, time, coordinates, IDs, observations, ephemerides, events, errors, capabilities, bounded collections, bit views, checksums, FEC primitives and stable traits.
- **`navheim-math`** — zero-dependency, `no_std` deterministic elementary
  floating math, admitted statistical kernels and narrowly scoped backend
  traits used by coordinates, DSP and solvers.
- **`navheim-linalg`** — zero-third-party-dependency, `no_std`, bounded
  fixed-capacity and caller-scratch linear algebra depending only on
  `navheim-math`; it does not expose a broad generic matrix ecosystem
  prematurely or reimplement scalar math.
- **`navheim-geo`** — zero-third-party-dependency, `no_std` mathematical
  coordinate transformations, projections, ellipsoidal geodesics,
  great-circle/rhumb primitives and frame transformations depending on
  representation-only `navheim-core` plus `navheim-math`.
- **`navheim-dsp`** — zero-third-party-dependency, `no_std` DSP algorithms
  depending on `navheim-math`: complex types, NCOs, filters, FFTs, resamplers,
  channelizers, acquisition and tracking-loop primitives.
- **`navheim-sdr`** — source/front-end abstractions, band planning, sample metadata, coherent-array support and device adapter traits.
- **`navheim-executor`** — optional Tier 2 `std` multicore execution,
  cancellation and bounded-queue adapter over canonical scalar work units; it
  is outside `navheim-dsp`.

#### Constellations

- **`navheim-gps`**
- **`navheim-galileo`**
- **`navheim-glonass`**
- **`navheim-beidou`**
- **`navheim-qzss`**
- **`navheim-navic`**
- **`navheim-sbas`**

Each constellation crate contains modules for code generation, acquisition hints, tracking configuration, FEC, framing, navigation decoding, ephemeris conversion and signal-specific corrections. Do not publish one crate per signal because that would create dependency and version fragmentation.

#### Solving and applications

- **`navheim-pvt`** — standalone and weighted least-squares PVT, velocity, clock, covariance and solution management.
- **`navheim-rtk`** — differential observations, cycle-slip handling, ambiguity management, single/double differences, network RTK and validation.
- **`navheim-ppp`** — precise product interpolation, PPP, PPP-AR and PPP-RTK/SSR state models.
- **`navheim-integrity`** — RAIM/ARAIM building blocks, fault detection/exclusion, protection levels, consistency checks and integrity state.
- **`navheim-fusion`** — IMU/odometry/barometer/magnetometer fusion, dead reckoning and multi-rate filters.
- **`navheim-timing`** — GNSS time resolution, time-only solutions,
  PPS/time-mark meaning, receiver clock estimates, delay calibration,
  uncertainty, health, authentication, integrity and consumer-facing events.
- **`navheim-security`** — navigation-message authentication protocols, anti-spoofing evidence, provenance and security policy. Cryptographic primitives are injected through traits.
- **`navheim-navigation`** — bounded waypoints, routes, tracks, geofences,
  segment policies and navigation-facing wrappers composed from
  `navheim-geo`; it depends on `navheim-geo`, never reimplements coordinate
  mathematics and is intentionally not a road-map routing engine.
- **`navheim-science`** — optional calibrated scintillation, reflectometry,
  space-weather and remote-sensing artifacts built from canonical observations;
  it does not turn exploratory metrics into operational scientific products.

#### Formats and interoperability

- **`navheim-nmea`**
- **`navheim-nmea2000`**
- **`navheim-rtcm`**
- **`navheim-ntrip`**
- **`navheim-rinex`**
- **`navheim-products`** — SP3, CLK, SINEX, Bias-SINEX, IONEX, ANTEX and related IGS products.
- **`navheim-receiver`** — public hardware-receiver protocol adapters and auto-detection.
- **`navheim-assist`** — common A-GNSS model, SUPL/LPP and mobile raw-measurement adapters.
- **`navheim-io`** — `std` platform I/O for serial, native USB, sockets, files
  and OS location providers; generic PPS capture remains consumer-owned.

#### Explicit integration adapters

These should be small, optional crates so external dependencies never leak into GNSS core:

- **`navheim-tls-rustls`** — Rustls-backed secure transport for NTRIP/SUPL/other network clients.
- **`navheim-crypto-rustcrypto`** — audited cryptographic primitive backend for OSNMA/QZNMA when the selected algorithms are supported.
- **`navheim-snapshot-protection`** — optional `std` bridge to
  caller-provided external AEAD and platform-keystore authorities with a
  common protection-envelope/lifecycle contract and separately admitted
  platform modules; it keeps platform dependencies, key custody and encryption
  policy outside canonical snapshot formats.
- **`navheim-uhd`** — UHD adapter for Ettus/NI radios.
- **`navheim-bladerf`** — libbladeRF or direct device adapter.
- **`navheim-lime`** — LimeSuite or direct device adapter.
- **`navheim-android`** — Android platform bindings.

External libraries in these adapters are acceptable because they are not implementing GNSS algorithms and can be omitted.

### 7.2 GitHub-only crates and binaries

Do not initially publish the following to crates.io:

- **`navheim-cli`** — inspect, convert, solve, record and replay.
- **`navheimd`** — system daemon exposing local sockets/gRPC-like or HTTP management adapters.
- **`navheim-caster`** — NTRIP caster deployment binary.
- **`navheim-station`** — reference/base-station service.
- **`navheim-survey`** — field and post-processing survey application.
- **`navheim-inspector`** — message/signal diagnostic TUI.
- **`navheim-viewer`** — desktop/web visualization.
- **`navheim-lab`** — controlled interference, spoofing and robustness experiments.
- **`navheim-sim`** — high-level scenario and signal generation tooling.
- **`navheim-conformance`** — standards test runner.
- **`navheim-bench`** — performance harnesses.
- **`navheim-fuzz`** — fuzz targets and corpus management.
- **`navheim-capture`** — capture utilities until the file format is stable.
- **`navheim-fpga`** — HDL/firmware and host glue.
- packaging, service files, containers and deployment configurations.

Large raw captures and generated test vectors should live in a separate `navheim-data` repository or release-object store, not in the primary Git history.

### 7.3 Suggested tree

```text
navheim/
├── Cargo.toml
├── SECURITY.md
├── CONTRIBUTING.md
├── LICENSE-APACHE
├── LICENSE-MIT
├── standards/
│   ├── manifest.toml
│   ├── coverage.md
│   └── licensing.md
├── crates/
│   ├── navheim/
│   ├── navheim-core/
│   ├── navheim-math/
│   ├── navheim-dsp/
│   ├── navheim-sdr/
│   ├── navheim-gps/
│   ├── navheim-galileo/
│   ├── navheim-glonass/
│   ├── navheim-beidou/
│   ├── navheim-qzss/
│   ├── navheim-navic/
│   ├── navheim-sbas/
│   ├── navheim-pvt/
│   ├── navheim-rtk/
│   ├── navheim-ppp/
│   ├── navheim-integrity/
│   ├── navheim-fusion/
│   ├── navheim-timing/
│   ├── navheim-security/
│   ├── navheim-navigation/
│   ├── navheim-nmea/
│   ├── navheim-nmea2000/
│   ├── navheim-rtcm/
│   ├── navheim-ntrip/
│   ├── navheim-rinex/
│   ├── navheim-products/
│   ├── navheim-receiver/
│   ├── navheim-assist/
│   ├── navheim-io/
│   └── adapters/
├── tools/
│   ├── navheim-cli/
│   ├── navheimd/
│   ├── navheim-caster/
│   ├── navheim-station/
│   ├── navheim-survey/
│   ├── navheim-inspector/
│   ├── navheim-lab/
│   └── navheim-conformance/
├── tests/
│   ├── conformance/
│   ├── interoperability/
│   ├── replay/
│   ├── fault-injection/
│   └── platform/
├── fuzz/
├── benches/
├── examples/
└── docs/
```

---

## 8. `no_std`, allocation and dependency rules

### 8.1 Capability tiers

Every published crate must declare one of these tiers:

- **Tier 0 — `core` only:** no heap, no OS, no floating-point assumption unless feature-gated.
- **Tier 1 — `alloc`:** dynamic satellite/state sets and owned messages, still no OS.
- **Tier 2 — `std`:** files, sockets, threads, serial, USB and clocks.
- **Tier 3 — external integration:** Rustls, vendor drivers, mobile APIs and other optional dependencies.

Default foundational/constellation builds should be Tier 0 or Tier 1. A `std` feature may add convenience without changing wire behavior.

### 8.2 Zero hidden allocation

- Parsers accept caller-owned buffers or emit borrowed views.
- DSP plans report exact scratch requirements before construction.
- Solvers expose fixed-capacity and allocated variants.
- Events borrow internal epoch storage where possible.
- No `Vec` is created in a hot loop without an explicit allocated profile.
- Every algorithm documents exact heap/scratch/state needs where structurally
  knowable; stack evidence is target/toolchain/profile-specific or explicitly
  unavailable, never presented as a portable exact fact.

### 8.3 Zero hidden execution

- The core never creates threads.
- The core never chooses an async runtime.
- The core exposes synchronous `push`, `poll`, iterator and callback APIs.
- Optional Tokio/async-std/smol adapters, if ever created, live outside the canonical crates.
- Cancellation and deadlines are explicit inputs.

### 8.4 Dependency policy

A checked machine-readable dependency DAG is authoritative for every workspace
crate and capability. It records normal, optional, build and development
edges; feature-unified behavior; tier; `alloc`/`std`; unsafe; TLS; cryptography;
publication; and platform scope. CI rejects cycles, undeclared edges and any
feature combination that silently promotes a lower tier or canonical GNSS
crate into OS, unsafe, TLS or cryptographic authority.

Navheim should self-implement everything that defines GNSS correctness:

- bit and symbol codecs;
- CRC/parity/FEC specified by GNSS protocols;
- spreading codes and modulation helpers;
- FFT/resampling/filtering/tracking loops;
- navigation-message parsers;
- ephemeris and correction models;
- PVT, RTK, PPP and integrity algorithms;
- RINEX/NMEA/RTCM/NTRIP/SUPL/LPP protocol behavior.

Do **not** self-implement:

- TLS;
- modern cryptographic primitives such as elliptic-curve signature verification or cryptographic hashes;
- operating-system kernels and device stacks;
- vendor FPGA bitstreams whose legal/technical contract requires a vendor stack.

For OSNMA/QZNMA, Navheim implements protocol state, key-chain logic, message binding, freshness, policy and evidence. An audited backend implements the cryptographic primitive. This avoids the dangerous contradiction of calling a project “security first” while inventing its own elliptic-curve code.

### 8.5 Unsafe policy

- `#![forbid(unsafe_code)]` in all protocol, constellation, solver and format crates.
- Unsafe is allowed only in platform FFI, SIMD intrinsics or hardware DMA modules.
- Each unsafe module has a written safety contract, Miri tests where applicable and an independent review owner.
- FFI copies untrusted device data into bounded Rust-owned buffers before parsing.

---

## 9. Canonical data model

The data model is the most important compatibility surface in Navheim.

### 9.1 Extensible identifiers

Avoid closed enums and unscoped integer spaces that require semver breaks or
allow standards, vendors and experiments to collide:

```rust
pub struct RegistryId {
    authority: RegistryAuthority,
    code: u32,
}

pub struct SatelliteId {
    system: RegistryId,
    vehicle: u16,
}
```

Provide named standard constants and versioned registry snapshots, but
preserve unknown authority/code pairs. Public system/signal selections use
bounded sets rather than fixed-width masks.

### 9.1.1 Canonical signal definitions

`navheim-core` owns `SignalDefinition`, registry traits and extensible IDs.
Constellation crates contribute versioned physical fragments keyed by those
IDs: nominal or channel-dependent carrier frequency, including GLONASS FDMA
formulas and channel context; derived wavelength; chip/code/symbol rates;
data/pilot/component identity; modulation and secondary-code properties;
native time scale; constellation; observation applicability; revision; and
provenance. RINEX and RTCM crates separately own version-specific wire-ID
mappings into canonical `SignalId`; constellation crates never depend on those
format standards. The facade composes only selected fragments without forcing
format crates to depend on every constellation. Unknown or partial definitions
and mappings remain representable without duplicate physical tables.

### 9.2 Units

Do not expose naked `f64` for semantically different quantities. `navheim-core` should provide transparent types:

- `Seconds`, `Nanoseconds`, `Hertz`, `Radians`, `Meters`, `MetersPerSecond`;
- `CarrierCycles`, `Chips`, `Decibels`, `DbHz`;
- `UtcOffset`, `ClockBias`, `ClockDrift`;
- interval/uncertainty types with asymmetric bounds;
- covariance layouts that name state ordering, squared/cross units, frame and
  reference epoch.

Tier 0 protocol/interchange values use exact scaled integers or reduced
rationals. Construction is explicit and checked. Floating adapters reject
non-finite values; optimized kernels may use raw arrays only behind private
APIs with documented rounding, overflow and numerical backend behavior.

### 9.2.1 `no_std` elementary math

`navheim-math` provides the normative first-party pure-Rust scalar
implementations required by the roadmap: square root/hypot, reciprocal square
root where justified, sine/cosine, `atan2`, logarithm/exponential and the
small derived functions actually used by admitted algorithms. Each function
defines domain, exceptional inputs, signed zero, subnormal policy, argument
reduction, rounding and maximum absolute/relative/ULP error against
high-precision independent references.

Tier 0 always has deterministic scalar math without `std`, an allocator,
nightly features, OS `libm`, or a third-party dependency. Algorithms accept a
narrow reviewed math-backend capability where acceleration is useful; callers
cannot substitute an unbounded or semantically weaker backend silently.
Platform-native implementations must identify their behavior and pass the
same domain/error corpus before selection.

Fixed-size FFT twiddles and coefficients may be audited constants. Runtime
FFT twiddles, geodesic series and loop/filter coefficients are created during
side-effect-free planning into caller-provided storage, recorded in the plan
receipt and reused during execution. No real-time stage computes unplanned
tables or performs hidden allocation.

As of the Rust 1.97.1 baseline, `core::simd`/`std::simd` remains nightly-only.
Published Navheim crates use stable Rust only: scalar/auto-vectorized code and
reviewed target-specific `core::arch` adapters with explicit feature detection
and scalar fallback. A future portable-SIMD API is admitted only when stable
on the MSRV or behind a separately raised MSRV, never by enabling nightly.

### 9.2.2 Bounded linear algebra

`navheim-linalg` owns fixed-capacity vectors, matrices and symmetric storage,
plus caller-scratch runtime dimensions. It depends inward only on
`navheim-math` for qualified square-root/hypot and other admitted scalar
operations; it neither privately reimplements them nor calls platform math.
Its admitted kernels include
Householder/Givens QR, Cholesky and LDLT with definiteness checks, triangular
solves, symmetric rank updates/downdates, square-root covariance/information
updates, and rank/condition estimation. Dimensions and scratch arithmetic are
checked; aliasing/non-overlap, state order, pivoting, rounding and work are
explicit. Singular, indefinite, non-finite and badly scaled inputs have typed
failure rather than plausible output.

Production least squares uses a qualified stable factorization; it does not
silently invert normal equations. Generic raw matrix APIs remain private or
narrow until concrete solvers establish their required public abstraction.
Every admitted kernel is compared with independent high-precision references,
including adversarial scaling and update/downdate cases.

### 9.2.3 Conservative statistical kernels

`navheim-math` admits only the probability functions required by implemented
GNSS algorithms: normal tail/CDF and inverse tail, chi-square CDF/tail/
quantile, and their validated degrees-of-freedom/confidence domains. Very
small risks use explicit log-probability paths. Each approximation publishes
monotonicity, error bounds, validated range and unavailable behavior.

Threshold APIs encode rounding direction. Integrity/protection calculations
must remain conservative after approximation and rounding: error may not
underestimate a protection level or make an acceptance test more permissive.
Independent arbitrary-precision tables cover ordinary, tail, boundary and
out-of-domain cases.

### 9.2.4 Coordinate algorithm ownership

`navheim-core` owns only coordinate, frame, datum, epoch and covariance
representations plus dependency-free validation. `navheim-geo` depends on
`navheim-core` and `navheim-math` and owns every mathematical coordinate
transformation, projection, ellipsoidal geodesic, great-circle/rhumb primitive
and frame transformation, including UTM/UPS, Transverse Mercator and
ENU/NED/body-frame transformations.
`navheim-navigation` depends on `navheim-geo` and owns only waypoints, routes,
tracks, geofences, segment policies and navigation-facing composition. This
prevents core or navigation from privately duplicating trigonometry, square
root or geodesic series while keeping all physical coordinate APIs canonical.

### 9.3 Time model

```rust
pub struct RawGnssTime {
    scale: GnssTimeScale,
    fields: RawTimeFields,
}

pub struct ResolvedGnssTime {
    scale: GnssTimeScale,
    instant: NativeScaleInstant,
    resolution: TimeResolutionEvidence,
}

pub struct TaiInstant {
    seconds_from_epoch: i64,
    fractional: FractionalSecond,
}

pub struct CaptureStamp<C> {
    domain: CaptureClockDomainId,
    generation: CaptureGeneration,
    value: C,
}
```

Requirements:

- raw, ambiguous, resolved native, atomic and UTC values are distinct types;
- fields are private and constructed through checked APIs;
- no implicit conversion through Unix time;
- explicit leap/UTC model identity, activation, expiry and provenance;
- exact integer representation before optional floating conversion;
- week/day/era alternatives and resolution context remain explicit;
- receive time and transmit time kept separately;
- capture clock domain and reset generation attached to every epoch;
- different capture domains/generations are incomparable without an explicit
  caller-provided mapping;
- hardware timestamp/PPS relationship modeled explicitly.

`TaiInstant`, `FractionalSecond` and duration types freeze an exact epoch,
canonical fractional representation, supported range and granularity. Checked
construction, addition, subtraction, difference and scale conversion report
overflow; they never wrap, saturate or silently lose subsecond precision.
Sequence and generation counters likewise define exhaustion and renewal rather
than relying on accidental integer wrap.

#### 9.3.1 UTC civil and calendar representations

UTC civil labels preserve Gregorian date, hour/minute and second `60` for a
positive leap; the model also represents a hypothetical negative-leap deleted
label without pretending it is an ordinary second. Labels are ordered and
subtracted only after checked resolution through the identified UTC model to
TAI. UTC models carry revision, announcement, activation, replacement,
invalidation, expiry and provenance.

POSIX conversion is an explicit potentially ambiguous/lossy adapter returning
mapping evidence; Navheim does not identify POSIX seconds with UTC labels and
does not implement an implicit leap smear. Gregorian calendar, ordinal day,
Julian Date and Modified Julian Date conversions define epoch, day boundary,
scale context, precision and rounding for RINEX and precise products. Julian
Date/MJD uses an integer day plus exact bounded fraction or reduced rational,
never an implicit `f64`. The profile freezes the supported
proleptic-Gregorian range and its BCE/year-zero convention.

#### 9.3.2 Precision-geodesy time arguments

TT and UT1 are not `GnssTimeScale` variants. TT is derived explicitly from
atomic time under a named definition. UT1 is an EOP-derived argument carrying
the EOP series/product, revision, interpolation method, validity, uncertainty
and provenance. Earth rotation, tides and precise positioning accept these
typed arguments and return unavailable outside their evidence interval rather
than treating them as receiver/GNSS clock scales.

### 9.4 Observation model

The canonical pipeline never overwrites an earlier stage:

```text
IngressEnvelope
  -> TrackingEstimate | RawProtocolRecord
  -> RawSdrObservation | RawReceiverObservation | RawNavigationMessage
  -> Observation | ValidatedNavigationMessage
  -> CorrectedObservation + transactional NavigationState
  -> ObservationEpoch
  -> SolverInputEpoch
  -> Solution
```

Every value is wrapped in an immutable `Artifact<T>` with an `ArtifactId`,
bounded parent IDs and derivation algorithm/version. Correctness,
navigation-message authentication, signal-authenticity evidence, integrity
and policy decisions are separate immutable objects targeting artifact IDs.
Delayed OSNMA/QZNMA results add assessments; they never mutate earlier facts.

Artifact and provenance IDs contain a source namespace, reset generation and
non-wrapping local sequence with explicit exhaustion and renewal. IDs are
never reused after reset. Replay/import remaps untrusted namespaces while
preserving parent relationships; artifact identity remains distinct from an
optional content digest. Canonical serialization defines duplicate/collision
behavior, and routine formatting is privacy-safe rather than globally
correlatable. External IDs never become globally authoritative by assertion.

Important absence uses a reason-bearing `Availability<T, R>` rather than a
bare `Option`. Stage-specific types prevent corrected/raw measurements,
unresolved clocks, unavailable fixes and pending assessments from forming
ambiguous combinations.

#### 9.4.1 Opt-in algorithm-state snapshots

Live state is not serializable by default. An explicitly admitted state type
may implement a minimal, versioned and bounded snapshot profile inside a
canonical envelope carrying type/schema, algorithm, source/generation,
creation epoch, validity/expiry, parent artifacts, model/calibration/product
identities, required capabilities, byte/work bounds and corruption digest.
Authenticity and confidentiality are independent properties:
`SnapshotAuthenticity::{Untrusted, IntegrityChecked, Authenticated}` and
`SnapshotConfidentiality::{Plaintext, ExternallyEncrypted}`. Freshness is a
third independent property:
`SnapshotFreshness::{Unchecked, CounterChecked, RollbackResistant}`. An
unkeyed digest detects corruption only. `Authenticated` requires verification
through an injected external MAC/signature authority but does not establish
freshness. `ExternallyEncrypted` requires an injected external AEAD or
platform-keystore authority and never follows merely from authentication.
`RollbackResistant` requires comparison with and advancement of trusted
external monotonic state; an authenticated embedded counter alone establishes
no freshness. `CounterChecked` means only that an authenticated,
structurally valid counter was compared with named local authority state that
is not qualified as rollback-resistant. It is diagnostic replay evidence,
never satisfies a policy requiring guaranteed freshness or rollback
resistance, and carries the authority identity, counter namespace and checked
relationship explicitly.
Restore treats bytes as untrusted input, remaps provenance, checks
compatibility and external anti-rollback authority, validates all numerical/
state invariants, and commits atomically or not at all. Untrusted or merely
integrity-checked state can only initialize or aid and must reacquire/
reconverge as the profile requires.

Every admitted profile classifies fields by sensitivity, contains only the
minimum state required for its stated restore outcome and declares storage/
export consent plus retention policy. Snapshot contents never enter ordinary
`Debug`, `Display`, errors or routine telemetry. Owned plaintext temporaries
use the reviewed zeroization boundary where possible, while documentation
states the limits imposed by copies, allocator/OS behavior and caller-owned
buffers. Confidential storage remains a caller/platform policy rather than a
hidden core-cryptography implementation.

An externally protected snapshot carries opaque extensible scheme/suite,
authority, key/version and nonce-allocation identifiers; authenticated-data
schema; rollback generation/counter; bounded ciphertext/tag lengths; and
creation, expiry and rotation context. Associated data authenticates every
outer field that affects interpretation, including envelope/schema/algorithm,
state type, source generation, validity, capabilities and lengths. Unknown,
downgraded or incompatible suites fail closed.

The rollback protocol uses a distinct opaque `SnapshotTransactionBinding`,
never the envelope's unkeyed corruption digest or an artifact's optional
content digest. An admitted external protection authority creates it with a
suite-approved collision-resistant hash or MAC over the one exact canonical
protected envelope, including ciphertext, tag and authenticated metadata.
Domain separation binds the Navheim snapshot-transaction purpose, authority
identity, counter namespace, suite/version, counter value and operation.
Alternative/noncanonical encodings are rejected, and the type provides no
conversion from generic digest types. The binding is stored in the authority
transaction record or a separate sidecar and is explicitly excluded from its
own hash/MAC input, avoiding self-reference. It is computed only after the
protected envelope is complete and immutable.

Nonce allocation and rollback-counter persistence are crash-safe. The
normative cross-authority transaction is:

1. reserve authority identity/namespace, next non-wrapping counter, nonce,
   transaction ID and authority-monotonic expiry/boot generation in a durable
   `Pending` record;
2. seal the complete canonical protected envelope and compute its
   `SnapshotTransactionBinding`;
3. durably stage the candidate snapshot under that transaction ID;
4. atomically compare-and-advance the authority record from `Pending` to
   `AuthorityCommitted`, binding the counter and candidate;
5. durably promote exactly that staged candidate as active;
6. finalize the authority record as `Committed` and only then return
   `RollbackResistant` evidence.

The pending/authority-committed record defines recovery at every crash point.
If authority advancement succeeds but promotion fails, the outcome is a
recoverable pending transaction or fail-closed availability loss—never
success or permission to restore an older snapshot. Namespace locking/CAS
ensures recovery and a new writer cannot both commit. Cancellation is allowed
only before authority commit; afterward recovery, reboot, key rotation and
counter migration must carry or resolve the transaction before admitting
another writer. Reservation expiry uses authority-owned monotonic state and
boot generation, never UTC, wall time or caller time. Reboot either resumes
from durable authority recovery evidence or leaves freshness unavailable; it
cannot orphan an apparently current snapshot. Counter exhaustion, reservation
expiry, concurrent writers, cloned/restored authority state and every crash
boundary fail closed.

Recovery uses one explicit state matrix; adapters may not infer a weaker
platform-specific shortcut:

| Durable recovery state | Restore behavior | New writer | Required action |
| --- | --- | --- | --- |
| `Committed` | Restore only the exactly bound active snapshot | Allowed after ordinary validation | Normal validation and restore |
| `Pending` | The previously committed snapshot may restore only under the same namespace lock and pre-authority-commit linearization; the staged candidate cannot | Blocked | Resume or cancel the reservation and deterministically clean its candidate |
| `AuthorityCommitted` | No older snapshot may restore; the committed candidate is not usable as rollback-resistant until recovery completes | Blocked | Verify the binding, promote and finalize, or report unavailable |
| `PromotedUnfinalized` | Restore only after synchronous recovery verifies the promoted binding and finalizes `Committed` | Blocked | Verify and finalize, or report unavailable |
| `CorruptOrUnknown` | No rollback-resistant restore | Blocked | Fail closed; only the separate Tier 3 repair capability may act |

Each `PlanReceipt` and authority profile bound active namespaces, one live
writer transaction per namespace, pending records, staged candidates, retained
prior/superseded candidates, retained bytes, retry attempts and deterministic
recovery work. Pre-authority cancellation may delete its staged candidate only
after proving it is not authority-committed. Superseded committed candidates
are deleted only after the replacement is finalized and its retention policy
permits it. Ordinary cleanup never deletes an authority-committed,
promoted-unfinalized, corrupt or unknown candidate. Cleanup interruption is
itself recovered through the same bounded state machine.

Snapshot repair is not an ordinary restore or writer operation. It is a
separately enabled Tier 3 platform capability with explicit operator authority
and audit evidence. It may either recover and verify the exact current
authority-bound candidate, completing the normal state machine, or durably
retire the damaged namespace/key/counter and create a fresh namespace with a
typed continuity break. It can never reset a counter inside the same
namespace, accept an older candidate, reuse a reserved nonce, erase unresolved
authority evidence or downgrade freshness to `CounterChecked`. Namespace
retirement and replacement require new identity/key/nonce domains and durable
anti-revival evidence; if the platform cannot prove that boundary, repair
remains unavailable. Every repair emits a security/invalidation artifact,
invalidates restored assessments and forces affected algorithms to reacquire
or reconverge before producing authoritative outputs.

Key rotation has an explicit migration operation that never silently weakens
the suite, namespace or generation. Outer lengths and resource limits are
validated before decryption into bounded caller-provided plaintext/ciphertext
buffers. Authentication failure is uniform and exposes no parsing/decryption
oracle. The common bridge defines these semantics; Linux/BSD, Windows, Apple
and Android authorities are admitted and tested in separate platform
milestones.
Each authority returns separate evidence for cryptographic verification,
durable commit completion, trusted monotonic comparison/update, crash recovery
and key/counter migration. A crash-consistent atomic file replacement plus
AEAD is not rollback-resistant against restoration of an older file. Profiles
report `Unchecked` or `CounterChecked` whenever qualified external monotonic
state is unavailable rather than silently upgrading freshness.

Restored authentication, signal-authenticity, correctness, integrity and
policy assessments never regain authority merely from a valid snapshot,
digest or seal. They are invalidated or reverified against current evidence,
trust roots, models and generations.

The 1.0 admitted profiles are separately versioned for acquisition/
reacquisition memory after scheduler integration, tracking channels/raw page
assembly, semantic navigation stores after model implementation, selected PPP
state and selected fusion state. Other algorithms explicitly report restore
as unsupported; a raw memory image is never a snapshot.

### 9.5 Ephemeris and corrections

Use constellation-specific raw structures plus a validated canonical orbit interface. Never discard source fields merely because the common solver does not need them.

```rust
pub trait OrbitModel {
    fn validity(&self) -> TimeInterval;
    fn state_at(&self, t: ResolvedGnssTime) -> Result<SatelliteState, OrbitError>;
    fn health(&self) -> HealthState;
    fn provenance(&self) -> ProvenanceId;
}
```

Corrections contain:

- target satellite/signal;
- issue of data/version;
- epoch and validity interval;
- update interval;
- reference frame and datum;
- provider/solution ID;
- uncertainty and integrity;
- authentication/provenance;
- whether the correction has already been applied.

Every correction also belongs to an immutable `CorrectionSessionId` binding
transport peer, provider/mountpoint, station/solution, frame/datum, antenna,
authenticated peer and session generation. Incomplete, stale or cross-session
groups cannot partially update navigation or solver state.

A canonical correction ledger classifies broadcast TGD/BGD, differential and
inter-frequency biases, Bias-SINEX products, antenna PCO/PCV, carrier phase
wind-up, ionosphere and troposphere terms by physical target and application
stage. Every applied term records its convention and source artifact. Mutually
exclusive alternatives and already-applied terms are rejected so format
translation cannot apply the same physical correction twice.

### 9.6 Solution model

A solution artifact contains more than coordinates, but assessments remain
separate:

```rust
pub enum SolutionEvent {
    Available(Artifact<Solution>),
    Unavailable(SolutionUnavailable),
    Invalidated(TargetedInvalidation),
}
```

Time-only, 2D, standalone 3D, SBAS, DGPS and other completed solutions have
explicit solution kinds. RTK/PPP convergence, fixed/float transitions,
rollback and coasting are lifecycle artifacts. "No fix" is never represented
as a valid fix.

Public typed outputs include solution age, contributing and excluded satellite
summaries, GDOP/PDOP/HDOP/VDOP/TDOP, residual and exclusion diagnostics, fix
kind and convergence state. Ellipsoidal height and orthometric height are
different types; an orthometric result always identifies its geoid or vertical
datum model, epoch, interpolation method, validity and uncertainty.

---

## 10. Public API design

### 10.1 The simple application API

```rust
use navheim::{Profile, ReceiverEvent, ReceiverPlan, Systems};

fn main() -> Result<(), navheim::Error> {
    let prepared = ReceiverPlan::navigation()
        .source(source_config)
        .profile(Profile::Navigation)
        .systems(Systems::ALL_PUBLIC)
        .prepare(&limits)?;

    inspect(prepared.capabilities());
    inspect(prepared.resources());

    let mut receiver = prepared.open_and_build(&mut buffers, policy)?;

    while let Some(event) = receiver.next_event()? {
        match event {
            ReceiverEvent::Solution(solution) => consume(solution),
            ReceiverEvent::Assessment(assessment) => consume(assessment),
            ReceiverEvent::Security(alert) => eprintln!("{alert:?}"),
            _ => {}
        }
    }

    Ok(())
}
```

This friendly builder is Tier 2. Planning is side-effect free; devices,
credentials, networking and threads are touched only after the complete
immutable plan is accepted. Tier 0 remains caller-buffered and does not expose
automatic discovery.

### 10.2 Explicit hardware-receiver API

```rust
let prepared = navheim::ReceiverPlan::survey()
    .source(navheim_receiver::SerialConfig::ubx("/dev/ttyACM0", 921_600))
    .profile(Profile::Survey)
    .raw_observations(true)
    .prepare(&limits)?;

let mut receiver = prepared.open_and_build(&mut buffers, policy)?;
```

The same source works on Windows COM ports and BSD/macOS device paths through `navheim-io`.

### 10.3 SDR API with capability planning

```rust
use navheim_sdr::{DspPlan, SignalSelection, SoftwareReceiver};

let requested = SignalSelection::all_public();
let plan = DspPlan::builder()
    .signals(requested)
    .simultaneous(true)
    .coherent(true)
    .validate(front_end_capabilities, &limits)?;

println!("front ends: {}", plan.front_end_count());
println!("sample memory: {}", plan.required_sample_bytes());
println!("scratch memory: {}", plan.required_scratch_bytes());

let mut receiver = SoftwareReceiver::builder()
    .plan_receipt(plan)
    .buffers(&mut buffers)
    .build()?;
```

A plan classifies every resource statement as an exact structural amount, a
target/toolchain/profile-specific static upper bound, a deterministic work
bound, a measured envelope, a caller assumption, or an unavailable estimate.
Portable plans never mislabel measured throughput/latency or target-specific
stack evidence as exact facts. All computable bounds use checked arithmetic,
and the immutable receipt accepts only
matching sample blocks; untrusted hardware metadata is revalidated for every
block. RF input cannot choose allocations, FFT plans, thread/channel counts,
FEC iterations, candidate counts or queue growth. A plan either succeeds
completely or returns a structured explanation:

```rust
pub enum CapabilityFailure {
    FrequencyOutOfRange { signal: SignalId, required: FrequencyRange },
    InsufficientBandwidth { group: BandGroup, required_hz: u64, available_hz: u64 },
    InsufficientChannels { required: u8, available: u8 },
    NoCoherentClock,
    NoHardwareTimestamp,
    SampleFormatUnsupported,
    ThroughputExceeded,
    AntennaCoverageUnknown,
}
```

There is no implicit “degraded” mode for a plan marked `complete`. A user may deliberately request a reduced development plan.

### 10.4 Bare-metal parser API

```rust
let mut parser = navheim_nmea::Parser::<256>::new();
let mut input = uart_bytes;

while !input.is_empty() {
    let progress = parser.push(input)?;
    input = &input[progress.consumed()..];
    if let Some(sentence) = progress.borrowed_event() {
        consume(sentence);
    }
}
```

Every call consumes input or explicitly requests more. No allocation, I/O
trait, global clock or async runtime is required.

### 10.5 Epoch solver API

```rust
let mut solver = navheim_pvt::Solver::<64>::builder()
    .algorithm(navheim_pvt::Algorithm::RobustWeightedLeastSquares)
    .admission(navheim_pvt::AdmissionPolicy::navigation())
    .build()?;

let solution = solver.solve(&epoch, &navigation_store, approximate_state)?;

let integrity = navheim_integrity::Assessor::<64>::builder()
    .policy(navheim_integrity::Policy::navigation())
    .build()?;
let assessment = integrity.assess(&epoch, &solution)?;
```

Measurement admission may exclude structurally invalid or policy-disallowed
inputs, but it does not label the resulting solution integrity-approved.
Integrity consumes the immutable solution plus residual/exclusion artifacts
and emits a separate targeted `IntegrityAssessment`.

### 10.6 RTK rover API

```rust
let mut rover = navheim_rtk::Rover::<96>::builder()
    .reference_station(base_position)
    .ambiguity_policy(navheim_rtk::AmbiguityPolicy::validated())
    .max_correction_age(core::time::Duration::from_secs(3))
    .build()?;

rover.push_rover_epoch(rover_epoch)?;
rover.push_base_epoch(base_epoch)?;

if let Some(fix) = rover.poll_fix()? {
    use_fix(fix);
}
```

### 10.7 Security API

```rust
let policy = navheim_security::Policy::builder()
    .require_authenticated_navigation_for(SystemId::GALILEO)
    .cross_check_constellations(3)
    .maximum_time_step(Nanoseconds::new(100_000))
    .on_authentication_loss(navheim_security::Reaction::Quarantine)
    .on_spoof_suspicion(navheim_security::Reaction::FailClosed)
    .build()?;

let receiver = Receiver::builder()
    .security(policy)
    .build()?;
```

The API distinguishes:

- authenticated navigation data;
- unauthenticated but internally consistent measurements;
- authentication pending because delayed keys have not arrived;
- authentication unavailable on the signal;
- authentication failed;
- signal-source authenticity, which OSNMA/QZNMA alone do not fully prove;
- solution integrity, which is not the same as cryptographic authentication.

### 10.8 Timing API

```rust
let mut source = navheim_timing::ReceiverTimeSource::builder(receiver)
    .require_valid_utc_model(true)
    .maximum_uncertainty(Nanoseconds::new(500_000))
    .build()?;
let mut slot = GnssTimeEventSlot::new(&mut event_storage);

while source.poll_time(&mut slot)?.is_ready() {
    let sequence = {
        let event = slot.borrow()?;
        match event.value() {
            GnssTimeEvent::Artifact(observation) => consume(observation),
            GnssTimeEvent::Assessment(assessment) => consume(assessment),
            GnssTimeEvent::Invalidated(target) => withdraw_source(target),
            GnssTimeEvent::Security(alert) => handle_alert(alert),
            _ => {}
        }
        event.sequence()
    };
    source.acknowledge(&mut slot, sequence)?;
}
```

Navheim produces GNSS timing evidence; it does not steer a system clock.
Consumer-owned adapters map this event stream into generic time frameworks.
Navheim has no dependency on those frameworks.

---

## 11. SDR architecture

### 11.1 Front-end traits

```rust
pub trait SampleSource {
    type Sample;
    type Error;

    fn capabilities(&self) -> FrontEndCapabilities;
    fn prepare(
        &self,
        request: &FrontEndRequest,
        limits: &ResourceLimits,
    ) -> Result<FrontEndPlan, FrontEndPlanError>;
    fn apply(
        &mut self,
        plan: &FrontEndPlan,
    ) -> FrontEndApplyOutcome<Self::Error>;
    fn read(
        &mut self,
        out: &mut [Self::Sample],
    ) -> Result<SampleRead, Self::Error>;
}

pub enum FrontEndApplyOutcome<E> {
    Applied {
        configuration: FrontEndConfiguration,
        evidence: AppliedTransitionEvidence,
    },
    RejectedNoMutation {
        cause: E,
        proof: NoMutationEvidence,
    },
    PartiallyApplied {
        cause: E,
        evidence: TransitionEvidence,
    },
    StateUnknown {
        cause: E,
        evidence: TransitionEvidence,
    },
}
```

`prepare` is side-effect free and binds the normalized request, capabilities,
resource limits, exact device/firmware identity and expected transition.
`apply` accepts only that immutable plan and creates a non-reused
`FrontEndConfigurationGeneration` covering clock source, antenna/port,
coherent group, center frequency, bandwidth, sample rate, encoding, I/Q order,
scaling, gain/AGC, bias tee/antenna power, calibration and effective interval.
Hardware acknowledgement and read-back are device assertions. A distinct
front-end assessment records observed sample timing/rate and calibration
consistency for a stated interval, evidence coverage, uncertainty and
unverifiable fields.

`RejectedNoMutation` is legal only when the adapter positively proves that no
externally visible command or mutation occurred, such as local validation
failure before submission; it is the only failure that preserves the previous
generation. The checked apply framework privately issues a linear
`PreSubmissionToken` bound to plan, device identity and prior generation.
Acquiring the exclusive Navheim command-transport capability consumes that
token; after acquisition or any submission, constructing
`RejectedNoMutation` is structurally impossible. Third-party adapters cannot
mint or implement proof tokens and receive transport only through this
framework state machine.

`NoMutationEvidence` proves narrowly that no command crossed that exclusive
Navheim transport boundary. Preserving the prior generation additionally
requires a still-valid exclusive device-control lease and a frozen profile
that excludes autonomous relevant reconfiguration. Another controller,
control-lease loss, reset, hotplug/identity change or possible autonomous
reconfiguration yields `StateUnknown` even when Navheim issued no command.
The proof never claims arbitrary physical hardware remained unchanged.
`AppliedTransitionEvidence` binds the new configuration and every required
per-device/channel command, acknowledgement and read-back. It proves only the
completed adapter/device transaction; it never implies independently observed
sample timing, rate, calibration or coherence.

A timeout, disconnect, lost acknowledgement, transport failure after
submission or uncertain rollback is `StateUnknown`. `PartiallyApplied` and
`StateUnknown` preserve the original failure cause and bounded
`TransitionEvidence`, retire the old generation without activating the
intended one, invalidate all queued samples, mappings, calibration and affected
DSP/tracking state, prohibit reads, and require reprobe plus a new plan.
Evidence preserves per-device/channel commands, results, acknowledgements,
read-back, timing, rollback and reprobe results, and the last independently
observed state. Required proof/evidence-capacity exhaustion records overflow
and escalates to `StateUnknown`; it never discards facts and reports
`Applied`, `RejectedNoMutation` or another more favorable outcome. Best-effort
rollback is evidence, never an assumed success.

Multi-device or coherent-array configuration is one prepared group transaction
with bounded per-device outcomes. Coherence remains unavailable unless every
front end reaches the intended generation and shared clock/timestamp
calibration is independently revalidated. Disconnect, power loss, partial
multi-channel application or failed rollback cannot silently retain or claim
coherence.

Retune, gain, clock, port, power or format transitions drain or invalidate old
sample blocks, terminate old capture mappings, reset affected DSP/tracking
state and emit explicit gap/discontinuity events before new-generation output.
This same contract governs sequential band operation and planned
`Profile::LowPower` switching. `SampleRead` always reports the initialized
valid sample count, block and configuration generation, timestamp/capture
mapping, gaps, overruns and explicit data/end-of-stream/would-block state;
uninitialized capacity is never presented as samples.

Capabilities include:

- tuning range and gaps;
- instantaneous bandwidth;
- supported sample rates and formats;
- independent/coherent RF channels;
- gain stages and AGC behavior;
- bias-tee and antenna-power capabilities;
- hardware time stamps;
- external 10 MHz/PPS support;
- oscillator accuracy and calibration;
- transport throughput and alignment;
- half/full duplex and clock-sharing topology.

### 11.2 Band groups for full civil/open coverage

A practical full receiver should plan at least these front-end groups:

- **Upper L band:** approximately 1559–1610 MHz — GPS/QZSS L1, Galileo E1, BeiDou B1, NavIC L1, SBAS L1 and GLONASS G1.
- **Lower L band:** approximately 1164–1215 MHz — GPS/QZSS L5, Galileo E5a/E5b/AltBOC, BeiDou B2, NavIC L5 and GLONASS G3.
- **Middle L band:** approximately 1215–1300 MHz — GPS/QZSS L2, GLONASS G2, BeiDou B3 and Galileo/QZSS E6/L6. Depending on filtering and hardware bandwidth, split this into two coherent channels.
- **NavIC S band:** around 2492.028 MHz — separate antenna, LNA/filter and front end unless a genuinely wideband antenna system covers it.

A four-channel coherent SDR is the cleanest full implementation platform. A two-channel SDR can implement and validate all signals sequentially, or simultaneously in two band groups, but cannot observe all groups at the same instant without switching or a second synchronized unit.

### 11.3 DSP stages

```text
RF source
  -> sample validation and timestamping
  -> DC/IQ imbalance correction
  -> optional interference blanking
  -> channelization and resampling
  -> acquisition search
  -> channel allocation
  -> code/carrier tracking
  -> bit/symbol synchronization
  -> demodulation and FEC
  -> frame/page reconstruction
  -> navigation/authentication decode
  -> observable generation
  -> quality/integrity metrics
```

Each stage is replaceable by a trait but has a Navheim-native implementation.

### 11.4 Native DSP implementation

`navheim-dsp` should implement:

- integer and floating complex types;
- saturating fixed-point arithmetic helpers;
- NCO and phase accumulators;
- FIR/IIR filters;
- polyphase resamplers;
- CIC filters for hardware-friendly decimation;
- radix-2, radix-4 and mixed-radix FFTs;
- overlap-save convolution;
- polyphase filter-bank channelizers;
- coherent/noncoherent integration;
- serial and FFT acquisition;
- peak detection and false-alarm thresholds;
- DLL, PLL, FLL and combined loops;
- early/prompt/late and multi-correlator discriminators;
- pilot/data combining;
- secondary-code synchronization;
- bit-edge and symbol synchronization;
- adaptive bandwidth and vector tracking hooks;
- CN0, multipath and lock estimators.

Optimization layers:

1. portable scalar reference implementation;
2. fixed-point deterministic implementation;
3. architecture-specific SIMD selected at compile or runtime;
4. optional FPGA/GPU offload using the same validated kernels and vectors.

The scalar implementation is normative. Optimized implementations must be bit-exact where integer arithmetic is specified or remain within documented numerical tolerances.

`navheim-dsp` depends inward on `navheim-math` for runtime twiddles, loop
coefficients, acquisition statistics and estimator functions. It may use
audited fixed constants where the plan admits them, but it cannot privately
reimplement scalar math or call platform math.

Front-end conditioning preserves sample encoding, signedness, endianness, I/Q
ordering, scaling, gain/AGC and calibration provenance. It reports clipping,
quantization, DC offset and I/Q gain/phase imbalance evidence. Optional bounded
pulse blanking or notching emits distortion evidence and can never silently
upgrade a mitigated block into a trustworthy observation. SIMD begins only
after alignment, aliasing, feature-detection, fallback and unsafe contracts are
specified and tested against the scalar path.

### 11.5 Acquisition scheduler

Before acquisition, a dependency-free `SearchAid`/`AcquisitionHint` artifact
may carry approximate time, location, velocity, orbit/almanac and Doppler
windows; source/generation; validity; uncertainty; trust class; tracked-signal
aiding; and reacquisition-memory identity/expiry. Every resulting search-space
reduction stays inside the immutable `PlanReceipt` maximum blind-search,
channel, scratch and work bounds. A separate immutable
`SearchExecutionReceipt` records the dynamic hint IDs, accepted/rejected
windows, actual per-search work budget, fallback reason and deterministic
decision order. Poisoned, stale or conflicting hints fall back to a bounded
blind search. Hints may reduce work but cannot resolve canonical time/position
or establish trust. Later SUPL, LPP, Android and receiver assistance adapters
translate into this early artifact.

The scheduler should combine:

- blind full search;
- warm/hot acquisition using time/location/almanac;
- Doppler prediction from ephemeris and approximate motion;
- priority based on service profile and geometry;
- reacquisition memory;
- CPU and power budgets;
- cross-signal aiding;
- constellation-specific search spaces;
- GLONASS frequency-channel search.

It must expose why a signal was not searched or why a channel was evicted.

#### 11.5.1 Deterministic Tier 2 multicore execution

Tier 0 and `navheim-dsp` remain thread-free and expose scalar polling/work
units. The separate optional `navheim-executor` accepts caller-selected worker
count, affinity/priority assumptions and bounded queues. A validated
`WorkPartition` produces ordered `ParallelWorkUnit`s with deterministic
identity; immutable input and exclusively owned output/scratch; checked
non-overlapping regions; scoped lifetimes for caller-owned buffers; explicit
`Send` bounds; and no hidden shared mutable state. A stateful channel belongs
to exactly one worker until deterministic handback. Cancellation joins or
otherwise proves completion before borrowed storage is released: detached work
cannot retain it. A deadline or timeout never releases or reuses borrowed
storage. Result slots and merge failures are bounded and explicit.

Execution distinguishes `CancellationRequested` (cooperative request issued),
`Cancelled` (worker acknowledged and returned ownership), `DeadlineMissed`
(deadline passed while work may still run), `WorkerUnresponsive` (ownership is
not recoverable yet) and `WorkerFailed` (error or admitted unwind-capable
panic). In-process deadlines are observable scheduling requirements, not
thread-kill guarantees. Only statically bounded first-party kernels or
independently admitted extensions with bounded cooperative checkpoints may
borrow into this executor. Arbitrary/potentially blocking external algorithms
and I/O stages are prohibited work units; callers needing hard termination
must use process isolation with process-owned memory.

Executor-owned job registration is authoritative and occurs before dispatch.
Each `PlanReceipt` bounds registry slots, job identities, worker join records,
lease/result storage and terminal records. Workers/registry entries—not
handles or destructors—own submitted buffers and capacity until actual
completion and claimed return. An `ExecutionHandle<'executor, ...>` is only a
lifetime-bound observation/claim token for its executor entry; executor
ownership transfer is not admitted in the 1.0 profile.

Every slot has a linearizable atomic lifecycle:

```text
Vacant(g) -> Registered -> Running -----------------------> TerminalUnclaimed
              |                                                |    |    |
              +-> TerminalUnclaimed(CancelledBeforeDispatch)   |    |    |
                                                        Claimed Discarded ShutdownReclaimed
                                                             \    |    /
                                                               Cleaning
                                                                  |
                                                     Vacant(g+1) or Retired
```

`JobId` includes executor namespace, slot and a non-wrapping, non-reused
generation so a reclaimed slot cannot create ABA identity. Generation
exhaustion permanently retires that slot; an executor namespace may be renewed
only after every entry is idle/reconciled, and generations never wrap.
Dispatch and cancellation-before-dispatch compete on exactly one CAS from
`Registered`: if dispatch wins, the worker owns execution and later
cancellation is cooperative; if cancellation wins, the worker cannot execute
the job and the terminal kind is `CancelledBeforeDispatch`. Worker completion
publishes all terminal result/lease writes before atomically transitioning
`Running -> TerminalUnclaimed`. `status(&self)` borrows a status snapshot and
never claims anything. `try_terminal_result(self)` consumes the handle and
either atomically claims `TerminalUnclaimed -> Claimed` or returns the still-
owned nonterminal handle. `join(self)` and `cancel_and_join(self)` consume,
wait and perform the same claim transition. Shutdown uses the same registered
CAS to create `CancelledBeforeDispatch`, or reclaims an already terminal
entry; a running job must first cancel/join and publish
`TerminalUnclaimed` before shutdown reclaims it.

Two execution modes make those lifetime rules representable:

- Borrowed scoped execution uses an `ExecutionScope<'scope>` and
  `ScopedJob<'scope, ...>`. A job may report `DeadlineMissed` or
  `WorkerUnresponsive` while polled inside the scope, but neither the job nor
  its borrows can escape. The scope cannot return until every worker returns
  ownership. Permanently stuck work therefore traps that scope/process.
- Owned asynchronous execution transfers explicitly planned owned buffers or
  arena leases into a `#[must_use] ExecutionHandle`. The handle may leave a
  scope and be polled through explicit status/terminal-result APIs. Consuming
  `join` and `cancel_and_join` are the only normal paths that wait for a
  running job and recover buffers; recovery occurs only after a completed,
  cancelled or failed-and-returned terminal state. Dropping a handle attempts
  only `TerminalUnclaimed -> Discarded`; it never destroys a caller or generic
  payload, returns a lease or finalizes a trace. If the entry is `Registered`
  or `Running`, `Drop`
  directly invokes `std::process::abort()` without joining, detaching,
  panicking or unwinding. Completion racing with drop has one atomic
  linearization winner: completion must publish `TerminalUnclaimed` before
  drop's transition or drop observes nonterminal state and aborts. A
  permanently unresponsive job therefore cannot deadlock destruction or
  silently outlive ownership. Navheim 1.0 admits no quarantine/reaper mode; any
  future such profile must preplan bounded slots, retention and shutdown in
  `PlanReceipt`. No hidden `Arc`, heap allocation, worker or lease capacity
  bypasses planning.

Claim, discard and shutdown retirement feed a caller-driven, bounded registry
cleanup path before a slot becomes `Vacant`; Navheim starts no hidden cleanup
worker or reaper. The public progress contract is equivalent to:

```rust
pub fn poll_cleanup(
    &self,
    budget: CleanupBudget,
) -> Result<CleanupProgress, CleanupStartError>;
```

The shared borrow is required so completed/discarded entries can be reclaimed
while unrelated lifetime-bound handles remain live; it does not transfer
executor ownership or introduce an `Arc`. Synchronized interior registry state
contains an atomic single-cleaner guard. A cleanup call validates its budget,
then acquires the guard by CAS; a concurrent call returns
`CleanupStartError::Busy` before changing any entry, payload or admission
state. The guard is private, non-cloneable and never returned as a capability,
so callers cannot leak or forget it. Every normal return explicitly releases
it; cleanup panic/failure aborts the process, so unwinding cannot strand it.
The executor uses safe `std` synchronization and automatic trait bounds; the
1.0 profile admits no handwritten unsafe `Sync` implementation.

`PlanReceipt` bounds `Cleaning` entries, total cleanup work, work per poll and
trace capacity. `CleanupProgress` explicitly reports `Complete` or
`MoreRequired` plus bounded cleaned/remaining/retired counts and work used;
there is no hidden wakeup contract. Preflight rejects an invalid/zero budget
without mutation.
Once cleanup begins, failure, panic or same-entry reentrancy is
process-terminal rather than a recoverable return. Admission never performs
implicit cleanup: when no clean slot is available but dirty slots remain it
returns `AdmissionError::CleanupRequired` with bounded progress information.
`Executor::shutdown` first reconciles every job and then drains all cleanup;
the receipt bounds total drain work. Cleanup order, slot retirement and every
semantics-affecting result enter `ExecutionTrace` in deterministic order.
Each poll selects eligible entries by the lowest generation-bearing `JobId`;
the receipt also bounds the deterministic scan. A `Busy` result performs no
cleanup mutation; if caller behavior makes that contention semantically
relevant, its bounded scheduling fact is recorded in the runtime trace before
the caller proceeds.

`Executor` itself is `#[must_use]` because consuming shutdown is the normal
lifecycle. Dropping it with any registered, running, terminal-unclaimed,
claimed, discarded, shutdown-reclaimed or cleaning entry follows the existing
allocation-free `std::process::abort()` rule. A clean all-vacant/retired
executor may be destroyed without invoking payload cleanup.

Registry payload/result storage prefers safe state-owning enums or `Option<T>`.
The 1.0 executor admits only safe payload ownership transitions. If
`ManuallyDrop` remains for layout, it may use safe
`ManuallyDrop::into_inner`; unsafe `take`/manual-drop payload extraction is
excluded. A future unsafe layout requires a separate roadmap stop and explicit
unsafe-policy amendment rather than entering v0.48.3 implicitly. Atomic
lifecycle and payload-initialization state cannot diverge, and exactly one
transition may extract or destroy each payload. Only sealed, reviewed first-
party cleanup may reclaim payloads in-process; extension-owned arbitrary
destructors require an admitted isolation profile. On unwind-capable builds
cleanup panic is caught and immediately converted to abort, never unwinding
through registry invariants.
The slot becomes reusable only after result transfer or destruction, lease
return, trace finalization and a checked generation increment have completed.
Miri covers extraction/destruction and panic paths. Loom covers cleanup against
completion, claim, handle drop, admission, another cleanup call and shutdown,
including single-cleaner exclusion and release/acquire publication. Kani
proves the bounded exactly-once ownership machine.

`mem::forget`, `ManuallyDrop` or a leaked handle permanently forfeits that
result but never unregisters or detaches the job. The entry, buffers and slot
remain executor/worker-owned; even a completed orphan is not reused by new
admission before explicit executor shutdown. Consuming `Executor::shutdown`
cooperatively cancels and joins every registered entry, including lost-handle
and completed-orphan entries; it owns remaining transitions to
`ShutdownReclaimed` and returns only after all ownership is reconciled.
Permanently unresponsive work traps that explicit shutdown.
Dropping an executor with any unreconciled or uncleaned entry is fail-stop.
Forgetting the executor itself intentionally leaks its complete registry and
all capacity until process termination, but cannot make storage reusable or
violate memory soundness.

The Tier 2 `std` profile's fatal path is concretely
`std::process::abort()`: it is non-returning, performs no allocation or
formatting, never panics/unwinds, and runs no recovery destructors. Fatal
reason/status may be written to preallocated executor memory before entering
that path, but this is best-effort volatile evidence—not a durable or emitted
diagnostic claim. Memory soundness and ownership accounting never depend on
`ExecutionHandle`, executor or worker destructors executing.

The buffer-lease state machine is
`CallerOwned -> Submitted -> WorkerOwned -> Returned`, with
`CancellationRequested` leaving the lease `WorkerOwned` until acknowledged.
`DeadlineMissed` and `WorkerUnresponsive` are observations, not ownership
transitions. Every completion/failure path proves exactly which input, output
and scratch leases returned before exposing them to the caller.

Logical partitioning, merge order and event/invalidation ordering are
deterministic. `PlanReceipt` fixes `ExecutionTrace` capacity. The trace records
only nondeterministic deadline, cancellation, scheduling and worker-failure
facts that change semantics; replay consumes those facts instead of consulting
wall time. Overflow stops execution, forces resynchronization or explicitly
marks replay unavailable—never silently drops an event. Worker panic is a
recoverable recorded failure only on an admitted unwind-capable profile;
`panic = "abort"` or permanently stuck work is terminal for that process and
is never described as contained. Floating reductions are bit-exact only where
specified, otherwise they use published tolerances. Scalar comparison is
required verification evidence, not duplicate production computation.
Untrusted input cannot create workers or queues.

### 11.6 Tracking channel state

A channel exports:

- satellite/signal identity and confidence;
- code phase and variance;
- carrier phase and accumulated delta range;
- Doppler and rate;
- CN0;
- correlator values;
- loop discriminator/error and bandwidth;
- lock duration;
- cycle-slip and half-cycle state;
- data/pilot/secondary-code synchronization;
- interference/multipath metrics;
- hardware/sample timestamp mapping.

---

## 12. Navigation-message architecture

Every constellation crate should use the same layered decoder structure:

```text
soft symbols
  -> deinterleaver
  -> FEC decoder
  -> frame synchronizer
  -> validated bit view
  -> raw message struct
  -> semantic message struct
  -> navigation store transaction
```

Rules:

- soft-decision FEC is supported where meaningful;
- frame synchronization is reversible and reports confidence;
- all input lengths are checked before bit access;
- reserved/unknown values are preserved;
- semantic conversion occurs only after parity/CRC/FEC status is known;
- invalid messages can be retained as forensic events without entering navigation state;
- partial multi-page products have explicit assembly state and expiry;
- issue-of-data changes are atomic;
- navigation stores keep multiple generations and source provenance;
- conflicting ephemerides are not silently overwritten.

The navigation store should support transactions:

```rust
let mut update = store.begin(epoch);
update.stage(message)?;
let result = update.validate(policy)?;
update.commit()?;
```

Validation can compare health, issue-of-data, time, orbit continuity, authentication and independent sources.

Solver queries name satellite, signal, model kind and requested transmit/
receive epoch. Selection checks toe/toc, fit interval, issue-of-data, health,
future/stale/expiry/discontinuity state and source/session/generation
compatibility. Authentication assessments are inputs without becoming message
correctness. Equivalent and conflicting healthy sources are handled
deterministically through `Selected`, `Ambiguous`, `Unavailable` or `Rejected`
outcomes. A selection artifact records every candidate and rejection reason;
there is no ambient “latest wins.” Corrections and precise products use the
same explicit applicability/selection pattern.

---

## 13. PVT, RTK and PPP design

### 13.1 PVT layers

`navheim-pvt` should provide:

- Bancroft or equivalent initialization;
- iterative weighted least squares;
- robust M-estimation;
- Kalman and square-root information filtering;
- position-only, time-only, position/time and position/velocity/time states;
- multi-constellation receiver clock offsets;
- inter-system bias estimation;
- Earth rotation/Sagnac correction;
- relativistic correction;
- satellite clock and group-delay corrections;
- ionosphere and troposphere models;
- elevation/CN0/variance weighting;
- outlier detection and satellite exclusion;
- covariance and residual diagnostics.

The sequential GNSS-only state estimator is distinct from multi-sensor fusion.
Its state layout, process model, initialization, convergence, resets,
measurement admission and unavailable lifecycle are public and testable.

The solver never reports more precision than the measurement and model uncertainty support.

### 13.2 Code-differential GNSS

`navheim-rtk` also owns pseudorange/code differential positioning:

- reference-station position, observation and correction artifacts;
- satellite/issue/frequency/common-view epoch matching;
- correction age, validity and station/session identity;
- code-differential covariance and quality propagation;
- a separately typed `Dgps` solution, never an alias for RTK float;
- ordered `RtkFixed` → `RtkFloat` → `Dgps` → `Standalone` → `Unavailable`
  degradation and recovery policy with visible reasons.

Each transition is a new lifecycle artifact. A stale or incompatible base
cannot silently leave a code correction applied.

### 13.3 Carrier phase and RTK

`navheim-rtk` should include:

- carrier smoothing;
- geometry-free, Melbourne–Wübbena and time-difference cycle-slip detectors;
- single and double differences;
- pivot/reference-satellite management;
- GLONASS FDMA inter-channel bias models;
- baseline state filters;
- integer ambiguity search and validation implemented natively;
- partial ambiguity resolution;
- fix-and-hold policies with rollback;
- moving-base and heading modes;
- network RTK inputs, including VRS/FKP/MAC concepts where standardized;
- explicit ratio, success probability and residual tests;
- safe transition from fixed to float.

An `RtkFixed` result always carries the validation method and metrics.

### 13.4 PPP

`navheim-ppp` should provide:

- precise orbit and clock interpolation;
- code/phase bias application;
- uncombined and ionosphere-free models;
- troposphere state estimation;
- phase wind-up;
- solid Earth tide, pole tide and ocean-loading hooks;
- antenna phase-center models;
- convergence state and quality;
- PPP ambiguity resolution where bias products permit it;
- real-time SSR and post-processed product paths;
- PPP-RTK regional atmospheric corrections;
- product-age and reference-frame validation.

### 13.5 Atmospheric models

Support simple through scientific tiers:

- broadcast ionosphere models;
- dual-frequency ionosphere-free combinations;
- TEC estimation;
- SBAS ionosphere grids;
- global/regional precise ionosphere products;
- standard troposphere mapping functions;
- estimated wet delay and gradients;
- user-provided meteorological observations.

Models must identify their source, expected validity and uncertainty.

---

## 14. Integrity, authentication and anti-spoofing

### 14.1 Separate four concepts

Navheim must never conflate:

1. **message correctness** — CRC/parity/FEC passed;
2. **navigation-message authentication** — signed/authenticated navigation content verified;
3. **signal-source authenticity** — RF actually came through the expected satellite path;
4. **solution integrity** — probability/bounds that position or time is acceptably correct.

OSNMA can authenticate selected Galileo navigation data; it does not by itself prove that a delayed authentic signal was not rebroadcast. Multi-sensor and RF-consistency defenses remain necessary.

RAIM and ARAIM use explicit satellite, constellation-wide,
correction-provider and common-mode fault hypotheses. Their contracts name
integrity-risk allocation, alert limits, time-to-alert, continuity,
availability, correlation assumptions, service-health/URA/SISA inputs,
solution-separation or subset algorithms, exclusion exhaustion, recovery and
re-admission. Missing assumptions produce an unavailable protection level,
not a misleadingly large numeric value. SBAS-derived integrity is a separate
targeted input and is never relabeled as RAIM or ARAIM evidence.

### 14.2 OSNMA engine

The Galileo OSNMA implementation should include:

- DSM/PKR/KROOT/MACK parsing and assembly according to the current specification;
- root public-key trust store with version, source and activation times;
- public-key renewal/revocation handling;
- TESLA key-chain verification and delayed disclosure;
- tag accumulation and authenticated-data selection;
- time/freshness checks;
- cross-authentication state;
- pending/verified/failed/expired result states;
- trusted-time context, key-chain generation, trust-root version and optional
  platform anti-rollback authority;
- full evidence export without leaking secrets;
- recorded-vector replay;
- cryptographic backend traits.

### 14.3 QZNMA engine

Implement current QZSS authentication messages and their applicable authenticated constellations/signals. Keep algorithm identifiers open for future revisions. Use the same evidence and trust-store abstractions as OSNMA without forcing the protocols into one false common wire model.

### 14.4 Spoofing and meaconing detection

Provide evidence producers, not a single magical boolean:

- multi-constellation position/time disagreement;
- multi-frequency ionosphere inconsistency;
- Doppler versus ephemeris/receiver-motion mismatch;
- common-mode code/carrier behavior;
- sudden synchronized power increase;
- impossible CN0 or AGC changes;
- correlation-function distortion;
- clock step/ramp anomalies;
- navigation-message conflict;
- angle-of-arrival inconsistency using multiple antennas;
- independent receiver disagreement;
- inertial/odometry inconsistency;
- authenticated-message failure or delayed replay suspicion;
- satellite visibility/terrain mismatch when a trusted environment model is supplied.

Each evidence item targets bounded artifact IDs and records observation
interval, prerequisites, algorithm/version, confidence/statistical assumptions,
insufficient-data state and provenance. Absence of evidence is not evidence of
authenticity.

The acceptance matrix covers multi-frequency ionosphere inconsistency,
common-mode code/carrier behavior, impossible AGC/CN0 changes, trusted-terrain
visibility and every explicit insufficient-data path. A producer that lacks
its prerequisite data emits `Unavailable`/`InsufficientData`; it never emits
benign evidence.

A policy engine combines evidence with configurable thresholds and hysteresis.

### 14.5 Jamming detection

- broadband/narrowband spectral power;
- AGC saturation;
- noise-floor rise;
- per-band loss-of-lock pattern;
- pulse interference;
- intermodulation and local oscillator artifacts;
- antenna/open-circuit diagnostics when hardware supports them.

### 14.6 Provenance

Every derived item should be traceable:

```text
front-end + configuration
  -> sample block hashes/sequence
  -> tracking channel states
  -> raw frame and validation
  -> ephemeris/correction generation
  -> observation corrections
  -> solver inputs and exclusions
  -> final solution and security policy result
```

For normal embedded use this can be compact numeric IDs. For forensic profiles it can be a signed append-only evidence stream.

---

## 15. Timing architecture

`navheim-timing` should be usable independently of position solving.

Components:

- GNSS time-scale conversion;
- leap-second and UTC realization database;
- reason-bearing native/TAI/UTC availability;
- time-only solution using one or more satellites with known position;
- common-view/all-in-view time transfer primitives;
- semantic pairing of caller-captured PPS edges with receiver time marks;
- bounded named cable, antenna, receiver, capture and message-delay budgets;
- receiver clock bias, drift, covariance and discontinuity estimates;
- freshness, uncertainty growth and explicit invalidation of GNSS evidence;
- immutable targeted time-authentication, signal-source and
  solution-integrity assessments/evidence;
- a stable dependency-free observation/event API for consumer-owned adapters.

A GNSS timing observation includes:

- native GNSS and resolved atomic instants;
- UTC realization, leap model and resolution provenance;
- receiver clock bias, drift and covariance;
- caller-owned capture value wrapped by clock domain and reset generation;
- reason-bearing PPS/time-mark/frequency-output availability;
- bounded asymmetric uncertainty, named delay contributors, confidence
  semantics and correlation groups;
- satellite, signal, message and receiver health;
- freshness deadline and explicit invalidation reasons;
- complete provenance.

Authentication, integrity and spoofing evidence are separate immutable objects
targeting the observation artifact. Events carry sequence/source generation;
mandatory targeted withdrawal must be acknowledged and cannot be dropped
silently under queue pressure.

Generic PPS device capture, comparison with NTP/NTS/PTP/radio/local clocks,
clock discipline, system or PHC adjustment, oscillator servos and holdover are
outside Navheim. A project such as Mundilfari may provide a companion adapter
that depends on Navheim. Navheim never depends on it.

---

## 16. Sensor fusion and attitude

`navheim-fusion` should avoid committing all users to one filter.

Provide:

- mechanization primitives in ECEF and local NED/ENU;
- IMU bias, scale-factor, axis-misalignment, noise and temperature models;
- coning and sculling compensation;
- gravity, Earth-rate and transport-rate models;
- configurable extended Kalman filter;
- error-state EKF;
- square-root variants for numerical robustness;
- factor-graph interface for allocated/post-processing builds;
- zero-velocity and known-motion updates;
- wheel-speed/non-holonomic constraints;
- barometric altitude;
- magnetometer with explicit trust policy;
- dual/multi-antenna GNSS heading and attitude;
- lever-arm and time-offset calibration states;
- delayed/out-of-sequence measurement handling;
- dead-reckoning uncertainty growth;
- re-acquisition smoothing without hiding jumps.

Sensor timestamps and clock domains are first-class. Fusion must reject unsynchronized data rather than assuming arrival time equals measurement time.

Reacquisition corrections and state discontinuities remain observable
artifacts. The allocated factor-graph interface shares canonical measurement,
calibration, clock and residual types with the bounded real-time filters but
does not force allocation into Tier 0.

---

## 17. Receiver and operating-system support

### 17.1 Receiver protocol policy

`navheim-receiver` should contain modular adapters for public, maintainable protocols such as:

- u-blox UBX;
- Septentrio SBF;
- NovAtel OEM family where public documentation permits;
- NMEA-only receivers;
- gpsd JSON protocol;
- SkyTraq, SiRF and MediaTek/PMTK where specifications and test hardware are available;
- generic RTCM/RINEX/raw-observation sources.

Do not add a decoder based only on reverse-engineered fragments with no conformance evidence. Experimental adapters remain GitHub-only until stable.

#### 17.1.1 Receiver control boundary

Every receiver profile declares read-only, control-capable or unsupported.
Control begins with a side-effect-free plan of allowlisted typed commands for
admitted firmware/hardware profiles—never arbitrary byte injection. Plans may
cover signal enablement, output rates, time-pulse convention, correction
input, dynamic model and protocol/baud transitions. Execution correlates
ACK/NAK, uses bounded timeouts/retries, defines idempotency, survives
reconnect/baud changes, detects partial application and verifies effective
state by read-back. These wire facts form a `ControlTransaction`; ACK and
read-back are receiver assertions, not independent proof that the receiver
behaves as configured. A separate `ConfigurationAssessment` compares observed
output rate, enabled signals, protocol, time-pulse behavior and correction
ingestion with the requested state. It targets one configuration generation
and carries the observation interval, evidence sources, coverage, uncertainty
and unverifiable fields. It reports `ReceiverAsserted` wherever behavior cannot
be independently observed and `ObservedConsistent` only for the behavior and
interval actually evidenced; neither state proves internal configuration or
signal authenticity. Capability matrices and logs redact location, credentials
and sensitive configuration.

Every applied change creates a `ReceiverConfigurationGeneration` bound to
exact device/firmware identity and an effective epoch or transition interval.
The transition drains or marks stale input/output queues and mandates targeted
invalidation of affected observations, time/capture mappings, calibrations and
correction sessions before rebinding. Commands are typed as volatile,
persistent-flash or destructive/reset operations. Persistent writes have
flash-wear budgets; persistent and destructive classes require separate
authorization and cannot hide inside ordinary retry.
Configuration assessments are invalidated on receiver reset, firmware change,
device replacement or contradictory stream evidence.

### 17.2 OS-native I/O

`navheim-io` should expose portable traits and target-specific modules:

- Linux: termios, usbfs/libusb adapter, sockets and IIO where useful;
- Windows: COM, WinUSB, Winsock, location sensor interfaces and high-resolution clocks;
- macOS: serial, IOKit USB, Network framework/standard sockets, Core Location adapter;
- FreeBSD/OpenBSD/NetBSD: termios, ugen/libusb adapter and sockets;
- Android: raw GNSS measurements, location, USB host and network adapters;
- iOS: Core Location-derived fixes; raw measurement access only if the platform exposes it;
- WASM: files/buffers/web streams for decode and post-processing, no direct radio claim.

The direct system-call/FFI backend may remain zero third-party dependencies. A separately feature-gated libusb or platform-binding backend may improve maintenance without contaminating core crates.

Android raw measurements and fused/location-provider fixes are different
artifacts. OS-derived fixes preserve provider, permission, mock state, elapsed
realtime/capture domain, accuracy and reset provenance and never manufacture
raw observations. USB-host adapters model permission intents, attach/detach,
endpoint cancellation and identity reuse. Network adapters expose Android
connectivity/background/throttling failures without hidden retries or threads.

### 17.3 Device discovery

Device discovery returns candidates and evidence, not an automatically trusted device:

```rust
pub struct DeviceCandidate {
    pub transport: TransportKind,
    pub path: DevicePath,
    pub vendor_product: Option<(u16, u16)>,
    pub protocols: CandidateProtocols,
    pub permissions: PermissionState,
    pub trust: DeviceTrust,
}
```

Candidate enumeration is bounded and records transport identity, evidence,
permission and hotplug generation. Opening a candidate is always a separate
explicit action. Each protocol probe receives independent byte, work, response
and elapsed-time budgets and isolated parser state; one failed probe cannot
pollute another.

Deterministic source ranking returns a `SelectionExplanation` containing every
candidate, disqualifying capability/policy reason, score component and tie
break. Users can disable discovery and configure transport/device/protocol
allowlists. Hotplug, removal and path/identifier reuse create new generations
and invalidate prior evidence. Discovery never opens a device automatically.

---

## 18. Configuration profiles

The facade should provide safe profiles that are merely documented configuration sets, never separate algorithms:

- `Profile::Navigation` — balanced, robust live navigation.
- `Profile::Embedded` — fixed memory and CPU budget.
- `Profile::Survey` — complete observations and conservative corrections.
- `Profile::Timing` — PPS/time quality and integrity prioritized.
- `Profile::SecurityMonitor` — maximum evidence and cross-checking.
- `Profile::Scientific` — preserve raw and intermediate data.
- `Profile::LowPower` — scheduled acquisition/tracking.
- `Profile::AviationResearch` — integrity outputs; explicitly not certification.
- `Profile::Replay` — deterministic, no wall-clock dependence.

Every profile can be expanded to a printable canonical configuration so there are no hidden defaults.

Profile defaults are versioned data. Expansion is side-effect free and either
produces one complete canonical configuration/plan input or a structured
capability/resource failure; it never silently falls back. Tests compare each
profile against the equivalent explicit configuration and prove that profiles
select no alternative implementations or hidden algorithms.

### 18.1 Runtime source supervision

After explicitly opened sources enter a facade, a deterministic supervisor
tracks their identity, generation, capability, health, gaps and withdrawal.
Source loss or provider change emits withdrawal/gap artifacts before any
reselection. Every source has a logical role and a machine-readable
composition/compatibility graph. Old and replacement generations of the same
role cannot overlap unless a declared transition policy permits it. Different
roles—receiver/correction, GNSS/inertial, antenna/receiver arrays and
independent security comparators—may compose only with valid clock mappings,
correction sessions, calibration, provenance and epoch compatibility. Retry,
failover and recovery are bounded caller-authorized policies with deterministic
ordering and explicit decisions; the supervisor never silently lowers
accuracy, integrity, authentication or trust requirements.

Same-role replacement invalidates source-dependent receiver-clock and
inter-system biases, antenna/lever-arm calibration, carrier ambiguities and
cycle-slip continuity, correction ledgers, smoothing filters, timing/PPS
mappings, and integrity/authenticity assessments by default. State survives
only through an explicit handover transform carrying calibration, clock
mapping, uncertainty growth and provenance. Outputs expose a gap,
discontinuity, reconvergence or bounded coasting state during the handover;
they never imply silent continuity.

---

## 19. Error and event design

### 19.1 Errors

Use structured, non-string errors:

- `DecodeError` with protocol, offset, expected/actual and recoverability;
- `CapabilityError` with missing hardware feature;
- `TimeError` with ambiguity/scale/leap source;
- `SolutionError` with geometry, rank, convergence or invalid model;
- `IntegrityError` with failed assumption;
- `SecurityError` with trust/authentication stage;
- `IoError` only in `std` crates;
- `ResourceError` with required and available capacity.

No input-dependent panic is acceptable under the parser's declared capacity
and work limits.

### 19.2 Events

Events should cover:

- device and source state;
- front-end overrun/underrun;
- signal acquired/lost;
- frame synchronized/lost;
- navigation data accepted/rejected/conflicted;
- authentication progress/result;
- correction connected/stale/rejected;
- epoch observations;
- position/time/attitude fix;
- integrity transition;
- interference/security alert;
- resource pressure;
- recording and replay checkpoints.

Events include sequence, source generation, capture domain/time, target
artifact where applicable and provenance. Mandatory invalidation/security
events cannot be dropped silently; queue pressure stops, explicitly coalesces
or forces resynchronization.

---

## 20. Performance and resource planning

Every configuration should be able to answer before starting:

- required RF channels;
- selected center frequencies and sample rates;
- input throughput;
- minimum sustained disk/network rate for recording;
- tracking channel count;
- fixed and peak memory;
- approximate scalar CPU cost;
- availability of SIMD/FPGA acceleration;
- solver state dimension;
- maximum parser frame and correction cache sizes;
- stack, caller scratch, alignment and non-overlap requirements;
- work tokens, candidate/event/output limits and queue depth;
- maximum navigation/FEC assemblies and decoder iterations;
- latency budget, recovery policy and forensic retention.

The builder returns a normalized immutable receipt and rejects impossible
configurations before opening hardware. Execution accepts only inputs matching
that receipt.

Performance targets should be profile- and platform-specific, for example:

- bounded NMEA/RTCM decoding on microcontrollers;
- real-time GPS L1 on a modest desktop CPU;
- real-time upper-L multi-constellation processing on a modern multicore CPU;
- full multi-band processing with SIMD and/or FPGA assistance;
- deterministic replay faster than real time for CI subsets.

Do not publish one meaningless “real-time” claim.

---

## 21. Security engineering requirements

### 21.1 Threat model

Document threats from:

- malicious RF transmitters;
- malformed receiver firmware output;
- malicious RTCM/NTRIP/SUPL servers;
- hostile RINEX/product/capture files;
- compromised local devices;
- time rollback and stale data;
- stale, replayed, rolled-back, forged, privacy-exposing, misleadingly
  digest-valid, authenticated-but-plaintext or authenticated/encrypted but
  freshness-unchecked algorithm snapshots, including counter-checked state
  misrepresented as guaranteed fresh;
- nonce reuse, protection-suite downgrade, unauthenticated envelope metadata,
  corruption/artifact/transaction-digest confusion, noncanonical protected
  encodings, caller-time reservation expiry, partially committed cross-
  authority promotion/finalization, ambiguous restore eligibility, unbounded
  pending candidates/retries/retention, cleanup of unresolved authoritative
  state, unauthorized repair, old-namespace revival, same-namespace counter
  reset, nonce reuse or silent freshness downgrade, competing recovery/writer
  state and platform-keystore lifecycle failure;
- source role/failover/generation confusion and silent trust downgrade;
- receiver-control partial application, configuration-generation confusion or
  receiver-asserted false state, unintended persistent/destructive transition;
- direct/unplanned/partially applied SDR mutation, missing success/no-mutation
  proof, control-flow proof overstated as physical stability, lost control
  lease/other-controller/autonomous changes, lost apply causes/evidence, stale
  configuration-generation samples, false rollback/coherence or device-
  asserted state;
- aliased/detached/unresponsive parallel work, forgotten/leaked handles or
  executors, dispatch/cancel and completion/drop/cleanup races, arbitrary or
  reentrant destructors in handle `Drop`, hidden/unbounded cleanup, admission
  starvation from live-handle-exclusive cleanup, overlapping cleaners, leaked
  cleanup authority, nondeterministic entry selection, lifecycle/payload-state
  divergence, duplicate extraction or destruction, stale/ABA/exhausted job
  IDs, detached registry entries,
  premature capacity/buffer reuse, overstated pre-abort
  diagnostics, trace overflow, nondeterministic ordering or uncaptured runtime
  outcomes;
- correction mixing across stations/frames;
- resource exhaustion and decompression bombs;
- parser differential behavior;
- supply-chain compromise;
- unsafe FFI and DMA;
- privacy leakage from position streams and caster credentials.

### 21.2 Mandatory controls

- bounded parsing and allocation;
- checked arithmetic around lengths, epochs and bit offsets;
- no input-dependent panic under declared resource limits;
- exact CRC/parity/FEC status;
- time and issue-of-data freshness checks;
- correction provider/station/coordinate validation;
- atomic versioned snapshot restore with separate authenticity/confidentiality,
  independent freshness evidence, minimum sensitive profiles, authenticated
  metadata, nonce/key/rotation/counter lifecycle, consent/retention, external
  protection plus staged/pending/authority-commit/promotion/finalization
  recovery over a domain-separated canonical protected-snapshot binding where
  admitted, a common restore/writer/action state matrix, bounded candidates,
  retention/retries and deterministic cleanup, authority-clock reservation
  expiry, narrow counter-checked semantics, privileged repair limited to exact
  current recovery or durable fresh-domain continuity break, honest repair/
  freshness unavailability and restored-assessment invalidation;
- prepared/reviewable SDR configuration plans with non-reusing generations,
  framework-issued pre-submission tokens, exclusive control leases,
  proof-carrying success/no-command outcomes and cause-carrying partial/unknown
  outcomes, coherent group transactions, initialized-count reads, transition
  invalidation and observed consistency;
- typed allowlisted receiver-control plans with configuration generations,
  command-class authority, transactional acknowledgement/read-back and
  independently evidenced configuration assessment;
- role-aware source withdrawal/composition/reselection, explicit solver-state
  handover and deterministic scoped-borrowed or owned-handle cooperative
  parallel work with authoritative executor registration, dispatch/cancel
  linearization, destructor-free handle retirement, caller-driven receipt-
  bounded shared-borrow cleanup/backpressure with no hidden reaper, internal
  single-cleaner CAS, deterministic bounded selection and no caller-held
  cleanup authority, coupled lifecycle/payload state and safe-only 1.0
  ownership transitions, non-wrapping generation-safe slot reuse, leak-safe
  accounting, explicit claim/shutdown/fail-stop rules, bounded traces and
  unresponsive lease ownership;
- TLS certificate validation through Rustls adapter;
- non-clone/non-serializable secret types, guarded exposure and reviewed
  zeroization where owned buffers exist;
- no logs containing passwords, authorization headers, precise location/time,
  raw captures or globally correlatable provenance by default;
- explicit network allow lists;
- reproducible builds and locked toolchains;
- dependency allow list for adapter crates;
- fuzzing and sanitizers;
- independent audits before 1.0.

### 21.3 Security modes

- **Permissive:** maximize availability, emit alerts.
- **Balanced:** reject clearly invalid/stale data, allow unauthenticated open signals with status.
- **Strict:** require configured authentication/integrity and independent consistency.
- **Forensic:** retain raw evidence and every rejection reason.
- **Safety research:** conservative timeouts/protection outputs, no certification claim.

---

## 22. Testing and conformance strategy

### 22.1 Test pyramid

1. bit/field unit tests from standards examples;
2. property tests for codecs and arithmetic;
3. generated valid/invalid frames;
4. official or operator-provided sample vectors;
5. independent recorded RF and receiver observations;
6. differential tests against multiple mature implementations/receivers;
7. live-sky tests;
8. shielded simulator tests;
9. multi-day field and timing tests;
10. cross-platform and `no_std` builds.

### 22.2 Required release gate for every 0.x release

Every version, even a small one, must pass:

- clean build with stable Rust and behavioral core tests at pinned MSRV once
  behavior exists;
- `no_std` builds for applicable crates;
- all unit/property/conformance tests;
- fuzz smoke run for touched parsers;
- Miri for applicable unsafe-adjacent APIs;
- sanitizer runs for FFI tools;
- zero undocumented panic paths on untrusted input;
- benchmark comparison with an explicit regression budget;
- source-first review of exact authoritative revisions, amendments, errata,
  sections/tables, legal access and independent references before code;
- standards/requirements mappings from source to implementation and tests;
- all applicable positive, negative, boundary, malformed, adversarial,
  conformance, differential, resource, fuzz, platform and regression tests in
  the same milestone, with reasons for every not-applicable class;
- standards manifest update; an implemented record cannot have empty
  `implemented_by` or `tests` mappings;
- changed-code security review;
- public API and migration notes;
- at least one negative/adversarial test for the new surface.

Missing or ambiguous authoritative evidence stops implementation rather than
being filled from memory or unofficial summaries. A tag is created only after
the release-specific threat review passes. This fits a “pentest from previous
tag to HEAD” workflow while periodic full-project audits remain mandatory.

### 22.3 Fuzz targets

At minimum:

- every navigation frame/page decoder;
- NMEA, RTCM, NTRIP source table, RINEX and IGS files;
- SUPL/LPP ASN.1 decoders;
- receiver vendor protocols;
- capture metadata;
- time conversion and rollover handling;
- correction caches and issue-of-data transitions;
- solver rank/degenerate geometry;
- OSNMA/QZNMA state machines.

### 22.4 Numerical verification

- high-precision reference calculations generated independently;
- exact rational/integer checks where possible;
- randomized orbit/clock comparison;
- condition-number and near-singular geometry tests;
- reproducible floating-point modes for replay;
- cross-architecture tolerances documented per algorithm;
- fixed-point versus floating-reference comparison.

### 22.5 RF validation

Use conducted or shielded tests for generated GNSS-like signals. Never radiate spoofing or simulator signals into the open environment. Include:

- nominal dynamics;
- high Doppler/acceleration;
- weak signal;
- multipath;
- CW/chirp/pulsed interference;
- data-bit errors;
- oscillator error;
- sample loss and timestamp discontinuity;
- spoof/meaconing scenarios;
- constellation outages and bad ephemerides.

---

## 23. Hardware architecture for full implementation

The software architecture assumes the complete lab exists. Hardware acquisition is a project staging issue, not a reduction of the 1.0 target.

### 23.1 Minimum serious development lab

#### Primary SDR

Choose one:

- **USRP B210:** 2 coherent RX channels, approximately 70 MHz–6 GHz, up to roughly 56 MHz instantaneous bandwidth, external 10 MHz/PPS/GPSDO support. This has a strong research ecosystem and is a safe reference choice.
- **bladeRF 2.0 micro xA9:** 2x2, approximately 47 MHz–6 GHz, up to roughly 56 MHz filtered bandwidth, 61.44 MS/s-class operation and a larger FPGA than xA4. This is often the stronger value choice for custom FPGA work.

A LimeSDR-USB is also useful, but the project should pick one primary reference SDR to prevent driver/testing dilution.

Two-channel hardware is sufficient to implement and validate every public band sequentially and many dual-band combinations. It is not sufficient for simultaneous observation of all four broad band groups.

#### Full-band L-band antenna

Use a survey-grade antenna covering:

- GPS/QZSS L1/L2/L5/L6;
- Galileo E1/E5/E6;
- GLONASS G1/G2/G3;
- BeiDou B1/B2/B3;
- NavIC L5;
- SBAS.

A Tallysman TW3990XF-class full-band antenna is an example. Prefer a calibrated antenna with a phase-center model for survey/PPP work.

#### NavIC S-band antenna path

Buy or build a separate approximately 2492 MHz antenna system:

- right-hand circularly polarized patch or helix centered near 2492.028 MHz;
- low-noise amplifier with known noise figure and gain;
- narrow band-pass filter;
- bias tee and power supply compatible with the LNA;
- suitable low-loss coax.

Most “full-band GNSS” antennas stop below this S-band service.

#### Reference GNSS receiver

Use at least one independent multi-band raw-observation receiver:

- **u-blox ZED-F9P development board** for accessible multi-band RTK, RTCM and raw code/carrier comparison;
- **Septentrio mosaic-X5 evaluation kit** or equivalent professional multi-frequency receiver for broader signal coverage and independent high-quality observables.

The inexpensive receiver is excellent for continuous CI/field comparison; the professional receiver is important for full-band and advanced-signal verification.

#### Timing reference

- **u-blox ZED-F9T development/evaluation board** or equivalent timing receiver;
- stable OCXO or rubidium reference if timing is a major objective;
- 10 MHz/PPS distribution amplifier when synchronizing several SDRs;
- time-interval counter or high-quality oscilloscope for PPS measurements.

#### RF accessories

- full-band low-noise amplifiers and band-specific filters;
- 2/4-way GNSS RF splitter with DC-path plan;
- DC blocks;
- bias tees;
- fixed attenuator kit from roughly 1 to 60 dB;
- SMA torque wrench and good cables;
- lightning/surge protection for outdoor antennas;
- optional notch filters for local interference;
- RF power meter or spectrum analyzer access;
- antenna current/voltage measurement.

#### Safe test enclosure

- RF shield box or Faraday enclosure;
- conducted RF path with at least 60–100 dB controllable attenuation;
- feedthroughs and DC paths;
- termination loads;
- strict “no open-air simulator transmission” procedure.

#### Computer

Recommended practical host:

- modern 12–16 or more CPU cores;
- 64 GB RAM minimum, 128 GB useful for long scientific processing;
- 2–4 TB fast NVMe for raw captures;
- reliable USB 3.x for B210/bladeRF or 10/25/100 GbE for higher-end USRPs;
- Linux as the primary SDR development OS, while CI validates other OSes.

### 23.2 Full simultaneous all-band laboratory

For simultaneous upper-L, lower-L, middle-L and NavIC S-band reception, use one of:

1. **USRP X410** with four independent coherent RX channels, suitable clocking and high-throughput Ethernet; or
2. **USRP N310** where its per-channel bandwidth is sufficient for the chosen splits; or
3. two synchronized B210/bladeRF-class units with shared 10 MHz/PPS, carefully calibrated transport latency and four RF paths.

The X410-class approach is the cleanest but costs tens of thousands of dollars before antennas, host networking and accessories. Renting one or using a university/company RF laboratory for final conformance may be more rational than buying it early.

A full simultaneous setup needs:

- four RF channels;
- four band-specific filtered/LNA paths or a correctly engineered antenna/splitter network;
- coherent common reference;
- calibrated channel delay and phase;
- a host that can sustain the aggregate sample rate;
- large NVMe capture storage;
- an independent multi-band reference receiver.

### 23.3 Simulator and certification-grade validation

For complete repeatable validation, obtain access to a commercial multi-constellation, multi-frequency simulator such as a Spirent, Rohde & Schwarz or Safran/Skydel-class system. Required capabilities depend on the final scope:

- GPS, Galileo, GLONASS, BeiDou, QZSS, NavIC and SBAS;
- modern signals and authentication data;
- multi-antenna/angle simulation if attitude/anti-spoofing is tested;
- interference/spoofing scenarios;
- external clock and hardware-in-the-loop;
- calibrated RF levels.

This is expensive and can be rented or accessed through a lab. An open Navheim simulator remains useful but cannot be the only oracle for its own receiver.

### 23.4 Optional research equipment

- calibrated IMU and wheel/odometry source;
- dual or triple GNSS antennas for heading/attitude;
- antenna rotator or surveyed baseline;
- vector network analyzer for antenna/filter checks;
- environmental chamber for oscillator/front-end tests;
- spectrum analyzer;
- programmable attenuator;
- RF recorder;
- precise survey monument/reference coordinates.

---

## 24. What your current hardware can do

Your current equipment remains valuable as the first development target.

### 24.1 NooElec NESDR SMArTee XTR

Strengths:

- inexpensive and easy to dedicate to continuous tests;
- TCXO improves tuning stability over basic dongles;
- bias tee can power a compatible active antenna;
- E4000 tuning range covers the main 1.575–1.61 GHz L1/E1/B1/G1 region;
- enough bandwidth for GPS L1 C/A and useful single-signal/limited multi-signal acquisition work;
- ideal for building the raw sample, acquisition, tracking, LNAV and replay foundations.

Limitations to isolate to this hardware section—not to the architecture:

- practical RTL2832U sample bandwidth is only a few megahertz;
- it cannot capture the full roughly 50 MHz upper-L group at once;
- it cannot perform full AltBOC/E5 or other wideband signal work;
- the E4000 has a documented gap around the 1.1–1.2 GHz region, making the 1176.45 MHz L5/E5a/NavIC-L5 area unsuitable as a dependable reference;
- its upper tuning range does not reach NavIC S band near 2492 MHz;
- it lacks the deterministic timestamps, coherent multichannel operation and external-reference integration desired for precision phase/timing work;
- 8-bit samples and consumer USB behavior limit dynamic range and repeatability.

Recommended first milestones with it:

1. raw USB sample source and recording;
2. GPS L1 C/A code generation;
3. acquisition and Doppler search;
4. DLL/PLL tracking;
5. LNAV and ephemeris decode;
6. pseudorange generation and standalone PVT;
7. Galileo E1/BeiDou B1/QZSS L1/SBAS experiments one configuration at a time;
8. selected GLONASS L1 FDMA channel experiments within the chosen sample window;
9. jamming/noise-floor metrics;
10. deterministic replay and fuzz/conformance infrastructure.

### 24.2 Your dual-band active antenna

Treat the marketing label as provisional until a datasheet or measurement confirms:

- exact passbands;
- LNA gain and noise figure;
- supply voltage/current;
- polarization;
- out-of-band rejection;
- whether it covers Galileo E5/E1, QZSS, NavIC L5, BeiDou B1/B2 and GLONASS bands—not merely a subset;
- maximum bias voltage.

Before connecting it to an always-on bias tee, verify its accepted voltage/current and make sure it is not also being powered from another source. It is a good development antenna, but it should not be the only conformance antenna.

---

## 25. Concrete purchase plan

### 25.1 Buy first

1. **Primary serious SDR:** bladeRF 2.0 micro xA9 or USRP B210. Choose B210 for the broadest reference ecosystem; choose xA9 for value and FPGA experimentation.
2. **Full-band calibrated L-band GNSS antenna:** Tallysman TW3990XF-class or equivalent.
3. **u-blox ZED-F9P evaluation/development board:** inexpensive raw-observation and RTK reference.
4. **RF attenuator kit, DC block, splitter, good SMA cables and compatible bias-tee power plan.**
5. **RF shield box:** needed before generating or replaying GNSS-like RF.
6. **Fast 2–4 TB NVMe storage** if the existing workstation does not already have capture capacity.

This set allows serious work on almost every L-band civil signal, sequential band validation, RTK comparison and safe replay.

### 25.2 Buy for timing and security work

7. **ZED-F9T timing board** or professional timing receiver.
8. **Stable 10 MHz/PPS reference and distribution** for multiple devices.
9. **Time interval counter or suitable oscilloscope.**
10. **Second independent receiver/antenna** for spoofing and common-mode comparison.
11. **Dual-antenna hardware** if angle-of-arrival and heading are goals.

### 25.3 Buy to close complete signal coverage

12. **Separate NavIC S-band 2492 MHz antenna, BPF and LNA.**
13. **Professional full-signal receiver, preferably Septentrio mosaic-X5-class.**
14. **Additional synchronized SDR channels** or access to an N310/X410-class platform.
15. **Commercial simulator access** for modern signals, authentication, dynamics and repeatable fault scenarios.

### 25.4 Do not buy immediately

- A USRP X410 solely to begin development.
- Multiple unrelated low-cost SDR models before one reference backend is mature.
- Unknown “all-band” antennas without passband and power specifications.
- Open-air GNSS transmit hardware.

The best cost sequence is RTL-SDR foundation → B210/xA9 + full-band antenna → ZED-F9P/F9T references → S-band path → professional receiver/lab access → four-channel/simulator validation.

---

## 26. Version and implementation roadmap

The roadmap deliberately uses many small releases. Each release adds one auditable surface and must satisfy the universal release gate in section 22.2.

### Phase A — Foundation and contracts

- **0.1.0** — workspace, licenses, security policy, MSRV, CI and `standards/manifest.toml`.
- **0.1.1** — metadata-driven crate/tier/unsafe policy plus strict SemVer, tag, pentest-parent and package-provenance validation.
- **0.1.2** — exact standards-document, amendment, legal-access, implementation and test-traceability schema.
- **0.1.3** — repository-wide requirement, public-claim, ownership, milestone and verification traceability ledger.
- **0.1.4** — machine-readable crate and capability dependency DAG with normal, optional, build and development edges, tier/feature annotations and escalation checks.
- **0.2.0** — checked arithmetic, capacities and structured core error model.
- **0.2.1** — safe fixed byte buffers and checked fixed-capacity UTF-8 strings.
- **0.2.2** — safe bounded sequence/deque contracts with documented representation and cost.
- **0.2.3** — caller-owned scratch-region and bounded-arena handles.
- **0.3.0** — exact scaled-integer and reduced-rational numeric primitives.
- **0.3.1** — physical unit types and checked conversions.
- **0.3.2** — measurement intervals, asymmetric uncertainty, typed covariance and finite floating adapters.
- **0.3.3** — deterministic first-party `no_std` elementary math and stable backend contract.
- **0.3.4** — bounded first-party linear algebra with fixed/caller-scratch storage, stable factorizations, rank/condition evidence and narrow solver-facing APIs.
- **0.3.5** — admitted statistical kernels with bounded error, log-probability support and conservative integrity-threshold rounding.
- **0.4.0** — raw native GNSS time fields and extensible scale identifiers.
- **0.4.1** — resolved native instants with private fields and resolution evidence.
- **0.4.2** — capture clock-domain/generation identifiers and exact sample timestamps.
- **0.4.3** — truncated week/day/era ambiguity alternatives and resolution context.
- **0.5.0** — exact TAI instant and explicit GNSS-scale conversion.
- **0.5.1** — UTC realization and leap model with provenance, activation, freshness and expiry.
- **0.5.2** — time rollback/freshness guard and platform persistence-authority contract.
- **0.5.3** — reason-bearing time availability and targeted invalidation primitives.
- **0.5.4** — exact TAI/duration epoch, representation, range, granularity and checked-arithmetic contract.
- **0.5.5** — UTC civil/calendar labels, leap insertion/deletion, POSIX ambiguity/loss and exact-range Gregorian/ordinal/Julian/MJD conversion contracts.
- **0.6.0** — coordinate types: geodetic, ECEF, ENU and NED.
- **0.6.1** — body frames, velocity, acceleration, rotations, lever arms and sensor latency.
- **0.6.2** — typed covariance layouts with state ordering, units, frame and epoch.
- **0.7.0** — geodesic, ellipsoid and reference-frame primitives.
- **0.7.1** — datum/reference-frame realization and Earth-orientation input contracts.
- **0.7.2** — `navheim-geo` bounded UTM/UPS and Transverse Mercator projected-coordinate profiles with explicit zone, frame, epoch, convergence and distortion evidence.
- **0.7.3** — TT and UT1/EOP-derived precision-geodesy time arguments with revision, validity, uncertainty and explicit separation from GNSS scales.
- **0.8.0** — bit readers/writers, sign extension and reserved-bit preservation.
- **0.8.1** — exact-consumption results and original-bit/canonical round-trip modes.
- **0.9.0** — checksums, CRC framework and GNSS parity primitives.
- **0.9.1** — named constellation parity/checksum families with authoritative vectors.
- **0.10.0** — convolutional, BCH, Reed–Solomon and interleaving primitives required by the selected ICDs.
- **0.10.1** — bounded soft decisions, path-metric saturation and interleaver capacity contracts.
- **0.11.0** — LDPC/polar or other modern FEC kernels required by public signals, one verified family at a time.
- **0.11.1** — fixed iteration/work limits and decoder resource receipts.
- **0.12.0** — extensible system/satellite/signal identifiers and registry versioning.
- **0.12.1** — namespaced registry authorities and bounded identifier sets without closed public masks.
- **0.12.2** — bounded user-decoder registration and namespaced opaque-artifact boundary.
- **0.12.3** — safe external algorithm and processing-stage extension contracts with preflight capabilities, resource limits, trust, provenance and reset isolation.
- **0.12.4** — versioned canonical signal definitions for frequency, wavelength, rates, components, modulation, native time and format mappings.
- **0.13.0** — canonical observation/epoch model with distinct transmit, receive and capture times.
- **0.13.1** — immutable artifacts, bounded provenance parents and separate targeted assessment identifiers.
- **0.13.2** — tracking, raw receiver, raw SDR, normalized, corrected and solver-input observation stages.
- **0.13.3** — typed horizontal/three-dimensional speed, course-over-ground and climb-rate observations with covariance, epoch and unavailable-state semantics.
- **0.14.0** — ephemeris, almanac, health and satellite-clock model traits.
- **0.14.1** — model issue, validity, discontinuity, delay, uncertainty and transactional generation rules.
- **0.14.2** — deterministic navigation-model and correction/product applicability selection with explicit considered-candidate evidence.
- **0.15.0** — correction and provenance models.
- **0.15.1** — immutable correction sessions and ordered applied-correction ledger with anti-mixing policy.
- **0.15.2** — canonical physical correction/bias taxonomy and duplicate-application prevention.
- **0.16.0** — event, source, sink and deterministic polling traits with explicit invalidation.
- **0.16.1** — small push/poll/transform/reset vocabulary with borrowed or caller-provided output slots.
- **0.16.2** — sequenced targeted invalidation, acknowledgement, queue pressure and resynchronization contracts.
- **0.16.3** — sequence/generation exhaustion, renewal and non-wrapping replay-safety contract.
- **0.17.0** — capability negotiation and resource-planning contracts.
- **0.17.1** — executable preflight schema and immutable normalized `PlanReceipt`.
- **0.17.2** — prepared facade planning and caller review before devices, credentials, networking or threads.
- **0.18.0** — canonical configuration serialization without external serialization crates.
- **0.18.1** — versioned bounded algorithm-state snapshot envelope, opt-in restore contract and external freshness-authority boundary.
- **0.18.2** — orthogonal snapshot authenticity/confidentiality/freshness, narrow counter-checked semantics, minimal sensitive profiles and restored-assessment invalidation policy.
- **0.19.0** — allocated convenience layer.
- **0.20.0** — initial `navheim` facade and `Profile::Replay`.
- **0.20.1** — structural Tier 0/static, Tier 1/owned and Tier 2/host facade boundaries.
- **0.20.2** — all named facade profiles, versioned canonical expansion and capability-failure equivalence.
- **0.20.3** — deterministic runtime source supervisor with explicit withdrawal, gap, authorized retry/failover and generation-safe reselection artifacts.
- **0.20.4** — source-role composition/compatibility graph with solver-state-safe same-role handover and valid cross-role mixing evidence.

### Phase B — File and byte-stream interoperability

- **0.21.0** — NMEA 0183 framing, checksum and bounded recovery.
- **0.21.1** — parser forward progress, exact consumption, deterministic chunks and structured offsets.
- **0.22.0** — GNSS-relevant NMEA 0183 sentence models for the licensed baseline.
- **0.22.1** — borrowed/visitor, owned, canonical and original-preserving NMEA APIs.
- **0.23.0** — RTCM 3 framing and CRC.
- **0.23.1** — raw frame, correctness assessment, semantic conversion and transactional insertion boundary.
- **0.24.0** — RTCM station/antenna descriptor messages.
- **0.25.0** — RTCM MSM observation decoding/encoding.
- **0.25.1** — MSM provider/station/frame/session binding and cross-constellation round trips.
- **0.26.0** — RTCM constellation ephemeris messages.
- **0.26.1** — RTCM legacy observation profiles retained by the frozen baseline.
- **0.26.2** — RTCM surveying transformation and projection message profiles.
- **0.27.0** — NTRIP source table and version 1 client.
- **0.28.0** — NTRIP version 2 client/server/caster protocol core.
- **0.28.1** — bounded redirects/reconnects/headers, credential redaction, GGA consent and downgrade policy.
- **0.29.0** — RINEX 2 observation streaming parser/writer.
- **0.29.1** — RINEX 2 navigation streaming parser/writer.
- **0.30.0** — RINEX 3 observation and navigation support.
- **0.31.0** — RINEX 4 generic navigation records and current additions.
- **0.31.1** — cross-version canonical/original preservation and deterministic chunk-boundary audit.
- **0.31.2** — RINEX meteorological and clock file profiles across supported revisions.
- **0.31.3** — RINEX 4 observations and picosecond timing-field support.
- **0.31.4** — bounded optional CRINEX/Hatanaka codec integration.
- **0.32.0** — SP3 orbit and precise clock products.
- **0.33.0** — IONEX.
- **0.34.0** — ANTEX.
- **0.35.0** — SINEX and Bias-SINEX foundations.
- **0.35.1** — Earth-orientation and reference-frame product parsing with validity and provenance.
- **0.36.0** — deterministic raw-I/Q and observation replay container v0.
- **0.36.1** — replay checkpoints, digests, corruption recovery and version compatibility.
- **0.36.2** — cross-format canonical comparison and differential parser audit.
- **0.36.3** — GitHub-only `navheim-capture` record/import/export utility with privacy-safe metadata.

### Phase C — Native DSP reference implementation

- **0.37.0** — complex/fixed-point types, NCO and oscillators.
- **0.37.1** — fixed-point widening, narrowing, rounding, saturation and sticky-overflow replay contract.
- **0.37.2** — native front-end sample normalization, DC/IQ correction and bounded interference conditioning.
- **0.38.0** — FIR/IIR and decimation primitives.
- **0.39.0** — polyphase resampling.
- **0.39.1** — rational resampler timestamp and group-delay accounting.
- **0.40.0** — scalar radix-2/radix-4 FFT.
- **0.40.1** — accepted FFT size families, checked factorization and caller-scratch planning.
- **0.41.0** — mixed-radix FFT and convolution.
- **0.41.1** — floating numerical replay contract for FMA, denormals, finiteness and platform tolerances.
- **0.42.0** — polyphase channelizer.
- **0.42.1** — dependency-free search-aid and acquisition-hint artifacts with bounded fallback, expiry, trust and plan-reduction evidence.
- **0.42.2** — immutable search-execution/decision receipt type, serialization and bounded schema contract.
- **0.43.0** — acquisition search framework and peak statistics.
- **0.43.1** — acquisition work tokens, bounded candidates and named false-alarm assumptions.
- **0.43.2** — acquisition integration for executable search-decision receipts, dynamic hints, bounded fallback and deterministic replay.
- **0.44.0** — DLL/FLL/PLL tracking-loop primitives.
- **0.44.1** — loop coefficient/stability evidence and discontinuity/reacquisition lifecycle.
- **0.45.0** — correlator banks, CN0 and lock estimators.
- **0.46.0** — bit/symbol/secondary-code synchronization.
- **0.47.0** — sample timestamp, gap and overrun model.
- **0.47.1** — sample/host/hardware capture-domain mapping and per-block metadata validation.
- **0.47.2** — explicit capture-domain mapping validity, uncertainty, discontinuity and generation contract.
- **0.48.0** — scalar real-time scheduler and channel lifecycle.
- **0.48.1** — scheduler work tokens, candidate/channel eviction, backpressure and resource events.
- **0.48.2** — SIMD alignment, aliasing, feature-detection, fallback and unsafe-contract boundary.
- **0.48.3** — `navheim-executor` scoped/owned modes with live-handle-compatible serialized cleanup, proved payload ownership, dispatch/cancel linearization and generation-safe slot recycling.
- **0.48.4** — versioned acquisition and reacquisition-memory snapshot profile after scheduler integration, with expiry, remapping and independent freshness evidence.
- **0.49.0** — SIMD dispatch boundary with reference equivalence tests.
- **0.50.0** — SDR deployment/band planner and complete capability errors.
- **0.50.1** — sealed DSP plan receipt, scratch layout, throughput/latency budget and matching-block enforcement.
- **0.50.2** — independent signal/message vector admission gate required before each constellation implementation.
- **0.50.3** — side-effect-free front-end preparation, linear pre-submission/transport state, control-lease-bounded proofs, coherent transactions and safe reads.

### Phase D — GPS end-to-end

- **0.51.0** — GPS L1 C/A code generation and test vectors.
- **0.52.0** — GPS L1 C/A acquisition.
- **0.53.0** — GPS L1 C/A tracking and observables.
- **0.54.0** — GPS LNAV parity/frame/subframe decode.
- **0.54.1** — bounded multi-page assembly and atomic navigation-store transactions.
- **0.54.2** — versioned tracking-channel and raw page-assembly snapshot profiles with compatibility, provenance and calibration restore checks.
- **0.55.0** — GPS LNAV ephemeris, almanac, UTC and ionosphere.
- **0.55.1** — versioned semantic navigation-store/ephemeris snapshot profile with issue, model, health, validity and assessment invalidation checks.
- **0.56.0** — satellite state and clock computation.
- **0.57.0** — pseudorange formation and transmit-time iteration.
- **0.58.0** — standalone GPS weighted least-squares PVT.
- **0.58.1** — typed solver covariance, rank/condition/non-finite checks and explicit unavailable events.
- **0.59.0** — Doppler velocity and receiver clock drift.
- **0.59.1** — recorded-I/Q-to-PVT independent receiver, resource and input-panic audit.
- **0.60.0** — GPS L2C codes, acquisition and tracking.
- **0.61.0** — GPS CNAV decode.
- **0.62.0** — GPS L5 acquisition/tracking.
- **0.63.0** — GPS L5 CNAV and signal corrections.
- **0.64.0** — GPS L1C acquisition/tracking.
- **0.65.0** — GPS CNAV-2.
- **0.66.0** — GPS multi-frequency combinations and consistency.

### Phase E — Galileo

- **0.67.0** — Galileo E1 code generation/acquisition.
- **0.68.0** — Galileo E1 tracking and secondary-code synchronization.
- **0.69.0** — Galileo I/NAV page/FEC decode.
- **0.70.0** — Galileo ephemeris, clock, health, GST/UTC.
- **0.71.0** — Galileo E5a acquisition/tracking.
- **0.72.0** — Galileo F/NAV.
- **0.73.0** — Galileo E5b acquisition/tracking and I/NAV path.
- **0.74.0** — Galileo AltBOC component and full-band processing.
- **0.75.0** — Galileo E6 acquisition/tracking.
- **0.76.0** — Galileo HAS message and correction model.
- **0.77.0** — Galileo SAR/RLS public message support.
- **0.78.0** — Galileo Timing Service Message.
- **0.79.0** — Galileo EWSS/public emergency-message support.
- **0.80.0** — Galileo E5 quasi-pilot/current new-signal additions.

### Phase F — GLONASS

- **0.81.0** — GLONASS FDMA band/channel planner.
- **0.82.0** — GLONASS L1OF acquisition/tracking.
- **0.83.0** — GLONASS L1OF navigation strings and time.
- **0.84.0** — GLONASS orbit/clock computation.
- **0.85.0** — GLONASS L2OF acquisition/tracking and navigation.
- **0.86.0** — GLONASS FDMA observation/bias model.
- **0.87.0** — GLONASS L1OC public CDMA signal.
- **0.88.0** — GLONASS L2OC public CDMA signal.
- **0.89.0** — GLONASS L3OC public CDMA signal.
- **0.90.0** — mixed FDMA/CDMA solution validation.

### Phase G — BeiDou

- **0.91.0** — BeiDou B1I acquisition/tracking.
- **0.92.0** — BeiDou D1/D2 navigation and GEO/IGSO/MEO handling.
- **0.93.0** — BeiDou time, orbit and clock computation.
- **0.94.0** — BeiDou B2I and B3I public signal paths.
- **0.95.0** — BeiDou B1C acquisition/tracking.
- **0.96.0** — BeiDou B-CNAV1.
- **0.97.0** — BeiDou B2a acquisition/tracking.
- **0.98.0** — BeiDou B-CNAV2.
- **0.99.0** — BeiDou B2b acquisition/tracking.
- **0.100.0** — BeiDou B-CNAV3/basic navigation.
- **0.101.0** — BeiDou B2ab combined processing.
- **0.102.0** — BeiDou PPP-B2b correction service.
- **0.103.0** — public BDSBAS interfaces.
- **0.103.1** — public BeiDou SAR/short-message profile freeze with implementation only where a stable open interoperable specification exists.

### Phase H — QZSS, NavIC and SBAS

- **0.104.0** — QZSS L1 family and regional geometry.
- **0.105.0** — QZSS L2C/L5.
- **0.106.0** — QZSS L1S and SLAS.
- **0.107.0** — QZSS L5S public augmentation path.
- **0.108.0** — QZSS L6 acquisition/tracking.
- **0.109.0** — QZSS CLAS correction decode.
- **0.110.0** — QZSS MADOCA/MADOCA-PPP public profiles.
- **0.111.0** — NavIC L5 SPS.
- **0.112.0** — NavIC S-band SPS.
- **0.113.0** — NavIC L1 SPS.
- **0.114.0** — NavIC time/orbit/clock and multi-band solution.
- **0.114.1** — SBAS L1 code generation, acquisition, tracking and bounded GEO search.
- **0.114.2** — conditional public NavIC messaging profile freeze with lawful-document admission, privacy boundaries and explicit unavailable non-claims.
- **0.115.0** — generic legacy SBAS L1 framing/messages.
- **0.116.0** — SBAS correction/degradation state machine.
- **0.117.0** — SBAS integrity and protection-level inputs.
- **0.118.0** — DFMC SBAS signal/messages.
- **0.118.1** — complete DFMC code, acquisition, tracking, symbol/FEC, frame, correction, GEO mode and message acceptance matrix.
- **0.119.0** — provider profiles and future-ID registry.
- **0.119.1** — public GBAS/ABAS data-model, applicability and integrity-interface boundary.
- **0.119.2** — exact WAAS, EGNOS, MSAS, GAGAN, SDCM, BDSBAS, KASS, SouthPAN and African SBAS provider/service profile matrix.

### Phase I — Multi-GNSS solution quality

- **0.120.0** — multi-constellation PVT and inter-system biases.
- **0.120.1** — named solver state/covariance layout and explicit solution availability lifecycle.
- **0.120.2** — typed DOP, solution-age, satellite-summary, fix-kind and convergence outputs.
- **0.120.3** — typed residual, exclusion and measurement-contribution diagnostics.
- **0.120.4** — complete PVT initializer, state-mode and measurement-weighting acceptance matrix.
- **0.121.0** — robust estimation and fault exclusion.
- **0.121.1** — square-root filtering and near-singular numerical failure evidence.
- **0.121.2** — sequential GNSS-only PVT estimator with explicit initialization, reset and convergence lifecycle.
- **0.122.0** — broadcast ionosphere/troposphere model suite.
- **0.123.0** — dual/multi-frequency combinations and TEC.
- **0.124.0** — carrier smoothing and multipath metrics.
- **0.124.1** — optional `navheim-science` artifact, calibration, sampled-window, gap and batch-provenance foundation.
- **0.124.2** — amplitude/phase scintillation and S4-style metrics with lock, detrending, bandwidth and validity attribution.
- **0.124.3** — direct/reflected observable and GNSS reflectometry geometry, surface-delay and uncertainty artifacts.
- **0.124.4** — calibrated GNSS space-weather and remote-sensing outputs with explicit scientific-product non-claims.
- **0.125.0** — antenna phase-center and phase-wind-up models.
- **0.126.0** — Earth rotation, tides and reference-frame transforms.
- **0.126.1** — geoid/vertical-datum models and typed orthometric-height results.
- **0.127.0** — RAIM.
- **0.127.1** — RAIM hypotheses, risk allocation, solution separation, alert, continuity and exclusion contract.
- **0.128.0** — ARAIM building blocks and assumptions API.
- **0.128.1** — ARAIM constellation/common-mode hypotheses, correlation, service-health and availability contract.
- **0.129.0** — protection levels and integrity event model.
- **0.129.1** — immutable targeted integrity assessments, exclusions and recovery lifecycle.
- **0.129.2** — SBAS integrity-input separation and unavailable-protection-level semantics.
- **0.129.3** — code-differential corrections, reference-station geometry and common-view epoch matching.
- **0.129.4** — DGPS solution, covariance, correction-age and quality propagation.
- **0.129.5** — PVT fact and integrity-assessment pipeline separation.

### Phase J — RTK and precise positioning

- **0.130.0** — carrier-phase epoch model and slip detectors.
- **0.131.0** — base/rover synchronization and single differences.
- **0.132.0** — double-difference baseline filter.
- **0.133.0** — native integer ambiguity search.
- **0.134.0** — ambiguity validation and partial fixing.
- **0.135.0** — RTK fixed/float lifecycle and rollback.
- **0.135.1** — explicit RTK convergence artifacts, withdrawal and superseded-state handling.
- **0.135.2** — explicit RTK fixed/float, DGPS, standalone and unavailable transition policy.
- **0.135.3** — RTK pivot, fix-and-hold, ratio, success-probability and residual acceptance matrix.
- **0.136.0** — GLONASS FDMA RTK biases.
- **0.137.0** — moving-base and dual-antenna heading.
- **0.138.0** — network RTK standardized inputs.
- **0.138.1** — exact standardized VRS, FKP, MAC and MAX network-RTK profile matrix separated from proprietary extensions.
- **0.139.0** — RTCM SSR complete public baseline.
- **0.139.1** — atomic SSR group completeness, expiry and correction-session anti-mixing.
- **0.140.0** — IGS SSR profile.
- **0.141.0** — post-processed PPP.
- **0.142.0** — real-time PPP.
- **0.142.1** — PPP convergence, product/frame/age validation, rollback and invalidation.
- **0.143.0** — PPP ambiguity resolution.
- **0.144.0** — PPP-RTK regional atmosphere/bias models.
- **0.144.1** — PPP tide/loading, wet-delay/gradient and meteorological-input acceptance matrix.
- **0.144.2** — complete PPP state-layout, observation-combination, bias, interpolation, discontinuity, convergence and rollback matrix.
- **0.144.3** — versioned admitted PPP state snapshot/restore profiles with product, bias, frame, calibration, expiry and independent authenticity/confidentiality/freshness evidence.
- **0.145.0** — static/rapid-static survey workflow.

### Phase K — Authentication and resilience

- **0.146.0** — cryptographic backend traits and trust-store model.
- **0.146.1** — trusted-time, trust-root generation and platform anti-rollback authority binding.
- **0.146.2** — reviewed `navheim-crypto-rustcrypto` primitive/backend conformance.
- **0.147.0** — Galileo OSNMA framing/assembly.
- **0.148.0** — OSNMA key-chain and tag verification.
- **0.149.0** — OSNMA policy, renewal/revocation and evidence.
- **0.149.1** — immutable delayed-authentication assessments targeting existing artifacts.
- **0.150.0** — QZSS QZNMA decode and verification.
- **0.150.1** — RustCrypto-backed OSNMA/QZNMA end-to-end integration vectors.
- **0.151.0** — multi-constellation navigation conflict detector.
- **0.152.0** — Doppler/motion/clock spoofing evidence.
- **0.153.0** — correlation/power/interference evidence.
- **0.154.0** — meaconing/time-replay evidence.
- **0.155.0** — caller-provided multi-receiver and multi-antenna security evidence inputs without claiming native direction production.
- **0.155.1** — complete spoofing/jamming evidence and insufficient-data acceptance matrix.
- **0.156.0** — security policy engine and fail/degrade reactions.
- **0.156.1** — versioned targeted policy decisions, hysteresis and ordered reevaluation.
- **0.157.0** — signed forensic provenance stream.
- **0.157.1** — sensitive forensic sinks, routine telemetry privacy and scoped correlation identifiers.

### Phase L — Timing, fusion and navigation

- **0.158.0** — all GNSS time-scale conversions, UTC models and leap provenance.
- **0.158.1** — reason-bearing time availability and explicit capture-domain/generation stamps.
- **0.159.0** — external PPS/time-mark semantic correlation and calibrated-delay model.
- **0.159.1** — bounded named delay/uncertainty contributions, confidence semantics and correlation groups.
- **0.160.0** — validated time-only solution and stable GNSS timing observation/event API.
- **0.160.1** — caller-provided bounded event slots and maximum event/queue resource contract.
- **0.160.2** — timing event-slot ownership, borrowing, release and idempotent acknowledgement state machine.
- **0.161.0** — satellite/receiver clock estimates and GNSS timing uncertainty budget.
- **0.162.0** — GNSS timing freshness, discontinuity, outage and explicit invalidation.
- **0.162.1** — targeted withdrawal sequence, acknowledgement, queue-pressure and forced-resynchronization behavior.
- **0.163.0** — authenticated/integrity-aware GNSS time evidence and consumer policy inputs.
- **0.163.1** — common-view/all-in-view GNSS time-transfer results and CGGTTS V2E interoperability.
- **0.164.0** — inertial mechanization.
- **0.164.1** — IMU bias, scale-factor, axis-misalignment, noise and temperature models.
- **0.164.2** — coning/sculling compensation plus gravity, Earth-rate and transport-rate models.
- **0.165.0** — error-state EKF.
- **0.165.1** — lever-arm and sensor time-offset calibration states.
- **0.165.2** — square-root real-time fusion variant with numerical equivalence evidence.
- **0.165.3** — bounded vector-tracking implementation with scalar loop fallback and observable discontinuities.
- **0.166.0** — wheel/barometer/magnetometer inputs.
- **0.166.1** — zero-velocity, known-motion and non-holonomic constraint updates.
- **0.167.0** — delayed/out-of-sequence fusion.
- **0.167.1** — bounded delayed queues, deterministic update order and sensor clock/reset generations.
- **0.167.2** — allocated factor-graph interface sharing canonical fusion artifacts.
- **0.168.0** — GNSS outage/dead-reckoning lifecycle.
- **0.168.1** — GNSS reacquisition smoothing with explicit correction and discontinuity artifacts.
- **0.168.2** — deterministic fixed-rate fusion output at caller epochs with bounded interpolation, propagation, extrapolation, covariance growth and stale/coasting states.
- **0.168.3** — versioned admitted fusion state snapshot/restore profiles with sensor/calibration/model identity, covariance validation, expiry and independent authenticity/confidentiality/freshness evidence.
- **0.169.0** — multi-antenna attitude.
- **0.169.1** — `navheim-geo` ellipsoidal geodesic, great-circle and rhumb primitive completion without navigation-policy duplication.
- **0.169.2** — `navheim-navigation` bounded waypoint, route and track models plus wrappers over `navheim-geo`.
- **0.169.3** — geofence boundary, altitude and time-window evaluation.
- **0.169.4** — local-frame navigation composition over `navheim-geo` ENU/NED/body transformations and explicit road-network-routing non-claim.
- **0.169.5** — calibrated multi-antenna angle-of-arrival and direction-consistency production with ambiguity, coherence, validity and expiry evidence.

### Phase M — Hardware, OS and assistance

- **0.170.0** — recorded-I/Q and virtual SDR source.
- **0.171.0** — Linux RTL2832U/E4000 reference backend.
- **0.172.0** — bladeRF adapter.
- **0.173.0** — USRP/UHD adapter.
- **0.174.0** — LimeSDR adapter.
- **0.175.0** — coherent multi-device clock/timestamp calibration.
- **0.175.1** — bounded FPGA/GPU/external-DSP FFT, channelizer, acquisition, candidate, correlator and tracking boundary plus GitHub-only `navheim-fpga` host/artifact contract.
- **0.176.0** — portable serial backend.
- **0.177.0** — native USB backend contracts and Linux implementation.
- **0.177.1** — isolated unsafe/sys boundary, reproducible bindings and ownership/alignment/unplug safety evidence.
- **0.178.0** — Windows WinUSB/COM/location implementation.
- **0.178.1** — Windows provider permission/mock/timestamp/accuracy metadata and no synthetic raw observations.
- **0.179.0** — macOS IOKit/serial/Core Location implementation.
- **0.179.1** — iOS Core Location OS-derived fix adapter with explicit raw-measurement non-claim.
- **0.180.0** — shared BSD serial, USB and socket I/O contracts.
- **0.180.1** — FreeBSD I/O implementation and fault matrix.
- **0.180.2** — OpenBSD I/O implementation and fault matrix.
- **0.180.3** — NetBSD I/O implementation and fault matrix.
- **0.180.4** — bounded device discovery, isolated probing, deterministic ranking and hotplug identity.
- **0.181.0** — gpsd protocol adapter.
- **0.182.0** — u-blox UBX adapter.
- **0.183.0** — Septentrio SBF adapter.
- **0.184.0** — NovAtel/public receiver adapter baseline.
- **0.185.0** — receiver-protocol admission gate; every additional protocol requires a named patch milestone.
- **0.185.1** — canonical assistance artifact, trust, freshness, rollback and translation model.
- **0.185.2** — generic NMEA-only, RTCM, RINEX and canonical raw-observation receiver/source adapters.
- **0.185.3** — evidence-gated SkyTraq, SiRF, MediaTek/PMTK, Trimble and other public receiver profile matrix and admitted adapters.
- **0.185.4** — capability-gated receiver control with side-effect-free plans, allowlisted commands, ACK/NAK correlation, transition recovery and read-back transaction evidence.
- **0.185.5** — receiver-configuration generation barrier with effective intervals, queue draining, targeted invalidation, correction rebinding and persistent-command authorization.
- **0.185.6** — receiver control transactions separated from interval-scoped `ObservedConsistent` configuration assessments and receiver-asserted fallback.
- **0.186.0** — Android raw GNSS observation-fact adapter without assistance translation.
- **0.186.1** — Android fused/location-provider fix adapter and provenance.
- **0.186.2** — Android USB-host lifecycle, permission and detach-safe I/O.
- **0.186.3** — Android network, background, throttling and provider-reset integration.
- **0.186.4** — Android-to-canonical-assistance translation.
- **0.186.5** — bounded first-party aligned/unaligned ASN.1 PER core.
- **0.187.0** — OMA SUPL/ULP core.
- **0.187.1** — exact SUPL/ULP message, role and PER profile matrix.
- **0.188.0** — 3GPP LPP assistance core.
- **0.188.1** — exact LPP message, assistance and PER profile matrix.
- **0.189.0** — Rustls network adapter and secure credential policy.
- **0.189.1** — non-clone secret types, redacted diagnostics and reviewed zeroization boundary.
- **0.189.2** — canonical protected-snapshot binding, bounded recovery matrix and narrowly authorized exact-recovery-or-continuity-break repair contract.
- **0.189.3** — Linux/BSD protection/persistence profile with transactional freshness, optional repair/anti-revival evidence and no-universal-keystore non-claim.
- **0.189.4** — Windows snapshot-protection adapter with exact transactional, optional repair/anti-revival and honest weaker-capability evidence.
- **0.189.5** — Apple macOS/iOS snapshot-protection adapter with exact Keychain/crypto transactional, optional repair/anti-revival and honest weaker-capability evidence.
- **0.189.6** — Android snapshot-protection adapter with exact Keystore transactional, optional repair/anti-revival and honest weaker-capability evidence.
- **0.190.0** — NMEA 2000 transport/legal PGN baseline.
- **0.190.1** — bounded J1939 address-claim state machine, fast-packet and licensed PGN semantics.
- **0.190.2** — CAN frame I/O executing protocol decisions with platform lifecycle ownership.
- **0.190.3** — GitHub-only tool workspace, privilege, secret, privacy, configuration and `publish = false` enforcement foundation.
- **0.190.4** — `navheim-cli` inspect, convert, solve, record and replay workflows.
- **0.190.5** — `navheimd` local daemon, bounded IPC/management and least-authority service lifecycle.
- **0.190.6** — `navheim-caster` NTRIP caster deployment with authenticated tenant/session isolation.
- **0.190.7** — `navheim-station` reference/base-station service with survey, correction and continuity evidence.
- **0.190.8** — `navheim-survey` field and post-processing survey application.
- **0.190.9** — `navheim-inspector` bounded message/signal diagnostic TUI.
- **0.190.10** — `navheim-viewer` desktop/web visualization with precise-location and provenance privacy controls.
- **0.190.11** — `navheim-lab` conducted/shielded robustness experiment controller with transmit-safety interlocks.

### Phase N — Simulation, hardening and 1.0 stabilization

- **0.191.0** — synthetic navigation-message generators.
- **0.192.0** — scalar baseband signal generator for all implemented open signals.
- **0.193.0** — dynamics, atmosphere, multipath and clock scenario engine.
- **0.194.0** — controlled interference/jamming scenario generation.
- **0.195.0** — controlled spoofing/meaconing scenario generation.
- **0.196.0** — cross-constellation full replay suite.
- **0.196.1** — `navheim-sim` high-level scenario and signal-generation tool composition.
- **0.196.2** — external `navheim-data` capture/vector manifest, object-integrity, access and retention contract.
- **0.197.0** — long-duration resource-leak and rollover suite.
- **0.198.0** — full parser fuzz corpus and coverage audit.
- **0.198.1** — differential/chunk-boundary parser corpus and sensitive diagnostic snapshot audit.
- **0.198.2** — GitHub-only `navheim-fuzz` target/corpus lifecycle and reproducibility harness.
- **0.198.3** — GitHub-only `navheim-conformance` standards/vector test runner.
- **0.199.0** — numerical condition/precision audit.
- **0.199.1** — fixed/floating cross-architecture replay and tolerance audit.
- **0.200.0** — unsafe/FFI audit and device fault injection.
- **0.200.1** — Miri/Kani/Loom/sanitizer evidence-role and generated-code provenance audit.
- **0.201.0** — stable-Rust cross-architecture SIMD performance release with scalar fallback.
- **0.201.1** — GitHub-only `navheim-bench` performance, resource and regression harness.
- **0.202.0** — fixed-point/embedded performance release.
- **0.203.0** — WASM decoding/post-processing profile.
- **0.203.1** — bare-metal and future Aesynx caller-buffer/work-budget conformance contract.
- **0.204.0** — API naming and visibility freeze.
- **0.205.0** — configuration/profile freeze.
- **0.206.0** — file/wire round-trip compatibility freeze.
- **0.207.0** — all-platform CI and hardware farm release.
- **0.207.1** — MSRV behavioral core test suite and allocator-free target evidence.
- **0.208.0** — independent receiver comparison campaign.
- **0.209.0** — multi-band live-sky and simulator evidence release.
- **0.210.0** — standards inventory refresh and 1.0 baseline freeze.
- **0.210.1** — exact document/amendment/module/vector/adversarial-test traceability closure.
- **0.210.2** — complete architecture requirement, public claim, crate/tool owner, milestone, test and non-claim traceability closure.
- **0.211.0** — complete public-signal coverage audit.
- **0.212.0** — complete correction/format/assistance coverage audit.
- **0.213.0** — complete security/integrity/timing audit.
- **0.214.0** — documentation, examples and migration audit.
- **0.214.1** — capability-tier, side-effect, resource, privacy and failure-contract documentation audit.
- **0.215.0** — external security audit fixes.
- **0.216.0** — external GNSS/domain review fixes.
- **0.217.0** — 1.0.0 release candidate 1.
- **0.218.0** — release candidate 2 and only blocker fixes.
- **0.219.0** — final reproducibility, packaging and provenance rehearsal.
- **0.219.1** — GitHub-only packages, service units, containers and deployment configuration security/reproducibility freeze.
- **1.0.0** — frozen, documented and independently tested public civil/open GNSS/PNT platform.

The exact number may change, but features should not be collapsed merely to reach 1.0 sooner.

---

## 27. Definition of done for 1.0.0

Navheim 1.0.0 is released only when all of the following are true:

1. Every public civil/open signal in the frozen GPS, Galileo, GLONASS, BeiDou, QZSS, NavIC and SBAS baseline has a standards mapping.
2. Every promised signal has code generation/acquisition/tracking, navigation
   decode and observation evidence where applicable, with official plus
   independent or externally sourced vectors admitted alongside it.
3. Restricted signals are clearly labeled and never falsely decoded.
4. Multi-GNSS PVT, RTK, PPP, integrity, timing, authentication and complete
   fusion paths have independent test evidence and typed failure states.
5. NMEA, RTCM/NTRIP, every promised RINEX file profile and principal IGS/Earth
   orientation product support match the frozen public/licensed baselines.
6. No foundational, constellation, solver or format crate depends on another GNSS implementation.
7. Core crates build under `no_std`; heap and OS dependencies are explicit.
8. TLS and cryptographic primitives are isolated in audited adapters.
9. All untrusted parsers are fuzzed and have bounded resource behavior.
10. Every public API documents units, frames, time scales, validity and failure behavior.
11. Linux, Windows, macOS and the BSD targets pass their supported I/O test matrices; Android and WASM profiles are documented.
12. The project has repeated live-sky, recorded-capture, shielded-simulator and independent-receiver comparisons.
13. The project has completed external security and GNSS-domain reviews.
14. The standards manifest and legal-material policy are complete.
15. The facade can serve a beginner while lower crates expose every advanced stage.
16. There is no silent degradation: capabilities, exclusions, authentication and integrity are visible.
17. The 1.0 compatibility policy and deprecation process are published.
18. `navheim-geo` owns all coordinate/geodesic/frame mathematics;
    `navheim-navigation` depends on it for route/track, geofence, segment and
    local-frame composition and clearly excludes road routing.
19. Canonical assistance prevents rollback/cross-session mixing before SUPL,
    LPP, Android or receiver translation.
20. PVT exposes typed DOP, age, satellite, residual, exclusion, fix,
    convergence and vertical-datum outputs; unavailable values remain explicit.
21. Deterministic `no_std` math covers every required operation with published
    error bounds, MSRV evidence and no nightly or implicit OS-math dependency.
22. Code DGPS has independent evidence and cannot be confused with RTK float;
    every fixed/float/DGPS/standalone/unavailable transition is observable.
23. Every facade profile expands canonically, and discovery/probing/source
    ranking remains bounded, explainable, disabled/allowlisted and side-effect
    free until explicit open.
24. Android location/USB/network and SUPL/LPP PER matrices meet their named
    platform, provenance, lifecycle, interoperability and resource contracts.
25. Common-view and all-in-view GNSS time transfer produces independently
    verified, provenance-rich results and interoperates with the frozen CGGTTS
    V2E profile without performing generic clock discipline or consensus.
26. Every admitted SBAS provider has an exact service-definition,
    applicability, message/profile and test matrix; named providers that
    cannot be implemented from lawful current material remain explicit
    unsupported profiles rather than inferred equivalents.
27. BeiDou SAR or short-message behavior is implemented only from a stable
    public interoperable specification; otherwise identifiers and an explicit
    unavailable/non-claim outcome are preserved.
28. NMEA-only, RTCM, RINEX and raw-observation sources share canonical
    adapters, while every vendor receiver profile is tied to official
    documentation, exact hardware/firmware and independent hardware evidence.
29. Every named GitHub-only tool has its own bounded release stop, remains
    `publish = false`, uses least authority, protects precise location/time and
    secrets, and cannot bypass canonical validation or policy.
30. FPGA and external-DSP inputs cross a versioned bounded interface with
    timestamp, calibration, firmware/bitstream, device and scalar-equivalence
    provenance; no accelerator output is trusted implicitly.
31. Every architecture requirement and public claim maps bidirectionally to
    an owning crate or GitHub-only component, release milestone, authoritative
    source, verification evidence, current status and explicit non-claim.
32. All hand-maintained Rust, Python and shell code anywhere in the repository
    remains at or below 500 lines, and every publishable package has its own
    package README while GitHub-only components avoid duplicate crate-style
    documentation.
33. MIT and Apache-2.0 license notices, package metadata, documentation,
    archives and published artifacts consistently identify Navheim.
34. Every resource claim is explicitly classified as exact structural
    evidence, a target/toolchain/profile-specific static upper bound, a work
    bound, a measured envelope, a caller assumption or unavailable; portable
    APIs never overstate stack, throughput or latency certainty.
35. A machine-readable acyclic crate/capability graph covers normal, optional,
    build and development edges, feature unification, tier, `alloc`, `std`,
    unsafe, TLS and cryptography, and rejects undeclared privilege escalation.
36. Projected coordinates and derived kinematics have explicit frame, datum,
    epoch, units, covariance, boundary behavior and unavailable-state tests.
37. Fixed-rate fusion output never invents GNSS freshness and has bounded,
    tested propagation, interpolation, extrapolation, latency, covariance
    growth, reset, stale and coasting semantics.
38. Optional science APIs preserve raw observations, calibration, lock,
    sampling, windows, gaps, provenance and uncertainty, and distinguish
    research metrics from validated operational products.
39. NavIC messaging, DFMC, every named SBAS provider including SouthPAN,
    standardized network RTK and every PPP state/product mode are governed by
    exact acceptance matrices and explicit unsupported cells.
40. External decoders, algorithms and accelerators declare capabilities and
    resource limits before execution, cannot bypass canonical correctness or
    trust policy, and prove deterministic reset, invalidation, scalar
    equivalence and fallback behavior where applicable.
41. Caller-provided angle/direction evidence remains distinguished from the
    native calibrated multi-antenna producer, whose ambiguity, coherence,
    validity and expiry are independently tested.
42. All solver/filter linear algebra uses bounded, independently verified
    factorizations with dimension, scratch, rank, condition, definiteness,
    finiteness and badly scaled failure evidence; production least squares
    never relies on unqualified normal-equation inversion.
43. Statistical kernels publish validated domains and approximation bounds;
    integrity/protection thresholds use conservative rounding and cannot
    become permissive because of numerical error.
44. Artifact/provenance IDs have non-reusing namespace/generation/sequence,
    exhaustion, renewal, import/remap, serialization, collision, parent and
    privacy semantics; navigation selection records all candidates and never
    uses ambient latest-wins behavior.
45. Canonical versioned signal definitions expose frequency, wavelength,
    rates, components, modulation and native-time metadata once, while each
    format mapping is versioned and round-trippable without duplicating the
    physical table.
46. Early acquisition hints are dependency-free, bounded, expiring and
    provenance-rich; every work reduction is receipted, conflicting hints
    fall back safely, and no hint resolves time, position or trust.
47. `navheim-linalg` depends only on `navheim-math`, carries no third-party
    dependency, and neither duplicates scalar math nor calls platform math.
48. Immutable `PlanReceipt` records maximum execution bounds, while each
    dynamic acquisition choice produces a separate immutable decision receipt
    with hints, actual work, fallback and deterministic order; the receipt
    schema precedes acquisition, but executable receipt and snapshot tests do
    not claim state before its owning acquisition/scheduler milestones.
49. UTC civil/calendar, POSIX ambiguity/loss, leap insertion/deletion,
    Gregorian/ordinal/Julian/MJD, TT and EOP-derived UT1 semantics are fully
    typed, model-versioned and boundary-tested; Julian/MJD is integer-day plus
    exact fraction/rational under frozen range/BCE rules, and leap smear is a
    non-claim.
50. Core owns signal contracts, constellation crates own physical fragments,
    format crates own versioned wire mappings, and facade composition creates
    no dependency inversion or forced all-constellation graph.
51. Tier 0 remains thread-free; Tier 2 multicore execution and runtime source
    supervision preserve separate scoped-borrowed and owned-handle modes,
    `#[must_use]` handles, explicit join/cancel-and-join/terminal-result APIs,
    authoritative pre-dispatch registry ownership independent of destructors,
    generation-safe IDs and atomic vacant/registered dispatch-or-cancel/
    running/terminal-unclaimed/claimed/discarded/shutdown-reclaimed/cleaning
    transitions, permanent retirement or namespace renewal at generation
    exhaustion, non-reusable forgotten-handle entries, exact observing versus
    consuming result APIs, destructor-free handle Drop, sealed bounded cleanup
    with caller-driven budgeted progress, no hidden reaper or implicit
    admission cleanup, shared-borrow progress usable beside live handles,
    internal non-exported single-cleaner CAS, pre-mutation busy result, bounded
    lowest-JobId selection, explicit cleanup-required backpressure, must-use
    executor lifecycle, process-terminal panic/failure/reentrancy, safe-only
    payload ownership with unsafe extraction excluded from 1.0,
    Miri/Loom/Kani exactly-once evidence, slot reuse only after
    result/lease/trace finalization, shutdown
    coverage of every orphan, concrete allocation-free/non-unwinding
    `std::process::abort()` on invalid handle/executor destruction, best-effort
    non-durable pre-abort diagnostics, explicit lease states, deterministic
    logical ordering, cooperative cancellation, unresponsive ownership,
    lossless bounded runtime traces, scalar verification, source roles, valid
    cross-role composition, solver-state-safe same-role handover, withdrawal
    and caller-authorized no-downgrade failover.
52. Receiver control is separate from read-only parsing and uses only planned
    allowlisted typed commands with firmware capabilities, ACK/NAK,
    idempotency, configuration generations, transition queue draining,
    invalidation/rebinding, volatile/persistent/destructive authority,
    flash-wear budgets, receiver-asserted read-back and separately invalidated
    interval-scoped `ObservedConsistent` behavioral assessments.
53. Snapshot/restore is opt-in, versioned, bounded, atomic and provenance-
    remapped; authenticity, confidentiality and freshness are orthogonal,
    unkeyed digests imply only corruption detection, external authentication
    establishes authenticated bytes, external encryption protects sensitive
    bytes, only trusted external monotonic comparison and advancement
    establishes rollback resistance, counter-checked evidence never implies
    guaranteed freshness,
    rollback-resistant sealing uses a distinct suite-approved, domain-
    separated `SnapshotTransactionBinding` over the exact canonical protected
    envelope—not corruption/artifact digests and excluding its sidecar self—
    with durable pending reservation, complete-envelope binding, staged
    candidate, authority commit, durable promotion and finalization in that
    order; recovery is exclusive against new writers at every crash point,
    post-authority promotion failure is pending/unavailable rather than
    success, committed/pending/authority-committed/promoted-unfinalized/
    corrupt-or-unknown states have one explicit restore/writer/action matrix,
    each namespace bounds transactions, candidates, retained bytes, retries
    and cleanup, cancellation/supersession cleanup is deterministic and cannot
    delete authoritative unresolved state, corrupt/unknown repair is a
    separate Tier 3 capability limited to exact current-candidate recovery or
    durable namespace/key/counter retirement with a fresh-domain continuity
    break and anti-revival proof, never in-namespace counter reset, older
    restore, nonce reuse or freshness downgrade; repair emits security/
    invalidation evidence and forces reacquisition/reconvergence, all
    interpretive metadata is
    authenticated, nonce/key/rotation/
    counter state is crash-safe, platform adapters report unavailable freshness
    honestly, profiles are minimal/consent-bound, restored assessments are
    reverified/invalidated, correctly ordered state profiles pass uninterrupted
    equivalence, and every other algorithm reports restore unsupported.
54. `navheim-dsp` depends on `navheim-math`; `navheim-geo` depends on
    representation-only `navheim-core` plus `navheim-math`; neither duplicates
    platform/private math, `navheim-geo` owns ENU/NED/body transformations,
    `navheim-navigation` only composes them, and Tier 2 `navheim-executor`
    remains outside DSP.
55. Every SDR configuration is side-effect-free prepared and explicitly
    applied from an immutable plan; non-reusing front-end generations bind
    hardware, clocks, RF/sample/calibration state, `Applied` structurally
    carries bounded adapter/device transaction evidence,
    `RejectedNoMutation` requires an unconsumed framework-only pre-submission
    token plus exclusive control/no-autonomous-change evidence and proves only
    no Navheim command crossed the boundary, transport acquisition consumes
    that possibility, every other failure preserves its cause/evidence,
    uncertainty/evidence overflow becomes state-unknown, partial/unknown
    application retires state and blocks reads, coherent group transactions
    expose every device result without implying independent consistency and
    revalidate calibration, transitions invalidate stale samples/mappings/DSP,
    and reads expose only initialized samples with gaps, overruns and progress
    state.

---

## 28. Recommended first implementation sequence with your equipment

While the architecture targets the complete laboratory, start development in this order:

1. Create `navheim-core`, the standards manifest and security policy.
2. Implement integer time, units, deterministic `no_std` math, bit access and
   bounded parsing.
3. Build the RTL2832U sample source and a deterministic capture format.
4. Implement scalar complex DSP, resampling and FFT.
5. Implement GPS L1 C/A acquisition against generated and recorded vectors.
6. Add tracking loops and observables.
7. Decode LNAV and compute satellite states.
8. Produce the first standalone GPS fix.
9. Add RINEX/NMEA/RTCM interoperability around the same canonical model.
10. Buy the B210/xA9 and full-band antenna before modern multi-band tracking work.
11. Add Galileo E1 and BeiDou B1, then GLONASS L1.
12. Add the lower/middle bands and reference receivers.
13. Build RTK/PPP/authentication only after observation time/phase correctness is proven.
14. Add S-band and full simultaneous hardware near the final signal-coverage phases.

This produces useful releases early without changing or shrinking the final design.

---

## 29. Final architectural principles

1. **Protocol correctness before convenience.**
2. **Canonical observations before constellation-specific solvers.**
3. **No hidden allocation, threads, networking or degradation.**
4. **`no_std` at the mathematical and protocol core.**
5. **No external GNSS implementation dependencies.**
6. **Do not reinvent TLS or cryptographic primitives.**
7. **Authentication, signal authenticity and integrity are different.**
8. **Every result has units, time scale, reference frame, uncertainty and provenance.**
9. **Unknown future IDs are preserved, not rejected by closed enums.**
10. **One monorepo, separately publishable stable library crates.**
11. **Binaries, test laboratories and large data stay GitHub-side until stable.**
12. **Every release is small enough to threat-model, fuzz and pentest.**
13. **1.0 means all publicly documented civil/open coverage—not classified promises.**
14. **The beginner API is simple because the lower layers are rigorously designed, not because important state is hidden.**
15. **Navheim determines GNSS time; consumer-owned adapters decide how to use
    it and never become Navheim dependencies.**

Navheim can become unusually valuable because it would join layers that are normally fragmented: raw SDR, receiver protocols, precise positioning, timing, authentication, integrity and portable Rust APIs. The strongest differentiator is not merely “written in Rust.” It is that the entire solution can explain **where each measurement came from, which standards governed it, how it was corrected, why it was trusted or rejected, and how it contributed to the final position or time result.**

---

## Appendix A — Authoritative source families to track

The standards manifest should continuously track at least:

- GPS.gov technical documentation and current interface specifications for L1 C/A, L1C, L2C and L5;
- EUSPA/EU Galileo OS SIS ICD, OSNMA, HAS, SAR, timing and service notices;
- GLONASS Information-Analytical Centre official ICD/document pages;
- China Satellite Navigation Office BeiDou SIS ICDs for B1I, B1C, B2a, B2b, B3I and PPP-B2b;
- Japan Cabinet Office QZSS interface specifications for PNT, SLAS, CLAS, MADOCA and QZNMA;
- ISRO NavIC SPS ICDs for L1, L5 and S bands;
- ICAO/RTCA/EUROCAE SBAS, GBAS and integrity material;
- RTCM 10403.x and 10410.x;
- NMEA 0183 and NMEA 2000;
- IGS RINEX, SP3, SINEX, IONEX, ANTEX and SSR standards;
- in-force ITU-R/IGS and other authoritative GNSS scintillation,
  reflectometry, space-weather and remote-sensing methods selected by the
  science-profile freeze;
- Netlib/LAPACK numerical stability and factorization references plus NIST
  DLMF probability/special-function definitions selected by the numerical
  profile freezes;
- OMA SUPL and 3GPP LPP;
- BIPM/CCTF CGGTTS V2E, current BDS-3 extensions and guidance, together with
  in-force ITU-R GNSS time-transfer terminology and recommendations;
- official Rust stable/MSRV documentation for `core` floating math,
  target-specific `core::arch` and portable-SIMD stabilization status;
- official Linux/BSD, Microsoft and Apple platform API/ABI documentation used
  by each admitted I/O adapter;
- official RTL-SDR, bladeRF, UHD/USRP, LimeSuite and FPGA/toolchain
  documentation tied to every supported hardware/firmware profile;
- official receiver protocol specifications used by adapters.

## Appendix B — Key 2026 research observations

- Galileo OSNMA entered initial service in July 2025, so authentication is no longer merely a future research option.
- QZNMA operational service began in 2024 and should be part of the security architecture.
- Galileo OS SIS ICD 2.2 was published in late 2025 and includes current open-signal evolution that must be represented in the standards baseline.
- RINEX 4.02 includes newer navigation-record coverage such as NavIC L1 and GLONASS CDMA additions.
- Current public QZSS specifications cover PNT, SLAS, CLAS, MADOCA-PPP and authentication services.
- The RTL2832U/E4000 device is a strong starter for L1 work, but a serious multi-band, coherent, timestamped SDR is required for complete implementation evidence.
