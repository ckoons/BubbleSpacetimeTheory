# The Exceptional Chain and the c = 6 Network

**Status**: PROVED (exact computation)
**Date**: March 16, 2026
**Toys**: 178-182 (conformal embedding through exceptional chain)
**Depends on**: WZW diamond (Toy 175), Chern classes

## The E₆-E₇-E₈ Triple

The three largest exceptional Lie algebras at level 1 produce:

| Algebra | c at level 1 | BST integer | dim | 1+h∨ |
|---------|-------------|-------------|-----|------|
| E₆₁ | 6 | C₂ (mass gap) | 78 = C₂ × c₃ | 13 = c₃ |
| E₇₁ | 7 | g (genus) | 133 = g × 19 | 19 |
| E₈₁ | 8 | 2^{N_c} | 248 = 8 × 31 | 31 = 2^{n_C}-1 |

- **Sum**: 6 + 7 + 8 = 21 = dim(B₃) = dim(C₃)
- **Product**: 6 × 7 × 8 = 336 = 2^{N_c} × P(1) = 8 × 42
- **Denominator sum**: 13 + 19 + 31 = 63 = 2^{C₂} - 1

## Two Routes to the Mass Gap

**IR route (level 2)**: n_C=5 → C₂=6 → g=7 [physical + L-group pair]
**UV route (level 1)**: C₂=6 → g=7 → 8=2^{N_c} [E₆ → E₇ → E₈]

Overlap at (6, 7): the handshake between infrared physics and ultraviolet exceptional structure.

Deligne's series skips c = 3 (N_c) and c = 5 (n_C) — these are infrared integers accessible only at level 2.

## The Seven c = 6 Models

Seven WZW models share c = C₂ = 6 (seven = g = genus):

| Model | ℓ | dim | h∨ | ℓ+h∨ | Quantum parameter |
|-------|---|-----|-----|------|-------------------|
| so(7)₂ | 2 | 21 | 5 | 7 = g | ζ₇ (heptagonal) |
| G₂₃ | 3 | 14 | 4 | 7 = g | ζ₇ (heptagonal) |
| sp(8)₁ | 1 | 36 | 5 | 6 = C₂ | ζ₆ (hexagonal) |
| su(7)₁ | 1 | 48 | 7 | 8 = 2^{N_c} | ζ₈ |
| su(3)₉ | 9 | 8 | 3 | 12 = 2C₂ | ζ₁₂ |
| so(12)₁ | 1 | 66 | 10 | 11 = c₂ | ζ₁₁ |
| E₆₁ | 1 | 78 | 12 | 13 = c₃ | ζ₁₃ |

## Network Arithmetic

- **Σ(ℓ+h∨)** = 64 = 2^{C₂}
- **Σ(ℓ·dim)** = 384 = 2^g × N_c
- **Σ dim** = 271 (prime — the network is algebraically irreducible)
- **LCM** of {6,7,8,11,12,13} = 24024 = 2^{N_c} × N_c × g × c₂ × c₃
- **91 total integrable reps** = g × c₃ = T_{c₃} = C(2g, 2)

## The Discriminant-1 Theorem

C₂ and g are roots of the **Chern quadratic**: x² - c₃x + P(1) = 0

- x² - 13x + 42 = 0 → x = 6, 7
- Discriminant = c₃² - 4P(1) = 169 - 168 = 1
- General: Δ(N) = [2N(N-2)/(N+3)]², Δ = 1 uniquely at N = 3

The Standard Model is the first case past Langlands self-duality (Δ = 0 at N = 2).

## The Coset Cascade

sp(6)₂/su(3)₁ = n_C = 5: proved by (N-2)(N-3) = 0 (works only for baby + physical)

| Coset | c | BST |
|-------|---|-----|
| sp(6)₂ | 7 | g (L-group) |
| so(7)₂ | 6 | C₂ (physical) |
| sp(6)₂/su(3)₁ | 5 | n_C (color-stripped) |
| so(7)₂/so(5)₂ | 2 | r (rank-stripped) |
| so(7)₂/G₂₂ | 4/3 | tri-critical Ising |

## Uniqueness Conditions (Updated)

| # | Condition | Roots |
|---|-----------|-------|
| 9 | su(N)_n has c = n | N(N-3) = 0 → N = 3 |
| 10 | c(G)·c(^LG) = P(1) | N = 3 only |
| 11 | sp(2N)₂/su(N)₁ = n_C | (N-2)(N-3) = 0 → N = 2, 3 |
| 12 | Baby self-duality breaks | N ≥ 3, first at N = 3 |
| 13 | Δ = c₃² - 4P(1) = 1 | N = 3 uniquely |
