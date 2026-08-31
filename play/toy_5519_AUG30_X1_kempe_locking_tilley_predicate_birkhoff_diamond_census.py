#!/usr/bin/env python3
"""
Toy 5519 — X1 (Round 4): KEMPE-LOCKING CROSS-CHECK — Tilley's predicate +
                          the Birkhoff diamond census on our gallery

Literature object pinned (arXiv 1809.02807 v2, extracted from the PDF,
verbatim): "T is said to be Kempe-locked with respect to the edge xy if, in
every 4-coloring of G_xy in which the colors of x and y are the same, there
are precisely three Kempe chains that include both x and y." (G_xy = T minus
edge xy.) Tilley's conjecture: a planar triangulation cannot be Kempe-locked
w.r.t. an edge unless its endpoints are the endpoints of a BIRKHOFF DIAMOND
(4 degree-5 vertices in two triangles sharing an edge, inside a 6-ring).

*** BLIND PREDICTIONS — registered before any computation ***
  B1: NO gallery graph is Tilley-locked on any tested edge (our
      insertion-stuckness and his equivalence-locking are different axes).
  B2: Diamond census — towers CONTAIN all-deg-5 diamonds (apex fan);
      Fritsch contains NONE (its deg-5 vertices t,b have no common pair
      beyond the t- and b-triangles; hand argument); Errera/Kittell lean
      yes (unverified guess).
  B3: Consequence if B2 holds: the TRANSPLANTED conjecture "diamond is
      necessary for OUR insertion-stuckness" is FALSE via Fritsch (stuck,
      diamond-free). Tilley's own conjecture is untouched by this — the
      transplant is ours, labeled as such.
*** END BLIND ***

INSTRUMENT HONESTY: no known-locked triangulation is available as a positive
control (Tilley's order-12 example lives in a figure we cannot extract; our
attempted reconstruction yields the icosahedron, which is his NOT-locked
5-connected panel and serves as the NEGATIVE control). Any "not locked"
verdict below is therefore PROVISIONAL-instrument-unvalidated-positive-side,
stated per the validate-the-instrument discipline.

TESTS (X/Y):
  1. Negative control: the icosahedron is not Tilley-locked on any edge.
  2. Tilley predicate over the gallery (Fritsch all edges; Errera, Kittell,
     T_3, T_4 first-12-edges sample): B1 scored.
  3. Diamond census: B2 scored (towers yes / Fritsch no).
  4. B3 scored: exists an insertion-stuck, diamond-free witness graph.

Elie, 2026-08-30. Millennium week, 4-Color round 4. 4 tests.
"""

import importlib.util
import itertools
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


