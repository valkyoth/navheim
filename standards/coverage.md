# Standards Coverage

Status: inventory only; no GNSS protocol behavior is implemented.

| Family | 1.0 target | Current status |
| --- | --- | --- |
| GPS | All publicly documented civil L1/L2/L5 signals and messages in frozen baseline | Planned |
| Galileo | Public E1/E5/E6, I/NAV, F/NAV, HAS, OSNMA, SAR/RLS, timing, and stabilized public additions | Planned |
| GLONASS | Public FDMA and officially documented public CDMA services | Planned |
| BeiDou | Public B1/B2/B3 signals, navigation, PPP-B2b, BDSBAS, and conditional public SAR/short-message interfaces | Planned; messaging requires stable open specification |
| QZSS | Public L1/L2/L5/L6, SLAS, CLAS, MADOCA, and QZNMA services | Planned |
| NavIC | Public L1/L5/S SPS signals/navigation and conditionally documented public messaging | Planned; messaging requires stable open specification |
| SBAS | Provider-neutral legacy and DFMC protocol plus exact WAAS, EGNOS, MSAS, GAGAN, SDCM, BDSBAS, KASS, SouthPAN and admitted African provider profiles | Planned |
| Corrections | RTCM OSR/SSR, network RTK, IGS SSR | Planned |
| Exchange | NMEA 0183, legal NMEA 2000 boundary, RINEX 2/3/4, principal IGS products | Planned |
| Assistance | OMA SUPL, 3GPP LPP, Android raw measurements, injected assistance | Planned |
| GNSS time transfer | Common-view/all-in-view results and frozen CGGTTS V2E interoperability | Planned; clock discipline/consensus excluded |
| Civil/geodetic time | UTC leap/calendar, POSIX ambiguity, Julian/MJD, TT and EOP-derived UT1 arguments | Planned; no implicit POSIX cast or leap-smear claim |
| Numerical foundations | Bounded linear algebra plus admitted normal/chi-square kernels with conservative integrity rounding | Planned; first-party implementation, independent high-precision evidence |
| Persistent state protection | Orthogonal evidence, canonical binding, bounded state-matrix recovery/cleanup, narrow repair authority and separately admitted platform authorities | Planned; no universal keystore, implicit suite, unbounded retention, same-namespace reset or rollback-resistance claim |
| Receiver sources/control | gpsd, named public vendor protocols, NMEA-only, RTCM, RINEX, raw observations, configuration-generation-safe allowlisted control and interval-scoped behavioral assessment | Planned; exact hardware/firmware evidence required, arbitrary commands excluded, ACK/read-back remains receiver-asserted |
| GNSS science | Calibrated scintillation, reflectometry, space-weather and remote-sensing artifacts from frozen methods | Planned; optional research surface, no unvalidated operational-product claim |
| SDR/accelerator I/O | Prepared plans, linear pre-submit/transport state, control-lease-bounded proof, coherent outcomes and safe reads for named stacks | Planned; device read-back and accelerator output remain assertions |
| GitHub-only tools | Capture, CLI, daemon, caster, station, survey, inspector, viewer, lab, simulator, conformance, fuzz, bench, and deployment | Planned; never in crates.io graph |
| Aviation integrity | Public SBAS/GBAS/ABAS data models and research interfaces | Planned; no certification claim |
| Restricted services | Identifier/metadata preservation and RF measurement only | Planned; no decoding claim |

Every status changes only after `standards/manifest.toml` contains a verified
revision and concrete `implemented_by` and `tests` mappings.

The acquisition inventory in `standards/sources.toml` covers the authoritative
source families needed by this table. It records current candidates and access
rules but is not an implementation claim. Exact RFC transport/security
references are checksum-locked under `standards/rfc/`; all other document
bytes default to the ignored local vault.
