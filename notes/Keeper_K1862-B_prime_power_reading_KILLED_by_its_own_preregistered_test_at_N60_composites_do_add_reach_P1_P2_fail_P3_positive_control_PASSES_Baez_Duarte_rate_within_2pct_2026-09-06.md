# K1862-B — the "composites add no reach" reading is KILLED by its own pre-registered test at N = 60; the instrument is validated (Báez-Duarte's rate reproduced within 2 %)

**Keeper, 2026-09-06 09:05 EDT, clock-verified. Amends K1862 Sections B and G. Run by Keeper, solo, on Casey's word ("then prime-power"); Elie's independent run remains owed.**

## Instrument
d_N² = dist²(χ, span{ {x/k} : k ≤ N }) in L²((0,∞), dx/x²), N ≤ 60. Gram entries and the target vector integrated **exactly piecewise** between breakpoints (on each piece the integrand is 1/(km) − (a/m + b/k)/x + ab/x², closed form), cutoff X = 2×10⁵, tail from the Franel mean ∫₀¹{kt}{mt}dt = ¼ + gcd(k,m)²/(12km). Controls: ‖{x}‖² = 1.260661 = log 2π − γ ✓; ⟨χ,{x}⟩ = 0.422784 = 1 − γ ✓. One sign error in the target vector caught by the control before any number was read (first run gave ⟨χ,{x}⟩ = 23.99; fixed; rerun).

## Results against the pre-registration (K1862 G)
- **P3 (positive control): PASS.** d₆₀² · log 60 = 0.0470 vs Báez-Duarte's conjectured C = Σ_ρ 1/|ρ|² = 0.0462 — ratio 1.02. The instrument sees the criterion's asymptotics at N = 60.
- **P1: FAIL** (kill fires as written). Composites with ≥ 2 distinct primes DO add reach: Δ₁₄ = 1.3×10⁻³ exceeds Δ₁₃ = 6.2×10⁻⁴; Δ₃₃ = 5.5×10⁻⁴ exceeds Δ₃₁ = 5.9×10⁻⁷ by three orders. 28 failures of 30 eligible k.
- **P2: FAIL.** Prime-power increments are nonzero but not monotone in the exponent (Δ₈ = 1.4×10⁻⁴ < Δ₁₆ = 4.4×10⁻⁴ < Δ₃₂ = 4.8×10⁻⁴).
- The N ≤ 8 pattern of K1862 B (drops only at prime powers) was a small-N accident. **The reading "the composites add no reach; the primes do" is DEAD.** Casey's sentence survives as the theorem it always was (an off-line zero is a vector orthogonal to the reach of multiplication); it does not survive as a statement about which k contribute.

| k | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 11 | 13 | 14 | 31 | 33 | 60 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Δ_k ×10⁴ | 5682 | 1961 | 287 | 290 | 1.2 | 117 | 1.4 | 33 | 6.2 | 13 | 0.006 | 5.5 | 0.13 |

## Lesson (filed)
An observation at N = 8 with a clean arithmetic gloss is exactly the object `feedback_no_wave_through_on_a_perfect_number` exists for. It was pre-registered as can-fail before the run, and it failed. Cost: 20 minutes. The instrument survives and is the right one for Elie's independent run (N ≤ 500 with the exact Vasyunin Gram formula would also test the rate constant).

Retained instrument: `notes/Keeper_K1862-B_primepower_gram_instrument_2026-09-06.py` (1.5 s).
