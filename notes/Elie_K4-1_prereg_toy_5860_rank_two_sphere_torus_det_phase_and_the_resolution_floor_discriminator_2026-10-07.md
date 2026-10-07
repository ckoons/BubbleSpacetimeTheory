# Elie — PREREG toy 5860 (Round K4-1, Lane B). Wed 2026-10-07 14:34 EDT (header said 14:36 at 9d1d29f3; `date` read 14:34; predictions untouched). Written BEFORE any code.
didwe ("rank two subdomain torus Shilov compact dual quadric"; "flat connection holonomy torus sphere interference") → 0 hits each. Builds on 5776 (09-22: region-count floor 1/√N, time-independent, vs Oppenheim; does not fire). Cal S1031 read (lines 12, 31, 33, 37) before writing; no lane output read.

## 1. Rank two (exact, symbolic)
- R1 so(2,2) splits into two commuting 3-dim ideals, each ≅ sl(2,ℝ): Killing signature (2,1) on each. D_IV² ≅ H × H.
- R2 The Lie ball at n = 2 is the bidisc EXACTLY: with w± = z₁ ± i z₂, |z|² + √(|z|⁴ − |z·z|²) = max(|w₊|², |w₋|²).
- R3 Šilov(D_IV²) = {e^{iθ}x : x ∈ S¹} maps 2:1 onto T² = {|w₊| = |w₋| = 1}; the deck (x, θ) ↦ (−x, θ + π) has degree +1 on S¹, so the quotient is a TORUS (not a Klein bottle).
- R4 Compact dual Q² ⊂ ℂP³ ≅ ℂP¹ × ℂP¹ = S² × S² (Segre map lands on the quadric and is injective).
- R5 For n = 3..7, the coordinate copy D_IV² ⊂ D_IV^n is the fixed set of an isometry (hence totally geodesic) and Šilov(D_IV^n) ∩ ℂ² = Šilov(D_IV²) = T². Prediction: GENERIC, "allowed, not forced by n = 5". Also: Šilov(D_IV^n) contains an embedded S² (inside the S^{n−1} fibre at fixed θ) iff n ≥ 3. So 2-spheres are not only on the compact-dual side.

## 2. The determinant phase on Λ³V₁ (V₁ = ℂ³, J = multiplication by e^{iθ})
- D1 Positive control (Keeper's six): signed σ ↦ sgn(σ)P_σ preserves ε for all 6; bare P_σ preserves ε only on A₃.
- D2 J acts on Λ³V₁ by e^{3iθ}; a bare odd reorder acts by −1 = J at θ = π/3. The read-order sign is J-invariant ONLY for θ ∈ (2π/3)ℤ = the centre ℤ₃ of SU(3). The full circle carries a triple continuously into its reverse.
- D3 J ↦ −J (complex conjugation) does NOT exchange the two orientation classes (the sign −1 is real). **Prediction: the one circle CARRIES the parity (det = sgn, and J surjects onto det with degree 3); it does not FIX which read order is positive.** The orientation is visible only as a relative phase against a reference (cf. Cal S1031 item 7).
- D4 On the record ρ = TT†, both the sign and the J-phase vanish.
- D5 Null: on Λ^k, k = 2, 4, 5, the odd sign = J at θ = π/k. Nothing in the circle selects 3.

## 3. Discriminator (09-15), extending 5776
- Q1 Rounding floor (step Δ): error bounded by Δ/2, variance Δ²/12 independent of T, kurtosis 9/5, deterministic in the signal. CQ diffusion: Var = 2DT, kurtosis 3, independent of the signal. 5776's counting floor is T-independent but Gaussian at large N. **So the robust discriminator is accumulation (slope in T), not Gaussianity.** Seeded simulation agrees with the exact moments.
- Q2 Preparation uncertainty: the rounding model admits states with σ_x = σ_p = 0, so it FAILS to reproduce Heisenberg. A finite Fourier ledger on ℤ_N passes: Donoho–Stark |supp f|·|supp f̂| ≥ N, checked exhaustively at small N and on a random sample at larger N, with equality on subgroup indicators (the positive control). Verdict: a resolution limit reproduces preparation uncertainty only if the conjugate variable is the Fourier dual on the same discrete ledger; then the Fourier relation is inherited, not derived.
- Q3 Flat U(1) connections. On the tetrahedron surface (K4, genus 0), b₁ = 0, so every flat connection is pure gauge and every two-path relative phase is 1. On a 3×3 torus triangulation (9 vertices, 27 edges, 18 faces; chosen to avoid 7), b₁ = 2, with two free holonomies, and the fringe |1 + e^{iφ}|²/4 sweeps 0..1. With curvature (face flux) the sphere does interfere, with total flux in 2πℤ. **So "the sphere record cannot" holds for FLAT (field-free) instruction phases only.**
