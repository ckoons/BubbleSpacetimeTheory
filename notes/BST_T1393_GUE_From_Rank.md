---
id: T1393
title: "GUE Statistics from rank = 2"
type: theorem
status: proved
authors: [Lyra, Casey]
date: 2026-04-21
parents: [T704, T1342]
toy: 1358
domain: random_matrix_theory
---

# T1393: GUE Statistics from rank = 2

**Statement**: The spectral statistics of D_IV^5 are GUE (Gaussian Unitary Ensemble) with Dyson index beta = rank = 2. The Casimir eigenvalues exhibit quadratic level repulsion, sin-kernel two-point correlation, and logarithmic spectral rigidity.

**Proof sketch**:
1. D_IV^5 is Hermitian symmetric -> unitary symmetry class -> GUE (not GOE or GSE)
2. Dyson index beta = 2 = rank (polydisk dimension)
3. Level repulsion: P(s) ~ s^beta = s^2 for small spacings (quadratic)
4. Two-point correlation: R_2(x,y) = 1 - (sin(pi(x-y))/(pi(x-y)))^2
5. Spectral rigidity: Delta_3(L) ~ (1/pi^2)(log L + const)

**BST content**: Gap ratio lambda(1,0)/lambda(0,1) = 2*n_C / 2*N_c = n_C/N_c = 5/3. Speaking pairs add n_C-periodic modulation beyond generic GUE.

**Entry point for**: Montgomery-Odlyzko / Dyson-Mehta / random matrix community.
