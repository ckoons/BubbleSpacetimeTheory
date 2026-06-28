---
title: "Mixing lane (Grace, 2026-06-27) — the Cabibbo angle from inter-stratum Bergman overlap on D_IV⁵, and the honest constraint that the full CKM needs non-aligned stratum geometry. SOLID: V_12 (Cabibbo) = N_μ^{n_C/2} = (1−r_μ²)^{n_C}, the e–μ inter-stratum overlap on the Lie ball (canonical polynomial h(z,w)=1−2z·w̄+(z·z)(w̄·w̄), genus n_C=5; gen-1/electron at the origin trivializes the cross-term). The n_C/2 = 5/2 half-integer is FORCED by n_C odd (→ √). With the muon Cartan-slice localization N_μ ≈ 0.55, V_12 = 0.2243 = |V_us|. The hierarchy V_12 ≫ V_23 ≫ V_13 emerges from the localizations N_e=1 > N_μ > N_τ→0. OPEN (not fished): exact N_μ derivation from the muon Cartan-slice geometry — substrate-natural candidate r_μ=1/2 (N_μ=9/16) gives 0.237 (+5.8%, structural); exact 0.55=11/20 is NOT a clean substrate ratio, so I do NOT bank it. NEW honest constraint: the ALIGNED 3-point model CANNOT fit |V_cb| and |V_ub| together (fitting V_cb=0.041 forces V_ub=0.0005 vs obs 0.0037, off 8×) → the full CKM needs the NON-ALIGNED off-axis geometry of the three strata, not three points on one real line. Five-Absence clean (Bergman geometry, no GUT); target-innocence: n_C/2 from the primary n_C, N_μ the open piece."
author: "Grace"
date: "2026-06-27 Saturday"
status: "Mixing lane. Cabibbo MECHANISM solid (e–μ overlap, n_C/2 power forced); N_μ derivation OPEN (not fished); full CKM needs non-aligned stratum geometry (new constraint). Builds on F84–F86. Count not moved — mechanism + constraint, honestly tiered."
---

# The Cabibbo angle from inter-stratum overlap — and what the full CKM needs

Casey: "please do math." The mixing lane, concretely. The masses are diagonal deposits on the three
Korányi–Wolf strata; the **mixing is the off-diagonal — the inter-stratum overlap** of the mass bases.

## The Bergman overlap on D_IV⁵

Canonical polynomial of the Lie ball: `h(z,w) = 1 − 2(z·w̄) + (z·z)(w̄·w̄)`, genus = n_C = 5. A coherent state
at `z` has localization norm `N(z) = h(z,z)`; for a real-direction point `z = r·e`, `h(z,z) = (1−r²)²`. The
normalized overlap of two aligned states (radii r_i, r_j) is
```
⟨i|j⟩ = [h_ii h_jj]^{n/2} / h_ij^n = [(1−r_i²)(1−r_j²)/(1−r_i r_j)²]^{n_C}.
```

## Cabibbo — SOLID

Generation-1 (electron/down) sits at the **origin** (r=0, N_e=1), which trivializes the cross-term. Then the
e–μ overlap is
```
V_12 = ⟨e|μ⟩ = (1 − r_μ²)^{n_C} = N_μ^{n_C/2},   N_μ = (1−r_μ²)².
```
- The power `n_C/2 = 5/2` is **forced by n_C being odd** (odd genus → half-integer → √) — target-innocent.
- With the muon Cartan-slice localization `N_μ ≈ 0.55` (corpus, F86): `V_12 = 0.55^{2.5} = 0.2243 = |V_us|`. ✓
- Hierarchy: `V_12 ≫ V_13 = N_τ^{n_C/2} → 0` (tau at the Shilov boundary, N_τ→0) — the CKM hierarchy emerges
  from the localizations `N_e=1 > N_μ > N_τ→0`.

## N_μ — ALIGNED to the corpus form (CORRECTION to my first draft)

**Correction:** my first draft flagged `N_μ=0.55=11/20` as "not a clean substrate ratio." That was wrong —
the corpus (Lyra F87b, Elie 4073) already has the clean form:
```
Cabibbo = rank/√(rank⁴·n_C − 1) = 2/√79 = 0.22502   (+0.10% vs obs 0.2248)
79 = rank⁴·n_C − 1 = 16·5 − 1     ← substrate-clean
N_μ = (rank²/(rank⁴·n_C − 1))^{1/n_C} = (4/79)^{1/5} = 0.5507,   N_μ^{n_C/2} = 2/√79 ✓
```
So N_μ IS substrate-clean; I reproduced F87b's e–μ overlap + n_C/2 √-structure without connecting to it.
Credit F87b/4073.

**The genuine open core (Lyra's flag, adopted):** `λ² = N(w_μ)^{n_C}` is an **IDENTITY** (re-expresses λ as a
position), **not yet a forcing**. The forcing = K-type quantization fixes `N(w_μ)=(4/79)^{1/5}` from the (a,b)
lattice addresses — the Hua computation, still open. Pairing with Lyra on it (Keeper routing).

## The full CKM needs NON-ALIGNED geometry — NEW honest constraint

The aligned 3-points-on-one-line model gives Cabibbo and the qualitative hierarchy, but **cannot fit the full
CKM**: fitting `|V_cb| = 0.041` forces `r_τ = 0.886`, which then gives `|V_ub| = 0.0005` vs observed `0.0037`
— **off by 8×**. So the three strata are **not** collinear in the domain; the full CKM (V_cb, V_ub, the phase)
requires the **off-axis geometry** of the three localization points. Cabibbo (1–2) works cleanly only because
gen-1 sits at the origin (cross-term trivializes); the 2–3 and 1–3 elements probe the genuine off-axis
positions. **This locates what's needed for the full CKM: the off-axis stratum coordinates, not just the
localization norms.**

## Tier

- **SOLID:** the inter-stratum overlap mechanism; `V_12 = N_μ^{n_C/2}`; the `n_C/2` half-integer forced by odd
  n_C; the hierarchy from localizations. (Consolidates/verifies F84–F86.)
- **STRUCTURAL:** Cabibbo = 0.237 at the substrate-natural `r_μ=1/2` (N_μ=9/16), +5.8%.
- **OPEN:** exact N_μ derivation (not fished); the full CKM (V_cb, V_ub, phase) via the non-aligned off-axis
  geometry. The off-axis coordinates are the concrete next computation.
- **Five-Absence:** clean (Bergman geometry, no GUT). **Target-innocence:** n_C/2 from the primary n_C.

— Grace, 2026-06-27 Saturday. Cabibbo = N_μ^{n_C/2} (e–μ overlap, n_C/2 forced by odd n_C), 0.224 at N_μ≈0.55;
N_μ exact derivation OPEN (r=1/2 → 9/16 → 0.237 structural, not fished); full CKM needs non-aligned stratum
geometry (aligned model fails V_cb/V_ub 8×) — the off-axis coordinates are the next computation.
