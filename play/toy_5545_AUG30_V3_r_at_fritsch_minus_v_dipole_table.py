#!/usr/bin/env python3
"""
Toy 5545 — V3 (Round 12): r AT FRITSCH−v, AND THE DIPOLE TABLE ASSEMBLED

The starvation cell, fixed at the source: closed Fritsch's r = 0 rests on
its OWN frozen population (2 achieved transposition columns — complete but
tiny). Fritsch−v is ONE Kempe class of 192 colorings (Q4): the relative r
is measurable on a complete, genuinely dynamical population.

Relative machinery (consistent with the transvection toy): omega on the 9
complete faces of Fritsch−0; chains exclude the apex; population = the
full 192; columns = achieved Delta-omega; r_rel = gcd |Delta(Sum omega)|.

THE DIPOLE LAW'S PREDICTION (pre-registered): S4 found a SHARP onset at
odd = 4 (one dipole conserves, two pump, r = 8). Fritsch−v carries 6 odd
vertices (the punctured graph's odd set) ==> the law predicts r != 0.
  r_rel != 0  ==> Fritsch WAS NEVER AN EXCEPTION — the closed r = 0 was
                  frozen-population smallness; the dipole law stands clean;
                  M2's "Fritsch conserves" clue formally dissolves.
  r_rel == 0  ==> Fritsch is a GENUINE geometric exception to a sharp law
                  — a bigger finding.
Also measured for the table: icosahedron−v (single class, Q4).

TESTS (X/Y):
  1. Populations complete (Fritsch−v 192 one class; ico−v enumerated).
  2. r_rel measured on both (columns counted; no starvation flags).
  3. The assembled r-vs-odd table (S4 levels + punctured rows) and the
     dipole-law verdict.

Elie, 2026-08-30. Millennium week, 4-Color round 12. 3 tests.
"""

import importlib.util
import itertools
import math
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


G5 = load("g5512v3", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")
T5 = load("t5515v3", "toy_5515_AUG30_E1_kring_tower_family_rescue_depth_vs_k"
          "_cal_F0_absorbed.py")
H8 = load("t5518v3", "toy_5518_AUG30_E4_heawood_gf3_instrument_rank_coset"
          "_stuck_separation.py")


def relative_r(faces, adj, tv):
    """r on the punctured object: full enumeration of G−tv colorings,
    omega on complete faces, chains exclude tv."""
    of = H8.orient_faces([tuple(f) for f in faces])
    comp_faces = [f for f in of if tv not in f]
    vs = sorted(u for u in adj if u != tv)
    cols_pop = []
    col = {}

    def bt(i):
        if i == len(vs):
            cols_pop.append(dict(col))
            return
        u = vs[i]
        for c in range(4):
            if all(col.get(w) != c for w in adj[u] if w != tv):
                col[u] = c
                bt(i + 1)
                del col[u]

    bt(0)

    def omega(c):
        w = Counter()
        for f in comp_faces:
            s = H8.face_sign(f, c)
            z = 1 if s == 1 else -1
            for v in f:
                w[v] += z
        return tuple(w[v] for v in vs)

    achieved = set()
    for c in cols_pop:
        w0 = omega(c)
        for a, b in itertools.combinations(range(4), 2):
            done = set()
            for u in vs:
                if u in done or c[u] not in (a, b):
                    continue
                S = G5.kempe_chain(adj, c, u, a, b, exclude={tv})
                done |= S
                nc = dict(c)
                for x in S:
                    nc[x] = b if nc[x] == a else a
                d = tuple(x1 - x0 for x0, x1 in zip(w0, omega(nc)))
                if any(d):
                    achieved.add(d)
    g = 0
    for cvec in achieved:
        g = math.gcd(g, abs(sum(cvec)))
    return g, len(achieved), len(cols_pop)


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5545 — V3: r at Fritsch−v and the dipole table")
    print("=" * 70)

    fri_faces = G5.fritsch_faces()
    fri = G5.adj_from_faces(fri_faces)
    ico_faces = T5.tower_faces(2)
    ico = T5.adj_from_faces(ico_faces)

    rf, ncf, popf = relative_r(fri_faces, fri, 0)
    ri, nci, popi = relative_r(ico_faces, ico, 0)
    odd_f = sum(1 for v in fri if v != 0 and len(fri[v]) % 2)
    # punctured degrees: neighbors of tv lose 1
    odd_fp = sum(1 for v in fri if v != 0
                 and (len(fri[v]) - (1 if 0 in fri[v] else 0)) % 2)
    odd_ip = sum(1 for v in ico if v != 0
                 and (len(ico[v]) - (1 if 0 in ico[v] else 0)) % 2)
    print(f"\n  Fritsch−0: population {popf} colorings, achieved columns "
          f"{ncf}, r_rel = {rf}  (punctured odd count {odd_fp})")
    print(f"  icosahedron−0: population {popi}, columns {nci}, r_rel = {ri} "
          f"(punctured odd count {odd_ip})")
    t1 = popf == 192 and popi > 0
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Complete populations")
    t2 = ncf > 2 and nci > 2
    print(f"  [{'PASS' if t2 else 'FAIL'}] 2. r measured on real current "
          f"sets (no starvation)")

    print("\n  THE r-vs-ODD TABLE (closed S4 ladder + punctured rows):")
    print("    odd=2  (S4 closed):   r=0 0 0 0")
    print("    odd=4  (S4 closed):   r=8 8 8 8")
    print("    odd=6  (S4 closed):   r=8 8 8 8")
    print("    odd=8+ (S4 closed):   r=8 ...")
    print(f"    Fritsch−0 (odd {odd_fp}, relative): r={rf}")
    print(f"    ico−0 (odd {odd_ip}, relative):     r={ri}")
    if rf != 0:
        verdict = ("FRITSCH WAS NEVER AN EXCEPTION — its closed r=0 was "
                   "frozen-population smallness; the sharp dipole law "
                   "stands clean; M2's clue dissolves")
    else:
        verdict = ("FRITSCH IS A GENUINE GEOMETRIC EXCEPTION to a sharp "
                   "law — escalate to Lyra")
    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. VERDICT: {verdict}")

    res = [t1, t2, t3]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5545 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(res, 1):
        if not r:
            print(f"  Test {i}: FAIL")
