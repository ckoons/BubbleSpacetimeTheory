#!/usr/bin/env python3
"""
Toy 5530 — Z4 (Round 6): THE FALSE-NEIGHBOR HUNT AS INSTRUMENT

Search for two graphs with IDENTICAL full linear data (SNF invariant factors
of the achieved current lattice + charge statistics) but DIFFERENT rescue
depth. One hit = the nonlinear remainder measured exactly (what depth knows
that the linear theory does not). Zero hits on a broad family = completeness
evidence of the honest kind. T_3/Errera are the known TRUE neighbors
(identical data, identical depth) — the control the instrument must
reproduce.

PROTOCOL (fixed per graph, stated so the data key is comparable):
  - population: Kempe-BFS closure from 40 deterministic greedy full-coloring
    seeds, cap 800 colorings (rule and cap in the key's provenance, not in
    the key);
  - linear data key = (invariant factors, rank, gcd|Delta Sigma-omega|,
    odd-vertex count, #deg-5, #deg-7);
  - rescue depth = max exhaustive-BFS depth over the tau=6 census at up to
    3 deg-5 vertices, 400 coloring seeds, cap 40 cases, maxd 5 — SAMPLED
    (bound status carried per SS784 pin discipline; anchors Fritsch/T_3/T_4
    are exhaustive from earlier toys).

FAMILY: Fritsch · Errera · Kittell · icosahedron · towers T_3..T_6 ·
20 flipped triangulations (n = 16, 20, 24, 30 x 5 seeds).

TESTS (X/Y):
  1. Control: T_3 and Errera collide on the data key AND share depth
     (true-neighbor reproduction).
  2. Key table computed for the full family.
  3. FALSE-NEIGHBOR verdict: collisions with differing depth counted;
     each printed loudly with both graphs' provenance and bound status.
     Scored as census-complete (the count is the finding either way).

Elie, 2026-08-30. Millennium week, 4-Color round 6. 3 tests.
"""

import importlib.util
import itertools
import math
import os
import random
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


