# GNSS Timing API and Consumer Boundary

Status: architectural contract; public names remain provisional until their
release milestones.

## Decision

Navheim determines time from satellite-navigation signals, navigation
messages, receiver protocols, corrections, and receiver timing outputs.
Navheim exposes the result as complete GNSS timing evidence.

Navheim does not depend on Mundilfari or any other clock framework. Mundilfari
or another consumer may depend on Navheim through a companion adapter and
decide how GNSS contributes to a larger clock system.

The dependency direction is strictly one way:

```text
navheim
   ↑
mundilfari-navheim
   ↓
mundilfari
```

`mundilfari-navheim` is an example consumer-owned crate, not a Navheim
workspace crate. Navheim must remain fully useful without it.

## Ownership

Navheim owns all GNSS-specific timing behavior:

- GPS, Galileo, GLONASS, BeiDou, QZSS, NavIC, and SBAS time fields and epochs;
- navigation-frame decoding and receiver-protocol decoding;
- native GNSS time scales, inter-system offsets, and transmitted UTC models;
- leap-second announcements carried by GNSS and their provenance;
- truncated-week, era, day, rollover, and stale-model resolution;
- satellite clock corrections and group/inter-signal delay corrections;
- receiver clock bias, drift, covariance, and time-only GNSS solutions;
- satellite, signal, message, and receiver health affecting time;
- OSNMA, QZNMA, and other applicable navigation-message authentication;
- spoofing, meaconing, jamming, replay, and inconsistent-time evidence;
- the meaning of receiver PPS/time-mark edges, 10 MHz/frequency outputs, and
  their message or receiver-state association;
- antenna, cable, receiver, quantization, and transport-delay contributions;
- common-view and all-in-view GNSS time-transfer primitives;
- uncertainty, integrity, freshness, validity, and provenance of GNSS time.

Navheim does not own generic clock-system behavior:

- NTP, NTS, PTP, radio-time, PHC, or system-clock protocols;
- generic PPS/frequency device capture, GPIO/serial edge timestamping, or
  frequency counting;
- comparison and consensus across unrelated clock-source families;
- local oscillator discipline, servo policy, or frequency steering;
- generic holdover after all GNSS evidence has expired;
- privileged adjustment of a system clock, PHC, or oscillator;
- the consumer's final trust policy for using GNSS as a clock source.

Navheim may report receiver oscillator and clock estimates because they are
part of interpreting GNSS observations. It must not turn those estimates into
privileged clock-control actions.

## No Duplicated GNSS Implementation

A consumer may have its own canonical atomic-time and UTC types. Its Navheim
adapter maps Navheim values into those types; it does not decode navigation
messages, resolve GNSS weeks, reinterpret receiver health, verify OSNMA, or
reconstruct PPS association.

Both sides may validate leap and offset information. Independent validation is
a security check, not permission to create a second partial GNSS decoder. Any
disagreement remains visible and prevents silent clock discipline.

## API Layers

Timing data progresses through explicit states:

1. `RawGnssTime` preserves fields exactly as received, including truncated or
   ambiguous values.
2. `ResolvedGnssTime` identifies a native scale and resolves the era only from
   explicit context and evidence.
3. `GnssTimeSolution` applies satellite and receiver clock models and produces
   a time-only or position/time solution with an uncertainty budget.
4. `GnssTimeObservation<C>` associates the solution with a caller-selected
   capture timestamp `C` and all security evidence.
5. `GnssTimeEvent<C>` reports observations, model changes, invalidations,
   ambiguity, discontinuity, gaps, and security alerts.

Raw, resolved, corrected, and accepted values are different types. A caller
cannot accidentally treat a raw receiver field as validated time.

## Provisional Observation Shape

The eventual API should provide the information represented by this
provisional shape. Fields should use checked constructors and read-only
accessors rather than unrestricted public construction.

```rust
pub struct GnssTimeObservation<C> {
    pub native: ResolvedGnssTime,
    pub tai: Option<TaiInstant>,
    pub utc: Option<ResolvedUtc>,
    pub captured_at: C,
    pub uncertainty: TimeUncertainty,
    pub receiver_clock: Option<ReceiverClockEstimate>,
    pub correlation: Option<PpsCorrelation>,
    pub frequency: Option<GnssFrequencyObservation<C>>,
    pub source: GnssTimeSource,
    pub health: GnssTimeHealth,
    pub authentication: TimeAuthentication,
    pub integrity: GnssTimeIntegrity,
    pub provenance: ProvenanceId,
}
```

`C` is opaque to Navheim's protocol core. It lets an adapter preserve the
consumer's monotonic timestamp domain without Navheim depending on that
consumer's time crate.

The stable API must expose at least:

- native system instant and scale;
- exact resolved atomic instant when resolution is possible;
- UTC realization, model identity, leap state, and source when available;
- asymmetric error bounds and named uncertainty contributions;
- capture clock domain and correlation state;
- constellation, signal, satellite, receiver, and message provenance;
- receiver clock bias/drift and covariance when estimated;
- navigation-data health and receiver timing validity;
- cryptographic authentication state;
- separate signal-source and solution-integrity evidence;
- freshness deadline and explicit invalidation reasons.

Absence is not validity. `Option` only means that a value is unavailable; an
explicit state explains whether it is unsupported, pending, ambiguous, stale,
rejected, or failed.

## Time Representations

Navheim provides its own dependency-free, exact representations:

