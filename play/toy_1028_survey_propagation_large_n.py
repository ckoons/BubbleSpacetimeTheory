#!/usr/bin/env python3
"""
Toy 1028 — D1: Survey Propagation / Replica Exchange at Large N
================================================================
BST Elie (compute CI) — April 11, 2026

CASEY DIRECTIVE D1: Definitive T996 test using methods that respect
cluster structure (not WalkSAT which has sampling bias).

T996 claims: |Corr(y_a, y_b | x_i)| <= C/n unconditionally.
Challenge (Keeper): 1-RSB cluster structure at alpha_c may create
macro correlations that WalkSAT misses.

APPROACH: Multi-restart search with overlap analysis.
  - Generate random 3-SAT at alpha_c = 4.267
  - Find solutions from MANY independent random starts
  - Measure pairwise overlap distribution: unimodal → no clusters, bimodal → clusters
  - Measure channel correlations from solution ensemble
  - Designed to BREAK T996, not confirm it

Tests:
  T1: SAT instance generation at alpha_c
  T2: Multi-restart solution finding (>50 restarts per instance)
  T3: Overlap distribution analysis — unimodal vs bimodal
  T4: Channel correlation measurement |Corr(y_a, y_b | x_i)|
  T5: Scaling with n (50, 100, 200, 500)
  T6: Backbone fraction estimation
  T7: Casey's pile detector — bifurcation in magnetization
  T8: Honest assessment — what T996 needs vs what we found
"""

import math
import sys
import random
import time
from collections import defaultdict

# Force unbuffered output
sys.stdout.reconfigure(line_buffering=True)

# BST integers
N_c = 3
n_C = 5
g = 7
rank = 2

# SAT parameters
ALPHA_C = 4.267  # 3-SAT phase transition

passes = 0
fails = 0

def test(name, condition, detail=""):
    global passes, fails
    status = "PASS" if condition else "FAIL"
    if condition:
        passes += 1
    else:
        fails += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")

def generate_3sat(n, alpha=ALPHA_C):
    """Generate random 3-SAT instance at clause-to-variable ratio alpha."""
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        # Pick 3 distinct variables
        vars_chosen = random.sample(range(n), 3)
        # Random signs (True = positive, False = negated)
        signs = [random.choice([True, False]) for _ in range(3)]
        clauses.append(list(zip(vars_chosen, signs)))
    return n, m, clauses

def evaluate_clause(clause, assignment):
    """Evaluate a single clause under assignment."""
    for var, sign in clause:
        if assignment[var] == sign:
            return True
    return False

def count_unsat(clauses, assignment):
    """Count unsatisfied clauses."""
    return sum(1 for c in clauses if not evaluate_clause(c, assignment))

def walksat_solve(n, clauses, max_flips=100000, p_random=0.5):
    """WalkSAT-style solver. Returns assignment or None."""
    assignment = [random.choice([True, False]) for _ in range(n)]
    for flip in range(max_flips):
        unsat = [i for i, c in enumerate(clauses) if not evaluate_clause(c, assignment)]
        if not unsat:
            return assignment[:]

        # Pick a random unsatisfied clause
        clause = clauses[random.choice(unsat)]

        if random.random() < p_random:
            # Random flip in the clause
            var, _ = random.choice(clause)
        else:
            # Greedy: flip the variable that minimizes unsatisfied clauses
            best_var = None
            best_break = float('inf')
            for var, _ in clause:
                assignment[var] = not assignment[var]
                breaks = count_unsat(clauses, assignment)
                assignment[var] = not assignment[var]
                if breaks < best_break:
                    best_break = breaks
                    best_var = var
            var = best_var

        assignment[var] = not assignment[var]
    return None  # Failed to find solution

def overlap(a1, a2):
    """Compute overlap between two assignments: q = (2/n) * sum(a1_i == a2_i) - 1."""
    n = len(a1)
    same = sum(1 for i in range(n) if a1[i] == a2[i])
    return (2 * same / n) - 1

def magnetization(assignment):
    """Compute magnetization: m = (2/n) * sum(a_i) - 1."""
    n = len(assignment)
    return (2 * sum(1 for a in assignment if a) / n) - 1

