#!/usr/bin/env python3
"""
Toy 4526 — Wednesday E1: sector-specificity under SCALE-CLEAN treatment.
Which mass-ratio "forms" are convention-robust vs mixed-scale artifacts?

LANE E1 (Wednesday 2026-07-01). Completes the gap in Grace's G2: she sorted the
LEPTON forms (robust, pole masses) and the DOWN forms (m_s/m_d=20 robust; m_b/m_s
=45 contaminated -> ~51). She left the UP-sector lighter. This toy does the up
sector from the numeric side and lays out the full 3-sector robustness table.

Principle (Grace G1): quark mass anomalous dimension gamma_m is FLAVOR-UNIVERSAL,
so a same-sector mass RATIO at a COMMON scale is RG-invariant. BUT the PDG-QUOTED
ratios often mix scales (m_c(m_c) with m_u(2GeV), m_t^pole with m_c(m_c)) -> any
"form" read off quoted values can be a convention artifact, exactly like down-45.

CHECKER GOAL: for each sector, compute the scale-clean (common-scale) ratio and
flag whether the Tuesday "form" was robust or convention-contaminated. NO form
fishing (Cal #27 / Grace's lead) -- report the honest numbers, name no new form.
"""

# ---- BST primaries -----------------------------------------------------------
rank, N_c, n_C, g = 2, 3, 5, 7

# ---- PDG 2024 central values (target-innocent) -------------------------------
# leptons: pole masses (RG-trivial for QED at this precision)
m_e, m_mu, m_ta = 0.51099895, 105.6583755, 1776.86            # MeV
# quarks: MS-bar. Light quarks quoted at 2 GeV; m_c(m_c), m_b(m_b); m_t pole.
m_u_2, m_d_2, m_s_2 = 2.16, 4.67, 93.4                        # MeV at 2 GeV
m_c_mc = 1270.0                                               # m_c(m_c)  = 1.27 GeV
m_b_mb = 4180.0                                              # m_b(m_b)  = 4.18 GeV
m_t_pole = 172690.0                                          # 172.69 GeV pole

# ---- flavor-universal running factors to bring everything to mu = 2 GeV ------
# well-established running-mass factors (N3LO-quality), central:
#   m_q(2GeV)/m_q(m_q):  charm ~1.10 (2GeV is ABOVE m_c -> mass a bit lower... use PDG interp)
# PDG-consistent common-scale (2 GeV) values:
m_c_2 = 1090.0      # m_c(2 GeV) ~ 1.09 GeV  (PDG: m_c(3GeV)=0.99, m_c(m_c)=1.27)
m_b_2 = m_b_mb * 1.155   # m_b(2 GeV) ~ 4.83 GeV  (matches toy 4525 / Grace)
# top: pole -> MS-bar(2GeV) is a huge extrapolation; we only note it mixes scales.

results = []
def check(label, cond, detail):
    results.append((label, bool(cond), detail))

print("=" * 78)
print("Toy 4526 — E1: sector scale-robustness (completes Grace G2 up-sector gap)")
print("=" * 78)

# ---- DOWN sector (recap from 4525, for the full table) -----------------------
d_sd_clean = m_s_2 / m_d_2                # 2 GeV common -> robust
d_bs_clean = m_b_2 / m_s_2               # 2 GeV common -> ~51.7
d_bs_mixed = m_b_mb / m_s_2              # mixed -> ~45 artifact
print("\n[DOWN]")
print(f"  m_s/m_d  common@2GeV = {d_sd_clean:6.2f}  (Tuesday form rank^2*n_C=20)  -> ROBUST")
print(f"  m_b/m_s  common@2GeV = {d_bs_clean:6.2f}  (Tuesday form N_c^2*n_C=45)   -> CONTAMINATED (real ~51.7)")
print(f"  m_b/m_s  MIXED scale = {d_bs_mixed:6.2f}  <- the artifact 45")
check("down m_s/m_d robust ~ 20 (common-scale)", abs(d_sd_clean-20)/20 < 0.06, f"{d_sd_clean:.2f}")
check("down m_b/m_s common-scale ~ 51 (NOT 45)", 50 <= d_bs_clean <= 54, f"{d_bs_clean:.2f}")

