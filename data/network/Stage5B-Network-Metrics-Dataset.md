---
type: relational-dataset
stage: 5b-network-metrics
status: preliminary
derived_from: [Stage5-Dataset1-Participation-Access.md, Stage5-Dataset2-Established-Coordination.md]
related_episodes: [EP-BLETCHLEY-SEQUENCE-2023, EP-AISI-NETWORK-2024, EP-HIROSHIMA-AI-2024, EP-GPAI-2024]
---

# Stage 5B — Network-Analysis Dataset and Metrics

Three network representations, each built directly from the validated Stage 5 datasets (no new empirical claim, no re-coding of M/L/GL). Computed with `networkx` 3.2.1; the computation script and raw JSON output are retained in the session scratchpad for reproducibility and are not part of this repository. All counts below were verified by direct recount against `Stage5-Dataset2-Established-Coordination.md` (Table 2B has 22 rows, not the 19 an earlier pass mistakenly totaled — corrected there and reflected here).

## 1. Bipartite participation/access network (from Dataset 1)

Nodes: 6 actors, 4 Episodes. An edge exists where an actor has at least one documented participation row in that Episode (Dataset 1); this collapses Dataset 1's 47 role-level rows into one tie per actor–Episode pair actually present, which is the correct level for a bipartite access structure.

| Actor | Bletchley | AISI Network | Hiroshima | GPAI | Breadth (of 4) |
|---|---|---|---|---|---|
| Brazil | ✓ | — | ✓ (observer tier only) | ✓ | 3 |
| Canada | ✓ | ✓ | ✓ | ✓ | 4 |
| India | ✓ | — | ✓ | ✓ | 3 |
| Japan | ✓ | ✓ | ✓ | ✓ | 4 |
| Korea | ✓ | ✓ | ✓ | ✓ | 4 |
| Singapore | ✓ | ✓ | ✓ | ✓ | 4 |
| **Episode breadth (of 6)** | **6** | **4** | **6** (5 full + 1 observer) | **6** | |

- Participation edges: **22** including Brazil's weaker Hiroshima observer-tier tie; **21** if that tie is excluded.
- Maximum possible actor–Episode ties: 6 × 4 = 24.
- Bipartite density: **0.917** (including the observer tie) / **0.875** (excluding it).
- No one-mode projection was computed from this bipartite structure (see §3, below, for why).

## 2. Direct actor-to-actor established coordination network (Table 2A only)

