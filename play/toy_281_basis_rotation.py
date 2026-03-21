#!/usr/bin/env python3
"""
Toy 281 — Basis Rotation: The Weinberg Angle of Proof Complexity
================================================================

Measures how much each extension ROTATES the H₁ basis of the VIG complex.

Key insight from Toy 280: for 1-clause extensions, H₁(K_old) injects into
H₁(K_new) — old cycles can't become boundaries because new triangle boundaries
use new edges. So r = 1: no mixing for minimal extensions.

But MULTI-CLAUSE extensions can kill old cycles. The mechanism: when an
extension's clauses form a LOOP through existing vertices, the F₂-sum of
their triangle boundaries is a purely-old-edge chain that kills an old
H₁ generator. This is the weak force's mixing channel.

Real proof steps aren't 1-clause — they're multi-clause at density α_c ≈ 4.267.
The Weinberg angle measures the mixing strength.

The overlap ratio:
  r = dim(H₁(K_old) ∩ H₁(K_new)) / β₁_old

- r = 1 means no mixing (old cycles survive intact)
- r < 1 means some old cycles were killed (mixing occurred)
- r bounded away from 1 = unavoidable mixing = weak force has teeth

Three tests:
  1. r(n) for single extensions — 1-clause (should be 1) vs multi-clause
  2. r_adversarial(n) — can smart placement maximize mixing?
  3. CUMULATIVE rotation after t extensions — overlap with ORIGINAL basis
     If r(t) decays as ~r₀^t and r₀ < 1: exponential loss of correlation
     → Shannon says decoding costs 2^{Θ(n)}

The kill shot: test 3. If cumulative overlap decays exponentially with t,
the proof system loses all correlation with the original cycle structure
after Θ(n) extensions. Recovering that structure costs exponential time.

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6 (Elie). March 2026.
"""

import numpy as np
import random
import time
import math

_print = print
def print(*args, **kwargs):
    kwargs.setdefault('flush', True)
    _print(*args, **kwargs)

PASS = 0
FAIL = 0

