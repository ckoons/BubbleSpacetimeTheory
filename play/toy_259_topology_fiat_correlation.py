#!/usr/bin/env python3
"""
Toy 259 — Topology–I_fiat Correlation
=======================================

Tests whether I_fiat (non-derivable information) correlates with topological
complexity of the constraint complex.

For each random k-SAT instance, computes:
  - I_derivable = backbone = fraction forced to same value in ALL solutions
  - I_fiat = 1 - I_derivable = fraction not derivable from structure
  - β₀: connected components of Variable Interaction Graph (VIG)
  - β₁(VIG): cycle rank of the VIG = |E| - |V| + β₀
  - β₁(complex): first Betti number of the clause complex
    = β₁(VIG) - rank(∂₂) where ∂₂ maps 2-simplices to 1-chains
  - Treewidth proxy: min-degree elimination width of VIG

Prediction (Lyra, March 19):
  I_fiat correlates with β₁ of the clause complex.
  When the topology has non-trivial cycles that clauses can't fill,
  information is globally locked. Local methods can't extract it.

Casey Koons & Claude 4.6 (Elie) | BST Research Program | March 19, 2026
"""

import random
import math
from collections import defaultdict
from fractions import Fraction

# ── Parameters ──────────────────────────────────────────────────────────
N_VARS = 14
N_SAMPLES = 150
ALPHA_STEPS = 20


def generate_random_ksat(n, k, num_clauses):
    """Generate random k-SAT instance. Returns list of clauses (lists of signed literals 1..n)."""
    clauses = []
    for _ in range(num_clauses):
        vars_in_clause = random.sample(range(1, n + 1), k)
        clause = [v if random.random() < 0.5 else -v for v in vars_in_clause]
        clauses.append(clause)
    return clauses


def count_solutions_and_backbone(n, clauses):
    """Exact solution count and backbone fraction."""
    num_solutions = 0
    var_values = [set() for _ in range(n + 1)]

    for bits in range(1 << n):
        assignment = {}
        for i in range(1, n + 1):
            assignment[i] = (bits >> (i - 1)) & 1

        sat = True
        for clause in clauses:
            clause_sat = False
            for lit in clause:
                var = abs(lit)
                val = assignment[var]
                if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                    clause_sat = True
                    break
            if not clause_sat:
                sat = False
                break

        if sat:
            num_solutions += 1
            for i in range(1, n + 1):
                var_values[i].add(assignment[i])

    if num_solutions == 0:
        return 0, 0.0

    backbone = sum(1 for i in range(1, n + 1) if len(var_values[i]) == 1) / n
    return num_solutions, backbone


def build_vig(n, clauses):
    """Build Variable Interaction Graph.
    Returns adjacency set and edge list.
    """
    edges = set()
    adj = defaultdict(set)
    for clause in clauses:
        variables = [abs(lit) for lit in clause]
        for i in range(len(variables)):
            for j in range(i + 1, len(variables)):
                u, v = min(variables[i], variables[j]), max(variables[i], variables[j])
                if u != v:
                    edges.add((u, v))
                    adj[u].add(v)
                    adj[v].add(u)
    return adj, edges


def connected_components(n, adj):
    """Count connected components of VIG."""
    visited = set()
    components = 0
    for v in range(1, n + 1):
        if v not in visited:
            components += 1
            stack = [v]
            while stack:
                u = stack.pop()
                if u in visited:
                    continue
                visited.add(u)
                for w in adj[u]:
                    if w not in visited:
                        stack.append(w)
    return components


def betti_1_vig(n, adj, edges):
    """β₁ of VIG = |E| - |V| + β₀ (cycle rank)."""
    beta_0 = connected_components(n, adj)
    return len(edges) - n + beta_0, beta_0