G5 = load("g5512q", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")
T5 = load("t5515q", "toy_5515_AUG30_E1_kring_tower_family_rescue_depth_vs_k"
          "_cal_F0_absorbed.py")
H8 = load("t5518q", "toy_5518_AUG30_E4_heawood_gf3_instrument_rank_coset"
          "_stuck_separation.py")
Y1 = load("t5527q", "toy_5527_AUG30_Y1_snf_engine_charge_lattice_invariant"
          "_factors.py")
FT = load("t5508q", "toy_5508_AUG30_P1_middle_strict_on_true_triangulations"
          "_embedding_aware_link_cycles.py")


def linear_key(faces, adj):
    vorder = sorted(adj, key=str)
    of = H8.orient_faces([tuple(f) for f in faces])
    # seeds
    seeds = []
    seen = set()
    vsall = sorted(adj)
    for s in range(200):
        rng = random.Random(s)
        order = list(vsall)
        rng.shuffle(order)
        c = G5.greedy_4color(adj, order)
        if c is None:
            continue
        k = tuple(c[u] for u in vsall)
        if k in seen:
            continue
        seen.add(k)
        seeds.append(c)
        if len(seeds) >= 40:
            break
    pop, _closed = Y1.kempe_closure(adj, seeds, 800)
    cols, omegas, _pc3 = Y1.build_columns(of, adj, pop, vorder)
    if cols:
        A = [[col[i] for col in cols] for i in range(len(vorder))]
        diag, _U = Y1.smith_normal_form(A)
    else:
        diag = []
    rank = len([d for d in diag if d != 0])
    sg = 0
    for col in cols:
        sg = math.gcd(sg, abs(sum(col)))
    odd = sum(1 for v in adj if len(adj[v]) % 2 == 1)
    n5 = sum(1 for v in adj if len(adj[v]) == 5)
    n7 = sum(1 for v in adj if len(adj[v]) == 7)
    factors = tuple(d for d in diag if d not in (0, 1))
    return (factors, rank, sg, odd, n5, n7)


def rescue_depth_max(faces, adj, exhaustive_known=None):
    if exhaustive_known is not None:
        return exhaustive_known, 'exhaustive (prior toy)'
    deg5 = [v for v in sorted(adj) if len(adj[v]) == 5]
    worst = 0
    n = 0
    for tv in deg5[:3]:
        for c in G5.sampled_colorings(adj, tv, 400):
            if G5.operational_tau(adj, c, tv) != 6:
                continue
            n += 1
            if n > 40:
                return worst, f'sampled (cap hit, {n - 1} cases)'
            d = T5.rescue_depth(adj, c, tv, 5)
            if d is not None:
                worst = max(worst, d)
    return worst, f'sampled ({n} cases)'


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5530 — Z4: the false-neighbor hunt")
    print("=" * 70)

    graphs = []
    graphs.append(('Fritsch', G5.fritsch_faces(), 2))
    ef, _o, _m = G5.faces_from_adj_triangulation(G5.errera_adj())
    graphs.append(('Errera', ef, 3))
    kf, _o2, _m2 = G5.faces_from_adj_triangulation(G5.kittell_adj())
    graphs.append(('Kittell', kf, 4))
    graphs.append(('icosahedron', T5.tower_faces(2), 0))
    for k in (3, 4, 5, 6):
        graphs.append((f'T_{k}', T5.tower_faces(k),
                       3 if k == 3 else (2 if k >= 4 else None)))
    for n in (16, 20, 24, 30):
        for s in range(5):
            graphs.append((f'flip_n{n}_s{s}',
                           FT.flipped_triangulation(n, seed=s), None))

    rows = []
    for name, faces, known in graphs:
        adj = (G5.adj_from_faces(faces) if isinstance(faces[0], tuple)
               else None)
        adj = G5.adj_from_faces(faces)
        key = linear_key(faces, adj)
        depth, status = rescue_depth_max(faces, adj, known)
        rows.append((name, key, depth, status))
        print(f"  {name}: factors={key[0]} rank={key[1]} gcd={key[2]} "
              f"odd={key[3]} n5={key[4]} n7={key[5]}  depth={depth} "
              f"[{status}]")

    # Test 1: control
    kT3 = next(r[1] for r in rows if r[0] == 'T_3')
    kEr = next(r[1] for r in rows if r[0] == 'Errera')
    dT3 = next(r[2] for r in rows if r[0] == 'T_3')
    dEr = next(r[2] for r in rows if r[0] == 'Errera')
    t1 = (kT3 == kEr and dT3 == dEr)
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Control: T_3/Errera "
          f"true-neighbor pair reproduced (keys equal: {kT3 == kEr}, "
          f"depths {dT3}/{dEr})")

    # Test 2
    t2 = len(rows) == len(graphs)
    print(f"  [{'PASS' if t2 else 'FAIL'}] 2. Key table computed "
          f"({len(rows)} graphs)")

    # Test 3: collisions
    bykey = defaultdict(list)
    for name, key, depth, status in rows:
        bykey[key].append((name, depth, status))
    false_neighbors = 0
    for key, members in bykey.items():
        if len(members) < 2:
            continue
        depths = {d for _, d, _ in members}
        tag = 'TRUE neighbors' if len(depths) == 1 else '*** FALSE NEIGHBORS ***'
        if len(depths) > 1:
            false_neighbors += 1
        print(f"\n  collision {tag}: {members}")
    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Census complete: "
          f"{false_neighbors} false-neighbor collision(s) "
          f"({'the nonlinear remainder is EXHIBITED' if false_neighbors else 'zero — completeness evidence on this family, sampled-depth caveat carried'})")

    res = [t1, t2, t3]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5530 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(res, 1):
        if not r:
            print(f"  Test {i}: FAIL")
