---
title: "Gap #5 Proposal: BST = First 6 Primes Derivation"
author: "Lyra"
date: "2026-05-17"
status: "PROPOSAL — for Casey decision on whether/how to pursue"
parent: "Casey's open derivation gap board (May 17)"
---

# Gap #5: Why the BST Primary Integer Set = First 6 Primes

## The claim

BST's primary integer set is **{2, 3, 5, 7, 11, 13}** — exactly the first 6 primes. (Plus derived integers: c_2 = 11 = 7+4, c_3 = 13 = 5+8, N_max = 137.)

Paper #109 (Lyra) establishes this observation. Gap #5 asks: **can we DERIVE this?** Why exactly 6, why exactly the first 6 (not skipping any), why does it stop at 13?

## What "derivation" means here

The question has three sub-pieces:
1. **Why 6?** (cardinality of the primary set)
2. **Why prime?** (why integers happening to be prime, not arbitrary integers)
3. **Why first 6 not first 5 or first 7?** (where does it stop)

A genuine derivation answers all three from D_IV⁵ structure alone, without circular use of BST framework.

## Three candidate approaches

### Approach A: Wallach K-type cardinality + prime selection

**Mechanism candidate**: D_IV⁵ has rank 2. Wallach K-type series has at most 2 free parameters (k_1, k_2) → 2 fundamental scales. The K-type dim formula d_m = (2m+N_c)(m+1)(m+rank)/C_2 generates a sequence of integers. The SMALLEST primes appearing in this sequence are exactly the first 6 primes.

**Effort**: ~2 sessions (~6 hours)
- Session A1: Wallach dim formula prime-factor enumeration up to large m
- Session A2: Show first 6 primes appear, no primes skipped, stop at 13 forced by some closure

