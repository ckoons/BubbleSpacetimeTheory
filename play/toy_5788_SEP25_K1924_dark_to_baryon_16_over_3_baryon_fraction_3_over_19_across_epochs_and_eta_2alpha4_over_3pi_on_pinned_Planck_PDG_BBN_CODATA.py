#!/usr/bin/env python3
"""
Toy 5788 — K1924 validation lines, abundance part (Elie, 2026-09-25).
  (a) Omega_c/Omega_b = 16/3 (T1966; Casey 16:38: uncommitted : committed)
  (b) f_b = Omega_b/(Omega_b + Omega_c) = 3/19 at every epoch where it is measured
  (c) eta = 2 alpha^4/(3 pi) (March, BST_BaryonAsymmetry_Derivation.md) vs eta_10 pins

PINS (every number opened in its source file):
  Planck 2018 VI, arXiv:1807.06209 (Grace, data/sources_grace_2026-09-25/r3/1807.06209.txt):
    l.3258 base LCDM TT,TE,EE+lowE+lensing: omega_b = 0.02237(15), omega_c = 0.1200(12)
    l.1177-78 last column (+BAO):             omega_b = 0.02242(14), omega_c = 0.11933(91)
  PDG 2026 BBN review (Grace, r3/pdg_bbn_2026.txt):
    l.317 (eta10)_SBBN = 6.040(118);  l.353 (eta10)_CMB = 6.12(4);  l.360 CMB+BBN eta10 = 6.115(38)
  CODATA 2022 (Elie, data/sources_elie_2026-09-25/nist_codata_allascii.txt, curl of NIST allascii):
    inverse fine-structure constant 137.035999177(21)
NOT PINNED / NOT USED: the omega_b-omega_c correlation coefficient (Planck chains not opened) —
  errors combined as uncorrelated, and the correlated case is bracketed with rho = +-0.5.
  Cluster gas f_b (Grace pin owed) — line (b3) is left OPEN, not scored.

DIRECTION BEFORE NUMBERS (from the pinned values' leading digits only, not computed):
  P1 16/3 = 5.333 sits within 1 sigma of Planck's omega_c/omega_b (both columns).
  P2 3/19 = 0.1579 sits within 1 sigma of Planck's f_b (both columns).
  P3 BBN (D/H) eta10 and CMB eta10 agree within 1 sigma (one baryon archive, not grown after BBN).
  P4 eta = 2 alpha^4/(3pi) sits more than 2 sigma below the CMB+BBN eta10 (K1924 said -2.6 sigma);
     this is a line the March formula can FAIL, and I expect it does at 2 sigma.
"""
from math import pi, sqrt

checks = []
def check(name, ok, can_fail=True):
    checks.append((name, bool(ok), can_fail))
    print(f"  [{'PASS' if ok else 'FAIL'}]{'' if can_fail else ' (control)'} {name}")

cols = {"TT,TE,EE+lowE+lensing": (0.02237, 0.00015, 0.1200, 0.0012),
        "+BAO": (0.02242, 0.00014, 0.11933, 0.00091)}
ainv = 137.035999177
eta10 = {"SBBN (D/H)": (6.040, 0.118), "CMB": (6.12, 0.04), "CMB+BBN": (6.115, 0.038)}

print("Toy 5788 — 16/3, 3/19, eta\n")
print("DIRECTION: P1 16/3 within 1 sigma; P2 3/19 within 1 sigma; P3 BBN = CMB within 1 sigma; P4 eta formula > 2 sigma low\n")

print("(a) omega_c / omega_b vs 16/3 = %.5f" % (16/3))
pa, pb = [], []
for name, (wb, sb, wc, sc) in cols.items():
    R = wc/wb
    for rho in (0.0, -0.5, +0.5):
        # var(R)/R^2 = (sc/wc)^2 + (sb/wb)^2 - 2 rho (sc/wc)(sb/wb)
        sR = R*sqrt((sc/wc)**2 + (sb/wb)**2 - 2*rho*(sc/wc)*(sb/wb))
        z = (16/3 - R)/sR
        if rho == 0.0:
            pa.append(z)
        print(f"  {name:24s} rho={rho:+.1f}: R = {R:.4f} +- {sR:.4f}  -> 16/3 pull {z:+.2f} sigma")
check("P1 16/3 within 1 sigma of omega_c/omega_b, both columns (rho = 0)", all(abs(z) < 1 for z in pa))

print("\n(b) f_b = omega_b/(omega_b + omega_c) vs 3/19 = %.5f" % (3/19))
for name, (wb, sb, wc, sc) in cols.items():
    fb = wb/(wb + wc)
    # df/dwb = wc/(wb+wc)^2 ; df/dwc = -wb/(wb+wc)^2
    s = sqrt((wc*sb)**2 + (wb*sc)**2)/(wb + wc)**2
    z = (3/19 - fb)/s
    pb.append(z)
    print(f"  (b1) CMB, {name:24s}: f_b = {fb:.5f} +- {s:.5f}  -> 3/19 pull {z:+.2f} sigma")
check("P2 3/19 within 1 sigma of Planck f_b, both columns", all(abs(z) < 1 for z in pb))
(e1, s1), (e2, s2) = eta10["SBBN (D/H)"], eta10["CMB"]
zB = (e1 - e2)/sqrt(s1**2 + s2**2)
print(f"  (b2) BBN vs CMB baryon density (eta10): {e1} vs {e2} -> {zB:+.2f} sigma")
print("       note: BBN measures omega_b only; f_b at BBN would borrow omega_c from the CMB, so (b2) tests")
print("       that the baryon archive did not grow between BBN and recombination — the part of 'every epoch'")
print("       that is measurable without a second dark-matter probe.")
check("P3 BBN and CMB eta10 agree within 1 sigma", abs(zB) < 1)
print("  (b3) cluster gas f_b: OPEN — Grace pin owed; not scored.")

print("\n(c) eta = 2 alpha^4 / (3 pi)")
a = 1/ainv
eta_bst = 2*a**4/(3*pi)
print(f"  alpha^-1 = {ainv} (CODATA 2022) -> eta = {eta_bst:.5e}, eta10 = {eta_bst*1e10:.4f}")
zs = {}
for name, (e, s) in eta10.items():
    z = (eta_bst*1e10 - e)/s
    zs[name] = z
    print(f"  vs {name:12s} {e} +- {s}: {100*(eta_bst*1e10/e - 1):+.2f} %  {z:+.2f} sigma")
check("control: eta10 from the formula is 6.0 +- 0.1 (sanity on the alpha^4 arithmetic)", 5.9 < eta_bst*1e10 < 6.1, can_fail=False)
check("P4 formula sits > 2 sigma below the CMB+BBN eta10", zs["CMB+BBN"] < -2)
print(f"  K1924's '-1.7 %, -2.6 sigma' vs this toy on CMB+BBN: {100*(eta_bst*1e10/6.115 - 1):+.2f} %, {zs['CMB+BBN']:+.2f} sigma;"
      f" vs SBBN alone {zs['SBBN (D/H)']:+.2f} sigma")

n = len(checks); k = sum(ok for _, ok, _ in checks)
cf = [c for c in checks if c[2]]; kcf = sum(ok for _, ok, _ in cf)
print(f"\nSCORE {k}/{n}  (can-fail {kcf}/{len(cf)}; {n-len(cf)} controls); (b3) cluster f_b OPEN")
