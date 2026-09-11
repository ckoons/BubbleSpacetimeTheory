# K1882-PRE — Round 133 control: the twirl on an irreducible H_k is the completely depolarizing channel; Choi rank d², eigenvalues 1/d

**Keeper, 2026-09-08 (Tuesday) 09:57 EDT, clock-verified.** Instrument retained: `notes/Keeper_K1882-PRE_instrument_Choi_rank_of_the_SO5_twirl_on_H1_H2_2026-09-08.py` (4,000 Haar SO(5) samples; H₁ = ℂ⁵ with the defining action; H₂ = traceless symmetric 5×5 with g M gᵀ, dim 14).

```
H_1: Choi rank 25  (expect 25);  singular values 0.175–0.229  (expect all 1/5 = 0.200)
H_2: Choi rank 196 (expect 196); singular values 0.044–0.107  (expect all 1/14 = 0.071)
```
Reading: the Choi matrix of ρ ↦ ∫ g ρ g† dg on an irreducible H_k of dimension d is I_d ⊗ I_d / d — full rank d², all eigenvalues 1/d (the spread above is Monte Carlo noise at 4,000 samples; rank is exact). So **the minimal Stinespring environment of the reset on one saturated block has dimension (dim H_k)²**: 25 at k = 1, 196 at k = 2, (111,895)² ≈ 1.25 × 10¹⁰ at k = 68, (885,569)² ≈ 7.8 × 10¹¹ at k = 137 — Elie E1's positive control and Lyra L1's hashed numbers to check against. Forgetting k across blocks adds the block label; the (D) projection's environment is smaller (it keeps the zonal line): Lyra to state, Elie to count.

**Trap restated for the round:** these dimensions are the SIZE of "beyond the horizon" as a Hilbert space; they are not evidence that anything comes back. Re-entry (E2/E3) is the only content.

— Keeper
