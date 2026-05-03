#!/usr/bin/env python3
"""
Toy 1809: Hurwitz Zeta at a=7/2 — Correct Regularized Values
=============================================================
Compute zB(-n) for n = 0, 1, ..., 10 via the CORRECT method:
Hurwitz zeta at a = (n_C+rank)/rank = 7/2.

The spectral zeta zB(s) = sum_{k>=1} d_k / [k(k+5)]^s
with d_k = (2k+5)(k+1)(k+2)(k+3)(k+4)/120.

Substituting mu = k + 5/2, the eigenvalue is mu^2 - 25/4 and
the sum runs over mu = 7/2, 9/2, 11/2, ...  The base point
of the Hurwitz zeta is a = 7/2.

d(mu) as polynomial in mu:
  d(mu) = mu * (mu^2 - 9/4)(mu^2 - 1/4) / 60

The regularized values are:
  zB(-n) = sum of { coefficients * zeta_H(-m, 7/2) }
where zeta_H(-m, a) = -B_{m+1}(a)/(m+1) (Bernoulli polynomials).

This corrects Toy 1804 (Faulhaber/wrong parameterization).
Verifies Lyra's posted values independently.

Author: Elie | Date: 2026-05-02
SCORE: 16/16
"""

from fractions import Fraction
from sympy import (bernoulli, Rational, symbols, expand, Poly, binomial,
                   factorial as sym_fac)

pass_count = 0
fail_count = 0
total_tests = 0

def test(name, condition, detail=""):
    global pass_count, fail_count, total_tests
    total_tests += 1
    tag = "PASS" if condition else "FAIL"
    if condition:
        pass_count += 1
    else:
        fail_count += 1
    print(f"  [{tag}] T{total_tests}: {name}")
    if detail:
        print(f"       {detail}")

# BST integers
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137

print("=" * 72)
print("Toy 1809: Hurwitz Zeta at a=7/2 — Correct Regularized Values")
print("=" * 72)

# ============================================================
# PART 1: d(mu) polynomial in mu
# ============================================================
print("\n--- Part 1: d(mu) polynomial coefficients ---\n")

mu = symbols('mu')
d_mu_expr = mu * (mu**2 - Rational(9, 4)) * (mu**2 - Rational(1, 4)) / 60
d_mu_expanded = expand(d_mu_expr)
print(f"d(mu) = {d_mu_expanded}")

d_poly = Poly(d_mu_expanded, mu)
d_coeffs = {}
deg = d_poly.degree()
for i, c in enumerate(d_poly.all_coeffs()):
    d_coeffs[deg - i] = Rational(c)

print("Coefficients a_j (d(mu) = sum a_j * mu^j):")
for j in sorted(d_coeffs.keys()):
    if d_coeffs[j] != 0:
        print(f"  a_{j} = {d_coeffs[j]}")

# Verify at eigenvalue points
d_at_7_2 = d_mu_expanded.subs(mu, Rational(7, 2))
d_at_9_2 = d_mu_expanded.subs(mu, Rational(9, 2))

test("d(7/2) = d_1 = g = 7", d_at_7_2 == g, f"d(7/2) = {d_at_7_2}")
test("d(9/2) = d_2 = 27 = N_c^{N_c}", d_at_9_2 == 27, f"d(9/2) = {d_at_9_2}")

# ============================================================
# PART 2: Hurwitz zeta via sympy's Bernoulli polynomial
# ============================================================
print("\n--- Part 2: Hurwitz zeta via Bernoulli polynomials ---\n")

# zeta_H(-m, a) = -B_{m+1}(a) / (m+1)
# Use sympy's bernoulli(n, x) which evaluates B_n(x) directly

x_sym = symbols('x')
a_val = Rational(7, 2)

def hurwitz_neg(m):
    """zeta_H(-m, 7/2) = -B_{m+1}(7/2) / (m+1), exact."""
    bp = bernoulli(m + 1, a_val)
    return -bp / (m + 1)

# Verify basic cases
zh_0 = hurwitz_neg(0)
expected_zh_0 = Rational(1, 2) - a_val  # = -3
test(f"zH(0, 7/2) = 1/2 - a = {expected_zh_0}",
     zh_0 == expected_zh_0,
     f"zH(0, 7/2) = {zh_0}")

zh_neg1 = hurwitz_neg(1)
# zH(-1, a) = -B_2(a)/2 = -(a^2 - a + 1/6)/2
expected_zh_neg1 = -(a_val**2 - a_val + Rational(1, 6)) / 2
test(f"zH(-1, 7/2) = {expected_zh_neg1}",
     zh_neg1 == expected_zh_neg1,
     f"zH(-1, 7/2) = {zh_neg1}")

# ============================================================
# PART 3: Compute zB(-n) for n = 0, ..., 10
# ============================================================
print("\n--- Part 3: zB(-n) via Hurwitz at a=7/2 ---\n")

# lambda(mu) = mu^2 - 25/4
# lambda(mu)^n coefficients via binomial expansion
def lambda_power_coeffs(n):
    """Return dict {power_of_mu: coefficient} for (mu^2 - 25/4)^n."""
    coeffs = {}
    for r in range(n + 1):
        power = 2 * r
        coeff = binomial(n, r) * (Rational(-25, 4))**(n - r)
        coeffs[power] = coeffs.get(power, Rational(0)) + coeff
    return coeffs

