#!/usr/bin/env python3
"""
Toy 5518 — E4 (Round 3): THE HEAWOOD GF(3) INSTRUMENT

Heawood 1898: a sphere triangulation is 4-colorable iff the triangle-sum
linear system over GF(3) — one variable x_f per face, one constraint per
vertex (sum of incident faces == 0 mod 3) — has a solution with every
x_f in {+1,-1} (nonzero support). This is 4CT as LINEAR ALGEBRA — the
corpus's home game (GF/Reed-Solomon substrate framing; linear-algebra
standing order; board Round 73 literature anchor arXiv 2411.15992).

THE INSTRUMENT: (a) consistent face orientations via dual BFS; (b) the
coloring -> x map: for an oriented face, the Klein edge labels in cyclic
order (a XOR b, b XOR c, c XOR a) are a permutation of {1,2,3}; x_f = +1 for
cyclic (even), -1 for anti-cyclic (odd); (c) the vertex-face incidence
matrix over GF(3) with rank/nullity; (d) the LOCAL EXTENSION predicate at a
tau=6 vertex v: do there exist star-face values y_1..y_5 in {+1,-1}
satisfying v's constraint and the five link-vertex constraints, given the
x's derived from the G-v coloring? (32-way brute force.)

*** BLIND PREDICTION — registered before the cross-tab was computed ***
(E4-blind, Elie): stuck (double-fail) colorings are locally GF(3)-INFEASIBLE
and rescuable ones feasible — i.e., the local Heawood system detects
stuckness. Uncertain; can fail; either outcome calibrates whether the GF(3)
window sees Kempe dynamics at all.
*** END BLIND ***

TESTS (X/Y):
  1. Orientation instrument: every edge traversed twice in opposite
     directions, all witness graphs.
  2. Heawood correspondence VALIDATED: full proper colorings of Fritsch
     (and T_3) -> derived x satisfies every vertex sum == 0 mod 3, 100%.
  3. Rank/nullity of the incidence system over GF(3) per witness graph
     computed and reported.
  4. G-v witness colorings: interior vertices (full star) satisfy their
     constraint, 100% (the partial-coloring instrument is sound).
  5. Blind cross-tab scored: stuck ==> locally infeasible (full 2x2
     reported either way).

Elie, 2026-08-30. Millennium week, 4-Color round 3. 5 tests.
"""

import importlib.util
import itertools
import os
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


