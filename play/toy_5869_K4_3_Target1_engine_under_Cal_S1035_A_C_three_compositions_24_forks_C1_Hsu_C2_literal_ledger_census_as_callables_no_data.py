#!/usr/bin/env python3
"""
Toy 5869 — Round K4-3, Lane B, Target 1 ENGINE (Elie, 2026-10-09). Built on Lyra's rate law (54a5c539, sha 4b868c9f)
as ruled CONDITIONAL by Cal S1035 (badad661), Conditions A–C applied. Reads NO cosmological pin. The census enters as
callables; only the two controls and a SYNTHETIC shape (labelled, meaningless numbers) are run here.

Objects (Lyra Sec. 2, inputs i–xii):
  A(a)      cumulative comoving absorption count density counted as commits (the census integral; Engine A)
  W(a)      committed EVENTS inside the Hubble volume = (A/eta_gamma) a^-3 V_H(a)               [Cal A: primary]
  N         the charged count: {W (events), W^3 (capacity; the P-substrate fork), W/3 (quotient control)}
  X(f)      saturation on the SOURCE: exclusion (1-f) | hard wall | none            (Lyra's clause; forks)
  N_H       {S_BH/ln2 (bits): Omega_DE = f ;  A_H/l_P^2 (rule R): Omega_DE = 4 ln2 f}
  rho_DE = E_commit N / V_H, E = hbar H ln2/(2 pi)  =>  rho_DE = kappa f rho_crit, kappa in {1, 4 ln2}
  Friedmann: H^2 = H_b^2(a)/(1 - Omega),  H_b^2 = H0^2 (Om a^-3 + Or a^-4)   (background SHAPE; placeholders, not pins)
  w from continuity: 1 + w = -(1/3) d ln rho_DE/dx,  d ln rho_DE/dx = d ln N/dx + 2 d ln H^2/dx,  x = ln a
Dynamics:  d ln N/dx = m s_1 X(f),  m = 3 (capacity) or 1 (events, quotient);  s_1 = d ln W/dx = (dA/dx)/A - 3 + d ln V_H/dx.
Closure (exact): with g = kappa N H_b^2/c_H,  Omega(1-Omega) = g; d ln H^2/dx = D + q (s_N + D), D = d ln H_b^2/dx,
  q = Omega/(1-2 Omega); s_1 solved linearly from that (no quasi-static step). Omega(1-Omega) <= 1/4 is a WALL:
  a fork that pushes g past 1/4 has no Friedmann solution (reported). Omega = 1/2 is crossed only where s_N + D = 0.
Controls: C1 (Hsu) constant f -> w = the background's own p/rho (0 in matter, 1/3 in radiation; the 5864 lesson).
          C2 (literal ledger) d ln W/dx = 2, capacity, exclusion -> 5779 check 5: w = -1 identically late, -1/3 in
          radiation; no-exclusion -> phantom then the wall; rule R -> the wall (4 ln2 > 1); quotient/events: not -1.
The one free number of Engine B (the initial count; Lyra's T3) is set by SHOOTING to a declared f(a=1) for the controls;
in the real run the census fixes it (that is T3). Outputs O1–O3 and T1 printed per fork; direction before size.
"""
import itertools, signal
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

RESULTS, CANFAIL = [], []
def score(tag, ok, msg, canfail=True):
    RESULTS.append(bool(ok)); CANFAIL.append(canfail); print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")

LN2 = float(np.log(2.0))
OM_PLACEHOLDER, OR_PLACEHOLDER = 0.3, 1e-4        # background SHAPE placeholders for Grace's pins; never read as results
KAPPA = {"bits": 1.0, "ruleR": 4 * LN2}
MULT = {"events": 1, "capacity": 3, "quotient": 1}
XFUN = {"exclusion": lambda f: max(1 - f, 0.0), "wall": lambda f: 1.0 if f < 1 else 0.0, "none": lambda f: 1.0}
C_H = 1.0                                          # N_H = C_H/H^2 ; units: N in N_H(a = 1, H = H0 = 1)

