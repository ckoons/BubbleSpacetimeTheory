#!/usr/bin/env python3
"""
Toy 321: Frontier Information Flow — Width vs. Backbone Access
===============================================================
Tests whether sequential narrow-width probing can accumulate backbone
information, or whether it plateaus (confirming parallel constraint checking).

The LDPC bedrock claim: backbone information is delocalized across Θ(n)
independent cycles. A width-w "view" (connected subgraph of w variables)
can determine at most c·w backbone bits, where c ≈ 1/expansion_ratio.
Multiple independent views of the SAME width do NOT accumulate — they
see the SAME backbone bits because the LDPC expansion entangles them.

Four tests:
  T1: Width-backbone curve — window of w vars → backbone bits determined
  T2: Sequential accumulation — k windows of size w → union plateaus?
  T3: Random walk probing — sliding window → cumulative plateau?
  T4: Expansion ratio — direct Tanner graph measurement

Key predictions (from T52 + LDPC):
  T1: backbone_bits(w) ≤ c·w, linear with slope < 1
  T2: union(k windows) → plateau at O(w), NOT O(k·w)
  T3: cumulative along walk → plateau at O(w) regardless of walk length
  T4: expansion ≥ 2 for small sets (random 3-SAT at α_c)

If confirmed → LDPC bedrock holds → proof by contradiction closes P≠NP gap.

Casey Koons & Claude 4.6 (Elie), March 22, 2026.
"""

import numpy as np
from collections import defaultdict
import random
import time
import sys

# ── Parameters ────────────────────────────────────────────────────────
SIZES = [14, 16, 18, 20]          # n values (exhaustive backbone feasible)
ALPHA = 4.267                      # critical threshold
N_INSTANCES = 40                   # instances per size
N_WINDOWS = 100                    # random windows per width per instance
K_ROUNDS = 20                      # sequential accumulation rounds
WALK_LENGTH = 200                  # random walk steps
SEED = 321

# Width fractions to test
WIDTH_FRACS = [0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]


# ── Random 3-SAT generator ───────────────────────────────────────────

def gen_3sat(n, alpha=ALPHA, rng=None):
    """Generate random 3-SAT at critical threshold."""
    if rng is None:
        rng = random.Random()
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vs = rng.sample(range(1, n + 1), 3)
        clause = tuple(v * rng.choice([-1, 1]) for v in vs)
        clauses.append(clause)
    return clauses, m


# ── Backbone computation (vectorized) ─────────────────────────────────

def compute_backbone(clauses, n):
    """
    Vectorized exhaustive backbone computation.
    Returns: (backbone_dict {var: value}, solution_matrix, n_solutions)
    """
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
        return None, None, 0

    # Extract solution matrix: (n_sol × n)
    sol_indices = np.where(sat)[0]
    sol_matrix = np.zeros((n_sol, n), dtype=np.int8)
    for v in range(n):
        sol_matrix[:, v] = (sol_indices >> v) & 1

    backbone = {}
    for v in range(n):
        col = sol_matrix[:, v]
        if np.all(col == 1):
            backbone[v] = 1
        elif np.all(col == 0):
            backbone[v] = 0

    return backbone, sol_matrix, n_sol


# ── Variable Interaction Graph ────────────────────────────────────────

def build_vig(clauses, n):
    """Build VIG: adjacency list and edge set."""
    adj = defaultdict(set)
    for clause in clauses:
        vs = [abs(lit) - 1 for lit in clause]
        for i in range(len(vs)):
            for j in range(i + 1, len(vs)):
                adj[vs[i]].add(vs[j])
                adj[vs[j]].add(vs[i])
    return adj


# ── Connected window sampling ─────────────────────────────────────────

def random_connected_window(adj, n, w, rng):
    """
    Sample a random connected subgraph of w variables via BFS
    with random neighbor selection.
    """
    start = rng.randint(0, n - 1)
    visited = {start}
    frontier = [start]

    while len(visited) < w and frontier:
        # Pick random frontier node
        idx = rng.randint(0, len(frontier) - 1)
        node = frontier[idx]
        neighbors = [nb for nb in adj[node] if nb not in visited]
        if neighbors:
            next_node = rng.choice(neighbors)
            visited.add(next_node)
            frontier.append(next_node)
        else:
            frontier.pop(idx)

    return frozenset(visited)