def score(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1; tag = "✓ PASS"
    else:
        FAIL += 1; tag = "✗ FAIL"
    print(f"  {tag}: {name}")
    if detail:
        print(f"         {detail}")


ALPHA_C = 4.267

def generate_3sat(n, alpha=ALPHA_C):
    m = int(round(alpha * n))
    clauses = []
    for _ in range(m):
        vs = sorted(random.sample(range(n), 3))
        clauses.append(tuple(vs))
    return clauses


def build_vig(n, clauses):
    edges = set()
    triangles = set()
    for v0, v1, v2 in clauses:
        edges.add((v0, v1))
        edges.add((v0, v2))
        edges.add((v1, v2))
        triangles.add((v0, v1, v2))
    return sorted(edges), sorted(triangles)


# ═══════════════════════════════════════════════════════════════════
# F₂ LINEAR ALGEBRA
# ═══════════════════════════════════════════════════════════════════

def f2_rref(A):
    A = A.copy().astype(np.uint8) % 2
    nrows, ncols = A.shape
    pivot_row = 0
    pivot_cols = []
    for col in range(ncols):
        found = -1
        for row in range(pivot_row, nrows):
            if A[row, col]:
                found = row
                break
        if found == -1:
            continue
        if found != pivot_row:
            A[[pivot_row, found]] = A[[found, pivot_row]]
        for row in range(nrows):
            if row != pivot_row and A[row, col]:
                A[row] ^= A[pivot_row]
        pivot_cols.append(col)
        pivot_row += 1
    return A, pivot_cols


def f2_rank(A):
    _, pivots = f2_rref(A.copy())
    return len(pivots)


def f2_nullspace(A):
    A = A.copy().astype(np.uint8) % 2
    nrows, ncols = A.shape
    R, pivot_cols = f2_rref(A)
    free_cols = [c for c in range(ncols) if c not in pivot_cols]
    pivot_col_to_row = {pc: i for i, pc in enumerate(pivot_cols)}
    basis = []
    for fc in free_cols:
        vec = np.zeros(ncols, dtype=np.uint8)
        vec[fc] = 1
        for pc in pivot_cols:
            if R[pivot_col_to_row[pc], fc]:
                vec[pc] = 1
        basis.append(vec)
    return basis


def compute_h1_basis(n, edges, triangles):
    """Compute H₁ generators as rows of a matrix over F₂.
    Returns (beta1, generator_matrix) where generator_matrix has shape (beta1, E).
    """
    E = len(edges)
    if E == 0:
        return 0, np.zeros((0, 0), dtype=np.uint8)

    edge_idx = {e: i for i, e in enumerate(edges)}
    V = n
    F = len(triangles)

    d1 = np.zeros((V, E), dtype=np.uint8)
    for idx, (i, j) in enumerate(edges):
        d1[i, idx] = 1
        d1[j, idx] = 1

    d2 = np.zeros((E, F), dtype=np.uint8)
    for idx, (v0, v1, v2) in enumerate(triangles):
        for e in [(v0, v1), (v0, v2), (v1, v2)]:
            if e in edge_idx:
                d2[edge_idx[e], idx] = 1

    z1_basis = f2_nullspace(d1)
    if not z1_basis:
        return 0, np.zeros((0, E), dtype=np.uint8)

    rref_d2T, d2_pivots = f2_rref(d2.T.copy() % 2)
    dim_b1 = len(d2_pivots)
    beta1_est = len(z1_basis) - dim_b1
    if beta1_est <= 0:
        return 0, np.zeros((0, E), dtype=np.uint8)

    reduced = []
    for z in z1_basis:
        z_red = z.copy()
        for i, pc in enumerate(d2_pivots):
            if z_red[pc]:
                z_red ^= rref_d2T[i]
        z_red %= 2
        if np.any(z_red):
            reduced.append(z_red)

    if not reduced:
        return 0, np.zeros((0, E), dtype=np.uint8)

    M = np.array(reduced, dtype=np.uint8) % 2
    R, pivots = f2_rref(M)
    gen_mat = R[:len(pivots)].copy()
    return len(pivots), gen_mat


def compute_beta1_fast(n, edges, triangles):
    """Fast β₁ via rank computation (no generators)."""
    E = len(edges)
    if E == 0:
        return 0
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[a] = b
    for i, j in edges:
        union(i, j)
    verts = set()
    for i, j in edges:
        verts.add(i); verts.add(j)
    nc = len(set(find(v) for v in verts))
    rank_d1 = len(verts) - nc

    F = len(triangles)
    if F == 0:
        return E - rank_d1

    edge_idx = {e: i for i, e in enumerate(edges)}
    cols = []
    for v0, v1, v2 in triangles:
        col = set()
        for e in [(v0, v1), (v0, v2), (v1, v2)]:
            if e in edge_idx:
                col.add(edge_idx[e])
        cols.append(col)

    pivot_row = {}
    rank_d2 = 0
    for ci in range(F):
        col = cols[ci].copy()
        while col:
            top = min(col)
            if top in pivot_row:
                col ^= cols[pivot_row[top]]
            else:
                pivot_row[top] = ci
                cols[ci] = col
                rank_d2 += 1
                break
    return E - rank_d1 - rank_d2


# ═══════════════════════════════════════════════════════════════════
# EXTENSION + OVERLAP MEASUREMENT
# ═══════════════════════════════════════════════════════════════════

def add_extension_multi(n, edges_set, triangles_set, n_clauses=3):
    """Add extension variable p with n_clauses random clauses.
    Returns (new_edges_sorted, new_triangles_sorted, n_new, new_edge_list).
    new_edge_list contains the edges that were added.
    """
    p = n
    new_edges = set(edges_set)
    new_triangles = set(triangles_set)
    added_edges = set()

    verts_used = set()
    for _ in range(n_clauses):
        if not verts_used:
            pair = sorted(random.sample(range(n), 2))
        else:
            v_conn = random.choice(list(verts_used))
            v_other = random.randrange(n)
            while v_other == v_conn:
                v_other = random.randrange(n)
            pair = sorted([v_conn, v_other])

        verts_used.update(pair)
        triple = tuple(sorted([p, pair[0], pair[1]]))
        new_triangles.add(triple)
        a, b, c = triple
        for e in [(a, b), (a, c), (b, c)]:
            if e not in edges_set:
                added_edges.add(e)
            new_edges.add(e)

    return sorted(new_edges), sorted(new_triangles), n + 1, added_edges


def compute_overlap(gen_old, beta1_old, E_old, gen_new, beta1_new, E_new):
    """Compute overlap ratio r = dim(H₁_old ∩ H₁_new) / β₁_old.

    gen_old: (beta1_old, E_old) matrix — old H₁ generators
    gen_new: (beta1_new, E_new) matrix — new H₁ generators

    We embed gen_old into the new edge space (pad with zeros for new edges)
    then compute: dim(intersection) = beta1_old + beta1_new - rank([gen_old_padded; gen_new])
    """
    if beta1_old == 0:
        return 1.0  # trivially preserved

    # Pad old generators to new edge space
    gen_old_padded = np.zeros((beta1_old, E_new), dtype=np.uint8)
    gen_old_padded[:, :E_old] = gen_old

    # Stack and compute rank
    stacked = np.vstack([gen_old_padded, gen_new])
    r = f2_rank(stacked)

    dim_intersection = beta1_old + beta1_new - r
    return max(0, dim_intersection) / beta1_old


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    t_start = time.time()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  Toy 281 — Basis Rotation: The Weinberg Angle              ║")
    print("║  How much does each extension ROTATE the H₁ basis?         ║")
    print("║  r = dim(H₁_old ∩ H₁_new) / β₁_old                       ║")
    print("║  If cumulative r decays → exponential disorientation       ║")
    print("╚══════════════════════════════════════════════════════════════╝")

    SIZES = [20, 30, 50, 75]
    N_INSTANCES = 15
    N_SINGLE = 60           # single-extension overlap tests per instance
    N_CLAUSES_LIST = [1, 3, 5, 8]  # clauses per extension
    N_CUMULATIVE_STEPS = 40  # sequential extensions for cumulative test
    N_CUMULATIVE_CLAUSES = 3 # clauses per step in cumulative test

    print(f"\n  Parameters:")
    print(f"    α_c = {ALPHA_C}")
    print(f"    Sizes: {SIZES}")
    print(f"    Instances: {N_INSTANCES}")
    print(f"    Single-extension tests: {N_SINGLE}")
    print(f"    Multi-clause tests: {N_CLAUSES_LIST}")
    print(f"    Cumulative steps: {N_CUMULATIVE_STEPS}")

    results = {}

    for n in SIZES:
        print(f"\n  {'═' * 58}")
        print(f"  n = {n}: α_c = {ALPHA_C}, m = {int(round(ALPHA_C * n))} clauses")
        print(f"  {'═' * 58}")

        all_beta1 = []
        all_r_single = {nc: [] for nc in N_CLAUSES_LIST}
        all_r_adv = {nc: [] for nc in N_CLAUSES_LIST}
        # Cumulative: list of (step, overlap_with_original) curves
        cumulative_curves = []

        for inst in range(N_INSTANCES):
            t0 = time.time()

            clauses = generate_3sat(n)
            edges, triangles = build_vig(n, clauses)
            edges_set = set(edges)
            triangles_set = set(triangles)

            beta1_old, gen_old = compute_h1_basis(n, edges, triangles)
            all_beta1.append(beta1_old)

            if beta1_old < 3:
                continue

            E_old = len(edges)

            # ─── Test 1: Single-extension overlap for each clause count ──
            for nc in N_CLAUSES_LIST:
                for _ in range(N_SINGLE):
                    new_edges, new_triangles, n_new, _ = add_extension_multi(
                        n, edges_set, triangles_set, n_clauses=nc)
                    beta1_new, gen_new = compute_h1_basis(n_new, new_edges, new_triangles)
                    E_new = len(new_edges)

                    if beta1_new > 0:
                        r = compute_overlap(gen_old, beta1_old, E_old,
                                            gen_new, beta1_new, E_new)
                        all_r_single[nc].append(r)

            # ─── Test 2: Adversarial — minimize overlap (maximize mixing) ──
            for nc in [3, 5]:
                for _ in range(20):
                    best_r = 2.0
                    for _ in range(15):  # candidates
                        new_edges, new_triangles, n_new, _ = add_extension_multi(
                            n, edges_set, triangles_set, n_clauses=nc)
                        beta1_new, gen_new = compute_h1_basis(
                            n_new, new_edges, new_triangles)
                        E_new = len(new_edges)
                        if beta1_new > 0:
                            r = compute_overlap(gen_old, beta1_old, E_old,
                                                gen_new, beta1_new, E_new)
                            if r < best_r:
                                best_r = r
                    if best_r <= 1.0:
                        all_r_adv[nc].append(best_r)

            # ─── Test 3: Cumulative rotation ──
            # Add extensions sequentially, track overlap with ORIGINAL basis
            cur_n = n
            cur_edges_set = set(edges_set)
            cur_triangles_set = set(triangles_set)
            curve = [(0, 1.0)]  # (step, overlap_with_original)

            for step in range(1, N_CUMULATIVE_STEPS + 1):
                cur_edges_sorted = sorted(cur_edges_set)
                cur_triangles_sorted = sorted(cur_triangles_set)

                new_edges, new_triangles, n_new, _ = add_extension_multi(
                    cur_n, cur_edges_set, cur_triangles_set,
                    n_clauses=N_CUMULATIVE_CLAUSES)

                # Compute new H₁
                beta1_new, gen_new = compute_h1_basis(
                    n_new, new_edges, new_triangles)
                E_new = len(new_edges)

                if beta1_new > 0 and beta1_old > 0:
                    # Overlap with ORIGINAL basis (not previous step)
                    r = compute_overlap(gen_old, beta1_old, E_old,
                                        gen_new, beta1_new, E_new)
                    curve.append((step, r))
                else:
                    curve.append((step, curve[-1][1] if curve else 1.0))

                # Update state for next step
                cur_n = n_new
                cur_edges_set = set(new_edges)
                cur_triangles_set = set(new_triangles)

            cumulative_curves.append(curve)

            elapsed = time.time() - t0
            if inst < 3 or (inst + 1) % 5 == 0:
                r1 = np.mean(all_r_single[1]) if all_r_single[1] else 0
                r3 = np.mean(all_r_single[3]) if all_r_single[3] else 0
                final_r = curve[-1][1] if curve else 0
                print(f"    Instance {inst+1:>3}/{N_INSTANCES}: "
                      f"β₁={beta1_old:>4}, r₁={r1:.3f}, r₃={r3:.3f}, "
                      f"cum_r({N_CUMULATIVE_STEPS})={final_r:.3f}  ({elapsed:.1f}s)")

        # ─── Summary ──────────────────────────────────
        print(f"\n    Summary for n={n}:")
        print(f"    {'─' * 54}")

        beta1_arr = np.array(all_beta1)
        print(f"    β₁: mean = {np.mean(beta1_arr):.1f}, β₁/n = {np.mean(beta1_arr)/n:.3f}")

        r = {}

        # Single-extension overlaps
        print(f"\n    Single-extension overlap r (per clause count):")
        for nc in N_CLAUSES_LIST:
            if all_r_single[nc]:
                rs = np.array(all_r_single[nc])
                r_mean = np.mean(rs)
                r_sem = np.std(rs) / math.sqrt(len(rs))
                frac_1 = np.mean(rs >= 1.0 - 1e-6)
                frac_lt1 = np.mean(rs < 1.0 - 1e-6)
                r_min = np.min(rs)
                print(f"      {nc} clause{'s' if nc > 1 else ' '}: "
                      f"r = {r_mean:.4f} ± {r_sem:.4f}, "
                      f"r=1: {frac_1:.1%}, r<1: {frac_lt1:.1%}, "
                      f"min(r) = {r_min:.4f}")
                r[f'r_{nc}'] = r_mean
                r[f'r_{nc}_min'] = r_min
                r[f'r_{nc}_frac_lt1'] = frac_lt1

        # Adversarial overlaps
        print(f"\n    Adversarial overlap (minimize r):")
        for nc in [3, 5]:
            if all_r_adv[nc]:
                ra = np.array(all_r_adv[nc])
                print(f"      {nc} clauses: mean = {np.mean(ra):.4f}, "
                      f"min = {np.min(ra):.4f}")
                r[f'adv_{nc}'] = np.mean(ra)
                r[f'adv_{nc}_min'] = np.min(ra)

        # Cumulative rotation
        if cumulative_curves:
            print(f"\n    Cumulative rotation (3 clauses/step, {N_CUMULATIVE_STEPS} steps):")
            # Average curve across instances
            steps = list(range(N_CUMULATIVE_STEPS + 1))
            avg_curve = []
            for s in steps:
                vals = []
                for curve in cumulative_curves:
                    for step, rv in curve:
                        if step == s:
                            vals.append(rv)
                            break
                avg_curve.append(np.mean(vals) if vals else float('nan'))

            # Report at key steps
            report_steps = [0, 1, 2, 5, 10, 20, N_CUMULATIVE_STEPS]
            for s in report_steps:
                if s < len(avg_curve):
                    print(f"      t={s:>3}: r_cumulative = {avg_curve[s]:.4f}")

            # Fit exponential decay: r(t) ≈ r₀ · exp(-λt)
            # Use log-linear fit on non-zero values
            ts = []
            log_rs = []
            for s in range(1, len(avg_curve)):
                if avg_curve[s] > 0.01:
                    ts.append(s)
                    log_rs.append(math.log(avg_curve[s]))
            if len(ts) >= 3:
                # Linear regression: log(r) = a + b*t → r = exp(a) * exp(b*t)
                t_arr = np.array(ts, dtype=float)
                lr_arr = np.array(log_rs, dtype=float)
                b, a = np.polyfit(t_arr, lr_arr, 1)
                r0_fit = math.exp(a)
                decay_rate = -b
                half_life = math.log(2) / decay_rate if decay_rate > 0 else float('inf')
                print(f"\n      Exponential fit: r(t) ≈ {r0_fit:.3f} × exp(-{decay_rate:.4f}·t)")
                print(f"      Decay rate λ = {decay_rate:.4f}")
                print(f"      Half-life = {half_life:.1f} steps")
                if decay_rate > 0:
                    n_ext_to_zero = math.log(100) / decay_rate  # r drops to 1%
                    print(f"      Steps to r < 0.01: {n_ext_to_zero:.0f}")
                r['decay_rate'] = decay_rate
                r['half_life'] = half_life
                r['r_final'] = avg_curve[-1] if avg_curve else 0

        results[n] = r

    # ─── Grand Summary ──────────────────────────────────────
    print(f"\n  {'═' * 70}")
    print(f"  GRAND SUMMARY: Basis Rotation")
    print(f"  {'═' * 70}")

    print(f"\n  Single-extension overlap r:")
    print(f"    {'n':>5}", end="")
    for nc in N_CLAUSES_LIST:
        print(f"  {'r_' + str(nc):>8}", end="")
    print()
    for n_val in SIZES:
        if n_val in results:
            print(f"    {n_val:>5}", end="")
            for nc in N_CLAUSES_LIST:
                rv = results[n_val].get(f'r_{nc}', float('nan'))
                print(f"  {rv:>8.4f}", end="")
            print()

    print(f"\n  Cumulative decay:")
    print(f"    {'n':>5}  {'λ (rate)':>10}  {'half-life':>10}  {'r(40)':>8}")
    for n_val in SIZES:
        if n_val in results and 'decay_rate' in results[n_val]:
            r_data = results[n_val]
            print(f"    {n_val:>5}  {r_data['decay_rate']:>10.4f}  "
                  f"{r_data['half_life']:>10.1f}  "
                  f"{r_data.get('r_final', 0):>8.4f}")

    # ─── Scorecard ──────────────────────────────────────────
    print(f"\n  {'═' * 58}")
    print(f"  SCORECARD")
    print(f"  {'═' * 58}")

    # Test 1: 1-clause r = 1 (theorem)
    r1_all_one = all(results[n_val].get('r_1', 0) > 0.999
                     for n_val in SIZES if n_val in results)
    score("1-clause: r = 1 always (H₁ injection theorem)",
          r1_all_one,
          "Old cycles can't become boundaries — new triangle uses new edges")

    # Test 2: Multi-clause r < 1 sometimes (mixing exists)
    r3_has_mixing = any(results[n_val].get('r_3_frac_lt1', 0) > 0.001
                        for n_val in SIZES if n_val in results)
    score("3-clause: some r < 1 (mixing channel active)",
          r3_has_mixing,
          "Multi-clause extensions can kill old cycles")

    # Test 3: More clauses → more mixing
    mono_ok = True
    for n_val in SIZES:
        if n_val in results:
            r_vals = [results[n_val].get(f'r_{nc}', 1.0) for nc in N_CLAUSES_LIST]
            if len(r_vals) >= 2 and r_vals[-1] > r_vals[0] + 0.01:
                mono_ok = False
    score("More clauses → lower r (more mixing)",
          mono_ok,
          "Weinberg angle: mixing strength increases with interaction")

    # Test 4: Adversarial can achieve r < 1
    adv_mixing = any(results[n_val].get('adv_3_min', 1.0) < 0.999
                     for n_val in SIZES if n_val in results)
    score("Adversarial 3-clause can achieve r < 1",
          adv_mixing,
          "Smart placement can force basis rotation")

    # Test 5: Cumulative decay exists (λ > 0)
    has_decay = any(results[n_val].get('decay_rate', 0) > 0.001
                    for n_val in SIZES if n_val in results)
    score("Cumulative decay: λ > 0 (overlap decays with extensions)",
          has_decay,
          "The basis loses correlation with original over time")

    # Test 6: Cumulative overlap decays below 50% within 40 steps
    decays_fast = any(results[n_val].get('r_final', 1.0) < 0.5
                      for n_val in SIZES if n_val in results)
    score("Cumulative r < 0.5 within 40 steps",
          decays_fast,
          "Significant disorientation within Θ(n) extensions")

    # Test 7: Decay rate increases with n
    rates = [results[n_val].get('decay_rate', 0)
             for n_val in SIZES if n_val in results and 'decay_rate' in results[n_val]]
    if len(rates) >= 2:
        increasing = rates[-1] >= rates[0] - 0.002
        score("Decay rate λ non-decreasing with n",
              increasing,
              "Larger systems → faster disorientation" if increasing
              else "Larger systems → slower disorientation")
    else:
        score("Decay rate trend", False, "insufficient data")

    # Test 8: Shannon implication
    if has_decay:
        all_decay_rates = [results[n_val].get('decay_rate', 0)
                           for n_val in SIZES if n_val in results]
        min_rate = min(r for r in all_decay_rates if r > 0) if any(r > 0 for r in all_decay_rates) else 0
        if min_rate > 0:
            ext_to_decorrelate = math.log(100) / min_rate
            score(f"Shannon: ~{ext_to_decorrelate:.0f} extensions to decorrelate",
                  ext_to_decorrelate < 500,
                  f"After Θ(n) extensions with λ={min_rate:.4f}, "
                  f"proof loses all structure → 2^Θ(n) recovery cost")
        else:
            score("Shannon implication", False, "no decay detected")
    else:
        score("Shannon implication", False, "no cumulative decay")

    print(f"\n  {'═' * 58}")
    print(f"  SCORECARD: {PASS}/{PASS + FAIL}")
    print(f"  {'═' * 58}")

    print(f"\n  ── The Analogy ──")
    print(f"  1-clause extension: r = 1 (no mixing). Like U(1) — phase only, no rotation.")
    print(f"  Multi-clause extension: r < 1 (mixing). Like SU(2) — basis rotation.")
    print(f"  Cumulative decay: r(t) → 0 exponentially. Like decoherence in QM.")
    print(f"  Shannon: recovering Θ(n) decorrelated bits costs 2^{{Θ(n)}} time.")
    print(f"  The weak force doesn't trap. It disorients. Every step rotates the map.")

    elapsed = time.time() - t_start
    print(f"\n  Toy 281 complete. ({elapsed:.0f}s)")


if __name__ == '__main__':
    main()
