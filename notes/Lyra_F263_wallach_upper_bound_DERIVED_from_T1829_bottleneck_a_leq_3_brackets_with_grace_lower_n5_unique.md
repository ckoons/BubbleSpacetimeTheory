---
title: "F263 — my half of the Wallach derivation, CLOSED, grounded in the existing PROVED T1829 (Wallach Bottleneck Theorem, toy 2151 26/26). The UPPER bound m_s ≤ 3 is now DERIVED, not asserted: T1829 establishes that the BST-relevant substrate representation sits at the bottleneck Wallach parameter k = rank = 2 (the first integer Wallach point, through which weight-2 modular forms / elliptic curves / BSD L-values pass). For that bottleneck rep to EXIST and carry full arithmetic content, k=2 must lie in the Wallach set W = {0, a/2} ∪ (a/2, ∞) — specifically in the CONTINUOUS part (a/2, ∞). This requires a/2 < 2, i.e., a < 4, i.e. a ≤ 3 (a = m_s = n−2). VERIFIED across the family: n=3 (a=1) and n=5 (a=3) → k=2 in the continuous part ✓; n=7 (a=5), n=9 (a=7) → k=2 is BELOW the set (2 < a/2), so the bottleneck rep DOES NOT EXIST → excluded. So R5 (upper, a≤3) excludes n≥7, DERIVED from T1829. This REFINES/GROUNDS Paper B's old 'R5 = Selberg d_F≤2' assertion: the upper bound is now a Wallach-bottleneck existence statement, principled. COMBINED CLOSE: R5 (upper, a≤3, mine, derived) ∧ R3 (lower, a≥3, Grace's Plancherel/convergence density, excludes n=3) ∧ R2 (tube, n odd) ⟹ a=3, n=5, N_c=3 — UNIQUE. Neither bound alone suffices (R5 doesn't exclude n=3; R3 doesn't exclude n≥7), so the close is genuinely JOINT, exactly as Casey routed (Lyra+Grace). CRITERIA-INNOCENCE (Cal #332 Check 1, decisive): both bounds are conditions on the MULTIPLICITY a and the rank-2 Wallach structure; the dimension enters ONLY through a = n−2 — dimension genuinely not smuggled. Check 2 (independence): the bounds are OPPOSITE-DIRECTION (convergence-from-below + bottleneck-existence-from-above), independent (F262). HONEST DEPENDENCIES: (1) Grace's R3 lower-bound numerical value (a≥3) is her density computation — structurally confirmed, exact number hers; (2) my upper bound is GROUNDED IN T1829, so it is NOT independent of T1829 (don't double-count as separate over-determination). v0.5 ships when Grace's lower-bound number lands; my half is IN."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-21 Sunday 13:40 EDT"
status: "v0.1 — my half of the Wallach derivation CLOSED. R5 (upper, m_s≤3) DERIVED from T1829's k=rank=2 bottleneck (rep must be in continuous Wallach part ⟹ a<4 ⟹ a≤3; excludes n≥7, verified). Brackets with Grace's R3 (lower, a≥3, density, excludes n=3) + R2 (tube) ⟹ n=5 unique. JOINT close (neither alone). Criteria-innocent: dimension via multiplicity only (Check 1 decisive). Check 2: opposite-direction independent bounds. Grounded in T1829 (not independent of it). v0.5 ships on Grace's lower number. Count HOLDS 4. For Grace, Casey, Cal, Keeper, Elie."
---

# F263 — Wallach upper bound DERIVED from T1829; the bracket closes at n=5

Casey routed the Wallach derivation (Lyra + Grace) to close Cal #332 Check 1 and ship Paper B v0.5. My half is now done — and it's grounded in an existing **PROVED** result (T1829, the Wallach Bottleneck Theorem, toy 2151 26/26), not a fresh assertion.

## The upper bound, derived

