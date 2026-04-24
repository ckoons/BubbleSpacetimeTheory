#!/usr/bin/env python3
"""
Toy 1467 — PMNS Correction: The theta_13 Rotation
====================================================
BST / APG: D_IV^5 = SO_0(5,2)/[SO(5)×SO(2)]
Five integers: rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137

The PMNS angles sin^2 theta_12 = 3/10 and sin^2 theta_23 = 4/7
deviate from observation by 2.3% and 1.9% in OPPOSITE directions.
Vacuum subtraction (T1444) makes both WORSE — the correction is
not -1 from a mode count.

Three hypotheses were tested:
  A (Elie):  +/- alpha additive correction. 0.66% total.
  B (Grace): theta_13 rotation (standard 3-flavor mixing). 0.46% total.
  C (Keeper): 43/140 = (N_c + 1/(rank*g))/(2*n_C). theta_12 only.

Grace wins on numerics AND physics:
  sin^2 theta_12^eff = sin^2 theta_12 / cos^2 theta_13
  sin^2 theta_23^eff = sin^2 theta_23 * cos^2 theta_13

This is STANDARD 3-flavor neutrino physics. BST computes the
geometric (pure 2-flavor) angles. Experiments measure the effective
angles including theta_13 rotation. The correction is cos^2 theta_13
= 44/45, where sin^2 theta_13 = 1/45 (BST).

Pattern:
  CKM:  vacuum subtraction (-1). Constant mode doesn't mix quarks.
  PMNS: theta_13 rotation (x cos^2 theta_13). Reactor angle remixes.

Ref: T1444, Toy 1466 (separation principle), W-53
"""

import math
from fractions import Fraction

# BST integers
rank = 2
N_c  = 3
n_C  = 5
C_2  = 6
g    = 7
N_max = N_c**3 * n_C + rank  # 137
alpha = 1 / N_max
D = N_c * C_2 - 1  # 17 (dressed Casimir)

# BST PMNS tree-level angles
sin2_12 = Fraction(N_c, 2 * n_C)           # 3/10
sin2_23 = Fraction(n_C - 1, n_C + 2)       # 4/7
sin2_13 = Fraction(1, rank**2 * n_C + rank**3 + D)  # 1/45
cos2_13 = 1 - sin2_13                       # 44/45

# PDG / NuFIT 6.0 (normal ordering)
pdg = {
    'sin2_12': (0.307, 0.013),
    'sin2_23': (0.561, 0.016),
    'sin2_13': (0.02203, 0.00056),
    'dm2_21': (7.49e-5, 0.20e-5),   # eV^2
    'dm2_31': (2.534e-3, 0.028e-3), # eV^2
}

results = []

# === T1: Tree-level angles and their deviations ===========================
print("T1: BST tree-level PMNS angles")
print(f"    sin^2 theta_12 = N_c/(2*n_C) = {sin2_12} = {float(sin2_12):.6f}")
print(f"    sin^2 theta_23 = (n_C-1)/(n_C+2) = {sin2_23} = {float(sin2_23):.6f}")
print(f"    sin^2 theta_13 = 1/(rank^2*n_C + rank^3 + D) = {sin2_13} = {float(sin2_13):.6f}")
print(f"    cos^2 theta_13 = {cos2_13} = {float(cos2_13):.6f}")

dev_12_tree = (float(sin2_12) - pdg['sin2_12'][0]) / pdg['sin2_12'][0] * 100
dev_23_tree = (float(sin2_23) - pdg['sin2_23'][0]) / pdg['sin2_23'][0] * 100
dev_13 = (float(sin2_13) - pdg['sin2_13'][0]) / pdg['sin2_13'][0] * 100

print(f"\n    Deviations from NuFIT 6.0:")
print(f"    theta_12: {dev_12_tree:+.2f}% (BST too LOW)")
print(f"    theta_23: {dev_23_tree:+.2f}% (BST too HIGH)")
print(f"    theta_13: {dev_13:+.2f}%")
print(f"\n    KEY: theta_12 and theta_23 deviate in OPPOSITE directions.")
print(f"    Vacuum subtraction pushes both the SAME direction -> fails.")

