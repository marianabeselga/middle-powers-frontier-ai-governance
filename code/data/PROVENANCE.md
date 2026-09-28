# Data extract provenance

**These CSV files are newly created for this reproduction package.** They did not exist in the original research vault. Each is a direct, verbatim transcription of a table already present in the markdown records under `/data`, `/sources`, and `/evidence` — no value has been changed, added, inferred, or recalculated by hand. They exist only so the scripts in `/code` can read structured input instead of parsing markdown prose.

If anything below looks inconsistent with the source record, the source record under `/data` is authoritative — please open an issue rather than trust the CSV.

| File | Transcribed from | Section |
|---|---|---|
| `capability_structural_matrix.csv` | `/data/countries/CTY-*.md` (all 6) | "Capability Profile (C1–C5)" and "Structural Conditions Profile (S1–S4)" tables, Assessment column only (evidence citations and justification prose omitted — see the source file for those) |
| `participation_matrix.csv` | `/data/network/Stage5B-Network-Metrics-Dataset.md` | §1, "Bipartite participation/access network" table |
| `direct_coordination_edges.csv` | `/data/network/Stage5-Dataset2-Established-Coordination.md` | Table 2A — Established, genuinely dyadic (state-to-state) coordination |
| `hub_coordination_edges.csv` | `/data/network/Stage5-Dataset2-Established-Coordination.md` | Table 2B — Established coordination represented via a MECHANISM/COALITION/INSTRUMENT hub node |
| `leverage_pathways.csv` | `/data/episodes/Stage4-Cross-Case-Matrix.md` | §1 and §1a (Institutionalisation levels), cross-referenced with the Results Synthesis Draft's "Episode → coordination configuration → institutional instrument → governance leverage" table |
| `pathway_breaks.csv` | `/data/episodes/Stage4-Cross-Case-Matrix.md` | §4 ("Comparing the breaks") and §9, cross-referenced against the four Episode records' own GL findings |

## Known simplifications

- `capability_structural_matrix.csv` keeps only the short assessment code (e.g. `STR`, `MOD`, `LTD`, `MIX`, `ENB`) per construct. The full justification, evidence IDs, and confidence notes are in the source country-profile files and are not duplicated here — consult those for the reasoning behind any single cell.
- `direct_coordination_edges.csv` omits the free-text "Institutional instrument/output" and "Note" columns present in the source table; see `Stage5-Dataset2-Established-Coordination.md` Table 2A for that context.
- The `—` em-dash in two hub names ("GPAI Expert Working Group — Innovation & Commercialisation" / "— Responsible AI") is rendered as a plain hyphen in the CSV for encoding safety; this is a formatting change only, not a content change.
