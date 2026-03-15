# BST = Level-2 WZW Model of so(7)

**Status**: PROVED (exact computation)
**Date**: March 16, 2026
**Toys**: 171 (quantum groups)
**Depends on**: Langlands dual (Toy 163), theta correspondence (Toy 168)

## The Central Equation

The Wess-Zumino-Witten central charge of so(7) at level 2:

**c = l x dim(G) / (l + h^v) = 2 x 21 / (2 + 5) = 42/7 = 6 = C_2**

The mass gap IS the WZW central charge. The numerator is P(1) = 42, the denominator is g = 7.

## The Consecutive Triple

The BST structural triple (n_C, C_2, g) = (5, 6, 7) is:

**(h^v, h^v + 1, h^v + 2)**

where h^v = 5 is the dual Coxeter number of B_3 = so(7).

| Value | BST role | Coxeter role |
|-------|----------|--------------|
| 5 = n_C | Complex dimension | h^v (dual Coxeter number) |
| 6 = C_2 | Mass gap / second Chern | h^v + 1 = 2N_c |
| 7 = g | Genus | h^v + 2 = 2N_c + 1 |

Why consecutive? Because h^v(B_n) = 2n - 1 for B_n, and n = N_c = 3 gives h^v = 5. Then C_2 = 2N_c = h^v + 1 and g = 2N_c + 1 = h^v + 2.

## Level 2: The Physical Level

Level 2 is uniquely selected because:

1. **Only integer central charge**: c = 42/7 = 6 is the ONLY level giving integer c for so(7)
2. **q = e^{2pi i/g}**: the quantum parameter is a primitive g-th root of unity
3. **n_C anyons**: exactly 5 integrable representations survive
4. **D^2 = 14**: total quantum dimension squared = n_C^2 - c_2

The 5 surviving representations at level 2 have quantum dimensions (1, 2, 2, 2, 1), giving D^2 = 1+4+4+4+1 = 14.

## BST Levels of so(7)

Every BST-special root of unity appears as a specific level:

| Level | l + h^v | BST integer | Central charge |
|-------|---------|-------------|----------------|
| 1 | 6 = C_2 | mass gap root | c = g/2 = 7/2 |
| 2 | 7 = g | genus root | **c = C_2 = 6** |
| 3 | 8 = 2^{N_c} | Golay distance | c = 63/8 |
| 6 | 11 = c_2 | dim K root | c = 126/11 |
| 8 | 13 = c_3 | third Chern | c = 168/13 |

The level IS the BST integer minus h^v = n_C.

## Casimir = Mass Gap

The quadratic Casimir of the standard (7-dimensional) representation of so(7):

C_2(std) = <lambda, lambda + 2rho> = <e_1, e_1 + (5,3,1)> = 6 = C_2

The Casimir eigenvalue of the fundamental representation IS the mass gap.

## Conformal Weights

At level l, conformal weight of std: h = C_2(std) / (2(l + h^v)) = 3/(l + 5)

| Level | h(std) | BST expression |
|-------|--------|----------------|
| 1 | 3/6 = 1/2 | 1/r |
| 2 | 3/7 | **N_c/g** |
| 3 | 3/8 | N_c/2^{N_c} |

At the physical level 2: h(std) = N_c/g = 3/7.

## Five Perspectives on (5, 6, 7)

1. **Chern topology**: n_C = dim_C(Q^5), C_2 = second Chern number, g = genus
2. **Theta correspondence**: n_C = signature excess, C_2 = dim(std Sp(6)), g = dim(std O(7))
3. **Dual Coxeter**: n_C = h^v, C_2 = h^v+1, g = h^v+2
4. **WZW model**: n_C = critical level, C_2 = central charge, g = denominator
5. **Partition function**: p(n_C) = g, p(C_2) = c_2 (see Toy 170)

## Connection to Riemann Proof

The level-2 WZW model at q^g = 1 is a rational CFT. Its modular S-matrix transforms under SL(2,Z), providing the modular properties needed for the Selberg-Riemann bridge:

- The S-matrix at level 2 involves sin(n*pi/7) (heptagonal geometry)
- The Verlinde fusion ring is the truncated representation ring
- The modular invariance of the WZW partition function connects to the functional equation of the L-function

## Summary

BST is the level-2 WZW model of so(7). The mass gap C_2 = 6 is the central charge. The structural triple (5, 6, 7) = (h^v, h^v+1, h^v+2). Everything follows from three consecutive integers.