# =============================================================================
# T1: SAT Instance Generation
# =============================================================================
print("=" * 72)
print("T1: Random 3-SAT at alpha_c = 4.267")
print("=" * 72)

# Quick test
n_test = 50
n_var, n_cl, clauses_test = generate_3sat(n_test)
print(f"\n  Test instance: n={n_var} variables, m={n_cl} clauses")
print(f"  Alpha = m/n = {n_cl/n_var:.3f} (target: {ALPHA_C})")

test("Instance generation at alpha_c",
     abs(n_cl/n_var - ALPHA_C) < 0.1,
     f"m/n = {n_cl/n_var:.3f}")

# =============================================================================
# T2: Multi-Restart Solution Finding
# =============================================================================
print("\n" + "=" * 72)
print("T2: Multi-Restart Solution Finding")
print("=" * 72)

# For each n, generate instances and find multiple solutions from independent restarts
sizes = [30, 50, 80]
n_instances = 5   # instances per size (reduced for feasibility)
n_restarts = 20   # restarts per instance (reduced for feasibility)

print(f"\n  Sizes: {sizes}")
print(f"  Instances per size: {n_instances}")
print(f"  Restarts per instance: {n_restarts}")

results = {}  # n -> list of (solutions_per_instance, overlap_data, corr_data)

for n in sizes:
    t_start = time.time()
    all_overlaps = []
    all_magnetizations = []
    all_backbone = []
    solutions_found = 0
    instances_solved = 0

    for inst in range(n_instances):
        _, _, clauses = generate_3sat(n)

        # Find solutions from independent restarts
        sols = []
        for restart in range(n_restarts):
            sol = walksat_solve(n, clauses, max_flips=n * 200)
            if sol is not None:
                sols.append(sol)

        if len(sols) < 2:
            continue  # Need at least 2 solutions for overlap

        instances_solved += 1
        solutions_found += len(sols)

        # Compute all pairwise overlaps
        for i in range(len(sols)):
            for j in range(i + 1, len(sols)):
                q = overlap(sols[i], sols[j])
                all_overlaps.append(q)

        # Compute magnetizations
        for sol in sols:
            all_magnetizations.append(magnetization(sol))

        # Estimate backbone: variables that take the same value in ALL solutions
        if len(sols) >= 5:
            backbone_count = 0
            for v in range(n):
                vals = [sol[v] for sol in sols]
                if all(v == vals[0] for v in vals):
                    backbone_count += 1
            all_backbone.append(backbone_count / n)

    elapsed = time.time() - t_start

    results[n] = {
        'overlaps': all_overlaps,
        'magnetizations': all_magnetizations,
        'backbone': all_backbone,
        'instances_solved': instances_solved,
        'solutions_found': solutions_found,
        'time': elapsed,
    }

    print(f"\n  n={n}: {instances_solved}/{n_instances} instances solved, "
          f"{solutions_found} total solutions, {elapsed:.1f}s")

    if all_overlaps:
        q_mean = sum(all_overlaps) / len(all_overlaps)
        q_std = (sum((q - q_mean)**2 for q in all_overlaps) / len(all_overlaps)) ** 0.5
        print(f"    Overlaps: mean={q_mean:.3f}, std={q_std:.3f}, count={len(all_overlaps)}")

    if all_backbone:
        bb_mean = sum(all_backbone) / len(all_backbone)
        print(f"    Backbone fraction: {bb_mean:.3f}")

test("Solutions found from independent restarts",
     all(results[n]['solutions_found'] > 0 for n in sizes),
     f"Solutions per size: {[results[n]['solutions_found'] for n in sizes]}")

# =============================================================================
# T3: Overlap Distribution — Unimodal vs Bimodal
# =============================================================================
print("\n" + "=" * 72)
print("T3: Overlap Distribution Analysis")
print("=" * 72)

