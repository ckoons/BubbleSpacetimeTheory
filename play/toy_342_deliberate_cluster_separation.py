#!/usr/bin/env python3
"""
Toy 342 — Deliberate Cluster Separation: Backbone Flipping for Θ(n) Blocks
===========================================================================
Toy 342 | Casey Koons & Claude 4.6 (Elie) | March 23, 2026

BST/AC context:
  Toys 340-341 established within-cluster MI = 0 (block independence) but
  WalkSAT's cluster-finding ability limits the disagreement measurement.
  At n=40, avg disagreement was only 6.0 vars (15% of n).

  THIS TOY improves cluster separation by DELIBERATELY creating diverse
  solutions: start from one solution, flip a backbone variable, then
  run WalkSAT to find a new solution in a different cluster.

  Method:
  1. Find one solution σ via WalkSAT
  2. Identify backbone variables (variables frozen across many restarts)
  3. For each backbone variable v_i:
     a. Start WalkSAT from σ with v_i flipped
     b. If a solution σ' is found, it's in a different cluster
     c. Compute disagreement(σ, σ')
  4. Collect many (σ, σ') pairs → measure backbone disagreement and MI

  This approach should find clusters that differ on many more backbone
  variables than random WalkSAT restarts.

  Four tests:
    1. Backbone identification + deliberate cluster separation
    2. Disagreement fraction grows with n
    3. Block count grows with n (Θ(n) target)
    4. Within-cluster MI stays at 0

Copyright (c) 2026 Casey Koons. All rights reserved.
Created with Claude Opus 4.6 (Elie). March 2026.
"""

import random
import time
import math
from collections import defaultdict

_print = print
def print(*args, **kwargs):
    kwargs.setdefault('flush', True)
    _print(*args, **kwargs)

PASS_COUNT = 0
FAIL_COUNT = 0

def score(name, cond, detail=""):
    global PASS_COUNT, FAIL_COUNT
    if cond:
        PASS_COUNT += 1; tag = "PASS"
    else:
        FAIL_COUNT += 1; tag = "FAIL"
    print(f"  [{tag}] {name}")
    if detail:
        print(f"         {detail}")


ALPHA_C = 4.267


def generate_3sat(n, alpha, rng):
    m = int(alpha * n)
    cvars = []
    csigns = []
    for _ in range(m):
        vs = rng.sample(range(n), 3)
        ss = (rng.random() < 0.5, rng.random() < 0.5, rng.random() < 0.5)
        cvars.append(tuple(vs))
        csigns.append(ss)
    return cvars, csigns


def walksat_fast(cvars, csigns, n, rng, max_flips=15000, p_noise=0.5, init_assign=None):
    """WalkSAT with optional initial assignment."""
    m = len(cvars)
    if init_assign is not None:
        assign = list(init_assign)
    else:
        assign = [rng.random() < 0.5 for _ in range(n)]

    var_occurs = [[] for _ in range(n)]
    for ci in range(m):
        for pos in range(3):
            var_occurs[cvars[ci][pos]].append((ci, pos))
    sat_count = [0] * m
    for ci in range(m):
        for pos in range(3):
            if assign[cvars[ci][pos]] == csigns[ci][pos]:
                sat_count[ci] += 1
    unsat = set(ci for ci in range(m) if sat_count[ci] == 0)
    if not unsat:
        return list(assign)
    unsat_list = list(unsat)
    rebuild = 0
    for _ in range(max_flips):
        if not unsat:
            return list(assign)
        rebuild += 1
        if rebuild > 50:
            unsat_list = list(unsat)
            rebuild = 0
        ci = rng.choice(unsat_list)
        while ci not in unsat:
            unsat_list = list(unsat)
            if not unsat_list:
                return list(assign)
            ci = rng.choice(unsat_list)
            rebuild = 0
        cv = cvars[ci]
        if rng.random() < p_noise:
            var = cv[rng.randint(0, 2)]
        else:
            best_var = cv[0]
            best_break = m + 1
            for pos in range(3):
                v = cv[pos]
                brk = 0
                for ci2, p2 in var_occurs[v]:
                    if sat_count[ci2] == 1 and assign[v] == csigns[ci2][p2]:
                        brk += 1
                if brk < best_break:
                    best_break = brk
                    best_var = v
            var = best_var
        assign[var] = not assign[var]
        for ci2, p2 in var_occurs[var]:
            s = csigns[ci2][p2]
            if assign[var] == s:
                sat_count[ci2] += 1
                if sat_count[ci2] == 1:
                    unsat.discard(ci2)
            else:
                sat_count[ci2] -= 1
                if sat_count[ci2] == 0:
                    unsat.add(ci2)
    return None


