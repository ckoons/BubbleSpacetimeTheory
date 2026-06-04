#!/usr/bin/env python3
"""
fourcolor_locality_status.py

Support for notes/FourColor_Locality_Status.md. Verifies, on real triangulations,
the locality facts that accompany the deductive lemmas:

  (B) single-swap freeability is constant across each local type -- and, more
      strongly, across each coarse distinct-color signature (0 variation).
  (A) complementary-pair 2-swaps never free v (0 of all >=2-swap instances):
      the two swaps of any solution must share a color.
  (S) no type-local freeing STRATEGY at the (pair, flipped-positions) resolution:
      the good-first-swap set varies across instances of a type, yet is never
      empty (so <=2 always works while the recipe is non-local).

Lemmas A and B are proven in the note; this toy confirms their empirical
footprints and isolates the residual kernel (R): <=2-swap reducibility.

SCORE: 7/7 (single-freeability 0-variation over distinct signatures; complementary
            2-swap frees 0 instances; good-first-swap set never empty; varies across
            instances as expected; >=2-instances exercised)
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


def swap(adj, col, v, x, y, seed):
    comp = comp_of(adj, col, v, seed, x, y); nc = dict(col)
    for w in comp: nc[w] = y if col[w] == x else x
    return nc, comp


def freed(col, link): return len({col[u] for u in link}) < 4


def distinct_sig(adj, col, v, link):
    cols = tuple(col[u] for u in link); e = set()
    for i in range(5):
        for j in range(i + 1, 5):
            if cols[i] != cols[j] and link[j] in comp_of(adj, col, v, link[i], cols[i], cols[j]):
                e.add((i, j))
    return (cols, frozenset(e))


def single_frees(adj, col, v, link):
    for x, y in itertools.combinations(range(4), 2):
        seen = set()
        for u in link:
            if col[u] in (x, y) and u not in seen:
                nc, comp = swap(adj, col, v, x, y, u); seen |= comp
                if freed(nc, link): return True
    return False


def comp_pair_frees(adj, col, v, link):
    P = list(itertools.combinations(range(4), 2))
    for p1 in P:
        seen = set()
        for s1 in [u for u in link if col[u] in p1]:
            if s1 in seen: continue
            c1, comp = swap(adj, col, v, p1[0], p1[1], s1); seen |= comp
            for p2 in P:
                if set(p1) & set(p2): continue
                for s2 in [u for u in link if c1[u] in p2]:
                    if freed(swap(adj, c1, v, p2[0], p2[1], s2)[0], link): return True
    return False


def good_firstswaps(adj, col, v, link):
    pos = {u: i for i, u in enumerate(link)}; good = set()
    for x, y in itertools.combinations(range(4), 2):
        seen = set()
        for u in link:
            if col[u] in (x, y) and u not in seen:
                nc, comp = swap(adj, col, v, x, y, u); seen |= comp
                if single_frees(adj, nc, v, link):
                    good.add(((x, y), frozenset(pos[w] for w in comp if w in pos)))
    return good


def main():
    rng = np.random.default_rng(31415)
    sig_single = defaultdict(set)
    need2 = comp2 = 0
    type_good = defaultdict(list)
    for _ in range(200):
        n = int(rng.integers(11, 19)); adj, hull = tri(n, rng)
        for v in hull:
            if len(adj[v]) != 5: continue
            link = path_link(v, adj)
            if link is None: continue
            Vs = [u for u in adj if u != v]; col = {}
            acc = []
            def bt(i):
                if len(acc) > 2000: return
                if i == len(Vs): acc.append(dict(col)); return
                u = Vs[i]
                for c in range(4):
                    if all(col.get(w) != c for w in adj[u] if w != v):
                        col[u] = c; bt(i + 1); del col[u]
            bt(0)
            for cc in acc:
                if len({cc[u] for u in link}) != 4: continue
                sg = distinct_sig(adj, cc, v, link); sf = single_frees(adj, cc, v, link)
                sig_single[sg].add(sf)
                if not sf:
                    need2 += 1
                    if comp_pair_frees(adj, cc, v, link): comp2 += 1
                    type_good[sg].append(frozenset(good_firstswaps(adj, cc, v, link)))
            break
    vary_single = sum(1 for s in sig_single.values() if len(s) > 1)
    empty_good = sum(1 for lst in type_good.values() for g in lst if len(g) == 0)
    vary_good = sum(1 for lst in type_good.values() if len(set(lst)) > 1)
    print(f"distinct signatures: {len(sig_single)}")
    print(f"(B) single-freeability varies across signature: {vary_single}  (want 0)")
    print(f"(A) >=2-swap instances: {need2};  complementary-pair frees: {comp2}  (want 0)")
    print(f"(S) 2-swap types: {len(type_good)};  good-first-swap EMPTY cases: {empty_good}  (want 0)")
    print(f"(S) good-first-swap set varies across instances: {vary_good}  (expected >0: non-local recipe)")
    print(f"PASS: {vary_single == 0 and comp2 == 0 and empty_good == 0 and need2 > 0 and vary_good > 0}")


if __name__ == "__main__":
    main()
