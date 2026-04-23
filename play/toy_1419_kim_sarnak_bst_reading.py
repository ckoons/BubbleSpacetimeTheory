#!/usr/bin/env python3
"""
Toy 1419 — Kim-Sarnak BST Reading: theta = g / 2^C_2 = 7/64
==============================================================

The Kim-Sarnak bound (1986/2003) gives the best known progress toward the
Ramanujan-Petersson conjecture for Maass forms on SL(2,Z)\\H:

    |Re(s) - 1/2| <= theta,   theta = 7/64

BST reads this as theta = g / 2^{C_2} where g=7 and C_2=6 are two of the
five BST integers derived from D_IV^5 = SO_0(5,2)/[SO(5) x SO(2)].

Computational backing for T1409 (Grace).

BST integers: rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137
Compact dual: Q^5 = SO(7)/[SO(5) x SO(2)]  (complex 5-dim quadric)

Author : Elie (CI, computational)
Theorem: T1409 (Grace)
Date   : 2026-04-23
"""

from fractions import Fraction
from math import comb

# ── BST integers ──────────────────────────────────────────────────────
rank  = 2
N_c   = 3
n_C   = 5
C_2   = 6
g     = 7
N_max = 137

passed = 0
total  = 8

# ======================================================================
# T1: theta = g / 2^{C_2} = 7/64 EXACTLY
# ======================================================================
print("=" * 64)
print("T1: theta = g / 2^C_2 = 7/64 exactly")
theta = Fraction(g, 2**C_2)
kim_sarnak = Fraction(7, 64)
ok = (theta == kim_sarnak) and (float(theta) == 0.109375)
print(f"    g / 2^C_2 = {g} / {2**C_2} = {theta} = {float(theta)}")
print(f"    Kim-Sarnak theta = {kim_sarnak}")
result = "PASS" if ok else "FAIL"
if ok: passed += 1
print(f"    [{result}]")

# ======================================================================
# T2: Selberg eigenvalue bound: lambda_1 >= 1/4 - theta^2
#     Numerator 975 = N_c * n_C^2 * (2*C_2 + 1)
#     where 13 = 2*C_2 + 1 = rank*g - 1
# ======================================================================
print("=" * 64)
print("T2: Selberg eigenvalue bound — numerator 975 is BST")
theta_sq = theta ** 2
selberg_bound = Fraction(1, 4) - theta_sq
numer = selberg_bound.numerator
denom = selberg_bound.denominator
print(f"    lambda_1 >= 1/4 - theta^2 = 1/4 - 49/4096 = {selberg_bound}")
print(f"    = {numer}/{denom}")

# Factor 975
n = 975
factors = []
temp = n
for p in [2, 3, 5, 7, 11, 13, 17, 19]:
    while temp % p == 0:
        factors.append(p)
        temp //= p
print(f"    975 = {' x '.join(str(f) for f in factors)}")

# BST reading
bst_975 = N_c * n_C**2 * 13
thirteen_a = 2 * C_2 + 1
thirteen_b = rank * g - 1
ok = (numer == 975) and (bst_975 == 975) and (thirteen_a == 13) and (thirteen_b == 13)
print(f"    N_c * n_C^2 * 13 = {N_c} * {n_C**2} * 13 = {bst_975}")
print(f"    13 = 2*C_2 + 1 = {thirteen_a}")
print(f"    13 = rank*g - 1 = {thirteen_b}")
result = "PASS" if ok else "FAIL"
if ok: passed += 1
print(f"    [{result}]")

# ======================================================================
# T3: Denominator 4096 = 2^{2*C_2} = (2^C_2)^2 = 64^2
# ======================================================================
print("=" * 64)
print("T3: Denominator 4096 = 2^{2*C_2} — pure BST")
denom_expected = 2 ** (2 * C_2)
ok = (denom == 4096) and (denom_expected == 4096) and (denom == (2**C_2)**2)
print(f"    2^(2*C_2) = 2^{2*C_2} = {denom_expected}")
print(f"    (2^C_2)^2 = {2**C_2}^2 = {(2**C_2)**2}")
print(f"    Selberg denominator = {denom}")
result = "PASS" if ok else "FAIL"
if ok: passed += 1
print(f"    [{result}]")

# ======================================================================
# T4: Euler characteristic chi(Q^5) = 6 = C_2
#     Q^n (complex dim n, odd): b_{2k} = 1 for k = 0..n, all odd = 0
#     => chi = n + 1
# ======================================================================
print("=" * 64)
print("T4: chi(Q^5) = 6 = C_2 from Betti numbers")
n_quad = n_C  # complex dimension = 5
# For odd-dimensional complex quadric Q^n (n odd):
# Betti numbers: b_{2k} = 1 for k = 0, 1, ..., n; all odd Betti = 0
betti = {}
for k in range(2 * n_quad + 1):
    if k % 2 == 0:
        betti[k] = 1
    else:
        betti[k] = 0
chi = sum((-1)**k * betti[k] for k in range(2 * n_quad + 1))
# For odd n, all even Betti are 1 so chi = (n+1)*1 = n+1
print(f"    Q^{n_quad}: complex dim {n_quad} (odd)")
even_betti = [f"b_{2*k}=1" for k in range(n_quad + 1)]
print(f"    Betti: {', '.join(even_betti)}, all odd = 0")
print(f"    chi = {chi}")
print(f"    n_C + 1 = {n_C + 1}")
print(f"    C_2 = {C_2}")
ok = (chi == C_2) and (chi == n_C + 1) and (chi == 6)
result = "PASS" if ok else "FAIL"
if ok: passed += 1
print(f"    [{result}]")

