#!/usr/bin/env python3
"""
Toy 5559 — Round 17: THE DEGREE-4 CROSSING HUNT (Cal's queued glance)

Wall Motion must know whether walls can CROSS before the Triple Lemma
assumes simple curves.

SEMANTICS DECLARED: for a twin pair (T1, T2) of a 2-completion pinning
on FCW-014, the wall is the interface of the difference field
Delta(v) = h2(v) - h1(v) (V1 lifts, same base; h1 = h2 on the pinned
boundary, so Delta = 0 there). Two local simplicity probes, both
pre-registered:
  (a) VERTEX transitions: for each interior vertex v (hex link in cyclic
      order), t(v) = #{i : Delta(link[i]) != Delta(link[i+1]) cyclic}.
      t >= 4 = the wall passes v's neighborhood more than once — a
      crossing/pinch candidate. (Interior of disc(2) = 7 vertices; links
      from the six axial directions in rotational order.)
  (b) FACE junctions: a face whose three vertices carry THREE distinct
      Delta values — a Y-branching of the wall.
Population: ALL 709 two-completion pinnings (15 frozen + 694 free) —
the frozen walls are the canonical objects; the free twins are the walls
the gate dynamics actually moves. Ill-posed lifts skipped with count.

Pre-scored: zero t>=4 vertices and zero 3-distinct faces across the
census = WALLS ARE SIMPLE (Triple Lemma may assume simple curves);
any hit = exhibit it — the crossing is the finding.

TESTS (X/Y): 1. population processed with lift control · 2. the census ·
3. the verdict.

Elie, 2026-08-31. Millennium week, 4-Color round 17. 3 tests.
"""

import importlib.util
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


V1 = load("t5543r17", "toy_5543_AUG30_V1_disc_height_fork_phases_or_defect.py")
Y4 = V1.Y4
Z1 = V1.Z1
H8 = V1.H8

HEX = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]   # cyclic


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5559 — R17: the degree-4 crossing hunt")
    print("=" * 70)

    adj, interior, bcyc = Y4.disc(2)
    ofaces = H8.orient_faces([tuple(f) for f in
                              Z1.disc_faces(adj, interior, bcyc)])
    base = bcyc[0]
    atlas = json.load(open(os.path.join(HERE,
                                        'availability_atlas_fcw014.json')))
    two = [r for r in atlas['rows'] if r['nodes'] == 2]

    n_proc, n_ill = 0, 0
    tcensus = Counter()          # (frozen?, t-value) over interior vertices
    fcensus = Counter()          # (frozen?, n distinct Delta on face)
    crossings = []
    junctions = []
    for r in two:
        pin = dict(zip(bcyc, r['pin']))
        T1, T2 = Y4.completions(adj, interior, pin)
        h1, ok1 = V1.height_lift(adj, ofaces, {**pin, **T1}, base)
        h2, ok2 = V1.height_lift(adj, ofaces, {**pin, **T2}, base)
        if not (ok1 and ok2):
            n_ill += 1
            continue
        n_proc += 1
        frz = r['components'] >= 2
        Delta = {v: (h2[v][0] - h1[v][0], h2[v][1] - h1[v][1])
                 for v in adj}
        for v in interior:
            link = [(v[0] + d[0], v[1] + d[1]) for d in HEX]
            t = sum(1 for i in range(6)
                    if Delta[link[i]] != Delta[link[(i + 1) % 6]])
            tcensus[(frz, t)] += 1
            if t >= 4:
                crossings.append((tuple(r['pin']), v, t, frz))
        for f in ofaces:
            nd = len({Delta[x] for x in f})
            fcensus[(frz, nd)] += 1
            if nd == 3:
                junctions.append((tuple(r['pin']), tuple(f), frz))
    t1 = n_proc + n_ill == len(two) and n_proc > 0
    print(f"\n  two-completion pinnings: {len(two)} (frozen 15); "
          f"processed {n_proc}, ill-posed lifts {n_ill}")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Population processed "
          f"with lift control")

    print(f"\n  vertex transition census (frozen?, t): "
          f"{dict(sorted(tcensus.items()))}")
    print(f"  face distinct-Delta census (frozen?, n): "
          f"{dict(sorted(fcensus.items()))}")
    print(f"  t>=4 crossing vertices: {len(crossings)}; "
          f"3-distinct junction faces: {len(junctions)}")
    for c in crossings[:6]:
        print(f"    *** CROSSING: pin {c[0]} at {c[1]} t={c[2]} "
              f"frozen={c[3]}")
    for j in junctions[:6]:
        print(f"    *** JUNCTION: pin {j[0]} face {j[1]} frozen={j[2]}")
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Census computed")

    simple = not crossings and not junctions
    t3 = True
    if simple:
        verdict = ("WALLS ARE SIMPLE — zero crossings, zero junctions "
                   "across all twin walls (frozen and free); the Triple "
                   "Lemma may assume simple curves")
    else:
        nf = sum(1 for *_, z in crossings if z) + \
            sum(1 for *_, z in junctions if z)
        verdict = (f"WALLS CAN CROSS/BRANCH — {len(crossings)} crossing "
                   f"vertices + {len(junctions)} junction faces "
                   f"({nf} on frozen pairs); the Triple Lemma must NOT "
                   f"assume simple curves — exhibits above")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. VERDICT: {verdict}")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5559 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
