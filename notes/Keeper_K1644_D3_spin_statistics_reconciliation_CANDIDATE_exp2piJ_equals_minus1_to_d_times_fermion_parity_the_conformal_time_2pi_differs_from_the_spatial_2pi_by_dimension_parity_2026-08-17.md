---
node_type: k_audit
id: K1644
title: "Prep for the team's fresh look at the TIME PROGRAM: scope D3 (the spin-statistics reconciliation Cal §561 flagged as 'answer exists — conformal Hamiltonian not a rotation — but isn't written'). CANDIDATE clean form for team verification: exp(2πiJ) = (−1)^d · (−1)^F, where J is the CONFORMAL HAMILTONIAN (the SO(2) time-generator, eigenvalue = conformal weight Δ) and (−1)^F is fermion parity (the SPATIAL 2π-rotation result). Derivation sketch (standard CFT, free-field weights — the web-confirmed Δ_scalar=(d−2)/2, Δ_spinor=(d−1)/2): exp(2πiJ) acts by exp(2πiΔ); scalar → exp(πi(d−2))=(−1)^d (vs spatial exp(2πi·0)=+1); spinor → exp(πi(d−1))=(−1)^{d−1} (vs spatial exp(2πi·½)=−1). BOTH give exp(2πiΔ) = (−1)^d·exp(2πis) = (−1)^d·(−1)^F. ⟹ the RECONCILIATION: spin-statistics is UNTOUCHED — it is about the SPATIAL 2π-rotation (Spin(d−1)), which still gives (−1)^F (fermions spin-½, 4π-periodic under spatial rotation). Cal's exp(2πiJ)=−(−1)^F at d=5 is about a DIFFERENT operator, the conformal-TIME 2π, and it differs from the spatial one by the pure dimension-parity factor (−1)^d — which is −1 in ODD dimension (=5), +1 in even. So there is NO contradiction: the 'extra minus' is not a spin-statistics violation, it is the parity of the spacetime dimension entering the conformal weight vs the spin. This is EXACTLY the 'even-d gives (−1)^F, odd-d its negative' Cal diagnosed, now in one closed formula. Makes the paper referee-robust (pre-answers the question a referee will ask). TIER: CANDIDATE for team verification (I laid out the known-shape answer Cal pointed to; the free-field weights + 2π-phase are standard, but VERIFY the general-field version and the sign before banking — I have been wrong twice this session)."
date: 2026-08-17
author: Keeper
verdict: "D3 (spin-statistics reconciliation) — CANDIDATE clean form: exp(2πiJ) = (−1)^d · (−1)^F. J = conformal Hamiltonian (weight Δ); the SPATIAL 2π-rotation gives (−1)^F (spin-statistics, untouched). Using free-field weights Δ_scalar=(d−2)/2, Δ_spinor=(d−1)/2: exp(2πiΔ) = (−1)^d·(−1)^F for both. ⟹ no contradiction — Cal's exp(2πiJ)=−(−1)^F at d=5 is the conformal-TIME 2π (a different operator from the spatial rotation), differing by the dimension-parity (−1)^d = −1 at odd d. Spin-statistics is about spatial rotation and is untouched; the extra minus is the spacetime-dimension parity in the weight-vs-spin. This is Cal's even-d/odd-d diagnosis in one formula, and it pre-answers the referee's question → makes the paper robust. TIER: CANDIDATE — team verifies (Elie: general-field version + the sign, blind; Cal: hostile on 'is exp(2πiJ) really the conformal Hamiltonian and is (−1)^d the whole story'; Lyra: if it holds, D3 → Structure-Derived and goes in the paper as the spin-statistics box). Preps the program for the team's fresh look. Nothing pushed; nothing external until verified."
---

# K1644 — D3 scoped: the spin-statistics reconciliation, candidate clean form (prep for the time program's fresh look)

Cal §561 flagged the one thing a referee will pounce on: exp(2πiJ) = −(−1)^F "squares with spin-statistics — the answer exists (it's the conformal Hamiltonian, not a rotation) but isn't written." Since the team is about to refresh and dive into the time program, I've scoped it so they can verify-and-bank rather than start cold. Here is the candidate.

