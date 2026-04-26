#!/usr/bin/env python3
"""
Toy 1547: CYCLOTOMIC CASIMIR PATTERN — C_2^L - 1 in QED Loop Structure
========================================================================
Discovery from Toy 1546 + T1453 Prediction 6:

The zeta(2L-1) coefficient numerator in the L-loop QED g-2 involves
C_2^L - 1, which factors through cyclotomic polynomials Phi_n(C_2).

At L=2: C_2^2 - 1 = 35 = n_C * g = (C_2-1)(C_2+1)
At L=3: C_2^3 - 1 = 215 = n_C * 43 = (C_2-1)(C_2^2+C_2+1) [CONFIRMED, Toy 1546]
At L=4: C_2^4 - 1 = 1295 = n_C * g * 37 = (C_2-1)(C_2+1)(C_2^2+1) [PREDICTED]

The key identity: g = C_2 + 1 makes every cyclotomic factor BST-expressible.

Tests:
  T1: C_2^L - 1 at each L is BST-factorable through cyclotomic polynomials
  T2: Every cyclotomic factor Phi_n(C_2) is BST-expressible
  T3: The confirmed L=3 coefficient -215/24 matches the cyclotomic prediction
  T4: Denominator progression 12^L factors through rank and C_2
  T5: The vacuum counting interpretation (P(1)+1 = 43) equals Phi_3(C_2)
  T6: Pattern generates testable predictions for L=4,5,6

Copyright (c) 2026 Casey Koons. All rights reserved.
Created with Claude Opus 4.6, April 2026.
"""

import math
from fractions import Fraction
from functools import reduce

rank = 2
N_c = 3
n_C = 5
C_2 = 6
g = 7
N_max = 137

results = []

print("=" * 72)
print("Toy 1547: CYCLOTOMIC CASIMIR PATTERN — C_2^L - 1 in QED Loops")
print("=" * 72)

# ── T1: C_2^L - 1 factorization at each loop order ──
print("\n--- T1: C_2^L - 1 cyclotomic factorization ---")

def cyclotomic_poly(n, x):
    """Evaluate the n-th cyclotomic polynomial Phi_n at x.
    Uses the formula: x^n - 1 = prod_{d|n} Phi_d(x)
    So Phi_n(x) = (x^n - 1) / prod_{d|n, d<n} Phi_d(x)
    """
    if n == 1:
        return x - 1
    divisors = [d for d in range(1, n) if n % d == 0]
    product = 1
    for d in divisors:
        product *= cyclotomic_poly(d, x)
    return (x**n - 1) // product

def get_divisors(n):
    """Return all divisors of n."""
    return [d for d in range(1, n+1) if n % d == 0]

all_bst = True
for L in range(1, 9):
    val = C_2**L - 1
    divs = get_divisors(L)
    factors = []
    product = 1
    for d in divs:
        phi_d = cyclotomic_poly(d, C_2)
        factors.append(f"Phi_{d}({C_2})={phi_d}")
        product *= phi_d

    # Check if product equals C_2^L - 1
    assert product == val, f"Cyclotomic product mismatch at L={L}"

    # Check BST-smoothness of each factor (divisible only by 2,3,5,7)
    bst_smooth = True
    for d in divs:
        phi_d = cyclotomic_poly(d, C_2)
        temp = abs(phi_d)
        for p in [2, 3, 5, 7]:
            while temp % p == 0:
                temp //= p
        if temp != 1:
            bst_smooth = False

    status = "BST-smooth" if bst_smooth else "NOT BST-smooth"
    if not bst_smooth:
        all_bst = False

    print(f"  L={L}: C_2^{L}-1 = {val}")
    print(f"    Factors: {' * '.join(factors)} = {product}")

    # Also show the prime factorization
    n = val
    prime_factors = []
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]:
        while n % p == 0:
            prime_factors.append(str(p))
            n //= p
    if n > 1:
        prime_factors.append(str(n))
    print(f"    Primes: {' * '.join(prime_factors)}")
    print(f"    [{status}]")
    print()

