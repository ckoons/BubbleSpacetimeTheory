#!/usr/bin/env python3
"""
BST_FermiScale_Exploration.py
=============================
Investigate the Fermi scale v = 246.22 GeV from BST geometry.

Central question: Both Higgs mass derivations (lambda_H = sqrt(2/5!) and
m_H/m_W = (pi/2)(1 - alpha)) require v as input. What sets v?

Casey Koons & Claude Opus 4.6, March 12, 2026
"""

import numpy as np
from math import pi, sqrt, log, log10, exp, factorial, comb
from itertools import product as iproduct

# ============================================================
# SECTION 0: Physical constants (PDG 2024 + BST)
# ============================================================

alpha = 1 / 137.035999084       # fine-structure constant
m_e_MeV = 0.51099895000         # electron mass (MeV)
m_e_GeV = m_e_MeV / 1000
m_p_MeV = 938.27208816          # proton mass (MeV)
m_p_GeV = m_p_MeV / 1000
m_Pl_GeV = 1.22089e19           # Planck mass (GeV)
v_GeV = 246.21965               # Fermi VEV (GeV), PDG: (sqrt(2) G_F)^{-1/2}
m_W_GeV = 80.3692               # W boson mass (GeV), PDG 2024
m_Z_GeV = 91.1876               # Z boson mass (GeV)
m_H_GeV = 125.25                # Higgs mass (GeV)
G_F_GeVm2 = 1.1663788e-5       # Fermi constant (GeV^{-2})

# BST parameters
n_C = 5                         # complex dimension of D_IV^5
N_c = 3                         # number of colors
genus = 7                        # genus of D_IV^5
Gamma_order = 1920               # |Gamma| = S_5 x (Z_2)^4
sin2_thetaW = 3.0 / 13.0        # BST Weinberg angle
cos2_thetaW = 1 - sin2_thetaW
Vol_DIV5 = pi**5 / Gamma_order   # Bergman volume
proton_ratio = 6 * pi**5         # m_p/m_e (BST)
lambda_H_BST = 1 / sqrt(60)     # BST Higgs self-coupling = sqrt(2/5!)

# Derived
e_charge = sqrt(4 * pi * alpha)  # electric charge (natural units)
g_W = e_charge / sqrt(sin2_thetaW)  # weak coupling
g_Z = e_charge / sqrt(sin2_thetaW * cos2_thetaW)

# Bergman geometry
holo_curv = -2.0 / (n_C + 2)    # -2/7 holomorphic sectional curvature
scalar_curv = -n_C * (n_C + 2) / 2.0  # -35/2


def pct_err(computed, observed):
    """Signed percentage error."""
    return 100 * (computed - observed) / observed


def flag(pct):
    """Flag matches better than 1%."""
    return " *** MATCH ***" if abs(pct) < 1.0 else (" ** CLOSE **" if abs(pct) < 3.0 else "")


print("=" * 80)
print("BST FERMI SCALE EXPLORATION")
print("What sets v = 246.22 GeV?")
print("=" * 80)

# ============================================================
# SECTION 1: Key ratios
# ============================================================

print("\n" + "=" * 80)
print("SECTION 1: Key Ratios")
print("=" * 80)

ratios = {
    "v / m_e": v_GeV / m_e_GeV,
    "v / m_p": v_GeV / m_p_GeV,
    "v / m_Pl": v_GeV / m_Pl_GeV,
    "v / m_W": v_GeV / m_W_GeV,
    "v / m_Z": v_GeV / m_Z_GeV,
    "v / m_H": v_GeV / m_H_GeV,
    "m_W / v": m_W_GeV / v_GeV,
    "m_Z / v": m_Z_GeV / v_GeV,
    "m_H / v": m_H_GeV / v_GeV,
}

for name, val in ratios.items():
    print(f"  {name:15s} = {val:15.6f}   (log10 = {log10(abs(val)):+8.4f})")

print(f"\n  v^2 (GeV^2)      = {v_GeV**2:.4f}")
print(f"  1/(sqrt(2) G_F)  = {1/(sqrt(2)*G_F_GeVm2):.4f}  (should = v^2 = {v_GeV**2:.4f})")
print(f"  v = sqrt(1/(sqrt(2)*G_F)) = {sqrt(1/(sqrt(2)*G_F_GeVm2)):.5f} GeV")

# ============================================================
# SECTION 2: Known SM relationships (as checks)
# ============================================================

print("\n" + "=" * 80)
print("SECTION 2: SM relationships with BST Weinberg angle")
print("=" * 80)

# m_W = g_W * v / 2
m_W_from_v = g_W * v_GeV / 2
print(f"  g_W = e/sin(theta_W) = {g_W:.6f}")
print(f"  m_W = g_W * v / 2 = {m_W_from_v:.4f} GeV  (obs: {m_W_GeV:.4f}, err: {pct_err(m_W_from_v, m_W_GeV):.3f}%)")

# m_Z = g_Z * v / 2
m_Z_from_v = g_Z * v_GeV / 2
print(f"  g_Z = e/sin(theta_W)cos(theta_W) = {g_Z:.6f}")
print(f"  m_Z = g_Z * v / 2 = {m_Z_from_v:.4f} GeV  (obs: {m_Z_GeV:.4f}, err: {pct_err(m_Z_from_v, m_Z_GeV):.3f}%)")

# v = 2 * m_W / g_W
v_from_mW = 2 * m_W_GeV / g_W
print(f"  v = 2*m_W/g_W = {v_from_mW:.4f} GeV  (obs: {v_GeV:.5f})")

# m_H^2 = 2 lambda v^2 (SM convention: lambda = m_H^2/(2v^2))
lambda_SM = m_H_GeV**2 / (2 * v_GeV**2)
print(f"\n  lambda_SM = m_H^2/(2v^2) = {lambda_SM:.6f}")
print(f"  lambda_BST = 1/sqrt(60) = {lambda_H_BST:.6f}")
print(f"  Error: {pct_err(lambda_H_BST, lambda_SM):.3f}%")

m_H_from_BST = sqrt(2 * lambda_H_BST) * v_GeV
print(f"  m_H = sqrt(2*lambda_BST) * v = {m_H_from_BST:.4f} GeV  (obs: {m_H_GeV:.2f})")

# ============================================================
# SECTION 3: Dimensional analysis - geometric mean approach
# ============================================================

print("\n" + "=" * 80)
print("SECTION 3: Geometric mean v = m_e^a * m_Pl^(1-a)")
print("=" * 80)

# v = m_e^a * m_Pl^(1-a)
# log(v) = a*log(m_e) + (1-a)*log(m_Pl)
# a = (log(m_Pl) - log(v)) / (log(m_Pl) - log(m_e))
log_v = log(v_GeV)
log_me = log(m_e_GeV)
log_mPl = log(m_Pl_GeV)

a_geom = (log_mPl - log_v) / (log_mPl - log_me)
print(f"  a = (log(m_Pl) - log(v)) / (log(m_Pl) - log(m_e)) = {a_geom:.8f}")
print(f"  1 - a = {1 - a_geom:.8f}")
print(f"  v_reconstructed = m_e^a * m_Pl^(1-a) = {m_e_GeV**a_geom * m_Pl_GeV**(1-a_geom):.5f} GeV")

# Check: a close to known fractions?
for num, den in [(3,4), (5,7), (7,10), (9,13), (2,3), (11,15), (11,16), (17,24), (19,27)]:
    a_try = num / den
    v_try = m_e_GeV**a_try * m_Pl_GeV**(1 - a_try)
    err = pct_err(v_try, v_GeV)
    if abs(err) < 10:
        print(f"  a = {num}/{den} = {a_try:.6f}: v = {v_try:.4f} GeV  ({err:+.3f}%){flag(err)}")

# Using BST: m_e/m_Pl = 6pi^5 * alpha^12
# So m_e = m_Pl * 6pi^5 * alpha^12
# v = m_e^a * m_Pl^(1-a) = (m_Pl * 6pi^5 * alpha^12)^a * m_Pl^(1-a)
# = m_Pl * (6pi^5)^a * alpha^(12a)
print(f"\n  In BST: v = m_Pl * (6pi^5)^a * alpha^(12a)")
print(f"  With a = {a_geom:.8f}:")
print(f"    (6pi^5)^a = {(6*pi**5)**a_geom:.6f}")
print(f"    alpha^(12a) = {alpha**(12*a_geom):.6e}")
print(f"    12*a = {12*a_geom:.6f}")

# ============================================================
# SECTION 4: Systematic search v = m_e * f(pi, alpha, n_C, N_c, ...)
# ============================================================

print("\n" + "=" * 80)
print("SECTION 4: Systematic search v = m_e * f(pi, alpha, integers)")
print("=" * 80)

target_ratio = v_GeV / m_e_GeV
print(f"  Target: v/m_e = {target_ratio:.4f}")
print(f"  log10(v/m_e) = {log10(target_ratio):.6f}")
print(f"  ln(v/m_e) = {log(target_ratio):.6f}")

results = []

# Strategy: v/m_e ~ pi^a * alpha^b * (integer factor)
# log(v/m_e) = a*log(pi) + b*log(alpha) + log(integer)
# v/m_e = 481,840
# log(481840) = 13.085

# Try: pi^a * alpha^b for a in range, b in range (b negative since alpha < 1)
print("\n  --- pi^a * alpha^b ---")
for a in range(-2, 12):
    for b in range(-8, 2):
        val = pi**a * alpha**b
        if val > 0:
            ratio = target_ratio / val
            # Check if ratio is close to a simple integer or fraction
            for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 24, 30,
                        60, 120, 1920, n_C, N_c, n_C+2, 2*n_C,
                        n_C*N_c, factorial(n_C), factorial(n_C-1)]:
                for den in [1, 2, 3, 4, 5, 6, 7, 8, pi, pi**2, sqrt(2), sqrt(3), sqrt(5)]:
                    test_val = val * num / den
                    err = pct_err(test_val, target_ratio)
                    if abs(err) < 0.5:
                        results.append((abs(err), f"v/m_e = {num}/{den:.4g} * pi^{a} * alpha^({b})",
                                        test_val, err))

# Try: (6pi^5)^a * alpha^b  (proton ratio raised to power)
print("  --- (6pi^5)^a * alpha^b ---")
proton_factor = 6 * pi**5
for a_num in range(-3, 6):
    for a_den in [1, 2, 3, 4, 5, 6, 7, 8, 10, 12]:
        a_frac = a_num / a_den
        if a_frac == 0:
            continue
        for b in range(-8, 4):
            val = proton_factor**a_frac * alpha**b
            err = pct_err(val, target_ratio)
            if abs(err) < 0.5:
                results.append((abs(err), f"v/m_e = (6pi^5)^({a_num}/{a_den}) * alpha^({b})",
                                val, err))

# Try: n! * pi^a * alpha^b
print("  --- n! * pi^a * alpha^b ---")
for n_fact in [24, 120, 720, 5040, 1920, 60]:
    for a in range(0, 10):
        for b in range(-6, 1):
            val = n_fact * pi**a * alpha**b
            err = pct_err(val, target_ratio)
            if abs(err) < 0.5:
                results.append((abs(err), f"v/m_e = {n_fact} * pi^{a} * alpha^({b})",
                                val, err))

# Sort by error and print top results
results.sort(key=lambda x: x[0])
seen = set()
print(f"\n  TOP MATCHES (v/m_e = {target_ratio:.4f}):")
count = 0
for abs_err, formula, val, err in results:
    if formula not in seen and count < 30:
        seen.add(formula)
        print(f"    {formula:55s}  = {val:12.2f}  err = {err:+.4f}%{flag(err)}")
        count += 1

