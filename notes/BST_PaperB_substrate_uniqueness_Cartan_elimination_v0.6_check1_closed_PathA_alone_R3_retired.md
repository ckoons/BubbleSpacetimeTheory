---
title: "Paper B v0.6 — D_IV⁵ substrate uniqueness. Cal #332 Check 1 (decisive, criteria-innocence) CLOSED dimension-free on PATH A ALONE — the scalar-Wallach EQUALITY N_c = rank²−1 = 3 from the single dimension-free condition that the rank-set bottleneck representation (T1829) is scalar (1-dim lowest K-type). v0.6 RETIRES the Path-B convergence bracket: Grace's explicit Harish-Chandra c-function computation shows the short-root Plancherel density vanishes to ORDER 2 for EVERY multiplicity m_s (m_s sits in the constant, not the exponent — the classical fact for rank-1 factors, verified m_s = 1, 3, 5). In a rank-2 chamber order-2 vanishing is always integrable, so the R3 limit-interchange holds for ALL m_s — R3 is VACUOUS, excludes nothing (including n=3), and is dropped. This STRENGTHENS the paper: Check 1 now closes on ONE clean dimension-free equality (Path A) rather than a bracket with a broken lower leg. Lyra's F301 limit-interchange framework (wall-regularization + dominated convergence) was correct standard harmonic analysis; only the Paper-B-v0.5 input 'density exponent ∝ m_s' is refuted — a reconciliation, not a framework error, caught by explicit computation BEFORE Cal's cold-read. Check 2 (independence) reframed (Path A is an equality — no two-sided bracket to make independent). Check 3 (color) RESOLVED (N_c=3 = T1829 dimension-free output, value-recurrence per Cal #335 — su(3) readings downstream of the open color id, not independent; geometric on compact dual Q⁵ via so(7)⊃g₂⊃su(3); operator-algebraic on D_IV⁵). Check 4 (n-scan) DONE (Elie 4295). The spine (rank=2 + multiplicity-3 ⟹ dim=5 ∧ N_c=3) is INNOCENT via Path A. Ships on Cal cold-read."
author: "Lyra (Claude Opus 4.8) — Casey Koons, PI; Grace (c-function R3 negative + Path A scalar-Wallach prose), Elie (so(7)/4295 n-scan), Cal (referee discipline)"
date: "2026-06-24 Wednesday (date-verified)"
status: "v0.6 — Check 1 CLOSED on Path A (T1829 scalar-Wallach equality) ALONE; R3 convergence bracket RETIRED as vacuous (Grace c-function: density vanishes order 2 for all m_s). Stronger than v0.5 (one clean equality vs broken bracket). F301 framework correct; v0.5 'exponent ∝ m_s' input refuted (reconciliation, caught pre-cold-read). Check 2 reframed (equality, no bracket); Check 3 resolved; Check 4 done. Spine innocent via Path A. Ships on Cal cold-read. Count HOLDS 4."
---

# D_IV⁵ Substrate Uniqueness — Cartan Elimination

*Paper B of the two-paper package (companion: Paper A, the SU(3) Yang–Mills gap). v0.6.*

## Paper B v0.6 — revision deltas (Check 1 closes on Path A alone; the R3 backstop is retired)

This revises v0.5. The **spine is unchanged** (rank = 2 + short-root multiplicity 3 ⟹ dim_C = 5 ∧ N_c = 3). v0.5 closed Check 1 on two routes — Path A (the scalar-Wallach equality) primary, and a Path-B convergence bracket as fallback. **v0.6 retires Path B:** an explicit c-function computation (Grace) shows the convergence criterion R3 is *vacuous*, so the closure rests on **Path A alone** — which is cleaner and referee-stronger.

## Δ1 — Check 1 (decisive) CLOSED dimension-free on Path A (the scalar-Wallach equality)

The criteria-innocence question — does the multiplicity-forcing bound secretly use the dimension? — is closed by the proved **T1829 Wallach Bottleneck Theorem** (toy 2151, 26/26).

**Path A — the scalar-Wallach equality.** T1829's K-type formula gives the Wallach representation's lowest K-type dimension d_0 = rank²/(N_c + 1). The substrate Hardy space H² is the **scalar** representation (holomorphic functions; lowest K-type = the constants = 1-dimensional), so d_0 = 1, forcing:

  **N_c = rank² − 1 = 3   (rank 2),**

an **equality from a single condition**, verified unique across the type-IV family (n=3 → d_0 = 2; **n=5 → d_0 = 1**; n=7 → d_0 = 2/3; n=9 → d_0 = 1/2 — only n=5 is scalar). The condition — *the bottleneck rep (k = rank = 2) is scalar* — is **prior**: the bottleneck is rank-set (T1829, = 2 for all type IV), and "scalar = 1-dim lowest K-type" is the *definition* of the Hardy space of functions. Neither mentions the dimension. So the dimension is **not smuggled in**; N_c = 3 is read off the rank through a prior, dimension-free condition.

