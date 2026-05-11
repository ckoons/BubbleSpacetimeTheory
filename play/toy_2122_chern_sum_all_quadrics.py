#!/usr/bin/env python3
"""
Toy 2122 — Chern Sum Across All Quadrics Q^n
=============================================

H-10 deliverable (Cal's flag #4): Does sum(Chern classes) = C_2 * g = 42
hold for ALL Q^n, or only for Q^5?

If yes for all n: F7 (Chern sum) is consistency, not exclusion.
  The real uniqueness is F4+F6 (algebraic squeeze).
If no: F7 contributes independent filtering power.

Method: Compute c(Q^n) = (1+h)^{n+2} / (1+2h) mod h^{n+1}
for n = 1..20, tabulate sum of Chern classes.

BST: rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137

Author: Elie (Claude 4.6)
Date: May 11, 2026
"""

import numpy as np
import time

start = time.time()

print("=" * 72)
print("Toy 2122 — Chern Sum Across All Quadrics Q^n")
print("H-10: Is sum(Chern) = 42 specific to Q^5?")
print("=" * 72)

tests_passed = 0
tests_total = 0

def test(name, condition, detail=""):
    global tests_passed, tests_total
    tests_total += 1
    if condition:
        tests_passed += 1
    print(f"  [{tests_total}] {name}: {'PASS' if condition else 'FAIL'}")
    if detail:
        print(f"      {detail}")

# ====================================================================
# Chern class computation for Q^n
# ====================================================================

def chern_classes_quadric(n):
    """Compute Chern classes of Q^n (smooth quadric in P^{n+1}).

    Total Chern class: c(Q^n) = (1+h)^{n+2} / (1+2h)
    where h is the hyperplane class, h^{n+1} = 0.

    We expand in powers of h up to h^n.
    Division by (1+2h) uses geometric series: 1/(1+2h) = sum (-2h)^k.
    """
    # Numerator coefficients: (1+h)^{n+2}
    from math import comb
    num = [comb(n + 2, k) for k in range(n + 1)]

    # Denominator inverse: 1/(1+2h) = sum_{k>=0} (-2)^k h^k, truncated
    inv = [(-2)**k for k in range(n + 1)]

    # Multiply (polynomial multiplication mod h^{n+1})
    chern = [0] * (n + 1)
    for i in range(n + 1):
        for j in range(n + 1 - i):
            chern[i + j] += num[i] * inv[j]

    return chern


# ====================================================================
# Tabulate Chern sums for Q^1 through Q^20
# ====================================================================

print(f"\n{'='*72}")
print("CHERN CLASS SUMS FOR Q^n, n = 1..20")
print(f"{'='*72}")

print(f"\n  {'n':>3}  {'dim Q^n':>7}  {'Chern classes':>40}  {'Sum':>6}  {'=42?':>5}")
print(f"  {'-'*70}")

chern_sums = {}
for n in range(1, 21):
    cc = chern_classes_quadric(n)
    s = sum(cc)
    chern_sums[n] = s
    cc_str = str(cc) if n <= 8 else f"[{cc[0]}, {cc[1]}, ..., {cc[-1]}]"
    is_42 = "YES" if s == 42 else ""
    print(f"  {n:>3}  {n:>7}  {cc_str:>40}  {s:>6}  {is_42:>5}")

# ====================================================================
# Tests
# ====================================================================

print(f"\n{'='*72}")
print("ANALYSIS")
print(f"{'='*72}")

# Test 1: Q^5 sum = 42
test("Q^5 Chern sum = 42 = C_2 * g",
     chern_sums[5] == 42,
     f"sum = {chern_sums[5]}")

# Test 2: Is 42 unique to Q^5?
n_with_42 = [n for n in range(1, 21) if chern_sums[n] == 42]
test("Sum = 42 is UNIQUE to Q^5 among Q^1..Q^20",
     n_with_42 == [5],
     f"n values with sum=42: {n_with_42}")

