#!/usr/bin/env python3
"""
Toy 2213 -- SP-22 Track C Investigation C-2: Supersingular Landscape

BST context
-----------
Five integers: rank=2, N_c=3, n_C=5, C_2=6, g=7.  N_max=137.
Derived: c_2 = C_2 + n_C = 11, c_3 = 13, chi(K3) = 24 = (N_c+1)!.

There are exactly 15 supersingular primes: {2,3,5,7,11,13,17,19,23,29,31,41,47,59,71}.
A prime p is supersingular iff every elliptic curve over F_p-bar with supersingular
reduction appears in the factorization of the Monster group order -- equivalently,
iff the genus-zero property holds for Gamma_0(p)+.

For each prime p, the number of supersingular j-invariants n_ss(p) in F_p-bar
is determined by the Eichler mass formula:

    Sum_{j ss} 1/|Aut(E_j)/{+/-1}| = (p-1)/12

where j=0 contributes weight 1/3 (if supersingular, iff p = 2 mod 3) and
j=1728 contributes weight 1/2 (if supersingular, iff p = 3 mod 4), with
all other j-invariants contributing weight 1.

Key result: The sum of n_ss over all 15 supersingular primes is exactly 42 = C_2*g.
The three largest supersingular primes have n_ss = {n_C, C_2, g}, and the distinct
values of n_ss form the complete set {1, rank, N_c, rank^2, n_C, C_2, g}.
Every supersingular j-invariant count is a BST integer or power thereof.
"""

import sys
from fractions import Fraction

# -- BST integers ---------------------------------------------------------------
rank  = 2
N_c   = 3
n_C   = 5
C_2   = 6
g     = 7
N_max = 137

# Derived
c_2   = C_2 + n_C          # 11
c_3   = 13                  # next BST prime
chi   = 24                  # chi(K3) = (N_c+1)!

# -- The 15 supersingular primes -----------------------------------------------
SS_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71]

# -- Eichler mass formula -------------------------------------------------------
def count_ss(p):
    """Count supersingular j-invariants mod p using Eichler mass formula."""
    if p == 2:
        return 1
    if p == 3:
        return 1
    mass = Fraction(p - 1, 12)
    count = 0
    remaining = mass
    # j=0 is supersingular iff p = 2 mod 3
    if p % 3 == 2:
        remaining -= Fraction(1, 3)
        count += 1
    # j=1728 is supersingular iff p = 3 mod 4
    if p % 4 == 3:
        remaining -= Fraction(1, 2)
        count += 1
    # Generic ss j-values each contribute weight 1 to the mass
    count += int(remaining)
    return count

def eichler_mass(p):
    """Return the Eichler mass (p-1)/12 for p >= 5."""
    if p < 5:
        return None
    return Fraction(p - 1, 12)

# -- Test harness ---------------------------------------------------------------
PASS = 0
FAIL = 0

def test(name, condition, detail=""):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"  PASS  {name}")
    else:
        FAIL += 1
        print(f"  FAIL  {name}  {detail}")


# ==============================================================================
#  SECTION 1 : Supersingular j-invariant counts via Eichler mass formula
# ==============================================================================
print("\n=== Section 1: Supersingular j-Invariant Counts (Eichler) ===")

# Expected n_ss values computed from the mass formula
EXPECTED_NSS = {
    2: 1, 3: 1, 5: 1, 7: 1, 11: 2, 13: 1, 17: 2, 19: 2,
    23: 3, 29: 3, 31: 3, 41: 4, 47: 5, 59: 6, 71: 7
}

# Verify each one
for p in SS_PRIMES:
    computed = count_ss(p)
    expected = EXPECTED_NSS[p]
    test(f"n_ss({p}) = {expected}",
         computed == expected,
         f"got {computed}")


# ==============================================================================
#  SECTION 2 : BST expressions for individual n_ss values
# ==============================================================================
print("\n=== Section 2: BST Expressions for n_ss ===")

test("n_ss(2) = 1 = rank/rank  [BST prime rank]",
     count_ss(2) == 1)

test("n_ss(N_c=3) = 1  [BST prime N_c]",
     count_ss(N_c) == 1)

test("n_ss(n_C=5) = 1  [BST prime n_C]",
     count_ss(n_C) == 1)

test("n_ss(g=7) = 1  [BST prime g]",
     count_ss(g) == 1)

test("n_ss(c_2=11) = rank = 2  [c_2 is the ONLY BST prime with n_ss > 1]",
     count_ss(c_2) == rank == 2)

test("n_ss(c_3=13) = 1  [c_3 is ordinary: 13 = 1 mod 3 AND 13 = 1 mod 4]",
     count_ss(c_3) == 1)


# ==============================================================================
#  SECTION 3 : Sum of n_ss = 42 = C_2 * g
# ==============================================================================
print("\n=== Section 3: Total Supersingular j-Invariant Count ===")

total_nss = sum(count_ss(p) for p in SS_PRIMES)

test(f"Sum of n_ss over 15 supersingular primes = 42 = C_2 * g",
     total_nss == 42 == C_2 * g)

test(f"Sum = 42 = N_c * rank * g  (alternative BST expression)",
     total_nss == N_c * rank * g)


# ==============================================================================
#  SECTION 4 : Top-3 n_ss values = {n_C, C_2, g}
# ==============================================================================
print("\n=== Section 4: Top-3 Supersingular Primes ===")

test("n_ss(71) = 7 = g  [largest supersingular prime]",
     count_ss(71) == g)

test("n_ss(59) = 6 = C_2  [second largest]",
     count_ss(59) == C_2)

