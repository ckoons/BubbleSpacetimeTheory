# Toy 474: Linearized Trace Formula — Spectral Data from Geodesic Sums

**Assigned to**: Elie
**Spec by**: Lyra (for Casey)
**Date**: March 27, 2026
**Investigation**: I16 extension — trace formula as linearizer of quantum mechanics

---

## Motivation

The Selberg trace formula converts a NONLINEAR problem (find eigenvalues of the Laplacian) into a LINEAR one (sum known geometric coefficients over closed geodesics). Casey's insight: this is the AC(0) route to chemistry. Compute the geodesic table ONCE, then every spectral question is a linear lookup.

This toy demonstrates the principle on the simplest case: **SL(2,Z)\H** (the modular surface — rank 1, "hydrogen-like"). Then shows how D_IV^5 parameters extend it.

---

## What to Compute

### Part 1: The Geodesic Table for SL(2,Z)\H

Build the table of primitive closed geodesics on the modular surface.

Each primitive hyperbolic conjugacy class of SL(2,Z) has:
- **Trace**: t = Tr(A) for the conjugacy class representative A
- **Norm**: N(γ) = ((t + sqrt(t²-4))/2)² (square of the larger eigenvalue)
- **Length**: ℓ(γ) = log N(γ) = 2 arccosh(t/2)
- **Orbital integral weight**: determined by the centralizer

The first few primitive geodesics have traces t = 3, 4, 5, 6, 7, ... (t ≥ 3).

Enumerate all primitive geodesics with trace t ≤ 100 (or ℓ ≤ some cutoff). Store as a sorted table.

**Connection to primes**: For SL(2,Z), the prime geodesics are in bijection with equivalence classes of binary quadratic forms. The norm N(γ) plays the role of p^m in the prime sum.

### Part 2: Spectral Recovery from the Geodesic Table

The Selberg trace formula for SL(2,Z)\H with test function h(r):

```
Σ_n h(r_n) = (Area/4π) ∫ h(r) r tanh(πr) dr
           - Σ_{γ primitive} Σ_{m=1}^∞ ℓ(γ)/(2 sinh(m ℓ(γ)/2)) × ĥ(m ℓ(γ))
           + (elliptic terms from elements of order 2,3)
           + (parabolic/cusp terms)
```

where:
- {r_n} are spectral parameters: λ_n = 1/4 + r_n²
- ĥ(x) = (1/2π) ∫ h(r) e^{-irx} dr is the Fourier transform
- Area = π/3 for SL(2,Z)\H

**Key tests with specific test functions:**

**T1: Heat kernel** h(r) = e^{-t(r²+1/4)}
- Spectral side: Σ_n e^{-t λ_n} = heat trace K(t)
- Geodesic side: compute from table
- Verify they match for t = 0.1, 0.5, 1.0, 5.0
- Show that the geodesic sum CONVERGES to the spectral answer

**T2: Resolvent** h(r) = 1/(r² + s²) for s > 0
- Spectral side: Σ_n 1/(λ_n - 1/4 + s²) = Green's function at coincident points
- Geodesic side: compute from table
- This gives the PROPAGATOR — the thing you need for bond calculations

**T3: Characteristic function** h(r) = 1 if |r| < R, else 0
- Spectral side: counts eigenvalues below λ = 1/4 + R²
- Geodesic side: Weyl law with oscillatory corrections from geodesics
- Show: N(λ) = (Area/4π)λ - (oscillatory from geodesics)

**T4: Spectral recovery — find the eigenvalues**
- Use a peaked test function h_ν(r) = e^{-(r-ν)²/(2σ²)} for various ν
- Scan ν from 0 to 30
- The spectral side peaks at r = r_n (eigenvalues)
- The geodesic side gives the SAME peaks — without ever solving an eigenvalue problem!
- Plot or tabulate: recovered eigenvalues vs known eigenvalues of SL(2,Z)\H
- Known first few: r₁ ≈ 9.534 (λ₁ ≈ 91.14), r₂ ≈ 12.173, r₃ ≈ 13.780

