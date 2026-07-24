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
   capture timestamp `C` and GNSS timing facts.
5. Separate immutable correctness, authentication, signal-authenticity and
   integrity assessments target the observation's artifact ID.
6. `GnssTimeEvent<C>` reports artifacts, assessments, model changes, targeted
   invalidations, ambiguity, discontinuity, gaps, and security alerts.

Raw, resolved, corrected, and accepted values are different types. A caller
cannot accidentally treat a raw receiver field as validated time.

## Provisional Observation Shape

The eventual API should provide the information represented by this
provisional shape. Fields should use checked constructors and read-only
accessors rather than unrestricted public construction.

```rust
pub enum Availability<T, R> {
    Available(T),
    Pending(R),
    Unsupported(R),
    Ambiguous(R),
    Stale(R),
    Rejected(R),
    Failed(R),
}

pub struct CaptureStamp<C> {
    domain: CaptureClockDomainId,
    generation: CaptureGeneration,
    value: C,
}

pub struct GnssTimeObservation<C> {
    native: ResolvedGnssTime,
    tai: Availability<TaiInstant, TimeResolutionReason>,
    utc: Availability<ResolvedUtc, UtcResolutionReason>,
    captured_at: CaptureStamp<C>,
    uncertainty: TimeUncertainty,
    receiver_clock: Availability<ReceiverClockEstimate, ClockEstimateReason>,
    correlation: Availability<PpsCorrelation, CorrelationReason>,
    frequency: Availability<GnssFrequencyObservation<C>, FrequencyReason>,
    source: GnssTimeSource,
    health: GnssTimeHealth,
    provenance: ProvenanceId,
}
```

`C` remains opaque to Navheim's protocol core, while `CaptureStamp<C>` carries
the clock-domain identity and reset generation. Values from different domains
or generations cannot be ordered or subtracted without an explicit
consumer-provided mapping. This preserves foreign timestamp types without a
dependency on the consumer's time crate.

Authentication, signal authenticity and integrity are not fields of the
observation. They are immutable targeted assessments:

```rust
pub struct NavigationAuthenticationAssessment {
    target: ArtifactId,
    state: AuthenticationState,
    trust: AuthenticationProvenance,
}

pub struct IntegrityAssessment {
    target: ArtifactId,
    model: IntegrityModelId,
    bounds: IntegrityBounds,
    assumptions: BoundedAssumptions,
}
```

Delayed authentication or later integrity evidence adds an assessment event;
it does not mutate or silently upgrade an existing observation.

The stable API must expose at least:

- native system instant and scale;
- exact resolved atomic instant when resolution is possible;
- UTC realization, model identity, leap state, and source when available;
- asymmetric error bounds and named uncertainty contributions;
- capture clock domain and correlation state;
- constellation, signal, satellite, receiver, and message provenance;
- receiver clock bias/drift and covariance when estimated;
- navigation-data health and receiver timing validity;
- targeted cryptographic authentication assessments;
- separate targeted signal-source and solution-integrity evidence;
- freshness deadline and explicit invalidation reasons.

Absence is not validity. Important values use `Availability<T, R>` so callers
can distinguish unsupported, pending, ambiguous, stale, rejected and failed.
`Option` is reserved for semantically optional data whose absence needs no
trust or failure interpretation.

## Time Representations

Navheim provides its own dependency-free, exact representations:

- `GnssTimeScale` for native satellite-system scales and unknown future IDs;
- `RawGnssTime` for protocol-native, truncated, or otherwise unresolved fields;
- `ResolvedGnssTime` for one checked native-scale instant plus its resolution
  evidence;
- `TaiInstant` as the resolved continuous atomic result;
- `UtcRealization` and `ResolvedUtc` for explicit UTC mappings;
- `WeekResolution` and equivalent GLONASS day/era resolution evidence;
- `ReceiverClockEstimate` for bias, drift, reference epoch, and covariance;
- `TimeUncertainty` for asymmetric bounds, confidence/coverage meaning, named
  contributors, correlation groups and evidence quality.

