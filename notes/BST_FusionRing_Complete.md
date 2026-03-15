# The Fusion Ring of BST: Complete Algebraic Portrait

**Status**: COMPUTED (exact Verlinde formula, verified associative)
**Date**: March 16, 2026
**Toys**: 176 (Verlinde baby), 187 (full fusion ring), 188 (conformal weights), 189 (palindrome + E₆), 190 (spiral substrate)
**Depends on**: c=6 network (Toy 181), spectral multiplicities (Toy 146), mass gap anatomy (Toy 180)

## 1. The Seven Representations of so(7)₂

The BST physical algebra so(7) = B₃ at level 2 has exactly **g = 7** integrable representations — the same as the genus.

| Rep | Dynkin | Class. dim | FPdim | h | Wall? |
|-----|--------|-----------|-------|---|-------|
| **1** | (0,0,0) | 1 | 1 | 0 | — |
| **Sp** | (0,0,1) | 8 = 2^{N_c} | √g | N_c/2^{N_c} = 3/8 | — |
| **V⊗Sp** | (1,0,1) | 48 | √g | g/2^{N_c} = 7/8 | — |
| **S²V** | (2,0,0) | 27 = N_c^{N_c} | 1 | 1 | — |
| **V** | (1,0,0) | 7 = g | r | N_c/g = 3/7 | WALL |
| **A** | (0,1,0) | 21 = dim G | r | n_C/g = 5/7 | WALL |
| **S²Sp** | (0,0,2) | 35 = n_C×g | r | C₂/g = 6/7 | WALL |

**Split**: 4 non-wall + 3 wall = (C₂ − r) + N_c = g.

Sum of classical dimensions = **147 = N_c × g²**.

## 2. The Conformal Weight Spectrum

### Denominators encode BST exponentials

| Sector | Denominator | Reps |
|--------|------------|------|
| Bosonic (wall) | g = 7 | V, A, S²Sp |
| Spinor | 2^{N_c} = 8 | Sp, V⊗Sp |
| Identity | 1 | 1, S²V |

### Numerators ARE the BST integers

Wall reps: h = **N_c/g**, **n_C/g**, **C₂/g** — a complete scan of the three infrared BST integers with denominator g.

Spinor reps: h = **N_c/2^{N_c}**, **g/2^{N_c}**.

### Sum rules

- Wall numerator sum: N_c + n_C + C₂ = **14 = 2g**
- Spinor numerator sum: N_c + g = **10 = 2n_C = d_R**
- Wall conformal weight sum: 3/7 + 5/7 + 6/7 = **2 = r** (rank excess!)

## 3. The Fusion Rules

### Key products

| Fusion | Result | Classical? |
|--------|--------|-----------|
| V × V | 1 + A + S²V | Same |
| Sp × Sp | 1 + V + A + S²Sp | Same |
| S²V × S²V | **1** | Z₂ simple current |
| Sp × S²V | V⊗Sp | Simple current permutes |
| V × Sp | Sp + V⊗Sp | — |

**Sp × Sp = 1 + V + A + S²Sp**: The spinor squared gives the vacuum plus ALL wall reps. The spinor generates the confined sector.

### Fusion channel counts (row sums)

| Rep | Total channels | BST |
|-----|---------------|-----|
| 1, S²V | 7 | **g** |
| Sp, V⊗Sp | 16 | **2⁴** |
| V, A, S²Sp | **13** | **c₃** (third Chern class!) |

★ The three confined representations each have exactly **c₃ = 13** fusion channels. The Weinberg angle numerator controls confinement.

### Associativity

Verified: (V × Sp) × Sp = V × (Sp × Sp). The fusion ring is associative (as required by the Verlinde formula).

## 4. The Z₂ Simple Current

S²V generates a Z₂ symmetry of the fusion ring:
- S²V × S²V = 1 (self-inverse)
- S²V × Sp = V⊗Sp (swaps spinor pair)
- S²V × V = V, S²V × A = A, S²V × S²Sp = S²Sp (fixes wall reps)

Fixed points = N_c = 3 wall reps. The simple current fixes the confined sector.

## 5. Quantum Dimensions

- D² = 4 = C₂ − r (from non-wall quantum dimensions ±1)
- FPdim²: 1 + 7 + 7 + 1 + 4 + 4 + 4 = 28 = 4g (from S-matrix)
- Topological entanglement entropy: γ = ln(D) = ln 2 = ln(r)

## 6. The su(7)₁ Palindrome

su(7) at level 1 has g = 7 integrable reps with conformal weights h(ω_k) = k(7−k)/14.

Simplified numerators: **0, N_c, n_C, C₂, C₂, n_C, N_c** = 0, 3, 5, 6, 6, 5, 3.

