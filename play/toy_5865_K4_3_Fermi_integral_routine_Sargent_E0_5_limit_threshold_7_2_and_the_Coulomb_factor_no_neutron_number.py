#!/usr/bin/env python3
"""
Toy 5865 — Round K4-3, Lane B (Elie, 2026-10-09). Prereg: notes/Elie_K4-3_prereg_toys_5864-5867_* (976951e1).

The Fermi phase-space routine f(W0) for beta decay, m_e = c = 1, W0 = 1 + E0/m_e.
  f(W0) = int_1^W0 F(Z,W) p W (W0 - W)^2 dW ;   Z = 0 closed form f0 = (p0/60)(2W0^4 - 9W0^2 - 8) + (W0/4) ln(W0 + p0).
Checks: closed form vs quadrature; Sargent's W0^5/30 limit and how far it is off at low W0 (Keeper's catch as a number);
the threshold law (W0-1)^(7/2); the Coulomb factor's alpha -> 0 and Sommerfeld limits; Z = 1 beside Z = 0.
NO W0 in (2.4, 2.7) is evaluated. The neutron's 0.78233 MeV waits for Cal's hash.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from _k4_3_lib_loader import lib
fermi_f, fermi_f0_closed, fermi_F, sommerfeld = lib.fermi_f, lib.fermi_f0_closed, lib.fermi_F, lib.sommerfeld
mp.mp.dps = 30

RESULTS = []
def score(tag, ok, msg):
    RESULTS.append((tag, bool(ok))); print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")

GRID = [mp.mpf(x) for x in ('1.2', '1.5', '2', '3', '5', '10', '30', '100')]
assert not any(mp.mpf('2.4') < W0 < mp.mpf('2.7') for W0 in GRID)

print("F1  closed form vs quadrature (Z = 0)")
err = max(abs(fermi_f(W0, 0) - fermi_f0_closed(W0)) / fermi_f0_closed(W0) for W0 in GRID)
score("F1", err < mp.mpf('1e-20'), f"max relative difference {mp.nstr(err, 3)}")

print("F2  Sargent: f0 / (W0^5/30)")
ratios = {W0: fermi_f0_closed(W0) / (W0 ** 5 / 30) for W0 in GRID}
for W0, r in ratios.items():
    print(f"      W0 = {mp.nstr(W0,4):>5}: f0 = {mp.nstr(fermi_f0_closed(W0), 8):>14}   f0/(W0^5/30) = {mp.nstr(r, 8)}")
ok2 = abs(ratios[mp.mpf(100)] - 1) < mp.mpf('0.01') and all(abs(ratios[W0] - 1) > mp.mpf('0.30') for W0 in GRID if W0 <= 3)
score("F2", ok2, f"within 1% of W0^5/30 at W0 = 100 ({mp.nstr(ratios[mp.mpf(100)], 6)}); off by > 30% at every W0 <= 3 "
                 f"(W0 = 3: {mp.nstr(ratios[mp.mpf(3)], 4)}, W0 = 2: {mp.nstr(ratios[mp.mpf(2)], 4)}) — E0^5 is not a law for a 1.5 m_e endpoint")

print("F3  threshold law")
def logslope(T, h=mp.mpf('1e-4')):
    g = lambda t: mp.log(fermi_f0_closed(1 + t))
    return (g(T * (1 + h)) - g(T * (1 - h))) / (mp.log(1 + h) - mp.log(1 - h))
s = logslope(mp.mpf('1e-3')); s_big = logslope(mp.mpf('99'))
score("F3", abs(s - mp.mpf(3.5)) < mp.mpf('0.035') and abs(s_big - 5) < mp.mpf('0.1'),
      f"dln f0/dln(W0-1) = {mp.nstr(s, 6)} at W0-1 = 1e-3 (7/2), {mp.nstr(s_big, 5)} at W0-1 = 99 (5): the neutron sits between")

print("F4  the Coulomb factor")
W = mp.mpf('1.5')
lim0 = fermi_F(1, W, alpha=mp.mpf('1e-12'))
# Sommerfeld comparison at small alpha Z (the relativistic F differs by O((alpha Z)^2 ln(pR)) terms)
devs = []
for al in (mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')):
    devs.append(abs(fermi_F(1, mp.mpf('3'), alpha=al) / sommerfeld(1, mp.mpf('3'), alpha=al) - 1))
ratio_shrink = devs[0] / devs[1], devs[1] / devs[2]
score("F4", abs(lim0 - 1) < mp.mpf('1e-9') and all(abs(r - 100) < 30 for r in ratio_shrink),
      f"F -> 1 as alpha -> 0 ({mp.nstr(lim0, 12)}); |F/Sommerfeld - 1| = {[mp.nstr(d, 3) for d in devs]} at alpha = 1e-2, 1e-3, 1e-4: scales as alpha^2 (ratios {[mp.nstr(r,4) for r in ratio_shrink]})")

print("F5  Z = 1 beside Z = 0 (R = 0.87 fm / 386.16 fm)")
mono = True
for W0 in GRID:
    f0, f1, f2 = fermi_f0_closed(W0), fermi_f(W0, 1), fermi_f(W0, 2)
    mono &= f0 < f1 < f2
    print(f"      W0 = {mp.nstr(W0,4):>5}: f(Z=0) = {mp.nstr(f0, 8):>14}  f(Z=1) = {mp.nstr(f1, 8):>14}  f(Z=1)/f(Z=0) = {mp.nstr(f1/f0, 6)}")
score("F5", mono, "f(Z=0) < f(Z=1) < f(Z=2) on the whole grid (Coulomb attraction raises electron emission); the neutron's W0 is NOT on the grid")

passed = sum(ok for _, ok in RESULTS)
print(f"\nSCORE: {passed}/{len(RESULTS)}  (all {len(RESULTS)} can fail)")