def Hb2(a, Om=OM_PLACEHOLDER, Or=OR_PLACEHOLDER): return Om * a ** -3 + Or * a ** -4
def D_of(a, Om=OM_PLACEHOLDER, Or=OR_PLACEHOLDER): return (-3 * Om * a ** -3 - 4 * Or * a ** -4) / Hb2(a, Om, Or)
def w_bg(a, Om=OM_PLACEHOLDER, Or=OR_PLACEHOLDER): return (Or * a ** -4 / 3) / Hb2(a, Om, Or)

def w_alg(sN, Omg, Omr):
    """Ledger (Omega ∝ N H^2) and continuity (rho_DE ∝ a^-3(1+w)) both give d ln Omega/dx; equating them:
       w = (s_N - 3 - 2 Omega_r) / (3 (2 Omega - 1)).   Checks: s_N = d ln N_H/dx -> w = Omega_r/(3(1-Omega)) (Hsu);
       s_N = 6(1-f), Omega = f -> w = -1; s_N = 2 -> -1/(6f-3).  Omega = 1/2 is a pole unless s_N = 3 + 2 Omega_r there."""
    return (sN - 3 - 2 * Omr) / (3 * (2 * Omg - 1))

def run_engine(comp, sat, norm, a0, a1, lnOm0, census=None, A0=0.0, ledger_rule=None, npts=2000, w_cap=50.0, Or=OR_PLACEHOLDER):
    """State (A, ln Omega). census(a) -> dA/dx. ledger_rule: force s_1 (the literal ledger) and ignore the census.
    d ln Omega/dx = -3 w (1 - Omega) + Omega_r, with w algebraic (w_alg). A pole of w (|w| > w_cap) is the WALL:
    the Friedmann closure Omega(1-Omega) = kappa N H_b^2/c_H has no solution past 1/4 — the same wall, no branch logic."""
    kappa, m, X = KAPPA[norm], MULT[comp], XFUN[sat]
    def pieces(x, y):
        a = np.exp(x); A, lnOm = y; Omg = np.exp(lnOm); f = Omg / kappa
        Omr = (1 - Omg) * Or * a ** -4 / Hb2(a, OM_PLACEHOLDER, Or)
        c = m * X(f)
        if ledger_rule is not None:
            dA, s1 = 0.0, ledger_rule
        else:
            dA = census(a); dlnA = dA / A if A > 0 else 0.0
            # s1 = dlnA - 3 + d ln V_H/dx,  d ln V_H/dx = (9/2)(1 + Omega_r/3 + w Omega), w = w_alg(c s1, ...): linear in s1
            K = dlnA - 3 + 4.5 * (1 + Omr / 3)
            den = 3 * (2 * Omg - 1)
            coef = 4.5 * Omg * c / den; const = 4.5 * Omg * (-3 - 2 * Omr) / den
            s1 = (K + const) / (1 - coef) if abs(1 - coef) > 1e-12 else 0.0
        sN = c * s1
        w = w_alg(sN, Omg, Omr)
        return dA, sN, w, Omg, Omr
    def rhs(x, y):
        dA, sN, w, Omg, Omr = pieces(x, y)
        return [dA, -3 * w * (1 - Omg) + Omr]
    def wall_event(x, y):
        return w_cap - abs(pieces(x, y)[2])
    wall_event.terminal = True; wall_event.direction = -1
    xs = np.linspace(np.log(a0), np.log(a1), npts)
    if wall_event(xs[0], [A0, lnOm0]) <= 0:
        return dict(a=np.array([a0]), wall=a0, f=np.array([np.nan]), w=np.array([np.nan]), dlnN=np.array([np.nan]), A=np.array([A0]), Omega=np.array([np.nan]))
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError()))
    signal.alarm(25)
    try:
        sol = solve_ivp(rhs, [xs[0], xs[-1]], [A0, lnOm0], t_eval=xs, rtol=1e-10, atol=1e-13, method="DOP853", events=wall_event)
    except TimeoutError:
        return dict(a=np.array([a0]), wall="STALL", f=np.array([np.nan]), w=np.array([np.nan]), dlnN=np.array([np.nan]), A=np.array([A0]), Omega=np.array([np.nan]))
    finally:
        signal.alarm(0)
    a, A, lnOm = np.exp(sol.t), sol.y[0], sol.y[1]
    wall = float(np.exp(sol.t_events[0][0])) if sol.status == 1 else None
    if len(a) < 10:
        return dict(a=np.array([a0]), wall=wall, f=np.array([np.nan]), w=np.array([np.nan]), dlnN=np.array([np.nan]), A=np.array([A0]), Omega=np.array([np.nan]))
    out = np.array([pieces(x, y) for x, y in zip(sol.t, sol.y.T)])
    sN, w, Omg = out[:, 1], out[:, 2], out[:, 3]
    return dict(a=a, f=Omg / kappa, Omega=Omg, w=w, dlnN=sN, A=A, wall=wall)