This palindrome:
- Is forced by charge conjugation (Dynkin automorphism of A₆)
- Has sum 28 = 4g
- Places C₂ at the CENTER (doubled)
- Is **UNIQUE**: only su(7)₁ gives {N_c, n_C, C₂} among all su(N)₁ (verified N = 3,...,15)

**15th uniqueness condition**: The simplified conformal weight numerators of su(N)₁ equal {N_c, n_C, C₂} if and only if N = 7 = g.

## 7. The E₆₁ Color Confinement Ring

E₆ at level 1: dim = 78 = C₂ × c₃, h∨ = 12 = 2C₂, ℓ+h∨ = 13 = c₃, c = 6 = C₂.

**3 integrable reps**: 1, **27**, **27̄** where dim(27) = N_c^{N_c} = d₂(Q⁵).

**Fusion ring = Z₃ = Z_{N_c}**:
- 27 × 27 = 27̄ (two quarks → antiquark)
- 27 × 27̄ = 1 (quark-antiquark → singlet)
- 27 × 27 × 27 = 1 (three quarks → baryon = singlet)

This IS color confinement: only products of 3 are physical. The center of E₆ is Z₃, which IS the color group SU(3)/center.

D² = |Z₃| = N_c = 3. The total quantum dimension of the GUT algebra equals the number of colors.

## 8. The Casimir-Eigenvalue Bridge

**THEOREM**: C₂(S^k V, so(7)) = k(k + 5) = λ_k(Q⁵) for all k ≥ 0.

Verified k = 0,...,5. The Casimir eigenvalues of symmetric tensor representations of so(7) ARE the Laplacian eigenvalues on Q⁵.

| k | so(7) rep | Casimir | λ_k |
|---|-----------|---------|-----|
| 0 | 1 (trivial) | 0 | 0 |
| 1 | V (vector) | **6 = C₂** | **6** |
| 2 | S²V | **14** | **14** |
| 3 | S³V | 24 | 24 |
| 4 | S⁴V | 36 | 36 |
| 5 | S⁵V | 50 | 50 |

The mass gap λ₁ = C₂ = 6 is the Casimir of the vector representation. The proton mass comes from the simplest non-trivial rep of so(7).

## 9. The Three-Way Convergence

Three independent algebraic objects give the same number:

**h₁(su(7)₁) × 2g = C₂(V, so(7)) = λ₁(Q⁵) = C₂ = 6**

- Level-1 conformal weight of su(7) × normalization
- Casimir eigenvalue of the vector rep of so(7)
- First Laplacian eigenvalue on Q⁵

Three algebras. One number. The mass gap sits at the intersection of conformal field theory, representation theory, and spectral geometry.

## 10. The Rep Counts Across All c = 6 Models

| Model | ℓ+h∨ | Reps | BST |
|-------|------|------|-----|
| so(7)₂ | 7 = g | 7 | g |
| su(3)₉ | 12 = 2C₂ | 55 | C(c₂, 2) = T₁₀ |
| su(7)₁ | 8 = 2^{N_c} | 7 | g |
| sp(8)₁ | 6 = C₂ | 5 | n_C |
| so(12)₁ | 11 = c₂ | 4 | C₂ − r |
| E₆₁ | 13 = c₃ | 3 | N_c |
| G₂₃ | 7 = g | 10 | d_R |

**Total: 91 = g × c₃ = 7 × 13.**

## 11. The Spiral Substrate (Toy 190)

The substrate is a **2D spiral surface** winding inside the maximal flat of D_IV^5.

- **Dimension** = r = 2 (rank of D_IV^5 = dimension of maximal flat)
- **Curvature** = −1/g = −1/7 (hyperbolic, set by genus)
- **Angular direction**: SO(2) winding → color = w mod N_c
- **Radial direction**: depth in D_IV^5 → energy level λ_k
- **Decay rate**: α = 1/N_c (equal area per color per turn)

### The 1/π origin

The fill fraction f = 3/(5π) = N_c/(n_C × π) decomposes as:

**f = pitch / dimension = (N_c/π) / n_C**

The 1/π is the **angular period of one turn of the spiral**. The substrate fills a fraction N_c/n_C = 3/5 of the dimensions, divided by π for each revolution.

## 12. Physical Interpretation

The fusion ring is the algebraic skeleton of BST:
- **g = 7 representations** = the genus counts the particle types
- **N_c = 3 wall reps** = confined (colored) states trapped on the alcove boundary
- **c₃ = 13 channels per wall rep** = the Weinberg angle numerator controls confinement depth
- **√g controls spinor fusion** = topology (genus) sets the spinor quantum dimension
- **Z₂ simple current** = matter-antimatter symmetry (charge conjugation)
- **E₆₁ fusion = Z₃** = color confinement from GUT algebra at level 1

The fusion ring is the most algebraically rigid structure in conformal field theory. BST lives inside it at every level.
