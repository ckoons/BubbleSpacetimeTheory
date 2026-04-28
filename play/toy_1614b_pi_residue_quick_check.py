#!/usr/bin/env python3
"""
Quick check: pi - N_c = 0.14159... — does this residue appear in BST corrections?

Not a full toy, just a curiosity probe from the SP-12 Understanding Program.
If significant, will become a numbered toy.

BST integers: rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137.
"""
import math

rank = 2
N_c = 3
n_C = 5
C_2 = 6
g = 7
N_max = 137
DC = 11
alpha = 1/N_max

pi = math.pi
residue = pi - N_c  # = 0.14159265...

print("pi - N_c residue check")
print(f"  pi = {pi:.10f}")
print(f"  N_c = {N_c}")
print(f"  pi - N_c = {residue:.10f}")
print()

# Check: is residue close to known BST expressions?
candidates = {
    'alpha': alpha,
    '1/g': 1/g,
    '1/C_2': 1/C_2,
    '1/(g-1)': 1/(g-1),
    'rank/(rank*g+1)': rank/(rank*g+1),
    '1/N_c!': 1/math.factorial(N_c),
    'N_c/DC^2': N_c/DC**2,
    'alpha*DC*rank': alpha*DC*rank,
    'n_C/(C_2*g-1)': n_C/(C_2*g-1),
    'ln(2)/(n_C-1)': math.log(2)/(n_C-1),
    '1/(N_c*rank+1)': 1/(N_c*rank+1),
    'alpha*rank*N_c^2': alpha*rank*N_c**2,
    'N_c/(N_c*g)': N_c/(N_c*g),
    '1/(2*g)': 1/(2*g),
    'e^(-rank)': math.exp(-rank),
    'alpha*N_c*C_2+alpha': alpha*N_c*C_2+alpha,  # 19/137
    '(g-C_2)/g': (g-C_2)/g,
}

print(f"{'Expression':30s} {'Value':>12s} {'Dev from pi-3':>12s}")
print(f"{'-'*30} {'-'*12} {'-'*12}")

for name, val in sorted(candidates.items(), key=lambda x: abs(x[1] - residue)):
    dev = (val - residue) / residue * 100
    flag = ' ***' if abs(dev) < 5 else ''
    print(f"  {name:28s} {val:12.8f} {dev:+10.4f}%{flag}")

# Special check: does pi = N_c + 1/g + correction?
# pi = 3 + 1/7 + ...
print(f"\n  Continued fraction of pi - N_c:")
print(f"  pi - 3 = {residue:.10f}")
print(f"  1/7 = {1/7:.10f}")
print(f"  pi - 3 - 1/7 = {residue - 1/7:.10f}")
print(f"  This is ~0.001 -- very small!")
print(f"  So pi ~ N_c + 1/g + 0.001...")

# More precisely:
r2 = residue - 1/g
print(f"\n  pi - N_c - 1/g = {r2:.10f}")
print(f"  1/r2 = {1/r2:.4f}")
# 1/r2 should be close to an integer for continued fraction
print(f"  Continued fraction: pi = {N_c} + 1/{g} + ...")
print(f"  Next CF term: floor(1/r2) = {int(1/r2)}")
# pi = 3; 7, 15, 1, ...
# So pi = 3 + 1/(7 + 1/(15 + 1/(1 + ...)))
# The CF is [3; 7, 15, 1, 292, ...]
# BST: first term = N_c, second = g, third = N_c*n_C = 15!

r3 = 1/r2 - 15
print(f"  pi CF = [{N_c}; {g}, 15, ...]")
print(f"  15 = N_c * n_C = {N_c*n_C}")
print(f"  Residual: 1/r2 - 15 = {r3:.10f}")
print(f"  Next CF term: floor(1/r3) = {int(1/r3) if r3 > 0 else 'N/A'}")

# The CF of pi is [3; 7, 15, 1, 292, 1, 1, 1, 2, ...]
# First three terms: 3, 7, 15 = N_c, g, N_c*n_C
# This is significant!

print(f"\n  RESULT: pi = [{N_c}; {g}, {N_c*n_C}, 1, 292, ...]")
print(f"  First three CF terms of pi are BST integers:")
print(f"    3 = N_c")
print(f"    7 = g")
print(f"    15 = N_c * n_C")
print(f"  After that the CF becomes irregular (1, 292, 1, ...)")
print(f"  The BST connection is in the FIRST THREE terms only.")

# Approximation quality:
# [3;7] = 22/7 = 3.14286 (deviation from pi: 0.040%)
approx_1 = 22/7
dev_1 = abs(approx_1 - pi)/pi * 100
print(f"\n  Convergents:")
print(f"  [N_c; g] = 22/7 = {approx_1:.6f} ({dev_1:.4f}% from pi)")

# [3;7,15] = 3 + 1/(7 + 1/15) = 3 + 15/106 = 333/106
approx_2 = 333/106
dev_2 = abs(approx_2 - pi)/pi * 100
print(f"  [N_c; g, N_c*n_C] = 333/106 = {approx_2:.8f} ({dev_2:.6f}% from pi)")

# 106 = rank * 53. 53 = prime. Not obviously BST.
# 333 = N_c * 111 = N_c * N_c * 37 = N_c^2 * 37. 37 = 36+1 = N_c^2*rank^2+1 = (rank*N_c)^2+1
print(f"  333 = N_c^2 * 37 = N_c^2 * (N_c^2*rank^2 + 1)")
print(f"  106 = rank * 53")
print(f"  37 = Phi_4(C_2) = cyclotomic(4, 6) [from T1462!]")

# 37 IS Phi_4(6) = 6^2 - 6 + 1 = 31. Wait, Phi_4(x) = x^2+1. Phi_4(6)=37. YES!
phi4_6 = 6**2 + 1
print(f"  Phi_4(C_2) = C_2^2 + 1 = {phi4_6}")
print(f"  333/106 = N_c^2 * Phi_4(C_2) / (rank * 53)")

print(f"\n  TIER: I-tier (BST reading of pi's CF, structural)")
print(f"  The first three CF terms {N_c}, {g}, {N_c*n_C} are BST,")
print(f"  but this may be SELECTION BIAS: these are small integers")
print(f"  and BST primes {2,3,5,7} densely cover small integers.")
print(f"  HONEST: suggestive, not conclusive. Worth noting, not claiming.")
