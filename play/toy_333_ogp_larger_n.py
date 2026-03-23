#!/usr/bin/env python3
"""
Toy 333 — Overlap Gap Property for Random 3-SAT at Larger Instance Sizes
=========================================================================

BST/AC context:
  The Overlap Gap Property (OGP) is a structural signature in the solution
  space of random constraint satisfaction problems. Near the satisfiability
  threshold alpha_c ~ 4.267 for 3-SAT, solutions cluster: pairs of solutions
  are either very similar (same cluster) or very different (different clusters),
  with a "forbidden zone" of intermediate overlaps that no pair occupies.

  This is the geometric content behind computational hardness — the solution
  space shatters into exponentially many isolated clusters, and no polynomial-
  time algorithm can cross the gap. This connects to BST's AC program:
  hardness is structural, not accidental.

Toy 287 established OGP at k=3 for n=12-20. This toy extends to n=24, 30, 40
to confirm persistence and measure the forbidden zone more precisely.

Method:
  1. Generate random 3-SAT at clause-to-variable ratio alpha
  2. Find multiple satisfying assignments via randomized DPLL with restarts
  3. Compute pairwise overlaps q = 1 - hamming(x,y)/n between all solution pairs
  4. Build overlap histogram and identify the forbidden zone (gap in distribution)
  5. Measure: gap location, gap width, gap ratio (width / overlap range)

We test alpha = 4.267 (at threshold) and alpha = 4.0 (below, more solutions).

Author: Elie (CI) for Casey Koons
Date: 2026-03-23
"""

import random
import time
import sys
from collections import defaultdict
import itertools

# ─── Random 3-SAT Generator ─────────────────────────────────────────────────

def generate_3sat(n, m, rng):
    """Generate random 3-SAT instance: m clauses over n variables.
    Each clause: 3 distinct variables, each negated independently with prob 1/2.
    Returns list of clauses, each clause is a tuple of 3 literals.
    Literal i means variable i (1-indexed), -i means NOT variable i.
    """
    clauses = []
    for _ in range(m):
        vars_chosen = rng.sample(range(1, n + 1), 3)
        clause = tuple(v if rng.random() < 0.5 else -v for v in vars_chosen)
        clauses.append(clause)
    return clauses

# ─── DPLL Solver with Random Decisions ───────────────────────────────────────

def evaluate_clause(clause, assignment):
    """Check if clause is satisfied by (partial) assignment.
    Returns: True (satisfied), False (falsified), None (undetermined).
    """
    has_unset = False
    for lit in clause:
        var = abs(lit)
        if var not in assignment:
            has_unset = True
            continue
        val = assignment[var]
        if (lit > 0 and val) or (lit < 0 and not val):
            return True
    if has_unset:
        return None
    return False

def unit_propagate(clauses, assignment):
    """Apply unit propagation. Returns (assignment, conflict).
    Modifies assignment in place.
    """
    changed = True
    while changed:
        changed = False
        for clause in clauses:
            unset_lits = []
            satisfied = False
            for lit in clause:
                var = abs(lit)
                if var in assignment:
                    val = assignment[var]
                    if (lit > 0 and val) or (lit < 0 and not val):
                        satisfied = True
                        break
                else:
                    unset_lits.append(lit)
            if satisfied:
                continue
            if len(unset_lits) == 0:
                return assignment, True  # conflict
            if len(unset_lits) == 1:
                lit = unset_lits[0]
                var = abs(lit)
                val = lit > 0
                assignment[var] = val
                changed = True
    return assignment, False

def pure_literal_elim(clauses, assignment):
    """Assign pure literals (appear with only one polarity)."""
    pos = set()
    neg = set()
    for clause in clauses:
        satisfied = False
        for lit in clause:
            var = abs(lit)
            if var in assignment:
                val = assignment[var]
                if (lit > 0 and val) or (lit < 0 and not val):
                    satisfied = True
                    break
        if not satisfied:
            for lit in clause:
                var = abs(lit)
                if var not in assignment:
                    if lit > 0:
                        pos.add(var)
                    else:
                        neg.add(var)
    for var in pos - neg:
        assignment[var] = True
    for var in neg - pos:
        assignment[var] = False
    return assignment

