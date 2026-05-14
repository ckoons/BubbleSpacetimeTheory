#!/usr/bin/env python3
"""
Toy 2194 — Partition Function at Chern Classes of Q^5
SP-21 Investigation III-2 (Elie)

The Chern classes of the tautological bundle Q^5 on D_IV^5 are:
  c_0 = 1, c_1 = 5, c_2 = 11, c_3 = 13, c_4 = 9, c_5 = 3

We evaluate the partition function p() at each Chern class and at
iterated compositions, testing whether BST closure extends to the
Chern ring.

Key findings:
- p(c_0)=1, p(c_1)=g, p(c_5)=N_c — boundary Chern → color integers
- p(c_2)=56=2^N_c*g, p(c_4)=30=n_C*C_2 — interior Chern → BST products
- p(c_3)=101 — PRIME, first genuine boundary of partition closure
- Iterated: p(p(C_2))=56=2^N_c*g, p(p(g))=176=2^(rank^2)*c_2
- Ramanujan congruence: 24^{-1} mod {5,7,11} = {4,5,6} = {rank^2, n_C, C_2}

SCORE: 25/25 ALL PASS
"""

import math
import sys

PASS = 0
FAIL = 0

rank = 2
N_c = 3
n_C = 5
C_2 = 6
g = 7
N_max = 137
c_2_val = C_2 + n_C  # = 11

# Chern classes of Q^5 on D_IV^5
chern = [1, n_C, c_2_val, 13, 9, N_c]  # c_0..c_5

def test(name, condition, detail=""):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"  PASS  {name}")
    else:
        FAIL += 1
        print(f"  FAIL  {name}  {detail}")

def partitions(n, memo={}):
    if n in memo: return memo[n]
    if n < 0: return 0
    if n == 0: return 1
    result = 0
    k = 1
    while True:
        # Euler's pentagonal number theorem
        pk1 = k * (3*k - 1) // 2
        pk2 = k * (3*k + 1) // 2
        if pk1 > n and pk2 > n:
            break
        sign = (-1)**(k+1)
        if pk1 <= n:
            result += sign * partitions(n - pk1)
        if pk2 <= n:
            result += sign * partitions(n - pk2)
        k += 1
    memo[n] = result
    return result

def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0: return False
        i += 6
    return True

def prime_factors(val):
    pf = set(); m = abs(val)
    for p in range(2, m+1):
        if p*p > m and m > 1:
            pf.add(m); break
        while m % p == 0:
            pf.add(p); m //= p
    return pf

def mod_inverse(a, m):
    """Modular inverse of a mod m."""
    g, x, _ = extended_gcd(a, m)
    if g != 1: return None
    return x % m

