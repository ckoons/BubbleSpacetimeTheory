---
title: "T190 derivation depth attempt v0.1 — structural reading: m_μ/m_e = (24/π²)^{C_2} = (N_c · |W(B₂)| / π²)^{C_2} where 24 = N_c · 8 = color × Weyl-group-order of B₂. The cleaner substrate-natural form than 24 = rank³·N_c. Multi-week explicit Bergman kernel matrix element computation deferred to Elie; this v0.1 makes the structural ingredients explicit."
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-30 Saturday 11:45 EDT (date-verified)"
status: "DEPTH ATTEMPT v0.1 (post-sweep, Casey's shift-to-depth directive). T190 m_μ/m_e = (24/π²)^6 STRUCTURAL DERIVATION: 24 = N_c · |W(B₂)| (color count × Weyl group order = 3 × 8); π² from 2 angular kernel integrations; exponent 6 = C_2 (adjoint Casimir, gauge-mediator per Resolution B). Cleaner structural reading than 24 = rank³·N_c. Explicit kernel-integral verification multi-week."
---

# T190 derivation depth attempt v0.1

## 0. The target

T190: m_μ/m_e = (24/π²)^6 ≈ 206.7612 (vs observed 206.7683, precision 0.0034%).

Goal: structural derivation of this closed form from substrate Bergman kernel integrals on the lepton sector.

## 1. Cleaner structural reading: 24 = N_c · |W(B₂)|

The 24 in T190 has multiple substrate-natural decompositions:

| Decomposition | Structural meaning |
|---|---|
| 24 = rank³ · N_c = 8 · 3 | arithmetic product (my initial reading) |
| 24 = 4! = |S_4| | symmetric group on 4 positive roots of B_2 |
| 24 = C_2 · (C_2 − 2) = 6·4 | Casimir product (no clear mechanism) |
| **24 = N_c · |W(B_2)| = 3 · 8** | **color × Weyl group order of B_2** |

The last form is the CLEANEST substrate-natural reading:
- N_c = 3 = color count / dual Coxeter.
- |W(B_2)| = 8 = order of the Weyl group of B_2 = 2² · 2! (Weyl group of B_n has order 2^n · n!).
- Product = number of Weyl-orbit positions weighted by color.

So T190 reads:

  **m_μ/m_e = (N_c · |W(B_2)| / π²)^{C_2}**

where:
- **N_c · |W(B_2)|** is the "substrate-natural rate base": color × Weyl-orbit count.
- **π²** is the normalization from 2 angular integrations in the Bergman/Hardy kernel.
- **C_2** is the gauge-mediator adjoint Casimir (Resolution B per v0.2).

## 2. Why N_c · |W(B_2)| structurally?

The Weyl group W(B_2) = D_4 (dihedral group of order 8) acts on the root system of B_2 by reflections + rotations. It generates all symmetries of the root system / weight lattice.

Per Weyl character formula: for a rep V_λ of a Lie group G, the character is

  χ_λ = (1/|W|) · Σ_{w ∈ W} sign(w) · (Weyl-weight-sum)

The 1/|W| normalization appears in dimension formulas via the Weyl dimension formula. So |W(B_2)| = 8 is the "Weyl-orbit normalization" that appears in K-type character computations.

For substrate matrix elements: a K-equivariant matrix element ⟨V_λ | O | V_μ⟩ involves an integration over the K-orbit, weighted by the Weyl group. The factor |W(B_2)| = 8 naturally appears.