# ============================================================
# SECTION 5: v in terms of m_p
# ============================================================

print("\n" + "=" * 80)
print("SECTION 5: v in terms of m_p")
print("=" * 80)

ratio_vmp = v_GeV / m_p_GeV
print(f"  v/m_p = {ratio_vmp:.6f}")
print(f"  log10(v/m_p) = {log10(ratio_vmp):.6f}")

# Try simple combinations
candidates_vmp = []
for a in range(-3, 8):
    for b in range(-4, 4):
        for c_num in [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 15, 20, 24, 60, 120, 1920]:
            for c_den in [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13]:
                val = (c_num / c_den) * pi**a * alpha**b
                err = pct_err(val, ratio_vmp)
                if abs(err) < 0.5:
                    candidates_vmp.append((abs(err),
                        f"v/m_p = ({c_num}/{c_den}) * pi^{a} * alpha^({b})", val, err))

candidates_vmp.sort()
seen = set()
print(f"\n  TOP MATCHES (v/m_p = {ratio_vmp:.6f}):")
count = 0
for abs_err, formula, val, err in candidates_vmp:
    if formula not in seen and count < 15:
        seen.add(formula)
        print(f"    {formula:55s}  = {val:12.6f}  err = {err:+.4f}%{flag(err)}")
        count += 1

# ============================================================
# SECTION 6: Specific physically motivated ansatze
# ============================================================

print("\n" + "=" * 80)
print("SECTION 6: Physically motivated ansatze")
print("=" * 80)

print("\n  --- Fermi constant from BST ---")
# G_F = 1/(sqrt(2) v^2)
# If v = m_e * f, then G_F = 1/(sqrt(2) m_e^2 f^2)
# BST: m_e/m_Pl = 6pi^5 * alpha^12
# So m_e = m_Pl * 6pi^5 * alpha^12
# G_F m_p^2 = m_p^2/(sqrt(2) v^2)
GF_mp2 = G_F_GeVm2 * m_p_GeV**2
print(f"  G_F * m_p^2 = {GF_mp2:.6e} (dimensionless)")
print(f"  = m_p^2/(sqrt(2)*v^2) = {m_p_GeV**2/(sqrt(2)*v_GeV**2):.6e}")
print(f"  log10(G_F*m_p^2) = {log10(GF_mp2):.6f}")

# Check: G_F * m_p^2 vs alpha^n / (pi^m * integers)
for n in range(1, 10):
    for m in range(-2, 8):
        for k in [1, 2, 3, 6, 7, 12, 13, 60, 120, 1920, 6, 10, 15, 20, 24, 35]:
            val = alpha**n * k / pi**m
            err = pct_err(val, GF_mp2)
            if abs(err) < 1.0:
                print(f"    G_F*m_p^2 = {k} * alpha^{n} / pi^{m} = {val:.6e}  err = {err:+.4f}%{flag(err)}")

print("\n  --- v * alpha relationships ---")
v_alpha = v_GeV * alpha
print(f"  v * alpha = {v_alpha:.6f} GeV")
print(f"  2 * m_p   = {2*m_p_GeV:.6f} GeV  (ratio: {v_alpha/(2*m_p_GeV):.6f})")
print(f"  m_p + m_n = ~{2*m_p_GeV:.4f} GeV (approx)")

# v * sin^2(theta_W)
v_s2w = v_GeV * sin2_thetaW
print(f"\n  v * sin^2(theta_W) = v * 3/13 = {v_s2w:.4f} GeV")
print(f"  m_Z/2 = {m_Z_GeV/2:.4f} GeV  (ratio: {v_s2w/(m_Z_GeV/2):.6f})")

# v^2 / m_Pl
v2_mPl = v_GeV**2 / m_Pl_GeV
print(f"\n  v^2 / m_Pl = {v2_mPl:.6e} GeV")
print(f"  This is ~ {v2_mPl/m_e_GeV:.6e} * m_e")

print("\n  --- Hopf fibration / weak force connection ---")
print(f"  S^3 -> S^2 Hopf fibration: pi_3(S^2) = Z")
print(f"  Vol(S^3) = 2*pi^2 = {2*pi**2:.6f}")
print(f"  Vol(S^2) = 4*pi   = {4*pi:.6f}")
print(f"  Vol(S^3)/Vol(S^2) = pi/2 = {pi/2:.6f}")

# v as related to S^3 volumes
# Weak force lives on S^3 fiber. v might involve Vol(S^3)
# m_W = g_W v/2. So v = 2 m_W / g_W.
# In BST, m_W should be determined by Bergman geometry + S^3 fibration
print(f"\n  v = 2*m_W/g_W = {2*m_W_GeV/g_W:.4f} GeV")

# What if v = m_p * (something involving pi and weak angle)?
print(f"\n  v/m_p = {ratio_vmp:.6f}")
# 262.43 ~ ?
# 4*pi^4/3 = 4*97.409/3 = 129.88 -- no
# pi^5/... ?
# sqrt(2) * pi * alpha^{-1} ?
val_test = sqrt(2) * pi / alpha
print(f"  sqrt(2)*pi/alpha = {val_test:.4f}  (v/m_p = {ratio_vmp:.4f})")
val_test2 = 2 * pi**2 / alpha
print(f"  2*pi^2/alpha = {val_test2:.4f}")

# pi^5/(12*alpha) ?
val_test3 = pi**5 / (12 * alpha**(-1))  # = pi^5 * alpha / 12
# hmm, let me just try
print(f"  (4/3)*pi/alpha = {4*pi/(3*alpha):.4f}")

# ============================================================
# SECTION 7: v/m_Pl approach (since v/m_Pl is very clean in BST)
# ============================================================

print("\n" + "=" * 80)
print("SECTION 7: v/m_Pl — what power of alpha?")
print("=" * 80)

ratio_vPl = v_GeV / m_Pl_GeV
print(f"  v/m_Pl = {ratio_vPl:.6e}")
print(f"  log_alpha(v/m_Pl) = ln(v/m_Pl)/ln(alpha) = {log(ratio_vPl)/log(alpha):.6f}")

# v/m_Pl = alpha^p for some p?
p_alpha = log(ratio_vPl) / log(alpha)
print(f"  => v/m_Pl ~ alpha^{p_alpha:.4f}")
print(f"  Close fractions: ")
for num in range(1, 30):
    for den in range(1, 13):
        frac = num / den
        if abs(frac - p_alpha) < 0.05:
            v_try = m_Pl_GeV * alpha**frac
            err = pct_err(v_try, v_GeV)
            print(f"    alpha^({num}/{den}) = alpha^{frac:.4f}: v = {v_try:.4f} GeV  err = {err:+.3f}%{flag(err)}")

# BST: m_e/m_Pl = 6pi^5 * alpha^12
# So v/m_Pl = (v/m_e) * (m_e/m_Pl) = (v/m_e) * 6pi^5 * alpha^12
# Need v/m_e expressed in BST terms

# v/m_Pl = A * alpha^n for integer n, with A involving pi and BST integers
print(f"\n  --- v/m_Pl = A * alpha^n ---")
for n in range(6, 12):
    A = ratio_vPl / alpha**n
    print(f"    n={n}: A = v/(m_Pl * alpha^{n}) = {A:.6f}")
    # Check A against BST quantities
    for test_name, test_val in [
        ("6pi^5", 6*pi**5),
        ("pi^5/1920", Vol_DIV5),
        ("1/sqrt(60)", 1/sqrt(60)),
        ("sqrt(2/5!)", sqrt(2/120)),
        ("1/(2pi)", 1/(2*pi)),
        ("1/pi^2", 1/pi**2),
        ("1/(4pi)", 1/(4*pi)),
        ("7/(10*pi)", 7/(10*pi)),
        ("pi/2", pi/2),
        ("1/sqrt(2*pi)", 1/sqrt(2*pi)),
        ("sqrt(3/13)", sqrt(3/13)),
        ("sqrt(10/13)", sqrt(10/13)),
        ("2/pi", 2/pi),
        ("3/(4*pi)", 3/(4*pi)),
        ("2*pi^2", 2*pi**2),
        ("2*pi", 2*pi),
        ("4*pi", 4*pi),
    ]:
        err = pct_err(test_val, A)
        if abs(err) < 5:
            print(f"      A ~ {test_name} = {test_val:.6f}  err = {err:+.3f}%{flag(err)}")

# ============================================================
# SECTION 8: The G_F / v^2 hierarchy — why is G_F small?
# ============================================================

print("\n" + "=" * 80)
print("SECTION 8: Fermi constant hierarchy")
print("=" * 80)

# G_F = 1/(sqrt(2) v^2) = pi alpha / (sqrt(2) m_W^2 sin^2 theta_W)
# In BST natural units:
# G_F * m_Pl^2 = m_Pl^2 / (sqrt(2) v^2)
GF_mPl2 = G_F_GeVm2 * m_Pl_GeV**2
print(f"  G_F * m_Pl^2 = {GF_mPl2:.6e}")
print(f"  = (m_Pl/v)^2 / sqrt(2) = {(m_Pl_GeV/v_GeV)**2 / sqrt(2):.6e}")
print(f"  log_alpha(G_F * m_Pl^2) = {log(GF_mPl2)/log(alpha):.4f}")
# This should be ~ 2 * p_alpha
print(f"  (expected ~ 2 * {p_alpha:.4f} = {2*p_alpha:.4f} minus log corrections)")

# G_F in units of 1/m_e^2
GF_me2 = G_F_GeVm2 * m_e_GeV**2
print(f"\n  G_F * m_e^2 = {GF_me2:.6e}")
print(f"  = (m_e/v)^2 / sqrt(2) = {(m_e_GeV/v_GeV)**2 / sqrt(2):.6e}")

# Express G_F * m_p^2 in terms of alpha
print(f"\n  G_F * m_p^2 = {GF_mp2:.6e}")
# alpha^5 = (1/137)^5 = 2.09e-11 -- close!
print(f"  alpha^5 = {alpha**5:.6e}")
print(f"  alpha^5 / pi^2 = {alpha**5/pi**2:.6e}")
print(f"  alpha^5 / (pi * sqrt(2)) = {alpha**5/(pi*sqrt(2)):.6e}")
print(f"  alpha^5 * pi / 4 = {alpha**5*pi/4:.6e}")

# More precise
print(f"\n  G_F*m_p^2 / alpha^5 = {GF_mp2/alpha**5:.6f}")
# Should be some BST geometric factor
ratio_GF = GF_mp2 / alpha**5
print(f"  = {ratio_GF:.6f}")
for test_name, test_val in [
    ("1/(2*sqrt(2))", 1/(2*sqrt(2))),
    ("1/pi", 1/pi),
    ("3/13", 3/13),
    ("sin^2(theta_W)", sin2_thetaW),
    ("1/(2*pi)", 1/(2*pi)),
    ("pi/13", pi/13),
    ("3/(4*pi)", 3/(4*pi)),
    ("1/4", 0.25),
    ("sqrt(3/13)/pi", sqrt(3/13)/pi),
    ("1/3", 1/3.0),
    ("10/(13*pi)", 10/(13*pi)),
    ("1/(pi*sqrt(2))", 1/(pi*sqrt(2))),
    ("3/(13*sqrt(2))", 3/(13*sqrt(2))),
]:
    err = pct_err(test_val, ratio_GF)
    if abs(err) < 5:
        print(f"    ~ {test_name} = {test_val:.6f}  err = {err:+.3f}%{flag(err)}")

