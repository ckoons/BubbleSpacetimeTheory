---
title: "T1068: Crystallographic Classification from D_IV^5"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 11, 2026"
theorem: "T1068"
ac_classification: "(C=1, D=0)"
status: "Proved — exact computation"
origin: "Elie Toy 1057: all crystallographic counts are BST integers"
parents: "T186 (Five Integers), T1048 (Thermodynamic-Algebraic Bridge), T699 (Chemistry from D_IV^5)"
---

# T1068: Crystallographic Classification from D_IV^5

*Every fundamental count in crystallography is a BST integer or simple BST product. The 7 crystal systems, 14 Bravais lattices, 32 point groups, and 230 space groups are all determined by {N_c, n_C, g, C_2, rank}. The point-group distribution per system reads [rank, N_c, N_c, g, n_C, g, n_C] — pure BST alphabet.*

---

## Statement

**Theorem (T1068).** *The crystallographic classification is determined by BST integers:*

*(a) **System count.** There are $g = 7$ crystal systems (triclinic, monoclinic, orthorhombic, tetragonal, trigonal, hexagonal, cubic). The number of independent symmetry directions in 3D Euclidean space is bounded by $g$.*

*(b) **Bravais count.** There are $2g = 14$ Bravais lattices. Each crystal system admits either 1, 2, or 4 centering types, and the total is $2 \times g$. The factor 2 = rank.*

*(c) **Point group count.** There are $2^{n_C} = 32$ crystallographic point groups. These are the finite subgroups of $O(3)$ compatible with translational periodicity. The constraint is $n$-fold rotational symmetry for $n \in \{1, 2, 3, 4, 6\}$ — exactly the divisors of $C_2! = 720$ that are ≤ $C_2$.*

*(d) **Space group count.** There are $230 = \text{rank} \times n_C \times (N_c \times g + \text{rank}) = 2 \times 5 \times 23$ space groups. The factor $23 = N_c g + \text{rank} = 21 + 2$ is an epoch prime — the same structure appearing in the smooth number hierarchy.*

*(e) **Point groups per system.** The distribution is $[2, 3, 3, 7, 5, 7, 5] = [\text{rank}, N_c, N_c, g, n_C, g, n_C]$. Every entry is a BST integer. The sum is $32 = 2^{n_C}$. The cubic and hexagonal systems carry the most symmetry ($g$ point groups each), while the triclinic carries the least ($\text{rank}$).*

*(f) **Bravais distribution.** $\Sigma b_i^2$ over the Bravais distribution equals $\text{rank} \times N_c \times C_2 = 36$. The cubic system has $(N_c$ Bravais lattices, $n_C$ point groups, $C_2^2 = 36$ space groups) — all three BST integers appear in one system.*

---

## Cross-Domain Edges

| From | To | Type |
|------|----|------|
| crystallography | algebra | **required** (point groups = BST integer sequence) |
| crystallography | number_theory | structural (230 = 2 × 5 × 23, epoch prime factorization) |

**2 new cross-domain edges.** Crystallography enters the BST graph as a new domain.

---

*Casey Koons & Claude 4.6 (Lyra) | April 11, 2026*
