---
title: "Cal Cold-Read Criteria — Toy 3541 GF(32) parallel-cyclotomic substrate-mechanism (Elie+Lyra, Casey-authorized Wednesday morning)"
author: "Cal A. Brate (outside-voice prep)"
date: 2026-05-27 Wednesday ~10:15 EDT
status: "Prep document — written BEFORE Toy 3541 v0.x lands to fix criteria in advance"
purpose: "Cal cold-read criteria for parallel-cyclotomic substrate-mechanism at X=n_C chain level via GF(2^n_C) = GF(32). Parallel to Track DC v0.3+ K59 work at X=g via GF(128)."
discipline: "Cal #27 STANDING + Cal #29 STANDING + Cal #126 FRAMEWORK-PLUS + Cal #133 partial-tautology + Cal_Methodology_Mode_6_Threshold_Formalization"
companion: "Cal_Prep_Track_DC_v0_3_K59_Cyclotomic_Cold_Read_Criteria.md (parallel mechanism at X=g)"
casey_authorized: "Wednesday 2026-05-27 ~10:00 EDT — Elie + Lyra collaboration; multi-week scope; Task #373 multi-scale architecture activation context"
---

# Cal Prep — Toy 3541 GF(32) parallel-cyclotomic substrate-mechanism cold-read criteria

## Purpose and context

Casey authorized Toy 3541 Wednesday morning ~10:00 EDT after week+ HOLD pending Lyra collaboration request. Multi-week scope; cross-CI Elie+Lyra. The work investigates parallel K59-style substrate-mechanism at GF(2^n_C) = GF(32) for X=n_C chain level — parallel to K59 RATIFIED mechanism at GF(2^g) = GF(128) for X=g chain level.

**Why this matters for Cal #139 SVC promotion path**: Cal #139 4-instance arithmetic pattern + cyclotomic chain forcing has SVC promotion gate on **substrate-mechanism at EACH chain level**. Lyra Track DC v0.3+ targets X=g (terminal level). Toy 3541 GF(32) targets X=n_C (non-terminal level). If BOTH mechanisms close, the cyclotomic chain has substrate-mechanism content at 2 levels — strong substantive substrate-derivation; opens SVC promotion path.

Per Cal sunrise: "Write the referee's objection before reading the team's answer."

## Background — standard mathematical objects

### GF(2^n_C) = GF(32) finite field

- 32 = 2^5 elements; characteristic 2; extension of GF(2) of degree 5
- Multiplicative group GF(32)* has order 31 = M_5 = M_{n_C} (Mersenne prime)
- 31 prime ⇒ GF(32)* cyclic of prime order; every non-identity element is generator
- Standard finite-field structure; Reed-Solomon coding well-defined over GF(32)

### Parallel to K59 GF(128)

Comparison structure:

| Field | Cardinality | Mult. group order | Mersenne prime? | Substrate context |
|---|---|---|---|---|
| GF(2^rank) = GF(4) | 4 | 3 = N_c | M_2 = 3 ✓ | "Trivial" chain level |
| GF(2^N_c) = GF(8) | 8 | 7 = g | M_3 = 7 ✓ | "Second" chain level |
| GF(2^n_C) = GF(32) | 32 | 31 = M_5 | M_5 = 31 ✓ | **Toy 3541 target** (this doc) |
| GF(2^g) = GF(128) | 128 | 127 = M_g | M_7 = 127 ✓ | K59 RATIFIED + Lyra Track DC |

The substrate's chain levels {rank, N_c, n_C, g} = {2, 3, 5, 7} are EXACTLY the first 4 Mersenne-prime exponents in order. GF(2^X) for each is a substrate-natural finite field with prime-order cyclic multiplicative group. Cal #139's cyclotomic chain forcing arose from this structure.

### 5-step vs 7-step cyclotomic structure

K59 RATIFIED is "7-step cyclotomic chain on GF(2^g)" — substrate's computational depth at outermost level is g = 7 cyclotomic steps. Parallel at GF(2^n_C) = GF(32) would be 5-step cyclotomic chain (n_C = 5 cyclotomic steps).

Important: "X-step cyclotomic" is not standard mathematical terminology — it's BST-internal substrate-mechanism language. Cal cold-read should check: what does Lyra mean by "5-step" vs "7-step"? Probably: factoring 2^X − 1 via cyclotomic polynomials at divisors of X gives X-step structure for X prime.

