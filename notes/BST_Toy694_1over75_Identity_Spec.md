---
title: "Toy 694 Spec: The 1/75 Identity — Retiring the e-Exception"
author: "Keeper (from Lyra's finding)"
date: "April 3, 2026"
status: "SPEC — for Elie"
feeds: "T719 (Observable Algebra), Paper #14"
---

# Toy 694: The 1/(N_c · n_C²) Identity

## Background

Lyra discovered that the cosmological constant identity involving e and ln can be replaced by a cleaner BST expression:

**Old**: Λ ~ (7/12)^8 → agreement 0.53%
**New**: ln(138)/(50·e²) ≈ 1/(N_c · n_C²) = 1/75 → agreement **0.025%** (20× more precise)

If exact, the cosmological constant becomes:
$$\Lambda = \frac{\alpha^{8g}}{N_c \cdot n_C^2}$$

This would retire the e-exception from T719 (Observable Algebra). Every BST observable would live in Q̄(N_c, n_C, g, C₂, N_max)[π] — five integers and π, nothing else.

## Tests (8)

T1: Verify ln(138)/(50·e²) to 50+ digits
T2: Verify 1/(N_c · n_C²) = 1/75 = 0.01333333...
T3: Compute residual: ln(138)/(50·e²) - 1/75 to 50 digits
T4: Check if correction term ε = residual has BST form: ε/N_max^k for small k
T5: Check if 138 = N_max + 1 = α⁻¹ + 1 has BST significance
T6: Verify Λ = α^{56}/(N_c · n_C²) matches the observed cosmological constant
T7: Compare old identity (7/12)^8 vs new 1/75 — is 1/75 strictly better at all precisions?
T8: Does α^{8g}·N_c·n_C² = 1 have closed-form algebraic roots?

## PASS Criterion

8/8 = all verifications confirm. 7/8 = strong. If T4 finds a BST correction term, the e-exception is officially retired.

## Key Numbers

- N_c = 3, n_C = 5, g = 7, N_max = 137
- 75 = 3 × 25 = N_c × n_C²
- 138 = N_max + 1
- 8g = 56 (exponent in α^{56})
- 50 = 2 × n_C² = 2 × 25

## Why This Matters

If the e-exception falls, BST's observable algebra is **closed**: every physical quantity is a rational function of five integers times powers of α and π. No transcendentals from analysis (e, ln, γ) leak in. The arithmetic IS the physics.

---

*Keeper | April 3, 2026 | Toy 694 spec for Elie*
