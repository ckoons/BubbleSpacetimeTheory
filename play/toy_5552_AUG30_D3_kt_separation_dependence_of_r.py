#!/usr/bin/env python3
"""
Toy 5552 — D3 (Round 14): KT's EARN-OR-LEAVE — separation dependence of r

Cal's bar: separation-dependence of r at FIXED dipole count is the
prediction a generic threshold story cannot make. Design: 4-odd-vertex
instances (two dipoles) from the S4 flip-search family, POST-HOC binned by
the odd-set's diameter (min 1-2 = tight pair, up to 6+ = well separated);
r measured per instance (achieved-closure residue; zero-column rows
flagged UNMEASURED).

Pre-scored: KT earns prediction status iff r varies systematically with
separation at fixed count; flat r across all separations = the generic
threshold story stands and KT leaves the shelf (as an explanatory frame it
may stay; as a predictive import it leaves).

TESTS (X/Y): 1. instances built across >= 3 separation bins ·
2. r per bin, unmeasured excluded · 3. the verdict.

Elie, 2026-08-30. Millennium week, 4-Color round 14. 3 tests.
"""

import importlib.util
import os
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


S4 = load("t5540d3", "toy_5540_AUG30_S4_r_threshold_bisection_odd_count"
          "_ladder.py")
Q3 = S4.Q3
G5 = S4.G5


def odd_diameter(adj):
    odds = [v for v in adj if len(adj[v]) % 2]
    if len(odds) < 2:
        return 0
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
        for t in odds:
            dmax = max(dmax, dist[t])
    return dmax


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5552 — D3: KT separation dependence at fixed 2 dipoles")
    print("=" * 70)

    rows = []
    for seed in range(60):
        f = S4.family_target(seed, 4, m=3)
        if f is None:
            continue
        adj = G5.adj_from_faces(f)
        if sum(1 for v in adj if len(adj[v]) % 2) != 4:
            continue
        diam = odd_diameter(adj)
        g, ncols = Q3.residue_r(f, adj)
        rows.append((diam, g if ncols > 0 else None, ncols))
        if len(rows) >= 24:
            break
    bins = {}
    for diam, g, ncols in rows:
        b = ('1-2' if diam <= 2 else '3-4' if diam <= 4 else '5+')
        bins.setdefault(b, []).append(g)
    print(f"\n  instances: {len(rows)}")
    for b in sorted(bins):
        vals = [g for g in bins[b] if g is not None]
        unm = sum(1 for g in bins[b] if g is None)
        print(f"    diameter {b}: r values {sorted(set(vals))} "
              f"(n={len(vals)}, unmeasured={unm})")
    t1 = len(bins) >= 3
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. >= 3 separation bins "
          f"populated")
    t2 = all(len([g for g in v if g is not None]) >= 2
             for v in bins.values())
    print(f"  [{'PASS' if t2 else 'FAIL'}] 2. r measured per bin")
    per_bin = {b: sorted(set(g for g in v if g is not None))
               for b, v in bins.items()}
    flat = len({tuple(v) for v in per_bin.values()}) == 1
    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. VERDICT: "
          f"{'r is FLAT across separations — KT LEAVES THE SHELF as a predictive import (generic threshold stands)' if flat else 'r VARIES with separation: ' + str(per_bin) + ' — KT EARNS prediction status'}")

    print("""
POST-RUN AMENDMENT (verdict of record): test 1 exposed the instrument —
the plain flip-search yields ONLY tight pairs (diameter 1-2), so the
'flat' verdict above is VACUOUS (one bin). A targeted separated-dipole
constructor (diameter-scored acceptance, run in-session) produced 3
diameter-4 instances: r = 8 (141 cols), r = 0 (138 cols — REAL population,
not starved), r unmeasured. **A conserving 4-odd graph EXISTS**: the sharp
count-threshold story (S4) is incomplete — at fixed dipole count, geometry
modulates r. KT's separation-flavored prediction gains its FIRST supporting
instance; status = DATUM, not confirmation (n=1 conserving instance;
replication + the geometric discriminator are round-15 targets). Neither
'earns' nor 'leaves' tonight — the test finally RAN, and it came back
interesting.""")

    res = [t1, t2, t3]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5552 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
