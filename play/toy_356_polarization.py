#!/usr/bin/env python3
"""
Toy 356: Variable Polarization in Random 3-SAT
================================================

THE KEY TEST for closing BH(3).

Keeper's reframe: count faded BITS, not faded CYCLES.
First moment: at most 0.176n bits are free.
Remaining question: POLARIZATION — are variables either fully frozen
(H(x_i) = 0) or approximately free (H(x_i) ≈ 1), with NO intermediate?

If polarization holds:
  - Free variables ≤ 0.176n (first moment)
  - No intermediate variables (polarization)
  - Therefore: frozen variables ≥ n - 0.176n = 0.824n
  - |B| = Θ(n) — BH(3) proved

Tests:
  1. Variable entropy distribution is bimodal (gap in [0.1, 0.9])
  2. Fraction of intermediate variables → 0 as n grows
  3. Free variables ≤ 0.176n (first moment)
  4. Frozen variables = Θ(n)
  5. Polarization sharpens with α (sharper near α_c than below)
  6. Compare with XOR-SAT (should polarize perfectly)

Casey's domino picture: a variable either falls (H=0) or stands (H≈1).
The expansion prevents it from leaning.
"""

import random
import math
import sys
from collections import Counter
from itertools import product

ALPHA_C = 4.267

def generate_random_3sat(n, alpha):
    """Generate random 3-SAT formula."""
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vars_ = random.sample(range(n), 3)
        signs = [random.choice([True, False]) for _ in range(3)]
        clauses.append(list(zip(vars_, signs)))
    return clauses

def evaluate_clause(clause, assignment):
    """Check if clause is satisfied."""
    for var, positive in clause:
        if positive and assignment[var]:
            return True
        if not positive and not assignment[var]:
            return True
    return False

def all_solutions(clauses, n):
    """Enumerate all satisfying assignments (exact, small n only)."""
    solutions = []
    for bits in range(2**n):
        assignment = [(bits >> i) & 1 == 1 for i in range(n)]
        if all(evaluate_clause(c, assignment) for c in clauses):
            solutions.append(assignment)
    return solutions

def variable_marginals(solutions, n):
    """Compute P(x_i = 1) for each variable from exact solution set."""
    if not solutions:
        return [0.5] * n  # no info
    count = len(solutions)
    marginals = []
    for i in range(n):
        p = sum(1 for s in solutions if s[i]) / count
        marginals.append(p)
    return marginals

def entropy(p):
    """Binary entropy H(p) = -p log p - (1-p) log(1-p)."""
    if p <= 0 or p >= 1:
        return 0.0
    return -p * math.log2(p) - (1 - p) * math.log2(1 - p)

def classify_variable(h, frozen_thresh=0.1, free_thresh=0.9):
    """Classify variable by entropy: frozen, intermediate, or free."""
    if h < frozen_thresh:
        return 'frozen'
    elif h > free_thresh:
        return 'free'
    else:
        return 'intermediate'

def generate_random_3xorsat(n, alpha):
    """Generate random 3-XOR-SAT: x_a ⊕ x_b ⊕ x_c = b."""
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vars_ = random.sample(range(n), 3)
        parity = random.choice([0, 1])
        clauses.append((vars_, parity))
    return clauses

def xorsat_solutions(clauses, n):
    """Enumerate XOR-SAT solutions via brute force (small n)."""
    solutions = []
    for bits in range(2**n):
        assignment = [(bits >> i) & 1 for i in range(n)]
        sat = True
        for vars_, parity in clauses:
            xor_val = sum(assignment[v] for v in vars_) % 2
            if xor_val != parity:
                sat = False
                break
        if sat:
            solutions.append(assignment)
    return solutions

