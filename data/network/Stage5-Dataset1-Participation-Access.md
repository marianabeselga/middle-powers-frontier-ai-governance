---
type: relational-dataset
stage: 5-network-analysis-stage1
dataset: participation-access
status: preliminary
related_episodes: [EP-BLETCHLEY-SEQUENCE-2023, EP-AISI-NETWORK-2024, EP-HIROSHIMA-AI-2024, EP-GPAI-2024]
---

# Stage 5, Dataset 1 — Participation / Access Network

**Purpose.** Actor ↔ Episode/institutional-process participation, membership, endorsement, institutional access, and hosting/co-chairing — documented involvement only. This dataset does **not** represent coordination, mobilisation, or influence. It is a separate, derived analytical dataset; it does not modify `06-Relational-Data/Nodes.md` or `Edges.md`, and it does not itself feed a new node/relationship type into the canonical schema (see the Validation Memo for the ontology basis of this choice).

**Critical rule, applied throughout.** A row in this dataset records that an actor was present, a member, a signatory/endorser, or held a titled role (host, co-chair, lead/co-lead of a track). It never asserts, and must never be read as asserting, that the actor coordinated (M) with another actor. Several actors below hold a titled role (e.g., "co-chair," "co-lead") that *also* happens to be the documented basis for a separately-established M finding recorded in Dataset 2 — in every such case this is flagged explicitly in the Note column, and the two records remain analytically distinct: this dataset records that the title/role existed; Dataset 2 separately and independently establishes that a documented joint activity meeting the Codebook §11 Critical Rule occurred. Holding a title is not, by itself, sufficient for the Dataset 2 edge — see the Validation Table for the specific test applied in each case.

Canonical actor identifiers used: `CTY-BRA`, `CTY-CAN`, `CTY-IND`, `CTY-JPN`, `CTY-KOR`, `CTY-SGP` (Codebook §25). Episode identifiers per Codebook §25: `EP-BLETCHLEY-SEQUENCE-2023`, `EP-AISI-NETWORK-2024`, `EP-HIROSHIMA-AI-2024`, `EP-GPAI-2024`. An actor with **no** documented participation in an Episode (e.g., Brazil and India in `EP-AISI-NETWORK-2024`; Brazil in `EP-HIROSHIMA-AI-2024` at full-membership level) has **no row** for that Episode — absence is preserved exactly as the frozen Episode records it, not filled in.

## EP-BLETCHLEY-SEQUENCE-2023