def shoot_lnOm0(comp, sat, norm, a0, a1, f_target, census=None, A0=0.0, ledger_rule=None, lo=-60, hi=-3, Or=OR_PLACEHOLDER):
    """Engine B's one free number (Lyra T3): pick Omega(a0) so that f(a = 1) = f_target in THIS fork."""
    def miss(lnOm0):
        r = run_engine(comp, sat, norm, a0, a1, lnOm0, census, A0, ledger_rule, npts=600, Or=Or)
        if r["wall"] == "STALL": return 1.0
        if r["wall"] is not None and r["wall"] <= 1.0: return 1.0
        return float(np.interp(1.0, r["a"], r["f"])) - f_target
    return brentq(miss, lo, hi, xtol=1e-9)

def cpl_direction(a, w, lo=0.5, hi=1.0):
    msk = (a >= lo) & (a <= hi) & np.isfinite(w)
    if msk.sum() < 5: return None, None
    A = np.vstack([np.ones(msk.sum()), 1 - a[msk]]).T
    return tuple(np.linalg.lstsq(A, w[msk], rcond=None)[0])

# ====================================================================== the algebra of the controls (exact)
print("ALGEBRA (exact; Omega_DE = f, pure matter background)")
f_, w_, s_ = sp.symbols('f w s')
def w_of_sN(sN): return sp.solve(sp.Eq(sN - 3 * (1 + w_ * f_), -3 * w_ * (1 - f_)), w_)
w_C1, w_C2_ex, w_C2_no, w_C2_q, w_ev = (w_of_sN(3 * (1 + w_ * f_)), w_of_sN(6 * (1 - f_)), w_of_sN(6), w_of_sN(2), w_of_sN(s_ * (1 - f_)))
print(f"  C1 constant f: w = {w_C1};  C2 capacity+exclusion: w = {w_C2_ex};  none: w = {w_C2_no};  quotient: w = {w_C2_q}")
print(f"  N = W with source s(1-f): w = {w_ev}  -> w = -1 iff s = 6 at every f (Cal S1035 Condition A, T1)")
score("A1", w_C1 == [0], "constant fraction ⇒ w = 0 exactly (Hsu)")
score("A2", w_C2_ex == [-1] and sp.simplify(w_C2_no[0] - 1 / (2 * f_ - 1)) == 0 and w_C2_q != [-1],
      "literal ledger: capacity+exclusion w = −1 identically; no exclusion 1/(2f−1); quotient ≠ −1 (5779 check 5 + K1922)")
score("A3", sp.simplify(w_ev[0].subs(s_, 6) + 1) == 0 and sp.simplify(w_ev[0].subs(s_, 2) + 1) != 0,
      "N = W needs d ln W/dx = 6 for w = −1; slope 2 does not")

# ====================================================================== C1 through the engine's w formula
print("\nENGINE — C1 (Hsu): N = f0 N_H(a) at fixed f0; w must equal the BACKGROUND's p/rho (0 matter, 1/3 radiation)")
worst = 0.0
for norm in KAPPA:
    for f0 in (0.05, 0.2):
        kappa = KAPPA[norm]; a = np.exp(np.linspace(np.log(1e-6), 0, 1200))
        Omg = kappa * f0 * np.ones_like(a); H2 = Hb2(a) / (1 - Omg); N = f0 * C_H / H2
        w = -1 - (np.gradient(np.log(N), np.log(a)) + 2 * np.gradient(np.log(H2), np.log(a))) / 3
        worst = max(worst, np.max(np.abs(w[5:-5] - w_bg(a[5:-5]))))