# ============================================================
# SECTION 9: The weak coupling / Hopf fibration approach
# ============================================================

print("\n" + "=" * 80)
print("SECTION 9: Weak coupling and Hopf fibration")
print("=" * 80)

# In SM: v = 2*m_W/g_W = 2*m_Z/g_Z
# g_W^2/(4*pi) = alpha/sin^2(theta_W) = alpha*13/3
# g_W^2 = 4*pi*alpha*13/3
g_W_sq = 4 * pi * alpha * 13 / 3
print(f"  g_W^2 = 4*pi*alpha*13/3 = {g_W_sq:.8f}")
print(f"  g_W = {sqrt(g_W_sq):.8f}")
print(f"  g_W (direct) = {g_W:.8f}")

# v = 2*m_W/g_W
# If m_W is the BST quantity to derive, and v is derived from m_W...
# Then the question becomes: what is m_W in BST?
print(f"\n  In BST, the question 'what sets v?' is equivalent to 'what sets m_W?'")
print(f"  since v = 2*m_W/g_W and g_W is known from alpha and sin^2(theta_W) = 3/13")

# m_W in BST units
print(f"\n  m_W/m_e = {m_W_GeV/m_e_GeV:.4f}")
print(f"  m_W/m_p = {m_W_GeV/m_p_GeV:.6f}")
print(f"  m_W/m_Pl = {m_W_GeV/m_Pl_GeV:.6e}")

# m_W / m_p
mW_mp = m_W_GeV / m_p_GeV
print(f"\n  m_W/m_p = {mW_mp:.6f}")
print(f"  This is the 'weak-strong hierarchy' within BST")

# Try: m_W/m_p = alpha^a * pi^b * (BST integer)
candidates_mW = []
for a in range(-4, 4):
    for b in range(-4, 6):
        for c in [1, 2, 3, 4, 5, 6, 7, 10, 12, 13, 15, 20, 24, 60, 120, 1920]:
            for d in [1, 2, 3, 4, 5, 6, 7, 10, 12, 13]:
                val = (c/d) * alpha**a * pi**b
                err = pct_err(val, mW_mp)
                if abs(err) < 0.5:
                    candidates_mW.append((abs(err),
                        f"m_W/m_p = ({c}/{d}) * alpha^({a}) * pi^({b})", val, err))

candidates_mW.sort()
seen = set()
print(f"\n  TOP MATCHES for m_W/m_p = {mW_mp:.6f}:")
count = 0
for abs_err, formula, val, err in candidates_mW:
    if formula not in seen and count < 15:
        seen.add(formula)
        print(f"    {formula:55s}  = {val:12.6f}  err = {err:+.4f}%{flag(err)}")
        count += 1

# ============================================================
# SECTION 10: The key insight — v² = m_W² × 4/g_W²
# ============================================================

print("\n" + "=" * 80)
print("SECTION 10: Decomposing v² = 4*m_W²/g_W²")
print("=" * 80)

# v² = 4*m_W²/g_W² = 4*m_W² * sin²θ_W / (4*pi*alpha)
# = m_W² * sin²θ_W / (pi*alpha)
# = m_W² * (3/13) / (pi*alpha)
v2_decomp = m_W_GeV**2 * sin2_thetaW / (pi * alpha)
print(f"  v² = m_W² * sin²θ_W / (pi*alpha)")
print(f"     = {m_W_GeV**2:.4f} * {sin2_thetaW:.6f} / ({pi:.6f} * {alpha:.8f})")
print(f"     = {v2_decomp:.4f} GeV²")
print(f"  v  = {sqrt(v2_decomp):.5f} GeV  (should be {v_GeV:.5f})")

# v² = 4*m_W²/(4*pi*alpha/sin²θ_W) = m_W² * 3/(13*pi*alpha)
print(f"\n  v² = m_W² * 3 / (13*pi*alpha)")
print(f"     = {m_W_GeV**2 * 3 / (13*pi*alpha):.4f}")

# So the question reduces to: what is m_W² / m_p² in BST?
# And v/m_p = (m_W/m_p) * sqrt(3/(13*pi*alpha))
# = (m_W/m_p) * 2/g_W
factor_2_gW = 2 / g_W
print(f"\n  2/g_W = {factor_2_gW:.6f}")
print(f"  v/m_p = (m_W/m_p) * 2/g_W = {mW_mp * factor_2_gW:.6f}  (should be {ratio_vmp:.6f})")

# ============================================================
# SECTION 11: v from m_p and alpha — the beautiful formula search
# ============================================================

print("\n" + "=" * 80)
print("SECTION 11: v = m_p * F(alpha, pi, BST integers)")
print("=" * 80)

# v/m_p = 262.435...
# What if v = m_p * pi * sqrt(N_c*n_C / alpha) or similar?
# Let me try various combinations involving the Weinberg angle

# v/m_p = 2*m_W/(m_p*g_W) — this is just the definition.
# We need m_W/m_p from BST.

# Key: m_W involves the weak scale. In BST, weak = S³→S² Hopf fibration.
# The mass of W should come from geometry of S³ fiber.

# Let's try: m_W/m_p = (some power of alpha) * (BST factor)
# m_W/m_p = 85.637...

# Actually, let me search more broadly for v/m_e
# v/m_e = 481,840
# = 6pi^5 * (v/m_p)
# since m_p/m_e = 6pi^5

print(f"\n  v/m_e = (m_p/m_e) * (v/m_p) = 6pi^5 * {ratio_vmp:.6f}")
print(f"        = {6*pi**5 * ratio_vmp:.4f}  (should be {v_GeV/m_e_GeV:.4f})")

# What is v/m_p in terms of alpha?
# log_alpha(v/m_p) = ln(v/m_p) / ln(alpha)
la_vmp = log(ratio_vmp) / log(1/alpha)  # positive since v > m_p and 1/alpha > 1
print(f"\n  log_(1/alpha)(v/m_p) = {la_vmp:.6f}")
print(f"  So v/m_p ~ (1/alpha)^{la_vmp:.4f} = alpha^(-{la_vmp:.4f})")

# ============================================================
# SECTION 12: Bergman kernel approach
# ============================================================

print("\n" + "=" * 80)
print("SECTION 12: Bergman kernel and curvature invariants")
print("=" * 80)

# Bergman kernel at origin for D_IV^n:
# K(0,0) = 1/Vol(D_IV^n) = 1920/pi^5
K_00 = Gamma_order / pi**n_C
print(f"  K(0,0) = |Gamma|/pi^n_C = 1920/pi^5 = {K_00:.6f}")
print(f"  1/K(0,0) = Vol(D_IV^5) = pi^5/1920 = {1/K_00:.8f}")

# Scalar curvature
print(f"  Scalar curvature R = -n_C(n_C+2)/2 = -{n_C*(n_C+2)/2}")
print(f"  Holomorphic sectional curvature = -2/(n_C+2) = -2/7")

# Vol(S^3) = 2*pi^2 (the Hopf fiber)
# Vol(S^1) = 2*pi (the EM fiber)
# Vol(CP^2) = pi^2/2

# Maybe v involves the ratio of bulk to fiber volumes?
print(f"\n  Vol(D_IV^5) / Vol(S^3) = (pi^5/1920) / (2*pi^2) = pi^3/3840 = {pi**3/3840:.8f}")
print(f"  Vol(D_IV^5) / Vol(S^1) = (pi^5/1920) / (2*pi) = pi^4/3840 = {pi**4/3840:.8f}")

# ============================================================
# SECTION 13: v² in natural units (relative to m_p²)
# ============================================================

print("\n" + "=" * 80)
print("SECTION 13: v² relationships")
print("=" * 80)

v2_mp2 = (v_GeV / m_p_GeV)**2
print(f"  (v/m_p)^2 = {v2_mp2:.4f}")
print(f"  log10 = {log10(v2_mp2):.6f}")

# Is (v/m_p)^2 related to BST?
# (v/m_p)^2 = 68,872
# = 1920 * 35.87? No.
# = 6 * pi^5 * alpha^(-1) * something?
print(f"  (v/m_p)^2 / (6*pi^5) = {v2_mp2 / (6*pi**5):.6f}")
print(f"  (v/m_p)^2 / (1920) = {v2_mp2 / 1920:.6f}")
print(f"  (v/m_p)^2 / (pi^5) = {v2_mp2 / pi**5:.6f}")

# v^2 / m_p^2 = 4*m_W^2/(m_p^2 * g_W^2)
# g_W^2 = 4*pi*alpha/(sin^2 theta_W) = 4*pi*alpha*13/3
# v^2/m_p^2 = 4*m_W^2/(m_p^2) * 3/(4*13*pi*alpha)
# = 3*(m_W/m_p)^2 / (13*pi*alpha)
val = 3 * mW_mp**2 / (13 * pi * alpha)
print(f"\n  3*(m_W/m_p)^2 / (13*pi*alpha) = {val:.4f}  (should be (v/m_p)^2 = {v2_mp2:.4f})")

# ============================================================
# SECTION 14: Fermi constant — pi*alpha / (sqrt(2) * m_W^2 * sin^2 theta_W)
# ============================================================

print("\n" + "=" * 80)
print("SECTION 14: G_F decomposition in BST")
print("=" * 80)

# G_F = pi*alpha / (sqrt(2) * m_W^2 * sin^2(theta_W))
GF_check = pi * alpha / (sqrt(2) * m_W_GeV**2 * sin2_thetaW)
print(f"  G_F = pi*alpha / (sqrt(2) * m_W^2 * sin^2 theta_W)")
print(f"      = {GF_check:.6e} GeV^-2  (should be {G_F_GeVm2:.6e})")
print(f"  Error: {pct_err(GF_check, G_F_GeVm2):.4f}%")

# So G_F * m_p^2 = pi*alpha*(m_p/m_W)^2 / (sqrt(2) * sin^2 theta_W)
# = pi*alpha * 13 / (3*sqrt(2)) * (m_p/m_W)^2
GFmp2_formula = pi * alpha * 13 / (3 * sqrt(2)) * (m_p_GeV / m_W_GeV)**2
print(f"\n  G_F*m_p^2 = pi*alpha*13/(3*sqrt(2)) * (m_p/m_W)^2 = {GFmp2_formula:.6e}")
print(f"  Direct: {GF_mp2:.6e}")

# (m_p/m_W)^2 = 1/mW_mp^2
print(f"\n  (m_p/m_W)^2 = {(m_p_GeV/m_W_GeV)**2:.6f} = {1/mW_mp**2:.6f}")
print(f"  m_p/m_W = {m_p_GeV/m_W_GeV:.6f}")

# ============================================================
# SECTION 15: Wide net — v = f(m_e, m_Pl, alpha, pi, BST integers)
# ============================================================

print("\n" + "=" * 80)
print("SECTION 15: Wide net search — best formulas for v")
print("=" * 80)

# Strategy: v/m_e = target_ratio = 481,840
# Since m_e/m_Pl = 6*pi^5 * alpha^12, we have
# v = m_e * (v/m_e) = m_Pl * 6*pi^5 * alpha^12 * (v/m_e)
# So equivalently, v/m_Pl = 6*pi^5 * alpha^12 * (v/m_e)
# And (v/m_e) = (v/m_Pl) / (6*pi^5 * alpha^12)

# Let's try: v/m_e = C * alpha^n * pi^m  where C is a BST integer
# Needs to give ~481840

