# K684 — Over-claim sweep: pre-discipline landmines that must be corrected BEFORE any external outreach. Smoking gun: three incompatible "derived" δ_CP values.

**Keeper | 2026-07-14 | Triggered by deprecating BST_CKM_CPPhase_Derivation.md (a March-2026 "all CKM derived, zero free parameters, no fitting" note contradicted by F498's proved J=0). Swept for siblings. Found ~9 documents (several EXTERNAL-facing, several machine-read) asserting derivations the current honest state holds at lower tiers. "Nothing goes to external reviewers without Keeper's pass" — this is that gate.**

## The smoking gun
The corpus carries **three mutually incompatible "derived" values for δ_CP**: 12π/7 ≈ 309° (Neutrino note, registry T329), 3π/7 (registry T2018, data layer), and π (the CP doc, MixingMatrices body). One observable cannot have three forward derivations — this is proof the phase was **reverse-fit**, and it is the single cleanest line to cite when deprecating any CP-phase over-claim. δ_CP is OPEN (can-fail); only "CP violation exists" is structural (F498).

## Prioritized list (most severe first)
### TIER 1 — EXTERNAL-FACING (deprecate/banner)
1. **`BST_Neutrino_Predictions.md`** (targets JUNO/DUNE) — "zero-parameter," δ_CP=309° as forward prediction, coeffs {7/12,10/3} as derived, θ12=1/3, neutrinos Dirac. Violates: δ_CP OPEN, coeffs FITTED, θ12=3/10, Majorana. **→ DEPRECATED (banner added this session).** Highest risk — a false "prediction for DUNE" would get BST falsely falsified.
2. **`BST_Nuclear_Physics_Paper.md`** (targets PRD/NPA) — arctan(√5) CP "no free parameters." **→ NEEDS banner scoped to the CP passages (:297,305,344).** [Lyra/Keeper]
3. **`BST_CKM_PMNS_MixingMatrices.md`** — header "all six mixing angles, zero free parameters" while θ23 octant + CKM CP OPEN (body is honest). **→ EDIT the status line (:11), don't full-deprecate.** [Grace/Lyra]

### TIER 2 — DATA LAYER (machine-read by verify_bst.py + outreach — demote tiers) [GRACE owns data/]
4. **`data/bst_constants.json`** — four live tier-D violations:
   - CKM CP phase (:812-841) `tier:D, derived, atan(sqrt(n_C))` — **re-blessed 2026-07-12**, contradicts F498. → **demote Open/Conditional.**
   - α (:127-149) `tier:D`, mechanism "Wyler integral" (:144) — Wyler ¼ RETIRED (Robertson trap); α is IDENTIFIED-strong/nearly-proven. → **demote to nearly-proven; drop the Wyler chain, cite the charge-count/capacity + scale-falsifier (K681).**
   - PMNS θ12 (:4925) `tier:D` for 4/13 — current is 3/10 identified. → **demote.**
   - PMNS CP (:4954) `tier:D, derived, 3π/7` — the note already says "retire, not a bank" but the FIELD was never updated. → **fix field to Open.**
   - Header (:5) "all constants derived… zero free parameters" — soften.

### TIER 3 — LOAD-BEARING INDICES (demote; they propagate) [KEEPER owns the registry]
5. **`BST_AC_Theorem_Registry.md`** — T329 (:413/759: δ_CP=309°, θ12=1/3, "complete sector," Proved) + T2018 (:2745: all PMNS, δ_CP=3π/7, "ZERO free parameters," PROVED). → **demote both from PROVED.** [Keeper next pass]
6. **`BST_Architectural_Audit.md`** (:67, D-14) — CKM CP arctan(√5) "DERIVED" (ironic — the honesty audit itself is stale). → **demote row.** [Keeper — my doc]
7. **`BST_Koons_Substrate_Constants.md`** (:4,170) — arctan(√5) DERIVED + "zero free parameters." → **flag/demote CP row.** [Keeper/Grace]

### TIER 4 — EXTERNAL BUT DISCIPLINED (freshness banner, NOT deprecate)
8. **`BST_Paper_106_v0.4_assembled.md`** — "no parameter is fit / zero free parameters," but frames as identifications with explicit open sections. → **freshness banner** (as-of-2026-07: α identified-not-derived, CKM CP + θ23 octant OPEN, forced count 2/26). [Lyra]
9. **Outreach one-pagers** (`BST_Outreach_OnePage_v0.1/v0.2`) + CLAUDE.md/README tagline "zero free parameters" — v0.2 partly hedged ("relative to D_IV⁵ classification"). → **lowest priority; align headline before outreach.** [Casey/Keeper]

### Checked and HONEST (do NOT flag)
`grace_F437_...zero_parameters` (title loud, body STRUCTURAL 5-8% no bank); `bst_constants.json` m_τ entry (tier S, gap noted). Leave alone.

## Actions
- **DONE this session:** deprecation banners on `BST_CKM_CPPhase_Derivation.md` and `BST_Neutrino_Predictions.md` (the two worst — external, CP reverse-fit, contradict F498/Majorana).
- **KEEPER next:** demote registry T329/T2018 from PROVED; fix `BST_Architectural_Audit.md` D-14; banner `BST_Nuclear_Physics_Paper.md` CP passages.
- **GRACE (owns data/):** the four `bst_constants.json` tier-D demotions — HIGHEST remaining risk (machine-read, CKM-CP re-blessed 07-12). Do before any `verify_bst.py`-based outreach.
- **LYRA:** freshness banner on Paper 106; scope the MixingMatrices status line.

## Standing rule (reaffirmed)
**No BST document goes to an external reviewer, experiment, or arXiv/Zenodo without a Keeper pass against the current scorecard.** These landmines are all pre-discipline (March–April 2026) and survived because nobody swept the old external/data-layer docs when the tiers tightened. The discipline is now retroactive: the honest tiers must propagate to every doc a referee could read, especially the data layer and the "predictions for experiment X" papers. The three-δ_CP-values inconsistency is the cautionary exemplar — a single reverse-fit, asserted three ways, sitting in an experiment-facing paper.

— Keeper K684, 2026-07-14. Over-claim sweep: ~9 pre-discipline landmines. 2 worst deprecated (CP doc, Neutrino_Predictions). Data layer (Grace) is the highest remaining risk (tier-D α-via-Wyler + CKM-CP-arctan√5, machine-read). Smoking gun: 3 incompatible "derived" δ_CP values (309°/3π/7/π) = reverse-fit proof. Nothing external without a Keeper pass. See [[Keeper_K682...]], [[Keeper_26_Parameter_Scorecard_v0.1_2026-07-12]].
