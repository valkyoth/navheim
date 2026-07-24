# Unsafe Code Policy

Current workspace crates forbid unsafe code.

Protocol, constellation, solver, integrity, format, and canonical model crates
must continue to forbid unsafe code. Unsafe code may exist only in isolated
platform FFI, SIMD intrinsic, or hardware DMA modules when safe Rust cannot
provide the required boundary.

Before unsafe code is admitted:

- create a separate module or adapter crate;
- document every invariant, ownership rule, alignment/lifetime requirement,
  concurrency assumption, and untrusted-data copy boundary;
- keep protocol parsing outside unsafe code;
- add Miri, sanitizer, fault-injection, and platform tests where applicable;
- require an independent safety review and milestone pentest;
- update this policy, the threat model, SBOM/dependencies, and release notes.

Unsafe code is never admitted only for convenience or speculative performance.