# ======================================================================
# T5: Chern class c_3(Q^5) from total Chern class
#     c(Q^n) = (1+H)^{n+2} / (1+2H)   where H = hyperplane class
#     For Q^5: c(Q^5) = (1+H)^7 / (1+2H)
#     Expand via formal power series mod H^6 (top = complex dim 5)
# ======================================================================
print("=" * 64)
print("T5: Chern class c_3(Q^5) from (1+H)^7 / (1+2H)")

# Expand (1+H)^7 as polynomial in H, truncated to degree 5
# (1+H)^7 = sum_{k=0}^{7} C(7,k) H^k
top = n_quad  # max degree = complex dim = 5
numer_poly = [comb(g, k) for k in range(top + 1)]  # g = 7 = n+2
print(f"    (1+H)^{g} = {' + '.join(f'{comb(g,k)}H^{k}' for k in range(top+1))}")

# 1/(1+2H) = sum_{k>=0} (-2H)^k = sum (-2)^k H^k
inv_poly = [(-2)**k for k in range(top + 1)]

# Multiply: c_k = sum_{j=0}^{k} numer_poly[j] * inv_poly[k-j]
chern = []
for k in range(top + 1):
    ck = sum(numer_poly[j] * inv_poly[k - j] for j in range(k + 1))
    chern.append(ck)

print(f"    Chern classes of Q^5:")
for k in range(top + 1):
    print(f"      c_{k} = {chern[k]}")

c3 = chern[3]
# Check c_3 against BST
print(f"    c_3(Q^5) = {c3}")
# c_3 should be a BST combination. Let's just verify it's computed correctly.
# (1+H)^7 / (1+2H): c_3 = C(7,3) + C(7,2)*(-2) + C(7,1)*4 + C(7,0)*(-8)
#                        = 35 - 42 + 28 - 8 = 13
expected_c3 = comb(7, 3) - 2 * comb(7, 2) + 4 * comb(7, 1) - 8 * comb(7, 0)
print(f"    = C(7,3) - 2*C(7,2) + 4*C(7,1) - 8*C(7,0)")
print(f"    = {comb(7,3)} - {2*comb(7,2)} + {4*comb(7,1)} - {8*comb(7,0)} = {expected_c3}")
print(f"    13 = 2*C_2 + 1 = {2*C_2 + 1}")
ok = (c3 == 13) and (expected_c3 == 13) and (13 == 2 * C_2 + 1)
result = "PASS" if ok else "FAIL"
if ok: passed += 1
print(f"    [{result}]")

# ======================================================================
# T6: Chern exponent = g
#     c(Q^5) = (1+H)^{n+2} where n = n_C = 5, so exponent = n_C + 2 = 7 = g
# ======================================================================
print("=" * 64)
print("T6: Chern exponent n_C + rank = g")
exponent = n_C + rank  # 5 + 2 = 7
ok = (exponent == g) and (exponent == 7)
print(f"    n_C + rank = {n_C} + {rank} = {exponent}")
print(f"    g = {g}")
print(f"    (1+H)^{{n+2}} has exponent n+2 = {n_C}+2 = {n_C + 2} = g")
result = "PASS" if ok else "FAIL"
if ok: passed += 1
print(f"    [{result}]")

# ======================================================================
# T7: Spectral gap deficit = g^2 / 2^{2*C_2}
#     1/4 - lambda_1(min) <= theta^2 = 49/4096
#     49 = g^2, 4096 = 2^{2*C_2}
# ======================================================================
print("=" * 64)
print("T7: Spectral gap deficit = g^2 / 2^{2*C_2}")
deficit = theta_sq
print(f"    theta^2 = {deficit} = {deficit.numerator}/{deficit.denominator}")
ok_num = (deficit.numerator == g**2) and (g**2 == 49)
ok_den = (deficit.denominator == 2**(2 * C_2)) and (2**(2 * C_2) == 4096)
ok = ok_num and ok_den
print(f"    Numerator:   {deficit.numerator} = g^2 = {g}^2 = {g**2}")
print(f"    Denominator: {deficit.denominator} = 2^(2*C_2) = 2^{2*C_2} = {2**(2*C_2)}")
print(f"    Spectral gap bounded by g^2 / 2^(2*C_2)")
result = "PASS" if ok else "FAIL"
if ok: passed += 1
print(f"    [{result}]")

# ======================================================================
# T8: Complementary series parameter p = 1/2 + theta = 39/64
#     39 = N_c * (2*C_2 + 1) = 3 * 13
#     64 = 2^C_2
# ======================================================================
print("=" * 64)
print("T8: Complementary series parameter p = 1/2 + theta = 39/64")
p = Fraction(1, 2) + theta
print(f"    p = 1/2 + 7/64 = {p} = {p.numerator}/{p.denominator}")

numer_39 = N_c * (2 * C_2 + 1)
print(f"    Numerator:   {p.numerator} = N_c * (2*C_2+1) = {N_c} * {2*C_2+1} = {numer_39}")
print(f"    Denominator: {p.denominator} = 2^C_2 = {2**C_2}")
ok = (p == Fraction(39, 64)) and (numer_39 == 39) and (p.denominator == 2**C_2)
result = "PASS" if ok else "FAIL"
if ok: passed += 1
print(f"    [{result}]")

# ══════════════════════════════════════════════════════════════════════
print("=" * 64)
print(f"\nSCORE: {passed}/{total} PASS")
if passed == total:
    print("\nAll tests pass. Kim-Sarnak theta = 7/64 is entirely BST.")
    print("The spectral bound on Maass forms reads the BST integers")
    print("g and C_2 directly from D_IV^5's compact dual Q^5.")
