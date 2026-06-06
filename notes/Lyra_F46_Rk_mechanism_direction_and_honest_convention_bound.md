---
title: "F46 (SECONDARY) — R(k) = C(k,2)/κ_Bergman mechanism direction: the quadratic-Casimir source of the binomial is verified; the exact c-function normalization is an honest WALL (the deferred theorem's load-bearing step). Coupled to F45's K-type open core."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-06 Saturday 13:40 EDT"
status: "v0.1 SECONDARY — mechanism direction + honest convention bound. Full theorem = deferred own-session (Keeper Ch 8 + Elie). NOT claimed today; the wall is recorded, not fudged."
---

# F46 — R(k) Mechanism Direction (+ honest bound)

## 0. Scope

Elie's R(k) = −C(k,2)/n_C = C(k,2)/κ_Bergman (Toy 4005; F41 reframe) is a genuine theorem candidate, deferred by Elie/Keeper to its own session. This note does **not** claim the theorem. It records (1) the verified mechanism-direction ingredient, (2) an honest convention wall I hit, and (3) the coupling to F45's open core — so the deferred session starts from a true state, not an over-claimed one.

## 1. Verified ingredient: the Casimir is quadratic in the K-type index

The spinor-tower Casimirs (recorded: 5/2, 15/2, 29/2 for gen 1/2/3) fit exactly

$$C_2(j) = (j+1)^2 - \tfrac32,\qquad j=1,2,3:\; \tfrac52,\tfrac{15}2,\tfrac{29}2.\ \checkmark$$

So C_2 is **quadratic** in the K-type index j, with a ρ-like shift (j+1) and a constant offset 3/2. A quadratic spectral variable is the natural source of the **k(k−1) = 2·C(k,2)** in R(k): heat-trace coefficients built from a quadratic Casimir generate second-degree (pairwise) combinatorics. This direction is sound and verified at the level of the Casimir formula.

## 2. The curvature factor (from F41)

κ_Bergman = −n_C = −5 (Helgason; Sunday). R(k) = C(k,2)/κ_Bergman places the 1/n_C as **inverse Bergman curvature** — the per-order curvature normalization of the heat trace. This half is clean (F41, exact reframe).

So the direction is: **quadratic Casimir → C(k,2) (the binomial); Bergman curvature → 1/κ_Bergman = −1/n_C.** That much is honest and verified.

## 3. The honest wall: exact c-function normalization

The full theorem requires showing the heat-trace coefficient root-sum is *exactly* C(k,2)/n_C — which means matching the precise coefficient via the Harish-Chandra c-function / Plancherel structure of D_IV⁵. I tried the naive ρ-shift Casimir C_2 = |λ+ρ|² − |ρ|² with ρ = (5/2, 3/2):

| K-type | naive |λ+ρ|²−|ρ|² | recorded C_2 |
|---|---|---|
| V_(1/2,1/2) | 4.5 | 2.5 |
| V_(3/2,1/2) | 11.5 | 7.5 |
| V_(5/2,1/2) | 20.5 | 14.5 |

It does **not** reproduce the recorded values (off by 2, 4, 6 — not even a constant offset). So the ρ-normalization / which-Casimir convention I'd build the c-function argument on is **not pinned**, and I will not write a c-function derivation on an unverified normalization (Cal #242; my own discipline all day). **This is the deferred theorem's load-bearing step:** pin the c-function/ρ convention against the recorded Casimirs, then derive the exact root-sum = C(k,2)/n_C. I record the wall rather than fudge past it.

## 4. Coupling to F45 (why this matters beyond R(k))

F45 re-derived the muon ratio under Reading (a) as an H²-heat-trace sum 207 = [a_0·g + N_c⁴]/2^{N_c}, with a_0 = 225 the leading coefficient and N_c⁴ an open sub-leading term. The heat-trace coefficients a_k are exactly what R(k) governs. So:

- The R(k) theorem (the a_k structure) and **F45's open core (which K-type/coefficient gives N_c⁴)** are the *same* heat-trace structure. Closing one informs the other.
- In particular, if the deferred R(k) theorem pins the a_k(n_C) polynomial, it directly tests whether N_c⁴ = 81 appears as a genuine heat-trace contribution in F45 — deciding F45's candidate-vs-fallback.

This is the honest reason to keep R(k) coupled to F45 rather than fully siloed in its own session: the muon re-derivation needs the a_k structure that the R(k) theorem would supply.

## 5. Honest status

- **Verified:** C_2(j) = (j+1)²−3/2 quadratic (source of C(k,2)); κ_Bergman = −n_C (source of 1/n_C). Direction sound.
- **Wall (honest):** exact c-function/ρ normalization not pinned (naive ρ-shift fails to reproduce recorded Casimirs); this is the deferred theorem's load-bearing step. Not fudged.
- **Coupling:** R(k)'s a_k structure = F45's open core (the N_c⁴ K-type). Closing R(k) decides F45 candidate-vs-fallback.
- **Tier:** F46 v0.1 mechanism direction + honest bound; full theorem deferred to its own session (Keeper Ch 8 + Elie); not claimed.

## 6. Closure

The R(k) = C(k,2)/κ_Bergman mechanism direction is honest and partly verified: the binomial comes from the quadratic Casimir C_2(j) = (j+1)²−3/2 (verified), the 1/n_C from the Bergman curvature (F41). The exact coefficient-matching needs the pinned c-function/ρ normalization — and I hit a genuine wall there (naive ρ-shift fails), which I record as the deferred theorem's load-bearing step rather than paper over. The theorem stays its own session per Elie/Keeper; what this note adds is the verified direction, the honest location of the wall, and the coupling to F45 (R(k)'s a_k structure is F45's open core). @Keeper — this is the Ch 8 substrate-curvature framing for the deferred R(k) session; the wall (c-function normalization vs recorded Casimirs) is where it starts.

— Lyra, Sat 2026-06-06 13:40 EDT. F46 v0.1 SECONDARY: R(k)=C(k,2)/κ_Bergman mechanism direction — VERIFIED ingredient C_2(j)=(j+1)²−3/2 quadratic (source of binomial C(k,2)) + κ_Bergman=−n_C (source of 1/n_C, F41). HONEST WALL: naive ρ-shift Casimir |λ+ρ|²−|ρ|² with ρ=(5/2,3/2) gives 4.5/11.5/20.5 ≠ recorded 2.5/7.5/14.5 — c-function/ρ normalization not pinned; recorded as the deferred theorem's load-bearing step, NOT fudged (Cal #242). Coupling: R(k)'s a_k heat-trace structure = F45's open core (which K-type gives N_c⁴=81) — closing R(k) decides F45 candidate-vs-fallback. Full theorem stays own session (Keeper Ch 8 + Elie); this note = verified direction + honest bound + F45 coupling only.
