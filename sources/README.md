# Sources

One file per cited source. ID format: `SRC-[ORG]-[YEAR]-[NNN]` (e.g. `SRC-AISI-2025-001`).

Each record gives the source's title, authoring institution/actor, publication date, URL or
document location (where the underlying research note specified one), source type (E1
primary official, etc. — see `/codebook/Codebook.md` §17 for the Evidence Type scale), the
country/actor and Episode it relates to, and any notes on how it was used (e.g. where two
sources were consolidated into one record, or a source supports more than one Evidence
record).

Sources link forward to `/evidence` (an Evidence record cites one or more Source IDs) and
are cited from `/data/countries` and `/data/episodes` (which cite Evidence IDs, which in turn
cite Source IDs) — see the root README for the full source → evidence → coding → figure
chain.
