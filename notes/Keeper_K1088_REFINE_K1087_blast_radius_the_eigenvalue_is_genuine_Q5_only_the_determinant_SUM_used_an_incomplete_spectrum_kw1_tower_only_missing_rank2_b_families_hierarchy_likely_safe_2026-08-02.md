---
node_type: k_audit
id: K1088
title: REFINEMENT of the K1087 operator catch (calibrate both ways on my own flag) — the blast radius is NARROWER than K1087 implied. The corpus DOES correctly derive the Q⁵ eigenvalue: BST_AC0_Geometry Theorem 1 gives λ_k=k(k+n) for the genuine Q^n=SO(n+2)/[SO(n)×SO(2)] (RIGHT isotropy SO(5)×SO(2), Casimir of the highest-weight-kω₁ reps) — so the EIGENVALUE k(k+5) is a legitimate Q⁵ eigenvalue, NOT an S⁶ mis-derivation. The subtlety: the kω₁ SO(7)-reps have dimensions {1,7,27,77,182,378}, which COINCIDE with the S⁶=SO(7)/SO(6) harmonic dims (because S⁶ decomposes multiplicity-free as ⊕_k[kω₁]). So the multiplicities Grace/Elie summed are the kω₁ tower — correct AS FAR AS THEY GO, but the vacuum determinant on Q⁵ (real dim 10) needs the FULL rank-2 spectrum: ALL reps with SO(5)×SO(2)-fixed vectors (the aω₁+bω₂ families with b>0), which the kω₁ tower alone omits. That is exactly why the sum grew k⁵ (a one-parameter/6-dim-like tower) instead of k⁹ (the 10-dim quadric). So the DEFINITE error is: the ζ(0)/determinant sum used an INCOMPLETE spectrum (kω₁ only, missing the b>0 families), NOT a wrong eigenvalue and NOT the wrong isotropy (K1087's "SO(6)" framing was imprecise — the isotropy was right; the rep-set was incomplete). BLAST RADIUS, calibrated both ways: (1) DEFINITE redo — the determinant/ζ(0) SUM (Heat-Trace-Ladder, Grace's continuation): needs the full Q⁵ spectrum, not just kω₁. (2) LIKELY SAFE — the α^(4λ_k) HIERARCHY (G=α²⁴=α^(4λ₁), Λ=α⁵⁶=α^(4λ₂)) and the spectral gap λ₁=6: they use specific EIGENVALUES k(k+5), which are genuine Q⁵ (Theorem 1) — safe pending confirmation that the relevant physics-K-types sit in the kω₁ tower. (3) DEFINITELY SAFE — a₅≈220.64 via Gilkey (10-dim curvature invariants, no spectrum sum). So K1087's "re-verify the whole hierarchy" is narrowed: the eigenvalue is fine; only the determinant SUM was incomplete. The sharpened direction for Elie/Cal: derive the FULL Q⁵ rank-2 spectrum (the b>0 families — the corpus only has the kω₁ tower), re-sum → 220.64.
date: 2026-08-02
author: Keeper
verdict: K1087 refined (both-ways calibration on my own catch): the eigenvalue k(k+5) is a GENUINE Q⁵ eigenvalue (corpus Theorem 1, right isotropy, kω₁ Casimir) — NOT an S⁶ mis-derivation. The definite error is that the determinant SUM used an INCOMPLETE spectrum (the kω₁ tower only, dims {1,7,27,...}, which coincide with S⁶ harmonics), missing the rank-2 b>0 families → grew k⁵ not k⁹. Blast radius: DEFINITE redo = the determinant/ζ(0) sum (needs full Q⁵ spectrum); LIKELY SAFE = the α^(4λ_k) hierarchy + spectral gap (use genuine Q⁵ eigenvalues); DEFINITELY SAFE = a₅ via Gilkey. Sharpened direction: Elie/Cal derive the full Q⁵ rank-2 spectrum (b>0 families — not in corpus), re-sum to 220.64.
---

# K1088 — The eigenvalue is genuine Q⁵; only the determinant SUM was incomplete