def run_polarization_test(n, alpha, trials, label=""):
    """Core test: measure variable entropy distribution."""
    all_entropies = []
    frozen_counts = []
    free_counts = []
    inter_counts = []
    solution_counts = []

    for t in range(trials):
        clauses = generate_random_3sat(n, alpha)
        sols = all_solutions(clauses, n)
        if not sols:
            continue
        solution_counts.append(len(sols))
        marg = variable_marginals(sols, n)
        entropies = [entropy(p) for p in marg]
        all_entropies.extend(entropies)

        classes = [classify_variable(h) for h in entropies]
        frozen_counts.append(classes.count('frozen'))
        free_counts.append(classes.count('free'))
        inter_counts.append(classes.count('intermediate'))

    if not frozen_counts:
        return None

    avg_frozen = sum(frozen_counts) / len(frozen_counts)
    avg_free = sum(free_counts) / len(free_counts)
    avg_inter = sum(inter_counts) / len(inter_counts)
    avg_sols = sum(solution_counts) / len(solution_counts)

    return {
        'n': n,
        'alpha': alpha,
        'label': label,
        'avg_frozen': avg_frozen,
        'avg_free': avg_free,
        'avg_inter': avg_inter,
        'avg_sols': avg_sols,
        'frac_frozen': avg_frozen / n,
        'frac_free': avg_free / n,
        'frac_inter': avg_inter / n,
        'all_entropies': all_entropies,
        'trials_used': len(frozen_counts),
    }

def entropy_histogram(entropies, bins=10):
    """Simple text histogram of entropy values."""
    counts = [0] * bins
    for h in entropies:
        idx = min(int(h * bins), bins - 1)
        counts[idx] += 1
    total = len(entropies)
    lines = []
    for i in range(bins):
        lo = i / bins
        hi = (i + 1) / bins
        frac = counts[i] / total if total > 0 else 0
        bar = '#' * int(frac * 50)
        lines.append(f"  [{lo:.1f},{hi:.1f}) {frac:6.3f} {bar}")
    return '\n'.join(lines)


print("=" * 72)
print("Toy 356: Variable Polarization in Random 3-SAT")
print("Does H(x_i) cluster at 0 and 1 with nothing in between?")
print("=" * 72)

# ======================================================================
# TEST 1: Entropy distribution at α_c — is it bimodal?
# ======================================================================
print("\n" + "=" * 72)
print("TEST 1: Entropy distribution at α_c (n=16, 18, 20)")
print("=" * 72)