T1829 establishes that the BST-relevant substrate representation sits at the **bottleneck Wallach parameter k = rank = 2** — the *first integer Wallach point*, the "narrowest passage" through which weight-2 modular forms, elliptic curves, and BSD L-values pass. Take that as given (it's proved).

For that bottleneck representation to **exist** and carry its full arithmetic content, k = 2 must lie in the Wallach set W = {0, a/2} ∪ (a/2, ∞) — and in the **continuous part** (a/2, ∞), not at a degenerate boundary point (a = m_s = n−2, rank r = 2). This requires:

  **2 > a/2  ⟺  a < 4  ⟺  a ≤ 3.**

Verified across the family:

| n | a = n−2 | top discrete a/2 | k = 2 status | bottleneck rep |
|---|---|---|---|---|
| 3 | 1 | 0.5 | in continuous part (2 > 0.5) | exists ✓ |
| **5** | **3** | **1.5** | **in continuous part (2 > 1.5)** | **exists ✓** |
| 7 | 5 | 2.5 | **below the set (2 < 2.5)** | **does NOT exist ✗** |
| 9 | 7 | 3.5 | below the set (2 < 3.5) | does NOT exist ✗ |

For n ≥ 7 the bottleneck rep at k = rank = 2 **isn't a Wallach point at all** — the substrate's arithmetic-carrying representation simply doesn't exist there. So **R5 (upper): a ≤ 3 excludes n ≥ 7, derived from T1829.** This grounds (and arguably replaces) Paper B's old "R5 = Selberg degree d_F ≤ 2" assertion with a principled Wallach-bottleneck existence statement.

## The joint close

| bound | direction | mechanism | excludes | status |
|---|---|---|---|---|
| **R5: a ≤ 3** | upper | Wallach bottleneck k=rank=2 must exist (T1829) | n ≥ 7 | **DERIVED (this note)** |
| **R3: a ≥ 3** | lower | Plancherel/trace-formula convergence (density wall-order ∝ a) | n = 3 | Grace (structurally confirmed; numerical value hers) |
| **R2: n odd** | — | tube type / rational functional equation | even n | SOLID |

**R5 ∧ R3 ∧ R2 ⟹ a = 3, n = 5, N_c = 3 — unique.** The close is genuinely **joint**: R5 alone does not exclude n = 3 (a=1: k=2 is in the continuous part, rep exists), and R3 alone does not exclude n ≥ 7. Each half removes what the other cannot — exactly the Lyra+Grace pairing Casey routed.

## Cal #332 resolved

- **Check 1 (decisive, criteria-innocence):** both bounds are conditions on the **multiplicity a** and the **rank-2** Wallach structure; the dimension enters **only through a = n−2**. The dimension is genuinely not smuggled — confirmed from both sides now (lower: Grace; upper: this note). The "2" throughout is the rank (discrete Wallach point count + bottleneck k=rank=2), never ⌊n_C/2⌋.
- **Check 2 (independence):** the two bounds point in **opposite directions** (convergence-from-below, bottleneck-existence-from-above). They are independent constraints that meet at a = 3, not one requirement tuned twice (F262).
- **Check 3:** color over-determination + no geometric SU(3) (F258/F259), separately resolved.
- **Check 4:** Elie 4295 n-scan, done.

## Honest dependencies (no over-counting)

1. **Grace's R3 lower-bound numerical value (a ≥ 3)** is her Plancherel density computation — structurally confirmed ("order ∝ a"), the exact threshold number is hers to land. v0.5 ships when it does.
2. **My upper bound is GROUNDED IN T1829** — so it is *not* independent of T1829. Paper B's selection and T1829's own n=5 selection (its three equations a/b/c) **share the Wallach-bottleneck structure**; do not count them as separate over-determination legs for the upper bound. (T1829's three *algebraic* selectors a/b/c remain independent of the *analytic* convergence bound R3 — that genuine independence is worth keeping; the Wallach-bottleneck upper bound is the shared piece.)

## Net (Result | Confidence | Next)

| Result | Confidence | Next |
|---|---|---|
| R5 upper bound a ≤ 3 (bottleneck k=rank=2 ∈ continuous Wallach part) | DERIVED (grounded in T1829, verified) | — |
| joint close R5∧R3∧R2 ⟹ n=5 | SOLID modulo Grace's R3 number | Grace lands a≥3 density value |
| Check 1 dimension-innocence (both sides) | CONFIRMED | — |
| Check 2 independence (opposite-direction bounds) | SOLID (F262) | — |
| upper bound vs T1829 independence | NOT independent (grounded in T1829) — flagged | Keeper over-determination accounting |

**Count HOLDS 4 of 26.** SU(3) scope. My half of the Wallach derivation is closed: the upper bound a ≤ 3 is derived from T1829's bottleneck, brackets with Grace's lower bound, and the close is criteria-innocent (dimension via multiplicity only). v0.5 ships on Grace's lower-bound number. INTERNAL.

@Grace — reassignment confirmed and my half done: **Wallach gives the UPPER bound (a ≤ 3), via T1829's k=rank=2 bottleneck** — not the lower bound you'd expected my Wallach work to give. The **lower bound a ≥ 3 is YOUR convergence/density** (excludes n=3), which my upper bound can't do. So the bracket is: your density (a≥3) + my T1829 bottleneck (a≤3) + R2 tube ⟹ n=5. v0.5 ships when your density lands the exact a≥3; my T1829 half is in. Your toy_2140 Wallach K-type decomposition is the corpus anchor for the discrete points; T1829/toy_2151 is the bottleneck anchor. @Casey — my half closed, grounded in our own PROVED T1829 rather than a fresh assertion; the close is genuinely joint with Grace. @Cal — Checks 1 and 2 resolved (dimension-innocence from both sides; opposite-direction independence). @Keeper — flag: the upper bound is grounded in T1829, NOT independent of it (don't double-count); but T1829's three algebraic selectors stay independent of the analytic R3 — genuine over-determination there.

— Lyra, Sun 2026-06-21 13:40 EDT (date-verified). F263: Wallach upper bound DERIVED. T1829 (PROVED, toy 2151) puts the BST rep at the bottleneck k=rank=2; it must lie in the continuous Wallach part (a/2,∞) ⟹ a<4 ⟹ a≤3 (R5 upper). Verified: n=3,5 → k=2 in continuous part (rep exists); n≥7 → k=2 below the set (rep doesn't exist) → excluded. Brackets with Grace's R3 (lower, a≥3, density, excludes n=3) + R2 (tube) ⟹ a=3, n=5, N_c=3 unique — JOINT (neither alone). Criteria-innocent: dimension via multiplicity a=n−2 only (Check 1 decisive, both sides). Check 2: opposite-direction independent bounds. Upper bound grounded in T1829 (not independent of it). v0.5 ships on Grace's lower number. Count HOLDS 4.
