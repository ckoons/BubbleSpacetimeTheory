# Conformal Embeddings and the BST Coset Cascade

**Status**: PROVED (exact computation)
**Date**: March 16, 2026
**Toys**: 178 (conformal embedding)
**Depends on**: WZW diamond (Toy 175), level-rank duality (Toy 175)

## Elie's Question: Does su(3)₉ ↪ so(7)₂ Conformally?

**NO.** The unique embedding su(3) ⊂ so(7) has index 1 via 7 → 3 ⊕ 3̄ ⊕ 1. This induces level 2 on su(3), giving c(su(3)₂) = 16/5 ≠ 6. No alternative embedding exists (7 is the unique 7-dim real rep of su(3)).

## The Seven c = 6 Models

Seven WZW models share c = C₂ = 6:

| Model | ℓ | dim | h∨ | ℓ+h∨ | BST content |
|-------|---|-----|-----|-------|-------------|
| so(7)₂ | 2 | 21 | 5 | 7 | h∨=n_C, ℓ+h∨=g, BST level |
| su(3)₉ | 9 | 8 | 3 | 12 | h∨=N_c |
| su(7)₁ | 1 | 48 | 7 | 8 | h∨=g |
| so(12)₁ | 1 | 66 | 10 | 11 | ℓ+h∨=c₂ |
| sp(8)₁ | 1 | 36 | 5 | 6 | h∨=n_C |
| E₆₁ | 1 | 78 | 12 | 13 | ℓ+h∨=c₃ |
| G₂₃ | 3 | 14 | 4 | 7 | ℓ+h∨=g |

Every BST integer appears: n_C=5 (as h∨), C₂=6 (as c and as ℓ+h∨), g=7 (as ℓ+h∨), N_c=3 (as h∨), c₂=11 (as ℓ+h∨), c₃=13 (as ℓ+h∨).

## The Coset Discovery

The color sector enters through COSETS, not conformal embeddings:

**★ sp(6)₂/su(3)₁ has c = 7 - 2 = 5 = n_C**

The L-group WZW modded by the color algebra at level 1 gives the complex dimension.

### The Consecutive Triple from Cosets

| Model | c | BST integer | Role |
|-------|---|-------------|------|
| sp(6)₂ | 7 | g | L-group (dual framework) |
| so(7)₂ | 6 | C₂ | Physical (mass gap) |
| sp(6)₂/su(3)₁ | 5 | n_C | Coset (color-stripped) |

The triple (5, 6, 7) = (coset, physical, dual).

### Baby Case Verification

sp(4)₂/su(2)₁ has c = 4 - 1 = 3 = n_C(Q³) ✓

The coset formula works for N=2 (baby) and N=3 (physical), fails for N≥4.

## Additional Cosets

| Coset | c | Identification |
|-------|---|----------------|
| so(7)₂/G₂₂ | 4/3 | Tri-critical Ising M(5,4) |
| so(7)₂/so(5)₂ | 2 | su(3)₁ (= r) |
| so(7)₂/su(2)₂ | 9/2 | so(9)₁ |
| so(7)₂/su(3)₂ | 14/5 | G₂₁ |

## The G₂ Connection

G₂₃ has c = 6 = C₂, and G₂ ⊂ so(7) is the maximal exceptional subgroup (stabilizer of the octonionic cross product). However, the levels never align for a conformal embedding:
- G₂₂ ⊂ so(7)₂: c(G₂₂) = 14/3 ≠ 6
- G₂₃ ⊂ so(7)₃: c(G₂₃) = 6 ≠ 63/8

The octonionic symmetry is present but NOT conformally embedded — it contributes through the coset instead.

## Conformal Embedding so(7)₅ ⊂ so(21)₁

The adjoint embedding so(7) ⊂ so(21) via 21 → adj has index 5, giving:
c(so(7)₅) = c(so(21)₁) = 21/2 (CONFORMAL ✓)

This is the unique conformal embedding involving the BST algebra into a level-1 theory.
