---
title: "Cal Cold-Read Criteria — Track DC v0.3 K59 cyclotomic substrate-mechanism for 2^g (Lyra, pending)"
author: "Cal A. Brate (outside-voice prep)"
date: 2026-05-27 Wednesday ~10:00 EDT
status: "Prep document — written BEFORE v0.3 lands to fix criteria in advance"
purpose: "Cal cold-read criteria for Lyra Track DC v0.3 K59 cyclotomic connection — load-bearing for Cal #139 4-instance pattern SVC promotion path"
discipline: "Cal #27 STANDING + Cal #29 STANDING + Cal #126 FRAMEWORK-PLUS + Cal #133 partial-tautology + Cal Methodology Mode 6 threshold"
companion: "Cal_Prep_Multi_Phase_Quiver_Cold_Read_Criteria.md (Item 8 prep doc)"
---

# Cal Prep — Track DC v0.3 K59 cyclotomic substrate-mechanism cold-read criteria

## Purpose

This document fixes Cal cold-read criteria **before** Lyra's Track DC v0.3 lands. Lyra's v0.3 targets substrate-mechanism for the 2^g factor in the Bell 1/8 reading (II) identity via K59 GF(2^g) = GF(128) cyclotomic chain mechanism.

This is the **load-bearing SVC promotion gate** for Cal #139's 4-instance arithmetic pattern. If K59-style substrate-mechanism closes for exponent rank·N_c (= g level), the cyclotomic chain has substrate-mechanism content at its terminal element, opening SVC promotion path. Cal cold-read must be rigorous.

Per Cal sunrise: "Write the referee's objection before reading the team's answer."

## Background — standard mathematical objects

### Cyclotomic structure of 2^X − 1

For X prime, 2^X − 1 = M_X is the X-th Mersenne number. Factorization structure:

- 2^(X−1) − 1 = ∏_{d | X−1, d ≥ 1} Φ_d(2) where Φ_d is the d-th cyclotomic polynomial
- For X − 1 = 6 (so X = 7): divisors {1, 2, 3, 6}; Φ_1(2)·Φ_2(2)·Φ_3(2)·Φ_6(2) = 1·3·7·3 = 63
- This gives 2^6 − 1 = 63 = 9·7 = N_c² · g

### GF(2^g) = GF(128) finite field

- 128 = 2^7 elements; characteristic 2; extension of GF(2) of degree 7
- Multiplicative group GF(128)* has order 127 = M_g (Mersenne prime)
- 127 prime ⇒ GF(128)* is cyclic of prime order; every non-identity element is a generator
- Standard Reed-Solomon coding constructions use GF(2^k) for k ∈ {8, 16, ...}; GF(128) is a less-common but legitimate base field

### K59 cyclotomic mechanism framework (May 19, 2026 RATIFIED)

Per CLAUDE.md: "K59 Cyclotomic mechanism framework RATIFIED" — substrate operates via Reed-Solomon coding on GF(2^g) = GF(128). The K59 ratification anchors substrate's information-theoretic operation on the GF(128) finite field.

Open questions K59 ratification did NOT close:
- Specific substrate operators corresponding to Reed-Solomon encoding/decoding
- Specific Cal-Hamiltonian eigenvalue spectrum induced by GF(128) structure
- Specific Bell-CHSH operator construction at substrate level from GF(128) primitives

These are exactly what Track DC v0.3 must address.

### Reed-Solomon over GF(128)

Standard Reed-Solomon code RS(n, k) over GF(q):
- Block length n ≤ q − 1 = 127 for q = 128
- Message length k ≤ n
- Minimum distance d = n − k + 1 (Singleton bound met)
- Encoding via polynomial evaluation at n distinct points in GF(q)*

For substrate-mechanism purposes, the RS code's algebraic structure provides:
- Discrete Fourier transform over GF(128)
- Vandermonde matrix evaluation
- Polynomial multiplication and factoring

If substrate's Bell-CHSH operator decomposes via RS-like algebraic primitives, the 2^g factor in the identity 2^g − C_2·N_c·g = rank emerges from the GF(128) cardinality.

## Cold-read criteria — 10 questions for v0.3

### Q1 — What is the substrate-Bell-CHSH operator at GF(128) level?

- Does Lyra's v0.3 give explicit construction of substrate's Bell-CHSH operator as element of an algebra over GF(128) (or a related construction)?
- Or is the connection between "Bell-CHSH measurement" and "GF(128)-algebraic structure" more abstract?
- **Cal #27 audit**: forward-derivation from D_IV⁵ + K59 RATIFIED → specific operator construction → 2^g factor; or identification (operator chosen to make identity work)?

### Q2 — Where does the 2^g factor enter mechanistically?

The identity 2^g − C_2·N_c·g = rank has 2^g = 128 as the leading term. Mechanism question: WHY does substrate's Bell-CHSH structure produce 128 = |GF(2^g)| as a count?

