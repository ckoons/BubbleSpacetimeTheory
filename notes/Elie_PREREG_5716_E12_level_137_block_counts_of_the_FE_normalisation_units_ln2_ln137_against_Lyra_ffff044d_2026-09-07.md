# PRE-REGISTRATION — Toy 5716, E12 at level 137 (Round 125 item 1a): the constant-coefficient part, block by block, against Lyra's hash ffff044d

**Elie, 2026-09-07 (Monday) 08:04 EDT (shell-copied). Hashed before the run. Convention: the one that survived 5714 — each rank-one factor L(x)/[ε(x)L(x+1)], ε(x,χ) = w(χ)N(χ)^{½−x}, ∂ = ∂₁+∂₂, Weyl average (1/8)Σ_w over inversion sets (5713's sets).**

## What is computed and what is not
COMPUTED: the σ = 1 sector's constant-coefficient logarithms — exact counts over the 136² blocks (ψ₁,ψ₂) of characters of 𝔽₁₃₇^× (as exponents mod 136), the per-block c₁₃₇ and the ln 2 unit, their sums, the distribution of c₁₃₇, and the resulting constant-coefficient piece −(1/4π²)[N₂ ln 2 + N₁₃₇ ln 137]·∫h at t = 1 and 2/17 with ∫h printed. NOT computed: the twisted functional pieces (ψ-, L′/L-, comb-integrals per block: 18,496 two-dimensional integrals with Dirichlet L-functions ≈ days of compute) and the σ ≠ 1 sector (needs the σ-decomposition of A(q₀;137)); both stated as owed, not estimated.

## Hashed lines
- **P1 (Weyl bookkeeping, control):** in 5713's eight inversion sets, e₁, e₂, e₁+e₂ each occur in exactly four, e₁−e₂ in four — Lyra's "four of eight" holds; (∂₁+∂₂) kills e₁−e₂ and gives weight 2 on e₁+e₂.
- **P2 (Lyra P2, exact enumeration):** c₁₃₇(ψ₁,ψ₂) = δ(ψ₁ψ₂) + δ(ψ₁²) + δ(ψ₁) + δ(ψ₂²) + δ(ψ₂) enumerated over all 136² blocks: sum **91,528**, block average 673/136 = 4.9485, value 0 at exactly one block (trivial), and the distribution of values 0…5 reported; the arithmetic identity Σ = 136·(135 + 2·134 + 2·135) exhibited. Kill: any block off the table.
- **P3 (Lyra P1):** ln 2 unit per block = 1 in the σ = 1 sector → N₂ = 136² = 18,496 (a convention statement under the FE normalisation; recorded, not "derived").
- **P4 (the number, constant-coefficient part only):** E_const^{(137)}[h_t] = −(1/4π²)(18,496 ln 2 + 91,528 ln 137)·∫h_t, printed with ∫h_t at t = 1 (6.392×10⁻⁴) and t = 2/17 (9.824); the ln 137 part exceeds the ln 2 part by the factor 91,528·ln 137/(18,496·ln 2) ≈ 35.1. Never compared to −3.4205.
- **P5 (Lyra P5):** no ln π, no prime other than 2 and 137 in any constant coefficient — by 5714 and by the conductor list of the row (only 2 and 137 are ramified anywhere); recorded.

Score X/5; P2 is the only line with content that can fail.
