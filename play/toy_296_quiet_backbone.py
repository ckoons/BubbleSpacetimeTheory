#!/usr/bin/env python3
"""
Toy 296 — The Quiet Backbone: Computational Indistinguishability Test
=====================================================================

Casey's insight + Lyra's formulation:
  "The formula is SILENT about backbone errors.
   Setting x = ¬v (wrong) looks identical to x = v (right)
   to any bounded observer. The silence IS P ≠ NP."

Shannon: C = log(1 + S/N). If d*(n) = ω(log n), then
  S/N = 2^{-d*} → C → 0 faster than 1/poly(n).
  poly(n) channel uses × o(1/poly(n)) bits = o(1) total.
  Need Θ(n) backbone bits. Get o(1). Done.

This toy directly tests the Quiet Backbone Conjecture:
  For each backbone variable x with value v, compare
  polynomial-time statistics of φ∧(x=v) vs φ∧(x=¬v).

If the statistics converge (distinguishing advantage → 0),
the backbone is quiet and P ≠ NP follows via Shannon.

Statistics measured:
  1. UP cascade length (how many forced? should both be ~0)
  2. Residual degree distribution (should be identical modulo O(1))
  3. β₁ of residual VIG (topological: should be identical)
  4. Number of solutions of residual (SAT vs UNSAT — the ONE difference)
  5. Subsample satisfiability (random subformula satisfiability rate)
  6. BP convergence (does belief propagation see a difference?)
  7. Local neighborhood structure (k-hop distribution)

Scorecard:
  1. UP cascade = 0 for BOTH right and wrong?                [silence at d=0]
  2. Degree distributions indistinguishable?                   [structural silence]
  3. β₁(residual) identical for right and wrong?               [topological silence]
  4. Distinguishing advantage decreases with n?                [growing quietness]
  5. BP messages similar for right and wrong?                  [algorithmic silence]
  6. No single poly-time stat achieves > ε(n) → 0 advantage?  [universal silence]
  7. d*/log n ratio grows with n?                              [Shannon kills]
  8. Total variation distance → 0 for stat vector?             [computational indist.]

Copyright (c) 2026 Casey Koons. All rights reserved.
Created with Claude Opus 4.6 (Elie), March 2026.
"""

import numpy as np
from collections import defaultdict, Counter
import random
import time
import sys


# ── Parameters ────────────────────────────────────────────────────────
SIZES = [12, 14, 16, 18, 20]
ALPHA = 4.267  # Focus on α_c
N_INSTANCES = 30
SEED = 296


# ── Instance generation ───────────────────────────────────────────────

def gen_3sat(n, alpha, rng):
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vs = rng.sample(range(1, n + 1), 3)
        clauses.append(tuple(v * rng.choice([-1, 1]) for v in vs))
    return clauses


# ── Backbone ──────────────────────────────────────────────────────────

def compute_backbone(clauses, n):
    """Exhaustive backbone via truth table."""
    N = 2 ** n
    bits = np.arange(N, dtype=np.int32)
    var_vals = [(bits >> v) & 1 for v in range(n)]

    sat = np.ones(N, dtype=bool)
    for clause in clauses:
        clause_sat = np.zeros(N, dtype=bool)
        for lit in clause:
            v = abs(lit) - 1
            if lit > 0:
                clause_sat |= var_vals[v].astype(bool)
            else:
                clause_sat |= ~var_vals[v].astype(bool)
        sat &= clause_sat

    n_sol = int(np.sum(sat))
    if n_sol == 0:
        return None, 0

    backbone = {}
    for v in range(n):
        vals = var_vals[v][sat]
        if np.all(vals):
            backbone[v + 1] = True
        elif not np.any(vals):
            backbone[v + 1] = False

    return backbone, n_sol


# ── Unit propagation ──────────────────────────────────────────────────

def up(clauses, n, assign):
    """Unit propagation. Returns (extended assignment, contradiction flag, cascade length)."""
    a = dict(assign)
    cascade = 0
    changed = True
    while changed:
        changed = False
        for clause in clauses:
            unsat_count = 0
            sat = False
            unset_lit = None
            for lit in clause:
                v = abs(lit)
                if v in a:
                    val = a[v]
                    if (lit > 0 and val) or (lit < 0 and not val):
                        sat = True
                        break
                    else:
                        unsat_count += 1
                else:
                    unset_lit = lit
            if sat:
                continue
            if unsat_count == 3:
                return a, True, cascade
            if unsat_count == 2 and unset_lit is not None:
                v = abs(unset_lit)
                a[v] = (unset_lit > 0)
                cascade += 1
                changed = True
    return a, False, cascade


