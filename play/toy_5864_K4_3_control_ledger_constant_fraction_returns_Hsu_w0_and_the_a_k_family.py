#!/usr/bin/env python3
"""
Toy 5864 — Round K4-3, Lane B (Elie, 2026-10-09). Prereg: notes/Elie_K4-3_prereg_toys_5864-5867_* (976951e1).

The control ledger. Objects (Lyra FILLING_LAW 09-22 Sec. 3): rho_DE = E_commit N / V_H, E_commit = hbar H ln2/(2 pi),
N = f N_H, N_H = 4 pi/(H^2 l_P^2), V_H = (4 pi/3) H^-3  =>  rho_DE = f (3 ln2/2 pi)(hbar/l_P^2) H^2, Omega_DE = 4 ln2 f.
w = -1 - (1/3) dln rho_DE/dln a.  Two readings of H: (T) test field on a fixed background; (S) self-consistent Friedmann.
Reads NOTHING cosmological. The only fractions run are the constant control and the a^k family (K1922 / Lyra check 5).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import sympy as sp
from _k4_3_lib_loader import lib
w_of_a, w_ode, LN2 = lib.w_of_a, lib.w_ode, lib.LN2

RESULTS = []
def score(tag, ok, msg):
    RESULTS.append((tag, bool(ok))); print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")

# ---------------------------------------------------------------- symbolic (exact)
a, k, Om0, n = sp.symbols('a k Omega_0 n', positive=True)
f_sym = Om0 * a ** k                       # Omega(a) = 4 ln2 f(a) = Omega_0 a^k
rho_T = (f_sym) * a ** (-n)                # test field: H^2 ~ a^-n
rho_S = f_sym / (1 - f_sym) * a ** (-n)    # self-consistent: rho_DE = Omega rho_m/(1 - Omega)
def w_sym(rho):
    return sp.simplify(-1 - sp.Rational(1, 3) * sp.diff(sp.log(rho), a) * a)
wT, wS = w_sym(rho_T), w_sym(rho_S)

print("SYMBOLIC")
print(f"  (T) w = {wT}")
print(f"  (S) w = {wS}")
c1 = sp.simplify(wT.subs({k: 0, n: 3})) == 0 and sp.simplify(wS.subs({k: 0, n: 3})) == 0
c1r = sp.simplify(wT.subs({k: 0, n: 4}) - sp.Rational(1, 3)) == 0 and sp.simplify(wS.subs({k: 0, n: 4}) - sp.Rational(1, 3)) == 0
score("C1", c1, "constant fraction => w = 0 identically in BOTH readings in the matter era (Hsu; the control)")
# PREREG ERROR, owned: I wrote 'every era'. A constant fraction tracks the DOMINANT fluid: w = 1/3 in radiation, not 0.
# First run scored this as a FAIL of the instrument; the instrument was right and the prereg sentence was wrong.
score("C1r", c1r, "constant fraction in the RADIATION era => w = +1/3 (tracks radiation) in both readings — prereg said 0; the prereg was wrong, reported")

c2 = (sp.simplify(wT.subs(n, 3) - (-k / 3)) == 0 and sp.simplify(wT.subs(n, 4) - (1 - k) / 3) == 0
      and wT.subs({n: 3, k: 3}) == -1 and wT.subs({n: 4, k: 2}) == sp.Rational(-1, 3))
score("C2", c2, "(T) f ~ a^k: w = -k/3 (matter), (1-k)/3 (radiation); k=3 -> -1 (K1922 product a^6/a^3); k=2 radiation -> -1/3 (K1922 C5)")

Om = sp.symbols('Omega', positive=True)
wS_k = sp.simplify(wS.subs(n, 3).subs(Om0 * a ** k, Om))
c3 = (sp.simplify(wS.subs({n: 3, k: 0})) == 0
      and sp.simplify(wS.subs(n, 3) - (-k / (3 * (1 - Om0 * a ** k)))) == 0
      and all(float(wS.subs({n: 3, k: 3, Om0: 1, a: x})) < -1 for x in (0.1, 0.5, 0.9)))
score("C3", c3, "(S) f ~ a^k: w = -k/(3(1-Omega)); constant -> 0; k=3 -> w < -1 for 0<Omega<1 (Lyra check-5 phantom, re-derived); Omega -> 1 is a wall")

# the Hsu identity: constant Omega => H^2 = (8piG/3) rho_m /(1-Omega) tracks matter exactly
H2 = sp.symbols('H2'); rho_m = sp.symbols('rho_m', positive=True); Oc = sp.symbols('Omega_c', positive=True)
sol = sp.solve(sp.Eq(H2, rho_m + Oc * H2), H2)[0]        # 8piG/3 = 1 units
c5 = sp.simplify(sol - rho_m / (1 - Oc)) == 0
score("C5", c5, f"constant Omega: H^2 = rho_m/(1-Omega) exactly => tracks matter; w = 0 is the same fact (H^2 = {sol})")

# ---------------------------------------------------------------- numeric (two routes: finite-difference grid and ODE)
print("NUMERIC")
grid = np.exp(np.linspace(np.log(1e-3), np.log(0.5), 600))
worst = 0.0
for era, nn in (("matter", 3), ("radiation", 4)):
    for kk in (0, 1, 2, 3):
        for Omz in (1e-3, 0.3):
            fk = lambda x, kk=kk, Omz=Omz: Omz * x ** kk / (4 * LN2)      # f such that Omega = Omz a^k (Omega < 1 on the grid)
            for reading, expr in (("T", wT), ("S", wS)):
                w_num, Omn = w_of_a(fk, reading, grid, era=era)
                w_ex = np.array([float(expr.subs({n: nn, k: kk, Om0: Omz, a: x})) for x in grid])
                err = np.max(np.abs(w_num[5:-5] - w_ex[5:-5]))
                worst = max(worst, err)
            _, w_o = w_ode(fk, "S", 1e-3, 0.5, era=era, npts=50)
            w_ex_o = np.array([float(wS.subs({n: nn, k: kk, Om0: Omz, a: x})) for x in np.exp(np.linspace(np.log(1e-3), np.log(0.5), 50))])
            worst = max(worst, np.max(np.abs(w_o - w_ex_o)))
score("C4", worst < 1e-8, f"grid + ODE routes reproduce the symbolic w on k in {{0..3}}, Omega_0 in {{1e-3, 0.3}}, both eras, both readings: max |dw| = {worst:.2e}")

# print the family once, as a table (no physical f is run)
print("  table (S, matter, Omega_0 = 0.3 at a = 1 extrapolated; w at a = 0.1 / 0.5):")
for kk in (0, 1, 2, 3):
    vals = [float(wS.subs({n: 3, k: kk, Om0: 0.3, a: x})) for x in (0.1, 0.5)]
    print(f"    k = {kk}: w(0.1) = {vals[0]:+.4f}, w(0.5) = {vals[1]:+.4f}")

passed = sum(ok for _, ok in RESULTS)
print(f"\nSCORE: {passed}/{len(RESULTS)}  (all {len(RESULTS)} can fail; control = C1)")
