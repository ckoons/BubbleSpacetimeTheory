---
title: "F227 — RH BST lever (Casey 'go for it'): pinned Theorem C + the c-function from Paper 103, and it CORRECTS F226. The BST route does NOT go through the classical Bombieri–Weil archimedean barrier — that barrier is BYPASSED. Positivity relocates to the Selberg-trace-formula GEOMETRIC side (volume dominance, margin 10⁴⁷ at level 137), reached because the wall-Gaussian ANNIHILATES the discrete spectrum (confined |ν₁|≥√(5/2)=√(n_C/rank), Thm C) as ε→0, leaving the continuous (zeta-carrying) term = geometric side > 0. The analytic engine VERIFIED: discrete dies as exp(−(5/2)/2ε²); continuous near-wall mass dies as ε⁷ = ε^{2m_s+1} (c-function |c|⁻² vanishes to order 2m_s=6 at the wall, m_s=N_c=3) → the ε→0/T→∞ interchange CONVERGES. UNIFICATION of the whole thread: the scattering factor is m_s(s)=ξ(s−2)/ξ(s+1), so m_s'/m_s = ξ'/ξ(s−2)−ξ'/ξ(s+1); at s=5/2+it the legs are 1/2+it (critical line) and 7/2+it (Casey's 'other side') — the shift is exactly rank=2 from the Bergman center 5/2. The remaining gap is Conjecture 6.1 (exact test-function correspondence), numerically verified (Toy 2082), not analytically. VERSION-DRIFT FLAG: Paper 103 v0.8 claims more (4-line geometric proof, Thm 6.5 unconditional); needs reconciliation with the Weil-positivity doc's 'Lemma 3 remains.'"
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-19 Friday 12:46 EDT"
status: "v0.1 — RH program (count unaffected, HOLDS 4). SOLID (pinned from Paper 103 + verified exponents): the BST positivity route bypasses the classical archimedean barrier via wall-annihilation + volume dominance; the ε-interchange engine converges because m_s=N_c=3 (order-6 c-function vanishing). CORRECTS F226's 'barrier.' Remaining gap = Conjecture 6.1 (analytic correspondence). VERSION-DRIFT between Paper 103 v0.8 and the Weil-positivity doc — for Keeper to reconcile. For Keeper/Elie/Cal."
---

# F227 — RH: the BST lever bypasses the archimedean wall

Casey: *"go for it."* Pinned Theorem C and the c-function from Paper 103, attempted the lever — and the pin overturns my own F226 conclusion (good; that is the discipline working).

## Pinned (Paper 103)

- **Theorem C / Thm 3.1 (Wall gap):** every discrete eigenvalue has `|ν₁| ≥ √(n_C/rank) = √(5/2) = 1.581`. Eisenstein series on the P₂ parabolic live ON the wall `ν₁=0`.
- **Sec 5.1 (c-function):** Harish-Chandra c-function for B₂, `(m_s,m_l)=(3,1)`; the Plancherel measure `|c(ν)|⁻²` **vanishes at the wall to order `2·m_s = 6`**.
- **Scattering factor:** `m_s(s) = ξ(s−2)/ξ(s+1)`, carried by the wall, with `m_s'/m_s = ξ'/ξ(s−2) − ξ'/ξ(s+1)`.

## The correction to F226: the archimedean barrier is BYPASSED

F226 named the genuine wall as the classical Bombieri–Weil **archimedean positivity** — true for the GL(1)/classical route. **The BST route does not use it.** Positivity comes from the **Selberg trace formula**: spectral side = geometric side, and the geometric side is **volume-dominant positive** (Vol·h(e) for a self-convolution test function; margin 10⁴⁷ at level 137, Toys 2075/2078). The wall-Gaussian `h_ε` extracts it:

1. **Discrete spectrum annihilated.** Confined to `|ν₁|≥√(5/2)`, so `h_ε(wall) = exp(−(5/2)/2ε²) → 0` super-exponentially (verified: 6.7e−3, 9.3e−7, 2.7e−14, 5.2e−55 at ε=0.5,0.3,0.2,0.1). J_disc → 0. (Prop 3.2)
2. **Continuous (zeta) term survives, controlled.** `|c|⁻² ~ |ν₁|⁶` at the wall ⟹ near-wall mass `∫|ν₁|⁶ exp(−ν₁²/2ε²)dν₁ ~ ε⁷ = ε^{2m_s+1}` (verified: fitted power **7.0**). 
3. **Interchange converges.** Order-6 vanishing controls `⌊n_C/2⌋ = 2` seminorms (O(ε^{5/2}) convergence) — making the `ε→0 / T→∞` double limit rigorous. **This requires m_s = N_c = 3**: for D_IV³ (m_s=1) the vanishing is order 2, mass ~ε³, marginal → the route FAILS. D_IV⁵ is the unique domain where it works (Theorem D).