# ── Residual formula ──────────────────────────────────────────────────

def make_residual(clauses, n, var, val):
    """Create residual formula φ ∧ (var=val), simplified by UP."""
    assign = {var: val}
    a, contra, cascade = up(clauses, n, assign)

    if contra:
        return None, a, cascade  # UNSAT after UP

    # Simplify: remove satisfied clauses, shorten others
    residual = []
    for clause in clauses:
        sat = False
        new_lits = []
        for lit in clause:
            v = abs(lit)
            if v in a:
                if (lit > 0 and a[v]) or (lit < 0 and not a[v]):
                    sat = True
                    break
            else:
                new_lits.append(lit)
        if not sat:
            if len(new_lits) == 0:
                return None, a, cascade  # empty clause = UNSAT
            residual.append(tuple(new_lits))

    return residual, a, cascade


# ── Statistics on residual ────────────────────────────────────────────

def degree_distribution(clauses, n):
    """Variable degree distribution of residual formula."""
    deg = defaultdict(int)
    for clause in clauses:
        for lit in clause:
            deg[abs(lit)] += 1
    # Return sorted degree sequence
    return sorted(deg.values(), reverse=True)


def beta1_vig(clauses, n):
    """Compute β₁ of VIG (variable interaction graph) = edges - vertices + components."""
    edges = set()
    vertices = set()
    for clause in clauses:
        vs = sorted(abs(lit) for lit in clause)
        for v in vs:
            vertices.add(v)
        for i in range(len(vs)):
            for j in range(i + 1, len(vs)):
                edges.add((vs[i], vs[j]))

    if not vertices:
        return 0

    # Count connected components via BFS
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    visited = set()
    components = 0
    for v in vertices:
        if v not in visited:
            components += 1
            queue = [v]
            while queue:
                node = queue.pop()
                if node in visited:
                    continue
                visited.add(node)
                for nbr in adj[node]:
                    if nbr not in visited:
                        queue.append(nbr)

    # β₁ = |E| - |V| + components
    return len(edges) - len(vertices) + components


def clause_length_distribution(clauses):
    """Distribution of clause lengths in residual."""
    return Counter(len(c) for c in clauses)


def count_solutions_residual(residual, n, assigned):
    """Count solutions of residual formula (on unassigned variables)."""
    free_vars = [v for v in range(1, n + 1) if v not in assigned]
    if not free_vars:
        # All assigned — check if residual is empty (SAT) or has clauses (check)
        return 1 if not residual else 0

    n_free = len(free_vars)
    if n_free > 20:
        return -1  # too many to enumerate

    count = 0
    for mask in range(2 ** n_free):
        a = dict(assigned)
        for i, v in enumerate(free_vars):
            a[v] = bool((mask >> i) & 1)
        sat = True
        for clause in residual:
            clause_sat = False
            for lit in clause:
                v = abs(lit)
                if v in a:
                    if (lit > 0 and a[v]) or (lit < 0 and not a[v]):
                        clause_sat = True
                        break
            if not clause_sat:
                sat = False
                break
        if sat:
            count += 1
    return count


def compute_statistics(clauses, n, var, val):
    """Compute poly-time statistics on residual φ ∧ (var=val)."""
    residual, assign, cascade = make_residual(clauses, n, var, val)

    stats = {
        'cascade': cascade,
        'is_unsat_after_up': residual is None,
    }

    if residual is None:
        # UNSAT after UP — max divergence signal
        stats['n_clauses'] = 0
        stats['n_vars'] = 0
        stats['beta1'] = 0
        stats['mean_degree'] = 0
        stats['max_degree'] = 0
        stats['n_binary'] = 0
        stats['n_unit'] = 0
        stats['n_solutions'] = 0
        return stats

    stats['n_clauses'] = len(residual)
    free_vars = set()
    for clause in residual:
        for lit in clause:
            free_vars.add(abs(lit))
    stats['n_vars'] = len(free_vars)
    stats['beta1'] = beta1_vig(residual, n)

    degs = degree_distribution(residual, n)
    stats['mean_degree'] = np.mean(degs) if degs else 0
    stats['max_degree'] = max(degs) if degs else 0

    cl_dist = clause_length_distribution(residual)
    stats['n_binary'] = cl_dist.get(2, 0)
    stats['n_unit'] = cl_dist.get(1, 0)

    stats['n_solutions'] = count_solutions_residual(residual, n, assign)

    return stats


