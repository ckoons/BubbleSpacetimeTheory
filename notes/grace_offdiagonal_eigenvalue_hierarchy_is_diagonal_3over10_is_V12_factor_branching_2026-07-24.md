# Off-diagonal eigenvalue structure + the 3/10 V₁₂-factor: hierarchy is diagonal, off-diagonal is mixing (two attacks agree)

*Grace | 2026-07-24 Fri | my upgraded assignment (Keeper): (1) build the 3×3 F585 mass matrix in the Wallach-strata basis with the V₁₂ off-diagonal, compute eigenvalues, answer Casey's off-diagonal question (hierarchy vs mixing) from the eigenvalue side — complementary to Lyra's diagonal width; (2) the D_IV⁵↓D_IV³ branching — does the reduction coefficient give 3/10 = N_c/(2n_C)? Sourced from F585 + K865 + the c-function branching rule, not memory.*

## Setup (sourced)
- **F585** (Lyra): M_ij = ⟨ψ_i|O|ψ_j⟩, ψ_i localized at support stratum i, O = single **rank-1** Higgs condensate → M_ij = O_i O_j. Diagonal = masses (localization width w_i); off-diagonal = mixing.
- **K865** (Keeper): the off-diagonal is the Peirce **V₁₂** (dim = n−2 = N_c = 3, the color space; T2511/F157), the ½-eigenspace of the idempotent. 2×2 block [[λ₁, v],[v*, λ₂]], eigenvalues **λ± = (λ₁+λ₂)/2 ± √(((λ₁−λ₂)/2)² + |v|²)**.

## ★ Computation 1 — off-diagonal feeds MIXING, not independent hierarchy (answers Casey; agrees with Lyra)
The key is whether v is **locked** to the diagonal (rank-1 Gatto) or **independent**:
- **Rank-1 Gatto (F585): v = √(λ_i λ_j).** Then [[λ_e, √(λ_e λ_μ)],[√(λ_e λ_μ), λ_μ]] is **rank-1** → eigenvalues **{λ_e+λ_μ, 0}** — one massive, one **texture-zero**, with mixing **θ = arctan√(λ_e/λ_μ) = √(mass ratio)** (Gatto). The off-diagonal does **not** add hierarchy; it **converts** the diagonal width hierarchy into (one massive + a texture zero) + the √-ratio mixing.
- **Independent v (< √product):** lifts the light eigenvalue off zero — perturbs, doesn't set, the hierarchy.

**Answer to Casey's off-diagonal question:** in the rank-1 condensate, v is locked to the diagonal, so **the mass HIERARCHY lives in the DIAGONAL localization widths** (Lyra's lane), and the off-diagonal **V₁₂ sets MIXING (+ the texture zeros), not independent hierarchy.** ⟹ **the two attacks AGREE** — Lyra's diagonal width and my off-diagonal eigenvalues both put the hierarchy in the widths. That convergence is the check Keeper asked for, and it passes.

## ★ Computation 2a — 3/10 = N_c/(2n_C) IS a V₁₂ factor (doubly), my assigned check
3/10 = **(½)·(N_c/n_C)** = **(Peirce off-diagonal EIGENVALUE ½) × (V₁₂ dimensional FRACTION N_c/n_C)**. Both factors are the V₁₂/off-diagonal characteristics from K865 (½-eigenspace; dim N_c). So the answer is **YES — 3/10 is the product of the two V₁₂ off-diagonal invariants.** Target-innocent structural read.

## Computation 2b — the branching D_IV⁵↓D_IV³ route to 3/10
3/10 = **dim(D_IV³)/(2·dim(D_IV⁵))** = **child/(2·parent)** = N_c/(2n_C) — dimensionally natural for the reduction, the "2" being the rank/Peirce-½ normalization. **Three consistent routes** to 3/10 (K865 eigenvalue×fraction; branching child/(2·parent); Casey N_c/(2n_C)), all V₁₂/branching-grounded (N_c = dim V₁₂ = dim D_IV³). Over-determined the good way. **Honest flag:** the exact branching **measure** must *return* the factor 2 (the Peirce/rank normalization) for this to be forced, not just a dimensional match — the c-function branching (B[k][j]=k−j+1) evaluated at the Wallach point k₁ is the pin. Candidate, sourced-routes-agree, not yet forced-from-the-measure.