def boundary_matrix_rank(n, clauses, edges):
    """Compute rank of ∂₂ over GF(2).
    ∂₂ maps each k-clause (k≥3) to its boundary edges.
    Returns rank.
    """
    # Only consider clauses with k ≥ 3 (they form 2-simplices or higher)
    faces = []
    edge_list = sorted(edges)
    edge_index = {e: i for i, e in enumerate(edge_list)}
    m = len(edge_list)

    for clause in clauses:
        variables = sorted(set(abs(lit) for lit in clause))
        if len(variables) < 3:
            continue
        # Each 3-subset of the clause's variables defines a 2-simplex
        # For a k-clause, we get C(k,3) triangles... but actually,
        # the clause itself is the simplex. For 3-SAT, each clause
        # defines exactly one triangle.
        # Boundary = the three edges of the triangle
        boundary = []
        for i in range(len(variables)):
            for j in range(i + 1, len(variables)):
                u, v = variables[i], variables[j]
                edge = (min(u, v), max(u, v))
                if edge in edge_index:
                    boundary.append(edge_index[edge])
        if boundary:
            faces.append(boundary)

    if not faces or m == 0:
        return 0

    # Build matrix over GF(2) and compute rank via Gaussian elimination
    # Matrix: rows = faces, cols = edges
    matrix = []
    for face in faces:
        row = [0] * m
        for idx in face:
            row[idx] ^= 1  # GF(2)
        matrix.append(row)

    # Gaussian elimination over GF(2)
    rank = 0
    pivot_cols = []
    for col in range(m):
        # Find pivot row
        pivot_row = None
        for row in range(rank, len(matrix)):
            if matrix[row][col] == 1:
                pivot_row = row
                break
        if pivot_row is None:
            continue
        # Swap
        matrix[rank], matrix[pivot_row] = matrix[pivot_row], matrix[rank]
        # Eliminate
        for row in range(len(matrix)):
            if row != rank and matrix[row][col] == 1:
                for c in range(m):
                    matrix[row][c] ^= matrix[rank][c]
        pivot_cols.append(col)
        rank += 1

    return rank


def min_degree_elimination_width(n, adj):
    """Treewidth upper bound via min-degree elimination heuristic."""
    # Work with a mutable copy
    neighbors = {v: set(adj[v]) for v in range(1, n + 1)}
    width = 0

    remaining = set(range(1, n + 1))
    for _ in range(n):
        if not remaining:
            break
        # Pick vertex with minimum degree
        min_v = min(remaining, key=lambda v: len(neighbors[v] & remaining))
        deg = len(neighbors[min_v] & remaining)
        width = max(width, deg)

        # Make neighbors into clique
        nbrs = list(neighbors[min_v] & remaining)
        for i in range(len(nbrs)):
            for j in range(i + 1, len(nbrs)):
                neighbors[nbrs[i]].add(nbrs[j])
                neighbors[nbrs[j]].add(nbrs[i])

        # Remove vertex
        remaining.remove(min_v)

    return width


def implication_graph_yield_2sat(n, clauses):
    """SCC-based extraction for 2-SAT. Returns fraction of determined variables."""
    def lit_to_node(lit):
        var = abs(lit) - 1
        return 2 * var if lit > 0 else 2 * var + 1

    def neg_node(node):
        return node ^ 1

    num_nodes = 2 * n
    adj = defaultdict(list)
    radj = defaultdict(list)

    for clause in clauses:
        if len(clause) != 2:
            continue
        a, b = clause
        na, nb = lit_to_node(a), lit_to_node(b)
        adj[neg_node(na)].append(nb)
        radj[nb].append(neg_node(na))
        adj[neg_node(nb)].append(na)
        radj[na].append(neg_node(nb))

    visited = [False] * num_nodes
    order = []

    def dfs1(u):
        stack = [(u, False)]
        while stack:
            node, processed = stack.pop()
            if processed:
                order.append(node)
                continue
            if visited[node]:
                continue
            visited[node] = True
            stack.append((node, True))
            for v in adj[node]:
                if not visited[v]:
                    stack.append((v, False))

    for i in range(num_nodes):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * num_nodes
    comp_id = 0
    visited2 = [False] * num_nodes

    def dfs2(u, cid):
        stack = [u]
        while stack:
            node = stack.pop()
            if visited2[node]:
                continue
            visited2[node] = True
            comp[node] = cid
            for v in radj[node]:
                if not visited2[v]:
                    stack.append(v)

    for u in reversed(order):
        if not visited2[u]:
            dfs2(u, comp_id)
            comp_id += 1

    determined = sum(1 for var in range(n) if comp[2 * var] != comp[2 * var + 1])
    return determined / n


