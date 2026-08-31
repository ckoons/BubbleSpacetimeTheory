#!/usr/bin/env python3
"""
Toy 5536 — Q4 (Round 10): THE PUNCTURE PROBE — is deletion-unfreezing general?

Toy 5535's corollary: closed Fritsch has 2 frozen partitions; Fritsch−v is
ONE Kempe class. If that generalizes, the insertion problem — which lives
in G−v — sits in the FRIENDLY regime, and the endgame changes shape.

*** BLIND PREDICTION (registered before the runs): deletion-unfreezing is
GENERAL — every frozen closed object tested collapses to a single relative
class after one vertex deletion; and the disc's twins, after deleting the
CENTER, become connected. Basis: Fritsch anchor + E1's rings-add-escape-
routes + Z1's availability reading (freezing = starved availability;
deletion feeds it). Can fail per object. ***

OBJECTS:
  A. Fritsch − v (anchor, replicates 5535: 1 class from 2 frozen).
  B. icosahedron − v (the sharp one: 10 frozen singleton partitions
     closed; what survives puncture?).
  C. triakis − apex (deg-3) and triakis − original (deg-6).
  D. THE DISC, center deleted, decision pinning kept: do the twin
     completions (restricted to the 6 surviving interior vertices)
     become connected under legal (boundary-avoiding, center-excluded)
     moves?

Classes computed on PARTITION space (Z2 convention) for A-C; for D on raw
completions of the pinned punctured disc.

TESTS (X/Y):
  1. Anchor: Fritsch−v single partition-class (5535 replication at
     partition level).
  2. icosahedron−v class count (blind: 1).
  3. triakis−v both deletion types (blind: 1 each).
  4. Disc-center deletion: twins' restrictions connected (blind: yes).
  5. Verdict: deletion-unfreezing general on all tested objects.

Elie, 2026-08-30. Millennium week, 4-Color round 10. 5 tests.
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


G5 = load("g5512q4", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")
T5 = load("t5515q4", "toy_5515_AUG30_E1_kring_tower_family_rescue_depth_vs_k"
          "_cal_F0_absorbed.py")
Y3 = load("t5525q4", "toy_5525_AUG30_Y3_dilution_test_akempic_knot_in"
          "_eulerian_bulk.py")
Y4 = load("t5526q4", "toy_5526_AUG30_Y4_boundary_fisk_disc_relative_kempe"
          "_connectivity.py")


def punctured_partition_classes(adj_full, tv):
    """Kempe classes of G−tv colorings (chains exclude tv), counted on
    partition space. Returns (n_partitions, n_classes)."""
    vs = sorted((u for u in adj_full if u != tv), key=str)
    cols = []
    col = {}

    def bt(i):
        if i == len(vs):
            cols.append(dict(col))
            return
        u = vs[i]
        for c in range(4):
            if i == 0 and c != 0:
                continue
            if all(col.get(w) != c for w in adj_full[u] if w != tv):
                col[u] = c
                bt(i + 1)
                del col[u]

    bt(0)

    def pkey(c):
        classes = {}
        key = []
        nxt = 0
        for v in vs:
            cc = c[v]
            if cc not in classes:
                classes[cc] = nxt
                nxt += 1
            key.append(classes[cc])
        return tuple(key)

    parts = {}
    for c in cols:
        k = pkey(c)
        if k not in parts:
            parts[k] = c
    cid = {}
    ncl = 0
    for k0, c0 in parts.items():
        if k0 in cid:
            continue
        ncl += 1
        q = deque([c0])
        cid[k0] = ncl - 1
        while q:
            c = q.popleft()
            for a, b in itertools.combinations(range(4), 2):
                done = set()
                for u in vs:
                    if u in done or c[u] not in (a, b):
                        continue
                    S = G5.kempe_chain(adj_full, c, u, a, b, exclude={tv})
                    done |= S
                    nc = dict(c)
                    for x in S:
                        nc[x] = b if nc[x] == a else a
                    k = pkey(nc)
                    if k not in cid:
                        cid[k] = ncl - 1
                        q.append(nc)
    return len(parts), ncl


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5536 — Q4: the puncture probe")
    print("=" * 70)

    fri = G5.adj_from_faces(G5.fritsch_faces())
    ico = T5.adj_from_faces(T5.tower_faces(2))
    tri = Y3.adj_from_faces(Y3.triakis_faces())

    # A. Fritsch anchor
    pA, cA = punctured_partition_classes(fri, 0)
    t1 = (cA == 1)
    print(f"\n  Fritsch−0: partitions={pA} classes={cA} "
          f"(closed Fritsch: 2 frozen)")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Anchor: single class")

    # B. icosahedron−v
    pB, cB = punctured_partition_classes(ico, 0)
    t2 = (cB == 1)
    print(f"\n  icosahedron−0: partitions={pB} classes={cB} "
          f"(closed: 10 frozen singletons)")
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. icosahedron unfreezes to "
          f"{cB} class(es) (blind: 1)")

    # C. triakis − both types
    apex = next(v for v in tri if len(tri[v]) == 3)
    orig = next(v for v in tri if len(tri[v]) == 6)
    pC1, cC1 = punctured_partition_classes(tri, apex)
    pC2, cC2 = punctured_partition_classes(tri, orig)
    t3 = (cC1 == 1 and cC2 == 1)
    print(f"\n  triakis−apex({apex}): partitions={pC1} classes={cC1}")
    print(f"  triakis−orig({orig}): partitions={pC2} classes={cC2} "
          f"(closed: 1 frozen partition)")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. triakis−v single class, "
          f"both deletion types (blind: 1 each)")

    # D. the disc, center deleted, decision pinning kept
    adj, interior, bcyc = Y4.disc(2)
    center = (0, 0)
    pin = dict(zip(bcyc, [0, 1, 0, 1, 0, 1, 0, 1, 2, 1, 2, 1]))
    # original twins (for restriction comparison)
    twins = Y4.completions(adj, interior, pin)
    interior2 = [v for v in interior if v != center]
    # completions of the punctured disc: proper on adj minus center
    comps2 = []
    col2 = dict(pin)

    def bt2(i):
        if i == len(interior2):
            comps2.append(dict(col2))
            return
        u = interior2[i]
        for c in range(4):
            if all(col2.get(w) != c for w in adj[u] if w != center):
                col2[u] = c
                bt2(i + 1)
                del col2[u]

    bt2(0)
    bset = set(bcyc)

    def legal_moves2(c):
        for a, b in itertools.combinations(range(4), 2):
            done = set()
            for u in interior2:
                if u in done or c[u] not in (a, b):
                    continue
                S = G5.kempe_chain(adj, c, u, a, b,
                                   exclude={center} | bset)
                # kempe_chain excludes only vertices in exclude from entry;
                # chains through boundary are blocked by exclusion, matching
                # legal = interior-only, center gone
                done |= S
                if not (S & bset) and center not in S:
                    yield a, b, S

    keyf = lambda c: tuple(c[u] for u in sorted(interior2, key=str))
    idx = {keyf(c): i for i, c in enumerate(comps2)}
    cls = [None] * len(comps2)
    ncl2 = 0
    for i0, c0 in enumerate(comps2):
        if cls[i0] is not None:
            continue
        ncl2 += 1
        q = deque([c0])
        cls[i0] = ncl2 - 1
        while q:
            c = q.popleft()
            for a, b, S in legal_moves2(c):
                nc = dict(c)
                for x in S:
                    nc[x] = b if nc[x] == a else a
                j = idx.get(keyf(nc))
                if j is not None and cls[j] is None:
                    cls[j] = ncl2 - 1
                    q.append(nc)
    r1 = keyf({u: twins[0][u] for u in interior2} | pin)
    r2 = keyf({u: twins[1][u] for u in interior2} | pin)
    same = (r1 in idx and r2 in idx
            and cls[idx[r1]] == cls[idx[r2]])
    t4 = same
    print(f"\n  punctured disc (center deleted, decision pinning): "
          f"completions={len(comps2)} classes={ncl2}")
    print(f"  twin restrictions present: {r1 in idx and r2 in idx}; "
          f"same class: {same}")
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. The twins CONNECT after "
          f"center deletion (blind: yes)")

    t5 = t1 and t2 and t3 and t4
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. VERDICT: deletion-unfreezing "
          f"general on all tested objects"
          + (" — the insertion problem lives in the friendly regime"
             if t5 else " — NOT general; exceptions above"))

    res = [t1, t2, t3, t4, t5]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5536 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(res, 1):
        if not r:
            print(f"  Test {i}: FAIL")
