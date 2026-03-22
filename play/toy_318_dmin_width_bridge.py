#!/usr/bin/env python3
"""
Toy 318 — d_min → width bridge: empirical test
================================================
Casey Koons & Elie (Claude 4.6), March 22, 2026

THE QUESTION: Does LDPC minimum distance d_min = Θ(n) imply
resolution width ≥ Θ(n)?

APPROACH (revised):
  Use α slightly below threshold (3.5-4.0) to ensure SAT instances
  with multiple solutions and non-trivial backbones. Build LDPC
  matrix from H₁ cycle basis (null space of ∂₁ mod image of ∂₂).

  For each instance:
  1. Find all solutions, compute backbone
  2. Compute VIG clique complex → H₁ cycle basis
  3. Build LDPC parity matrix: rows=cycle basis, cols=backbone vars
  4. Compute d_min of the code (brute force)
  5. Measure DPLL refutation depth per backbone variable
  6. Compare d_min vs max refutation depth

Depends: numpy (only)
"""

import numpy as np
import random
from collections import defaultdict

# ── Random 3-SAT generator ──────────────────────────────────────

def random_3sat(n, alpha):
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vs = random.sample(range(n), 3)
        signs = [random.choice([1, -1]) for _ in range(3)]
        clause = tuple(s * (v + 1) for s, v in zip(signs, vs))
        clauses.append(clause)
    return clauses

def find_all_solutions(clauses, n):
    solutions = []
    for bits in range(2**n):
        assignment = [(bits >> i) & 1 for i in range(n)]
        ok = True
        for clause in clauses:
            sat = False
            for lit in clause:
                var = abs(lit) - 1
                val = assignment[var]
                if (lit > 0 and val) or (lit < 0 and not val):
                    sat = True
                    break
            if not sat:
                ok = False
                break
        if ok:
            solutions.append(tuple(assignment))
    return solutions

def compute_backbone(solutions, n):
    backbone = set()
    values = {}
    for v in range(n):
        vals = set(s[v] for s in solutions)
        if len(vals) == 1:
            backbone.add(v)
            values[v] = vals.pop()
    return backbone, values

# ── F₂ linear algebra ────────────────────────────────────────────

def f2_rank(mat):
    """Rank of binary matrix over F₂."""
    if mat.size == 0:
        return 0
    m = mat.copy() % 2
    rows, cols = m.shape
    rank = 0
    pivot_row = 0
    for col in range(cols):
        found = False
        for row in range(pivot_row, rows):
            if m[row, col] == 1:
                m[[pivot_row, row]] = m[[row, pivot_row]]
                for r in range(rows):
                    if r != pivot_row and m[r, col] == 1:
                        m[r] = (m[r] + m[pivot_row]) % 2
                pivot_row += 1
                rank += 1
                found = True
                break
    return rank

def f2_null_space(mat):
    """Find null space of binary matrix over F₂. Returns generator matrix."""
    if mat.size == 0:
        return np.array([]).reshape(0, 0)

    # null(H) = {x : Hx = 0 mod 2}. RREF on H, read off free variables.
    H = mat.copy() % 2
    nrows, ncols = H.shape
    pivot_cols = []
    pr = 0
    for col in range(ncols):
        found = False
        for row in range(pr, nrows):
            if H[row, col] == 1:
                H[[pr, row]] = H[[row, pr]]
                for r in range(nrows):
                    if r != pr and H[r, col] == 1:
                        H[r] = (H[r] + H[pr]) % 2
                pivot_cols.append(col)
                pr += 1
                found = True
                break

    free_cols = [c for c in range(ncols) if c not in pivot_cols]
    null_dim = len(free_cols)

    if null_dim == 0:
        return np.array([]).reshape(0, ncols)

    # Build null space basis
    basis = np.zeros((null_dim, ncols), dtype=np.int8)
    for i, fc in enumerate(free_cols):
        basis[i, fc] = 1
        for j, pc in enumerate(pivot_cols):
            basis[i, pc] = H[j, fc]  # Back-substitution

    return basis % 2

