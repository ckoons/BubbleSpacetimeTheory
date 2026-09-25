#!/usr/bin/env python3
"""
Toy 5791 — Grace, 2026-09-25 (round 3, dark-matter validation). Casey's corrected reading
(K1924 Addendum 2): 16 matter-uncommitted : 3 matter-committed  =>  Omega_c/Omega_b = 16/3
(T1966) and f_b = Omega_b/Omega_m = 3/19, fixed at every epoch after the freeze.

Retained instrument for the abundance table in
notes/grace_R162_dark_matter_validation_pins_16_3_and_3_19_three_epochs_2026-09-25.md.
Every source value is grep-checked in data/sources_grace_2026-09-25/{r3,dm}/.
Errors propagated WITHOUT the omega_b-omega_c correlation (stated on every line).

CONVENTION PIN (flagged before any sigma is quoted): Planck's Omega_m includes one massive
neutrino (0.06 eV). 16/3 is a ratio of CDM to baryons; 3/19 = b/(b + c) is the SAME statement
only if neutrinos are not 'matter'. With omega_nu in the denominator the Planck pull moves
from +0.48 to +0.92 sigma. Which convention BST's '19' counts is Lyra's to state.
"""
import math, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.join(ROOT, "data", "sources_grace_2026-09-25")
score = [0, 0]
def check(name, ok):
    score[1] += 1; score[0] += bool(ok); print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
def has(f, s):
    with open(os.path.join(S, f), encoding="utf-8", errors="replace") as fh: return s in fh.read()

print("=== source strings ===")
for f, s in [("r3/1807.06209.txt", "0.1200 ± 0.0012"), ("r3/1807.06209.txt", "0.11933 ± 0.00091"),
             ("r3/1807.06209.txt", "0.1430 ± 0.0011"), ("dm/2503.14452.txt", "0.11790 ± 0.00085"),
             ("dm/2503.14452.txt", "0.02256 ± 0.00011"), ("dm/2111.09343.txt", "Ωb /Ωm = 0.156 ± 0.034"),
             ("dm/2111.09343.txt", "Ωb /Ωm = 0.173 ± 0.024"), ("dm/2111.09343.txt", "Ωb /Ωm = 0.150 ± 0.021"),
             ("dm/2204.12823.txt", "0.140+0.014"), ("dm/1309.3565.txt", "fbary = 0.144±0.005")]:
    check(f"{f}: '{s}'", has(f, s))

R_BST, FB_BST = 16 / 3, 3 / 19
print(f"\n=== (1) Omega_c/Omega_b vs 16/3 = {R_BST:.4f} (CMB epoch; uncorrelated errors) ===")
cmb = [("Planck 2018 TT,TE,EE+lowE+lensing", 0.1200, 0.0012, 0.02237, 0.00015),
       ("Planck 2018 +BAO", 0.11933, 0.00091, 0.02242, 0.00014),
       ("ACT DR6 P-ACT", 0.1193, 0.0012, 0.02250, 0.00011),
       ("ACT DR6 P-ACT-L", 0.1191, 0.0011, 0.02251, 0.00011),
       ("ACT DR6 P-ACT-LB (includes DESI BAO)", 0.11790, 0.00085, 0.02256, 0.00011)]
pulls = {}
for n, c, dc, b, db in cmb:
    R = c / b; dR = R * math.hypot(dc / c, db / b)
    pulls[n] = (R_BST - R) / dR
    fb0, fbv = b / (b + c), b / (b + c + 0.000644)
    print(f"  {n:38s} R = {R:.3f} ± {dR:.3f}  pull {pulls[n]:+.2f}σ   | f_b = {fb0:.5f} (no ν), {fbv:.5f} (with ω_ν = 0.000644)")
check("16/3 within 1 sigma of every CMB combination WITHOUT DESI BAO",
      all(abs(v) < 1 for k, v in pulls.items() if "DESI" not in k))
check("16/3 is > 2 sigma from P-ACT-LB (the DESI-BAO combination) — reported, not hidden",
      abs(pulls["ACT DR6 P-ACT-LB (includes DESI BAO)"]) > 2)
b, db, m, dm_ = 0.02237, 0.00015, 0.1430, 0.0011
fb = b / m; dfb = fb * math.hypot(db / b, dm_ / m)
print(f"  Planck ω_b/ω_m (ω_m incl. 0.06 eV ν) = {fb:.5f} ± {dfb:.5f}  -> 3/19 pull {(FB_BST - fb) / dfb:+.2f}σ")

print(f"\n=== (2) f_b vs 3/19 = {FB_BST:.6f} (late epoch, clusters; systematics-limited) ===")
cl = [("Mantz+2022 low-z f_gas, h prior F01 (Table 2)", 0.156, 0.034, 0.034),
      ("Mantz+2022, h prior P18", 0.173, 0.024, 0.024),
      ("Mantz+2022, h prior R19", 0.150, 0.021, 0.021),
      ("Wicker+2023 CB (Table 2)", 0.140, 0.014, 0.020),
      ("Gonzalez+2013 stars+ICL+gas r500 (no depletion corr.)", 0.144, 0.005, 0.005)]
for n, v, up, dn in cl:
    s = up if FB_BST > v else dn
    print(f"  {n:55s} {v:.3f} (+{up}/-{dn})  pull {(FB_BST - v) / s:+.2f}σ")
print("  NOTE: every cluster f_b inherits the depletion factor from simulations run in a Planck cosmology.")

print("\n=== (3) BBN epoch: omega_b only — f_b needs an external omega_m (not independent) ===")
for n, w in [("Pitrou 2021", 0.02195), ("PDG 2025 SBBN", 0.02205), ("Cooke 2018 D/H", 0.02166)]:
    print(f"  {n:16s} ω_b = {w}  -> f_b = {w / 0.1430:.4f} only with Planck's ω_m (mixes epochs; illustrative)")
print(f"\nSCORE {score[0]}/{score[1]}")
sys.exit(0 if score[0] == score[1] else 1)
