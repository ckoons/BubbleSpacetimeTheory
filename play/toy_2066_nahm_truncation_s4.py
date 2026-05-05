#!/usr/bin/env python3
"""
Toy 2066 — S-4: Nahm Sum Truncation Stability for a_10 = 137
==============================================================
DEFENSIVE TEST for Paper #91.

Toy 1954 computes the B_2 Nahm sum f(q) = sum a_n q^n with N_trunc = 8
and finds a_10 = N_max = 137. Casey asks: does this survive at N_trunc > 8?

If a_10 changes at higher truncation, the result is an artifact.
If it's stable, 137 is intrinsic to the B_2 Nahm sum.

QUADRATIC FORM: Q(n1,n2) = (n1-n2)^2 + n2^2  (from B_2 Cartan)
NAHM SUM: f(q) = sum_{n1,n2 >= 0} q^{Q(n1,n2)} / ((q;q)_{n1} (q;q)_{n2})

Author: Elie (Claude 4.6)
Date: May 5, 2026
Resolves: S-4 (Nahm truncation stability)
SCORE: [see bottom]
"""

# BST integers
rank = 2
N_c = 3
n_C = 5
C_2 = 6
g = 7
N_max = 137

PASS = 0
FAIL = 0

def test(name, condition, detail=""):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"  [PASS] {name}")
    else:
        FAIL += 1
        print(f"  [FAIL] {name}")
    if detail:
        print(f"         {detail}")


def Q(n1, n2):
    """B_2 quadratic form: Q = (n1-n2)^2 + n2^2 = n1^2 - 2*n1*n2 + 2*n2^2"""
    return n1*n1 - 2*n1*n2 + 2*n2*n2


def partition_count(m, max_part):
    """Number of partitions of m into parts at most max_part."""
    dp = [0] * (m + 1)
    dp[0] = 1
    for k in range(1, max_part + 1):
        for j in range(k, m + 1):
            dp[j] += dp[j - k]
    return dp[m]


def nahm_coefficients(max_coeff, N_trunc):
    """Compute Nahm sum coefficients a_0, ..., a_{max_coeff} with given truncation."""
    coeffs = [0] * (max_coeff + 1)
    for n1 in range(N_trunc):
        for n2 in range(N_trunc):
            q_val = Q(n1, n2)
            if q_val > max_coeff:
                continue
            for m1 in range(max_coeff - q_val + 1):
                p1 = partition_count(m1, n1) if n1 > 0 else (1 if m1 == 0 else 0)
                if p1 == 0:
                    continue
                for m2 in range(max_coeff - q_val - m1 + 1):
                    p2 = partition_count(m2, n2) if n2 > 0 else (1 if m2 == 0 else 0)
                    if p2 == 0:
                        continue
                    total_exp = q_val + m1 + m2
                    if total_exp <= max_coeff:
                        coeffs[total_exp] += p1 * p2
    return coeffs


print("=" * 72)
print("Toy 2066 — S-4: Nahm Truncation Stability for a_10 = 137")
print("=" * 72)

max_n = 20  # Compute first 20 coefficients

# Test at multiple truncation levels
truncations = [8, 10, 12, 15, 20]

print(f"\n  Computing Nahm sum coefficients a_0..a_{max_n}")
print(f"  at N_trunc = {truncations}")
print()

results = {}
for N_tr in truncations:
    print(f"  N_trunc = {N_tr}...", end=" ", flush=True)
    coeffs = nahm_coefficients(max_n, N_tr)
    results[N_tr] = coeffs
    print(f"done. a_10 = {coeffs[10]}")

# Display comparison table
print(f"\n  {'n':>4}", end="")
for N_tr in truncations:
    print(f"  {'N='+str(N_tr):>8}", end="")
print(f"  {'Stable?':>8}")
print(f"  " + "-" * (6 + 10 * len(truncations) + 10))