There is no implicit conversion through Unix/POSIX time and no silent selection
of an era, leap table, UTC realization, or current wall clock. Unknown scales
and identifiers remain representable.

### Exact atomic representation

`TaiInstant` uses the epoch `1970-01-01T00:00:00 TAI`. Its canonical storage is
an `i64` count of whole SI seconds from that epoch and a `u64` attosecond field
in `0..1_000_000_000_000_000_000`. The epoch is an atomic coordinate only; it
does not imply that the same field values denote a POSIX/Unix instant.

Signed exact durations use an `i128` count of attoseconds. Constructors,
normalization, instant-plus-duration, instant-minus-duration, instant
difference, negation and scale conversion are checked. They return a typed
range or precision error instead of wrapping, saturating or truncating. The
supported `TaiInstant` range is the full canonical `i64`-second range at
one-attosecond granularity; narrower protocol or platform ranges remain
explicit conversion errors. Serialization fixes field widths, endianness and
canonical form and rejects non-canonical fractions.

Floating and lower-resolution adapters state rounding direction and report
lost precision. UTC and POSIX mappings additionally require an identified,
valid leap/UTC model and cannot be implemented as numeric casts.

### Capture-domain mapping

Opaque capture values become comparable only through an explicit mapping:

```rust
pub struct CaptureDomainMapping<S, D> {
    source: CaptureClockDomainId,
    source_generation: CaptureGeneration,
    destination: CaptureClockDomainId,
    destination_generation: CaptureGeneration,
    valid_source_interval: CaptureInterval<S>,
    transform: CaptureTransform<S, D>,
    uncertainty: TimeUncertainty,
    discontinuity: Availability<DiscontinuityEvidence, MappingReason>,
    mapping_generation: MappingGeneration,
}
```

A checked mapping operation verifies both domain IDs, both reset generations,
the validity interval and mapping generation, then returns a new destination
stamp plus accumulated uncertainty and provenance. A discontinuity ends the
mapping interval; it is never normalized away. Raw `C` values have no public
cross-domain ordering/subtraction convenience API, and mappings cannot be
silently chained without composing their intervals and uncertainties.

## PPS, Time Marks, and Frequency Outputs

Generic edge capture belongs outside Navheim's GNSS core. Navheim accepts a
bounded pulse event with an opaque capture timestamp and determines its GNSS
meaning:

```rust
pub struct PulseCapture<C> {
    captured_at: CaptureStamp<C>,
    sequence: u64,
    edge: PulseEdge,
    capture_uncertainty: TimeUncertainty,
}

pub struct PpsCorrelation {
    represented_instant: ResolvedGnssTime,
    time_mark: Availability<ReceiverTimeMark, TimeMarkReason>,
    convention: PulseConvention,
    delay: DelayBudget,
    uncertainty: TimeUncertainty,
}
```

`DelayBudget` is a bounded ordered set of antenna, cable, receiver, message,
quantization/sawtooth, capture-path and user-calibration contributions. Every
entry has sign convention, value/bounds, validity interval, provenance and
correlation group. The combination algorithm is explicit; correlated terms
are never blindly root-sum-squared.

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
    nominal: Hertz,
    captured_at: CaptureStamp<C>,
    receiver_error: Availability<FrequencyError, FrequencyReason>,
    lock: FrequencyLockState,
    uncertainty: FrequencyUncertainty,
    provenance: ProvenanceId,
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
        output: &mut GnssTimeEventSlot<Self::Capture>,
    ) -> Result<core::task::Poll<()>, Self::Error>;

    fn acknowledge(
        &mut self,
        sequence: EventSequence,
    ) -> Result<(), Self::Error>;
}
```

The caller-provided slot has a documented maximum size and contains no hidden
allocation. Every source documents maximum event size, queue depth and
unacknowledged-event capacity. It must not choose an async runtime, spawn a
thread, open an arbitrary device, or perform a privileged clock change.

The slot follows one explicit state machine:

```text
Vacant
  -- source publishes --> Occupied(sequence)
  -- consumer borrows --> Borrowed(sequence)
  -- borrow released --> Released(sequence)
  -- acknowledge --> Vacant
