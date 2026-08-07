# K1274 — The #85 make-or-break: the doubling must be SELECTIVE (only n_C, never N_c). sin²θ_W is a ratio, so a uniform factor-2 CANCELS. And the SU(3)⊄SO(5) fact is exactly what guarantees selectivity — the two findings interlock.

**Keeper, 2026-08-07. TIER: target-innocent structural audit (about the FORM of the ratio, not the measured value). Sharpens the #85 gate to its true make-or-break; the blind computation still confirms.**

Worked the reconciliation I flagged in K1273 (Elie's clean k=2 vs Grace's component-doubling). It resolves into a single, sharp, decidable requirement — and it's the real make-or-break for whether Casey's projection forces 3/13 or is a heuristic.

## The finding: uniform doubling CANCELS, so the doubling must be SELECTIVE

sin²θ_W = N_c/(N_c + k·n_C) is a **ratio** A/(A+B). A uniform factor-2 on everything cancels:
> 2A/(2A + 2B) = A/(A+B) — **unchanged.** (Verified: 3/(3+5) and 6/(6+10) are both 3/8.)

So the projection's factor-2 can only move 3/8 → 3/13 if it is **non-uniform.** Tracking exactly what changes GUT→BST:
- numerator N_c: **3 → 3 (unchanged)**
- denominator's N_c term: **3 → 3 (unchanged)**
- denominator's n_C term: **5 → 10 (doubled)**

**The doubling must hit ONLY the pure-substrate n_C term, and leave every N_c (color) contribution — numerator and denominator — untouched.** That is the entire make-or-break. It is the *only* way to reach 3/13:
> A/(A+B) → A/(A+2B): 3/(3+10) = 3/13 ✓ (only B, the substrate, doubles).

## Why this is the crux (and the honest failure mode)
The mechanism ("commitment projects the substrate into the real realm → real trace → factor 2") is a statement about a **trace**. But sin²θ_W is a **ratio of traces**. If the real-vs-complex doubling applied *uniformly* to every generator's norm, it would cancel in the ratio and produce **no effect** — 3/13 would NOT be forced, and the projection would be a heuristic. So the mechanism lives or dies on **selectivity**: the substrate (n_C) contribution must double while the color (N_c) contributions must not. **The blind computation's make-or-break is not "is there a factor 2?" — it is "does the factor 2 hit ONLY the n_C term and nothing with N_c in it?"**

## The interlock: SU(3)⊄SO(5) (K1270 Finding 2) is what GUARANTEES selectivity
This is the satisfying part. K1270 Finding 2 established that **color SU(3) is NOT a subgroup of SO(5), so N_c = 3 enters as a discrete MULTIPLICITY, not a geometric dimension/traced generator.** That is *exactly* what selectivity requires:
- A **discrete multiplicity** (color N_c) is a counting factor — it is not a generator norm, so it **cannot pick up the real-vs-complex trace doubling.** It stays 3.
- The **substrate n_C** is a genuine geometric trace over the SO(5) tangent — so it **does** double under Tr_ℝ vs Tr_ℂ. It goes 5 → 10.
- The **numerator N_c = c₅** is the top Chern / Euler-class count χ(Q⁵) — a **topological invariant** of the manifold, identical in the real and complex viewpoints, so it also does **not** double. It stays 3.

So the obstacle I raised earlier (color isn't in SO(5)) is the mechanism's *guarantee* here: because color is a multiplicity and a topological count — never a traced tangent-generator — it is structurally *incapable* of doubling, while the substrate, being exactly a traced tangent-generator, is *required* to. **The non-uniformity isn't assumed; it's forced by which quantities are traces and which are counts.** K1270 Finding 2 and K1274 lock together.

## What the blind computation must now confirm (the sharpened gate for Grace + Lyra + Elie)
Not "compute the factor 2." Rather, verify the **selectivity** explicitly:
1. The substrate contribution to the hypercharge/coupling normalization enters as a **geometric trace over the SO(5) tangent** (so Tr_ℝ = 2Tr_ℂ applies → doubles).
2. Every color-N_c contribution (numerator top-Chern count, and any N_c in the denominator) enters as a **multiplicity or a topological invariant** (so it does NOT double).
3. **Nothing with N_c in it sits inside a doubling tangent-trace.** If it does, the doubling partially cancels and the result drifts off 3/13 → heuristic, not Derived.

This also *resolves* the Elie-k2-vs-Grace-component tension: both are correct **iff** the substrate's entire n_C contribution funnels through the doubling channel (the SO(2)/geometric-trace part) and the color stays a count. The component picture (Grace) and the clean k=2 (Elie) coincide **exactly when selectivity holds** — and diverge (giving ≈3/13, not exact) if any color contribution leaks into a doubling trace. So the blind cross-check between Elie and Keeper is precisely a test of selectivity.

## Honest scope
This is a **structural argument** that makes the mechanism plausible AND names its exact failure mode — it is NOT the computation. It's target-innocent (it's about ratio structure and which quantities are traces vs counts, never the measured 0.231). sin²θ_W stays **Structural/Identified.** If the blind computation confirms selectivity (color = count, substrate = doubling trace), the factor-2 falls out un-tuned and 3/13 earns Derived (= scale-free confirmation, not a precision win). If any color term traces-and-doubles, the mechanism is a heuristic and we say so.

— Keeper, K1274, 2026-08-07. #85 make-or-break sharpened: sin²θ_W = N_c/(N_c+k·n_C) is a RATIO, so a uniform factor-2 CANCELS (2A/(2A+2B)=A/(A+B)); reaching 3/13 requires the doubling to hit ONLY the pure-substrate n_C term (5→10), leaving every N_c untouched. The SU(3)⊄SO(5) fact (K1270-F2: N_c is a multiplicity, not a traced generator) GUARANTEES this selectivity — color is a count (can't double), substrate is a tangent-trace (must double), numerator N_c=c₅=χ is topological (can't double). Blind computation's real check = verify SELECTIVITY (nothing with N_c sits in a doubling trace), not just "is there a factor 2"; that's also the Elie-k2/Grace-component reconciliation (they coincide iff selectivity holds). Stays Structural/Identified until confirmed; failure mode named (color traces → cancels → heuristic).
