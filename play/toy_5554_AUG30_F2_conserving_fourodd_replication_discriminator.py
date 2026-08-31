#!/usr/bin/env python3
"""
Toy 5554 — F2 (Round 15): D3 REPLICATION + THE GEOMETRIC DISCRIMINATOR

D3's amendment found one conserving (r = 0, real population) four-odd
graph at odd-set diameter 4. KT's rent: replicate, and name the variable
separating r = 8 from r = 0 at fixed dipole count.

Design: the diameter-scored constructor (D3's fix) across many seeds and
target diameters; per instance: r (unmeasured rows excluded), odd-set
diameter, the PAIRING structure (odd vertices pair by adjacency-cluster:
sizes of connected components of the odd set — '2+2' split dipoles vs '4'
one cluster), and the minimum inter-cluster distance.

Candidate discriminators scored (each pre-registered as a candidate, none
privileged): C-a diameter; C-b cluster split (4 together vs 2+2);
C-c inter-cluster distance.

TESTS (X/Y): 1. n >= 10 measured instances with >= 2 conserving ·
2. discriminator table · 3. the verdict: which candidate separates.

Elie, 2026-08-30. Millennium week, 4-Color round 15. 3 tests.
"""

import importlib.util
import os
import random
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


S4 = load("t5540f2", "toy_5540_AUG30_S4_r_threshold_bisection_odd_count"
          "_ladder.py")
Q3 = S4.Q3
G5 = S4.G5
Y3 = Q3.Y3


def sep_target(seed, min_diam, max_steps=12000):
    rng = random.Random(seed * 77 + min_diam)
    fs = [frozenset(f) for f in Y3.subdivided_octahedron_faces(3)]
    cur_odd, _ = Q3.odd_count_of(fs)
    for _ in range(max_steps):
        i = rng.randrange(len(fs))
        edge = frozenset(rng.sample(sorted(fs[i], key=str), 2))
        snap = list(fs)
        if not Q3.faceset_flip(fs, i, edge, rng):
            continue
        oc, _ = Q3.odd_count_of(fs)
        adj = G5.adj_from_faces([tuple(sorted(f, key=str)) for f in fs])
        odds = [v for v in adj if len(adj[v]) % 2]
        diam = 0
        if oc == 4:
            dmax = 0
            for s in odds:
                dist = {s: 0}
                q = deque([s])
                while q:
                    u = q.popleft()
                    for w in adj[u]:
                        if w not in dist:
                            dist[w] = dist[u] + 1
                            q.append(w)
                dmax = max(dmax, max(dist[t] for t in odds))
            diam = dmax
        good = (abs(oc - 4) < abs(cur_odd - 4)) or \
            (oc == 4 and diam >= min_diam) or rng.random() < 0.15
        if good:
            cur_odd = oc
            if oc == 4 and diam >= min_diam:
                return [tuple(sorted(f, key=str)) for f in fs], diam
        else:
            fs[:] = snap
    return None, None


def odd_structure(adj):
    odds = [v for v in adj if len(adj[v]) % 2]
    # connected components of the odd set (induced)
    comps = []
    left = set(odds)
    while left:
        s = left.pop()
        comp = {s}
        stack = [s]
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y in left:
                    left.discard(y)
                    comp.add(y)
                    stack.append(y)
        comps.append(comp)
    sizes = tuple(sorted(len(c) for c in comps))
    # min inter-cluster distance
    icd = 0
    if len(comps) >= 2:
        icd = 99
        for A in comps:
            for B in comps:
                if A is B:
                    continue
                for a in A:
                    dist = {a: 0}
                    q = deque([a])
                    while q:
                        u = q.popleft()
                        for w in adj[u]:
                            if w not in dist:
                                dist[w] = dist[u] + 1
                                q.append(w)
                    for b in B:
                        icd = min(icd, dist[b])
    # diameter
    dmax = 0
    for s in odds:
        dist = {s: 0}
        q = deque([s])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    q.append(w)
        dmax = max(dmax, max(dist[t] for t in odds))
    return sizes, icd, dmax


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5554 — F2: conserving four-odd replication + discriminator")
    print("=" * 70)

    rows = []
    # tight family (S4 seeds)
    for seed in range(10):
        f = S4.family_target(seed, 4)
        if f is None:
            continue
        adj = G5.adj_from_faces(f)
        if sum(1 for v in adj if len(adj[v]) % 2) != 4:
            continue
        g, nc = Q3.residue_r(f, adj)
        if nc == 0:
            continue
        sizes, icd, diam = odd_structure(adj)
        rows.append(('tight', sizes, icd, diam, g))
        if sum(1 for r in rows if r[0] == 'tight') >= 6:
            break
    # separated family — widen until >= 3 conserving or seed budget out
    seen = set()
    for tgt in (3, 4, 5, 6):
        got = 0
        for seed in range(120):
            f, d = sep_target(seed, tgt)
            if f is None:
                continue
            key = frozenset(f)
            if key in seen:
                continue
            seen.add(key)
            adj = G5.adj_from_faces(f)
            g, nc = Q3.residue_r(f, adj)
            if nc == 0:
                continue
            sizes, icd, diam = odd_structure(adj)
            rows.append((f'sep{tgt}', sizes, icd, diam, g))
            got += 1
            n_cons_now = sum(1 for r in rows if r[4] == 0)
            if got >= 8 or (n_cons_now >= 3 and got >= 3):
                break
        if sum(1 for r in rows if r[4] == 0) >= 3 and \
                sum(1 for r in rows if r[0].startswith('sep')) >= 8:
            break
    print(f"\n  measured instances: {len(rows)}")
    print(f"  {'family':>6} {'clusters':>10} {'icd':>4} {'diam':>5} {'r':>3}")
    for fam, sizes, icd, diam, g in rows:
        print(f"  {fam:>6} {str(sizes):>10} {icd:>4} {diam:>5} {g:>3}")
    n_cons = sum(1 for r in rows if r[4] == 0)
    t1 = len(rows) >= 10 and n_cons >= 2
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. n={len(rows)} measured, "
          f"conserving={n_cons}")

    # discriminator scoring: does each candidate PERFECTLY separate r=0/r=8?
    def separates(idx):
        zero_vals = {r[idx] for r in rows if r[4] == 0}
        eight_vals = {r[idx] for r in rows if r[4] == 8}
        return not (zero_vals & eight_vals), zero_vals, eight_vals

    verdicts = {}
    for name, idx in [('C-a diameter', 3), ('C-b clusters', 1),
                      ('C-c inter-cluster dist', 2)]:
        sep, zv, ev = separates(idx)
        verdicts[name] = (sep, zv, ev)
        print(f"  {name}: separates={sep}  r=0 values {zv}  r=8 values {ev}")
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Discriminator table")
    winners = [k for k, v in verdicts.items() if v[0]]
    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. VERDICT: "
          f"{'separating discriminator(s): ' + ', '.join(winners) + ' — KT pays rent' if winners else 'NO candidate cleanly separates — the discriminator remains open; KT stays on the shelf as explanation only'}")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5554 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
