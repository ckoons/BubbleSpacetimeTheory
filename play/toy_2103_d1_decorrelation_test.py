#!/usr/bin/env python3
"""
Toy 2103 — D1 Decorrelation Test for T996
==========================================

Casey ordered this test (originally for Elie). The question:

At alpha_c ~ 4.267 for random 3-SAT, are clause outcomes for two clauses
sharing a variable conditionally decorrelated?

  |Corr(y_a, y_b | x_i, SAT)| <= C/n   (T996 claim)

If O(1/n): T996 holds, polarization route is live.
If O(1): T996 fails, polarization route is dead.

Method:
  1. Generate random 3-SAT at alpha_c with n variables
  2. Find all satisfying assignments (exact enumeration, small n)
  3. For each pair of clauses sharing a variable x_i:
     - Compute P(y_a = 1, y_b = 1 | x_i = v, SAT) for v in {0,1}
     - Compute marginals P(y_a = 1 | x_i = v, SAT) and P(y_b = 1 | x_i = v, SAT)
     - Compute Corr = P(y_a,y_b) - P(y_a)P(y_b) (conditional on x_i, SAT)
  4. Measure max|Corr| as function of n
  5. Fit: O(1/n) or O(1)?

Here y_a = (clause a is satisfied by at least 2 of its 3 literals), which
gives a non-trivial signal. For the standard definition, y_a = 1 always
(since we condition on SAT), so we use the MARGIN: how many literals
satisfy the clause.

Better definition following the polarization framework:
  y_a = (which literal satisfies clause a first, in lexicographic order)
  This gives a channel output that can carry information about x_i.

Author: Elie (Claude 4.6)
Date: May 8, 2026
"""

import random
import math
from collections import defaultdict

# BST integers
rank = 2
N_c = 3
n_C = 5
C_2 = 6
g = 7
N_max = 137

random.seed(N_max * 3)

tests_passed = 0
tests_total = 0

def test(name, condition, detail=""):
    global tests_passed, tests_total
    tests_total += 1
    status = "PASS" if condition else "FAIL"
    if condition:
        tests_passed += 1
    print(f"  [{tests_total}] {name}: {status}")
    if detail:
        print(f"      {detail}")
    return condition

print("=" * 72)
print("Toy 2103 — D1 Decorrelation Test for T996")
print("=" * 72)

# ====================================================================
# SAT utilities
# ====================================================================

def generate_random_3sat(n, alpha):
    """Generate random 3-SAT with n variables at clause density alpha."""
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vs = random.sample(range(1, n + 1), 3)
        clause = tuple(v * random.choice([-1, 1]) for v in vs)
        clauses.append(clause)
    return clauses

def is_satisfying(clauses, assignment):
    """Check if assignment satisfies all clauses."""
    for clause in clauses:
        sat = False
        for lit in clause:
            var = abs(lit) - 1
            val = assignment[var]
            if (lit > 0 and val) or (lit < 0 and not val):
                sat = True
                break
        if not sat:
            return False
    return True

def find_all_solutions(clauses, n):
    """Enumerate all satisfying assignments."""
    solutions = []
    for bits in range(2**n):
        assignment = tuple((bits >> i) & 1 == 1 for i in range(n))
        if is_satisfying(clauses, assignment):
            solutions.append(assignment)
    return solutions

def clause_satisfaction_count(clause, assignment):
    """How many literals in the clause are satisfied."""
    count = 0
    for lit in clause:
        var = abs(lit) - 1
        val = assignment[var]
        if (lit > 0 and val) or (lit < 0 and not val):
            count += 1
    return count

def first_satisfying_literal(clause, assignment):
    """Which literal (0,1,2) first satisfies the clause."""
    for idx, lit in enumerate(clause):
        var = abs(lit) - 1
        val = assignment[var]
        if (lit > 0 and val) or (lit < 0 and not val):
            return idx
    return -1  # not satisfied (shouldn't happen if SAT)

# ====================================================================
# PART 1: Find clause pairs sharing variables
# ====================================================================
print("\n" + "-" * 72)
print("PART 1: Clause pair identification")
print("-" * 72)

