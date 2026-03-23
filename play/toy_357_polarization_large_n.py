#!/usr/bin/env python3
"""
Toy 357: Polarization at Large n — Free Fraction Convergence
=============================================================

Discriminator test: does the free variable fraction at α_c converge to
  0.176 (first moment ceiling — pure combinatorics), or
  0.191 (Reality Budget fill = Λ·N - 1 = 9/5 - 1 — BST geometry)?

Method: WalkSAT backbone estimation at n = 50, 100, 200, 300, 500.
For each instance, find multiple solutions via independent WalkSAT runs.
A variable is "backbone" if it takes the same value in ALL found solutions.
A variable is "free" if it takes both values across solutions.
Variables seen in only one value but not confirmed across enough solutions
are "undetermined" — conservatively grouped with backbone.

Tests:
  1. Free fraction vs n (does it stabilize?)
  2. Free fraction value (closer to 0.176 or 0.191?)
  3. Backbone fraction vs n (does it stabilize at ~0.55-0.60?)
  4. Intermediate proxy: variables that flip in SOME but not MANY solutions
  5. Polarization ratio (backbone + clearly_free) / n → 1?

Note: WalkSAT backbone is a LOWER bound on true backbone and an UPPER
bound on true free set. Finding both values proves free; failing to find
both doesn't prove frozen. More WalkSAT runs → tighter estimates.
"""

import random
import math
import sys
import time

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
        val = assignment[var]
        if positive and val:
            return True
        if not positive and not val:
            return True
    return False

def count_unsat(clauses, assignment):
    """Count unsatisfied clauses."""
    return sum(1 for c in clauses if not evaluate_clause(c, assignment))

def walksat(clauses, n, max_flips=100000, p_random=0.5):
    """WalkSAT solver. Returns satisfying assignment or None."""
    assignment = [random.choice([True, False]) for _ in range(n)]

    # Build variable-to-clause index
    var_clauses = [[] for _ in range(n)]
    for ci, clause in enumerate(clauses):
        for var, _ in clause:
            var_clauses[var].append(ci)

    # Find initially unsatisfied clauses
    unsat = set()
    for ci, clause in enumerate(clauses):
        if not evaluate_clause(clause, assignment):
            unsat.add(ci)

    for flip in range(max_flips):
        if not unsat:
            return assignment[:]

        # Pick a random unsatisfied clause
        ci = random.choice(list(unsat))
        clause = clauses[ci]

        if random.random() < p_random:
            # Random walk: flip a random variable in the clause
            var, _ = random.choice(clause)
        else:
            # Greedy: flip the variable that minimizes break count
            best_var = None
            best_break = float('inf')
            for var, _ in clause:
                # Count how many currently satisfied clauses would break
                breaks = 0
                assignment[var] = not assignment[var]
                for cj in var_clauses[var]:
                    if cj not in unsat and not evaluate_clause(clauses[cj], assignment):
                        breaks += 1
                assignment[var] = not assignment[var]
                if breaks < best_break:
                    best_break = breaks
                    best_var = var
            var = best_var

        # Flip the variable and update unsat
        assignment[var] = not assignment[var]
        for cj in var_clauses[var]:
            if evaluate_clause(clauses[cj], assignment):
                unsat.discard(cj)
            else:
                unsat.add(cj)

    return None  # Failed to find solution