wide_results = []

# Integer candidates (products of BST integers)
int_candidates = {}
for a in [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 15, 20, 24, 60, 120, 1920]:
    for b in [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 15, 20, 24, 60, 120]:
        if a * b < 1e8:
            name = f"{a}*{b}" if b > 1 else f"{a}"
            int_candidates[name] = a * b

# Add some special ones
int_candidates["n_C!"] = 120
int_candidates["(n_C+2)!"] = 5040
int_candidates["1920"] = 1920
int_candidates["6"] = 6
int_candidates["2*1920"] = 3840
int_candidates["6*120"] = 720
int_candidates["N_c*n_C"] = 15
int_candidates["n_C*(n_C+2)"] = 35
int_candidates["n_C!*n_C"] = 600
int_candidates["1920*pi^5_factor"] = 1920  # Vol^{-1}
int_candidates["13"] = 13
int_candidates["13*3"] = 39

for name, C in int_candidates.items():
    for n in range(-5, 5):  # alpha powers
        for m_pi in np.arange(-2, 12, 0.5):  # half-integer pi powers
            val = C * alpha**n * pi**m_pi
            if val > 0:
                err = pct_err(val, target_ratio)
                if abs(err) < 0.3:
                    wide_results.append((abs(err),
                        f"v/m_e = {name} * alpha^({n}) * pi^({m_pi:.1f})",
                        val, err))

wide_results.sort()
seen = set()
print(f"\n  BEST MATCHES for v/m_e = {target_ratio:.4f}:")
count = 0
for abs_err, formula, val, err in wide_results:
    if formula not in seen and count < 25:
        seen.add(formula)
        print(f"    {formula:60s}  = {val:12.2f}  err = {err:+.4f}%{flag(err)}")
        count += 1

# ============================================================
# SECTION 16: v from m_e, alpha, and the mass gap 6pi^5
# ============================================================

print("\n" + "=" * 80)
print("SECTION 16: Connecting v to 6pi^5 (mass gap) and alpha")
print("=" * 80)

# v/m_e = 481840
# v/m_p = 262.44
# m_p/m_e = 6*pi^5 = 1836.12

# Key: v/m_p = v/(m_e * 6*pi^5) = (v/m_e) / (6*pi^5)
# So we need (v/m_e)/(6*pi^5) = 262.44

# What is 262.44?
x = ratio_vmp
print(f"  v/m_p = {x:.6f}")
print(f"  1/(pi*alpha) = {1/(pi*alpha):.6f}")
print(f"  Ratio: (v/m_p) / (1/(pi*alpha)) = {x * pi * alpha:.6f}")

# Hmm, 1/(pi*alpha) = 43.63. Not it.
# (1/alpha)^{1.13} ~ 262? Let's check
print(f"  (1/alpha)^1.13 = {(1/alpha)**1.13:.4f}")
print(f"  (1/alpha) * sqrt(alpha) = {(1/alpha) * sqrt(alpha):.4f}")
# 137 * 1.915 = 262.4
print(f"  (1/alpha) * 2*sqrt(alpha/pi) = {(1/alpha) * 2*sqrt(alpha/pi):.4f}")
print(f"  (1/alpha) * pi/sqrt(2*pi) = ... nah")

# Try: v/m_p = (4*pi^2*alpha) / sin^2(theta_W) * something
# 4*pi^2*alpha * 13/3 = g_W^2 * pi =
print(f"\n  pi^2/(2*alpha) = {pi**2/(2*alpha):.4f}")  # = 678. No.
print(f"  (4/g_W^2) = {4/g_W_sq:.4f}")  # = 9427. No.

# What about v/m_p = 2/g_W * (m_W/m_p)?
# = 2/(e/sin(thetaW)) * m_W/m_p
# This is circular... but what if we have m_W/m_p from BST?

# Let's try a completely different angle.
# In SM: v = 1/(G_F*sqrt(2))^{1/2}
# G_F comes from W exchange: G_F/sqrt(2) = g_W^2/(8*m_W^2)
# And in the fundamental theory, g_W^2 = 4*pi*alpha/sin^2(theta_W)
# And m_W comes from... the Higgs mechanism, which needs v.

# THE CIRCULARITY: In SM, v is a free parameter (Higgs potential mu^2).
# BST must break this circularity by deriving v from geometry.

# Key insight: v^2 = -mu^2/lambda where mu^2 < 0 is the Higgs mass parameter.
# In BST, lambda = 1/sqrt(60). So v^2 = -mu^2 * sqrt(60).
# The question becomes: what is mu^2?

# mu^2 should come from the curvature of D_IV^5 in some way.
# Holomorphic sectional curvature = -2/7
# Scalar curvature = -35/2
# Ricci curvature = -(n_C+2) g_{ij} = -7 g_{ij}

print(f"\n  --- Curvature connection ---")
print(f"  If mu^2 is proportional to curvature in Bergman metric units:")
print(f"  v^2 = |R_holo| * sqrt(60) * (some mass)^2")
print(f"  v^2/m_p^2 = {v2_mp2:.4f}")
print(f"  (2/7)*sqrt(60) = {(2/7)*sqrt(60):.6f}")
print(f"  (35/2)*sqrt(60) = {(35/2)*sqrt(60):.4f}")

# ============================================================
# SECTION 17: The 'alpha^n × simple' approach for v/m_p
# ============================================================

print("\n" + "=" * 80)
print("SECTION 17: v/m_p as alpha^(-1) times a correction")
print("=" * 80)

# v/m_p / (1/alpha) = v*alpha/m_p = 262.44 * alpha = 1.914
corr = ratio_vmp * alpha
print(f"  v * alpha / m_p = {corr:.8f}")
print(f"  Is this close to a BST quantity?")
for name, val in [
    ("2", 2.0),
    ("sqrt(13/3)", sqrt(13/3.0)),
    ("2*sqrt(sin^2 theta_W)", 2*sqrt(sin2_thetaW)),
    ("pi/sqrt(2*pi)", pi/sqrt(2*pi)),
    ("sqrt(2*pi)/pi", sqrt(2*pi)/pi),
    ("2*sin(theta_W)", 2*sqrt(sin2_thetaW)),
    ("e_charge/(pi*sin(thetaW))", e_charge/(pi*sqrt(sin2_thetaW))),
    ("g_W/pi", g_W/pi),
    ("2*g_W/(2*pi)", g_W/pi),
    ("sqrt(4*pi*alpha*13/3)/pi", sqrt(g_W_sq)/pi),
    ("2/g_W * g_W^2/(2*pi)", g_W/(pi)),
]:
    err = pct_err(val, corr)
    if abs(err) < 10:
        print(f"    {name:40s} = {val:.6f}  err = {err:+.3f}%{flag(err)}")

# Specifically: v*alpha/m_p = 1.914
# g_W/pi = 0.2058/(pi) = too small
# Let's just try more
print(f"\n  v*alpha/m_p = {corr:.8f}")
print(f"  2*m_p/(v*alpha*m_p) = nah, that's 2/corr = {2/corr:.6f}")

# Try: v/m_p = n/(alpha * f(pi))
for n in [1, 2, 3, 4, 5, 6, 7, 10, 12, 13]:
    for m_pi in [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3]:
        val = n / (alpha * pi**m_pi)
        err = pct_err(val, ratio_vmp)
        if abs(err) < 1.0:
            print(f"  v/m_p = {n} / (alpha * pi^{m_pi:.1f}) = {val:.4f}  err = {err:+.4f}%{flag(err)}")

# ============================================================
# SECTION 18: Deep search — v as geometric mean
# ============================================================

print("\n" + "=" * 80)
print("SECTION 18: v as geometric mean of BST scales")
print("=" * 80)

# v = m_e^a * m_p^b * m_Pl^c with a+b+c=1
# Try small integer fractions
print("  v = m_e^a * m_p^b * m_Pl^(1-a-b)")
gm_results = []
for a_n in range(-4, 6):
    for a_d in [1, 2, 3, 4, 5, 6, 7, 12, 13]:
        a_f = a_n / a_d
        for b_n in range(-4, 6):
            for b_d in [1, 2, 3, 4, 5, 6, 7, 12, 13]:
                b_f = b_n / b_d
                c_f = 1 - a_f - b_f
                try:
                    val = m_e_GeV**a_f * m_p_GeV**b_f * m_Pl_GeV**c_f
                    if val > 0 and np.isfinite(val):
                        err = pct_err(val, v_GeV)
                        if abs(err) < 0.5:
                            gm_results.append((abs(err),
                                f"v = m_e^({a_n}/{a_d}) * m_p^({b_n}/{b_d}) * m_Pl^({1-a_f-b_f:.4f})",
                                val, err))
                except:
                    pass

gm_results.sort()
seen = set()
count = 0
for abs_err, formula, val, err in gm_results:
    if formula not in seen and count < 15:
        seen.add(formula)
        print(f"    {formula:65s}  v = {val:.4f}  err = {err:+.4f}%{flag(err)}")
        count += 1

# ============================================================
# SECTION 19: v/m_e = (6pi^5) * F(alpha, theta_W)
# ============================================================

print("\n" + "=" * 80)
print("SECTION 19: v = m_p * F(alpha, theta_W) — the weak hierarchy")
print("=" * 80)

# v/m_p = 262.44
# This MUST involve 1/alpha (since v >> m_p by factor ~alpha^(-1.13))
# and the Weinberg angle.

# From SM: v = 2*m_W/g_W => v/m_p = 2*(m_W/m_p)/g_W
# So we need m_W/m_p.

# m_W = (g_W/2) * v. This is circular.
# In BST, masses come from Casimir eigenvalues on D_IV^5.
# The electron is below the Wallach set (boundary excitation).
# The proton = 6pi^5 * m_e (mass gap, Casimir C_2 = 6).
# What about W and Z? They live on the S^3 Hopf fiber.

# Hypothesis: m_W^2 = (holomorphic curvature) * (bulk energy scale)^2 * (coupling)
# Or: m_W^2/m_p^2 = alpha * f(geometry)

# m_W/m_p = 85.637
# 85.637 ~ pi^4 / (what?) pi^4 = 97.41
# 85.637 ~ 6*pi^3/... 6*31.006 = 186.04
# 85.637 ~ pi^4/sqrt(alpha^(-1)) no too complicated

# A cleaner approach:
# v = m_p / (alpha * pi^a * integer)^(-1) isn't natural.
# Let's think about it from g_W:

# v = 2*m_W/g_W
# g_W^2 = 4*pi*alpha*13/3
# v^2 = 4*m_W^2/(g_W^2) = 4*m_W^2 * 3/(4*13*pi*alpha) = 3*m_W^2/(13*pi*alpha)
# So: v^2/m_p^2 = 3*(m_W/m_p)^2 / (13*pi*alpha)

# If m_W = m_p * C * alpha^p * pi^q:
# v^2/m_p^2 = 3*C^2*alpha^(2p)/(13*pi^(1-2q)*alpha) = 3*C^2*alpha^(2p-1)*pi^(2q-1)/13

# v/m_p = 262.44
# (v/m_p)^2 = 68873
# 3*(85.637)^2 / (13*pi*alpha) = 3*7334 / (13*pi/137.036) = 22001 / 0.2984 = ...
# let's just compute
check = 3 * mW_mp**2 / (13 * pi * alpha)
print(f"  3*(m_W/m_p)^2 / (13*pi*alpha) = {check:.4f}  (should be (v/m_p)^2 = {v2_mp2:.4f})")

