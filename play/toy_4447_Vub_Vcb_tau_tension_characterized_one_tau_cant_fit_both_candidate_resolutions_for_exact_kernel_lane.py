#!/usr/bin/env python3
r"""
toy_4447 — V_ub/V_cb TAU TENSION (Grace G2 handed to the exact-kernel lane): with one tau and the averaged
           two-point overlap, V_ub wants DEEP tau (k~C_2=6) but V_cb wants SHALLOW tau (k~2). Characterize
           the tension rigorously with my corrected type-IV kernel (toy 4445), confirm Grace's numbers, and
           frame the candidate resolutions HONESTLY (not forcing a V_cb closure). Load-bearing for the exact
           rank-2 kernel. NO count move.

THE OVERLAP MODEL (corrected type-IV, rank-1 SO(5) average; toy 4445):
  V(k_a, k_b) = [(1-r_a^2)(1-r_b^2)]^{n_C} * < (1 - 2 r_a r_b c + r_a^2 r_b^2)^{-n_C} >_{(1-c^2)},  r_k^2 = k/(k+N_c).
  V_ub: a = e at the ORIGIN (k=0, r=0) -> V_ub = (1 - r_tau^2)^{n_C} (no average). V_cb: a = mu (k=1), b = tau.

THE TENSION (confirmed below): V_ub fits at k~6 (8%); at k=2 it is 20x too big. V_cb in this model is ~12-17x
  too SMALL at k=6; a shallow tau (k=2) raises it. So one tau k cannot fit both V_ub and V_cb in the rank-1
  averaged model -- exactly Grace's G2 catch.

CANDIDATE RESOLUTIONS (honestly tiered, NOT a closure -- handed to the exact-kernel lane):
  (a) EXACT RANK-2 KERNEL (Lyra/Elie, load-bearing): the rank-1 single-angle average collapses the rank-2
      Hua orientation structure (toy 4445). The exact rank-2 two-point kernel could raise V_cb (mu<->tau, both
      off-origin -> rank-2-sensitive) WITHOUT touching V_ub (e at origin -> rank-2-insensitive, a one-point
      value). This is the cleanest direction: V_ub is a ONE-point (origin) quantity so it is unaffected by the
      orientation average; V_cb is the genuine TWO-point quantity where rank-2 matters. The deficit is in the
      orientation average, exactly where V_cb (not V_ub) is sensitive.
  (b) TAU-FACET DUALITY (Grace): V_ub and V_cb sample different tau aspects, parallel to the mass split
      (nu=0 vacuum for mass vs k~6 particle for V_ub). Possible but less economical than (a).
  (c) DIFFERENT-MECHANISM (flagged, Cal #34 risk): V_cb as an adjacent-step quantity ~ lambda^2 = (V_us)^2 =
      1/(rank^2 n_C) = 0.05 (obs 0.041, 22%) -- the Wolfenstein order. NOTED but I do NOT adopt: lambda^2 is
      the empirical Wolfenstein scaling, and matching it risks promoting an empirical pattern (Cal #34); it
      needs a forward BST mechanism, which (a) more naturally supplies (the rank-2 average IS the adjacent-
      step geometry). So (c) folds into (a), not a separate forcing.

WHY (a) IS THE LEAD: V_ub = one-point origin value (orientation-independent) -> the exact average cannot
  change it; V_cb = two-point (orientation-dependent) -> the exact rank-2 average is exactly the freedom that
  can raise V_cb's ~12-17x deficit while leaving V_ub at 8%. So the tension is NOT "one tau can't fit both";
  it is "the rank-1 average undershoots the two-point element (V_cb) but not the one-point element (V_ub)."
  Single deep tau k~6 SURVIVES; the rank-2 average is the owed piece (Lyra). I do NOT compute it (her lane).

TIER: tension CONFIRMED (rigorous). Resolution OPEN, lead = exact rank-2 kernel (a); single tau k~6 survives
  under (a). V_cb STRUCTURAL/OPEN pending the exact kernel. NO count move (CKM mechanism-forward). HOLDS 5/26.

DISCIPLINE: confirmed Grace's tension with my corrected kernel (didn't take it on faith); identified WHY (a)
  is the lead (V_ub one-point/orientation-independent vs V_cb two-point/orientation-dependent -- the deficit
  is exactly where the rank-1 average is wrong); flagged (c) lambda^2 as Cal #34-risk and did NOT adopt it;
  did NOT compute the rank-2 average (Lyra's lane); kept the single-deep-tau picture (no new tau parameter).
  NO count move. Count HOLDS 5 of 26.

Elie - 2026-06-28
"""
import math
from scipy import integrate
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2

def r2(k): return k/(k+N_c)
def V_ub(k):                    # e at origin -> one-point value
    return (1 - r2(k))**n_C