| Actor | Participation / involvement type | Institutional role / title | Source ID(s) | Evidence ID | Note |
|---|---|---|---|---|---|
| CTY-BRA | Participant / endorser (Bletchley Declaration, Bletchley State of Science, Seoul Ministerial Statement, Paris Statement, Paris Co-Chairs' Statement, India AI Impact Summit) | None | SRC-UKGOV-2023-001/003; SRC-UKGOV-2024-002; SRC-ELYSEE-2025-001/002; SRC-MEA-2026-001 | EVD-BRA-013, EVD-BRA-015, EVD-BRA-018, EVD-BRA-020 | Not a signatory to Bletchley Safety Testing, Seoul Declaration, or Seoul SOI; not a corporate signatory to Frontier AI Safety Commitments; not a government commitment-maker under New Delhi Frontier AI Impact Commitments. Peripheral, broadest-declaratory-tier participation only. |
| CTY-CAN | Participant / signatory across nearly every instrument, including Bletchley Safety Testing and Seoul SOI | None | SRC-UKGOV-2023-001/002; SRC-UKGOV-2024-001/002/003; SRC-ELYSEE-2025-001; SRC-MEA-2026-001 | EVD-CAN-011–014 | Strongest participation tier among non-host cases. |
| CTY-CAN | Bilateral joint committee / research-call party (with France, a non-case actor) | None (no formal title; a named joint committee, est. Apr. 2023) | Canada–France Declaration (not separately registered as a Table 2 instrument; verified 2026-09-04) | (no formal Evidence ID registered) | Documents planned/joint activity; the underlying M finding is **plausible, not established** — see Dataset 2 exclusion table. Recorded here purely as a participation/access fact. |
| CTY-CAN | **Co-chair**, New Delhi Science Working Group (with Singapore, India) | Co-chair | SRC-MDDI-2026-002 | EVD-CAN-015 | This title is also the basis of a separately-established M edge in Dataset 2 (New Delhi Science WG configuration) — see that dataset; the two records are analytically distinct per the Critical Rule above. |
| CTY-IND | Represented in broad declarations; not a signatory to Seoul Declaration or SOI | None | Existing Table 3 rows; EVD-IND-014 | EVD-IND-014, EVD-IND-015 | |
| CTY-IND | **Co-chair**, Paris Co-Chairs' Statement | Co-chair | SRC-PMINDIA-2025-001 | EVD-IND-014 | A large multilateral co-chair role (standard host-sequence mechanism), distinct in kind from the Science WG co-chair role below; **not** linked to any established M finding. |
| CTY-IND | **Host**, India AI Impact Summit / New Delhi stage; endorser of New Delhi Frontier AI Impact Commitments | Host | SRC-MEA-2026-001; SRC-PIB-2026-003 | EVD-IND-015 | |
| CTY-IND | Organisational design of the Sutra–Chakra Working Group framework; appointment of the Safe and Trusted AI Working Group's chair | Working-Group-framework designer / chair-appointer | (New Delhi Working Group preparation sources) | EVD-IND-016, EVD-IND-017 | Documents an organisational/structuring role; the underlying M finding on this specific channel is **plausible, not established** — see Dataset 2 exclusion table. |
| CTY-IND | **Co-chair**, New Delhi Science Working Group (with Singapore, Canada) | Co-chair | SRC-MDDI-2026-002 | EVD-IND-019 | Basis of a separately-established M edge in Dataset 2 — see note on CTY-CAN's identical role, above. |
| CTY-JPN | Participant / signatory across nearly every instrument | None | SRC-UKGOV-2023-001/002; SRC-UKGOV-2024-001/002/003; SRC-ELYSEE-2025-001; SRC-MEA-2026-001 | EVD-JPN-013–016 | |
| CTY-JPN | Presentation of the Hiroshima AI Process at Bletchley; forum-linkage statement at Seoul; Friends Group expansion statement at New Delhi | Presenter / position-articulator | Table 2 sources (Bletchley, Seoul stages) | EVD-JPN-013, EVD-JPN-014, EVD-JPN-016 | Documents a position/participation act; the underlying M finding (forum linkage) is **plausible, not established** — see Dataset 2 exclusion table. |
| CTY-JPN | Named co-participant, Singapore–Japan joint testing (AISI Testing and Evaluation Track) | Co-participant | (Announced as a Paris-stage deliverable; per the Episode-level configuration table) | EVD-SGP-015 (Japan not separately named in its own Research Note — see Dataset 2 validation notes) | This participation fact is the basis of an established M edge in Dataset 2 (Singapore–Japan), even though it is not corroborated within this same Episode's Japan-side country-attribution section — flagged, not silently resolved. `EP-AISI-NETWORK-2024.md` later documents this same activity as its own Feb. 2025 second Joint Testing Exercise — cross-Episode corroboration (`corroboration_scope = cross_episode`), not same-Episode corroboration by Japan; see Dataset 2, Table 2A note, and `Coding-Decisions-Log.md`, 2026-09-07. |
| CTY-KOR | Participant / signatory across nearly every instrument | None | SRC-UKGOV-2023-001/002; SRC-ELYSEE-2025-001; SRC-MEA-2026-001 | EVD-KOR-011–014 | |
| CTY-KOR | **Host**, Seoul stage (Declaration, Statement of Intent, Ministerial Statement, Frontier AI Safety Commitments — including named corporate signatories Naver and Samsung) | Host | SRC-UKGOV-2024-001/002/003 | EVD-KOR-011, EVD-KOR-012 | This hosting/authorship role is also the basis of Korea's candidate M finding, which remains **plausible, approaching established, not established** — see Dataset 2 exclusion table. |
| CTY-SGP | Participant / signatory across nearly every instrument | None | SRC-UKGOV-2023-001/002; SRC-UKGOV-2024-001/002/003; SRC-ELYSEE-2025-001; SRC-MEA-2026-001 | EVD-SGP-013, EVD-SGP-014 | |
| CTY-SGP | **Co-lead**, AISI Testing and Evaluation Track (Paris) | Co-lead (with Japan) | SRC-IMDA-2025-003; SRC-ELYSEE-2025-001 | EVD-SGP-015 | Basis of the established Singapore–Japan M edge in Dataset 2. |
| CTY-SGP | **Co-chair**, New Delhi Science Working Group (with India, Canada) | Co-chair | SRC-MDDI-2026-002 | EVD-SGP-016 | Basis of the established Singapore–India–Canada M edge in Dataset 2. |

## EP-AISI-NETWORK-2024

| Actor | Participation / involvement type | Institutional role / title | Source ID(s) | Evidence ID | Note |
|---|---|---|---|---|---|
| CTY-CAN | Founding member; participant, Joint Statement on Risk Assessment; supporting member (not co-lead), Research Agenda on Synthetic Content Risks | Founding member | SRC-NIST-2024-001/002; SRC-ISED-2025-001 | EVD-CAN-016; EVD-CAN-010 | The researcher's original "Canada–Australia co-lead" claim for the Research Agenda was independently checked and found unsupported by the primary source — corrected; recorded here as ordinary supporting-member participation only. |
| CTY-CAN | Documented contributor (dataset translation and annotation), Subsequent Multilateral Joint Testing Exercises | Contributor | SRC-UKAISI-2025-001 | EVD-CAN-016 | Basis of Canada's established M edge (Joint Testing Exercises configuration) in Dataset 2. |
| CTY-JPN | Founding member; participant, Mission Statement and Joint Statement on Risk Assessment; supporting member, Research Agenda | Founding member | SRC-NIST-2024-001/002; SRC-ISED-2025-001 | EVD-JPN-017 | |
| CTY-JPN | Documented contributor (dataset validation, translation/annotation), Subsequent Multilateral Joint Testing Exercises | Contributor | SRC-UKAISI-2025-001 | EVD-JPN-017 | Basis of Japan's established M edge (Joint Testing Exercises configuration) in Dataset 2. |
| CTY-KOR | Founding member; participant, Mission Statement and Joint Statement on Risk Assessment; supporting member, Research Agenda; presenter of domestic research at founding meeting | Founding member / presenter | SRC-NIST-2024-001/002; SRC-MSIT-2024-001/002 | EVD-KOR-015 | Founding-meeting presentation documents participation only; not established as M on its own — see Dataset 2 exclusion table. |
| CTY-KOR | Documented contributor (dataset validation, translation/annotation), Subsequent Multilateral Joint Testing Exercises | Contributor | SRC-UKAISI-2025-001 | EVD-KOR-015 | Basis of Korea's established M edge (Joint Testing Exercises configuration) in Dataset 2. |
| CTY-SGP | Founding member; AISI designation (Digital Trust Centre, 22 May 2024) | Founding member | SRC-IMDA-2024-003 | EVD-SGP-017 | |
| CTY-SGP | **Lead** (with non-case US/UK), First Multilateral Testing Exercise; **strand lead**, Subsequent Multilateral Joint Testing Exercises | Lead / strand lead | SRC-SGAISI-2024-001; SRC-UKAISI-2025-001 | EVD-SGP-017 | Basis of Singapore's established M edge (Joint Testing Exercises configuration, leadership role) in Dataset 2. |

*CTY-BRA and CTY-IND have no rows for this Episode — both are confirmed absent from every component instrument (not a network member, not participating), preserved exactly as the frozen record states.*

## EP-HIROSHIMA-AI-2024

| Actor | Participation / involvement type | Institutional role / title | Source ID(s) | Evidence ID | Note |
|---|---|---|---|---|---|
| CTY-BRA | **Observer** (not member), second in-person Friends Group meeting (2026) | Observer | (MOFA Japan AI×Trust Program page, not independently re-fetched this round) | (not independently re-verified this round) | Materially weaker than the other five cases' founding (May 2024) membership. The frozen Episode does not treat Brazil as an Episode actor on this basis; recorded here only as a documented participation fact, flagged, not upgraded. |
| CTY-CAN | G7 participant, all core instruments; founding Friends Group member (May 2024) | Founding member | SRC-GOJ-2023-001; SRC-SOUMU-2023-001–005, 2024-001/003; SRC-SOUMU-2024-002 | EVD-CAN-017 | No coordination activity beyond membership documented — see Dataset 2 exclusion table. |
| CTY-IND | Absent from G7-core instruments; founding Friends Group member (May 2024); Action Plan 2026 participant | Founding member | SRC-SOUMU-2024-002; SRC-SOUMU-2026-001 | EVD-IND-020 | |
| CTY-IND | Party, Japan–India Joint Statement on Cooperation in AI (2 Jul. 2026) | Bilateral partner | SRC-PMINDIA-2026-002 | EVD-IND-020 | Basis of the established Japan–India M edge in Dataset 2. |
| CTY-JPN | G7 host/participant, all core instruments | Host | SRC-GOJ-2023-001; SRC-SOUMU series | EVD-JPN-018 | |
| CTY-JPN | **Founder/convenor**, Hiroshima AI Process Friends Group (May 2024, 49 members); **host**, second in-person meeting (Tokyo, Mar. 2026, 66 members) at which the Action Plan was announced | Founder / host | SRC-SOUMU-2024-002; SRC-SOUMU-2026-001 | EVD-JPN-018 | Basis of Japan's established M edge (Friends Group creation, unilateral institutional-entrepreneurship) in Dataset 2. |
| CTY-JPN | Party, Japan–India Joint Statement on Cooperation in AI | Bilateral partner | SRC-PMINDIA-2026-002 | EVD-JPN-018; EVD-IND-020 | Basis of the established Japan–India M edge in Dataset 2. |
| CTY-JPN | Party, Japan–Korea working-level bilateral meeting | Bilateral partner | SRC-MOFAKR-2026-001 | EVD-KOR-016 | Underlying M finding is **plausible, not established** as Hiroshima-specific — see Dataset 2 exclusion table. |
| CTY-KOR | Absent from G7-core instruments; founding Friends Group member (May 2024); Action Plan 2026 participant | Founding member | SRC-SOUMU-2024-002; SRC-SOUMU-2026-001 | EVD-KOR-016 | |
| CTY-KOR | Party, Japan–Korea working-level bilateral meeting (5 Feb. 2026) | Bilateral partner | SRC-MOFAKR-2026-001 | EVD-KOR-016 | See M-status note above; excluded from Dataset 2. |
| CTY-SGP | Absent from G7-core instruments; founding Friends Group member (May 2024); Action Plan 2026 participant | Founding member | SRC-SOUMU-2024-002; SRC-SOUMU-2026-001 | EVD-SGP-018 | No coordination activity beyond membership documented — see Dataset 2 exclusion table. Singapore's unilateral mapping of its own domestic framework to the Hiroshima Principles is a positional act, not a joint activity with a second named actor, and is not recorded as a separate participation row. |

## EP-GPAI-2024

| Actor | Participation / involvement type | Institutional role / title | Source ID(s) | Evidence ID | Note |
|---|---|---|---|---|---|
| CTY-BRA | Participant, all four ministerial declarations | None | SRC-OECD-2022-001; SRC-OECD-2023-001; SRC-GPAI-2024-001; SRC-OECD-2024-002 | EVD-BRA-021 | |
| CTY-BRA | Named expert participant (Laercio Aniceto Silva; Norberto Ferreira), Innovation & Commercialisation Working Group; cited (not independently re-fetched) participation, Data Governance and Future of Work Working Groups | Named-expert contributor | SRC-OECDAI-2024-001 | EVD-BRA-021 | Individual experts act independently of government (per `SRC-OECDAI-2025-001`'s independence qualification, applied Episode-wide). Basis of Brazil's established M edge (Innovation & Commercialisation WG) in Dataset 2. |
| CTY-CAN | Participant, all four declarations; founding member (2020); host, first GPAI Multistakeholder Experts Group Plenary (Montréal, Dec. 2020); operator of CEIMIA (national Expert Support Centre) | Founding member / host / ESC operator | SRC-OECD-2022-001; SRC-OECD-2023-001; SRC-GPAI-2024-001; SRC-OECD-2024-002 | EVD-CAN-018 | Founding/hosting/CEIMIA claims not independently re-fetched this round; consistent with well-documented public facts. Basis of Canada's established M edge (GPAI Founding Coalition) in Dataset 2. |
| CTY-CAN | Named-expert contributor (Marc-André Sirard, Specialist tier), Innovation & Commercialisation WG; 2 members, Responsible AI WG | Named-expert contributor | SRC-OECDAI-2024-001; SRC-OECDAI-2025-001 | EVD-CAN-018 | Independently verified. Basis of Canada's established M edges (both GPAI Working Groups) in Dataset 2. |
| CTY-IND | Participant, all four declarations; **host**, 2024 New Delhi ministerial meeting; 2024 Lead Chair | Host / Lead Chair | SRC-GPAI-2024-001 | EVD-IND-021 | Basis of India's established M edge (chairmanship / GPAI–OECD Integrated Partnership) in Dataset 2. |
| CTY-IND | Named-expert contributor (Mausam, IIT), Innovation & Commercialisation WG; 2 members, Responsible AI WG | Named-expert contributor | SRC-OECDAI-2024-001; SRC-OECDAI-2025-001 | EVD-IND-021 | Basis of India's established M edges (both GPAI Working Groups) in Dataset 2. |
| CTY-JPN | Participant, all four declarations; **host/presidency**, 2022 Tokyo declaration; founding member; 2023 Lead Chair; operator of Tokyo Expert Support Center (NICT) | Founding member / host / chair / ESC operator | SRC-OECD-2022-001 | EVD-JPN-019 | Founding/hosting/ESC claims not independently re-fetched this round; consistent with well-documented public facts. Basis of Japan's established M edge (GPAI Founding Coalition) in Dataset 2. |
| CTY-JPN | Named-expert contributor (3 named individuals), Innovation & Commercialisation WG; 2 members, Responsible AI WG | Named-expert contributor | SRC-OECDAI-2024-001; SRC-OECDAI-2025-001 | EVD-JPN-019 | Basis of Japan's established M edges (both GPAI Working Groups) in Dataset 2. |
| CTY-KOR | Participant, all four declarations; founding member (2020) | Founding member | SRC-OECD-2022-001; SRC-OECD-2023-001; SRC-GPAI-2024-001; SRC-OECD-2024-002 | EVD-KOR-017 | No founding-architect or chairmanship-level role documented for Korea within this Episode (distinct from Canada/Japan/India). |
| CTY-KOR | Named-expert contributor (Mekyung Lee, Korea University, newly identified), Innovation & Commercialisation WG; ≥1 member, Responsible AI WG | Named-expert contributor | SRC-OECDAI-2024-001; SRC-OECDAI-2025-001 | EVD-KOR-017 | Basis of Korea's established M edges (both GPAI Working Groups) in Dataset 2. |
| CTY-SGP | Participant, all four declarations; founding member | Founding member | SRC-OECD-2022-001; SRC-OECD-2023-001; SRC-GPAI-2024-001; SRC-OECD-2024-002 | EVD-SGP-019 | |
| CTY-SGP | **Co-chair** (Laurence Liew, with France's Françoise Soulié-Fogelman), Innovation & Commercialisation WG; confirmed representation, Responsible AI WG | Co-chair / named-expert contributor | SRC-OECDAI-2024-001; SRC-OECDAI-2025-001 | EVD-SGP-019 | Leadership act, not passive membership. Basis of Singapore's established M edges (both GPAI Working Groups) in Dataset 2. |

## Summary counts (descriptive only — see §11 of the task instruction: not interpreted here)

| Episode | Actor rows | Distinct actors present |
|---|---|---|
| EP-BLETCHLEY-SEQUENCE-2023 | 17 | 6 (BRA, CAN, IND, JPN, KOR, SGP) |
| EP-AISI-NETWORK-2024 | 7 | 4 (CAN, JPN, KOR, SGP) |
| EP-HIROSHIMA-AI-2024 | 11 | 5 full + 1 observer-only (CAN, IND, JPN, KOR, SGP; BRA as observer) |
| EP-GPAI-2024 | 12 | 6 (BRA, CAN, IND, JPN, KOR, SGP) |
| **Total participation rows** | **47** | — |

Row counts are higher than a simple actor×Episode count because a single actor's participation in a single Episode is frequently documented as more than one distinct, separately-sourced involvement type (e.g., "participant" plus "host," or "founding member" plus "contributor to a specific testing exercise"). Each distinct, separately-evidenced involvement type is recorded as its own row rather than collapsed into one summary cell, so that provenance (Source ID, Evidence ID) stays specific to the exact claim it supports.