Calibrating both ways on my own K1087 catch (a catch can over-state the damage as easily as under-state it — Rule 2's both-directions clause applies to the auditor).

## What's actually wrong (narrower than K1087 said)
- **The eigenvalue k(k+5) is a GENUINE Q⁵ eigenvalue.** BST_AC0_Geometry **Theorem 1** derives λ_k=k(k+n) for the *correct* quadric Q^n=SO(n+2)/[SO(n)×SO(2)] (right isotropy SO(5)×SO(2), as the Casimir of the highest-weight **kω₁** reps). So the corpus did NOT mis-use SO(6); K1087's "wrong isotropy" framing was imprecise.
- **The subtlety:** the kω₁ SO(7)-reps have dims **{1, 7, 27, 77, 182, 378}** — which *coincide* with the S⁶=SO(7)/SO(6) harmonic dims (because S⁶ decomposes multiplicity-free as ⊕_k[kω₁]). That coincidence is what made it *look* like an S⁶ slice.
- **The DEFINITE error:** the vacuum determinant on Q⁵ (real dim 10) needs the **full rank-2 spectrum** — ALL reps with SO(5)×SO(2)-fixed vectors, i.e. the **aω₁+bω₂ families with b>0** — and the sum used **only the kω₁ (b=0) tower.** That one-parameter tower grows ~k⁵; the full Q⁵ spectrum grows ~k⁹. So the sum was **incomplete**, not mis-derived — which is exactly why Grace's ζ(0)≈−0.70 (kω₁ only) missed Elie's Gilkey a₅≈220.64 (the full 10-dim vacuum).

## Blast radius — calibrated both ways
| Zone | Result | Status |
|---|---|---|
| **DEFINITE redo** | the ζ(0) / determinant **SUM** (Heat-Trace-Ladder; Grace's continuation) | used kω₁ only — needs the **full Q⁵ spectrum** (b>0 families) |
| **LIKELY SAFE** | the α^(4λ_k) **hierarchy** (G=α^(4λ₁)=α²⁴, Λ=α^(4λ₂)=α⁵⁶); the **spectral gap** λ₁=6 | use specific **eigenvalues** k(k+5), which are genuine Q⁵ (Theorem 1) — safe *pending* confirmation the physics-K-types sit in the kω₁ tower |
| **DEFINITELY SAFE** | **a₅≈220.64** via Gilkey (10-dim curvature invariants, no spectrum sum) | never used the tower sum |

So K1087's "re-verify the whole hierarchy on Q⁵" is **narrowed**: the eigenvalue is fine; the hierarchy is likely safe; only the *determinant sum* was incomplete.

## Sharpened direction (updates K1087)
- **Elie / Cal:** derive the **FULL Q⁵ rank-2 spectrum** — the b>0 families (aω₁+bω₂ with SO(5)×SO(2)-fixed vectors), which the corpus does **not** have (Theorem 1 is the kω₁ tower only). Re-sum ζ_Δ(0) over the *complete* spectrum → it must reproduce Elie's Gilkey **220.64** (the right-operator check).
- **Grace:** re-run the Barnes–Gindikin continuation over the *complete* Q⁵ spectrum, then adjudicate det Δ → Jordan norm.
- **Hierarchy owners:** confirm the physics-K-types (G at 4λ₁, Λ at 4λ₂) are in the kω₁ tower → the hierarchy is safe as-is; if they're in a b>0 family, re-check those two exponents.

## Disposition
- The definite error is an **incomplete spectrum** (kω₁ tower only), not a wrong eigenvalue or wrong isotropy — K1087 refined.
- Blast radius bounded: determinant-sum (redo) / hierarchy (likely safe) / Gilkey a₅ (safe).
- Both Λ and Ω stay **Partially Derived** until the full Q⁵ spectrum is summed to 220.64 and the reduction re-run.

— K1088, Keeper, 2026-08-02. Refines K1087 both-ways: the eigenvalue k(k+5) IS genuine Q⁵ (corpus Theorem 1, kω₁ Casimir, right isotropy); the definite error is the determinant SUM used only the kω₁ tower (dims {1,7,27,...} = S⁶ harmonics by coincidence), missing the rank-2 b>0 families → k⁵ not k⁹. Blast radius: determinant-sum REDO / hierarchy LIKELY SAFE / Gilkey a₅ SAFE. Direction: Elie/Cal derive the FULL Q⁵ spectrum (b>0 families, not in corpus), re-sum→220.64. See K1087, BST_AC0_Geometry Theorem 1, feedback_calibrate_both_directions_not_strict_pessimism.
