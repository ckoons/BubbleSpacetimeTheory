# PRE-REGISTRATION — Toy 5718, E14 (Round 126): a modular resonance at level 137 — the newform 137.2.a.a, its zeros, and the block pole

**Elie, 2026-09-07 (Monday) 08:44 EDT (shell-copied). Hashed before the run. Ceiling stated first: GRH one degree up; this is a LOCATION of a resonance, not a route to anything; RH parks per Casey's ruling.**

## Object
f = 137.2.a.a (LMFDB), weight 2, level 137, coefficient field x⁴−x³−3x²+x+1, embedding 1.1 (ν = −1.35567), Fricke sign +1, analytic rank 1. Hecke eigenvalues a_p for p ≤ 97 from the LMFDB embedding page (25 values, pinned in the toy); a_n for n ≤ 100 by multiplicativity and a_{p^{k+1}} = a_p a_{p^k} − p a_{p^{k−1}}. Completed L-function Λ(s) = 137^{s/2}(2π)^{−s}Γ(s)L(s,f) = ε Λ(2−s) with ε = −(Fricke sign) = −1 for weight 2; AFE Λ(s) = Σ_n a_n[(√137/2πn)^s Γ(s, 2πn/√137) + ε(√137/2πn)^{2−s} Γ(2−s, 2πn/√137)], 30 digits, n ≤ 100 (tail e^{−2π·100/√137} ≈ 10⁻²³).

## Hashed lines
- **P1 (sign, control):** the AFE with ε = −1 is self-consistent — Λ(1+it) is purely imaginary on the line (max |Re/Im| < 10⁻¹⁵ over t ∈ [0.5, 8]) and Λ(1.3) = −Λ(0.7) to 10⁻¹⁰; with ε = +1 both fail. Kill: the numerics prefer ε = +1 (then LMFDB's sign convention is re-read, not the form).
- **P2 (rank, control):** L(1, f) = 0 to 10⁻¹⁵ (forced by ε = −1) and Λ′(1) ≠ 0 (rank exactly 1, |Λ′(1)| > 10⁻³).
- **P3 (the first zero above the centre, can-fail on its value):** Z(t) := Im Λ(1+it) has its first sign change at some t₁ ∈ (0, 8]; t₁ is located by bisection to 10⁻¹⁰ and a second, t₂, if below 8. I hash the INTERVAL only: 1.5 < t₁ < 6 (the level-137 zero density ≈ (1/π)log(√137·t/2π) gives ~one zero per unit t near t ≈ 3–5; prior 70 %).
- **P4 (the block pole — a tautology of the block formula, stated as such):** in Lyra's (σ_f, ψ trivial) block, factor B is L(λ, 1×σ_f)/[ε L(λ+1, …)] with L in the unitary normalisation (critical line Re = ½), so 1/L(λ+1, f) has poles at λ = −½ + iγ for every zero ½ + iγ of L_unit, i.e. at **λ = −½ + i t₁** (and λ = −½ from the central zero — the comb's real part again, Steinberg's ½, not the critical line's). The exhibit is |L_unit(½ + i t₁)| = |L_arith(1 + i t₁)| < 10⁻¹⁰ at the located t₁; the prompt's kill "no pole within 10⁻⁶" cannot fire because the pole IS the zero by construction — the content of E14 is P1–P3 and the numerical t₁, not P4.
- **P5 (structure, stated):** the σ_f blocks carry a degree-2 L-function in factor B (Lyra's P4) — exhibited here only as the formula; the constant-term matrix at level 137 is not computed (E12-137's twisted sector, held on Casey's word).

Score X/5 (P4, P5 are statements; P1–P3 carry the numbers).
