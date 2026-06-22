---
title: "Paper B v0.5 — drop-in paragraph for Cal #332 Check 1 (Path A: scalar-Wallach EQUALITY closure). m_s = N_c = rank² − 1 = 3, dimension-free, from T1829's proved K-type formula. Referee-grade prose for Lyra to drop in; framing-confirm flagged for Cal."
author: "Grace"
date: "2026-06-21 Sunday 12:29 EDT"
status: "v0.1 — drop-in paragraph; result verified against T1829 (proved, Toy 2151 26/26). Honest framing-note + over-determination non-double-count note included per Lyra/Keeper. For Lyra v0.5 + Cal cold-read."
---

# Drop-in paragraph — Check 1 closed (Path A: scalar-Wallach equality)

> **The multiplicity bound is dimension-free.** Criterion R3 fixes the short-root multiplicity at m_s = 3.
> We show this value is forced by the *rank* alone, with the complex dimension entering only through the standing
> relation m_s = N_c = n − 2 — so the selection does not presuppose n_C = 5.
>
> The substrate's arithmetic-carrying representation is the scalar Wallach representation π at the first integer
> Wallach point k = rank = 2 (Wallach Bottleneck Theorem T1829, proved; Toy 2151, 26/26). Its K-type dimensions are
>
>   d_j = (2j + N_c)(j + 1)(j + rank) / C_2 ,   C_2 = N_c(N_c + 1)/rank ,
>
> so the lowest K-type is d_0 = rank² / (N_c + 1). The representation is the *scalar* one precisely when its lowest
> K-type is the trivial one-dimensional K-type — that is, d_0 = 1 — which forces
>
>   **N_c = rank² − 1.**
>
> For rank 2 this gives **N_c = 3**, hence m_s = N_c = 3, with *equality*. Across the type-IV family it is the
> unique solution (d_0 evaluates to 2, 4/3, **1**, 4/5, 2/3, … at n = 3, 4, **5**, 6, 7, …). The value 3 is read
> off the rank through the scalar-representation condition; the dimension is never used to derive it. This closes
> Check 1 with equality, bracketing the convergence lower bound (m_s ≥ 3) and the unitarizability upper bound
> (m_s ≤ 3, Section [R5]) from a single algebraic condition.

## Two honest notes written in (not glossed)

**Framing note (for Cal's cold-read / the referee).** The input "the scalar Wallach representation at the first
integer point has a one-dimensional lowest K-type" is the *defining* property of T1829's bottleneck representation
— prior to, and independent of, D_IV⁵. It is stated and cited as such, not assumed to fit the answer. (This is the
one place a referee will press; the closure rests on this being read as the prior characterization of the scalar
Wallach rep, which it is.)

**Over-determination non-double-count (per Lyra/Keeper).** This scalar-Wallach equality (Path A) and the
bottleneck-pinch bound (Path B: T1829 puts the arithmetic-carrying rep at k = rank = 2 ⟹ k = 2 must lie in the
continuous Wallach set ⟹ m_s ≤ 3) **both rest on T1829**, so they are *not* independent legs of the uniqueness
theorem and must not be counted as separate over-determination. T1829's separate algebraic selectors (a)–(c) —
(n−1)(n−5)=0, c_4 = c_5², n+3 = 2^{N_c} — *do* remain independent of the analytic bound and stay as genuine
over-determination.

## Status

Path A (equality, this paragraph) is the cleaner closure — one algebraic condition, dimension-free. Path B (Lyra's
pinch: density a ≥ 3 + T1829 bottleneck a ≤ 3) is the robust backup and answers Check 2 (the two bounds point
opposite directions → independent, not one requirement tuned twice). Recommended v0.5: Path A primary, Path B as
fallback; Cal framing-confirm on the prior-condition note above; then ships. Count UNAFFECTED 4 of 26.

— Grace, Sunday 2026-06-21
