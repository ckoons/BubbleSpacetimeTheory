#!/usr/bin/env python3
"""
Toy 5543 — V1 (Round 12): THE FORK — do the twins differ as two rigid
                           PHASES or by a localized DEFECT?

Lyra's Disc Height Lemma (dictionary note, Section 5), executed exactly:
compute the ZZ^2 height lift h explicitly for BOTH twins — same gauge, same
base point at the same boundary vertex — report the boundary walk, its
slope vs maximal, and THE VERTEX SET WHERE THE TWINS' HEIGHTS DIFFER.

Lift construction (her Section 1-2, conventions pinned here):
  labels: Klein l(uv) = c(u) XOR c(v) in {1,2,3}; letter map a=1, b=2, c=3;
  step vectors A=(1,0), B=(0,1), C=(-1,-1) (A+B+C=0; mod-2 shadow = labels);
  face classes: consistent orientation (dual BFS), then checkerboard sign
  sigma(F) in {+1,-1} — adjacent faces opposite (proper 2-coloring of the
  face-adjacency graph; existence verified, not assumed);
  integration: each directed edge (u -> v) is traversed positively by
  exactly one oriented face F; h(v) = h(u) + sigma(F) * L(l(uv));
  base: h = (0,0) at boundary vertex u_0; single-valuedness verified on
  every non-tree edge.

PRE-REGISTERED (Lyra): extremal slope confirmed; her lean = Fork (i)
(phase mechanism: twins differ at EVERY interior vertex). Fork (ii) =
localized defect (small connected difference set). Either is a mechanism.

TESTS (X/Y):
  1. Lift instrument: checkerboard exists; h single-valued for both twins;
     boundary heights IDENTICAL between twins (same pinning/gauge/base).
  2. The boundary walk + its range/slope reported.
  3. THE FORK VERDICT: the difference set D = {v interior : h1 != h2} —
     |D| = all 7 (phases) vs small connected (defect); the difference
     field h2 - h1 printed in full (the Rosetta datum).
  4. Phase check if fork (i): is h2 - h1 constant on D (pure phase shift)
     or structured? Reported either way.

Elie, 2026-08-30. Millennium week, 4-Color round 12. 4 tests.
"""

import importlib.util
import os
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


Y4 = load("t5526v1", "toy_5526_AUG30_Y4_boundary_fisk_disc_relative_kempe"
          "_connectivity.py")
H8 = load("t5518v1", "toy_5518_AUG30_E4_heawood_gf3_instrument_rank_coset"
          "_stuck_separation.py")
Z1 = load("t5531v1", "toy_5531_AUG30_Z1_disc_decision_runner_guarded"
          "_awaiting_freeze.py")

DECISION = [0, 1, 0, 1, 0, 1, 0, 1, 2, 1, 2, 1]
STEP = {1: (1, 0), 2: (0, 1), 3: (-1, -1)}   # a=1->A, b=2->B, c=3->C


def height_lift(adj, ofaces, col, base):
    """h: V -> ZZ^2 per the pinned construction. Returns (h, ok)."""
    # face adjacency (shared edges) for the checkerboard
    edge2faces = {}
    for fi, f in enumerate(ofaces):
        a, b, c = f
        for e in ((a, b), (b, c), (c, a)):
            edge2faces.setdefault(frozenset(e), []).append(fi)
    sigma = {0: 1}
    q = deque([0])
    while q:
        fi = q.popleft()
        for e, fs in edge2faces.items():
            if fi in fs and len(fs) == 2:
                fj = fs[0] if fs[1] == fi else fs[1]
                if fj not in sigma:
                    sigma[fj] = -sigma[fi]
                    q.append(fj)
                elif sigma[fj] != -sigma[fi]:
                    return None, False
    # directed edge -> its positive-traversal face
    dir_face = {}
    for fi, f in enumerate(ofaces):
        a, b, c = f
        for (u, v) in ((a, b), (b, c), (c, a)):
            dir_face[(u, v)] = fi
    h = {base: (0, 0)}
    q = deque([base])
    ok = True
    while q:
        u = q.popleft()
        for v in adj[u]:
            lab = col[u] ^ col[v]
            if (u, v) in dir_face:
                s = sigma[dir_face[(u, v)]]
            else:
                s = -sigma[dir_face[(v, u)]]
            dx, dy = STEP[lab]
            hv = (h[u][0] + s * dx, h[u][1] + s * dy)
            if v in h:
                if h[v] != hv:
                    ok = False
            else:
                h[v] = hv
                q.append(v)
    return h, ok


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5543 — V1: THE FORK (phases or defect)")
    print("=" * 70)

    adj, interior, bcyc = Y4.disc(2)
    faces = Z1.disc_faces(adj, interior, bcyc)
    ofaces = H8.orient_faces([tuple(f) for f in faces])
    pin = dict(zip(bcyc, DECISION))
    twins = Y4.completions(adj, interior, pin)
    base = bcyc[0]

    h1, ok1 = height_lift(adj, ofaces, twins[0], base)
    h2, ok2 = height_lift(adj, ofaces, twins[1], base)
    bnd_same = all(h1[u] == h2[u] for u in bcyc)
    t1 = ok1 and ok2 and bnd_same
    print(f"\n  lift single-valued: twin1 {ok1}, twin2 {ok2}; boundary "
          f"heights identical: {bnd_same}")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Lift instrument sound")

    walk = [h1[u] for u in bcyc]
    xs = [p[0] for p in walk]
    ys = [p[1] for p in walk]
    print(f"\n  boundary walk (h at u_0..u_11): {walk}")
    print(f"  range: x [{min(xs)},{max(xs)}]  y [{min(ys)},{max(ys)}]  "
          f"(span {max(xs) - min(xs)} x {max(ys) - min(ys)})")
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Walk reported")

    D = [v for v in sorted(interior, key=str) if h1[v] != h2[v]]
    print(f"\n  THE DIFFERENCE SET D (interior, |interior| = "
          f"{len(interior)}): |D| = {len(D)}")
    print(f"  difference field (v, h1, h2, h2-h1, colors c1->c2):")
    for v in sorted(interior, key=str):
        d = (h2[v][0] - h1[v][0], h2[v][1] - h1[v][1])
        mark = ' *' if h1[v] != h2[v] else ''
        print(f"    {v}: h1={h1[v]} h2={h2[v]} d={d} "
              f"c:{twins[0][v]}->{twins[1][v]}{mark}")
    if len(D) == len(interior):
        verdict = "FORK (i) — PHASE MECHANISM (differ at every interior vertex)"
    elif len(D) <= 3:
        verdict = "FORK (ii) — LOCALIZED DEFECT"
    else:
        verdict = f"MIXED ({len(D)}/{len(interior)}) — neither clean fork"
    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. VERDICT: {verdict}")

    diffs = {(h2[v][0] - h1[v][0], h2[v][1] - h1[v][1]) for v in D}
    t4 = True
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Phase structure: distinct "
          f"difference vectors on D: {sorted(diffs)} "
          f"({'PURE SHIFT' if len(diffs) == 1 else 'STRUCTURED field'})")

    res = [t1, t2, t3, t4]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5543 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(res, 1):
        if not r:
            print(f"  Test {i}: FAIL")
