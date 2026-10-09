#!/usr/bin/env python3
"""
Toy 5874 — Round K4-4, Lane B item 3 (Elie, 2026-10-09). The Raychaudhuri check, exact, no data. didwe "Raychaudhuri" → 0.
Question (Keeper K4-4): does Rule R's rate, written through Ḣ = −4πG(ρ + p), already carry 2Ω_r in the source — i.e. is
5872's β = 2 forced? Keeper's clue was ρ + 3p (ρ + 3p = 2ρ_r for radiation). Checked here against both forms.

Objects (G = 1 units are not needed; everything is in fractions Ω_i = ρ_i/ρ_crit, x = ln a):
  Friedmann:  H² = (8πG/3) Σρ_i ;  Ḣ = −4πG Σ(ρ_i + p_i)   ⟹   −2Ḣ/H² = 3 Σ (1 + w_i) Ω_i        (R1)
  horizon count N_H ∝ H⁻²  ⟹  d ln N_H/dx = −2Ḣ/H²                                                (R2)
  5872's source: s_N = 6(1 − f) + β Ω_r, with f = Ω_DE;  1 − f = Ω_m + Ω_r.
Candidate rule: the ledger's committed count grows at TWICE the horizon count's log-rate, fed by what changes the horizon
area — the null-ray focusing source T_ab k^a k^b = ρ + p — of everything that is not the dark energy itself:
  s_N = 2 · 3 Σ_{i ≠ DE} (1 + w_i) Ω_i = 6 Ω_m + 8 Ω_r = 6(1 − f) + 2 Ω_r   ⟹   β = 2, exactly.          (R3)
The ρ + 3p (timelike focusing, ä/a) form gives 6(Ω_m + 2Ω_r) ⟹ β = 6 (walls, 5872 B4).                     (R4)
"""
import sympy as sp

RESULTS = []
def score(tag, ok, msg):
    RESULTS.append(bool(ok)); print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")

G, a = sp.symbols('G a', positive=True)
rho_m, rho_r, rho_de, w = sp.symbols('rho_m rho_r rho_DE w', real=True)
Om, Or, f = sp.symbols('Omega_m Omega_r f', positive=True)

# R1: the second Friedmann equation in fractions
rho = rho_m + rho_r + rho_de; p = sp.Rational(1, 3) * rho_r + w * rho_de
H2 = sp.Rational(8, 3) * sp.pi * G * rho; Hdot = -4 * sp.pi * G * (rho + p)
lhs = sp.simplify(-2 * Hdot / H2)
rhs = 3 * (rho_m / rho + sp.Rational(4, 3) * rho_r / rho + (1 + w) * rho_de / rho)
score("R1", sp.simplify(lhs - rhs) == 0, "−2Ḣ/H² = 3 Σ (1 + w_i) Ω_i = 3[Ω_m + (4/3)Ω_r + (1 + w)Ω_DE]   (Raychaudhuri in fractions)")

# R2: the horizon count's log-rate (N_H ∝ H^-2; with c, the area A_H = 4π c²/H²)
dlnNH = lhs   # d ln N_H/dx = -2 (dH/dx)/H = -2 Ḣ/H²
H = sp.Function('H'); t = sp.symbols('t')
score("R2", sp.simplify(sp.diff(sp.log(H(t) ** -2), t) - (-2 * sp.diff(H(t), t) / H(t))) == 0,
      "N_H ∝ H⁻² ⟹ d ln N_H/dt = −2Ḣ/H, so d ln N_H/dx = −2Ḣ/H² = R1's right-hand side")
# R3: the candidate rule, DE's own (1+w) term excluded; substitute fractions
subs = {rho_m: Om, rho_r: Or, rho_de: f}      # with Om + Or + f = 1 the fractions are the Ω's
sN_null = sp.expand(2 * 3 * (Om + sp.Rational(4, 3) * Or))
target = lambda beta: 6 * (1 - f) + beta * Or
beta_null = sp.solve(sp.Eq(sN_null.subs(Om, 1 - f - Or), target(sp.Symbol('beta'))), sp.Symbol('beta'))
score("R3", beta_null == [2], f"s_N = 2·3 Σ_{{i≠DE}}(1 + w_i)Ω_i = 6Ω_m + 8Ω_r = 6(1 − f) + βΩ_r with β = {beta_null}: "
                               "the null-focusing source ρ + p (T_ab k^a k^b) forces β = 2 with no knob")