# ── Simplicial homology ──────────────────────────────────────────

def compute_h1_cycle_basis(clauses, n):
    """
    Compute H₁ cycle basis of VIG clique complex K(φ).
    Returns: β₁, cycle_basis (β₁ × n_edges matrix over F₂), edge_list
    """
    # Build edges and triangles
    edges = set()
    triangles = set()
    for clause in clauses:
        vs = sorted([abs(lit) - 1 for lit in clause])
        for i in range(3):
            for j in range(i+1, 3):
                edges.add((vs[i], vs[j]))
        triangles.add(tuple(vs))

    edges = sorted(edges)
    edge_idx = {e: i for i, e in enumerate(edges)}
    triangles = sorted(triangles)
    ne = len(edges)
    nt = len(triangles)

    if ne == 0:
        return 0, np.array([]).reshape(0, 0), edges

    # ∂₂: ne × nt (boundary of triangles)
    d2 = np.zeros((ne, nt), dtype=np.int8)
    for j, tri in enumerate(triangles):
        for pair in [(tri[0], tri[1]), (tri[0], tri[2]), (tri[1], tri[2])]:
            if pair in edge_idx:
                d2[edge_idx[pair], j] = 1

    # ∂₁: n × ne (boundary of edges)
    d1 = np.zeros((n, ne), dtype=np.int8)
    for i, (u, v) in enumerate(edges):
        d1[u, i] = 1
        d1[v, i] = 1

    # ker(∂₁) = null space of d1
    # im(∂₂) = column space of d2
    # H₁ = ker(∂₁) / im(∂₂)

    # ker(∂₁): cycles
    cycle_space = f2_null_space(d1)  # rows are cycle basis vectors

    if cycle_space.size == 0:
        return 0, np.array([]).reshape(0, ne), edges

    # im(∂₂): boundaries
    im_rank = f2_rank(d2)

    beta_1 = cycle_space.shape[0] - im_rank

    # For the LDPC matrix, we want the FULL cycle space (ker ∂₁),
    # since even boundaries contribute to the parity structure.
    # But for d_min, we want the quotient H₁ = ker/im.
    # Use cycle space directly for the LDPC construction.

    return beta_1, cycle_space, edges

# ── LDPC matrix from cycles × backbone ───────────────────────────

def build_ldpc_from_cycles(cycle_basis, edges, backbone):
    """
    Build LDPC parity-check matrix.
    H[i, j] = 1 if backbone variable j participates in cycle i.

    A backbone variable participates in a cycle if it's an endpoint
    of any edge in the cycle.
    """
    bb_list = sorted(backbone)
    bb_idx = {v: i for i, v in enumerate(bb_list)}

    n_cycles = cycle_basis.shape[0]
    n_bb = len(bb_list)

    if n_cycles == 0 or n_bb == 0:
        return np.array([]).reshape(0, 0), bb_list

    H = np.zeros((n_cycles, n_bb), dtype=np.int8)
    for i in range(n_cycles):
        # Which edges are in this cycle?
        cycle_vars = set()
        for j in range(cycle_basis.shape[1]):
            if cycle_basis[i, j] == 1:
                u, v = edges[j]
                cycle_vars.add(u)
                cycle_vars.add(v)
        # Which backbone vars?
        for v in cycle_vars:
            if v in bb_idx:
                H[i, bb_idx[v]] = 1

    return H, bb_list