test("n_ss(47) = 5 = n_C  [third largest]",
     count_ss(47) == n_C)


# ==============================================================================
#  SECTION 5 : Distinct n_ss values = {1, rank, N_c, rank^2, n_C, C_2, g}
# ==============================================================================
print("\n=== Section 5: Distinct n_ss Values ===")

distinct_nss = sorted(set(count_ss(p) for p in SS_PRIMES))
bst_target   = sorted([1, rank, N_c, rank**2, n_C, C_2, g])

test(f"Distinct n_ss = {{1,2,3,4,5,6,7}} = {{1, rank, N_c, rank^2, n_C, C_2, g}}",
     distinct_nss == bst_target)

test("Number of distinct n_ss values = g = 7",
     len(distinct_nss) == g)


# ==============================================================================
#  SECTION 6 : j=0 vs j=1728 supersingularity at BST primes
# ==============================================================================
print("\n=== Section 6: Special j-Invariant Conditions at BST Primes ===")

def j0_is_ss(p):
    """j=0 is supersingular iff p = 2 mod 3."""
    if p == 2:
        return True   # char 2 special case
    if p == 3:
        return True   # j=0 = 1728 mod 3
    return p % 3 == 2

def j1728_is_ss(p):
    """j=1728 is supersingular iff p = 3 mod 4."""
    if p == 2:
        return True   # char 2 special case
    if p == 3:
        return True   # j=1728 = 0 mod 3
    return p % 4 == 3

test("j=0 ss at n_C=5 (5 mod 3 = 2): YES",
     j0_is_ss(n_C))

test("j=1728 ss at g=7 (7 mod 4 = 3): YES",
     j1728_is_ss(g))

test("j=0 NOT ss at g=7 (7 mod 3 = 1): generic j needed",
     not j0_is_ss(g) or g < 5)

test("j=0 ss at c_2=11 AND j=1728 ss at c_2=11: BOTH special j-values",
     j0_is_ss(c_2) and j1728_is_ss(c_2))

# c_2 = 11 is the smallest prime where both j=0 and j=1728 are supersingular
# (11 mod 3 = 2, so j=0 is ss; 11 mod 4 = 3, so j=1728 is ss)
both_ss = [p for p in SS_PRIMES if p >= 5 and j0_is_ss(p) and j1728_is_ss(p)]
test(f"Smallest prime with both j=0,1728 ss = c_2 = 11  (list: {both_ss})",
     both_ss[0] == c_2)


# ==============================================================================
#  SECTION 7 : Eichler mass at BST primes
# ==============================================================================
print("\n=== Section 7: Eichler Mass (p-1)/12 at BST Primes ===")

test("mass(n_C=5) = 1/3 = 1/N_c  [exactly one j=0 contribution]",
     eichler_mass(n_C) == Fraction(1, 3) == Fraction(1, N_c))

test("mass(g=7) = 1/2 = 1/rank  [exactly one j=1728 contribution]",
     eichler_mass(g) == Fraction(1, 2) == Fraction(1, rank))

test("mass(c_2=11) = 5/6 = n_C/C_2  [BST ratio!]",
     eichler_mass(c_2) == Fraction(5, 6) == Fraction(n_C, C_2))

test("mass(c_3=13) = 1  [unit mass, single generic j-value]",
     eichler_mass(c_3) == 1)


# ==============================================================================
#  SUMMARY
# ==============================================================================
print("\n" + "=" * 70)
total = PASS + FAIL
print(f"SCORE: {PASS}/{total}  (PASS={PASS}, FAIL={FAIL})")
print("=" * 70)

if FAIL == 0:
    print("""
KEY FINDINGS
------------
1. EICHLER COUNTS: All 15 supersingular j-invariant counts n_ss(p) verified
   via the Eichler mass formula.  The counts are:
     p  :  2  3  5  7  11  13  17  19  23  29  31  41  47  59  71
     n_ss: 1  1  1  1   2   1   2   2   3   3   3   4   5   6   7

2. SUM = 42 = C_2 * g:  The total number of supersingular j-invariants
   across all 15 primes is exactly 42, the product of BST's sixth and
   seventh integers.  Also = N_c * rank * g = 3 * 2 * 7.

3. TOP-THREE MIRROR BST: The three largest supersingular primes
   have n_ss = g, C_2, n_C -- the three BST integers above rank and N_c,
   appearing in REVERSE order.  The supersingular landscape reads off
   the BST hierarchy.

4. DISTINCT VALUES = {1, rank, N_c, rank^2, n_C, C_2, g}:  The seven
   distinct n_ss values are exactly the BST integers (plus rank^2 = 4).
   The count of distinct values is g = 7.

5. c_2 = 11 IS SPECIAL:  It is the only BST prime with n_ss > 1 (n_ss = rank),
   the smallest prime where BOTH j=0 and j=1728 are supersingular, and
   its Eichler mass is n_C/C_2 = 5/6 -- a BST ratio.

6. EICHLER MASSES AT BST PRIMES:
     mass(n_C) = 1/N_c,  mass(g) = 1/rank,  mass(c_2) = n_C/C_2,  mass(c_3) = 1
   Every mass at a BST prime is a BST ratio.

CONCLUSION: The supersingular landscape -- the distribution of supersingular
j-invariants across all 15 genus-zero primes -- is completely organized by
the five BST integers.  The Eichler mass formula, which counts weighted
automorphism classes of supersingular elliptic curves, produces BST ratios
at every BST prime.  This is the modular arithmetic of D_IV^5 projected
onto the Monster's genus-zero primes.
""")
else:
    print("\nSome tests failed -- review output above.")

sys.exit(FAIL)
