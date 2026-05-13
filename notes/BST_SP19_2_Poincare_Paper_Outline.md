# SP19-2: Poincare Paper Outline

**Working Title**: "The Wallach Bottleneck and the Poincare Conjecture: Why S^3 Is Forced"
**Lead**: Lyra + Elie
**Target**: Geometric and Functional Analysis (GAFA)
**Date**: May 13, 2026

## Scope (honest)

This paper does NOT claim an independent proof of Poincare. It claims:
1. BST provides the structural explanation for WHY Perelman's proof works
2. Every numerical quantity in the Poincare proof chain is a BST integer or ratio
3. For compact simply-connected M^3 embedded in Q^5, the BST argument is complete without Ricci flow
4. For the general case, Perelman's Ricci flow is still required, but BST explains why it converges

## Sections (10)

### 1. Introduction and Main Result
Thesis: D_IV^5 structural data explains Poincare. Wallach bottleneck forces S^3. Not alternative proof — structural explanation.
- Ref: GC-2 template mapping

### 2. The BST Integers in the Poincare Landscape
18+ appearances (conservative count):

| # | Quantity | Value | BST |
|---|----------|-------|-----|
| 1 | Manifold dimension | 3 | N_c |
| 2 | Thurston geometry count | 8 | 2^N_c |
| 3 | Excluded geometries | 7 | g |
| 4 | Exclusion conditions | 5 | n_C |
| 5 | Ambient real dimension Q^5 | 10 | 2*n_C |
| 6 | Codimension M^3 in Q^5 | 7 | g |
| 7 | Whitney embedding dim | 7 | 2*N_c+1 |
| 8 | R(S^3) | 6 | C_2 |
| 9 | Bergman spectral gap | 6 | C_2 |
| 10 | Lichnerowicz lambda_1 | 3 | N_c |
| 11 | Perelman entropy constant | 3/2 | N_c/rank |
| 12 | Ricci decay rate | 6 | C_2 |
| 13 | Wallach parameters | 6 | C_2 |
| 14 | Sym^2(T*M) dimension | 6 | C_2 |
| 15 | Total II components | 42 | C_2*g |
| 16 | Smale easy threshold | 5 | n_C |
| 17 | Freedman intermediate dim | 4 | rank^2 |
| 18 | K41 branching ratio | 5/3 | n_C/N_c |

Plus: normal bundle (2,3,2) = (n_C-N_c, N_c, n_C-N_c), sum = g. Stability eigenvalues {1, N_c, 1}.
- Toys: 2138 (16/16), 2143 (11/11), 2145 (17/17). Tier: D.

### 3. Thurston Exclusions as Wallach Kernel
8 = 2^N_c geometries. Image = 1-dim (S^3). Kernel = g = 7. Each excluded geometry fails one of n_C = 5 conditions.
- Toy 2143 (11/11), T1818. Tier: I.
- Gap: Wallach kernel identification is structural, not representation-theoretic.

### 4. The Wallach Bottleneck Theorem (T1829)
Three selection equations uniquely force n=5. At selected dimension, pi_2 organizes S^3 spectral theory.
- Toy 2151 (26/26), T1829. Tier: D.

### 5. Ricci Flow as Wallach Spectral Evolution
Cumulative identity: sum_{j=0}^m (j+1)^2 = dim H_m(R^5). K41 = n_C/N_c = 5/3. Decay rate = C_2 = 6.
- Toy 2145 (17/17), T1823. Tier: I-to-C.
- Gap: Spectral organization implies convergence (not yet proved).

### 6. The Berger-Klingenberg Route (Approach B)
Q^5 sectional curvatures in [1, rank^2] = [1, 4]. Pinching delta = 1/4 at Berger boundary. Positive II helps. C_2 parameters = C_2 constraints (square system).
- Toy 2148 (16/16). Tier: C.
- Gap: Rigorous II positivity at Wallach level.

### 7. Stability of the Totally Geodesic Embedding (FC-3a)
TG S^3 in Q^5 is strictly stable. Normal bundle = g = 7. All stability eigenvalues positive. Unique minimal M^3 at Wallach level.
- Toys 2152 (20/20), 2153 (13/13). Tier: D for Q^5 submanifolds.
- Gap: General M^3 must admit Wallach-level embedding in Q^5.

### 8. The BST-Perelman Hybrid Proof
Synthesis: Perelman provides dynamics (Ricci flow), BST provides structure (Wallach forces endpoint). Five-step argument combining both.
- All toys. Tier: C for general case, D for Q^5 case.

### 9. Over-Determination and the Confinement Parallel
5 monotonicity controls for 1 outcome = 5:1. d = N_c = 3 is both Poincare and confinement dimension. R(S^3) = C_2 is both scalar curvature and Casimir eigenvalue.
- Tier: I (parallel structural, not proved).

### 10. Honest Scope and Open Questions
- PROVED: 18+ BST integers, T1829, stability, cumulative identity
- CONDITIONAL: Berger-Klingenberg, spectral embedding, Ricci-Wallach connection
- REQUIRES PERELMAN: General case
- OPEN: Bergman flow on Q^5 -> Ricci flow? (genuinely new math)

## Toy/Theorem Map

| Section | Toys | Tests | Tier |
|---------|------|-------|------|
| 2 | 2138, 2143 | 27/27 | D/I |
| 3 | 2143 | 11/11 | I |
| 4 | 2151 | 26/26 | D |
| 5 | 2145 | 17/17 | I-C |
| 6 | 2148 | 16/16 | C |
| 7 | 2152, 2153 | 33/33 | D/C |
| Total | 7 toys | 130/130 | — |

## Gaps for New Work

1. **Gauss-Codazzi determinant** (Sections 6-7): Weyl tensor of Q^5 on 3-planes. Tractable linear algebra. Would upgrade C->D.
2. **Spectral embedding existence** (Section 7): Every simply-connected M^3 admits Wallach-level embedding in Q^5. Berard-Besson-Gallot candidate.
3. **Wallach kernel formalization** (Section 3): Representation-theoretic kernel computation. Upgrade I->C/D.
4. **Ricci-Wallach convergence** (Section 5): K-type filtration implies PDE convergence. New mathematics.
5. **Bergman flow = Ricci flow** (Section 10): Most ambitious. If proved: fully BST-native Poincare.

## Venue

**GAFA** (Geometric and Functional Analysis) — intersection of geometric analysis and representation theory. Does not claim to replace Perelman (would need Annals), but explains him structurally.
