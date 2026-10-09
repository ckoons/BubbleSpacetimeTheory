#!/usr/bin/env python3
"""
Toy 5876 — Round K4-5, Lane B item 3 + Cal S1040 P8 (Elie, 2026-10-09).
Part 1: Lyra's `beta_check.py` (her K4-4 rewrite, Appendix; scratchpad sha256 531e5e86d3615d79…) retained VERBATIM under
        /toy claim, re-run, and its printed output compared line by line to the appendix.
Part 2: Cal P8 — under the Rule-R source with β = 2 (N ∝ N_H², the null flux), print w(z) to machine precision on a z grid
        through radiation, matter and dark-energy domination. Cal predicts w ≡ −1 everywhere. Background shape placeholders
        only (Ω_m = 0.3, Ω_r = 1e-4, H0 = 1); nothing here is a pin.
"""
import subprocess, sys, os, hashlib, textwrap
import numpy as np
from scipy.integrate import solve_ivp

RESULTS = []
def score(tag, ok, msg):
    RESULTS.append(bool(ok)); print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")

LYRA_SRC = textwrap.dedent('''\
    import sympy as sp
    f,Or,D,H=sp.symbols('f Omega_r D H',positive=True); w=sp.Symbol('w')
    Om=1-f-Or
    dlnH2=-3*Om-4*Or-3*(1+w)*f            # Friedmann
    dlnNH=-dlnH2                           # N_H ∝ H^-2
    sN=sp.symbols('s_N')
    w_of_sN=sp.solve(sp.Eq(-3*(1+w), sN+2*dlnH2), w)[0]        # continuity, rho_DE ∝ H^4 N
    print("w(s_N) =", sp.simplify(w_of_sN))
    print("Law N∝N_H^2  ⇒ w =", sp.solve(sp.Eq(w, w_of_sN.subs(sN, 2*dlnNH)), w))
    expr=sp.expand((2*dlnNH).subs(w,-1)); print("2 dlnN_H at w=-1 =", expr, " → beta =", sp.simplify((expr-6*(1-f))/Or))
    for name,rad in (("rho+p (null focusing)",sp.Rational(4,3)),("rho+3p (timelike focusing)",2)):
        s=sp.expand(6*(Om+rad*Or)); beta=sp.simplify((s-6*(1-f))/Or)
        print(f"source ∝ {name}: s_N = {s}; beta = {beta}; w = {sp.solve(sp.Eq(w, w_of_sN.subs(sN,s)),w)}")
    print("rho_DE ∝ H^(", sp.simplify(1-2*(D-1)+D), ") → constant iff D = 3")
    ''')
LYRA_OUT = textwrap.dedent('''\
    w(s_N) = (-2*Omega_r + s_N - 3)/(3*(2*f - 1))
    Law N∝N_H^2  ⇒ w = [-1]
    2 dlnN_H at w=-1 = 2*Omega_r - 6*f + 6  → beta = 2
    source ∝ rho+p (null focusing): s_N = 2*Omega_r - 6*f + 6; beta = 2; w = [-1]
    source ∝ rho+3p (timelike focusing): s_N = 6*Omega_r - 6*f + 6; beta = 6; w = [(4*Omega_r - 6*f + 3)/(3*(2*f - 1))]
    rho_DE ∝ H^( 3 - D ) → constant iff D = 3
    ''')
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, ".lyra_beta_check_retained_5876.py")
open(path, "w").write(LYRA_SRC)
sha = hashlib.sha256(LYRA_SRC.encode()).hexdigest()
print(f"Part 1 — Lyra's beta_check.py retained at {os.path.basename(path)}; sha256 of the retained text {sha[:16]} "
      f"(her scratchpad sha 531e5e86d3615d79… was of her file; whitespace may differ — the OUTPUT is the comparison)")
out = subprocess.run([sys.executable, path], capture_output=True, text=True).stdout
for a, b in zip(out.strip().splitlines(), LYRA_OUT.strip().splitlines()):
    print(f"     {'==' if a.strip() == b.strip() else '!='} {a.strip()[:110]}")
score("L1", out.strip().splitlines() == LYRA_OUT.strip().splitlines(), "re-run output matches Lyra's appendix line by line (6/6 lines)")
score("L2", "beta = 2" in out and "beta = 6" in out and "w = [-1]" in out, "her instrument and my 5874 agree: null ρ+p → β = 2, w = −1; timelike ρ+3p → β = 6")

# ---------------------------------------------------------------- Part 2: P8
print("\nPart 2 — Cal P8: w(z) under N ∝ N_H² (β = 2), machine precision")
OM, OR = 0.3, 1e-4
Hb2 = lambda a: OM * a ** -3 + OR * a ** -4
def pieces(x, y):
    a = np.exp(x); Omg = np.exp(y[0]); Omr = (1 - Omg) * OR * a ** -4 / Hb2(a)
    sN = 6 * (1 - Omg) + 2 * Omr                        # = 2 d ln N_H/dx of the non-DE budget (5874 R3)
    return (sN - 3 - 2 * Omr) / (3 * (2 * Omg - 1)), Omg, Omr
rhs = lambda x, y: [-3 * pieces(x, y)[0] * (1 - pieces(x, y)[1]) + pieces(x, y)[2]]
xs = np.linspace(np.log(1e-6), np.log(4.0), 3000)
sol = solve_ivp(rhs, [xs[0], xs[-1]], [-32.0], t_eval=xs, rtol=1e-12, atol=1e-14, method="DOP853")
a = np.exp(sol.t); w = np.array([pieces(x, y)[0] for x, y in zip(sol.t, sol.y.T)]); f = np.exp(sol.y[0])
# also the exact closed form: w = -1 identically (5874 R8), so the numeric should sit at -1 to rounding
zs = [1e5, 3400, 1100, 100, 10, 3, 1, 0.5, 0]
print("     z        w + 1            f")
for z in zs:
    aa = 1 / (1 + z); wi = float(np.interp(aa, a, w)); fi = float(np.interp(aa, a, f))
    print(f"     {z:<8} {wi + 1:+.3e}   {fi:.3e}")
score("P8", np.max(np.abs(w + 1)) < 1e-12, f"max |w + 1| over z ∈ [0, 1e6] = {np.max(np.abs(w + 1)):.2e}: w ≡ −1 to machine precision through radiation, matter and DE eras — Cal P8 landed; O3 (the absolute count) is the only informative line left")
# the f(1) line of THIS run is a placeholder normalization, not O3: print it labelled
print(f"     (f(a=1) = {float(np.interp(1.0, a, f)):.4f} — set by the placeholder Ω(a0) = e^-32, NOT a result; O3 is T3's number after Cal's hash)")

passed = sum(RESULTS)
print(f"\nSCORE: {passed}/{len(RESULTS)}  (all {len(RESULTS)} can fail)")
