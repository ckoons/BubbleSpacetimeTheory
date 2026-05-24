---
title: "Vol 14 Chapter 8 — BST Coding Optimal"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 14 Information Theory"
chapter: 8
load_bearing: "BST coding is substrate-optimal: GF(128) alphabet (g=7) + RS-MDS structure + Bergman commitment + Koons-tick clock; minimum free parameters"
---

# Chapter 8 — BST Coding Optimal

## Level 1 — one sentence

BST's substrate coding — Reed-Solomon on GF(2^g) = GF(128), Bergman-kernel commitment, Koons-tick clock — is **substrate-optimal**: under the constraints of (i) finite alphabet, (ii) bounded operational power per cycle, (iii) MDS error correction, the BST primaries $(rank, N_c, n_C, C_2, g)$ are the unique choice minimizing free parameters while achieving the observed physical structure.

## Level 2 — graduate-physicist precision

### 8.1 Optimality criteria

A "substrate-optimal" coding scheme must satisfy:

1. **Finite alphabet**: substrate has bounded internal state at each spatial position
2. **Bounded operational power per cycle**: per Casey's SCMP (Vol 5 Ch 8) and Koons-tick discrete time
3. **MDS error correction**: substrate must correct against finite noise rate
4. **Holomorphic commitment**: substrate commits to single output (Born = Bergman, Ch 5)
5. **Minimum free parameters**: parsimony — substrate cannot tune

### 8.2 BST primary forcing

D_IV⁵ Rigidity Theorem (T2467 + T2468, Casey-named #7) shows: the BST primaries $(2, 3, 5, 6, 7)$ are uniquely forced under D_IV⁵-type structure.

g = 7 → GF(128) alphabet
C_2 = 6 → $\alpha^{36}$ Koons-tick exponent
n_C = 5 → 5 Wallach layers
N_c = 3 → 3 commitments per outcome
rank = 2 → 2-dimensional substrate degrees-of-freedom

### 8.3 Strong-Uniqueness Theorem v0.10.5

BST framework documented: **11 RIGOROUSLY CLOSED + 7 candidates** distinct uniqueness criteria for D_IV⁵.

Combined null-model $(1/3)^{11} \approx 5.6 \cdot 10^{-6}$, conservatively (pending C12-C18 ratifications could reach $(1/3)^{18} \approx 2.6 \cdot 10^{-9}$). [Values corrected per Cal #119 v0.4 absorption 2026-05-24; exponents 11+7=18 verified against current Cal #19 enumeration.]

D_IV⁵ is the unique substrate satisfying BST's optimality criteria.

### 8.4 Alternative codings

Why not GF(256) (g=8)? Failing T2467/T2468 uniqueness — g=7 is BST-primary, g=8 is not.

Why not Plank time as tick (no $\alpha^{36}$)? Failing observed $10^{-120}$ s natural cosmological cycle inference.

Why not infinite-precision continuous-time? Tsirelson saturation contradicts BST sub-Tsirelson prediction at 1/8 = $1/2^{N_c}$ deviation.

### 8.5 Substrate Information Completeness

Casey-named candidate principle: substrate provides the COMPLETE information channel for observable physics — no hidden variables, no super-substrate.

Falsifier: find an observable BST cannot derive from $\{rank, N_c, n_C, C_2, g\}$ + D_IV⁵ structure.

Current status: 600+ predictions verified within precision; no clean falsifier yet.

### 8.6 K-audit anchors

- **T2467 + T2468**: D_IV⁵ Rigidity (Casey-named #7)
- **Strong-Uniqueness Theorem v0.10.5**
- **Paper #122**: Information Substrate

## Level 3 — 5th-grader accessibility

**BST coding is substrate-optimal**: GF(128) alphabet (= $2^g$), Reed-Solomon error-correction, Bergman commitment, Koons-tick clock — all forced by BST primaries. **D_IV⁵ Rigidity (Casey-named #7)** says the choices $(2, 3, 5, 6, 7)$ are uniquely forced. **Strong-Uniqueness Theorem**: 11 closed + 7 candidate criteria distinguish D_IV⁵ from alternatives. **Information completeness**: substrate is the complete channel for observable physics.

---

## What comes next

Chapter 9 develops Kolmogorov complexity + AC(0).

## Where to look this up

- BST: T2467, T2468 (D_IV⁵ Rigidity)
- Strong-Uniqueness Theorem
- Paper #122
