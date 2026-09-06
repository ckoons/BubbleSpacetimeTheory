# PRE-REGISTRATION — Toy 5710, E11 (Round 123): the kernel swap, scored by a DIRECT local computation

**Elie, 2026-09-06 (Sunday) 16:17 EDT (shell-copied). Hashed before the run. Holds: Lyra L10 (f550457f: comb 2π/ln 3, even k) and Cal §865 (077257f5: comb π/ln 3, all k). Cal's instruments not opened beyond the header; the integrand below is derived, not copied.**

## The object
Rank-one group SO(V), V = H ⊕ W, H = ℤ_p e ⊕ ℤ_p f with ⟨e,f⟩ = 1, (W, q₀) a ternary lattice. Minimal parabolic = stabiliser of ℚ_p e, N ≅ W via n(w): e ↦ e, x ↦ x − ⟨x,w⟩e, f ↦ f + w − ½q₀(w)e (an isometry). Spherical vector for K = Stab(L), L = H ⊕ W: F_λ(g) = ‖g^{−1}e‖_L^{−(λ+ρ)}, ρ = dim N / 2 = 3/2, ‖v‖_L = p^{−min val of L-coordinates}. With w₀: e ↔ f, the intertwining integral is
  **c_p(λ) = ∫_{ℚ_p³} max(1, |w|_p, |q₀(w)/2|_p)^{−(λ+3/2)} dw**, vol(ℤ_p³) = 1.
Shells: w = p^{−j}u, u primitive, |w| = p^j (j ≥ 1), measure p^{3j}(1 − p^{−3}); with i = v_p(q₀(u)) the height is p^{max(j, 2j−i)} (p odd, ½ a unit). P_i := fraction of primitive u ∈ ℤ_p³ with p^i | q₀(u), counted exactly mod p^k; for an anisotropic q₀ the P_i vanish from some i₀; for an isotropic q₀, P_{i+1} = P_i/p for i ≥ 1 (Hensel) and the tail is summed in closed form. So c_p is an exact rational function of 3^{−λ} computed with Fractions.
At p = 3 the corpus's planes ⟨1,−1⟩ ≅ H over ℤ₃ (2 a unit), so this is the corpus's lattice; the p = 2 odd-lattice case is NOT modelled here (½ ∉ ℤ₂; that is §855's territory) and is not scored.

## Hashed lines
- **P1 (controls, the instrument must pass before P2 is read):** for the split ternary q₀ = x² + y² − z² at p = 3, and for q₀ = x² + y² + 3z² at p = 5 (split there: (−1,−3)₅ = +1), c_p(λ) equals the Gindikin–Karpelevich split factor **(1 − p^{−2λ−1})(1 − p^{−λ−3/2}) / [(1 − p^{−2λ})(1 − p^{−λ+½})]** exactly as rational functions in p^{−λ}.
- **P2 (THE DECISIVE LINE):** for q₀ = x² + y² + 3z² at p = 3 (anisotropic: P₁ = 1/13, P₂ = 0), the correction factor R₃(λ) := c₃^{aniso}(λ)/c₃^{split}(λ) has a pole comb. **My prediction: spacing π/ln 3 = 2.8596, all k (Cal's hold), prior 65 %** — because every shell height is 3^{2j−i} with i ∈ {0, 1}, so the λ-dependence enters only through 3^{−2λ}, and the only geometric denominator is (1 − 3^{−2λ}); Lyra's 2π/ln 3 (even k only) requires an odd-k cancellation by a numerator factor (1 + 3^{c−λ}), which I will test by evaluating the numerator at 3^{λ} = −3^{c} for the candidate c. Whichever spacing the rational function shows is the finding; the pole positions (Re λ) are reported with it.
- **P3 (the constant):** the Steinberg-type constant, read as the large-Re λ behaviour of R₃: R₃(λ) → const·3^{a λ} with a reported; under Lyra's JL form a = 0 with ε = 3^{½−λ} absorbed elsewhere — reported, not predicted.

Score X/3. A P1 miss stops the toy: no P2 is read from an instrument that fails the split control.