G5 = load("toy5512g", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")
T5 = load("toy5515g", "toy_5515_AUG30_E1_kring_tower_family_rescue_depth_vs_k"
          "_cal_F0_absorbed.py")


# ---------------------------------------------------------------- orientation

def orient_faces(faces):
    """Consistently orient a sphere triangulation's face list via dual BFS.
    Returns list of ordered triples."""
    edge2faces = defaultdict(list)
    for i, f in enumerate(faces):
        p, q, r = f
        for e in ((p, q), (q, r), (p, r)):
            edge2faces[frozenset(e)].append(i)
    oriented = {0: tuple(faces[0])}
    queue = [0]
    while queue:
        i = queue.pop()
        a, b, c = oriented[i]
        dir_edges = {(a, b), (b, c), (c, a)}
        for e in (frozenset((a, b)), frozenset((b, c)), frozenset((c, a))):
            for j in edge2faces[e]:
                if j == i or j in oriented:
                    continue
                u, w = tuple(e)
                # face j must traverse this edge opposite to face i
                if (u, w) in dir_edges:
                    need = (w, u)
                else:
                    need = (u, w)
                x = next(y for y in faces[j] if y not in e)
                oriented[j] = (need[0], need[1], x)
                queue.append(j)
    return [oriented[i] for i in range(len(faces))]


def check_orientation(oriented):
    dir_count = Counter()
    for a, b, c in oriented:
        for e in ((a, b), (b, c), (c, a)):
            dir_count[e] += 1
    for (u, w), cnt in dir_count.items():
        if cnt != 1 or dir_count.get((w, u), 0) != 1:
            return False
    return True


# ---------------------------------------------------------------- Heawood map

def face_sign(face, color):
    """+1 (GF3: 1) if the Klein edge labels around the oriented face are a
    cyclic permutation of (1,2,3); -1 (GF3: 2) otherwise. None if any vertex
    uncolored."""
    a, b, c = face
    if color.get(a) is None or color.get(b) is None or color.get(c) is None:
        return None
    l1 = color[a] ^ color[b]
    l2 = color[b] ^ color[c]
    l3 = color[c] ^ color[a]
    if {l1, l2, l3} != {1, 2, 3}:
        return None
    return 1 if (l1, l2, l3) in ((1, 2, 3), (2, 3, 1), (3, 1, 2)) else 2


def gf3_rank(rows, ncols):
    """Gaussian elimination over GF(3). rows: list of lists."""
    M = [r[:] for r in rows]
    rank = 0
    col = 0
    nrows = len(M)
    while rank < nrows and col < ncols:
        piv = next((i for i in range(rank, nrows) if M[i][col] % 3), None)
        if piv is None:
            col += 1
            continue
        M[rank], M[piv] = M[piv], M[rank]
        inv = 1 if M[rank][col] % 3 == 1 else 2
        M[rank] = [(x * inv) % 3 for x in M[rank]]
        for i in range(nrows):
            if i != rank and M[i][col] % 3:
                f = M[i][col] % 3
                M[i] = [(M[i][j] - f * M[rank][j]) % 3 for j in range(ncols)]
        rank += 1
        col += 1
    return rank


# ---------------------------------------------------------------- main

if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5518 — E4: the Heawood GF(3) instrument")
    print("=" * 70)

    fri_faces = G5.fritsch_faces()
    fri = G5.adj_from_faces(fri_faces)
    err = G5.errera_adj()
    err_faces, _o, _m = G5.faces_from_adj_triangulation(err)
    kit = G5.kittell_adj()
    kit_faces, _o2, _m2 = G5.faces_from_adj_triangulation(kit)
    t3_faces = T5.tower_faces(3)
    t3 = T5.adj_from_faces(t3_faces)

    graphs = [('Fritsch', fri_faces, fri), ('Errera', err_faces, err),
              ('Kittell', kit_faces, kit), ('T_3', t3_faces, t3)]

    # Test 1: orientation
    print("\n" + "=" * 70)
    print("Test 1: consistent orientations")
    print("=" * 70)
    ok1 = True
    oriented = {}
    for name, faces, adj in graphs:
        of = orient_faces(faces)
        good = check_orientation(of) and len(of) == len(faces)
        oriented[name] = of
        print(f"  {name}: {len(of)} faces oriented -> {'ok' if good else 'FAIL'}")
        ok1 &= good
    t1 = ok1
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Orientation instrument")

    # Test 2: Heawood correspondence on full colorings
    print("\n" + "=" * 70)
    print("Test 2: coloring -> x satisfies all vertex sums (full colorings)")
    print("=" * 70)
    n2 = ok2 = 0
    for name, adj, faces in [('Fritsch', fri, oriented['Fritsch']),
                             ('T_3', t3, oriented['T_3'])]:
        # full proper colorings via backtracking, cap 150
        cols = []
        col = {}
        vs = sorted(adj)

        def bt(i):
            if len(cols) >= 150:
                return
            if i == len(vs):
                cols.append(dict(col))
                return
            u = vs[i]
            for c in range(4):
                if all(col.get(w) != c for w in adj[u]):
                    col[u] = c
                    bt(i + 1)
                    del col[u]

        bt(0)
        for c in cols:
            xs = [face_sign(f, c) for f in faces]
            if any(x is None for x in xs):
                continue
            good = True
            for v in adj:
                s = sum(x for f, x in zip(faces, xs) if v in f) % 3
                if s != 0:
                    good = False
                    break
            n2 += 1
            ok2 += good
        print(f"  {name}: {len(cols)} full colorings checked")
    t2 = n2 > 0 and ok2 == n2
    print(f"\n  vertex-sum law holds: {ok2}/{n2}")
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Heawood correspondence "
          f"validated (convention pinned: +1 = cyclic (1,2,3) labels)")

    # Test 3: rank/nullity
    print("\n" + "=" * 70)
    print("Test 3: incidence system rank over GF(3)")
    print("=" * 70)
    for name, faces, adj in graphs:
        F = len(faces)
        V = len(adj)
        vs = sorted(adj)
        rows = [[1 if v in f else 0 for f in faces] for v in vs]
        rk = gf3_rank(rows, F)
        print(f"  {name}: V={V} F={F} rank={rk} nullity={F - rk}")
    t3_ = True
    print(f"\n  [PASS] 3. Rank data computed")

    # Tests 4-5: witness colorings
    print("\n" + "=" * 70)
    print("Tests 4-5: G-v witnesses — interior validation + local extension")
    print("=" * 70)
    n4 = ok4 = 0
    xtab = Counter()
    for name, faces, adj, tvs, exhaustive in [
            ('Fritsch', oriented['Fritsch'], fri,
             [v for v in sorted(fri) if len(fri[v]) == 5], True),
            ('T_3', oriented['T_3'], t3, [0], True),
            ('Errera', oriented['Errera'], err, [0, 4], False)]:
        for tv in tvs:
            cols = (G5.exhaustive_colorings(adj, tv) if exhaustive
                    else G5.sampled_colorings(adj, tv, 600))
            for c in cols:
                if G5.operational_tau(adj, c, tv) != 6:
                    continue
                info = G5.structure_true(
                    [tuple(sorted(f)) for f in faces], adj, c, tv)
                if info is None:
                    continue
                swaps, _fl = G5.forced_swaps(adj, c, tv, info)
                succ = sum(1 for (a, b), fv, ch in swaps
                           if G5.operational_tau(
                               adj, G5.do_swap(c, ch, a, b), tv) <= 5)
                stuck = (succ == 0)
                star = [f for f in faces if tv in f]
                rest = [f for f in faces if tv not in f]
                xs = {f: face_sign(f, c) for f in rest}
                # test 4: interior vertices (no star face) satisfy the law
                for v in adj:
                    if v == tv or v in adj[tv]:
                        continue
                    s = sum(xs[f] for f in rest if v in f) % 3
                    n4 += 1
                    ok4 += (s == 0)
                # test 5: local extension over the 5 star faces
                feasible = False
                for assign in itertools.product((1, 2), repeat=5):
                    if sum(assign) % 3 != 0:
                        continue
                    good = True
                    for u in adj[tv]:
                        s = sum(xs[f] for f in rest if u in f and xs[f])
                        s += sum(a for f, a in zip(star, assign) if u in f)
                        if s % 3 != 0:
                            good = False
                            break
                    if good:
                        feasible = True
                        break
                xtab[(name, stuck, feasible)] += 1
    t4 = n4 > 0 and ok4 == n4
    print(f"\n  interior vertex-sum law on witnesses: {ok4}/{n4}")
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Partial-coloring instrument "
          f"sound")
    print("\n  local-extension cross-tab (graph, stuck?, feasible?): count")
    for k in sorted(xtab):
        print(f"    {k}: {xtab[k]}")
    # blind: stuck ==> infeasible AND rescuable ==> feasible
    viol_a = sum(v for (g, st, fe), v in xtab.items() if st and fe)
    viol_b = sum(v for (g, st, fe), v in xtab.items() if not st and not fe)
    t5 = (sum(xtab.values()) > 0 and viol_a == 0 and viol_b == 0)
    print(f"\n  blind-prediction violations: stuck-but-feasible {viol_a}, "
          f"free-but-infeasible {viol_b}")
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. Blind: GF(3) local "
          f"feasibility separates stuck from rescuable")

    results = [t1, t2, t3_, t4, t5]
    passed = sum(results)
    print(f"\n{'=' * 70}")
    print(f"Toy 5518 -- SCORE: {passed}/{len(results)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(results, 1):
        if not r:
            print(f"  Test {i}: FAIL")
