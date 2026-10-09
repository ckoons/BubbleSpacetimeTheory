# Elie — PREREG toys 5864–5867 (Round K4-3, Lane B, the no-data items). Fri 2026-10-09 12:33 EDT (from `date`, its own call). Written BEFORE any code.

`didwe`: "restricted roots" → 2 (K1222 OPEN: do the B₂ multiplicities force 3+1; K1228 the ruling). "pi audit" → 136 by keyword only (none is an audit of π's source). "Fermi integral neutron" → 0. "constant fraction control ledger" → 0. "Wyler" → 35 (K614 and the retired Vol^{1/4} formula; Grace 08-10: α = charge count, the Wyler formula is NOT the source).
Read before writing: the 10-08 and 10-09 K4-3 prompts; K1922 and its instrument; Lyra FILLING_LAW 09-22 Sections 0–3 and the 09-25 appendix (check 5 is Lyra's own disclosure, so the a^k family here is a re-derivation, not a blind); K1228. **No cosmological number is read. No MeV is computed. The neutron's endpoint is not evaluated.**

## 5864 — the control ledger (Target 1's declared control)
Inputs (Lyra Section 3, verbatim objects): ρ_DE = E_commit·N/V_H; E_commit = ħH ln2/(2π); N = f·N_H; N_H = 4π/(H²ℓ_P²); V_H = (4π/3)H⁻³. So ρ_DE = f·(3 ln2/2π)(ħ/ℓ_P²)·H², and the DE fraction is Ω_DE = (8πG/3)ρ_DE/H² = 4 ln2·f (rule R, coefficient 1).
w from continuity: w = −1 − (1/3) d ln ρ_DE/d ln a.
Two readings of "H" in ρ_DE, both run:
- (T) test-field: H² is the matter-era background a⁻³ (radiation: a⁻⁴); f does not feed back.
- (S) self-consistent: 3H²/8πG = ρ_m + ρ_DE with ρ_DE = Ω(a)·3H²/8πG, Ω = 4 ln2·f.
Predictions, exact (sympy), then checked numerically by an ODE in ln a:
- C1 (the control, both readings): f constant ⇒ w = 0 identically, every a, every era. Hsu. **Can fail.**
- C2 (T), f ∝ a^k: w = −k/3 in matter, (1−k)/3 in radiation. So k = 3 ⇒ w = −1 (K1922's product, a⁶/a³), and k = 2 in radiation ⇒ w = −1/3 (K1922 C5). **Can fail.**
- C3 (S), f ∝ a^k, Ω = Ω₀a^k: w = −k/(3(1−Ω)). Constant ⇒ 0 (C1 again); k = 3 ⇒ w < −1 whenever 0 < Ω < 1 (Lyra's check-5 phantom, re-derived), and Ω → 1 is a wall: the saturation clause is not optional. **Can fail.**
- C4 numeric: the ODE reproduces C1–C3 to 1e-10 on a grid of k and Ω₀. **Can fail.**
- C5 the Hsu identity: constant f ⇒ Ω_DE constant ⇒ H² ∝ ρ_m exactly (tracks matter). **Can fail.**
Output: a function `w_of_a(f_callable, reading)` kept in `play/.k4_3_lib.py` for Target 1 after the hash. The instrument prints no direction for any real f; the only f's run are the control and the a^k family.

## 5865 — the Fermi routine f(W₀) (Target 2's instrument, kept away from the neutron)
Units m_e = c = 1; W = total electron energy; W₀ = 1 + E₀/m_e the endpoint; p = √(W²−1).
f(W₀) = ∫₁^{W₀} F(Z,W)·p·W·(W₀−W)² dW. Statistical factor only (F = 1) has the closed form
f₀(W₀) = (p₀/60)(2W₀⁴ − 9W₀² − 8) + (W₀/4)·ln(W₀ + p₀), p₀ = √(W₀²−1).
- F1 closed form = quadrature (mpmath, 30 dps) to 1e-20 at W₀ ∈ {1.2, 1.5, 2, 3, 5, 10, 30, 100}. **Can fail.**
- F2 Sargent: f₀/(W₀⁵/30) → 1 as W₀ → ∞; print the ratio on the grid. At W₀ = 100 within 1%; **at W₀ ≤ 3 the E₀⁵ law is off by more than 30%** (Keeper's catch, as a number). **Can fail.**
- F3 threshold law: f₀ ∝ (W₀−1)^{7/2} as W₀ → 1 (local log-slope at W₀ − 1 = 1e-3 within 1% of 3.5). The neutron sits between the 7/2 and the 5. **Can fail.**
- F4 the Coulomb factor F(Z,W) = 2(1+γ)(2pR)^{2γ−2}e^{πη}|Γ(γ+iη)|²/Γ(2γ+1)², γ = √(1−(αZ)²), η = αZW/p (Z = 1 for the proton; R the nuclear radius in units ħ/m_e c): F → 1 as α → 0, and F matches the Sommerfeld form 2πη/(1−e^{−2πη}) to O((αZ)²) at p ≫ αZ. **Can fail.**
- F5 the general-Z scan: the full f(Z, W₀) with Z = 1 on the same grid, reported beside f₀. No W₀ in (2.4, 2.7) is evaluated. **Can fail** (Z-dependence must be monotone increasing in Z for electrons).
Output: `fermi_f(W0, Z)` in `play/.k4_3_lib.py`.

## 5866 — the restricted roots of so(5,2): are the two 3s the same 3? (B-new-1)
Build so(5,2) as the 7×7 real matrices X with Xᵀη + ηX = 0, η = diag(+1⁵, −1²); dim 21. Cartan: k = so(5)⊕so(2) (dim 11), p = the 5×2 off-diagonal block (dim 10). a = span{E₁₆+E₆₁, E₂₇+E₇₂} (dim 2, abelian — checked).
- R1 restricted roots by simultaneous diagonalisation of ad(a): **B₂ with m(±eᵢ) = 3, m(±e₁±e₂) = 1**; 2 + 4·1 + 4·3 = 18 = 21 − dim m, so dim m = 3. **Can fail.**
- R2 m = z_k(a) ≅ so(3) acting on coordinates {3,4,5}; M = Z_K(a) has identity component SO(3) and component group Z₂ (ε₁ = ε₂ = −1). **Can fail.**
- R3 M's action: on each short root space g_{±eᵢ} the so(3) Casimir is 2 (the vector, l = 1) and the trace of a rotation by θ is 1 + 2cos θ; on each long root space it is 0 (trivial). **Can fail.** This is the Keeper check.
- R4 the frame vertex: S₃ ⊂ S₄ permuting three faces, fixing one. Characters computed from permutation matrices: faces = 1 ⊕ 2, opposite face = 1 (trivially passes, as Keeper said).
- R5 the obstruction that is not trivial: M acts on g_{e₁} through SO(3) only (R2). A transposition of faces as a permutation matrix has det −1, so it is NOT in M. The only S₃'s inside M = SO(3) are the dihedral D₃'s (C₃ about an axis + three 2-fold rotations), whose vector rep restricts to 2 ⊕ sign, not 1 ⊕ 2. Hence **dim Hom_{S₃}(faces, g_{e₁}) = 1 (the 2 matches; the singlet does not) unless the frame's S₃ acts on its faces by (perm)⊗sign = sign ⊕ 2, which is exactly 5859's std⊗sign embedding of S₄ in SO(3).** Prediction: the intertwiner exists (dim Hom = 2 → an isomorphism of 3-dim reps) iff the face action is sign-twisted. Computed by Schur orthogonality from explicit matrices. **Can fail.**
- R6 the closure face: S₃-trivial as a label (R4); in the rotation realization the vertex's own axis carries sign. g_{long} is M-trivial. So "closure face ↔ g_{long}" is consistent as a LABEL (trivial ↔ trivial) and inconsistent as the AXIS (sign ↔ trivial). Report both; Lyra and Casey settle the words. **Can fail** (the axis character is computed, not assumed).
- R7 the (3,1) reading: the Killing form restricted to a ⊕ (long root directions) vs short: print signature of the Killing form on p (should be positive-definite on p, so "timelike" is not a signature statement about p; it is K1228's 1 = m_long). Reported as a fact, not ruled.
Kill lines (Keeper's): R3 fails ⇒ the two 3s are different 3s. R5's Hom = 0 for both face actions ⇒ no intertwiner. Neither is expected; both can fail.

## 5867 — the π audit over data/bst_constants.json (B-new-2)
Claim under test: every π enters through the boundary (a measure, a kernel normalization, a sphere volume); every rational is spectral.
Method: for every row with `formula_code` (195 of 196; 35 rows carry no `id` and are counted by position), evaluate in the file's namespace; for the rows containing `pi`, extract the π-exponent structure with sympy (π as a symbol; collect the exponent set of π in the expression, including fractional and negative) and tag each distinct π-power by a NAMED boundary object from this fixed table, written now:
- π¹ (denominator) and 1/(2π): |S¹| = 2π, the Šilov circle's measure (a_e = α/2π; the ln 137 class; B_α etc. with /π).
- π² : |S³| = 2π² (the Hopf total space; polarization + phase) or |S¹|² — ambiguous, tagged "S³ or (S¹)²: route owed".
- π⁵ : Vol(D_IV⁵) = π⁵/1920 with 1920 = |W(B₅)| = 2⁴·5! (computed in the toy) — the Hua/Bergman measure (m_p/m_e, m_ρ, m_K, m_φ, Γ_W, T_deconf, the Gamma_mu row's π^{4n_C+3}).
- π^{5/4} and π⁴ together: the retired Wyler form; π^{5/4} = Vol^{1/4} (boundary), π⁴: candidate |S¹|²·|S⁴| ∝ π⁴ — **tagged "route owed", not pinned.** The toy evaluates (9/8π⁴)(π⁵/1920)^{1/4} and prints it beside 137 once, as the exhibit Keeper asked for, with Grace's 08-10 retirement quoted.
- 180/π: unit conversion (degrees), NOT a physical π — tagged "unit".
- π in SI definitional rows (σ_SB, ħ = h/2π, μ_B): standard physics, tagged "SI/not BST".
- π² in C₂^QED (197/144 + π²(1/12 − ln2/2) + 3ζ(3)/4): the two-loop QED coefficient (Petermann–Sommerfield) — a loop measure, tagged "loop integral: boundary route owed".
- 3/(5π) (f, Δ_f, δ_trans): "route owed".
Scores: P1 every π row receives exactly one tag from the table (coverage 100%; **can fail** if an exponent appears that the table does not name). P2 the exhibits: 6π⁵ and π⁵/|W(B₅)| with 1920 computed from the Weyl group order. P3 the rational audit: for every evaluable row, the rational coefficient (formula with π → 1, m_e → 1, sqrt-free part) has prime support ⊆ {2, 3, 5, 7, 11, 13, 137}; rows outside are listed (expected: 79, 197/144, 11/12-type rows — these are the list, reported not hidden). **Can fail.** P4 the kill count: the number of π rows tagged "route owed" is printed as k/N. Keeper's kill is "one formula whose π has no boundary route"; the honest output is the list, and the verdict is Keeper's.
Wording pin kept: "the interior's spectrum is rational", never "the interior is rational".

## What is NOT done here
No w for any physical f. No 0.78233. No Q*. No cosmological pin. 5864 and 5865 are instruments for after Cal's hash.