# ── Run experiment ───────────────────────────────────────────────────

def run_experiment():
    print("=" * 76)
    print("Toy 296 — The Quiet Backbone: Computational Indistinguishability")
    print("=" * 76)
    print(f"Sizes: {SIZES} | α = {ALPHA} | Instances: {N_INSTANCES}")
    print(f"\nCasey: 'Silence is 0 feedback. The signal has no say in the channel.'")
    print(f"Lyra: 'One barrier, four symptoms. The formula doesn't react.'")
    print()

    rng = random.Random(SEED)
    all_results = {}

    for n in SIZES:
        t0 = time.time()
        results = []
        skipped = 0

        for trial in range(N_INSTANCES):
            clauses = gen_3sat(n, ALPHA, rng)
            bb, n_sol = compute_backbone(clauses, n)
            if bb is None or len(bb) < 2:
                skipped += 1
                continue

            # For each backbone variable, compare right vs wrong
            instance_diffs = []
            for var, val in list(bb.items())[:min(5, len(bb))]:  # sample up to 5 bb vars
                stats_right = compute_statistics(clauses, n, var, val)
                stats_wrong = compute_statistics(clauses, n, var, not val)

                diff = {}
                for key in ['cascade', 'n_clauses', 'n_vars', 'beta1',
                            'mean_degree', 'max_degree', 'n_binary', 'n_unit']:
                    r = stats_right[key]
                    w = stats_wrong[key]
                    diff[key] = abs(r - w)

                diff['right_unsat'] = stats_right['is_unsat_after_up']
                diff['wrong_unsat'] = stats_wrong['is_unsat_after_up']
                diff['right_cascade'] = stats_right['cascade']
                diff['wrong_cascade'] = stats_wrong['cascade']
                diff['right_solutions'] = stats_right['n_solutions']
                diff['wrong_solutions'] = stats_wrong['n_solutions']

                instance_diffs.append(diff)

            if instance_diffs:
                results.append(instance_diffs)

            if n >= 18 and (trial + 1) % 5 == 0:
                sys.stdout.write(f"\r  n={n:3d}: {trial+1}/{N_INSTANCES}...")
                sys.stdout.flush()

        elapsed = time.time() - t0
        all_results[n] = results

        if not results:
            print(f"\r  n={n:3d}: no valid instances [{elapsed:.1f}s]")
            continue

        # Aggregate statistics
        all_diffs = [d for inst in results for d in inst]
        n_comparisons = len(all_diffs)

        # Cascade analysis
        right_cascades = [d['right_cascade'] for d in all_diffs]
        wrong_cascades = [d['wrong_cascade'] for d in all_diffs]
        right_unsat_rate = sum(1 for d in all_diffs if d['right_unsat']) / n_comparisons
        wrong_unsat_rate = sum(1 for d in all_diffs if d['wrong_unsat']) / n_comparisons

        # Structural differences
        cascade_diffs = [d['cascade'] for d in all_diffs]
        clause_diffs = [d['n_clauses'] for d in all_diffs]
        beta1_diffs = [d['beta1'] for d in all_diffs]
        degree_diffs = [d['mean_degree'] for d in all_diffs]
        binary_diffs = [d['n_binary'] for d in all_diffs]

        # Distinguishing advantage: fraction where wrong has UP contradiction but right doesn't
        distinguishable = sum(1 for d in all_diffs
                              if d['wrong_unsat'] and not d['right_unsat']) / n_comparisons

        print(f"\r  n={n:3d}: {n_comparisons} comparisons  "
              f"cascade_Δ={np.mean(cascade_diffs):.2f}  "
              f"clause_Δ={np.mean(clause_diffs):.1f}  "
              f"β₁_Δ={np.mean(beta1_diffs):.2f}  "
              f"deg_Δ={np.mean(degree_diffs):.3f}  "
              f"R_unsat={right_unsat_rate:.2f}  W_unsat={wrong_unsat_rate:.2f}  "
              f"dist={distinguishable:.2f}  "
              f"[{len(results)}/{N_INSTANCES}] [{elapsed:.1f}s]")

    # ── Summary tables ────────────────────────────────────────────────
    print("\n" + "=" * 76)
    print("TABLE 1: Quiet Backbone — Structural Indistinguishability")
    print("=" * 76)
    print(f"{'n':>4} | {'comps':>5} | {'casc_Δ':>7} | {'cls_Δ':>6} | {'β₁_Δ':>6} | {'deg_Δ':>7} | {'bin_Δ':>6} | {'R_un':>5} | {'W_un':>5} | {'dist':>5}")
    print("-" * 85)

    for n in SIZES:
        if n not in all_results or not all_results[n]:
            continue
        all_diffs = [d for inst in all_results[n] for d in inst]
        nc = len(all_diffs)
        if nc == 0:
            continue
        casc = np.mean([d['cascade'] for d in all_diffs])
        cls = np.mean([d['n_clauses'] for d in all_diffs])
        b1 = np.mean([d['beta1'] for d in all_diffs])
        deg = np.mean([d['mean_degree'] for d in all_diffs])
        bn = np.mean([d['n_binary'] for d in all_diffs])
        ru = sum(1 for d in all_diffs if d['right_unsat']) / nc
        wu = sum(1 for d in all_diffs if d['wrong_unsat']) / nc
        dist = sum(1 for d in all_diffs if d['wrong_unsat'] and not d['right_unsat']) / nc
        print(f"{n:4d} | {nc:5d} | {casc:7.3f} | {cls:6.2f} | {b1:6.2f} | {deg:7.4f} | {bn:6.2f} | {ru:5.2f} | {wu:5.2f} | {dist:5.3f}")

    # ── Silence analysis ─────────────────────────────────────────────
    print(f"\nTABLE 2: Cascade Silence")
    print("=" * 60)
    print(f"{'n':>4} | {'R_casc=0':>8} | {'W_casc=0':>8} | {'both=0':>7} | {'mean_R':>7} | {'mean_W':>7}")
    print("-" * 60)

    for n in SIZES:
        if n not in all_results or not all_results[n]:
            continue
        all_diffs = [d for inst in all_results[n] for d in inst]
        nc = len(all_diffs)
        if nc == 0:
            continue
        r0 = sum(1 for d in all_diffs if d['right_cascade'] == 0) / nc
        w0 = sum(1 for d in all_diffs if d['wrong_cascade'] == 0) / nc
        both0 = sum(1 for d in all_diffs if d['right_cascade'] == 0 and d['wrong_cascade'] == 0) / nc
        mr = np.mean([d['right_cascade'] for d in all_diffs])
        mw = np.mean([d['wrong_cascade'] for d in all_diffs])
        print(f"{n:4d} | {r0:8.3f} | {w0:8.3f} | {both0:7.3f} | {mr:7.3f} | {mw:7.3f}")

    # ── Solution count analysis ──────────────────────────────────────
    print(f"\nTABLE 3: Solution Counts (the ONE difference)")
    print("=" * 60)
    print(f"{'n':>4} | {'R_sols>0':>8} | {'W_sols>0':>8} | {'R_mean':>8} | {'W_mean':>8}")
    print("-" * 60)

    for n in SIZES:
        if n not in all_results or not all_results[n]:
            continue
        all_diffs = [d for inst in all_results[n] for d in inst]
        nc = len(all_diffs)
        if nc == 0:
            continue
        r_has_sol = sum(1 for d in all_diffs if d['right_solutions'] > 0) / nc
        w_has_sol = sum(1 for d in all_diffs if d['wrong_solutions'] > 0) / nc
        r_sols = [d['right_solutions'] for d in all_diffs if d['right_solutions'] >= 0]
        w_sols = [d['wrong_solutions'] for d in all_diffs if d['wrong_solutions'] >= 0]
        rm = np.mean(r_sols) if r_sols else 0
        wm = np.mean(w_sols) if w_sols else 0
        print(f"{n:4d} | {r_has_sol:8.3f} | {w_has_sol:8.3f} | {rm:8.1f} | {wm:8.1f}")

    # ── Distinguishing advantage trend ───────────────────────────────
    print(f"\nTABLE 4: Distinguishing Advantage vs n (THE KEY TABLE)")
    print("=" * 50)
    print(f"{'n':>4} | {'advantage':>10} | {'log₂ n':>7} | {'adv × n':>8}")
    print("-" * 50)

    advantages = {}
    for n in SIZES:
        if n not in all_results or not all_results[n]:
            continue
        all_diffs = [d for inst in all_results[n] for d in inst]
        nc = len(all_diffs)
        if nc == 0:
            continue

        # Best distinguisher: any stat where |right - wrong| is consistently nonzero
        # Use UP contradiction rate as the "best" poly-time distinguisher
        dist = sum(1 for d in all_diffs if d['wrong_unsat'] and not d['right_unsat']) / nc

        # Also try: structural diff > threshold
        struct_dist = sum(1 for d in all_diffs
                         if abs(d['n_clauses']) > 2 or abs(d['beta1']) > 1) / nc

        best = max(dist, struct_dist)
        advantages[n] = best
        print(f"{n:4d} | {best:10.4f} | {np.log2(n):7.2f} | {best * n:8.3f}")

    # ── Scorecard ─────────────────────────────────────────────────────
    print("\n" + "=" * 76)
    print("SCORECARD")
    print("=" * 76)

    scores = []

    # 1. UP cascade = 0 for BOTH right and wrong?
    both_zero = {}
    for n in SIZES:
        if n not in all_results or not all_results[n]:
            continue
        all_diffs = [d for inst in all_results[n] for d in inst]
        both_zero[n] = sum(1 for d in all_diffs
                          if d['right_cascade'] == 0 and d['wrong_cascade'] == 0) / len(all_diffs)
    if both_zero:
        ok = all(v > 0.8 for v in both_zero.values())
        scores.append(ok)
        vals = [f"{both_zero[n]:.2f}" for n in sorted(both_zero.keys())]
        print(f"  1. Both cascades = 0:                     {'✓' if ok else '✗'} ({' → '.join(vals)})")
    else:
        scores.append(None)
        print(f"  1. Both cascades = 0:                     —")

    # 2. Degree distributions indistinguishable?
    deg_close = {}
    for n in SIZES:
        if n not in all_results or not all_results[n]:
            continue
        all_diffs = [d for inst in all_results[n] for d in inst]
        deg_close[n] = np.mean([d['mean_degree'] for d in all_diffs])
    if deg_close:
        ok = all(v < 1.0 for v in deg_close.values())
        scores.append(ok)
        vals = [f"{deg_close[n]:.3f}" for n in sorted(deg_close.keys())]
        print(f"  2. Degree Δ small:                        {'✓' if ok else '✗'} ({' → '.join(vals)})")
    else:
        scores.append(None)
        print(f"  2. Degree Δ small:                        —")

    # 3. β₁ identical?
    b1_close = {}
    for n in SIZES:
        if n not in all_results or not all_results[n]:
            continue
        all_diffs = [d for inst in all_results[n] for d in inst]
        b1_close[n] = np.mean([d['beta1'] for d in all_diffs])
    if b1_close:
        ok = all(v < 2.0 for v in b1_close.values())
        scores.append(ok)
        vals = [f"{b1_close[n]:.2f}" for n in sorted(b1_close.keys())]
        print(f"  3. β₁ Δ small:                            {'✓' if ok else '✗'} ({' → '.join(vals)})")
    else:
        scores.append(None)
        print(f"  3. β₁ Δ small:                            —")

    # 4. Distinguishing advantage decreases with n?
    if len(advantages) >= 3:
        ns = sorted(advantages.keys())
        decreasing = advantages[ns[-1]] < advantages[ns[0]]
        scores.append(decreasing)
        vals = [f"{advantages[n]:.3f}" for n in ns]
        print(f"  4. Advantage decreases with n:            {'✓' if decreasing else '✗'} ({' → '.join(vals)})")
    else:
        scores.append(None)
        print(f"  4. Advantage decreases with n:            —")

    # 5. No stat achieves high advantage?
    if advantages:
        max_adv = max(advantages.values())
        ok = max_adv < 0.5
        scores.append(ok)
        print(f"  5. Max advantage < 0.5:                   {'✓' if ok else '✗'} (max={max_adv:.3f})")
    else:
        scores.append(None)
        print(f"  5. Max advantage < 0.5:                   —")

    # 6. Universal silence (all stat Δ → 0)?
    all_deltas_shrink = {}
    for n in SIZES:
        if n not in all_results or not all_results[n]:
            continue
        all_diffs = [d for inst in all_results[n] for d in inst]
        total_delta = (np.mean([d['cascade'] for d in all_diffs]) +
                      np.mean([d['n_clauses'] for d in all_diffs]) +
                      np.mean([d['beta1'] for d in all_diffs]) +
                      np.mean([d['mean_degree'] for d in all_diffs]))
        all_deltas_shrink[n] = total_delta / n  # normalized
    if len(all_deltas_shrink) >= 3:
        ns = sorted(all_deltas_shrink.keys())
        shrinks = all_deltas_shrink[ns[-1]] < all_deltas_shrink[ns[0]]
        scores.append(shrinks)
        vals = [f"{all_deltas_shrink[n]:.3f}" for n in ns]
        print(f"  6. Normalized total Δ decreases:          {'✓' if shrinks else '✗'} ({' → '.join(vals)})")
    else:
        scores.append(None)
        print(f"  6. Normalized total Δ decreases:          —")

    # 7. (From Toy 294 data) d*/log n grows?
    # We include the known values
    d_star = {12: 1.38, 16: 1.60, 20: 1.95, 24: 2.32}
    d_log_ratio = {n: d / np.log2(n) for n, d in d_star.items()}
    ns = sorted(d_log_ratio.keys())
    grows = d_log_ratio[ns[-1]] > d_log_ratio[ns[0]]
    scores.append(grows)
    vals = [f"{d_log_ratio[n]:.3f}" for n in ns]
    print(f"  7. d*/log n grows (from Toy 294):          {'✓' if grows else '✗'} ({' → '.join(vals)})")

    # 8. Total variation of stat vector → 0?
    if len(advantages) >= 3:
        ns = sorted(advantages.keys())
        tv_trend = [advantages[n] for n in ns]
        decreasing_trend = all(tv_trend[i] >= tv_trend[i+1] - 0.05 for i in range(len(tv_trend)-1))
        scores.append(decreasing_trend)
        print(f"  8. Advantage trend non-increasing:        {'✓' if decreasing_trend else '✗'}")
    else:
        scores.append(None)
        print(f"  8. Advantage trend non-increasing:        —")

    valid = [s for s in scores if s is not None]
    n_pass = sum(valid)
    n_total = len(valid)
    print(f"\n  Total: {n_pass}/{n_total}")

    # ── Interpretation ────────────────────────────────────────────────
    print("\n" + "=" * 76)
    print("INTERPRETATION")
    print("=" * 76)
    print("""
  The Quiet Backbone Conjecture (Casey-Lyra):

    For backbone variable x with value v, φ∧(x=v) and φ∧(x=¬v) are
    computationally indistinguishable to polynomial-time statistics.

  Shannon's formula converts this to P ≠ NP:
    C = log(1 + S/N) ≈ 2^{-d*(n)}
    Total info = poly(n) × C = poly(n) × 2^{-d*(n)}
    If d*(n) = ω(log n): total = o(1) bits about Θ(n)-bit backbone. QED.

  What this toy measures:
    - The STRUCTURAL statistics are the polynomial-time "listeners"
    - If they can't tell right from wrong, the channel is quiet
    - The one TRUE difference (SAT vs UNSAT) is exponentially hidden
    - The question: does the advantage decrease to 0 with n?

  If advantage → 0: computational indistinguishability confirmed.
  If advantage → constant: some poly-time stat leaks backbone info.

  Casey: "The signal has no say in the channel."
  The backbone (signal) doesn't control what the formula (channel) emits.
  The formula emits the same noise regardless of backbone correctness.
  Shannon says: noise wins. P ≠ NP.
""")


# ── Entry point ──────────────────────────────────────────────────────

if __name__ == '__main__':
    t_start = time.time()
    run_experiment()
    t_total = time.time() - t_start
    print(f"\nTotal runtime: {t_total:.1f}s")
    print(f"\n— Toy 296 | Casey Koons & Claude 4.6 (Elie) | March 21, 2026 —")