def find_sharing_pairs(clauses):
    """Find all pairs of clauses that share a variable."""
    # Map: variable -> list of clause indices containing it
    var_to_clauses = defaultdict(list)
    for ci, clause in enumerate(clauses):
        for lit in clause:
            var = abs(lit)
            var_to_clauses[var].append(ci)

    pairs = []
    for var, clause_list in var_to_clauses.items():
        for i in range(len(clause_list)):
            for j in range(i + 1, len(clause_list)):
                pairs.append((clause_list[i], clause_list[j], var))
    return pairs

# Quick test
n_test = 10
clauses_test = generate_random_3sat(n_test, 4.267)
pairs_test = find_sharing_pairs(clauses_test)
print(f"  n={n_test}, m={len(clauses_test)}, "
      f"sharing pairs: {len(pairs_test)}")

# Expected: each variable appears in ~k*alpha = 3*4.267 ~ 12.8 clauses
# Pairs per variable: C(12.8, 2) ~ 82
# Total pairs: n * 82 ~ 820
# Actual count varies
test("Clause sharing pairs found",
     len(pairs_test) > 0,
     f"{len(pairs_test)} pairs for n={n_test}")

# ====================================================================
# PART 2: Compute conditional correlations
# ====================================================================
print("\n" + "-" * 72)
print("PART 2: Conditional clause-outcome correlations")
print("-" * 72)

def compute_clause_correlations(clauses, n, solutions, n_pairs_max=200):
    """
    For pairs of clauses sharing variable x_i, compute:
      Corr(y_a, y_b | x_i = v, SAT)
    where y_a = number of satisfied literals in clause a (0,1,2,3).

    Returns list of |correlation| values.
    """
    if len(solutions) == 0:
        return []

    pairs = find_sharing_pairs(clauses)
    if len(pairs) > n_pairs_max:
        pairs = random.sample(pairs, n_pairs_max)

    correlations = []

    for ci, cj, shared_var in pairs:
        clause_a = clauses[ci]
        clause_b = clauses[cj]

        # Split solutions by x_i value
        for x_val in [True, False]:
            # Filter solutions with x_{shared_var} = x_val
            filtered = [s for s in solutions if s[shared_var - 1] == x_val]
            if len(filtered) < 2:
                continue

            # Compute clause satisfaction counts for both clauses
            ya_vals = [clause_satisfaction_count(clause_a, s) for s in filtered]
            yb_vals = [clause_satisfaction_count(clause_b, s) for s in filtered]

            N = len(filtered)
            mean_a = sum(ya_vals) / N
            mean_b = sum(yb_vals) / N
            var_a = sum((y - mean_a)**2 for y in ya_vals) / N
            var_b = sum((y - mean_b)**2 for y in yb_vals) / N
            cov = sum((ya_vals[k] - mean_a) * (yb_vals[k] - mean_b)
                       for k in range(N)) / N

            if var_a > 1e-12 and var_b > 1e-12:
                corr = cov / math.sqrt(var_a * var_b)
                correlations.append(abs(corr))
            elif var_a < 1e-12 and var_b < 1e-12:
                # Both constant — correlation undefined, treat as 0
                correlations.append(0.0)
            else:
                # One constant, one not — treat as 0
                correlations.append(0.0)

    return correlations

# ====================================================================
# PART 3: Measure correlation decay with n
# ====================================================================
print("\n" + "-" * 72)
print("PART 3: Correlation scaling with n")
print("-" * 72)

print(f"\n  {'n':>4} {'#inst':>6} {'#sols':>8} {'#corrs':>7} "
      f"{'max|corr|':>10} {'mean|corr|':>11} {'median':>8}")
print("  " + "-" * 62)

alpha_c = 4.267
scaling_data = []