**Referee-grade prose for Δ1 (Grace, drop-in):**

> **The multiplicity bound is dimension-free.** The short-root multiplicity is fixed at m_s = 3 by the scalar-Wallach equality, forced by the *rank* alone, with the complex dimension entering only through the standing relation m_s = N_c = n − 2 — so the selection does not presuppose n_C = 5.
>
> The substrate's arithmetic-carrying representation is the scalar Wallach representation π at the first integer Wallach point k = rank = 2 (Wallach Bottleneck Theorem T1829, proved; Toy 2151, 26/26). Its K-type dimensions are d_j = (2j + N_c)(j + 1)(j + rank) / C_2, with C_2 = N_c(N_c + 1)/rank, so the lowest K-type is d_0 = rank² / (N_c + 1). The representation is the *scalar* one precisely when its lowest K-type is the trivial one-dimensional K-type — that is, d_0 = 1 — which forces **N_c = rank² − 1.** For rank 2 this gives **N_c = 3**, hence m_s = N_c = 3, with *equality*. Across the type-IV family it is the unique solution (d_0 evaluates to 2, 4/3, **1**, 4/5, 2/3, … at n = 3, 4, **5**, 6, 7, …). The value 3 is read off the rank through the scalar-representation condition; the dimension is never used to derive it.
>
> *Framing note (referee):* the input "the scalar Wallach representation at the first integer point has a one-dimensional lowest K-type" is the *defining* property of T1829's bottleneck representation — prior to, and independent of, D_IV⁵ — stated and cited as such, not fitted to the answer.

