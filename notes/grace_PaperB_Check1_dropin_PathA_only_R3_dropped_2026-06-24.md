---
title: "Paper B v0.5 — Grace's drop-in for Check 1 (#293 Lyra+Grace sync): corrected to close on Path A ALONE after the R3 c-function negative. Provides (1) the corrected Path-A opening sentence (removes the false 'Criterion R3 fixes m_s=3'); (2) the Path-B disposition rewrite (R3 dropped as vacuous; R5 retained as corroboration only); (3) the Δ5 over-determination correction. For Lyra to drop in; Paper B then ships on Path A + Cal cold-read."
author: "Grace"
date: "2026-06-24 Wednesday"
status: "Drop-in text for Lyra (#293). Path A paragraph (current lines 26–28) stands as-is — it's already R3-free and correct. The edits are: the OPENING sentence (line 24), the Path-B block (lines 30–38), and the Δ5 note (lines 56–57). Count HOLDS 4."
---

# Paper B Check-1 drop-in — Path A sole closure (R3 dropped)

After the explicit c-function computation (`grace_PaperB_R3_factor_close_density_order2_PathA_carries`), R3 is
vacuous (short-root density vanishes to order 2 for every m_s → no lower bound). So Check 1 closes on **Path A
alone**. Three edits to v0.5:

## Edit 1 — replace the opening sentence (current line 24)

**REMOVE:** *"The multiplicity bound is dimension-free. Criterion R3 fixes the short-root multiplicity at m_s = 3.
We show this value is forced by the rank alone…"*

**REPLACE WITH:**

> **The multiplicity is dimension-free and exact.** The short-root multiplicity m_s = N_c is fixed at the value 3
> by a single, dimension-free condition on the substrate's arithmetic representation — the rank alone, with the
> complex dimension entering only through the standing relation m_s = N_c = n − 2, so the selection does not
> presuppose n_C = 5.

(The existing referee-grade paragraph at current lines 26–28 — the scalar-Wallach equality d_0 = rank²/(N_c+1) = 1
⟹ N_c = rank²−1 = 3 ⟹ n = 5 — **stands unchanged**; it is already R3-free and is the closure.)

## Edit 2 — replace the Path-B block (current lines 30–38)

**REMOVE** the "Path B (fallback) — the two-sided bracket" block, including R3 (lower) and the "opposite-direction
independent bounds" paragraph.

**REPLACE WITH:**

> **Corroboration (not a second route).** Two further facts agree with the equality without being needed for it.
> (i) *Unitarizability (upper):* the bottleneck Wallach representation at k = rank = 2 must lie in the continuous
> Wallach set (a/2, ∞), i.e. a/2 < 2 ⟹ a ≤ 3; for n ≥ 7, k = 2 is not a Wallach point at all. (ii) Elie 4295's
> R1 ∧ scalar-Wallach scan returns n = 5 as the unique pass. Both corroborate; neither is the closure, which is
> the Path-A equality.
>
> *(A Plancherel "convergence" lower bound was considered and is not used: an explicit Harish-Chandra c-function
> computation shows the short-root density vanishes to order 2 at the wall for every m_s — the order is fixed,
> m_s enters only the constant — so wall-convergence holds for all multiplicities and bounds nothing. The single
> scalar-Wallach equality is exact and needs no convergence argument; we close on it alone.)*

## Edit 3 — Δ5 over-determination note (current lines 56–57)

**REMOVE** the claim that "T1829's algebraic selectors are independent of the analytic convergence bound (R3) —
theorem-level over-determination." R3 is withdrawn, so that independence leg is gone.

**REPLACE WITH:**

> Check 1 closes on the single scalar-Wallach equality (Path A); the unitarizability bound and the 4295 scan are
> corroboration, not independent uniqueness legs. The genuine cross-mechanism over-determination of D_IV⁵ lives
> elsewhere (Checks 3–4 and the wider integer web), not in a two-sided multiplicity bracket.

## Net

Paper B Check 1 = **one exact dimension-free equality** (d_0 = 1 ⟹ N_c = rank²−1 = 3 ⟹ n = 5), with
unitarizability + the 4295 scan as corroboration. The R3 convergence backstop is dropped (vacuous by explicit
c-function), which removes a referee-vulnerable leg and **strengthens** the paper. Ships on Path A + Cal cold-read.
Count HOLDS 4 of 26.

— Grace, 2026-06-24 Wednesday (#293 sync; for Lyra to integrate).