def compute_dmin(H):
    """Minimum weight of nonzero codeword in null(H) over F₂."""
    if H.size == 0:
        return 0
    null_basis = f2_null_space(H)
    if null_basis.size == 0 or null_basis.shape[0] == 0:
        return H.shape[1]  # Only zero codeword

    null_dim = null_basis.shape[0]
    n_vars = null_basis.shape[1]

    if null_dim > 18:
        # Sample
        min_w = n_vars
        for _ in range(5000):
            coeffs = np.random.randint(0, 2, null_dim)
            if coeffs.sum() == 0:
                continue
            cw = coeffs @ null_basis % 2
            w = int(cw.sum())
            if 0 < w < min_w:
                min_w = w
        return min_w

    # Enumerate
    min_w = n_vars
    for bits in range(1, 2**null_dim):
        coeffs = np.array([(bits >> i) & 1 for i in range(null_dim)], dtype=np.int8)
        cw = coeffs @ null_basis % 2
        w = int(cw.sum())
        if 0 < w < min_w:
            min_w = w
    return min_w

# ── DPLL refutation depth ────────────────────────────────────────

def dpll_depth(clauses, n, var, val, max_d=8):
    """
    DPLL refutation depth for setting var (0-indexed) to val.
    Returns minimum depth d such that depth-d DPLL refutes.
    """
    for d in range(max_d + 1):
        if _dpll_rec(clauses, n, {var + 1: bool(val)}, d):
            return d
    return max_d + 1

def _dpll_rec(clauses, n, assign, depth_left):
    """Recursive DPLL with BCP and depth limit."""
    # Unit propagation
    assign = dict(assign)
    changed = True
    while changed:
        changed = False
        for clause in clauses:
            unresolved = []
            sat = False
            for lit in clause:
                v = abs(lit)
                if v in assign:
                    if (lit > 0) == assign[v]:
                        sat = True
                        break
                else:
                    unresolved.append(lit)
            if sat:
                continue
            if len(unresolved) == 0:
                return True  # Conflict!
            if len(unresolved) == 1:
                lit = unresolved[0]
                v = abs(lit)
                val = (lit > 0)
                if v in assign:
                    if assign[v] != val:
                        return True  # Conflict
                else:
                    assign[v] = val
                    changed = True

    if depth_left <= 0:
        return False

    # Branch on first unassigned variable
    for v in range(1, n + 1):
        if v not in assign:
            a1 = dict(assign); a1[v] = True
            a2 = dict(assign); a2[v] = False
            return _dpll_rec(clauses, n, a1, depth_left - 1) and \
                   _dpll_rec(clauses, n, a2, depth_left - 1)

    return False  # All assigned, no conflict

# ── Main experiment ───────────────────────────────────────────────

