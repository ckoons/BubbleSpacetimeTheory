---
title: "INV-5: Spectral Zeta Confinement — Three Boundaries at s = N_c"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 13, 2026"
status: "Formulated — investigation, not yet theorem"
ac_classification: "(C=3, D=1) — if proved"
origin: "Casey's Euler-Mascheroni seed + three-boundary pattern. Does the Laurent expansion mix all three irreducible remainders inseparably?"
---

# INV-5: Spectral Zeta Confinement — Precise Formulation

*Do the three boundary invariants (+1, γ_EM, f_c) appear inseparably in the spectral zeta function at s = N_c?*

---

## The Question

The three irreducible remainders of BST (+1, γ_EM, f_c = N_c/(n_C π)) each arise at a different kind of boundary:

| Boundary | Invariant | Mathematical source |
|----------|-----------|-------------------|
| Composite ↔ Prime | +1 | Factorization gap (T914) |
| Discrete ↔ Continuous | γ ≈ 0.5772 | Harmonic-logarithmic defect |
| Known ↔ Unknown | f_c = 3/(5π) ≈ 0.191 | Gödel self-reference limit |

**Confinement conjecture:** At s = N_c = 3, the Laurent expansion of the meromorphically continued ζ_{Q^5}(s) necessarily involves all three — they cannot appear in isolation.

---

## Evidence

### 1. Integer pole positions (+1)

The poles of ζ_{Q^5}(s) are at s = 5, 4, 3, 2, 1 — the integers from 1 to n_C. The INTEGRALITY of these positions is the +1 boundary: factorization creates discrete structure. The Gamma function Γ(s) in the Mellin transform has poles at non-positive integers, and the interaction with the heat trace asymptotics produces poles at s = (d/2 − j) = 5 − j, which are integers because d/2 = n_C = 5 is an integer.

**Contribution of +1:** The pole at s = N_c = 3 is a SIMPLE pole precisely because the dimension is an integer. If n_C were not an integer, the meromorphic continuation would not produce poles at all.

### 2. γ_EM at the constant term

From T1184 (Theorem 2): the constant term (Stieltjes constant) in the Laurent expansion at s = 3 is:

$$\gamma_\Delta = \frac{\gamma_{\text{EM}}}{60} + C_{\text{spec}}$$

**Contribution of γ:** The harmonic defect γ_EM appears with coefficient 1/|A_5| because the asymptotic ratio d_k/λ_k^3 ~ 1/(60k) reduces the spectral sum to a harmonic sum.

### 3. π in the normalization (f_c)

The residue at s = 3:

$$\operatorname{Res}_{s=3} \zeta_{Q^5}(s) = \frac{A_2}{(4\pi)^5 \cdot \Gamma(3)}$$

The factor (4π)^5 involves π^5. The volume of D_IV^5 is Vol = π^5/1920. The Gödel limit f_c = N_c/(n_C × π) involves π^1.

**Contribution of f_c:** The normalization of the Seeley-DeWitt coefficients involves powers of π through the heat kernel normalization (4πt)^{-d/2}. The ratio A_2/[(4π)^5 × Γ(3)] necessarily involves π.

### 4. The confinement structure

At s = N_c = 3, the full Laurent expansion is:

$$\zeta_{Q^5}(s) = \frac{A_2}{(4\pi)^5 \cdot 2 \cdot (s-3)} + \frac{\gamma_{\text{EM}}}{60} + C_{\text{spec}} + O(s-3)$$

This single formula involves:
- **+1** (integrality): s = 3 is an integer, Γ(3) = 2! = rank!
- **γ_EM** (defect): appears in the constant term with coefficient 1/|A_5|
- **π** (normalization): appears in the residue through (4π)^5

You cannot write this expansion without all three. Remove the integer structure → no simple pole. Remove γ → wrong constant term. Remove π → wrong residue.

---

## What Would Make This a Theorem

**Conjecture (INV-5).** *For any spectral zeta function ζ_Δ(s) on a compact symmetric space M = G/K with dim_ℂ M = n_C an integer, the Laurent expansion at the convergence boundary s = s_0 necessarily involves:*
1. *Integer pole order (from dim_ℂ being integer)*
2. *γ_EM (from harmonic sum asymptotics)*
3. *π (from heat kernel normalization)*

*This would be the spectral analogue of quark confinement: the three "flavors" of irreducible remainder always appear together.*

**Required to prove:**
1. Show that γ_EM appears generically (not just for Q^5) — this needs the leading asymptotics d_k/λ_k^{s_0} ~ c/k for some rational c
2. Show that π appears in residues for all compact symmetric spaces — this follows from the heat kernel normalization if d/2 is an integer
3. Show that integer poles require integer dimension — true by the Mellin transform structure

**Estimated difficulty:** The first point is the hardest. Not all symmetric spaces have d_k/λ_k^{s_0} ~ c/k. This depends on the growth rates of multiplicities and eigenvalues matching appropriately. For D_IV^n, d_k ~ k^{2n-1}/(2n-1)! and λ_k ~ k^2, so d_k/λ_k^{(2n-1)/2} ~ k^0/(2n-1)! (logarithmic ONLY when (2n-1)/2 is half-integer). The convergence boundary is at s = n, and d_k/λ_k^n ~ k^{-1}/(2n-1)! — so γ_EM always appears! But the coefficient is 1/(2n-1)!, not always 1/|A_n|.

Wait: for D_IV^n, the leading coefficient is 1/d_0^{(n)} where d_0^{(n)} = (2n-1)!!/... Let me compute this more carefully before claiming a general theorem.

---

## Status

**FORMULATED.** The evidence is suggestive but the generalization to arbitrary symmetric spaces needs more computation. The specific case Q^5 is proved (T1184). The confinement interpretation adds physical meaning but is not yet a theorem.

**Recommended next steps:**
1. Compute d_k/λ_k^n asymptotics for D_IV^n at n = 3, 4, 6, 7 to test whether γ_EM always appears
2. Check whether the coefficient is always 1/|A_n| or just 1/(2n-1)! (these differ for n > 5)
3. If γ_EM appears generically, the "confinement" is a theorem about symmetric spaces, not just D_IV^5

---

*Casey Koons & Claude 4.6 (Lyra) | April 13, 2026*
*Confinement: the three boundaries meet at s = N_c. You cannot hear one without hearing all three.*
