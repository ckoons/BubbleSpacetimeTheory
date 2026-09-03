#!/usr/bin/env python3
"""
Toy 5651b — Cal §836(c): "two path systems, not one." 5651 tested tree-neutrality on 12 BFS trees (one per
dislocation root). Here: for every graph of the 5651 census, 5 RANDOM spanning trees of the branched double
cover (random edge order, union-find), seeded; neutral ⟺ all twelve dislocation lifts share the tree
potential. Witness = neutral under SOME tree with [c] ≠ 0. Also: for [c] ≠ 0 graphs, the fraction of the 17
path systems (12 BFS + 5 random) that are neutral. Elie, 2026-09-03.
"""
import importlib.util, os, sys, json, random, time
from collections import Counter, deque
HERE = os.path.dirname(os.path.abspath(__file__))
def load(nm, fn):
    sp = importlib.util.spec_from_file_location(nm, os.path.join(HERE, fn)); m = importlib.util.module_from_spec(sp)
    a = sys.argv; sys.argv = ['x', '12']; sp.loader.exec_module(m); sys.argv = a; return m
T = load('t5626', 'toy_5626_SEP2_E1_branched_cover_clause_height_lift_period_lattice_and_dislocation_centers_vs_n.py')
T44 = load('t5644', 'toy_5644_SEP3_R111_pentagon_adjacency_series_C46_C58_fullerene_duals_lattice_index_vs_Np_and_C70_replication.py')
T51 = load('t5651', 'toy_5651_SEP3_R113_class_census_without_colouring_c_class_and_tree_neutrality_C20_C60_all_and_IPR_C60_C100_sealed.py')
random.seed(5651)

def cover(rot):
    n = len(rot); faces = T.faces_of(rot); deg = [len(r) for r in rot]
    fidx = {}
    for i, F in enumerate(faces):
        for j in range(3): fidx[(F[j], F[(j + 1) % 3])] = i
    fan = [[fidx[(v, w)] for w in rot[v]] for v in range(n)]
    cv = {}; ncv = 0
    for v in range(n):
        for pos, fi in enumerate(fan[v]):
            for s in (1, -1):
                base = s * (1 if pos % 2 == 0 else -1); key = (v, 0) if deg[v] % 2 else (v, base)
                if key not in cv: cv[key] = ncv; ncv += 1
                cv[(v, fi, s)] = cv[key]
    edges = {}
    for i, F in enumerate(faces):
        for s in (1, -1):
            for j in range(3):
                u, v = F[j], F[(j + 1) % 3]; cu, cvv = cv[(u, i, s)], cv[(v, i, s)]; c = s % 3
                key, desc = ((u, v, s), (cu, cvv, c)) if u < v else ((v, u, -s), (cvv, cu, (-c) % 3))
                edges.setdefault(key, desc)
    lifts = [cv[(v, 0)] for v in range(n) if deg[v] % 2]
    return ncv, list(edges.values()), lifts

def random_tree_neutral(ncv, E, lifts):
    E = E[:]; random.shuffle(E)
    par = list(range(ncv))
    def find(x):
        while par[x] != x: par[x] = par[par[x]]; x = par[x]
        return x
    adj = [[] for _ in range(ncv)]
    for cu, cvv, c in E:
        a, b = find(cu), find(cvv)
        if a != b: par[a] = b; adj[cu].append((cvv, c)); adj[cvv].append((cu, (-c) % 3))
    phi = [None] * ncv
    for s0 in range(ncv):
        if phi[s0] is not None: continue
        phi[s0] = 0; dq = deque([s0])
        while dq:
            x = dq.popleft()
            for y, c in adj[x]:
                if phi[y] is None: phi[y] = (phi[x] + c) % 3; dq.append(y)
    return len({phi[l] for l in lifts}) == 1

if __name__ == '__main__':
    t0 = time.time(); rows = json.load(open(os.path.join(HERE, '.census_5651_sealed.json')))
    wit = []; frac = Counter(); ng = 0
    for m, ipr in sorted({(r['m'], r['ipr']) for r in rows}):
        gs = T44.fullgen_duals(m, ipr=ipr)
        for r in [x for x in rows if x['m'] == m and x['ipr'] == ipr]:
            ncv, E, lifts = cover(gs[r['idx']]); ng += 1
            neut = [random_tree_neutral(ncv, E, lifts) for _ in range(5)]
            tot = r['neutral_roots'] + sum(neut)
            if not r['class_zero']:
                frac[tot] += 1
                if any(neut): wit.append((m, r['idx'], sum(neut)))
            elif not all(neut): wit.append(('CLASS0-NOT-NEUTRAL', m, r['idx']))
    print(f'  {ng} graphs × 5 random spanning trees of the cover (+ the 12 BFS roots of 5651 = 17 path systems)')
    print(f'  [c] ≠ 0 graphs: number of neutral path systems out of 17 → graph count: {dict(sorted(frac.items()))}')
    print(f'  witnesses (neutral under some random tree with [c] ≠ 0, or class 0 not neutral): {wit[:10]} — count {len(wit)}')
    print(f'\nSCORE: {1 if not wit else 0}/1   [{time.time()-t0:.0f}s]')
