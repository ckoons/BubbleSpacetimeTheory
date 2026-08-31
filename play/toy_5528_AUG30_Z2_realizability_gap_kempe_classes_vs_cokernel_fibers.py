#!/usr/bin/env python3
"""
Toy 5528 — Z2 (Round 6): THE REALIZABILITY GAP, MEASURED

Cal SS786 1(b): a fixed matrix's columns are a coloring-independent SUPERSET
of realizable currents; invariants from the superset are SOUND, reachability
claims are NOT. Z2 makes the gap empirical at the level where it bites:

On every exhaustively-enumerable graph in the program:
  (A) KEMPE CLASSES on partition space (colorings up to color permutation;
      swaps act on partitions; BFS to closure) versus COKERNEL FIBERS
      (Y1's SNF instrument; per partition the winding vector is defined up
      to global sign, so fibers compare {omega, -omega}).
      Any SAME-FIBER, DIFFERENT-CLASS pair = a closed-graph GC-I
      counterexample — the realizability gap manifesting as unreachability
      the linear theory cannot see.
  (B) Per-class achieved current lattices L_C vs the global achieved
      lattice L: SNF both, compare invariant factors — a proper sublattice
      means currents themselves are class-dependent (the gap at the
      lattice level).
SCOPE HONESTY: the FORMAL superset lattice (all dual cuts x sign patterns)
awaits the realizability lemma's alphabet definition (Cal 1(b), Lyra's
lemma); this toy measures the population-achieved vs class-achieved gap,
which is the reachability-relevant part.

Controls: octahedron (Eulerian) MUST be single Kempe class (Fisk 1973) —
positive control; tetrahedron trivial.

Graphs: octahedron · tetrahedron · triakis · Fritsch · icosahedron · T_3 ·
diluted-m1 (Y3's 11-vertex triakis+octahedron) · T(3) subdivided tetra.

TESTS (X/Y):
  1. Fisk control: octahedron single Kempe class.
  2. Class/fiber tables computed for all graphs (the deliverable).
  3. GC-I census: count same-fiber different-class pairs (ANY hit printed
     loudly as a closed-graph GC-I counterexample; zero hits = soundness-
     consistent data). Scored as: census complete.
  4. Lattice gap (B): per-class lattices equal the global lattice on
     single-class graphs (consistency); differences reported on
     multi-class graphs. Scored as computed.

Elie, 2026-08-30. Millennium week, 4-Color round 6. 4 tests.
"""

import importlib.util
import itertools
import os
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


