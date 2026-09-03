#!/usr/bin/env python3
"""
Toy (a-free non-facial triangles) — follow-on to toy 5643 (Grace, 2026-09-03): the small-V-image obstruction on a
theta-clean record is a NON-FACIAL triangle carrying no a-edge (odd girth 3 on every non-bipartite b∪c graph).  Count
it: per theta-clean record and per label a, the number of non-facial triangles of the triangulation with no a-edge
(T_a); the record's V-image is <= <a> iff T_a = 0 (b∪c bipartite) — asserted per record as the check.  Then the
population statement Cal (b) needs: the distribution of the triangulation's NON-FACIAL TRIANGLE COUNT (a record-free
graph invariant) on the 63 colorable vs the 40 non-colorable 11-vertex genus-2 members, and the per-record mean of
min_a T_a.  If the non-colorable members carry more non-facial triangles, the depletion is a graph statement.
"""
import os, sys, json, time, itertools
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib
m = importlib.import_module('toy_5635_SEP2_R108_genus_two_census_footprint_image_of_Phi_histogram_and_12_sheet_one_floor_witness_lutz_865')
t5643 = importlib.import_module('toy_5643_SEP3_R111_sign_negation_pairs_on_realized_records_and_odd_girth_of_the_bc_graph_on_theta_clean_records')
t = m.t
HERE = os.path.dirname(os.path.abspath(__file__)); T0 = time.time()

def nonfacial_triangles(faces, adj):
    F = {frozenset(f) for f in faces}
    tri = set()
    for u in adj:
        for v in adj[u]:
            if v <= u: continue
            for w in adj[u] & adj[v]:
                if w <= v: continue
                s = frozenset((u, v, w))
                if s not in F: tri.add(s)
    return tri

def run(members, label):
    g = dict(m.parse_lutz(os.path.join(m.LUTZ, 'manifolds_lex_d2_n11_o1_g2.txt')))
    ntri = []; minTa = []; checks = 0; recs_n = 0
    for k in members:
        faces = m.orient(g[k]); adj = t.adjacency(faces); tri = nonfacial_triangles(faces, adj); ntri.append(len(tri))
        for r, lab in t5643.theta_clean_records(faces, 11):
            Ta = []
            for a in (1, 2, 3):
                Ta.append(sum(1 for s in tri if all(lab[frozenset(e)] != a for e in itertools.combinations(sorted(s), 2))))
            # check: T_a == 0  <=>  b∪c bipartite (odd girth None)
            for a, ta in zip((1, 2, 3), Ta):
                og = t5643.odd_girth(11, t5643.bc_graph_edges(faces, lab, a))
                assert (ta == 0) == (og is None), (k, a, ta, og)
            checks += 1; minTa.append(min(Ta)); recs_n += 1
    print(f"[{label}] {len(members)} members: non-facial triangles per triangulation min/median/max = {min(ntri)}/{sorted(ntri)[len(ntri)//2]}/{max(ntri)}; "
          f"theta-clean records {recs_n}; per-record min_a T_a histogram {dict(sorted(Counter(minTa).items()))}; "
          f"share(min_a T_a = 0) = {sum(1 for x in minTa if x == 0)/recs_n:.4f}; T_a = 0 <=> bipartite checked on {checks} records   [{time.time()-T0:.0f}s]")
    return dict(ntri=ntri, minTa_hist=dict(Counter(minTa)), records=recs_n)

def main():
    col = json.load(open(os.path.join(HERE, '.genus2_n11_colorable_subset_5638.json')))['colorable']
    non = [r['k'] for r in json.load(open(os.path.join(HERE, '.genus2_n11_sweep_5638_noncol.json')))]
    out = dict(colorable=run(col, 'colorable 63'), noncolorable=run(non, 'non-colorable 40'))
    json.dump(out, open(os.path.join(HERE, '.out_' + os.path.basename(__file__).split('_')[1] + '.json'), 'w'), indent=1)
    print("SCORE: PASS — T_a = 0 <=> bipartite on every record; population counts reported")

if __name__ == '__main__':
    main()