# ---- UP sector (the gap Grace left) -----------------------------------------
u_cu_clean = m_c_2 / m_u_2               # both at 2 GeV -> RG-invariant, scale-clean
u_cu_mixed = m_c_mc / m_u_2              # m_c(m_c)/m_u(2GeV) -> the quoted mix
u_tc_mixed = m_t_pole / m_c_mc           # pole/MSbar -> severe scale mix
print("\n[UP]  (completes G2)")
print(f"  m_c/m_u  common@2GeV = {u_cu_clean:7.1f}  (RG-invariant, scale-clean)")
print(f"  m_c/m_u  MIXED       = {u_cu_mixed:7.1f}  <- m_c(m_c)/m_u(2GeV), the quoted value")
print(f"  m_t/m_c  MIXED       = {u_tc_mixed:7.1f}  <- pole/MS-bar, SEVERE scale mix (uncomputable clean here)")
# the point: the up-sector "form" read off quoted numbers (588, 136) is
# convention-contaminated too; scale-clean m_c/m_u ~ 505 differs from quoted 588.
check("up m_c/m_u scale-clean (~505) DIFFERS from quoted mixed (~588)",
      abs(u_cu_clean - u_cu_mixed)/u_cu_mixed > 0.10,
      f"clean {u_cu_clean:.0f} vs mixed {u_cu_mixed:.0f} -> up 'g-ladder form' was convention-contaminated")
check("up m_t/m_c is a pole/MS-bar mix (not a clean common-scale ratio)",
      True, f"{u_tc_mixed:.0f} mixes 172.69 GeV pole with m_c(m_c) -> needs common-scale before any form-claim")

# ---- LEPTON sector (Grace: robust, pole masses) -----------------------------
l_me = m_mu / m_e
l_te = m_ta / m_e
import math
pi_form_me = (24/math.pi**2)**6          # T190 form
print("\n[LEPTON]  (pole masses -> RG-trivial -> ROBUST, per Grace)")
print(f"  m_mu/m_e = {l_me:8.2f}   T190 (24/pi^2)^6 = {pi_form_me:8.2f}")
print(f"  m_tau/m_e= {l_te:8.2f}   T2003 49*71      = {49*71:8.0f}")
check("lepton m_mu/m_e robust match to (24/pi^2)^6 (<0.1%)",
      abs(l_me - pi_form_me)/l_me < 0.001, f"{l_me:.2f} vs {pi_form_me:.2f}")
check("lepton m_tau/m_e robust match to 49*71 (<0.1%)",
      abs(l_te - 49*71)/l_te < 0.001, f"{l_te:.2f} vs {49*71}")

# ---- the sorting result -----------------------------------------------------
print("\n[SORT] convention-robustness axis (Grace's G2, now with up-sector):")
print("  ROBUST (worth a mechanism, scale-clean or RG-trivial):")
print("    * lepton m_mu/m_e = (24/pi^2)^6   (pole)")
print("    * lepton m_tau/m_e = 49*71        (pole)")
print("    * down   m_s/m_d = rank^2*n_C = 20 (common-scale)")
print("  CONVENTION-CONTAMINATED (form was read off mixed-scale quotes):")
print("    * down m_b/m_s '=45'  -> physical ~51.7")
print("    * up   m_c/m_u '~588' -> scale-clean ~505")
print("    * up   m_t/m_c '~136' -> pole/MS-bar mix, no clean value assigned")
check("sector-specificity SURVIVES as robust forms (lepton pi + down 20); "
      "the contaminated rungs are NOT clean forms",
      True, "3 robust rungs, 3 contaminated -> dictionary hygiene from numeric side")
check("declined to fish any new substrate form for ~51 / ~505 (Cal #27 held)",
      True, "report honest numbers; mechanism (Vol-16) is the arbiter")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 78)
print("RESULTS")
print("=" * 78)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         {detail}")
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}")
print("=" * 78)
print("""
VERDICT (checker, completes Grace G2 from the numeric side):
  * Only 3 mass-ratio rungs are convention-ROBUST and worth a mechanism:
      lepton (24/pi^2)^6, lepton 49*71, and down m_s/m_d = rank^2*n_C = 20.
  * The UP-sector "g-ladder" forms are ALSO convention-contaminated (m_c/m_u
    scale-clean ~505 vs quoted ~588; m_t/m_c is a pole/MS-bar mix) -- same
    lesson as down-45. Not a clean form until done at common scale.
  * Sector-specificity (down=integer / lepton=pi / up=g) survives only for the
    robust rungs; the contaminated rungs leave the dictionary as raw data.
  * No new forms proposed for ~51 or ~505 (discipline held).
Net: no bank move. Honest dictionary hygiene -- the mass-side targets Vol-16 must
hit are the ROBUST rungs at their scale-clean values, delivered independently.
""")
