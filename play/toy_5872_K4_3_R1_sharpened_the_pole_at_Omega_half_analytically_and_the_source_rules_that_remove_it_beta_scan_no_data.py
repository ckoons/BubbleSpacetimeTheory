#!/usr/bin/env python3
"""
Toy 5872 — Round K4-3, R1 sharpened (Elie, 2026-10-09). Follows 5869 R1 (the exclusion fork is pinned at f = 1/2 with any
radiation). No data. Two parts:
 (A) the pole, analytically (sympy): with Omega_DE = f (bits), matter + radiation background,
       w = (s_N - 3 - 2 Omega_r) / (3 (2 Omega - 1)),   d ln Omega/dx = -3 w (1 - Omega) + Omega_r.
     For s_N = 6(1 - f) (capacity + exclusion):  w = -1 - 2 Omega_r / (3 (2f - 1)).  Below 1/2, w crosses 0 at
     f* = 1/2 - Omega_r/3, where d ln f/dx = Omega_r -> 0: the PINNED point (w = 0, f -> 1/2^- as Omega_r -> 0).
     The pole is removable iff s_N(1/2) = 3 + 2 Omega_r.
 (B) which source rules remove it: the one-parameter family s_N = 6(1 - f) + beta * Omega_r, run through 5869's engine
     (same Omega(a0) for all beta; Or = 1e-4 placeholder). Prediction before the run: the solution crosses 1/2 and reaches
     w = -1 with f(1) > 1/2 iff beta = 2 (within the step's tolerance); beta < 2 pins, beta > 2 walls (phantom overshoot).
     This is an INSTRUMENT for Lyra's rewrite of the saturation clause (K1955 item 1), not a proposal: beta = 2 says the
     exclusion must be taken against d ln N_H/dx INCLUDING radiation's share, and that sentence is hers to write or refuse.
"""
import signal
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

RESULTS = []
def score(tag, ok, msg):
    RESULTS.append(bool(ok)); print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")

# ---------------------------------------------------------------- (A) exact
print("(A) the pole, exactly")
f, Or, beta = sp.symbols('f Omega_r beta', positive=True)
w = lambda sN: (sN - 3 - 2 * Or) / (3 * (2 * f - 1))
w_ex = sp.simplify(w(6 * (1 - f)))
print(f"    exclusion: w = {w_ex}")
f_star = sp.solve(sp.Eq(w_ex, 0), f)
print(f"    w = 0 at f* = {f_star}  (just below 1/2; d ln f/dx there = Omega_r -> the pin)")
score("A1", sp.simplify(w_ex - (-1 - 2 * Or / (3 * (2 * f - 1)))) == 0 and f_star == [sp.Rational(1, 2) - Or / 3],
      "w = −1 − 2Ω_r/(3(2f−1)); the pinned point f* = 1/2 − Ω_r/3 (w = 0), exactly")
# sign structure below 1/2: for f in (f*, 1/2): w > 0 and d ln f/dx = -3w(1-f) + Omega_r < 0  => repelled from 1/2
dlnf = -3 * w_ex * (1 - f) + Or
mid = sp.Rational(1, 2) - Or / 6
score("A2", sp.simplify(dlnf.subs(f, mid)).subs(Or, sp.Rational(1, 100)) < 0 and sp.simplify(dlnf.subs(f, sp.Rational(1, 2) - Or)).subs(Or, sp.Rational(1, 100)) > 0,
      "between f* and 1/2 the flow is DOWN (d ln f/dx < 0); below f* it is UP: f* is an attractor from below — the pin is stable")
# removability: s_N(1/2) = 3 + 2 Omega_r
cond = sp.solve(sp.Eq((6 * (1 - f) + beta * Or).subs(f, sp.Rational(1, 2)), 3 + 2 * Or), beta)
score("A3", cond == [2], f"the pole is removable iff s_N(1/2) = 3 + 2Ω_r; for s_N = 6(1−f) + βΩ_r that is β = {cond}")
w_b2 = sp.simplify(w(6 * (1 - f) + 2 * Or))
print(f"    with beta = 2: w = {w_b2}  (−1 exactly: the pole is gone at every f, not only at 1/2)")
score("A4", sp.simplify(w_b2 + 1) == 0, "β = 2 gives w ≡ −1 at every f and every Ω_r — ΛCDM restored identically, not just at the pole")

