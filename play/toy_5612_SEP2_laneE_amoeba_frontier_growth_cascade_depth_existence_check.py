#!/usr/bin/env python3
"""
Toy 5612 — LANE E EXISTENCE CHECK: CASEY'S AMOEBA. A frontier-growing
4-coloring with cascade repair, on plantri triangulations; the
maximum depth (below the frontier) of any recolored vertex; failures;
positive control = a pinned boundary with NO proper extension must
fail.

THE ALGORITHM (Casey, verbatim in substance, made deterministic):
  seed = a triangle plus one neighbor (4 vertices), colored properly;
  grow by one vertex at a time in BFS order from the seed (the
  amoeba's frontier); color the new vertex with the smallest color
  absent from its colored neighbors; if none is absent (all four
  present): CONFLICT — assign the color whose conflicting colored
  neighbors are fewest, preferring neighbors that themselves have
  uncolored neighbors (conflicts are cheap at the frontier), then
  push: each conflicting neighbor x is recolored the same way (a free
  color if any; else the least-conflict color preferring outward);
  repeat until no conflict (cascade). DEPTH of a recolored vertex =
  its distance to the uncolored set at that moment (0 = on the
  frontier). Cap: 20·n recolorings per cascade -> FAIL (non-
  terminating cascade). A proper coloring of T at the end = SUCCESS
  (verified independently).

POPULATIONS: plantri all triangulations n = 6..11 (1,553 graphs),
every face as seed for n <= 9, first 6 faces for n = 10, 11; -c5
n = 12..22 (930 graphs), first 6 faces each.
CONTROL: discs T-v (n = 12..14, -c5) with the link 5-cycle colored and
PINNED (not recolorable); pinned colorings that have NO proper
extension (exhaustive check) must FAIL; those with one — reported
(the amoeba is not claimed complete).

Elie, 2026-09-02.
"""

import importlib.util
import itertools
import os
import sys
import time
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


EA = load("t5594am", "toy_5594_SEP2_EA_class_insertability_kempe_classes"
          "_of_T_minus_v.py")
G5 = EA.G5


def dist_to_uncolored(adj, col, pinned):
    """BFS distances from the uncolored set (0 = uncolored/frontier-adjacent counts as 0 for uncolored)."""
    d = {}
    q = deque()
    for u in adj:
        if u not in col:
            d[u] = 0
            q.append(u)
    while q:
        u = q.popleft()
        for w in adj[u]:
            if w not in d:
                d[w] = d[u] + 1
                q.append(w)
    return d


def amoeba(adj, seed_face, pinned=None, cap_factor=20):
    """Returns (success, max_depth, n_recolor, n_cascades, fail_reason)."""
    pinned = pinned or {}
    col = dict(pinned)
    n = len(adj)
    a, b, c = seed_face
    order = []
    seen = set(col)
    # seed: the triangle then BFS
    q = deque()
    for u in (a, b, c):
        if u not in seen:
            seen.add(u)
            order.append(u)
            q.append(u)
    for u in list(col):
        q.append(u)
    while q:
        u = q.popleft()
        for w in sorted(adj[u]):
            if w not in seen:
                seen.add(w)
                order.append(w)
                q.append(w)
    max_depth = 0
    n_rec = 0
    n_casc = 0

    def free_colors(u):
        return [k for k in range(4) if all(col.get(w) != k for w in adj[u])]

    def choose(u, dist):
        fc = free_colors(u)
        if fc:
            return fc[0], []
        best = None
        for k in range(4):
            confl = [w for w in adj[u] if col.get(w) == k]
            if any(w in pinned for w in confl):
                continue
            # prefer conflicts at the frontier (small dist)
            score = (len(confl), sum(dist.get(w, 0) for w in confl))
            if best is None or score < best[0]:
                best = (score, k, confl)
        if best is None:
            return None, None
        return best[1], best[2]

    for u in order:
        dist = dist_to_uncolored(adj, col, pinned)
        k, confl = choose(u, dist)
        if k is None:
            return False, max_depth, n_rec, n_casc, 'pinned-block'
        col[u] = k
        if confl:
            n_casc += 1
            work = deque(confl)
            steps = 0
            while work:
                x = work.popleft()
                if all(col.get(w) != col[x] for w in adj[x]):
                    continue                     # resolved meanwhile
                if x in pinned:
                    return False, max_depth, n_rec, n_casc, 'pinned-conflict'
                dist = dist_to_uncolored(adj, col, pinned)
                max_depth = max(max_depth, dist.get(x, 0))
                kx, cx = choose(x, dist)
                if kx is None:
                    return False, max_depth, n_rec, n_casc, 'pinned-block'
                col[x] = kx
                n_rec += 1
                steps += 1
                if steps > cap_factor * n:
                    return False, max_depth, n_rec, n_casc, 'cascade-cap'
                for w in cx:
                    work.append(w)
    ok = all(col[u] != col[w] for u in adj for w in adj[u]) and len(col) == n
    return ok, max_depth, n_rec, n_casc, None if ok else 'improper-at-end'