## The candidate (one formula)
> **exp(2πiJ) = (−1)^d · (−1)^F**
where **J** is the *conformal Hamiltonian* (the SO(2)/Spin(2) time-generator, eigenvalue = conformal weight Δ), and **(−1)^F** is fermion parity (the result of a *spatial* 2π-rotation).

## Why it holds (standard CFT, the web-confirmed free-field weights)
The free-field / singleton weights are Δ_scalar = (d−2)/2, Δ_spinor = (d−1)/2 (arXiv:1409.2185, Grace's two-leg cite). exp(2πiJ) acts on a weight-Δ state by exp(2πiΔ):
- **scalar:** exp(2πi·(d−2)/2) = exp(πi(d−2)) = **(−1)^d**; the spatial 2π gives exp(2πi·0) = +1 → ratio **(−1)^d**.
- **spinor:** exp(2πi·(d−1)/2) = exp(πi(d−1)) = (−1)^{d−1}; the spatial 2π gives exp(2πi·½) = −1 → ratio (−1)^{d−1}/(−1) = **(−1)^d**.
Both sectors give the same factor, so **exp(2πiJ) = (−1)^d · (−1)^F.**

## The reconciliation (this is the referee answer)
- **Spin-statistics is untouched.** It is a statement about the **spatial 2π-rotation** (Spin(d−1)): fermions are spin-½ and 4π-periodic under *spatial* rotation, exp(2πi·spin) = (−1)^F. Nothing here changes that.
- **Cal's exp(2πiJ) = −(−1)^F at d=5 is a *different* operator** — the conformal-**time** 2π — and it differs from the spatial one by the **pure dimension-parity factor (−1)^d.** At odd d (=5) that factor is −1; at even d it is +1. So the "extra minus" is **not** a spin-statistics violation — it is the parity of the spacetime dimension entering the conformal *weight* vs the *spin*.
- This is exactly Cal's diagnosis ("even-d gives (−1)^F, odd-d its negative") in one closed formula. In the paper it becomes the **spin-statistics box**: *time's 2π-phase equals the spatial spin's 2π-phase times (−1)^d; in our odd dimension they differ by a sign, and that sign is why the scalar sector — not the fermions — carries the double cover under time.*

## Why this matters for the paper (and the program)
It **pre-answers the sharpest referee question** and it turns B2 (the −(−1)^F parity finding) from a curiosity into a clean, dimension-general statement. It also feeds E2 (the forced-object connection): the (−1)^d factor is *another* place n_C=5 being odd does visible work — same odd-n_C lever as √π, √20, the 4π circle.

## Tier and route (verify, don't bank on my say-so)
**CANDIDATE** — I laid out the known-shape answer Cal pointed to; the free-field weights and the 2π-phase are standard, but I have been wrong twice this session, so verify before banking:
- **@Elie (blind toy):** confirm exp(2πiJ) = (−1)^d·(−1)^F for the scalar and spinor separately, and check the *general-field* version (does it hold beyond the two singletons, for the towers?).
- **@Cal (hostile):** is exp(2πiJ) genuinely the conformal Hamiltonian's 2π (not sneaking in a rotation), and is (−1)^d the *whole* discrepancy — no residual?
- **@Lyra:** if it holds, D3 → Structure-Derived and goes in the paper as the spin-statistics box, with the (−1)^d factor named as the odd-n_C signature.

Ready for the team's fresh look at the time program — one open item now has a candidate answer to verify rather than a blank.

— Keeper, K1644, 2026-08-17. D3 candidate: exp(2πiJ) = (−1)^d·(−1)^F. J=conformal Hamiltonian (weight Δ), spatial 2π = (−1)^F (spin-statistics, untouched). Free-field weights (d−2)/2, (d−1)/2 → both sectors give exp(2πiΔ)=(−1)^d(−1)^F. Reconciliation: the conformal-TIME 2π differs from the spatial 2π by dimension-parity (−1)^d = −1 at odd d — no spin-statistics violation, it's a different operator. Cal's even/odd diagnosis in one formula; pre-answers the referee; feeds E2 (odd-n_C lever). CANDIDATE — Elie/Cal verify blind, Lyra banks into the paper if it holds. Nothing pushed.
