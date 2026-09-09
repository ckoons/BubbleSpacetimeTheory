# PRE-REGISTRATION — Toy 5747, Round 138 LANE B (E2, E3). Hashed before the run.

**Elie, 2026-09-09 (Wednesday) 11:23 EDT (shell-copied).**

## E2 — the write tuple is a resolution of the identity on H²(Š), verified by integration
Effects E_u = M_{z_u}*M_{z_u}, u = 1..5. On Š, Σ_u |z_u|² = |z|² = 1, so Σ_u E_u = I.
- **P1 (can fail):** for the words (z·z)^j Y_k with Y_k = harm(x₁^k) and with random integer harmonics, k = 0..5, j = 0..3, **Σ_u ‖z_uψ‖²_H / ‖ψ‖²_H = 1 EXACTLY** (exact S⁴ moments, rationals — not machine precision, exact).
- **P2 (the five-outcome law, hashed):** the outcomes are NOT uniform for a zonal word. For Y_k zonal along e₁, p₁ = ⟨x₁²⟩ under |Y_k|² and p₂ = … = p₅ by symmetry. **Hashed: p₁ = (k+1)/(2k+3) ... reported exactly; at k = 0, p_u = 1/5 for all u (the vacuum is isotropic, so the five writes are equiprobable and 1/5 here is the ISOTROPY of the vacuum, not the retired push-cost number — the collision is named before it is read).**
- **P3 (the branching, from the POVM and not from a table):** splitting each outcome by Hua component, Σ_u ‖P_light z_uψ‖²_H/‖ψ‖² = **(k+3)/(2k+3)** and Σ_u ‖P_matter z_uψ‖²_H/‖ψ‖² = **k/(2k+3)**, exactly, for zonal AND random harmonics, k = 0..5. **These are K1860-A's branching probabilities, obtained here as Born probabilities of the write tuple's own resolution — no effect chosen, no observable imported.**
- **P4 (positive control, must FAIL to sum to one):** the same sum at the Bergman weight gives Σ_u ‖z_uψ‖²_{A²}/‖ψ‖²_{A²} = 1 − c(j,k), deficit **exactly** my 5735 closed form — the defect of the row isometry, closing the loop with Rounds 134–137.

## E3 — the three-write word 3/7 from Born probabilities alone
Chain the P3 weights (each computed by integration, none read from a table): from the vacuum, write 1 is forced to light; write 2 gives matter with 1/5; write 3 gives matter from (0,2) with 2/7.
- **P5 (hashed):** P(state = (1,1) after exactly three writes) = 1/5 + (4/5)(2/7) = **3/7**, exact, with **no branching-table input anywhere in the computation**. If it lands, **the signature fraction 3/7 is a Born probability of the write tuple's own resolution of the identity.**
- **Trap named before reading:** 3/7 is already three objects in this corpus (the d = 5 three-write probability; the d = 3 dipole weight l/(2l+1) at l = 3; the cell (0,5) of the push-cost table). This computation speaks only to the first.

Score X/5; P1, P3, P5 can fail.