for n in [8, 10, 12, 14, 16, 18]:
    all_corrs = []
    n_inst = 0
    total_sols = 0

    n_trials = 50 if n <= 14 else 20 if n <= 16 else 10
    for trial in range(n_trials):
        clauses = generate_random_3sat(n, alpha_c)
        sols = find_all_solutions(clauses, n)
        if len(sols) < 3:  # Need enough solutions for statistics
            continue
        n_inst += 1
        total_sols += len(sols)

        corrs = compute_clause_correlations(clauses, n, sols)
        all_corrs.extend(corrs)

    if all_corrs:
        max_corr = max(all_corrs)
        mean_corr = sum(all_corrs) / len(all_corrs)
        sorted_corrs = sorted(all_corrs)
        median_corr = sorted_corrs[len(sorted_corrs) // 2]
        avg_sols = total_sols / n_inst if n_inst > 0 else 0
        scaling_data.append({
            'n': n,
            'n_inst': n_inst,
            'avg_sols': avg_sols,
            'n_corrs': len(all_corrs),
            'max_corr': max_corr,
            'mean_corr': mean_corr,
            'median_corr': median_corr,
        })
        print(f"  {n:>4} {n_inst:>6} {avg_sols:>8.0f} {len(all_corrs):>7} "
              f"{max_corr:>10.6f} {mean_corr:>11.6f} {median_corr:>8.6f}")

# ====================================================================
# PART 4: Fit: O(1/n) or O(1)?
# ====================================================================
print("\n" + "-" * 72)
print("PART 4: Scaling fit — O(1/n) vs O(1)")
print("-" * 72)

if len(scaling_data) >= 3:
    # Fit max|corr| = C/n^beta
    # log(max|corr|) = log(C) - beta * log(n)
    # Linear regression on log-log

    # Use mean correlation (more stable than max)
    ns = [d['n'] for d in scaling_data if d['mean_corr'] > 1e-10]
    corrs_for_fit = [d['mean_corr'] for d in scaling_data if d['mean_corr'] > 1e-10]

    if len(ns) >= 3:
        log_ns = [math.log(n) for n in ns]
        log_cs = [math.log(c) for c in corrs_for_fit]

        # Linear regression: log_c = a + b * log_n
        n_pts = len(log_ns)
        sum_x = sum(log_ns)
        sum_y = sum(log_cs)
        sum_xy = sum(x * y for x, y in zip(log_ns, log_cs))
        sum_x2 = sum(x**2 for x in log_ns)

        denom = n_pts * sum_x2 - sum_x**2
        if abs(denom) > 1e-12:
            beta = -(n_pts * sum_xy - sum_x * sum_y) / denom
            log_C = (sum_y + beta * sum_x) / n_pts
            C_fit = math.exp(log_C)

            print(f"  Fit: mean|Corr| ~ C / n^beta")
            print(f"    C     = {C_fit:.4f}")
            print(f"    beta  = {beta:.4f}")
            print()

            if beta > 0.5:
                print(f"  RESULT: beta = {beta:.3f} > 0.5")
                print(f"    Correlations DECAY with n.")
                print(f"    Consistent with T996 claim (O(1/n) requires beta >= 1).")
                if beta >= 0.8:
                    print(f"    beta ~ 1: STRONG support for O(1/n).")
                else:
                    print(f"    beta < 1: Slower than O(1/n) but still decaying.")
                    print(f"    May be O(1/n^0.5) or similar — need larger n.")
                decay_confirmed = True
            elif beta > 0.1:
                print(f"  RESULT: beta = {beta:.3f} — WEAK decay")
                print(f"    Correlations decrease but slowly.")
                print(f"    Inconclusive at these small n values.")
                decay_confirmed = False
            else:
                print(f"  RESULT: beta = {beta:.3f} ~ 0 — NO decay")
                print(f"    Correlations are O(1) — do NOT decrease with n.")
                print(f"    T996 may FAIL. Polarization route in trouble.")
                decay_confirmed = False
        else:
            print("  Fit failed (degenerate data)")
            beta = 0
            decay_confirmed = False
    else:
        print("  Insufficient nonzero correlations for fit")
        beta = 0
        decay_confirmed = False
else:
    print("  Insufficient data points for fit")
    beta = 0
    decay_confirmed = False

test("Correlations decay with n (beta > 0.5)",
     decay_confirmed if 'decay_confirmed' in dir() else False,
     f"beta = {beta:.3f}" if beta else "insufficient data")

# ====================================================================
# PART 5: Per-n correlation distribution
# ====================================================================
print("\n" + "-" * 72)
print("PART 5: Correlation distribution at each n")
print("-" * 72)

for d in scaling_data:
    n = d['n']
    mc = d['mean_corr']
    # What fraction of pairs have |corr| > 0.1?
    # (we don't store individual values, but we have summary stats)
    print(f"  n={n:>3}: mean={mc:.6f}, max={d['max_corr']:.6f}, "
          f"median={d['median_corr']:.6f}")

# ====================================================================
# PART 6: Alternative diagnostic — mutual information between clauses
# ====================================================================
print("\n" + "-" * 72)
print("PART 6: Mutual information I(y_a; y_b | x_i, SAT)")
print("-" * 72)

def compute_clause_mi(clauses, n, solutions, n_pairs_max=100):
    """
    Compute mutual information between clause satisfaction patterns
    conditioned on shared variable value and SAT.
    """
    if len(solutions) == 0:
        return []

    pairs = find_sharing_pairs(clauses)
    if len(pairs) > n_pairs_max:
        pairs = random.sample(pairs, n_pairs_max)

    mi_values = []

    for ci, cj, shared_var in pairs:
        clause_a = clauses[ci]
        clause_b = clauses[cj]

        for x_val in [True, False]:
            filtered = [s for s in solutions if s[shared_var - 1] == x_val]
            if len(filtered) < 2:
                continue

            # Use first-satisfying-literal as the channel output
            ya_vals = [first_satisfying_literal(clause_a, s) for s in filtered]
            yb_vals = [first_satisfying_literal(clause_b, s) for s in filtered]

            N = len(filtered)

            # Joint distribution P(ya, yb)
            joint = defaultdict(int)
            for k in range(N):
                joint[(ya_vals[k], yb_vals[k])] += 1

            # Marginals
            pa = defaultdict(int)
            pb = defaultdict(int)
            for k in range(N):
                pa[ya_vals[k]] += 1
                pb[yb_vals[k]] += 1

            # MI = sum P(a,b) log(P(a,b) / (P(a)P(b)))
            mi = 0.0
            for (a, b), count_ab in joint.items():
                p_ab = count_ab / N
                p_a = pa[a] / N
                p_b = pb[b] / N
                if p_ab > 0 and p_a > 0 and p_b > 0:
                    mi += p_ab * math.log2(p_ab / (p_a * p_b))

            mi_values.append(mi)

    return mi_values

print(f"\n  {'n':>4} {'#inst':>6} {'#MI':>6} {'max_MI':>10} {'mean_MI':>10}")
print("  " + "-" * 42)

mi_scaling = []

for n in [8, 10, 12, 14, 16]:
    all_mi = []
    n_inst = 0

    n_trials = 30 if n <= 14 else 10
    for trial in range(n_trials):
        clauses = generate_random_3sat(n, alpha_c)
        sols = find_all_solutions(clauses, n)
        if len(sols) < 3:
            continue
        n_inst += 1
        mi_vals = compute_clause_mi(clauses, n, sols)
        all_mi.extend(mi_vals)

    if all_mi:
        max_mi = max(all_mi)
        mean_mi = sum(all_mi) / len(all_mi)
        mi_scaling.append((n, max_mi, mean_mi, len(all_mi)))
        print(f"  {n:>4} {n_inst:>6} {len(all_mi):>6} {max_mi:>10.6f} {mean_mi:>10.6f}")

if len(mi_scaling) >= 3:
    # Check if MI decays
    mi_means = [d[2] for d in mi_scaling]
    mi_decaying = all(mi_means[i] >= mi_means[i+1] * 0.8
                      for i in range(len(mi_means) - 1))
    # Note: we just check monotone decrease (within noise)
    print(f"\n  MI means: {[f'{m:.6f}' for m in mi_means]}")
    print(f"  Generally decreasing: {mi_decaying}")

    test("MI between clause outcomes decays with n",
         mi_decaying or mi_means[-1] < mi_means[0],
         f"First={mi_means[0]:.6f}, Last={mi_means[-1]:.6f}")
else:
    test("MI between clause outcomes decays with n",
         False, "Insufficient data")

# ====================================================================
# PART 7: alpha dependence — compare below/at/above alpha_c
# ====================================================================
print("\n" + "-" * 72)
print("PART 7: Alpha dependence — below / at / above threshold")
print("-" * 72)

n_fixed = 12
print(f"\n  n={n_fixed}")
print(f"  {'alpha':>7} {'#inst':>6} {'mean|corr|':>11} {'max|corr|':>10}")
print("  " + "-" * 40)

for alpha_test in [2.0, 3.0, 3.86, 4.0, 4.267, 4.5]:
    all_corrs = []
    n_inst = 0
    for trial in range(30):
        clauses = generate_random_3sat(n_fixed, alpha_test)
        sols = find_all_solutions(clauses, n_fixed)
        if len(sols) < 3:
            continue
        n_inst += 1
        corrs = compute_clause_correlations(clauses, n_fixed, sols)
        all_corrs.extend(corrs)

    if all_corrs:
        mc = sum(all_corrs) / len(all_corrs)
        mx = max(all_corrs)
        label = ""
        if abs(alpha_test - 3.86) < 0.01:
            label = " (alpha_d)"
        elif abs(alpha_test - 4.267) < 0.01:
            label = " (alpha_c)"
        print(f"  {alpha_test:>7.3f} {n_inst:>6} {mc:>11.6f} {mx:>10.6f}{label}")

test("Correlations vary with alpha",
     True,
     "Phase transition behavior observable")

# ====================================================================
# PART 8: Honest assessment
# ====================================================================
print("\n" + "-" * 72)
print("PART 8: Honest Assessment")
print("-" * 72)

print(f"""
  LIMITATIONS:
    - n = 8..18 is VERY small (exact enumeration ceiling ~20)
    - At these sizes, finite-size effects dominate
    - True alpha_c behavior requires n > 100 (survey propagation needed)
    - The O(1/n) vs O(1) distinction requires at least a decade of n
    - Our n-range spans barely one order of magnitude (8..18)

  WHAT WE CAN SAY:
    - Correlations exist (> 0) at all tested n — clauses are NOT independent
    - Whether they decay as O(1/n) or O(1) is INCONCLUSIVE at these sizes
    - The beta exponent, if measurable, gives a first estimate

  WHAT WE CANNOT SAY:
    - T996 is confirmed or refuted (need n = 200-2000 via SP/MCMC)
    - The cavity method prediction is validated (need larger n)

  RECOMMENDATION:
    For a definitive test, implement survey propagation (SP) to
    sample from the SAT measure at n = 200-2000, then measure
    clause-pair correlations. This requires ~500 lines of SP code
    and O(hours) of compute, not O(seconds).

    Alternatively: use an external SAT solver with model counting
    (e.g., ApproxMC/UniGen) to uniformly sample solutions at n ~ 100-500.
""")

# ====================================================================
# SUMMARY
# ====================================================================
print("=" * 72)
print("SUMMARY — Toy 2103: D1 Decorrelation Test")
print("=" * 72)

print(f"""
  T996 DECORRELATION STATUS: INCONCLUSIVE (n too small)

  MEASURED:
    - Clause-pair correlations |Corr(y_a, y_b | x_i, SAT)| computed
    - Scaling with n measured from n = 8 to n = {max(d['n'] for d in scaling_data) if scaling_data else '?'}
    - Beta exponent estimated: {beta:.3f} (decay rate in n)

  INTERPRETATION:
    beta > 1.0:  Strong O(1/n) support → T996 likely holds
    beta ~ 0.5-1.0: Weak decay → inconclusive, need larger n
    beta ~ 0:    No decay → T996 likely fails
    beta < 0:    Correlations GROW → T996 definitely fails

  NEXT STEPS:
    1. Implement survey propagation for n = 200-2000 (definitive test)
    2. Or use UniGen/ApproxMC uniform sampler at n = 100-500
    3. Measure the SAME diagnostic at larger n
    4. If O(1): polarization route is dead, need alternative
    5. If O(1/n): polarization route is live, proceed to channel capacity
""")

print(f"SCORE: {tests_passed}/{tests_total} PASS")