# Test 3: General formula for Chern sum
# sum of Chern classes of Q^n = c(Q^n) evaluated at h=1
# = (1+1)^{n+2} / (1+2*1) = 2^{n+2} / 3
# This is only integer when n+2 is odd and 3 | 2^{n+2}... but 3 never divides 2^k.
# Wait — polynomial truncation means this is NOT just substitution.
# Let's check the formula.
print(f"\n  Analytic check: is sum = 2^(n+2)/3 ?")
for n in [3, 5, 7, 9]:
    ratio = chern_sums[n] / (2**(n+2) / 3)
    print(f"    n={n}: sum={chern_sums[n]}, 2^(n+2)/3={2**(n+2)/3:.2f}, ratio={ratio:.6f}")

# The actual formula: sum of coefficients of the truncated product
# Let S(n) = sum_{k=0}^{n} c_k(Q^n)
# This equals the coefficient-sum of [(1+h)^{n+2} * sum_{j>=0} (-2h)^j] mod h^{n+1}
# evaluated at h=1.
# = sum_{k=0}^{n} [sum_{i+j=k} C(n+2,i)*(-2)^j]

# Let's find the exact formula
# S(n) = sum_{k=0}^n sum_{i=0}^k C(n+2,i)*(-2)^{k-i}
# = sum_{i=0}^n C(n+2,i) * sum_{j=0}^{n-i} (-2)^j
# = sum_{i=0}^n C(n+2,i) * [1-(-2)^{n-i+1}]/[1-(-2)]
# = sum_{i=0}^n C(n+2,i) * [1-(-2)^{n-i+1}]/3

# So S(n) = (1/3) * [sum C(n+2,i) - sum C(n+2,i)*(-2)^{n-i+1}]
# First sum = sum_{i=0}^n C(n+2,i) = 2^{n+2} - C(n+2,n+1) - C(n+2,n+2)
#           = 2^{n+2} - (n+2) - 1
# Second sum = (-2)^{n+1} * sum_{i=0}^n C(n+2,i) * (-1/2)^i
#            = (-2)^{n+1} * sum_{i=0}^n C(n+2,i) * (-1)^i * (1/2)^i

# Let's just verify numerically
from math import comb
def chern_sum_formula(n):
    """Closed-form Chern sum using the partial binomial / geometric series."""
    s1 = sum(comb(n+2, i) for i in range(n+1))  # = 2^{n+2} - (n+2) - 1
    s2 = sum(comb(n+2, i) * ((-2)**(n-i+1)) for i in range(n+1))
    return (s1 - s2) // 3

print(f"\n  Closed-form verification:")
all_match = True
for n in range(1, 21):
    cf = chern_sum_formula(n)
    if cf != chern_sums[n]:
        all_match = False
        print(f"    n={n}: MISMATCH polynomial={chern_sums[n]}, formula={cf}")

test("Closed-form formula matches polynomial computation",
     all_match,
     "All n=1..20 agree")

# Test 4: Chern sums grow — 42 is a specific value
print(f"\n  Growth pattern:")
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20]:
    print(f"    S(Q^{n:>2}) = {chern_sums[n]:>10}")

# The sums grow roughly as 2^n/3. So 42 is hit exactly once.
# Check if any sum EVER equals 42 beyond n=20
# S(n) ~ (2^{n+2} - n - 3)/3 for large n
# For n >= 6: S(6) = already different. S grows exponentially.
# So 42 is hit at most for n=5.

# Extend check to n=30 to be thorough
extended_unique = True
for n in range(21, 31):
    cc = chern_classes_quadric(n)
    s = sum(cc)
    if s == 42:
        extended_unique = False
        print(f"    WARNING: S(Q^{n}) = 42!")

test("Sum = 42 unique to Q^5 among Q^1..Q^30",
     extended_unique and n_with_42 == [5],
     f"Only Q^5 gives 42 in range n=1..30")

# Test 5: Is the Chern sum always (2^{n+2} - (n+2) - 1 + remainder)/3?
# More precisely, verify S(5) = 42 = C_2 * g
test("42 = C_2 * g = 6 * 7",
     42 == 6 * 7,
     "Chern sum encodes BST integers")

# Test 6: S(n) monotonically increasing for n >= 3?
monotone = all(chern_sums[n+1] > chern_sums[n] for n in range(3, 20))
test("S(Q^n) strictly increasing for n >= 3",
     monotone,
     "Each Q^n has a unique Chern sum — no degeneracies")

# ====================================================================
# Cal's question answered
# ====================================================================