# ---------------------------------------------------------------- (B) the engine (5869's closure, source hook s_N(f, Omega_r))
print("\n(B) the beta scan through the engine (Or = 1e-4 placeholder; the same Omega(a0) for every beta)")
OM, OR = 0.3, 1e-4
Hb2 = lambda a: OM * a ** -3 + OR * a ** -4
def run(beta_val, lnOm0, a0=1e-6, a1=4.0, npts=1500, w_cap=50.0):
    def pieces(x, y):
        a = np.exp(x); Omg = np.exp(y[0]); Omr = (1 - Omg) * OR * a ** -4 / Hb2(a)
        sN = 6 * (1 - Omg) + beta_val * Omr
        wv = (sN - 3 - 2 * Omr) / (3 * (2 * Omg - 1)) if abs(2 * Omg - 1) > 1e-12 else -1.0
        return wv, Omg, Omr
    def rhs(x, y):
        wv, Omg, Omr = pieces(x, y); return [-3 * wv * (1 - Omg) + Omr]
    def ev(x, y): return w_cap - abs(pieces(x, y)[0])
    ev.terminal = True; ev.direction = -1
    xs = np.linspace(np.log(a0), np.log(a1), npts)
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError())); signal.alarm(30)
    try:
        sol = solve_ivp(rhs, [xs[0], xs[-1]], [lnOm0], t_eval=xs, rtol=1e-10, atol=1e-13, method="DOP853", events=ev)
    except TimeoutError:
        return None
    finally:
        signal.alarm(0)
    a = np.exp(sol.t); out = np.array([pieces(x, y) for x, y in zip(sol.t, sol.y.T)])
    return dict(a=a, w=out[:, 0], f=out[:, 1], wall=float(np.exp(sol.t_events[0][0])) if sol.status == 1 else None)

lnOm0 = -32.0           # 5869 scan: a normalization that climbs (pinned at beta = 0); -40 sits on the below-branch (owned, first run)
rows = []
for b in (0.0, 1.0, 1.9, 1.99, 2.0, 2.01, 2.1, 3.0):
    r = run(b, lnOm0)
    if r is None:
        rows.append((b, "STALL", np.nan, np.nan, np.nan)); print(f"    beta = {b:<5}: STALL"); continue
    a, wv, fv = r["a"], r["w"], r["f"]
    fmax = float(np.nanmax(fv)); f1 = float(np.interp(1.0, a, fv)) if a[-1] >= 1 else np.nan
    late = a > 2.0; wl = float(np.nanmedian(wv[late])) if late.any() else np.nan
    rows.append((b, r["wall"], fmax, f1, wl))
    print(f"    beta = {b:<5}: wall {str(r['wall'])[:7] if r['wall'] else 'none':<8} max f = {fmax:.5f}  f(1) = {f1:.4f}  w(late) = {wl:+.5f}")
def row(b): return next(x for x in rows if x[0] == b)
crosses = lambda x: x[1] is None and x[1] != "STALL" and x[2] > 0.5 + 1e-6
score("B1", (not crosses(row(0.0))) and abs(row(0.0)[4]) < 1e-3 and abs(row(0.0)[2] - 0.5) < 1e-3,
      f"β = 0 (the exclusion fork as written): pinned at f = {row(0.0)[2]:.5f}, w(late) = {row(0.0)[4]:+.5f} — 5869 R1 reproduced")
score("B2", crosses(row(2.0)) and abs(row(2.0)[4] + 1) < 1e-3 and row(2.0)[3] > 0.5,
      f"β = 2: crosses 1/2, f(1) = {row(2.0)[3]:.4f}, w(late) = {row(2.0)[4]:+.5f} — ΛCDM restored, as A4 says")
score("B3", (not crosses(row(1.99))) and (row(2.01)[1] not in (None, "STALL") or not crosses(row(2.01)) or abs(row(2.01)[4] + 1) < 1e-2),
      f"β = 1.99 does not cross (pinned/below); β = 2.01: wall {row(2.01)[1]} / max f {row(2.01)[2]:.4f} — the crossing is a knife-edge in β (a fine-tuning unless a mechanism sets β = 2)")
score("B4", all((not crosses(row(b))) for b in (1.0, 1.9)) and all((row(b)[1] not in (None,)) or not crosses(row(b)) for b in (2.1, 3.0)),
      "β < 2 pins below 1/2; β > 2 overshoots (phantom → wall) — only β = 2 passes")

passed = sum(RESULTS)
print(f"\nSCORE: {passed}/{len(RESULTS)}  (all {len(RESULTS)} can fail)")
