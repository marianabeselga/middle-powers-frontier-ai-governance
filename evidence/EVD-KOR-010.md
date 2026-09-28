---
id: EVD-KOR-010
type: evidence
country_actor: CTY-KOR
episode_id:
source_ids: SRC-MSIT-2025-001, SRC-MSIT-2025-002, SRC-MSIT-2025-003, SRC-OECD-2025-003
evidence_type: E1
evidence_strength: ES1
constructs: S1
---

# EVD-KOR-010 — Korea's AI-compute expansion: quantified current infrastructure, large planned scale-up, and NVIDIA-concentrated hardware dependence

## Evidence (from Source)

**Current, operational capacity:** the Gwangju AI Data Center operates 880 H100 GPUs, of which 416 are government-secured and used to support AI development across industry, academia, and research institutions (MSIT, 20 February 2025).

**Near-term planned capacity:** the government has set a target of 18,000 high-performance GPUs by the first half of 2026 (10,000 via public-private cooperation; 8,000 via Supercomputer No. 6). Supercomputer No. 6 is planned with 8,496 NVIDIA GPUs (including GH200 units), a projected peak performance of 600 petaFLOPS, and 205 PB of storage, explicitly intended for frontier AI research, foundation-model development, and large-scale training/inference — **not yet operational**.

**Longer-term announced target:** Korea subsequently announced plans to secure more than 260,000 NVIDIA GPUs (~50,000 public sector; 200,000+ private sector, including Samsung, SK Group, Hyundai Motor Group, and NAVER) — an **announced target, not current or committed-and-built capacity**.

**Domestic semiconductor capacity:** Korea is developing a National AI Computing Center ("AI Highway") and has domestic AI-semiconductor design firms (SAPEON Korea, Rebellions, FuriosaAI). An earlier target of 50% domestic AI-chip use within the National AI Computing Center by 2030 was subsequently loosened toward a more flexible public-private adoption model.

**Dependence:** OECD's Roundtable on Competition in AI Infrastructure describes the Korean AI-semiconductor market as "led by NVIDIA," reflecting NVIDIA's technological capability, production capacity, and market demand. Every GPU figure above (880 current; 8,496 in Supercomputer No. 6; 260,000+ announced target) is NVIDIA hardware — Korea's flagship national compute infrastructure, at every scale documented, currently depends on foreign-designed accelerators.

## Constructs supported

- **S1 — Compute/infrastructure:** assessed against Codebook §16 and §18, distinguishing current operational capacity from planned/announced targets (per explicit instruction not to treat the two as equivalent):
  - *Domestic infrastructure and compute capacity:* substantial and quantified — 880 H100 GPUs currently operational (Gwangju), with an actively expanding National AI Computing Center. Enabling, and now supported by concrete, current-tense E1 evidence (an evidentiary upgrade from the prior general characterisation in [EVD-KOR-005](EVD-KOR-005.md)).
  - *Actual/planned access to frontier-relevant compute:* current operational scale (880 GPUs) is modest in absolute frontier-AI terms; planned scale (18,000 by H1 2026; 260,000+ as a longer-term announced target, not yet built) is substantial and well-funded, with significant private-sector co-investment (Samsung, SK, Hyundai, NAVER) evidencing genuine execution capacity, not merely aspirational language. The 260,000-GPU figure is explicitly treated here as an **announced target**, not current or committed-and-built capacity.
  - *Domestic semiconductor and related technological capacity:* real, named domestic AI-chip design firms exist (SAPEON, Rebellions, FuriosaAI), but the domestic-content mandate for Korea's own flagship National AI Computing Center was *loosened*, not strengthened, indicating domestic AI-chip capacity is not yet relied upon at the scale of Korea's own compute ambitions.
  - *Dependence on foreign GPUs/chips:* explicit and specific — every documented GPU figure (current and planned) is NVIDIA hardware; the Korean AI-semiconductor market is OECD-characterised as NVIDIA-led. This is a materially more specific and quantified dependence finding than the general "embedded in international supply chains" language previously on file.
  - *Whether this dependence is a material structural constraint:* the evidence documents dependence on foreign chip *design/manufacture*, but does **not** document a constraint on Korea's *access* to that hardware — on the contrary, Korea is shown successfully securing, deploying, and rapidly scaling acquisition of large GPU volumes, with committed government funding and substantial private-sector capital. This is a dependence-on-sourcing configuration, not a demonstrated access-denial or capacity-ceiling configuration (distinguishing dependence from lack of access, per the assessment framework). It differs in kind from Singapore's evidence, which is a direct government admission of an inability to compete in assembling compute at scale (a demonstrated access ceiling), and from Japan's evidence, which documents a specific current-tense domestic-control shortfall (only ~30% of Japan's cloud market is domestically controlled today).
  - **This supports retaining S1 — Enabling**, now on a substantially stronger, quantified, primary-source (E1/ES1) evidentiary basis than before. **Korea is not technologically autonomous**: Korea's S1 condition is Enabling because substantial and expanding domestic and planned access to compute and related infrastructure, combined with significant (if not yet frontier-chip-manufacturing) semiconductor capabilities, provides strong access to relevant technological resources; this enabling condition remains qualified by Korea's dependence on internationally supplied frontier accelerators and other components of the global AI technology supply chain.

## Notes

**Current vs. planned, kept explicit:** only the 880 H100 GPUs (Gwangju) and the existing domestic AI-chip design firms represent currently operational/existing capacity. Supercomputer No. 6 (8,496 GPUs) and the 18,000-GPU and 260,000+-GPU figures are planned or announced targets, not yet built or committed capacity, and are not treated as equivalent to current capacity in this assessment.

**Relationship to prior evidence:** this record supersedes [EVD-KOR-005](EVD-KOR-005.md)'s S1 discussion as the primary quantified basis for the S1 rating, while EVD-KOR-005's C3/S2 content and its qualitative OECD-sourced S1 characterisation remain valid background; EVD-KOR-005's own S1 "visible uncertainty" flag (absence of a quantified GPU/accelerator dependence figure) is now substantially addressed by this record's quantified figures, though the current-vs-planned distinction should still be tracked if the rating is revisited in future.
