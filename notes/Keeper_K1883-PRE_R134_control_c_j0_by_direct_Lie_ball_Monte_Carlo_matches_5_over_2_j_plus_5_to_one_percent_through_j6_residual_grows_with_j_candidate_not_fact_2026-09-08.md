# K1883-PRE — Round 134 control: c(j,0) on the Lie ball by direct Monte Carlo

**Keeper, 2026-09-08 (Tuesday) 10:25 EDT, clock-verified.** Instrument retained: `notes/Keeper_K1883-PRE_instrument_push_cost_c_j0_Monte_Carlo_Bergman_on_the_Lie_ball_2026-09-08.py` (uniform Lebesgue on the Lie ball by rejection from the unit ball of ℂ⁵; acceptance 0.0623 vs the exact 1/16 = 0.0625 — the volume ratio π⁵/1920 : π⁵/120 — a control on the sampler; 498,601 accepted points; c(j,0) := 1 − ⟨|z|²⟩ under the weight |z·z|^{2j}, Lyra's Round 130 definition).

| j | c(j,0) MC | 5/(2(j+5)) | Round 130 exact |
|---|---|---|---|
| 0 | 0.5001 | 0.5000 | 1/2 |
| 1 | 0.4171 | 0.4167 | 5/12 |
| 2 | 0.3580 | 0.3571 | 5/14 |
| 3 | 0.3137 | 0.3125 | — |
| 4 | 0.2793 | 0.2778 | — |
| 5 | 0.2517 | 0.2500 | — |
| 6 | 0.2290 | 0.2273 | — |

**Reading.** The sampler reproduces Round 130's three exact values to 3 decimals. My hashed guess 5/(2(j+5)) matches to 0.1 % at j ≤ 2 and the residual GROWS with j (0.4 % at j = 3, 0.7 % at j = 6), always above the formula. That is either Monte Carlo weight concentration (the weight |z·z|^{2j} pushes mass to the boundary where sampling is sparse) or a formula that is only asymptotically 5/(2j). **The hash stands as a CANDIDATE, not a fact;** Lyra's closed form (L2) or Elie's exact Gram (E1) decides. Either way the round's claim survives the control: c(j,0) falls monotonically with j, from ½ toward 0, at rate ~1/j.

— Keeper