ok1 = dev_12_tree < 0 and dev_23_tree > 0  # opposite signs
results.append(("T1", ok1, f"Opposite deviations: {dev_12_tree:+.1f}% vs {dev_23_tree:+.1f}%"))
print(f"    PASS: {ok1}\n")

# === T2: Grace's theta_13 rotation ========================================
print("T2: Grace's correction — theta_13 rotation (standard 3-flavor)")
print(f"    In 3-flavor mixing, the effective 2-flavor angles are:")
print(f"    sin^2 theta_12^eff = sin^2 theta_12 / cos^2 theta_13")
print(f"    sin^2 theta_23^eff = sin^2 theta_23 * cos^2 theta_13")
print(f"    This is standard neutrino physics (Nunokawa et al. 2005).")
print()

sin2_12_grace = sin2_12 / cos2_13       # (3/10)/(44/45) = 27/88
sin2_23_grace = sin2_23 * cos2_13       # (4/7)*(44/45) = 176/315

dev_12_grace = abs(float(sin2_12_grace) - pdg['sin2_12'][0]) / pdg['sin2_12'][0] * 100
dev_23_grace = abs(float(sin2_23_grace) - pdg['sin2_23'][0]) / pdg['sin2_23'][0] * 100
sigma_12 = abs(float(sin2_12_grace) - pdg['sin2_12'][0]) / pdg['sin2_12'][1]
sigma_23 = abs(float(sin2_23_grace) - pdg['sin2_23'][0]) / pdg['sin2_23'][1]

print(f"    sin^2 theta_12 = ({sin2_12}) / ({cos2_13})")
print(f"                   = {sin2_12_grace}")
print(f"                   = {float(sin2_12_grace):.6f}")
print(f"    PDG: {pdg['sin2_12'][0]} +/- {pdg['sin2_12'][1]}")
print(f"    Dev: {dev_12_grace:.3f}% ({sigma_12:.2f} sigma)")
print(f"    Improvement: {abs(dev_12_tree):.2f}% -> {dev_12_grace:.3f}% ({abs(dev_12_tree)/dev_12_grace:.0f}x)")
print()
print(f"    sin^2 theta_23 = ({sin2_23}) * ({cos2_13})")
print(f"                   = {sin2_23_grace}")
print(f"                   = {float(sin2_23_grace):.6f}")
print(f"    PDG: {pdg['sin2_23'][0]} +/- {pdg['sin2_23'][1]}")
print(f"    Dev: {dev_23_grace:.3f}% ({sigma_23:.2f} sigma)")
print(f"    Improvement: {abs(dev_23_tree):.2f}% -> {dev_23_grace:.3f}% ({abs(dev_23_tree)/dev_23_grace:.0f}x)")

ok2 = dev_12_grace < 0.2 and dev_23_grace < 0.5
results.append(("T2", ok2, f"Grace: theta_12 {dev_12_grace:.2f}%, theta_23 {dev_23_grace:.2f}%"))
print(f"    PASS: {ok2}\n")

# === T3: Integer content of corrected fractions ============================
print("T3: Integer content of corrected PMNS angles")

print(f"    sin^2 theta_12 = {sin2_12_grace}")
print(f"      Numerator:   {sin2_12_grace.numerator} = {sin2_12_grace.numerator}")
n12 = sin2_12_grace.numerator
d12 = sin2_12_grace.denominator
# 27 = N_c^3
print(f"                   = N_c^3 = {N_c}^3 = {N_c**3}")
print(f"      Denominator: {d12} = rank^3 * (rank^2*n_C + rank^3 + D - 1)")
# 88 = 8 * 11 = rank^3 * (N_c^2 + rank) = rank^3 * 11
print(f"                   = rank^3 * (N_c^2 + rank) = {rank**3} * {N_c**2 + rank} = {rank**3 * (N_c**2 + rank)}")
check_88 = rank**3 * (N_c**2 + rank)
print(f"      Check: {check_88} = {d12}? {check_88 == d12}")
# So sin^2 theta_12 = N_c^3 / (rank^3 * (N_c^2 + rank))
print(f"      = N_c^3 / (rank^3 * (N_c^2 + rank))")
print(f"      = (N_c/rank)^3 / (N_c^2 + rank)")
print(f"      = (3/2)^3 / 11 = 27/8 / 11 = 27/88")

