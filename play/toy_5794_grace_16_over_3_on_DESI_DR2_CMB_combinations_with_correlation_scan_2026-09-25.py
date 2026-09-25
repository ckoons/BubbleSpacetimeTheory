#!/usr/bin/env python3
"""
Toy 5794 — Grace, 2026-09-25 (round 4, item 1: where 16/3 can die).

Omega_c/Omega_b against 16/3 on every published CMB and CMB+BAO combination that PRINTS omega_c
and omega_b (ACT DR6 Table 5; SPT-3G D1 Tables I, VI). DESI DR2 Results II prints no omega_c
for DESI+CMB (Table V has Omega_m, H0 only) — its CMB COMPRESSION (Eq. A1-A2) is used here
only to estimate the omega_b-omega_c correlation, which none of the tables print.

The A13 kill clause reads 'Omega_c/Omega_b off 16/3 at > 3 sigma'. With uncorrelated errors
ACT+DESI DR2 (P-ACT-LB2) sits past it. Whether it is past it with the true correlation is
the question this toy makes explicit: it scans rho and reports the rho at which the pull
crosses 3 sigma, beside the CMB-compression rho from DESI's own Eq. A2.
Every source string is grep-checked; a missing string FAILS the toy.
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
for f, s in [("dm/2503.14452.txt", "12.38 ± 0.21 . . . 12.00 ± 0.14 . . . 12.20 ± 0.18 . . . 11.93 ± 0.12 . . . 11.79 ± 0.09 . . . 11.74 ± 0.06"),
             ("dm/2503.14452.txt", "2.259 ± 0.017 . . 2.237 ± 0.015 . . 2.263 ± 0.012 . . 2.250 ± 0.011 . . 2.256 ± 0.011 . . 2.258 ± 0.010"),
             ("dm/2503.14452.txt", "referred to as P-ACT-LB2"),
             ("r4/2506.20707.txt", "11.749 ± 0.079 11.809 ± 0.060"),
             ("r4/2506.20707.txt", "2.218 ± 0.022 2.2478 ± 0.0091"),
             ("desi.txt", "1488.4"), ("desi.txt", "21.344"), ("desi.txt", "−94.001")]:
    check(f"{f}: '{s[:60]}'", has(f, s))

# DESI DR2 II Eq. A2: covariance of (theta*, omega_b, omega_bc) x 1e-9 (CMB compression, Planck PR4 + ACT lensing)
vb, vbc, cb_bc = 21.344, 1488.4, -94.001
vc = vbc + vb - 2 * cb_bc
cb_c = cb_bc - vb
rho_cmb = cb_c / math.sqrt(vb * vc)
print(f"\n  DESI Eq. A2 (CMB compression): corr(omega_b, omega_c) = {rho_cmb:+.3f}  (arith: omega_c = omega_bc - omega_b)")

T = 16 / 3
def pull(c, dc, b, db, rho):
    R = c / b
    rel2 = (dc / c) ** 2 + (db / b) ** 2 - 2 * rho * (dc / c) * (db / b)
    return (R - T) / (R * math.sqrt(rel2)), R
rows = [("ACT alone (ACT T5)", 12.38, 0.21, 2.259, 0.017),
        ("Planck (ACT T5 rerun)", 12.00, 0.14, 2.237, 0.015),
        ("P-ACT (ACT T5)", 11.93, 0.12, 2.250, 0.011),
        ("P-ACT-LB, DESI DR1 (ACT T5)", 11.79, 0.09, 2.256, 0.011),
        ("P-ACT-LB2, DESI DR2 (ACT T5)", 11.74, 0.06, 2.258, 0.010),
        ("SPT-3G D1 (SPT T-I)", 12.14, 0.16, 2.221, 0.020),
        ("CMB-SPA (SPT T-I)", 12.028, 0.094, 2.2398, 0.0095),
        ("SPT+DESI DR2 (SPT T-VI)", 11.749, 0.079, 2.218, 0.022),
        ("CMB-SPA+DESI DR2 (SPT T-VI)", 11.809, 0.060, 2.2478, 0.0091)]
print(f"\n=== R = omega_c/omega_b vs 16/3; pull = (R - 16/3)/sigma at rho = 0 and rho = {rho_cmb:+.2f} ===")
res = {}
for n, c, dc, b, db in rows:
    p0, R = pull(c, dc, b, db, 0.0); p1, _ = pull(c, dc, b, db, rho_cmb)
    res[n] = (p0, p1)
    print(f"  {n:32s} R = {R:.3f}   rho=0: {p0:+.2f}σ   rho={rho_cmb:+.2f}: {p1:+.2f}σ")

print("\n=== P-ACT-LB2: the rho at which |pull| crosses 3 sigma ===")
c, dc, b, db = 11.74, 0.06, 2.258, 0.010
rho_x = -1.0
for k in range(0, -1001, -1):
    rho = k / 1000
    if abs(pull(c, dc, b, db, rho)[0]) < 3:
        rho_x = rho; break
print(f"  |pull| < 3 sigma once rho <= {rho_x:+.3f}; CMB-compression rho = {rho_cmb:+.3f}")
check("CMB-only combinations all within 2 sigma of 16/3 (rho = 0)",
      all(abs(v[0]) < 2 for k, v in res.items() if "DESI" not in k))
check("P-ACT-LB2 past 3 sigma with uncorrelated errors (reported, not hidden)", abs(res["P-ACT-LB2, DESI DR2 (ACT T5)"][0]) > 3)
straddle = (rho_cmb <= rho_x)
print(f"  -> with the CMB-compression rho the P-ACT-LB2 pull is {res['P-ACT-LB2, DESI DR2 (ACT T5)'][1]:+.2f}σ "
      f"({'UNDER' if straddle else 'OVER'} 3σ). The P-ACT-LB2 chain's own rho is NOT printed: the verdict waits on it.")
print("\n=== (2) A2's kaon line as a LATTICE number (round 4 item 2) ===")
# K_mu2 measures |V_us/V_ud| * f_K/f_pi = 0.27679(28)BR(20)corr (PDG 2026 Vud/Vus Eq. 67.15).
# A2 fixes |V_us| = 1/sqrt20 and |V_ud| = sqrt(19/20)  =>  |V_us/V_ud| = 1/sqrt19 exactly.
# So A2 PREDICTS f_K+/f_pi+ = 0.27679 * sqrt(19): 'the K_mu2 route moves' means the lattice ratio moves up to this.
for f, s in [("vv26.txt", "0.27679(28)BR (20)corr"), ("vv26.txt", "1.1978(22) Nf = 2 + 1 + 1"),
             ("flag.txt", "fK ± /fπ± = 1.1934(19)"), ("r4/a2605.06560.txt", "1.1962(34)"),
             ("r4/a2512.19294.txt", "1.1848(59)stat (84)χ−cont (24)SU(2)")]:
    check(f"{f}: '{s}'", has(f, s))
P, dP = 0.27679, math.hypot(0.00028, 0.00020)
fk_pred, dfk_pred = P * math.sqrt(19), dP * math.sqrt(19)
print(f"  A2 predicts f_K+/f_pi+ = 0.27679 x sqrt(19) = {fk_pred:.5f} ± {dfk_pred:.5f}")
lat = [("FLAG 2024 Nf=2+1+1 (Eq. 76)", 1.1934, 0.0019), ("FLAG 2024 Nf=2+1 (Eq. 77)", 1.1916, 0.0034),
       ("PDG 2026 'FLAG' as quoted (Eq. 67.16) — NOT FLAG 2024's number", 1.1978, 0.0022),
       ("Hudspith et al. 2026 Nf=2+1+1 (arXiv:2605.06560 Eq. 1)", 1.1962, 0.0034),
       ("Conigli-Frison-Saez 2025 Nf=2+1 (arXiv:2512.19294 Eq. 5.7)", 1.1848, math.sqrt(0.0059**2 + 0.0084**2 + 0.0024**2))]
zs = []
for n, v, dv in lat:
    z = (fk_pred - v) / math.hypot(dv, dfk_pred); zs.append(z)
    print(f"  {n:62s} {v:.4f}({dv*1e4:.0f})  A2 is {z:+.2f}σ above it")
check("every current lattice f_K/f_pi sits BELOW A2's 1.2065 (the direction A2 needs is UP)", all(z > 0 for z in zs))
print(f"  FLAG 2024 2+1+1 alone: A2 needs the lattice ratio to move up by {fk_pred - 1.1934:.4f} ({(fk_pred - 1.1934) / 1.1934 * 100:.2f} %)")
print(f"\nSCORE {score[0]}/{score[1]}")
sys.exit(0 if score[0] == score[1] else 1)
