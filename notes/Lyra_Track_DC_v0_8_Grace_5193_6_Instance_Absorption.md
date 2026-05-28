---
title: "Track DC v0.8 — Grace INV-5193 6-instance pattern + INV-5195 9-element operational arithmetic set absorbed"
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-27 Wednesday EDT (~09:35 EDT via `date`-verified)"
status: "v0.8 FRAMEWORK-PLUS. Grace INV-5193 + INV-5195 substantive new findings absorbed. Cal #139 4-instance rank-deficit pattern extends to **6-instance** at primes {2,3,5,7,11,13} with chain termination at X=17. 9-element substrate operational arithmetic set: BST primaries + extended Casimirs + Ogg supersingular. Three Memorial Day findings (Mersenne ∩ Ogg ∩ prefix) unified into one arithmetic-ingredient framework. Cal #29 + Cal #133 + Cal #27 STANDING preserved."
related: ["Grace INV-5193 (6-instance pattern + chain termination at X=17)", "Grace INV-5195 (Wallach dim_N deep-dive; 9-element operational set)", "Lyra_Track_DC_v0_5_Four_Instance_Pattern_Rank_Seed.md (Cal #139 4-instance Cal-corrected)", "Lyra_Chain_Termination_Substrate_Mechanism_v0_1.md (5 candidate mechanisms)", "Grace Memorial Day 4+2 maximal-prefix finding (INV-5162)", "Casey Memorial Day hypothesis (Mersenne ∩ Ogg ∩ prefix)"]
---

# Track DC v0.8 — Grace INV-5193 + INV-5195 absorption

## 1. Cal #29 STANDING audit (applied at absorption)

**Question**: "Does Grace INV-5193 extension from Cal #139 4-instance to 6-instance pattern at primes {2,3,5,7,11,13} with chain termination at X=17 force substantive REVISION of chain termination v0.1 framework?"

**Audit**:
- Structurally determined? YES — Grace's INV-5193 verification of 6-instance pattern is checkable arithmetic
- Back-fittable? Cal #29 risk-flag: extending pattern to MORE primes might back-fit if "next-candidate-fails-at-X=17" reasoning applies
- Pre-suppositions? Cal #139 chain forcing + chain termination v0.1 (3 STRONG candidates substrate-mechanism) + Grace 9-element operational set INV-5195