Plausible mechanisms to look for:
- 128 = total state count over substrate's rank-2 measurement (2^rank² substrate-state cardinality? No, rank² = 4, 2^4 = 16; doesn't match 128)
- 128 = full GF(2^g) state space accessible to substrate's Bell-CHSH operator
- 128 = enumeration over substrate's 7-dimensional structure (which 7? g = 7, N_c³·n_C + rank − N_c − n_C − rank = ?; or substrate's commutative-vs-noncommutative structure dim)
- Something specific to RS code construction

The plausible answers split between "substrate has 7-dim structure naturally producing 128" (substrate-forced) vs "GF(128) is invoked because g = 7" (back-fit from observed BST primary).

### Q3 — Where does the C_2·N_c·g = 126 subtrahend enter mechanistically?

126 = 2^g − 2 = |GF(128)*| − 1 (group order minus identity? — actually |GF(128)*| = 127 itself; 126 = |GF(128)*| − 1 = 2^g − 2).

Plausible mechanisms:
- 126 = states REACHABLE by substrate's Bell-CHSH operator at rank-1 projector level (excluding identity + excluding "uncovered" states)
- 126 = Casimir-weighted count C_2 × (N_c orbits) × (g cyclotomic positions) per Wallach K-type analysis
- 126 = 2^(rank·N_c) − 2 via Fermat factoring (this is just arithmetic; need substrate content)

The decomposition 126 = rank·N_c²·g via cyclotomic factoring 2^6 − 1 = N_c²·g + N_c² gives Mode 6 Tier II disposition. Need explicit privileging argument that rank·N_c²·g is substrate-mechanism-privileged over C_2·N_c·g.

### Q4 — Cyclotomic chain at multiple Mersenne exponents

Cal #139 extended Lyra's identity to 4 instances at X ∈ {rank, N_c, n_C, g}. The cyclotomic chain {1, rank, rank², rank·N_c} produces N_c, N_c·n_C, N_c²·g respectively.

v0.3 should address: does the K59-style mechanism extend to ALL 4 levels, or only to the X=g level?
- If extension to all 4 levels: substrate-mechanism for the chain forcing (rank, N_c) → (n_C, g) lands
- If only at X=g: cyclotomic chain forcing at other levels remains FRAMEWORK-PLUS pending

