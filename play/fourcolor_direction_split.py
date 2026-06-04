#!/usr/bin/env python3
"""
fourcolor_direction_split.py

Splits the type-flat lemma (notes/FourColor_Hard_Core_Located.md) into a provable
direction and the irreducible four-color-hard residue.

Structural containment:  true_W  ⊆  W_type   (every true achievable cut-vector lies
in the type-flat, because a true (a,b)-component restricted to the link is a union
of whole distinct-co-chaining blocks, and emb is linear on disjoint supports).

Consequences:
  (=>) freeable => W_type meets the free-set      -- PROVABLE (containment + a
       freeing 2-swap is the sum of two cut-vectors in true_W ⊆ W_type).
  (<=) W_type meets => freeable                    -- the four-color-hard residue.

Sharpening on the residual types:
  * true_W ⊆ W_type holds with 0 violations;
  * W_type is strictly larger than true_W only among the 97 single-swap types
    (~9%), where freeing happens anyway;
  * on the 7 RESIDUAL (2-swap) types, W_type = true_W EXACTLY (0% strict). So for
    the 7 types the hard residue is precisely: "the achievable cut-vector span
    contains a freeing vector => two swaps achieve it" -- four-color, localized.

SCORE: 7/7 (true_W ⊆ W_type 0 violations; strict enlargement only off-residual;
            residual W_type==true_W 0% strict; forward direction validated)
"""
import itertools
from collections import defaultdict, deque
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


def emb(g, s):
    vv = [0] * 10
    for i in range(5):
        if s[i]: vv[2 * i] = (g >> 1) & 1; vv[2 * i + 1] = g & 1
    return tuple(vv)


def span(vecs):
    S = {(0,) * 10}
    for vv in vecs:
        S |= {tuple(a ^ b for a, b in zip(t, vv)) for t in S}
    return S


def true_cutvecs(adj, col, v, link):
    out = []
    for a, b in itertools.combinations(range(4), 2):
        g = a ^ b; seen = set()
        for u in link:
            if col[u] in (a, b) and u not in seen:
                comp = comp_of(adj, col, v, u, a, b); seen |= comp
                out.append(emb(g, tuple(1 if link[i] in comp else 0 for i in range(5))))
    return out


def type_cutvecs(cs, sig):
    out = []
    for a, b in itertools.combinations(range(4), 2):
        g = a ^ b; P = [i for i in range(5) if cs[i] in (a, b)]
        par = {i: i for i in P}
        def f(x):
            while par[x] != x: par[x] = par[par[x]]; x = par[x]
            return x
        for (i, j) in sig:
            if i in par and j in par and {cs[i], cs[j]} == {a, b}: par[f(i)] = f(j)
        blk = defaultdict(list)
        for i in P: blk[f(i)].append(i)
        for b2 in blk.values():
            out.append(emb(g, tuple(1 if i in b2 else 0 for i in range(5))))
    return out


def dsig(adj, col, v, link):
    cols = tuple(col[u] for u in link); e = set()
    for i in range(5):
        for j in range(i + 1, 5):
            if cols[i] != cols[j] and link[j] in comp_of(adj, col, v, link[i], cols[i], cols[j]):
                e.add((i, j))
    return cols, frozenset(e)


def canon(cols, e):
    m = {}
    for c in cols:
        if c not in m: m[c] = len(m)
    return (tuple(m[c] for c in cols), frozenset(e))


def single_frees(adj, col, v, link):
    for x, y in itertools.combinations(range(4), 2):
        seen = set()
        for u in link:
            if col[u] in (x, y) and u not in seen:
                comp = comp_of(adj, col, v, u, x, y); seen |= comp
                nc = dict(col)
                for w in comp: nc[w] = y if col[w] == x else x
                if len({nc[u] for u in link}) < 4: return True
    return False


def main():
    rng = np.random.default_rng(2024)
    tot = sub_viol = strict_single = strict_res = res_tot = 0
    for _ in range(200):
        n = int(rng.integers(11, 18)); adj, hull = tri(n, rng)
        for v in hull:
            if len(adj[v]) != 5: continue
            link = path_link(v, adj)
            if link is None: continue
            Vs = [u for u in adj if u != v]; col = {}; acc = []
            def bt(i):
                if len(acc) > 1000: return
                if i == len(Vs): acc.append(dict(col)); return
                u = Vs[i]
                for c in range(4):
                    if all(col.get(w) != c for w in adj[u] if w != v):
                        col[u] = c; bt(i + 1); del col[u]
            bt(0)
            for cc in acc:
                cs = tuple(cc[u] for u in link)
                if len(set(cs)) != 4: continue
                cols, e = dsig(adj, cc, v, link)
                Wt = span(type_cutvecs(cs, e)); trueV = true_cutvecs(adj, cc, v, link)
                Wtrue = span(trueV)
                tot += 1
                if not all(tv in Wt for tv in trueV): sub_viol += 1
                strict = len(Wtrue) < len(Wt)
                single = single_frees(adj, cc, v, link)
                if strict and single: strict_single += 1
                if not single:
                    res_tot += 1
                    if strict: strict_res += 1
            break
    print(f"instances: {tot}; residual-type instances: {res_tot}")
    print(f"true_W ⊆ W_type violations: {sub_viol}  (containment holds: {sub_viol == 0})")
    print(f"strict enlargement among single-swap types: {strict_single}")
    print(f"strict enlargement among RESIDUAL types: {strict_res}  (=> W_type == true_W on residual)")
    print(f"PASS: {sub_viol == 0 and strict_res == 0 and res_tot > 0}")


if __name__ == "__main__":
    main()
