# PRE-REGISTRATION — Toys 5735 (E1) and 5736 (E2, E3), Round 134. Hashed before any runs.

**Elie, 2026-09-08 (Tuesday) 10:32 EDT (shell-copied).**

## E1 — Toy 5735: c(j,k) in closed form, derived on a route that is not Lyra's, then tested on the Gram instrument at cells it has never seen
Route: a write splits (z·z)^j Y_k into two K-types, (z·z)^j H_{k+1} and (z·z)^{j+1} ∂Y_k/(2k+3), orthogonal in A². By Schur the Bergman norm of (z·z)^j Y_k is a(j,k) × (S⁴ norm of Y_k); Stein–Weiss (5723) supplies the S⁴ weights (k+3)/(2k+3) and k/(2k+3). From the 12 known exact values the ratios are forced: a(j,k+1)/a(j,k) = (j+k+5/2)/(j+k+5) and a(j+1,k−1)/a(j,k) = (j+1)/(j+7/2), i.e. a(j,k) = j!(5/2)_{j+k}/((5)_{j+k}(7/2)_j). **Hashed closed form:**
  **c(j,k) = 1 − [(k+3)/(2k+3)]·(j+k+5/2)/(j+k+5) − [k/(2k+3)]·(j+1)/(j+7/2).**
- **P1 (control):** reproduces all twelve Round 130 rationals.
- **P2 (can fail):** the kernel-Gram instrument (5722, exact) at NEW cells (3,0), (4,0), (3,1), (3,2), (0,4), (1,4), (2,3), (0,5) returns exactly the closed form's rationals.
- **P3 (hashed):** k = 0 line c(j,0) = 5/(2(j+5)) — **Keeper's guess is the exact k = 0 line of the closed form** (it holds, not just at j = 0, 1, 2). Values: c(58,0) = 5/126 = 0.039683, c(570,0) = 1/230 = 0.0043478, c(2329,0) = 5/4668 = 0.0010711; c(58,1), c(570,1), c(2329,1) printed from the form.
- **P4 (hashed asymptotics):** c(j,k) = 5/(2j) + O(1/j²) for EVERY k — the leading coefficient A(k) = 5/2 is k-independent; large-k line at fixed j: c(j,k) → 1 − (1/2)(1 + (j+1)/(j+7/2)) = (5/4)/(j+7/2). Family in n (5724's route): the k = 0 line is n/(2(j+n)).

## E2 — Toy 5736: the cycle's total push cost against the carried winding
5726's chain from (j₀, 0), three stopping rules on the INCREMENT (137 writes; first k = 68; first k = 137), Σc = E[Σ_writes c(j_t, k_t)], exact DP. Then five successive cycles with j₀ accumulating (full distribution propagated).
- **Q1 (hashed shape, can fail):** Σc(j₀) monotone decreasing in j₀, → 0, and for large j₀ Σc(j₀) ≈ (5/2)·N_writes/j₀ (N_writes = 137 at the m-cap) within 10 % at j₀ = 2329.
- **Q2:** the per-cycle drift ΔΣc over five cycles is negative and shrinking in magnitude at every step (asymptote from below). Shared-number trap: the ratio Σc(cycle 2)/Σc(cycle 1) is refused as a BST integer before it is read.

## E3 — Toy 5736: blindness control (cannot fail; reported as such)
H(Δj), P(3-write word = (1,1)) = 3/7, and the stopping degrees at j₀ = 0 and j₀ = 2329: identical to the digit, because no transition probability involves j.

Score: E1 X/4 (P2 can fail), E2 X/2 (Q1 can fail), E3 X/1.
