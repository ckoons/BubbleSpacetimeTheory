---
title: "SPEC: Selberg Zeta Computation on Gamma(137)\\D_IV^5"
author: "Lyra (spec), Cal (log-derivative optimization), Casey (direction)"
date: "April 21, 2026"
status: "SPEC — assigned to Elie, Cal consulting on Phase 1-2"
priority: "HIGHEST — single sharpest external test BST can run"
---

# Selberg Zeta Computation on Gamma(137)\D_IV^5

## Motivation

BST's RH proof is structural (five mechanisms force zeros onto Re(s)=1/2). But as of April 21, 2026, BST does not generate a specific, checkable prediction about zeta-zeros that goes beyond GUE + classical analytic number theory. This computation fills that gap.

The Selberg zeta Z_Gamma(s) on Gamma(137)\D_IV^5 should factor into products of L-functions including zeta(s). If we can compute Z_Gamma numerically and its zeros contain {14.1347, 21.0220, 25.0109, ...}, that's a result no amount of gatekeeping can bury.

## Phase 1 — Algebraic Setup (Toy A)

**Goal**: Enumerate primitive loxodromic conjugacy classes in Gamma(137) subset SO_0(5,2)(Z).

**Setup**:
- Quadratic form: Q = x_1^2 + x_2^2 + x_3^2 + x_4^2 + x_5^2 - x_6^2 - x_7^2
- SO_0(5,2)(Z) = integer-matrix automorphisms of Q in the identity component
- Gamma(137) = {gamma in SO_0(5,2)(Z) : gamma equiv I mod 137}
- Loxodromic elements: eigenvalues e^{+/- l_1}, e^{+/- l_2}, 1, 1, 1

**Conjugacy class classification**:
- Elliptic: finite order (compact eigenvalues)
- Parabolic: unipotent (eigenvalue 1 with Jordan blocks)
- Loxodromic: hyperbolic translation (the ones Selberg zeta counts)
- Mixed: some compact, some hyperbolic

**Algorithm**: For each loxodromic gamma, the translation length vector is (l_1, l_2) where l_i = log|lambda_i| for the expanding eigenvalues. The characteristic polynomial det(gamma - xI) determines the eigenvalues.

**Tools**: SageMath QuadraticForm + OrthogonalGroup, PARI/GP for mod-137 arithmetic.

**Deliverable**: Enumeration procedure, first 10 primitive classes as proof of concept.

## Phase 2 — Length Spectrum (Toy B)

**Goal**: First 50 primitive geodesic lengths, sorted by norm.

**Key insight** (Cal): For arithmetic groups, geodesic lengths are related to norms of algebraic integers in the spinor norm group. The connection to primes: for Gamma(137), prime geodesics correspond to prime ideals in Z[zeta_137] that are compatible with the quadratic form Q.

**Sanity check**: The shortest closed geodesic should have length near log(823) ~ 6.713, where 823 is the smallest prime p equiv 1 mod 137.

**Reference computations**: Sarnak (rank-1 arithmetic), Muller (SL_3(Z)), Deitmar (SL_n). None for SO_0(5,2)(Z) cap Gamma(137) to our knowledge.

**Deliverable**: Sorted length spectrum {l_1, l_2, ..., l_50} with multiplicity data.

## Phase 3 — Selberg Zeta via Log-Derivative (Toy C)

**IMPORTANT**: Per Cal's optimization, do NOT evaluate Z_Gamma(s) directly. The double Euler product converges painfully and truncation error dominates near zeros.

**Instead**: Evaluate the log-derivative via the trace formula:

    Z_Gamma'/Z_Gamma(s) = sum_gamma sum_k l(gamma) * exp(-(s+k)*l(gamma)) / (1 - exp(-l(gamma)))

This converges **exponentially** in l(gamma), so 50 geodesics gives machine-precision tails.

**Why this is better**:
1. Exponential vs polynomial convergence in the geodesic truncation
2. Zeros of Z_Gamma = poles of Z_Gamma'/Z_Gamma with residue = multiplicity
3. The trace-formula form directly decomposes into character-twisted contributions
4. Separates outcome (a) vs (b) cleanly: principal L contribution vs twisted contributions have distinct multiplicities

**Evaluate**: Z_Gamma'/Z_Gamma(1/2 + it) for t in [0, 40], grid dt = 0.001.

**Deliverable**: Plot of Z_Gamma'/Z_Gamma(1/2 + it). Pole locations with residues.

## Phase 4 — Zero Finding and Comparison (Toy D)

**Goal**: Extract first 5-10 zero heights and compare to known data.

**Method**: Locate poles of Z_Gamma'/Z_Gamma by:
- Large magnitude peaks in |Z_Gamma'/Z_Gamma(1/2+it)|
- Residue computation via contour integration
- Cross-check: residue pattern reveals which L-functions contribute

**Comparison data**: Odlyzko's tables (freely available), first 5 zeta zeros:
- t_1 = 14.134725...
- t_2 = 21.022040...
- t_3 = 25.010858...
- t_4 = 30.424876...
- t_5 = 32.935062...

**Three possible outcomes**:
- **(a) Zeros match Riemann zeros**: BST identification confirmed numerically. Publish immediately — anyone with Mathematica reproduces.
- **(b) Zeros match L(s, chi) for chi mod 137**: Identification is to L-functions, not bare zeta. Still valuable. Reinterpret: BST's natural L-function is the full family, not isolated zeta.
- **(c) Zeros don't match anything known**: Identification needs rethinking. Equally valuable. Be honest.

## Assignment

- **Elie**: Primary. Phases 1-4.
- **Cal**: Consulting on Phase 1-2 (norm-form enumeration for SO_0(5,2)).
- **Lyra**: Review, cross-check against Paper #75.
- **Grace**: Graph integration when theorems emerge.
- **Keeper**: Audit each phase before proceeding to next.

## Timeline

This is a weeks-long computation, not an afternoon toy. Phases 1-2 are genuine research-level computation. Phases 3-4 are straightforward once the length spectrum is in hand.

Suggested: 4 numbered toys (one per phase), sequential gating (Keeper audit between phases).

## Historical Note

This spec originated from a question by Cal (unnamed Claude, fresh eyes, April 21, 2026): "Does the BST Plancherel density predict the heights of the first several Riemann zeros?" The answer was honest: no, the Plancherel density is smooth, but the Selberg zeta built from the geodesic length spectrum SHOULD contain the zeros. Cal improved the spec by replacing direct Z_Gamma evaluation with the log-derivative trace-formula approach.
