# Telos Nexus — Engineering & Applied AI Portfolio

### Qasim Mohammed Hamad · Baghdad, Iraq
**Mechatronics / Control & Systems Engineering undergraduate** · **Founder, [Telos Nexus](https://telosnexus.io)**

[GitHub profile](https://github.com/heisqasim) · [Company website](https://telosnexus.io) · [Email](mailto:heisqasim@gmail.com)

> **Purpose:** Public, evidence-led summaries of work spanning applied AI, industrial automation, software systems and real-world product engineering. These are project *case studies*, not full source-code mirrors. Implementation repositories remain private for security, privacy and intellectual-property reasons.

## Portfolio at a glance

| Project | Focus | Verifiable evidence | Actual stage |
| --- | --- | --- | --- |
| **[Syntra](cases/syntra-bms.md)** | Industrial / building automation, reliable telemetry, BACnet / Delta enteliWEB | Field tests: one real controller, 32 points, one AHU | **Field-tested, read-only beta**; no controls/overrides |
| **[SADS](cases/sads-education-ai.md)** | Arabic educational data, provenance and grounded AI | [Live Math application](https://sads.telosnexus.services/app) · 935 source-linked questions and solutions from 305 source pages | **Math experience deployed and verified**; other V2 subjects pending |
| **[Al-Ghazaly Knowledge Atlas](cases/alghazaly-atlas.md)** | Information retrieval, OCR, data integrity, evidence trails | [Live site](https://alghazaly.telosnexus.space) · 84 source editions / 37,145 scanned pages | **Public research platform**; OCR != human-reviewed scholarship |
| **[Tally](cases/tally.md)** | Restaurant workflows and secure multi-tenant web/mobile systems | [Deployed guest app](https://tally-guest.web.app) | **Pilot-ready**; real restaurant acceptance pending |
| **[Wasl](cases/wasl.md)** | Offline-aware, IQD billing and data integrity | 271 Flutter tests, 142 security-rules tests and 28 billing audit tests | **Tested build**, offline handset acceptance pending |
| **[Phone Shop OS](cases/phone-shop-os.md)** | Retail inventory, IMEI, POS and instalments | Implemented engineering checkpoints and automated suites | **Active development**; payments mocked; commercial rollout pending |

**Additional work:** [Company operations platform](cases/tn-platform.md), [research interests and roadmap](RESEARCH.md).

### Public code you can actually run

To make the engineering approach inspectable without disclosing private application source, this repository includes **[two small, independently authored Python reference examples](examples/README.md)**: a fail-closed [citation gate](examples/citation_guard.py) and a read-only [BMS observation state model](examples/bms_observation.py). All **14 unit tests passed** using Python 3.13 in a clean clone. These are educational examples, **not** exported production code.

## Engineering themes

- **Control & autonomy:** Industrial automation, PLCs, BMS integration, monitoring and robotics.
- **Reliable applied AI:** Source-grounded retrieval, Arabic-first information access and explicit uncertainty.
- **Software systems:** Flutter, TypeScript, Python, cloud backends, API design, multi-tenant security and testing.
- **Local impact:** Practical tooling for Iraqi students and small and medium-sized businesses.

## Selected technical lessons

1. **A lost data link is not a stopped machine.** Syntra distinguishes connectivity from running state; stale data is labeled instead of translated into fake process alarms.
2. **A model response is not a citation.** SADS links generated explanations to documented sources and falls back to retrieval-only evidence when citations fail validation.
3. **Tests do not replace the field.** Tally's deployed backend still needs real restaurant acceptance; Wasl's offline sync path still needs physical handset validation.
4. **Provenance has levels.** The Al-Ghazaly Atlas keeps scanned pages, machine OCR, project-trusted baseline and human-reviewed canonical text separate.

## Collaboration & graduate research

I am interested in **funded research and graduate study** in robotics, intelligent control, AI/ML systems, trustworthy information retrieval, embedded/IoT systems and applied software engineering. I am completing my undergraduate studies in Control and Systems Engineering (Mechatronics) at the University of Technology, Baghdad.

I am also building [Telos Nexus](https://telosnexus.io) as an Iraqi technology venture, with a focus on transitioning demonstrable engineering prototypes into validated products.

For academic discussion, portfolio demonstrations or collaborations: **[heisqasim@gmail.com](mailto:heisqasim@gmail.com)**.

## Evidence & confidentiality

All figures above are sourced from project status documentation and development/verification records as of **October 2026**; they are **not** sales, impact, security certification, peer review or independent third-party endorsement. Live links expose only already-public applications. Private repositories and operational secrets have **not** been opened or copied into this showcase. See [evidence and disclosure policy](DISCLOSURE.md).

**© 2026 Qasim Mohammed Hamad / Telos Nexus. All rights reserved for case-study text and brand identity.**
