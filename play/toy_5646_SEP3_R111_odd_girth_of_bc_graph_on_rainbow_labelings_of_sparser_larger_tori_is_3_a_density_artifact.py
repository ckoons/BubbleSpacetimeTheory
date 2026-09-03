#!/usr/bin/env python3
"""
Toy (odd girth beyond the dense regime) — Grace, 2026-09-03.  Toy 5643 found the shortest odd cycle of the b∪c graph
is ALWAYS 3 on non-bipartite cases at n = 10, 11 genus 2 — but those graphs have mean degree ~7 and triangles
everywhere.  One line is derivable: an a-free triangle has V-holonomy in {b, c} (labels from {b,c} only: sums b or c),
so it forces im[l] ⊄ <a>; on the SPHERE every non-facial triangle bounds a disc, its labels sum to 0, hence it is
rainbow and T_a = 0 always.  The converse (im ⊄ <a> ⟹ some a-free TRIANGLE exists) is what "local" means, and it may be
a density artifact.  Test on sparser, larger TORI (degree 6): enumerate rainbow labelings directly (backtracking over
edges, every face {1,2,3}); for each labeling and label a with im ⊄ <a>, the odd girth of the b∪c graph.
Populations: Mohar–Salas T(6,3) (n=18), T(9,3) (n=27, sampled labelings), T(6,6) (n=36, sampled); flip-family
tori n = 10 (all 4-colorable, exhaustive labelings).  Report the odd-girth histogram; kill of "local" = odd girth
>= 5 appearing with positive share as the graphs get sparser/larger.
"""
import os, sys, json, time, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib
t = importlib.import_module('toy_5627_SEP2_E2_bundle_law_torus_test_completions_per_sign_record_mod_A4_with_sphere_disc_controls')
t43 = importlib.import_module('toy_5643_SEP3_R111_sign_negation_pairs_on_realized_records_and_odd_girth_of_the_bc_graph_on_theta_clean_records')
HERE = os.path.dirname(os.path.abspath(__file__)); T0 = time.time(); random.seed(5646)

def rainbow_labelings(faces, cap=None):
    """all edge labelings in {1,2,3} with every face rainbow (backtracking); if cap, a random sample of size cap
    obtained by randomized branching order with restarts (not uniform; a sample, labeled as such)."""
    E = sorted({frozenset((f[i], f[(i+1)%3])) for f in faces for i in range(3)}, key=lambda e: sorted(e))
    idx = {e: i for i, e in enumerate(E)}
    face_edges = [[idx[frozenset((f[i], f[(i+1)%3]))] for i in range(3)] for f in faces]
    edge_faces = [[] for _ in E]
    for fi, fe in enumerate(face_edges):
        for e in fe: edge_faces[e].append(fi)
    lab = [0] * len(E); out = []
    def ok(e):
        for fi in edge_faces[e]:
            ls = [lab[x] for x in face_edges[fi]]
            if len({l for l in ls if l}) != sum(1 for l in ls if l): return False
        return True
    order = list(range(len(E)))
    def rec(i):
        if cap and len(out) >= cap: return
        if i == len(E): out.append({E[k]: lab[k] for k in range(len(E))}); return
        e = order[i]; ch = [1, 2, 3]
        if cap: random.shuffle(ch)
        for l in ch:
            lab[e] = l
            if ok(e): rec(i + 1)
            lab[e] = 0
    rec(0)
    return out

def v_image_and_girths(faces, n, lab):
    adj = t.adjacency(faces)
    import importlib as _il
    w = _il.import_module('toy_5630_SEP2_E2_tower_of_covers_derived_from_holonomy_on_flip_family_tori_floor1_floor2_occupancy')
    parent = w.spanning_tree(adj)
    def val(cyc):
        s = 0
        for i in range(len(cyc)): s ^= lab[frozenset((cyc[i], cyc[(i+1) % len(cyc)]))]
        return s
    volt = w.voltages_from_cycle_function(faces, adj, parent, val, 0, lambda x: x)
    img = {0}
    for v in volt.values(): img |= {x ^ v for x in img}
    res = {}
    for a in (1, 2, 3):
        og = t43.odd_girth(n, t43.bc_graph_edges(faces, lab, a))
        res[a] = og
        assert (og is None) == (img <= {0, a}), "T_a=0 <=> im in <a> failed"   # bipartite iff image in <a>
    return sorted(img), res

def scan(name, faces, n, cap=None):
    labs = rainbow_labelings(faces, cap)
    h = Counter()
    for lab in labs:
        img, res = v_image_and_girths(faces, n, lab)
        for a, og in res.items():
            if og is not None: h[og] += 1
        h[('image', len(img))] += 1
    tot = sum(v for k, v in h.items() if isinstance(k, int))
    print(f"  {name}: n={n} F={len(faces)} labelings {len(labs)}{' (sample)' if cap else ''}; image sizes {dict((k[1],v) for k,v in h.items() if isinstance(k,tuple))}; "
          f"odd girth over non-bipartite (labeling,label) pairs: {dict(sorted((k,v) for k,v in h.items() if isinstance(k,int)))}; share(girth 3) = {h[3]/tot if tot else float('nan'):.4f}   [{time.time()-T0:.0f}s]")
    return {str(k): v for k, v in h.items()}

def main():
    out = {}
    fam = t.torus_family(10)
    done = 0
    for key, faces in fam[10].items():
        if not t.all_4colorings(t.adjacency(faces), 10): continue
        out[f'flip10_{done}'] = scan(f"flip torus n=10 #{done}", faces, 10); done += 1
        if done >= 6: break
    for a, b, cap in ((6, 3, None), (9, 3, 20000), (6, 6, 20000), (12, 3, 20000), (9, 6, 20000)):
        faces, n = t.ms_torus(a, b)
        out[f'T{a}x{b}'] = scan(f"T({a},{b})", faces, n, cap)
    json.dump(out, open(os.path.join(HERE, '.out_' + os.path.basename(__file__).split('_')[1] + '.json'), 'w'), indent=1)
    print("SCORE: REPORTED — T_a=0 <=> im in <a> asserted on every (labeling,label); odd-girth histograms by size/density")

if __name__ == '__main__':
    main()
