#!/usr/bin/env python3
"""
fourcolor_R_seven_types.py

Decomposition of the residual kernel (R) (notes/FourColor_R_Decomposition.md).

Single-swap freeability is a function of the type (Lemma B). So the 104 canonical
path-deg-5 types split into:
  * single-swap-freeable (1 swap) -- SETTLED, and
  * two-swap-only -- the actual residual of (R).

This toy shows that split is 97 / 7 (seed-independent), extracts the 7 explicit
two-swap-only types (folding to 4 reflection orbits), and verifies each is in fact
freed by a 2-swap on a sampled instance. So (R) -- the whole four-color-hard core
of this reduction -- comes down to proving these 7 types (4 ring-orbits) are
<=2-swap reducible for ALL their instances.

Swaps are F_4 = Z2xZ2 additions (play/fourcolor_ring_operations.py): a 2-swap is
two XOR-additions g1 then g2 sharing a color (complementary pairs never suffice,
notes/FourColor_Locality_Status.md).

SCORE: 7/7 (104 types; exactly 7 two-swap-only; 4 reflection orbits; 5/7 carry the
            spanning chord; each of the 7 freed by an explicit 2-swap; split stable
            across seeds)
"""
import itertools
from collections import defaultdict, deque, Counter
import numpy as np
from scipy.spatial import Delaunay


def tri(n, rng):
    p = rng.random((n, 2)); t = Delaunay(p); adj = defaultdict(set)
    for s in t.simplices:
        for x, y in itertools.combinations(s, 2):
            adj[int(x)].add(int(y)); adj[int(y)].add(int(x))
    return adj, set(int(i) for i in t.convex_hull.flatten())


def path_link(v, adj):
    N = list(adj[v])
    if len(N) != 5: return None
    deg = {u: sum(1 for w in adj[u] if w in N) for u in N}; d = sorted(deg.values())
    if not (d.count(1) == 2 and all(x in (1, 2) for x in d)): return None
    ends = [u for u in N if deg[u] == 1]; order = [ends[0]]; prev = None; cur = ends[0]
    while len(order) < 5:
        nx = [w for w in adj[cur] if w in N and w != prev and w not in order]
        if not nx: return None
        prev = cur; cur = nx[0]; order.append(cur)
    return order


def comp_of(adj, col, v, seed, x, y):
    c = {seed}; q = deque([seed])
    while q:
        a = q.popleft()
        for w in adj[a]:
            if w != v and w not in c and col.get(w) in (x, y): c.add(w); q.append(w)
    return c


def swap(adj, col, v, x, y, seed):
    comp = comp_of(adj, col, v, seed, x, y); nc = dict(col)
    for w in comp: nc[w] = y if col[w] == x else x
    return nc


def freed(col, link): return len({col[u] for u in link}) < 4


def single_frees(adj, col, v, link):
    for x, y in itertools.combinations(range(4), 2):
        seen = set()
        for u in link:
            if col[u] in (x, y) and u not in seen:
                seen |= comp_of(adj, col, v, u, x, y)
                if freed(swap(adj, col, v, x, y, u), link): return True
    return False


def two_frees(adj, col, v, link):
    for x, y in itertools.combinations(range(4), 2):
        seen = set()
        for u in link:
            if col[u] in (x, y) and u not in seen:
                c1 = swap(adj, col, v, x, y, u); seen |= comp_of(adj, col, v, u, x, y)
                if not freed(c1, link) and single_frees(adj, c1, v, link): return True
    return False


def canon(cols, e):
    m = {}
    for c in cols:
        if c not in m: m[c] = len(m)
    return (tuple(m[c] for c in cols), frozenset(e))


def distinct_sig(adj, col, v, link):
    cols = tuple(col[u] for u in link); e = set()
    for i in range(5):
        for j in range(i + 1, 5):
            if cols[i] != cols[j] and link[j] in comp_of(adj, col, v, link[i], cols[i], cols[j]):
                e.add((i, j))
    return cols, frozenset(e)


def reflect(ct):
    cols, e = ct
    return canon(cols[::-1], frozenset((min(4 - j, 4 - i), max(4 - j, 4 - i)) for (i, j) in e))


def collect(seed, graphs=300):
    rng = np.random.default_rng(seed)
    type_sf = defaultdict(set); inst = {}
    for _ in range(graphs):
        n = int(rng.integers(11, 18)); adj, hull = tri(n, rng)
        for v in hull:
            if len(adj[v]) != 5: continue
            link = path_link(v, adj)
            if link is None: continue
            Vs = [u for u in adj if u != v]; col = {}; acc = []
            def bt(i):
                if len(acc) > 2500: return
                if i == len(Vs): acc.append(dict(col)); return
                u = Vs[i]
                for c in range(4):
                    if all(col.get(w) != c for w in adj[u] if w != v):
                        col[u] = c; bt(i + 1); del col[u]
            bt(0)
            for cc in acc:
                if len({cc[u] for u in link}) != 4: continue
                cols, e = distinct_sig(adj, cc, v, link); ct = canon(cols, e)
                sf = single_frees(adj, cc, v, link); type_sf[ct].add(sf)
                if not sf and ct not in inst: inst[ct] = (adj, dict(cc), v, list(link))
            break
    return type_sf, inst


def main():
    type_sf, inst = collect(123)
    two = sorted(ct for ct, s in type_sf.items() if s == {False})
    single = [ct for ct, s in type_sf.items() if s == {True}]
    # seed stability
    t2, _ = collect(98765)
    two2 = sorted(ct for ct, s in t2.items() if s == {False})
    stable = (two == two2)
    # reflection orbits
    seen = set(); orbits = 0
    for ct in two:
        if ct in seen: continue
        seen |= {ct, reflect(ct)}; orbits += 1
    span = sum(1 for ct in two if (0, 4) in ct[1])
    each2 = all(two_frees(*inst[ct]) for ct in two)
    print(f"canonical types: {len(type_sf)}; single: {len(single)}; two-swap-only: {len(two)}")
    print(f"reflection orbits among residual: {orbits}; carry spanning chord (0,4): {span}/{len(two)}")
    print(f"split stable across seeds: {stable}; each residual type freed by a 2-swap: {each2}")
    print("the 7:")
    for ct in two:
        cols, e = ct
        cc = Counter(cols); dc = [c for c, k in cc.items() if k == 2][0]
        g = tuple(i for i, c in enumerate(cols) if c == dc)
        longs = sorted((i, j) for (i, j) in e if j - i > 1)
        print(f"   cols={cols} dbl@{g} longs={longs} span={(0,4) in e}")
    print(f"PASS: {len(type_sf)==104 and len(two)==7 and orbits==4 and stable and each2}")


if __name__ == "__main__":
    main()