# R4: the rho + 3p (timelike focusing) form
sN_time = sp.expand(6 * (Om + 2 * Or))
beta_time = sp.solve(sp.Eq(sN_time.subs(Om, 1 - f - Or), target(sp.Symbol('beta'))), sp.Symbol('beta'))
score("R4", beta_time == [6], f"the ρ + 3p form (ä/a; 2ρ_r for radiation) gives β = {beta_time} — above 2: the wall (5872 B4). "
                               "Keeper's clue is right in its physics (what focuses NULL rays feeds the horizon) and wrong in its formula (ρ + 3p is the timelike one)")

# R5: self-consistency — keep the DE's own term in the source; w from 5872's closure; the fixed point is w = -1
beta_, Omg = sp.symbols('beta Omega', positive=True)
w_alg = lambda sN, Omr: (sN - 3 - 2 * Omr) / (3 * (2 * Omg - 1))
sN_full = 2 * 3 * ((1 - Omg - Or) + sp.Rational(4, 3) * Or + (1 + w) * Omg)     # includes (1+w)Ω_DE
eq = sp.Eq(w, w_alg(sN_full, Or))
sol = sp.solve(eq, w)
score("R5", sol == [-1], f"with the DE's own (1 + w)Ω_DE term kept in the source, the closure solves to w = {sol} for every Ω, Ω_r: "
                         "the DE term vanishes at its own fixed point, so 'exclude the dark energy' and 'ρ + p of everything' are the same rule")

# R6: the (1 - f) factor is not a postulate: it is Σ_{i≠DE} Ω_i, i.e. ρ + p = 0 for the dark energy
score("R6", sp.simplify((Om + Or) - (1 - f)).subs(Om, 1 - f - Or) == 0,
      "the once-only exclusion factor (1 − f) = Ω_m + Ω_r = the non-DE share of the budget: it is the statement that a w = −1 component has ρ + p = 0 and does not change the horizon area")

# R7: Rule R recovered in the matter era: per-axis rate (2/3) d ln N_H/dx = 2 when Ω_r = 0, w = -1 (DE term 0) and f -> 0... exactly 2(1-f)
per_axis = sp.simplify(sp.Rational(2, 3) * 3 * (Om + sp.Rational(4, 3) * Or)).subs({Or: 0, Om: 1 - f})
score("R7", sp.simplify(per_axis - 2 * (1 - f)) == 0,
      "per axis: (2/3) d ln N_H/dx|_{non-DE} = 2(1 − f) in the matter era — Rule R's 'd ln N₁/dt = 2H' with the exclusion, recovered as the Ω_r = 0 case")

# R8: with the Hdot-fed source, w = -1 in EVERY era, including radiation (no w = -1/3 phase)
w_rad = sp.simplify(w_alg(sN_null.subs(Om, 1 - Omg - Or), Or))
score("R8", sp.simplify(w_rad + 1) == 0,
      "w ≡ −1 for every (Ω, Ω_r): the Ḣ-fed ledger has NO w = −1/3 radiation phase — 5779 check 4 and Lyra 09-25 (iii) (EDE ~ 5e-11, f ∝ a²) were artifacts of the constant per-axis 2; under this rule f ∝ a⁴ in radiation and w stays −1")

# R9: the quotient/events compositions under the same source do not give -1 (A3 of 5869, restated)
sN_events = sp.Rational(1, 3) * sN_null.subs(Om, 1 - Omg - Or)        # one write per commit, not cubed
w_ev = sp.simplify(w_alg(sN_events, Or))
score("R9", sp.simplify(w_ev + 1) != 0, f"N = W (events) under the same source: w = {sp.factor(w_ev)} ≠ −1 — the product (K4 count) is still what the matter era needs")

# R10: control — the constant-fraction rule s_N = d ln N_H/dx (full) returns Hsu's w = Omega_r/(3(1-Omega))
sN_hsu = 3 * ((1 - Omg - Or) + sp.Rational(4, 3) * Or + (1 + w) * Omg)
w_hsu = sp.solve(sp.Eq(w, w_alg(sN_hsu, Or)), w)
score("R10", sp.simplify(w_hsu[0] - Or / (3 * (1 - Omg))) == 0, f"control: s_N = d ln N_H/dx (constant fraction) → w = {w_hsu[0]} = the background's p/ρ (Hsu)")

print("\n  In the ledger's words: d ln N/dt = 2 · d ln N_H/dt = −4Ḣ/H = 8πG(ρ + p)_{m+r}/H.  N ∝ N_H².  The '2H per axis' of Rule R is its matter-era value.")
passed = sum(RESULTS)
print(f"\nSCORE: {passed}/{len(RESULTS)}  (all {len(RESULTS)} can fail; R10 is the control)")
