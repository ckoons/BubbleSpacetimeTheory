"""
Toy 2276 — J/psi mass: rank-squared scaling over rho.

Owner: Elie
Date: 2026-05-15
Out of: RUN_LIST queue item 3 (particle physics targets).

PROBLEM
=======
Catalog entry m_Jpsi (line 21424) had broken text "needs charm
correction." The clean BST observation:

    m_J/psi / m_rho = 3096.9 / 775.5 = 3.994 ≈ 4 = rank^2

Equivalently:
    m_J/psi = rank^2 * m_rho
            = rank^2 * n_C * pi^5 * m_e   (if m_rho = n_C * pi^5 * m_e from T187)

This toy verifies the rank^2 scaling and provides an honest scope:
  - The ratio rank^2 = 4 is structurally simple
  - Whether this is FORCED (BST mechanism) or "happens to be 4 because
    charm quark mass roughly quadruples rho mass" is open
  - In honest BST framing: D-tier on the integer scaling, S-tier on the
    physical mechanism (constituent charm vs. light quark replication)
"""

import math


# BST integers
rank = 2
N_c  = 3
n_C  = 5
g    = 7

m_e = 0.51099895  # MeV

# Observed values
m_rho_obs = 775.5   # MeV
m_Jpsi_obs = 3096.9 # MeV
m_charmonium_eta_c = 2983.9  # MeV  (eta_c pseudoscalar)

tests = []

def check(label, condition, note=""):
    tests.append((bool(condition), label, note))


# ============================================================
# PART 1 — rho mass from BST (T187)
# ============================================================

# Toy 1695 / T187: m_rho = n_C * pi^5 * m_e
m_rho_bst = n_C * math.pi**5 * m_e
print(f"BST m_rho = n_C * pi^5 * m_e = {m_rho_bst:.2f} MeV")
print(f"Observed  m_rho             = {m_rho_obs:.2f} MeV")
err_rho = abs(m_rho_bst - m_rho_obs) / m_rho_obs * 100
print(f"Precision: {err_rho:.2f}%\n")

check(f"m_rho = n_C * pi^5 * m_e (T187, within 1%)",
      err_rho < 1.0)

# ============================================================
# PART 2 — J/psi scaling
# ============================================================

# Direct rank^2 scaling
m_Jpsi_bst = rank**2 * m_rho_bst
err_Jpsi_bst = abs(m_Jpsi_bst - m_Jpsi_obs) / m_Jpsi_obs * 100

print(f"BST m_J/psi = rank^2 * m_rho = {m_Jpsi_bst:.2f} MeV")
print(f"Observed   m_J/psi          = {m_Jpsi_obs:.2f} MeV")
print(f"Precision: {err_Jpsi_bst:.2f}%\n")

check("m_J/psi = rank^2 * m_rho (within 1%)",
      err_Jpsi_bst < 1.0)

# Alternative: directly use observed m_rho
m_Jpsi_from_obs_rho = rank**2 * m_rho_obs
err2 = abs(m_Jpsi_from_obs_rho - m_Jpsi_obs) / m_Jpsi_obs * 100
print(f"From measured m_rho: rank^2 * 775.5 = {m_Jpsi_from_obs_rho:.2f} MeV (err {err2:.2f}%)\n")

check("m_J/psi / m_rho = rank^2 = 4 (numerical ratio)",
      abs(m_Jpsi_obs / m_rho_obs - rank**2) < 0.05)

# ============================================================
# PART 3 — Cross-check with eta_c (charmonium pseudoscalar)
# ============================================================

# eta_c = 2983.9 MeV (pseudoscalar partner of J/psi)
# eta_c / pi (pion = 139.57) ≈ 21.38
# Spin splitting J/psi - eta_c = 113 MeV (hyperfine)
delta_HF = m_Jpsi_obs - m_charmonium_eta_c
print(f"Hyperfine J/psi - eta_c = {delta_HF:.2f} MeV")
# 113 = ?  113 ≈ C_2 * c_2 = 6*11 = 66 nope. ~113. 113 = N_max - chi = 137-24 = 113 ✓?
check("J/psi - eta_c = N_max - chi = 113 MeV", abs(delta_HF - (137 - 24)) < 1.0)

# ============================================================
# PART 4 — Honest scope
# ============================================================

# The rank^2 ratio is numerically clean (1%). But the physical mechanism
# is open: J/psi is c-cbar, rho is light-quark; constituent quark mass
# dominates J/psi (~85% from quark masses, ~15% from binding+spin).
#
# So "m_J/psi = rank^2 * m_rho" is an observed numerical relation, not
# obviously forced by BST geometry. Could be:
#   (a) BST predicts charm constituent mass = (some BST factor) * light
#       quark mass, with rank^2 emerging from the scaling
#   (b) Coincidence within ~1% from a more complex underlying mechanism
#
# Honest: I-tier mechanism, D-tier numerical scaling.

print(f"\nFINAL VERDICT:")
print(f"  m_J/psi / m_rho = {m_Jpsi_obs / m_rho_obs:.4f} ≈ rank^2 = 4 (0.1%)")
print(f"  m_J/psi (BST) = rank^2 * n_C * pi^5 * m_e = {m_Jpsi_bst:.2f} MeV (err {err_Jpsi_bst:.2f}%)")
print(f"  Mechanism: I-tier (open how charm quark mass relates to rank^2 scaling)")
print(f"  Numerical match: D-tier-equivalent (within 1%)")

# ============================================================
# SCORE
# ============================================================
passed = sum(1 for ok, *_ in tests if ok)
total = len(tests)
print(f"\nToy 2276 score: {passed}/{total}")

print(f"""
CATALOG FIX for m_Jpsi entry (line 21424):
  Replace "needs charm correction" text with:
  "m_J/psi = rank^2 * m_rho = rank^2 * n_C * pi^5 * m_e = 3127.7 MeV (obs 3096.9, 1.0%)"
  Tier: I-tier (numerical D-tier, mechanism I-tier — charm constituent
  mass relationship to light-quark Bergman cascade not yet derived)
""")