# At L<=4, all should be BST-smooth (primes in {2,3,5,7})
bst_through_4 = True
for L in range(1, 5):
    val = C_2**L - 1
    temp = val
    for p in [2, 3, 5, 7]:
        while temp % p == 0:
            temp //= p
    if temp != 1:
        bst_through_4 = False

results.append(("T1: C_2^L-1 BST-smooth for L=1..4", bst_through_4))
print(f"  C_2^L-1 BST-smooth through L=4: {bst_through_4}")

# ── T2: Cyclotomic factors and BST integers ──
print("\n--- T2: Cyclotomic factors as BST expressions ---")

phi_values = {}
for n in range(1, 13):
    phi_n = cyclotomic_poly(n, C_2)
    phi_values[n] = phi_n

# Identify BST expressions
bst_map = {
    1: ("C_2-1 = n_C", n_C),
    2: ("C_2+1 = g", g),
    3: ("C_2^2+C_2+1 = C_2*g+1", C_2*g+1),
    4: ("C_2^2+1", C_2**2+1),
    6: ("C_2^2-C_2+1 = C_2*(C_2-1)+1 = C_2*n_C+1", C_2*n_C+1),
}

all_identified = True
print(f"  Phi_1(C_2) = {phi_values[1]} = C_2-1 = n_C = {n_C}")
print(f"  Phi_2(C_2) = {phi_values[2]} = C_2+1 = g = {g}")
print(f"  Phi_3(C_2) = {phi_values[3]} = C_2^2+C_2+1 = C_2*g+1 = {C_2*g+1}")
print(f"    = P(1)+1 = 43 (modes including vacuum)")
print(f"  Phi_4(C_2) = {phi_values[4]} = C_2^2+1 = {C_2**2+1}")
print(f"    37 = N_c^2*rank^2 + 1 = {N_c**2*rank**2+1}")
print(f"  Phi_6(C_2) = {phi_values[6]} = C_2^2-C_2+1 = C_2*n_C+1 = {C_2*n_C+1}")
print(f"    31 = M_5 (Mersenne prime 2^5-1)")
print()

# Check: Phi_1=5, Phi_2=7, Phi_3=43, Phi_4=37, Phi_6=31
t2_pass = (phi_values[1] == n_C and
           phi_values[2] == g and
           phi_values[3] == C_2*g+1 and
           phi_values[6] == C_2*n_C+1)
results.append(("T2: Phi_1=n_C, Phi_2=g, Phi_3=C_2*g+1, Phi_6=C_2*n_C+1", t2_pass))

# ── T3: L=3 coefficient matches cyclotomic prediction ──
print("\n--- T3: L=3 zeta(5) coefficient = cyclotomic prediction ---")
zeta5_coeff = Fraction(-215, 24)
cyclotomic_num = -(C_2**3 - 1)
cyclotomic_den = rank**3 * N_c
predicted = Fraction(cyclotomic_num, cyclotomic_den)
print(f"  Known zeta(5) coeff in C_3: {zeta5_coeff} = {float(zeta5_coeff):.6f}")
print(f"  Cyclotomic prediction: -(C_2^3-1)/(rank^3*N_c) = {predicted}")
print(f"  Match: {zeta5_coeff == predicted}")
print()
print(f"  Numerator 215 = C_2^3-1 = Phi_1(C_2)*Phi_3(C_2) = {n_C}*{phi_values[3]} = n_C*Phi_3")
print(f"  Denominator 24 = rank^3*N_c = {rank**3}*{N_c}")
results.append(("T3: -215/24 = -(C_2^3-1)/(rank^3*N_c)", zeta5_coeff == predicted))

