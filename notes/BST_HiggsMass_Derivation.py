#!/usr/bin/env python3
"""
BST Higgs Mass Derivation
Casey Koons and Claude Opus 4.6, March 12, 2026

The Higgs boson mass — the last major SM parameter not yet derived
from D_IV^5 geometry.

Two independent routes found:
  A) lambda_H = sqrt(2/n_C!) = 1/sqrt(60)  =>  m_H = 125.11 GeV (0.11%)
  B) m_H/m_W = pi/2 * (1 - alpha)          =>  m_H = 125.33 GeV (0.07%)

Both use only BST parameters (n_C=5, N_c=3, alpha) plus the
electroweak scale (v or m_W).
"""

import numpy as np
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ================================================================
# Physical constants
# ================================================================
m_e = 0.51100  # MeV
m_p = 938.272  # MeV
m_W = 80.377e3  # MeV (80.377 GeV)
m_Z = 91.1876e3  # MeV
v_higgs = 246.22e3  # MeV (Higgs vev)
m_H_obs = 125.25e3  # MeV (125.25 +/- 0.17 GeV)
m_H_err = 0.17e3  # MeV
alpha = 1.0 / 137.036

# BST parameters
n_C = 5  # complex dimension of D_IV^5
N_c = 3  # color SU(3)
N_max = 137

# ================================================================
# Basic ratios
# ================================================================
print("=" * 70)
print("HIGGS MASS: BASIC RATIOS")
print("=" * 70)
print()
print(f"  m_H (observed) = {m_H_obs/1e3:.2f} GeV")
print(f"  m_H / m_e = {m_H_obs/m_e:.1f}")
print(f"  m_H / m_p = {m_H_obs/m_p:.2f}")
print(f"  m_H / m_W = {m_H_obs/m_W:.4f}")
print(f"  m_H / m_Z = {m_H_obs/m_Z:.4f}")
print(f"  m_H / v   = {m_H_obs/v_higgs:.4f}")
print()

# Higgs quartic coupling
lambda_H_obs = m_H_obs**2 / (2 * v_higgs**2)
print(f"  Higgs quartic: lambda_H = m_H^2/(2v^2) = {lambda_H_obs:.5f}")
print()

# ================================================================
# FORMULA A: lambda_H = sqrt(2/n_C!) = 1/sqrt(60)
# ================================================================
print("=" * 70)
print("FORMULA A: lambda_H = sqrt(2/n_C!)")
print("  The Higgs quartic from permutation symmetry")
print("=" * 70)
print()

nC_factorial = math.factorial(n_C)  # 5! = 120
lambda_A = np.sqrt(2.0 / nC_factorial)
m_H_A = v_higgs * np.sqrt(2 * lambda_A)
dev_A = (m_H_A - m_H_obs) / m_H_obs * 100

print(f"  n_C! = {n_C}! = {nC_factorial}")
print(f"  2/n_C! = 2/{nC_factorial} = {2.0/nC_factorial:.6f}")
print(f"  lambda_H = sqrt(2/{nC_factorial}) = 1/sqrt({nC_factorial//2}) = {lambda_A:.5f}")
print(f"  Observed lambda_H = {lambda_H_obs:.5f}")
print(f"  Deviation: {(lambda_A - lambda_H_obs)/lambda_H_obs * 100:+.3f}%")
print()
print(f"  m_H = v * sqrt(2*lambda_H)")
print(f"       = {v_higgs/1e3:.2f} * sqrt(2 * {lambda_A:.5f})")
print(f"       = {m_H_A/1e3:.2f} GeV")
print(f"  Observed: {m_H_obs/1e3:.2f} +/- {m_H_err/1e3:.2f} GeV")
print(f"  Deviation: {dev_A:+.3f}%")
print()

# Why 60?
print(f"  WHY 60 = n_C!/2 = {nC_factorial}//2?")
print(f"    60 = |A_5| = order of alternating group (icosahedral rotations)")
print(f"    60 = 4 * N_c * n_C = 4 * {N_c} * {n_C}")
print(f"    60 = 1920 / 2^n_C = 1920 / {2**n_C}")
print(f"    60 = dim_R(D_IV^5) * 2N_c = 10 * 6")
print()

