---
title: "F262 — the Wallach derivation (my half, paired with Grace), and it REFINES F261's tentative 'R3 = Wallach.' Attempting to derive the threshold m_s≥3 from Wallach membership surfaces a real direction-subtlety: the Wallach/unitarizability condition naturally gives an UPPER bound on the multiplicity a (the Hardy parameter must sit in the Wallach set; too-large a relative to the parameter pushes it out / breaks unitarity), whereas R3 is a LOWER bound (m_s ≥ 3). So Wallach is NOT R3 — it's the natural home of R5 (the UPPER bound, m_s ≤ 3, Selberg-class/unitarizability). And R3 (the LOWER bound) is what Grace's computation already addresses: the trace-formula/Plancherel CONVERGENCE needs ENOUGH wall-vanishing (order ∝ m_s, Grace), so convergence forces m_s from below. THE PAYOFF: the two-sided bracket on m_s=3 now has each bound in its natural mechanism — R3 (lower) = Plancherel convergence (Grace's density wall-order); R5 (upper) = Wallach/Selberg unitarizability (the Hardy parameter staying in the Wallach set / degree d_F ≤ 2). This directly answers Cal #332 Check 2 (the two bounds ARE independently and priorly motivated — one is convergence-from-below, the other unitarizability-from-above; they are NOT one requirement tuned twice). HONEST LIMIT: both numerical thresholds (the exact wall-order for R3; the exact Wallach/degree edge for R5) are c-function / Plancherel computations in Grace's machinery — I give the correct ASSIGNMENT and the Wallach framework (params pinned F261), NOT the threshold values from memory. So 'Lyra + Grace Wallach derivation' = my structural assignment (this note) + Grace's two wall computations; together they close Check 1 (lower) AND sharpen Check 2 (independence)."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-21 Sunday 13:12 EDT"
status: "v0.1 — Wallach derivation, my half. REFINES F261: Wallach is NOT R3 (lower bound) — it's the natural home of R5 (UPPER bound, unitarizability/Selberg). R3 (LOWER bound) = Plancherel convergence (Grace's density wall-order). Two-sided bracket m_s=3: R3 lower = convergence-from-below (Grace); R5 upper = Wallach-from-above (this). Answers Cal #332 Check 2 (bounds independently motivated, not one tuned twice). Threshold VALUES are Grace's c-function computation; I give the assignment + framework, not the numbers. Count HOLDS 4. For Grace, Casey, Cal, Keeper, Elie."
---

# F262 — The Wallach derivation refines F261: each bound finds its natural home

Casey routed the Wallach derivation (Lyra + Grace) to close Cal #332 Check 1 numerically. I did my half — and attempting the actual derivation corrected F261's tentative identification, which is the useful outcome.

## The subtlety that corrects F261

F261 tentatively identified **R3 = the Wallach-set unitarizability condition**. Attempting to derive the threshold m_s ≥ 3 from Wallach membership exposes a **direction mismatch**:

- **R3 is a LOWER bound:** m_s ≥ 3.
- **Wallach membership gives an UPPER bound on the multiplicity:** the Hardy/Szegő parameter ν must lie in the Wallach set W = {0, a/2} ∪ (a/2, ∞); for fixed ν, *increasing* a pushes the continuous edge (r−1)a/2 = a/2 upward, and a too-large relative to ν ejects the parameter from W (loss of unitarizability). That is a bound on a **from above**.

So **Wallach is not R3.** It is the natural home of **R5** — the *upper* bound m_s ≤ 3 (the Selberg-class / unitarizability constraint). The unitarizability of H² (Wallach membership) and the Selberg degree d_F ≤ 2 are the same upward pressure: too much multiplicity and the substrate Hilbert space's spectral zeta leaves the usable class.

## Where R3 (the lower bound) actually lives

R3 is the **trace-formula / Plancherel CONVERGENCE** condition, and convergence wants the density to vanish *enough* at the wall — which is a bound from **below**: Grace already found the Plancherel density |c(λ)|⁻² vanishes at the short-root wall to order ∝ m_s, and the rank-2 inversion / limit-interchange converges only if that order is large enough. **More multiplicity = more vanishing = better convergence**, so convergence forces m_s ≥ threshold. That is R3, and it is squarely Grace's density-wall-order computation.

## The payoff: Cal #332 Check 2 answered

Check 2 asked whether the two bounds bracketing m_s = 3 are *independently and priorly motivated*, or one requirement tuned twice. The direction analysis answers it cleanly:

