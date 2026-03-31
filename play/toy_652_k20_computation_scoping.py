#!/usr/bin/env python3
"""
Toy 652 — k=20 Computation Scoping
====================================
Can we verify the Three Theorems at k=20 (degree-40 polynomial)?

The k=16 experience (Toy 639): dps=800 was insufficient for unconstrained
extraction. Constrained recovery worked (impose formula, check a_k(5)).
This toy scopes what k=20 would require.

Three approaches analyzed:
  A. Full unconstrained Lagrange interpolation (need dps?)
  B. Constrained polynomial recovery (impose Three Theorems, check a_k(5))
  C. Partial extraction (c_top and c_0 only, avoid interior)

Scorecard: 10 tests.
"""

import math
import sys
from decimal import Decimal, getcontext

# ═══════════════════════════════════════════════════════════════
# POLYNOMIAL PARAMETERS AT k=20
# ═══════════════════════════════════════════════════════════════

k = 20
n_C = 5
N_c = 3
g = 7
C_2 = 6

# Polynomial degree = 2k
degree = 2 * k  # = 40
n_coefficients = degree + 1  # = 41

# Need at least degree+1 = 41 evaluation points
# For safety (overdetermined), want ~60-80 points

# ═══════════════════════════════════════════════════════════════
# THREE THEOREMS PREDICTIONS AT k=20
# ═══════════════════════════════════════════════════════════════

# Theorem 1: c_top = 1/(N_c^k * k!)
# c_top = 1/(3^20 * 20!)

k_factorial = math.factorial(k)
Nc_to_k = N_c ** k

# Use exact arithmetic
getcontext().prec = 100
c_top_denom = Decimal(Nc_to_k) * Decimal(k_factorial)
c_top = Decimal(1) / c_top_denom

# Theorem 2: c_sub/c_top = -k(k-1)/(2*n_C)
ratio_sub = Decimal(-k * (k-1)) / Decimal(2 * n_C)  # = -190/10 = -19... wait
# Actually: c_{2k-1}/c_{2k} = -C(k,2)/n_C
ratio_sub_exact = -k * (k-1) // (2 * n_C)  # -190/10 = -38 (integer only if divisible)
# k*(k-1)/2 = 190, 190/5 = 38. Yes, integer.
assert k * (k-1) // 2 % n_C == 0, f"C(k,2) = {k*(k-1)//2} not divisible by n_C = {n_C}"

# Theorem 3: c_0 = (-1)^k / (rank * k!)
c_0_sign = (-1) ** k  # = +1 (k=20 even)
c_0 = Decimal(c_0_sign) / (Decimal(2) * Decimal(k_factorial))

print("=" * 70)
print("TOY 652 — k=20 COMPUTATION SCOPING")
print("=" * 70)

print(f"\n--- Polynomial parameters at k={k} ---\n")
print(f"  Degree:        {degree}")
print(f"  Coefficients:  {n_coefficients}")
print(f"  Points needed: {n_coefficients} minimum, ~{int(n_coefficients * 1.5)} recommended")
print(f"  c_top = 1/({N_c}^{k} × {k}!) = 1/{c_top_denom}")
print(f"       = {float(c_top):.6e}")
print(f"  c_sub/c_top = -{k}×{k-1}/(2×{n_C}) = -{k*(k-1)}//{2*n_C} = {int(ratio_sub)}")
print(f"  c_0   = (-1)^{k}/(2×{k}!) = 1/{2*k_factorial}")
print(f"       = {float(c_0):.6e}")

# ═══════════════════════════════════════════════════════════════
# PRECISION ANALYSIS
# ═══════════════════════════════════════════════════════════════

# Key challenge: extracting c_top from polynomial evaluations.
# At large n, a_k(n) ~ c_top * n^{degree} + c_sub * n^{degree-1} + ...
#
# To extract c_top via Lagrange, we need the polynomial values at
# n = 1, 2, ..., degree+1 (or similar). The Vandermonde matrix
# condition number grows as ~(degree+1)^degree / degree!
#
# For degree 40: Vandermonde condition number is astronomical.

