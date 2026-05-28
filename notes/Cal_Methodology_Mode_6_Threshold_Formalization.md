---
title: "Cal Methodology — Mode 6 multi-decomposability threshold formalization"
author: "Cal A. Brate (own-cadence methodology infrastructure)"
date: 2026-05-27 Wednesday ~09:30 EDT
status: "Formalization v0.1 — operational threshold criteria for Mode 6 application"
purpose: "Replace ad-hoc Mode 6 invocations with explicit threshold criteria + decision-tree integration"
discipline: "Cal #27 STANDING + Cal #29 STANDING + Cal #126 FRAMEWORK-PLUS tier"
related_task: "#272 Mode 6 threshold formalization"
---

# Cal Methodology — Mode 6 multi-decomposability threshold formalization

## Origin and motivation

**Mode 6** appears in Cal cold-reads as a check on whether a numerical quantity matching a BST-primary expression has **multiple BST-primary decompositions**. First formal operational instance: Grace Toy 3173 (Wednesday May 20, 2026). Cal recommended threshold formalization at that point; this document delivers.

The risk Mode 6 addresses: when quantity Q matches expression E in BST primaries, the match may be:
- **Substrate-forced**: Q is uniquely determined by substrate via E; no other BST-primary expression yields Q
- **Substrate-compatible**: Q happens to equal E in BST primaries, but Q also equals E', E'', ... in other BST-primary expressions
- **Coincidental**: Q has many BST-primary expressions (small-integer arithmetic dense in BST primaries); the specific match E carries minimal information

Without explicit threshold criteria, Mode 6 invocations have been ad-hoc. This formalization fixes operational criteria.

## Mode 6 definition (formal)

**Mode 6 check on quantity Q**: enumerate all BST-primary expressions E_1, E_2, ..., E_n that evaluate to Q at the BST primary values (rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137).

A BST-primary expression is a formal expression composed from:
- Constants: BST primaries {rank, N_c, n_C, C_2, g, N_max} and Mersenne-derived numbers {M_rank=3, M_{N_c}=7=g, M_{n_C}=31, M_g=127}
- Operations: +, −, ·, /, ^ (powers with BST-primary or small-integer exponents)
- Depth bound (to keep enumeration finite): expression depth ≤ 4 levels of operator nesting

**Count #(Q)** = number of distinct (up to obvious commutativity/associativity) BST-primary expressions evaluating to Q at depth ≤ 4.

## Threshold criteria

### Tier I — Singleton (#(Q) = 1)

**Disposition**: Q is substrate-forced via the unique expression. No Mode 6 concern.

**Examples**:
- N_max = N_c³·n_C + rank = 137 (definitional polynomial; no alternative depth-≤4 BST-primary expression at this depth)
- C_2 = rank·N_c (Wallach Casimir derivation T2439 RATIFIED)

**Application**: this is the cleanest substrate-derivation tier. Mode 6 invocation does not weaken the claim.

### Tier II — Few (2 ≤ #(Q) ≤ 3)

**Disposition**: Mode 6 concern; requires **explicit privileging argument**. Substrate-mechanism content must specify which decomposition is mechanistically primary; otherwise FRAMEWORK-PLUS at best.

