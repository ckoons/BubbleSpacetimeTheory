# PRE-REGISTRATION — Toys 5740 (E1), 5741 (E2), 5742 (E3), Round 136. Hashed before any runs.

**Elie, 2026-09-09 (Wednesday) 09:51 EDT (shell-copied).**

## The instrument I will use, stated before it runs (it is a derivation, not a fit)
T_n := Σ_{|α|=n} C(n;α) M_{z^α}* M_{z^α} is K-invariant and degree-preserving, so by Schur it is DIAGONAL on the Hua components (z·z)^j H_k (they are pairwise inequivalent K-types inside one degree). Its eigenvalue is τ_n(j,k) = ⟨|z|^{2n}⟩ for that word. The algebraic identity z_i Y_k = H_{k+1}^{(i)} + (z·z)(∂_iY_k)/(2k+3) plus the Stein–Weiss shares (5723) and the Bergman weights a(j,k) = j!(5/2)_{j+k}/((5)_{j+k}(7/2)_j) (5735) give the **exact recursion**

  **τ_n(j,k) = L(j,k)·τ_{n−1}(j,k+1) + M(j,k)·τ_{n−1}(j+1,k−1),  τ_0 ≡ 1,**
  **L(j,k) = [(k+3)/(2k+3)]·(j+k+5/2)/(j+k+5),  M(j,k) = [k/(2k+3)]·(j+1)/(j+7/2),  L + M = τ_1 = 1 − c(j,k).**

**Reading, hashed as the round's structural claim:** ⟨|z|^{2n}⟩ is the n-step norm retention of the SAME write chain, so the family member n is the effect "the word reaches the boundary within n writes." The family is not a menagerie — it is one chain read at n horizons.

## E1 — Toy 5740: the family sweep, exact
- **A1 (control):** n = 1 returns Round 130's twelve rationals exactly.
- **A2 (control, independent route):** ⟨|z|⁴⟩ computed directly from the exact kernel-Gram (5722) as Σ_{|α|=2}C(2;α)‖z^αψ‖²/‖ψ‖² equals the recursion at (0,0), (1,0), (0,1), (1,1), (0,2). This validates the recursion against an instrument that shares none of its steps.
- **A3 (can fail — Keeper's columns, exact):** c₂(j,0) at j = 0,1,2,3 and c₃(j,0) at j = 0,1,2,3 reproduce K1885-PRE's Monte Carlo to its stated precision. **Hashed exact values: c₂(0,0) = 31/42 = 0.738095 (MC 0.7378); c₃(0,0) = 6/7 = 0.857143 (MC 0.8569).** Vacuum commitment probabilities across the family: **1/2, 11/42, 1/7** for n = 1, 2, 3 — i.e. Keeper's relayed "one half, about one quarter, about one seventh."
- **A4:** the k = 0 line for n = 2, 3 printed as exact rationals in j, with the closed form given if it factors; τ_n(j,k) at general n does not need one, the recursion IS the closed form.

## E2 — Toy 5741: is the order invariant?
- **B1 (can fail):** for n = 1..8 and j = 0..40 at k = 0..3, c_n(j,k) is strictly decreasing in j and → 0. **Asymptotics hashed: c_n(j,k) = 5n/(2j) + O(1/j²) — the effect choice is exactly ONE SCALE CONSTANT n, and the leading behaviour 5n/(2j) is k-independent.**
- **B2 (a second, non-power member, can fail):** the defining function ρ = 1 − 2|z|² + |z·z|² gives the admissible effect f = 1 − ρ (0 ≤ f < 1 inside, f = 1 on Š, and it is NOT of the form |z|^{2n}). Exact: c_ρ(j,k) = ⟨ρ⟩ = 1 − 2τ₁(j,k) + (j+1)(j+k+5/2)/[(j+7/2)(j+k+5)]. **Hashed: c_ρ(0,0) = 1/7 = 0.1429 and c_ρ(1,1) = 5/63 = 0.0794 — which my own Round 130 Monte Carlo measured as 0.1417 ± 0.0011 and 0.0786 ± 0.0011 (toy 5721), so this member arrives with an instrument already attached.** Order: monotone decreasing in j, → 0, and its constant is NOT 5n/2 — hashed 5/(2j)·(something < 1), i.e. ρ is a *cheaper* effect than |z|² at every cell.
- **B3 (the break, can fail in the other direction):** the order is NOT invariant across all admissible effects. Two exhibits: (i) a multiplication effect 1 − f = (1 − |z|²)(|z|² − c)² for c ∈ (0,1) — admissible after scaling (0 ≤ f ≤ 1, f = 1 on Š) — tested for monotonicity; (ii) **the general K-invariant effect: by Schur any assignment λ(j,k) ∈ [0,1] on Hua components is an admissible effect, and "equals the identity on Š" constrains a FUNCTION, not an operator's eigenvalues — so λ(j,k) non-monotone in j is admissible and the order breaks trivially.** Hashed verdict: **the order is a theorem of the multiplication sub-family, not of "K-invariant effects"; "the effect is multiplication by a function that is 1 on Š" is itself part of the identification, and it is the part that carries the order.**

## E3 — Toy 5742: the physical spread
Under n = 1, 2, 3 and the ρ member: the vacuum commitment probability; Σc over the m-cap cycle from j₀ = 0; the cycle-1 failed-push fraction (mean of c along the landed chain); and the five-cycle series. **Hashed: every quantity moves by a factor of order 2–8 across the family while every sign and ordering is unchanged; Σc(n=2) ≈ 2×Σc(n=1) at large j₀ and less than 2× at j₀ = 0** (because the n-fold retention saturates where c is large). Trap named before reading: **no ratio or difference between family members is a BST integer, and none may be quoted as one.**

Score: E1 X/4 (A3 can fail), E2 X/3 (all can fail), E3 X/2.