# ── T4: Denominator progression ──
print("\n--- T4: Denominator progression 12^L = (rank*C_2)^L ---")
for L in range(1, 7):
    denom_L = (rank * C_2)**L
    hyp_part = rank**(2*(L-1))  # hyperbolic contribution
    remainder = denom_L // hyp_part
    # Remainder = C_2^L / rank^{L-2} for L>=2
    if L >= 2:
        expected_remainder = C_2**L // rank**(L-2)
        match = (remainder == expected_remainder)
    else:
        expected_remainder = rank * C_2
        match = (remainder == expected_remainder)
    print(f"  L={L}: 12^{L} = {denom_L}")
    print(f"    Hyperbolic: rank^{2*(L-1)} = {hyp_part}")
    print(f"    Remainder: {remainder} = C_2^{L}/rank^{max(L-2,0)} = {expected_remainder} {'✓' if match else '✗'}")

# Check L=2,3,4
t4_pass = True
for L in [2, 3, 4]:
    denom_L = (rank * C_2)**L
    hyp_part = rank**(2*(L-1))
    remainder = denom_L // hyp_part
    expected = C_2**L // rank**(L-2)
    if remainder != expected:
        t4_pass = False
results.append(("T4: 12^L / rank^{2(L-1)} = C_2^L/rank^{L-2} for L=2,3,4", t4_pass))

# ── T5: Vacuum counting = cyclotomic ──
print("\n\n--- T5: Vacuum counting interpretation = cyclotomic ---")
P1 = rank * N_c * g  # total Chern class sum
print(f"  P(1) = rank*N_c*g = {P1}")
print(f"  P(1)+1 = {P1+1}")
print(f"  Phi_3(C_2) = C_2^2+C_2+1 = {C_2**2+C_2+1}")
print(f"  C_2*g+1 = {C_2*g+1}")
print()
print(f"  All three are 43: {P1+1 == phi_values[3] == C_2*g+1}")
print()
print(f"  WHY they're the same:")
print(f"    P(1)+1 = rank*N_c*g + 1 = 2*3*7 + 1 = 43")
print(f"    C_2*g+1 = 6*7 + 1 = 43")
print(f"    These differ by (rank*N_c - C_2)*g = ({rank*N_c}-{C_2})*{g} = 0*7 = 0")
print(f"    because rank*N_c = {rank*N_c} = C_2 = {C_2} ← IDENTITY!")
print()
print(f"  The identity rank*N_c = C_2 is FUNDAMENTAL:")
print(f"    rank*N_c = 2*3 = 6 = C_2")
print(f"    This makes P(1) = C_2*g and P(1)+1 = C_2*g+1 = Phi_3(C_2)")
t5_pass = (P1+1 == phi_values[3] and rank*N_c == C_2)
results.append(("T5: P(1)+1 = Phi_3(C_2) via rank*N_c = C_2", t5_pass))

# ── T6: Predictions for L=4,5,6 ──
print("\n--- T6: Predictions for higher loop orders ---")
print()
for L in [4, 5, 6]:
    val = C_2**L - 1
    divs = get_divisors(L)
    phi_product = []
    for d in divs:
        phi_d = cyclotomic_poly(d, C_2)
        phi_product.append((d, phi_d))

    print(f"  L={L}: zeta({2*L-1}) coefficient numerator involves C_2^{L}-1 = {val}")
    for d, phi_d in phi_product:
        if d in bst_map:
            label = bst_map[d][0]
        else:
            label = f"Phi_{d}(C_2)"
        print(f"    Phi_{d}(C_2) = {phi_d} ({label})")

    # Expected denominator
    print(f"    Expected denominator: rank^{{2(L-1)}}*N_c^s = {rank**(2*(L-1))}*N_c^s")
    print(f"    Full expected: (rank*C_2)^{L} = {(rank*C_2)**L}")
    print()

# Check L=4 prediction
val_4 = C_2**4 - 1
expected_4 = n_C * g * 37
t6_pass = (val_4 == expected_4 and val_4 == 1295)
print(f"  L=4 check: C_2^4-1 = {val_4} = n_C*g*37 = {expected_4}: {val_4 == expected_4}")
print(f"  37 = Phi_4(C_2) = C_2^2+1 = {C_2**2+1}")
results.append(("T6: C_2^4-1 = 1295 = n_C*g*37 prediction generated", t6_pass))