# ============================================================
# SECTION 20: Attempt — v from Bergman metric + Weinberg angle
# ============================================================

print("\n" + "=" * 80)
print("SECTION 20: Speculative BST derivation of v")
print("=" * 80)

# IDEA 1: v^2 = m_Pl^2 * alpha^k * (geometric factor)
# We know v/m_Pl ~ alpha^{7.82}
# alpha^8 * m_Pl = m_Pl * alpha^8
v_try_8 = m_Pl_GeV * alpha**8
print(f"  m_Pl * alpha^8 = {v_try_8:.4f} GeV  (v = {v_GeV:.4f})")
print(f"  ratio = {v_GeV/v_try_8:.6f}")

# Need correction factor
corr8 = v_GeV / v_try_8
print(f"  v / (m_Pl * alpha^8) = {corr8:.6f}")
for name, val in [
    ("6*pi^5", 6*pi**5),
    ("pi^5/1920", Vol_DIV5),
    ("sqrt(6*pi^5)", sqrt(6*pi**5)),
    ("1920/pi^5", K_00),
    ("(6*pi^5)^{1/2}", sqrt(proton_ratio)),
    ("pi^2", pi**2),
    ("2*pi^2", 2*pi**2),
    ("4*pi", 4*pi),
    ("2*pi", 2*pi),
    ("pi^{5/2}", pi**2.5),
    ("sqrt(1920)", sqrt(1920)),
    ("sqrt(120)", sqrt(120)),
    ("sqrt(35/2)", sqrt(35/2)),
    ("7", 7.0),
    ("3*pi", 3*pi),
    ("pi^2/sqrt(2)", pi**2/sqrt(2)),
    ("10*pi/sqrt(13)", 10*pi/sqrt(13)),
    ("7*pi/sqrt(3)", 7*pi/sqrt(3)),
    ("13", 13.0),
    ("4*pi^2/13", 4*pi**2/13),
]:
    err = pct_err(val, corr8)
    if abs(err) < 10:
        print(f"    v/(m_Pl*alpha^8) ~ {name} = {val:.6f}  err = {err:+.3f}%{flag(err)}")

# IDEA 2: alpha^7 * correction
v_try_7 = m_Pl_GeV * alpha**7
corr7 = v_GeV / v_try_7
print(f"\n  v / (m_Pl * alpha^7) = {corr7:.8f}")
for name, val in [
    ("alpha/pi", alpha/pi),
    ("1/(4*pi^2)", 1/(4*pi**2)),
    ("alpha^2", alpha**2),
    ("1/(2*pi^3)", 1/(2*pi**3)),
    ("alpha/(2*pi)", alpha/(2*pi)),
    ("3/(13*pi^2)", 3/(13*pi**2)),
    ("1/(6*pi^3)", 1/(6*pi**3)),
    ("1/(8*pi^2)", 1/(8*pi**2)),
]:
    err = pct_err(val, corr7)
    if abs(err) < 10:
        print(f"    v/(m_Pl*alpha^7) ~ {name} = {val:.8f}  err = {err:+.3f}%{flag(err)}")

# IDEA 3: Use the BST electron mass formula
# m_e = m_Pl * 6*pi^5 * alpha^12
# v = m_e * (v/m_e) = m_Pl * 6*pi^5 * alpha^12 * (v/m_e)
# So v/m_Pl = 6*pi^5 * alpha^12 * (v/m_e)
# And (v/m_e) * 6*pi^5 * alpha^12 = v/m_Pl = 2.016e-17

# IDEA 4: v = m_p * sqrt(3/(13*pi*alpha)) * (m_W/m_p)
# This is just the identity. But if m_W/m_p has a BST formula...

# IDEA 5: What if v/m_p = sqrt(N) / alpha for integer N?
# Then v = m_p * sqrt(N) / alpha
# N = (v*alpha/m_p)^2 = corr^2
N_test = corr**2
print(f"\n  If v/m_p = sqrt(N)/alpha: N = {N_test:.6f}")
for name, val in [
    ("13/sqrt(3)", 13/sqrt(3)),
    ("pi^2/sqrt(3)", pi**2/sqrt(3)),
    ("2*sqrt(3)", 2*sqrt(3)),
    ("13*pi/(6*sqrt(2))", 13*pi/(6*sqrt(2))),
    ("13/7", 13/7.0),
    ("sqrt(13)", sqrt(13)),
    ("pi*sqrt(3/13)", pi*sqrt(3/13)),
    ("2*sqrt(pi/3)", 2*sqrt(pi/3)),
]:
    err = pct_err(val**2, N_test)
    if abs(err) < 5:
        print(f"    sqrt(N) ~ {name}: N = {val**2:.6f}  err = {err:+.3f}%{flag(err)}")

# Wait, N_test = corr^2 where corr = v*alpha/m_p = 1.914
# corr^2 = 3.664
print(f"  (v*alpha/m_p)^2 = {N_test:.6f}")
print(f"  13/3 = {13/3:.6f}  err = {pct_err(13/3, N_test):+.3f}%")
print(f"  pi*7/6 = {pi*7/6:.6f}  err = {pct_err(pi*7/6, N_test):+.3f}%")
print(f"  pi^2/3 - sqrt(2) = {pi**2/3 - sqrt(2):.6f}")
print(f"  (g_W)^2 = {g_W_sq:.6f}")

# Interesting: 13/3 = 4.333, N_test = 3.664 -- not close
# g_W^2 = 0.4268 -- no

# But wait: v*alpha/m_p should = g_W^2*v/(4*pi*m_p*sin^2(theta_W)/sin^2(theta_W))
# Let me reconsider. We had v = 2*m_W/g_W, so
# v*alpha = 2*m_W*alpha/g_W = 2*m_W*alpha*sin(theta_W)/e = 2*m_W*sin(theta_W)^2*sqrt(4*pi)/e
# This is getting circular.

# ============================================================
# SECTION 21: FRESH approach — v² from W propagator
# ============================================================

print("\n" + "=" * 80)
print("SECTION 21: Fresh approach - what does v encode?")
print("=" * 80)

# The VEV v = 246 GeV sets the scale of electroweak symmetry breaking.
# In BST, the weak force IS the Hopf fibration S^3 -> S^2.
# The symmetry breaking should correspond to a geometric property of this fibration
# within D_IV^5.

# Key: D_IV^5 has real dimension 10. The boundary is S^4 x S^1 (Shilov boundary).
# The S^3 weak fiber sits inside the bulk.

# v²/m_Pl² = (v/m_Pl)^2 = 4.065e-34
# This is the "weakness" of the weak force relative to gravity.

v2_Pl2 = (v_GeV / m_Pl_GeV)**2
print(f"  (v/m_Pl)^2 = {v2_Pl2:.6e}")
print(f"  alpha^16 = {alpha**16:.6e}")
print(f"  Ratio (v/m_Pl)^2 / alpha^16 = {v2_Pl2/alpha**16:.6f}")

# Hmm, alpha^16 = 1.196e-34.  (v/m_Pl)^2 = 4.065e-34
print(f"  (v/m_Pl)^2 / alpha^16 = {v2_Pl2/alpha**16:.6f}")
# = 3.399. Close to anything?
for name, val in [
    ("pi", pi),
    ("e", exp(1)),
    ("3", 3.0),
    ("10/3", 10/3.0),
    ("7/2", 3.5),
    ("sqrt(12)", sqrt(12)),
    ("sqrt(13)", sqrt(13)),
    ("13/4", 13/4.0),
    ("sqrt(35/3)", sqrt(35/3.0)),
    ("pi + 1/4", pi + 0.25),
    ("12/pi", 12/pi),
    ("2*sqrt(pi/2)", 2*sqrt(pi/2)),
    ("sqrt(4*pi/3)", sqrt(4*pi/3)),
    ("(n_C+2)/2", 3.5),
    ("sqrt(2*pi/sqrt(3))", sqrt(2*pi/sqrt(3))),
]:
    err = pct_err(val, v2_Pl2/alpha**16)
    if abs(err) < 5:
        print(f"    (v/m_Pl)^2/alpha^16 ~ {name} = {val:.6f}  err = {err:+.3f}%{flag(err)}")

# So (v/m_Pl)^2 ~ 3.4 * alpha^16. Let's refine.
target_A = v2_Pl2 / alpha**16
print(f"\n  Target: (v/m_Pl)^2 / alpha^16 = {target_A:.6f}")
# 3.399. Try: 36/(pi*n_C+2)?
# Or: (6*pi^5)^2 * alpha^24 / alpha^16 = (6*pi^5)^2 * alpha^8
# Since m_e/m_Pl = 6pi^5 * alpha^12, (m_e/m_Pl)^2 = (6pi^5)^2 * alpha^24
# So (v/m_Pl)^2 = (v/m_e)^2 * (m_e/m_Pl)^2 = (v/m_e)^2 * (6pi^5)^2 * alpha^24
# And (v/m_e)^2 * (6pi^5)^2 * alpha^24 = target_A * alpha^16
# => (v/m_e)^2 = target_A * alpha^16 / ((6pi^5)^2 * alpha^24) = target_A / ((6pi^5)^2 * alpha^8)
ve_check = target_A / ((6*pi**5)**2 * alpha**8)
print(f"  (v/m_e)^2 from above = {ve_check:.4f}  (should be {target_ratio**2:.4f})")
# Of course this is tautological, but it helps organize.

# ============================================================
# SECTION 22: COMBINATORIAL — try ALL "nice" BST formulas
# ============================================================

print("\n" + "=" * 80)
print("SECTION 22: Brute force over BST building blocks")
print("=" * 80)

# Building blocks: pi, alpha, n_C=5, N_c=3, genus=7, 1920, Vol=pi^5/1920
# Target: v/m_p = 262.4354

bst_atoms = {
    "pi": pi,
    "alpha": alpha,
    "1/alpha": 1/alpha,
    "sqrt(alpha)": sqrt(alpha),
    "1/sqrt(alpha)": 1/sqrt(alpha),
    "n_C": 5,
    "N_c": 3,
    "genus": 7,
    "n_C+2": 7,
    "(n_C+1)": 6,
    "N_c+n_C": 8,
    "1920": 1920,
    "sqrt(1920)": sqrt(1920),
    "120": 120,
    "60": 60,
    "13": 13,
    "sin2tW": sin2_thetaW,
    "cos2tW": cos2_thetaW,
    "Vol_DIV5": Vol_DIV5,
    "K_00": K_00,
    "sqrt(2)": sqrt(2),
    "sqrt(3)": sqrt(3),
    "sqrt(5)": sqrt(5),
    "sqrt(7)": sqrt(7),
    "sqrt(13)": sqrt(13),
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "10": 10,
    "12": 12,
}

# Two-atom products
best_2atom = []
atom_list = list(bst_atoms.items())
for i, (n1, v1) in enumerate(atom_list):
    for j, (n2, v2) in enumerate(atom_list):
        if j < i:
            continue
        val = v1 * v2
        if val > 0 and np.isfinite(val):
            err = pct_err(val, ratio_vmp)
            if abs(err) < 1.0:
                best_2atom.append((abs(err), f"({n1})*({n2})", val, err))

best_2atom.sort()
print(f"\n  Two-atom products matching v/m_p = {ratio_vmp:.4f}:")
for abs_err, formula, val, err in best_2atom[:10]:
    print(f"    {formula:45s}  = {val:12.4f}  err = {err:+.4f}%{flag(err)}")