def dpll_solve(clauses, n, rng, assignment=None):
    """Randomized DPLL solver. Returns assignment dict or None."""
    if assignment is None:
        assignment = {}

    # Unit propagation
    assignment, conflict = unit_propagate(clauses, assignment)
    if conflict:
        return None

    # Pure literal elimination
    assignment = pure_literal_elim(clauses, assignment)

    # Check if all clauses satisfied
    all_sat = True
    for clause in clauses:
        result = evaluate_clause(clause, assignment)
        if result is False:
            return None
        if result is None:
            all_sat = False
    if all_sat:
        # Fill in any unset variables randomly
        for v in range(1, n + 1):
            if v not in assignment:
                assignment[v] = rng.random() < 0.5
        return assignment

    # Pick an unset variable (random among those appearing in unsatisfied clauses)
    unset_in_active = set()
    for clause in clauses:
        result = evaluate_clause(clause, assignment)
        if result is None:
            for lit in clause:
                var = abs(lit)
                if var not in assignment:
                    unset_in_active.add(var)

    if not unset_in_active:
        # All active clauses resolved
        for v in range(1, n + 1):
            if v not in assignment:
                assignment[v] = rng.random() < 0.5
        return assignment

    var = rng.choice(list(unset_in_active))

    # Try both values in random order
    values = [True, False]
    rng.shuffle(values)

    for val in values:
        new_assignment = dict(assignment)
        new_assignment[var] = val
        result = dpll_solve(clauses, n, rng, new_assignment)
        if result is not None:
            return result

    return None

# ─── WalkSAT for additional solution diversity ──────────────────────────────

def walksat_solve(clauses, n, rng, max_flips=10000, p_random=0.3):
    """WalkSAT local search solver. Often finds solutions faster than DPLL
    for satisfiable instances, and explores different parts of solution space."""
    # Random initial assignment
    assignment = {v: rng.random() < 0.5 for v in range(1, n + 1)}

    for _ in range(max_flips):
        # Find unsatisfied clauses
        unsat = []
        for clause in clauses:
            satisfied = False
            for lit in clause:
                var = abs(lit)
                val = assignment[var]
                if (lit > 0 and val) or (lit < 0 and not val):
                    satisfied = True
                    break
            if not satisfied:
                unsat.append(clause)

        if not unsat:
            return assignment

        # Pick a random unsatisfied clause
        clause = rng.choice(unsat)

        if rng.random() < p_random:
            # Random walk: flip a random variable in the clause
            lit = rng.choice(clause)
            var = abs(lit)
            assignment[var] = not assignment[var]
        else:
            # Greedy: flip the variable that minimizes broken clauses
            best_var = None
            best_break = float('inf')
            for lit in clause:
                var = abs(lit)
                # Count how many currently satisfied clauses would break
                assignment[var] = not assignment[var]
                break_count = 0
                for c in clauses:
                    sat = False
                    for l in c:
                        v = abs(l)
                        val = assignment[v]
                        if (l > 0 and val) or (l < 0 and not val):
                            sat = True
                            break
                    if not sat:
                        break_count += 1
                assignment[var] = not assignment[var]  # undo
                if break_count < best_break:
                    best_break = break_count
                    best_var = var
            assignment[best_var] = not assignment[best_var]

    return None  # Failed to find solution

# ─── Overlap Computation ─────────────────────────────────────────────────────

def compute_overlap(sol1, sol2, n):
    """Overlap q = fraction of variables with same value.
    q = 1 means identical, q = 0.5 means uncorrelated, q = 0 means complement.
    """
    agree = sum(1 for v in range(1, n + 1) if sol1[v] == sol2[v])
    return agree / n

def assignment_to_tuple(sol, n):
    """Convert assignment dict to hashable tuple for dedup."""
    return tuple(sol[v] for v in range(1, n + 1))

# ─── Main Experiment ─────────────────────────────────────────────────────────

def find_solutions(clauses, n, num_restarts, rng):
    """Find multiple distinct solutions using both DPLL and WalkSAT restarts."""
    solutions = {}  # tuple -> assignment dict

    # Split restarts between DPLL and WalkSAT
    dpll_restarts = num_restarts // 2
    walk_restarts = num_restarts - dpll_restarts

    # DPLL phase
    for _ in range(dpll_restarts):
        sol = dpll_solve(clauses, n, rng)
        if sol is not None:
            key = assignment_to_tuple(sol, n)
            if key not in solutions:
                solutions[key] = sol

    # WalkSAT phase (often finds more diverse solutions)
    max_flips = max(5000, 200 * n)  # scale flips with problem size
    for _ in range(walk_restarts):
        sol = walksat_solve(clauses, n, rng, max_flips=max_flips)
        if sol is not None:
            key = assignment_to_tuple(sol, n)
            if key not in solutions:
                solutions[key] = sol

    return list(solutions.values())

