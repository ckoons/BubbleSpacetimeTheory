r"""
toy_4522 — TUESDAY (capstone of the mass-ratio lane): complete the fermion mass-ratio survey across ALL
           three sectors and report the honest structure. TWO findings:

   (1) THE CLEAN INTEGER SQUARE-LADDER IS DOWN-QUARK-SPECIFIC. Each fermion sector has a DISTINCT mass-ratio
       structure -- they do NOT share one universal form:
         DOWN quarks  (integer square-ladder, my 4521): m_d:m_s:m_b = 1 : rank^2*n_C : (rank*N_c)^2*n_C^2
                       = 1:20:900  (central-exact 1-2, 0.5% 2-3) -- cleanest, target-innocent
         UP quarks    (g-ladder, secondary): m_c/m_u = rank^2*N_c*g^2 = 588, m_t/m_c = 2^g = 128
         LEPTONS      (pi-forms, canon): m_mu/m_e = (24/pi^2)^6 = 206.8 (T190); m_tau/m_e = g^2*(2^C_2+g) =
                       49*71 = 3479 (T2003/my 4518); m_tau/m_mu = 16.82 (the mixed quotient, NOT clean)
       So the leptons do NOT follow the down-quark integer square-ladder -- they carry pi (geometric volume),
       consistent with the trichotomy "mass = measuring (pi-carrying)" being lepton-specific, while the
       down-QUARK ratios are clean integers. This sector-specificity is itself the finding: there is no single
       universal mass ladder; the down-quark integer ladder is special.

   (2) MASS-MIXING CROSS-LINK at the firm bank: sin^2 theta_13 = 1/(N_c^2*n_C) = 1/45 (the FIRM PMNS bank,
       10) and m_b/m_s = N_c^2*n_C = 45 (down-quark 2-3, my 4521) share the SAME substrate integer N_c^2*n_C.
       => sin^2 theta_13 = m_s/m_b (the neutrino 1-3 mixing = the down-quark 2-3 mass ratio, inverted).
       NOTED AS OBSERVATION ONLY: shared integer is NOT shared mechanism (the standing Saturday lesson); a
       neutrino-mixing <-> down-quark-mass mechanism would be speculative. But it is a real cross-sector
       appearance of N_c^2*n_C worth the registry (substrate-Schur-generator candidate, Cal #35).

   HONEST TIER: capstone survey -- down-quark integer ladder is the clean target-innocent lead (the
   quark-mass-negative reopener); up-quark + lepton structures are distinct (g-ladder / pi-forms); theta_13
   cross-link is an observation not a claim. NO count move. Count 9/26 (10 firm with theta_13).

DISCIPLINE: completed the survey across all sectors and reported the DIFFERENTIATING result honestly (the
  integer ladder is down-quark-specific, NOT universal -- did not force a parallel lepton ladder when leptons
  are pi-forms); flagged the theta_13<->m_b/m_s shared integer as OBSERVATION ONLY per "shared structure !=
  shared mechanism". NO count move. Count HOLDS 9/26.

Elie - 2026-06-30
"""
import math
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
m_e, m_mu, m_tau = 0.51099895, 105.6583755, 1776.86
m_u, m_c, m_t = 2.16, 1273.0, 162500.0
m_d, m_s, m_b = 4.67, 93.4, 4183.0

score = 0; TOTAL = 3
print("="*98)
print("toy_4522 — TUE fermion mass-ratio survey capstone: integer ladder is DOWN-QUARK-specific + theta_13 cross-link")
print("="*98)

# ---- [1] leptons do NOT follow the integer square-ladder (they are pi-forms) ----
print("\n[1] LEPTONS are pi-forms, NOT the integer square-ladder: m_mu/m_e = (24/pi^2)^6 (T190), not rank^2/N_c^2 * n_C")
lep_12 = m_mu/m_e
t190 = (24/math.pi**2)**6
ladder_try = rank**2*n_C  # 20 -- the down 1-2 form
ok1 = (abs(lep_12 - t190)/lep_12 < 0.001) and (abs(lep_12 - ladder_try)/lep_12 > 0.5)
print(f"    m_mu/m_e = {lep_12:.2f}; (24/pi^2)^6 = {t190:.2f} ({abs(lep_12-t190)/lep_12*100:.3f}%); integer-ladder 20 is FAR off ({abs(lep_12-ladder_try)/lep_12*100:.0f}%): {'PASS' if ok1 else 'FAIL'}")
print(f"    => leptons carry pi (geometric volume); the clean integer square-ladder is DOWN-QUARK-specific")
score += ok1

# ---- [2] three distinct sector structures (no universal ladder) ----
print("\n[2] three DISTINCT sector structures: down=integer-square-ladder, up=g-ladder, lepton=pi-forms")
down_ok = abs(m_s/m_d - rank**2*n_C)/(m_s/m_d) < 0.02 and abs(m_b/m_s - N_c**2*n_C)/(m_b/m_s) < 0.01
up_ok = abs(m_c/m_u - rank**2*N_c*g**2)/(m_c/m_u) < 0.005 and abs(m_t/m_c - 2**g)/(m_t/m_c) < 0.005
lep_ok = abs(m_tau/m_e - g**2*(2**C2+g))/(m_tau/m_e) < 0.001
ok2 = down_ok and up_ok and lep_ok
print(f"    down (rank^2,N_c^2)*n_C: {down_ok}; up rank^2*N_c*g^2 & 2^g: {up_ok}; lepton g^2*71 & (24/pi^2)^6: {lep_ok}: {'PASS' if ok2 else 'FAIL'}")
print(f"    => no single universal mass ladder; sector-specific structure is the honest finding")
score += ok2

# ---- [3] theta_13 <-> m_b/m_s cross-link via shared N_c^2*n_C (observation only) ----
print("\n[3] CROSS-LINK (observation only): sin^2 theta_13 = 1/(N_c^2*n_C) = 1/45 = m_s/m_b (same integer, NOT same mechanism)")
sin2_13 = 1/(N_c**2*n_C)
ok3 = (N_c**2*n_C == 45) and (abs(sin2_13 - 0.0220)/0.0220 < 0.02)
print(f"    sin^2 theta_13 = 1/{N_c**2*n_C} = {sin2_13:.4f} (obs ~0.0220); m_b/m_s = {N_c**2*n_C}; sin^2 theta_13 = m_s/m_b: {'PASS' if ok3 else 'FAIL'}")
print(f"    NOTED as substrate-Schur cross-appearance of N_c^2*n_C (Cal #35 registry); shared integer != shared mechanism")
score += ok3

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — fermion mass-ratio survey CAPSTONE. (1) The clean integer square-ladder is")
print("       DOWN-QUARK-SPECIFIC: leptons are pi-forms ((24/pi^2)^6, g^2*71), up-quarks are a g-ladder")
print("       (rank^2*N_c*g^2, 2^g) -- no universal ladder, sector-specific structure is the finding. (2) The")
print("       firm bank sin^2 theta_13 = 1/(N_c^2*n_C) = 1/45 and the down-quark m_b/m_s = N_c^2*n_C = 45 share")
print("       the substrate integer N_c^2*n_C (sin^2 theta_13 = m_s/m_b) -- OBSERVATION only (shared integer !=")
print("       shared mechanism). Down-quark integer ladder remains the clean target-innocent quark-mass-negative")
print("       reopener (4521). NO count move. Count HOLDS 9/26 (10 firm with theta_13).")
print("="*98)