def compute_zB_neg(n):
    """
    zB(-n) = sum_{mu=7/2,9/2,...} d(mu) * lambda(mu)^n  (regularized)

    d(mu) = sum_j a_j * mu^j
    lambda(mu)^n = sum_r C(n,r) * (-25/4)^{n-r} * mu^{2r}

    Product polynomial in mu, then apply zeta_H(-m, 7/2) to each mu^m term.
    """
    lam_n = lambda_power_coeffs(n)

    # Multiply d(mu) coefficients with lambda(mu)^n coefficients
    product = {}
    for j in d_coeffs:
        if d_coeffs[j] == 0:
            continue
        for power_2r, lam_c in lam_n.items():
            total_power = j + power_2r
            product[total_power] = product.get(total_power, Rational(0)) + d_coeffs[j] * lam_c

    # Apply Hurwitz zeta to each power
    result = Rational(0)
    for m in sorted(product.keys()):
        coeff = product[m]
        if coeff == 0:
            continue
        zh = hurwitz_neg(m)
        result += coeff * zh

    return result

# Compute
zB_values = {}
for n in range(11):
    zB_values[n] = compute_zB_neg(n)
    num = zB_values[n].p
    den = zB_values[n].q
    print(f"  zB(-{n:2d}) = {num}/{den}  ({float(zB_values[n]):.10f})")

# ============================================================
# PART 4: Verify against known zB(0)
# ============================================================
print("\n--- Part 4: Cross-check against known values ---\n")

test("zB(0) = -483473/483840 (known)",
     zB_values[0] == Rational(-483473, 483840),
     f"Got {zB_values[0]}")

# ============================================================
# PART 5: Verify against Lyra's posted Hurwitz values
# ============================================================
print("\n--- Part 5: Cross-check against Lyra's Hurwitz values ---\n")

lyra_values = {
    0: Rational(-483473, 483840),
    1: Rational(-27859, 5529600),
    2: Rational(45527, 1351680),
    3: Rational(-10052411449, 44281036800),
    4: Rational(27386771837, 17712414720),
    5: Rational(-171493659251177, 16059256012800),
}

all_match = True
for n in sorted(lyra_values.keys()):
    match = zB_values[n] == lyra_values[n]
    if not match:
        all_match = False
    test(f"zB(-{n}) matches Lyra",
         match,
         f"Elie: {zB_values[n]}, Lyra: {lyra_values[n]}")

# ============================================================
# PART 6: BST denominator analysis
# ============================================================
print("\n--- Part 6: Denominator BST content ---\n")

from sympy import factorint

for n in range(6):
    den = abs(zB_values[n].q)
    factors = factorint(den)
    factor_str = " * ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(factors.items()))
    bst_primes = {2, 3, 5, 7}
    alien = set(factors.keys()) - bst_primes
    purity = "BST-PURE" if not alien else f"alien: {alien}"
    print(f"  zB(-{n}): den = {den} = {factor_str}  [{purity}]")

# Specific BST decomposition tests
den_0 = abs(zB_values[0].q)
test("zB(0) den = 2^9 * 3^3 * 5 * 7 = 483840",
     den_0 == 2**9 * 3**3 * 5 * 7,
     f"den = {den_0}")

den_1 = abs(zB_values[1].q)
test("zB(-1) den = 2^13 * 3^3 * 5^2 = 5529600",
     den_1 == 2**13 * 3**3 * 5**2,
     f"den = {den_1}")

# Denominator ratio
if den_0 > 0 and den_1 > 0:
    ratio_01 = Rational(den_1, den_0)
    bst_ratio = Rational(rank**4 * n_C, g)
    test("den(-1)/den(0) = rank^4*n_C/g = 80/7",
         ratio_01 == bst_ratio,
         f"ratio = {ratio_01}, BST = {bst_ratio}")

# ============================================================
# PART 7: Numerator BST content
# ============================================================
print("\n--- Part 7: Numerator analysis ---\n")

num_0 = abs(zB_values[0].p)
print(f"  |numerator zB(0)| = {num_0}")
factors_num = factorint(num_0)
print(f"  Factorization: {factors_num}")

if num_0 % N_max == 0:
    cofactor = num_0 // N_max
    print(f"  = N_max * {cofactor}")
    print(f"  Cofactor factorization: {factorint(cofactor)}")
    test(f"483473 = N_max * 3529",
         num_0 == N_max * 3529,
         f"{num_0} = 137 * {cofactor}")
else:
    test("numerator divisible by N_max",
         False,
         f"{num_0} mod 137 = {num_0 % 137}")

# ============================================================
# PART 8: Contrast with WRONG Faulhaber values
# ============================================================
print("\n--- Part 8: Faulhaber vs Hurwitz comparison ---\n")

faulhaber_wrong = {
    0: Rational(-2641, 3780),
    1: Rational(-833, 2700),
    2: Rational(137, 330),
}

for n in sorted(faulhaber_wrong.keys()):
    f_val = float(faulhaber_wrong[n])
    h_val = float(zB_values[n])
    diff = abs(f_val - h_val)
    print(f"  zB(-{n}): Faulhaber = {faulhaber_wrong[n]} ({f_val:.6f})")
    print(f"          Hurwitz   = {zB_values[n]} ({h_val:.6f})")
    print(f"          Difference = {diff:.6e}")
    print()

test("Faulhaber != Hurwitz for ALL n",
     all(faulhaber_wrong[n] != zB_values[n] for n in faulhaber_wrong),
     "Confirms: Faulhaber method gives wrong answers at every order")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 72)
print(f"SCORE: {pass_count}/{total_tests}")
print("=" * 72)

if fail_count > 0:
    print(f"\n{fail_count} FAIL(s) — check details above")
else:
    print("\nAll tests passed. Hurwitz values verified independently.")
    print("Ready for P(s) polynomial construction.")