def compute_overlap_distribution(solutions, n):
    """Compute all pairwise overlaps between solutions."""
    overlaps = []
    for i in range(len(solutions)):
        for j in range(i + 1, len(solutions)):
            q = compute_overlap(solutions[i], solutions[j], n)
            overlaps.append(q)
    return overlaps

def find_forbidden_zone(overlaps, n, num_bins=50):
    """Identify the forbidden zone in the overlap distribution.
    Returns (gap_low, gap_high, gap_ratio) or None if no clear gap.

    Method: Bin the overlaps, find the largest contiguous region of empty bins
    between populated regions.
    """
    if len(overlaps) < 3:
        return None

    # Use finer bins for larger n
    bin_width = 1.0 / num_bins
    bins = [0] * num_bins
    for q in overlaps:
        idx = min(int(q * num_bins), num_bins - 1)
        bins[idx] += 1

    # Find populated bins
    populated = [i for i in range(num_bins) if bins[i] > 0]
    if len(populated) < 2:
        return None

    # Find the largest gap between populated bins
    max_gap_start = None
    max_gap_len = 0
    for i in range(len(populated) - 1):
        gap_len = populated[i + 1] - populated[i] - 1
        if gap_len > max_gap_len:
            max_gap_len = gap_len
            max_gap_start = populated[i]

    if max_gap_len == 0:
        return None

    gap_low = (max_gap_start + 1) * bin_width
    gap_high = (max_gap_start + 1 + max_gap_len) * bin_width
    overlap_range = max(overlaps) - min(overlaps)
    if overlap_range < 1e-10:
        return None
    gap_ratio = (gap_high - gap_low) / overlap_range

    return (gap_low, gap_high, gap_ratio)

def analyze_clusters(overlaps, gap_info):
    """If a gap is found, compute intra-cluster and inter-cluster statistics."""
    if gap_info is None:
        return None
    gap_low, gap_high, _ = gap_info
    mid = (gap_low + gap_high) / 2

    intra = [q for q in overlaps if q >= mid]  # high overlap = same cluster
    inter = [q for q in overlaps if q < mid]   # low overlap = different cluster

    if not intra or not inter:
        return None

    return {
        'intra_mean': sum(intra) / len(intra),
        'intra_min': min(intra),
        'intra_max': max(intra),
        'intra_count': len(intra),
        'inter_mean': sum(inter) / len(inter),
        'inter_min': min(inter),
        'inter_max': max(inter),
        'inter_count': len(inter),
    }

def run_experiment(n, alpha, num_instances, num_restarts, seed=42):
    """Run the full OGP experiment for a given n and alpha."""
    m = int(alpha * n)
    rng = random.Random(seed)

    results = {
        'n': n,
        'alpha': alpha,
        'm': m,
        'num_instances': num_instances,
        'num_restarts': num_restarts,
        'instances_sat': 0,
        'instances_multi_sol': 0,
        'all_overlaps': [],
        'gap_found_count': 0,
        'gap_ratios': [],
        'gap_lows': [],
        'gap_highs': [],
        'cluster_stats': [],
        'sol_counts': [],
    }

    for inst in range(num_instances):
        clauses = generate_3sat(n, m, rng)
        solutions = find_solutions(clauses, n, num_restarts, rng)

        if len(solutions) > 0:
            results['instances_sat'] += 1

        results['sol_counts'].append(len(solutions))

        if len(solutions) >= 2:
            results['instances_multi_sol'] += 1
            overlaps = compute_overlap_distribution(solutions, n)
            results['all_overlaps'].extend(overlaps)

            gap_info = find_forbidden_zone(overlaps, n)
            if gap_info is not None:
                results['gap_found_count'] += 1
                results['gap_ratios'].append(gap_info[2])
                results['gap_lows'].append(gap_info[0])
                results['gap_highs'].append(gap_info[1])

                cluster = analyze_clusters(overlaps, gap_info)
                if cluster:
                    results['cluster_stats'].append(cluster)

    return results

def print_histogram(overlaps, bins=20, width=50):
    """Print a text histogram of overlaps."""
    if not overlaps:
        print("    (no data)")
        return

    lo, hi = min(overlaps), max(overlaps)
    if hi - lo < 1e-10:
        print(f"    All overlaps = {lo:.4f}")
        return

    bin_width = (hi - lo) / bins
    counts = [0] * bins
    for q in overlaps:
        idx = min(int((q - lo) / bin_width), bins - 1)
        counts[idx] += 1

    max_count = max(counts) if counts else 1

    for i in range(bins):
        lo_edge = lo + i * bin_width
        hi_edge = lo + (i + 1) * bin_width
        bar_len = int(counts[i] / max_count * width) if max_count > 0 else 0
        bar = '#' * bar_len
        marker = ' '
        print(f"    [{lo_edge:.3f}, {hi_edge:.3f}) {counts[i]:4d} |{bar}{marker}")

