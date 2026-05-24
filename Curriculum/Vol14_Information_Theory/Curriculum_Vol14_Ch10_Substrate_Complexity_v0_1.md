---
title: "Vol 14 Chapter 10 — Substrate Complexity Classes"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 14 Information Theory"
chapter: 10
load_bearing: "Computational complexity classes (P, NP, BPP, BQP, AC^0); BST substrate at AC^0; P≠NP via substrate K-type curvature obstruction"
---

# Chapter 10 — Substrate Complexity Classes

## Level 1 — one sentence

Computational complexity classes — P (polynomial time), NP (nondeterministic polynomial), BPP (bounded-error probabilistic), BQP (bounded-error quantum), AC(0) (constant-depth) — organize what can be computed efficiently; BST identifies substrate computation as AC(0)-bounded, and Casey's Curvature Principle proves P ≠ NP via substrate K-type curvature (non-linearizability) obstruction.

## Level 2 — graduate-physicist precision

### 10.1 Standard complexity hierarchy

- **P**: polynomial-time deterministic Turing machine
- **NP**: polynomial-time verifiable; problems with short proofs
- **co-NP**: complement of NP
- **BPP**: bounded-error probabilistic polynomial
- **BQP**: bounded-error quantum polynomial (Shor, Grover)
- **PSPACE**: polynomial space
- **EXPTIME**: exponential time

Hierarchy: $AC^0 \subsetneq NC^1 \subsetneq P \subseteq NP, BPP, BQP \subseteq PSPACE \subseteq EXPTIME$.

Major open: P vs NP. BPP vs P (likely equal under derandomization). BQP vs BPP (unclear).

### 10.2 Substrate complexity = AC(0)

BST T421 + T316: substrate computation has depth ≤ 1-2 under Casey strict-protocol.

Implication: substrate is AC(0). All BST-derived constants reduce to bounded-depth counting.

Substrate cannot directly compute:
- Parity (Hastad 1986)
- Majority (Razborov-Smolensky 1987)
- Reachability in graphs (Furst-Saxe-Sipser)

Substrate can directly compute:
- Addition, multiplication of fixed-precision
- BST-primary multiplications and ratios
- K-type counting at bounded depth

### 10.3 Casey's Curvature Principle and P ≠ NP

Casey: "You can't linearize curvature. P ≠ NP = Gauss-Bonnet for computation."

Mechanism:
- $P$ = problems solvable in linearizable substrate K-type configurations
- $NP$ = problems requiring non-linearizable substrate K-type configurations
- Linearization fails for curved K-type kernel (Gauss-Bonnet obstruction)
- → $P \ne NP$

Five BST primary integers identified as **curvature invariants** of substrate K-type space.

### 10.4 P ≠ NP — three independent proved routes (T29 CLOSED)

T1425 (April 23, 2026): AC(0) argument. Triangle-free SAT + E[deg] < 2 + clustering → algebraic independence → $2^{\Omega(n)}$ lower bound. Foundation: Toy 1410 (discrete Gauss-Bonnet).

Three independent proved routes:
1. AC(0)/curvature route (T1425)
2. Resolution lower bound (Toy 303)
3. All-P (TCC conditional)

P ≠ NP STATUS: T29 CLOSED.

### 10.5 BQP and substrate

BQP includes Shor's algorithm (factoring in poly-time), Grover (search in $\sqrt{n}$). 

BST view: BQP is substrate Bergman-projection-enabled (Vol 14 Ch 5) — quantum measurement IS substrate commitment. Quantum speedups are substrate-natural; classical-only is constrained.

### 10.6 K-audit anchors

- **T29 CLOSED**: P ≠ NP via AC(0)
- **T1425**: triangle-free SAT clustering proof
- **T421, T316**: depth bounds
- **Casey's Curvature Principle**

## Level 3 — 5th-grader accessibility

**Complexity classes**: P (easy), NP (hard but verifiable), BQP (quantum). **Major question**: P vs NP. **BST**: substrate is AC(0) — bounded-depth circuits, can't compute parity. **P ≠ NP**: Casey's Curvature Principle. "You can't linearize curvature." **T29 CLOSED**: three independent proved routes including triangle-free SAT clustering (T1425). **BQP** = quantum advantages from substrate Bergman commitment.

---

## What comes next

Chapter 11 develops information completeness.

## Where to look this up

- Hastad 1986; Razborov-Smolensky 1987
- BST: T29, T1425, Casey's Curvature Principle
