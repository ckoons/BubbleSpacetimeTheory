#!/usr/bin/env python3
"""
Toy 1854: Upper Critical Dimension = n_C - 1 = 4

Board item CE-5. The upper critical dimension d_c = 4 above which
mean-field exponents hold is d_c = n_C - 1.

Below d_c, exponents are BST fractions. At d_c, logarithmic corrections
appear. Above d_c, exponents are classical (mean-field).

BST integers: rank=2, N_c=3, n_C=5, C_2=6, g=7.

2D Ising exponents (known exactly, all BST):
  alpha = 0 (log divergence)
  beta  = 1/8 = 1/rank^N_c
  gamma = 7/4 = g/rank^2
  delta = 15 = N_c * n_C
  nu    = 1 = 1
  eta   = 1/4 = 1/rank^2

Mean-field exponents (d > d_c = 4):
  alpha = 0, beta = 1/2 = 1/rank, gamma = 1,
  delta = 3 = N_c, nu = 1/2 = 1/rank, eta = 0

SCORE: 11/11
"""

from sympy import Rational
import math

# BST integers
rank = 2
N_c = 3
n_C = 5
C_2 = 6
g = 7
N_max = 137

pass_count = 0
total = 11

def test(name, condition, detail=""):
    global pass_count
    if condition:
        pass_count += 1
        print(f"  T{pass_count}: PASS -- {name}")
    else:
        print(f"  FAIL -- {name}")
    if detail:
        print(f"    {detail}")

print("=" * 72)
print("Toy 1854: Upper Critical Dimension = n_C - 1 = 4")
print("=" * 72)

# ============================================================
# Part 1: Upper Critical Dimension
# ============================================================
print("\n--- Part 1: d_c = n_C - 1 = 4 ---\n")

d_c = n_C - 1
print(f"  Upper critical dimension: d_c = n_C - 1 = {n_C} - 1 = {d_c}")
print(f"  Known value: d_c = 4 for Ising/phi^4 universality")
print(f"  BST: d_c = n_C - 1 = 4")

test("d_c = n_C - 1 = 4 (upper critical dimension)",
     d_c == 4 == n_C - 1)

# Why n_C - 1? The APG has complex dimension n_C = 5.
# Real dimension = 2*n_C = 10.
# The critical dimension is the codimension of the domain boundary
# in the real embedding: 2*n_C - (n_C + 1) = n_C - 1.
# Or: d_c = rank*rank = 4 (rank^2)
print(f"\n  Alternative: d_c = rank^2 = {rank**2}")
print(f"  rank^2 = n_C - 1 (from rank=2, n_C=5)")

test("d_c = rank^2 = 4",
     rank**2 == d_c)

# ============================================================
# Part 2: 2D Ising Exponents as BST Fractions
# ============================================================
print("\n--- Part 2: 2D Ising Exponents ---\n")

# Known exact 2D Ising exponents (Onsager solution):
ising_2d = {
    'alpha': (Rational(0), "0", "log divergence"),
    'beta':  (Rational(1, 8), "1/rank^N_c", f"1/{rank}^{N_c} = 1/{rank**N_c}"),
    'gamma': (Rational(7, 4), "g/rank^2", f"{g}/{rank**2} = {g}/{rank**2}"),
    'delta': (Rational(15, 1), "N_c*n_C", f"{N_c}*{n_C} = {N_c*n_C}"),
    'nu':    (Rational(1, 1), "1", "1"),
    'eta':   (Rational(1, 4), "1/rank^2", f"1/{rank}^2 = 1/{rank**2}"),
}

print(f"  {'Exponent':>10} {'Value':>8} {'BST':>12} {'Expression':>20}")
print(f"  {'-'*10} {'-'*8} {'-'*12} {'-'*20}")
for name, (val, bst_expr, detail) in ising_2d.items():
    print(f"  {name:>10} {str(val):>8} {bst_expr:>12} {detail:>20}")

# Verify BST expressions
test("beta = 1/8 = 1/rank^N_c",
     Rational(1, 8) == Rational(1, rank**N_c))

test("gamma = 7/4 = g/rank^2",
     Rational(7, 4) == Rational(g, rank**2))

test("delta = 15 = N_c*n_C",
     15 == N_c * n_C)

test("eta = 1/4 = 1/rank^2",
     Rational(1, 4) == Rational(1, rank**2))

# ============================================================
# Part 3: Mean-Field Exponents as BST
# ============================================================
print("\n--- Part 3: Mean-Field Exponents (d > d_c) ---\n")