Nodes: the 6 study actors (isolates retained for reference rather than dropped, so the graph's node set stays consistent across representations). Edges: only the 2 genuinely dyadic established M relationships.

| Actor | Degree | Betweenness (normalised) | Betweenness (raw) | Component |
|---|---|---|---|---|
| Brazil | 0 | 0.000 | 0.000 | {Brazil} (isolate) |
| Canada | 0 | 0.000 | 0.000 | {Canada} (isolate) |
| India | 1 | 0.000 | 0.000 | {Singapore, Japan, India} |
| Japan | 2 | 0.100 | 1.000 | {Singapore, Japan, India} |
| Korea | 0 | 0.000 | 0.000 | {Korea} (isolate) |
| Singapore | 1 | 0.000 | 0.000 | {Singapore, Japan, India} |

- Nodes: 6. Edges: 2. Density: **0.133**.
- Connected components: **4** (one 3-node path — Singapore–Japan–India — plus three singleton isolates: Canada, Korea, Brazil).
- Japan is the only cut-vertex in this graph: it sits on the one path connecting Singapore and India, which is what produces its non-zero betweenness. With only 2 edges in the entire graph, this is a structural fact about a 3-node path, not evidence of Japan "brokering" anything beyond what the two dyads (Singapore–Japan, Bletchley; Japan–India, Hiroshima) already, individually, established through process tracing — see the Interpretation Safeguards in the accompanying memo.

## 3. Actor-to-configuration (hub) network (Table 2B only)

Nodes: 6 actors, 7 MECHANISM/COALITION/INSTRUMENT hubs. Edges: 22 (bipartite — no actor-to-actor edge is implied by co-attachment to the same hub).

**A one-mode projection of this bipartite graph (connecting any two actors who share a hub) was deliberately not constructed.** Doing so would manufacture, for example, a Brazil–Canada tie purely because both are named in the same GPAI Working Group roster, with no documentation that Brazil's and Canada's named experts interacted with each other specifically — exactly the kind of invented pairwise relationship the task instructs against. The bipartite (actor–hub) form is retained as the only representation of this data.

| Actor | Distinct hubs (affiliation count) | Distinct Episodes with ≥1 established hub/dyadic tie |
|---|---|---|
| Brazil | 1 | 1 (GPAI) |
| Canada | 5 | 3 (Bletchley, AISI Network, GPAI) |
| India | 4 | 2 (Bletchley, GPAI) |
| Japan | 5 | 3 (AISI Network, Hiroshima, GPAI) |
| Korea | 3 | 2 (AISI Network, GPAI) |
| Singapore | 4 | 3 (Bletchley, AISI Network, GPAI) |

| Hub node | Node type | Episode | Coordination level | Attached actors (degree) |
|---|---|---|---|---|
| GPAI WG — Innovation & Commercialisation | MECHANISM | GPAI | expert/epistemic | 6 (all study cases) |
| GPAI WG — Responsible AI | MECHANISM | GPAI | expert/epistemic | 5 (all but Brazil, not independently confirmed for this WG this round) |
| AISI Network Joint Testing Exercises | MECHANISM | AISI Network | technical-operational | 4 |
| New Delhi Science Working Group | MECHANISM | Bletchley | mixed | 3 |
| GPAI Founding Coalition | COALITION | GPAI | state/diplomatic | 2 (Canada, Japan — each individually established as one of 15 founders; **no direct Canada–Japan tie is documented**, only shared attachment to the same founding-era institution) |
| GPAI–OECD Integrated Partnership | INSTRUMENT | GPAI | state/diplomatic | 1 (India only — a singleton attachment) |
| Hiroshima AI Process Friends Group | COALITION | Hiroshima | state/diplomatic | 1 (Japan only — a singleton attachment) |

Note the last three rows are structurally distinct from one another despite all being unilateral-institutional-entrepreneurship-type established M findings: a 2-actor hub with no documented tie between the two attached actors (GPAI Founding Coalition) versus two true singleton attachments (GPAI–OECD Integrated Partnership; Hiroshima Friends Group). This distinction is used directly in the memo's institutional-entrepreneurship check.

## Table A — Compact metrics table (all representations)

| Network representation | Nodes | Edges | Density | Connected components | Degree / affiliation | Betweenness | Caveats |
|---|---|---|---|---|---|---|---|
| Bipartite participation/access | 6 actors + 4 Episodes = 10 | 21–22 | 0.875–0.917 | 1 (fully connected once Brazil's weak tie is included; AISI Network is the only Episode not reaching all 6 actors) | See breadth table, §1 | Not computed — not a meaningful measure on a near-complete bipartite graph of this size | Density is high largely because participation is a low evidentiary bar (Codebook §11 explicitly treats it as insufficient for M); a high participation density is expected and uninformative about coordination. |
| Direct actor-to-actor coordination | 6 | 2 | 0.133 | 4 (1 triad-path + 3 isolates) | Degree: Japan 2, Singapore/India 1, others 0 | Japan: 0.100 (normalised); all others 0.000 | n is far too small (2 edges) for density/centrality to carry comparative weight; reported because requested, not because it is analytically load-bearing. |
| Actor-to-configuration (hub) | 6 actors + 7 hubs = 13 | 22 | Not computed as a single density figure — a bipartite graph with two very differently-sized sides (6 vs. 7) makes one-mode density comparisons misleading; affiliation counts (above) are the appropriate descriptive measure instead | 1 (all actors and hubs fall in one connected bipartite component, via GPAI's Working Groups) | Affiliation counts: Canada/Japan 5, India/Singapore 4, Korea 3, Brazil 1 (actor side); GPAI WG-I&C 6, GPAI WG-RAI 5, AISI JTE 4, New Delhi WG 3, GPAI Founding Coalition 2, other two hubs 1 each (hub side) | Not computed — betweenness on a bipartite hub structure would conflate "connects many configurations" with "brokers between actors," which this stage explicitly avoids asserting (see memo) | Affiliation count mixes tie types of very different evidentiary weight (a WG-level expert-tier tie and a founding-tier state-level tie both count as "1" in an actor's degree) — flagged, not resolved, since disaggregating by level is done qualitatively in the memo instead of through a single blended number. |

## Table B — Episode-level structural comparison

| Episode | Participating actors (Dataset 1) | Actors with ≥1 established coordination tie (Dataset 2, direct + hub) | Established coordination edges | Coordination levels present | Structural pattern |
|---|---|---|---|---|---|
| Bletchley | 6 | 4 (Singapore, Japan, India, Canada) | 4 (1 dyadic + 3 hub) | technical-operational (1), mixed (3) | Selective: two of six participating actors (Brazil, Korea) show zero established coordination. |
| AISI Network | 4 | 4 (all participants) | 4 (all hub) | technical-operational (4) | Universal-within-participants: every actor who participates in this Episode also has an established coordination tie — no participation/coordination gap at the actor level (though a within-configuration leadership/contributor distinction still exists — see the Singapore check in the memo). |
| Hiroshima | 6 (5 full + 1 observer) | 2 (Japan, India) | 2 (1 dyadic + 1 hub, the hub being unilateral) | state/diplomatic (2) | Most selective: four of six participating actors (Brazil, Canada, Korea, Singapore) show zero established coordination — the widest participation/coordination gap of the four Episodes. |
| GPAI | 6 | 6 (all participants) | 14 (all hub) | expert/epistemic (11), state/diplomatic (3) | Universal-but-stratified: every participating actor has at least one established tie, but tie count and tier vary sharply (Brazil: 1 expert-tier tie only; Canada/Japan: 5 ties each, including a state-tier founding-coalition tie unavailable to the other four). |

This table is descriptive; it is not converted into a ranking of "coordination strength" or "influence" — see the memo's Interpretation Safeguards.
