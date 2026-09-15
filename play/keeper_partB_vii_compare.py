#!/usr/bin/env python3
"""Keeper — step (vii) comparison for Part B.1 under v1.4 Section 5 as proposed for v1.5 (K1907; landing instrument v1.5 mode).
Inputs: Elie's posted (vi) JSON {b: [bx,by,bz] (dimensionless beta*u, Galactic Cartesian), cov: 3x3, sigma_beta (km/s),
bin_resid_p: [...], C_triggers: {...}, hatch: {...}, aprime: bool, u_region_frac_95: float, sigma_beta_over_half_beta_cmb: bool}
and Grace's held CMB target {beta_cmb_kms: 369.82, sigma_cmb_kms: 0.11, l_deg: 264.021, b_deg: 48.253}.
Computes chi2_3(b, b_CMB) under Sigma_b + sigma_cmb^2*1, chi2_3(b, 0), the debiased norm, the angle to u_CMB, and hands the
record to land_v13. NOTHING is typed: the letter comes from the numbers. Usage: keeper_partB_vii_compare.py vi.json cmb.json | --selftest"""
import sys, json, math, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from keeper_partB_landing import land_v15, CHI2_3_95, CHI2_3_3SIG, DCHI2_A
C_KMS = 299792.458
def unit_from_lb(l, b):
    l, b = math.radians(l), math.radians(b)
    return np.array([math.cos(b)*math.cos(l), math.cos(b)*math.sin(l), math.sin(b)])
def compare(vi, cmb):
    b = np.array(vi['b'], float); S = np.array(vi['cov'], float)
    beta_cmb = cmb['beta_cmb_kms'] / C_KMS; s_cmb = cmb['sigma_cmb_kms'] / C_KMS
    bc = beta_cmb * unit_from_lb(cmb['l_deg'], cmb['b_deg'])
    St = S + (s_cmb**2) * np.eye(3); Sti = np.linalg.inv(St)
    d = b - bc; chi2_cmb = float(d @ Sti @ d); chi2_zero = float(b @ np.linalg.inv(S) @ b)
    norm = float(np.linalg.norm(b)); deb = math.sqrt(max(norm**2 - float(np.trace(S)), 0.0))
    ang = math.degrees(math.acos(max(-1, min(1, float(b @ bc) / (norm * np.linalg.norm(bc)))))) if norm > 0 else float('nan')
    rec = dict(chi2_cmb=chi2_cmb, chi2_zero=chi2_zero, sigma_beta=vi['sigma_beta'], beta_cmb=cmb['beta_cmb_kms'],
               bin_resid_p=vi['bin_resid_p'], C_triggers=vi['C_triggers'], hatch=vi.get('hatch', {}))
    if not rec['hatch']: rec['hatch'] = {'H%d' % i: True for i in range(1, 7)}  # hatch only matters at B-level; requested then
    letter, clause = land_v15(rec)
    if letter == 'A' and not vi.get('aprime', True): letter, clause = 'C', "A-level chi2 but Landing A' of 4.5(a) failed"
    diag = dict(norm_kms=norm*C_KMS, debiased_norm_kms=deb*C_KMS, angle_to_cmb_deg=ang, chi2_cmb=chi2_cmb, chi2_zero=chi2_zero,
                thresholds=dict(A_max=CHI2_3_95, B_min=CHI2_3_3SIG, dchi2_A=DCHI2_A))
    return letter, clause, diag
def selftest():
    cmb = dict(beta_cmb_kms=369.82, sigma_cmb_kms=0.11, l_deg=264.021, b_deg=48.253)
    bc = 369.82 / C_KMS * unit_from_lb(264.021, 48.253); sig = 166.0 / C_KMS; S = (sig**2) * np.eye(3)
    base = dict(cov=S.tolist(), sigma_beta=166.0, bin_resid_p=[0.5, 0.4, 0.6, 0.3, 0.2], C_triggers=dict(sigma_ge_half_beta=False, region_gt_quarter_sky=False), aprime=True)
    t = []
    t.append(compare(dict(base, b=bc.tolist()), cmb)[0] == 'A')                                   # exactly the CMB vector -> A
    t.append(compare(dict(base, b=(bc + 1.5*sig*np.array([1, 0, 0])).tolist()), cmb)[0] == 'A')  # 1.5 sigma off -> chi2 2.25 -> A
    t.append(compare(dict(base, b=(bc + 3.0*sig*np.array([1, 0, 0])).tolist()), cmb)[0] == 'C')  # 3 sigma on one axis: chi2 9 -> between -> C
    t.append(compare(dict(base, b=(bc + 4.0*sig*np.array([1, 0, 0])).tolist()), cmb)[0] == 'B')  # chi2 16 -> B-level, hatch default pass
    t.append(compare(dict(base, b=[0.0, 0.0, 0.0]), cmb)[0] == 'C')                               # zero vector at 166 km/s: C (v1.4 said B — the false fire)
    t.append(compare(dict(base, b=bc.tolist(), aprime=False), cmb)[0] == 'C')                     # A-level but A' failed -> C
    t.append(compare(dict(base, b=bc.tolist(), bin_resid_p=[0.5, 0.004, 0.6, 0.3, 0.2]), cmb)[0] == 'C')
    L, cl, d = compare(dict(base, b=(bc*1.2).tolist()), cmb)                                      # norm bias 1.2 at S/N 2.2: chi2 ~ (0.2*2.23)^2 = 0.2 -> A (the vector test does not fire on the bias)
    t.append(L == 'A' and abs(d['norm_kms'] - 1.2*369.82) < 1e-6)
    print('SELFTEST vii', 'PASS' if all(t) else 'FAIL', t); return all(t)
if __name__ == '__main__':
    if '--selftest' in sys.argv: sys.exit(0 if selftest() else 1)
    vi = json.load(open(sys.argv[1])); cmb = json.load(open(sys.argv[2]))
    L, cl, d = compare(vi, cmb)
    print(json.dumps(d, indent=1)); print('LANDING', L, '—', cl)