### Part 3: Linearization Demonstration

**T5: The table IS the theory**
- Show that once the geodesic table is built (a list of (ℓ_γ, c_γ) pairs), every spectral question reduces to:
  ```
  answer = Σ_γ c_γ × f(ℓ_γ, parameters)
  ```
  where f depends on which question you're asking (heat kernel, resolvent, etc.)
- This is a LINEAR operation: dot product of the coefficient vector with a function vector
- Time complexity: O(number of geodesics) per query — no matrix diagonalization!

**T6: Comparison with "solving" the eigenvalue problem**
- Numerically solve the Laplacian eigenvalue problem on SL(2,Z)\H (standard Hejhal algorithm or use known tabulated values)
- Compare: time to solve eigenvalue problem vs time to evaluate geodesic sum
- The geodesic sum should be FASTER for individual spectral queries

### Part 4: BST Extension (Conceptual + Numerical Where Possible)

**T7: From SL(2,Z)\H to SO_0(5,2)/K**
- Write the STRUCTURE of the trace formula for SO_0(5,2):
  - Volume: π⁵/1920 (known)
  - Root system: B₂ with multiplicities m_s = N_c = 3, m_l = 1
  - Plancherel measure: |c(λ)|⁻² where c is the Harish-Chandra c-function
  - Geodesic sum: over conjugacy classes of Γ = SO(Q,Z)
- Show how the BST parameters {N_c=3, n_C=5, g=7, C₂=6, N_max=137} enter:
  - N_c: root multiplicity (controls orbital integral weights)
  - g: Bergman genus (controls Casimir eigenvalues)
  - N_max: spectral cutoff (controls the finest corrections)
  - Vol = π⁵/1920: the "area" that determines the Weyl law

**T8: Chemistry preview — hydrogen energy levels from BST**
- The hydrogen atom's energy levels E_n = -13.6/n² eV
- In the trace formula picture: these correspond to periodic orbits of the Kepler problem (Gutzwiller)
- The Kepler problem on D_IV^5 would give corrections from the curved geometry
- Show: the Bohr levels are depth 0 (counting), fine structure is depth 1 (one correction from curvature)
- This is AC(0) → AC(1) for atomic physics

---

## Expected Output

8 tests, target 8/8. Mix of numerical verification (T1-T4) and structural demonstration (T5-T8).

Key deliverables:
1. A geodesic table for SL(2,Z)\H (first ~50 primitive geodesics)
2. Numerical verification that the trace formula recovers eigenvalues from geodesics
3. Timing comparison showing linearization speedup
4. The BST extension framework (conceptual, with numerical where possible)

---

## BST Connection Summary

The trace formula linearizes quantum mechanics:
- **Nonlinear**: solve Δψ = λψ (eigenvalue problem, requires matrix diagonalization)
- **Linear**: sum c_γ × ĥ(ℓ_γ) over geodesic table (dot product, O(n) per query)

For chemistry: build the D_IV^5 geodesic table once. Every orbital, every bond, every energy level = linear lookup. AC(0) chemistry.

Casey's analogy: the trace formula does for QM what Fourier transform does for signal processing — converts a hard problem (deconvolution) into an easy one (multiplication).

---

## Notes for Elie

- The elliptic terms for SL(2,Z) come from elements of order 2 (trace 0) and order 3 (trace 1). These are finite sums, easy to compute.
- The parabolic/cusp term is a single contribution from the cusp at infinity. For SL(2,Z), it involves the scattering determinant φ(s) = ξ(2s-1)/ξ(2s).
- For the spectral recovery (T4), the first eigenvalue of SL(2,Z)\H is known: λ₁ ≈ 91.14 (r₁ ≈ 9.534). But recovering it from the geodesic sum is the whole point — show the method works WITHOUT knowing the eigenvalues in advance.
- Use mpmath for precision. 30 digits should suffice.
- File: `play/toy_474_linearized_trace.py`