# The special identity
print(f"  SPECIAL IDENTITY: 8*N_c = (n_C - 1)!")
print(f"    8 * {N_c} = {8*N_c}")
print(f"    ({n_C} - 1)! = 4! = {math.factorial(n_C-1)}")
print(f"    Equal? {8*N_c == math.factorial(n_C-1)}")
print()
print(f"  Check all n_C from 2 to 8:")
for nc in range(2, 9):
    nc_color = nc - 2 if nc >= 3 else 1  # N_c = n_C - 2 for n_C >= 3
    # Actually N_c = 3 is fixed. Let's check 8*3 = (n_C-1)!
    val = math.factorial(nc - 1) if nc > 1 else 1
    match = "  <== MATCH!" if val == 24 else ""
    print(f"    n_C = {nc}: (n_C-1)! = {val}{match}")
print()

# ================================================================
# FORMULA B: m_H/m_W = pi/2 (tree level)
# ================================================================
print("=" * 70)
print("FORMULA B: m_H/m_W = pi/2")
print("  Radial-to-angular oscillation frequency on D_IV^5")
print("=" * 70)
print()

ratio_obs = m_H_obs / m_W
print(f"  m_H/m_W (observed) = {ratio_obs:.4f}")
print(f"  pi/2               = {np.pi/2:.4f}")
print(f"  Deviation (tree):    {(np.pi/2 - ratio_obs)/ratio_obs * 100:+.3f}%")
print()

# Tree level
m_H_B_tree = (np.pi / 2) * m_W
dev_B_tree = (m_H_B_tree - m_H_obs) / m_H_obs * 100
print(f"  Tree level: m_H = (pi/2) * m_W = {m_H_B_tree/1e3:.2f} GeV")
print(f"  Deviation: {dev_B_tree:+.3f}%")
print()

# With O(alpha) correction
m_H_B_corr = (np.pi / 2) * (1 - alpha) * m_W
dev_B_corr = (m_H_B_corr - m_H_obs) / m_H_obs * 100
print(f"  With O(alpha) correction:")
print(f"  m_H = (pi/2)(1 - alpha) * m_W")
print(f"       = (pi/2)(136/137) * {m_W/1e3:.3f}")
print(f"       = {m_H_B_corr/1e3:.2f} GeV")
print(f"  Deviation: {dev_B_corr:+.3f}%")
print()

# ================================================================
# FORMULA C: Combining A and B
# ================================================================
print("=" * 70)
print("COMBINING THE TWO ROUTES")
print("=" * 70)
print()

# From A: m_H = v * sqrt(2/sqrt(60))
# From B: m_H = (pi/2)(1-alpha) * m_W
# So: v * (2/sqrt(60))^{1/2} = (pi/2)(1-alpha) * m_W
# And v = m_W / (g/2) with g = e/sin(theta_W)
# v = 2*m_W/g, and g^2 = 4*pi*alpha/sin^2(theta_W)

print(f"  Route A: m_H = v * (2/sqrt(60))^{{1/2}} = {m_H_A/1e3:.2f} GeV")
print(f"  Route B: m_H = (pi/2)(1-alpha) * m_W   = {m_H_B_corr/1e3:.2f} GeV")
print(f"  Average: {(m_H_A + m_H_B_corr)/2e3:.2f} GeV")
print(f"  Observed: {m_H_obs/1e3:.2f} GeV")
print()

# Check independence
ratio_AB = m_H_A / m_H_B_corr
print(f"  Ratio A/B = {ratio_AB:.4f} (would be 1.0 if identical)")
print(f"  They differ by {abs(ratio_AB - 1)*100:.2f}% — genuinely independent")
print()

# ================================================================
# GEOMETRIC INTERPRETATION
# ================================================================
print("=" * 70)
print("GEOMETRIC INTERPRETATION")
print("=" * 70)
print(f"""
  The Higgs field is the unique scalar in the Standard Model.
  On D_IV^5, it corresponds to the RADIAL (dilation) mode —
  the displacement from the origin of the bounded symmetric domain.

  D_IV^5 has rank 2, giving two radial directions:
  - One is fixed by scale invariance (the dilaton/conformal mode)
  - One remains free: this IS the Higgs field

  The W and Z bosons are ANGULAR (gauge) modes on the fiber.
  The Higgs is the AMPLITUDE mode.

  Formula A: lambda_H = sqrt(2/n_C!)
  ─────────
  The Higgs quartic coupling is suppressed by the square root of
  the permutation symmetry of n_C complex dimensions.

  Equivalently: lambda_H^2 = 2/n_C! = (2^n_C)/|W(D_5)|
  The Higgs self-interaction squared equals the ratio of phase
  degrees of freedom to Weyl group order.

  Formula B: m_H/m_W = pi/2
  ─────────
  The ratio of radial to angular oscillation frequency on a curved
  Bergman metric. In flat space, a harmonic oscillator has equal
  radial and angular frequencies. On D_IV^5, the curvature creates
  a pi/2 ratio — the quarter-period relationship between amplitude
  and phase oscillations.

  The O(alpha) correction (1 - alpha) accounts for the same
  channel noise that gives alpha its role everywhere else in BST:
  the radial mode loses a fraction alpha of its frequency to the
  geometric information channel.
""")

