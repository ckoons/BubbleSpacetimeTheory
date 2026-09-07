# PRE-REGISTRATION — Toy 5721, Round 130 (kinematics on the record space): the exact objects on the Lie ball, before Lyra's file and before any data

**Elie, 2026-09-07 (Monday) 09:47 EDT (shell-copied). Hashed before the run. T1452's k(k+5) not copied: the eigenvalues are computed by applying the operators to explicit basis functions.**

## Objects
Holomorphic polynomials on ℂ⁵ restricted to the Lie ball D_IV⁵; Hua components P_m = ⊕_j (z·z)^j H_k, m = 2j + k, H_k the SO(5)-harmonic polynomials in the five coordinates. K = SO(5) × SO(2): the SO(5) Casimir as the differential operator C₅ = −Σ_{i<l}(z_i∂_l − z_l∂_i)², the SO(2) generator E = Σ z_i∂_i (degree). K-type label λ = (j+k, j) in the Faraut–Korányi (Jordan) parametrisation; for D_IV⁵: rank 2, a = 3, genus p = 5, n/r = 5/2; (ν)_λ := (ν)_{λ₁}(ν − 3/2)_{λ₂}.

## Hashed lines
- **P1 (Casimir on the components, by the operators):** on (z·z)^j Y_k for random harmonic Y_k, C₅ acts as the scalar **k(k+3)** (independent of j: z·z is SO(5)-invariant) and E as **m = 2j + k**, exactly (sympy), for j ≤ 2, k ≤ 3. So the K-Casimir spectrum on H²(D_IV⁵) is k(k+3) ⊕ (an SO(2) part in m); the number k(k+5) of T1452 is NOT the SO(5) Casimir on H_k ⊂ five variables — if it is anything here it is a different operator (e.g. the Laplacian in seven variables on Q⁵'s harmonics: k(k+5) = k(k + 7 − 2)); which operator is Lyra's item (0); I report both eigenvalue families side by side (k(k+3) for S⁴ ⊂ ℝ⁵, k(k+5) for S⁶ ⊂ ℝ⁷).
- **P2 (the disc control, exact):** the moment observable f_disc(m) := ⟨|z|²⟩ for Bergman-normalised z^m = (m+1)/(m+2), push cost 1/(m+2); the FK ratio (Bergman-norm)/(Hardy-norm) reproduces ‖z^m‖²_A = 1/(m+1). Both exact; the toy prints them.
- **P3 (the ball control, exact):** on B⁵ (Lebesgue), ⟨|z|²⟩ for z₁^m = (m+5)/(m+6), push 1/(m+6): a second known domain to place the Lie ball against.
- **P4 (f(j,k) on the Lie ball, moment method):** f(j,k) := ⟨|z|²⟩_{Bergman} for the component word (z·z)^j·(v·z)^k-type representative (one harmonic representative per (j,k): (z·z)^j z₁^k with the harmonic projection applied to z₁^k when k ≥ 2) for j ∈ {0,1,2}, k ∈ {0,1,2,3}, 25-block Monte Carlo with the same 13,136-sample Lie-ball set (error bars printed); also ⟨ρ⟩ with ρ = 1 − 2|z|² + |z·z|². Hashed shape: f increases with m; at fixed m the j-heavy (matter) word has the larger f (nearer the boundary), as 5719 found (0.606 vs 0.552 at m = 3).
- **P5 (FK exact Hardy/Bergman norm ratios):** R(j,k) = (5)_{j+k}(7/2)_j / [(5/2)_{j+k}(1)_j] printed for the same grid — the exact reproducing-kernel object beside the moment object; the disc limit of the same formula is m + 1 (P2). Which of f or R is "retained/absorbed" is Lyra's definition; both are on the table exactly.

Score X/5 (P4's shape is the only can-fail line; P1's "k(k+3) not k(k+5)" is a naming seam flagged for Keeper's watch).