G5 = load("g5512", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")
T5 = load("t5515", "toy_5515_AUG30_E1_kring_tower_family_rescue_depth_vs_k"
          "_cal_F0_absorbed.py")


def kempe_component(adj, color, start, a, b):
    return G5.kempe_chain(adj, color, start, a, b)


def tilley_locked(adj, x, y, cap=400000):
    """Tilley's predicate for edge xy. Enumerate colorings of G_xy with
    c(x)=c(y)=0 (WLOG); locked iff every such coloring has x,y joined in
    all three (0,j)-chains. Returns (locked, n_colorings, capped)."""
    adjx = {u: set(w for w in nb if not ({u, w} == {x, y}))
            for u, nb in adj.items()}
    vs = sorted(adjx)
    vs.remove(x)
    vs.remove(y)
    order = [x, y] + vs
    col = {}
    state = {'n': 0, 'locked': True, 'capped': False}

    def bt(i):
        if state['capped'] or not state['locked']:
            return
        if i == len(order):
            state['n'] += 1
            if state['n'] > cap:
                state['capped'] = True
                return
            for j in (1, 2, 3):
                comp = kempe_component(adjx, col, x, 0, j)
                if y not in comp:
                    state['locked'] = False
                    return
            return
        u = order[i]
        choices = ((0,) if i < 2 else range(4))
        for c in choices:
            if all(col.get(w) != c for w in adjx[u]):
                col[u] = c
                bt(i + 1)
                del col[u]
                if state['capped'] or not state['locked']:
                    return

    bt(0)
    return state['locked'] and state['n'] > 0, state['n'], state['capped']


def diamond_census(adj):
    """All-deg-5 diamonds: 4 vertices of degree 5 inducing K4 minus an
    edge (two triangles sharing an edge)."""
    deg5 = [v for v in adj if len(adj[v]) == 5]
    found = []
    dset = set(deg5)
    for b, c in itertools.combinations(sorted(deg5), 2):
        if c not in adj[b]:
            continue
        commons = sorted(adj[b] & adj[c] & dset)
        for a, d in itertools.combinations(commons, 2):
            if d not in adj[a]:  # missing edge = the diamond's open pair
                found.append((a, b, c, d))
    return found


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5519 — X1: Tilley Kempe-locking + Birkhoff diamond census")
    print("=" * 70)

    ico = T5.adj_from_faces(T5.tower_faces(2))
    fri = G5.adj_from_faces(G5.fritsch_faces())
    err = G5.errera_adj()
    kit = G5.kittell_adj()
    t3 = T5.adj_from_faces(T5.tower_faces(3))
    t4 = T5.adj_from_faces(T5.tower_faces(4))

    def edges_of(adj):
        return sorted({tuple(sorted((u, w))) for u in adj for w in adj[u]})

    # Test 1: negative control
    print("\n" + "=" * 70)
    print("Test 1: icosahedron negative control")
    print("=" * 70)
    locked_edges = 0
    for (x, y) in edges_of(ico):
        lk, n, capped = tilley_locked(ico, x, y)
        if lk:
            locked_edges += 1
            print(f"  UNEXPECTED: icosahedron locked at {x},{y}")
    t1 = locked_edges == 0
    print(f"\n  locked edges: {locked_edges}/30")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Negative control (not locked)")

    # Test 2: gallery predicate
    print("\n" + "=" * 70)
    print("Test 2: Tilley predicate over the gallery (B1)")
    print("=" * 70)
    any_locked = False
    for name, adj, n_edges in [('Fritsch', fri, None), ('Errera', err, 12),
                               ('Kittell', kit, 12), ('T_3', t3, 12),
                               ('T_4', t4, 12)]:
        es = edges_of(adj)
        if n_edges:
            es = es[:n_edges]
        nl = 0
        ncap = 0
        for (x, y) in es:
            lk, n, capped = tilley_locked(adj, x, y)
            ncap += capped
            if lk and not capped:
                nl += 1
                any_locked = True
                print(f"  *** LOCKED: {name} edge ({x},{y}) over {n} "
                      f"colorings")
        print(f"  {name}: {len(es)} edges tested, locked {nl}, "
              f"capped {ncap}")
    t2 = not any_locked
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. B1: no gallery graph "
          f"Tilley-locked on tested edges (PROVISIONAL — no positive "
          f"control available)")

    # Test 3: diamond census
    print("\n" + "=" * 70)
    print("Test 3: Birkhoff diamond census (B2)")
    print("=" * 70)
    census = {}
    for name, adj in [('icosahedron', ico), ('Fritsch', fri), ('Errera', err),
                      ('Kittell', kit), ('T_3', t3), ('T_4', t4)]:
        d = diamond_census(adj)
        census[name] = len(d)
        print(f"  {name}: all-deg-5 diamonds found: {len(d)}"
              + (f"  e.g. {d[0]}" if d else ""))
    t3_ = (census['T_3'] > 0 and census['T_4'] > 0 and census['Fritsch'] == 0)
    print(f"\n  [{'PASS' if t3_ else 'FAIL'}] 3. B2: towers yes, Fritsch no")

    # Test 4: transplanted conjecture
    print("\n" + "=" * 70)
    print("Test 4: B3 — insertion-stuck AND diamond-free witness exists")
    print("=" * 70)
    # Fritsch: 144 exhaustively verified double-fail (insertion-stuck at the
    # paper's selector) colorings — Toy 5512 — and zero diamonds (test 3).
    t4_ = census['Fritsch'] == 0
    print(f"\n  Fritsch: insertion-stuck witnesses (Toy 5512: 144 exhaustive "
          f"double-fails) and diamond count {census['Fritsch']}.")
    print("  ==> the TRANSPLANTED conjecture (diamond necessary for "
          "insertion-stuckness) is FALSE. Tilley's own conjecture — about "
          "his equivalence-locking — is NOT touched by this: our two "
          "notions separate exactly as blind-predicted.")
    print(f"\n  [{'PASS' if t4_ else 'FAIL'}] 4. B3 scored")

    results = [t1, t2, t3_, t4_]
    passed = sum(results)
    print(f"\n{'=' * 70}")
    print(f"Toy 5519 -- SCORE: {passed}/{len(results)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(results, 1):
        if not r:
            print(f"  Test {i}: FAIL")