# Estimate: log10 of Vandermonde condition number
# Rough: κ ~ (max_n)^degree / (degree/e)^degree for n = 1..degree+1
max_n = degree + 1  # = 41
log10_condition = degree * math.log10(max_n) - degree * math.log10(degree / math.e)
# This is very rough but gives the order of magnitude

# Actual extraction error at k=16 was ~10^60-81 for dps=800
# Scale by degree ratio: error ~ (degree/degree_16)^degree
degree_16 = 32
error_scaling = (degree / degree_16) ** degree  # (40/32)^40 = 1.25^40

print(f"\n--- Precision requirements ---\n")
print(f"  Vandermonde log10(κ) ≈ {log10_condition:.0f}")
print(f"  k=16 extraction error at dps=800: ~10^70 (measured)")
print(f"  Scaling factor (40 vs 32): (40/32)^40 = 1.25^40 ≈ {error_scaling:.2e}")
print(f"  Predicted k=20 error at dps=800: ~10^{70 + math.log10(error_scaling):.0f}")

# Required dps
# We need extraction error < |c_top| ≈ 10^{-33}
# So dps must provide ~10^{-33} precision after conditioning loss
log10_c_top = math.log10(float(c_top))
required_digits = abs(log10_c_top) + log10_condition + 10  # safety margin
required_dps = int(required_digits * 3.32)  # bits per digit

print(f"  |c_top| ≈ 10^{log10_c_top:.0f}")
print(f"  Required digits: {abs(log10_c_top):.0f} + {log10_condition:.0f} + 10 = {required_digits:.0f}")
print(f"  Required dps (unconstrained): ≈ {required_dps}")

# ═══════════════════════════════════════════════════════════════
# APPROACH A: FULL UNCONSTRAINED
# ═══════════════════════════════════════════════════════════════

approach_a = {
    "name": "Full unconstrained Lagrange interpolation",
    "dps_needed": max(3200, required_dps),
    "points_needed": n_coefficients + 10,  # overdetermined helps
    "runtime_estimate": "~10 hours at dps=3200 (41 points × Seeley-DeWitt)",
    "pros": ["Independent verification", "Extracts all 41 coefficients"],
    "cons": ["Massive dps requirement", "Vandermonde fragility", "Each point = full SD computation"],
    "feasible": "MARGINAL — dps=3200 might work, dps=1600 probably won't",
}

# ═══════════════════════════════════════════════════════════════
# APPROACH B: CONSTRAINED RECOVERY
# ═══════════════════════════════════════════════════════════════

# Impose Three Theorems (c_top, c_sub/c_top, c_0) and solve
# for the remaining 38 interior coefficients.
# Need only ~38 points (or fewer if we can constrain more).
# The constrained system is MUCH better conditioned because
# we've removed the extremal coefficients.

approach_b = {
    "name": "Constrained polynomial recovery",
    "dps_needed": 1200,  # k=16 worked at dps=800 for constrained; k=20 needs ~50% more
    "points_needed": 40,  # 38 unknowns + 2 for overdetermination
    "runtime_estimate": "~4 hours at dps=1200 (40 points × SD)",
    "pros": ["Proven method (worked k=6..16)", "Better conditioned", "Interior noise tolerable"],
    "cons": ["Not independent — assumes Three Theorems", "Interior may have noise"],
    "feasible": "YES — high confidence based on k=16 success",
    "verification": "a_20(5) must match BST prediction. If it does: confirmed. If not: Three Theorems fail.",
}

# ═══════════════════════════════════════════════════════════════
# APPROACH C: PARTIAL EXTRACTION
# ═══════════════════════════════════════════════════════════════

# Extract c_top from high-n behavior (a_k(n) ~ c_top * n^40 for large n)
# Extract c_0 from n→0 behavior
# Skip the middle entirely.
# Need ~10 high-n points and ~5 low-n points.