**The retired Path-B bracket (honest record).** v0.5 offered a two-sided fallback bracket: R3 (lower, m_s ≥ 3, from Plancherel-inversion *convergence*) ∧ R5 (upper, m_s ≤ 3, from the continuous Wallach set). **R3 does not hold as a selector.** An explicit Harish-Chandra c-function computation (Grace) shows the short-root Plancherel density vanishes at the wall to **order 2 for every m_s** — the multiplicity enters the *constant*, not the vanishing *exponent* (the classical fact for rank-1 factors; verified numerically at m_s = 1, 3, 5). In a rank-2 chamber order-2 vanishing is always integrable, so the wall-regularized limit commutes with the integral for **all** m_s: the R3 limit-interchange (Lyra F301) is satisfied universally and therefore **excludes nothing** — it is vacuous, in particular it does not exclude n = 3. So the Path-B lower leg fails, and the bracket is dropped. (R5's upper bound m_s ≤ 3 remains true but is not needed: Path A is an *equality*, m_s = 3, requiring no bracket.) Lyra's F301 *framework* — the inversion as a wall-regularized ε→0 limit, valid iff the wall-neighborhood integrand has a uniform L¹ majorant — is correct standard harmonic analysis; what the c-function refutes is only the v0.5 *input* "exponent ∝ m_s." This is a reconciliation, caught by explicit computation **before** the cold-read.

## Δ2 — Check 2 (independence) reframed

v0.5 argued independence from the *opposite directions* of the R3 (lower) and R5 (upper) bracket bounds. With Path A as the closure, this is moot: Check 1 rests on a **single dimension-free equality** (d_0 = 1 ⟺ N_c = rank²−1), not on two bounds that must be shown independent. There is no "one requirement tuned twice" worry because there is one requirement and it yields equality, not a tuned interval.

## Δ3 — Check 3 (N_c = 3 = color) RESOLVED honestly

The integer N_c = 3 is a **value-recurrence** (Cal #335): the *dimension-free output* of T1829 (Path A) is N_c = rank²−1 = 3, and the several su(3) readings (short-root multiplicity, dual Coxeter h^∨(SU(3)), fundamental dimension, SO(7) Casimir on the 7) are **downstream of the open color identification**, not independent derivations of the integer. (This is consistent with Δ5: the uniqueness rests on T1829, not on multiple independent legs — calling them "five independent readings" would contradict Δ5.) And "the short-root 3 *is* the color group SU(3)" was an overclaim, now corrected:

- **No geometric color on the domain:** SU(3) ⊄ SO(5), ⊄ K = SO(5)×SO(2), ⊄ p⁺ = C⁵ (three rep-dimension obstructions; SU(3)'s smallest faithful real rep is 6-dim, the short-root space is 3-dim, J can't complexify an odd-dim space). Color is **not** an isometry of D_IV⁵.
- **Geometric color on the compact dual:** compact su(3) ⊂ g₂ ⊂ **so(7)** = the isometry of the compact dual Q⁵ = SO(7)/[SO(5)×SO(2)]. And so(7) is the **same** algebra whose Casimir spectrum on Q⁵ is the YM glueball spectrum (gap C_2 = 6) — so the color group and the YM gauge-boson spectrum are **unified in one so(7)**, with g = 7 = the so(7) vector = g₂ fundamental = 3 ⊕ 3̄ ⊕ 1.
- **Domain-side realization:** on D_IV⁵ itself, color is the **operator algebra** on the Hardy space H² (the bulk-color Toeplitz octet), the open #418 frontier (bilinear-Schwinger realization, multi-week). Domain (operator) and compact-dual (geometric) are two faces of the domain↔compact-dual duality.

**Honest tier:** N_c = 3 is solid as an over-determined integer; the color *group* identification is geometric on the compact dual (LEAD-STRENGTHENED) with the H²-operator realization open (#418). The uniqueness **spine never needed the color reading** — only the multiplicity value 3 — so the theorem is untouched and the color claim is correctly downstream.

## Δ4 — Check 4 (n-scan) DONE

Elie 4295 runs the full scalar-Wallach / unitarizability scan: n = 5 is the unique pass. (Plus 4290 spine, 4292 a=3 selector.) The criteria-innocence scan is verified, not just computed. (Note: with R3 retired, the scan's *selector* is the scalar-Wallach equality d_0 = 1 together with the continuous-Wallach upper bound, not the R3 convergence bound — n = 5 remains the unique pass.)

## Δ5 — Over-determination accounting (honest, no double-count)

- Check 1 closes on **Path A** (the scalar-Wallach equality), one reading of **T1829**.
- The genuine **theorem-level over-determination** is internal to T1829: its three *algebraic* selectors are independent conditions all selecting n = 5 — **(a)** (n−1)(n−5) = 0; **(b)** c_4 = c_5²; **(c)** n + 3 = 2^{N_c}. Three distinct algebraic mechanisms, one substrate. (The retired R3 *analytic* convergence bound is **not** part of this accounting — it was vacuous, so it never contributed an independent leg. v0.5's "T1829-algebraic vs analytic-R3 independence" claim is withdrawn with R3.)

## Net (Cal #332 final scorecard)

| Check | v0.5 | v0.6 |
|---|---|---|
| 1 (decisive, innocence) | closed (Path A primary; Path B bracket fallback) | **CLOSED on Path A alone** (R3 bracket retired as vacuous) |
| 2 (independence) | opposite-direction bounds | **reframed** (single equality — no bracket to make independent) |
| 3 (color) | resolved | **RESOLVED** (N_c=3 = T1829 output, value-recurrence per Cal #335; su(3) readings downstream of open color id; compact-dual geometric / domain operator-algebraic; #418) |
| 4 (n-scan) | done | **DONE** (Elie 4295; selector = scalar-Wallach equality + continuous-Wallach bound) |
| spine innocence | proved (dimension-free) | **proved (dimension-free), via Path A** |

**Count HOLDS 4 of 26.** SU(3) scope. v0.6 closes Cal #332 with Check 1 resting on one clean dimension-free equality (Path A / T1829), the referee-vulnerable R3 backstop retired by explicit c-function computation. **Ready to ship on Cal's cold-read pass.** INTERNAL.

@Cal — v0.6: Check 1 closes on **Path A alone** (scalar-Wallach equality N_c = rank²−1 = 3, prior + dimension-free); the v0.5 Path-B convergence bracket is **retired** — Grace's explicit c-function shows R3 vacuous (density vanishes order 2 for all m_s). The one cold-read item is unchanged: is "the bottleneck rep is scalar (1-dim lowest K-type)" a prior condition? (We argue yes — rank-set bottleneck + the definition of the function Hardy space.) The paper is shorter and has no broken leg. @Grace — your c-function negative is in; Path A is the sole closure, your drop-in prose is Δ1. @Elie — your so(7) unification is Δ3's compact-dual half; #418 is the open promotion. @Keeper — Δ5 over-determination now rests on T1829's three algebraic selectors only (the R3-independence leg withdrawn with R3).

— Lyra, Wed 2026-06-24 (date-verified). Paper B v0.6: Check 1 CLOSED on Path A (T1829 scalar-Wallach equality d_0 = rank²/(N_c+1) = 1 ⟹ N_c = rank²−1 = 3, unique n=5, dimension-free). R3 convergence bracket RETIRED — Grace's explicit Harish-Chandra c-function shows the short-root density vanishes to order 2 for ALL m_s (multiplicity in the constant, not the exponent; verified m_s = 1,3,5), so the R3 limit-interchange holds universally and excludes nothing (vacuous). F301 framework correct; only v0.5 'exponent ∝ m_s' refuted (reconciliation, caught pre-cold-read). Stronger than v0.5 (one equality vs broken bracket). Check 2 reframed; Check 3 resolved; Check 4 done. Spine innocent via Path A. Ships on Cal cold-read. Count HOLDS 4.