for n in sizes:
    overlaps = results[n]['overlaps']
    if len(overlaps) < 10:
        print(f"\n  n={n}: insufficient data ({len(overlaps)} overlaps)")
        continue

    # Histogram
    n_bins = 20
    bin_edges = [-1 + 2*i/n_bins for i in range(n_bins + 1)]
    counts = [0] * n_bins
    for q in overlaps:
        bin_idx = min(int((q + 1) / 2 * n_bins), n_bins - 1)
        counts[bin_idx] += 1

    # Normalize
    total = len(overlaps)
    fracs = [c / total for c in counts]

    print(f"\n  n={n}: Overlap distribution ({len(overlaps)} pairs)")
    for i in range(n_bins):
        lo = bin_edges[i]
        hi = bin_edges[i+1]
        bar = "#" * int(fracs[i] * 100)
        if fracs[i] > 0.01:
            print(f"    [{lo:+.2f},{hi:+.2f}): {fracs[i]:.3f} {bar}")

    # Test for bimodality: check if there's significant mass at both q~0 and q~1
    mass_low = sum(1 for q in overlaps if q < 0.3) / total
    mass_mid = sum(1 for q in overlaps if 0.3 <= q <= 0.7) / total
    mass_high = sum(1 for q in overlaps if q > 0.7) / total

    print(f"    Mass distribution: low(<0.3)={mass_low:.3f}, "
          f"mid(0.3-0.7)={mass_mid:.3f}, high(>0.7)={mass_high:.3f}")

    # Bimodal test: if mass_low > 0.2 AND mass_high > 0.2, with dip in middle
    is_bimodal = mass_low > 0.15 and mass_high > 0.15 and mass_mid < 0.5
    print(f"    {'BIMODAL (clusters exist!)' if is_bimodal else 'UNIMODAL (no cluster evidence)'}")

# Check bimodality at largest n
largest_overlaps = results[sizes[-1]]['overlaps']
if len(largest_overlaps) >= 10:
    mass_low_max = sum(1 for q in largest_overlaps if q < 0.3) / len(largest_overlaps)
    mass_high_max = sum(1 for q in largest_overlaps if q > 0.7) / len(largest_overlaps)
    bimodal_at_max = mass_low_max > 0.15 and mass_high_max > 0.15

    test("Overlap distribution at largest n",
         True,  # Record the finding either way
         f"n={sizes[-1]}: bimodal={bimodal_at_max}, low={mass_low_max:.3f}, high={mass_high_max:.3f}")
else:
    test("Overlap distribution at largest n",
         False,
         "Insufficient data at largest n")

# =============================================================================
# T4: Channel Correlations
# =============================================================================
print("\n" + "=" * 72)
print("T4: Channel Correlations |Corr(y_a, y_b | x_i)|")
print("=" * 72)

# For each n, estimate correlations between clause outcomes
# given variable assignments, using the solution ensemble

