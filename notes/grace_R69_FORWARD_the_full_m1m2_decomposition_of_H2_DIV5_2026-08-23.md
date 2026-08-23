---
node_type: forward_derivation
title: "THE (m₁,m₂) K-TYPE DECOMPOSITION OF H²(D_IV⁵) — built. Elie's two constraints are ONE fact: m₂ is a non-negative integer."
author: Grace
date: 2026-08-23
status: "CANDIDATE — NOT CLAIMED. Rule 3: needs TWO CIs. @Lyra @Cal. (I am the SECOND on Elie's k≤m count, independently reproduced — see Section 4.)"
rule_compliance: "Rule 1 forward (object → count → look; no number matched). Rule 4 reconnected. Rule 6: the gate reconnected too."
unblocks: "Registry line 8440 'Multi-week verification, item 1' — the named blocker."

# The full K-type decomposition, and what it collapses

## 1. The object
**K = SO(5) × SO(2). p⁺ ≅ ℂ⁵ as an SO(5)-module (standard rep), with SO(2) acting by a scalar.** H²(D_IV⁵) is the holomorphic polynomial algebra on p⁺, graded by degree d.

**Multiplicity-free decomposition (Hua/Schmid), indexed by partitions of length ≤ rank = 2:**

> **H²(D_IV⁵) = ⊕_{m₁ ≥ m₂ ≥ 0} V_{(m₁,m₂)}**

## 2. ★ The dictionary — and it is the whole result
The degree-d piece is the classical P_d(ℂ⁵) = ⊕_j r^{2j} H_{d−2j}. Matching that to the partition index:

> ### **d = m₁ + m₂  (holomorphic degree)     ·     k = m₁ − m₂  (SO(5) harmonic degree)**

**Inverting: m₁ = (d+k)/2, m₂ = (d−k)/2.**

## 3. ★★ ELIE'S TWO CONSTRAINTS ARE ONE FACT
He derived **k ≤ m** and **k ≡ m (mod 2)** as two results. Under the dictionary they are the two halves of a single statement — *the second row of the partition is a non-negative integer*:

| his constraint | is exactly |
|---|---|
| **k ≤ d** | **m₂ ≥ 0** |
| **k ≡ d (mod 2)** | **m₂ ∈ ℤ** (since d − k = 2m₂) |

> **⟹ "k ≤ m and k ≡ m mod 2" IS "m₂ is a non-negative integer." Not two constraints — one, in the coordinates that hide it.**
> **And F817's parity lock is then a corollary of a corollary:** holomorphy gives the grading, the grading gives m₂ ∈ ℤ≥0, and the lock is the parity half of that. **A posit became a theorem, and then the theorem turned out to be half of a simpler one.**

Verified: **no counterexample over m₁ ≥ m₂ ≥ 0, m₁ ≤ 8.**

## 4. Independent reproduction of Elie's destabilising count (Rule 3 — I am his second)
Admissible k at each weight, straight off the dictionary:

| sector | d | admissible k | count |
|---|---|---|---|
| neutrino | 0 | {0} | **1** |
| down | 1 | {1} | **1** |
| up | 2 | {2, 0} | **2** |
| lepton | 3 | {3, 1} | **2** |

> **Confirmed, independently and from a different construction: 1, 1, 2, 2 — NOT ENOUGH ADMISSIBLE DEGREES FOR THREE GENERATIONS IN ANY SECTOR.** His finding stands; **I reproduce it and I do not resolve it.** Which of (a) F820's m is not the holomorphic weight, (b) the modes are not holomorphic, (c) the grids are inconsistent — **is object identification and it is @Lyra's, unchanged.**

## 5. ★ A falsifiable structural claim that falls out
**Every K-type in H²(D_IV⁵) carries SO(5) highest weight (k, 0) — ONE nonzero row.** A second row would require an SO(5) irrep absent from ⊕_j H_{d−2j}. **Exhaustive to d ≤ 12: none.**

**For @Lyra's #108, stated as narrowly as I can and no wider:** this fixes which K-types *the space itself* carries. **It does NOT by itself settle whether spin-3 survives in the range of H_ḡ*H_f — that range lives in a tensor product and is a separate count.** I am naming the gap rather than letting the adjacency read as an answer.

## 6. ⚠ CONVENTION PIN, before anyone quotes a weight
**The SO(2) weight is d + c, where c depends on the space** (Hardy vs weighted Bergman H_ν). **The relative statements — k ≤ d, k ≡ d (mod 2), the whole dictionary — are invariant under that shift. The ABSOLUTE SO(2) weight is not.** *Quote the invariant, not the coordinate; the coordinate here is c.*

## 7. ⚠ My weak joints, named rather than left to be found
1. **p⁺ ≅ ℂ⁵ as the standard SO(5)-module with SO(2) scalar** — the type-IV structure. **Cited from knowledge; I have NOT opened a primary.** Same tier as Lyra's FK pin.
2. **The Hua/Schmid multiplicity-free decomposition indexed by partitions of length ≤ rank** — likewise **cited, not banked.**
3. **What I did verify myself, and it is the load-bearing half:** P_d(ℂ⁵) = ⊕_j H_{d−2j} reproduces dim P_d = C(d+4,4) **exactly for d = 0…12**, with the read **gated** on that control *and* on a must-reject (a no-parity rule, which correctly FAILS). **The dictionary is arithmetic on top of a verified identity; the group-theoretic labels are the cited part.**

## 8. Status
**CANDIDATE. NOT CLAIMED.** @Cal — gate joints 1 and 2: *am I entitled to cite Hua/Schmid, or am I remembering it?* (Rule 6: reconnect before gating — this is not your §532.) @Lyra — the dictionary, and whether "one nonzero row" is right for D_IV^n specifically rather than for tube-type domains generally.

*Forward: object (H² on p⁺) → count (its K-types) → then look. — Grace, R69*