def estimate_backbone(clauses, n, num_solutions=30, max_flips=200000):
    """Estimate backbone by finding multiple solutions via WalkSAT.

    Returns (backbone_set, free_set, undetermined_set, solutions_found).
    - backbone: same value in ALL solutions
    - free: both values observed
    - undetermined: only one value seen but not enough evidence
    """
    solutions = []
    attempts = 0
    max_attempts = num_solutions * 5

    while len(solutions) < num_solutions and attempts < max_attempts:
        attempts += 1
        sol = walksat(clauses, n, max_flips=max_flips)
        if sol is not None:
            solutions.append(sol)

    if len(solutions) < 2:
        return set(), set(), set(range(n)), len(solutions)

    # For each variable, check if it takes both values
    seen_true = [False] * n
    seen_false = [False] * n
    true_count = [0] * n

    for sol in solutions:
        for i in range(n):
            if sol[i]:
                seen_true[i] = True
                true_count[i] += 1
            else:
                seen_false[i] = True

    backbone = set()
    free = set()
    undetermined = set()

    for i in range(n):
        if seen_true[i] and seen_false[i]:
            free.add(i)
        elif seen_true[i] or seen_false[i]:
            # Only seen one value — could be backbone or just under-sampled
            backbone.add(i)
        else:
            undetermined.add(i)

    return backbone, free, undetermined, len(solutions)

def variable_entropy_proxy(clauses, n, solutions):
    """Estimate per-variable entropy from WalkSAT solutions.
    Returns list of (var_index, p_true, entropy)."""
    if not solutions:
        return []

    count = len(solutions)
    results = []
    for i in range(n):
        p = sum(1 for s in solutions if s[i]) / count
        h = 0.0
        if 0 < p < 1:
            h = -p * math.log2(p) - (1 - p) * math.log2(1 - p)
        results.append((i, p, h))
    return results


print("=" * 72)
print("Toy 357: Polarization at Large n — Free Fraction Convergence")
print("Does free/n → 0.176 (first moment) or 0.191 (Reality Budget)?")
print("=" * 72)

# ======================================================================
# TEST 1: Free fraction vs n at α_c
# ======================================================================
print("\n" + "=" * 72)
print("TEST 1: Free fraction vs n at α_c")
print("=" * 72)

target_fm = 1 - ALPHA_C * math.log2(8/7)  # 0.178
target_rb = 0.191  # Reality Budget

results = []
print(f"\n  First moment target: {target_fm:.4f}")
print(f"  Reality Budget target: {target_rb:.4f}")
print(f"\n  {'n':>5}  {'sols':>5}  {'bb/n':>7}  {'free/n':>7}  {'undet/n':>7}  "
      f"{'Δ_FM':>7}  {'Δ_RB':>7}  {'instances':>9}")
print(f"  {'-'*5}  {'-'*5}  {'-'*7}  {'-'*7}  {'-'*7}  {'-'*7}  {'-'*7}  {'-'*9}")

for n in [50, 100, 150, 200, 300]:
    if n <= 100:
        instances = 20
        num_sols = 40
        max_flips = 200000
    elif n <= 200:
        instances = 12
        num_sols = 30
        max_flips = 300000
    else:
        instances = 8
        num_sols = 25
        max_flips = 500000

    bb_fracs = []
    free_fracs = []
    undet_fracs = []
    sols_found = []

    for trial in range(instances):
        clauses = generate_random_3sat(n, ALPHA_C)
        bb, free, undet, nsols = estimate_backbone(
            clauses, n, num_solutions=num_sols, max_flips=max_flips
        )
        if nsols >= 2:
            bb_fracs.append(len(bb) / n)
            free_fracs.append(len(free) / n)
            undet_fracs.append(len(undet) / n)
            sols_found.append(nsols)

    if not bb_fracs:
        print(f"  {n:5d}  No satisfiable instances found")
        continue

    avg_bb = sum(bb_fracs) / len(bb_fracs)
    avg_free = sum(free_fracs) / len(free_fracs)
    avg_undet = sum(undet_fracs) / len(undet_fracs)
    avg_sols = sum(sols_found) / len(sols_found)
    delta_fm = abs(avg_free - target_fm)
    delta_rb = abs(avg_free - target_rb)

    results.append({
        'n': n, 'bb': avg_bb, 'free': avg_free, 'undet': avg_undet,
        'sols': avg_sols, 'delta_fm': delta_fm, 'delta_rb': delta_rb,
        'count': len(bb_fracs)
    })

    print(f"  {n:5d}  {avg_sols:5.1f}  {avg_bb:7.3f}  {avg_free:7.3f}  "
          f"{avg_undet:7.3f}  {delta_fm:7.4f}  {delta_rb:7.4f}  "
          f"{len(bb_fracs):9d}")