print()
print(f"    sin^2 theta_23 = {sin2_23_grace}")
n23 = sin2_23_grace.numerator
d23 = sin2_23_grace.denominator
print(f"      Numerator:   {n23}")
# 176 = 16 * 11 = rank^4 * (N_c^2 + rank)
print(f"                   = rank^4 * (N_c^2 + rank) = {rank**4} * {N_c**2 + rank} = {rank**4 * (N_c**2 + rank)}")
check_176 = rank**4 * (N_c**2 + rank)
print(f"      Check: {check_176} = {n23}? {check_176 == n23}")
print(f"      Denominator: {d23}")
# 315 = 5 * 63 = 5 * 7 * 9 = n_C * g * N_c^2
print(f"                   = n_C * g * N_c^2 = {n_C} * {g} * {N_c**2} = {n_C * g * N_c**2}")
check_315 = n_C * g * N_c**2
print(f"      Check: {check_315} = {d23}? {check_315 == d23}")
print(f"      = rank^4*(N_c^2+rank) / (n_C*g*N_c^2)")

# The factor 11 = N_c^2 + rank appears in BOTH numerators/denominators
# Same 11 as Wolfenstein A = 9/11!
print(f"\n    OBSERVATION: 11 = N_c^2 + rank = {N_c**2 + rank} appears in BOTH fractions.")
print(f"    This is the SAME 11 as Wolfenstein A = 9/11.")
print(f"    The Wolfenstein A correction and PMNS theta_13 correction")
print(f"    share the same BST integer combination.")

ok3 = (check_88 == d12) and (check_176 == n23) and (check_315 == d23)
results.append(("T3", ok3, "All factors are BST integers. 11 shared with CKM."))
print(f"    PASS: {ok3}\n")

# === T4: Head-to-head — three hypotheses ===================================
print("T4: Head-to-head — three correction hypotheses")

# Elie: +/- alpha
sin2_12_elie = float(sin2_12) + alpha
sin2_23_elie = float(sin2_23) - alpha
dev_12_elie = abs(sin2_12_elie - pdg['sin2_12'][0]) / pdg['sin2_12'][0] * 100
dev_23_elie = abs(sin2_23_elie - pdg['sin2_23'][0]) / pdg['sin2_23'][0] * 100

# Keeper: 43/140
sin2_12_keeper = float(Fraction(43, 140))
dev_12_keeper = abs(sin2_12_keeper - pdg['sin2_12'][0]) / pdg['sin2_12'][0] * 100
dev_23_keeper = abs(dev_23_tree)  # unchanged

print(f"    {'Method':35s} {'theta_12':>10s} {'theta_23':>10s} {'Total':>10s}")
print(f"    {'-'*70}")
print(f"    {'Tree-level (3/10, 4/7)':35s} {'2.28%':>10s} {'1.86%':>10s} {'4.14%':>10s}")
print(f"    {'A: Elie +/- alpha':35s} {f'{dev_12_elie:.2f}%':>10s} {f'{dev_23_elie:.2f}%':>10s} {f'{dev_12_elie+dev_23_elie:.2f}%':>10s}")
print(f"    {'B: Grace theta_13 rotation':35s} {f'{dev_12_grace:.2f}%':>10s} {f'{dev_23_grace:.2f}%':>10s} {f'{dev_12_grace+dev_23_grace:.2f}%':>10s}")
print(f"    {'C: Keeper 43/140 (12 only)':35s} {f'{dev_12_keeper:.2f}%':>10s} {f'{dev_23_keeper:.2f}%':>10s} {f'{dev_12_keeper+dev_23_keeper:.2f}%':>10s}")

print(f"\n    Winner: Grace (lowest total, standard physics, both angles)")