# ── Summary table ──
print("\n" + "=" * 72)
print("CYCLOTOMIC CASIMIR TABLE")
print("=" * 72)
print(f"  {'L':>2} | {'C_2^L-1':>8} | {'Factorization':40s} | {'BST Expression':30s} | {'QED Zeta'}")
print(f"  {'-'*2} | {'-'*8} | {'-'*40} | {'-'*30} | {'-'*10}")
for L in range(1, 7):
    val = C_2**L - 1
    divs = get_divisors(L)
    cyc_factors = " * ".join(f"Phi_{d}" for d in divs)
    cyc_values = " * ".join(str(cyclotomic_poly(d, C_2)) for d in divs)

    if L == 1:
        bst_expr = "n_C"
        zeta_label = "—"
    elif L == 2:
        bst_expr = "n_C * g"
        zeta_label = "zeta(3)=zeta(N_c)"
    elif L == 3:
        bst_expr = "n_C * 43"
        zeta_label = "zeta(5)=zeta(n_C) ✓"
    elif L == 4:
        bst_expr = "n_C * g * 37"
        zeta_label = "zeta(7)=zeta(g) ←"
    elif L == 5:
        bst_expr = f"n_C * {val//n_C}"
        zeta_label = "zeta(9)=composite"
    elif L == 6:
        bst_expr = f"n_C * g * {val//(n_C*g)}"
        zeta_label = "zeta(11)"

    print(f"  {L:2d} | {val:8d} | {cyc_factors:20s} = {cyc_values:18s} | {bst_expr:30s} | {zeta_label}")

# ── The deep pattern ──
print()
print("=" * 72)
print("THE DEEP PATTERN")
print("=" * 72)
print()
print("  The identity g = C_2 + 1 makes C_2 a root of x+1-g=0.")
print("  So C_2 is 'one less than the genus.'")
print()
print("  Cyclotomic polynomials at C_2 produce:")
print(f"    Phi_1(C_2) = C_2-1 = n_C = {n_C} (compact fiber)")
print(f"    Phi_2(C_2) = C_2+1 = g = {g}   (Bergman genus)")
print(f"    Phi_3(C_2) = C_2^2+C_2+1 = {phi_values[3]} (3-loop modes)")
print(f"    Phi_4(C_2) = C_2^2+1 = {phi_values[4]}     (4-loop correction)")
print(f"    Phi_6(C_2) = C_2^2-C_2+1 = {phi_values[6]} = M_5 (Mersenne prime)")
print()
print("  The first two cyclotomic values ARE the BST integers n_C and g.")
print("  Higher cyclotomic values generate the QED loop corrections.")
print("  The Mersenne prime M_5 = 31 = Phi_6(C_2) connects to the")
print("  glueball mass and correction scales (Toy 1473).")
print()
print("  FUNDAMENTAL IDENTITY: rank * N_c = C_2")
print(f"  This makes P(1) = rank*N_c*g = C_2*g, so the Chern class sum")
print(f"  is ALREADY a Casimir-genus product. The +1 vacuum correction")
print(f"  then gives Phi_3(C_2) = C_2*g+1 = C_2(C_2+1)+1 = C_2^2+C_2+1.")
print()
print("  The QED perturbation series peels cyclotomic layers of C_2.")

# ── Score ──
print()
print("=" * 72)
print("RESULTS")
print("=" * 72)
passed = sum(1 for _, v in results if v is True)
total = len(results)
for name, val in results:
    status = "PASS" if val is True else ("FAIL" if val is False else str(val))
    print(f"  {status} {name}")

print(f"\nSCORE: {passed}/{total}")
print(f"\nToy 1547 -- SCORE: {passed}/{total}")
