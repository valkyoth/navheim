# Standards Coverage

Status: inventory only; no GNSS protocol behavior is implemented.

| Family | 1.0 target | Current status |
| --- | --- | --- |
| GPS | All publicly documented civil L1/L2/L5 signals and messages in frozen baseline | Planned |
| Galileo | Public E1/E5/E6, I/NAV, F/NAV, HAS, OSNMA, SAR/RLS, timing, and stabilized public additions | Planned |
| GLONASS | Public FDMA and officially documented public CDMA services | Planned |
| BeiDou | Public B1/B2/B3 signals, navigation, PPP-B2b, BDSBAS, and conditional public SAR/short-message interfaces | Planned; messaging requires stable open specification |
| QZSS | Public L1/L2/L5/L6, SLAS, CLAS, MADOCA, and QZNMA services | Planned |
| NavIC | Public L1/L5/S SPS signals and navigation | Planned |
| SBAS | Provider-neutral legacy and DFMC protocol plus documented provider profiles | Planned |
| Corrections | RTCM OSR/SSR, network RTK, IGS SSR | Planned |
| Exchange | NMEA 0183, legal NMEA 2000 boundary, RINEX 2/3/4, principal IGS products | Planned |
| Assistance | OMA SUPL, 3GPP LPP, Android raw measurements, injected assistance | Planned |
| GNSS time transfer | Common-view/all-in-view results and frozen CGGTTS V2E interoperability | Planned; clock discipline/consensus excluded |
| Receiver sources | gpsd, named public vendor protocols, NMEA-only, RTCM, RINEX, and raw observations | Planned; exact hardware/firmware evidence required |
| SDR/FPGA I/O | Named SDR stacks plus bounded FPGA/external-DSP artifacts | Planned; accelerator output remains untrusted |
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