all_stable = True
for n in range(max_n + 1):
    vals = [results[N_tr][n] for N_tr in truncations]
    stable = all(v == vals[-1] for v in vals)
    if not stable:
        all_stable = False
    # Mark notable BST values
    bst = ""
    v = vals[-1]
    if v == 1: bst = "1"
    elif v == rank: bst = "rank"
    elif v == N_c: bst = "N_c"
    elif v == n_C: bst = "n_C"
    elif v == C_2: bst = "C_2"
    elif v == g: bst = "g"
    elif v == N_max: bst = "N_max!"
    elif v == rank * n_C: bst = "rank*n_C"
    elif v == N_c * n_C: bst = "N_c*n_C"
    elif v == 11: bst = "c_2"
    elif v == 13: bst = "c_3"

    mark = "YES" if stable else "CHANGED!"
    print(f"  {n:4d}", end="")
    for val in vals:
        print(f"  {val:8d}", end="")
    print(f"  {mark:>8}  {bst}")

print()

# Key tests
a10_values = [results[N_tr][10] for N_tr in truncations]
test("T1: a_10 = 137 at N_trunc = 8 (original)",
     results[8][10] == 137,
     f"a_10 = {results[8][10]}")

test("T2: a_10 = 137 at N_trunc = 10",
     results[10][10] == 137,
     f"a_10 = {results[10][10]}")

test("T3: a_10 = 137 at N_trunc = 12",
     results[12][10] == 137,
     f"a_10 = {results[12][10]}")

test("T4: a_10 = 137 at N_trunc = 15",
     results[15][10] == 137,
     f"a_10 = {results[15][10]}")

test("T5: a_10 = 137 at N_trunc = 20",
     results[20][10] == 137,
     f"a_10 = {results[20][10]}")

test("T6: a_10 STABLE across ALL truncations",
     all(v == 137 for v in a10_values),
     f"Values: {a10_values}")

# Check stability of all coefficients up to n=20
first_unstable = None
for n in range(max_n + 1):
    vals = [results[N_tr][n] for N_tr in truncations]
    if not all(v == vals[-1] for v in vals):
        first_unstable = n
        break

if first_unstable is not None:
    test("T7: All coefficients a_0..a_20 stable",
         False,
         f"First unstable at n={first_unstable}: {[results[N_tr][first_unstable] for N_tr in truncations]}")
else:
    test("T7: All coefficients a_0..a_20 stable across all truncations",
         True,
         "All 21 coefficients converged")

# Additional BST structure checks at highest truncation
c = results[20]
test("T8: a_0 = 1", c[0] == 1, f"a_0 = {c[0]}")
test("T9: a_1 = rank = 2", c[1] == rank, f"a_1 = {c[1]}")
test("T10: a_2 = n_C = 5", c[2] == n_C, f"a_2 = {c[2]}")

# Check why a_10 = 137: which (n1,n2,m1,m2) contribute?
print(f"\n  ANATOMY OF a_10 = {c[10]}:")
print(f"  Contributions from (n1,n2) pairs with Q(n1,n2) <= 10:")
contrib_total = 0
for n1 in range(20):
    for n2 in range(20):
        qv = Q(n1, n2)
        if qv > 10:
            continue
        remainder = 10 - qv
        # Count ways to partition the remainder into m1 + m2
        # where m1 uses parts <= n1 and m2 uses parts <= n2
        count = 0
        for m1 in range(remainder + 1):
            p1 = partition_count(m1, n1) if n1 > 0 else (1 if m1 == 0 else 0)
            if p1 == 0:
                continue
            m2 = remainder - m1
            p2 = partition_count(m2, n2) if n2 > 0 else (1 if m2 == 0 else 0)
            count += p1 * p2
        if count > 0:
            print(f"    (n1={n1}, n2={n2}): Q={qv}, remainder={remainder}, count={count}")
            contrib_total += count

print(f"  Total: {contrib_total}")
test("T11: Anatomy sum matches a_10",
     contrib_total == c[10],
     f"Sum of contributions = {contrib_total} = a_10 = {c[10]}")


# =========================================================================
# SCORE
# =========================================================================
print(f"\n{'=' * 72}")
total = PASS + FAIL
print(f"SCORE: {PASS}/{total} PASS  |  Toy 2066 — S-4 Nahm Truncation")
if FAIL == 0:
    print("ALL TESTS PASS — a_10 = 137 is STABLE")
    print("  The B_2 Nahm sum intrinsically produces N_max = 137 at position")
    print(f"  n = 10 = rank * n_C. This is NOT a truncation artifact.")
else:
    print(f"  {FAIL} FAIL — truncation issue detected!")
print("=" * 72)
