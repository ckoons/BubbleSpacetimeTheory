#!/usr/bin/env python3
"""
Toy (genus-2 theta-class histogram) — Cal §829 B: under the Hom-with-multiplicity (Dijkgraaf–Witten) null the theta
classes are NOT equidistributed: N_{theta=0} : N_{theta=c!=0} = 256 : 64 = 4 : 1 per nonzero class, share(theta=0) =
256/5376 = 0.0476; a Z3-cohomology null says 1 : 1 (share 1/81 = 0.0123).  Pre-registered direction of the finite-size
deviation (Cal): toward trivial holonomy, share(theta=0) > 0.0476.  Grace, 2026-09-02, first K genus-2 triangulations
of Lutz's 865 (toy 5635 instrument).  theta class = the Z3 voltage vector on the 27 fundamental cycles of a spanning
tree (they generate H_1, so equal vectors <=> equal class in H^1(Sigma_2; Z3) = Z3^4, 81 classes); V class likewise for
the theta = 0 records (H^1(Sigma_2; V) = V^4, 256 classes).
"""
import os, sys, time, json
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib
m = importlib.import_module('toy_5635_SEP2_R108_genus_two_census_footprint_image_of_Phi_histogram_and_12_sheet_one_floor_witness_lutz_865')
t, w = m.t, m.w
HERE = os.path.dirname(os.path.abspath(__file__)); T0 = time.time()
K = int(sys.argv[1]) if len(sys.argv) > 1 else 5

def main():
    g2 = m.parse_lutz(os.path.join(m.LUTZ, 'manifolds_lex_d2_n10_o1_g2.txt'))
    out = []
    for k, tris in g2[:K]:
        faces = m.orient(tris); adj = t.adjacency(faces); rot = t.rotation_system(faces); parent = w.spanning_tree(adj)
        nontree = sorted({(min(u, v), max(u, v)) for u in adj for v in adj[u] if parent.get(v) != u and parent.get(u) != v})
        recs = m.closed_records(faces, 10)
        th = Counter(); vc = Counter()
        for r in recs:
            vec = []
            for (u, v) in nontree:
                cyc = w.cycle_from(parent, u, v)
                vec.append(w.holonomy_z3(faces, r, w.fattened_dual_walk(faces, rot, cyc)))
            th[tuple(vec)] += 1
            if not any(vec):
                lab, obs = t.propagate_labels(faces, r); assert not obs
                vv = []
                for (u, v) in nontree:
                    cyc = w.cycle_from(parent, u, v); s = 0
                    for i in range(len(cyc)): s ^= lab[frozenset((cyc[i], cyc[(i + 1) % len(cyc)]))]
                    vv.append(s)
                vc[tuple(vv)] += 1
        zero = tuple([0] * len(nontree))
        n0 = th.get(zero, 0); nz = [c for cl, c in th.items() if cl != zero]
        share0 = n0 / len(recs); per_class = sum(nz) / 80
        row = dict(k=k, closed=len(recs), theta_classes_occupied=len(th), theta0=n0, share_theta0=share0,
                   nonzero_classes_occupied=len(nz), nonzero_total=sum(nz), per_nonzero_class_mean=per_class,
                   ratio_theta0_to_per_class=(n0 / per_class if per_class else None),
                   nonzero_class_counts_min_max=(min(nz), max(nz)) if nz else None,
                   V_classes_occupied_among_theta0=len(vc), V_class_counts=sorted(vc.values(), reverse=True))
        out.append(row)
        print(f"  g2 #{k}: closed {len(recs)}; theta classes occupied {len(th)}/81; theta=0: {n0} (share {share0:.4f}; null 0.0476, Z3-null 0.0123); "
              f"nonzero classes {len(nz)}/80, per-class mean {per_class:.1f} (min {min(nz)}, max {max(nz)}); ratio theta0 : per-nonzero-class = {n0/per_class:.2f} : 1 (null 4 : 1); "
              f"V classes among theta=0: {len(vc)}/256 with counts {sorted(vc.values(), reverse=True)[:8]}   [{time.time()-T0:.0f}s]")
    json.dump(out, open(os.path.join(HERE, '.genus2_theta_classes.json'), 'w'), indent=1)
    print("SCORE: REPORTED — Cal's 4:1 ratio and share(theta=0) measured on the first", K, "triangulations")

if __name__ == '__main__':
    main()
