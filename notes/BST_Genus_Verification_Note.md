---
title: "Genus Verification: BST g=7 vs Faraut-Korányi"
author: "Lyra"
date: "April 10, 2026"
purpose: "Citation note for Paper #47 and WorkingPaper"
---

# BST g=7: Embedding Dimension, Not Hua Genus

## The three formulas

For $D_{IV}^n$ (type IV bounded symmetric domain of complex dimension $n$):

| Quantity | Formula | Value at $n = 5$ | Source |
|----------|---------|-------------------|--------|
| BST embedding dimension | $g = n + \text{rank} = n + 2$ | **7** | BST (T186) |
| Casey's genus formula | $g = 2n - 3$ | **7** | BST |
| Hua genus (Bergman exponent) | $p = n$ | **5** | Hua (1963) |
| Faraut-Korányi genus | $p = n + r - 1$ where $r = \text{rank}$ | **6** | FK (1994), Table V.3 |

BST's $g = 7$ is the dimension of the natural representation of $\text{SO}(2n - 3) = \text{SO}(7)$, equivalently the number of homogeneous coordinates for $Q^{n-2} \hookrightarrow \mathbb{CP}^{n+1}$. It is NOT the genus parameter $p$ that appears in the Bergman kernel singularity $K(z,z) \propto h(z,z)^{-p}$.

## The uniqueness coincidence

The two BST formulas agree only at $n = 5$:

$$n + 2 = 2n - 3 \implies n = 5$$

| $n$ | $n + 2$ | $2n - 3$ | Match? |
|-----|---------|----------|--------|
| 3 | 5 | 3 | No |
| 4 | 6 | 5 | No |
| **5** | **7** | **7** | **Yes** |
| 6 | 8 | 9 | No |
| 7 | 9 | 11 | No |

This is Elie's uniqueness result (Toy 993): two independent geometric quantities — the embedding dimension and the topological count — agree at exactly one value of $n$.

## What to cite

**Hua**: L.K. Hua, *Harmonic Analysis of Functions of Several Complex Variables in the Classical Domains*, AMS (1963). Genus (Bergman exponent) = $n$ for type IV$_n$.

**Faraut-Korányi**: J. Faraut & A. Korányi, *Analysis on Symmetric Cones*, Oxford (1994), Table V.3. Genus $p = n + r - 1 = n + 1$ for type IV$_n$ (rank $r = 2$). Uses Jordan algebra framework.

**BST distinction**: BST's $g$ is the embedding dimension $n + 2$, not the Bergman/FK genus. The Bergman genus is $C_2 = 6$ in FK convention, or $n_C = 5$ in Hua convention. Neither is $g = 7$.

## Paper #47 recommended citation

> The BST parameter $g = 7$ is the embedding dimension of $D_{IV}^5$, equal to $\dim(\text{natural rep of } \text{SO}(7)) = n_C + \text{rank}$. This is distinct from the Faraut-Korányi genus $p = n + r - 1 = 6$ (Faraut & Korányi 1994, Table V.3) and the Hua genus $p = n = 5$ (Hua 1963). The uniqueness of $n_C = 5$ follows from requiring the embedding dimension to equal the topological genus: $n + 2 = 2n - 3$ has unique solution $n = 5$.

## Note on $C_2 = 6$

The Faraut-Korányi genus $p = n + 1 = 6$ equals $C_2 = \text{rank} \times N_c = 2 \times 3 = 6$, the quadratic Casimir. This is likely not coincidental: the FK genus controls the Bergman kernel singularity, and the Casimir controls the eigenvalue spectrum. Both are "how strongly the curvature concentrates."