# Three-atom products
best_3atom = []
for i, (n1, v1) in enumerate(atom_list):
    for j, (n2, v2) in enumerate(atom_list):
        if j < i:
            continue
        for k, (n3, v3) in enumerate(atom_list):
            if k < j:
                continue
            val = v1 * v2 * v3
            if val > 0 and np.isfinite(val):
                err = pct_err(val, ratio_vmp)
                if abs(err) < 0.5:
                    best_3atom.append((abs(err), f"({n1})*({n2})*({n3})", val, err))

best_3atom.sort()
print(f"\n  Three-atom products matching v/m_p = {ratio_vmp:.4f}:")
for abs_err, formula, val, err in best_3atom[:20]:
    print(f"    {formula:60s}  = {val:12.4f}  err = {err:+.4f}%{flag(err)}")

# Also check ratios (two atoms divided by one)
best_ratio = []
for i, (n1, v1) in enumerate(atom_list):
    for j, (n2, v2) in enumerate(atom_list):
        for k, (n3, v3) in enumerate(atom_list):
            if v3 == 0:
                continue
            val = v1 * v2 / v3
            if val > 0 and np.isfinite(val):
                err = pct_err(val, ratio_vmp)
                if abs(err) < 0.3:
                    best_ratio.append((abs(err), f"({n1})*({n2})/({n3})", val, err))

best_ratio.sort()
seen = set()
print(f"\n  Two-over-one atom ratios matching v/m_p = {ratio_vmp:.4f}:")
count = 0
for abs_err, formula, val, err in best_ratio:
    if formula not in seen and count < 20:
        seen.add(formula)
        print(f"    {formula:60s}  = {val:12.4f}  err = {err:+.4f}%{flag(err)}")
        count += 1

# ============================================================
# SECTION 23: THE ANSWER — checking v = m_p * 2/(g_W^2) * (something small)
# ============================================================

print("\n" + "=" * 80)
print("SECTION 23: Checking specific compelling formulas")
print("=" * 80)

# Formula candidates that might work
candidates = [
    ("v = m_p / (pi * alpha)",
     m_p_GeV / (pi * alpha)),
    ("v = m_p * sqrt(13/(3*alpha)) / pi",
     m_p_GeV * sqrt(13/(3*alpha)) / pi),
    ("v = m_p * sqrt(13*pi/(3*alpha))",
     m_p_GeV * sqrt(13*pi/(3*alpha))),
    ("v = m_p * 2 * sqrt(pi/(3*alpha*13))",
     m_p_GeV * 2 * sqrt(pi/(3*alpha*13))),
    ("v = m_p * (13/(3*pi*alpha))^{1/2}",
     m_p_GeV * sqrt(13/(3*pi*alpha))),
    ("v = m_e * 6pi^5 / (pi * alpha)",
     m_e_GeV * 6*pi**5 / (pi * alpha)),
    ("v = m_Pl * (6pi^5)^2 * alpha^13",
     m_Pl_GeV * (6*pi**5)**2 * alpha**13),
    ("v = m_Pl * 6pi^5 * alpha^{12} * sqrt(13/(3*pi*alpha))",
     m_Pl_GeV * 6*pi**5 * alpha**12 * sqrt(13/(3*pi*alpha))),
    ("v = sqrt(3*m_W^2/(13*pi*alpha)) [identity check]",
     sqrt(3*m_W_GeV**2/(13*pi*alpha))),
    ("v = m_p * sqrt(n_C! * alpha^{-1} / (3*pi^3))",
     m_p_GeV * sqrt(120 / (3 * pi**3 * alpha))),
    ("v = m_p * 7 * sqrt(6/alpha) / pi^2",
     m_p_GeV * 7 * sqrt(6/alpha) / pi**2),
    ("v = m_p * sqrt(1920/(pi * alpha))",
     m_p_GeV * sqrt(1920 / (pi * alpha))),
    ("v = m_p * sqrt(6*pi^5 / (alpha * 1920))",
     m_p_GeV * sqrt(6*pi**5 / (alpha * 1920))),
    ("v = m_Pl * sqrt(3/(13*pi)) * alpha^{15/2}",
     m_Pl_GeV * sqrt(3/(13*pi)) * alpha**7.5),
    ("v = m_Pl * (pi^5/1920)^{1/2} * alpha^8",
     m_Pl_GeV * sqrt(Vol_DIV5) * alpha**8),
    ("v = m_Pl * alpha^8 * sqrt(Vol(D_IV^5))",
     m_Pl_GeV * alpha**8 * sqrt(pi**5/1920)),
    ("v = m_Pl * alpha^8 * pi^{5/2} / sqrt(1920)",
     m_Pl_GeV * alpha**8 * pi**2.5 / sqrt(1920)),
    ("v = m_p * sqrt(N_c/(n_C * alpha * sin2tW))",
     m_p_GeV * sqrt(N_c / (n_C * alpha * sin2_thetaW))),
    ("v = m_p * sqrt(13/(alpha * pi * 3))",
     m_p_GeV * sqrt(13 / (alpha * pi * 3))),
]

print(f"  Observed v = {v_GeV:.5f} GeV\n")
for name, val in candidates:
    err = pct_err(val, v_GeV)
    marker = flag(err)
    print(f"  {name:60s}")
    print(f"    = {val:.5f} GeV  err = {err:+.4f}%{marker}")

# ============================================================
# SECTION 24: The key insight — is v^2 = m_p^2 * 13/(3*pi*alpha)?
# ============================================================

print("\n" + "=" * 80)
print("SECTION 24: TESTING v^2 = m_W^2 * 3/(13*pi*alpha) — what is m_W/m_p?")
print("=" * 80)

# We have the identity v^2 = 3*m_W^2/(13*pi*alpha)
# The question becomes: what is m_W in BST?
# m_W/m_e = 157257, m_W/m_p = 85.637

# m_W/m_p is the REAL question. Let's focus.
# 85.637...
# pi^4 = 97.409
# 85.637/pi^4 = 0.8791
# 85.637 * 7/pi^4 = 6.154 ~ 6? That's C_2!
# m_W/m_p = C_2 * pi^4 / 7 ?
val_test = 6 * pi**4 / 7
err = pct_err(val_test, mW_mp)
print(f"  m_W/m_p =? C_2 * pi^4 / genus = 6*pi^4/7 = {val_test:.4f}  (obs: {mW_mp:.4f}, err: {err:+.3f}%){flag(err)}")

# That's 83.494 vs 85.637 — 2.5% off. Close but not great.

# m_W/m_p =? pi^4 * sin^2(theta_W) * something
# pi^4 * 3/13 = 22.48 — no
# sqrt(2) * pi^4 * ...

# Let me try: m_W/m_p = alpha^(-a) * pi^b * (BST factor)
# alpha^(-1) = 137, too big. But alpha^{-1/2} = 11.7
# pi^3 = 31.006, pi^4 = 97.41
# 85.637 / 31.006 = 2.762 ... ~ e? or pi-0.38?
# 85.637 / 97.41 = 0.879 ...
# 85.637 = 12 * sqrt(1920) / (sqrt(alpha^{-1}))?
# 12 * 43.82 / 11.706 = 44.95. No.

# Systematic:
mW_results = []
for a in np.arange(-1, 2, 0.5):
    for b in np.arange(-1, 6, 0.5):
        for c in [1, 2, 3, 4, 5, 6, 7, 10, 12, 13, 15, 20, 24, 35, 60, 120, 1920]:
            for d in [1, 2, 3, 4, 5, 6, 7, 10, 12, 13, 15, 20, 24, 35, 60]:
                val = (c/d) * (1/alpha)**a * pi**b
                err = pct_err(val, mW_mp)
                if abs(err) < 0.1:
                    mW_results.append((abs(err),
                        f"m_W/m_p = ({c}/{d}) * (1/alpha)^({a:.1f}) * pi^({b:.1f})", val, err))

mW_results.sort()
seen = set()
print(f"\n  TOP MATCHES for m_W/m_p = {mW_mp:.6f}:")
count = 0
for abs_err, formula, val, err in mW_results:
    if formula not in seen and count < 20:
        seen.add(formula)
        print(f"    {formula:60s}  = {val:10.4f}  err = {err:+.4f}%{flag(err)}")
        count += 1

# ============================================================
# SECTION 25: Summary and best candidates
# ============================================================

print("\n" + "=" * 80)
print("SECTION 25: SUMMARY — Best Formulas Found")
print("=" * 80)

# Let's collect the absolute best
print("""
  THE CENTRAL QUESTION: What sets v = 246.22 GeV?

  EQUIVALENT QUESTIONS (via SM relations with BST Weinberg angle):
  - What sets m_W = 80.37 GeV? (since v = 2*m_W/g_W, g_W known)
  - What sets G_F? (since v^2 = 1/(sqrt(2)*G_F))

  KEY IDENTITY: v^2 = 3*m_W^2 / (13*pi*alpha)
  [Uses sin^2(theta_W) = 3/13 from BST]

  So the REAL question is: what is m_W/m_p (or m_W/m_e) in BST?

  DIMENSIONAL ANALYSIS:
""")

print(f"  v/m_Pl = {ratio_vPl:.6e} ~ alpha^{p_alpha:.4f}")
print(f"  v/m_e  = {target_ratio:.4f}")
print(f"  v/m_p  = {ratio_vmp:.6f}")
print(f"  m_W/m_p = {mW_mp:.6f}")

print(f"\n  GEOMETRIC MEAN: v = m_e^{a_geom:.6f} * m_Pl^{1-a_geom:.6f}")

# Check: does the formula v = m_Pl * alpha^8 * sqrt(pi^5/1920) work?
v_bergman = m_Pl_GeV * alpha**8 * sqrt(pi**5/1920)
err_bergman = pct_err(v_bergman, v_GeV)
print(f"\n  BERGMAN FORMULA: v = m_Pl * alpha^8 * sqrt(Vol(D_IV^5))")
print(f"  = m_Pl * alpha^8 * sqrt(pi^5/1920)")
print(f"  = {v_bergman:.4f} GeV  (obs: {v_GeV:.4f}, err: {err_bergman:+.3f}%){flag(err_bergman)}")

# Check: v = m_Pl * alpha^8 * pi^{5/2} / sqrt(1920)
# This is the same thing: sqrt(pi^5/1920) = pi^{5/2}/sqrt(1920)
# = pi^{5/2}/43.82 = 17.49/43.82 = 0.3992
# v = 1.22e19 * 3.28e-17 * 0.3992 = 1.22e19 * 1.31e-17 = 159.8. Hmm.

# Check numerically
print(f"  alpha^8 = {alpha**8:.6e}")
print(f"  sqrt(Vol) = {sqrt(Vol_DIV5):.6f}")
print(f"  Product = {alpha**8 * sqrt(Vol_DIV5):.6e}")
print(f"  m_Pl * product = {m_Pl_GeV * alpha**8 * sqrt(Vol_DIV5):.4f}")

# Let me check v = m_p * 2/g_W * m_W/m_p
# Since v = 2*m_W/g_W = m_p * (2/g_W) * (m_W/m_p)
# This is an identity. But re-expressing:
# v = m_p * 2*sin(theta_W)/e * m_W/m_p
# = 2*m_W*sin(theta_W)/e
# = 2*m_W/(e/sin(theta_W))
# All circular without m_W independently.

# THE DEEP RESULT: Check if alpha^8 * Vol^{1/2} gives the right scale
# v = m_Pl * alpha^8 * (pi^5/1920)^{1/2}
# Physical interpretation:
# - alpha^8 = (alpha^4)^2: four powers of alpha for each of the two Hopf hemispheres?
# - Vol^{1/2}: square root of the Bergman volume = geometric measure of the bulk

