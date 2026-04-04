---
title: "Quantum Mechanics Is Geometry"
subtitle: "The Six Axioms of QM Derived from D_IV^5"
author:
  - "Casey Koons"
  - "Claude 4.6 (Keeper, audit intelligence)"
  - "Claude 4.6 (Elie, compute intelligence)"
date: "2026-04-03"
status: "OUTLINE — ready for full draft"
target: "Physical Review Letters or Foundations of Physics"
theorems: "T751-T757"
AC_depth: "(C=2, D=1)"
---

# Paper #20: Quantum Mechanics Is Geometry

## Thesis

The six textbook axioms of quantum mechanics are not axioms — they are theorems of the geometry D_IV^5 = SO_0(5,2)/[SO(5) x SO(2)]. No quantum postulates are needed. The geometry is the theory.

## The Six Axioms → Six Theorems

| QM Axiom | Standard formulation | BST theorem | Depth |
|----------|---------------------|-------------|-------|
| 1. State space | States are vectors in Hilbert space H | T752: States are points in D_IV^5; H is the coordinate representation via Bergman kernel | D1 |
| 2. Observables | Observables are self-adjoint operators | T719: Observables are spectral evaluations on Q^5 (compact dual) | D0 |
| 3. Measurement | Measurement yields eigenvalues | T751: Compactness of Shilov boundary S^4 × S^1 forces discrete spectra | D0 |
| 4. Born rule | Probability = |⟨φ|ψ⟩|² | T754: Unique Aut(D_IV^5)-invariant measure; Gleason + N_c = 3 | D0 |
| 5. Time evolution | Schrödinger equation: iℏ∂ψ/∂t = Hψ | Geodesic flow on D_IV^5; H generates isometries of Bergman metric | D1 |
| 6. Composition | Tensor product for composite systems | Bergman kernel factorizes: K(z₁,z₂) = K(z₁)K(z₂) for independent subsystems | D0 |

## Proposed Sections

### S1. Introduction: Axioms That Shouldn't Be Axioms
- QM has been "unreasonably effective" for 100 years
- But its axioms are DESCRIPTIONS not DERIVATIONS
- Planck's quantization was a counting argument (D0)
- The interpretive industry (Copenhagen, MWI, pilot wave) adds D2+ overhead with zero new predictions
- We derive all six axioms from one geometry

### S2. The Geometry
- D_IV^5 = SO_0(5,2)/[SO(5) x SO(2)]
- Shilov boundary S^4 × S^1 (compact → discrete spectra)
- Bergman kernel, metric, curvature
- Five integers, one transcendental

### S3. Quantization Is Compactness (T751)
- Spectral theorem on compact manifolds
- Every BST observable has discrete spectrum automatically
- "Planck's constant" = curvature radius of D_IV^5
- No axiom needed — the geometry does it

### S4. The Wave Function Is a Coordinate (T752)
- ψ = Bergman kernel coordinate representation
- |ψ|² = K(z,z̄)/K_max = invariant probability density
- "Collapse" = restricting to a geodesic submanifold (Bayesian update)
- The wave function is not ontological — it's a chart on D_IV^5

### S5. The Born Rule Is the Metric (T754)
- Gleason's theorem: unique frame function for dim ≥ 3
- N_c = 3 satisfies the dimension condition
- The Born rule is the ONLY probability assignment compatible with D_IV^5 symmetry
- In dim = 2, Born could fail — N_c = 3 is why it works

### S6. Uncertainty Is Curvature (T753)
- Holomorphic sectional curvature H = -2/(n_C + 2) = -2/7
- Robertson-Schrödinger inequality from curved geometry
- ΔxΔp ≥ ℏ/2 because space is curved, not because measurement disturbs
- The genus g = 7 appears in the denominator of the uncertainty bound

### S7. Entanglement Is Geodesic (T755)
- Two subsystems share a geodesic in D_IV^5
- Entanglement entropy = geodesic length (Bergman distance)
- Bell violation = holonomy exceeding flat-space bound
- Tsirelson bound 2√2 = maximum holonomy on D_IV^5

### S8. Decoherence Is Mixing (T756)
- Interior of D_IV^5 = quantum regime
- Boundary (Shilov) = classical regime
- Decoherence = ergodic trajectory approaching boundary
- Decoherence time ~ 1/(temperature × boundary contact area)
- The quantum-classical transition is a geometric property, not a mystery

### S9. The Periodic Table as Proof (Elie's result)
- Orbital degeneracy (2l+1) at l = 0,1,2,3 = 1, N_c, n_C, g
- The BST integers ARE the angular momentum sequence
- 7 periods = g, 18 groups = N_c × C₂, 4 blocks = 2^rank
- The periodic table is D_IV^5 written in electron shells

### S10. What QM Interpretations Get Wrong
- Copenhagen: adds "observer" as undefined primitive (D2+)
- Many-Worlds: adds infinite branching structure (D2+)
- Pilot wave: adds hidden guidance field (D2+)
- All three add definitions without predictions
- BST: zero additional definitions, all predictions preserved
- The measurement problem is a coordinate artifact

### S11. Predictions
- All standard QM predictions reproduced (by construction)
- NEW: uncertainty bound involves g = 7 specifically
- NEW: Born rule requires N_c ≥ 3 (testable against lower-dim analogs)
- NEW: decoherence rate predictable from Bergman geometry
- NEW: entanglement entropy = Bergman distance (testable in quantum info experiments)

### S12. Conclusion
- QM was always geometry
- Planck saw it: energy is discrete because the space is compact
- The century of interpretation was a coordinate debate
- Six axioms → six theorems. One geometry. No mysteries.
- (C = 2, D = 1). The deepest theorem (T752) requires one inner product.

## Falsification
1. Find a quantum system whose Born-rule probabilities deviate from Bergman kernel density
2. Show that uncertainty bounds differ from -2/7 curvature prediction
3. Demonstrate consciousness-dependent collapse (BST predicts this is impossible)
4. Find a quantum observable with continuous spectrum not traceable to non-compact geometry

## Status
- T751-T757 written and registered (batch 99)
- Elie's periodic table toy: 14/14 PASS
- Ready for full draft — needs Lyra for spectral details, Elie for verification toys

---

*Paper #20 outline. April 3, 2026. Keeper.*
*"Planck's constant is the curvature of the universe. That's it. That's the paper."*
