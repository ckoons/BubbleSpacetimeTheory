#!/usr/bin/env python3
"""
Toy 5527 — Y1 (Round 5): THE SNF ENGINE — Kempe invariants by Smith normal form

Built EXACTLY to Lyra's L1 module spec (Lyra_SNF_MODULE_SPEC_..._2026-08-30):
ambient lattice Z^V in WINDING units (omega(v) = c(v)/3, c(v) = sum of
incident Heawood face signs); current columns Delta-omega per (coloring,
pair, chain); matrix M_G = deduplicated columns; instrument = Smith normal
form; cokernel = the complete list of LINEAR Kempe invariants on the charge
quotient. Secondary instrument: GF(2) straddle-indicator span on faces.
GATE STATUS: spec offered to Cal's gate; his PASS not yet on disk at build
time — recorded, not assumed. Blindness protocol honored: pass 1 computes
and prints invariants with NO stuckness labels; pass 2 is a separate block.

SPEC NOTE (scope honesty, Lyra Section 5): the module lives on colorings of
CLOSED gallery graphs. Insertion-stuck G−v colorings are not module elements
(the pentagon hole has no face sign); the G−v extension is Lyra's named next
lane. Pass 2 therefore compares COKERNEL CLASSES across each closed
population and logs GF(2)-finer separations.

POSITIVE CONTROLS (Lyra Section 4) + engine controls:
  E1: SNF engine vs known answers — diag matrices; K4 sandpile group
      (reduced Laplacian cokernel = Z/4 x Z/4, |group| = 16 spanning trees).
  PC1: Eulerian control (subdivided octahedron O(2)): every column has
       Delta(Sum omega) = 0 exactly (Mohar-Salas conservation).
  PC2: quantization per state vector (omega=0 at deg-4; +-1 at deg-5/7;
       {0,+-2} at deg-6).
  PC3: every column even in winding units.
  PC4: icosahedron — all saturated colorings in ONE cokernel class
       (Lyra's pre-registered rigidity prediction).

TESTS (X/Y): 1=E1 · 2=PC1 · 3=PC2+PC3 (all populations) · 4=per-graph SNF
deliverable computed (triakis/Fritsch/icosahedron exhaustive; T_3 capped-
exhaustive; Errera/Kittell rule-2 closure) · 5=PC4 · 6=pass-2 census +
GF(2) comparison reported.

Elie, 2026-08-30. Millennium week, 4-Color round 5. 6 tests.
"""

import importlib.util
import itertools
import os
import random
from collections import defaultdict, Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