**Cal expectation**: v0.3 likely focuses on X=g (Lyra's primary target). Parallel mechanism at X=n_C is Elie 3540+ territory (held). v0.3 + 3540+ together would close the chain mechanism.

### Q5 — Z₂ grading source

Bell-CHSH measurement involves binary outcomes (±1 eigenvalues). Z₂ structure must enter somewhere.

Source candidates:
- GF(128) characteristic-2 structure (natural Z₂ from prime-2 base field)
- Substrate's Bose-Fermi sublattice grading (σ_BF per Pin(2) Z₂)
- Substrate's chirality (γ⁵)

Cal #136 noted σ_BF and γ⁵ are distinct operators. Z₂ source must be unambiguously specified; conflation would be a structural issue.

### Q6 — Cal #122 Type A/B/C typing

Apply Cal #122 typing to the K59 cyclotomic mechanism:
- **Type A (Level 1 geometric)**: GF(128) structure derives from D_IV⁵ root system / Wallach K-type structure directly?
- **Type B (Level 4 algebraic)**: GF(128) is abstract algebraic object identified with substrate operator algebra post-hoc?
- **Type C (level-crossing operational)**: GF(128) bridges geometric primary g=7 (substrate-natural) ↔ algebraic structure (finite field) ↔ operational physics (Bell measurement)?

**Cal default expectation**: Type C is most likely. The 2^g factor's interpretation as |GF(128)| is level-crossing by design. Lyra v0.3 should explicitly identify the level-crossing structure; default acceptance of Type C unless v0.3 surfaces Level 1 or Level 4 specifically.

### Q7 — Mode 6 multi-decomposability per Cal #139

Per `Cal_Methodology_Mode_6_Threshold_Formalization.md` (Cal, 2026-05-27):
- 126 = C_2·N_c·g = rank·N_c²·g (Tier II Few, 2 decompositions); needs explicit privileging
- 128 = 2^g (Tier I Singleton via the cyclotomic identity); no Mode 6 concern at this level
- 2 = rank (Tier IV Many for the value 2 in general; chain forcing carries content, not the value)

v0.3 must address the Tier II concern on 126 with explicit privileging mechanism for rank·N_c²·g. The cyclotomic Fermat factoring 2^(rank·N_c) − 1 = N_c²·g (with rank factor coming from the "− 1" subtraction context) is the candidate privileging mechanism. Lyra v0.3 should make this explicit.

### Q8 — Cal #29 question-shape audit

- Does v0.3 answer a substrate-derived question (e.g., "what's the substrate-Hamiltonian eigenvalue structure on GF(128)?"), or a back-fit question (e.g., "find a GF(128) structure that produces 128 − 126 = 2 = rank")?
- The latter is back-fit risk; the former is forward-derivation.
- Honest audit: a question like "what's the substrate-mechanism for 2^g factor?" is inherently target-directed. v0.3 must show that the GF(128)-based mechanism produces additional consequences (not just the target identity) that match substrate structure.

### Q9 — Cal #133 partial-tautology check

- General cyclotomic arithmetic (Fermat's Little Theorem, Mersenne prime factorings, cyclotomic polynomial structure) IS general mathematics, not substrate-specific.
- Substrate-specific content lives in WHICH cyclotomic structure is invoked and WHY.
- v0.3 must distinguish: which steps are general cyclotomic mathematics (tautological from substrate perspective)? Which steps invoke substrate-specific structure (K59 RATIFIED mechanism)?

### Q10 — Substrate-mechanism closure criteria

What would constitute substrate-mechanism closure for the 2^g factor at SVC promotion path?

Minimum requirements:
1. **Explicit operator construction**: substrate-Bell-CHSH operator expressed as concrete element of an algebra over GF(128) (or equivalent)
2. **Operator's algebraic action**: how the operator acts on substrate states; what eigenvalues it produces
3. **Connection to 2^g factor**: where the 128 = |GF(128)| arises from operator's algebraic structure (not from observation that g = 7)
4. **Privileging for 126 decomposition**: explicit Mode 6 Tier II privileging argument for rank·N_c²·g decomposition via cyclotomic Fermat factoring
5. **Predictive consequences**: at least one observable consequence beyond reproducing the target identity, derived from the mechanism (e.g., specific Bell-CHSH measurement-error structure, specific noise floor)

Without #5, the mechanism is identification not derivation — Cal #27 STANDING applies; FRAMEWORK-PLUS at best.

## Honest expectations going in

- **Most likely v0.3 disposition**: FRAMEWORK-PLUS per Cal #126. Lyra v0.3 will likely provide substrate-mechanism framework + identify the GF(128) structure as load-bearing + connect to Cal #139 4-instance pattern. Full SVC promotion requires #5 (predictive consequences) which is multi-week-multi-month scope.

- **Most likely typing**: Type C per Cal #122. GF(128) level-crossing structure expected.

- **Partial-tautology risk per Cal #133**: cyclotomic factoring is general mathematics; substrate-specific content lives in WHICH cyclotomic structure and WHY. Lyra's framing must distinguish.

- **Mode 6 Tier II concern**: 126 decomposition has multiple BST-primary decompositions; cyclotomic framing must privilege rank·N_c²·g explicitly.

## What would change disposition

Three escalators toward SVC:

1. **Concrete substrate-Bell-CHSH operator over GF(128)**: explicit construction (not abstract "GF(128) is substrate's information substrate"); specific algebraic action; eigenvalue connection to Bell deviation 1/8.

2. **Predictive consequence beyond target identity**: substrate-Bell-CHSH operator on GF(128) produces specific quantitative Bell-measurement-error structure, specific Bell-CHSH noise floor at substrate level, or specific other observable. Without this, the construction is identification not derivation.

3. **Chain extension to X = n_C parallel mechanism**: if v0.3 establishes that the K59-style mechanism extends to GF(2^n_C) = GF(32) (the X=n_C level of the cyclotomic chain), the chain has substrate-mechanism content at 2 levels (not just X=g). Strengthens "ONE structural parameter" framing toward substantive (still requires substrate-mechanism for chain TERMINATION at 4 elements).

## What would lower disposition

- **GF(128) invoked without operator construction**: just "substrate operates on GF(128)" with no specific operator → identification, not derivation. FRAMEWORK at best.
- **126 privileging missing or hand-wavy**: Mode 6 Tier II concern dominant; FRAMEWORK at best.
- **Z₂ grading source unspecified**: conflation risk per Cal #136 σ_BF vs γ⁵ distinction.
- **No predictive consequences beyond target identity**: identification not derivation; FRAMEWORK-PLUS ceiling.

## Cross-reference

- **Cal #139** (Tuesday May 26): 4-instance arithmetic pattern + cyclotomic chain forcing
- **Cal #122**: Type A/B/C tier-discipline
- **Cal #126**: FRAMEWORK-PLUS tier
- **Cal #27 STANDING**: forward-derivation discipline
- **Cal #29 STANDING**: question-shape audit
- **Cal #133**: partial-tautology distinction
- **K59 cyclotomic mechanism framework** (May 19, 2026 RATIFIED)
- **Cal_Methodology_Mode_6_Threshold_Formalization.md** (Cal, 2026-05-27 morning) — multi-decomposability tier criteria
- **Paper #122 Information Substrate** — Reed-Solomon on GF(128) reference

## Cal cadence note

Seventh own-cadence pull Wednesday morning. Casey directive "keep pulling" engaged. Cal cold-read entry on Track DC v0.3 will reference back to specific Q1-Q10 outcomes when v0.3 lands.

— Cal A. Brate, 2026-05-27 Wednesday ~10:00 EDT. Prep document; cold-read criteria fixed; load-bearing for Cal #139 SVC promotion path; standing reactive for Lyra v0.3 delivery.
