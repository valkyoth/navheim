# Unsafe Code Policy

Current workspace crates forbid unsafe code.

Protocol, constellation, solver, integrity, format, and canonical model crates
must continue to forbid unsafe code. Unsafe code may exist only in isolated
platform FFI, SIMD intrinsic, or hardware DMA modules when safe Rust cannot
provide the required boundary.

Before the first adapter requiring unsafe code, the workspace-default lint
changes from `forbid` to `deny`, while every canonical crate retains an
explicit crate-root `#![forbid(unsafe_code)]`. An adapter remains
`#![deny(unsafe_code)]` and permits unsafe code only in one narrowly scoped
`sys`, `ffi`, `dma`, or `simd` module. This transition occurs at an explicit
adapter milestone and must not weaken canonical crates.

For SIMD, v0.48.2 freezes alignment, aliasing, ownership, feature-detection,
length/tail and scalar-fallback contracts before v0.49.0 may add dispatch.
Dispatch cannot retroactively define safety conditions under which it already
runs.

The Rust 1.90.0–1.97.1 line does not use nightly portable SIMD. Optimized
implementations use stable target-specific `core::arch` behind reviewed
modules or compiler auto-vectorization, always with a deterministic scalar
fallback. A future portable API cannot enter until it is stable on the MSRV or
the project deliberately raises the MSRV.

Before unsafe code is admitted:

- create a separate module or adapter crate;
- document every invariant, ownership rule, alignment/lifetime requirement,
  buffer-length rule, concurrency assumption, cancellation/unplug/reset
  behavior, and untrusted-data copy boundary;
- isolate generated bindings, pin their source/generator, and reproduce them
  byte-for-byte;
- keep protocol parsing outside unsafe code;
- use Miri for safe wrapper/ownership models, Kani for bounded arithmetic and
  state machines, Loom for concurrency/order, and sanitizers/hardware fault
  injection for native calls as applicable;
- require an independent safety review and milestone pentest;
- update this policy, the threat model, SBOM/dependencies, and release notes.

Unsafe code is never admitted only for convenience or speculative performance.