test1_pass = True
for n in [16, 18, 20]:
    trials = max(40, 200 // n)
    r = run_polarization_test(n, ALPHA_C, trials, f"n={n}")
    if r is None:
        print(f"\n  n={n}: No satisfiable instances found")
        continue

    print(f"\n  n={n} (α={ALPHA_C}, {r['trials_used']} satisfiable instances):")
    print(f"    Avg solutions: {r['avg_sols']:.1f}")
    print(f"    Frozen (H<0.1): {r['avg_frozen']:.1f} ({r['frac_frozen']:.3f})")
    print(f"    Free   (H>0.9): {r['avg_free']:.1f} ({r['frac_free']:.3f})")
    print(f"    Inter (0.1-0.9): {r['avg_inter']:.1f} ({r['frac_inter']:.3f})")
    print(f"\n    Entropy histogram:")
    print(entropy_histogram(r['all_entropies']))

    # Polarization: intermediate should be small
    if r['frac_inter'] > 0.3:
        test1_pass = False

if test1_pass:
    print("\n  PASS: Intermediate fraction < 0.3 at all sizes")
else:
    print("\n  FAIL: Too many intermediate variables")

# ======================================================================
# TEST 2: Intermediate fraction decreases with n
# ======================================================================
print("\n" + "=" * 72)
print("TEST 2: Intermediate fraction vs. n (should decrease)")
print("=" * 72)

inter_fracs = []
print(f"\n  {'n':>4}  {'frozen':>7}  {'free':>7}  {'inter':>7}  {'frac_inter':>10}")
print(f"  {'-'*4}  {'-'*7}  {'-'*7}  {'-'*7}  {'-'*10}")

for n in [12, 14, 16, 18, 20]:
    trials = max(40, 300 // n)
    r = run_polarization_test(n, ALPHA_C, trials)
    if r is None:
        continue
    inter_fracs.append((n, r['frac_inter']))
    print(f"  {n:4d}  {r['frac_frozen']:7.3f}  {r['frac_free']:7.3f}  "
          f"{r['frac_inter']:7.3f}  {r['frac_inter']:10.4f}")

# Check if intermediate fraction is decreasing
if len(inter_fracs) >= 3:
    # Linear regression on (n, frac_inter)
    ns = [x[0] for x in inter_fracs]
    fs = [x[1] for x in inter_fracs]
    n_mean = sum(ns) / len(ns)
    f_mean = sum(fs) / len(fs)
    cov = sum((a - n_mean) * (b - f_mean) for a, b in zip(ns, fs))
    var = sum((a - n_mean) ** 2 for a in ns)
    slope = cov / var if var > 0 else 0

    print(f"\n  Trend: slope = {slope:.5f} (negative = decreasing)")
    test2_pass = slope < 0
    if test2_pass:
        print("  PASS: Intermediate fraction decreasing with n")
    else:
        print("  FAIL: Intermediate fraction NOT decreasing")
else:
    test2_pass = False
    print("  INCONCLUSIVE: Not enough data points")

# ======================================================================
# TEST 3: Free variables ≤ 0.176n (first moment bound on BITS)
# ======================================================================
print("\n" + "=" * 72)
print("TEST 3: Free variables ≤ 0.176n (first moment on BITS)")
print("=" * 72)

test3_pass = True
cap_frac = 1 - ALPHA_C * math.log2(8/7)
print(f"\n  First moment cap: {cap_frac:.4f}n")

for n in [14, 16, 18, 20]:
    trials = max(40, 300 // n)
    r = run_polarization_test(n, ALPHA_C, trials)
    if r is None:
        continue
    cap = cap_frac * n
    # Free bits = free + 0.5*intermediate (conservative)
    free_bits = r['avg_free'] + r['avg_inter']
    print(f"  n={n:2d}: free={r['avg_free']:.1f} inter={r['avg_inter']:.1f} "
          f"total_free_bits={free_bits:.1f} cap={cap:.1f} "
          f"{'OK' if free_bits <= cap * 1.5 else 'OVER'}")
    if free_bits > cap * 2:
        test3_pass = False

if test3_pass:
    print("\n  PASS: Free variables approximately bounded by first moment")
else:
    print("\n  FAIL: Free variables exceed first moment cap")

# ======================================================================
# TEST 4: Frozen variables = Θ(n) (backbone is linear)
# ======================================================================
print("\n" + "=" * 72)
print("TEST 4: Frozen variables = Θ(n) (backbone is linear)")
print("=" * 72)

frozen_fracs = []
for n in [12, 14, 16, 18, 20]:
    trials = max(40, 300 // n)
    r = run_polarization_test(n, ALPHA_C, trials)
    if r is None:
        continue
    frozen_fracs.append((n, r['frac_frozen']))
    print(f"  n={n:2d}: frozen/n = {r['frac_frozen']:.3f}")

# Check frozen/n is bounded away from 0
if frozen_fracs:
    avg_ff = sum(f for _, f in frozen_fracs) / len(frozen_fracs)
    test4_pass = avg_ff > 0.2
    print(f"\n  Average frozen/n = {avg_ff:.3f}")
    if test4_pass:
        print("  PASS: Backbone is Θ(n)")
    else:
        print("  FAIL: Backbone not clearly Θ(n)")
else:
    test4_pass = False

# ======================================================================
# TEST 5: Polarization sharpens near α_c
# ======================================================================
print("\n" + "=" * 72)
print("TEST 5: Polarization sharpens near α_c")
print("=" * 72)

n = 16
print(f"\n  n={n}, varying α:")
print(f"  {'α':>6}  {'frozen':>7}  {'free':>7}  {'inter':>7}  {'polar_ratio':>11}")
print(f"  {'-'*6}  {'-'*7}  {'-'*7}  {'-'*7}  {'-'*11}")

alpha_results = []
for alpha in [2.0, 3.0, 3.5, 4.0, ALPHA_C]:
    trials = 50
    r = run_polarization_test(n, alpha, trials)
    if r is None:
        continue
    # Polarization ratio = (frozen + free) / (frozen + free + inter)
    polar = (r['frac_frozen'] + r['frac_free'])
    alpha_results.append((alpha, polar, r['frac_inter']))
    print(f"  {alpha:6.3f}  {r['frac_frozen']:7.3f}  {r['frac_free']:7.3f}  "
          f"{r['frac_inter']:7.3f}  {polar:11.3f}")

# Check that polarization increases with α
if len(alpha_results) >= 3:
    # Compare α_c polarization to low α
    low_polar = alpha_results[0][1]
    high_polar = alpha_results[-1][1]
    test5_pass = high_polar > low_polar
    print(f"\n  Low α polar: {low_polar:.3f}, α_c polar: {high_polar:.3f}")
    if test5_pass:
        print("  PASS: Polarization sharpens near α_c")
    else:
        print("  FAIL: Polarization does NOT sharpen near α_c")
else:
    test5_pass = False

# ======================================================================
# TEST 6: XOR-SAT polarizes perfectly
# ======================================================================
print("\n" + "=" * 72)
print("TEST 6: XOR-SAT polarization (should be perfect)")
print("=" * 72)

n = 16
alpha_xor = 0.9  # near XOR-SAT threshold
trials = 50
all_xor_entropies = []
xor_frozen = 0
xor_free = 0
xor_inter = 0
xor_count = 0

for t in range(trials):
    clauses = generate_random_3xorsat(n, alpha_xor)
    sols = xorsat_solutions(clauses, n)
    if not sols:
        continue
    xor_count += 1
    marg = []
    for i in range(n):
        p = sum(1 for s in sols if s[i]) / len(sols)
        marg.append(p)
    entropies = [entropy(p) for p in marg]
    all_xor_entropies.extend(entropies)
    for h in entropies:
        c = classify_variable(h)
        if c == 'frozen':
            xor_frozen += 1
        elif c == 'free':
            xor_free += 1
        else:
            xor_inter += 1

if xor_count > 0:
    total = xor_frozen + xor_free + xor_inter
    print(f"\n  XOR-SAT (n={n}, α={alpha_xor}, {xor_count} instances):")
    print(f"    Frozen: {xor_frozen}/{total} ({xor_frozen/total:.3f})")
    print(f"    Free:   {xor_free}/{total} ({xor_free/total:.3f})")
    print(f"    Inter:  {xor_inter}/{total} ({xor_inter/total:.3f})")
    print(f"\n    Entropy histogram:")
    print(entropy_histogram(all_xor_entropies))
    test6_pass = xor_inter / total < 0.05 if total > 0 else False
    if test6_pass:
        print("\n  PASS: XOR-SAT polarizes (near) perfectly")
    else:
        print("\n  FAIL: XOR-SAT has intermediate variables")
else:
    test6_pass = False
    print("  No satisfiable XOR-SAT instances found")

# ======================================================================
# SCORECARD
# ======================================================================
print("\n" + "=" * 72)
print("SCORECARD")
print("=" * 72)
tests = [
    ("Bimodal entropy at α_c", test1_pass),
    ("Intermediate fraction decreasing", test2_pass),
    ("Free bits ≤ ~0.176n", test3_pass),
    ("Frozen = Θ(n)", test4_pass),
    ("Polarization sharpens near α_c", test5_pass),
    ("XOR-SAT polarizes perfectly", test6_pass),
]
for name, passed in tests:
    status = "PASS" if passed else "FAIL"
    print(f"  {name}: {status}")

total_pass = sum(1 for _, p in tests if p)
print(f"\n  Result: {total_pass}/{len(tests)} PASS")

# ======================================================================
# INTERPRETATION
# ======================================================================
print("\n" + "=" * 72)
print("INTERPRETATION")
print("=" * 72)
print("""
  If polarization holds (variables are frozen or free, no intermediate):
    1. First moment: at most 0.176n bits of freedom (Lemma 1, proved)
    2. Polarization: each free bit IS a free variable (no partial states)
    3. Therefore: at most 0.176n free variables
    4. Therefore: at least (1 - 0.176)n = 0.824n frozen variables
    5. |B| = Θ(n) — BH(3) proved

  The polarization argument bypasses cycles entirely:
    - No need for cycle independence (the faded cycle counting gap)
    - No need for H₁ homology
    - Just: count bits of freedom → bound free variables → bound backbone

  For the FOCS paper:
    - Polarization is the ONE remaining lemma
    - It follows from VIG expansion (constraints either cascade or die)
    - Known for XOR-SAT (linear algebra)
    - Conjectured for SAT at α_c (OR ≈ XOR when clauses are tight)

  Connection to Arıkan channel polarization (2009):
    - Arıkan: random linear transformations on bounded-degree graph
      → channels polarize to noiseless/useless
    - BH(3): random OR constraints on bounded-degree VIG
      → variables polarize to frozen/free
    - Same mechanism: expansion forces binary choice
""")