score("C1", worst < 1e-6, f"constant f tracks the dominant fluid: max |w − w_bg| = {worst:.1e}; w_bg runs 1/3 → 0 across equality (5864's radiation lesson)")

# ====================================================================== C2 through the engine, by fork
print("\nENGINE — C2 (literal ledger d ln W/dx = 2) on 5779's PURE-MATTER background (Or = 0); Omega(a0) SHOT to f(1) = 0.7 in capacity+exclusion+bits, then reused")
a0, a1 = 1e-6, 4.0
lnOm0 = shoot_lnOm0("capacity", "exclusion", "bits", a0, a1, 0.7, ledger_rule=2.0, Or=0.0)
print(f"  shot Omega(a0 = 1e-6) = {np.exp(lnOm0):.3e} (Engine B's one free number; in the real run the census fixes it — T3)")
c2 = {}
for comp, sat, norm in (("capacity", "exclusion", "bits"), ("capacity", "none", "bits"), ("capacity", "wall", "bits"),
                        ("capacity", "exclusion", "ruleR"), ("quotient", "exclusion", "bits"), ("events", "exclusion", "bits")):
    r = run_engine(comp, sat, norm, a0, a1, lnOm0, ledger_rule=2.0, Or=0.0)
    a, w, f = r["a"], r["w"], r["f"]
    late = (a > 2.0) & np.isfinite(w)
    w_late = float(np.nanmedian(w[late])) if late.any() else np.nan
    w0, wa = cpl_direction(a, w)
    direction = "n/a" if wa is None else ("flat" if abs(wa) < 1e-3 else ("wa > 0, relaxing from above" if wa > 0 else "wa < 0"))
    f1 = float(np.interp(1.0, a, f)) if a[-1] >= 1.0 else np.nan
    c2[(comp, sat, norm)] = dict(w_late=w_late, wall=r["wall"], f1=f1, wa=wa, a=a, w=w, f=f)
    print(f"  {comp:<9}{sat:<10}{norm:<6}: wall {str(r['wall'])[:8] if r['wall'] else 'none':<8} direction {direction:<28} "
          f"w(late) = {w_late:+.4f}  f(1) = {f1:.3f}")
k = c2[("capacity", "exclusion", "bits")]
print(f"     exclusion fork: w at a = 0.3, 0.5, 0.7, 1.0 = {[round(float(np.interp(x, k['a'], k['w'])), 5) for x in (0.3, 0.5, 0.7, 1.0)]}; "
      f"f = {[round(float(np.interp(x, k['a'], k['f'])), 3) for x in (0.3, 0.5, 0.7, 1.0)]}")
score("C2", abs(k["w_late"] + 1) < 1e-3 and k["wall"] is None and abs(k["f1"] - 0.7) < 1e-3 and np.nanmax(k["f"]) > 0.9,
      "capacity+exclusion+bits, Or = 0: w = −1 identically, f crosses 1/2 and → 1, f(1) = 0.7 as shot — 5779 check 5 reproduced dynamically")
score("C2b", c2[("capacity", "none", "bits")]["wall"] is not None,
      f"no exclusion: phantom, then the WALL (w pole at Ω = 1/2) at a = {c2[('capacity', 'none', 'bits')]['wall']}")
score("C2c", c2[("capacity", "exclusion", "ruleR")]["wall"] is not None,
      f"rule-R normalization: the WALL at a = {c2[('capacity', 'exclusion', 'ruleR')]['wall']} (Lyra 09-25: 4 ln2 > 1, dynamically)")
score("C2d", abs(c2[("quotient", "exclusion", "bits")]["w_late"] + 1) > 0.1 and abs(c2[("events", "exclusion", "bits")]["w_late"] + 1) > 0.1,
      f"quotient / events at the ledger's slope 2 do not give −1 (w_late {c2[('quotient','exclusion','bits')]['w_late']:+.3f}, "
      f"{c2[('events','exclusion','bits')]['w_late']:+.3f}): K1922 and Condition A in the engine")