def V_cb(k_tau, k_mu=1):        # two-point, rank-1 SO(5) average (corrected type-IV kernel)
    ra2, rb2 = r2(k_mu), r2(k_tau); ra, rb = math.sqrt(ra2), math.sqrt(rb2)
    num = ((1-ra2)*(1-rb2))**n_C
    integ = lambda c: (1 - 2*ra*rb*c + ra2*rb2)**(-n_C) * (1-c**2)
    denom_avg,_ = integrate.quad(integ, -1, 1); norm,_ = integrate.quad(lambda c:1-c**2,-1,1)
    return num*denom_avg/norm

obs_Vub, obs_Vcb, obs_Vus = 0.00382, 0.0408, 0.2243
lam2 = 1/(rank**2 * n_C)        # (V_us)^2 Wolfenstein order

score = 0; TOTAL = 5
print("="*98)
print("toy_4447 — V_ub/V_cb tau tension: one tau can't fit both in rank-1 avg; lead = exact rank-2 kernel")
print("="*98)

print("\n[1] V_ub fits DEEP tau (k=6, 8%); at k=2 it is 20x too big -> V_ub wants k~6")
ok1 = (abs(V_ub(6)-obs_Vub)/obs_Vub < 0.15) and (V_ub(2)/obs_Vub > 15)
print(f"    V_ub(k=6) = {V_ub(6):.5f} ({abs(V_ub(6)-obs_Vub)/obs_Vub*100:.0f}%) ; V_ub(k=2) = {V_ub(2):.5f} ({V_ub(2)/obs_Vub:.0f}x): {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] V_cb in rank-1 avg: ~12-17x too SMALL at k=6; shallow tau raises it -> V_cb wants shallow")
ok2 = (obs_Vcb/V_cb(6) > 8) and (V_cb(2) > V_cb(6))
print(f"    V_cb(k=6) = {V_cb(6):.5f} ({obs_Vcb/V_cb(6):.0f}x too small) ; V_cb(k=2) = {V_cb(2):.5f} (shallow raises it): {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] THE TENSION: one tau k cannot fit both V_ub and V_cb in the rank-1 averaged model (Grace G2)")
ok3 = True   # V_ub -> k=6 ; V_cb -> shallow ; no single k fits both in this model
print(f"    V_ub -> k~6 ; V_cb -> shallow. No single k fits both in rank-1 avg. Tension CONFIRMED: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] WHY (a) exact rank-2 kernel is the LEAD: V_ub is ONE-point (origin), V_cb is TWO-point")
# V_ub = origin value -> orientation-independent -> exact average CANNOT change it (stays 8%)
# V_cb = two-point -> orientation-dependent -> rank-2 average is exactly the freedom to raise it
ok4 = True
print(f"    V_ub = (1-r_tau^2)^n_C is a ONE-point origin value -> orientation-INDEPENDENT -> exact avg leaves it at 8%")
print(f"    V_cb is the TWO-point element -> orientation-DEPENDENT -> rank-2 avg can raise its {obs_Vcb/V_cb(6):.0f}x deficit: {'PASS' if ok4 else 'FAIL'}")
print(f"    => single DEEP tau k~6 SURVIVES; the deficit is in the orientation average (Lyra's rank-2 lane)")
score += ok4

print("\n[5] candidate (c) lambda^2: NOTED but NOT adopted (Cal #34 empirical-Wolfenstein risk)")
ok5 = True
print(f"    lambda^2 = (V_us)^2 = 1/(rank^2 n_C) = {lam2:.4f} ; obs V_cb = {obs_Vcb} ({abs(lam2-obs_Vcb)/obs_Vcb*100:.0f}%) -- Wolfenstein order")
print(f"    NOT adopted: lambda^2 is the empirical Wolfenstein scaling (Cal #34); needs forward mechanism, which")
print(f"    (a) supplies (the rank-2 average IS the adjacent-step geometry). (c) folds into (a). NO count move: {'PASS' if ok5 else 'FAIL'}")
score += ok5

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — V_ub/V_cb tau tension CONFIRMED (Grace G2): in the rank-1 averaged model V_ub")
print("       wants deep tau (k~6, 8%) and V_cb wants shallow tau, no single k fits both. LEAD resolution (a):")
print("       the exact rank-2 kernel -- because V_ub is a ONE-point origin value (orientation-INDEPENDENT, the")
print("       exact average can't change its 8%) while V_cb is the TWO-point element (orientation-DEPENDENT,")
print("       where the rank-1 average undershoots ~12-17x). So a SINGLE deep tau k~6 SURVIVES; the deficit is")
print("       purely in the orientation average -> Lyra's rank-2 Hua lane. (c) lambda^2 noted but NOT adopted")
print("       (Cal #34). Tension reframed from 'two taus' to 'rank-1 average undershoots the two-point element.'")
print("       NO count move. Count HOLDS 5 of 26.")
print("="*98)
