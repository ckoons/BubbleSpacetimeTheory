---
title: "Track BC v0.5 — hydrogen 1s explicit Bergman integral evaluation"
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-27 Wednesday EDT (~11:08 EDT)"
status: "v0.5 FRAMEWORK + EVALUATION. Continues v0.4 asymptotic methodology toward explicit Bergman integral evaluation. Partially unblocks Elie Toy 3562 Bergman harness."
related: ["Track BC v0.4 Bergman integral asymptotic methodology", "Track BC v0.3 substrate-Coulomb via Bergman 3D-projection"]
---

# Track BC v0.5 — explicit Bergman integral evaluation

## 1. Setup

Per v0.3 + v0.4: Bergman integral for hydrogen 1s electron is:

  ψ_{1s}(z) = c_FK · ∫_{S⁴ × S¹} (1 - ⟨z, w̄⟩)^(-7/2) · V_(1/2, 1/2)(w̄) · exp(-i α / r(w̄)) dμ(w̄)

v0.5 explicit evaluation via steepest descent + Hua-coordinate projection.

## 2. Explicit evaluation steps

### 2.1 Saddle point identification

Bergman exponent (-7/2) at boundary distance Δ → 0: dominant saddle at boundary ⟨z, w̄⟩ → 1.

Phase from substrate-Coulomb: phase(w̄) = -α/r(w̄); contributes Δ-r relation via Hua-coord mapping.

Saddle point w̄_* satisfies:
  ∂/∂w̄ [phase(w̄) - (7/2) · ln(1 - ⟨z, w̄⟩)] = 0

### 2.2 Steepest descent expansion

At saddle: 
  ψ_{1s}(z) ≈ (1/sqrt(det Hessian)) · exp[phase(w̄_*) - (7/2) · ln(1 - ⟨z, w̄_*⟩)]

Leading term: ψ_{1s} ∝ exp(-α · scale/r) for atomic-scale r >> L_K substrate-tick.

### 2.3 Compare to hydrogen 1s observed

Observed: ψ_{1s}(r) = (1/√(πa_0³)) · e^(-r/a_0)

Match: exp(-α · scale/r) vs e^(-r/a_0) requires α · scale = r²/a_0 — gives decay structure WRONG (1/r decay vs linear-r decay in exponent).

**Honest finding**: simple saddle-point asymptotic doesn't directly reproduce e^(-r/a_0). The "atomic scale" of hydrogen 1s requires more careful Hua-coord projection.

### 2.4 Refined analysis (multi-week)

Multi-week explicit work:
- Proper Hua-coord 3D-projection map π: D_IV⁵ → ℝ³
- Substrate-natural length scale (Bohr radius a_0 emerges from substrate-mechanism)
- Loop corrections via Hall algebra substrate-mechanism
- Comparison to standard QM hydrogen 1s

## 3. Elie Toy 3562 pre-pass spec

For Elie's Toy 3562 Bergman harness:
- Verify Bergman integral form (Section 2 setup)
- Numerical saddle-point evaluation at small substrate parameters
- Compare to standard QM hydrogen 1s at far-field

## 4. Honest scope

**What's READY**:
- v0.3 + v0.4 framework foundations
- Bergman integral setup explicit
- Steepest descent methodology

**What's FRAMEWORK in v0.5**:
- Explicit saddle-point setup
- Asymptotic decay structure

**What's INTERPRETIVE / OPEN**:
- Match to standard hydrogen 1s exponential decay requires multi-week Hua-coord 3D-projection refinement
- Bohr radius a_0 substrate-mechanism emergence

Cal #29 STANDING risk-flag preserved — must NOT back-fit; multi-week explicit derivation gates substantive content.

— Lyra, Track BC v0.5 hydrogen 1s explicit Bergman integral evaluation v0.1 filed Wednesday 2026-05-27 ~11:08 EDT. FRAMEWORK. Multi-week refinement gates substantive content; partially unblocks Elie Toy 3562.
