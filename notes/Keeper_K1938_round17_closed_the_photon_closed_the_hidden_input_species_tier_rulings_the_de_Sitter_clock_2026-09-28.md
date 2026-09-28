---
node_type: k_audit
id: K1938
title: "Round 17 closed (written 09-28; Casey left before EOD on 09-27, and the work was on disk and pushed). (A) The photon is CLOSED: H² has no conformally covariant coupling to the photon through its records, of any kind (Cal Section 1012: a covariant map restricts to (𝔤,K)-maps between irreducible Harish-Chandra modules, and the photon is not tempered, so the map is zero; the family premise was corrected by Cal and owned by Grace). (B) The hidden-input species is 12 rows, not 1 (Elie 5840 swept all 197 rows and read every flagged one; Grace fixed each face). Keeper's tier rulings are below; the explorer and verify_bst now show it. (C) The de Sitter clock: J is exact only as Λ → 0. The Time, Derived parenthesis is drafted, with Cal's arrow question first and then Casey's word."
date: 2026-09-28
author: Keeper
rubric_cell: "External — the data layer's honesty (hidden inputs named on the face); Internal — mechanism open (the photon closed); presentation"
---

# K1938 — Round 17 closed

## Part 1 — Rulings (Grace R176 b1349536, R177 0e794d22, 2dd15044; Elie 5840 25f8e777; Lyra R17 15f0c7da, toy 5841 3/3; Cal Section 1012 b1b530b3)
1. **The photon: CLOSED.** Every covariant route between H² and the photon is closed:
   - odd vertices, by the central characters (K1935);
   - the H² H² pair, by lowest weights (Cal Section 1009);
   - the current (J·A) and field-strength (F·O) couplings, because a covariant map from the tempered records into the photon's distribution vectors restricts to (𝔤,K)-maps between irreducible Harish-Chandra modules, and the photon is not tempered, so the map is zero (Cal Section 1012). One disintegration pin is owed (Grace: CCH Thm 6.6 = HC 38.1 already staged).
   - **The family premise, corrected:** the records are spherical for SO(5,2), and their restriction to SO(4,2) is tempered but NOT necessarily spherical (Cal). Grace owned her R175/R176 use of "spherical" as a link. The rule "state the family" failed one round after it was written, and was caught.
   - **A photon coupling needs the breaking.** Together with K1936: every charge, every mass and every photon vertex enters through the breaking scale.
2. **The hidden-input species (Keeper found H₀ on 09-27; the sweep made it a class).** Elie 5840 swept all 197 rows of `data/bst_constants.json`, flagged 57, and read every flagged row. It found 10 species rows (H₀ as the control), 2 weak, 1 empty (Γ_Z), and one text-only slip (m_W). Grace added a₀ (a symbol-only import that no literal sweep can see). **Elie's own miss:** he predicted the m_p rows would be the largest cluster; they are clean, because m_p = 6π⁵ m_e is BST's own. His run-1 whitelist leaked (no size limit on "simple fractions"), was caught by reading what it let through, and was kept.
   - **Cal's gap in the prereg, which must be closed before anyone cites the count:** the sweep exempted 137.036 as "α, identified". **BST's identified value is 137; 137.036 is the MEASURED α⁻¹,** so a row using it is exactly this species. Literal scanning also misses imports by variable reference (a₀). **Owed: 5840b, a separate hash, before its results are read.**
3. **Keeper's tier rulings** on Grace's recommendations. A ruling is not an edit: Grace applies each one; Cal concurs or objects.

| row | ruling |
|---|---|
| const_100 H₀ | **I → "consistency (Ω_m)"; H is NOT a BST prediction.** ω_m h² = 0.1430 is named. The precision field measures Ω_m's agreement. |
| const_101 T₀, const_102 t₀, const_046 a₀ | **inherit H₀:** consistency rows, with ω_m named. **t₀: the stored 13.78 does not reproduce (its own formula gives 13.81). Store the formula's value, or retire the row. Never keep a number the row cannot produce.** |
| const_110 m_b | **I** (the identified ratio m_b/m_τ = 7/3; m_τ measured, named). Not D. |
| const_123 √σ | **SUSPENDED, not citable:** code (441.36, uses measured m_π) ≠ chain (434.33) ≠ stored (441.0). Resolve one form or retire the row. |
| const_082 f_π | **SUSPENDED:** the literal 140.2 is unsourced. Source it or retire the row. |
| const_114 γ_p | **not a BST derivation as coded** (a unit conversion of CODATA's μ_p). Recode from BST's μ_p (const_043) or reclassify as a conversion. |
| const_113 Faraday | **REMOVED from the derived tiers:** the SI definition N_A·e restated, not a BST result. |
| const_037 z_rec, const_038 r_s | **not D until h and T_CMB are named;** then "consistency, inherited". |
| const_031 C–H, proton radius | **recode with BST's own inputs** (Ry = m_e/(2N_max²) = 13.6128 eV; m_p = 6π⁵ m_e). Both still match (0.07 %; 0.001 %). |
| const_115 Γ_Z | name G_F and m_Z (measured); no D until a formula exists. |
| const_012 m_W | text fix only (the chain writes 938.272; the code uses BST's m_p). |

4. **Presentation (Keeper, done, c930936b):**
   - `verify_bst.py`: D_e(C–H) now uses BST's own Rydberg (it was the measured 13.6057), and still passes at 0.07 %.
   - The explorer prints **MATCH\*** with the row's status whenever the status says the weight is an imported measurement, and counts those separately (8 rows today: H₀ among them; T187 still PASS).
   - **Zenodo is unaffected:** no staged document cites an affected row (Lecture 05 already lists the string tension as imported).
5. **The de Sitter clock (Lyra R17, 5841 3/3):**
   - Λ > 0 fixes a timelike vector in J's plane, so J ∉ so(4,1), and the surviving time is a de Sitter boost (continuous spectrum).
   - H²'s ladder is unchanged as kinematics, and approximate as dynamics to order H/E (no value computed, per the no-scan rule).
   - The odd-H² prohibition and the mod-2 label are exact only as Λ → 0.
   - SO(4,2) → SO(4,1) branching was not computed; the naive m²/H² = Δ(3 − Δ) fails for Δ ≥ 7/2 (a pin is owed).
   - **The Time, Derived parenthesis is DRAFTED, not applied** (it would be v1.5). **Cal's question first:** does the paper's arrow argument need J CONSERVED? If so, the arrow also holds only to order H/E, and the draft's last clause changes. **Then Casey's word.**

## Part 2 — Round 18 (today, 09-28): the TOMORROW file carries the prompt
