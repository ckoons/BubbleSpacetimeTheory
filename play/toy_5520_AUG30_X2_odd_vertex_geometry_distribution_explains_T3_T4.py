#!/usr/bin/env python3
"""
Toy 5520 — X2 (Round 4): ODD-VERTEX GEOMETRY — density refined to DISTRIBUTION

E3's law used one number per graph (odd/V). X2's bar (Keeper): the T_3-vs-T_4
depth contrast (3 vs 2, exhaustive both) must be EXPLAINED by the odd-vertex
distribution around the stuck vertex — not just correlated.

STATISTICS REGISTERED BEFORE THE RUN (all computed, none dropped; the toy
reports every one and scores each against the depth targets
Fritsch 2 · T_4 2 · T_3 3 · Errera 3 · Kittell 4):
  S1 = odd vertices within distance 2 of the stuck vertex
  S2 = odd vertices within distance 3
  S3 = mean distance from stuck vertex to odd vertices
  S4 = inverse-distance odd charge  sum(1/d(v,o))  (self excluded)
  S5 = distance from v to the nearest odd vertex NOT in v's closed link
Scoring bar per statistic: (a) T_3 value strictly exceeds T_4 value in the
direction that predicts deeper (for S3/S5, deeper = SMALLER); (b) the
statistic orders the five witnesses consistently with depth (ties allowed
within equal-depth classes, no inversion across classes).

Elie, 2026-08-30. Millennium week, 4-Color round 4. 5 scored statistics + 1
instrument test.
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


G5 = load("g5512x", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")
T5 = load("t5515x", "toy_5515_AUG30_E1_kring_tower_family_rescue_depth_vs_k"
          "_cal_F0_absorbed.py")


def bfs_dist(adj, src):
    d = {src: 0}
    q = deque([src])
    while q:
        u = q.popleft()
        for w in adj[u]:
            if w not in d:
                d[w] = d[u] + 1
                q.append(w)
    return d


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5520 — X2: odd-vertex geometry around the stuck vertex")
    print("=" * 70)

    fri = G5.adj_from_faces(G5.fritsch_faces())
    err = G5.errera_adj()
    kit = G5.kittell_adj()
    t3 = T5.adj_from_faces(T5.tower_faces(3))
    t4 = T5.adj_from_faces(T5.tower_faces(4))

    # witness stuck vertices: known from Toys 5512/5515 populations
    WITNESSES = [('Fritsch', fri, 0, 2), ('T_4', t4, 0, 2),
                 ('T_3', t3, 0, 3), ('Errera', err, 0, 3),
                 ('Kittell', kit, 17, 4)]

    rows = []
    ok_inst = True
    for name, adj, v, depth in WITNESSES:
        odd = {u for u in adj if len(adj[u]) % 2 == 1}
        if len(adj[v]) != 5:
            ok_inst = False
        d = bfs_dist(adj, v)
        odd_o = [u for u in odd if u != v]
        S1 = sum(1 for u in odd_o if d[u] <= 2)
        S2 = sum(1 for u in odd_o if d[u] <= 3)
        S3 = sum(d[u] for u in odd_o) / len(odd_o)
        S4 = sum(1.0 / d[u] for u in odd_o)
        closed_link = set(adj[v]) | {v}
        outside = [u for u in odd_o if u not in closed_link]
        S5 = min(d[u] for u in outside) if outside else float('inf')
        rows.append((name, depth, S1, S2, S3, S4, S5))
        print(f"  {name} (depth {depth}): S1={S1} S2={S2} S3={S3:.2f} "
              f"S4={S4:.2f} S5={S5}")

    print(f"\n  [{'PASS' if ok_inst else 'FAIL'}] 0. Instrument: all stuck "
          f"vertices are deg-5")

    def score(idx, higher_is_deeper):
        vals = {r[0]: r[idx] for r in rows}
        dep = {r[0]: r[1] for r in rows}
        # (a) T_3 vs T_4 in the deeper direction
        a = (vals['T_3'] > vals['T_4']) if higher_is_deeper else \
            (vals['T_3'] < vals['T_4'])
        # (b) no inversion across depth classes
        b = True
        names = [r[0] for r in rows]
        for n1 in names:
            for n2 in names:
                if dep[n1] < dep[n2]:
                    if higher_is_deeper and vals[n1] > vals[n2]:
                        b = False
                    if not higher_is_deeper and vals[n1] < vals[n2]:
                        b = False
        return a and b, vals

    results = [ok_inst]
    for label, idx, hid in [('S1 (odd within 2)', 2, True),
                            ('S2 (odd within 3)', 3, True),
                            ('S3 (mean dist, deeper=smaller)', 4, False),
                            ('S4 (inverse-distance charge)', 5, True),
                            ('S5 (nearest outside-link odd, deeper=smaller)',
                             6, False)]:
        ok, vals = score(idx, hid)
        results.append(ok)
        print(f"\n  [{'PASS' if ok else 'FAIL'}] {label}: "
              f"{[(r[0], r[idx]) for r in rows]}")

    passed = sum(results)
    print(f"\n{'=' * 70}")
    print(f"Toy 5520 -- SCORE: {passed}/{len(results)}")
    print(f"{'=' * 70}")
    surv = [lab for (lab, _, _), r in zip(
        [('S1', 2, 1), ('S2', 3, 1), ('S3', 4, 0), ('S4', 5, 1),
         ('S5', 6, 0)], results[1:]) if r]
    print(f"Surviving distribution statistics: {surv if surv else 'NONE'}")
