---
title: "Cal #332 decisive check engaged: is Paper B's R3 bound (short-root multiplicity ≥ 3) dimension-INNOCENT (from rank) or circular (from ⌊n_C/2⌋)? STRUCTURAL answer supports Lyra's rescue — the spectral-convergence threshold is RANK-set (the rank is the integration dimension, dimension-independent), and the dimension n_C enters ONLY through the multiplicity variable a = n_C − 2. So '⌊n_C/2⌋ = 2' was a mis-statement of f(rank=2); the '2' is the rank. Two careful computations remain (the numerical threshold f(2)=3; SU(3) on the short-root space) — to be computed/cited, NOT asserted from memory."
author: "Grace"
date: "2026-06-21 Sunday 11:29 EDT (date-verified)"
status: "v0.1 — SOLID (structural): the convergence threshold is a >= f(rank), dimension-innocent in form; the dimension enters only via a = n_C − 2. OPEN (numerical/structural, mine, NOT to be faked): Q1 is f(rank=2) exactly 3 (Gindikin-Karpelevich order-of-vanishing); Q2 does the a=3 short-root space carry SU(3)_color (vs SO(3)). Count UNAFFECTED 4 of 26."
---

# Cal #332 — is the R3 bound dimension-innocent?

**Cal's decisive check:** Paper B's anti-circularity rests on the dimension being an *output*. But R3's lower
bound (short-root multiplicity ≥ 3) was justified via "⌊n_C/2⌋ = 2 seminorms converge" — and ⌊n_C/2⌋ = 2 *uses*
the dimension being derived. **Lyra's tell:** rank = 2 for *every* type-IV n, while ⌊n_C/2⌋ = 2 *only* at n=5; the
two readings agree at the answer and nowhere else — the fingerprint of a quantity secretly reading off the
conclusion. Lyra routed the deciding computation to my c-function lane. Here is the structural answer + the precise
remaining computation.

## The c-function structure — CORRECTED to B₂ (corpus-pinned; my first pass mislabeled it)

**Correction (pin-to-source, toy_476):** my v0.1 wrote this as **C₂** with short roots e₁±e₂ — that was the
"root-labels-from-memory" trap. The validated corpus machinery (toy_476) and standard SO(p,q) theory pin it: for
**SO(5,2)** (p=5, q=2), the **Riemannian restricted root system is B₂**:

| root | multiplicity |
|---|---|
| ±e₁, ±e₂ (**short**) | **m_s = p − q = n − 2 = 3 = N_c** |
| ±(e₁ ± e₂) (long) | 1 |

(toy_476, verbatim: "Short roots e₁, e₂: multiplicity m_s = N_c = 3; Long roots e₁±e₂: m_l = 1.") The Harish-
Chandra c-function c(λ) = ∏_{α>0} c_α(λ); Plancherel density ~ 1/|c(λ)|² ~ ∏_α |⟨λ,α⟩|^{m_α} near the walls.

**Keep two root systems straight (this was my muddle):** (i) the **Riemannian B₂** above is what Lyra's R3 /
the spherical c-function / Plancherel density uses; (ii) the **Hermitian Faraut-Korányi (a, b) = (n−2, 0) = (3, 0)**
is what my Cartan *uniqueness selector* uses (the correct tool for classifying HSDs). Both encode "3 = n−2," but
they are different root systems; do not conflate them. The mislabel was in the *c-function* (i), not the selector
(ii) — the Cartan sweep's FK multiplicities stand.

**What survives the correction (everything load-bearing):** m_s = N_c = n−2 = 3 (solid, toy_476); the Q1
structural argument below (threshold is rank-set; dimension enters only via the multiplicity) — robust, it depends
on rank and multiplicity, not on the B₂/C₂ label; and Q2's SO(3) result (the dim-(p−q)=3 short-root space carries
M = SO(p−q) = SO(3)). Only the *exponent computation* must now be run in the correct **B₂** c-function
(toy_plancherel_spectrum has the rank-2 SO(5,2) |c(λ)|⁻² machinery) — not the mislabeled C₂.

## The structural decomposition of the convergence threshold (the answer)

A spectral-convergence requirement is: an integral over the **spectral parameter λ** converges. Two ingredients:

- λ ranges over an **r-dimensional** space — **r = rank = 2** — the *integration dimension*.
- the integrand powers come from the **multiplicities** m_α (short-root mult a = n − 2).

Convergence ⟺ (total power from the multiplicities) exceeds (the integration dimension = rank). So the threshold
is a relation **a ≥ f(rank)** — **f depends on the RANK** (the integration dimension), **not on the ambient
dimension n_C**. The dimension n_C enters *only* through the variable a = n_C − 2.

> **Structural verdict (supports Lyra's rescue):** the convergence criterion is naturally "short-root multiplicity
> a ≥ f(rank = 2)," which is **dimension-innocent** (f(rank) doesn't know n_C). The dimension bound n_C ≥ 5 appears
> *only* on substituting a = n_C − 2. So **"⌊n_C/2⌋ = 2" was a mis-statement of f(rank = 2)** — the "2" is the
> rank (the integration dimension), which is dimension-free. At n = 5 they coincide (rank 2 = ⌊5/2⌋), which is
> exactly why the slip hid.

So the innocence is recoverable: state the bound as "a ≥ f(rank)," with rank a prior criterion. The dimension is
still an output.

## What remains — the careful computations (I will NOT assert these from memory)

- **Q1 (decisive numerical):** is **f(rank = 2) exactly 3**? — i.e. does rank-2 spectral convergence require
  short-root multiplicity ≥ 3? This is the Gindikin-Karpelevich / Plancherel order-of-vanishing at the wall, a
  specific Harish-Chandra computation. The *structure* says rank-driven; the *value* f(2) = 3 must be **computed,
  or cited from Faraut-Korányi / Helgason**, not recalled.
- **Q2 (Cal Check 3 — derivation vs coincidence):** is N_c = 3 = a a derivation or a small-integer coincidence
  (#286)? The structural link needed: does the **(a = 3)-dimensional short-root multiplicity space carry color
  SU(3)** (vs merely SO(3))? For a *Hermitian* domain the root spaces are **complex**, so the structure group on
  the short-root space is U(·)/SU(·)-type, not SO — which is the candidate link to SU(3)_color. But *which exact
  group acts* is a structural fact to **verify**, not assert.

## Honest state (for Lyra's v0.3 and Cal)

- **SOLID (structural):** the threshold is rank-set; the dimension enters only via the multiplicity variable. This
  *recovers* the innocence claim in principle and pins the mis-statement (⌊n_C/2⌋ → f(rank)). Supports Lyra's
  rescue and Cal's fallback alike: at worst R3 jointly determines (a ≥ 3 ∧ n_C ≥ 5) from one rank-set requirement
  — still a uniqueness theorem with the dimension as output.
- **OPEN (mine, c-function lane, NOT to be faked):** Q1 (f(2) = 3) and Q2 (SU(3) on the short-root space). Both
  bounded; both careful; neither to be asserted from memory — the week's discipline.
- **v0.3 guidance:** state R3's bound as "a ≥ f(rank)" (not "⌊n_C/2⌋"); carry "maximal innocence" as *pending Q1*;
  carry N_c = 3 as *derivation pending Q2* (else honestly "a = 3 and color = 3 coincide, structural link pending").
  Count UNAFFECTED 4 of 26.

— Grace, Sunday 2026-06-21 11:29 EDT
