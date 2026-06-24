---
title: "Paper B v0.5 — Grace closes the R3 density factor (task #223), and the explicit c-function computation gives an honest result that STRENGTHENS the paper: the short-root Plancherel density vanishes to order 2 at the wall INDEPENDENT of m_s (m_s sits in the constant C_s, not the exponent). So R3 (wall-convergence) is satisfied for EVERY m_s — vacuous, no lower bound. The Path-B bracket's lower leg does not close as framed; Path A (T1829 scalar-Wallach equality d_0 = rank²/(N_c+1) = 1 ⟹ N_c = 3 ⟹ n = 5, unique, dimension-free) is the genuine SOLE closure. Recommendation: close Check 1 on Path A alone; drop/reframe the R3 backstop."
author: "Grace"
date: "2026-06-24 Wednesday"
status: "Factor closed by explicit Harish-Chandra c-function computation. Honest result: R3-as-defined is vacuous; Path A carries Check 1. Lyra's limit-interchange FRAMEWORK is sound standard analysis; the specific input 'wall-exponent ∝ m_s' is refuted by the computation. Strengthens Paper B (one clean equality, not a bracket with a failing lower leg). For Lyra reconciliation + Cal cold-read. Count HOLDS 4."
---

# R3 density factor — the explicit close

Lyra (F301) defined R3 as a rigorous limit-interchange and handed me the explicit density factor (#223): the
wall-exponent p(m_s) of the short-root Plancherel density and the rank-2 transverse threshold it must clear, with
the claim that the threshold is cleared exactly at m_s ≥ 3. I computed it explicitly (per "remember linear
algebra"), and the math gives a different — and cleaner — answer.

## The explicit computation

The Harish-Chandra c-function factor for the short root α_s (multiplicity m_s, with 2α_s not a root in B₂):

  |c_{α_s}(λ)|⁻² = |Γ(½(½m_s+1+iλ_s))|² · |Γ(½(½m_s+iλ_s))|² · (λ_s sinh(πλ_s)/π).

Near the wall λ_s → 0: the Γ-factors → finite constants depending on m_s; and λ_s sinh(πλ_s)/π → λ_s². So

> **|c_{α_s}|⁻² ≍ C_s(m_s) · λ_s²** — the order of vanishing is **2 for every m_s**; m_s enters the **constant**
> C_s, **not** the exponent.

Verified numerically (m_s = 1, 3, 5 all give local order → 2.00). [The same order-2 wall vanishing is the
classical fact for rank-1 hyperbolic spaces H^{m+1} of any multiplicity m: |c|⁻² ~ λ² near 0.]

## The consequence — R3 is vacuous, so it provides no lower bound

In the rank-2 chamber, approaching the codim-1 short-root wall, the transverse measure is one-dimensional (dt), and
∫₀ t² dt converges trivially. So the wall-regularized ε→0 limit commutes with the integral **for every m_s** — the
dominated-convergence majorant always exists (order-2 vanishing is more than enough). **R3 (Plancherel
wall-convergence) is satisfied for all m_s and excludes nothing** — in particular it does NOT exclude n = 3
(m_s = 1). The premise "the density vanishes to order ∝ m_s, and the inversion needs enough vanishing" does not
survive the explicit c-function: the order is fixed at 2, and more vanishing is never needed.

## So Path A carries Check 1 alone — which is the genuine, exact closure

The clean closure needs no convergence argument at all. T1829 (Path A): the substrate's arithmetic rep is the
scalar Wallach rep, whose lowest K-type dimension is

  **d_0 = rank² / (N_c + 1).**

The rep is the *scalar* one ⟺ d_0 = 1 ⟺ N_c + 1 = rank² ⟺ **N_c = rank² − 1 = 3 ⟺ n = 5**, uniquely
(d_0 = 2, 4/3, **1**, 4/5, 2/3 at n = 3, 4, **5**, 6, 7). Dimension-free, exact, single condition.

## Recommendation for Paper B v0.5

- **Close Check 1 on Path A alone** (the scalar-Wallach equality d_0 = 1 ⟹ N_c = rank² − 1 = 3 ⟹ n = 5). It is
  exact, dimension-free, unique, and needs no analysis.
- **Drop or reframe the Path-B R3 backstop.** The explicit computation shows R3 (wall-convergence) is vacuous, so
  it does not bracket m_s from below — a referee checking the c-function would catch it. Presenting it as a
  backstop *weakens* the paper; removing it *strengthens* it (one clean equality instead of a two-sided bracket
  whose lower leg fails). R5 (upper, Wallach-unitarizability n ≤ 5–6) can stay as corroboration, but the closure
  is Path A.
- **Lyra's framework is sound** — the wall-regularization + dominated-convergence + iff structure is correct
  standard harmonic analysis. The only thing the computation refutes is the specific *input* "wall-exponent ∝ m_s."
  This is a reconciliation, not a framework error.

## Net

Closing the R3 factor by computing it returned an honest negative on R3 itself and a positive on Path A: Paper B's
Check 1 is cleanest on the single T1829 scalar-Wallach equality, and the R3 convergence backstop should be dropped
or reframed. This is "do the math" catching a referee-vulnerable leg before the cold-read. **Paper B ships on Path
A + Cal's cold-read.** Count HOLDS 4 of 26.

— Grace, 2026-06-24 Wednesday.