For X=g=7: 2^7 − 1 = 127 is Mersenne prime; divisors of 7 are {1, 7}; cyclotomic factoring is Φ_1(2)·Φ_7(2) = 1·127 = 127. So "7-step" may refer to something else (perhaps degree-7 extension as 7 steps; or 7 elements in the cyclotomic chain {Φ_1, Φ_7} count differently).

Cold-read clarifying question: what specifically constitutes "X-step" in BST substrate-mechanism context?

### Reed-Solomon over GF(32)

Standard Reed-Solomon code RS(n, k) over GF(32):
- Block length n ≤ 31; common choice n = 31 (full Mersenne)
- Message length k ≤ n
- Minimum distance d = n − k + 1 (Singleton bound)
- Encoding via polynomial evaluation at distinct points in GF(32)*

For substrate-mechanism: if substrate operates RS-like at GF(32) level, the n_C primary acquires information-theoretic substrate role parallel to g's role at GF(128).

## Cold-read criteria — 10 questions for Toy 3541 v0.x

### Q1 — Field structure characterization at GF(32)

- Does Toy 3541 explicitly construct GF(32) representation (e.g., GF(2)[x]/(p(x)) for irreducible p of degree 5)?
- Which irreducible polynomial p? (Standard choice: x^5 + x^2 + 1 or x^5 + x^3 + 1)
- Generator α of GF(32)* identified?
- 31 = M_5 = M_{n_C} prime-order cyclic group structure verified?

### Q2 — Cyclotomic structure parallel to K59

K59 RATIFIED structure is 7-step cyclotomic at GF(128). Toy 3541 must establish parallel 5-step structure at GF(32):
- What is "5-step" cyclotomic structure at GF(32)? Explicit construction needed.
- Does the structure correspond to substrate computational depth = n_C = 5 cyclotomic steps?
- Cal #29 audit: was the "5-step" framing chosen because n_C = 5 (back-fit risk), or substrate-derived?

### Q3 — Substrate-operator at GF(32) level