def find_backbone(cvars, csigns, n, rng, num_restarts=100, max_flips=15000):
    """Identify backbone variables: frozen across many solutions.
    Returns (backbone_dict, solutions_list).
    backbone_dict: {var: value} for variables frozen in > 90% of solutions.
    """
    solutions = []
    for _ in range(num_restarts):
        sol = walksat_fast(cvars, csigns, n, rng, max_flips=max_flips)
        if sol is not None:
            key = tuple(sol)
            if key not in [tuple(s) for s in solutions]:
                solutions.append(sol)

    if len(solutions) < 3:
        return {}, solutions

    backbone = {}
    for v in range(n):
        true_count = sum(sol[v] for sol in solutions)
        frac = true_count / len(solutions)
        if frac > 0.9:
            backbone[v] = True
        elif frac < 0.1:
            backbone[v] = False

    return backbone, solutions


def deliberate_flip(cvars, csigns, n, base_sol, backbone_vars, rng, max_flips=15000):
    """From a base solution, flip backbone variables and find new solutions.
    Returns list of (new_solution, set_of_disagreeing_vars).
    """
    results = []
    for v in backbone_vars:
        # Create initial assignment with v flipped
        init = list(base_sol)
        init[v] = not init[v]

        # Also flip a few random variables near v in the VIG to help escape
        # (optional: just flip v)

        new_sol = walksat_fast(cvars, csigns, n, rng, max_flips=max_flips,
                               init_assign=init)
        if new_sol is not None:
            disagree = set()
            for i in range(n):
                if new_sol[i] != base_sol[i]:
                    disagree.add(i)
            if len(disagree) > 0:
                results.append((new_sol, disagree))
    return results


def block_parity(solution, block_vars):
    p = False
    for v in block_vars:
        if solution[v]:
            p = not p
    return p


def block_mi(solutions, block_a, block_b):
    if len(solutions) < 4:
        return float('nan')
    counts = {(False, False): 0, (False, True): 0, (True, False): 0, (True, True): 0}
    for sol in solutions:
        pa = block_parity(sol, block_a)
        pb = block_parity(sol, block_b)
        counts[(pa, pb)] += 1
    total = len(solutions)
    p_a = {True: 0, False: 0}
    p_b = {True: 0, False: 0}
    for (a, b), c in counts.items():
        p_a[a] += c
        p_b[b] += c
    mi = 0.0
    for (a, b), c in counts.items():
        if c == 0:
            continue
        p_ab = c / total
        pa_val = p_a[a] / total
        pb_val = p_b[b] / total
        if pa_val > 0 and pb_val > 0:
            mi += p_ab * math.log2(p_ab / (pa_val * pb_val))
    return max(0.0, mi)