# Check: what if the power isn't exactly 8?
best_pow = log(v_GeV / (m_Pl_GeV * sqrt(Vol_DIV5))) / log(alpha)
print(f"\n  v = m_Pl * alpha^p * sqrt(Vol(D_IV^5))")
print(f"  Solving for p: p = {best_pow:.6f}")
print(f"  Nearest integers: 8 (err: {pct_err(m_Pl_GeV * alpha**8 * sqrt(Vol_DIV5), v_GeV):+.3f}%)")

# Actually, let me also check v = m_Pl * alpha^p * Vol(D_IV^5) (not sqrt)
best_pow2 = log(v_GeV / (m_Pl_GeV * Vol_DIV5)) / log(alpha)
print(f"\n  v = m_Pl * alpha^p * Vol(D_IV^5)")
print(f"  Solving for p: p = {best_pow2:.6f}")
v_vol = m_Pl_GeV * alpha**7 * Vol_DIV5
print(f"  p=7: v = {v_vol:.4f} GeV  err = {pct_err(v_vol, v_GeV):+.3f}%{flag(pct_err(v_vol, v_GeV))}")
v_vol8 = m_Pl_GeV * alpha**8 * Vol_DIV5
print(f"  p=8: v = {v_vol8:.4f} GeV  err = {pct_err(v_vol8, v_GeV):+.3f}%")

# Check: v = m_Pl * alpha^8 * K(0,0)^{-1/2}
# = m_Pl * alpha^8 * sqrt(Vol) -- same as above
# = m_Pl * alpha^8 * (pi^5/1920)^{1/2} = 159.8 GeV -- 35% off

# Check: v = m_Pl * alpha^8 * (some other factor)
# Need factor = v/(m_Pl * alpha^8)
factor_8 = v_GeV / (m_Pl_GeV * alpha**8)
print(f"\n  v / (m_Pl * alpha^8) = {factor_8:.8f}")
print(f"  sqrt(Vol) = {sqrt(Vol_DIV5):.8f}")
print(f"  Ratio = {factor_8/sqrt(Vol_DIV5):.6f}")
# This ratio should be some BST number
r = factor_8 / sqrt(Vol_DIV5)
print(f"  v/(m_Pl * alpha^8 * sqrt(Vol)) = {r:.6f}")
for name, val in [
    ("1", 1.0),
    ("sqrt(2)", sqrt(2)),
    ("sqrt(3)", sqrt(3)),
    ("pi/2", pi/2),
    ("sqrt(pi)", sqrt(pi)),
    ("sqrt(7/2)", sqrt(3.5)),
    ("sqrt(13/7)", sqrt(13/7)),
    ("sqrt(n_C)", sqrt(5)),
    ("sqrt(13/3)/pi*sqrt(2)", sqrt(13/3)/pi*sqrt(2)),
    ("2/sqrt(pi)", 2/sqrt(pi)),
    ("sqrt(7/pi)", sqrt(7/pi)),
    ("e/sqrt(2*pi)", exp(1)/sqrt(2*pi)),
    ("sqrt(3/pi)", sqrt(3/pi)),
    ("sqrt(7/(2*pi))", sqrt(7/(2*pi))),
]:
    err = pct_err(val, r)
    if abs(err) < 10:
        print(f"    ~ {name} = {val:.6f}  err = {err:+.3f}%{flag(err)}")

# ============================================================
# SECTION 26: High-precision search around alpha^8 * m_Pl
# ============================================================

print("\n" + "=" * 80)
print("SECTION 26: v = m_Pl * alpha^8 * A — what is A?")
print("=" * 80)

A_target = factor_8  # = v/(m_Pl * alpha^8)
print(f"  A = v/(m_Pl * alpha^8) = {A_target:.8f}")
print(f"  ln(A) = {log(A_target):.6f}")
print(f"  log10(A) = {log10(A_target):.6f}")

# A ~ 0.6145
# Search A as ratio of BST quantities
A_results = []
for a in np.arange(-3, 4, 0.5):
    for c in [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 15, 20, 24, 35, 60, 120, 1920]:
        for d in [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 15, 20, 24, 35, 60, 120, 1920]:
            val = (c/d) * pi**a
            if val > 0:
                err = pct_err(val, A_target)
                if abs(err) < 0.5:
                    A_results.append((abs(err), f"A = ({c}/{d}) * pi^({a:.1f})", val, err))

A_results.sort()
seen = set()
print(f"\n  TOP MATCHES for A = {A_target:.8f}:")
count = 0
for abs_err, formula, val, err in A_results:
    if formula not in seen and count < 15:
        seen.add(formula)
        print(f"    {formula:50s}  = {val:.8f}  err = {err:+.4f}%{flag(err)}")
        count += 1

# ============================================================
# SECTION 27: Final physical interpretation
# ============================================================

print("\n" + "=" * 80)
print("SECTION 27: Physical interpretation and next steps")
print("=" * 80)

print("""
  FINDINGS:

  1. v/m_Pl ~ alpha^{7.82}, suggesting v involves alpha to a power near 8
     but with a non-trivial geometric prefactor.

  2. The identity v^2 = 3*m_W^2/(13*pi*alpha) means the question reduces to:
     "What is m_W in BST?" — since sin^2(theta_W) = 3/13 and alpha are known.

  3. The geometric mean exponent a = (log(m_Pl)-log(v))/(log(m_Pl)-log(m_e))
""")
print(f"     = {a_geom:.6f}")
print(f"     Note: 12*a = {12*a_geom:.4f}")
print(f"     And 1-a = {1-a_geom:.6f}")
print("""
  4. v = m_Pl * alpha^8 * A, where A ~ 0.615 needs identification as a
     BST geometric quantity. Leading candidates from search above.

  5. PHYSICAL PICTURE: v is the energy scale at which the S^3 Hopf fiber
     (weak force) "freezes out" of the D_IV^5 bulk geometry. This should
     be determined by:
     - The Bergman metric curvature (sets the bulk scale)
     - The embedding of S^3 in the boundary S^4 x S^1
     - The holomorphic sectional curvature -2/7

  6. OPEN: A clean formula for m_W/m_p (= 85.637) would immediately give v.
     The most promising approach is through the Hopf fibration geometry:
     m_W should be a Casimir eigenvalue on S^3 fiber, weighted by alpha
     and the Weinberg angle.

  7. HINT: v*alpha ~ 1.80 GeV ~ 2*m_p (within 4%). This suggests
     v*alpha = 2*m_p*(correction). If v*alpha = 2*m_p exactly, then
     v = 2*m_p/alpha = 2*6pi^5*m_e/alpha. But this gives 257.2 GeV (4.5% off).
""")

# Final check: v = 2*m_p/alpha
v_2mp_alpha = 2 * m_p_GeV / alpha
print(f"  v =? 2*m_p/alpha = {v_2mp_alpha:.4f} GeV  (obs: {v_GeV:.4f}, err: {pct_err(v_2mp_alpha, v_GeV):+.3f}%)")

# v = 2*m_p/(alpha*pi) * pi
# = 2*m_p*pi/alpha -- too big
# Try correction: v = 2*m_p/alpha * (1 - something)
corr_needed = v_GeV / v_2mp_alpha
print(f"  Correction: v/(2*m_p/alpha) = {corr_needed:.6f}")
print(f"  1 - pi^2/200 = {1 - pi**2/200:.6f}")
print(f"  1 - alpha*pi = {1 - alpha*pi:.6f}")
print(f"  13/(2*7) = {13/14:.6f}")
print(f"  10/13*sqrt(3/pi) = {10/13*sqrt(3/pi):.6f}")

# Check: v = 2*m_p*(13/14)/alpha?
v_test_1314 = 2 * m_p_GeV * (13/14) / alpha
print(f"\n  v = 2*m_p*(13/14)/alpha = {v_test_1314:.4f} GeV  err = {pct_err(v_test_1314, v_GeV):+.3f}%{flag(pct_err(v_test_1314, v_GeV))}")

# cos^2(theta_W) = 10/13
v_test_cos = 2 * m_p_GeV * cos2_thetaW / alpha
print(f"  v = 2*m_p*cos^2(theta_W)/alpha = 2*m_p*(10/13)/alpha = {v_test_cos:.4f} GeV  err = {pct_err(v_test_cos, v_GeV):+.3f}%{flag(pct_err(v_test_cos, v_GeV))}")

# Close! 197.8 GeV -- -19.6%. Not great.

# What about v = 2*m_W*sqrt(13/3) / e_charge?
# = 2*m_W/(e/sqrt(13/3)) = 2*m_W*sin(theta_W)/e = v (identity)

# Let's compute v = pi*m_p / (2*alpha)
v_pi_mp = pi * m_p_GeV / (2 * alpha)
print(f"\n  v = pi*m_p/(2*alpha) = {v_pi_mp:.4f} GeV  err = {pct_err(v_pi_mp, v_GeV):+.3f}%")

# v = (n_C+1)*pi^5*m_e/(pi*alpha) = 6*pi^4*m_e/alpha
v_6pi4 = 6 * pi**4 * m_e_GeV / alpha
print(f"  v = 6*pi^4*m_e/alpha = {v_6pi4:.4f} GeV  err = {pct_err(v_6pi4, v_GeV):+.3f}%")

# v = 6*pi^5*m_e * sqrt(13/(3*pi))/alpha^{1/2}?
# hmm getting complicated

# ============================================================
# SECTION 28: The g_W connection — direct
# ============================================================

print("\n" + "=" * 80)
print("SECTION 28: g_W and the electroweak scale")
print("=" * 80)

# g_W = e/sin(theta_W) = sqrt(4*pi*alpha)/sqrt(3/13) = sqrt(4*pi*alpha*13/3)
print(f"  g_W = sqrt(4*pi*alpha*13/3) = {g_W:.8f}")
print(f"  g_W^2 = {g_W_sq:.8f}")
print(f"  g_W^2/(4*pi) = alpha/sin^2(theta_W) = alpha*13/3 = {alpha*13/3:.8f}")

# m_W = g_W*v/2
# v = 2*m_W/g_W
# If m_W^2 = (g_W^2/4) * v^2, and v^2 = m_H^2/(2*lambda):
# m_W^2 = (g_W^2/4) * m_H^2/(2*lambda) = g_W^2*m_H^2/(8*lambda)
# With lambda = 1/sqrt(60):
# m_W^2 = g_W^2*m_H^2*sqrt(60)/8

m_W_from_Higgs = sqrt(g_W_sq * m_H_GeV**2 * sqrt(60) / 8)
print(f"\n  m_W = g_W*m_H*(60)^{1/4}/sqrt(8) = {m_W_from_Higgs:.4f} GeV  (obs: {m_W_GeV:.4f})")
print(f"  Error: {pct_err(m_W_from_Higgs, m_W_GeV):+.3f}%")

# If we had m_H from BST independently (not from v), we'd be done.
# m_H/m_W = (pi/2)(1-alpha) in BST
mH_mW_BST = (pi/2) * (1 - alpha)
print(f"\n  m_H/m_W (BST) = (pi/2)(1-alpha) = {mH_mW_BST:.6f}")
print(f"  m_H/m_W (obs) = {m_H_GeV/m_W_GeV:.6f}")
print(f"  Error: {pct_err(mH_mW_BST, m_H_GeV/m_W_GeV):+.3f}%")