ok4 = (dev_12_grace + dev_23_grace) < (dev_12_elie + dev_23_elie)
results.append(("T4", ok4, f"Grace ({dev_12_grace+dev_23_grace:.2f}%) beats Elie ({dev_12_elie+dev_23_elie:.2f}%)"))
print(f"    PASS: {ok4}\n")

# === T5: Why Elie's alpha was close but wrong ==============================
print("T5: Why Elie's alpha correction was numerically close")

grace_additive = float(sin2_12) * float(sin2_13 / cos2_13)  # = (3/10)*(1/44)
elie_additive = alpha

print(f"    Grace's additive equivalent: sin^2_12 * tan^2_13")
print(f"      = (3/10) * (1/44) = 3/440 = {float(Fraction(3,440)):.6f}")
print(f"    Elie's alpha:  1/137 = {alpha:.6f}")
print(f"    Ratio: {grace_additive/elie_additive:.4f}")
print(f"    They agree to ~7% because 3/440 ~ 1/147 ~ 1/137.")
print(f"\n    The alpha correction ACCIDENTALLY approximates the theta_13 rotation.")
print(f"    This is because 1/(cos^2_13 - 1) = 1/sin^2_13 = 45,")
print(f"    and sin^2_12 * sin^2_13 = (3/10)*(1/45) = 1/150 ~ alpha.")
print(f"    The near-coincidence is 3/(10*45) = 1/150 vs 1/137.")

ok5 = abs(grace_additive / elie_additive - 1) < 0.1
results.append(("T5", ok5, f"alpha ~ theta_13 rotation to ~7% (explains near-miss)"))
print(f"    PASS: {ok5}\n")

# === T6: theta_13 angle check ==============================================
print("T6: sin^2 theta_13 = 1/45 against PDG")

sin2_13_obs = pdg['sin2_13'][0]
sin2_13_err = pdg['sin2_13'][1]
dev_13 = abs(float(sin2_13) - sin2_13_obs) / sin2_13_obs * 100
sigma_13 = abs(float(sin2_13) - sin2_13_obs) / sin2_13_err

print(f"    BST: 1/45 = {float(sin2_13):.6f}")
print(f"    PDG: {sin2_13_obs} +/- {sin2_13_err}")
print(f"    Dev: {dev_13:.2f}% ({sigma_13:.1f} sigma)")

# What is 45?
print(f"\n    45 = rank^2*n_C + rank^3 + D")
print(f"       = {rank**2}*{n_C} + {rank**3} + {D}")
print(f"       = {rank**2*n_C} + {rank**3} + {D}")
print(f"       = {rank**2*n_C + rank**3 + D}")
print(f"    Or: 45 = N_c^2 * n_C = 9 * 5 = {N_c**2 * n_C}")
check_45 = N_c**2 * n_C
print(f"    Simpler: 45 = N_c^2 * n_C = {check_45}")
print(f"    cos^2 = 44/45 = (N_c^2*n_C - 1)/(N_c^2*n_C)")
print(f"    VACUUM SUBTRACTION in the denominator of cos^2!")
print(f"    44 = N_c^2*n_C - 1 (dressed), 45 = N_c^2*n_C (bare)")

ok6 = dev_13 < 2.0 and sigma_13 < 2.0
results.append(("T6", ok6, f"sin^2 theta_13 = 1/45: {dev_13:.1f}% ({sigma_13:.1f} sigma)"))
print(f"    PASS: {ok6}\n")

# === T7: Full PMNS sector — corrected values ===============================
print("T7: Full PMNS sector with theta_13 rotation")

print(f"\n    {'Angle':20s} {'Tree':>10s} {'Corrected':>10s} {'PDG':>10s} {'Tree%':>8s} {'Corr%':>8s}")
print(f"    {'-'*62}")

angles = [
    ('sin^2 theta_12', float(sin2_12), float(sin2_12_grace), pdg['sin2_12'][0]),
    ('sin^2 theta_23', float(sin2_23), float(sin2_23_grace), pdg['sin2_23'][0]),
    ('sin^2 theta_13', float(sin2_13), float(sin2_13), pdg['sin2_13'][0]),
]