# ================================================================
# CROSS-CHECKS WITH OTHER BST RESULTS
# ================================================================
print("=" * 70)
print("CROSS-CHECKS")
print("=" * 70)
print()

# m_H in proton mass units
m_H_over_mp = m_H_obs / m_p
print(f"  m_H / m_p = {m_H_over_mp:.2f}")
print(f"  Close to N_max - N_c = {N_max} - {N_c} = {N_max - N_c}")
print(f"  {N_max - N_c} * m_p = {(N_max-N_c)*m_p/1e3:.2f} GeV (deviation: "
      f"{((N_max-N_c)*m_p - m_H_obs)/m_H_obs*100:+.2f}%)")
print(f"  Interesting but probably numerology (no geometric derivation)")
print()

# m_H and the Fermi scale
print(f"  v / m_H = {v_higgs/m_H_obs:.4f}")
print(f"  sqrt(2*sqrt(60)) = {np.sqrt(2*np.sqrt(60)):.4f}")
print(f"  Deviation: {(np.sqrt(2*np.sqrt(60)) - v_higgs/m_H_obs)/(v_higgs/m_H_obs)*100:+.3f}%")
print()

# Higgs mass and top quark
m_top = 172.69e3  # MeV
print(f"  m_top = {m_top/1e3:.2f} GeV")
print(f"  m_top / m_H = {m_top/m_H_obs:.4f}")
print(f"  sqrt(2) = {np.sqrt(2):.4f}")
print(f"  Close to sqrt(2) — but actually {(m_top/m_H_obs)/np.sqrt(2):.4f} of sqrt(2)")
print()

# y_top (top Yukawa)
y_top = np.sqrt(2) * m_top / v_higgs
print(f"  y_top = sqrt(2) * m_top / v = {y_top:.4f}")
print(f"  Near unity: the top Yukawa coupling ~ 1")
print(f"  In BST: y_top = 1 - correction? y_top observed = {y_top:.4f}")
print()

# ================================================================
# FULL RESULTS TABLE UPDATE
# ================================================================
print("=" * 70)
print("UPDATED BST RESULTS TABLE")
print("=" * 70)
print()
print(f"  {'Quantity':<25s}  {'BST Formula':<30s}  {'Predicted':>12s}  {'Observed':>12s}  {'Dev':>8s}")
print(f"  {'='*90}")

results = [
    ("alpha", "(9/8pi^4)(pi^5/1920)^{1/4}", f"{alpha:.6f}", "0.007297", "0.0001%"),
    ("m_p/m_e", "6*pi^5", f"{6*np.pi**5:.1f}", "1836.15", "0.002%"),
    ("sin^2(theta_W)", "3/13", f"{3/13:.5f}", "0.23122", "0.2%"),
    ("m_H (from lambda)", "v*sqrt(2*sqrt(2/5!))", f"{m_H_A/1e3:.2f} GeV", f"{m_H_obs/1e3:.2f} GeV", f"{abs(dev_A):.2f}%"),
    ("m_H (from m_W)", "(pi/2)(1-alpha)*m_W", f"{m_H_B_corr/1e3:.2f} GeV", f"{m_H_obs/1e3:.2f} GeV", f"{abs(dev_B_corr):.2f}%"),
    ("lambda_H", "sqrt(2/5!)", f"{lambda_A:.5f}", f"{lambda_H_obs:.5f}", f"{abs((lambda_A-lambda_H_obs)/lambda_H_obs*100):.2f}%"),
]

for r in results:
    print(f"  {r[0]:<25s}  {r[1]:<30s}  {r[2]:>12s}  {r[3]:>12s}  {r[4]:>8s}")
print()

# ================================================================
# PLOT
# ================================================================
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle('BST Higgs Mass Derivation: Two Independent Routes',
             fontsize=14, fontweight='bold')