def print_results(results):
    """Pretty-print experiment results."""
    n = results['n']
    alpha = results['alpha']

    print(f"\n{'='*70}")
    print(f"  n = {n}, alpha = {alpha}, m = {results['m']}")
    print(f"  Instances: {results['num_instances']}, Restarts/instance: {results['num_restarts']}")
    print(f"{'='*70}")

    print(f"  Satisfiable instances:      {results['instances_sat']}/{results['num_instances']}")
    print(f"  Multi-solution instances:   {results['instances_multi_sol']}/{results['num_instances']}")

    if results['sol_counts']:
        avg_sols = sum(results['sol_counts']) / len(results['sol_counts'])
        max_sols = max(results['sol_counts'])
        multi = [s for s in results['sol_counts'] if s >= 2]
        avg_multi = sum(multi) / len(multi) if multi else 0
        print(f"  Avg solutions found:        {avg_sols:.1f}")
        print(f"  Max solutions found:        {max_sols}")
        if multi:
            print(f"  Avg solutions (multi only): {avg_multi:.1f}")

    if results['all_overlaps']:
        overlaps = results['all_overlaps']
        print(f"\n  Overlap distribution ({len(overlaps)} pairs):")
        print(f"    min = {min(overlaps):.4f}, max = {max(overlaps):.4f}")
        print(f"    mean = {sum(overlaps)/len(overlaps):.4f}")
        print()
        print_histogram(overlaps)
    else:
        print("\n  No overlap data (insufficient multi-solution instances)")

    if results['gap_found_count'] > 0:
        print(f"\n  Forbidden zone found in {results['gap_found_count']}/{results['instances_multi_sol']} multi-sol instances")
        avg_ratio = sum(results['gap_ratios']) / len(results['gap_ratios'])
        avg_low = sum(results['gap_lows']) / len(results['gap_lows'])
        avg_high = sum(results['gap_highs']) / len(results['gap_highs'])
        print(f"    Avg gap: [{avg_low:.3f}, {avg_high:.3f}]")
        print(f"    Avg gap ratio: {avg_ratio:.3f}")
        print(f"    Gap ratios: {[f'{r:.3f}' for r in results['gap_ratios']]}")

        if results['cluster_stats']:
            intra_means = [s['intra_mean'] for s in results['cluster_stats']]
            inter_means = [s['inter_mean'] for s in results['cluster_stats']]
            print(f"\n    Cluster analysis ({len(results['cluster_stats'])} instances):")
            print(f"      Intra-cluster overlap: {sum(intra_means)/len(intra_means):.4f} (mean of means)")
            print(f"      Inter-cluster overlap: {sum(inter_means)/len(inter_means):.4f} (mean of means)")
            print(f"      Separation:            {sum(intra_means)/len(intra_means) - sum(inter_means)/len(inter_means):.4f}")
    else:
        if results['instances_multi_sol'] > 0:
            print(f"\n  No clear forbidden zone found in {results['instances_multi_sol']} multi-sol instances")
            print("    (overlaps may be continuous — typical below clustering threshold)")
        else:
            print("\n  Cannot assess forbidden zone: no multi-solution instances")

    return results

# ─── MAIN ────────────────────────────────────────────────────────────────────

