# Relational Data

Implements Codebook §24 (Relational Data and Future Analysis). The schema below is **unchanged** from the Codebook — this file documents it and states the approval safeguard for extending it; it does not introduce anything new.

## Current schema (Codebook §24, verbatim)

**Node types:** STATE, COALITION, MECHANISM, INSTRUMENT. Capabilities (C), structural conditions (S), governance leverage (GL), and red-line relevance (RL) are attributes of states/episodes/edges, not nodes.

**Edge attributes (minimum):** source node; target node; node type; relationship type; direction; date or temporal sequence; Episode ID; Evidence ID; Source ID.

**Relationship types:** coalition-building; information sharing; regulatory coordination; technical coordination; diplomatic coordination; joint monitoring; coalition membership; institutional linkage; instrument adoption or implementation.

*(In the original research repository, a `Nodes.md`/`Edges.md` pair implements this schema as a live register per the Codebook's own field list above. Both were empty placeholders at the time this package was prepared — the actual populated relational data for Figures 2–3 is in `Stage5-Dataset1-Participation-Access.md` and `Stage5-Dataset2-Established-Coordination.md` in this same folder, and the machine-readable extracts used by the reproduction code are in `/code/data`.)*

## How this data gets populated

Node and edge records are derived **from approved underlying Source/Evidence/Episode records** — they are not something the researcher manually populates while screening candidate episodes (a separate, earlier screening stage not included in this package; see the root README's Limitations section). Every derived node or edge must remain traceable to the Episode ID, Evidence ID, and Source ID it came from. Do not create a relationship that isn't supported by empirical evidence, and do not add one solely to make a network diagram richer (Codebook §24.3).

Co-participation in the same forum or initiative is not, by itself, coordination, mobilisation, governance leverage, or causal influence — network position or connectivity must never be treated as evidence of any of these on its own (Codebook §23 Stage 2, §24.4).

## Safeguard: no new methodological constructs for network analysis

Before creating a new network dataset schema — new fields, new node/relationship types, or any new scale — the schema must be **proposed to the researcher and approved** before implementation. In particular, do not introduce new scales for tie strength, coordination intensity, leverage, influence, or causal importance unless the researcher explicitly authorises them and they are incorporated into the Codebook itself. The existing STATE/COALITION/MECHANISM/INSTRUMENT node types and the relationship-type list above are the only ones currently authorised.

### Edge weight/count — proposed 2026-08-30, declined

A simple **edge weight** (a count of distinct Evidence IDs supporting the same source–target–relationship-type triple) was proposed as a possible future schema addition. **The researcher declined to add it to the canonical schema (2026-08-30).** `Edges.md` therefore has no `edge_weight` (or equivalent) column, and none should be added without a future, separate approval.

If a weighted-tie view is needed later for network analysis, it may be calculated as a **derived analytical measure** computed from the already-approved Edge register (e.g., counting existing Evidence IDs per source–target–relationship-type triple) — without modifying the canonical Edge schema itself. Any such derived measure must remain traceable to the underlying Episode/Evidence/Source IDs it was computed from, and must not be treated as a new Codebook construct, an authoritative Codebook scale, or evidence of tie strength, coordination intensity, leverage, influence, or causal importance. Any future change to the canonical schema still requires explicit researcher approval.

## Descriptive, not causal

Network analysis under this schema is descriptive and relational only. It supports patterns of co-participation and potential configurations (Codebook §23 Stage 2) and downstream visualisation (Codebook §24.5); it does not itself establish coordination, causal mechanisms, or governance effects, and it does not determine the coding of evidence.