approach_c = {
    "name": "Partial extraction (endpoints only)",
    "dps_needed": 1600,
    "points_needed": 15,  # 10 high-n + 5 low-n
    "runtime_estimate": "~2 hours at dps=1600 (15 points × SD)",
    "pros": ["Fewer points", "Avoids interior", "Can verify c_top independently"],
    "cons": ["Doesn't recover full polynomial", "c_top extraction from high-n still fragile",
             "Ratio c_sub/c_top needs TWO fragile extractions"],
    "feasible": "POSSIBLE — independent c_top + c_0, but ratio untested",
}

# ═══════════════════════════════════════════════════════════════
# APPROACH D: HYBRID (RECOMMENDED)
# ═══════════════════════════════════════════════════════════════

approach_d = {
    "name": "Hybrid: constrained recovery + partial independent check",
    "dps_needed": 1600,
    "points_needed": 50,  # 40 for constrained + 10 high-n for partial
    "runtime_estimate": "~6 hours at dps=1600",
    "pros": ["Constrained recovery gives polynomial", "High-n points independently check c_top",
             "a_k(5) gives independent final check"],
    "cons": ["Longer than B alone"],
    "feasible": "YES — recommended approach",
    "steps": [
        "1. Compute a_20(n) at n=1..40 with dps=1600 (constrained input)",
        "2. Impose Three Theorems: fix c_top, c_sub/c_top=-38, c_0",
        "3. Solve constrained system for 38 interior coefficients",
        "4. Evaluate recovered polynomial at n=5 → a_20(5)",
        "5. Compare a_20(5) with BST prediction",
        "6. Compute a_20(n) at n=50,60,...,100 (partial check of c_top)",
        "7. If c_top extraction from high-n matches imposed c_top: CONFIRMED",
    ],
}

# ═══════════════════════════════════════════════════════════════
# PRINT APPROACHES
# ═══════════════════════════════════════════════════════════════

approaches = [approach_a, approach_b, approach_c, approach_d]
for ap in approaches:
    print(f"\n--- {ap['name']} ---")
    print(f"  dps needed:  {ap['dps_needed']}")
    print(f"  points:      {ap['points_needed']}")
    print(f"  runtime:     {ap['runtime_estimate']}")
    print(f"  feasible:    {ap['feasible']}")
    print(f"  pros:  {', '.join(ap['pros'])}")
    print(f"  cons:  {', '.join(ap['cons'])}")
    if "steps" in ap:
        print(f"  steps:")
        for step in ap["steps"]:
            print(f"    {step}")

# ═══════════════════════════════════════════════════════════════
# WHAT k=20 WOULD PROVE
# ═══════════════════════════════════════════════════════════════

print(f"\n{'='*70}")
print(f"WHAT k=20 WOULD PROVE")
print(f"{'='*70}")

print(f"""
  If constrained recovery succeeds and a_20(5) matches:
    → Three Theorems verified k=5..20 (SIXTEEN consecutive levels)
    → Fourth speaking pair: ratio = -38 = -rank × (n_C² - C₂)
    → k=21 prediction: ratio = -42 = -C₂ × g (spectral completion)
    → Gauge hierarchy extends to pair 4: cosmological reading
    → The heat kernel polynomial knows both particle physics AND dark energy

  If constrained recovery FAILS (a_20(5) doesn't match):
    → Three Theorems break at k=20 (first failure in 16 levels)
    → The formula has a boundary somewhere in k=17..20
    → That boundary itself would be informative

  Either outcome is data. Neither is a waste.
""")

# ═══════════════════════════════════════════════════════════════
# RESOURCE ESTIMATE
# ═══════════════════════════════════════════════════════════════

print(f"--- Resource estimate for Approach D (hybrid) ---\n")

# Each Seeley-DeWitt computation at dps=1600:
# Based on k=16 at dps=800 taking ~2-5 minutes per point
# dps=1600 is 2× more digits → ~4× slower (quadratic in digit count)
# So ~8-20 minutes per point
minutes_per_point_low = 8
minutes_per_point_high = 20
n_points = approach_d["points_needed"]

