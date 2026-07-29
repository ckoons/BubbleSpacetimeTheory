---
id: grace_data_layer_dedup_pass_authoritative_fermion_table_29p_2026-07-29
date: 2026-07-29
program: TEGMARK
status: current
supersedes: []
superseded_by: null
topic_tags: [dedup, data-layer, fermion-sector, authoritative-table, engine-fire, blind-bar, m_c, m_t, 29p]
claims:
  - id: this-a
    topic: pre-fire data-layer dedup pass — reconciled the m_c and m_t duplicate ledger entries and compiled the single authoritative fermion-observable table Keeper rules the ~13 engine outputs against
    status: current
    superseded_by: null
    date: 2026-07-29
---

# [TEGMARK] Data-layer DEDUP pass before the engine fire (29p) — one authoritative number per fermion observable

*Grace | 2026-07-29 | 29p task: "Grace does the data-layer dedup pass before the fire so Keeper is ruling against clean numbers." One kernel → ~13 outputs, so an ambiguous ledger (two m_c's at conflicting tiers) would corrupt the σ-check. Scanned by exact symbol; two real duplicates found and reconciled; the rest single-entry clean.*

## Duplicates found + reconciled (backup .bak.20260729p_dedup)
- **m_c — two entries, conflicting tiers:** const_109 (older RFC charm/strange form, 0.6%, tier D) vs const_158 (y_c=α, 0.05%, tier **I — stale**). K997 banked m_c = α·v/√2 (y_c=α) as **DERIVED**. → **const_158 made AUTHORITATIVE, tier I→D**; const_109 stamped `duplicate_of: const_158` (retained for provenance, NOT used for the σ-check). Rule against const_158.
- **m_t — two entries (ceiling vs value):** const_157 (y_t=1 boundary saturation, 174, tier I) vs const_040 ((1−α)·v/√2, 172.75, 0.037%, tier S). These are the honest **Ceiling/Value split**, not rivals. → **const_157 made AUTHORITATIVE tier-home** = **CEILING:DERIVED (y_t≤1 ⟹ ≤174) / VALUE:IDENTIFIED (172.7 via the (1−α) correction, const_040)**; const_040 stamped `value_form_of: const_157`. Rule m_t as one via const_157.
- All other fermion observables (m_u, m_d, m_s, m_b, lepton ratios, CKM/PMNS in the 26-map): single-entry, clean.

## ★ AUTHORITATIVE fermion-observable table — Keeper rules the ~13 engine outputs against THESE
| observable | observed | current BST (prior) | authoritative tier |
|---|---|---|---|
| m_u | 2.16 | 2.168 | D |
| m_d | 4.67 | 4.697 | D |
| m_s | 93.4 | 93.95 | D |
| **m_c** ★ | 1270 | 1269 | **DERIVED** (y_c=α, K997) |
| m_b | 4180 | 4146 | D |
| **m_t** ★ | 172.69 | 174 (ceiling) / 172.75 (value) | **CEILING:DERIVED / VALUE:IDENTIFIED** |
| m_p/m_e | 1836.153 | 1836.118 | DERIVED (K992, 6=C₂·π⁵) |
| m_μ/m_e | 206.768 | 206.761 | DERIVED (e=n without counterexample) |
| m_τ/m_e | 3477.48 | 3483.8 | IDENTIFIED-FINAL (71 bounded) |
| m_s/m_d | 20 | 20 | DERIVED (K993) |
| m_c/m_s | — | — | DERIVED (K997) |
| m_u/m_d | — | — | DERIVED |
| m_t/m_b | — | — | DERIVED |
| V_us | 0.2243 | 0.2236 | DERIVED (K994, 1/√20) |
| V_cb | 0.041 | 0.044 | DERIVED (2-3-mode 3D-projected, w/o counterexample; conf. structural) |
| V_ub | — | — | IDENTIFIED |
| δ_CKM | — | — | IDENTIFIED |
| θ12 PMNS | — | — | IDENTIFIED |
| θ23 PMNS | — | — | IDENTIFIED |
| θ13 PMNS | — | — | DERIVED |
| δ_PMNS | — | — | DERIVED |

**How Keeper uses this:** the engine fires ONE kernel → ~13 predictions. Compare each engine output to the **observed** column at σ. The **prior BST** column is the consistency anchor (the engine should reproduce these where they already Derived — e.g. m_s/m_d=20, V_us, m_c); a divergence from a prior Derived is a flag. The **tier** column is the current record the whole-sector Derived must not silently downgrade. No observable now has two conflicting ledger numbers → the σ-check is unambiguous.

## Handoff
- **@Keeper** — rule the ~13 outputs against the `observed` column at σ; this table is the clean target. m_c=const_158, m_t=const_157 are the authoritative homes.
- The blind bar (all ~13 at σ, zero dials → Derived; soft-clean suspicious; provenance-gated) is committed in [[grace_mixing_lemma_hung_plus_checker_half_committed_blind_29o_2026-07-29]].

— Grace, 2026-07-29 [TEGMARK]. Pre-fire dedup: m_c reconciled (const_158 y_c=α DERIVED authoritative, tier I→D; const_109 duplicate_of), m_t reconciled (const_157 Ceiling:D/Value:I home; const_040 value_form_of). Authoritative fermion table compiled — Keeper rules the ~13 engine outputs against the observed column at σ, no conflicting numbers remain. Ledger backup .bak.20260729p_dedup.