```

The source writes only a vacant slot. An occupied event is immutable and
remains owned by the slot while borrowed. Polling, overwriting, or
acknowledging a borrowed event fails without changing state. Releasing a
borrow does not acknowledge it; acknowledgement is accepted only for the
released sequence and vacates the slot. Repeating acknowledgement of the most
recently acknowledged sequence is an idempotent success. A stale, future, or
different-generation acknowledgement is a structured error. Drop-based
borrow release may be offered by safe wrappers, but the state transition and
recovery behavior remain testable without unwinding.

Each event carries an event sequence and source generation. A targeted
invalidation includes target artifact/model ID, optional replacement ID,
reason, effective capture/GNSS interval and whether withdrawal is mandatory.
Invalidation and security transitions cannot be dropped silently. Queue
pressure stops production, performs a documented explicit coalescing, or
forces source resynchronization. This prevents a consumer from retaining a
formerly valid observation after stale UTC parameters, authentication failure,
a receiver reset, discontinuity or spoofing evidence.

Sequences and generations never wrap. Before an event sequence is exhausted,
the source emits and obtains acknowledgement for a mandatory end-of-generation
event, renews the source generation, and restarts sequencing only under that
new identity. If the terminal transition cannot be delivered or acknowledged,
the source fails closed and requires resynchronization. Generation exhaustion
is terminal until a caller establishes a new, non-reused source identity.
Persisted consumers compare `(source identity, generation, sequence)` and
never infer freshness from integer ordering across different identities.

## Consumer Adapter Contract

A companion adapter:

1. consumes sequenced `GnssTimeEvent<C>` values through the bounded slot;
2. rejects unresolved, stale, unhealthy, or policy-disallowed observations;
3. converts Navheim's exact `TaiInstant` or native instant without truncation;
4. maps uncertainty bounds without turning them into false precision;
5. preserves capture-domain identity and PPS correlation;
6. preserves frequency-reference status and error without steering it;
7. preserves health, authentication, integrity, and provenance;
8. emits and acknowledges explicit withdrawal when Navheim invalidates prior
   evidence;
9. resets comparability when a capture domain generation changes;
10. reports disagreements between Navheim and consumer time models.

The adapter must not collapse authentication, signal-source authenticity,
message correctness, and solution integrity into one trusted boolean.

## Security Invariants

- Receiver time, host wall time, and approximate user time are untrusted hints.
- Era/week resolution requires explicit context and reports all ambiguity.
- Every resolution records alternatives, anchor/context, model identity,
  freshness and whether an untrusted hint influenced the result.
- UTC or leap data is never accepted solely because a receiver emitted it.
- Freshness is checked at the navigation model, observation, PPS, and adapter
  boundaries.
- Every correction and delay has units, sign convention, validity, uncertainty,
  and provenance.
- Time discontinuities and backward steps become events, never normalization.
- Event reordering, replay, loss and unacknowledged mandatory withdrawal fail
  closed or force resynchronization.
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
- capture-domain mismatch, generation reset, event replay, queue pressure,
  targeted withdrawal and acknowledgement loss;
- exact TAI range endpoints, non-canonical fractions, every checked arithmetic
  overflow and lower-resolution rounding direction;
- slot borrow/release/acknowledgement transitions, repeated acknowledgement,
  wrong sequence/generation and panic-free recovery;
- sequence/generation terminal transitions and attempted wrap/reuse;
- capture mappings at interval endpoints, discontinuities, stale generations,
  uncertainty composition and forbidden direct cross-domain comparison;
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