- `GnssTimeScale` for native satellite-system scales and unknown future IDs;
- `GnssInstant` for an unambiguous native-scale instant;
- `TaiInstant` as the resolved continuous atomic result;
- `UtcRealization` and `ResolvedUtc` for explicit UTC mappings;
- `WeekResolution` and equivalent GLONASS day/era resolution evidence;
- `ReceiverClockEstimate` for bias, drift, reference epoch, and covariance;
- `TimeUncertainty` for bounds, contributors, and evidence quality.

There is no implicit conversion through Unix/POSIX time and no silent selection
of an era, leap table, UTC realization, or current wall clock. Unknown scales
and identifiers remain representable.

## PPS, Time Marks, and Frequency Outputs

Generic edge capture belongs outside Navheim's GNSS core. Navheim accepts a
bounded pulse event with an opaque capture timestamp and determines its GNSS
meaning:

```rust
pub struct PulseCapture<C> {
    pub captured_at: C,
    pub sequence: u64,
    pub edge: PulseEdge,
    pub capture_uncertainty: TimeUncertainty,
}

pub struct PpsCorrelation {
    pub represented_instant: GnssInstant,
    pub time_mark: Option<ReceiverTimeMark>,
    pub convention: PulseConvention,
    pub calibrated_delay: SignedNanoseconds,
    pub uncertainty: TimeUncertainty,
}
```

The concrete API must handle:

- leading/trailing-edge and beginning/end-of-second conventions;
- receiver message before/after pulse behavior;
- sequence gaps, duplicate pulses, reordered messages, and wraparound;
- receiver time-mark identifiers and message latency;
- antenna, cable, receiver, and capture delay with sign and provenance;
- quantization, sawtooth, and receiver time-pulse correction data;
- leap insertion/deletion boundaries and GNSS week/day rollover;
- pulse-without-valid-time and time-without-correlated-pulse states.

Navheim also exposes the GNSS meaning and reported quality of receiver
frequency outputs without capturing or steering them:

```rust
pub struct GnssFrequencyObservation<C> {
    pub nominal: Hertz,
    pub captured_at: C,
    pub receiver_error: Option<FrequencyError>,
    pub lock: FrequencyLockState,
    pub uncertainty: FrequencyUncertainty,
    pub provenance: ProvenanceId,
}
```

The API preserves receiver configuration, lock/discipline state, quantization
or sawtooth correction, calibrated output delay, reference epoch, validity,
and uncertainty when available. Generic counters, oscillators, servos, and
frequency-output control remain consumer-owned.

A Mundilfari adapter can obtain a pulse from its generic PPS implementation,
wrap or translate its monotonic timestamp into `C`, and feed the event into
Navheim's GNSS correlator. Navheim then returns the represented GNSS instant
and evidence; Mundilfari retains ownership of the physical capture and clock
policy.

## Source Trait

The adapter-facing source is deterministic, runtime-neutral, and allocation
free at the trait boundary:

```rust
pub trait GnssTimingSource {
    type Capture;
    type Error;

    fn poll_time(
        &mut self,
    ) -> Result<Option<GnssTimeEvent<Self::Capture>>, Self::Error>;
}
```

The final trait may use an explicit context or output slot to enforce resource
bounds. It must not choose an async runtime, spawn a thread, open an arbitrary
device, or perform a privileged clock change.

Events include invalidation and security transitions so a consumer cannot keep
using a formerly valid sample after Navheim detects stale UTC parameters,
authentication failure, a receiver reset, discontinuity, or spoofing evidence.

## Consumer Adapter Contract

A companion adapter:

1. consumes `GnssTimeEvent<C>`;
2. rejects unresolved, stale, unhealthy, or policy-disallowed observations;
3. converts Navheim's exact `TaiInstant` or native instant without truncation;
4. maps uncertainty bounds without turning them into false precision;
5. preserves capture-domain identity and PPS correlation;
6. preserves frequency-reference status and error without steering it;
7. preserves health, authentication, integrity, and provenance;
8. emits explicit withdrawal when Navheim invalidates prior evidence;
9. reports disagreements between Navheim and consumer time models.

The adapter must not collapse authentication, signal-source authenticity,
message correctness, and solution integrity into one trusted boolean.

## Security Invariants

- Receiver time, host wall time, and approximate user time are untrusted hints.
- Era/week resolution requires explicit context and reports all ambiguity.
- UTC or leap data is never accepted solely because a receiver emitted it.
- Freshness is checked at the navigation model, observation, PPS, and adapter
  boundaries.
- Every correction and delay has units, sign convention, validity, uncertainty,
  and provenance.
- Time discontinuities and backward steps become events, never normalization.
- Authentication success does not prove that an authentic signal was not
  delayed or rebroadcast.
- A consumer must be able to fail closed without parsing diagnostic strings.
- Serialization preserves unknown states and never upgrades trust.

## Verification Contract

Before the timing API is stable, tests must cover:

- every supported scale, epoch, rollover, and leap boundary;
- truncated-week resolution with absent, stale, conflicting, and malicious
  context;
- positive and negative cable/receiver delays and uncertainty accumulation;
- PPS/message reordering, omission, duplication, latency, and reset behavior;
- frequency-output lock loss, discontinuity, correction, and uncertainty;
- time-only solutions with unhealthy satellites and inconsistent systems;
- authenticated, pending, unavailable, failed, and revoked states;
- spoofing/meaconing/replay evidence and subsequent invalidation;
- adapter round trips using a foreign capture timestamp newtype;
- `no_std`, no-allocation, MSRV, serialization, and unknown-ID behavior;
- differential comparison with independent receivers and timing references.

The v1.0 API audit must include at least one independently implemented consumer
adapter. That adapter is test evidence for Navheim's public boundary, not a
dependency of Navheim or part of its crates.io publication graph.
