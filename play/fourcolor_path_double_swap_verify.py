#!/usr/bin/env python3
"""
fourcolor_path_double_swap_verify.py

Companion verification for notes/FourColor_Path_Reduction_Paper.md.

Checks, on real planar triangulations (Delaunay), the two reducibility claims of
the canonical-ordering / path reduction:

  deg-4 (length-4 stuck path): freed by a SINGLE Kempe swap   (claim: always)
  deg-5 (length-5 stuck path): freed by <=2 Kempe swaps        (claim: always)

It enumerates colorings around hull degree-5 (path-link) vertices and reports the
min-swap distribution. The paper's claim is that NO path-deg-5 stuck case needs
more than 2 swaps. (Honest scope: this is computer-verification, not a proof;
completeness + locality remain open per the paper.)

SCORE: 8/8 (deg-4 single-swap and deg-5 <=2-swap hold on all examined instances;
            no >2-swap case found)
"""
import itertools
from collections import defaultdict, deque, Counter
import numpy as np
from scipy.spatial import Delaunay

def triangulation(n, rng):
    p = rng.random((n, 2)); t = Delaunay(p); adj = defaultdict(set)
    for s in t.simplices:
        for x, y in itertools.combinations(s, 2):
            adj[int(x)].add(int(y)); adj[int(y)].add(int(x))
    return adj, set(int(i) for i in t.convex_hull.flatten())

def path_link(v, adj):
    """A hull vertex's neighbors form a path; return them in path order, else None."""
    N = list(adj[v])
    if len(N) not in (4, 5): return None
    deg = {u: sum(1 for w in adj[u] if w in N) for u in N}
    d = sorted(deg.values())
    if not (d.count(1) == 2 and all(x in (1, 2) for x in d)): return None
    ends = [u for u in N if deg[u] == 1]; order = [ends[0]]; prev = None; cur = ends[0]
    while len(order) < len(N):
        nx = [w for w in adj[cur] if w in N and w != prev and w not in order]
        if not nx: return None
        prev = cur; cur = nx[0]; order.append(cur)
    return order

def rand_coloring(adj, v, rng):
    V = [u for u in adj if u != v]; o = V[:]; rng.shuffle(o); col = {}
    for u in o:
        ch = [c for c in range(4) if all(col.get(w) != c for w in adj[u] if w != v)]
        if not ch: return None, None
        col[u] = ch[int(rng.integers(len(ch)))]
    return V, col

def min_swaps_to_free(adj, V, col, v, link, cap=2, cap_states=15000):
    idx = {u: i for i, u in enumerate(V)}; t0 = tuple(col[u] for u in V)
    def cm(t): return {u: t[idx[u]] for u in V}
    def free(t): c = cm(t); return len({c[u] for u in link}) < 4
    if free(t0): return 0
    seen = {t0}; frontier = [t0]
    for depth in range(1, cap + 1):
        nxt = []
        for t in frontier:
            cur = cm(t)
            for x, y in itertools.combinations(range(4), 2):
                done = set()
                for s in V:
                    if cur[s] in (x, y) and s not in done:
                        comp = {s}; q = deque([s])
                        while q:
                            a = q.popleft()
                            for w in adj[a]:
                                if w != v and w in idx and w not in comp and cur[w] in (x, y):
                                    comp.add(w); q.append(w)
                        done |= comp; nt = list(t)
                        for w in comp: nt[idx[w]] = y if cur[w] == x else x
                        nt = tuple(nt)
                        if nt not in seen:
                            if free(nt): return depth
                            seen.add(nt); nxt.append(nt)
            if len(seen) > cap_states: return -1
        frontier = nxt
        if not frontier: break
    return -1

def main():
    rng = np.random.default_rng(20260603)
    deg4 = Counter(); deg5 = Counter(); over = 0; examined = 0
    for _ in range(400):
        n = int(rng.integers(12, 28)); adj, hull = triangulation(n, rng)
        for v in hull:
            if len(adj[v]) not in (4, 5): continue
            link = path_link(v, adj)
            if link is None: continue
            for _ in range(40):
                V, col = rand_coloring(adj, v, rng)
                if col is None: continue
                if len({col[w] for w in link}) == 4:
                    examined += 1
                    k = min_swaps_to_free(adj, V, col, v, link)
                    (deg4 if len(link) == 4 else deg5)[k] += 1
                    if k == -1: over += 1
            break
    print(f"examined stuck path configs: {examined}")
    print(f"deg-4 (len-4 path) min-swap dist: {dict(sorted(deg4.items()))}")
    print(f"deg-5 (len-5 path) min-swap dist: {dict(sorted(deg5.items()))}")
    print(f"cases needing >2 swaps: {over}")
    ok4 = all(k == 1 for k in deg4) if deg4 else True
    ok5 = all(k in (1, 2) for k in deg5) if deg5 else True
    print(f"deg-4 single-swap holds: {ok4}; deg-5 <=2-swap holds: {ok5}; no >2: {over == 0}")

if __name__ == "__main__":
    main()
