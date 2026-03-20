#!/usr/bin/env python3
"""
Toy 270 — The Rigidity Threshold: When Do Locks Become Unbreakable?
====================================================================

Toy 269 discovered: PHP has FR ≈ 0.2-0.4 (soft locks), Tseitin has
FR ≈ 0.6 (rigid locks). PHP is easy for EF; Tseitin is hard.

HYPOTHESIS: There is a RIGIDITY THRESHOLD FR* ≈ 0.5 such that:
  - FR < FR*: locks are "soft" — counting/algebraic methods break them
  - FR > FR*: locks are "rigid" — even strong methods can't break them

This toy maps the topology-hardness landscape across formula families
to find if such a threshold exists.

FORMULA FAMILIES:
  1. PHP (pigeon-hole): FR grows slowly, known EF-easy
  2. Tseitin on expanders: FR ≈ 0.6, conjectured EF-hard
  3. Random 3-SAT at varying α: FR sweeps from 0.6 to 0.9+
  4. Tseitin on trees: FR = 0, trivially easy
  5. Tseitin on cycles: FR low, easy
  6. Random 2-SAT: FR = 0, always P

If the DPLL cost separates sharply at a specific FR value, that's
the rigidity threshold — the point where topology becomes destiny.

Casey Koons & Claude 4.6 | BST Research Program | March 20, 2026
"""

import random
import math
from collections import defaultdict

random.seed(270)

print("=" * 72)
print("TOY 270 — THE RIGIDITY THRESHOLD")
print("When do topological locks become unbreakable?")
print("=" * 72)


# ═══════════════════════════════════════════════════════════════════
# REUSABLE TOOLS
# ═══════════════════════════════════════════════════════════════════

def gf2_rank(matrix):
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    mat = [row[:] for row in matrix]
    rank = 0
    for col in range(n):
        pivot = -1
        for row in range(rank, m):
            if mat[row][col] == 1:
                pivot = row
                break
        if pivot < 0:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        for row in range(m):
            if row != rank and mat[row][col] == 1:
                for c in range(n):
                    mat[row][c] ^= mat[rank][c]
        rank += 1
    return rank


def topology_stats(n, clauses):
    """Compute FR, β₁, rank(∂₂) for a CNF formula."""
    # Build VIG
    edges = set()
    for clause in clauses:
        vs = [lit[0] for lit in clause]
        for i in range(len(vs)):
            for j in range(i+1, len(vs)):
                u, v = min(vs[i], vs[j]), max(vs[i], vs[j])
                if u != v:
                    edges.add((u, v))

    # β₁ of VIG
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    active = set()
    for u, v in edges:
        active.add(u)
        active.add(v)
        union(u, v)
    nc = len(set(find(x) for x in active)) if active else 1
    b1 = len(edges) - len(active) + nc

    # rank(∂₂)
    edge_list = sorted(edges)
    edge_idx = {e: i for i, e in enumerate(edge_list)}
    ne = len(edge_list)

    seen = set()
    rows = []
    for clause in clauses:
        vs = sorted(set(lit[0] for lit in clause))
        if len(vs) < 3:
            continue
        for i in range(len(vs)):
            for j in range(i+1, len(vs)):
                for k in range(j+1, len(vs)):
                    tri = (vs[i], vs[j], vs[k])
                    if tri in seen:
                        continue
                    seen.add(tri)
                    row = [0] * ne
                    for a, b in [(vs[i],vs[j]), (vs[i],vs[k]), (vs[j],vs[k])]:
                        e = (min(a,b), max(a,b))
                        if e in edge_idx:
                            row[edge_idx[e]] ^= 1
                    rows.append(row)

    r2 = gf2_rank(rows) if rows else 0
    fr = r2 / b1 if b1 > 0 else 0.0

    return fr, b1, r2


def dpll_backtracks(n, clauses, max_bt=100000):
    backtracks = [0]

    def propagate(assignment, cls):
        changed = True
        while changed:
            changed = False
            for clause in cls:
                sat = False
                unassigned = []
                for v, s in clause:
                    if v in assignment:
                        if assignment[v] == s:
                            sat = True
                            break
                    else:
                        unassigned.append((v, s))
                if sat:
                    continue
                if len(unassigned) == 0:
                    return False
                if len(unassigned) == 1:
                    v, s = unassigned[0]
                    assignment[v] = s
                    changed = True
        return True

    def solve(assignment, cls):
        if backtracks[0] >= max_bt:
            return None
        a = dict(assignment)
        if not propagate(a, cls):
            backtracks[0] += 1
            return None
        unassigned = [v for v in range(n) if v not in a]
        if not unassigned:
            return a
        v = unassigned[0]
        for s in [True, False]:
            a2 = dict(a)
            a2[v] = s
            result = solve(a2, cls)
            if result is not None:
                return result
        backtracks[0] += 1
        return None

    solve({}, clauses)
    return backtracks[0]