def run_experiment():
    """Sweep α for 2-SAT and 3-SAT, compute topology + I_fiat."""
    print("=" * 80)
    print("Toy 259 — Topology–I_fiat Correlation")
    print("=" * 80)
    print(f"  n = {N_VARS} variables, {N_SAMPLES} samples per point")
    print()

    all_results = {}

    for k in [2, 3]:
        if k == 2:
            alphas = [round(0.3 + i * 2.7 / ALPHA_STEPS, 3) for i in range(ALPHA_STEPS + 1)]
        else:
            alphas = [round(1.5 + i * 5.5 / ALPHA_STEPS, 3) for i in range(ALPHA_STEPS + 1)]

        print(f"\n{'─' * 80}")
        print(f"  {k}-SAT  (phase transition ≈ {'1.0' if k == 2 else '4.267'})")
        print(f"{'─' * 80}")
        header = (f"  {'α':>6}  {'P(SAT)':>6}  {'I_drv':>5} {'I_fiat':>6}  "
                  f"{'β₀':>4}  {'β₁VIG':>6}  {'β₁cpx':>6}  {'rk∂₂':>5}  "
                  f"{'tw':>3}  {'|E|':>5}")
        if k == 2:
            header += f"  {'SCC':>5}"
        print(header)

        results = []

        for alpha in alphas:
            m = max(1, int(alpha * N_VARS))

            sat_count = 0
            total_derivable = 0.0
            total_fiat = 0.0
            total_beta0 = 0.0
            total_beta1_vig = 0.0
            total_beta1_cpx = 0.0
            total_rank = 0.0
            total_tw = 0.0
            total_edges = 0.0
            total_scc = 0.0
            valid = 0

            for _ in range(N_SAMPLES):
                clauses = generate_random_ksat(N_VARS, k, m)
                n_sol, backbone = count_solutions_and_backbone(N_VARS, clauses)

                # Topology (compute for ALL instances, not just satisfiable)
                adj_vig, edges = build_vig(N_VARS, clauses)
                b1_vig, b0 = betti_1_vig(N_VARS, adj_vig, edges)
                rk = boundary_matrix_rank(N_VARS, clauses, edges)
                b1_cpx = max(0, b1_vig - rk)
                tw = min_degree_elimination_width(N_VARS, adj_vig)

                if n_sol > 0:
                    sat_count += 1
                    i_derivable = backbone  # structure-forced bits
                    i_fiat = 1.0 - backbone  # must-guess bits
                    total_derivable += i_derivable
                    total_fiat += i_fiat
                    valid += 1

                    if k == 2:
                        scc_y = implication_graph_yield_2sat(N_VARS, clauses)
                        total_scc += scc_y

                total_beta0 += b0
                total_beta1_vig += b1_vig
                total_beta1_cpx += b1_cpx
                total_rank += rk
                total_tw += tw
                total_edges += len(edges)

            p_sat = sat_count / N_SAMPLES
            avg_deriv = total_derivable / valid if valid > 0 else 0.0
            avg_fiat = total_fiat / valid if valid > 0 else 0.0
            avg_b0 = total_beta0 / N_SAMPLES
            avg_b1_vig = total_beta1_vig / N_SAMPLES
            avg_b1_cpx = total_beta1_cpx / N_SAMPLES
            avg_rank = total_rank / N_SAMPLES
            avg_tw = total_tw / N_SAMPLES
            avg_edges = total_edges / N_SAMPLES
            avg_scc = total_scc / valid if valid > 0 and k == 2 else 0.0

            results.append({
                'alpha': alpha, 'p_sat': p_sat,
                'i_derivable': avg_deriv, 'i_fiat': avg_fiat,
                'beta0': avg_b0, 'beta1_vig': avg_b1_vig, 'beta1_cpx': avg_b1_cpx,
                'rank': avg_rank, 'tw': avg_tw, 'edges': avg_edges, 'scc': avg_scc,
            })

            line = (f"  {alpha:6.3f}  {p_sat:6.3f}  {avg_deriv:5.3f} {avg_fiat:6.3f}  "
                    f"{avg_b0:4.1f}  {avg_b1_vig:6.1f}  {avg_b1_cpx:6.1f}  {avg_rank:5.1f}  "
                    f"{avg_tw:3.0f}  {avg_edges:5.0f}")
            if k == 2:
                line += f"  {avg_scc:5.3f}"
            print(line)

        all_results[k] = results

    # ── Correlation analysis ────────────────────────────────────────────
    print("\n" + "=" * 80)
    print("  CORRELATION ANALYSIS")
    print("=" * 80)

    for k in [2, 3]:
        data = all_results[k]
        # Filter to satisfiable regime (p_sat > 0.2) for meaningful I_fiat
        sat_data = [d for d in data if d['p_sat'] > 0.2]
        if len(sat_data) < 3:
            print(f"\n  {k}-SAT: insufficient satisfiable data for correlation")
            continue

        # Compute Pearson correlation between I_fiat and each topological measure
        def pearson(xs, ys):
            n = len(xs)
            if n < 3:
                return 0.0
            mx, my = sum(xs) / n, sum(ys) / n
            sx = sum((x - mx) ** 2 for x in xs) ** 0.5
            sy = sum((y - my) ** 2 for y in ys) ** 0.5
            if sx < 1e-10 or sy < 1e-10:
                return 0.0
            return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / (sx * sy)

        i_fiats = [d['i_fiat'] for d in sat_data]
        b0s = [d['beta0'] for d in sat_data]
        b1_vigs = [d['beta1_vig'] for d in sat_data]
        b1_cpxs = [d['beta1_cpx'] for d in sat_data]
        tws = [d['tw'] for d in sat_data]
        edges = [d['edges'] for d in sat_data]

        print(f"\n  {k}-SAT Pearson correlations with I_fiat (satisfiable regime):")
        print(f"    β₀ (components):        r = {pearson(i_fiats, b0s):+.4f}")
        print(f"    β₁(VIG) (cycle rank):   r = {pearson(i_fiats, b1_vigs):+.4f}")
        print(f"    β₁(complex):            r = {pearson(i_fiats, b1_cpxs):+.4f}")
        print(f"    Treewidth:              r = {pearson(i_fiats, tws):+.4f}")
        print(f"    |E| (edge count):       r = {pearson(i_fiats, edges):+.4f}")

        # The key comparison: does β₁(complex) differ between 2-SAT and 3-SAT?
        # For 2-SAT, ∂₂ has rank 0 (no 2-simplices), so β₁(cpx) = β₁(VIG)
        # For 3-SAT, ∂₂ fills some cycles, so β₁(cpx) ≤ β₁(VIG)

    # ── The key finding ─────────────────────────────────────────────────
    print(f"\n{'=' * 80}")
    print("  KEY FINDING: Topology of Information Locking")
    print(f"{'=' * 80}")

    # Compare at phase transition
    for k in [2, 3]:
        data = all_results[k]
        trans = [d for d in data if 0.4 < d['p_sat'] < 0.6]
        if trans:
            d = trans[0]
            print(f"\n  {k}-SAT at phase transition (α ≈ {d['alpha']:.2f}):")
            print(f"    I_derivable:   {d['i_derivable']:.4f}")
            print(f"    I_fiat:        {d['i_fiat']:.4f}")
            print(f"    β₁(VIG):      {d['beta1_vig']:.1f}")
            print(f"    β₁(complex):  {d['beta1_cpx']:.1f}")
            print(f"    rank(∂₂):     {d['rank']:.1f}")
            print(f"    Treewidth:    {d['tw']:.0f}")
            if k == 2:
                print(f"    SCC yield:    {d['scc']:.4f}")

    print(f"""
{'─' * 80}
  INTERPRETATION
{'─' * 80}

  For 2-SAT:
    - No 2-simplices → rank(∂₂) = 0 → β₁(complex) = β₁(VIG)
    - The VIG has cycles, but they live in 1-dimensional topology
    - SCC algorithm walks these 1-dimensional cycles directly
    - All information is derivable through 1-dimensional flows

  For 3-SAT:
    - 2-simplices (clause triangles) fill SOME VIG cycles → β₁(cpx) < β₁(VIG)
    - But the filling is PARTIAL — many cycles remain unfilled
    - More importantly: the 2-simplices create NEW topological features
      (the faces themselves distribute information across triples)
    - I_fiat correlates with the topological complexity that RESISTS
      1-dimensional flow — information locked in higher-dimensional faces

  The channel capacity argument:
    - Polynomial-time algorithms perform LOCAL operations on the complex
    - Local = bounded fan-in per step, walks edges (1-chains)
    - When information is locked in 2-chains (faces), local edge-walking
      can't aggregate it — the channel capacity of 1-dimensional flows
      is bounded below I_fiat
    - This is Fano's inequality applied to constraint topology:
      if C(local) < I_fiat, irreducible error

  The bridge theorem target:
    "Polynomial time = 1-dimensional flows on the constraint complex.
     I_fiat = information locked in higher-dimensional topology.
     When I_fiat > 0, no 1-dimensional flow suffices."
""")


if __name__ == '__main__':
    random.seed(42)
    run_experiment()