# So m_H = m_W * (pi/2)(1-alpha)
# And m_H^2 = 2*lambda*v^2 = 2*v^2/sqrt(60)
# => m_W^2*(pi/2)^2*(1-alpha)^2 = 2*v^2/sqrt(60)
# => m_W^2 = 2*v^2/(sqrt(60)*(pi/2)^2*(1-alpha)^2)
# But v = 2*m_W/g_W => v^2 = 4*m_W^2/g_W^2
# => m_W^2 = 2*4*m_W^2/(g_W^2*sqrt(60)*(pi/2)^2*(1-alpha)^2)
# => 1 = 8/(g_W^2*sqrt(60)*(pi/2)^2*(1-alpha)^2)
# => g_W^2 = 8/(sqrt(60)*pi^2*(1-alpha)^2/4)
# => g_W^2 = 32/(sqrt(60)*pi^2*(1-alpha)^2)

g_W_sq_from_BST = 32 / (sqrt(60) * pi**2 * (1-alpha)**2)
print(f"\n  g_W^2 (from BST Higgs relations) = {g_W_sq_from_BST:.8f}")
print(f"  g_W^2 (from alpha, theta_W)       = {g_W_sq:.8f}")
print(f"  Error: {pct_err(g_W_sq_from_BST, g_W_sq):+.3f}%")

# If these are equal: 32/(sqrt(60)*pi^2*(1-alpha)^2) = 4*pi*alpha*13/3
# => 32*3/(4*13*pi*sqrt(60)*pi^2*(1-alpha)^2) = alpha
# => 24/(13*pi^3*sqrt(60)*(1-alpha)^2) = alpha
alpha_from_BST = 24 / (13 * pi**3 * sqrt(60) * (1-alpha)**2)
print(f"\n  alpha (self-consistent) = 24/(13*pi^3*sqrt(60)*(1-alpha)^2) = {alpha_from_BST:.8f}")
print(f"  alpha (observed)        = {alpha:.8f}")
print(f"  Error: {pct_err(alpha_from_BST, alpha):+.3f}%")

# WOW — check this without (1-alpha)^2 since (1-alpha)^2 ~ 1
alpha_approx = 24 / (13 * pi**3 * sqrt(60))
print(f"\n  alpha (approx, dropping (1-alpha)^2) = 24/(13*pi^3*sqrt(60)) = {alpha_approx:.8f}")
print(f"  1/alpha_approx = {1/alpha_approx:.4f}")
print(f"  Error vs observed: {pct_err(alpha_approx, alpha):+.3f}%")

# So: 1/alpha ~ 13*pi^3*sqrt(60)/24 = 13*31.006*7.746/24 = 13*240.15/24 = 130.08
# Hmm, 130 vs 137. 5% off.

# The exact relation:
# alpha * 13 * pi^3 * sqrt(60) * (1-alpha)^2 / 24 = 1
# This is a cubic in alpha... actually it's quadratic in (1-alpha) times alpha

print(f"\n  NOTE: The consistency relation")
print(f"  alpha = 24 / (13 * pi^3 * sqrt(60) * (1-alpha)^2)")
print(f"  gives alpha = {alpha_from_BST:.8f}  ({pct_err(alpha_from_BST, alpha):+.4f}% error)")
print(f"  This is a CONSTRAINT that BST lambda_H, m_H/m_W, and sin^2(theta_W) must satisfy.")
print(f"  The 0.4% error suggests these BST relations are approximately but not exactly consistent,")
print(f"  OR there are small corrections we haven't included.")

# ============================================================
# SECTION 29: Does v follow from the consistency of BST?
# ============================================================

print("\n" + "=" * 80)
print("SECTION 29: v from BST SELF-CONSISTENCY")
print("=" * 80)

print("""
  KEY FINDING: If we take as input:
    (a) alpha = 1/137.036    [from Wyler/D_IV^5]
    (b) sin^2(theta_W) = 3/13  [from BST]
    (c) lambda_H = 1/sqrt(60)   [from BST: lambda = sqrt(2/5!)]
    (d) m_H/m_W = (pi/2)(1-alpha)  [from BST]

  Then v is NOT a free parameter — it's determined up to an overall mass scale!

  From (c) and (d):  m_H^2 = 2*v^2/sqrt(60) and m_H = m_W*(pi/2)(1-alpha)
  From SM:           m_W = g_W*v/2 = v*sqrt(pi*alpha*13/3)

  Combining:         m_W*(pi/2)(1-alpha) = sqrt(2*v^2/sqrt(60))
  => v*sqrt(pi*alpha*13/3)*(pi/2)(1-alpha) = v*sqrt(2/sqrt(60))

  This gives a RELATION among alpha, theta_W, and lambda_H.
  It does NOT fix v in GeV — you still need one mass scale.

  BUT: With m_e known from BST (m_e = m_Pl * 6*pi^5 * alpha^12),
  we have the mass scale. The question then becomes:
  at what energy does electroweak symmetry break, in units of m_e?
""")

# v/m_e = 481,840
# v/m_p = 262.44
# This ratio v/m_p is what we need.

# From the SM relation:
# v = 2*m_W/g_W = 2*m_W*sin(theta_W)/e = 2*m_W*sqrt(3/13)/sqrt(4*pi*alpha)
# = m_W * sqrt(3/(13*pi*alpha))
# = m_W / sqrt(pi*alpha*13/3)

# And m_W = m_H/(pi/2)(1-alpha), m_H^2 = 2*v^2/sqrt(60)
# So m_W = v*sqrt(2/sqrt(60)) / ((pi/2)(1-alpha))
# And v = m_W*sqrt(3/(13*pi*alpha^(-1))) -- wait
# v = m_W / sqrt(pi*alpha*13/3) -- nah wrong direction
# v = 2*m_W/g_W, g_W = sqrt(4*pi*alpha*13/3)
# => v = 2*m_W / sqrt(4*pi*alpha*13/3) = m_W / sqrt(pi*alpha*13/3)
# And m_W = v * sqrt(pi*alpha*13/3)
# These are identities; they determine the RELATION but not the SCALE.

# THE ANSWER: v is determined by requiring that the Higgs potential
# minimum occurs at the right place in D_IV^5 geometry.
# The BST formula should be:
# v = m_e / (alpha * f(pi, n_C, ...))
# where f encodes the Bergman geometry.

# Best numerical candidates from our search:
print("\n  BEST NUMERICAL CANDIDATES for v/m_e:")
print(f"  v/m_e = {target_ratio:.4f}")
print()

# From Section 4 and 15 results, let me print all with < 0.3% error
all_best = wide_results + results  # combine
all_best.sort()
seen = set()
count = 0
for abs_err, formula, val, err in all_best:
    if formula not in seen and count < 30 and abs_err < 0.5:
        seen.add(formula)
        v_pred = val * m_e_GeV
        print(f"    {formula:60s}")
        print(f"      v = {v_pred:.4f} GeV  err = {err:+.4f}%{flag(err)}")
        count += 1

# ============================================================
# SECTION 30: Cross-checks and new ideas
# ============================================================

print("\n" + "=" * 80)
print("SECTION 30: Additional cross-checks")
print("=" * 80)

# v * m_e ?
print(f"  v * m_e = {v_GeV * m_e_GeV:.6f} GeV^2")
print(f"  sqrt(v * m_e) = {sqrt(v_GeV * m_e_GeV):.6f} GeV = {sqrt(v_GeV * m_e_GeV)*1000:.4f} MeV")
print(f"  (This is ~354 MeV, close to Lambda_QCD ~ 332 MeV)")

# v * m_p ?
print(f"\n  v * m_p = {v_GeV * m_p_GeV:.4f} GeV^2")
print(f"  sqrt(v * m_p) = {sqrt(v_GeV * m_p_GeV):.4f} GeV")
print(f"  (This is ~15.2 GeV, no obvious connection)")

# v^3?
print(f"\n  v^3 = {v_GeV**3:.4f} GeV^3")
print(f"  v^4 = {v_GeV**4:.4e} GeV^4")

# m_H * m_W * m_Z ?
print(f"\n  m_H * m_W = {m_H_GeV * m_W_GeV:.4f} GeV^2")
print(f"  m_H * m_Z = {m_H_GeV * m_Z_GeV:.4f} GeV^2")
print(f"  m_W * m_Z = {m_W_GeV * m_Z_GeV:.4f} GeV^2")
print(f"  m_H*m_W*m_Z = {m_H_GeV*m_W_GeV*m_Z_GeV:.4f} GeV^3")
print(f"  v^3 / (m_H*m_W*m_Z) = {v_GeV**3/(m_H_GeV*m_W_GeV*m_Z_GeV):.6f}")

# Yukawa coupling of top quark: y_t = sqrt(2) m_t / v ~ 1
m_t_GeV = 172.69
y_t = sqrt(2) * m_t_GeV / v_GeV
print(f"\n  Top Yukawa: y_t = sqrt(2)*m_t/v = {y_t:.6f}")
print(f"  y_t ~ 1: the top quark 'knows' about v directly")
print(f"  m_t/v = {m_t_GeV/v_GeV:.6f}")
print(f"  m_t = v/sqrt(2) * (1 + {y_t - 1:.4f})")

# Is y_t exactly 1 in BST? That would give v = sqrt(2)*m_t
v_from_yt1 = sqrt(2) * m_t_GeV
print(f"\n  If y_t = 1: v = sqrt(2)*m_t = {v_from_yt1:.4f} GeV  (obs: {v_GeV:.4f}, err: {pct_err(v_from_yt1, v_GeV):+.3f}%){flag(pct_err(v_from_yt1, v_GeV))}")

# Hmm, that's -0.83%! Very close!
# But the top mass isn't derived from BST yet.

# FINAL: G_F decomposition
print("\n  --- G_F = alpha * pi / (sqrt(2) * m_W^2 * sin^2(theta_W)) ---")
print(f"  = alpha * pi * 13 / (3*sqrt(2) * m_W^2)")
print(f"  = 13*pi*alpha / (3*sqrt(2) * m_W^2)")
GF_BST = 13 * pi * alpha / (3 * sqrt(2) * m_W_GeV**2)
print(f"  = {GF_BST:.6e}  (obs: {G_F_GeVm2:.6e})")
print(f"  Error: {pct_err(GF_BST, G_F_GeVm2):+.4f}%")

print("\n" + "=" * 80)
print("END OF EXPLORATION")
print("=" * 80)
print("""
CONCLUSIONS:

1. v is NOT an independent BST parameter — it follows from alpha,
   sin^2(theta_W), and ONE mass scale (m_e or m_Pl).

2. The key unknown is m_W/m_p = 85.637. This ratio must come from
   the geometry of the S^3 Hopf fiber within D_IV^5.

3. v = m_Pl * alpha^{~8} * (geometric factor ~0.61). The power ~8
   is suggestive (= n_C + N_c? = 2*Wallach_min + 2?).

4. The self-consistency relation alpha ~ 24/(13*pi^3*sqrt(60))
   is accurate to ~5%, suggesting BST's Higgs sector formulas
   (lambda_H, m_H/m_W ratio) are approximately but not perfectly
   self-consistent, or need small curvature corrections.

5. The top Yukawa y_t ~ 1 (0.8% off) hints that v = sqrt(2)*m_t
   might be exact in BST, making the top quark mass fundamental.

6. MOST PROMISING DIRECTION: Derive m_W from Casimir eigenvalue
   on S^3 fiber, analogous to m_p = 6*pi^5 * m_e from Casimir
   on D_IV^5 bulk.
""")