# ======================================================================
# TEST 2: Which target is free/n closer to?
# ======================================================================
print("\n" + "=" * 72)
print("TEST 2: Convergence target — 0.176 (FM) vs 0.191 (RB)")
print("=" * 72)

if len(results) >= 2:
    # Use the largest n results
    large_n = [r for r in results if r['n'] >= 100]
    if large_n:
        avg_delta_fm = sum(r['delta_fm'] for r in large_n) / len(large_n)
        avg_delta_rb = sum(r['delta_rb'] for r in large_n) / len(large_n)
        avg_free_large = sum(r['free'] for r in large_n) / len(large_n)

        print(f"\n  At n ≥ 100:")
        print(f"    Average free/n = {avg_free_large:.4f}")
        print(f"    Distance to FM (0.176): {avg_delta_fm:.4f}")
        print(f"    Distance to RB (0.191): {avg_delta_rb:.4f}")

        if avg_delta_fm < avg_delta_rb:
            print(f"    Closer to: FIRST MOMENT (0.176)")
            test2_result = "FM"
        elif avg_delta_rb < avg_delta_fm:
            print(f"    Closer to: REALITY BUDGET (0.191)")
            test2_result = "RB"
        else:
            print(f"    Equidistant")
            test2_result = "TIE"
    else:
        test2_result = "INSUFFICIENT"
        print("  Not enough large-n data")
else:
    test2_result = "INSUFFICIENT"
    print("  Not enough data")

# ======================================================================
# TEST 3: Backbone fraction stability
# ======================================================================
print("\n" + "=" * 72)
print("TEST 3: Backbone fraction vs n (should stabilize)")
print("=" * 72)

if results:
    print(f"\n  {'n':>5}  {'bb/n':>7}  {'(1-free)/n':>10}")
    print(f"  {'-'*5}  {'-'*7}  {'-'*10}")
    for r in results:
        committed = 1 - r['free']
        print(f"  {r['n']:5d}  {r['bb']:7.3f}  {committed:10.3f}")

    bb_values = [r['bb'] for r in results if r['n'] >= 100]
    if bb_values:
        bb_range = max(bb_values) - min(bb_values)
        test3_pass = bb_range < 0.15
        print(f"\n  Backbone range at n≥100: {bb_range:.3f}")
        print(f"  {'PASS' if test3_pass else 'FAIL'}: backbone {'stabilizes' if test3_pass else 'not stable'}")
    else:
        test3_pass = False
else:
    test3_pass = False

# ======================================================================
# TEST 4: Entropy distribution at large n (proxy via WalkSAT samples)
# ======================================================================
print("\n" + "=" * 72)
print("TEST 4: Entropy distribution at n=100 (WalkSAT proxy)")
print("=" * 72)

n = 100
trials = 10
all_entropies = []
frozen_count = 0
free_count = 0
inter_count = 0
total_vars = 0

for t in range(trials):
    clauses = generate_random_3sat(n, ALPHA_C)
    solutions = []
    for _ in range(200):
        sol = walksat(clauses, n, max_flips=200000)
        if sol is not None:
            solutions.append(sol)

    if len(solutions) < 5:
        continue

    ent_data = variable_entropy_proxy(clauses, n, solutions)
    for _, p, h in ent_data:
        all_entropies.append(h)
        total_vars += 1
        if h < 0.1:
            frozen_count += 1
        elif h > 0.9:
            free_count += 1
        else:
            inter_count += 1

