# The Fusion Ring of so(7) at Level 2

**Status**: COMPUTED (exact Verlinde formula, verified associative)
**Date**: March 16, 2026
**Toys**: 176 (Verlinde baby case), 187 (full fusion ring)
**Depends on**: c=6 network (Toy 181), spectral multiplicities (Toy 146)

## The Seven Representations

so(7) at level 2 has exactly **g = 7** integrable representations:

| Rep | Dynkin | Classical dim | FPdim | h (conformal) | Type |
|-----|--------|--------------|-------|---------------|------|
| 1 | (0,0,0) | 1 | 1 | 0 | identity |
| Sp | (0,0,1) | 8 = 2^{N_c} | √g | 3/8 = N_c/2^{N_c} | spinor |
| S²V | (2,0,0) | 27 = N_c^{N_c} | 1 | 1 | simple current |
| S²Sp | (0,0,2) | 35 = n_C×g | r | 6/7 = C₂/g | wall |
| A | (0,1,0) | 21 = dim(G) | r | 5/7 = n_C/g | wall |
| V | (1,0,0) | 7 = g | r | 3/7 = N_c/g | wall |
| V⊗Sp | (1,0,1) | 48 = 2^{N_c}×C₂ | √g | 7/8 | tensor |

**Split**: 4 non-wall + 3 wall = (C₂ - r) + N_c = 4 + 3 = g.

## Classical Dimensions

Sum = 1 + 8 + 35 + 21 + 7 + 48 + 27 = **147 = N_c × g²**

## Conformal Weights

The wall reps have h = BST integer / g:
- h(V) = **3/7 = N_c/g**
- h(A) = **5/7 = n_C/g**
- h(S²Sp) = **6/7 = C₂/g**

The spinor reps have h = BST integer / 2^{N_c}:
- h(Sp) = **3/8 = N_c/2^{N_c}**
- h(V⊗Sp) = **7/8 = g/2^{N_c}**

The Chern integers are the NUMERATORS of the conformal weights.

## Key Fusion Rules

- Sp × Sp = **1 + S²Sp + A + V** (spinor² = vacuum + all wall reps)
- V × V = 1 + A + S²V (vector² = vacuum + adjoint + simple current)
- S²V × S²V = **1** (simple current, generates Z₂)
- Sp × S²V = V⊗Sp (simple current permutes spinor sector)

## Fusion Channel Counts (Row Sums)

| Rep | Total channels | BST |
|-----|---------------|-----|
| 1, S²V | 7 | g |
| Sp, V⊗Sp | 16 | 2⁴ |
| S²Sp, A, V | **13** | **c₃** |

★ The three wall (confined) representations each have exactly **c₃ = 13** fusion channels. The third Chern class controls confinement.

## Quantum Dimensions and D²

- D² = 4 = C₂ - r (from non-wall quantum dims)
- FPdim² sum = 1 + 7 + 1 + 4 + 4 + 4 + 7 = 28 = 4g (from S-matrix)
- D = 2 = r → topological entanglement entropy γ = ln(r) = ln 2

## The Z₂ Simple Current

S²V acts as an involution on the fusion ring:
- S²V × 1 = S²V (trivial orbit)
- S²V × Sp = V⊗Sp (swaps spinor pair)
- S²V × A = A (fixed point)
- S²V × S²Sp = S²Sp (fixed point)
- S²V × V = V (fixed point)

Fixed points = 3 wall reps = N_c objects. The simple current Z₂ fixes the confined sector.

## Spinor Generates Confinement

Sp × Sp = 1 + S²Sp + A + V: the spinor squared produces exactly one copy of each wall rep plus the vacuum. Every confined representation can be accessed by fusing two spinors.

In BST: the spinor is the ELECTRON (dim = 8 = 2^{N_c}), and fusing two electrons produces all confined (colored) states plus the vacuum.

## Physical Interpretation

The fusion ring is the ALGEBRAIC structure of how quantum numbers combine in BST:
- g = 7 representations = the genus counts the particle types
- N_c = 3 confined reps = the colors (permanently trapped on the wall)
- c₃ = 13 channels per wall rep = the Weinberg angle numerator controls confinement
- √g controls spinor fusion = topology (genus) sets the spinor quantum dimension
- Z₂ simple current = matter-antimatter symmetry (S²V = charge conjugation)
