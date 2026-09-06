# PRE-REGISTRATION — Toy 5693, E1 (gate item): BLIND re-run of Keeper K1862-A

**Elie, 2026-09-06 (Sunday) 09:56 EDT (`date`-rendered). Hashed before the instrument runs. Keeper's retained instrument (`scratchpad/siegel_check2_final.py`) NOT opened; his K1862-A/B/C notes and 09:44 handoff read for the DEFINITION only (form, roots, chamber, Siegel weight, the test).**

## Object
Q(x) = x₀² − x₁² − x₂² − x₃² − x₄² on ℤ^{1,4}; (x,y) = x₀y₀ − Σxᵢyᵢ. Roots (my sign choice so that the chamber is {(x,rᵢ) ≥ 0 ∀i} and (rᵢ,rⱼ) ≥ 0 for i ≠ j):
r₁ = e₂−e₁, r₂ = e₃−e₂, r₃ = e₄−e₃, r₄ = −e₄, r₅ = e₀+e₁+e₂+e₃ (norms −2,−2,−2,−1,−2).
Chamber C = {x₁ ≥ x₂ ≥ x₃ ≥ x₄ ≥ 0, x₀ ≥ x₁+x₂+x₃}. Reflection sᵣ(x) = x − 2(x,r)/(r,r)·r, integer matrices.
r*(N) := Σ_{x∈C, Q(x)=N} 1/|W_x|, W_x = ⟨sᵣ : (x,r) = 0⟩ computed by BFS closure on the matrices (NOT by Coxeter-type lookup).
Local density α_p(N) := lim_k p^{−4k}·#{x mod p^k : Q(x) ≡ N mod p^k}, by cyclic convolution of the five square-distributions (signs as in Q). Stability: odd p at k = e+1 vs e+2; p = 2 at k = e+3 vs e+4 (e = ord_p N). For p ∤ 2N: α_p = 1 + (N/p)·p⁻² (F_p point count, det Q = 1), product to p < 10⁵.
Control: I₅ (all signs +), r₅(N) = coefficient of θ⁵ by direct count, same α_p machinery with + signs.

## Hashed lines (each can fail)
- **P1 (chamber):** e₀ ∈ C with (e₀,r₅) = 1 > 0 and (e₀,rᵢ) = 0 for i ≤ 4; the Gram matrix of {r₂,r₃,r₄,r₅} is singular (affine B̃₃ cusp: one null vector, all other 4-subsets nonsingular); the Coxeter matrix read off the Gram matrix is chain r₁–r₂–r₃ (m=3,3), r₃=4=r₄, r₃–r₅ (m=3), all other pairs commute.
- **P2 (stabilizers by BFS):** |W_{e₀}| = 384; every stabilizer met for 1 ≤ N ≤ 60 is finite (BFS closes below 10⁴ elements); the orders met are a subset of {1,2,4,6,8,12,16,24,48,96,120,384} (products of A₁,A₂,B₂,A₃,B₃,A₄,B₄ types that occur as subdiagrams).
- **P3 (coefficients vs Keeper's published list — the direct blind check):** my r*(N) for N = 1..12 equals 1/384, 1/96, 1/48, 3/128, 7/240, 1/16, 1/12, 5/96, 25/384, 7/48, 7/48, 5/48 as exact Fractions, 12/12, and orbit counts 1,1,1,2,2,2,2,3,3,2,2,4.
- **P4 (odd-p densities two ways):** Lemma 1 recursion = convolution for p ∈ {3,5,7}, every N ≤ 60, to the convolution's exact rational value (stability at k=e+1 confirmed at e+2).
- **P5 (THE KILL — Siegel constancy):** relative sd of r*(N)/(N^{3/2}·Π_p α_p(N)) over N = 1..60 is < 10⁻⁵ (Euler-product truncation at 10⁵ is ~10⁻⁶). Any N-dependence above that = a cuspidal component or a bookkeeping error, reported by N.
- **P6 (positive control):** I₅ ratio constant with relative sd < 10⁻⁵ and equal to (8π²/3)/2 = 13.15947 (plain-density convention) — if my α₂ convention differs from Keeper's the constant will be 26.31895 and I say so; constancy is the invariant.
- **P7 (Keeper's constants):** ℤ^{1,4} constant = 0.0034269 within 10⁻⁴ relative under the same α₂ convention that returns 13.15947 for I₅; the ratio definite/indefinite = 3840 within 10⁻⁴. Reported, not interpreted (Grace G2).
- **P8 (fundamental-domain sanity, bookkeeping):** every forward vector of norm N ≤ 20 with x₀ ≤ 40 reduces by greedy reflection (reflect while some (x,rᵢ) < 0, cap 10⁴ steps) to a vector in my enumerated chamber list for that N; zero non-terminations, zero vectors outside the list.

Score X/8. A P5 or P3 failure is the headline whichever way it goes.
