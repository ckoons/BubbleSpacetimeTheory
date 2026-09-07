# PRE-REGISTRATION — Toy 5722, Round 130: Lyra's hashed file c657a24f scored on an independent exact instrument, plus the Einstein control against the pinned data

**Elie, 2026-09-07 (Monday) 09:56 EDT (shell-copied). Hashed before the run.**

## Instrument (independent of Faraut–Korányi Pochhammers)
Hua's Bergman kernel of D_IV^n, K(z,w) ∝ (1 − 2 z·w̄ + (z·z)(w̄·w̄))^{−n}. Its bidegree-(m,m) part is the reproducing kernel of P_m, so the coefficient matrix C_m (monomials × monomials) is the INVERSE Gram matrix of the monomial basis: ⟨z^α, z^β⟩ = (C_m^{−1})_{αβ}, exact over ℚ (parity blocks). The overall constant cancels between degrees m and m+1. Then ⟨|z|²⟩_ψ = Σ_i ‖z_iψ‖²/‖ψ‖² and c = 1 − ⟨|z|²⟩_ψ, all exact rationals. No Fischer form, no trace-vs-Euclidean choice, no Pochhammer.

## Hashed lines
- **Q1 (can fail; Lyra P1):** the twelve exact rationals of her table — (0,0) 1/2, (0,1) 10/21, (0,2) 45/98, (0,3) 25/56, (1,0) 5/12, (1,1) 25/63, (1,2) 55/144, (1,3) 10/27, (2,0) 5/14, (2,1) 15/44, (2,2) 65/198, (2,3) 7/22 — reproduced EXACTLY by the kernel Gram route for ψ = (z·z)^j·harm(z₀^k). Kill: any word off by any amount.
- **Q2 (control; Lyra P1):** n = 1 in the same code (kernel (1 − z w̄)^{−2}) gives c = 1/(m+2) for m = 0..7.
- **Q3 (can fail; Lyra P5):** family n = 3..7: constant's cost exactly 1/2 at every n; matter word (1,1): 0.3429, 0.3750, 0.3968, 0.4125, 0.4242 to four digits.
- **Q4 (can fail; Lyra P2):** fresh Monte Carlo at (1,1) with ~10× the 5721 sample (target ≥ 10⁵ Lie-ball points, 25 blocks): |c_MC − 25/63| ≤ 2σ. Kill: a stable value off 25/63 by more than 2σ.
- **Q5 (not can-fail — a scoring of a pre-known fact; Lyra P3):** (D2) W = c·hν makes the photoelectric slope (1−c)·h/e with c ∈ [0.318, 0.500]; Millikan's photoelectric h = 6.57e−27 agrees with Planck's radiation h = 6.55e−27 to 0.3 % (file l.309, l.2001), so a 32–50 % slope deficit is refuted at ≥ 30× its bound; Huang 2020's 2e−5 nonlinearity bound refutes the c-drift across words separately. (D1) empty. Recorded as REFUTED/EMPTY; counted in the denominator but flagged.
- **Q6 (not can-fail; Lyra P4):** the pinned Wigner law's l is the ℝ³ outgoing partial wave (Andersen eq. 5); no dictionary quantity carries an excess-energy variable; outcome (c), nothing compared. Flagged.

Score X/6, of which 3 (Q1, Q3, Q4) can fail.