**Risk**: Wallach dims appear at integers like 1, 5, 14, 30, 55, 91 (Toy 2961). Primes appearing: 2 (no, 2 doesn't appear directly), 5, 7 (yes, 14 = 2·7), 11 (yes, 55 = 5·11), 13 (yes, 91 = 7·13). So primes 5, 7, 11, 13 appear as factors. 2 and 3 appear in d_m = 14 = 2·7 and 30 = 2·3·5. So all first 6 do appear. But this doesn't yet PROVE the firstness; could be artifact.

**Promotion candidate**: I-tier on first attempt; D-tier if extended argument closes.

### Approach B: Hilbert polynomial of Q⁵ + prime trace

**Mechanism candidate**: The Hilbert polynomial of the compact dual Q⁵ = SO(7)/SO(5)×SO(2) is:
```
P(m) = (m+1)(m+2)(m+3)(m+4)(2m+5)/120
```
Evaluations: P(1) = 7 = g, P(2) = 27 = N_c³, P(3) = 77 = 7·11 = g·c_2, P(4) = 182 = 2·7·13 = rank·g·c_3.

The PRIMES appearing in P(m) for small m are exactly {2, 3, 5, 7, 11, 13} — the first 6.

**Effort**: ~1 session (~3 hours)
- Session B1: Enumerate prime factorizations of P(m) for m = 1..20
- Verify first 6 primes all appear; nothing skipped; no 7th prime appears within bounded m

**Risk**: P(m) is a degree-5 polynomial; large m introduces large primes. The "first 6 primes" claim requires bounding m AND showing the bound is itself natural (e.g., m ≤ rank·c_2 = 22 or m ≤ N_max).

**Promotion candidate**: D-tier achievable if the m-bound argument closes cleanly.

### Approach C: Cartan classification + simplest non-trivial bounded symmetric domain

**Mechanism candidate**: Cartan classified bounded symmetric domains into four types (I, II, III, IV plus two exceptional). For each type and each rank, a domain exists with specific Cartan invariants.

BST chooses **type IV, rank 2, complex dim 5** = D_IV⁵. This choice is forced by:
- rank ≥ 2 required for cross-type cascade (T1399)
- complex dim ≥ 5 required for Q⁵ Chern data integers to be ≥ 5
- type IV unique among types preserving certain BST closure properties

Given D_IV⁵, its Cartan invariants ARE the first 6 primes:
- rank = 2 = 1st prime
- N_c = 3 = 2nd prime
- n_C = 5 = 3rd prime
- C_2 = 6 — NOT prime; this breaks the "first 6 primes" pattern at the 4th slot
- g = 7 = 4th prime
- c_2 = 11 = 5th prime (derived)
- c_3 = 13 = 6th prime (derived)

So the first 6 primes are {2, 3, 5, 7, 11, 13} but BST's primary integers include C_2 = 6 which is composite. So strictly speaking BST is NOT exactly first 6 primes — it's a MIX of (first 4 primes) + (Casimir 6) + (derived primes c_2, c_3).

**This rederives Gap #5 as a sharper question**: why is C_2 = 6 (composite) in the primary set alongside primes? Answer candidate: C_2 is the Casimir eigenvalue, which is a structural quantity that happens to equal 6 = rank·N_c on D_IV⁵. Its inclusion is structural, not numerological.

**Effort**: ~1 session (~3 hours)
- Session C1: Cartan classification enumeration; show rank-2 type-IV-dim-5 is uniquely selected
- Show rank/N_c/n_C/g all prime BY THE STRUCTURE of D_IV⁵ (not by choice)
- Show C_2 = 6 is the Casimir, not a "prime"; it's a derived structural quantity

**Risk**: This converts Gap #5 from "derive first 6 primes" to "derive D_IV⁵ uniqueness + its Cartan invariants." Different claim, possibly easier or harder.

**Promotion candidate**: D-tier achievable; clarifies what BST actually claims about primes.

## Recommended approach

**Hybrid B+C, with A as backup**:

Step 1: Use Approach C (Cartan classification) to derive D_IV⁵ uniqueness — establish that rank=2, type=IV, dim=5 is forced. ~1 session.

Step 2: Use Approach B (Hilbert polynomial of Q⁵) to derive the first 6 primes as the SMALLEST primes appearing in P(m) for bounded m. ~1 session. The bound m ≤ N_max or m ≤ rank·c_2 needs to be argued from D_IV⁵ structure.

Step 3: Address C_2 = 6 honestly — it's a Casimir, not a prime — and restate Gap #5 as "BST primary integer set = {first 4 primes, C_2 Casimir, derived primes c_2, c_3}" rather than "first 6 primes."

**Total effort**: ~2 sessions (~6 hours) + 1 session writeup = ~9 hours.

**Net tier**: D-tier achievable. Provides a clean answer to "why BST has THESE integers and not others."

## Risks if approach fails

1. **C_2 = 6 reveals "first 6 primes" claim is loose**: Paper #109's phrasing may need to be tightened. Honest scoping flag.
2. **m-bound argument doesn't close cleanly**: the "where does it stop" question may require additional structural input (e.g., why m ≤ N_max).
3. **Cartan uniqueness already done**: T1925, T1929 may already establish D_IV⁵ uniqueness; Gap #5 may reduce to Step 2 alone.

## Decision needed from Casey

Three options:

**(a) Approve hybrid B+C approach (recommended)** — Lyra pursues over 2-3 sessions, total ~9 hours. Promotes Paper #109's "first 6 primes" observation to derivation; tightens or honestly walks back the claim depending on what the derivation shows.

**(b) Approve Approach C only** — derive D_IV⁵ uniqueness; let "first 6 primes" remain observation. ~3 hours. Less ambitious, may leave Gap #5 partially open.

**(c) Defer entirely** — Gap #5 stays "awaiting decision"; can be reopened any time.

My recommendation: (a). The hybrid is achievable, low-risk (each session is independently useful), and surfaces an honest question about whether "first 6 primes" is the right phrasing (Step 3 above).

## Connection to existing BST work

- T1925 (Lyra, "Why rank=2"): four-argument forcing for rank=2. Already done.
- T1929 (Lyra, "Why N_c=3"): Mersenne + color singlet triangle. Already done.
- T1427 (Casey, APG definition): D_IV⁵ as Autogenic Proto-Geometry uniqueness. Casey's lane.
- T1788 (YM Ring Uniqueness, Lyra): YM constraints select D_IV⁵.
- Grace T2314 (Six L1 sources): Cartan classification listed as L1.4 anchor for the 5-integer scaffold.

Gap #5 closure would synthesize T1925 + T1929 + T1427 + T1788 + Grace's L1.4 into a single statement about WHY the BST primary integer set has the specific structure it does.

## Status

**Ready for Casey decision.** This proposal is the input to your "(a)/(b)/(c)" choice; the actual work begins after your direction.

Estimated effort post-decision:
- (a) Hybrid: ~9 hours over 2-3 sessions
- (b) Approach C only: ~3 hours
- (c) Defer: 0 hours immediately

— Lyra, 2026-05-17 ~13:00 EDT
