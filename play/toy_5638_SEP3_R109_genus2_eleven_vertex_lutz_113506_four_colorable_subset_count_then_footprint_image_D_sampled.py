#!/usr/bin/env python3
"""
Toy 5638 — ROUND 109 item 3 (Grace, 2026-09-03): Lutz's 11-vertex orientable genus-2 census (tools/lutz/
manifolds_lex_d2_n11_o1_g2.txt, 113,506 entries; Lutz arXiv math/0610022).  Stage 1 (`count`): the 4-colorable
subset — count it, save the indices and coloring counts.  Stage 2 (`sweep K`): on K sampled 4-colorable members
(fixed prefix of the subset), exhaustive over 2^26 records: footprint / |image Phi| histogram / theta-class ratio /
D = log2(N_closed / N_realized).  Controls through the same code (toy 5635): sphere image 1 only; torus never 12.
Pre-registered by Cal (blind, K1851-A §4 second pass) — I run, I do not read his numbers first.
"""
import os, sys, json, time
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib
m = importlib.import_module('toy_5635_SEP2_R108_genus_two_census_footprint_image_of_Phi_histogram_and_12_sheet_one_floor_witness_lutz_865')
t, w = m.t, m.w
HERE = os.path.dirname(os.path.abspath(__file__)); T0 = time.time()
F11 = os.path.join(m.LUTZ, 'manifolds_lex_d2_n11_o1_g2.txt')
SUB = os.path.join(HERE, '.genus2_n11_colorable_subset_5638.json')

def has_4col(adj, n):
    verts = sorted(adj, key=lambda v: -len(adj[v])); col = {}
    def rec(i):
        if i == n: return True
        v = verts[i]; used = {col[u] for u in adj[v] if u in col}
        for c in range(4):
            if c not in used:
                col[v] = c
                if rec(i + 1): return True
                del col[v]
        return False
    return rec(0)

def count():
    g = m.parse_lutz(F11); assert len(g) == 113506, len(g)
    sub = []
    for i, (k, tris) in enumerate(g):
        faces = m.orient(tris); adj = t.adjacency(faces)
        if has_4col(adj, 11): sub.append(k)
        if i % 10000 == 0: print(f"  scanned {i}, colorable so far {len(sub)}   [{time.time()-T0:.0f}s]", flush=True)
    json.dump(dict(total=len(g), colorable=sub), open(SUB, 'w'))
    print(f"4-COLORABLE 11-vertex genus-2 triangulations: {len(sub)} of {len(g)}   [{time.time()-T0:.0f}s]")

def theta_ratio(faces, n, recs):
    adj = t.adjacency(faces); rot = t.rotation_system(faces); parent = w.spanning_tree(adj)
    nontree = sorted({(min(u, v), max(u, v)) for u in adj for v in adj[u] if parent.get(v) != u and parent.get(u) != v})
    th = Counter()
    for r in recs:
        vec = tuple(w.holonomy_z3(faces, r, w.fattened_dual_walk(faces, rot, w.cycle_from(parent, u, v))) for (u, v) in nontree)
        th[vec] += 1
    zero = tuple([0] * len(nontree)); n0 = th.get(zero, 0); nz = [c for cl, c in th.items() if cl != zero]
    return n0, len(nz), (sum(nz) / 80 if nz else 0)

def sweep(K, noncol=False):
    g = dict(m.parse_lutz(F11)); colset = set(json.load(open(SUB))['colorable'])
    sub = ([k for k in sorted(g) if k not in colset][::max(1, (len(g) - len(colset)) // K)][:K]) if noncol else json.load(open(SUB))['colorable'][:K]
    out = []
    for k in sub:
        faces = m.orient(g[k]); adj = t.adjacency(faces)
        cols = t.all_4colorings(adj, 11)
        r = m.analyse(faces, 11, -2); r['k'] = k; r['colorings'] = len(cols)
        recs = m.closed_records(faces, 11)
        n0, nzc, per = theta_ratio(faces, 11, recs)
        real = r['footprint'].get('realized', 0)
        r.update(theta0=n0, nonzero_classes=nzc, per_class=per, ratio=(n0 / per if per else None),
                 D=(__import__('math').log2(r['closed'] / real) if real else None))
        out.append(r)
        print(f"  n11 g2 #{k}: colorings {len(cols)} closed {r['closed']} {r['footprint']} image {r['image_hist']} "
              f"theta0 {n0} ratio {r['ratio'] and round(r['ratio'],2)}:1 D {r['D'] and round(r['D'],3)} one-floor fails {r['one_floor_failures']}   [{time.time()-T0:.0f}s]", flush=True)
        json.dump(out, open(os.path.join(HERE, '.genus2_n11_sweep_5638' + ('_noncol' if noncol else '') + '.json'), 'w'), indent=1)
    im = Counter(); fp = Counter()
    for r in out: im.update({int(a): b for a, b in r['image_hist'].items()}); fp.update(r['footprint'])
    tot = sum(im.values()) or 1
    print(f"[n=11 genus 2, {len(out)} colorable triangulations] footprint {dict(fp)} image shares {{k: round(v/tot,4) for k,v in sorted(im.items())}} "
          f"Mednykh {{1: 0.0002, 2: 0.0084, 3: 0.0595, 4: 0.0391, 12: 0.8929}}")
    print("SCORE: REPORTED")

if __name__ == '__main__':
    (count if sys.argv[1] == 'count' else lambda: sweep(int(sys.argv[2]), noncol=(sys.argv[1] == 'noncol')))()