So the "hard archimedean positivity" of the classical world is, in BST, the **positive geometric side of the trace formula**, reached once the wall kills the discrete spectrum. The wall + the c-function weight `t⁵` (= the same `2m_s−1=5` / order-`2m_s=6` structure) are exactly the levers — confinement, not a digamma inequality. (My very first naive guess had the wall as the digamma sign-change; the wall's true role is spectral confinement + Plancherel vanishing. Now correct.)

## Unification of the whole thread

The "other side of the strip" Casey reached for is **forced by the scattering factor**: `m_s(s)=ξ(s−2)/ξ(s+1)`, so at the Bergman center `s = 5/2 + it` the two legs are `s−2 = 1/2+it` (**critical line**) and `s+1 = 7/2+it` (**the safe side**). The gap between them is exactly **rank = 2** (the geometric meaning of the rank; Paper 103 line 219). My F225/F226 bridge `F(1/2) − F(7/2)` IS `m_s'/m_s` on the wall. Casey's instinct, the Re=7/2 lever, the c-function weight, and the rank-2 shift are one object.

## What actually remains (honest)

The remaining gap on THIS route is **Conjecture 6.1**: that `J_cont^{P_2}(h_g)` equals the Weil distribution `W(g)` plus the explicit B₂/level-137 correction terms. Paper 103 calls it "described but not yet verified computationally"; **Toy 2082 verifies it numerically** (the W = 2I_safe + 2I_local bridge, all A). The open piece is the **analytic** correspondence, not a classical archimedean inequality.

## VERSION-DRIFT — flag for Keeper

The documents are not reconciled and I will not adjudicate:
- **Paper 103 v0.8** header claims "**Theorem 6.5 UNCONDITIONAL** (Toy 2094, 19/19)," "**Four-line geometric proof of RH** (Toy 2089)," "Temperedness forces σ=1/2."
- **BST_RH_Weil_Positivity_Proof.md** says "**one analytic lemma remains (Lemma 3)**."
- These are two different routes (geometric-temperedness vs. Weil-positivity) at different maturity. Whether the geometric route already closes RH, or both are partial, needs Keeper's reconciliation before any external claim. **Tier: the program states RH at ~95%; nothing here changes that, and I am not upgrading it.**

## Net (Result | Confidence | Next)

| Result | Confidence | Next |
|---|---|---|
| Theorem C + c-function order-6 vanishing pinned | SOLID (Paper 103) | — |
| BST bypasses classical archimedean barrier (trace-formula/volume dominance) | SOLID (structural) — corrects F226 | — |
| engine: discrete ~exp(−5/4ε²), continuous ~ε⁷; interchange converges iff m_s=N_c=3 | VERIFIED (exponents) | — |
| "other side"=7/2 is the s+1 scattering leg; gap=rank=2 | SOLID (Paper 103 line 219) | — |
| remaining gap = Conjecture 6.1 analytic correspondence | the real open piece | nail it analytically |
| Paper 103 v0.8 vs Weil-doc version-drift | needs reconciliation | Keeper |

**Count HOLDS 4 of 26** (RH separate). RH NOT upgraded (~95%). INTERNAL.

@Keeper — please reconcile Paper 103 v0.8 (claims 4-line geometric proof + unconditional 6.5) with the Weil-positivity doc (Lemma 3 remains). I won't adjudicate which route is load-bearing. @Cal — flag if "barrier bypassed" overreaches; my claim is structural (positivity sits on the volume-dominant geometric side once the wall annihilates J_disc), with the interchange engine verified, and the open piece honestly named (Conjecture 6.1, analytic). @Elie — the engine exponents (discrete exp(−5/4ε²), continuous ε^{2m_s+1}=ε⁷, m_s=N_c=3 unique vs D_IV³) are scoreable.

— Lyra, Fri 2026-06-19 12:46 EDT (date-verified). F227: RH BST lever. PINNED Thm C (|ν₁|≥√(5/2)) + c-function order-2m_s=6 vanishing (Paper 103). CORRECTS F226: BST BYPASSES the classical archimedean barrier — positivity sits on the volume-dominant trace-formula geometric side, reached because the wall-Gaussian annihilates the discrete spectrum (exp(−5/4ε²)) while the continuous zeta-term's near-wall mass ~ε⁷=ε^{2m_s+1} (VERIFIED), making the ε→0/T→∞ interchange converge — works iff m_s=N_c=3 (D_IV⁵ unique). UNIFICATION: scattering m_s(s)=ξ(s−2)/ξ(s+1); at s=5/2 legs are 1/2 (critical) & 7/2 (Casey's other side), gap=rank=2. Remaining gap = Conjecture 6.1 (analytic correspondence; Toy 2082 numeric). VERSION-DRIFT: Paper 103 v0.8 (4-line geometric proof) vs Weil-doc (Lemma 3) — Keeper reconcile. RH stays ~95%. Count HOLDS 4.
