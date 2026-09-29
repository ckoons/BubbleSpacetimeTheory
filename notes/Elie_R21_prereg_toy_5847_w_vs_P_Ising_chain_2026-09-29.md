# Elie — round 21 PREREG, toy 5847: an interacting model separating the clock label from the action ℤ₂ — 2026-09-29 12:09 EDT, before any code
Antecedent (K1941 Part 2, verbatim): "In a model with a deformed fusion … show that the w-type label (e^{2πiΔ} mod 1, multiplicative) FAILS under the operator product, while the action ℤ₂ (P-type) holds. Control: a free theory, where both hold."
Group and sources (stated before use): the model is the critical transverse-field Ising chain H = −Σ σᶻᵢσᶻᵢ₊₁ − Σ σˣᵢ on a ring of L sites (no remembered CFT numbers used). Its ℤ₂ is Q = ∏σˣᵢ. It is solved EXACTLY by Jordan–Wigner: the Q = +1 sector is the antiperiodic (NS) fermion sector, and Q = −1 is periodic (R), each with the parity projection. The CFT (1+1D conformal group) supplies only the reading Δ = (E − E₀)·L/(2πv), with v measured from the dispersion (not assumed).
Checks:
(1) [H, Q] = 0 exactly (small-L exact diagonalisation, L = 8).
(2) Dimensions from exact finite-size gaps, extrapolated in 1/L²: Δ_σ = the lowest Q-odd level; Δ_ε = the lowest Q-even excited level with zero momentum; Δ_ψ = the single-fermion level (free-field control).
(3) Fusion at lattice level: σᶻᵢσᶻᵢ₊₁ (the product of two Q-odd σ's) is a term of H, the energy density, so σ × σ ∋ ε. The Q-charge is multiplicative there: (−1)(−1) = +1 = Q(ε).
(4) The clock label c(O) = e^{2πiΔ_O}: is c(σ)² = c(ε)? DIRECTION: NO. Δ_σ → 1/8, Δ_ε → 1, so e^{iπ/2} ≠ 1: the w-type label FAILS under the (deformed) fusion, while Q (the action ℤ₂) holds exactly.
(5) CONTROL (free sector): ψ (Δ = 1/2) with ψ × ψ ∋ ε (the fermion bilinear, Δ = 1): c(ψ)² = e^{2πi} = c(ε), so the label IS multiplicative where the fusion is free.
KILL (for Keeper's reading 'w fails, P holds'): c(σ)² = c(ε) within the extrapolation error, or [H, Q] ≠ 0.
Scope, stated now: this is a stand-in (a 1+1D CFT), not BST. It shows the mechanism Lyra's (b) names: a clock phase does not multiply across an interacting fusion, while an action symmetry does. It does not decide which label BST's interacting theory has.
