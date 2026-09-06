# PRE-REGISTRATION — Toy 5704, E6 (Round 120): the pole set of Lyra's L1 scattering factors, computed against her hashed list (be29f1dc)

**Elie, 2026-09-06 (Sunday) 12:01 EDT (`date`-rendered, copied). Hashed before the run. Lyra's L1 read (her formulas are the input; her toy 5700 not opened).**

## Objects (Lyra's conventions, verbatim)
ξ(s) = π^{−s/2}Γ(s/2)ζ(s); Γ_ℂ(s) = 2(2π)^{−s}Γ(s); Λ(s) = Γ_ℂ(s+½)ζ(s+½)ζ(s−½)(1 − 2^{½−s}); ε(s) = 2^{½−s}.
Long-root factor f_L(x) = ξ(x)/ξ(x+1), x = λ₁ ∓ λ₂. Short-root factor f_S(λ) = ξ(2λ)/ξ(2λ+1) · Λ(λ)/[ε(λ)Λ(λ+1)]. c(w₀,λ) = f_L(λ₁−λ₂)f_L(λ₁+λ₂)f_S(λ₁)f_S(λ₂).
Poles of c are poles of the factors (product of one-variable functions of four different arguments), so the pole SET is the union of the factor pole sets; I test the factors.

## Hashed lines
- **P1 (long roots):** the poles of f_L on Re x = −½ with 0 < Im x ≤ γ₅₀ are exactly x = −½ + iγ_n, n = 1…50, each simple, located by Newton on 1/f_L to |Δ| < 10⁻¹⁰ against mpmath's zetazero(n).
- **P2 (short roots, ζ twice):** poles of f_S at λ = −¼ + iγ_n/2 and at λ = −1 + iγ_n, n = 1…50, each simple, to 10⁻¹⁰.
- **P3 (the 2-comb):** poles of f_S at λ = −½ + 2πik/ln 2 for k = ±1,…,±5 (spacing 9.0647202836…), each simple; at k = 0 (λ = −½) the order is 0 — not a pole.
- **P4 (the cancellations — MY reading against Lyra's Check 1, can fail either way):** (i) λ = iγ_n (n ≤ 10) is NOT a pole of f_S: the ζ(λ+½) in Λ(λ+1) cancels against the ζ(λ+½) in Λ(λ). (ii) **At λ = ½ the order of f_S is 0 (regular, nonzero):** ξ(2λ) has a simple pole there, Λ(λ) is regular (ζ(1)·(1−2⁰)), and Λ(λ+1) = Γ_ℂ(2)ζ(2)ζ(1)(1−½) has a simple POLE in the denominator, which cancels the numerator's. Lyra wrote "the pole of c_{e₁} at λ₁ = ½ is simple"; her kill clause says a double pole there would falsify her p = 2 factor. I predict neither: order 0. Orders are read numerically from |f_S(½ + δe^{iθ})| ∝ δ^{−m} over δ = 10⁻³…10⁻⁶ at four angles.
- **P5 (no pole off the list — argument principle):** on the rectangle −1.2 < Re λ < 0.8, 0.1 < Im λ < 30, the winding number of f_S equals (#zeros − #poles) computed from the lists: zeros at λ = ¼ + iγ_n/2 (γ_n < 60: n ≤ 10) and λ = ½ + 2πik/ln 2 (k = 1, 2, 3); poles at λ = −¼ + iγ_n/2 (n ≤ 10), λ = −1 + iγ_n (γ_n < 30: n ≤ 3), λ = −½ + 2πik/ln 2 (k = 1, 2, 3). Predicted winding = 13 − 16 = **−3**. Any other value = a pole or zero off the list, to be located and reported.

Score X/5. P4(ii) is the line where Lyra and I differ on paper; the number decides, and either way her resonance list (which does not include ½) is unaffected — only the Check-1 sentence is.
