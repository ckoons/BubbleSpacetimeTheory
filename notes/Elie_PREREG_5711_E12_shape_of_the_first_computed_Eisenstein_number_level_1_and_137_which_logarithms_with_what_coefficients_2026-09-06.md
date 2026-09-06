# PRE-REGISTRATION — Toy 5711, E12 (Round 124): the SHAPE of the first computed Eisenstein number, hashed before L12 names h

**Elie, 2026-09-06 (Sunday) 16:37 EDT (shell-copied). Hashed before any run and before Lyra's L12 (the rule-fixed h) is posted; the numbers follow when h is named. Warning carried: the comb's poles at Re λ = −½ are the Steinberg parameter's ½, not the critical line's; on the unitary axis the comb enters only through the bounded periodic term (D).**

## The object (T2621's c(w₀,λ), L8's schematic E₀[h])
E₀[h] = −(1/(2π)²)(1/|W|) ∫_{i𝔞*} Σ_{w∈W} ∂ log c(w,λ) h(λ) dλ, |W| = 8, c(w,λ) = Π_{β>0, wβ<0} c_β(λ), ∂ := ∂_{λ₁} + ∂_{λ₂} (the diagonal direction, the one L8 P1 used; any other admissible ∂ changes only the (A)/(B)/(D) integrals, not which logarithms appear). h even under W, ∫h := ∫_{ℝ²} h.

## Hashed shape — level 1
E₀[h] = −(1/4π²)·[ **ln 2 · ∫h** + J_A[h] + J_B[h] + J_D[h] ], where
- **ln 2 · ∫h** is the ONLY constant-coefficient logarithm: each short root e_i is inverted by 4 of the 8 Weyl elements and carries ∂ log ε_{e_i}^{−1} = ln 2, so (1/8)Σ_w = (4+4)/8 · ln 2 = ln 2 per unit ∫h (this is E10's 2 ln 2 on the diagonal, halved by the Weyl average, and it is the FE-normalisation constant of E11's finding);
- J_A[h] = ∫ h · Σ(ψ-terms): values ψ(λ_i+½), ψ(λ_i+3/2), ψ((λ₁±λ₂)/2 + …) — NO ln 2·∫h term hides here (the ln 2 inside ψ(½) is a VALUE at λ = 0, not a coefficient of ∫h; J_A is a genuine functional of h);
- J_B[h] = ∫ h · Σ(−ζ′/ζ at the four shifts) = the explicit-formula prime sums against ĥ: every prime, ln p weighted by p^{−k·shift}; ln 2 appears here as a prime among all;
- J_D[h] = ∫ h · Σ(comb terms), bounded, periodic with period 2π/ln 2 in Im λ_i.
Long roots contribute to J_A, J_B only (no ε, no comb).

## Hashed shape — level 137 (Γ(137))
The constant term is block-diagonal by (χ₁,χ₂) ∈ characters of (ℤ/137)^{×2}; for a block with a nontrivial primitive character on a factor, the ξ-ratio becomes ξ(·,χ)/ξ(·+1,χ) with ξ(s,χ) = (137/π)^{(s+a)/2}Γ((s+a)/2)L(s,χ), whose ∂ log carries the constant **−½ ln 137** (E10 H3) — and the ε-factors of the L(s,χ) FE are root numbers of modulus 1 (no λ-dependence, no logarithm). So
E₀^{(137)}[h] = −(1/4π²)·[ ln 2·c₂·∫h **+ ln 137·c₁₃₇·∫h** + J_A + J_B + J_D + J_E ], with **c₁₃₇ = −½ × (number of twisted ξ-ratios per block, Weyl-averaged, summed over the 136² − 1 nontrivial blocks)/(total blocks)** — a combinatorial coefficient I will compute from the block structure of L1 §4a, and c₂ possibly modified at the blocks where the Steinberg factor at 2 meets the character (reported, not predicted). J_E = the new L′/L(·,χ) prime sums (ln p for every p ≠ 137, twisted by χ(p)).
**Hashed claims:** (i) exactly two constant-coefficient logarithms at level 137, ln 2 and ln 137; (ii) no ln 137 at level 1; (iii) the ln 137 coefficient is negative (−½ per twisted ratio); (iv) with a heat-kernel h(λ) = e^{−t|λ|²}, ∫h = π/t, and every J is a convergent integral I evaluate numerically at the stated t.

Score X/4 on (i)–(iv) once L12 names h. The numbers are posted with ∫h and never compared to −3.4205.