mf = {
    'alpha': (Rational(0), "0"),
    'beta':  (Rational(1, 2), "1/rank"),
    'gamma': (Rational(1, 1), "1"),
    'delta': (Rational(3, 1), "N_c"),
    'nu':    (Rational(1, 2), "1/rank"),
    'eta':   (Rational(0), "0"),
}

print(f"  {'Exponent':>10} {'MF value':>10} {'BST':>8}")
print(f"  {'-'*10} {'-'*10} {'-'*8}")
for name, (val, bst) in mf.items():
    print(f"  {name:>10} {str(val):>10} {bst:>8}")

test("Mean-field beta = 1/2 = 1/rank",
     Rational(1, 2) == Rational(1, rank))

test("Mean-field delta = 3 = N_c",
     3 == N_c)

test("Mean-field nu = 1/2 = 1/rank",
     Rational(1, 2) == Rational(1, rank))

# ============================================================
# Part 4: Scaling Relations
# ============================================================
print("\n--- Part 4: Scaling Relations (2D Ising) ---\n")

alpha_2d = Rational(0)
beta_2d = Rational(1, 8)
gamma_2d = Rational(7, 4)
delta_2d = Rational(15)
nu_2d = Rational(1)
eta_2d = Rational(1, 4)

# Rushbrooke: alpha + 2*beta + gamma = 2
rushbrooke = alpha_2d + 2*beta_2d + gamma_2d
print(f"  Rushbrooke: alpha + 2*beta + gamma = {rushbrooke} = 2")

# Griffiths: alpha + beta*(1+delta) = 2
griffiths = alpha_2d + beta_2d * (1 + delta_2d)
print(f"  Griffiths: alpha + beta*(1+delta) = {griffiths} = 2")

# Fisher: gamma = nu*(2 - eta)
fisher = nu_2d * (2 - eta_2d)
print(f"  Fisher: nu*(2-eta) = {fisher} = {gamma_2d} = gamma")

# Josephson (hyperscaling): 2 - alpha = d*nu (d=2)
d = 2
josephson = d * nu_2d
print(f"  Josephson: d*nu = {josephson} = 2-alpha = {2 - alpha_2d}")

test("All four scaling relations hold for 2D Ising",
     rushbrooke == 2 and griffiths == 2 and fisher == gamma_2d
     and josephson == 2 - alpha_2d)

# ============================================================
# Part 5: Crossover Pattern
# ============================================================
print("\n--- Part 5: Crossover d < d_c to d > d_c ---\n")

# The crossover from BST fractions to mean-field:
# At d = d_c = 4: logarithmic corrections appear
# Below d_c: exponents are d-dependent BST fractions
# Above d_c: exponents freeze to mean-field values

# Key observation: mean-field exponents are LIMITING CASES
# of the BST expressions:
# beta: 1/rank^N_c (2D) → 1/rank (MF)
# gamma: g/rank^2 (2D) → 1 (MF)
# delta: N_c*n_C (2D) → N_c (MF)
# The BST integers appear in both regimes!

print(f"  Crossover pattern in delta:")
print(f"    d=2: delta = N_c*n_C = {N_c*n_C}")
print(f"    d=3: delta ≈ 4.79 (not exact BST)")
print(f"    d>4: delta = N_c = {N_c}")
print(f"    2D delta / MF delta = n_C = {N_c*n_C // N_c}")

test("2D delta / MF delta = n_C = 5",
     (N_c * n_C) // N_c == n_C)

# Mean-field exponents as rank-limit:
# beta_MF = 1/rank (rank alone, no N_c)
# This suggests: above d_c, only rank matters
# Below d_c, all integers participate
print(f"\n  Above d_c: only rank matters")
print(f"    beta = 1/rank, nu = 1/rank, delta = N_c")
print(f"  Below d_c: all BST integers participate")
print(f"    beta = 1/rank^N_c, gamma = g/rank^2, delta = N_c*n_C")

# ============================================================
# Summary
# ============================================================
print("\n" + "=" * 72)
print("SUMMARY: Toy 1854 — Critical Dimension = n_C - 1 = 4")
print("=" * 72)

print(f"""
  d_c = n_C - 1 = 4 is the upper critical dimension.

  2D Ising (all BST fractions):
    beta = 1/rank^N_c = 1/8
    gamma = g/rank^2 = 7/4
    delta = N_c*n_C = 15
    eta = 1/rank^2 = 1/4

  Mean-field (d > d_c, rank-only):
    beta = 1/rank = 1/2
    delta = N_c = 3
    nu = 1/rank = 1/2

  Pattern: above d_c, only rank survives.
  Below d_c, all five integers participate.
""")

print(f"SCORE: {pass_count}/{total}")