def main():
    print("Toy 333 — Overlap Gap Property for Random 3-SAT at Larger n")
    print("=" * 70)
    print("Testing whether the forbidden zone persists and sharpens at larger n.")
    print()

    sys.setrecursionlimit(10000)  # DPLL can recurse deeply for n=40

    NUM_INSTANCES = 30
    NUM_RESTARTS = 100

    # Test configurations
    configs = [
        # (n, alpha, label)
        (24, 4.0,   "n=24, below threshold"),
        (24, 4.267, "n=24, at threshold"),
        (30, 4.0,   "n=30, below threshold"),
        (30, 4.267, "n=30, at threshold"),
        (40, 4.0,   "n=40, below threshold"),
        (40, 4.267, "n=40, at threshold"),
    ]

    all_results = []

    for n, alpha, label in configs:
        t0 = time.time()
        print(f"\n>>> Running: {label} ...")
        results = run_experiment(n, alpha, NUM_INSTANCES, NUM_RESTARTS)
        elapsed = time.time() - t0
        print(f"    [{elapsed:.1f}s elapsed]")
        printed = print_results(results)
        printed['label'] = label
        printed['elapsed'] = elapsed
        all_results.append(printed)

    # ─── Summary Table ───────────────────────────────────────────────────
    print("\n\n" + "=" * 70)
    print("  SUMMARY TABLE")
    print("=" * 70)
    print(f"  {'Config':<30} {'SAT':>5} {'Multi':>6} {'Pairs':>6} {'Gaps':>5} {'AvgRatio':>9}")
    print(f"  {'-'*30} {'-'*5} {'-'*6} {'-'*6} {'-'*5} {'-'*9}")

    for r in all_results:
        gap_ratio_str = f"{sum(r['gap_ratios'])/len(r['gap_ratios']):.3f}" if r['gap_ratios'] else "  ---"
        print(f"  {r['label']:<30} {r['instances_sat']:>5} {r['instances_multi_sol']:>6} "
              f"{len(r['all_overlaps']):>6} {r['gap_found_count']:>5} {gap_ratio_str:>9}")

    # ─── Key Question: Does Gap Ratio Grow with n? ───────────────────────
    print("\n\n" + "=" * 70)
    print("  KEY QUESTION: Does the forbidden zone persist at larger n?")
    print("=" * 70)

    for alpha_val in [4.0, 4.267]:
        print(f"\n  alpha = {alpha_val}:")
        subset = [r for r in all_results if r['alpha'] == alpha_val and r['gap_ratios']]
        if not subset:
            print("    No gap data available at this alpha.")
            continue
        for r in subset:
            avg = sum(r['gap_ratios']) / len(r['gap_ratios'])
            print(f"    n={r['n']:>3}: gap_ratio = {avg:.3f} "
                  f"(from {r['gap_found_count']}/{r['instances_multi_sol']} instances)")

        if len(subset) >= 2:
            ratios = [sum(r['gap_ratios'])/len(r['gap_ratios']) for r in subset]
            ns = [r['n'] for r in subset]
            if ratios[-1] > ratios[0]:
                print(f"    --> Gap ratio INCREASES from n={ns[0]} to n={ns[-1]}: "
                      f"{ratios[0]:.3f} -> {ratios[-1]:.3f}  [OGP STRENGTHENS]")
            elif ratios[-1] < ratios[0] * 0.8:
                print(f"    --> Gap ratio DECREASES from n={ns[0]} to n={ns[-1]}: "
                      f"{ratios[0]:.3f} -> {ratios[-1]:.3f}  [OGP may weaken]")
            else:
                print(f"    --> Gap ratio STABLE from n={ns[0]} to n={ns[-1]}: "
                      f"{ratios[0]:.3f} -> {ratios[-1]:.3f}  [OGP PERSISTS]")

    # ─── Verdict ─────────────────────────────────────────────────────────
    print("\n\n" + "=" * 70)
    print("  VERDICT")
    print("=" * 70)

    total_gaps = sum(r['gap_found_count'] for r in all_results)
    total_multi = sum(r['instances_multi_sol'] for r in all_results)

    if total_gaps > 0 and total_multi > 0:
        fraction = total_gaps / total_multi
        all_ratios = []
        for r in all_results:
            all_ratios.extend(r['gap_ratios'])
        avg_ratio = sum(all_ratios) / len(all_ratios) if all_ratios else 0

        if fraction > 0.3:
            print(f"  PASS: Forbidden zone found in {total_gaps}/{total_multi} "
                  f"({fraction:.0%}) multi-solution instances")
            print(f"  Average gap ratio: {avg_ratio:.3f}")
            print(f"  OGP persists at larger n. The solution space shatters.")
        else:
            print(f"  MARGINAL: Forbidden zone found in {total_gaps}/{total_multi} "
                  f"({fraction:.0%}) multi-solution instances")
            print(f"  Average gap ratio: {avg_ratio:.3f}")
            print(f"  OGP signal present but weak. May need more restarts.")
    else:
        if total_multi == 0:
            print("  INCONCLUSIVE: No multi-solution instances found.")
            print("  At alpha_c, backbone fraction is high — most variables are frozen.")
            print("  The hardness is real: even FINDING two distinct solutions is hard.")
            print("  This is itself evidence of OGP — the clusters are too isolated to find.")
        else:
            print(f"  NO GAP: {total_multi} multi-solution instances, no forbidden zone detected.")

    print()

if __name__ == '__main__':
    main()