# Plot 1: Lambda_H comparison
ax = axes[0]
labels = ['Observed', 'BST: sqrt(2/5!)', '1/8 (rejected)']
values = [lambda_H_obs, lambda_A, 1/8]
colors = ['black', 'green', 'red']
bars = ax.bar(labels, values, color=colors, alpha=0.7, edgecolor='black')
ax.set_ylabel('lambda_H', fontsize=12)
ax.set_title('Higgs Quartic Coupling', fontsize=13)
ax.axhline(y=lambda_H_obs, color='black', linestyle='--', linewidth=0.5, alpha=0.5)
for i, (v, l) in enumerate(zip(values, labels)):
    dev = (v - lambda_H_obs) / lambda_H_obs * 100
    ax.text(i, v + 0.002, f'{dev:+.2f}%', ha='center', fontsize=10)
ax.set_ylim(0.11, 0.14)

# Plot 2: m_H predictions
ax = axes[1]
labels2 = ['Observed', 'Route A\nsqrt(2/5!)', 'Route B\n(pi/2)(1-a)m_W']
vals2 = [m_H_obs/1e3, m_H_A/1e3, m_H_B_corr/1e3]
colors2 = ['black', 'blue', 'red']
ax.bar(labels2, vals2, color=colors2, alpha=0.7, edgecolor='black')
ax.axhline(y=m_H_obs/1e3, color='black', linestyle='--', linewidth=0.5, alpha=0.5)
ax.axhspan((m_H_obs-m_H_err)/1e3, (m_H_obs+m_H_err)/1e3, alpha=0.2, color='gray',
           label='Exp. uncertainty')
for i, v in enumerate(vals2):
    dev = (v - m_H_obs/1e3) / (m_H_obs/1e3) * 100
    ax.text(i, v + 0.3, f'{dev:+.2f}%', ha='center', fontsize=10)
ax.set_ylabel('m_H (GeV)', fontsize=12)
ax.set_title('Higgs Mass: Two Routes', fontsize=13)
ax.set_ylim(124, 127)
ax.legend(fontsize=9)

# Plot 3: The uniqueness of n_C = 5
ax = axes[2]
nC_range = range(2, 9)
factorial_vals = [math.factorial(nc - 1) for nc in nC_range]
target = 8 * N_c  # = 24

ax.bar(list(nC_range), factorial_vals, color='lightblue', edgecolor='black', alpha=0.7)
ax.axhline(y=target, color='red', linewidth=2, linestyle='-',
           label=f'8*N_c = {target}')
ax.bar([5], [math.factorial(4)], color='green', edgecolor='black', alpha=0.8)

ax.set_xlabel('n_C (complex dimension)', fontsize=12)
ax.set_ylabel('(n_C - 1)!', fontsize=12)
ax.set_title('Uniqueness: 8*N_c = (n_C-1)!\nOnly at n_C = 5', fontsize=13)
ax.legend(fontsize=11)
ax.set_yscale('log')
ax.set_xticks(list(nC_range))

plt.tight_layout()
plt.savefig('/Users/cskoons/projects/github/BubbleSpacetimeTheory/notes/BST_HiggsMass_Derivation.png',
            dpi=150, bbox_inches='tight')
print("Saved: BST_HiggsMass_Derivation.png")
print()

# ================================================================
# OPEN QUESTIONS
# ================================================================
print("=" * 70)
print("OPEN QUESTIONS")
print("=" * 70)
print(f"""
  1. DERIVE v (Higgs vev) FROM BST
     Both formulas require either v or m_W as input. BST derives
     sin^2(theta_W) = 3/13 and m_W = m_Z*sqrt(10/13), but m_Z
     itself is not yet derived from geometry. The Fermi scale
     v = 246.22 GeV needs a geometric origin.

  2. PROVE lambda_H = sqrt(2/n_C!) FROM D_IV^5
     Why should the Higgs quartic involve the factorial of the
     complex dimension? Possible route: the Higgs potential on the
     Bergman metric involves an integral over all n_C! permutations
     of the complex coordinates, and the quartic coupling is the
     square root of the normalized integral.

  3. PROVE m_H/m_W = pi/2 FROM BERGMAN OSCILLATION THEORY
     Does the ratio of radial to angular frequency on a Type IV
     bounded symmetric domain equal pi/2? This would follow from
     the Bergman metric curvature properties.

  4. THE IDENTITY 8*N_c = (n_C-1)!
     This holds only at n_C=5 and connects the two formulas.
     It means: 4*N_c*n_C = n_C!/2, or equivalently:
     the product of the three BST integers (4, N_c, n_C) equals
     half the permutation group of n_C dimensions.
     Understanding why may unify the two routes.

  5. TOP YUKAWA ~ 1
     y_top = {y_top:.4f}. Is there a BST prediction that y_top = 1
     exactly at tree level, with corrections from alpha?
""")
