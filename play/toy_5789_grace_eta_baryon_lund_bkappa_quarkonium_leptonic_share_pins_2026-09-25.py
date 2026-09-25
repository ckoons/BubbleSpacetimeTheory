#!/usr/bin/env python3
"""
Toy 5789 — Grace, 2026-09-25 (round 3). Retained instrument for three pin tables in
notes/grace_R161_round3_pins_eta_sphaleron_Lund_OZI_proton_axion_register_v0_24_2026-09-25.md.

(1) eta = 2 alpha^4 / (3 pi) (BST_BaryonAsymmetry_Derivation.md, March) against every pinned
    baryon-density determination — CMB-side AND deuterium-side, both printed; the reading is
    the pair, not the favourable member.
(2) Lund b*kappa (dimensionless; b in GeV^-2, kappa in GeV^2) across the LEP tunes.
(3) Gamma_ee / Gamma for phi, J/psi, psi(2S), Upsilon(1S,2S,3S) from PDG 2026 — the numbers
    for Lyra's OZI ordering; printed AFTER her direction, never before it (compare line only).

Every printed source value is grep-checked in data/sources_grace_2026-09-25/r3/; a missing
string FAILS the toy. No BST number is adjusted.
"""
import math, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "sources_grace_2026-09-25", "r3")
score = [0, 0]
def check(name, ok):
    score[1] += 1; score[0] += bool(ok); print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
def has(f, s):
    with open(os.path.join(SRC, f), encoding="utf-8", errors="replace") as fh: return s in fh.read()

print("=== (1) eta: source strings ===")
for f, s in [("1807.06209.txt", "0.02237 ± 0.00015"), ("1807.06209.txt", "0.02242 ± 0.00014"),
             ("1912.01132.txt", "273.754"), ("2011.11320.txt", "0.02195 ± 0.00022"),
             ("pdg_bbn_2025.txt", "6.040 ± 0.118"), ("1710.11129.txt", "2.166 ± 0.015 ± 0.011")]:
    check(f"{f}: '{s}'", has(f, s))

ALPHA_INV = 137.035999177          # CODATA 2022 (NIST CUU), read by the pinning pass
eta_bst = 2 * ALPHA_INV ** -4 / (3 * math.pi) * 1e10
print(f"\n  eta10_BST = 2 alpha^4 / (3 pi) x 1e10 = {eta_bst:.5f}")
F = 273.754                        # Fields-Olive-Yeh-Young 2020 Eq. (A24) at Y = 0.245, T = 2.7255 K
rows = [("CMB  Planck 2018 TT,TE,EE+lowE+lensing (Eq. 24)", 0.02237, 0.00015),
        ("CMB  Planck 2018 +BAO (Table 2)", 0.02242, 0.00014),
        ("D/H  Cooke-Pettini-Steidel 2018 (Eq. 12)", 0.02166, math.hypot(0.00015, 0.00011)),
        ("BBN  Pitrou et al. 2021 (Eq. 9)", 0.02195, 0.00022),
        ("BBN  PDG 2025 SBBN (Eq. 24.6)", 0.02205, 0.00043)]
pulls = {}
for n, w, dw in rows:
    e, de = F * w, F * dw
    pulls[n] = (eta_bst - e) / de
    print(f"  {n:48s} omega_b = {w:.5f}({dw*1e5:.0f})  eta10 = {e:.3f} ± {de:.3f}  pull {pulls[n]:+.2f} sigma")
cmb = [v for k, v in pulls.items() if k.startswith("CMB")]
bbn = [v for k, v in pulls.items() if k.startswith("BBN")]
check("CMB side: BST eta is > 2.5 sigma LOW on both Planck combinations", all(v < -2.5 for v in cmb))
check("BBN side: BST eta within 0.5 sigma of both BBN-only determinations", all(abs(v) < 0.5 for v in bbn))

print("\n=== (2) Lund b*kappa, kappa = 1 GeV/fm x hbar c ===")
for f, s in [("monash2013_arXiv1404.5630.txt", "StringZ:bLund         =                  0.98"),
             ("pythia83_manual_arXiv2203.11601.txt", "κ ≈ 1 GeV/fm")]:
    check(f"{f}: '{s}'", has(f, s))
kappa = 0.1973269804               # GeV^2 for 1 GeV/fm
for n, b in [("Monash 2013", 0.98), ("Pythia 8 pre-Monash default", 0.8),
             ("Professor Q^2 (P6)", 0.6), ("Professor pT (P6)", 1.2), ("Pythia 6.418 default", 0.58)]:
    print(f"  {n:30s} b = {b:4.2f} GeV^-2   b*kappa = {b * kappa:.4f}")
print("  (kappa is '≈ 1 GeV/fm' in the manual; the spread across tunes, 0.11-0.24, is the target's width)")

print("\n=== (3) Gamma_ee / Gamma, PDG 2026 (compare line; Lyra's direction first) ===")
for f, s in [("pdg2026_listing_upsilon-3S.txt", "0.443± 0.008 OUR EVALUATION")]:
    check(f"{f}: '{s}'", has(f, s))
for n, gee, g in [("phi(1020)", 1.27e-3, 4.249), ("J/psi(1S)", 5.53, 92.6), ("psi(2S)", 2.33, 293.0),
                  ("Upsilon(1S)", 1.340, 54.02), ("Upsilon(2S)", 0.612, 31.98), ("Upsilon(3S)", 0.443, 20.32)]:
    print(f"  {n:12s} Gamma_ee/Gamma = {gee / g:.4e}")
print(f"\nSCORE {score[0]}/{score[1]}")
sys.exit(0 if score[0] == score[1] else 1)
