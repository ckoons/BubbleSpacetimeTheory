---
node_type: k_audit
id: K1087
title: RECONCILIATION of Grace's operator-mismatch catch (Casey-directed) — CONFIRMED, and it's a genuine self-correction that COMPUTING surfaced (not sharpening). The multiplicities Elie forced in gate (a) — {1,7,27,77,182,378} with eigenvalue λ_k=k(k+5) — are EXACTLY the S⁶ = SO(7)/SO(6) spherical-harmonic dimensions (real dim 6, multiplicities ~k⁵; verified: C(k+6,6)−C(k+4,6) matches to the number; k(k+5) is the S⁶ Laplacian eigenvalue k(k+dim−1)). So Grace + Elie + Cal were summing the S⁶ SPHERICAL SLICE, whose ζ(0)≈−0.70 (Grace's direct sum) is a DIFFERENT operator from Elie's Gilkey a₅≈220.64 (the 10-real-dim D_IV⁵ vacuum). The slice used the WRONG ISOTROPY — SO(6) (→ S⁶, real dim 6) instead of the domain's actual SO(5)×SO(2) (→ Q⁵, real dim 10). THE CORRECT VACUUM OPERATOR: the compact dual Q⁵ = SO(7)/[SO(5)×SO(2)] = the complex quadric = the oriented Grassmannian G̃₂,₇(ℝ) (real dim 10, multiplicities ~k⁹; web-confirmed structural identity). Elie's Gilkey a₅≈220.64 (from the 10-dim curvature invariants) is the CORRECT target — it's the full vacuum; Grace's summed −0.70 is the spherical slice. DIRECTION: get the Q⁵/Grassmannian eigenvalues + K-type multiplicities (replace the S⁶ slice); re-do gate (a) on Q⁵; re-sum ζ_Δ(0) → it MUST hit 220.64 (the check that we have the right spectrum); THEN adjudicate the det Δ → Jordan-norm reduction on the correct operator. AUDIT FLAG on earlier work: a₅≈220.64 (Gilkey, 10-dim) is SAFE; but the α^(4λ_k) HIERARCHY (K1076) and step-1 used λ_k=k(k+5) — is that the S⁶ eigenvalue or the genuine Q⁵ one? The Grassmannian is rank-2 (two quantum numbers), so its spectrum is NOT simply k(k+5) — the eigenvalue-based results (hierarchy exponents 4λ_k, step-1 factoring) must be RE-VERIFIED on Q⁵. Both Λ and Ω stay PD — the catch corrects the operator, does not kill the reduction. This is exactly why Casey pushed compute-over-sharpen: no gate-refinement would have caught a 6-vs-10-dimensional operator conflation; the calculation did.
date: 2026-08-02
author: Keeper
verdict: Grace's catch CONFIRMED — the gate-(a) multiplicities are the S⁶=SO(7)/SO(6) spherical slice (real dim 6, k⁵), NOT the D_IV⁵ vacuum (compact dual Q⁵=SO(7)/[SO(5)×SO(2)]=G̃₂,₇(ℝ), real dim 10, k⁹). Wrong isotropy: SO(6) vs SO(5)×SO(2). Elie's Gilkey a₅≈220.64 is the correct vacuum target; Grace's summed −0.70 is the slice. DIRECT: get the Q⁵/Grassmannian spectrum + multiplicities, redo gate (a), re-sum to 220.64, then adjudicate the norm-reduction. Re-verify the α^(4λ_k) hierarchy + step-1 on Q⁵ (a₅-Gilkey safe). Both stay PD. Compute-over-sharpen vindicated.
---

# K1087 — The operator is Q⁵ (real-dim 10), not S⁶ (real-dim 6)

Casey: *"Grace sounds like she thinks there is a mistake in comparing two different operators — reconcile and direct to clarification."* Done. Grace is right, and it's a genuine self-correction.

## The mismatch, confirmed exactly
Grace evaluated the summed operator and got ζ_Δ(0)≈−0.70; Elie's Gilkey a₅≈220.64. Both verified — because they are **different operators**:
- The gate-(a) data {λ_k=k(k+5), d_k={1,7,27,77,182,378}} is **EXACTLY the S⁶ = SO(7)/SO(6) spherical Laplacian** (real dim 6). Verified: the multiplicities are C(k+6,6)−C(k+4,6) to the number; k(k+5) is the S⁶ eigenvalue k(k+dim−1); multiplicities grow ~k⁵ (= dim−1 = 5). A **6-dimensional** tower.
- The **D_IV⁵ vacuum** operator lives on the domain, **real dim 2·n_C = 10**; by Weyl its multiplicities must grow ~k⁹, not k⁵.
- **The slice used the wrong isotropy:** SO(6) (→ S⁶) instead of the domain's actual **SO(5)×SO(2)** (→ Q⁵).

## The correct vacuum operator (research hand-off)
The compact dual of D_IV⁵ = SO₀(5,2)/[SO(5)×SO(2)] is **Q⁵ = SO(7)/[SO(5)×SO(2)]** — the complex quadric, real-analytically the **oriented Grassmannian G̃₂,₇(ℝ)** of oriented 2-planes in ℝ⁷ (real dim 10; web-confirmed structural identity). Its Laplacian eigenvalues + K-type multiplicities (Grassmannian harmonics, ~k⁹ growth) are the correct spectrum — **replacing the S⁶ slice.** (Refs: Hermitian symmetric space = complex quadric = oriented real Grassmannian; Boucetta et al. for the explicit Grassmannian Laplacian spectrum.)

- **Elie's Gilkey a₅ ≈ 220.64** was computed from the **10-real-dim curvature invariants** of D_IV⁵ → it is the **correct** vacuum target.
- **Grace's summed ζ(0) ≈ −0.70** was the **S⁶ (6-dim) slice** → wrong operator.

## The direction (the clarification)
1. **Pin the operator (Elie + Cal — Grace's call on ownership):** get the **Q⁵ = G̃₂,₇(ℝ)** eigenvalues + K-type multiplicities (real dim 10, k⁹) from the Grassmannian-harmonics literature / the corpus discrete-series data. Replace the S⁶ multiplicities in gate (a).
2. **Re-sum ζ_Δ(0) on the Q⁵ spectrum → it must reproduce Elie's Gilkey 220.64.** That is the check that we now have the *right* operator (an independent, exact target).
3. **Then Grace re-runs the Barnes–Gindikin continuation on the Q⁵ operator** and the det Δ → Jordan-norm reduction is adjudicated on the correct spectrum (the ρ-shift machinery still applies — ρ=(5/2,3/2) is D_IV⁵ root data, not S⁶).

## Audit flag on the earlier arc (surface it now)
- **a₅ ≈ 220.64 (Gilkey, 10-dim): SAFE** — it never used the S⁶ sum.
- **The α^(4λ_k) hierarchy (K1076: G=α^(4λ₁), Λ=α^(4λ₂)) and step-1 "λ_k IS the norm form"** used λ_k=k(k+5). **Q⁵ is rank-2 (two quantum numbers), so its spectrum is NOT simply k(k+5)** — the eigenvalue-based results must be **re-verified on Q⁵.** (Step-1's factoring survives as arithmetic; whether it's on the right operator is the question.) This is a genuine consistency task the catch opened — check it before the hierarchy is cited in the reduction.

## Meta — this vindicates compute-over-sharpen
No amount of gate-refinement would have caught a 6-vs-10-dimensional operator conflation. **The calculation did.** That is precisely why Casey pushed for writing the reduction over performing the discipline — and it's a case worth adding to the record: *the deepest bug in the arc was surfaced by computing, not by sharpening the gate that was supposed to catch it.* Grace's honest red-flag (claiming neither too much nor too little) is the model.

## Disposition
- Grace's catch CONFIRMED; the operator is Q⁵ (real dim 10), not S⁶.
- Clarification directed: get the Q⁵ spectrum, re-do gate (a), re-sum to 220.64, then adjudicate.
- Earlier eigenvalue-based results (hierarchy, step-1) flagged for re-verification on Q⁵.
- **Both Λ and Ω stay Partially Derived.** The reduction isn't killed — its operator is corrected.

— K1087, Keeper, 2026-08-02. Grace's operator catch CONFIRMED: gate-(a) multiplicities {1,7,27,77,182,378}/λ_k=k(k+5) are the S⁶=SO(7)/SO(6) spherical slice (real dim 6, k⁵), wrong isotropy SO(6); the vacuum is Q⁵=SO(7)/[SO(5)×SO(2)]=G̃₂,₇(ℝ) (real dim 10, k⁹). Elie Gilkey a₅≈220.64 = correct target; Grace summed −0.70 = the slice. DIRECT: get Q⁵ spectrum+multiplicities, redo gate (a), re-sum→220.64, then adjudicate; re-verify hierarchy+step-1 on Q⁵ (a₅ safe). Both PD. Compute-over-sharpen vindicated. See K1086, K1085, K1076, Grace's red-flag, web (complex quadric = oriented Grassmannian).