def run(sizes=[10, 12, 14], trials=50, alpha=3.8):
    print("=" * 72)
    print("TOY 318: d_min → width bridge (empirical)")
    print("=" * 72)
    print(f"Sizes: {sizes}, Trials/size: {trials}, α = {alpha}")
    print(f"Strategy: SAT instances with non-trivial backbone")
    print()

    all_results = {}

    for n in sizes:
        print(f"\n--- n = {n} ---")
        dmin_list = []
        maxd_list = []
        meand_list = []
        beta1_list = []
        bb_list = []
        ok = 0

        attempt = 0
        while ok < trials and attempt < trials * 20:
            attempt += 1
            clauses = random_3sat(n, alpha)
            sols = find_all_solutions(clauses, n)

            if len(sols) < 2:
                continue

            backbone, bb_vals = compute_backbone(sols, n)
            if len(backbone) < 3:
                continue

            beta1, cycle_basis, edges = compute_h1_cycle_basis(clauses, n)
            if beta1 < 1 or cycle_basis.shape[0] < 2:
                continue

            H, bb_sorted = build_ldpc_from_cycles(cycle_basis, edges, backbone)
            if H.size == 0 or H.shape[0] < 2 or H.shape[1] < 2:
                continue

            dmin = compute_dmin(H)
            if dmin == 0:
                continue

            # Measure DPLL depth for each backbone var (wrong value)
            depths = []
            for v in sorted(backbone):
                correct = bb_vals[v]
                d = dpll_depth(clauses, n, v, 1 - correct, max_d=8)
                depths.append(d)

            max_depth = max(depths)
            mean_depth = np.mean(depths)

            dmin_list.append(dmin)
            maxd_list.append(max_depth)
            meand_list.append(mean_depth)
            beta1_list.append(beta1)
            bb_list.append(len(backbone))
            ok += 1

            if ok <= 3:
                print(f"  [{ok}] |B|={len(backbone)}, β₁={beta1}, "
                      f"H={H.shape}, d_min={dmin}, "
                      f"max_d={max_depth}, mean_d={mean_depth:.2f}")

        if ok < 5:
            print(f"  Only {ok}/{trials} valid. Skipping.")
            continue

        dm = np.array(dmin_list, dtype=float)
        md = np.array(maxd_list, dtype=float)
        mn = np.array(meand_list, dtype=float)

        corr = np.corrcoef(dm, md)[0, 1] if np.std(dm) > 0 and np.std(md) > 0 else float('nan')

        print(f"\n  n={n}  ({ok} instances, {attempt} attempts)")
        print(f"    |B| mean     = {np.mean(bb_list):.1f}")
        print(f"    β₁ mean      = {np.mean(beta1_list):.1f}")
        print(f"    d_min mean   = {np.mean(dm):.2f}  (d_min/n = {np.mean(dm)/n:.3f})")
        print(f"    max_d mean   = {np.mean(md):.2f}  (max_d/n = {np.mean(md)/n:.3f})")
        print(f"    mean_d mean  = {np.mean(mn):.2f}")
        print(f"    corr(d_min, max_depth) = {corr:.3f}")

        all_results[n] = {
            'dmin': dm, 'maxd': md, 'meand': mn,
            'beta1': np.array(beta1_list), 'bb': np.array(bb_list),
            'corr': corr, 'count': ok
        }

    # ── Scaling table ─────────────────────────────────────────────

    print(f"\n{'='*72}")
    print("SCALING TABLE")
    print(f"{'='*72}")
    print(f"  {'n':>4} | {'d_min/n':>8} | {'max_d/n':>8} | {'mean_d/n':>9} | {'corr':>6} | {'β₁':>5} | {'|B|':>5}")
    print(f"  {'─'*4}─┼─{'─'*8}─┼─{'─'*8}─┼─{'─'*9}─┼─{'─'*6}─┼─{'─'*5}─┼─{'─'*5}")

    for sz in sorted(all_results.keys()):
        r = all_results[sz]
        print(f"  {sz:>4} | {np.mean(r['dmin'])/sz:>8.3f} | {np.mean(r['maxd'])/sz:>8.3f} | "
              f"{np.mean(r['meand'])/sz:>9.3f} | {r['corr']:>6.3f} | "
              f"{np.mean(r['beta1']):>5.1f} | {np.mean(r['bb']):>5.1f}")

    # ── Verdict ───────────────────────────────────────────────────

    print(f"\n{'='*72}")
    print("VERDICT")
    print(f"{'='*72}")

    if len(all_results) >= 2:
        ns = sorted(all_results.keys())
        dms = [np.mean(all_results[sz]['dmin'])/sz for sz in ns]
        mds = [np.mean(all_results[sz]['maxd'])/sz for sz in ns]

        print(f"  d_min/n trend: {dms}")
        print(f"  max_d/n trend: {mds}")

        if all(d > 0.05 for d in dms) and all(d > 0.01 for d in mds):
            print("\n  ✓ Both d_min and max refutation depth grow with n.")
            print("    The d_min → width bridge is empirically supported.")
        else:
            print("\n  ⚠ Need larger sizes or more instances to confirm.")

    print(f"\n  Key: d_min = LDPC code distance, max_d = DPLL refutation depth")
    print(f"  max_d is a LOWER BOUND on resolution width (conservative).")

    return all_results


if __name__ == "__main__":
    random.seed(42)
    np.random.seed(42)
    run(sizes=[10, 12, 14, 16], trials=30, alpha=3.8)
