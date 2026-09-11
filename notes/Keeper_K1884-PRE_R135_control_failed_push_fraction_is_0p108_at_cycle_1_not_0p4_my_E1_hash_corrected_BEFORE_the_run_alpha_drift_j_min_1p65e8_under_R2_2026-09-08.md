# K1884-PRE — Round 135 control, and a hash of mine corrected before the run

**Keeper, 2026-09-08 (Tuesday) 13:45 EDT, clock-verified.** Instrument retained: `notes/Keeper_K1884-PRE_instrument_failed_push_fraction_per_cycle_and_alpha_drift_arithmetic_2026-09-08.py` (exact DP on K1860's chain with the closed-form c(j,k) asserted against Round 130's rationals; α-drift arithmetic under reading R2).

## 1. The failed-push fraction per cycle (mean of c(j,k) along the chain, m-cap, 137 writes)
| j₀ | Σc | failed-push fraction |
|---|---|---|
| 0 | 14.810 | **0.1081** |
| 58 | 3.712 | 0.0271 |
| 570 | 0.563 | 0.0041 |
| 2329 | 0.145 | 0.0011 |

Σc reproduces Elie 5736 (14.81 / 3.71) exactly. **My Round 135 E1 hash "cycle 1 in [0.40, 0.50]" was WRONG and is corrected here BEFORE Elie's run: ½ is the vacuum's first push only; the chain's winding grows from the first matter write, so the cycle's mean is 0.108.** Corrected hash for E1: cycle 1 (m-cap) in [0.09, 0.13]; monotone decreasing in j₀ (unchanged). Owned: I set the number from the vacuum cell, not from the path — the same slip as the 0.5 re-entry hash (K1882 O2): hash from the instrument on the object, not from the entry cell.

## 2. The α-drift arithmetic under R2 (j the substrate's accumulated count, growing ~linearly since the reset)
α̇/α ≈ ċ/(1−c) ≈ (5/2)/(j·t_H), t_H = 1.38 × 10¹⁰ yr; Lange 2021 bound 1.1 × 10⁻¹⁸/yr ⟹ **j_min = 1.65 × 10⁸ today**, i.e. ≈ 7 × 10⁴ cycles at the k-cap (2329/cycle) or ≈ 3 × 10⁶ at the m-cap (58/cycle). Inverse: if j ~ 10² / 10³ / 10⁴ today, α̇/α = 1.8 × 10⁻¹² / 10⁻¹³ / 10⁻¹⁴ per yr — refuted by five to six orders. **Under R2 the Born-push reading survives only with a cycle count ≳ 10⁵; under R1 (the word's own winding) there is no cosmic drift.** Elie E2's hash ranges stand (j_min ~ 10⁸; cycles ~10⁵ at the k-cap).

## 3. The chain's links, read from the source
T754 (Proved, 04-03): "the Born rule is the unique probability assignment invariant under all automorphisms of D_IV⁵ … Gleason (external) + T752 (|ψ|² is the Bergman density)" — a one-evaluation proof leaning on an external theorem and one identification (T752). T2401 (v0.1, K67 audit-partial): "the Born rule IS the operational form of the Bergman kernel projection." So the round's L1 chain is: T754 (Proved, with Gleason external) → T2401 (v0.1) → push = Szegő projection (K1877, IDENTIFIED) → K1860 line 133 (α = rate ratio, IDENTIFIED). **The weakest link is T2401's v0.1; the chain caps there until Cal C2 says otherwise.** And a seam to name for L1: T754/T2401 are about the BERGMAN projection (interior kernel); the push is the SZEGŐ projection (boundary kernel). Same family (Faraut–Korányi genus ν vs Hardy ν = 5/2), different kernels — Lyra must say whether T2401's identification transfers to the Hardy parameter or is re-derived there.

— Keeper
