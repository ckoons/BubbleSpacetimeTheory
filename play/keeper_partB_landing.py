#!/usr/bin/env python3
"""Keeper — Section 5 of the frozen Part B.1 protocol (v1.1) as CODE, so the landing is a computed reading and never a
typed verdict. Inputs are the run's own numbers; output is exactly one of A / B / C with the clause that decided it.
Usage: keeper_partB_landing.py <run.json>   |   --selftest
run.json keys: beta, sigma_beta (km/s); beta_cmb, sigma_cmb; u_cmb_in_95 (bool), u_cmb_in_99 (bool);
  bin_resid_p (list of per-bin chi2 p-values after subtracting the fitted intrinsic term and f_i*beta_cmb*u_cmb);
  C_triggers: {sigma_ge_half_beta, region_gt_quarter_sky, profile_moves_2sigma, boundary_forms_disagree, channels_disagree} (bools);
  hatch: {H1..H6: bool PASS};  beta_consistent_with_zero (bool: beta <= 2 sigma_beta while sigma_beta < beta_cmb/2)."""
import sys, json, math, tempfile, os
def land(r):
    C = r['C_triggers']
    for k, v in C.items():
        if v: return 'C', '4.4 trigger: %s' % k
    db = r['beta'] - r['beta_cmb']; sig = math.hypot(r['sigma_beta'], r['sigma_cmb'])
    hatch_all = all(r['hatch'].values())
    b_level = (abs(db) >= 3*sig) or (not r['u_cmb_in_99']) or r.get('beta_consistent_with_zero', False)
    if b_level:
        if hatch_all: return 'B', '5: |Δβ| = %.1fσ, u_CMB in 99%% region = %s, β≈0 = %s; every hatch check PASSES' % (abs(db)/sig, r['u_cmb_in_99'], r.get('beta_consistent_with_zero', False))
        failed = [k for k, v in r['hatch'].items() if not v]
        return 'C', '5: B-level discrepancy did NOT survive the hatch (failed %s) — not a fire, not a hold' % ','.join(failed)
    a_level = (abs(db) <= 2*sig) and r['u_cmb_in_95'] and all(p >= 0.01 for p in r['bin_resid_p'])
    if a_level: return 'A', '5: |Δβ| = %.1fσ ≤ 2σ, u_CMB inside 95%% region, no bin residual with p < 0.01' % (abs(db)/sig)
    return 'C', '5: between A and B (|Δβ| = %.1fσ; u_CMB in 95%%: %s; min bin p = %.3f)' % (abs(db)/sig, r['u_cmb_in_95'], min(r['bin_resid_p']))
def selftest():
    base = dict(beta=369.8, sigma_beta=60.0, beta_cmb=369.82, sigma_cmb=0.11, u_cmb_in_95=True, u_cmb_in_99=True,
                bin_resid_p=[0.5,0.4,0.6,0.3,0.2], C_triggers=dict(sigma_ge_half_beta=False, region_gt_quarter_sky=False,
                profile_moves_2sigma=False, boundary_forms_disagree=False, channels_disagree=False),
                hatch=dict(H1=True,H2=True,H3=True,H4=True,H5=True,H6=True), beta_consistent_with_zero=False)
    tests = []
    tests.append(land(base)[0] == 'A')                                                   # clean A
    r = dict(base, beta=800.0); tests.append(land(r)[0] == 'B')                           # 7σ off, hatch passes -> B
    r = dict(base, beta=800.0, hatch=dict(base['hatch'], H3=False)); tests.append(land(r)[0] == 'C')  # fails a hatch -> C
    r = dict(base, beta=520.0); tests.append(land(r)[0] == 'C')                           # 2.5σ: between A and B -> C
    r = dict(base, sigma_beta=443.0, C_triggers=dict(base['C_triggers'], sigma_ge_half_beta=True)); tests.append(land(r)[0] == 'C')  # Elie's count-only case
    r = dict(base, beta=40.0, sigma_beta=60.0, beta_consistent_with_zero=True); tests.append(land(r)[0] == 'B')  # no boost is not one boost
    r = dict(base, bin_resid_p=[0.5,0.004,0.6,0.3,0.2]); tests.append(land(r)[0] == 'C')  # A-level fit, one bin residual fails -> C
    r = dict(base, C_triggers=dict(base['C_triggers'], channels_disagree=True)); tests.append(land(r)[0] == 'C')  # C' routes to C
    print('SELFTEST', 'PASS' if all(tests) else 'FAIL', tests); return 0 if all(tests) else 1
if __name__ == '__main__':
    if '--selftest' in sys.argv: sys.exit(selftest())
    r = json.load(open(sys.argv[1])); L, why = land(r); print('LANDING', L, '—', why)