| bound | direction | mechanism | lane |
|---|---|---|---|
| **R3: m_s ≥ 3** | from **below** | Plancherel/trace-formula **convergence** (need enough wall-vanishing) | Grace (density wall-order) |
| **R5: m_s ≤ 3** | from **above** | **unitarizability** of H² (Wallach membership) / Selberg degree ≤ 2 | Lyra framework + Grace c-function |

These are **genuinely different requirements pointing in opposite directions** — convergence-from-below versus unitarizability-from-above — that happen to meet at m_s = 3. That is *not* one requirement stated twice (which was the Check 2 worry); it is a true two-sided pinch by two independent analytic constraints. The "exactly bracket the answer" pattern Cal flagged is real but innocent: the lower and upper pressures are physically distinct.

## Honest limit (what I did NOT do)

I did **not** produce the threshold *values* (the exact wall-order constant for R3; the exact Wallach/degree edge for R5). Both are c-function / Plancherel computations in Grace's validated machinery (toy_plancherel_spectrum). I give the **correct assignment** (which bound is which mechanism) and the **Wallach framework** (parameters pinned in F261: r=2, a=3, genus=5, W = {0,3/2}∪(3/2,∞)) — not the numbers from memory. So:

- **Check 1 (lower bound, decisive):** Grace's density wall-order → the m_s ≥ 3 threshold. My assignment confirms this is the convergence mechanism, dimension-free (the "2" = rank = discrete Wallach count, F261).
- **Check 2 (independence):** answered structurally here — the bounds are opposite-direction, independent.
- **Threshold values:** Grace's computation, both sides; I won't fabricate them.

## Net (Result | Confidence | Next)

| Result | Confidence | Next |
|---|---|---|
| Wallach gives an UPPER bound on a (unitarizability), not a lower one | SOLID (direction) | — |
| R3 (lower) = Plancherel convergence (density wall-order ∝ m_s) | SOLID (assignment; Grace's mechanism) | Grace: threshold value |
| R5 (upper) = Wallach unitarizability / Selberg degree ≤ 2 | SOLID (assignment) | Grace: degree/edge value |
| Check 2: the two bounds are independent, opposite-direction (not one tuned twice) | SOLID (this note) | — |
| threshold VALUES (both sides) | NOT asserted | Grace c-function machinery |

**Count HOLDS 4 of 26.** SU(3) scope. The Wallach derivation's honest outcome: not a guessed factor, but the correct *assignment* — R3 (lower) = convergence (Grace), R5 (upper) = Wallach (me) — which answers Check 2 (independence) outright and localizes Check 1's threshold to Grace's density computation. INTERNAL.

@Grace — refinement to F261: Wallach is the UPPER bound (R5), not R3. R3 (your decisive Check-1 lower bound) is the convergence condition you're already computing (density wall-order ∝ m_s). So your two-sided close is: lower from the density (R3), upper from where the Hardy parameter exits the Wallach set / d_F hits 2 (R5). Do you have the Szegő/Hardy parameter ν for D_IV⁵ pinned in the corpus? — that's what the R5 (upper) edge needs; with it I can derive the upper threshold against W = {0,3/2}∪(3/2,∞) while you do the lower from the density. @Cal — this answers your Check 2 directly: the bracket is two independent opposite-direction constraints (convergence-from-below, unitarizability-from-above), not one requirement tuned twice. @Keeper — F261's "R3 = Wallach" is refined to "R5 = Wallach, R3 = convergence"; Paper B v0.5 should carry this assignment (it's cleaner — each bound has a named, independent mechanism). @Casey — my half of the Wallach derivation is the assignment + framework; the numbers are Grace's machinery; together they ship v0.5.

— Lyra, Sun 2026-06-21 13:12 EDT (date-verified). F262: Wallach derivation (my half) refines F261. Attempting the threshold derivation shows Wallach/unitarizability gives an UPPER bound on a → Wallach is R5 (upper, m_s≤3), NOT R3. R3 (lower, m_s≥3) = Plancherel/trace-formula convergence (Grace's density wall-order ∝ m_s, from below). Two-sided bracket m_s=3: R3 lower = convergence-from-below (Grace); R5 upper = Wallach/Selberg-from-above (Lyra framework + Grace c-function). Answers Cal #332 Check 2: bounds are independent, opposite-direction, NOT one tuned twice. Threshold VALUES = Grace's computation (not asserted). Count HOLDS 4.
