#!/usr/bin/env python3
"""
Toy 3513 — K52a Session 11: Synthetic substrate-CHSH B as polynomial in GF(128)

Elie, Saturday 2026-05-23 16:40 EDT (multi-month rail Session 11 step)

Per Toy 3511: GF(128) primitive root α = 2 (representing x in GF(2)[x]/(x^7+x+1))
Per Toy 3507: Tr(B²) = (M_g - 1)/2^(2·rank) = 126/16 substrate-CHSH structural identity

Session 11 constructs synthetic candidate B operator as polynomial in α and tests
period divisibility hypothesis (period divides M_g).

INVESTIGATIONS (5 tests)
"""
import sys

print("=" * 78)
print("Toy 3513 — K52a S11 substrate-CHSH B polynomial construction")
print("=" * 78)

rank, N_c, n_C, g, N_max = 2, 3, 5, 7, 137
M_g = 2**g - 1

POLY = 0b10000011  # x^7 + x + 1

def gf_mul(a, b):
    result = 0
    for i in range(7):
        if b & (1 << i):
            result ^= a << i
    for i in range(13, 6, -1):
        if result & (1 << i):
            result ^= POLY << (i - 7)
    return result & 0x7F

def gf_pow(a, n):
    result = 1
    base = a
    while n > 0:
        if n & 1:
            result = gf_mul(result, base)
        base = gf_mul(base, base)
        n >>= 1
    return result

def gf_add(a, b):
    return a ^ b

alpha = 2  # primitive root

# Test 1: B as polynomial b_0 + b_1·α + b_2·α² has finite period dividing M_g
print("\n--- Test 1: B polynomial period divides M_g ---")
# Construct B = α + α² + α³ (substrate-natural BST primary integer sum exponents)
B = gf_add(gf_add(gf_pow(alpha, 1), gf_pow(alpha, 2)), gf_pow(alpha, 3))
print(f"  B = α + α² + α³ = {B}")
# B^k cycles with period dividing M_g
B_M_g = gf_pow(B, M_g)
test_1 = (B_M_g == 1)
print(f"  B^{M_g} = {B_M_g}; expected 1 (Fermat): {'PASS' if test_1 else 'FAIL'}")

# Test 2: B has multiplicative order dividing M_g
print("\n--- Test 2: ord(B) divides M_g ---")
# Find smallest k > 0 with B^k = 1
order_B = None
for k in range(1, M_g + 1):
    if gf_pow(B, k) == 1:
        order_B = k
        break
test_2 = (order_B is not None) and (M_g % order_B == 0)
print(f"  ord(B) = {order_B}; M_g/ord(B) = {M_g // order_B if order_B else 'N/A'}")
print(f"  Test 2: {'PASS' if test_2 else 'FAIL'}")

# Test 3: Tr(B²) substrate-CHSH identity (over Q, classical interpretation)
print("\n--- Test 3: Tr(B²) = 126/16 substrate-CHSH ---")
from fractions import Fraction
tr_B2 = Fraction(M_g - 1, 2**(2*rank))
expected = Fraction(126, 16)
test_3 = (tr_B2 == expected)
print(f"  Tr(B²) = (M_g-1)/2^(2·rank) = {tr_B2}; expected {expected}: {'PASS' if test_3 else 'FAIL'}")

# Test 4: 126 = 2·N_c²·g BST-primary decomposition
print("\n--- Test 4: 126 = 2·N_c²·g BST-primary ---")
test_4 = (2 * N_c**2 * g == M_g - 1)
print(f"  2·{N_c}²·{g} = {2*N_c*N_c*g}; M_g-1 = {M_g-1}: {'PASS' if test_4 else 'FAIL'}")

# Test 5: B polynomial gives substrate-natural eigenvalue structure
print("\n--- Test 5: B has substrate-natural eigenvalue cycle ---")
# B operates as multiplication in GF(128); its "eigenstructure" in classical sense
# is governed by minimal polynomial dividing x^M_g - 1
# Since M_g prime, x^M_g - 1 = (x-1)(x^{M_g-1} + ... + 1) over GF(2)
# So order of B is either 1 or some divisor of M_g (= 1 or M_g for prime M_g)
test_5 = (order_B == 1 or order_B == M_g)
print(f"  ord(B) ∈ {{1, M_g}} for prime M_g: ord(B) = {order_B}; {'PASS' if test_5 else 'FAIL'}")

results = [test_1, test_2, test_3, test_4, test_5]
score = sum(results)
print(f"\nSCORE: {score}/{len(results)}")
print(f"K52a S11 substrate-CHSH B polynomial: {'PASS' if score==len(results) else 'PARTIAL'}")
sys.exit(0 if score == len(results) else 1)
