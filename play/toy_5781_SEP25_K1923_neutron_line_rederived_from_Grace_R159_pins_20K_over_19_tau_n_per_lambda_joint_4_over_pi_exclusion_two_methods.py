#!/usr/bin/env python3
"""
Toy 5781 — K1923 Sections 2-3 re-derived from Grace's pins (Elie, 2026-09-25).
Keeper's script (keeper_K1923_neutron_lifetime_and_colour_stabilizers.py) NOT opened before this ran.

INPUTS (every number pinned; source in the comment):
  A2      |V_ud|^2 = 19/20                     register row A2 (lambda = 1/sqrt20, first row unitary)
  tau_U   877.82 +- 0.22 s                     UCNtau, arXiv:2409.05560, PRC 111 045501 (2025)   [Grace R159 l.23]
  tau_U21 877.75 +- 0.34 s                     UCNtau 2021 value, as used by Keeper K1923 (for the diff only)
  lam_P   1.27641, (45)stat (33)sys            PERKEO III, PRL 122 242501                        [Grace R159 l.23]
  Vud_n   0.97413 +- 0.00042                   PDG 2026 Eq. 67.8, built on tau_U and lam_P        [Grace R159 l.23]
  K_a     4905.7 +- 1.7 s                      arXiv:2501.17916 (as quoted in K1923; Grace pins in round 2)
  K_b     4908 +- 4 s                          Czarnecki-Marciano-Sirlin 2018 (as quoted in K1923)
Master formula: |V_ud|^2 tau_n (1 + 3 lambda^2) = K.

METHOD 1 (product space, K1923's): compare tau_n(1+3 lam^2) with 20K/19.
METHOD 2 (V_ud space, independent of K's quoted value): back out the K that PDG 2026 used from
          its own Eq. 67.8 (K_pdg = Vud_n^2 tau_U (1+3 lam_P^2)), then compare Vud_n with sqrt(19/20)
          directly. The two methods must agree on the sign and rough size of the pull.
"""
from math import sqrt, pi

checks = []
def check(name, ok, can_fail=True):
    checks.append((name, bool(ok), can_fail))
    print(f"  [{'PASS' if ok else 'FAIL'}]{'' if can_fail else ' (control)'} {name}")

A2 = 19/20
tau_U, s_tau_U = 877.82, 0.22
tau_U21, s_tau_U21 = 877.75, 0.34
lam_P, s_lam_P = 1.27641, sqrt(0.00045**2 + 0.00033**2)
Vud_n, s_Vud_n = 0.97413, 0.00042
Ks = {"K_a 4905.7(1.7) [2501.17916]": (4905.7, 1.7), "K_b 4908(4) [CMS 2018]": (4908.0, 4.0)}
lam_pi = 4/pi

def prod(tau, s_tau, lam, s_lam):
    f = 1 + 3*lam**2
    return tau*f, sqrt((s_tau*f)**2 + (tau*6*lam*s_lam)**2)

print("Toy 5781 — neutron line, re-derived\n")
print(f"INPUT DIFFERENCE vs K1923 (posted first): UCNtau {tau_U} +- {s_tau_U} s (PDG 2026 pin) vs {tau_U21} +- {s_tau_U21} s (K1923).")

print("\nMETHOD 1 — product space")
P, sP = prod(tau_U, s_tau_U, lam_P, s_lam_P)
P21, sP21 = prod(tau_U21, s_tau_U21, lam_P, s_lam_P)
print(f"  measured tau(1+3lam^2): {P:.1f} +- {sP:.1f} s (2024 tau);  {P21:.1f} +- {sP21:.1f} s (K1923's tau)")
pulls = {}
for name, (K, sK) in Ks.items():
    pred, spred = K/A2, sK/A2
    z = (P - pred)/sqrt(sP**2 + spred**2)
    z21 = (P21 - pred)/sqrt(sP21**2 + spred**2)
    pulls[name] = z
    print(f"  {name}: 20K/19 = {pred:.1f} +- {spred:.1f} s | pull {z:+.2f} sigma (2024 tau), {z21:+.2f} sigma (K1923 tau)")
    if name.startswith("K_a"):
        check("K1923's 0.87 sigma reproduced on its own inputs (K_a, tau 877.75) within 0.05",
              abs(z21 - 0.87) < 0.05, can_fail=False)
