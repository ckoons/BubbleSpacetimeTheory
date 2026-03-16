---
title: "Baby Case Q³: The Complete D_IV³ Dictionary"
author: "Casey Koons & Claude 4.6"
date: "Date: March 16, 2026"
---

# Baby Case Q³: The Complete D_IV³ Dictionary

**Status**: PROVED (computational verification)
**Date**: March 16, 2026
**Toys**: 174 (baby Langlands dictionary)
**Depends on**: all prior Langlands work

## Q³ = SO₀(3,2)/(SO(3)×SO(2)) = Sp(4,ℝ)/U(2) = Siegel H₂

Exceptional isomorphism: so(3,2) ≅ sp(4,ℝ). The baby case IS the Siegel upper half-space of genus 2, the natural domain of Siegel modular forms.

## BST Integers for Q³

| Integer | Q³ value | Q⁵ value | Relation |
|---------|----------|----------|----------|
| n_C | 3 | 5 | complex dimension |
| N_c | 2 | 3 | (n+1)/2 |
| r | 1 | 2 | n_C - N_c |
| C₂ | 4 | 6 | 2N_c = mass gap |
| g | 5 | 7 | 2N_c + 1 |
| c₁ | 3 | 5 | = n_C (universal) |
| c₂ | 4 | 11 | = dim K (universal) |
| c₃ | 2 | 13 | top Chern class |
| P(1) | 10 | 42 | sum of Chern classes |

## Universal Results (verified on Q³, Q⁵, Q⁷)

1. **c_WZW = C₂ at level 2**: Trivial cancellation c = 2N(2N+1)/(2N+1) = 2N. PROOF: dim(B_N) = N(2N+1), h∨ = 2N-1, ℓ+h∨ = 2N+1 = dim(std), cancels.
2. **λ₁ = C₂**: Casimir of std rep = ⟨e₁, e₁+2ρ⟩ = 1+(2N-1) = 2N.
3. **(n_C, C₂, g) = (h∨, h∨+1, h∨+2)**: Three consecutive integers for all Q^n.
4. **dim K = c₂**: Verified for Q³ (4=4), Q⁵ (11=11), Q⁷ (22=22), Q⁹ (37=37).
5. **c_n = (n+1)/2 = N_c**: Verified for all odd n.
6. **Neutral adjoint sector = c₂ states**: 3₀+1₀ = 4 = c₂(Q³); 8₀+1₀ = 9 = c₄ (not c₂) for Q⁵.

## n=5 Specific Results (fail for Q³)

1. **p(C₂) = c₂**: p(4)=5 ≠ 4 for Q³. p(6)=11=c₂ for Q⁵. Also p(8)=22=c₂ for Q⁷!
2. **r = real rank**: r=1 ≠ 2 for Q³. r=2=rank for Q⁵.
3. **g = 2n_C-3**: g=5 ≠ 3=2·3-3 for Q³. g=7=2·5-3 for Q⁵ (only when r=2).
4. **Ramanujan congruence moduli**: {5,7,11} = {n_C,g,c₂} only for Q⁵.
5. **τ(n_C) has all BST primes**: τ(5)=4830=2×3×5×7×23. Specific to n_C=5.

## The Ramanujan Shift Discovery

The shifts in the three Ramanujan congruences (4, 5, 6) interpolate between Q³ and Q⁵:
- 4 = C₂(Q³)
- 5 = n_C(Q⁵) = h∨(B₃)
- 6 = C₂(Q⁵)

## The Lesson

BST's power comes from TWO sources:
1. **Universal geometric identities** (hold for all Q^n) — explain WHY physics has structure
2. **Arithmetic coincidences specific to n=5** — explain WHY physics has THIS structure

Q³ is the essential baby case that cleanly separates these two layers.