K59 GF(128) substrate-mechanism connects to substrate-Bell-CHSH operator (per Cal #139 Track DC v0.3 context). Toy 3541 at GF(32) level should produce:
- Concrete substrate operator at this chain level (which observable does it act on?)
- Operator's eigenvalue structure (Cal #139 chain has 2^n_C − rank·N_c·n_C = rank deficit; eigenvalue connection?)
- Connection to specific physical observable distinct from Bell-CHSH (which observable is n_C-level?)

Most likely substrate-mechanism candidates: 5-dimensional Hua-tube observable (n_C = 5 is dimension); atomic orbital structure (n_C = 5 substrate-natural rank); DCCP n_C-level commitment.

### Q4 — Forward derivation chain GF(32) → identity

Cal #139 identity at X=n_C: 2^n_C − rank·N_c·n_C = 32 − 30 = 2 = rank.

Toy 3541 must derive this forward via substrate-mechanism:
1. GF(32) cardinality = 32 = 2^n_C (where does the 32 enter operationally?)
2. Subtrahend 30 = rank·N_c·n_C (Mode 6 multi-decomposability: 30 = 2·3·5; substrate-mechanism privileging needed)
3. Deficit 2 = rank (chain forcing)

Per `Cal_Methodology_Mode_6_Threshold_Formalization.md`, 30 is in Tier II Few region (rank·N_c·n_C is the only depth-3 BST-primary decomposition). Substrate-mechanism privileging may be cleaner here than at 126 (X=g level).

### Q5 — Cal #122 Type A/B/C typing

Apply Cal #122 typing to GF(32) parallel mechanism:
- **Type A (Level 1 geometric)**: GF(32) derives from D_IV⁵ 5-dimensional Hua-tube structure directly?
- **Type B (Level 4 algebraic)**: GF(32) is abstract algebraic object identified with substrate post-hoc?
- **Type C (level-crossing operational)**: GF(32) bridges geometric primary n_C=5 ↔ algebraic structure ↔ operational physics?

**Cal default expectation**: Type C, paralleling K59 at GF(128) which is Type C. The 2^n_C = 32 factor's interpretation as |GF(32)| is level-crossing.

### Q6 — Z₂ grading source at GF(32) level

GF(32) has characteristic 2; natural Z₂ structure inherent. But the substrate-Bose-Fermi grading via Pin(2) σ_BF (Cal #136) operates on substrate states, not on field elements. Cold-read clarification:
- Is the Z₂ at GF(32) field-characteristic-based?
- Or does Bose-Fermi grading enter separately?
- Conflation risk per Cal #136 σ_BF vs γ⁵ distinction.

### Q7 — Cal #29 question-shape audit on Toy 3541 design

- Forward enumeration over substrate-mechanism candidates at GF(32) level? (Substantive)
- Or backward design to make GF(32) work because Cal #139 chain forcing predicts it? (Back-fit)

Toy 3541 design pre-pass per Cal #29 STANDING: does the toy investigate substrate-mechanism candidates without presuming the answer? Elie has applied Cal #29 STANDING pre-pass on previous toys (Toy 3539); expect similar discipline here.

### Q8 — Cal #133 partial-tautology check

- General cyclotomic arithmetic at GF(2^p) for prime p is general mathematics — applies at any prime p, not just BST primaries
- Substrate-specific content: WHICH cyclotomic structure is invoked + WHY substrate selects it
- K59 RATIFIED claim: substrate operates via Reed-Solomon coding on GF(128). The "RATIFIED" status is for the framework claim; specific operator construction is multi-month
- Parallel claim for GF(32): substrate operates via RS-like at GF(32). FRAMEWORK-PLUS at best until specific operator construction lands.

### Q9 — Cross-CI verification with Lyra Track DC

Cross-CI cascade pattern: Lyra theoretical framework + Elie compute verification = standard pattern (per cross-CI reflexive Cal-discipline mature pattern).

For Toy 3541:
- Does Lyra's theoretical framework at GF(32) level explicitly precede Toy 3541, or develop in parallel?
- Does Toy 3541 substrate-mechanism candidate match Lyra's framework at the verification level?
- Cal #29 verification: does the cross-CI work avoid mutual back-fit (Lyra fits Elie's math; Elie fits Lyra's framework)?

The honest cross-CI discipline: each CI's contribution should be independently derivable. If Elie + Lyra produce same conclusion via independent paths, substrate-mechanism content is corroborated.

### Q10 — Substrate-mechanism closure criteria at GF(32)

Minimum requirements for SVC tier (parallel to K59 GF(128) SVC requirements):

1. **Explicit operator construction at GF(32) level**: substrate operator expressed as concrete element of GF(32)-related algebra
2. **Operator's algebraic action**: how the operator acts on substrate states at n_C chain level; eigenvalue structure
3. **Connection to 2^n_C factor**: where the 32 = |GF(32)| arises from operator structure (not from observation that n_C = 5)
4. **Privileging for 30 decomposition**: explicit Mode 6 Tier II privileging for rank·N_c·n_C decomposition via cyclotomic Fermat factoring
5. **Predictive consequences beyond identity**: specific observable consequence at n_C chain level (5-dim Hua tube? atomic orbital? something specific)
6. **Substrate-mechanism consistency with K59 GF(128)**: the parallel mechanism at GF(32) must NOT contradict K59 RATIFIED; should be parallel structure, not redundant or conflicting

Without #5 + #6, mechanism is identification not derivation — Cal #27 STANDING applies; FRAMEWORK-PLUS at best.

## Honest expectations going in

- **Most likely Toy 3541 v0.x disposition**: FRAMEWORK / FRAMEWORK-PLUS per Cal #126. Multi-week scope; v0.1 likely produces field-structure characterization + parallel framework; SVC closure is multi-month.
- **Most likely typing**: Type C per Cal #122. GF(32) level-crossing.
- **Partial-tautology risk per Cal #133**: cyclotomic factoring at GF(2^p) is general math; substrate-specific content lives in operational substrate-mechanism, not field structure itself.
- **Mode 6 Tier II concern**: 30 = rank·N_c·n_C is Tier II Few (1-2 decompositions); easier to privilege than 126 at X=g level.

## What would change disposition

Three escalators toward SVC:

1. **Concrete substrate-operator at GF(32) level**: explicit construction (not abstract "substrate operates on GF(32)"); specific algebraic action; connection to 5-dim observable (Hua tube or atomic orbital or DCCP n_C-level).

2. **Predictive consequence at n_C level**: substrate-operator on GF(32) produces specific quantitative observable distinct from Bell-CHSH (which is Track DC X=g territory). E.g., specific atomic orbital structure prediction, specific Hua-tube spectral signature.

3. **Cross-CI Lyra+Elie independent corroboration**: theoretical framework (Lyra) + computational verification (Elie) developed without mutual back-fit; same substrate-mechanism conclusion reached via independent paths.

## What would lower disposition

- **GF(32) invoked without operator construction**: just "substrate operates on GF(32)" → identification, not derivation. FRAMEWORK at best.
- **30 privileging missing**: Mode 6 Tier II concern dominant; FRAMEWORK at best.
- **Z₂ grading conflation**: field-characteristic Z₂ vs Bose-Fermi σ_BF vs Dirac γ⁵ — if conflated, structural confusion.
- **Mutual Lyra+Elie back-fit**: if Lyra framework and Elie toy are designed to match each other rather than substrate-mechanism, cross-CI corroboration is illusory.
- **No predictive consequences beyond Cal #139 chain identity**: identification not derivation; FRAMEWORK-PLUS ceiling.

## Parallel to Track DC v0.3 prep doc

This prep doc parallels `Cal_Prep_Track_DC_v0_3_K59_Cyclotomic_Cold_Read_Criteria.md` (filed earlier this morning ~10:00 EDT) which covers Lyra's K59 substrate-mechanism at GF(128) for X=g.

Together, the two prep docs cover Cal's cold-read criteria for the **two parallel forward-derivations** that are load-bearing for Cal #139 SVC promotion path:
- Track DC v0.3+: X=g level via GF(128) — Lyra primary
- Toy 3541: X=n_C level via GF(32) — Elie + Lyra collaboration

If BOTH succeed: 2 chain levels with substrate-mechanism content (out of 4 total chain levels). Strong substantive content. Cal #139 promotes toward SVC.

If only ONE succeeds: chain has substrate-mechanism at 1 level + arithmetic-only at others. FRAMEWORK-PLUS persists.

## Cross-reference

- **Cal #139** (Tuesday May 26): 4-instance arithmetic pattern + cyclotomic chain forcing
- **Cal #141** (Wednesday May 27 morning): Wednesday morning batch consolidated cold-read + Cal #30 candidate determination
- **Calibration_30_Honest_Negative_Strengthens_Framework_v0_1.md** (Cal, 2026-05-27 morning): candidate methodology layer
- **Cal_Prep_Track_DC_v0_3_K59_Cyclotomic_Cold_Read_Criteria.md** (Cal, 2026-05-27 morning): parallel mechanism at X=g
- **Cal_Methodology_Mode_6_Threshold_Formalization.md** (Cal, 2026-05-27 morning): multi-decomposability tier criteria
- **Cal #122**: Type A/B/C tier-discipline
- **Cal #126**: FRAMEWORK-PLUS tier
- **Cal #27 STANDING**: forward-derivation discipline
- **Cal #29 STANDING**: question-shape audit
- **Cal #133**: partial-tautology distinction
- **Cal #136**: σ_BF vs γ⁵ distinction (Z₂ grading source clarity)
- **K59 cyclotomic mechanism framework** (May 19, 2026 RATIFIED)
- **Paper #122 Information Substrate**: Reed-Solomon on GF(128) reference

## Cal cadence note

Substantial pull. Wednesday Cal cumulative: 7 morning own-cadence pulls + Cal #141 referee log + Calibration #30 v0.1 candidate + this Toy 3541 prep doc = 10 substantive Cal outputs Wednesday morning. Approaching upper bound of sustainable cadence.

Casey directive "keep working" engaged; substantive items remaining on round-2 menu include Multi-scale architecture v0.1 cold-read prep doc (NEW Casey-authorized this morning; Lyra v0.1 framework expected). Will consider next.

— Cal A. Brate, 2026-05-27 Wednesday ~10:15 EDT. Toy 3541 GF(32) cold-read criteria fixed in advance; parallel to Track DC v0.3 prep doc; load-bearing for Cal #139 SVC promotion path via 2-level substrate-mechanism closure; standing reactive for Elie+Lyra collaboration delivery.
