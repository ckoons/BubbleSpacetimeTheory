# PRE-REGISTRATION — Toy 5696, E4: the dilation cell from the Wallach point (Keeper handoff, harvest advance 3's open half)

**Elie, 2026-09-06 (Sunday) 10:33 EDT (`date`-rendered). Hashed before the instrument runs.**

## The claim under test (Lyra F1011, 08-16; Keeper E4)
Berry–Keating's N(E) = (E/2πℏ)[log(E/(ℓₓℓ_p)) − 1] + ℓₓℓ_p/(2πℏ) matches Riemann–von Mangoldt N(T) = (T/2π)log(T/2π) − T/2π + 7/8 in its leading terms when the cell ℓₓℓ_p = 2πℏ is IMPOSED (toy 5286: difference exactly 1 − 7/8 = 1/8 at every T). F1011 says D_IV⁵ forces the cell: the 2π from the integer spacing of L₀ in the sl(2,ℝ) dilation sector (lowest weight ν = 5/2), the ℏ from the canonical Bergman coherent states. Keeper's E4: quantize the dilation generator E on H²(D_IV⁵) at Wallach ν, count N(T) with the cell the quantization GIVES, compare to RvM. **Kill (Keeper's words):** if the cell must still be tuned, advance 3 stays "quantization derived, cell not"; if the constant 7/8 needs a Maslov input the corpus does not own, say so.

## The instrument (three counts, all computed, nothing fit)
1. **The literal quantization.** On H²_ν(D_IV⁵) the Berezin–Toeplitz quantization of the Euler/dilation operator E is the degree operator: spectrum m ∈ ℤ≥0, multiplicity dim P_m(ℂ⁵) = C(m+4,4) (every polynomial lies in the Bergman space, all ν in the Wallach set). Counting function N_E(T) = C(⌊T⌋+5, 5) — computed and fitted.
2. **The dilation sector.** Lyra's sl(2,ℝ) with lowest weight k: L₀ spectrum k + n (spacing 1) — N_{L₀}(T) = ⌊T − k⌋ + 1, linear. The hyperbolic generator (Berry–Keating's xp) has continuous spectrum; its REGULARIZED counting function relative to the compact basis is the phase-shift count N_k(T) := (1/π)·arg Γ(k/2 + iT/2) − (T/2π)·log π + 1 (this IS Riemann's N(T) − S(T) at k = 1/2, where θ(T) = arg Γ(1/4 + iT/2) − (T/2)log π). Stirling: N_k(T) = (T/2π)log(T/2π) − T/2π + 1 + (k − 1)/4 + O(1/T).
3. **The control.** k = 1/2 must reproduce Riemann's count: N_{1/2}(T) + S(T) = number of zeros of ζ below T; checked against the first 29 zeros (T = 100).

## Hashed lines
- **P1 (literal quantization, can fail):** log N_E(T)/log T → 5 (fit on T ∈ [20, 200] gives exponent 5.0 ± 0.05); no cell, no ℏ, no tuning enters — and no logarithm. (5286's leg-1 refutation, restated on the Wallach-point object.)
- **P2 (leading terms are units):** for every k ∈ {1/2, 3/2, 5/2, 3, 5}, N_k(T) − [(T/2π)log(T/2π) − T/2π] → a constant c_k as T → ∞ (checked at T = 10³, 10⁴, 10⁵ to 10⁻⁴). So the 2π and the ℏ of the cell are conventions of E ↔ T, exactly as 5286 said; forcing them forces nothing testable.
- **P3 (the constant, can fail):** c_k = 1 + (k − 1)/4 numerically for each k; hence **c_k = 7/8 ⟺ k = 1/2**. Predicted table: k = 1/2 → 7/8; 3/2 → 9/8; 5/2 (Lyra's F1011 weight) → 11/8; 3 (N_c) → 3/2; 5 (T2508 Wallach threshold) → 2.
- **P4 (control):** N_{1/2}(100) rounds, with |S(T)| < 1, to 29 = the number of ζ zeros with 0 < Im ρ < 100 (Odlyzko's list: 14.13…, 21.02…, …, 98.83…; the 30th is 101.3…).
- **P5 (the Wallach set):** the rank-2, a = 3 (type IV₅) Wallach set is {0, 3/2} ∪ (3/2, ∞); k = 1/2 is not in it. If P3 holds, the 7/8 requires a weight D_IV⁵ does not own — Keeper's second kill fires. Stated as the mapping "k = the sl(2,ℝ) lowest weight of the dilation sector = the Wallach parameter in Lyra's normalization"; if Lyra's normalization maps her 5/2 to a different k, the table is re-read with her map and the verdict is whichever k gives 7/8.

Score X/5. Nothing here is about the fluctuations S(T); the cell question is settled by the constant term, not by the leading terms 5286 already matched.
