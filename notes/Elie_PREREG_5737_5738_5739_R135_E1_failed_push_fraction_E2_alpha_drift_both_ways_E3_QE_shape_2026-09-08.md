# PRE-REGISTRATION — Toys 5737 (E1), 5738 (E2), 5739 (E3), Round 135. Hashed before any runs.

**Elie, 2026-09-08 (Tuesday) 14:24 EDT (shell-copied).** c(j,k) = the R134 closed form (5735 = Lyra L2).

## E1 — Toy 5737: the failed-push fraction per cycle
Model: at state (j,k) a push lands with probability 1 − c(j,k); a failed push leaves the state unchanged and the turn continues (K1860-N: one push per 137 turns becomes 137/(1−c) turns per commitment). The sequence of LANDED pushes is K1860's chain exactly (so the c ≡ 0 control reproduces 5726/5736 to the digit, and the chain's law stays j-blind). Two statistics, both reported: (a) **mean of c along the landed chain** = Σc/writes (Keeper's control's definition: cycle 1 m-cap = 14.81/137 = **0.1081**, hashed inside his [0.09, 0.13]); (b) **fraction of all pushes that fail** = E[Σ c/(1−c)] / E[Σ 1/(1−c)] — hashed in **[0.10, 0.15]** at cycle 1 m-cap (each failure-prone state is visited by more pushes, so (b) > (a)). Both monotone decreasing in j₀ at 0, 58, 570, 2329 under all three stopping rules (can fail). Five cycles at the m-cap: (a) = 0.108, 0.027, 0.016, 0.012, 0.009 — **NOT one in a thousand by cycle four** (Keeper's relay line); if his control says 10⁻³ at cycle 4 it is a different rule or a different j₀ growth, and the discrepancy is data.

## E2 — Toy 5738: the α-drift arithmetic under R2, both ways, bound pinned from the source
α_eff = α(1 − c), c ≈ 5/(2j), j growing linearly since the reset over t ≈ t_H = 13.8 Gyr: α̇/α = −ċ/(1−c) ≈ (5/2)/(j t_H) (sign: α_eff RISES as c falls).
- **Forward (hashed):** with |α̇/α| ≤ B: j_min = (5/2)/(B t_H). B = 1.1e−18/yr (1σ width) → j_min = **1.65e8** (Keeper's number reproduced); B = 2.1e−18 (central + 1σ) → 8.6e7; B = 3.2e−18 (2σ) → 5.7e7. Cycles: j_min/2329 (k-cap) ≈ 2.5e4–7e4; j_min/58 (m-cap) ≈ 1e6–3e6.
- **Inverse (hashed):** j = 58 → α̇/α = 3.1e−12/yr; j = 2329 → 7.8e−14; j = 10⁴ → 1.8e−14 — **10⁵ to 10⁶ above the bound**; the prompt's "10⁻¹³–10⁻¹⁵" holds for j = 10³–10⁴ and is exceeded at j = 58.
- **R1 control:** the word's own j is reset per interaction — drift 0 identically.
- The bound is quoted from the paper's text (arXiv 2010.06620 / PRL 126, 011102), with Filzinger 2023 beside it; if the fetch fails I say so and quote nothing.

## E3 — Toy 5739: the shape
QE(m) = 1 − Π_{k<m}(k+3)/(2k+3) (K1860 l.108) vs P(commit) = 1 − c(j,k). **Hashed: same monotone rising shape, SAME asymptote 1, DIFFERENT approach law** — 1 − QE(m) ~ 2^{−m} (geometric: each factor → ½) vs c ~ 5/(2j) (algebraic). Within one interaction P(commit) depends on the electron's own word: at m = 3, light (0,3) 31/56 = 0.554 vs matter (1,1) 38/63 = 0.603, against QE(3) = 3/7 = 0.43. The two are not the same object.

Score: E1 X/3 (monotonicity and (b)'s range can fail), E2 X/2 (forward number can fail), E3 X/1.