## Net (for the team)
- **Casey's off-diagonal question, eigenvalue side: off-diagonal V₁₂ = MIXING (+ texture zeros); the hierarchy is DIAGONAL.** Agrees with Lyra's diagonal-width attack — the two pictures converge on the widths.
- **3/10 = N_c/(2n_C) is a V₁₂ factor** = (½)·(N_c/n_C), doubly grounded in the off-diagonal invariants. Three routes agree.
- **The muon hierarchy therefore lives in Lyra's diagonal localization width** — so W0/W2 (is the width a genuinely new, exponential-capable object returning 3/10, not the 6th reframe) is the load-bearing test, and my eigenvalue result confirms the width is the right place to look.

— Grace, 2026-07-24. Off-diagonal eigenvalue analysis (F585+K865): rank-1 Gatto → off-diagonal V₁₂ LOCKED to diagonal → matrix rank-1 → off-diagonal sets MIXING (θ=√ratio) + texture zeros, NOT independent hierarchy; HIERARCHY is DIAGONAL (localization widths) — agrees with Lyra's attack. 3/10=N_c/(2n_C) is a V₁₂ factor = (½ Peirce eigenvalue)·(N_c/n_C off-diag fraction), doubly grounded (K865); branching route 3/10 = dim(D_IV³)/(2 dim D_IV⁵) = child/(2 parent); 3 routes agree, over-determined; the factor-2 needs the branching measure to be forced. Hierarchy lives in the diagonal width → W0/W2 (width new-object test) is load-bearing.

## ★★ RETRACTION (same morning) — I read my own eigenvalue result BACKWARDS. The light hierarchy is OFF-DIAGONAL.
Keeper caught it (K868) and he's right; owning it promptly. My eigenvalue COMPUTATION was correct — rank-1 Gatto → {heavy, 0}. But my CONCLUSION ("hierarchy is diagonal, two attacks agree") was exactly backwards:
- The rank-1 matrix forces eigenvalues {heavy, **0**} *regardless* of the diagonal width ratio. So the diagonal widths are NOT the physical masses — the light generation is **massless from the diagonal alone**. The texture-zero I correctly computed **IS** the massless light state that the OFF-DIAGONAL must lift.
- ⟹ the **light-generation hierarchy is OFF-DIAGONAL** (seesaw m_μ ≈ V_μτ²/m_τ), exactly Lyra's F677 and Casey's instinct. I claimed "convergence with Lyra" while concluding the OPPOSITE of her correct read — that was a supersession dressed as agreement. **Retracted.**
- **Corrected picture:** single rank-1 condensate → ONE mass (tau ≈ trace); muon & electron get mass from the off-diagonal inter-stratum overlap (a seesaw cascade down the Wallach strata). The muon is my **off-diagonal / overlap lane**, not a diagonal width.
- **My self-pattern (2 days):** computations sound, interpretations over-reach ({5,3,0} "no geometry" yesterday; "hierarchy diagonal" today). Fix: report what the numbers show, stop narrating past them.

**What SURVIVES from the morning:** (a) 3/10 = N_c/(2n_C) is a V₁₂ factor (½·(N_c/n_C), three routes) — that stands, and it lands in the **charged-lepton off-diagonal** block (Keeper K868: hold it ≠ the neutrino sin²θ₁₂, the 63× tension — which I do). (b) The redirected gate: compute **V_μτ = ⟨ψ_μ|O|ψ_τ⟩** from the Wallach-stratum overlap — does it = √(m_μ m_τ) with NO fit? The Gatto geometric-mean form is target-AWARE (fit to masses); the overlap-from-geometry is the derivation.
