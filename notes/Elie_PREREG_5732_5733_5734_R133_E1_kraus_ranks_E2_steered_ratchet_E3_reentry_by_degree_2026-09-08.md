# PRE-REGISTRATION — Toys 5732 (E1), 5733 (E2), 5734 (E3), Round 133. Hashed before any runs.

**Elie, 2026-09-08 (Tuesday) 10:03 EDT (shell-copied).** dim H_k(S⁴) = (2k+3)(k+1)(k+2)/6: d₁ = 5, d₂ = 14, d₆₈ = 111,895, d₁₃₇ = 885,569.

## E1 — Toy 5732: minimal environment (Kraus rank = Choi rank) of the reset on one saturated block H_k
Three channels, stated so nobody reads one number as another:
- **(T) the twirl alone** ρ ↦ ∫ π(g)ρπ(g)⁻¹dg = completely depolarizing on an irreducible H_k: Choi matrix I⊗I/d, **rank d²**: k = 1: **25**, k = 2: **196**; k = 68: **1.2521 × 10¹⁰**; k = 137: **7.8423 × 10¹¹**. Numerically at k = 1, 2 by Haar-sampled Choi matrices (rank read from the spectrum; Keeper's control 25 at k = 1).
- **(C) twirl-then-forget-k** = the trace channel H_k → ℂ (the survivor mode): Kraus operators ⟨e_i|, **rank d**: 5, 14, 111,895, 885,569. Twirl-then-forget has a SMALLER environment than the twirl: the depolarizing environment's d² is not the reset's.
- **(D) zonal projection with the rest discarded**, ρ ↦ ⟨Z|ρ|Z⟩|Z⟩⟨Z| ⊕ (1 − ⟨Z|ρ|Z⟩)|⊥⟩⟨⊥| (outcome flagged): **rank d** as well (one Kraus |Z⟩⟨Z| plus d − 1 for the discarded complement).
- Also printed: the full-L²(SO(5)) dilation is infinite-dimensional; the minimal ones above are what Lyra's L1 should carry.

## E2 — Toy 5733: the steered ratchet (the round's can-fail)
5731's chain (light branch from Z₂, six writes) with u drawn from the density |Z_{k_env}^ξ(u)|² dσ(u) on S⁴ (cos θ = u·ξ; marginal ∝ C_{k_env}^{3/2}(cos θ)² sin³θ; v uniform on S³). Zonal weight along ξ, exact S⁴ inner products (float coefficients, exact moments), 200 walks per setting.
- **S1 (control):** Haar directions reproduce 5731 within error: ≈ 0.24 after one write, ≈ 0.01 after six.
- **S2 (hashed, can fail — the round's line):** k_env = 68: **weight after six writes > 0.5.**
- **S3 (family, hashed direction, can fail):** k_env = 2, 5, 10, 20, 68: the six-write weight **rises monotonically with k_env** (a sharper density steers harder). Shared-number trap: at k_env = 2 the density (5cos²θ − 1)² is not sharp and the weight may sit near Haar's — that is the family's low end, not a failure of steering.

## E3 — Toy 5734: re-entry by degree
Steered chain from the VACUUM (degree 0) with the k_env = 68 density; R(k′) := expected zonal weight along ξ of the new cycle's state when it first reaches degree k′, k′ = 1..8. **Hashed shape: R(1) = E[cos²θ] under the density (printed), and R(k′) is monotone non-increasing in k′** (each write adds an independent misalignment). Trap named: 1 − 1/d_{k′} is the environment's norm share and is NOT R(k′); it is printed beside R for contrast and nothing is concluded from it.

Score: E1 X/3 (T's numerics at k = 1, 2 can fail), E2 X/3 (S2, S3 can fail), E3 X/1 (shape can fail).
