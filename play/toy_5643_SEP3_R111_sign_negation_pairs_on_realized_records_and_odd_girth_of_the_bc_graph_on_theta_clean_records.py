#!/usr/bin/env python3
"""
Toy 5643 — Round 111 §3 and §5 (Grace, 2026-09-03).
§3 (Keeper's one-line derivation, checked): an ODD colour permutation negates every face sign, so realized records come
in ± pairs and N_realized = 2 × (colourings mod S4).  Check on the 63 colorable 11-vertex genus-2 members: the realized
record set is closed under global negation, and N_realized == 2 * colourings/24.
§5 (Lyra 07:21, existence check): for a theta-clean record with rainbow labeling l, the b∪c graph (edges whose label is
not a) is bipartite iff im[l] ⊆ <a>.  Count, per theta-clean record and per label a, the shortest odd cycle (odd girth)
of the b∪c graph; report the histogram of the minimum over a: LOCAL (≤ 5) vs LONG (≥ 7) vs bipartite (none).  If the
suppression of small V-images is local, most records show an odd cycle of length ≤ 5.
Populations: n = 11 colorable (63, theta-clean 4,694 records) and n = 10 non-colorable (Lutz's first 30, theta-clean).
Control: on the sphere (plantri n = 8) every theta-clean record is realized, so im = 1 and ALL THREE b∪c graphs are
bipartite (odd girth = none) — asserted.
"""
import os, sys, json, time
from collections import Counter, deque
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib
m = importlib.import_module('toy_5635_SEP2_R108_genus_two_census_footprint_image_of_Phi_histogram_and_12_sheet_one_floor_witness_lutz_865')
t = m.t
HERE = os.path.dirname(os.path.abspath(__file__)); T0 = time.time()

def odd_girth(n, edges):
    """shortest odd cycle length in the graph (vertices 0..n-1); None if bipartite."""
    adj = {v: set() for v in range(n)}
    for u, v in edges: adj[u].add(v); adj[v].add(u)
    best = None
    for root in range(n):
        dist = {root: 0}; q = deque([root])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if w not in dist: dist[w] = dist[u] + 1; q.append(w)
        for u in dist:
            for w in adj[u]:
                if w in dist and dist[u] == dist[w]:       # same level => odd cycle of length <= 2*dist+1
                    L = dist[u] + dist[w] + 1
                    if best is None or L < best: best = L
    return best

def bc_graph_edges(faces, lab, a):
    E = set()
    for (u, v, w) in faces:
        for x, y in ((u, v), (v, w), (w, u)):
            e = frozenset((x, y))
            if lab[e] != a: E.add(tuple(sorted((x, y))))
    return list(E)

def theta_clean_records(faces, n):
    out = []
    for r in m.closed_records(faces, n):
        lab, obs = t.propagate_labels(faces, r)
        if not obs: out.append((r, lab))
    return out

def odd_girth_table(faces, n, recs):
    h = Counter()
    for r, lab in recs:
        gs = [odd_girth(n, bc_graph_edges(faces, lab, a)) for a in (1, 2, 3)]
        finite = [g for g in gs if g is not None]
        key = 'bipartite-for-some-label' if len(finite) < 3 else ('local<=5' if min(finite) <= 5 else f'long>={min(finite)}')
        h[key] += 1
        h[('min odd girth', min(finite) if finite else None)] += 1
    return h

def main():
    # control: sphere n = 8
    faces = t.plantri_triangulations(8)[0]; recs = theta_clean_records(faces, 8)
    for r, lab in recs:
        assert all(odd_girth(8, bc_graph_edges(faces, lab, a)) is None for a in (1, 2, 3)), "sphere b∪c graph not bipartite"
    print(f"[control sphere n=8] {len(recs)} theta-clean records: all three b∪c graphs bipartite — PASS   [{time.time()-T0:.0f}s]")
    # §3: sign-negation pairs on the 63 colorable n = 11
    g = dict(m.parse_lutz(os.path.join(m.LUTZ, 'manifolds_lex_d2_n11_o1_g2.txt')))
    sub = json.load(open(os.path.join(HERE, '.genus2_n11_colorable_subset_5638.json')))['colorable']
    ok = 0; tot = 0; hist = Counter(); H = Counter()
    for k in sub:
        faces = m.orient(g[k]); adj = t.adjacency(faces)
        cols = t.all_4colorings(adj, 11)
        recs = {t.record(faces, c) for c in cols}
        neg = {tuple(-z for z in r) for r in recs}
        closed_under_negation = (neg == recs)
        n_orbits_S4 = len(cols) // 24
        ok += (closed_under_negation and len(recs) == 2 * n_orbits_S4); tot += 1
        hist[(len(cols), len(recs), n_orbits_S4)] += 1
        H.update(odd_girth_table(faces, 11, theta_clean_records(faces, 11)))
    print(f"[§3 sign-negation pairs, n=11 colorable] {ok}/{tot} members: realized records closed under negation AND N_realized = 2·(colourings/24); (colourings, realized, S4-orbits) histogram {dict(hist)}   [{time.time()-T0:.0f}s]")
    print(f"[§5 odd girth of b∪c on theta-clean records, n=11 colorable] {dict(sorted(((str(k),v) for k,v in H.items())))}   [{time.time()-T0:.0f}s]")
    # §5 on n = 10 non-colorable, first 30
    g10 = m.parse_lutz(os.path.join(m.LUTZ, 'manifolds_lex_d2_n10_o1_g2.txt'))[:30]
    H10 = Counter()
    for k, tris in g10:
        faces = m.orient(tris); H10.update(odd_girth_table(faces, 10, theta_clean_records(faces, 10)))
    print(f"[§5 odd girth, n=10 non-colorable, first 30] {dict(sorted(((str(k),v) for k,v in H10.items())))}   [{time.time()-T0:.0f}s]")
    json.dump(dict(sign_pairs_ok=ok, members=tot, hist={str(k): v for k, v in hist.items()},
                   odd_girth_n11={str(k): v for k, v in H.items()}, odd_girth_n10={str(k): v for k, v in H10.items()}),
              open(os.path.join(HERE, '.out_5643.json'), 'w'), indent=1)
    print("SCORE:", "PASS" if ok == tot else "FAIL", "— §3 check; §5 reported")

if __name__ == '__main__':
    main()