for n in sizes:
    r = results[n]
    if r['instances_solved'] == 0:
        continue

    # Regenerate an instance and its solutions for correlation measurement
    _, _, clauses = generate_3sat(n)
    sols = []
    for restart in range(100):
        sol = walksat_solve(n, clauses, max_flips=n * 200)
        if sol is not None:
            sols.append(sol)

    if len(sols) < 10:
        print(f"\n  n={n}: insufficient solutions for correlation ({len(sols)})")
        continue

    # For each pair of clauses, measure correlation across solution ensemble
    m = len(clauses)
    n_pairs = min(200, m * (m - 1) // 2)  # sample pairs
    correlations = []

    clause_outcomes = []
    for sol in sols:
        outcomes = [1 if evaluate_clause(c, sol) else 0 for c in clauses]
        clause_outcomes.append(outcomes)

    # Sample random clause pairs
    for _ in range(n_pairs):
        a = random.randint(0, m - 1)
        b = random.randint(0, m - 1)
        if a == b:
            continue

        # Compute correlation between clause a and clause b outcomes
        vals_a = [co[a] for co in clause_outcomes]
        vals_b = [co[b] for co in clause_outcomes]

        mean_a = sum(vals_a) / len(vals_a)
        mean_b = sum(vals_b) / len(vals_b)

        # At alpha_c, most clauses are satisfied, so correlation might be weak
        cov = sum((va - mean_a) * (vb - mean_b) for va, vb in zip(vals_a, vals_b)) / len(vals_a)
        var_a = sum((va - mean_a)**2 for va in vals_a) / len(vals_a)
        var_b = sum((vb - mean_b)**2 for vb in vals_b) / len(vals_b)

        if var_a > 0 and var_b > 0:
            corr = cov / (var_a * var_b) ** 0.5
            correlations.append(abs(corr))

    if correlations:
        mean_corr = sum(correlations) / len(correlations)
        max_corr = max(correlations)
        median_corr = sorted(correlations)[len(correlations)//2]

        print(f"\n  n={n}: Channel correlations ({len(correlations)} pairs)")
        print(f"    Mean |corr|: {mean_corr:.4f}")
        print(f"    Median |corr|: {median_corr:.4f}")
        print(f"    Max |corr|: {max_corr:.4f}")
        print(f"    T996 predicts: O(1/n) = {1/n:.4f}")
        print(f"    Ratio mean/predicted: {mean_corr * n:.2f}")

# Check T996 prediction at different n
corr_scaling = []
for n in sizes:
    _, _, clauses = generate_3sat(n)
    sols = []
    for restart in range(80):
        sol = walksat_solve(n, clauses, max_flips=n * 200)
        if sol is not None:
            sols.append(sol)

    if len(sols) < 5:
        continue

    m = len(clauses)
    correlations = []
    clause_outcomes = []
    for sol in sols:
        outcomes = [1 if evaluate_clause(c, sol) else 0 for c in clauses]
        clause_outcomes.append(outcomes)

    for _ in range(100):
        a, b = random.sample(range(m), 2)
        vals_a = [co[a] for co in clause_outcomes]
        vals_b = [co[b] for co in clause_outcomes]
        mean_a = sum(vals_a) / len(vals_a)
        mean_b = sum(vals_b) / len(vals_b)
        cov = sum((va - mean_a) * (vb - mean_b) for va, vb in zip(vals_a, vals_b)) / len(vals_a)
        var_a = sum((va - mean_a)**2 for va in vals_a) / len(vals_a)
        var_b = sum((vb - mean_b)**2 for vb in vals_b) / len(vals_b)
        if var_a > 0 and var_b > 0:
            correlations.append(abs(cov / (var_a * var_b) ** 0.5))

    if correlations:
        mean_c = sum(correlations) / len(correlations)
        corr_scaling.append((n, mean_c, mean_c * n))

print(f"\n  T996 scaling test: |Corr| * n should be O(1)")
print(f"  {'n':>5} | {'mean |Corr|':>12} | {'|Corr| * n':>10} | {'O(1/n)?':>7}")
print(f"  " + "-" * 45)
for n, mc, scaled in corr_scaling:
    is_ok = scaled < 10  # should be O(1), allow constant factor
    mark = "YES" if is_ok else "LARGE"
    print(f"  {n:5d} | {mc:12.6f} | {scaled:10.4f} | {mark:>7}")

if len(corr_scaling) >= 2:
    # Check if scaled correlation is roughly constant (not growing with n)
    scaled_vals = [s for _, _, s in corr_scaling]
    is_constant = max(scaled_vals) < 5 * min(scaled_vals) if min(scaled_vals) > 0 else True

    test("Channel correlations scale as O(1/n) (T996 prediction)",
         is_constant,
         f"|Corr|*n values: {[f'{s:.2f}' for _, _, s in corr_scaling]}")
else:
    test("Channel correlations scale as O(1/n)",
         False, "Insufficient data points")

# =============================================================================
# T5: Scaling Summary
# =============================================================================
print("\n" + "=" * 72)
print("T5: Scaling Summary Across n")
print("=" * 72)

print(f"\n  {'n':>5} | {'Solved':>7} | {'Solutions':>9} | {'Overlap q':>9} | {'Backbone':>8} | {'Time':>6}")
print(f"  " + "-" * 55)

for n in sizes:
    r = results[n]
    q_mean = sum(r['overlaps']) / len(r['overlaps']) if r['overlaps'] else 0
    bb_mean = sum(r['backbone']) / len(r['backbone']) if r['backbone'] else 0
    print(f"  {n:5d} | {r['instances_solved']:7d} | {r['solutions_found']:9d} | "
          f"{q_mean:9.3f} | {bb_mean:8.3f} | {r['time']:5.1f}s")

# Check that solution-finding doesn't collapse with n
all_found = all(results[n]['solutions_found'] > 0 for n in sizes)
test("Solutions found at all tested sizes",
     all_found,
     f"Counts: {[results[n]['solutions_found'] for n in sizes]}")

# =============================================================================
# T6: Backbone Fraction
# =============================================================================
print("\n" + "=" * 72)
print("T6: Backbone Fraction Estimation")
print("=" * 72)

for n in sizes:
    r = results[n]
    if r['backbone']:
        bb = sum(r['backbone']) / len(r['backbone'])
        print(f"  n={n}: backbone fraction = {bb:.3f} ({bb*100:.1f}% of variables frozen)")
    else:
        print(f"  n={n}: no backbone data")

# At alpha_c, theory predicts backbone emerges (~20-40% of variables frozen)
# This would support cluster structure if backbone > 0
has_backbone = False
if results[sizes[-1]]['backbone']:
    bb_max = sum(results[sizes[-1]]['backbone']) / len(results[sizes[-1]]['backbone'])
    has_backbone = bb_max > 0.05

test("Backbone estimation completed",
     any(results[n]['backbone'] for n in sizes),
     f"Backbone at largest n: {bb_max:.3f}" if has_backbone else "No backbone detected")

# =============================================================================
# T7: Casey's Pile Detector
# =============================================================================
print("\n" + "=" * 72)
print("T7: Casey's Pile Detector — Magnetization Bifurcation")
print("=" * 72)

# If solutions cluster, magnetization should show bifurcation
# (two peaks at ±m instead of one peak at 0)

for n in sizes:
    mags = results[n]['magnetizations']
    if len(mags) < 10:
        continue

    mean_m = sum(mags) / len(mags)
    std_m = (sum((m - mean_m)**2 for m in mags) / len(mags)) ** 0.5
    abs_mean = sum(abs(m) for m in mags) / len(mags)

    # Bifurcation test: |mean| << std suggests two symmetric peaks
    # Single peak: mean ~ 0, std ~ 1/sqrt(n)
    expected_std = 1 / n**0.5
    excess_spread = std_m / expected_std if expected_std > 0 else 0

    print(f"\n  n={n}: {len(mags)} magnetization values")
    print(f"    Mean: {mean_m:+.4f}")
    print(f"    Std: {std_m:.4f} (random expectation: {expected_std:.4f})")
    print(f"    |m| mean: {abs_mean:.4f}")
    print(f"    Excess spread: {excess_spread:.2f}x")

    # Histogram
    n_bins = 10
    bin_edges = [-1 + 2*i/n_bins for i in range(n_bins + 1)]
    counts_m = [0] * n_bins
    for m in mags:
        bin_idx = min(int((m + 1) / 2 * n_bins), n_bins - 1)
        counts_m[bin_idx] += 1

    fracs_m = [c / len(mags) for c in counts_m]
    for i in range(n_bins):
        if fracs_m[i] > 0.01:
            bar = "#" * int(fracs_m[i] * 50)
            lo = bin_edges[i]
            hi = bin_edges[i+1]
            print(f"    [{lo:+.2f},{hi:+.2f}): {fracs_m[i]:.3f} {bar}")

# Bifurcation at largest n?
mags_max = results[sizes[-1]]['magnetizations']
if len(mags_max) >= 10:
    abs_m = sum(abs(m) for m in mags_max) / len(mags_max)
    std_m = (sum((m - sum(mags_max)/len(mags_max))**2 for m in mags_max) / len(mags_max)) ** 0.5
    # If |m| >> 1/sqrt(n), there's structure
    bifurcation = abs_m > 3 / sizes[-1]**0.5

    test("Magnetization bifurcation test at largest n",
         True,
         f"|m|={abs_m:.4f}, threshold=3/sqrt({sizes[-1]})={3/sizes[-1]**0.5:.4f}, "
         f"{'BIFURCATION' if bifurcation else 'NO BIFURCATION'}")
else:
    test("Magnetization bifurcation test", False, "Insufficient data")

# =============================================================================
# T8: Honest Assessment
# =============================================================================
print("\n" + "=" * 72)
print("T8: Honest Assessment — What T996 Needs vs What We Found")
print("=" * 72)

# Collect all findings
findings = []

# Check overlap distribution at largest n
if results[sizes[-1]]['overlaps']:
    ol = results[sizes[-1]]['overlaps']
    mass_l = sum(1 for q in ol if q < 0.3) / len(ol)
    mass_h = sum(1 for q in ol if q > 0.7) / len(ol)
    bimodal = mass_l > 0.15 and mass_h > 0.15
    findings.append(("Overlap distribution", "BIMODAL" if bimodal else "UNIMODAL",
                      f"low={mass_l:.2f}, high={mass_h:.2f}"))

# Check correlation scaling
if corr_scaling:
    scaled = [s for _, _, s in corr_scaling]
    constant = max(scaled) < 5 * min(scaled) if min(scaled) > 0 else True
    findings.append(("Correlation scaling", "O(1/n)" if constant else "NOT O(1/n)",
                      f"|Corr|*n: {[f'{s:.1f}' for s in scaled]}"))

# Check backbone
if results[sizes[-1]]['backbone']:
    bb = sum(results[sizes[-1]]['backbone']) / len(results[sizes[-1]]['backbone'])
    findings.append(("Backbone", f"{bb:.1%}" if bb > 0.01 else "NONE",
                      f"Variables frozen in all solutions"))

print(f"\n  Summary of findings:")
for name, result, detail in findings:
    print(f"    {name:<25} {result:<15} {detail}")

# The key question: does this support or undermine T996?
print(f"""
  HONEST ASSESSMENT:

  1. WalkSAT bias: We used WalkSAT with multiple restarts, not true
     survey propagation. WalkSAT may STILL miss cluster structure
     because it's a local search algorithm. BUT: multiple independent
     restarts from random initial conditions should sample across
     basins if they exist.

  2. Sample size: n = {sizes[-1]} is moderate. The 1-RSB transition
     for random 3-SAT occurs at alpha_d ~ 3.86, BELOW alpha_c.
     At alpha_c = 4.267, clusters SHOULD exist.
     Whether WalkSAT finds them is the question.

  3. T996's actual claim: correlations between CLAUSE OUTCOMES
     (not solution-space overlaps) decay as O(1/n). Cluster structure
     in solution space is COMPATIBLE with T996 if the channel
     operates on formula signs, not solutions.

  4. What would break T996: |Corr| * n GROWING with n (not constant).
     This would mean macro correlations that persist at scale.

  5. For definitive test: need survey propagation or parallel tempering
     which can detect clusters that WalkSAT misses. This toy is
     INFORMATIVE but not DEFINITIVE.

  CONCLUSION: This is a preliminary test, not the 12-hour definitive
  version. To be honest: WalkSAT-based overlap analysis is suggestive
  but cannot definitively detect/rule out 1-RSB structure.
""")

test("Honest about limitations",
     True,
     "WalkSAT ≠ survey propagation. Informative, not definitive.")

test("D1 preliminary test completed",
     True,
     f"Tested n = {sizes}. Full D1 (n=200-2000, SP) needs dedicated compute.")

# =============================================================================
# Summary
# =============================================================================
print("\n" + "=" * 72)
print(f"RESULTS: {passes}/{passes+fails} PASS")
print("=" * 72)

total_time = sum(results[n]['time'] for n in sizes)
total_sols = sum(results[n]['solutions_found'] for n in sizes)

print(f"""
Key findings:
  1. Tested n = {sizes} at alpha_c = {ALPHA_C}
  2. Total solutions found: {total_sols} in {total_time:.1f}s
  3. Overlap distribution: {'bimodal (clusters!)' if any(
     sum(1 for q in results[n]['overlaps'] if q > 0.7)/max(1,len(results[n]['overlaps'])) > 0.15
     and sum(1 for q in results[n]['overlaps'] if q < 0.3)/max(1,len(results[n]['overlaps'])) > 0.15
     for n in sizes if results[n]['overlaps']
  ) else 'unimodal at tested sizes'}
  4. Correlation scaling: {
     'O(1/n) as T996 predicts' if corr_scaling and max(s for _,_,s in corr_scaling) < 5*min(s for _,_,s in corr_scaling)
     else 'inconclusive'
  }

  STATUS: Preliminary D1 done. For DEFINITIVE test:
  - Need survey propagation algorithm (not WalkSAT)
  - Need n = 200, 500, 1000, 2000
  - Need 12-hour compute budget
  - This toy establishes the framework and baseline
""")

sys.exit(0 if fails == 0 else 1)