check("A2 product agrees with measured within 2 sigma for every pinned K and the 2024 tau",
      all(abs(z) < 2 for z in pulls.values()))

print("\n  tau_n predicted by A2 for each lambda (K_a):")
K, sK = Ks["K_a 4905.7(1.7) [2501.17916]"]
for lname, lam, slam in [("PERKEO III", lam_P, s_lam_P), ("4/pi (March)", lam_pi, 0.0)]:
    t = K/A2/(1 + 3*lam**2)
    st = sqrt((sK/A2/(1+3*lam**2))**2 + (t*6*lam*slam/(1+3*lam**2))**2)
    print(f"    lambda={lam:.5f} ({lname}): tau_n = {t:.2f} +- {st:.2f} s")
    if lname == "PERKEO III":
        tP, stP = t, st
    else:
        tpi, stpi = t, st
check("A2 + PERKEO lambda gives the bottle (|tau - 877.82| < 2 sigma)",
      abs(tP - tau_U)/sqrt(stP**2 + s_tau_U**2) < 2)
beam = 887.7  # K1923's '~887.7 s' beam figure; Grace pins the beam average with error in round 2
check("A2 + PERKEO lambda sits > 10 s below the ~887.7 s beam figure (error pending Grace)",
      beam - tP > 10)

lam_imp = sqrt((K/A2/tau_U - 1)/3)
print(f"  lambda implied by A2 + UCNtau(2024) + K_a: {lam_imp:.5f}")

print("\n  g_A = 4/pi:")
zP = (lam_P - lam_pi)/s_lam_P
zj = (tpi - tau_U)/sqrt(stpi**2 + s_tau_U**2)
zj21 = (tpi - tau_U21)/sqrt(stpi**2 + s_tau_U21**2)
print(f"    vs PERKEO III alone: {zP:.2f} sigma")
print(f"    jointly with A2: tau_n(4/pi) = {tpi:.2f} +- {stpi:.2f} s vs {tau_U} -> {zj:.2f} sigma "
      f"(K1923's tau: {zj21:.2f} sigma)")
check("4/pi vs PERKEO III > 5 sigma", zP > 5)
check("4/pi joint with A2 > 5 sigma on the 2024 UCNtau", zj > 5)
check("K1923's 6.4 sigma reproduced on its own inputs within 0.1", abs(zj21 - 6.4) < 0.1, can_fail=False)
for name, (Kb, sKb) in Ks.items():
    tb = Kb/A2/(1 + 3*lam_pi**2); stb = sKb/A2/(1 + 3*lam_pi**2)
    print(f"    joint, {name}: tau(4/pi) = {tb:.2f} +- {stb:.2f} -> {(tb - tau_U)/sqrt(stb**2 + s_tau_U**2):.2f} sigma")

print("\nMETHOD 2 — V_ud space (K backed out of PDG 2026's own Eq. 67.8)")
K_pdg = Vud_n**2 * P
print(f"  K implied by PDG 2026 = Vud_n^2 tau (1+3 lam^2) = {K_pdg:.1f} s  (vs K_a 4905.7, K_b 4908)")
z2 = (sqrt(A2) - Vud_n)/s_Vud_n
print(f"  sqrt(19/20) = {sqrt(A2):.6f} vs neutron |V_ud| {Vud_n}({int(s_Vud_n*1e5)}) -> {z2:+.2f} sigma")
check("method 2 reproduces Grace R159's +1.31 sigma within 0.02", abs(z2 - 1.31) < 0.02)
check("both methods give the same sign (A2 above the neutron |V_ud| <=> product below measured)",
      z2 > 0 and pulls["K_a 4905.7(1.7) [2501.17916]"] > 0)
pred_pdgK = K_pdg/A2
zK = (P - pred_pdgK)/sqrt(sP**2 + (1.7/A2)**2)
print(f"  method 1 re-run with PDG's implied K: pull {zK:+.2f} sigma (uncertainty on K taken as K_a's 1.7 s)")
check("with PDG's own K, method 1 lands within 0.3 sigma of method 2", abs(zK - z2) < 0.3)

n = len(checks); k = sum(ok for _, ok, _ in checks)
cf = [c for c in checks if c[2]]; kcf = sum(ok for _, ok, _ in cf)
print(f"\nSCORE {k}/{n}  (can-fail {kcf}/{len(cf)}; {n-len(cf)} controls)")