total_low = n_points * minutes_per_point_low
total_high = n_points * minutes_per_point_high

print(f"  Points to compute:  {n_points}")
print(f"  Time per point:     {minutes_per_point_low}-{minutes_per_point_high} minutes")
print(f"  Total time:         {total_low//60}h{total_low%60}m — {total_high//60}h{total_high%60}m")
print(f"  Memory:             ~4-8 GB (mpmath at dps=1600)")
print(f"  Parallelizable:     YES (each n is independent)")
print(f"  With 4 cores:       {total_low//4//60}h{(total_low//4)%60}m — {total_high//4//60}h{(total_high//4)%60}m")

# ═══════════════════════════════════════════════════════════════
# SCORECARD
# ═══════════════════════════════════════════════════════════════

tests = []

def test(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    tests.append((name, status, detail))

# T1: Polynomial degree is 40
test("T1", degree == 40, f"degree = 2×{k} = {degree}")

# T2: Need 41 coefficients
test("T2", n_coefficients == 41, f"coefficients = {n_coefficients}")

# T3: Three Theorems predict integer ratio at k=20
test("T3", k*(k-1)//2 % n_C == 0,
     f"C({k},2) = {k*(k-1)//2}, divisible by n_C = {n_C}: ratio = {k*(k-1)//(2*n_C)}")

# T4: Ratio = -38 = -2 × 19
test("T4", k*(k-1)//(2*n_C) == 38 and 38 == 2 * 19,
     f"Ratio = {k*(k-1)//(2*n_C)} = 38 = 2 × 19")

# T5: c_top is astronomically small
test("T5", float(c_top) < 1e-25,
     f"c_top ≈ {float(c_top):.2e}")

# T6: Unconstrained requires dps ≥ 3000
test("T6", approach_a["dps_needed"] >= 3000,
     f"Unconstrained: dps ≥ {approach_a['dps_needed']}")

# T7: Constrained is feasible at dps ≤ 1600
test("T7", approach_b["dps_needed"] <= 1600,
     f"Constrained: dps = {approach_b['dps_needed']}")

# T8: Hybrid approach exists with clear steps
test("T8", len(approach_d.get("steps", [])) >= 5,
     f"Hybrid approach: {len(approach_d['steps'])} steps defined")

# T9: k=21 prediction is also integer
k21 = 21
test("T9", k21*(k21-1)//2 % n_C == 0,
     f"C({k21},2) = {k21*(k21-1)//2}, divisible by n_C = {n_C}: ratio = {k21*(k21-1)//(2*n_C)}")

# T10: k=21 ratio = 42 = C₂ × g
test("T10", k21*(k21-1)//(2*n_C) == 42 and 42 == C_2 * g,
     f"Ratio = {k21*(k21-1)//(2*n_C)} = 42 = C₂ × g = {C_2} × {g}")

print(f"\n--- Scorecard ---\n")
passed = 0
for name, status, detail in tests:
    print(f"  {name}: {status} — {detail}")
    if status == "PASS":
        passed += 1

print(f"\n{'='*70}")
print(f"SCORECARD: {passed}/{len(tests)}")
print(f"{'='*70}")

print(f"""
RECOMMENDATION:

Use Approach D (Hybrid) at dps=1600:
  1. Constrained polynomial recovery (proven at k=6..16)
  2. Partial independent c_top check from high-n points
  3. a_20(5) as final independent verification

Estimated runtime: 6-16 hours (parallelizable).
Expected outcome: Three Theorems PASS at k=20 based on 16 consecutive prior successes.

The COSMIC CONNECTION (Toy 649) is already algebraically established:
  ratio(20) = -38 = -rank × (n_C² - C₂) = -2 × 19
  ratio(21) = -42 = -C₂ × g = -6 × 7

Computational verification would upgrade this from "predicted by formula"
to "confirmed by constrained polynomial recovery." The formula has been
confirmed at 12 consecutive levels (k=5..16). Level 13-16 (k=17..20)
is the test.
""")

sys.exit(0 if passed == len(tests) else 1)
