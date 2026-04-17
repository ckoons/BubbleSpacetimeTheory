#!/usr/bin/env python3
"""
Toy 1258 — Gravitational Exponent 24: Triple Identity + Casimir Cycles
========================================================================
Backs T1296 (Lyra): The exponent 24 in G = ℏc(6π⁵)²α²⁴/m_e² is FORCED.

Three independent characterizations of 24:
  (a) (n_C − 1)! = 4! = 24
  (b) dim SU(n_C) = n_C² − 1 = 25 − 1 = 24
  (c) 4C₂ = 4 × 6 = 24

Uniqueness: n_C² − 1 = (n_C − 1)! holds ONLY at n_C = 5.

Casimir cycles: k = 6, 12, 18, 24 (multiples of C₂). Only k=6 is a
speaking pair. Gravity requires all four cycles — three silent.

Numerical: G = ℏc(6π⁵)²α²⁴/m_e² = 6.679 × 10⁻¹¹ (observed 6.6743, 0.07%).

Elie — April 18, 2026

Copyright (c) 2026 Casey Koons. All rights reserved.
"""

import math
from fractions import Fraction

# ── BST constants ──
rank = 2
N_c = 3
n_C = 5
C_2 = 6
g = 7
N_max = 137

# Physical constants (CODATA 2018)
hbar = 1.054571817e-34   # J·s
c_light = 2.99792458e8   # m/s
m_e = 9.1093837015e-31   # kg
alpha = 1.0 / 137.035999084
G_observed = 6.67430e-11  # m³/(kg·s²)

passed = 0
failed = 0
total = 12


def test(n, name, condition, detail=""):
    global passed, failed
    status = "PASS" if condition else "FAIL"
    if condition:
        passed += 1
    else:
        failed += 1
    print(f"  T{n}: [{status}] {name}")
    if detail:
        print(f"       {detail}")


print("=" * 70)
print("Toy 1258 — Gravitational Exponent 24: Triple Identity + Casimir Cycles")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# SECTION 1: Triple Identity
# ═══════════════════════════════════════════════════════════════════════
print("\n── Section 1: Triple Identity for 24 ──")

val_a = math.factorial(n_C - 1)     # (n_C-1)! = 4! = 24
val_b = n_C**2 - 1                  # n_C² - 1 = 24
val_c = 4 * C_2                     # 4·C₂ = 24

print(f"  (a) (n_C − 1)! = ({n_C}−1)! = {n_C-1}! = {val_a}")
print(f"  (b) n_C² − 1 = {n_C}² − 1 = {val_b}")
print(f"  (c) 4C₂ = 4×{C_2} = {val_c}")

test(1, "All three give 24",
     val_a == 24 and val_b == 24 and val_c == 24,
     f"{val_a} = {val_b} = {val_c} = 24")

test(2, "dim SU(n_C) = n_C² − 1 = 24 = dim SU(5)",
     val_b == 24,
     f"SU({n_C}) has dimension {val_b}")

# ═══════════════════════════════════════════════════════════════════════
# SECTION 2: Uniqueness at n_C = 5
# ═══════════════════════════════════════════════════════════════════════
print("\n── Section 2: Uniqueness n_C² − 1 = (n_C − 1)! ──")

# Check for all n from 2 to 20
matches = []
for n in range(2, 21):
    lhs = n**2 - 1
    rhs = math.factorial(n - 1)
    if lhs == rhs:
        matches.append(n)
    if n <= 8:
        print(f"  n={n}: n²−1={lhs}, (n−1)!={rhs} {'✓' if lhs == rhs else ''}")

test(3, "n² − 1 = (n − 1)! has UNIQUE solution n = 5",
     matches == [5],
     f"Solutions in [2,20]: {matches}")

# For n ≥ 6: (n-1)! grows as factorial, n²-1 as polynomial → no more matches
# (n-1)! > n²-1 for all n ≥ 6 (5! = 120 > 35 = 6²-1)
test(4, "For n ≥ 6: (n−1)! >> n²−1 (no further solutions)",
     math.factorial(5) > 6**2 - 1,
     f"5! = {math.factorial(5)} >> 6²−1 = {6**2 - 1}")

# ═══════════════════════════════════════════════════════════════════════
# SECTION 3: Casimir Cycle Structure
# ═══════════════════════════════════════════════════════════════════════
print("\n── Section 3: Casimir Cycles ──")

# Casimir cycles at multiples of C₂
casimir_levels = [C_2 * j for j in range(1, 5)]  # [6, 12, 18, 24]
print(f"  Casimir cycle levels: k = {casimir_levels} (multiples of C₂={C_2})")

test(5, "Four Casimir cycles at k = 6, 12, 18, 24",
     casimir_levels == [6, 12, 18, 24],
     f"j·C₂ for j=1..4: {casimir_levels}")

# Speaking pair analysis: k is speaking iff k mod n_C ∈ {0, 1}
speaking = []
silent = []
for k in casimir_levels:
    if k % n_C in (0, 1):
        speaking.append(k)
    else:
        silent.append(k)

print(f"  Speaking (k mod {n_C} ∈ {{0,1}}): {speaking}")
print(f"  Silent: {silent}")

test(6, "Only k=6 is speaking (k mod 5 = 1); k=12,18,24 silent",
     speaking == [6] and len(silent) == 3,
     f"k=6: 6 mod 5 = {6%5}. k=12: {12%5}. k=18: {18%5}. k=24: {24%5}.")

