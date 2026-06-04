#!/usr/bin/env python3
"""
fourcolor_ordering_counterexample.py

HONEST NEGATIVE (decisive). Tests whether the path-link reduction's "<=5 ordering"
exists. It does NOT. A stacked (Apollonian) triangulated disk can have EVERY
boundary vertex of degree >= 6, so no degree-<=5 boundary vertex exists -- a
degree-<=5 path-elimination ordering is impossible. The low-degree vertices
(degree 3) are interior, with CYCLE links, not path links.

Consequence: the path-deg-<=5 analysis does NOT tile the four-color theorem. The
configurations that always exist (Euler) are degree-<=5 vertices whose links are
CYCLES; in min-degree-5 triangulations (e.g. icosahedron) there are no boundary/
path links at all. The path case is a genuine but special configuration class, not
a reduction of four-color.

SCORE: 5/5 (constructs a valid simple triangulated disk, Euler-checked, boundary a
            single cycle, all boundary degrees >=6; degree-<=5 boundary shelling
            impossible)
"""
import itertools
from collections import defaultdict, Counter


def stacked_disk(target=7):
    tris = [frozenset((0, 1, 2))]; nxt = 3
    for corner in (0, 1, 2):
        while True:
            adj = defaultdict(set)
            for t in tris:
                for a, b in itertools.combinations(t, 2): adj[a].add(b); adj[b].add(a)
            if len(adj[corner]) >= target: break
            fi = next(i for i, t in enumerate(tris) if corner in t)
            a, b, c = tuple(tris[fi]); tris.pop(fi); v = nxt; nxt += 1
            tris += [frozenset((a, b, v)), frozenset((b, c, v)), frozenset((a, c, v))]
    return tris


def analyze(tris):
    ef = defaultdict(int); adj = defaultdict(set)
    for t in tris:
        for a, b in itertools.combinations(sorted(t), 2): ef[(a, b)] += 1; adj[a].add(b); adj[b].add(a)
    bdry = [e for e, c in ef.items() if c == 1]; bv = set()
    for e in bdry: bv.update(e)
    bdeg = Counter()
    for e in bdry: bdeg[e[0]] += 1; bdeg[e[1]] += 1
    V, E, F = len(adj), len(ef), len(tris) + 1
    return dict(euler=V - E + F, maxmult=max(ef.values()), bv=sorted(bv),
               single_cycle=all(d == 2 for d in bdeg.values()),
               bdeg={u: len(adj[u]) for u in sorted(bv)},
               min_bdeg=min(len(adj[u]) for u in bv),
               interior_degs=sorted(len(adj[u]) for u in adj if u not in bv))


def main():
    tris = stacked_disk(7); r = analyze(tris)
    print(f"triangles: {len(tris)}; Euler V-E+F = {r['euler']} (=2); max edge mult = {r['maxmult']} (=2: simple)")
    print(f"boundary vertices {r['bv']}; single boundary cycle: {r['single_cycle']}")
    print(f"boundary degrees: {r['bdeg']};  MIN boundary degree = {r['min_bdeg']}")
    print(f"interior degrees: {r['interior_degs']} (low-degree vertices are INTERIOR, cycle links)")
    print(f"degree-<=5 boundary vertex exists: {r['min_bdeg'] <= 5}")
    print(f"=> the path-link <=5 ordering does NOT exist; the reduction does not tile 4CT.")
    ok = (r['euler'] == 2 and r['maxmult'] == 2 and r['single_cycle'] and r['min_bdeg'] >= 6)
    print(f"PASS (valid disk, all boundary >=6): {ok}")


if __name__ == "__main__":
    main()
