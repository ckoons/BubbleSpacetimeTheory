---
title: "L13: RH Closure via c-function Maass-Selberg Positivity"
author: "Lyra"
date: "March 22, 2026"
status: "Research brief — ready to formalize"
depends: "Toy 324 (c-function unitarity, 5/5 PASS), Lemma 5.5 (exponent rigidity, PROVED), Props 5.2-5.3 (PROVED)"
---

# L13: RH Closure via c-function Unitarity

## The mechanism (Toy 324)

The BC₂ c-function satisfies:
- c(ν)·c(-ν) = |c(ν)|² **exactly** at σ = 1/2 (verified to 50 digits)
- Monotonic deviation off the critical line

**Why:** At σ = 1/2, the spectral parameter ν = iγ is purely imaginary. So -ν = -iγ = ν̄ (complex conjugate). The conjugation identity $c(-\nu) = c(\bar{\nu}) = \overline{c(\nu)}$ gives c(ν)·c(-ν) = |c(ν)|².

At σ ≠ 1/2, ν acquires a real part. Then -ν ≠ ν̄, and the conjugation identity fails.

## Why this is different from the failed Laplace approach

- **Laplace (Lemma 5.6, FAILED):** Global property — pole structure of L[F](s). Mixes all zeros together. On-line zeros also produce complex poles → tautology.
- **c-function unitarity (L13):** Local property — checked at each spectral parameter independently. Each zero tested on its own. No mixing, no balancing, no tautology risk.

## The closure path

1. The Arthur trace formula spectral decomposition requires the Maass-Selberg positivity: ||Λ^T E(s)||² ≥ 0 for all truncation parameters T.

2. The Maass-Selberg formula for D_IV^5 expresses this norm in terms of c-function values at the spectral parameters of the Eisenstein series.

3. The scattering matrix M(s) has poles at the zeros of ξ. At each zero s₀, the residue contributes to the spectral decomposition.

4. The residual contribution from a zero at s₀ involves c(ν₀)·c(-ν₀) where ν₀ = s₀ - 1/2.

5. At σ₀ = 1/2: c(ν₀)·c(-ν₀) = |c(ν₀)|² → positivity holds.

6. At σ₀ ≠ 1/2: c(ν₀)·c(-ν₀) ≠ |c(ν₀)|² → positivity potentially violated.

7. Trace formula is proved → spectral decomposition IS consistent → positivity MUST hold → σ₀ = 1/2.

## Three concerns to address

**(a)** Must show Maass-Selberg positivity REQUIRES c(ν)·c(-ν) = |c(ν)|² at each zero's spectral parameter, not just correlates. Could other terms absorb the deviation?

**(b)** Residues at off-line zeros involve c-function RATIOS (from the Langlands-Shahidi scattering matrix), not bare c-function values. The unitarity violation must propagate through these ratios.

**(c)** Cross-parabolic contributions (maximal parabolics GL(1)×SO(3,2) and GL(2)×SO(1,2)) have different c-functions. Must show these don't compensate the minimal parabolic violation.

## Rank-2 advantage

In rank 1 (SL(2,ℝ)): the Maass-Selberg relation is scalar, and the constraint alone doesn't exclude off-line zeros. In rank 2 (SO(5,2)): the matrix-valued Maass-Selberg relation with the algebraic lock σ+1=3σ creates additional constraints. The 1:3:5 harmonic lock means the three short-root contributions must SIMULTANEOUSLY satisfy positivity — much more restrictive.

## Key references

- Langlands, "On the Functional Equations Satisfied by Eisenstein Series" (1976)
- Arthur, "An Introduction to the Trace Formula" (2005), §§26-27 on Maass-Selberg
- Müller, "The Trace Class Conjecture in the Theory of Automorphic Forms" (1989)
- Toy 324 data: play/toy_324_residue_matching.py

## Success criterion

Write a complete Proposition 5.X replacing Lemma 5.6 + Theorem 5.7 that:
1. States the Maass-Selberg positivity for D_IV^5 explicitly
2. Shows the residual contribution from an off-line zero violates positivity
3. Uses the rank-2 (BC₂) structure and algebraic lock
4. Does NOT assume anything about L[F]'s pole structure (avoids the Laplace trap)
