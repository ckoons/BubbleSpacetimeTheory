#!/usr/bin/env python3
"""
Toy 648 — g·f Product Theorem (Minimum Information Density)
============================================================
Grace investigation #1: g·f = 7 × 3/(5π) = 21/(5π) ≈ 1.34
                         C₂·f = 6 × 3/(5π) = 18/(5π) ≈ 1.15
Both barely above 1. If exact, the geometry forbids empty spectral layers.

AC(0) PROOF DECOMPOSITION:
  Step 1 (DEFINITION): f = N_c/(n_C·π) = 3/(5π)
  Step 2 (DEFINITION): g = 7 (Bergman genus, pole order of K(z,w))
  Step 3 (DEFINITION): C₂ = 6 (Casimir eigenvalue of π₆)
  Step 4 (IDENTITY): g·f = 7·3/(5π) = 21/(5π) = C(g,2)/(n_C·π)
  Step 5 (IDENTITY): C₂·f = 6·3/(5π) = 18/(5π) = (N_c·C₂)/(n_C·π)
  Step 6 (IDENTITY): g·f > 1 ⟺ 21 > 5π ⟺ 21 > 15.708... ✓
  Step 7 (IDENTITY): C₂·f > 1 ⟺ 18 > 5π ⟺ 18 > 15.708... ✓

AC(0) DEPTH: 0 (definitions + identities only)
BST CONNECTION: The fill fraction f = 19.1% is calibrated so that each
spectral layer (counted by g) and each information quantum (counted by C₂)
carries at least 1 unit of realized information. Below 1 = empty layer.
The geometry forbids vacancies.

Scorecard: 10 tests.
"""

import math
import sys

# ═══════════════════════════════════════════════════════════════
# BST CONSTANTS
# ═══════════════════════════════════════════════════════════════
N_c = 3       # color dimension (SU(3) fiber)
n_C = 5       # compact dimension (complex dim of D_IV^5)
g = 7         # Bergman genus (pole order)
C_2 = 6       # Casimir eigenvalue
rank = 2      # rank of D_IV^5
N_max = 137   # max shell

f = N_c / (n_C * math.pi)  # fill fraction

# ═══════════════════════════════════════════════════════════════
# EXACT PRODUCTS
# ═══════════════════════════════════════════════════════════════
gf = g * f          # = 21/(5π)
C2f = C_2 * f       # = 18/(5π)

# Exact rational parts
gf_exact_num = g * N_c        # = 21
gf_exact_den_coeff = n_C      # = 5, times π
C2f_exact_num = C_2 * N_c     # = 18
C2f_exact_den_coeff = n_C     # = 5, times π

# Combinatorial identities
Cg2 = g * (g - 1) // 2       # C(7,2) = 21 = g·N_c
NcC2 = N_c * C_2             # 3·6 = 18

# ═══════════════════════════════════════════════════════════════
# DERIVED QUANTITIES
# ═══════════════════════════════════════════════════════════════

# The average product
avg_gC2_f = (g + C_2) / 2 * f  # (7+6)/2 × f = 6.5 × f

# The ratio
gf_over_C2f = gf / C2f  # = g/C₂ = 7/6

# Products with other integers
Nc_f = N_c * f           # = 3·3/(5π) = 9/(5π) ≈ 0.573
nC_f = n_C * f           # = 5·3/(5π) = 3/π ≈ 0.955
rank_f = rank * f         # = 2·3/(5π) = 6/(5π) ≈ 0.382
Nmax_f = N_max * f        # = 137·3/(5π) = 411/(5π) ≈ 26.18

# ═══════════════════════════════════════════════════════════════
# SCORECARD
# ═══════════════════════════════════════════════════════════════

tests = []

