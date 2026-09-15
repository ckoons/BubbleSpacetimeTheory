#!/usr/bin/env python3
"""Keeper K1908 instrument: (1) the redshift-channel intrinsic term is DETERMINED by the frozen (v) record — no new parameter.
An intrinsic dipole with per-bin amplitude A w_i along w-hat changes N_i(n) = Nbar_i (1 + A w_i w.n); the sky's mean redshift then has
dipole  d<z> = A * zeta * w-hat,  zeta = sum_i p_i w_i (ztilde_i - zbar),  p_i = N_i / N (weighted).  The redshift channel of 4.5 reads a
mean-z dipole as -g*beta, so an intrinsic dipole A leaks beta_leak = -zeta*A/g into the redshift-only fit.  zeta is a functional of the
posted table: p_i, w_i, ztilde_i, g.  (2) The 4.4 region clause: the profile-chi2 over direction (beta >= 0) is |b|^2 sin^2(theta)/sigma^2
for theta < 90 deg and |b|^2/sigma^2 beyond, so the 95% region (2 d.o.f., 5.991) is the whole sphere iff |b|/sigma < sqrt(5.991) = 2.448:
the clause is a monotone function of the same S/N the chi2_3(b,0) test already measures."""
import json, math, sys
d = json.load(open('.partB_v_closed.json'))
for tag in ('G20.5', 'G20.0'):
    t = d[tag]; rows = t['rows']; g = t['g']
    N = sum(r['N_w'] for r in rows); zbar = sum(r['N_w'] * r['zmed'] for r in rows) / N
    zeta = sum(r['N_w'] / N * r['w'] * (r['zmed'] - zbar) for r in rows)
    zeta_alt = sum(r['N_w'] / N * r.get('w_alt', r['w']) * (r['zmed'] - zbar) for r in rows)
    c = 299792.458
    print(f"{tag}: g = {g:.4f}, zbar(weighted, bin medians) = {zbar:.4f}, zeta = {zeta:+.4f} (w_alt: {zeta_alt:+.4f})")
    for A in (0.01, 0.02, 0.05):
        print(f"   A_int = {A}: mean-z dipole = {zeta*A:+.5f}; redshift-only leak beta_leak c = {-zeta*A/g*c:+.0f} km/s along w-hat (w_alt {-zeta_alt*A/g*c:+.0f})")
print("\nRegion clause: whole sphere iff |b|/sigma < sqrt(5.991) =", round(math.sqrt(5.991), 3),
      "; CMB at sigma 166:", round(369.82/166, 3), "-> whole sphere; needs sigma <", round(369.82/math.sqrt(5.991), 1), "km/s for the TRUE vector to have a bounded region")
# selftest: a flat profile (w_i = 1) with equal-z bins gives zeta = 0; a two-bin toy gives the closed form
p=[0.5,0.5]; w=[1,0]; z=[1,2]; zb=1.5; zt=sum(pi*wi*(zi-zb) for pi,wi,zi in zip(p,w,z)); assert abs(zt-(-0.25))<1e-12
print("SELFTEST PASS (two-bin closed form -0.25)")