print("\nR1 — the radiation perturbation of the exclusion fork (NEW; can fail either way). Or = 1e-4; scan the one free number.")
print("     Algebra: the pole at Ω = 1/2 is removable iff s_N = 3 + 2Ω_r there; the exclusion source gives 3. In the radiation era")
print("     s_N = 6(1−f) = d ln N_H/dx = 4 at f = 1/3: a TRACKER (constant Ω_DE = 1/3, w = 1/3) exists while radiation dominates.")
print("     Prediction (Elie, before the scan): no Ω(a0) reaches f(1) = 0.7 with w = −1; the count is either captured by the")
print("     f = 1/3 tracker (early dark energy at 1/3 — dead by BBN/CMB in any real census) or pinned below 1/2 in the matter era.")
rows_r1 = []
for lnOm0_r in np.linspace(-52, -20, 9):
    r = run_engine("capacity", "exclusion", "bits", a0, a1, lnOm0_r, ledger_rule=2.0, Or=1e-4)
    if r["wall"] == "STALL":
        rows_r1.append((lnOm0_r, np.nan, np.nan, np.nan, np.nan, "STALL")); print(f"     Ω(a0) = e^{lnOm0_r:+.0f}: STALL (> 25 s: the stiff layer)"); continue
    a, w, f = r["a"], r["w"], r["f"]
    rad = (a < 3e-3) & np.isfinite(f); fr = float(np.nanmax(f[rad])) if rad.any() else np.nan     # up to ~10 a_eq
    f1 = float(np.interp(1.0, a, f)) if a[-1] >= 1 else np.nan
    late = (a > 2.0) & np.isfinite(w); wl = float(np.nanmedian(w[late])) if late.any() else np.nan
    fmax = float(np.nanmax(f))
    rows_r1.append((lnOm0_r, fr, fmax, f1, wl, r["wall"]))
    print(f"     Ω(a0) = e^{lnOm0_r:+.0f}: max f (a < 3e-3) = {fr:.4f}  max f = {fmax:.4f}  f(1) = {f1:.4f}  w(late) = {wl:+.5f}  wall {r['wall']}")
good = [x for x in rows_r1 if x[5] is None and np.isfinite(x[3])]
reach = any(x[3] >= 0.5 and abs(x[4] + 1) < 1e-2 for x in good)
pinned = [x for x in good if abs(x[2] - 0.5) < 1e-3 and abs(x[4]) < 1e-3]
tracker = [x for x in good if abs(x[1] - 1 / 3) < 0.03]
print(f"     any Ω(a0) with f(1) ≥ 0.5 and w(late) = −1: {reach};  pinned at f = 1/2 with w = 0: {len(pinned)}/{len(good)};  "
      f"near-equality tracker at 1/3 seen: {len(tracker)}/{len(good)}")
score("R1", (not reach) and len(pinned) >= 3 and len(good) >= 7,
      "exclusion fork with Or = 1e-4: NO normalization reaches f(1) ≥ 1/2 with w = −1; the ones that climb are PINNED at f = 1/2 with w → 0 (the s_N = 3 = d ln N_H/dx tracker) — 5779's w = −1 is the Or = 0 limit; for Lyra (T2) and Cal")
print(f"     (report, not scored) the algebraic radiation-era fixed point f = 1/3 (s_N = 6(1−f) = 4 = d ln N_H/dx) was reached in {len(tracker)} of these scan rows; an earlier run at Ω(a0) = 2.3e-18 peaked at f = 0.309 — a fixed point of the equations, not a result of this scan")

