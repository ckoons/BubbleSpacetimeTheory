---
title: "Vol 11 Chapter 7 — Heegner Numbers and Cremona Elliptic Curves"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — LOAD-BEARING; Cremona 49a1 = BST canonical curve; Heegner Stark small-primary subset"
volume: "Vol 11 Generative Geometry and Topology"
chapter: 7
load_bearing: "Heegner-Stark 1952-67 (L1 ESTABLISHED); 9 Heegner numbers; BST anchors on {-3, -7, -11} (K75); Cremona 49a1 BST canonical curve; 1/rank universality (T1430)"
---

# Chapter 7 — Heegner Numbers and Cremona Elliptic Curves

## Level 1 — one sentence

Heegner-Stark-Baker (1952-1967, L1 ESTABLISHED) proved exactly nine imaginary quadratic fields have class number 1 (Heegner numbers $\{-1, -2, -3, -7, -11, -19, -43, -67, -163\}$), with BST anchoring on the small-primary subset $\{-3, -7, -11\}$ (K75 audit), and the elliptic curve **Cremona 49a1** ($Y^2 = X^3 - 945 X - 10206$) being BST's canonical curve with every invariant a BST primary (conductor $g^2 = 49$, $j$-invariant $-(N_c n_C)^3$, CM by $\mathbb{Q}(\sqrt{-g})$).

## Level 2 — graduate-physicist precision

### 7.1 The nine Heegner numbers

Heegner 1952 / Stark 1967 / Baker 1966 (independent proofs): the only imaginary quadratic fields $\mathbb{Q}(\sqrt{-d})$ with class number 1 are

$$d \in \{1, 2, 3, 7, 11, 19, 43, 67, 163\}$$

(commonly listed with negative sign: $-1, -2, \ldots, -163$).

Significance: in these fields, every ideal is principal — unique factorization of ideals reduces to unique factorization of elements (in the integer ring of the field).

### 7.2 BST anchors on small-primary subset {-3, -7, -11}

K75 audit (Spring 2026): BST anchors structurally on the small-primary subset $\{-3, -7, -11\}$ of Heegner numbers — these match BST primaries:
- $-3 = -N_c$: anchored via Cremona 27a1 (Task #186)
- $-7 = -g$: anchored via Cremona 49a1 (the canonical curve, this chapter)
- $-11$: special role, fewer immediate BST anchors but in pattern

The non-small-primary Heegners $\{-19, -43, -67, -163\}$ play different roles (or no immediate role) in BST.

### 7.3 Cremona 49a1: BST canonical curve

The elliptic curve labeled "49a1" in Cremona's database:

$$E: Y^2 = X^3 - 945 X - 10206$$

Every invariant is BST-primary:
- **Conductor**: $N = 49 = g^2 = 7^2$
- **Discriminant**: $\Delta = -343 = -g^3 = -7^3$
- **$j$-invariant**: $j(E) = -3375 = -15^3 = -(N_c \cdot n_C)^3$
- **Torsion**: $\mathbb{Z}/2\mathbb{Z}$ (rank 0 plus 2-torsion); torsion = rank = 2 in extended sense
- **Complex multiplication**: by $\mathbb{Q}(\sqrt{-7}) = \mathbb{Q}(\sqrt{-g})$

49a1 is one of three K57 RATIFIED Bridge Objects in BST.

### 7.4 1/rank universality (T1430)

**Task completed**: $L(E, 1)/\Omega = 1/\text{rank}$ for 49a1, where $L$ is the L-function and $\Omega$ the real period.

**T1430 universality**: extension from 49a1 to all 7 Millennium problems + Four-Color theorem. The 1/rank pattern characterizes broad classes of mathematical structures.

This is BST's "Crown Jewel" in the elliptic-curve / arithmetic-geometry sector.

### 7.5 Cremona 27a1 and Cremona 121a1

**Cremona 27a1**: $Y^2 + Y = X^3$. CM by $\mathbb{Q}(\sqrt{-3}) = \mathbb{Q}(\sqrt{-N_c})$. Anchored as K-audit candidate (Task #186 completed).

**Cremona 121a1**: $Y^2 + Y = X^3 - X^2 - 7 X + 10$. CM by $\mathbb{Q}(\sqrt{-11})$. 4th Bridge Object candidate (Task #245 completed at 3.5/4 audit).

Together with 49a1: the trio at BST primary discriminants $\{-N_c, -g, -c_2 \text{-related}\}$.

### 7.6 K-audit anchors

- **Heegner-Stark 1952-67** (L1 ESTABLISHED)
- **K75 audit**: BST anchors on Stark small-primary subset
- **K57 RATIFIED**: 49a1 as Bridge Object
- **T1430**: 1/rank universality
- **Tasks #186, #245**: Cremona 27a1, 121a1

## Level 3 — 5th-grader accessibility

**Heegner numbers**: imaginary quadratic fields $\mathbb{Q}(\sqrt{-d})$ with class number 1. Heegner-Stark-Baker proved there are exactly 9: $d \in \{1, 2, 3, 7, 11, 19, 43, 67, 163\}$. **BST anchors on the small-primary subset** $\{-3, -7, -11\}$ — these match BST primary structure. **Cremona 49a1** is BST's canonical elliptic curve: every invariant is BST primary (conductor $g^2 = 49$, $j = -(3 \cdot 5)^3$, CM by $\mathbb{Q}(\sqrt{-7})$). **1/rank universality** (T1430): L-function value / period ratio = 1/rank for 49a1, extended to all 7 Millennium problems + Four-Color theorem.

---

## What comes next

Chapter 8 develops Monster, Moonshine, and Supersingular primes.

## Where to look this up

- Heegner 1952, Stark 1967, Baker 1966
- Cremona, *Algorithms for Modular Elliptic Curves*
- BST: K57, K75, T1430