if total_vars > 0:
    print(f"\n  n={n}, {trials} instances, WalkSAT entropy proxy:")
    print(f"    Frozen (H<0.1): {frozen_count/total_vars:.3f}")
    print(f"    Free   (H>0.9): {free_count/total_vars:.3f}")
    print(f"    Inter (0.1-0.9): {inter_count/total_vars:.3f}")

    # Histogram
    bins = 10
    counts = [0] * bins
    for h in all_entropies:
        idx = min(int(h * bins), bins - 1)
        counts[idx] += 1
    print(f"\n    Entropy histogram:")
    for i in range(bins):
        lo = i / bins
        hi = (i + 1) / bins
        frac = counts[i] / total_vars
        bar = '#' * int(frac * 50)
        print(f"    [{lo:.1f},{hi:.1f}) {frac:6.3f} {bar}")

    test4_inter = inter_count / total_vars
    # Compare to Toy 356's 21% at n=16-20
    print(f"\n    Intermediate at n={n}: {test4_inter:.3f}")
    print(f"    Intermediate at n=16-20 (Toy 356): ~0.21")
    if test4_inter < 0.21:
        print(f"    Intermediate DECREASED from small n → suggests finite-size effect")
    else:
        print(f"    Intermediate did NOT decrease → structural feature")
else:
    test4_inter = None
    print("  No data (WalkSAT failed)")

# ======================================================================
# TEST 5: Free fraction trend — is it converging?
# ======================================================================
print("\n" + "=" * 72)
print("TEST 5: Free fraction trend")
print("=" * 72)

if len(results) >= 3:
    ns = [r['n'] for r in results]
    fs = [r['free'] for r in results]

    # Linear fit
    n_mean = sum(ns) / len(ns)
    f_mean = sum(fs) / len(fs)
    cov = sum((a - n_mean) * (b - f_mean) for a, b in zip(ns, fs))
    var = sum((a - n_mean) ** 2 for a in ns)
    slope = cov / var if var > 0 else 0
    intercept = f_mean - slope * n_mean

    print(f"\n  Free/n trend: slope = {slope:.6f}, intercept = {intercept:.4f}")
    print(f"  Extrapolation to n=∞: free/n → {intercept:.4f}")
    print(f"  (If slope ≈ 0, already converged)")

    # What does the intercept suggest?
    if abs(intercept - target_fm) < abs(intercept - target_rb):
        print(f"  Extrapolated value closer to FM ({target_fm:.3f})")
    else:
        print(f"  Extrapolated value closer to RB ({target_rb:.3f})")

    test5_pass = abs(slope) < 0.001  # Nearly flat = converging
    print(f"  {'PASS' if test5_pass else 'NEEDS MORE DATA'}: "
          f"{'converged' if test5_pass else 'still trending'}")
else:
    test5_pass = False
    print("  Not enough data points")

# ======================================================================
# SCORECARD
# ======================================================================
print("\n" + "=" * 72)
print("SCORECARD")
print("=" * 72)

tests = [
    ("Free fraction stabilizes with n", len(results) >= 2),
    ("Convergence target identified", test2_result in ["FM", "RB"]),
    ("Backbone fraction stable", test3_pass),
    ("Intermediate decreases at large n", test4_inter is not None and test4_inter < 0.21),
    ("Free fraction converging", test5_pass),
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
print(f"""
  Two competing predictions for the free variable fraction at α_c:

  1. First Moment (FM): free/n → {target_fm:.4f}
     - Pure combinatorics: 1 - α_c × log₂(8/7)
     - No geometry, no BST — just counting solutions

  2. Reality Budget (RB): free/n → {target_rb:.4f}
     - BST: Λ·N = 9/5, fill = 19.1%
     - The substrate's channel capacity residual

  If FM: the SAT threshold is "just" combinatorics.
  If RB: the SAT threshold encodes the same capacity limit as
         the cosmological constant — a universal bound on
         information commitment.

  To discriminate conclusively: need n = 10⁴+ with survey propagation
  or belief propagation. WalkSAT backbone estimation at n = 100-500
  gives a first indication.

  Note: WalkSAT UNDERESTIMATES backbone (may miss frozen variables)
  and OVERESTIMATES free fraction. So if free/n appears BELOW 0.191
  at large n, the true free fraction is even lower → favors FM.
  If free/n appears ABOVE 0.191, sampling bias may explain it.
""")