# ====================================================================== the 24-fork harness on a SYNTHETIC census
print("\nSYNTHETIC census (shape only; numbers meaningless by construction): dA/dx = S (a/a_on)^p for a > a_on")
A_ON, P = 1e-2, 3.0
forks = list(itertools.product(("chi≡1", "chi=1−f"), (1, 3), ("events", "capacity", "quotient"), ("bits", "ruleR")))
print(f"  forks: {len(forks)} = 2 χ × 2 η_γ × 3 composition × 2 N_H (Cal S1035). χ = 1 − f_local is run with f_local := f (a proxy, declared).")
# the synthetic S is set once (in the events/χ≡1/η=1/bits fork) so that W(1)/N_H(1) = 0.3; every other fork inherits it — T3's logic
def W_of_A(A, a, eta): return (A / eta) * a ** -3 * (1.0 / Hb2(a)) ** 1.5 * (4 * np.pi / 3)
A1_target = 0.3 / W_of_A(1.0, 1.0, 1)
S0 = A1_target / ((1 / A_ON) ** P / P)                 # A(1) = (S/P)(1/a_on)^p with the smooth start A(a_on) = S/P
rows = []; n_wall = 0; dirs = {"wa>0": 0, "wa<0": 0, "flat": 0, "n/a": 0}
for chi, eta, comp, norm in forks:
    def census(a, S=S0):
        return S * (a / A_ON) ** P if a >= A_ON else 0.0
    # χ = 1 − f_local is applied inside the engine's source as X on dA (proxy): emulate by scaling with (1 − f) through sat='exclusion' on N and ALSO on A
    sat = "exclusion"
    a_start = A_ON
    A_start = S0 / P; W0 = W_of_A(A_start, a_start, eta)        # A(a_on) = S/P: the power law continued smoothly below a_on
    N0 = {"events": W0, "capacity": W0 ** 3, "quotient": W0 / 3}[comp]
    lnOm0 = np.log(KAPPA[norm] * N0 * Hb2(a_start) / C_H)        # Omega(a_on) from the census count (Omega << 1 there)
    r = run_engine(comp, sat, norm, a_start, 3.0, lnOm0, census=census, A0=A_start)
    a, w, f, dlnN = r["a"], r["w"], r["f"], r["dlnN"]
    win = (a > 0.05) & (a < 0.25) & np.isfinite(w)
    slope = float(np.nanmedian(dlnN[win])) if win.any() else np.nan
    need = 6
    w0, wa = cpl_direction(a, w)
    d = "n/a" if wa is None else ("flat" if abs(wa) < 1e-3 else ("wa>0" if wa > 0 else "wa<0")); dirs[d] += 1
    n_wall += r["wall"] is not None
    f1 = float(np.interp(1.0, a, f)) if a[-1] >= 1 else np.nan
    rows.append((chi, eta, comp, norm, slope, d, f1, r["wall"]))
    print(f"   {chi:<8} η={eta} {comp:<9}{norm:<6}: O1 d ln N/dx (z≈3–19) = {slope:+8.3f} vs T1 need {need}; O2 direction {d:<5} O3 f(1) = {f1:.3e}; wall {str(r['wall'])[:7] if r['wall'] else '—'}")
print("  NOTE: in this harness χ = 1 − f_local collapses onto χ ≡ 1 (the proxy f_local := f is already the source's exclusion factor); the real χ fork needs Lyra's local f, declared as an input.")
score("H1", len(rows) == 24, f"harness runs all 24 forks ({n_wall} walls; directions {dirs}); SYNTHETIC — nothing here is the sky", canfail=False)
ev = [r for r in rows if r[2] == "events" and r[0] == "chi≡1" and r[1] == 1 and r[3] == "bits"][0]
cap = [r for r in rows if r[2] == "capacity" and r[0] == "chi≡1" and r[1] == 1 and r[3] == "bits"][0]
score("H2", abs(ev[4] - (P + 1.5)) < 0.3 and abs(cap[4] - 3 * (P + 1.5)) < 1.0,
      f"T1 bookkeeping: events slope ≈ p + 3/2 = {P + 1.5} (got {ev[4]:+.2f}: dA/dx ∝ a^p and V_H ∝ a^{{3/2}}); capacity ≈ 3× (got {cap[4]:+.2f}); so N = W needs p = 9/2 from the census — Cal's P5 is a statement about p")

passed = sum(RESULTS); n = len(RESULTS); cf = sum(CANFAIL)
print(f"\nSCORE: {passed}/{n}  ({cf} can fail; H1 is a harness check)")
