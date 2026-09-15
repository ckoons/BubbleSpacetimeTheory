#!/usr/bin/env python3
"""Keeper step (vii) on v1.5.2 (8013d959…): the comparison of Elie's (vi) record with Grace's held CMB target, by the instrument.
Reads .partB_vi_dipoles.json; for each sample and each of the three §4.3 fits computes chi2_3(b, b_CMB), chi2_3(b, 0), delta-chi2,
angle, debiased norm; the per-bin residual test D_i - w_i a - f_i b_CMB (3 d.o.f., propagated covariance, non-null bins); the §4.4
triggers (profile-alternative > 2 sigma_beta); the landing by land_v151 (v1.5.2's Section 5 = v1.5's; C triggers as v1.5.1);
the prior-sensitivity report (§4.3: named if the three fits land differently). Nothing is typed; the letter comes from the numbers."""
import json, math, sys, numpy as np
sys.path.insert(0, '.')
from keeper_partB_landing import land_v151, CHI2_3_95, CHI2_3_3SIG, DCHI2_A
C = 299792.458
CMB = dict(beta_cmb_kms=369.82, sigma_cmb_kms=0.11, l_deg=264.021, b_deg=48.253)   # Grace's held pin (Planck 2018), R145 §2
def u(l, b):
    l, b = math.radians(l), math.radians(b); return np.array([math.cos(b)*math.cos(l), math.cos(b)*math.sin(l), math.sin(b)])
bc = CMB['beta_cmb_kms']/C * u(CMB['l_deg'], CMB['b_deg']); Sc = (CMB['sigma_cmb_kms']/C)**2 * np.eye(3)
from scipy.stats import chi2 as chi2d
d = json.load(open(sys.argv[1] if len(sys.argv) > 1 else '.partB_vi_dipoles.json'))
for tag in ('G20.5', 'G20.0'):
    g = d[tag]; print(f"\n===== {tag}: weights {g['weights_mode'][:40]}…; N_mask {g['N_mask']:,}")
    prof = g['profile_alt']['shift_sigma']; print(f"  §4.4 profile-alternative trigger: shift = {prof:+.2f} sigma_beta (frozen bar 2) -> {'FIRES' if abs(prof) > 2 else 'clear'}")
    co, ro = g['count_only'], g['redshift_only']; z = abs(co['beta_c'] - ro['beta_c']) / math.hypot(co['sigma_c'], ro['sigma_c'])
    print(f"  A' amplitude clause: count-only {co['beta_c']:.0f} ± {co['sigma_c']:.0f} vs redshift-only {ro['beta_c']:.0f} ± {ro['sigma_c']:.0f}: {z:.2f} sigma apart -> {'agree' if z < 2 else 'DISAGREE (C-prime)'}")
    letters = {}
    for name, f in g['fits_v152'].items():
        b = np.array(f['b']); S = np.array(f['cov_full'])[:3, :3]; a = np.array(f['a'])
        Sti = np.linalg.inv(S + Sc); dv = b - bc
        chi_cmb = float(dv @ Sti @ dv); chi_0 = float(b @ np.linalg.inv(S) @ b); dchi = chi_0 - chi_cmb
        ang = math.degrees(math.acos(float(b @ bc) / (np.linalg.norm(b) * np.linalg.norm(bc))))
        deb = math.sqrt(max(np.linalg.norm(b)**2 - np.trace(S), 0)) * C
        ps = []
        for r in f['per_bin_residuals']:
            if r['null']: continue
            res = np.array(r['D_minus_w_a']) - r['f'] * bc; cv = np.array(r['cov_propagated'])
            ps.append(float(chi2d.sf(float(res @ np.linalg.solve(cv, res)), 3)))
        rec = dict(chi2_cmb=chi_cmb, chi2_zero=chi_0, sigma_beta=f['sigma_beta_c'], beta_cmb=CMB['beta_cmb_kms'], bin_resid_p=ps,
                   region_gt_quarter_sky=f['region95'] > 0.25,
                   C_triggers=dict(profile_moves_2sigma=abs(prof) > 2, boundary_forms_disagree=False, channels_disagree=(z >= 2)),
                   hatch={'H%d' % i: True for i in range(1, 8)})   # hatch is requested only at B-level; H5 mandatory under the fallback, unrun
        L, why = land_v151(rec); letters[name] = L
        print(f"  [{name}] beta c = {f['beta_c']:.0f} ± {f['sigma_beta_c']:.0f} km/s toward ({f['u_lb'][0]:.1f}, {f['u_lb'][1]:.1f}); angle to CMB {ang:.1f} deg; debiased norm {deb:.0f}; |a| = {f['A_norm']:.4f}")
        print(f"      chi2_3(b, b_CMB) = {chi_cmb:.2f} [A <= {CHI2_3_95}, B >= {CHI2_3_3SIG}]; chi2_3(b, 0) = {chi_0:.2f}; delta-chi2 = {dchi:+.2f} [A needs >= {DCHI2_A}]; per-bin residual p (non-null bins) = {[round(p, 4) for p in ps]}")
        print(f"      LANDING {L} — {why}")
        # what Section 5 alone would say with the 4.4 trigger removed (a report, so the reader sees what the trigger is doing)
        L5, why5 = land_v151(dict(rec, C_triggers=dict(profile_moves_2sigma=False, boundary_forms_disagree=False, channels_disagree=False)))
        print(f"      (Section 5 alone, trigger set aside — a REPORT, not a landing: {L5} — {why5[:110]})")
    print(f"  prior-sensitivity (§4.3): the three fits land {letters} -> {'PRIOR-SENSITIVE, named' if len(set(letters.values())) > 1 else 'all three agree'}")