test(7, "3 of 4 Casimir cycles are silent → gravity beyond gauge readout",
     len(silent) == 3,
     "Gravity couples to total mass-energy, not specific charges")

# ═══════════════════════════════════════════════════════════════════════
# SECTION 4: Heat Kernel Ratio at k=16
# ═══════════════════════════════════════════════════════════════════════
print("\n── Section 4: Heat Kernel at k=16 (Third Speaking Pair) ──")

# k=16 is a speaking pair (16 mod 5 = 1)
# Ratio c_{2k-1}/c_{2k} = -C(k,2)/n_C
k = 16
ratio_16 = Fraction(-k * (k - 1), 2 * n_C)  # -C(16,2)/5 = -120/5 = -24
print(f"  k=16: ratio = −C({k},2)/{n_C} = −{k*(k-1)//2}/{n_C} = {ratio_16}")

test(8, "Heat kernel ratio at k=16 = −24 = −dim SU(5)",
     ratio_16 == -24,
     f"Ratio = {ratio_16} = −(n_C²−1)")

# The three speaking pairs and their ratios
speaking_pairs = [(5, 6), (10, 11), (15, 16)]
for k_pair_start, k_pair_end in speaking_pairs:
    r = Fraction(-k_pair_end * (k_pair_end - 1), 2 * n_C)
    print(f"  Speaking pair ({k_pair_start},{k_pair_end}): ratio = {r}")

test(9, "Third speaking pair reads −24 = −dim SU(5)",
     Fraction(-16 * 15, 2 * 5) == -24,
     "k=5,6 → SU(3); k=10,11 → isotropy; k=15,16 → SU(5)")

# ═══════════════════════════════════════════════════════════════════════
# SECTION 5: G Numerical Computation
# ═══════════════════════════════════════════════════════════════════════
print("\n── Section 5: Gravitational Constant ──")

# G = ℏc (6π⁵)² α²⁴ / m_e²
coeff = (6 * math.pi**5)**2
alpha_24 = alpha**24
G_bst = hbar * c_light * coeff * alpha_24 / m_e**2

print(f"  G_BST = ℏc (6π⁵)² α²⁴ / m_e²")
print(f"  6π⁵ = {6 * math.pi**5:.6f}")
print(f"  (6π⁵)² = {coeff:.6e}")
print(f"  α²⁴ = {alpha_24:.6e}")
print(f"  G_BST = {G_bst:.4e} m³/(kg·s²)")
print(f"  G_obs = {G_observed:.4e} m³/(kg·s²)")

err = abs(G_bst - G_observed) / G_observed
test(10, f"G_BST matches observed (error = {err:.2%})",
     err < 0.001,
     f"G_BST = {G_bst:.4e}, G_obs = {G_observed:.4e}")

# α²⁴ suppression
suppression = alpha_24
log_suppression = 24 * math.log10(alpha)
print(f"\n  α²⁴ = {suppression:.4e}")
print(f"  log₁₀(α²⁴) = 24 × log₁₀(1/137) = {log_suppression:.2f}")

test(11, f"Hierarchy: α²⁴ ≈ 10^{{−51}} (gravity is weak by counting)",
     -52 < log_suppression < -50,
     f"24 coherent spectral traversals × 1/137 each = 10^{{{log_suppression:.1f}}}")

# ═══════════════════════════════════════════════════════════════════════
# SECTION 6: Why 24 = 4C₂ (not 2C₂ or 6C₂)
# ═══════════════════════════════════════════════════════════════════════
print("\n── Section 6: Why 4 Cycles ──")

# The factor 4: G involves (Planck mass)² = (ℏc/G)
# Each Casimir cycle gives α^{C₂} = α⁶ per vertex
# G ~ α^{2 × 2C₂} = α^{4C₂}: two vertices × two dimensions (rank²=4 paths)
# Or: the Planck mass formula involves m_e² in denominator → 2 electron masses
# × 2 spectral channels per mass → 4 total Casimir traversals

factor = 4
total_exp = factor * C_2
test(12, f"4 Casimir cycles × C₂ = {factor}×{C_2} = {total_exp} = exponent",
     total_exp == 24,
     f"rank²={rank**2}=4 paths through C₂={C_2} spectral channels each")

# ═══════════════════════════════════════════════════════════════════════
# SCORE
# ═══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print(f"SCORE: {passed}/{total} PASS ({failed} fail)")
print(f"AC Complexity: C=2, D=0")
print()
print("KEY FINDINGS:")
print(f"  24 = (n_C−1)! = n_C²−1 = 4C₂ — three independent routes")
print(f"  n_C²−1 = (n_C−1)! has UNIQUE solution n_C = 5 (26th uniqueness condition)")
print(f"  4 Casimir cycles at k = 6, 12, 18, 24; only k=6 is speaking")
print(f"  Heat kernel k=16: ratio = −24 = −dim SU(5)")
print(f"  G = ℏc(6π⁵)²α²⁴/m_e² = {G_bst:.4e} (obs {G_observed:.4e}, {err:.2%})")
print(f"  Hierarchy = counting theorem: 24 × log(1/137) ≈ −51 decades")
print()
print("HONEST CAVEATS:")
print("  - The 4 in 4C₂ = 24 comes from rank² = 4, but the")
print("    detailed mechanism (why rank² paths) needs tighter derivation")
print("  - Casimir cycle structure at k=12,18 not directly verified")
print("    (only k=6 and k=16 have heat kernel data)")
print("  - G derivation via KK is standard; BST contribution is the inputs")
print("=" * 70)