def plantri_rot(n, flags=()):
    """plantri -a keeps each vertex's neighbours in cyclic (rotation) order;
    faces = (u, nbr[i], nbr[i+1]) — no dependence on G5's face finder."""
    import subprocess
    out = subprocess.run([EA.PLANTRI, '-a', *flags, str(n)], capture_output=True, text=True).stdout
    res = []
    for line in out.splitlines():
        line = line.strip()
        if not line or not line[0].isdigit():
            continue
        nv, rest = line.split(' ', 1)
        rot = [[ord(ch) - 97 for ch in p] for p in rest.split(',')]
        adj = {i: set(r) for i, r in enumerate(rot)}
        faces = set()
        for u, r in enumerate(rot):
            for i in range(len(r)):
                faces.add(tuple(sorted((u, r[i], r[(i + 1) % len(r)]))))
        res.append((adj, sorted(faces)))
    return res


def faces_of(adj):
    tris, ok, _m = G5.faces_from_adj_triangulation(adj)
    return [tuple(f) for f in tris] if tris else []


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5612 — Lane E: Casey's amoeba, existence check")
    print("=" * 70)
    t0 = time.time()
    # POSITIVE CONTROL first: pinned link colorings on T-v, -c5 n = 12..14
    print("\n  CONTROL: pinned link 5-cycle on T-v; extension-free (FROZEN) pinnings must FAIL")
    ctl = Counter()
    # trivial frozen disc: N[v] with the link 4-colored, interior = v alone
    triv = Counter()
    for adj, fs in plantri_rot(12, ('-c5',)):
        for v in [u for u in adj if len(adj[u]) == 5][:4]:
            lcyc = EA.G5.link_cycle(fs, v)
            sub = {u: {w for w in adj[u] if w != v} for u in adj if u != v}
            disc = {v: set(lcyc)}
            for i, u in enumerate(lcyc):
                disc[u] = {v, lcyc[i - 1], lcyc[(i + 1) % 5]}
            for cols5 in ((0, 1, 0, 2, 3), (0, 1, 2, 0, 3), (0, 1, 0, 1, 2)):
                pin = {lcyc[i]: cols5[i] for i in range(5)}
                ok, md, nr, nc, why = amoeba(disc, (v, lcyc[0], lcyc[1]), pinned=pin)
                frozen = len(set(cols5)) == 4
                triv[('FROZEN' if frozen else 'extendable', 'success' if ok else f'fail:{why}')] += 1
    print(f"    trivial disc N[v] (link pinned): {dict(triv)}")
    for n, flags in ((9, ()), (10, ()), (11, ()), (12, ('-c5',)), (14, ('-c5',))):
        for gi, (adj, fs) in enumerate(plantri_rot(n, flags)):
            for v in [u for u in adj if len(adj[u]) == 5][:3]:
                lcyc = EA.G5.link_cycle(fs, v)
                sub = {u: {w for w in adj[u] if w != v} for u in adj if u != v}
                # all proper colorings of the 5-cycle with 4 colors, up to a few
                for cols5 in itertools.product(range(4), repeat=5):
                    if any(cols5[i] == cols5[(i + 1) % 5] for i in range(5)):
                        continue
                    if cols5[0] != 0 or cols5[1] != 1:
                        continue                     # symmetry cut
                    pin = {lcyc[i]: cols5[i] for i in range(5)}
                    # exhaustive extension test
                    order = [u for u in sorted(sub) if u not in pin]
                    ext = [False]

                    def rec(i, col):
                        if ext[0]:
                            return
                        if i == len(order):
                            ext[0] = True
                            return
                        u = order[i]
                        for k in range(4):
                            if all(col.get(w) != k for w in sub[u]):
                                col[u] = k
                                rec(i + 1, col)
                                del col[u]
                    rec(0, dict(pin))
                    # amoeba with the pinned boundary; seed = a face touching the link
                    face = next(f for f in fs if v not in f and any(x in pin for x in f))
                    ok, md, nr, nc, why = amoeba(sub, face, pinned=pin)
                    ctl[('extendable' if ext[0] else 'FROZEN', 'amoeba-success' if ok else f'amoeba-fail:{why}')] += 1
    print(f"    T-v pinnings: {dict(ctl)}")
    n_frozen = sum(c for (e, r), c in ctl.items() if e == 'FROZEN') + sum(c for (e, r), c in triv.items() if e == 'FROZEN')
    frozen_ok = sum(c for (e, r), c in ctl.items() if e == 'FROZEN' and r == 'amoeba-success') + sum(c for (e, r), c in triv.items() if e == 'FROZEN' and r == 'success')
    print(f"    [{'PASS' if (frozen_ok == 0 and n_frozen > 0) else 'FAIL'}] control: FROZEN pinnings found {n_frozen}, amoeba succeeded on {frozen_ok} (must be 0, with n_frozen > 0); "
          f"extendable pinnings solved by the amoeba: "
          f"{sum(c for (e, r), c in ctl.items() if e == 'extendable' and r == 'amoeba-success')}/"
          f"{sum(c for (e, r), c in ctl.items() if e == 'extendable')}  [{time.time()-t0:.0f}s]", flush=True)

    # POPULATIONS
    for label, ns, flags, nfaces in (('all triangulations', range(6, 12), (), None),
                                     ('5-connected', range(12, 23), ('-c5',), 6)):
        print(f"\n  POPULATION: {label}")
        for n in ns:
            gs = plantri_rot(n, flags)
            cnt = Counter()
            depth = Counter()
            fails = []
            for gi, (adj, fs) in enumerate(gs):
                seeds = fs if (nfaces is None and n <= 9) else fs[:6]
                for f in seeds:
                    ok, md, nr, nc, why = amoeba(adj, f)
                    cnt['runs'] += 1
                    cnt['success' if ok else 'FAIL'] += 1
                    depth[md] += 1
                    cnt['recolorings'] += nr
                    cnt['cascades'] += nc
                    if not ok:
                        fails.append((n, gi, f, why))
            print(f"    n={n}: graphs {len(gs)}, runs {cnt['runs']}, success {cnt['success']}, FAIL {cnt['FAIL']}, "
                  f"max-depth histogram {dict(sorted(depth.items()))}, recolorings/run {cnt['recolorings']/max(1,cnt['runs']):.2f}, "
                  f"cascades/run {cnt['cascades']/max(1,cnt['runs']):.2f}  [{time.time()-t0:.0f}s]", flush=True)
            for fl in fails[:3]:
                print(f"      fail: {fl}")


