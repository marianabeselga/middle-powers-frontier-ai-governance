# Evidence

One file per empirical observation. ID format: `EVD-[XXX]-[NNN]` (e.g. `EVD-JPN-004`), where
`XXX` is the country/actor code (BRA, CAN, IND, JPN, KOR, SGP).

Each record states the evidence itself (as drawn from its Source(s)), which analytical
constructs it supports (C1–C5, S1–S4, or coordination/leverage constructs — see
`/codebook/Codebook.md` §§8–16), its evidence type and strength (§§17–18), and cites the
Source ID(s) it comes from.

Evidence records are the traceability link between `/sources` and the coded judgments in
`/data/countries` and `/data/episodes`: every C/S rating, and every established-coordination
or governance-leverage finding, cites one or more Evidence IDs, and every Evidence ID here
cites the Source ID(s) it was drawn from. See the root README for the full chain.