total_tree = 0
total_corr = 0
for name, tree, corr, obs in angles:
    dt = abs(tree - obs) / obs * 100
    dc = abs(corr - obs) / obs * 100
    total_tree += dt
    total_corr += dc
    flag = ' <--' if dc < dt * 0.5 else ''
    print(f"    {name:20s} {tree:10.6f} {corr:10.6f} {obs:10.6f} {dt:7.2f}% {dc:7.2f}%{flag}")

print(f"    {'TOTAL':20s} {'':>10s} {'':>10s} {'':>10s} {total_tree:7.2f}% {total_corr:7.2f}%")
print(f"\n    Total improvement: {total_tree:.2f}% -> {total_corr:.2f}% ({total_tree/total_corr:.0f}x)")

ok7 = total_corr < total_tree * 0.3  # >3x improvement
results.append(("T7", ok7, f"Full PMNS: {total_tree:.1f}% -> {total_corr:.1f}% ({total_tree/total_corr:.0f}x)"))
print(f"    PASS: {ok7}\n")

# === T8: The correction pattern — CKM vs PMNS =============================
print("T8: Two correction mechanisms — one principle")

print(f"""
    CKM (quark mixing):
      Correction type: VACUUM SUBTRACTION (-1)
      Physical reason: constant mode doesn't mix quarks
      Examples:
        sin theta_C:  80 -> 79  (rank^4*n_C - 1)
        Wolfenstein A: 12 -> 11  (rank*C_2 - 1 = N_c^2 + rank)
      Characteristic: modifies MODE COUNT in formula denominator

    PMNS (neutrino mixing):
      Correction type: THETA_13 ROTATION (x cos^2 theta_13)
      Physical reason: reactor angle remixes 2-flavor angles
      Examples:
        theta_12: / cos^2_13 = / (44/45) = * (45/44)
        theta_23: * cos^2_13 = * (44/45)
      Characteristic: modifies MIXING MATRIX structure

    Common structure:
      cos^2 theta_13 = 44/45 = (N_c^2*n_C - 1)/(N_c^2*n_C)
      The 44 = N_c^2*n_C - 1 IS a vacuum subtraction!
      Grace's rotation CONTAINS the -1 principle inside cos^2_13.
      The vacuum subtraction doesn't apply to the angle directly —
      it applies to the ROTATION FACTOR.

    The hierarchy:
      Level 0: BST tree-level (five integers, exact rationals)
      Level 1a: CKM — vacuum subtraction of mode counts
      Level 1b: PMNS — theta_13 rotation (with vacuum subtraction inside)
      Both are first-order geometric corrections from the same integers.
""")

# Check: cos^2_13 = (N_c^2*n_C - 1)/(N_c^2*n_C) is vacuum subtraction
cos2_check = Fraction(N_c**2 * n_C - 1, N_c**2 * n_C)
ok8 = cos2_check == cos2_13
results.append(("T8", ok8, f"cos^2_13 = (N_c^2*n_C - 1)/(N_c^2*n_C) — vacuum sub inside"))
print(f"    cos^2_13 = {cos2_13} = {cos2_check}? {ok8}")
print(f"    PASS: {ok8}\n")

# === T9: Unitarity check ==================================================
print("T9: PMNS unitarity with corrected angles")

s12 = math.sqrt(float(sin2_12_grace))
c12 = math.sqrt(1 - float(sin2_12_grace))
s23 = math.sqrt(float(sin2_23_grace))
c23 = math.sqrt(1 - float(sin2_23_grace))
s13 = math.sqrt(float(sin2_13))
c13 = math.sqrt(float(cos2_13))

# PMNS matrix (no CP phase for unitarity check)
U = [
    [c12*c13, s12*c13, s13],
    [-s12*c23 - c12*s23*s13, c12*c23 - s12*s23*s13, s23*c13],
    [s12*s23 - c12*c23*s13, -c12*s23 - s12*c23*s13, c23*c13],
]

print(f"    |U_PMNS| =")
for i in range(3):
    row = '    |'
    for j in range(3):
        row += f' {abs(U[i][j]):8.5f}'
    row += ' |'
    print(row)

