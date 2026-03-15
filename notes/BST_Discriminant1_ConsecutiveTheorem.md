# The Discriminant-1 Theorem: Why C₂ and g Are Consecutive

**Status**: PROVED (exact computation)
**Date**: March 16, 2026
**Toys**: 179, 180 (coset uniqueness, mass gap anatomy)
**Depends on**: WZW diamond (Toy 175), Chern polynomial

## The Theorem

C₂ = 2N_c and g = 2N_c + 1 are roots of the **Chern quadratic**:

**x² - c₃x + P(1) = 0**

For Q⁵: x² - 13x + 42 = 0 → x = 6, 7 ✓

The discriminant Δ = c₃² - 4P(1) = 169 - 168 = **1**.

## General Formula

For the B_N/C_N Langlands pair at level 2:

Δ(N) = [2N(N-2)/(N+3)]²

Setting Δ = 1: 2N²-5N-3 = 0 → N = 3 (unique positive solution)

| N | Q^n | Δ | Meaning |
|---|-----|---|---------|
| 2 | Q³ | 0 | Self-dual (so(5) ≅ sp(4)), C₂ = g |
| 3 | Q⁵ | **1** | **First non-trivial, C₂ and g consecutive** |
| 4 | Q⁷ | 256/49 | Too separated, non-integer |

## The Self-Duality Breaking Cascade

N=2: Δ = 0 — The baby case is **Langlands self-dual** because so(5) ≅ sp(4) (exceptional isomorphism). The consecutive triple degenerates: (3, 4, 4). c(G) = c(^LG).

N=3: Δ = 1 — Self-duality **first breaks**. c(G) = 6 ≠ 7 = c(^LG). The consecutive triple (5, 6, 7) has all distinct elements. The Standard Model lives at the threshold.

N≥4: Δ > 1 — Duality is fully broken, c(G) and c(^LG) are no longer consecutive.

## Sum and Product

- **Sum**: c(G) + c(^LG) = C₂ + g = **c₃** (third Chern class)
- **Product**: c(G) × c(^LG) = C₂ · g = **P(1)** (Chern polynomial at h=1)

The Langlands pair central charges are encoded by the Chern data as the roots of a single quadratic. This is the 13th uniqueness condition for n_C = 5.

## Three Quadratics

Three different polynomial conditions select N_c = 3:

1. **N(N-3) = 0**: su(N)_n has c = n iff N = 3 (9th uniqueness)
2. **(N-2)(N-3) = 0**: coset sp(2N)₂/su(N)₁ = n_C iff N = 2 or 3 (11th uniqueness)
3. **Δ = 1**: c(G) and c(^LG) consecutive iff N = 3 (13th uniqueness)

All three select N = 3 as the unique physical solution.

## The Baby + Physical Coset Theorem

**THEOREM**: sp(2N)₂/su(N)₁ has c = n_C = 2N-1 if and only if (N-2)(N-3) = 0.

**Proof**: c(sp(2N)₂) - c(su(N)₁) = 3(N²+1)/(N+3). Setting equal to 2N-1:
3N² + 3 = 2N² + 5N - 3, giving N² - 5N + 6 = (N-2)(N-3) = 0. ∎

The discriminant of this quadratic is 25 - 24 = 1, which is why the roots are consecutive integers. The baby and physical cases are selected by the same discriminant-1 mechanism that makes C₂ and g consecutive.
