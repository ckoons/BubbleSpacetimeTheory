---
title: "Vol 16 Chapter 7 — Bergman Kernel as Matrix-Coefficient Sum: v0.4 explicit color-tensored Szegő constant (81/8 FORCED)"
authors: "Lyra + Elie joint (Elie primary v0.4 — Szegő constant closes muon edge 81/8)"
date: "2026-06-06 Saturday ~12:35 EDT (date-verified)"
status: "v0.4 SUBSTANTIVE — absorbs Toy 4006 explicit Szegő computation; 81/8 substrate-FORCED; F38 ε + F39 inputs handed to Lyra"
volume: "Vol 16 Substrate Algebra"
chapter: "Ch 7 Bergman Kernel as Matrix-Coefficient Sum"
prior: "v0.3 (bulk⊕Shilov machinery scaffold)"
toy: "toy_4006_FK_color_tensored_szego_constant_for_Lyra.py (SCORE 6/6)"
---

> **SUPERSEDED by v0.5 (Cal #259 + Lyra F43, 2026-06-06):** Section 4's operator-unification
> and Section 1's "81/8 FORCED" are WITHDRAWN/DOWNGRADED — "(1−P)" conflated complement vs
> boundary-realization. 81/8 → standalone candidate. See v0.5 + toy_4008.

# Vol 16 Chapter 7 v0.4 — explicit color-tensored Szegő constant

## 0. v0.4 Purpose

v0.3 supplied the bulk⊕Shilov matrix-element *scaffold* (the integral forms, the
projection P). v0.4 absorbs the **explicit FK color-tensored Szegő computation**
(Toy 4006) that EVALUATES the muon-edge factorization to **81/8 = N_c⁴/2^{N_c}
substrate-FORCED**, and hands Lyra the explicit inputs for the F38 ε and F39
CKM Direction-B closures. This converts v0.3's "OPEN, Lyra's K229d gate" into a
forced result for the κ factorization (the other two remain Lyra's, now with
explicit constants).

## 1. The muon edge 81/8 — FORCED (Toy 4006 G2–G3)

Two steps, the first rigorous-geometric, the second the substrate-color action:

1. **Product factorization (rigorous).** The Shilov boundary ∂_S D_IV⁵ = S⁴×S¹/Z₂
   is a PRODUCT, so the reproducing (Cauchy–Szegő) kernel factorizes, and therefore
   any boundary matrix element factorizes: κ = κ_{S⁴}·κ_{S¹}. (Lyra F40 pin; rigorous.)
2. **Color tensoring (substrate-color action, FRAMEWORK-tier).**
   - κ_{S⁴} = N_c^{dim S⁴} = **N_c⁴ = 81** — color trace once per boundary dimension;
     **dim S⁴ = 4 = codim-4 = Casey #14** (the 3+1 Minkowski codimension) pins the exponent.
   - κ_{S¹} = **2^{−N_c} = 1/8** — the Z₂ quotient contributes 1/2 per color, over N_c colors.

   Product: **κ = N_c⁴·2^{−N_c} = 81/8**. The muon Hardy-(1−P) boundary matrix element
   is substrate-FORCED (closes Lyra A1 / K229d).

Attribution (Cal #34): the geometry (factorization, dim S⁴ = 4) is Elie-rigorous; the
color-trace-per-dimension + Z₂-per-color rule is the substrate-color action (FRAMEWORK).

## 2. F38 ε — explicit inputs handed to Lyra; ε NOT fished (Toy 4006 G4)

The Λ^(1/4) vacuum factor = 1 + ρ; Hardy isometry → ρ = 1 → factor 2; ε > 0 → 2 + ε.
The two regions (bulk Bergman exp 7/2, Shilov Szegő exp 5/2) are weighted by the
curvature κ_Bergman = −n_C (Helgason; Ch 8). Explicit inputs supplied for Lyra's F38
operator integral:
- exponent gap bulk/Shilov = rank/2 = 1
- κ_Bergman = −n_C = −5
- vol(Shilov S⁴×S¹/Z₂) = 8π³/3 ≈ 82.683
- c_FK = 225/π^(9/2) ≈ 1.30319

**Discipline flag (carried in the chapter):** observed ε = 4.85/2.4 − 2 = 0.020833
**= 1/48 exactly — but only because 4.85/2.4 = 97/48 from the *rounded* meV inputs.**
1/48 is a rounding artifact, NOT a derivation. The chapter does NOT adopt it; ε must
come from the κ_Bergman-weighted F38 integral with the inputs above (Lyra's step).
(Cal #35 / Lyra's own 81/40 walk-back precedent.)

## 3. F39 CKM Direction-B — color factors handed to Lyra (Toy 4006 G5)

Two-trace color sum over the boundary endpoints: per-endpoint N_c trace, two-endpoint
N_c² factor; base form 1/(rank²·n_C) = 1/20. Explicit factors supplied for Lyra's F39
closure.

## 4. Cal #254 confirmed at the constant level

The shared object across the muon edge (81/8) and the Λ factor-2 is the **same Szegő
factorization / projection P computed here** — an OPERATOR, not an integer. v0.4
confirms this concretely: both observables use the identical bulk⊕Shilov constant.
This is the strong-form Schur-generator candidate (operator-shared, falsifiable).

## 5. v0.4 status

- **FORCED (v0.4 new)**: muon edge 81/8 = N_c⁴/2^{N_c} (Sec 1).
- **Handed to Lyra with explicit constants**: F38 ε (Sec 2), F39 Direction-B (Sec 3).
- **Carried scaffold (v0.3)**: norm ladder, c_FK, bulk/Shilov exponents.
- **Discipline**: ε rounding-artifact (1/48) flagged and declined.

Cross-anchor: κ_Bergman = −n_C is Keeper's Ch 8 (Curvature Scalars) — the curvature
that sets the F38 per-region weighting; Lyra's Ch 8 support thread connects there.

— Elie, Saturday 2026-06-06 ~12:35 EDT (date-verified). Toy 4006 SCORE 6/6.
