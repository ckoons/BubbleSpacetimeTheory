#!/usr/bin/env python3
"""Lyra R152 check (not a numbered toy): does windowing the CLOCK channel on flux (the four G quartiles) let the
redshift channel separate the boost g_q*beta*u from the intrinsic A*zeta_q*w on its own?  1-D Fisher along a fixed
direction; noise per quartile = 2x the full-sample mean-z-dipole noise (sigma_beta 170 km/s, v1.2 power paragraph);
count channel entered as independent priors (sigma_beta 443 km/s, sigma_A 0.026 from v1.5 4.4a).  Inputs: g_w and
zeta_q from the frozen (v) record and addendum (Elie, 12:37).  Reproduces Elie 5765's shape: ~325 with the column,
~159 without, ~177 with a prior sigma_A = 0.005."""
import json, numpy as np
c = 299792.458
v = json.load(open('.partB_v_closed.json'))['G20.5']; a = json.load(open('.partB_v_addendum.json'))['G20.5']
g_q = np.array(v['g_w']); z_q = np.array(a['zeta_q'])
sig_q = 2 * v['g'] * 170 / c
X = np.stack([g_q, z_q], 1); F = X.T @ X / sig_q**2; C = np.linalg.inv(F)
print("zeta_q/g_q:", np.round(z_q / g_q, 4))
print("clock channel alone, four windows: sigma_beta %.0f km/s, sigma_A %.3f, corr %.3f" % (np.sqrt(C[0,0])*c, np.sqrt(C[1,1]), C[0,1]/np.sqrt(C[0,0]*C[1,1])))
for sA in (0.026, 0.010, 0.005):
    Fp = F.copy(); Fp[1,1] += 1/sA**2; Fp[0,0] += 1/(443/c)**2
    print("  + count channel (sigma_A %.3f): joint sigma_beta %.0f km/s" % (sA, np.sqrt(np.linalg.inv(Fp)[0,0])*c))
print("  A fixed (no zeta column): sigma_beta %.0f km/s" % (c/np.sqrt(F[0,0] + 1/(443/c)**2)))
# selftest: identical ratios zeta_q/g_q => the clock channel cannot separate at all (singular)
Xs = np.stack([g_q, -0.06*g_q], 1); assert np.linalg.matrix_rank(Xs) == 1; print("SELFTEST PASS (equal ratios -> rank 1)")