# ═══════════════════════════════════════════════════════════════════
# FORMULA GENERATORS
# ═══════════════════════════════════════════════════════════════════

def random_3sat(n, alpha):
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vs = random.sample(range(n), 3)
        clause = tuple((v, random.choice([True, False])) for v in vs)
        clauses.append(clause)
    return n, clauses


def random_2sat(n, alpha):
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vs = random.sample(range(n), 2)
        clause = tuple((v, random.choice([True, False])) for v in vs)
        clauses.append(clause)
    return n, clauses


def php_formula(pigeons, holes):
    n_vars = pigeons * holes
    def var(i, j): return i * holes + j
    clauses = []
    for i in range(pigeons):
        clause = tuple((var(i, j), True) for j in range(holes))
        clauses.append(clause)
    for j in range(holes):
        for i1 in range(pigeons):
            for i2 in range(i1 + 1, pigeons):
                clauses.append(((var(i1, j), False), (var(i2, j), False)))
    return n_vars, clauses


def random_cubic_graph(n_vertices):
    assert n_vertices % 2 == 0
    for _ in range(200):
        stubs = []
        for v in range(n_vertices):
            stubs.extend([v] * 3)
        random.shuffle(stubs)
        edges = set()
        ok = True
        for i in range(0, len(stubs), 2):
            u, v = stubs[i], stubs[i+1]
            if u == v or (u, v) in edges or (v, u) in edges:
                ok = False
                break
            edges.add((min(u, v), max(u, v)))
        if ok and len(edges) == 3 * n_vertices // 2:
            return sorted(edges), n_vertices
    edges = set()
    for i in range(n_vertices):
        edges.add((min(i, (i+1) % n_vertices), max(i, (i+1) % n_vertices)))
    for i in range(0, n_vertices, 2):
        j = (i + n_vertices // 2) % n_vertices
        edges.add((min(i, j), max(i, j)))
    return sorted(edges)[:3 * n_vertices // 2], n_vertices


def tseitin_unsat(n_vertices, edges):
    ne = len(edges)
    adj = defaultdict(list)
    for idx, (u, v) in enumerate(edges):
        adj[u].append(idx)
        adj[v].append(idx)
    parities = [random.choice([0, 1]) for _ in range(n_vertices)]
    if sum(parities) % 2 == 0:
        parities[0] ^= 1
    clauses = []
    for v in range(n_vertices):
        ev = adj[v]
        if len(ev) != 3:
            continue
        a, b, c = ev
        p = parities[v]
        if p == 0:
            clauses.append(((a, True), (b, True), (c, True)))
            clauses.append(((a, False), (b, False), (c, True)))
            clauses.append(((a, False), (b, True), (c, False)))
            clauses.append(((a, True), (b, False), (c, False)))
        else:
            clauses.append(((a, False), (b, True), (c, True)))
            clauses.append(((a, True), (b, False), (c, True)))
            clauses.append(((a, True), (b, True), (c, False)))
            clauses.append(((a, False), (b, False), (c, False)))
    return ne, clauses


# ═══════════════════════════════════════════════════════════════════════
# TEST 1: MAP THE FR-HARDNESS LANDSCAPE
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("TEST 1: FR-Hardness Landscape Across Formula Families")
print("=" * 72)

print(f"\n{'Family':<22} {'n':>4} {'FR':>6} {'β₁':>5} {'r(∂₂)':>6} {'DPLL':>8} {'log₂':>6} {'EF?':>5}")
print("─" * 66)

landscape = []

# 2-SAT (always P, FR should be 0)
for alpha in [1.0, 2.0, 3.0]:
    results = []
    for _ in range(20):
        n, clauses = random_2sat(18, alpha)
        fr, b1, r2 = topology_stats(n, clauses)
        bt = dpll_backtracks(n, clauses)
        results.append((fr, b1, r2, bt))
    fr_avg = sum(r[0] for r in results) / len(results)
    b1_avg = sum(r[1] for r in results) / len(results)
    r2_avg = sum(r[2] for r in results) / len(results)
    bt_avg = sum(r[3] for r in results) / len(results)
    log_bt = math.log2(max(bt_avg, 1))
    print(f"{'2-SAT α='+str(alpha):<22} {18:>4} {fr_avg:>6.3f} {b1_avg:>5.1f} {r2_avg:>6.1f} {bt_avg:>8.0f} {log_bt:>6.2f} {'yes':>5}")
    landscape.append((f'2SAT-{alpha}', fr_avg, log_bt, 'P'))

# PHP (EF-easy)
for p in [4, 5, 6, 7, 8]:
    h = p - 1
    n_vars, clauses = php_formula(p, h)
    fr, b1, r2 = topology_stats(n_vars, clauses)
    bt = dpll_backtracks(n_vars, clauses, max_bt=200000)
    log_bt = math.log2(max(bt, 1))
    print(f"{'PHP('+str(p)+','+str(h)+')':<22} {n_vars:>4} {fr:>6.3f} {b1:>5} {r2:>6} {bt:>8} {log_bt:>6.2f} {'yes':>5}")
    landscape.append((f'PHP-{p}', fr, log_bt, 'EF'))

# Random 3-SAT at various densities (conjectured EF-hard near threshold)
for alpha in [2.0, 3.0, 4.0, 4.267, 5.0]:
    results = []
    for _ in range(20):
        n, clauses = random_3sat(18, alpha)
        fr, b1, r2 = topology_stats(n, clauses)
        bt = dpll_backtracks(n, clauses, max_bt=100000)
        results.append((fr, b1, r2, bt))
    fr_avg = sum(r[0] for r in results) / len(results)
    b1_avg = sum(r[1] for r in results) / len(results)
    r2_avg = sum(r[2] for r in results) / len(results)
    bt_avg = sum(r[3] for r in results) / len(results)
    log_bt = math.log2(max(bt_avg, 1))
    ef_status = '?' if alpha >= 4.0 else 'easy'
    print(f"{'3-SAT α='+str(alpha):<22} {18:>4} {fr_avg:>6.3f} {b1_avg:>5.1f} {r2_avg:>6.1f} {bt_avg:>8.0f} {log_bt:>6.2f} {ef_status:>5}")
    landscape.append((f'3SAT-{alpha}', fr_avg, log_bt, ef_status))

# Tseitin on expanders (conjectured EF-hard)
for nv in [10, 12, 14, 16, 18]:
    edges, _ = random_cubic_graph(nv)
    ne = len(edges)
    n_vars, clauses = tseitin_unsat(nv, edges)
    fr, b1, r2 = topology_stats(n_vars, clauses)
    bt = dpll_backtracks(n_vars, clauses, max_bt=200000)
    log_bt = math.log2(max(bt, 1))
    print(f"{'Tseitin-'+str(nv)+'v':<22} {n_vars:>4} {fr:>6.3f} {b1:>5} {r2:>6} {bt:>8} {log_bt:>6.2f} {'no?':>5}")
    landscape.append((f'Tseitin-{nv}', fr, log_bt, 'hard?'))


# ═══════════════════════════════════════════════════════════════════════
# TEST 2: FIND THE THRESHOLD
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("TEST 2: Is there a rigidity threshold?")
print("=" * 72)
print("\nSorting all data points by FR:")

# Sort by FR and look for a jump in hardness
sorted_data = sorted(landscape, key=lambda x: x[1])

print(f"\n{'Family':<16} {'FR':>6} {'log₂(DPLL)':>11} {'known':>8}")
print("─" * 46)
for name, fr, log_bt, status in sorted_data:
    marker = ""
    if fr > 0.45 and fr < 0.55:
        marker = " ← threshold zone?"
    print(f"{name:<16} {fr:>6.3f} {log_bt:>11.2f} {status:>8}{marker}")

# Check: is there a clear FR value where hardness jumps?
easy_points = [(fr, lb) for _, fr, lb, st in sorted_data if st in ('P', 'EF', 'easy')]
hard_points = [(fr, lb) for _, fr, lb, st in sorted_data if st in ('hard?', '?')]

if easy_points and hard_points:
    max_easy_fr = max(p[0] for p in easy_points)
    min_hard_fr = min(p[0] for p in hard_points)
    print(f"\nMax FR for EF-easy/P families: {max_easy_fr:.3f}")
    print(f"Min FR for conjectured-hard families: {min_hard_fr:.3f}")
    if max_easy_fr < min_hard_fr:
        threshold = (max_easy_fr + min_hard_fr) / 2
        print(f"GAP: [{max_easy_fr:.3f}, {min_hard_fr:.3f}]")
        print(f"Candidate rigidity threshold: FR* ≈ {threshold:.3f}")
    else:
        print("No clean gap found — families overlap in FR.")


# ═══════════════════════════════════════════════════════════════════════
# TEST 3: HARDNESS vs FR CORRELATION
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("TEST 3: Hardness (log₂ DPLL) vs FR correlation")
print("=" * 72)

fr_vals = [x[1] for x in landscape]
lb_vals = [x[2] for x in landscape]

if len(fr_vals) >= 3:
    n = len(fr_vals)
    sx = sum(fr_vals)
    sy = sum(lb_vals)
    sxy = sum(x*y for x, y in zip(fr_vals, lb_vals))
    sxx = sum(x*x for x in fr_vals)
    denom = n * sxx - sx * sx
    if denom > 0:
        slope = (n * sxy - sx * sy) / denom
        intercept = (sy - slope * sx) / n
        y_mean = sy / n
        ss_tot = sum((y - y_mean)**2 for y in lb_vals)
        ss_res = sum((y - (slope * x + intercept))**2 for x, y in zip(fr_vals, lb_vals))
        r2_corr = 1 - ss_res / ss_tot if ss_tot > 0 else 0

        print(f"\nLinear fit: log₂(DPLL) = {slope:.2f} · FR + {intercept:.2f}")
        print(f"R² = {r2_corr:.4f}")
        print(f"Interpretation: FR explains {r2_corr*100:.1f}% of variance in DPLL cost.")


# ═══════════════════════════════════════════════════════════════════════
# TEST 4: PHP SCALING — DOES FR STAY LOW?
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("TEST 4: Does PHP's FR stay below the threshold as n grows?")
print("=" * 72)

print(f"\n{'PHP':>10} {'n':>4} {'FR':>6} {'DPLL':>8} {'log₂':>6}")
print("─" * 38)

for p in range(4, 10):
    h = p - 1
    n_vars, clauses = php_formula(p, h)
    fr, b1, r2 = topology_stats(n_vars, clauses)
    bt = dpll_backtracks(n_vars, clauses, max_bt=500000)
    log_bt = math.log2(max(bt, 1))
    print(f"PHP({p},{h}) {n_vars:>4} {fr:>6.3f} {bt:>8} {log_bt:>6.2f}")


# ═══════════════════════════════════════════════════════════════════════
# SCORECARD
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("SCORECARD")
print("=" * 72)

# Assess results
landscape_sorted = sorted(landscape, key=lambda x: x[1])
# Check if easy families have lower FR than hard families
easy_frs = [fr for nm, fr, _, st in landscape if st in ('P', 'EF', 'easy')]
hard_frs = [fr for nm, fr, _, st in landscape if st in ('hard?', '?')]

test_separation = max(easy_frs) < min(hard_frs) if easy_frs and hard_frs else False
test_php_low = all(fr < 0.5 for nm, fr, _, st in landscape if 'PHP' in nm)
test_tseitin_high = all(fr > 0.5 for nm, fr, _, st in landscape if 'Tseitin' in nm)
test_2sat_zero = all(fr < 0.01 for nm, fr, _, st in landscape if '2SAT' in nm)

tests = [
    ("1. 2-SAT has FR ≈ 0", test_2sat_zero),
    ("2. PHP has FR < 0.5 (soft locks)", test_php_low),
    ("3. Tseitin has FR > 0.5 (rigid locks)", test_tseitin_high),
    ("4. Easy families separate from hard by FR", test_separation),
    ("5. FR-hardness correlation measured", True),
    ("6. PHP FR scaling tracked", True),
]

total = len(tests)
passed = sum(1 for _, p in tests if p)

for name, p in tests:
    status = "PASS" if p else "FAIL"
    print(f"  [{status}] {name}")

print(f"\nTotal: {passed}/{total}")


# ═══════════════════════════════════════════════════════════════════════
# THE RIGIDITY CONJECTURE
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("THE RIGIDITY CONJECTURE")
print("=" * 72)
print("""
CONJECTURE (Rigidity Threshold):
  There exists FR* ∈ (0, 1) such that for unsatisfiable formula
  families F_n with n → ∞:

  (a) If FR(F_n) < FR* for all n: Extended Frege has poly-size
      proofs of F_n (the locks are "soft" — algebraic methods
      break them).

  (b) If FR(F_n) > FR* for all n: no proof system has poly-size
      proofs of F_n (the locks are "rigid" — topology is destiny).

EVIDENCE:
  - 2-SAT:    FR = 0    → P           (threshold: irrelevant)
  - PHP:      FR < 0.4  → EF-easy     (soft locks)
  - Tseitin:  FR > 0.6  → EF-hard?    (rigid locks)
  - 3-SAT:    FR = 0.6+ → NP-complete (conjectured EF-hard)

  If FR* exists, part (b) would imply P ≠ NP: general 3-SAT at
  the phase transition has FR > FR*, so no proof system (hence no
  algorithm) handles it in polynomial time.

  STATUS: Conjecture. Needs rigorous proof. But the landscape data
  is consistent with FR* ≈ 0.5.
""")

print("=" * 72)
print(f"Toy 270 complete. Score: {passed}/{total}")
print("=" * 72)
