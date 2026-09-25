#!/usr/bin/env python3
"""
Toy 5790 — 16/3 and f_b = 3/19 on ACT DR6 (second CMB experiment), extending toy 5788.
(Elie, 2026-09-25.)

NOT BLIND: I read ACT's table and estimated the ratios mentally before writing this file. No
direction is pre-registered; this is a computation on pinned numbers, reported as such.

PINS — ACT DR6, arXiv:2503.14452 (Grace, data/sources_grace_2026-09-25/dm/2503.14452.txt), l.4221-22:
  ACT (+Planck lowE):  omega_b 0.02259(17), omega_c 0.1238(21)
  P-ACT:               0.02250(11), 0.1193(12)
  P-ACT-L (+lensing):  0.02251(11), 0.1191(11)
  P-ACT-LB (+DESI DR1 BAO): 0.02256(11), 0.11790(85)
  Planck 2018 rows repeated from toy 5788 for the side-by-side (1807.06209 l.3258, l.1177-78).
Correlation omega_b-omega_c unpinned: rho = 0 quoted, rho = +-0.5 bracket.
Note: ACT alone and Planck alone are independent; P-ACT rows SHARE Planck data — not independent of 5788.
"""
from math import sqrt

rows = {
    "Planck TTTEEE+lowE+lens": (0.02237, 0.00015, 0.1200, 0.0012),
    "Planck +BAO(SDSS)":       (0.02242, 0.00014, 0.11933, 0.00091),
    "ACT DR6 alone":           (0.02259, 0.00017, 0.1238, 0.0021),
    "P-ACT":                   (0.02250, 0.00011, 0.1193, 0.0012),
    "P-ACT-L":                 (0.02251, 0.00011, 0.1191, 0.0011),
    "P-ACT-LB (+DESI DR1)":    (0.02256, 0.00011, 0.11790, 0.00085),
}
print("Toy 5790 — 16/3 and 3/19 across CMB datasets (NOT BLIND)\n")
print(f"{'dataset':26s} {'R=wc/wb':>9s} {'sig':>7s} {'16/3 pull':>10s} {'rho+-0.5':>14s} | {'f_b':>8s} {'sig':>8s} {'3/19 pull':>9s}")
out = {}
for k, (wb, sb, wc, sc) in rows.items():
    R = wc/wb
    def sR(rho):
        return R*sqrt((sc/wc)**2 + (sb/wb)**2 - 2*rho*(sc/wc)*(sb/wb))
    z = (16/3 - R)/sR(0)
    zlo, zhi = sorted([(16/3 - R)/sR(-0.5), (16/3 - R)/sR(0.5)])
    fb = wb/(wb + wc); sf = sqrt((wc*sb)**2 + (wb*sc)**2)/(wb + wc)**2
    zf = (3/19 - fb)/sf
    out[k] = (z, zf)
    print(f"{k:26s} {R:9.4f} {sR(0):7.4f} {z:+10.2f} [{zlo:+.2f},{zhi:+.2f}] | {fb:8.5f} {sf:8.5f} {zf:+9.2f}")

checks = []
def check(name, ok, can_fail=True):
    checks.append((name, bool(ok), can_fail))
    print(f"  [{'PASS' if ok else 'FAIL'}]{'' if can_fail else ' (control)'} {name}")
print()
check("control: Planck rows reproduce toy 5788 (-0.48, +0.21)",
      abs(out["Planck TTTEEE+lowE+lens"][0] + 0.48) < 0.01 and abs(out["Planck +BAO(SDSS)"][0] - 0.21) < 0.01, can_fail=False)
check("16/3 within 2 sigma of every dataset", all(abs(v[0]) < 2 for v in out.values()))
check("16/3 within 2 sigma of the two INDEPENDENT CMB experiments alone (Planck, ACT)",
      abs(out["Planck TTTEEE+lowE+lens"][0]) < 2 and abs(out["ACT DR6 alone"][0]) < 2)
n = len(checks); k = sum(ok for _, ok, _ in checks)
cf = [c for c in checks if c[2]]; kcf = sum(ok for _, ok, _ in cf)
print(f"\nSCORE {k}/{n}  (can-fail {kcf}/{len(cf)}; {n-len(cf)} controls) — NOT BLIND")
