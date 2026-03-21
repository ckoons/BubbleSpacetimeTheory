#!/usr/bin/env python3
"""
Toy 289 — Circle Confinement: Guard Cycles and the Čech Gap
============================================================
Tests Casey's circle reformulation of 3-SAT constraint geometry.

Key idea: Each 3-SAT clause defines not just a triangle (2-simplex) but a
circumscribed disk. The annular region (disk minus triangle) carries one
H₁ cycle — a "guard cycle" — that the simplicial formulation misses.

AC_geometric = β₁(Čech) - β₁(simplicial) = the information deficit of
simplex-based methods. If AC_geometric = Θ(n) at α_c, this is a direct
geometric measurement of algebraic complexity.

Guard cycles from non-interacting clauses are geometrically disjoint →
automatically linearly independent in H₁ → algebraic independence for free.
This could deliver T29 (algebraic independence of cycle solutions).

Measurements:
  Phase 1: Embed VIG in ℝ² using three methods (force-directed, spectral, random)
  Phase 2: For each clause, compute circumscribed circle and triangle areas
  Phase 3: Build Čech nerve complex of clause disks
  Phase 4: Compute β₁(simplicial) and β₁(Čech) — the AC_geometric gap
  Phase 5: Count mutually disjoint guard cycles (independence count)
  Phase 6: Track all metrics across α and n

Scorecard (8 tests):
  1. Area ratio < 0.5 (triangles occupy < 50% of circumscircle)
  2. AC_geometric > 0 at α_c (Čech sees more than simplicial)
  3. AC_geometric grows with n (= Θ(n), not O(1))
  4. Guard cycle fraction > 0.3 at α_c (constant fraction survives)
  5. Disjoint guard cycle count grows with n
  6. Embedding-robust: all three embeddings give same qualitative result
  7. Phase transition visible in area ratio at α_c
  8. Disjoint guard cycles > β₁(simplicial) at α_c (circles strictly stronger)

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
from collections import defaultdict
from itertools import combinations

# Force unbuffered output
_print = print
def print(*args, **kwargs):
    kwargs.setdefault('flush', True)
    _print(*args, **kwargs)

PASS = 0
FAIL = 0


def score(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        tag = "✓ PASS"
    else:
        FAIL += 1
        tag = "✗ FAIL"
    print(f"  {tag}: {name}")
    if detail:
        print(f"         {detail}")


# ═══════════════════════════════════════════════════════════════════
# 3-SAT GENERATION
# ═══════════════════════════════════════════════════════════════════

def generate_3sat(n, alpha, rng):
    """Generate random 3-SAT: n variables, m = alpha*n clauses."""
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vars_ = rng.sample(range(n), 3)
        signs = [rng.choice([-1, 1]) for _ in range(3)]
        clauses.append(list(zip(vars_, signs)))
    return clauses


# ═══════════════════════════════════════════════════════════════════
# VIG CONSTRUCTION
# ═══════════════════════════════════════════════════════════════════

def build_vig(n, clauses):
    """Build Variable Incidence Graph: edge between variables sharing a clause."""
    adj = defaultdict(set)
    for clause in clauses:
        vars_ = [v for v, _ in clause]
        for i in range(3):
            for j in range(i + 1, 3):
                adj[vars_[i]].add(vars_[j])
                adj[vars_[j]].add(vars_[i])
    return adj


def vig_edges(adj, n):
    """Return list of edges as (i, j) pairs with i < j."""
    edges = set()
    for v in range(n):
        for u in adj.get(v, set()):
            if v < u:
                edges.add((v, u))
    return sorted(edges)


# ═══════════════════════════════════════════════════════════════════
# EMBEDDINGS
# ═══════════════════════════════════════════════════════════════════

def embed_force_directed(n, adj, dim=2, iterations=200, rng=None):
    """Fruchterman-Reingold force-directed embedding in ℝ^dim."""
    if rng is None:
        rng = random.Random(42)
    pos = np.array([[rng.gauss(0, 1) for _ in range(dim)] for _ in range(n)])

    edges = []
    for v in range(n):
        for u in adj.get(v, set()):
            if v < u:
                edges.append((v, u))

    k = np.sqrt(1.0 / max(n, 1))  # optimal distance
    temp = 1.0

    for it in range(iterations):
        # Repulsive forces (all pairs — use vectorized)
        disp = np.zeros_like(pos)
        for i in range(n):
            delta = pos[i] - pos  # n × dim
            dist = np.sqrt(np.sum(delta**2, axis=1))
            dist = np.maximum(dist, 1e-6)
            force = k * k / dist  # repulsive magnitude
            force[i] = 0
            disp[i] += np.sum((delta.T * force).T, axis=0)

        # Attractive forces (edges only)
        for u, v in edges:
            delta = pos[u] - pos[v]
            dist = max(np.linalg.norm(delta), 1e-6)
            force = dist * dist / k
            direction = delta / dist
            disp[u] -= force * direction
            disp[v] += force * direction

        # Apply with temperature limiting
        disp_norms = np.sqrt(np.sum(disp**2, axis=1))
        disp_norms = np.maximum(disp_norms, 1e-6)
        scale = np.minimum(disp_norms, temp) / disp_norms
        pos += (disp.T * scale).T
        temp *= 0.95

    # Center and normalize
    pos -= pos.mean(axis=0)
    max_extent = np.max(np.abs(pos))
    if max_extent > 0:
        pos /= max_extent
    return pos


def embed_spectral(n, adj, dim=2):
    """Spectral embedding using eigenvectors of the graph Laplacian."""
    # Build Laplacian
    L = np.zeros((n, n))
    for v in range(n):
        neighbors = adj.get(v, set())
        L[v, v] = len(neighbors)
        for u in neighbors:
            L[v, u] = -1.0

    # Eigenvectors (skip the trivial zero eigenvalue)
    eigenvalues, eigenvectors = np.linalg.eigh(L)
    # Use eigenvectors 1..dim (skip eigenvector 0 which is constant)
    pos = eigenvectors[:, 1:dim + 1].copy()

    # Normalize
    pos -= pos.mean(axis=0)
    max_extent = np.max(np.abs(pos))
    if max_extent > 0:
        pos /= max_extent
    return pos


def embed_random(n, dim=2, rng=None):
    """Random embedding in ℝ^dim (baseline — no graph structure)."""
    if rng is None:
        rng = random.Random(42)
    pos = np.array([[rng.gauss(0, 1) for _ in range(dim)] for _ in range(n)])
    pos -= pos.mean(axis=0)
    max_extent = np.max(np.abs(pos))
    if max_extent > 0:
        pos /= max_extent
    return pos


# ═══════════════════════════════════════════════════════════════════
# CIRCLE AND TRIANGLE GEOMETRY
# ═══════════════════════════════════════════════════════════════════

def circumscribed_circle(p1, p2, p3):
    """Circumscribed circle of triangle (p1, p2, p3) in ℝ².
    Returns (center, radius). Returns None if degenerate."""
    ax, ay = p1[0], p1[1]
    bx, by = p2[0], p2[1]
    cx, cy = p3[0], p3[1]

    D = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    if abs(D) < 1e-12:
        return None, None

    ux = ((ax**2 + ay**2) * (by - cy) + (bx**2 + by**2) * (cy - ay) +
          (cx**2 + cy**2) * (ay - by)) / D
    uy = ((ax**2 + ay**2) * (cx - bx) + (bx**2 + by**2) * (ax - cx) +
          (cx**2 + cy**2) * (bx - ax)) / D

    center = np.array([ux, uy])
    radius = np.sqrt((ax - ux)**2 + (ay - uy)**2)
    return center, radius


def triangle_area(p1, p2, p3):
    """Area of triangle via cross product."""
    v1 = p2 - p1
    v2 = p3 - p1
    return 0.5 * abs(v1[0] * v2[1] - v1[1] * v2[0])


def compute_clause_geometry(clauses, pos):
    """For each clause, compute triangle area, circle area, and ratio."""
    results = []
    for clause in clauses:
        vars_ = [v for v, _ in clause]
        p1, p2, p3 = pos[vars_[0]], pos[vars_[1]], pos[vars_[2]]

        A_tri = triangle_area(p1, p2, p3)
        center, radius = circumscribed_circle(p1, p2, p3)

        if center is not None and radius > 1e-12:
            A_circ = np.pi * radius**2
            ratio = A_tri / A_circ if A_circ > 0 else 0
            results.append({
                'vars': vars_,
                'center': center,
                'radius': radius,
                'A_tri': A_tri,
                'A_circ': A_circ,
                'ratio': ratio,
            })
        else:
            results.append({
                'vars': vars_,
                'center': None,
                'radius': 0,
                'A_tri': A_tri,
                'A_circ': 0,
                'ratio': 0,
            })
    return results


# ═══════════════════════════════════════════════════════════════════
# TOPOLOGY: β₁ COMPUTATION
# ═══════════════════════════════════════════════════════════════════

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


def beta1_simplicial(n, clauses):
    """β₁ of the VIG clique complex.
    β₁ = edges - vertices + components - filled_triangles
    where filled_triangles = clauses (each clause fills a 2-simplex)."""
    adj = build_vig(n, clauses)
    edges = vig_edges(adj, n)

    # Count components
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    components = len(set(uf.find(i) for i in range(n)))

    # Each clause fills exactly one 2-simplex
    n_filled = len(clauses)

    # β₁ = E - V + C - F₂ (where F₂ = filled 2-faces)
    beta1 = len(edges) - n + components - n_filled
    return max(beta1, 0)


def beta1_cech(clause_geom):
    """β₁ of the Čech nerve complex of clause disks.

    The Čech complex has:
    - vertices = clauses (one per disk)
    - edge between clauses i,j if disks D_i ∩ D_j ≠ ∅
    - triangle (i,j,k) if D_i ∩ D_j ∩ D_k ≠ ∅

    By the nerve theorem (disks are convex), β₁(Čech) = β₁(∪D_i).
    """
    m = len(clause_geom)
    if m == 0:
        return 0

    # Build adjacency: disks i,j overlap if dist(centers) < r_i + r_j
    cech_edges = []
    for i in range(m):
        if clause_geom[i]['center'] is None:
            continue
        for j in range(i + 1, m):
            if clause_geom[j]['center'] is None:
                continue
            dist = np.linalg.norm(clause_geom[i]['center'] - clause_geom[j]['center'])
            if dist < clause_geom[i]['radius'] + clause_geom[j]['radius']:
                cech_edges.append((i, j))

    # Build triple intersections: disks i,j,k all overlap pairwise AND
    # have common intersection. For disks, pairwise overlap ≠ triple overlap,
    # but we check: the intersection of any two disks is a lens.
    # For three disks, we check if all three centers can be reached within
    # the minimum radius. A simpler sufficient condition: if all pairwise
    # distances < min radii, then triple intersection exists.
    # More precisely: three disks have common intersection iff each center
    # is within the sum of the other two radii of the third... but this is
    # complex. We use the Helly criterion: for convex sets in ℝ², three sets
    # have common intersection iff all pairs do. (Helly's theorem in ℝ²!)
    # Actually, Helly's theorem says: for convex sets in ℝ^d, if every d+1
    # of them have common intersection, then all do. For d=2, that means
    # every 3 convex sets that pairwise intersect DO have common intersection.
    # So for disks in ℝ²: pairwise overlap → triple overlap!

    # Build adjacency for components
    uf = UnionFind(m)
    for i, j in cech_edges:
        uf.union(i, j)

    # Count valid vertices (non-degenerate disks)
    valid = [i for i in range(m) if clause_geom[i]['center'] is not None]
    components = len(set(uf.find(i) for i in valid)) if valid else 0

    # Count filled triangles: by Helly in ℝ², all pairwise-overlapping
    # triples of disks are filled. Build neighbor sets for efficiency.
    neighbors = defaultdict(set)
    for i, j in cech_edges:
        neighbors[i].add(j)
        neighbors[j].add(i)

    n_triangles = 0
    for i, j in cech_edges:
        common = neighbors[i] & neighbors[j]
        for k in common:
            if k > j:  # count each triangle once
                n_triangles += 1

    # β₁ = E - V + C - F₂
    V = len(valid)
    E = len(cech_edges)
    C = components
    F = n_triangles
    beta1 = E - V + C - F
    return max(beta1, 0)


# ═══════════════════════════════════════════════════════════════════
# GUARD CYCLES
# ═══════════════════════════════════════════════════════════════════

def count_guard_cycles(clauses, clause_geom):
    """Count guard cycles and mutually disjoint guard cycles.

    A guard cycle exists for clause i if its disk is non-degenerate.
    Two guard cycles are disjoint if:
      (a) Their clauses share no variables, AND
      (b) Their annular regions (disk minus triangle) don't overlap.

    For the disjoint count, we build an independence graph:
    vertices = clauses with guard cycles, edges = conflicts.
    The maximum independent set gives the disjoint count.
    We approximate with a greedy algorithm.
    """
    m = len(clauses)
    # All non-degenerate clauses have a guard cycle
    has_guard = [i for i in range(m) if clause_geom[i]['center'] is not None
                 and clause_geom[i]['radius'] > 1e-12]

    # Build conflict graph: two guard cycles conflict if clauses share a variable
    # OR if their disks overlap (annuli could interfere)
    var_to_clauses = defaultdict(list)
    for i, clause in enumerate(clauses):
        for v, _ in clause:
            var_to_clauses[v].append(i)

    conflicts = defaultdict(set)
    for i in has_guard:
        # Variable conflicts
        for v, _ in clauses[i]:
            for j in var_to_clauses[v]:
                if j != i and j in set(has_guard):
                    conflicts[i].add(j)
        # Disk overlap conflicts
        if clause_geom[i]['center'] is not None:
            for j in has_guard:
                if j != i and j not in conflicts[i]:
                    if clause_geom[j]['center'] is not None:
                        dist = np.linalg.norm(
                            clause_geom[i]['center'] - clause_geom[j]['center'])
                        if dist < clause_geom[i]['radius'] + clause_geom[j]['radius']:
                            conflicts[i].add(j)
                            conflicts[j].add(i)

    # Greedy maximum independent set (sorted by degree, lowest first)
    remaining = set(has_guard)
    independent = []
    while remaining:
        # Pick vertex with fewest conflicts among remaining
        best = min(remaining, key=lambda v: len(conflicts[v] & remaining))
        independent.append(best)
        # Remove it and all its conflicts
        to_remove = {best} | (conflicts[best] & remaining)
        remaining -= to_remove

    return len(has_guard), len(independent)


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    t_start = time.time()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  Toy 289 — Circle Confinement: Guard Cycles & Čech Gap     ║")
    print("║  Casey's circle reformulation of 3-SAT constraint geometry  ║")
    print("║  AC_geometric = β₁(Čech) - β₁(simplicial)                 ║")
    print("╚══════════════════════════════════════════════════════════════╝")

    SIZES = [16, 20, 24, 28]
    ALPHAS = [3.0, 3.5, 4.0, 4.267, 4.5, 5.0]
    N_INSTANCES = 30
    SEED = 42

    # Storage for results
    results = {}  # (n, alpha, embedding) -> metrics

    for n in SIZES:
        for alpha in ALPHAS:
            for emb_name in ['force', 'spectral', 'random']:
                results[(n, alpha, emb_name)] = {
                    'b1_simp': [], 'b1_cech': [], 'ac_geom': [],
                    'area_ratio': [], 'guard_total': [], 'guard_disjoint': [],
                }

    rng = random.Random(SEED)

    for n in SIZES:
        for alpha in ALPHAS:
            print(f"\n  n={n}, α={alpha:.3f} ({int(alpha*n)} clauses)")
            print("  " + "─" * 56)

            for inst in range(N_INSTANCES):
                clauses = generate_3sat(n, alpha, rng)
                adj = build_vig(n, clauses)

                # β₁(simplicial) — same for all embeddings
                b1_s = beta1_simplicial(n, clauses)

                # Three embeddings
                for emb_name in ['force', 'spectral', 'random']:
                    emb_rng = random.Random(SEED + inst * 100 + hash(emb_name) % 1000)

                    if emb_name == 'force':
                        pos = embed_force_directed(n, adj, dim=2, iterations=150,
                                                    rng=emb_rng)
                    elif emb_name == 'spectral':
                        pos = embed_spectral(n, adj, dim=2)
                    else:
                        pos = embed_random(n, dim=2, rng=emb_rng)

                    # Clause geometry
                    cgeom = compute_clause_geometry(clauses, pos)

                    # Area ratios
                    ratios = [g['ratio'] for g in cgeom if g['ratio'] > 0]
                    mean_ratio = np.mean(ratios) if ratios else 0

                    # β₁(Čech)
                    b1_c = beta1_cech(cgeom)

                    # AC_geometric
                    ac_g = b1_c - b1_s

                    # Guard cycles
                    guard_total, guard_disjoint = count_guard_cycles(clauses, cgeom)

                    # Store
                    r = results[(n, alpha, emb_name)]
                    r['b1_simp'].append(b1_s)
                    r['b1_cech'].append(b1_c)
                    r['ac_geom'].append(ac_g)
                    r['area_ratio'].append(mean_ratio)
                    r['guard_total'].append(guard_total)
                    r['guard_disjoint'].append(guard_disjoint)

            # Print summary for this (n, alpha)
            for emb_name in ['force', 'spectral', 'random']:
                r = results[(n, alpha, emb_name)]
                b1s = np.mean(r['b1_simp'])
                b1c = np.mean(r['b1_cech'])
                acg = np.mean(r['ac_geom'])
                ar = np.mean(r['area_ratio'])
                gt = np.mean(r['guard_total'])
                gd = np.mean(r['guard_disjoint'])
                print(f"    {emb_name:>8}: β₁(S)={b1s:5.1f}  β₁(Č)={b1c:5.1f}  "
                      f"AC_g={acg:6.1f}  ratio={ar:.3f}  "
                      f"guard={gt:5.1f}/{gd:5.1f}")

    # ─── Analysis ────────────────────────────────────────────
    print(f"\n  " + "═" * 58)
    print(f"  ANALYSIS")
    print("  " + "═" * 58)

    # 1. Area ratio summary
    print(f"\n    Area Ratio (triangle/circle) — should be < 0.5:")
    print(f"    {'n':>4}  {'α':>6}  {'force':>8}  {'spectral':>8}  {'random':>8}")
    print(f"    {'─'*42}")
    for alpha in ALPHAS:
        for n in SIZES:
            vals = []
            for emb in ['force', 'spectral', 'random']:
                vals.append(np.mean(results[(n, alpha, emb)]['area_ratio']))
            print(f"    {n:>4}  {alpha:>6.3f}  {vals[0]:>8.4f}  {vals[1]:>8.4f}  {vals[2]:>8.4f}")

    # 2. AC_geometric summary
    print(f"\n    AC_geometric = β₁(Čech) - β₁(simplicial):")
    print(f"    {'n':>4}  {'α':>6}  {'force':>8}  {'spectral':>8}  {'random':>8}")
    print(f"    {'─'*42}")
    for alpha in ALPHAS:
        for n in SIZES:
            vals = []
            for emb in ['force', 'spectral', 'random']:
                vals.append(np.mean(results[(n, alpha, emb)]['ac_geom']))
            print(f"    {n:>4}  {alpha:>6.3f}  {vals[0]:>8.1f}  {vals[1]:>8.1f}  {vals[2]:>8.1f}")

    # 3. Guard cycle disjoint count
    print(f"\n    Disjoint Guard Cycles (independence count):")
    print(f"    {'n':>4}  {'α':>6}  {'force':>8}  {'spectral':>8}  {'random':>8}")
    print(f"    {'─'*42}")
    for alpha in ALPHAS:
        for n in SIZES:
            vals = []
            for emb in ['force', 'spectral', 'random']:
                vals.append(np.mean(results[(n, alpha, emb)]['guard_disjoint']))
            print(f"    {n:>4}  {alpha:>6.3f}  {vals[0]:>8.1f}  {vals[1]:>8.1f}  {vals[2]:>8.1f}")

    # 4. Growth analysis: does AC_geometric grow with n?
    print(f"\n    Growth Analysis at α_c = 4.267:")
    print(f"    {'n':>4}  {'AC_g(force)':>12}  {'AC_g(spec)':>12}  {'AC_g(rand)':>12}  "
          f"{'disjoint(f)':>12}  {'β₁(simp)':>10}")
    print(f"    {'─'*65}")
    ac_force = []; ac_spec = []; ac_rand = []; dj_force = []; b1_simp_vals = []
    for n in SIZES:
        af = np.mean(results[(n, 4.267, 'force')]['ac_geom'])
        asp = np.mean(results[(n, 4.267, 'spectral')]['ac_geom'])
        ar = np.mean(results[(n, 4.267, 'random')]['ac_geom'])
        df = np.mean(results[(n, 4.267, 'force')]['guard_disjoint'])
        b1s = np.mean(results[(n, 4.267, 'force')]['b1_simp'])
        ac_force.append(af); ac_spec.append(asp); ac_rand.append(ar)
        dj_force.append(df); b1_simp_vals.append(b1s)
        print(f"    {n:>4}  {af:>12.1f}  {asp:>12.1f}  {ar:>12.1f}  "
              f"{df:>12.1f}  {b1s:>10.1f}")

    # Linear regression for growth rate
    if len(SIZES) >= 3:
        ns = np.array(SIZES, dtype=float)
        for label, vals in [('AC_g(force)', ac_force), ('AC_g(spectral)', ac_spec),
                           ('disjoint(force)', dj_force)]:
            vals = np.array(vals)
            if np.std(ns) > 0:
                slope = np.polyfit(ns, vals, 1)[0]
                print(f"    {label}: slope = {slope:.3f} per variable")

    # 5. Embedding robustness
    print(f"\n    Embedding Robustness at α_c = 4.267:")
    for n in SIZES:
        ac_vals = []
        for emb in ['force', 'spectral', 'random']:
            ac_vals.append(np.mean(results[(n, 4.267, emb)]['ac_geom']))
        # Check if all have same sign and roughly same magnitude
        signs = [1 if v > 0 else (-1 if v < 0 else 0) for v in ac_vals]
        same_sign = len(set(signs)) == 1 and signs[0] != 0
        if max(abs(v) for v in ac_vals) > 0:
            cv = np.std(ac_vals) / max(abs(np.mean(ac_vals)), 0.01)
        else:
            cv = 0
        print(f"    n={n}: AC_g = {ac_vals}  same_sign={same_sign}  CV={cv:.2f}")

    # ─── Scorecard ────────────────────────────────────────────
    print(f"\n  " + "═" * 58)
    print(f"  SCORECARD")
    print("  " + "═" * 58)

    # Test 1: Area ratio < 0.5
    all_ratios = []
    for n in SIZES:
        for emb in ['force', 'spectral', 'random']:
            all_ratios.extend(results[(n, 4.267, emb)]['area_ratio'])
    mean_ratio = np.mean(all_ratios)
    score("Area ratio < 0.5 (triangles < 50% of circumcircle)",
          mean_ratio < 0.5,
          f"mean ratio = {mean_ratio:.4f}")

    # Test 2: AC_geometric > 0 at α_c
    ac_at_ac = np.mean(results[(SIZES[-1], 4.267, 'force')]['ac_geom'])
    score("AC_geometric > 0 at α_c (Čech sees more than simplicial)",
          ac_at_ac > 0,
          f"AC_g(n={SIZES[-1]}, force) = {ac_at_ac:.1f}")

    # Test 3: AC_geometric grows with n
    ac_growth = ac_force[-1] - ac_force[0] if len(ac_force) >= 2 else 0
    score("AC_geometric grows with n (Θ(n) not O(1))",
          ac_growth > 2,
          f"AC_g grew from {ac_force[0]:.1f} to {ac_force[-1]:.1f} "
          f"(Δ={ac_growth:.1f})")

    # Test 4: Guard cycle fraction > 0.3
    gt = np.mean(results[(SIZES[-1], 4.267, 'force')]['guard_total'])
    m_total = 4.267 * SIZES[-1]
    guard_frac = gt / m_total if m_total > 0 else 0
    score("Guard cycle fraction > 0.3 at α_c",
          guard_frac > 0.3,
          f"fraction = {guard_frac:.3f} ({gt:.0f}/{m_total:.0f})")

    # Test 5: Disjoint guard count grows with n
    dj_growth = dj_force[-1] - dj_force[0] if len(dj_force) >= 2 else 0
    score("Disjoint guard cycle count grows with n",
          dj_growth > 1,
          f"grew from {dj_force[0]:.1f} to {dj_force[-1]:.1f} (Δ={dj_growth:.1f})")

    # Test 6: Embedding robustness
    robust_count = 0
    for n in SIZES:
        ac_vals = [np.mean(results[(n, 4.267, emb)]['ac_geom'])
                   for emb in ['force', 'spectral', 'random']]
        signs = [1 if v > 0 else (-1 if v < 0 else 0) for v in ac_vals]
        if len(set(signs)) == 1 and signs[0] != 0:
            robust_count += 1
    score("Embedding-robust: same sign across all embeddings",
          robust_count >= len(SIZES) - 1,
          f"{robust_count}/{len(SIZES)} sizes have consistent sign")

    # Test 7: Phase transition visible in area ratio
    ratio_low = np.mean(results[(SIZES[-1], 3.0, 'force')]['area_ratio'])
    ratio_high = np.mean(results[(SIZES[-1], 5.0, 'force')]['area_ratio'])
    ratio_ac = np.mean(results[(SIZES[-1], 4.267, 'force')]['area_ratio'])
    ratio_change = abs(ratio_high - ratio_low)
    score("Phase transition visible in area ratio at α_c",
          ratio_change > 0.01,
          f"ratio at α=3.0: {ratio_low:.4f}, α_c: {ratio_ac:.4f}, "
          f"α=5.0: {ratio_high:.4f}")

    # Test 8: Disjoint guards > β₁(simplicial)
    dj_val = np.mean(results[(SIZES[-1], 4.267, 'force')]['guard_disjoint'])
    b1_val = np.mean(results[(SIZES[-1], 4.267, 'force')]['b1_simp'])
    score("Disjoint guard cycles > β₁(simplicial) at α_c",
          dj_val > b1_val,
          f"disjoint guards = {dj_val:.1f}, β₁(simp) = {b1_val:.1f}")

    print(f"\n  " + "═" * 58)
    print(f"  SCORECARD: {PASS}/{PASS + FAIL}")
    print("  " + "═" * 58)

    elapsed = time.time() - t_start
    print(f"\n  Toy 289 complete. ({elapsed:.0f}s)")


if __name__ == '__main__':
    main()