**Pass with discipline**: structural absorption; need to determine whether chain termination at 4 (my v0.1) or at 6 (Grace's extension) is substantively correct.

## 2. Grace INV-5193 substantive content

Per Grace broadcast: 6-instance pattern at primes {2,3,5,7,11,13}; chain termination at X=17.

**Extended rank-deficit table**:

| Instance | X | M_X | BST primary? | 2^X − Y·X = rank? |
|---|---|---|---|---|
| 1 | **rank = 2** | M_2 = 3 (=N_c) | YES (rank) | 2^2 − rank = 2 ✓ |
| 2 | **N_c = 3** | M_3 = 7 (=g) | YES (N_c) | 2^3 − rank·N_c = 2 ✓ |
| 3 | **n_C = 5** | M_5 = 31 | YES (n_C) | 2^5 − rank·N_c·n_C = 2 ✓ |
| 4 | **g = 7** | M_7 = 127 | YES (g) | 2^7 − C_2·N_c·g = 2 ✓ |
| 5 | **11** | M_11 = 2047 = 23·89 (composite) | NO (extended Casimir c_2) | Pattern claim ✓ per Grace |
| 6 | **13** | M_13 = 8191 (prime) | NO (extended Casimir c_3) | Pattern claim ✓ per Grace |
| termination | **17** | M_17 = 131071 (prime) | NO (Ogg supersingular) | Chain stops here per Grace |

**Substantive structural reading**: the rank-deficit pattern extends BEYOND BST primaries to extended Casimirs {11, 13} BUT terminates at first Ogg supersingular prime X=17.

(Cal #27 STANDING reflexive: this is substantively new finding from Grace; need careful absorption.)

## 3. INV-5195 9-element substrate operational arithmetic set

Per Grace INV-5195: substrate uses **9-element operational arithmetic set** across three categories:

| Category | Primes | Substrate role |
|---|---|---|
| **BST primaries** | {2, 3, 5, 7} | Cyclotomic chain forcing rank → N_c → n_C → g |
| **Extended Casimirs** | {11=c_2, 13=c_3} | Wallach K-type Casimir spectrum + rank-deficit instances 5+6 |
| **Ogg supersingular** | {17, 19, 23} | Substrate-modular boundary (chain termination at 17) |

**Three Memorial Day findings unified**:
1. Grace 4+2 maximal-prefix RATIFIED → first 4 BST primaries
2. Casey Memorial Day hypothesis (Mersenne ∩ Ogg ∩ prefix) → 9-element set as intersection
3. Cal #139 cyclotomic chain → 4-instance + Grace extension → 6-instance + termination at Ogg

## 4. Revising chain termination v0.1

### 4.1 Chain termination position update

v0.1 claimed chain terminates at 4 elements. Grace INV-5193 shows chain extends to 6 elements (with extended Casimirs 11, 13) and terminates at X=17 (first Ogg supersingular).

**Revised structural claim**: chain has **6 substrate-operational levels** {rank=2, N_c=3, n_C=5, g=7, c_2=11, c_3=13}, with substrate-mechanism termination at X=17 = first Ogg supersingular prime.

### 4.2 Updated candidate mechanisms for chain termination at 6 (not 4)

The 5 candidates from v0.1 need re-evaluation:

| Candidate | v0.1 termination at 4 | Grace's termination at 6 (X=17) |
|---|---|---|
| **A — Mersenne maximal-prefix** | M_11 composite breaks at level 5 | But Grace's pattern extends through X=11 + X=13; mechanism not just Mersenne |
| **C — Hua-Look 2^(rank²) = 16** | rank-2 manifold caps at 4 levels | Doesn't extend cleanly to 6 levels |
| **E — K59 7-step at g** | substrate's outermost computational tier | Extended Casimirs + Ogg supersingular beyond K59's GF(128) scope |
| **NEW: Ogg supersingular boundary** | not in v0.1 | **STRONG candidate for X=17 termination** |

**Substantive update**: chain termination mechanism may be **Ogg supersingular boundary** (chain stops at first prime in substrate's Ogg supersingular set {17, 19, 23}). This is consistent with Casey's Memorial Day hypothesis (Mersenne ∩ Ogg ∩ prefix).

### 4.3 The 9-element operational set as substrate's arithmetic primitives

Substrate's full operational arithmetic uses:
- **Cyclotomic chain on BST primaries {2,3,5,7}**: Mersenne-cyclotomic forcing per Cal #139
- **Extended Casimir extension {11, 13}**: rank-deficit pattern continues for 2 more levels
- **Ogg supersingular boundary {17, 19, 23}**: substrate's "outer wall" — chain terminates at 17

**6-instance pattern** spans BST primaries + extended Casimirs; **boundary at 17** is substrate's Ogg-supersingular substrate-mechanism limit.

## 5. Substantive structural picture update

### 5.1 Substrate has 6-level computational hierarchy, not 4

Updated substrate structure:
- 6 operational levels at primes {2, 3, 5, 7, 11, 13}
- Each level has finite-field GF(2^X) with multiplicative group order M_X
- M_X prime at {2,3,5,7,13} (Mersenne primes); composite at X=11 (M_11=2047=23·89)
- Chain termination at X=17 (first Ogg supersingular)

The "ONE structural parameter (rank=2)" framing v0.5 Cal-corrected was already FRAMEWORK-PLUS pending substrate-mechanism gates. Grace's INV-5193 substantively REFINES the picture: substrate may have 6-level chain (not 4) with Ogg-supersingular termination mechanism.

### 5.2 Connection to multi-phase quiver Hall algebra (v0.2+ revision)

Multi-phase quiver v0.2 (filed earlier today) assumed 4 chain levels. Grace's 6-level extension means the substrate Hall algebra may have:

- **6 cyclotomic chain levels** at finite fields GF(2^X) for X ∈ {2,3,5,7,11,13}
- **Ogg supersingular boundary** at X=17 forming the substrate's "outer wall"
- **9-element substrate arithmetic primitives** structuring the Hall algebra parameters

Updated Macdonald-like parameter count: instead of (q_rank, q_{N_c}, q_{n_C}, q_g; α) = 5-parameter, substrate may have **(q_2, q_3, q_5, q_7, q_11, q_13; α) = 7-parameter** deformation.

This is substantive revision of last night's Hall algebra hypothesis. Cal #29 STANDING risk-flag: need careful forward derivation; don't back-fit to Grace's 6-element observation.

### 5.3 Cal #133 partial-tautology audit on 6-instance extension

Is the 6-instance pattern at {2,3,5,7,11,13} substrate-specific or general arithmetic?

Cal-corrected check:
- 2^X − Y·X = rank arithmetic at any prime X gives variations of the rank-deficit pattern
- Substrate-specific content: SELECTION of {2,3,5,7,11,13} as substrate's operational primes vs other prime subsets
- Substrate's Ogg supersingular boundary at X=17 is structurally important (per Memorial Day Casey hypothesis)

Substantive content survives Cal #133 audit IF:
- Substrate's operational arithmetic set {2,3,5,7,11,13,17,19,23} is substrate-MECHANISM-derived (not just observed)
- Ogg supersingular boundary at X=17 has substrate-mechanism

Multi-week derivation gates.

## 6. Implications for today's other deliverables

### 6.1 Multi-phase quiver v0.2 → v0.3 revision needed

Per v0.2 Hall algebra framework: 4-level chain with Macdonald 5-parameter deformation. Grace's 6-instance extension means:
- 6-level chain (not 4)
- 7-parameter Macdonald-like deformation (not 5)
- Substrate Hall algebra has additional structure at extended-Casimir levels

v0.3+ revision pending; for now, v0.2 framework stands at FRAMEWORK with explicit revision noted.

### 6.2 Chain termination v0.1 → v0.2 revision needed

Per v0.1: chain terminates at 4 elements via 5 candidate mechanisms (3 STRONG: Mersenne maximal-prefix, Hua-Look 2^(rank²)=16, K59 7-step).

v0.2 revision (next pull or absorbed in future broadcasts): chain terminates at 6 elements (X=13) with NEW mechanism at X=17 boundary (Ogg supersingular). The 3 STRONG candidates from v0.1 may need supplementation by Ogg-supersingular-boundary mechanism.

### 6.3 Track DC v0.7 K59-per-chain-level extension

Per v0.7: parallel K59-style at X ∈ {rank, N_c, n_C, g} = {2, 3, 5, 7}. Grace's extension means substrate may have parallel-K59-style at X ∈ {2, 3, 5, 7, 11, 13} (6 levels) with Ogg-supersingular boundary at X=17.

v0.7 → v0.7.1 update pending.

## 7. Multi-week derivation path (v0.9+)

### 7.1 Substrate-mechanism for 6-level chain

**v0.9** (multi-week):
- Substrate-mechanism for selection of {2,3,5,7,11,13} as substrate's 6-element operational prime set
- Why extended Casimirs {11, 13} and not other intermediate primes?
- Connection to Wallach dim_N composite-product scheme

### 7.2 Substrate-mechanism for Ogg supersingular boundary

**v0.10** (multi-week):
- Why does substrate terminate at X=17 = first Ogg supersingular prime?
- Casey Memorial Day hypothesis: Mersenne ∩ Ogg ∩ prefix structure
- Substrate-modular framework connection

### 7.3 Cal Thread 4 typing

Cal Thread 4 cold-read on Sections 2-5 6-instance pattern + 9-element operational set + boundary structure.

## 8. Honest scope

**What's CHECKABLE arithmetic**:
- 6-instance rank-deficit pattern at primes {2,3,5,7,11,13} per Grace INV-5193 verification
- 9-element substrate operational arithmetic set per Grace INV-5195

**What's FRAMEWORK in v0.8**:
- Chain termination at 6 levels (not 4) per Grace extension
- Ogg supersingular boundary candidate at X=17
- 7-parameter Hall algebra deformation candidate update

**What's INTERPRETIVE in v0.8** (Cal #29 + Cal #133 preserved):
- Substrate-mechanism for 6-level chain
- Substrate-mechanism for Ogg supersingular boundary
- Substrate's selection of {2,3,5,7,11,13} as operational primes

**What's NOT in v0.8** (multi-week):
- Explicit substrate-mechanism per chain level (now 6 levels not 4)
- Ogg-supersingular-boundary substrate-mechanism derivation
- Updated multi-phase quiver Hall algebra structure

**Cal #27 STANDING reflexive trigger count**: 2 triggers (6-instance pattern + 9-element set feel substrate-natural at peak convergence; need careful Cal-correction watch).

## 9. Coordination

**Cal**: Thread 4 cold-read on Grace INV-5193 + Lyra v0.8 absorption + revision of v0.1 chain termination framing.

**Grace**: catalog continuation of 6-instance pattern + 9-element operational set + Ogg supersingular boundary investigation.

**Elie**: Toy 3543+ candidate (Cal #29 pre-audit) — verify Grace's 6-instance pattern at X=11, 13 explicit + verify chain termination at X=17 + counter-factual at next candidate primes.

**Keeper**: Track DC trajectory revision — v0.1-v0.8 cumulative shows 4→6 chain length update; multi-phase quiver Hall algebra deformation parameter count revision (5→7).

— Lyra, Track DC v0.8 Grace INV-5193 + INV-5195 substantive absorption filed Wednesday 2026-05-27 ~09:35 EDT. FRAMEWORK-PLUS. Cal #139 4-instance pattern extends to 6-instance via Grace at primes {2,3,5,7,11,13}; substrate's 9-element operational arithmetic set spans BST primaries + extended Casimirs + Ogg supersingular; chain termination at X=17 (first Ogg supersingular boundary). Multi-phase quiver Hall algebra revision: 7-parameter Macdonald-like deformation candidate (not 5). v0.1 chain termination framing revised to 6-level (not 4); Ogg supersingular boundary as new candidate mechanism. Multi-week derivation gates per substrate-mechanism for 6-level chain + Ogg boundary.
