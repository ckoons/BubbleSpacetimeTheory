# The Mass Gap Anatomy: A Complete Algebraic Portrait

**Status**: PROVED (exact computation, 6 toys)
**Date**: March 16, 2026
**Toys**: 178-183
**Depends on**: WZW diamond (175), Verlinde (176), Siegel (177), all Chern work

## Statement

The BST mass gap C₂ = 6 is not merely a number. It is a **meeting place** — the unique point where seven algebraic traditions, two energy scales, and the entire Chern class sequence converge.

## The Seven Faces (Toy 181)

Seven WZW models share c = C₂ = 6 (seven = g = genus):

| Model | ℓ+h∨ | BST encoding | Route |
|-------|------|-------------|-------|
| so(7)₂ | 7 = g | Physical algebra | IR |
| G₂₃ | 7 = g | Exceptional subgroup | — |
| sp(8)₁ | 6 = C₂ | Level-1 symplectic | UV |
| su(7)₁ | 8 = 2^{N_c} | Level-1 special unitary | UV |
| su(3)₉ | 12 = 2C₂ | Color at high level | — |
| so(12)₁ | 11 = c₂ | Level-1 orthogonal | UV |
| E₆₁ | 13 = c₃ | Exceptional E-type | UV |

Network arithmetic:
- Σ(ℓ+h∨) = 64 = 2^{C₂}
- Σ(ℓ·dim) = 384 = 2^g × N_c
- Σ dim = 271 (prime: the network is irreducible)
- LCM{6,7,8,11,12,13} = 24024 = 2^{N_c} × N_c × g × c₂ × c₃
- 91 total integrable reps = g × c₃ = T_{c₃} = C(2g, 2)

## The E₆-E₇-E₈ Triple (Toy 182)

The three largest exceptional algebras at level 1:
- c(E₆₁) = 6 = C₂
- c(E₇₁) = 7 = g
- c(E₈₁) = 8 = 2^{N_c}

Sum = 21 = dim(B₃) = dim(C₃). Product = 336 = 2^{N_c} × P(1).

Dimensions: dim(E₆) = C₂ × c₃ = 78, dim(E₇) = g × 19 = 133, dim(E₈) = 2^{N_c} × (2^{n_C}-1) = 248.

Denominator sum: 13 + 19 + 31 = 63 = 2^{C₂} - 1. The E-type primes are c₃ (strong force), 19 (dark energy denominator), 2^{n_C} - 1 (Mersenne at dimension).

dim(E₇) - dim(E₆) = 55 = C(c₂, 2) = T_{10} = triangular number of dim K.

Deligne's series skips c = 3 and c = 5 (= N_c and n_C) — these are infrared integers, invisible to level-1 exceptionals.

## The IR/UV Handshake

```
UV (bulk, level 1):         6 ← 7 ← 8     (E₆ → E₇ → E₈)
                            ↕   ↕
IR (boundary, level 2):   5 → 6 → 7        (n_C → C₂ → g)
```

The mass gap C₂ = 6 and genus g = 7 are **holographic** — present at both levels. N_c and n_C are infrared (level 2 only). 2^{N_c} is ultraviolet (level 1 only).

## The Chern Quadratic (Toy 180)

C₂ and g are roots of:

**x² - c₃x + P(1) = 0** → x² - 13x + 42 = 0

Discriminant = c₃² - 4P(1) = 169 - 168 = **1**.

General: Δ(N) = [2N(N-2)/(N+3)]². Setting Δ = 1: N = 3 uniquely.
- N=2: Δ = 0 (self-dual mirror, C₂ = g)
- N=3: Δ = 1 (mirror just cracked, consecutive integers)
- N≥4: Δ > 1 (mirror shattered, too far apart)

**The Standard Model is the first case past Langlands self-duality.**

## The Coset Cascade (Toys 178-179)

| Coset | c | BST | Theorem |
|-------|---|-----|---------|
| sp(6)₂ | 7 | g | L-group |
| so(7)₂ | 6 | C₂ | Physical |
| sp(6)₂/su(3)₁ | 5 | n_C | (N-2)(N-3)=0 selects N=2,3 |
| so(7)₂/so(5)₂ | 2 | r | Rank-stripped |
| so(7)₂/G₂₂ | 4/3 | — | Tri-critical Ising |

The consecutive triple (5, 6, 7) = (coset, physical, dual).

## The 14th Uniqueness Condition (Toy 183)

**d₂(Q^n) = N_c^{N_c}** if and only if n = 5.

Proof: d₂ = (n+1)(n+4)/2. Setting equal to ((n+1)/2)^{(n+1)/2} gives 2N+3 = N^{N-1}, which has unique positive solution N = 3.

The second spectral multiplicity of Q⁵ equals 27 = 3³ = dim(fund E₆) = m_s/m̂. The spectral geometry of Q⁵ contains E₆ representation theory.

## Uniqueness Conditions 9-14

| # | Condition | Equation | Solutions |
|---|-----------|----------|-----------|
| 9 | su(N)_n has c = n | N(N-3) = 0 | N = 3 |
| 10 | c(G)·c(^LG) = P(1) | Exponential = polynomial | N = 3 |
| 11 | Coset = n_C | (N-2)(N-3) = 0 | N = 2, 3 |
| 12 | Self-duality breaks | so(2N+1) ≇ sp(2N) | N ≥ 3 |
| 13 | Δ = 1 (consecutive) | 2N²-5N-3 = 0 | N = 3 |
| 14 | d₂ = N_c^{N_c} | 2N+3 = N^{N-1} | N = 3 |

## The Spectral Multiplicities (Toy 183)

- d₀ = 1 (vacuum)
- d₁ = 7 = g (genus)
- d₂ = 27 = N_c^{N_c} = dim(fund E₆)
- d₃ = 77 = g × c₂ (from Toy 146)
- d₄ = 182 = r × g × c₃ (from Toy 146)

Partial sums:
- Σ(k≤1) = 8 = 2^{N_c}
- Σ(k≤2) = 35 = n_C × g
- Σ(k≤9) = 8008 = 2^{N_c} × g × c₂ × c₃

## Conclusion

The mass gap C₂ = 6 is the algebraic center of gravity of BST. It is:
- The central charge of 7 WZW models (= g models)
- The first eigenvalue of the Laplacian on Q⁵
- The rank of E₆ (the GUT algebra)
- The number of free bosons encoding Q⁵
- The point where Langlands self-duality first breaks (Δ = 1)
- The holographic bridge between UV and IR
- The root of x² - c₃x + P(1) = 0
- C₂ = n_C + 1 = "geometry + existence"