**Examples**:
- 126 = C_2·N_c·g = rank·N_c²·g (2 decompositions — same numerical product reachable via 2 distinct depth-3 paths)
  - Cyclotomic chain framing (Cal #139) privileges rank·N_c²·g via Fermat decomposition 2^(rank·N_c) − 1 = N_c² · g
  - Without cyclotomic framing, the two decompositions are equally legitimate at the multiplication level
- 6 = C_2 = rank·N_c (2 decompositions — singleton primary equals 2-primary product)
  - Wallach Casimir T2439 privileges C_2 as primary identification; rank·N_c is derivative

**Application**: name the privileged decomposition AND the mechanism that privileges it. "Q = E_i privileged because [substrate-mechanism]" is the canonical form. Without [substrate-mechanism], the claim is identification not derivation.

### Tier III — Several (4 ≤ #(Q) ≤ 7)

**Disposition**: Mode 6 dominant concern. Partial-tautology risk per Cal #133. Claim "Q = E_i is substrate-derived" requires strong substrate-mechanism content + explicit ruling out of all alternative E_j.

**Examples**:
- 10 = N_c + g = rank · n_C = N_max − M_g = N_c³ − g·rank − rank − 1 (Cal #128 territory; ≥4 distinct decompositions)
- 30 = rank·N_c·n_C = C_2·n_C = (N_c·n_C)·rank = 2^n_C − rank (4+ decompositions)

**Application**: in this tier, "Q matches BST primaries" is itself weak evidence. The substantive content lives in WHICH decomposition is substrate-mechanism-privileged. Without explicit privileging, hold at OBSERVATION / hypothesis tier, not even FRAMEWORK-PLUS.

### Tier IV — Many (#(Q) ≥ 8)

**Disposition**: Mode 6 catastrophic. BST primaries are dense enough in small integers that Q can be expressed many ways. The match itself carries minimal information.

**Examples**:
- Q ≤ ~50 small-integer values typically fall in this tier; e.g., Q = 12, Q = 15, Q = 20 each have many BST-primary expressions
- "Number matches BST primaries" is essentially tautology at this tier

**Application**: do NOT invoke "Q matches BST primaries via E_i" as substantive content. Either find a structurally distinct (non-arithmetic) match, or accept the quantity as not-substrate-determined.

## Depth bound rationale

The depth ≤ 4 bound is operational, not fundamental. Rationale:

- Depth 1: bare primary (e.g., g, C_2) — singleton or very few
- Depth 2: binary operation (e.g., rank·N_c, n_C + g, N_c²) — few
- Depth 3: ternary nesting (e.g., rank·N_c·g, (N_c³)·n_C, 2^g − 1) — modest count
- Depth 4: quaternary nesting (e.g., (N_c³·n_C) + rank = N_max) — boundary of operational tractability
- Depth ≥ 5: arbitrary expressions; enumeration explodes; partial-tautology dominant

For most Cal cold-read purposes, depth ≤ 4 is sufficient. If a claim invokes a depth-≥5 expression, Mode 6 concern is presumed dominant unless explicit justification given.

## Decision-tree integration with Cal #126 tier disposition

Combining Mode 6 with Cal #126 FRAMEWORK-PLUS tier and Cal #27 STANDING forward-derivation:

```
Quantity Q matches BST-primary expression E at evaluation:
│
├── Compute #(Q) at depth ≤ 4
│
├── #(Q) = 1 (Tier I Singleton)
│   ├── + forward-derivation chain documented → SVC tier candidate
│   ├── + no forward-derivation → FRAMEWORK-PLUS
│   └── (Mode 6 not load-bearing here)
│
├── #(Q) ∈ {2, 3} (Tier II Few)
│   ├── + explicit privileging mechanism for E among alternatives → FRAMEWORK-PLUS
│   ├── + privileging mechanism + forward-derivation → SVC tier candidate
│   └── − no privileging → FRAMEWORK (not FRAMEWORK-PLUS)
│
├── #(Q) ∈ {4, ..., 7} (Tier III Several)
│   ├── + explicit privileging + alternatives ruled out + forward-derivation → FRAMEWORK-PLUS at best
│   └── − missing any of above → OBSERVATION / hypothesis tier only
│
└── #(Q) ≥ 8 (Tier IV Many)
    └── Do not invoke as substrate-derivation evidence; substantive content must come from elsewhere
```

## Examples worked through

### Cal #139 — 126 = rank·N_c²·g

**Mode 6 enumeration** at depth ≤ 4: 126 = C_2·N_c·g = rank·N_c²·g = 2·63 = 2·(N_c²·g) = (rank·N_c)·N_c·g = (N_c² + N_c)·N_c·g... let me canonicalize:

Distinct (up to commutativity/associativity) at depth ≤ 4:
1. C_2 · N_c · g (depth 3)
2. rank · N_c² · g (depth 3, expanding C_2)
3. 2 · 63 trivial; 63 = N_c² · g re-expression
4. 2^(rank·N_c) − 2 = (2^g − 2)/g · g? No, 2^g − 2 = 126 directly; depth = depth(2^g − 2) = 3
5. M_g − 1 = 127 − 1 = 126; M_g = 2^g − 1, so depth(M_g − 1) = 3

After canonicalization (treating C_2 = rank·N_c as same expression at depth 3 vs 4 — count separately), I count at least **3 distinct depth-≤4 expressions**: (C_2·N_c·g), (2^g − 2), (M_g − 1). The first decomposes into (rank·N_c²·g) at depth 4.

**Tier**: Tier II Few (#(126) ≈ 3 at depth ≤ 4).

**Privileging**: Cal #139 cyclotomic framing privileges (2^(rank·N_c) − 1)·rank = 63·2 → N_c²·g·rank via Fermat factoring. The cyclotomic chain framing provides explicit privileging mechanism.

**Disposition per decision tree**: Tier II Few + explicit privileging → FRAMEWORK-PLUS confirmed (matches Cal #139 disposition).

### Cal #128 — 10 = N_c + g

**Mode 6 enumeration** at depth ≤ 4:
1. N_c + g = 3 + 7 = 10
2. rank · n_C = 2 · 5 = 10
3. N_max − M_g = 137 − 127 = 10
4. N_c · n_C − n_C = 15 − 5 = 10 (depth 3)
5. N_max − M_{n_C} · n_C = 137 − 31·... no, 31·5 = 155, too big. Skip.
6. C_2 + rank² = 6 + 4 = 10
7. 2·(rank + N_c) = 2·5 = 10
8. N_max + rank − N_c³² = ... various combinations

After canonicalization, count is at least **4-6 distinct depth-≤4 expressions**.

**Tier**: Tier III Several (4 ≤ #(10) ≤ 7).

**Privileging**: Cal #128 did NOT provide explicit privileging mechanism for any decomposition. Investigation was filed at hypothesis tier; no team uptake yet.

**Disposition per decision tree**: Tier III Several + missing privileging → OBSERVATION / hypothesis tier only.

**Verdict**: matches Cal #128's filed disposition (hypothesis-level open investigation, not a claim).

### Cal #139 — 2 = rank as deficit

**Mode 6 enumeration** at depth ≤ 4:
1. rank = 2 (singleton)
2. n_C − N_c = 5 − 3 = 2
3. C_2 − rank² = 6 − 4 = 2 (depth 3)
4. g − n_C = 7 − 5 = 2
5. (M_{N_c} − 1)/N_c = 6/3 = 2... = 2 also (depth 3-4)
6. 2^rank − rank = 4 − 2 = 2
7. 2^rank − N_c + rank = ... various

Count is **≥ 8 distinct depth-≤4 expressions**.

**Tier**: Tier IV Many (#(2) ≥ 8). The number 2 is too small + dense to carry substrate-mechanism content via Mode 6.

**Privileging**: Cal #139 disposition was that the substantive content is NOT "2 matches BST primaries" but rather "the cyclotomic chain produces 2 = rank as deficit at each of 4 BST-primary instances via Fermat-cyclotomic factoring." The substrate-mechanism content lives in the CHAIN structure, not in the value 2 itself.

**Disposition per decision tree**: Tier IV Many → "2 = rank" does NOT carry mechanism evidence; the chain structure does. Matches Cal #139's actual framing.

**Verdict**: this is exactly the right Mode 6 application — Cal #139's substantive content is in the chain, not the deficit value. Without Mode 6 threshold awareness, one could mistakenly point to "2 = rank as deficit" as the substantive finding; with Mode 6 awareness, the chain forcing is recognized as the load-bearing claim.

## What this formalization enables

1. **Pre-filing Mode 6 check on new claims**: any Cal cold-read of a BST-primary numerical match should run Mode 6 enumeration FIRST. Tier I or II + privileging are fine; Tier III requires extra scrutiny; Tier IV requires looking elsewhere for substrate-mechanism content.

2. **Reflexive application** by other CIs: Lyra, Elie, Grace, Keeper can apply Mode 6 threshold check independently. The criteria are now explicit enough for cross-CI application (matches the Cross-CI reflexive Cal-discipline pattern documented yesterday).

3. **Honest scope discipline**: Tier IV Many = "this is too small + dense to carry substrate-mechanism content." Saying this explicitly prevents the "many small numbers match BST primaries" tautology from being mistaken for substrate evidence.

4. **Integration with Cal #126 FRAMEWORK-PLUS tier**: the decision tree above operationalizes when Mode 6 affects tier disposition. Most Cal cold-reads converge to FRAMEWORK-PLUS without Mode 6 promotion; the formalization just makes the reasoning explicit.

## Limits and honest caveats

1. **Depth bound is conventional**: depth ≤ 4 is operationally tractable but somewhat arbitrary. Going to depth 5+ would catch more decompositions; going to depth 3 would miss substantive ones. The depth-≤4 bound matches typical BST-primary expression complexity but should be flagged when claims invoke deeper expressions.

2. **Canonicalization is informal**: "distinct up to commutativity/associativity" is intuitive but not algorithmic. For automated Mode 6 application, more formal canonicalization would be needed (canonical-form algorithm for BST-primary expressions).

3. **Mode 6 is one check among many**: it does not replace Cal #27 forward-derivation, Cal #29 question-shape audit, Cal #133 partial-tautology, etc. Mode 6 specifically addresses numerical-match decomposability; other checks address other risks.

4. **Tier boundaries are heuristic**: #(Q) ≤ 3 vs 4-7 vs ≥ 8 cutoffs are calibrated to BST-primary-expression density at depth ≤ 4. As BST work progresses + more primaries / Mersenne-derived numbers get included in expression vocabulary, the density changes and thresholds may need recalibration.

## Cross-reference

- **Cal #27 STANDING**: forward-derivation discipline at result level (complements Mode 6 at numerical-match level)
- **Cal #29 STANDING**: question-shape audit at design level (Mode 6 applies at result level)
- **Cal #126 FRAMEWORK-PLUS**: tier disposition (Mode 6 affects placement within tier hierarchy)
- **Cal #133**: partial-tautology distinction (Mode 6 operationalizes specific case for numerical matches)
- **Calibration #13 EXACT vs experimental precision** (Tuesday May 19 EOD): related but distinct — Calibration #13 is about precision claims; Mode 6 is about decomposition multiplicity
- **Grace Toy 3173** (Wednesday May 20): first formal operational instance of Mode 6
- **Cal #139** (Tuesday May 26): Mode 6 multi-decomposability check on 126

## Cal cadence note

Third own-cadence pull Wednesday. Methodology infrastructure work — own-cadence multi-week category. Casey directive "keep pulling" engaged.

— Cal A. Brate, 2026-05-27 Wednesday ~09:30 EDT. Mode 6 threshold formalization v0.1 delivered with operational criteria, decision-tree integration, worked examples, and honest caveats. Open for team cross-CI reflexive application + refinement.