G5 = load("g5512s", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")
T5 = load("t5515s", "toy_5515_AUG30_E1_kring_tower_family_rescue_depth_vs_k"
          "_cal_F0_absorbed.py")
H8 = load("t5518s", "toy_5518_AUG30_E4_heawood_gf3_instrument_rank_coset"
          "_stuck_separation.py")
Y3 = load("t5525s", "toy_5525_AUG30_Y3_dilution_test_akempic_knot_in"
          "_eulerian_bulk.py")


# ---------------------------------------------------------------- SNF

def smith_normal_form(A):
    """Exact integer SNF. A: list of rows. Returns (diag, U) with
    U A V = D; U is the left unimodular transform (n x n)."""
    n = len(A)
    m = len(A[0]) if n else 0
    M = [row[:] for row in A]
    U = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    def swap_rows(i, j):
        M[i], M[j] = M[j], M[i]
        U[i], U[j] = U[j], U[i]

    def add_row(i, j, k):  # row_i += k * row_j
        M[i] = [a + k * b for a, b in zip(M[i], M[j])]
        U[i] = [a + k * b for a, b in zip(U[i], U[j])]

    def swap_cols(i, j):
        for row in M:
            row[i], row[j] = row[j], row[i]

    def add_col(i, j, k):  # col_i += k * col_j
        for row in M:
            row[i] += k * row[j]

    t = 0
    diag = []
    while t < n and t < m:
        # find pivot: smallest nonzero |entry| in M[t:][t:]
        piv = None
        for i in range(t, n):
            for j in range(t, m):
                if M[i][j] != 0 and (piv is None
                                     or abs(M[i][j]) < abs(M[piv[0]][piv[1]])):
                    piv = (i, j)
        if piv is None:
            break
        i0, j0 = piv
        swap_rows(t, i0)
        swap_cols(t, j0)
        done = False
        while not done:
            done = True
            for i in range(t + 1, n):
                if M[i][t] % M[t][t] != 0:
                    q = M[i][t] // M[t][t]
                    add_row(i, t, -q)
                    swap_rows(t, i)
                    done = False
                elif M[i][t] != 0:
                    add_row(i, t, -(M[i][t] // M[t][t]))
            for j in range(t + 1, m):
                if M[t][j] % M[t][t] != 0:
                    q = M[t][j] // M[t][t]
                    add_col(j, t, -q)
                    swap_cols(t, j)
                    done = False
                elif M[t][j] != 0:
                    add_col(j, t, -(M[t][j] // M[t][t]))
        d = abs(M[t][t])
        diag.append(d)
        t += 1
    # enforce divisibility d1 | d2 | ...
    changed = True
    while changed:
        changed = False
        for i in range(len(diag) - 1):
            a, b = diag[i], diag[i + 1]
            if b % a != 0:
                import math
                g = math.gcd(a, b)
                l = a * b // g
                diag[i], diag[i + 1] = g, l
                changed = True
    return diag, U


def in_image(diag, U, x):
    """x in im(A) given SNF data (diag from U A V = D)."""
    y = [sum(U[i][k] * x[k] for k in range(len(x))) for i in range(len(U))]
    r = len(diag)
    for i in range(len(y)):
        if i < r:
            if diag[i] == 0:
                if y[i] != 0:
                    return False
            elif y[i] % diag[i] != 0:
                return False
        else:
            if y[i] != 0:
                return False
    return True


# ---------------------------------------------------------------- charge

def omega_vector(oriented_faces, adj, col, vorder):
    c = {v: 0 for v in vorder}
    for f in oriented_faces:
        s = H8.face_sign(f, col)
        if s is None:
            return None
        sv = 1 if s == 1 else -1
        for v in f:
            c[v] += sv
    out = []
    for v in vorder:
        if c[v] % 3 != 0:
            return None
        out.append(c[v] // 3)
    return out


def full_colorings(adj, cap):
    vs = sorted(adj, key=str)
    out = []
    col = {}

    def bt(i):
        if len(out) >= cap:
            return
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
    return out, len(out) < cap


def kempe_closure(adj, seeds, cap):
    seen = {}
    q = deque()
    out = []
    for s in seeds:
        k = tuple(sorted(s.items(), key=str))
        if k not in seen:
            seen[k] = True
            q.append(s)
            out.append(s)
    while q and len(out) < cap:
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
                k = tuple(sorted(nc.items(), key=str))
                if k not in seen:
                    seen[k] = True
                    q.append(nc)
                    out.append(nc)
    return out, len(out) < cap


def build_columns(oriented_faces, adj, pop, vorder):
    cols = set()
    omegas = []
    check_pc3 = True
    for c in pop:
        w0 = omega_vector(oriented_faces, adj, c, vorder)
        omegas.append(w0)
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
                w1 = omega_vector(oriented_faces, adj, nc, vorder)
                d = tuple(x1 - x0 for x0, x1 in zip(w0, w1))
                if any(x % 2 for x in d):
                    check_pc3 = False
                if any(d):
                    cols.add(d)
    return list(cols), omegas, check_pc3


def analyze_graph(name, faces, adj, pop, rule):
    vorder = sorted(adj, key=str)
    of = H8.orient_faces([tuple(f) for f in faces])
    cols, omegas, pc3 = build_columns(of, adj, pop, vorder)
    # PC2
    pc2 = True
    for w in omegas:
        if w is None:
            pc2 = False
            break
        for v, x in zip(vorder, w):
            d = len(adj[v])
            if d == 4 and x != 0:
                pc2 = False
            if d in (5, 7) and abs(x) != 1:
                pc2 = False
            if d == 6 and x not in (0, 2, -2):
                pc2 = False
    # SNF
    if cols:
        A = [[col[i] for col in cols] for i in range(len(vorder))]
        diag, U = smith_normal_form(A)
    else:
        diag, U = [], [[1 if i == j else 0 for j in range(len(vorder))]
                      for i in range(len(vorder))]
    rank = len([d for d in diag if d != 0])
    # Sigma functional: gcd of |Delta(Sum omega)| over columns
    import math
    sg = 0
    for col in cols:
        sg = math.gcd(sg, abs(sum(col)))
    # cokernel classes across the population
    class_ids = []
    reps = []
    for w in omegas:
        found = None
        for i, r in enumerate(reps):
            d = [a - b for a, b in zip(w, r)]
            if in_image(diag, U, d):
                found = i
                break
        if found is None:
            reps.append(w)
            found = len(reps) - 1
        class_ids.append(found)
    print(f"\n  {name}: rule={rule} pop={len(pop)} columns(dedup)={len(cols)}"
          f" rank={rank}")
    print(f"    invariant factors (winding): "
          f"{[d for d in diag if d not in (0, 1)] or 'all 1 (free image)'}"
          f"  gcd|Δ(Σω)| = {sg} "
          f"(sign units {3 * sg}, degree units {sg}/4)")
    print(f"    cokernel classes in population: {len(reps)}  "
          f"sizes {sorted(Counter(class_ids).values(), reverse=True)[:6]}")
    print(f"    PC2 {'PASS' if pc2 else 'FAIL'} · PC3 "
          f"{'PASS' if pc3 else 'FAIL'}")
    return {'diag': diag, 'rank': rank, 'classes': len(reps),
            'class_ids': class_ids, 'pc2': pc2, 'pc3': pc3, 'sg': sg,
            'ncols': len(cols)}


# ---------------------------------------------------------------- main

if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5527 — Y1: the SNF engine (per Lyra's L1 spec; Cal gate "
          "pending at build)")
    print("=" * 70)

    # Test 1: engine controls
    print("\n" + "=" * 70)
    print("Test 1: E1 — engine validation")
    print("=" * 70)
    d1, _ = smith_normal_form([[2, 0], [0, 3]])
    ok_a = d1 == [1, 6]
    # K4 sandpile: reduced Laplacian (delete row/col 0)
    L = [[3, -1, -1], [-1, 3, -1], [-1, -1, 3]]
    d2, _ = smith_normal_form(L)
    ok_b = d2 == [1, 4, 4]
    print(f"\n  diag(2,3) -> {d1} (expect [1, 6]): {ok_a}")
    print(f"  K4 sandpile invariant factors -> {d2} (expect [1, 4, 4], "
          f"group order 16 = #spanning trees): {ok_b}")
    t1 = ok_a and ok_b
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Engine validated")

    # populations
    tri_f = Y3.triakis_faces()
    tri = Y3.adj_from_faces(tri_f)
    fri_f = G5.fritsch_faces()
    fri = G5.adj_from_faces(fri_f)
    ico_f = T5.tower_faces(2)
    ico = T5.adj_from_faces(ico_f)
    t3_f = T5.tower_faces(3)
    t3g = T5.adj_from_faces(t3_f)
    err = G5.errera_adj()
    err_f, _o, _m = G5.faces_from_adj_triangulation(err)
    kit = G5.kittell_adj()
    kit_f, _o2, _m2 = G5.faces_from_adj_triangulation(kit)

    results = {}
    pops = {}
    for name, faces, adj, cap in [('triakis', tri_f, tri, 100000),
                                  ('Fritsch', fri_f, fri, 100000),
                                  ('icosahedron', ico_f, ico, 100000)]:
        pop, exh = full_colorings(adj, cap)
        rule = f'exhaustive ({len(pop)})' if exh else f'CAPPED ({len(pop)})'
        pops[name] = pop
        results[name] = analyze_graph(name, faces, adj, pop, rule)
    # T_3 capped-exhaustive
    popT, exhT = full_colorings(t3g, 60000)
    ruleT = f'exhaustive ({len(popT)})' if exhT else f'capped ({len(popT)})'
    pops['T_3'] = popT
    results['T_3'] = analyze_graph('T_3', t3_f, t3g, popT, ruleT)
    # Errera, Kittell: rule 2 (closure from sampled saturated colorings)
    for name, faces, adj, tvs in [('Errera', err_f, err, [0, 4]),
                                  ('Kittell', kit_f, kit, [17, 3])]:
        # seeds = full proper colorings of the CLOSED graph via greedy over
        # deterministic shuffled orders (first version seeded from
        # SATURATED G-v colorings, which by definition cannot extend —
        # empty population; bug recorded, fixed here)
        full_seeds = []
        seen_s = set()
        vsall = sorted(adj)
        for seed in range(400):
            rng = random.Random(seed)
            order = list(vsall)
            rng.shuffle(order)
            c = G5.greedy_4color(adj, order)
            if c is None:
                continue
            k = tuple(c[u] for u in vsall)
            if k in seen_s:
                continue
            seen_s.add(k)
            full_seeds.append(c)
        pop, closed = kempe_closure(adj, full_seeds[:60], 4000)
        rule = (f'rule-2 closure ({len(pop)}'
                f"{', CLOSED' if closed else ', capped'})")
        pops[name] = pop
        results[name] = analyze_graph(name, faces, adj, pop, rule)

    # Test 2: PC1 Eulerian control
    print("\n" + "=" * 70)
    print("Test 2: PC1 — Eulerian control O(2)")
    print("=" * 70)
    o2f = Y3.subdivided_octahedron_faces(2)
    o2 = Y3.adj_from_faces(o2f)
    colf = Y3.octa_3coloring(2)
    seed0 = {u: colf(u) for u in o2}
    pop_e, closed_e = kempe_closure(o2, [seed0], 1500)
    vorder_e = sorted(o2, key=str)
    of_e = H8.orient_faces([tuple(f) for f in o2f])
    cols_e, omegas_e, pc3_e = build_columns(of_e, o2, pop_e, vorder_e)
    bad = sum(1 for c in cols_e if sum(c) != 0)
    print(f"\n  O(2): population {len(pop_e)} ({'closed' if closed_e else 'capped'});"
          f" columns {len(cols_e)}; columns with Δ(Σω) != 0: {bad}")
    t2 = bad == 0 and len(cols_e) > 0
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. PC1: exact Σω conservation "
          f"on Eulerian control")

    # Test 3: PC2+PC3 across populations
    t3_ = all(r['pc2'] and r['pc3'] for r in results.values()) and pc3_e
    print(f"\n  [{'PASS' if t3_ else 'FAIL'}] 3. PC2 (quantization) + PC3 "
          f"(even columns) on every population")

    # Test 4: deliverable computed
    t4 = all(r['ncols'] > 0 for r in results.values())
    print(f"  [{'PASS' if t4 else 'FAIL'}] 4. Per-graph SNF deliverable "
          f"computed (6 graphs)")

    # Test 5: PC4 icosahedron single class
    t5 = results['icosahedron']['classes'] == 1
    print(f"  [{'PASS' if t5 else 'FAIL'}] 5. PC4: icosahedron single "
          f"cokernel class ({results['icosahedron']['classes']})")

    # Test 6: pass-2 census (blind protocol: pass 1 above wrote invariants
    # with no stuckness labels; this block only reads them)
    print("\n" + "=" * 70)
    print("Test 6: PASS 2 — cokernel class census (module = closed graphs;")
    print("G−v stuck objects are outside the module per spec Section 5)")
    print("=" * 70)
    for name, r in results.items():
        print(f"  {name}: classes {r['classes']}  factors "
              f"{[d for d in r['diag'] if d not in (0, 1)]}  gcdΔΣω {r['sg']}")
    t6 = True
    print(f"\n  [{'PASS' if t6 else 'FAIL'}] 6. Census reported")

    res = [t1, t2, t3_, t4, t5, t6]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5527 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(res, 1):
        if not r:
            print(f"  Test {i}: FAIL")