# ── Backbone bits from window ─────────────────────────────────────────

def backbone_bits_in_window(window_vars, clauses, sol_matrix, backbone, n):
    """
    Given a window (set of variable indices), find clauses entirely within
    the window, then count how many backbone variables are determined by
    those clauses alone.

    Method: filter solutions to those consistent with ALL window-internal
    clauses. Check which backbone variables are forced.
    """
    window_set = set(window_vars)

    # Collect clauses internal to window
    internal_clauses = []
    for clause in clauses:
        vs = set(abs(lit) - 1 for lit in clause)
        if vs.issubset(window_set):
            internal_clauses.append(clause)

    if not internal_clauses:
        return set()

    # Filter solutions: keep those satisfying all internal clauses
    # (All original solutions satisfy them, but we're asking: what do
    # the internal clauses ALONE force?)
    # We need solutions of the SUBSYSTEM, not just the original formula.
    # Generate all 2^w assignments to window variables.
    w = len(window_vars)
    window_list = sorted(window_vars)
    var_to_idx = {v: i for i, v in enumerate(window_list)}

    # For each assignment to window variables, check internal clauses
    n_sub = 2 ** w
    if n_sub > 2**22:  # safety limit
        return _backbone_bits_sampling(window_list, internal_clauses, backbone)

    sub_bits = np.arange(n_sub, dtype=np.int32)
    sub_vals = [(sub_bits >> i) & 1 for i in range(w)]

    sat = np.ones(n_sub, dtype=bool)
    for clause in internal_clauses:
        clause_sat = np.zeros(n_sub, dtype=bool)
        for lit in clause:
            v = abs(lit) - 1
            idx = var_to_idx.get(v)
            if idx is None:
                continue
            if lit > 0:
                clause_sat |= sub_vals[idx].astype(bool)
            else:
                clause_sat |= ~sub_vals[idx].astype(bool)
        sat &= clause_sat

    # Check which backbone variables in window are forced
    determined = set()
    for v in backbone:
        if v not in window_set:
            continue
        idx = var_to_idx[v]
        col = sub_vals[idx][sat]
        if len(col) == 0:
            continue
        if np.all(col == 1) or np.all(col == 0):
            determined.add(v)

    return determined


def _backbone_bits_sampling(window_list, internal_clauses, backbone):
    """Fallback: random sampling for large windows."""
    rng = random.Random(42)
    n_samples = 10000
    vals_by_var = defaultdict(set)
    var_set = set(window_list)

    for _ in range(n_samples):
        assignment = {v: rng.randint(0, 1) for v in window_list}
        ok = True
        for clause in internal_clauses:
            clause_sat = False
            for lit in clause:
                v = abs(lit) - 1
                if v not in var_set:
                    continue
                val = assignment[v]
                if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                    clause_sat = True
                    break
            if not clause_sat:
                ok = False
                break
        if ok:
            for v in backbone:
                if v in var_set:
                    vals_by_var[v].add(assignment[v])

    return {v for v in backbone if v in var_set and len(vals_by_var.get(v, {0, 1})) == 1}


# ── Expansion measurement ─────────────────────────────────────────────