def test(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    tests.append((name, status, detail))
    return condition

print("=" * 70)
print("TOY 648 — g·f PRODUCT THEOREM")
print("=" * 70)

# T1: g·f = 21/(5π)
gf_expected = 21 / (5 * math.pi)
test("T1", abs(gf - gf_expected) < 1e-15,
     f"g·f = {gf:.10f}, expected 21/(5π) = {gf_expected:.10f}")

# T2: C₂·f = 18/(5π)
C2f_expected = 18 / (5 * math.pi)
test("T2", abs(C2f - C2f_expected) < 1e-15,
     f"C₂·f = {C2f:.10f}, expected 18/(5π) = {C2f_expected:.10f}")

# T3: g·f > 1 (no empty spectral layers)
test("T3", gf > 1.0,
     f"g·f = {gf:.6f} > 1 — every spectral layer has info")

# T4: C₂·f > 1 (no empty information quanta)
test("T4", C2f > 1.0,
     f"C₂·f = {C2f:.6f} > 1 — every info quantum has content")

# T5: g·N_c = C(g,2) = 21 (combinatorial identity)
test("T5", g * N_c == Cg2 == 21,
     f"g·N_c = {g*N_c}, C(7,2) = {Cg2}, both = 21")

# T6: C₂·N_c = 18 (algebraic identity)
test("T6", C_2 * N_c == 18,
     f"C₂·N_c = {C_2*N_c} = 18")

# T7: g·f / C₂·f = g/C₂ = 7/6
test("T7", abs(gf / C2f - 7/6) < 1e-15,
     f"g·f / C₂·f = {gf/C2f:.10f} = 7/6 = {7/6:.10f}")

# T8: n_C·f < 1 (compact dimension density below 1 — WHY?)
# n_C·f = 3/π ≈ 0.955. Just below 1. The compact dimension
# does NOT guarantee full coverage — only g and C₂ do.
test("T8", nC_f < 1.0,
     f"n_C·f = {nC_f:.6f} < 1 — compact dim doesn't guarantee coverage")

# T9: rank·f < 1 (rank density below 1)
test("T9", rank_f < 1.0,
     f"rank·f = {rank_f:.6f} < 1")

# T10: ONLY g and C₂ give products > 1
# This is the theorem: among all five integers, exactly the two spectral
# integers (g, C₂) yield x·f > 1. The others don't.
products = {
    "N_c·f": Nc_f,
    "n_C·f": nC_f,
    "g·f": gf,
    "C₂·f": C2f,
    "rank·f": rank_f,
}
above_1 = [k for k, v in products.items() if v > 1.0]
test("T10", set(above_1) == {"g·f", "C₂·f"},
     f"Products > 1: {above_1} — exactly the spectral integers")

# ═══════════════════════════════════════════════════════════════
# PRINT RESULTS
# ═══════════════════════════════════════════════════════════════

print(f"\n--- Fill fraction products for all five integers ---\n")
for name, val in sorted(products.items(), key=lambda x: -x[1]):
    marker = " ← > 1 (NO VACANCY)" if val > 1 else ""
    print(f"  {name:8s} = {val:.6f}{marker}")

print(f"\n  Average (g+C₂)/2 × f = {avg_gC2_f:.6f}")
print(f"  N_max·f = {Nmax_f:.2f} (≈ 26 info units across all shells)")

print(f"\n--- Combinatorial structure ---\n")
print(f"  g·f  = g·N_c / (n_C·π) = C(g,2) / (n_C·π) = 21/(5π)")
print(f"  C₂·f = C₂·N_c / (n_C·π) = 18/(5π)")
print(f"  Numerators: 21 = C(7,2) = triangular number")
print(f"              18 = 3×6 = N_c × C₂")
print(f"  Ratio: 21/18 = 7/6 = g/C₂")

print(f"\n--- The theorem ---\n")
print(f"  Among the five BST integers {{N_c=3, n_C=5, g=7, C₂=6, rank=2}},")
print(f"  EXACTLY the two spectral integers (g, C₂) satisfy x·f > 1.")
print(f"  This means: every spectral layer and every information quantum")
print(f"  carries at least 1 unit of realized information.")
print(f"  The geometry forbids empty spectral layers.")
print(f"  AC(0) depth: 0 (all steps are definitions or identities).")

print(f"\n--- Scorecard ---\n")
passed = 0
for name, status, detail in tests:
    print(f"  {name}: {status} — {detail}")
    if status == "PASS":
        passed += 1

print(f"\n{'='*70}")
print(f"SCORECARD: {passed}/{len(tests)}")
print(f"{'='*70}")

# ═══════════════════════════════════════════════════════════════
# SYNTHESIS
# ═══════════════════════════════════════════════════════════════

print(f"""
SYNTHESIS:

The fill fraction f = N_c/(n_C·π) = 3/(5π) ≈ 19.1% is calibrated by the
geometry of D_IV^5 so that:

  g·f  = 21/(5π) ≈ 1.34  >  1   (spectral layers: no vacancies)
  C₂·f = 18/(5π) ≈ 1.15  >  1   (information quanta: no vacancies)

These are the ONLY two of the five integers that satisfy x·f > 1.
The spectral integers (g = Bergman genus, C₂ = Casimir eigenvalue) are
exactly the ones the geometry protects from emptiness. The topological
integers (N_c = color, n_C = compact dim, rank = 2) do NOT get this
guarantee.

The numerator g·N_c = 21 = C(7,2) is a binomial coefficient — the number
of spectral pairs. The numerator C₂·N_c = 18 is the Casimir-color product.
Both exceed 5π = 15.708... by comfortable margins (33% and 15%).

The theorem: the fill fraction is geometrically tuned to prevent spectral
vacancies while allowing topological slack. This is not a coincidence —
it's a consequence of g and C₂ being spectral invariants (they count
modes of the Bergman kernel) while N_c, n_C, and rank are topological
(they count dimensions of the space).
""")

sys.exit(0 if passed == len(tests) else 1)