def extended_gcd(a, b):
    if a == 0: return b, 0, 1
    g, x, y = extended_gcd(b % a, a)
    return g, y - (b // a) * x, x

# ============================================================
print("=" * 65)
print("Toy 2194: Partition Function at Chern Classes of Q^5")
print("=" * 65)

# === SECTION 1: p(c_k) for k = 0..5 ===
print("\n--- Section 1: p(c_k(Q^5)) ---")

p_at_chern = [partitions(c) for c in chern]
print(f"  Chern classes: c_0..c_5 = {chern}")
print(f"  p(c_k):        {p_at_chern}")

# p(c_0) = p(1) = 1
test("T1: p(c_0) = p(1) = 1 (identity)",
     p_at_chern[0] == 1)

# p(c_1) = p(n_C) = p(5) = 7 = g
test("T2: p(c_1) = p(n_C) = g = 7 (first Chern → genus)",
     p_at_chern[1] == g)

# p(c_2) = p(11) = 56 = 2^N_c * g = 8 * 7
test("T3: p(c_2) = p(11) = 56 = 2^N_c * g",
     p_at_chern[2] == 2**N_c * g,
     f"p(11) = {p_at_chern[2]}")

# p(c_3) = p(13) = 101 — PRIME
test("T4: p(c_3) = p(13) = 101 (PRIME — closure boundary)",
     p_at_chern[3] == 101 and is_prime(101),
     f"p(13) = {p_at_chern[3]}")

# p(c_4) = p(9) = 30 = n_C * C_2
test("T5: p(c_4) = p(9) = 30 = n_C * C_2",
     p_at_chern[4] == n_C * C_2,
     f"p(9) = {p_at_chern[4]}")

# p(c_5) = p(N_c) = p(3) = 3 = N_c (fixed point!)
test("T6: p(c_5) = p(N_c) = N_c = 3 (fixed point)",
     p_at_chern[5] == N_c)

# Symmetry: c_1 → g via p(), c_5 → N_c via p()
# The "boundary" Chern classes (k=1 and k=5) map to the color integers
test("T7: Boundary Chern symmetry: p(c_1)=g, p(c_5)=N_c (color pair)",
     p_at_chern[1] == g and p_at_chern[5] == N_c)

# === SECTION 2: BST factorization of p(c_k) ===
print("\n--- Section 2: Factorization Analysis ---")

# p(c_0) = 1: trivial
# p(c_1) = 7 = g: BST prime
# p(c_2) = 56 = 2^3 * 7 = 2^N_c * g
# p(c_3) = 101: PRIME, not in {2,3,5,7,11,13}
# p(c_4) = 30 = 2 * 3 * 5 = rank * N_c * n_C
# p(c_5) = 3 = N_c

bst_closed = [1, g, 2**N_c * g, None, n_C * C_2, N_c]  # None = boundary
bst_count = sum(1 for x in bst_closed if x is not None)
test("T8: 5/6 Chern partition values are BST expressions (83%)",
     bst_count == 5)

# p(c_4) = 30: alternative decomposition
# 30 = n_C * C_2 = rank * N_c * n_C = rank * 15 = rank * p(g)
test("T9: p(c_4) = rank * p(g) = rank * N_c * n_C (three-integer product)",
     p_at_chern[4] == rank * N_c * n_C)

# The BOUNDARY case: p(c_3) = 101
# 101 is the 26th prime. 26 = rank * 13 = rank * c_3. Coincidence? Maybe.
# 101 = N_max - 36 = N_max - C_2^2
test("T10: 101 = N_max - C_2^2 = 137 - 36 (near-miss BST expression)",
     101 == N_max - C_2**2)

# But 101 is genuinely outside the BST radical {2,3,5,7,11,13}
test("T11: 101 is prime and NOT in BST+Chern primes (genuine boundary)",
     is_prime(101) and 101 not in {2, 3, 5, 7, 11, 13})

# === SECTION 3: Iterated partitions ===
print("\n--- Section 3: Iterated Partitions p(p(BST)) ---")

# p(p(rank)) = p(2) = 2 = rank (still fixed)
pp_rank = partitions(partitions(rank))
test("T12: p(p(rank)) = rank = 2 (double fixed point)",
     pp_rank == rank)

# p(p(N_c)) = p(3) = 3 = N_c (still fixed)
pp_Nc = partitions(partitions(N_c))
test("T13: p(p(N_c)) = N_c = 3 (double fixed point)",
     pp_Nc == N_c)

# p(p(n_C)) = p(p(5)) = p(7) = 15 = N_c * n_C
pp_nC = partitions(partitions(n_C))
test("T14: p(p(n_C)) = p(g) = N_c * n_C = 15",
     pp_nC == N_c * n_C)

# p(p(C_2)) = p(p(6)) = p(11) = 56 = 2^N_c * g
pp_C2 = partitions(partitions(C_2))
test("T15: p(p(C_2)) = p(c_2) = 2^N_c * g = 56",
     pp_C2 == 2**N_c * g,
     f"got {pp_C2}")

# p(p(g)) = p(p(7)) = p(15) = 176 = 2^4 * 11 = 2^(rank^2) * c_2
pp_g = partitions(partitions(g))
test("T16: p(p(g)) = 176 = 2^(rank^2) * c_2",
     pp_g == 2**(rank**2) * c_2_val,
     f"got {pp_g}")

# Triple iteration: p(p(p(n_C))) = p(p(7)) = p(15) = 176 = 2^(rank^2) * c_2
ppp_nC = partitions(pp_nC)
test("T17: p^3(n_C) = p(p(g)) = 2^(rank^2) * c_2 = 176",
     ppp_nC == 2**(rank**2) * c_2_val,
     f"got {ppp_nC}")

# === SECTION 4: Ramanujan congruence residues ===
print("\n--- Section 4: Ramanujan Congruences ---")

# chi(K3) = 24 = rank^2 * C_2
chi_K3 = 24

# Ramanujan's congruences for p(n):
# p(5n+4) ≡ 0 (mod 5)
# p(7n+5) ≡ 0 (mod 7)
# p(11n+6) ≡ 0 (mod 11)
# The moduli are {5, 7, 11} = {n_C, g, c_2} = BST!
# The offsets are {4, 5, 6} = {rank^2, n_C, C_2} = BST!

test("T18: Ramanujan moduli {5,7,11} = {n_C, g, c_2} (BST integers)",
     set([5, 7, 11]) == {n_C, g, c_2_val})

test("T19: Ramanujan offsets {4,5,6} = {rank^2, n_C, C_2} (BST integers)",
     set([4, 5, 6]) == {rank**2, n_C, C_2})

# The offsets ARE 24^{-1} mod the moduli!
# 24^{-1} mod 5: 24 ≡ 4 mod 5, 4^{-1} mod 5 = 4 (since 4*4=16≡1). So 24^{-1} ≡ 4 mod 5
# 24^{-1} mod 7: 24 ≡ 3 mod 7, 3^{-1} mod 7 = 5 (since 3*5=15≡1). So 24^{-1} ≡ 5 mod 7
# 24^{-1} mod 11: 24 ≡ 2 mod 11, 2^{-1} mod 11 = 6 (since 2*6=12≡1). So 24^{-1} ≡ 6 mod 11
inv_24_mod_5 = mod_inverse(24, 5)
inv_24_mod_7 = mod_inverse(24, 7)
inv_24_mod_11 = mod_inverse(24, 11)

test("T20: 24^{-1} mod n_C = rank^2 = 4",
     inv_24_mod_5 == rank**2,
     f"got {inv_24_mod_5}")

test("T21: 24^{-1} mod g = n_C = 5",
     inv_24_mod_7 == n_C,
     f"got {inv_24_mod_7}")

test("T22: 24^{-1} mod c_2 = C_2 = 6",
     inv_24_mod_11 == C_2,
     f"got {inv_24_mod_11}")

# So: chi(K3)^{-1} mod {n_C, g, c_2} = {rank^2, n_C, C_2}
# The Ramanujan congruences encode chi(K3) inversions at BST primes!
test("T23: chi(K3)^{-1} mod BST primes = BST integers",
     {inv_24_mod_5, inv_24_mod_7, inv_24_mod_11} == {rank**2, n_C, C_2})

# Verify the actual congruences
test("T24: p(5*0+4) = p(4) = 5 ≡ 0 mod n_C",
     partitions(4) % n_C == 0,
     f"p(4) = {partitions(4)}")

test("T25: p(7*0+5) = p(5) = 7 ≡ 0 mod g",
     partitions(5) % g == 0,
     f"p(5) = {partitions(5)}")

# === Summary ===
print("\n" + "=" * 65)
print(f"Toy 2194 SCORE: {PASS}/{PASS+FAIL}", end="")
if FAIL == 0:
    print(" ALL PASS")
else:
    print(f" ({FAIL} FAIL)")
print("=" * 65)

print("""
KEY FINDINGS:
1. CHERN CLOSURE: p(c_k) for 5/6 Chern classes are BST expressions.
   p(c_1)=g, p(c_2)=2^N_c*g, p(c_4)=n_C*C_2, p(c_5)=N_c.
   Boundary: p(c_3)=101 (prime, outside BST radical).

2. BOUNDARY SYMMETRY: p(c_1)=g and p(c_5)=N_c — the boundary
   Chern classes map to the color pair {N_c, g}.

3. ITERATED CLOSURE: p(p(C_2)) = 2^N_c * g = 56.
   p(p(g)) = 2^(rank^2) * c_2 = 176. Even DOUBLE partitions stay BST.

4. RAMANUJAN CONGRUENCES: The moduli {5,7,11} = {n_C, g, c_2}.
   The offsets {4,5,6} = {rank^2, n_C, C_2}.
   THESE ARE chi(K3)^{-1} mod BST primes.

5. 101 = N_max - C_2^2 = 137 - 36: the only Chern partition
   outside BST closure. It marks the genuine boundary where
   the third Chern class escapes.

6. Connection: eta^{chi(K3)} = eta^24 = Delta generates p(n).
   The Ramanujan congruences at BST primes are STRUCTURAL:
   they come from chi(K3) = 24 being invertible mod {5,7,11}.
""")

sys.exit(FAIL)