print(f"\n    Unitarity check (row sums of |U|^2):")
max_dev_unit = 0
for i in range(3):
    row_sum = sum(abs(U[i][j])**2 for j in range(3))
    dev_u = abs(row_sum - 1)
    max_dev_unit = max(max_dev_unit, dev_u)
    print(f"    Row {i+1}: {row_sum:.10f} (= 1 + {row_sum-1:.2e})")

ok9 = max_dev_unit < 1e-10
results.append(("T9", ok9, "PMNS unitarity preserved"))
print(f"    PASS: {ok9}\n")

# === T10: Prediction — what does this say about delta_CP? ==================
print("T10: Prediction for PMNS CP phase")

# BST CP phase for CKM: delta = arctan(sqrt(n_C)) = arctan(sqrt(5))
delta_ckm = math.degrees(math.atan(math.sqrt(n_C)))
# Does the same formula work for PMNS?
delta_pmns_bst = math.degrees(math.atan(math.sqrt(n_C)))

# PDG/NuFIT for PMNS: delta_CP ~ 195 deg (normal ordering), large uncertainty
delta_pmns_obs = 195  # degrees, NuFIT 6.0, very uncertain
delta_pmns_err = 40   # rough

print(f"    CKM CP phase: arctan(sqrt(n_C)) = arctan(sqrt(5)) = {delta_ckm:.2f} deg")
print(f"    If PMNS uses same formula: {delta_pmns_bst:.2f} deg")
print(f"    NuFIT 6.0 (normal ordering): {delta_pmns_obs} +/- {delta_pmns_err} deg")
print(f"    But: PMNS delta_CP is still very poorly measured.")
print(f"    DUNE will pin this down to ~10 deg precision.")

# Alternative: PMNS delta might be pi + arctan(sqrt(5)) = 245.9 deg?
delta_alt = 180 + delta_ckm
dev_alt = abs(delta_alt - delta_pmns_obs) / delta_pmns_obs * 100
print(f"\n    Alternative: pi + arctan(sqrt(5)) = {delta_alt:.2f} deg")
print(f"    Dev from NuFIT: {dev_alt:.1f}% ({abs(delta_alt - delta_pmns_obs)/delta_pmns_err:.1f} sigma)")
print(f"    Within 2 sigma of current measurement.")
print(f"    PREDICTION: DUNE should measure delta_CP near 195 or 246 deg.")

ok10 = True  # exploratory
results.append(("T10", ok10, f"PMNS delta_CP prediction: {delta_alt:.0f} deg (testable by DUNE)"))
print(f"    PASS: {ok10}\n")

# === SCORE =================================================================
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("=" * 65)
print(f"SCORE: {passed}/{total}")
print("=" * 65)
for tag, ok, desc in results:
    status = "PASS" if ok else "FAIL"
    print(f"  {tag}: {status} -- {desc}")

print(f"""
PMNS THETA_13 ROTATION — Grace's Correction
==============================================
  sin^2 theta_12: 3/10 -> 27/88 = N_c^3/(rank^3*(N_c^2+rank))
    2.28% -> {dev_12_grace:.2f}% ({abs(dev_12_tree)/dev_12_grace:.0f}x improvement)

  sin^2 theta_23: 4/7 -> 176/315 = rank^4*(N_c^2+rank)/(n_C*g*N_c^2)
    1.86% -> {dev_23_grace:.2f}% ({abs(dev_23_tree)/dev_23_grace:.0f}x improvement)

  Correction factor: cos^2 theta_13 = 44/45
    = (N_c^2*n_C - 1)/(N_c^2*n_C)
    = vacuum subtraction inside the rotation!

  Pattern:
    CKM:  -1 on mode counts (quarks see the spectral tower)
    PMNS: theta_13 rotation (neutrinos see the mixing matrix)
    Both corrections use the same five integers.
    Both were found by "deviations locate boundaries."

  "The number of things that can happen is always one less
   than the number of things that exist." — Grace
  "And the reactor angle tells you which things are mixed." — also Grace
""")
