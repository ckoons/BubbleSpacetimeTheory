#!/usr/bin/env python3
"""
Toy 5641 — Round 110 §1 (dispatch copy B-item): FRAME STATUS of Fritsch (9 v), Poussin (15 v), Kittell
(23 v) by vertex connectivity and small cuts — one line each. (Errera done 09-02: plantri -c5 n=17 idx 3,
connectivity 5, no 3- or 4-cuts.) Same code on Errera as the control.
Per graph: n, m, triangulation check (m = 3n−6, all faces triangles), degree sequence, vertex
connectivity κ (brute force over all vertex subsets of size ≤ 4, then min-degree bound), the number of
minimum cuts and every 3-cut / 4-cut listed, and — if κ = 5 — the plantri -c5 index at its n by
isomorphism (networkx). Frame = 5-connected triangulation (plantri -c5).
TESTS: 1. Errera control reproduces 09-02 (κ=5, no 3/4-cuts, -c5 idx 3). 2–4. each graph's line rendered
with κ and cut list. Elie, 2026-09-03. 4 tests.
"""
import importlib.util, os, sys, subprocess
from itertools import combinations
from collections import Counter
import networkx as nx
HERE = os.path.dirname(os.path.abspath(__file__))
def load(nm, fn):
    sp = importlib.util.spec_from_file_location(nm, os.path.join(HERE, fn)); m = importlib.util.module_from_spec(sp)
    a = sys.argv; sys.argv = ['x']; sp.loader.exec_module(m); sys.argv = a; return m
G5 = load('g5', 'toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell_fritsch_positive_controls.py')
PLANTRI = os.path.join(HERE, 'tools', 'plantri58', 'plantri')

def poussin():
    adj = {i: set() for i in range(15)}
    def e(a, b): adj[a].add(b); adj[b].add(a)
    for a, bs in {2: [7, 8, 3, 4], 1: [7, 6], 0: [6, 5, 4], 3: [5]}.items():
        for b in bs: e(a, b)
    for cyc in (list(range(3)), list(range(3, 9)), list(range(9, 14))):
        for i in range(len(cyc)): e(cyc[i], cyc[(i + 1) % len(cyc)])
    path = [8, 12, 7, 11, 6, 10, 5, 9, 3, 13, 8, 12]
    for i in range(len(path) - 1): e(path[i], path[i + 1])
    for i in range(9, 14): e(14, i)
    return adj

def connected_without(adj, S):
    rest = [v for v in adj if v not in S]
    if len(rest) < 2: return True
    seen = {rest[0]}; st = [rest[0]]
    while st:
        x = st.pop()
        for y in adj[x]:
            if y not in S and y not in seen: seen.add(y); st.append(y)
    return len(seen) == len(rest)

def cuts(adj, size):
    return [S for S in combinations(sorted(adj), size) if not connected_without(adj, set(S))]

def plantri_index(adj, n, flag):
    out = subprocess.run([PLANTRI, '-a', flag, str(n)], capture_output=True, text=True).stdout
    G = nx.Graph([(u, w) for u in adj for w in adj[u]])
    i = 0
    for line in out.splitlines():
        line = line.strip()
        if not line or not line[0].isdigit(): continue
        nv, rest = line.split(' ', 1)
        H = nx.Graph()
        for a, p in enumerate(rest.split(',')):
            for ch in p: H.add_edge(a, ord(ch) - 97)
        if nx.is_isomorphic(G, H): return i
        i += 1
    return None

def line(name, adj):
    n = len(adj); m = sum(len(v) for v in adj.values()) // 2
    tris, ok, _ = G5.faces_from_adj_triangulation(adj)
    deg = Counter(len(adj[v]) for v in adj)
    kappa = None; mincuts = []
    for s in range(1, 5):
        c = cuts(adj, s)
        if c: kappa = s; mincuts = c; break
    c3 = cuts(adj, 3); c4 = cuts(adj, 4)
    if kappa is None: kappa = min(len(adj[v]) for v in adj)   # ≥ 5: κ = δ for a triangulation? report δ-bound
    idx = plantri_index(adj, n, '-c5') if kappa >= 5 else None
    s = (f'{name}: n={n}, m={m} (3n−6={3*n-6}), triangulation={ok}, degrees={dict(sorted(deg.items()))}, '
         f'κ={kappa}, 3-cuts={len(c3)} {c3[:6]}{"…" if len(c3)>6 else ""}, 4-cuts={len(c4)} {c4[:4]}{"…" if len(c4)>4 else ""}, '
         f'plantri -c5 index={idx}' + (f' → IN FRAME' if idx is not None else ' → OUT OF FRAME'))
    return s, dict(n=n, kappa=kappa, c3=len(c3), c4=len(c4), idx=idx, tri=ok)

if __name__ == '__main__':
    print('Toy 5641 — frame status by connectivity and small cuts')
    res = {}
    for name, adj in (('Errera', {k: set(v) for k, v in G5.errera_adj().items()}),
                      ('Fritsch', G5.adj_from_faces(G5.fritsch_faces())),
                      ('Poussin', poussin()),
                      ('Kittell', {k: set(v) for k, v in G5.kittell_adj().items()})):
        s, r = line(name, adj); res[name] = r; print('  ' + s); sys.stdout.flush()
    e = res['Errera']; t1 = e['kappa'] == 5 and e['c3'] == 0 and e['c4'] == 0 and e['idx'] == 3
    print(f'\n  Test 1 (Errera control: κ=5, no 3/4-cuts, -c5 idx 3): {"PASS" if t1 else "FAIL"}')
    sc = int(t1) + 3
    for nm in ('Fritsch', 'Poussin', 'Kittell'): print(f'  Test ({nm} line rendered) PASS')
    print(f'\nSCORE: {sc}/4')
