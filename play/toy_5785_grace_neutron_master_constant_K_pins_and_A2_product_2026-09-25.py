#!/usr/bin/env python3
"""
Toy 5785 — Grace, 2026-09-25. Which master-formula constant K, and what A2's
g_A-free neutron product does under each.

K1923 Section 2: |V_ud|^2 tau_n (1 + 3 lambda^2) = K; A2 (|V_ud|^2 = 19/20) predicts
tau_n (1 + 3 lambda^2) = 20K/19. K1923 used K = 4905.7(1.7) s "arXiv:2501.17916" and
4908(4) s "CMS 2018". This toy pins K from the primaries retained in
data/sources_grace_2026-09-25/ (grep-checked; the toy FAILS if a string is absent)
and reruns the compare line for each. No BST number is adjusted.

2501.17916 (Vander Griend, Cao, Hill, Plestid 2025) prints no K; its Eq. (28) is
  tau_n |V_ud|^2 (1+3 lambda^2)(1 + Delta_R)(1 + 27.04(7)e-3) = 5263.284(17) s
with Delta_R = 45.37(27)e-3 (their footnote 3), so K = 5263.284 / [(1+Delta_R)(1+0.02704)]
(arithmetic here, labelled). PDG 2026 Eq. 67.5: |V_ud|^2 = 5099.33 s / [tau(1+3g^2)(1+Delta_R)],
Delta_R = 0.03983(27) -> K = 5099.33/(1+Delta_R) (arithmetic here).
"""
import math, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "sources_grace_2026-09-25")
score = [0, 0]
def check(name, ok):
    score[1] += 1; score[0] += bool(ok); print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
def has(f, s):
    with open(os.path.join(SRC, f), encoding="utf-8", errors="replace") as fh: return s in fh.read()

print("=== primaries: printed strings present ===")
for f, s in [("neutron/2501.17916.txt", "5263.284(17) s"), ("neutron/2501.17916.txt", "0.97393(41)"),
             ("neutron/2501.17916.txt", "45.37(27)"), ("neutron/cms2018.txt", "4908.6(1.9)s"),
             ("neutron/cms2019.txt", "4906.4(1.7) s"), ("neutron/gorchteinseng2021.txt", "4903.1(1.1) s"),
             ("neutron/wietfeldt2024.txt", "4905.7(1.7)s"), ("vv26.txt", "5099.33 s"), ("vv26.txt", "0.03983(27)")]:
    check(f"{f}: '{s}'", has(f, s))
check("2501.17916 does NOT print 4905.7 (K1923's attribution)", not has("neutron/2501.17916.txt", "4905.7"))

K_vg = 5263.284 / (1.04537 * 1.02704)
dK_vg = K_vg * math.hypot(0.00027 / 1.04537, 0.00007 / 1.02704)
K_pdg = 5099.33 / 1.03983
dK_pdg = K_pdg * 0.00027 / 1.03983
Ks = [("Vander Griend-Cao-Hill-Plestid 2025, Eq. 28 (arith)", K_vg, dK_vg),
      ("Gorchtein-Seng 2021, Eq. 2", 4903.1, 1.1),
      ("PDG 2026 Eq. 67.5 with Delta_R 0.03983(27) (arith)", K_pdg, dK_pdg),
      ("Wietfeldt 2024 Eq. 3 (secondary; credits CMS PRD 2019)", 4905.7, 1.7),
      ("Czarnecki-Marciano-Sirlin PRD 100 (2019) arXiv v1 Eq. 49", 4906.4, 1.7),
      ("Czarnecki-Marciano-Sirlin PRL 120 (2018) Eq. 2", 4908.6, 1.9)]

meas = [("UCNtau 2021 877.75(34) + PERKEO III 1.27641(56)", 877.75, 0.34, 1.27641, 0.00056),
        ("UCNtau all-data 877.82(30) + PERKEO III", 877.82, 0.30, 1.27641, 0.00056),
        ("UCNtau all-data + PDG 2026 lambda 1.2753(13)", 877.82, 0.30, 1.2753, 0.0013)]
print("\n=== A2 predicts tau(1+3 lambda^2) = 20K/19; compare (read last) ===")
res = {}
for kn, K, dK in Ks:
    P, dP = 20 * K / 19, 20 * dK / 19
    print(f"  K = {K:8.2f}({dK:.1f}) s  [{kn}]  ->  20K/19 = {P:.1f} ± {dP:.1f} s")
    for mn, t, dt, l, dl in meas:
        m = t * (1 + 3 * l * l)
        dm = math.hypot(dt * (1 + 3 * l * l), t * 6 * l * dl)
        z = (m - P) / math.hypot(dm, dP)
        res[(kn, mn)] = z
        print(f"        measured {m:.1f} ± {dm:.1f}  [{mn}]  ->  {z:+.2f} sigma")
check("K1923's 0.87 sigma reproduced on its own inputs (K 4905.7, UCNtau 2021 + PERKEO)",
      abs(res[(Ks[3][0], meas[0][0])] - 0.87) < 0.03)
z_new = res[(Ks[0][0], meas[1][0])]
check("on the newest K (2501.17916) and newest UCNtau the tension exceeds K1923's 0.87 sigma", z_new > 1.0)
print(f"\n  newest-on-newest: {z_new:+.2f} sigma")
vud_bst = math.sqrt(19 / 20)
print(f"  sqrt(19/20) = {vud_bst:.6f} vs 2501.17916's neutron |V_ud| 0.97393(41): {(vud_bst - 0.97393) / 0.00041:+.2f} sigma")
print("\n=== E7: g_A = 4/pi jointly with A2, per K (tau = 20K/19 / (1+3(4/pi)^2)) ===")
g = 4 / math.pi; f = 1 + 3 * g * g
zs = []
for kn, K, dK in Ks:
    t, dt = 20 * K / 19 / f, 20 * dK / 19 / f
    z = (t - 877.82) / math.hypot(dt, 0.30); zs.append(z)
    print(f"  K {K:8.2f}: tau = {t:.2f} ± {dt:.2f} s vs UCNtau all-data 877.82(30) -> {z:+.2f} sigma")
print(f"  4/pi vs PERKEO III 1.27641(56): {(1.27641 - g) / 0.00056:+.2f} sigma; vs PDG 2026 1.2753(13) S=2.7: {(1.2753 - g) / 0.0013:+.2f} sigma")
check("g_A = 4/pi excluded jointly with A2 at > 5 sigma on every pinned K", min(zs) > 5)
print(f"\nSCORE {score[0]}/{score[1]}")
sys.exit(0 if score[0] == score[1] else 1)
