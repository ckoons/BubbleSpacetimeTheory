# K735 — Casey's two-isomorphic-spheres basis-change reading of √rank DISSOLVES the K734 unequal-ruler worry, RECONCILES Lyra's 1/3-vs-3/13, and NAMES "where the two things meet." The √rank is |Y| = √(1²+1²) — the hypercharge is the diagonal (1,1) over two ISOMORPHIC spheres (charge + color), so the two projections are EQUAL and √2 is clean. Corroborated independently by Lyra's Killing-form ‖Y‖²=rank. Not yet closed: is Y=(1,1) FORCED by the boundary product (S⁴×S¹)/ℤ₂?

**Keeper | 2026-07-17 | Casey reframed the "two rulers" mid-recursion; I put it into explicit linear algebra and it reconciles the three competing numbers. Crediting Casey — this is his insight resolving my own K734 flag.**

## What Casey said (the reframe)
"Two different spheres, one for charge and the other for color — not identical, **isomorphic**. √2 feels like two different projections, 1+1 added together to be normalized. Look at the linear algebra and vectors — they are a product of something, a **basis change** occurs, and that's the normalization."

## Why this DISSOLVES K734
- K734's worry: "two rulers → √rank" assumed the two rank-2 Cartan directions are equal, but they're ρ-weighted & **unequal** (5/2, 3/2), so the factor might not be exactly √rank.
- Casey's fix: **the two rulers were never the ρ-components.** They are two **isomorphic** spheres — the charge sphere (S¹ = the SO(2) circle) and the color sphere (the N_c structure). Isomorphic ⇒ **equal weight** ⇒ the hypercharge as a diagonal (1,1) vector has |Y|² = 1²+1² = 2 = rank **cleanly**. The unequal-ruler problem never arises because we're not summing the unequal Cartan directions — we're combining two equal isomorphic-sphere projections. K734 worry retired.

## The linear algebra (verified, `two_spheres_basis_change.py`)
- **Fermion trace, one generation** (color multiplicity N_c on quarks): ΣT₃² = 2, ΣY² = 10/3.
  - c² = 1 → sin²θ_W = **3/8** (forbidden GUT). c² = rank → sin²θ_W = **3/13** (BST, obs 0.2312). The entire 3/8→3/13 shift is exactly **c² = rank on the hypercharge**.
- **Casey's mechanism for c² = rank:** hypercharge threads BOTH spheres (quarks carry hypercharge AND color) → **Y = (1,1)** → |Y|² = rank; T₃ lives on ONE sphere → |T₃|² = 1. Basis-change normalization **c² = |Y|²/|T₃|² = rank.** Because the spheres are isomorphic, the (1,1) projections are equal and √2 is exact.

## Independent corroboration (Lyra's own Killing form)
Lyra's pure-gauge Killing computation found ‖T₃‖² = 1, ‖Y‖² = 2 = rank **all by itself**. So |Y|² = rank is already in the Lie-algebra Killing form — **Casey's two-sphere (1,1) picture is the geometric MEANING of that result.** Two independent supports for |Y|²=rank now: (a) Killing form; (b) two-sphere basis change.

## RECONCILES the three numbers (this is the payoff)
| value | what it is | why |
|---|---|---|
| **1/3** | pure gauge Killing, NO fermion content | Lyra's clean-but-wrong number — the gauge ratio without the physical fermion trace |
| **3/8** | fermion trace (color sphere present) with c²=1 | forbidden GUT |
| **3/13** | fermion trace (COLOR sphere) × c²=rank (CHARGE sphere) | BST — lives where the **two isomorphic spheres meet** |
Lyra's caution (the clean gauge number is 1/3, not 3/13) is fully absorbed: 1/3 is the gauge ratio with **no fermions**; the physical angle **requires** the fermion trace (standard EW — hypercharge normalization is fixed by fermion content, not the gauge Killing form alone). Casey's picture says WHY both are needed: the **color** sphere is the N_c in the fermion trace, the **charge** sphere is the √rank basis change. **3/13 = their product.** This is exactly Lyra's "it lives where two things meet" — now NAMED — and it IS Casey's weak-color coupling (K731), made mechanical.

## Honest tier
- **RESOLVED:** the K734 unequal-ruler objection (isomorphic ⇒ equal ⇒ √2 clean).
- **RECONCILED:** Lyra's 1/3 vs BST 3/13 (gauge-ratio-without-fermions vs fermion-trace-with-c²=rank).
- **STRENGTHENED:** the √rank lead now has TWO independent supports (Killing form + two-sphere basis change) and a concrete linear-algebra mechanism (basis change, (1,1) diagonal).
- **STILL OPEN (the derivation):** is **Y = (1,1) diagonal over the two isomorphic spheres FORCED** by the boundary product structure (S⁴×S¹)/ℤ₂ of D_IV⁵ (equivalently: does the geometry force ‖Y‖²=rank in the Killing form)? If yes → c²=rank forced → sin²θ_W = 3/13 **DERIVED**, target-innocent. sin²θ_W stays **reduced-to-√rank-lead**, NOT one-norm-away (Lyra's re-tier stands) — but the lead is now sharper AND better-supported than at K733/K734.

## Handoff
The marquee is re-pointed (better than K733's single-norm target): **the basis change between the two isomorphic spheres.** Lyra — is the hypercharge forced to be the (1,1) diagonal over (charge-sphere, color-sphere) by the boundary product? Elie — verify the Killing ‖Y‖²=rank independently and check c²=rank against the 3 bars. This is Casey's linear-algebra steer ("basis change is the normalization") made concrete.

— Keeper K735, 2026-07-17. Casey's two ISOMORPHIC spheres (charge + color) → Y=(1,1) diagonal → |Y|²=rank cleanly (√2 = √(1+1), equal projections) → dissolves K734's unequal-ruler worry. Fermion trace: c²=1→3/8, c²=rank→3/13 (verified). Reconciles Lyra's 1/3 (gauge, no fermions) / 3/8 (GUT) / 3/13 (color-sphere × charge-sphere = weak-color coupling NAMED). Corroborated by Lyra's Killing ‖Y‖²=rank. OPEN: is Y=(1,1) forced by boundary (S⁴×S¹)/ℤ₂? See [[Keeper_K734_sqrt_rank_has_a_rho_weighting_subtlety...]], [[Keeper_K731_weak_color_coupling...]].