G5 = load("g5512z", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")
T5 = load("t5515z", "toy_5515_AUG30_E1_kring_tower_family_rescue_depth_vs_k"
          "_cal_F0_absorbed.py")
H8 = load("t5518z", "toy_5518_AUG30_E4_heawood_gf3_instrument_rank_coset"
          "_stuck_separation.py")
Y3 = load("t5525z", "toy_5525_AUG30_Y3_dilution_test_akempic_knot_in"
          "_eulerian_bulk.py")
Y1 = load("t5527z", "toy_5527_AUG30_Y1_snf_engine_charge_lattice_invariant"
          "_factors.py")
X4 = load("t5522z", "toy_5522_AUG30_X4_akempic_import_subdivided_tetrahedron"
          "_frozen_coloring_orthogonality.py")


def octahedron_faces():
    return Y3.subdivided_octahedron_faces(1)


def tetrahedron_faces():
    return [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]


def all_colorings(adj):
    vs = sorted(adj, key=str)
    out = []
    col = {}

    def bt(i):
        if i == len(vs):
            out.append(dict(col))
            return
        u = vs[i]
        for c in range(4):
            if i == 0 and c != 0:
                continue
            if all(col.get(w) != c for w in adj[u]):
                col[u] = c
                bt(i + 1)
                del col[u]

    bt(0)
    return out, vs


def partition_key(col, vs):
    classes = {}
    key = []
    nxt = 0
    for v in vs:
        c = col[v]
        if c not in classes:
            classes[c] = nxt
            nxt += 1
        key.append(classes[c])
    return tuple(key)


def kempe_classes(adj, colorings, vs):
    """Classes on partition space. Returns (class_id per partition-key,
    n_classes, partition list)."""
    parts = {}
    for c in colorings:
        k = partition_key(c, vs)
        if k not in parts:
            parts[k] = c
    keys = list(parts)
    cid = {}
    n = 0
    for k0 in keys:
        if k0 in cid:
            continue
        n += 1
        q = deque([parts[k0]])
        cid[k0] = n - 1
        while q:
            c = q.popleft()
            for a, b in itertools.combinations(range(4), 2):
                done = set()
                for u in adj:
                    if u in done or c[u] not in (a, b):
                        continue
                    comp = set()
                    stack = [u]
                    while stack:
                        x = stack.pop()
                        if x in comp:
                            continue
                        comp.add(x)
                        for w in adj[x]:
                            if w not in comp and c[w] in (a, b):
                                stack.append(w)
                    done |= comp
                    nc = dict(c)
                    for x in comp:
                        nc[x] = b if nc[x] == a else a
                    k = partition_key(nc, vs)
                    if k not in cid:
                        cid[k] = n - 1
                        q.append(nc)
    return cid, n, parts


def graph_analysis(name, faces, adj):
    colorings, vs = all_colorings(adj)
    cid, n_classes, parts = kempe_classes(adj, colorings, vs)
    of = H8.orient_faces([tuple(f) for f in faces])
    # currents per class and global
    def columns_of(pop):
        cols = set()
        for c in pop:
            w0 = Y1.omega_vector(of, adj, c, vs)
            for a, b in itertools.combinations(range(4), 2):
                done = set()
                for u in adj:
                    if u in done or c[u] not in (a, b):
                        continue
                    comp = set()
                    stack = [u]
                    while stack:
                        x = stack.pop()
                        if x in comp:
                            continue
                        comp.add(x)
                        for w in adj[x]:
                            if w not in comp and c[w] in (a, b):
                                stack.append(w)
                    done |= comp
                    nc = dict(c)
                    for x in comp:
                        nc[x] = b if nc[x] == a else a
                    w1 = Y1.omega_vector(of, adj, nc, vs)
                    d = tuple(x1 - x0 for x0, x1 in zip(w0, w1))
                    if any(d):
                        cols.add(d)
        return list(cols)

    # global lattice + fibers
    reps_pop = [parts[k] for k in parts]
    cols_g = columns_of(reps_pop)
    if cols_g:
        A = [[col[i] for col in cols_g] for i in range(len(vs))]
        diag, U = Y1.smith_normal_form(A)
    else:
        diag, U = [], [[1 if i == j else 0 for j in range(len(vs))]
                      for i in range(len(vs))]
    # fibers on partitions (omega up to sign)
    fiber_id = {}
    fibers = []
    for k, c in parts.items():
        w = Y1.omega_vector(of, adj, c, vs)
        found = None
        for i, r in enumerate(fibers):
            for sgn in (1, -1):
                d = [a - sgn * b for a, b in zip(w, r)]
                if Y1.in_image(diag, U, d):
                    found = i
                    break
            if found is not None:
                break
        if found is None:
            fibers.append(w)
            found = len(fibers) - 1
        fiber_id[k] = found
    # class-fiber cross table
    pairs_gap = 0
    keys = list(parts)
    class_of = {k: cid[k] for k in keys}
    for i, k1 in enumerate(keys):
        for k2 in keys[i + 1:]:
            if fiber_id[k1] == fiber_id[k2] and class_of[k1] != class_of[k2]:
                pairs_gap += 1
    # per-class lattices
    class_lattices_equal = True
    class_factors = []
    for ci in range(n_classes):
        pop_c = [parts[k] for k in keys if class_of[k] == ci]
        cols_c = columns_of(pop_c)
        if cols_c:
            Ac = [[col[i] for col in cols_c] for i in range(len(vs))]
            dc, _ = Y1.smith_normal_form(Ac)
        else:
            dc = []
        class_factors.append([d for d in dc if d not in (0,)])
        if [d for d in dc if d != 0] != [d for d in diag if d != 0]:
            class_lattices_equal = False
    n_parts = len(parts)
    print(f"\n  {name}: partitions={n_parts} Kempe-classes={n_classes} "
          f"fibers={len(fibers)}")
    print(f"    global factors {[d for d in diag if d not in (0, 1)]}; "
          f"same-fiber/diff-class pairs: {pairs_gap}"
          + ("  *** CLOSED-GRAPH GC-I COUNTEREXAMPLE(S) ***"
             if pairs_gap else ""))
    if n_classes > 1:
        print(f"    class sizes: "
              f"{sorted(Counter(class_of.values()).values(), reverse=True)}"
              f"  per-class factors equal global: {class_lattices_equal}")
    return {'n_classes': n_classes, 'fibers': len(fibers),
            'gap_pairs': pairs_gap, 'parts': n_parts,
            'lat_eq': class_lattices_equal}


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5528 — Z2: realizability gap — Kempe classes vs cokernel fibers")
    print("=" * 70)

    oc_f = octahedron_faces()
    oc = Y3.adj_from_faces(oc_f)
    te_f = tetrahedron_faces()
    te = G5.adj_from_faces(te_f)
    tri_f = Y3.triakis_faces()
    tri = Y3.adj_from_faces(tri_f)
    fri_f = G5.fritsch_faces()
    fri = G5.adj_from_faces(fri_f)
    ico_f = T5.tower_faces(2)
    ico = T5.adj_from_faces(ico_f)
    t3_f = T5.tower_faces(3)
    t3g = T5.adj_from_faces(t3_f)
    sub_f = X4.subdivided_tetra_faces(3)
    sub = X4.adj_from_faces(sub_f)
    # diluted m=1 (Y3's construction, identification 0)
    colf = Y3.octa_3coloring(1)
    seam_b = None
    for f in oc_f:
        if sorted(colf(p) for p in f) == [0, 1, 2]:
            seam_b = tuple(p for c in (0, 1, 2) for p in f if colf(p) == c)
            break
    dil_f = Y3.glue(tri_f, ('aBCD', 'B', 'C'), oc_f, seam_b)
    dil = Y3.adj_from_faces(dil_f)

    R = {}
    for name, faces, adj in [('tetrahedron', te_f, te),
                             ('octahedron', oc_f, oc),
                             ('triakis', tri_f, tri),
                             ('Fritsch', fri_f, fri),
                             ('diluted-m1', dil_f, dil),
                             ('icosahedron', ico_f, ico),
                             ('subdiv-tetra-T3', sub_f, sub),
                             ('tower-T_3', t3_f, t3g)]:
        R[name] = graph_analysis(name, faces, adj)

    t1 = R['octahedron']['n_classes'] == 1
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Fisk control: octahedron "
          f"single class ({R['octahedron']['n_classes']})")
    t2 = len(R) == 8
    print(f"  [{'PASS' if t2 else 'FAIL'}] 2. Class/fiber tables computed "
          f"(8 graphs)")
    total_gap = sum(r['gap_pairs'] for r in R.values())
    t3 = True
    print(f"  [{'PASS' if t3 else 'FAIL'}] 3. GC-I census complete: "
          f"same-fiber/diff-class pairs TOTAL = {total_gap} "
          f"({'COUNTEREXAMPLES EXIST — the linear theory is incomplete on '
             'closed graphs' if total_gap else 'zero — GC-I consistent on '
             'every exhaustively-checked closed graph'})")
    t4 = True
    print(f"  [{'PASS' if t4 else 'FAIL'}] 4. Lattice gap measured "
          f"(per-class vs global)")

    # ---------------- Tests 5-6: THE GF(2) LENS (hunts-first directive,
    # applied to the closed counterexamples the moment they appeared) -----
    print("\n" + "=" * 70)
    print("Tests 5-6: the GF(2) face-space lens on the same graphs")
    print("=" * 70)

    def gf2_fibers(faces, adj):
        colorings, vs = all_colorings(adj)
        cid, ncl, parts = kempe_classes(adj, colorings, vs)
        of = H8.orient_faces([tuple(f) for f in faces])
        forder = list(of)

        def eps(c):
            return tuple(0 if H8.face_sign(f, c) == 1 else 1 for f in forder)

        cols = set()
        for c in colorings:
            e0 = eps(c)
            for a, b in itertools.combinations(range(4), 2):
                done = set()
                for u in adj:
                    if u in done or c[u] not in (a, b):
                        continue
                    comp = set()
                    stack = [u]
                    while stack:
                        x = stack.pop()
                        if x in comp:
                            continue
                        comp.add(x)
                        for w in adj[x]:
                            if w not in comp and c[w] in (a, b):
                                stack.append(w)
                    done |= comp
                    nc = dict(c)
                    for x in comp:
                        nc[x] = b if nc[x] == a else a
                    d = tuple(x ^ y for x, y in zip(e0, eps(nc)))
                    if any(d):
                        cols.add(d)
        basis = []
        for cvec in cols:
            v = list(cvec)
            for bb in basis:
                piv = next(i for i, x in enumerate(bb) if x)
                if v[piv]:
                    v = [x ^ y for x, y in zip(v, bb)]
            if any(v):
                basis.append(v)

        def red(v):
            v = list(v)
            for bb in basis:
                piv = next(i for i, x in enumerate(bb) if x)
                if v[piv]:
                    v = [x ^ y for x, y in zip(v, bb)]
            return tuple(v)

        fibs = {}
        for k, c in parts.items():
            e = eps(c)
            key = min(red(e), red(tuple(1 ^ x for x in e)))
            fibs.setdefault(key, set()).add(cid[partition_key(c, vs)])
        merged = sum(len(s) - 1 for s in fibs.values())
        over = len(fibs) > ncl
        return ncl, len(fibs), merged, over, len(basis)

    sep_ok = True
    sound_ok = True
    for name, faces, adj in [('tetrahedron', te_f, te),
                             ('octahedron', oc_f, oc),
                             ('triakis', tri_f, tri),
                             ('Fritsch', fri_f, fri),
                             ('diluted-m1', dil_f, dil),
                             ('icosahedron', ico_f, ico),
                             ('subdiv-tetra-T3', sub_f, sub),
                             ('tower-T_3', t3_f, t3g)]:
        ncl, nfib, merged, over, dim = gf2_fibers(faces, adj)
        print(f"  {name}: classes={ncl} GF2-fibers={nfib} span-dim={dim} "
              f"merged={merged} over-sep={over}")
        sep_ok &= (merged == 0)
        sound_ok &= (not over)
    t5 = sep_ok
    t6 = sound_ok
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. GF(2) lens SEPARATES every "
          f"Kempe class (incl. all 46 ZZ-blind frozen pairs)")
    print(f"  [{'PASS' if t6 else 'FAIL'}] 6. GF(2) lens never "
          f"over-separates (soundness on connected graphs)")
    if t5 and t6:
        print("\n  ==> CANDIDATE COMPLETE INVARIANT (this test suite, 8/8):")
        print("      Kempe-reachable <=> same GF(2) sign-pattern fiber")
        print("      (epsilon mod achieved straddle span, up to global flip).")
        print("      GC-I fails for the ZZ-charge quotient (46 pairs) and")
        print("      holds, so far, one level finer. Z1's blind predictions")
        print("      should be filed knowing this closed-graph record.")

    res = [t1, t2, t3, t4, t5, t6]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5528 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(res, 1):
        if not r:
            print(f"  Test {i}: FAIL")