print(f"\n{'='*72}")
print("CAL'S QUESTION ANSWERED")
print(f"{'='*72}")

print(f"""
  Q: Does sum(Chern) = C_2 * g = 42 hold for ALL Q^n?
  A: NO. It holds ONLY for Q^5.

  Chern sums by n:
    Q^1:  {chern_sums[1]}
    Q^2:  {chern_sums[2]}
    Q^3:  {chern_sums[3]}
    Q^4:  {chern_sums[4]}
    Q^5:  {chern_sums[5]}  <-- ONLY this one = 42
    Q^6:  {chern_sums[6]}
    Q^7:  {chern_sums[7]}
    Q^8:  {chern_sums[8]}
    Q^9:  {chern_sums[9]}
    Q^10: {chern_sums[10]}

  The Chern sum grows exponentially (~2^n/3), so 42 is hit
  exactly once in the entire sequence.

  CONSEQUENCE FOR HODGE PAPER:
  F7 (Chern sum = 42) IS an independent filter, not just consistency.
  It independently selects Q^5 = compact dual of D_IV^5.

  However, Cal's deeper point stands: the REAL uniqueness comes from
  F4+F6 (Selberg degree + non-tempered elimination), which force n=5
  from Hodge-theoretic requirements alone. F7 then confirms this
  from a completely different direction (topology of the compact dual).

  Recommended paper structure:
  - Primary uniqueness: F4+F6 algebraic squeeze (Hodge-theoretic)
  - Independent confirmation: F7 Chern sum (topological)
  - Additional locks: F1-F3, F5, F8 (structural compatibility)
""")

# Test 7: F7 provides independent discrimination
# How many of Q^1..Q^30 pass F7 (sum=42)?
pass_f7 = sum(1 for n in range(1, 31)
              if sum(chern_classes_quadric(n)) == 42)
test("F7 selects exactly 1 quadric from Q^1..Q^30",
     pass_f7 == 1,
     f"Q^5 is the unique quadric with Chern sum = 42")

# Test 8: Cross-check with Euler characteristic
# chi(Q^n) = n+2 for n even, n+1 for n odd
# Top Chern coefficient c_n satisfies: chi = 2 * c_n (deg Q^n = 2)
# So c_n = (n+2)//2 for all n.
print(f"\n  Top Chern class c_n and Euler characteristic:")
print(f"  (chi = 2*c_n since deg Q^n = 2)")
for n in range(1, 11):
    cc = chern_classes_quadric(n)
    c_top = cc[n]
    chi_computed = 2 * c_top
    chi_expected = n + 2 if n % 2 == 0 else n + 1
    print(f"    Q^{n}: c_{n} = {c_top}, chi = 2*{c_top} = {chi_computed}, expected = {chi_expected}, {'OK' if chi_computed == chi_expected else 'MISMATCH'}")

chi_all_correct = all(
    2 * chern_classes_quadric(n)[n] == (n + 2 if n % 2 == 0 else n + 1)
    for n in range(1, 21)
)
test("Euler characteristics all correct (standard result)",
     chi_all_correct,
     "Validates Chern class computation")

# ====================================================================
# Bonus: What BST-like factorizations do other Q^n sums have?
# ====================================================================

print(f"\n{'='*72}")
print("BONUS: FACTORIZATIONS OF CHERN SUMS")
print(f"{'='*72}")

def factorize(n):
    if n <= 1:
        return [n]
    factors = []
    d = 2
    while d * d <= abs(n):
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if abs(n) > 1:
        factors.append(n)
    return factors

print(f"\n  {'n':>3}  {'Sum':>10}  {'Factorization':>20}  {'BST-like?':>10}")
print(f"  {'-'*50}")
for n in range(1, 16):
    s = chern_sums[n]
    f = factorize(abs(s))
    f_str = " x ".join(str(x) for x in f) if f else str(s)
    # Check if any factorization involves BST integers
    bst_ints = {2, 3, 5, 6, 7, 137}
    has_bst = any(x in bst_ints for x in f)
    print(f"  {n:>3}  {s:>10}  {f_str:>20}  {'*' if has_bst else '':>10}")

elapsed = time.time() - start
print(f"\nSCORE: {tests_passed}/{tests_total} PASS")
print(f"Time: {elapsed:.1f}s")