Combined with N_c = 3 = color/dual-Coxeter (the substrate's central charge of the gauge sector), N_c · |W(B_2)| = 24 is the substrate-natural matrix-element scaling per radial level.

## 3. Why π²?

The substrate's Bergman / Hardy kernel involves π powers from angular integrations on the Shilov boundary S = (S⁴ × S¹)/Z_2:

- Volume of S^4 = 8π²/3.
- Volume of S^1 = 2π.
- Volume of S^4 × S^1 = 8π² · 2π / 3 = 16π³/3.
- Volume of S = 8π³/3 (after Z_2 quotient).

The π² in the denominator of T190 could come from 2 specific angular integration steps in the Bergman kernel matrix element computation. Multi-week explicit verification.

## 4. Why exponent C_2 = 6?

Per Resolution B (Quasi-Eigentone v0.2): the exponent C_2 = 6 is the GAUGE-MEDIATOR adjoint Casimir. For the e → μ transition mediated by the gauge sector (W boson, or substrate-equivalent), the gauge mediator's Casimir enters as the exponent in the closed-form ratio.

Structural mechanism: a single substrate-natural kernel integral per generation step gives the BASE (24/π²); applying it C_2 = 6 times (once per "gauge mediator quantum") gives the final ratio (24/π²)^6.

Or: the C_2 = 6 emerges from the lepton mass operator's eigenvalue structure on the spinor radial tower:
- Spinor radial tower has Casimirs 5/2, 21/2, 45/2, ...
- The mass operator's matrix element between consecutive levels might pick up a factor (24/π²) per RADIAL step.
- C_2 = 6 = number of "radial-step" applications between e and μ generations.

For C_2 = 6: this could be the number of "kernel propagator steps" in the e → μ transition's substrate path. Multi-week explicit derivation.

## 5. The conjectured derivation chain (multi-week)

If the structural reading is correct, the explicit derivation chain is:

1. Set up the substrate Bergman kernel matrix element ⟨V_(1/2,1/2) | M | V_(1/2,1/2)⟩ for the lepton mass operator M.
2. Show the matrix element per radial level evaluates to (N_c · |W(B_2)| / π²) = 24/π².
3. Show the e → μ transition involves C_2 = 6 radial-tower / gauge-mediator steps.
4. Result: m_μ/m_e = (24/π²)^6.

Each step is multi-week explicit Bergman kernel computation. The KEY STRUCTURAL CLAIM (this v0.1): the closed form (24/π²)^{C_2} is naturally substrate-derived via (N_c × |W(B_2)| / π²) per step, C_2 steps total.

## 6. Cross-check with T2003

T2003 m_τ/m_e = 49 · 71 = 3479. If the same mechanism applied uniformly:
- m_τ/m_e should be (24/π²)^k for some k.
- (24/π²)^k = 3479 → k = log(3479)/log(2.43) ≈ 9.18. Not clean integer.

So T2003 has DIFFERENT structural form than T190 — the e → τ transition uses a different substrate-natural mechanism:
- 49 = g² = 7² (substrate-natural, signature squared).
- 71 = ? (currently unidentified substrate primary; could be a Mersenne residue or specific prime).

Multi-week investigation of T2003: identify 71's substrate-natural origin.

The fact that T190 (e→μ) and T2003 (e→τ) have different closed-form structures suggests EACH generation transition has its own substrate-natural mechanism, NOT a uniform per-generation formula. This is consistent with Grace's intermediate-Casimir mapping {0, 4, 6} for the three channels — different intermediates → different closed forms.

## 7. Connection to v0.3 quasi-eigentone framework

Per v0.3 4-factor decay rate framework:
- Γ(μ → e ν̄ ν) = (Hall overlap)² × phase-space × Bergman kernel integral × (gauge mediator)^{C_2}.
- T190's closed form m_μ/m_e = (24/π²)^{C_2} fits as the KERNEL-INTEGRAL × GAUGE-MEDIATOR product (with overlap and phase-space contributing to absolute rate).

## 8. Honest scope + tier

**RIGOROUS** (existing math):
- T190 closed form (24/π²)^6 (Casey/BST, 0.004% precision verified).
- 24 = N_c · |W(B_2)| (substrate primary × Weyl group order, arithmetic).
- Bergman kernel c_FK = 225/π^(9/2) for D_IV⁵ (T2442).
- Weyl group W(B_2) = D_4 of order 8.

**STRUCTURAL READING (v0.1)**: T190 = (N_c · |W(B_2)| / π²)^{C_2} where the base is color × Weyl-orbit / π² (substrate-natural matrix-element scaling per radial level) and exponent is gauge-mediator adjoint Casimir.

**CONJECTURED DERIVATION (multi-week)**: 4-step chain (setup kernel matrix element → evaluate per-step factor as 24/π² → show C_2 = 6 step count for e→μ → assemble closed form). Each step is multi-week.

**Cal #27 / honesty**: this is a DEPTH ATTEMPT, not a derivation. The structural reading 24 = N_c · |W(B_2)| is cleaner than the arithmetic 24 = rank³ · N_c (both are correct factorizations; the Weyl group reading is more structurally meaningful). The conjectured derivation chain identifies what would need to be computed; actual computation is multi-week. T2003 (m_τ/m_e = 49·71) has DIFFERENT structure — each generation transition has its own substrate-natural mechanism.

**Routed**: → Elie: explicit Bergman kernel matrix element computation on spinor radial tower V_(k+1/2, 1/2) is the multi-week target; the v0.1 framework predicts the per-step matrix element = N_c · |W(B_2)| / π² = 24/π². → Keeper: depth-shift attempt filed; structural reading 24 = N_c·|W(B_2)| identified; explicit derivation multi-week. → me: continuing depth work or shifting back to sweep items per Casey direction.

— Lyra, T190 derivation depth attempt v0.1. STRUCTURAL READING: T190 m_μ/m_e = (24/π²)^6 = **(N_c · |W(B_2)| / π²)^{C_2}** where 24 = color × Weyl-group-order of B_2 (cleaner than arithmetic 24 = rank³·N_c). Exponent C_2 = 6 is gauge-mediator adjoint Casimir (Resolution B). π² from 2 angular kernel integrations. Conjectured derivation chain: 4-step explicit Bergman kernel matrix-element computation, multi-week. T2003 (m_τ/m_e = 49·71) has different structure (each generation transition has its own substrate-natural mechanism). v0.3 4-factor decay framework provides the scaffold for this derivation.