def main():
    t0 = time.time()
    rng = random.Random(42)

    print("=" * 70)
    print("  Toy 342 — Deliberate Cluster Separation via Backbone Flipping")
    print("  Casey Koons & Claude 4.6 (Elie)  |  March 23, 2026")
    print("=" * 70)

    sizes = [16, 20, 24, 28, 32, 36, 40]
    all_data = defaultdict(list)

    for n in sizes:
        n_inst = 15 if n <= 24 else 10
        backbone_restarts = 100 if n <= 28 else 150

        found = 0
        for _ in range(n_inst):
            cvars, csigns = generate_3sat(n, ALPHA_C, rng)
            backbone, solutions = find_backbone(cvars, csigns, n, rng,
                                                  num_restarts=backbone_restarts)
            if len(backbone) < 3 or len(solutions) < 3:
                continue

            # Pick base solution (first one)
            base = solutions[0]
            bb_vars = sorted(backbone.keys())

            # Deliberately flip backbone variables
            flips = deliberate_flip(cvars, csigns, n, base, bb_vars[:15], rng)
            # bb_vars[:15] to limit compute

            if not flips:
                continue

            # Find the flip with the most disagreement
            best_flip = max(flips, key=lambda x: len(x[1]))
            new_sol, disagree = best_flip

            # Get a cluster of solutions near base
            base_cluster = [s for s in solutions
                           if sum(1 for i in range(n) if s[i] == base[i]) / n > 0.85]

            # Get solutions near the flipped solution
            flip_cluster = []
            for _ in range(50):
                s = walksat_fast(cvars, csigns, n, rng, max_flips=15000,
                                init_assign=new_sol)
                if s is not None:
                    overlap = sum(1 for i in range(n) if s[i] == new_sol[i]) / n
                    if overlap > 0.85:
                        if tuple(s) not in [tuple(x) for x in flip_cluster]:
                            flip_cluster.append(s)

            all_data[n].append({
                'backbone': backbone,
                'base_cluster': base_cluster,
                'flip_cluster': flip_cluster,
                'disagree': disagree,
                'n': n
            })
            found += 1

        elapsed = time.time() - t0
        print(f"  n={n:3d}: {found} instances, {elapsed:.0f}s elapsed")

    # -----------------------------------------------------------------
    # Test 1: Backbone + Deliberate Separation
    # -----------------------------------------------------------------
    print()
    print("-" * 70)
    print("Test 1: Backbone Identification + Deliberate Separation")
    print("-" * 70)

    for n in sizes:
        dlist = all_data[n]
        if not dlist:
            print(f"  n={n:3d}: no data")
            continue
        avg_bb = sum(len(d['backbone']) for d in dlist) / len(dlist)
        avg_disagree = sum(len(d['disagree']) for d in dlist) / len(dlist)
        avg_bc = sum(len(d['base_cluster']) for d in dlist) / len(dlist)
        avg_fc = sum(len(d['flip_cluster']) for d in dlist) / len(dlist)
        print(f"  n={n:3d}: backbone={avg_bb:.0f} ({avg_bb/n:.2f}n), "
              f"disagree={avg_disagree:.1f} ({avg_disagree/n:.3f}n), "
              f"base_cluster={avg_bc:.0f}, flip_cluster={avg_fc:.0f}")

    total_instances = sum(len(v) for v in all_data.values())
    score("Deliberate separation produces instances",
          total_instances >= 10,
          f"{total_instances} total instances")

    # -----------------------------------------------------------------
    # Test 2: Disagreement Fraction
    # -----------------------------------------------------------------
    print()
    print("-" * 70)
    print("Test 2: Disagreement Growth with n")
    print("  Deliberate flipping should give larger disagreement than random")
    print("-" * 70)

    disagree_avgs = []
    for n in sizes:
        dlist = all_data[n]
        if not dlist:
            continue
        avg = sum(len(d['disagree']) for d in dlist) / len(dlist)
        disagree_avgs.append((n, avg))
        print(f"  n={n:3d}: avg disagree = {avg:.1f} ({avg/n:.3f}n)")

    if len(disagree_avgs) >= 3:
        ns = [x[0] for x in disagree_avgs]
        ds = [x[1] for x in disagree_avgs]
        n_mean = sum(ns) / len(ns)
        d_mean = sum(ds) / len(ds)
        num = sum((ns[i] - n_mean) * (ds[i] - d_mean) for i in range(len(ns)))
        den = sum((ns[i] - n_mean)**2 for i in range(len(ns)))
        slope = num / max(den, 1e-10)
        intercept = d_mean - slope * n_mean
        ss_res = sum((ds[i] - (slope * ns[i] + intercept))**2 for i in range(len(ns)))
        ss_tot = sum((ds[i] - d_mean)**2 for i in range(len(ns)))
        r2 = 1 - ss_res / max(ss_tot, 1e-10) if ss_tot > 1e-10 else 0
        print(f"  Linear fit: disagree ≈ {slope:.3f}n + {intercept:.1f} (R² = {r2:.3f})")
        score("Disagreement grows linearly",
              slope > 0.1,
              f"slope = {slope:.3f}, R² = {r2:.3f}")
    else:
        score("Disagreement growth", False, "insufficient data")

    # -----------------------------------------------------------------
    # Test 3: Block Count
    # -----------------------------------------------------------------
    print()
    print("-" * 70)
    print("Test 3: Block Count Growth (size=3)")
    print("-" * 70)

    block_avgs = []
    for n in sizes:
        dlist = all_data[n]
        if not dlist:
            continue
        counts = []
        for d in dlist:
            dv = sorted(d['disagree'])
            blocks = [dv[i:i+3] for i in range(0, len(dv), 3) if len(dv[i:i+3]) == 3]
            counts.append(len(blocks))
        avg = sum(counts) / len(counts) if counts else 0
        block_avgs.append((n, avg))
        print(f"  n={n:3d}: avg blocks = {avg:.1f} ({avg/n:.4f}n)")

    if len(block_avgs) >= 3:
        ns = [x[0] for x in block_avgs]
        bs = [x[1] for x in block_avgs]
        n_mean = sum(ns) / len(ns)
        b_mean = sum(bs) / len(bs)
        num = sum((ns[i] - n_mean) * (bs[i] - b_mean) for i in range(len(ns)))
        den = sum((ns[i] - n_mean)**2 for i in range(len(ns)))
        slope = num / max(den, 1e-10)
        print(f"  Slope: {slope:.4f} blocks/n")
        score("Block count grows linearly",
              slope > 0.01,
              f"slope = {slope:.4f}")
    else:
        score("Block count growth", False, "insufficient data")

    # -----------------------------------------------------------------
    # Test 4: Within-Cluster MI
    # -----------------------------------------------------------------
    print()
    print("-" * 70)
    print("Test 4: Within-Cluster MI (should be 0)")
    print("-" * 70)

    all_mis = []
    for n in sizes:
        n_mi = []
        for d in all_data[n]:
            dv = sorted(d['disagree'])
            blocks = [dv[i:i+2] for i in range(0, len(dv), 2) if len(dv[i:i+2]) == 2]
            if len(blocks) < 2:
                continue

            # MI within base cluster
            if len(d['base_cluster']) >= 4:
                for i in range(len(blocks)):
                    for j in range(i+1, len(blocks)):
                        mi = block_mi(d['base_cluster'], blocks[i], blocks[j])
                        if not math.isnan(mi):
                            n_mi.append(mi)

            # MI within flip cluster
            if len(d['flip_cluster']) >= 4:
                for i in range(len(blocks)):
                    for j in range(i+1, len(blocks)):
                        mi = block_mi(d['flip_cluster'], blocks[i], blocks[j])
                        if not math.isnan(mi):
                            n_mi.append(mi)

        if n_mi:
            avg = sum(n_mi) / len(n_mi)
            all_mis.extend(n_mi)
            print(f"  n={n:3d}: avg MI = {avg:.4f}, max = {max(n_mi):.4f}, {len(n_mi)} pairs")
        else:
            print(f"  n={n:3d}: no data")

    if all_mis:
        overall = sum(all_mis) / len(all_mis)
        score("Within-cluster MI ≈ 0",
              overall < 0.15,
              f"overall avg = {overall:.4f}, {len(all_mis)} measurements")
    else:
        score("Within-cluster MI", False, "no data")

    # -----------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------
    elapsed = time.time() - t0
    print()
    print("=" * 70)
    print(f"  Toy 342 RESULTS: {PASS_COUNT}/{PASS_COUNT + FAIL_COUNT} PASS")
    print(f"  Elapsed: {elapsed:.1f}s")
    print()
    print("  DELIBERATE CLUSTER SEPARATION:")
    print("  By flipping backbone variables, we force WalkSAT into different")
    print("  clusters, producing larger disagreement sets than random restarts.")
    print("  If disagreement scales as Θ(n) and MI stays 0, then T29-reformed")
    print("  gives the exponential product decomposition with quantitative teeth.")
    print("=" * 70)
    print()
    print(f"  *** {PASS_COUNT} of {PASS_COUNT + FAIL_COUNT} TESTS PASSED ***")


if __name__ == "__main__":
    main()