def measure_expansion(adj, n, max_set_size=None):
    """
    Measure vertex expansion of VIG for random subsets of various sizes.
    Expansion(S) = |N(S) \ S| / |S|
    Returns: {size: avg_expansion}
    """
    if max_set_size is None:
        max_set_size = n // 2
    rng = random.Random(42)
    expansion = {}

    for s in range(1, min(max_set_size + 1, n)):
        ratios = []
        n_trials = min(200, max(50, 1000 // s))
        for _ in range(n_trials):
            # Random connected subset of size s
            start = rng.randint(0, n - 1)
            S = {start}
            front = [start]
            while len(S) < s and front:
                idx = rng.randint(0, len(front) - 1)
                node = front[idx]
                nbrs = [nb for nb in adj[node] if nb not in S]
                if nbrs:
                    nxt = rng.choice(nbrs)
                    S.add(nxt)
                    front.append(nxt)
                else:
                    front.pop(idx)
            if len(S) < s:
                continue
            # Neighborhood
            N_S = set()
            for v in S:
                for nb in adj[v]:
                    if nb not in S:
                        N_S.add(nb)
            if len(S) > 0:
                ratios.append(len(N_S) / len(S))
        if ratios:
            expansion[s] = np.mean(ratios)

    return expansion


# ── Betti number (graph-theoretic) ────────────────────────────────────

def compute_betti1(clauses, n):
    """
    β₁ = |E| - |V_active| + components (graph-theoretic, not simplicial).
    """
    edges = set()
    active = set()
    adj_local = defaultdict(set)
    for clause in clauses:
        vs = [abs(lit) - 1 for lit in clause]
        for v in vs:
            active.add(v)
        for i in range(len(vs)):
            for j in range(i + 1, len(vs)):
                u, v2 = min(vs[i], vs[j]), max(vs[i], vs[j])
                edges.add((u, v2))
                adj_local[u].add(v2)
                adj_local[v2].add(u)

    # Connected components via BFS
    visited = set()
    comps = 0
    for v in active:
        if v not in visited:
            comps += 1
            queue = [v]
            visited.add(v)
            while queue:
                node = queue.pop()
                for nb in adj_local[node]:
                    if nb not in visited:
                        visited.add(nb)
                        queue.append(nb)

    return max(0, len(edges) - len(active) + comps)


# ══════════════════════════════════════════════════════════════════════
#  TEST 1: Width-Backbone Curve
# ══════════════════════════════════════════════════════════════════════

def test1_width_backbone_curve(n, clauses, adj, sol_matrix, backbone, rng):
    """
    For each width w, sample random connected windows and measure
    average backbone bits determined.
    Returns: {w: (mean_bb_bits, std_bb_bits, mean_internal_clauses)}
    """
    results = {}
    bb_set = set(backbone.keys())
    n_bb = len(bb_set)

    for frac in WIDTH_FRACS:
        w = max(2, int(frac * n))
        if w > n:
            w = n

        bb_counts = []
        clause_counts = []
        for _ in range(N_WINDOWS):
            window = random_connected_window(adj, n, w, rng)
            determined = backbone_bits_in_window(window, clauses, sol_matrix, backbone, n)
            bb_counts.append(len(determined))
            # Count internal clauses
            ws = set(window)
            ic = sum(1 for cl in clauses if set(abs(l)-1 for l in cl).issubset(ws))
            clause_counts.append(ic)

        results[w] = (np.mean(bb_counts), np.std(bb_counts),
                      np.mean(clause_counts), n_bb)

    return results


# ══════════════════════════════════════════════════════════════════════
#  TEST 2: Sequential Accumulation
# ══════════════════════════════════════════════════════════════════════

def test2_sequential_accumulation(n, clauses, adj, sol_matrix, backbone, rng):
    """
    For width w, run k independent windows and take the union of
    determined backbone bits. Does the union grow linearly or plateau?
    Returns: {w: [(k, union_size), ...]}
    """
    results = {}
    test_fracs = [0.15, 0.25, 0.4]

    for frac in test_fracs:
        w = max(3, int(frac * n))
        if w > n:
            w = n

        trajectory = []
        union_bb = set()
        for k in range(1, K_ROUNDS + 1):
            window = random_connected_window(adj, n, w, rng)
            determined = backbone_bits_in_window(window, clauses, sol_matrix, backbone, n)
            union_bb |= determined
            trajectory.append((k, len(union_bb)))

        results[w] = trajectory

    return results


# ══════════════════════════════════════════════════════════════════════
#  TEST 3: Random Walk Probing
# ══════════════════════════════════════════════════════════════════════

def test3_random_walk(n, clauses, adj, sol_matrix, backbone, rng):
    """
    Sliding window along a random walk on VIG.
    At each step: add one variable, drop one (FIFO), measure backbone bits.
    Returns: {w: [(step, cumulative_bb_bits), ...]}
    """
    results = {}
    test_fracs = [0.15, 0.25, 0.4]

    for frac in test_fracs:
        w = max(3, int(frac * n))
        if w > n:
            w = n

        # Initialize window via BFS
        start = rng.randint(0, n - 1)
        window_list = [start]
        visited = {start}
        front = [start]
        while len(window_list) < w and front:
            idx = rng.randint(0, len(front) - 1)
            node = front[idx]
            nbrs = [nb for nb in adj[node] if nb not in visited]
            if nbrs:
                nxt = rng.choice(nbrs)
                visited.add(nxt)
                window_list.append(nxt)
                front.append(nxt)
            else:
                front.pop(idx)

        cumulative_bb = set()
        trajectory = []

        # Walk: at each step, random walk from last-added variable
        cursor = window_list[-1] if window_list else start
        for step in range(WALK_LENGTH):
            # Move cursor to random neighbor
            nbrs = list(adj[cursor])
            if not nbrs:
                break
            cursor = rng.choice(nbrs)

            # Update window: add cursor, drop oldest
            if cursor not in set(window_list):
                window_list.append(cursor)
                if len(window_list) > w:
                    window_list.pop(0)
            else:
                # Already in window, just shift
                window_list.append(cursor)
                if len(window_list) > w:
                    window_list.pop(0)

            # Measure every 5 steps (performance)
            if step % 5 == 0:
                window = frozenset(window_list[:w])
                determined = backbone_bits_in_window(
                    window, clauses, sol_matrix, backbone, n)
                cumulative_bb |= determined
                trajectory.append((step, len(cumulative_bb)))

        results[w] = trajectory

    return results


# ══════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════

def main():
    print("=" * 72)
    print("TOY 321: FRONTIER INFORMATION FLOW — WIDTH VS. BACKBONE ACCESS")
    print("=" * 72)
    print(f"Sizes: {SIZES} | Instances: {N_INSTANCES} | Windows: {N_WINDOWS}")
    print(f"Width fractions: {WIDTH_FRACS}")
    print()

    master_rng = random.Random(SEED)
    all_results = {}

    for n in SIZES:
        t0 = time.time()
        print(f"\n{'─'*72}")
        print(f"  n = {n}")
        print(f"{'─'*72}")

        # Collect per-instance results
        t1_all = defaultdict(list)  # w -> list of (mean_bb, n_bb)
        t2_all = defaultdict(list)  # w -> list of trajectories
        t3_all = defaultdict(list)  # w -> list of trajectories
        expansion_all = defaultdict(list)
        betti_vals = []
        bb_sizes = []
        valid = 0
        attempts = 0

        while valid < N_INSTANCES and attempts < N_INSTANCES * 5:
            attempts += 1
            seed_i = master_rng.randint(0, 10**9)
            rng_i = random.Random(seed_i)
            clauses, m = gen_3sat(n, ALPHA, rng_i)
            backbone, sol_matrix, n_sol = compute_backbone(clauses, n)

            if backbone is None or len(backbone) < 2 or n_sol == 0:
                continue

            valid += 1
            adj = build_vig(clauses, n)
            bb_sizes.append(len(backbone))
            betti_vals.append(compute_betti1(clauses, n))

            # Test 1
            r1 = test1_width_backbone_curve(n, clauses, adj, sol_matrix, backbone, rng_i)
            for w, (mean_bb, std_bb, mean_cl, n_bb) in r1.items():
                t1_all[w].append((mean_bb, n_bb))

            # Test 2
            r2 = test2_sequential_accumulation(n, clauses, adj, sol_matrix, backbone, rng_i)
            for w, traj in r2.items():
                t2_all[w].append(traj)

            # Test 3 (every 4th instance — expensive)
            if valid % 4 == 1:
                r3 = test3_random_walk(n, clauses, adj, sol_matrix, backbone, rng_i)
                for w, traj in r3.items():
                    t3_all[w].append(traj)

            # Test 4: expansion (every 4th instance)
            if valid % 4 == 1:
                exp = measure_expansion(adj, n, max_set_size=n // 2)
                for s, ratio in exp.items():
                    expansion_all[s].append(ratio)

            if valid % 10 == 0:
                print(f"  ... {valid}/{N_INSTANCES} instances ({time.time()-t0:.1f}s)")

        print(f"\n  Valid instances: {valid}/{attempts}")
        print(f"  Avg backbone size: {np.mean(bb_sizes):.1f} ({np.mean(bb_sizes)/n:.1%} of n)")
        print(f"  Avg beta_1: {np.mean(betti_vals):.1f}")

        # ── Report Test 1 ──────────────────────────────────────
        print(f"\n  --- TEST 1: Width-Backbone Curve (n={n}) ---")
        print(f"  {'w':>4} {'w/n':>6} {'bb_bits':>8} {'bb/|B|':>8} {'bb/w':>8} {'linear?':>8}")
        print(f"  {'─'*50}")

        t1_summary = {}
        for w in sorted(t1_all.keys()):
            data = t1_all[w]
            mean_bb = np.mean([d[0] for d in data])
            mean_nbb = np.mean([d[1] for d in data])
            ratio_B = mean_bb / mean_nbb if mean_nbb > 0 else 0
            ratio_w = mean_bb / w if w > 0 else 0
            t1_summary[w] = (mean_bb, ratio_B, ratio_w)
            print(f"  {w:>4} {w/n:>6.2f} {mean_bb:>8.2f} {ratio_B:>8.3f} {ratio_w:>8.3f} "
                  f"{'<1 ✓' if ratio_w < 1 else '>1 ✗':>8}")

        # Linearity check: fit bb = c * w
        ws = sorted(t1_summary.keys())
        if len(ws) >= 3:
            x = np.array(ws, dtype=float)
            y = np.array([t1_summary[w][0] for w in ws])
            # Linear fit through origin
            c_fit = np.sum(x * y) / np.sum(x * x)
            residuals = y - c_fit * x
            r_squared = 1 - np.sum(residuals**2) / np.sum((y - np.mean(y))**2)
            print(f"\n  Linear fit: bb_bits ≈ {c_fit:.4f} × w  (R² = {r_squared:.4f})")
            print(f"  Slope c = {c_fit:.4f} — each width-1 increase yields {c_fit:.3f} backbone bits")

        # ── Report Test 2 ──────────────────────────────────────
        print(f"\n  --- TEST 2: Sequential Accumulation (n={n}) ---")
        for w in sorted(t2_all.keys()):
            trajs = t2_all[w]
            if not trajs:
                continue
            # Average trajectory
            max_k = min(len(t) for t in trajs)
            avg_traj = []
            for ki in range(max_k):
                vals = [t[ki][1] for t in trajs]
                avg_traj.append(np.mean(vals))

            first = avg_traj[0] if avg_traj else 0
            last = avg_traj[-1] if avg_traj else 0
            mean_bb = np.mean(bb_sizes)
            growth = last / first if first > 0 else float('inf')
            plateau = "PLATEAU ✓" if growth < 2.0 else f"GROWS ×{growth:.1f}"

            print(f"  w={w:>3} (w/n={w/n:.2f}): "
                  f"k=1→{first:.1f} bb, k={max_k}→{last:.1f} bb  "
                  f"({plateau})  [|B|={mean_bb:.0f}]")

            # Show trajectory
            show_k = [0, 1, 2, 4, 9, 14, 19]
            traj_str = "    k: "
            for ki in show_k:
                if ki < len(avg_traj):
                    traj_str += f"{ki+1:>3}→{avg_traj[ki]:>5.1f}  "
            print(traj_str)

        # ── Report Test 3 ──────────────────────────────────────
        if t3_all:
            print(f"\n  --- TEST 3: Random Walk Probing (n={n}) ---")
            for w in sorted(t3_all.keys()):
                trajs = t3_all[w]
                if not trajs:
                    continue
                # Show first and last cumulative values
                firsts = [t[0][1] if t else 0 for t in trajs]
                lasts = [t[-1][1] if t else 0 for t in trajs]
                first_avg = np.mean(firsts)
                last_avg = np.mean(lasts)
                growth = last_avg / first_avg if first_avg > 0 else float('inf')
                n_steps = trajs[0][-1][0] if trajs and trajs[0] else 0
                plateau = "PLATEAU ✓" if growth < 2.5 else f"GROWS ×{growth:.1f}"
                print(f"  w={w:>3} (w/n={w/n:.2f}): "
                      f"step=0→{first_avg:.1f}, step={n_steps}→{last_avg:.1f}  "
                      f"({plateau})")

        # ── Report Test 4 ──────────────────────────────────────
        if expansion_all:
            print(f"\n  --- TEST 4: VIG Expansion (n={n}) ---")
            print(f"  {'|S|':>4} {'expansion':>10} {'≥2?':>5}")
            print(f"  {'─'*25}")
            for s in sorted(expansion_all.keys()):
                if s > n // 3:
                    continue
                avg_exp = np.mean(expansion_all[s])
                check = "✓" if avg_exp >= 2.0 else "·"
                print(f"  {s:>4} {avg_exp:>10.3f} {check:>5}")

        elapsed = time.time() - t0
        print(f"\n  n={n} completed in {elapsed:.1f}s")

        all_results[n] = {
            't1': dict(t1_all),
            'bb_sizes': bb_sizes,
            'betti': betti_vals,
        }

    # ══════════════════════════════════════════════════════════════
    #  CROSS-SIZE ANALYSIS
    # ══════════════════════════════════════════════════════════════
    print("\n" + "=" * 72)
    print("CROSS-SIZE ANALYSIS")
    print("=" * 72)

    # Does the slope c decrease with n? (Would confirm tightening)
    print("\n--- Slope c(n) from linear fit bb = c·w ---")
    print(f"{'n':>4} {'c':>8} {'c trend':>10}")
    print("-" * 25)
    slopes = {}
    for n_val in SIZES:
        data = all_results.get(n_val, {}).get('t1', {})
        if not data:
            continue
        ws = sorted(data.keys())
        if len(ws) < 3:
            continue
        x = np.array(ws, dtype=float)
        y = np.array([np.mean([d[0] for d in data[w]]) for w in ws])
        c = np.sum(x * y) / np.sum(x * x)
        slopes[n_val] = c
        print(f"{n_val:>4} {c:>8.4f}")

    if len(slopes) >= 2:
        ns = sorted(slopes.keys())
        cs = [slopes[n_val] for n_val in ns]
        trend = "DECREASING ✓" if cs[-1] < cs[0] else "FLAT/INCREASING"
        print(f"\nTrend: {trend}")
        if cs[-1] < cs[0]:
            print(f"c drops from {cs[0]:.4f} (n={ns[0]}) to {cs[-1]:.4f} (n={ns[-1]})")
            print(f"Consistent with c → 0 as n → ∞ (parallel checking tightens)")

    # ══════════════════════════════════════════════════════════════
    #  SCORECARD
    # ══════════════════════════════════════════════════════════════
    print("\n" + "=" * 72)
    print("SCORECARD: TOY 321")
    print("=" * 72)

    items = [
        ("T1: bb_bits(w) < w for all w < n",
         "Width-w window determines fewer than w backbone bits"),
        ("T1: bb_bits ≈ c·w (linear)",
         "Backbone access scales linearly with width"),
        ("T2: union(k windows) plateaus",
         "Sequential windows see SAME backbone bits, not new ones"),
        ("T3: random walk cumulative plateaus",
         "Sliding window doesn't accumulate across VIG"),
        ("T4: VIG expansion ≥ 2 for small sets",
         "Random 3-SAT Tanner graph has good expansion"),
        ("T1×: slope c decreases with n",
         "Parallel checking tightens as problem grows"),
        ("β₁ = Θ(n) confirmed",
         "Topological delocalization validated"),
        ("bb/n stable or growing",
         "Backbone density consistent with phase transition"),
    ]

    print()
    for item, desc in items:
        print(f"  [ ] {item}")
        print(f"       {desc}")
    print()
    print("PREDICTION: All 8 items pass → LDPC bedrock confirmed.")
    print("PREDICTION: T2 plateau is the SMOKING GUN for parallel constraint checking.")
    print("PREDICTION: If T2 shows linear growth instead → bedrock has a crack.")


if __name__ == "__main__":
    main()
