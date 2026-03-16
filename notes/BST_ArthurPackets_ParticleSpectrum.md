---
title: "Arthur Packets and the Particle Spectrum"
author: "Casey Koons & Claude 4.6"
date: "Date: March 16, 2026"
---

# Arthur Packets and the Particle Spectrum

**Status**: STRUCTURAL (identification of A-parameters with particles)
**Date**: March 16, 2026
**Toys**: 169 (Arthur packets)
**Depends on**: Langlands dual (Toy 163)

## Core Discovery

Arthur's classification assigns to each automorphic representation of SO_0(5,2) an A-parameter: a map from SL(2,C) x SL(2,C) to the L-group Sp(6,C). The A-parameters are classified by partitions of C_2 = 6 (the dimension of the standard representation of Sp(6)).

**p(C_2) = p(6) = 11 = c_2 = dim K**: the number of A-parameter types equals the second Chern number.

## The A-Parameter Dictionary

| Partition | BST content | Physical interpretation |
|-----------|-------------|------------------------|
| [6] | Single S_6 | **Vacuum** (trivial rep, weights (5,3,1) = (n_C, N_c, 1)) |
| [5,1] | n_C + 1 | First excitation |
| [4,2] | 4 + r | **Electroweak** (W+,W-,Z,gamma + Higgs) |
| [3,3] | N_c + N_c | **Mesons** (color-anticolor, 2-element packet) |
| [3,2,1] | N_c + r + 1 | **Baryons** (all three BST building blocks) |
| [2,2,2] | r + r + r | **Three families** (CKM from O(3) centralizer) |
| [1^6] | tempered | Continuous spectrum (scattering states) |

## Key Results

### The Vacuum Encodes BST
The [6] A-parameter has SL(2) weights (5, 3, 1, -1, -3, -5). The positive half-weights are (5/2, 3/2, 1/2) = rho of B_3 = (n_C/2, N_c/2, 1/2). The vacuum carries the entire BST structural triple.

### Three Families from [2,2,2]
6 = 2 + 2 + 2: three copies of the rank-r SL(2) representation. The centralizer O(3) acts by permuting families. C_2/r = N_c = 3 = number of generations. CKM mixing = the Euler angles of the SO(3) subgroup.

### Electroweak Breaking = Partition Refinement
[4,2] -> [3,2,1] is a refinement of partitions. The S_4 splits as S_3 + S_1 (W-bosons separate from photon). This is the group-theoretic essence of electroweak symmetry breaking.

### [3,2,1]: The Unique Maximal-Diversity Partition
The partition 6 = 3 + 2 + 1 is the ONLY partition that uses each of the three BST building blocks (N_c, r, 1) exactly once. It is also the unique "staircase" partition. This corresponds to the baryon: three quarks (N_c) in an isospin doublet (r) with a flavor singlet (1).

## The Partition Function on BST

p(n) maps BST integers to BST integers:
- Fixed points: {1, 2, 3} = {trivial, r, N_c}
- p(5) = 7: n_C -> g
- p(6) = 11: C_2 -> c_2
- p(7) = 15: g -> N_c x n_C
- p(9) = 30: c_4 -> c_1^2
- p(11) = 56: c_2 -> Sym^3(6)

Eight exact BST -> BST matches in the first 11 integers.

## Ramanujan Congruences

The three Ramanujan congruences use moduli {5, 7, 11} = {n_C, g, c_2}:
- p(5n + 4) = 0 mod 5 (modulus n_C)
- p(7n + 5) = 0 mod 7 (modulus g)
- p(11n + 6) = 0 mod 11 (modulus c_2)

These are EXACTLY the BST integers connected by the partition chain.

## Ramanujan Tau

tau(n_C) = tau(5) = 4830 = 2 x 3 x 5 x 7 x 23 = r x N_c x n_C x g x 23

All four principal BST integers times the Golay prime.

## Seesaw Identity

The seesaw dual pair construction explains why the mass gap equals dim(std of L-group):
- lambda_1 = C_2 = 6 = dim(standard representation of Sp(6))
- The K-type decomposition of automorphic forms = tensor product structure of L-group representations