# ---------------------------------------------------------------- v2 (run 10:4x, results in the 10:4x post)
def amoeba_v2(adj, seed_face, cap_factor=20):
    """v2: within one cascade a vertex may not return to a color it already
    held (tabu). Every v1 failure was a two-vertex ping-pong; v2 removes it.
    Failures that remain are 'tabu-exhausted' (a vertex runs out of colors
    inside one cascade) — genuine dead ends of the single-vertex push."""
    col = {}
    n = len(adj)
    a, b, c = seed_face
    order = []
    seen = set()
    q = deque()
    for u in (a, b, c):
        seen.add(u)
        order.append(u)
        q.append(u)
    while q:
        u = q.popleft()
        for w in sorted(adj[u]):
            if w not in seen:
                seen.add(w)
                order.append(w)
                q.append(w)

    def choose(u, dist, tabu):
        fc = [k for k in range(4) if all(col.get(w) != k for w in adj[u]) and (u, k) not in tabu]
        if fc:
            return fc[0], []
        best = None
        for k in range(4):
            if (u, k) in tabu:
                continue
            confl = [w for w in adj[u] if col.get(w) == k]
            score = (len(confl), sum(dist.get(w, 0) for w in confl))
            if best is None or score < best[0]:
                best = (score, k, confl)
        if best is None:
            return None, None
        return best[1], best[2]
    maxd = 0
    nrec = 0
    for u in order:
        dist = dist_to_uncolored(adj, col, {})
        k, confl = choose(u, dist, set())
        col[u] = k
        if confl:
            tabu = {(u, k)}
            work = deque(confl)
            steps = 0
            while work:
                x = work.popleft()
                if all(col.get(w) != col[x] for w in adj[x]):
                    continue
                dist = dist_to_uncolored(adj, col, {})
                maxd = max(maxd, dist.get(x, 0))
                tabu.add((x, col[x]))
                kx, cx = choose(x, dist, tabu)
                if kx is None:
                    return False, maxd, nrec, 'tabu-exhausted'
                col[x] = kx
                nrec += 1
                steps += 1
                if steps > cap_factor * n:
                    return False, maxd, nrec, 'cascade-cap'
                for w in cx:
                    work.append(w)
    ok = all(col[u] != col[w] for u in adj for w in adj[u]) and len(col) == n
    return ok, maxd, nrec, None if ok else 'improper'
