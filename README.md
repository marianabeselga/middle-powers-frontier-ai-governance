[README.md](https://github.com/user-attachments/files/32764428/README.md)
# Middle-Power Coordination and Frontier AI Governance — Reproducibility Package

This repository contains the data, coding, and reproduction code underlying **Figures**
of the article *Turning International AI Red Lines Into Action: The Role of Middle Powers by Mariana Beselga*, a comparative qualitative study of middle-power coordination in frontier AI
governance across six cases: Brazil, Canada, India, Japan, Singapore, and South Korea.

It is a reproducibility package, not the full research repository. It contains what is
needed to trace each figure back to the coded judgment, the evidence, and the source that
produced it, and to reproduce the figures' data-derived content. It does not contain the
full research process (see **Limitations**, below).

## The five figures

| Figure | Title | Reproduces from |
|---|---|---|
| [Figure 1](figures/Fig-RQ1-Capability-Structural-Configuration-Matrix.svg) | Capability and structural-condition configurations by country | `/data/countries` |
| [Figure 2](figures/Fig-RQ2-Participation-vs-Coordination-Gap.svg) | Participation versus established coordination, by Episode | `/data/network` |
| [Figure 3](figures/Fig-RQ2-Actor-Configuration-Network.svg) | Actor-to-configuration coordination network | `/data/network` |
| [Figure 4](figures/Fig-RQ3-Coordination-to-Leverage-Pathways.svg) | Coordination configuration → institutional instrument → governance location → governance leverage | `/data/episodes` |
| [Figure 5](figures/Fig-RQ4-Pathway-Breaks-Comparison.svg) | Where coordination pathways reach, stall, or break | `/data/episodes` |

Original filenames are preserved from the source repository (they use an internal `Fig-RQ*`
naming convention tied to the study's four research questions); the table above maps them to
the article's Figure 1–5 numbering.

## Repository structure

```
/codebook     The single authoritative methodology document (definitions, coding rules,
              scales, decision rules). Nothing in /data departs from it.
/data
  /countries  Six country-level baseline profiles: capability (C1-C5) and structural-
              condition (S1-S4) ratings, each cited to Evidence IDs. Underlies Figure 1.
  /episodes   The four coded coordination episodes (Bletchley Sequence, AISI Network,
              Hiroshima AI Process, GPAI), the cross-case comparison matrix, and the
              results-synthesis draft (figure captions and placement). Underlies
              Figures 4-5, and part of Figures 2-3.
  /network    The relational datasets: documented participation, established coordination
              (direct dyadic ties and hub/configuration ties), edge-validation notes, and
              the network-density/centrality metrics. Underlies Figures 2-3.
/sources      The source register: one file per cited document (title, author/institution,
              date, URL/location, type).
/evidence     The evidence register: one file per empirical observation, each citing its
              Source(s) and stating which analytical construct(s) it supports.
/code         Reproduction scripts (see below) and their machine-readable data extracts.
/figures      The five published figures (SVG), as they appear in the article.
```

## Traceability: source → evidence → coding → dataset → figure

Every quantitative or categorical value in `/figures` traces backward through this chain,
and every step is citable:

1. **Source** (`/sources/SRC-*.md`) — a document: a government report, an official statement,
   an institutional publication.
2. **Evidence** (`/evidence/EVD-*.md`) — one empirical observation drawn from a Source,
   tagged with the analytical construct(s) it bears on.
3. **Coding** — the Evidence is used to assign a rating or finding in `/data/countries`
   (capability/structural-condition ratings) or `/data/episodes` (coordination-mechanism,
   institutionalisation, and governance-leverage findings), per the rules in `/codebook`.
4. **Dataset** — coded findings are compiled into the relational datasets in `/data/network`
   (who participated where; which ties reached "established" coordination) or read directly
   from `/data/episodes`.
5. **Figure** — `/figures` renders the dataset. No figure introduces a value that isn't
   already present at step 3 or 4.

Follow any ID (`SRC-…`, `EVD-…`, `EP-…`, `CTY-…`) through the folders above to walk this
chain for any specific claim in the article.

## How the code reproduces the figures

**No original figure-generation or metrics-computation code is included, because none
survived** — see Limitations. `/code` contains newly written, minimal reproduction scripts
that:

- read the same coded values already in `/data` (via small CSV extracts in `code/data/`,
  each documented in `code/data/PROVENANCE.md` as a direct transcription of a specific
  table in a specific `/data` file — no new data, no new judgment);
- recompute the two network-density statistics in Figure 2 using the same formula and the
  same tool version (`networkx` 3.2.1) the original computation is documented to have used;
- re-plot each figure's data content as a plain, functional chart — not a pixel-accurate
  recreation of the published design.

Running `code/compute_network_density.py` reproduces the documented density values exactly
(0.875–0.917 for participation, 0.133 for established dyadic coordination, including Japan's
0.100 normalised betweenness) — see `/code/README.md` for the full verification table.

```bash
pip install -r code/requirements.txt
cd code
python3 compute_network_density.py          # network-density statistics (Figure 2)
python3 figure1_capability_matrix.py
python3 figure2_participation_coordination.py
python3 figure3_actor_configuration_network.py
python3 figure4_leverage_pathways.py
python3 figure5_pathway_breaks.py
```

Each script writes a PNG to `code/output/`. Requires Python 3.9+, `matplotlib`, and
`networkx` (see `code/requirements.txt`); no other system dependencies.

## Source data, derived data, and reproduction code — the distinction

- **Source data**: `/sources` and `/evidence` — the primary material and the discrete
  observations drawn from it. Nothing here is computed; it is transcribed and cited.
- **Coded/derived data**: `/data` — analytical judgments (ratings, established-coordination
  findings, institutionalisation levels) applied to the source data under the Codebook's
  rules, plus the relational datasets compiled from those judgments. This is the
  research's actual analytical output, not raw material.
- **Reproduction code**: `/code` — newly written for this package (explicitly marked as
  such in every file's header and in `/code/README.md`), used only to recompute the two
  density statistics and to re-plot the figures' data content from the coded/derived data
  above. It performs no coding, no new analysis, and no reinterpretation.

## Limitations

- **Original code is not available.** The scripts that computed the network-density
  statistics and generated the published SVG figures ran in a temporary environment that
  was never version-controlled; it no longer exists and could not be recovered. The
  scripts in `/code` are new reimplementations built only from the data and formulas
  already documented in this repository (see `/code/README.md`) — they reproduce the
  published values exactly, but they are not the original code.
- **This is not the full research repository.** Four categories of material are
  deliberately excluded: (1) a full decision-by-decision audit trail and ID log,
  (2) preliminary Stage 1 reading notes, (3) an earlier candidate-episode screening
  matrix from before the four Episodes in this package were selected, and (4) two
  in-progress internal methodological memos. None of this is needed to trace or
  reproduce Figures 1–5, and omitting it keeps the public package focused and avoids
  publishing internal working material. The frozen coded records themselves — country
  profiles, episode records, evidence, sources, and relational datasets — are included
  in full and unaltered.

  Because of that, a number of citation-style cross-references *inside* the included
  files (things like "see the Coding-Decisions-Log entry for 2026-09-03," or a rationale
  citing a "MEM-METHOD-001 Resolution") point to one of the four excluded categories
  above and will not resolve within this package. These are pointers to *supporting
  detail*, not gaps in the data itself — every rating, finding, and figure value is
  fully stated and cited to its Evidence/Source ID within the included files. The one
  partial exception is a handful of methodological rationales in the Bletchley Sequence
  episode record that reference a "MEM-METHOD-001 Resolution" when explaining why a
  specific leverage (L) finding was re-verified; the applied test itself is quoted
  inline from Codebook §14, but the memo document that originally produced the
  clarification is not included.
- **Figure reproductions are not pixel-identical to the published figures.** They use
  plain default styling and reproduce data content, layout logic, and category values,
  not the original custom visual design.
- **Named individuals.** A small number of Evidence/dataset entries name individual
  members of public multilateral working groups (e.g. GPAI Expert Working Group
  members), drawn from those groups' own public rosters/reports, in their professional
  capacity. No private or contact information is included.

## Citation

If you use this repository, please cite: Beselga, Mariana. (2026). *How Middle Powers Shape Frontier AI Governance: Replication Package.*
