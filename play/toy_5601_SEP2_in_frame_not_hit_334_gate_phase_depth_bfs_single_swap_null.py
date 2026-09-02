#!/usr/bin/env python3
"""
Toy 5601 — THE 334 IN-FRAME NOT-HIT CONFIGURATIONS: gate-phase exit,
word-depth, and the single-swap null

5600 first pass: 334 stuck colorings of 5-connected triangulations
(n = 17, 19, 20, 21) have NO fully-legal family word whose image has a
color absent at v. Three questions, in order, on every one of them:
 (a) GATE: does some fully-legal family word give an image with
     tau <= 5 (one swap from insertable) — K1838's leaf (G)?
 (b) DEPTH: BFS over fully-legal family words (re-deriving the
     canonical context at every stuck node; a non-stuck node is an
     exit) — minimal number of words to reach direct/gate exit, up to
     depth 3; frontier capped.
 (c) NULL: does ANY single Kempe swap (any seed, any pair) give a
     gate-phase image? And any single swap a direct exit?
Exhibit the deepest.

Elie, 2026-09-02.
"""

import importlib.util
import json
import os
import time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


OW = load("t5600k", "toy_5600_SEP2_in_frame_one_word_test_5connected_three_word"
          "_set_then_full_family.py")
OF, IF, EA, G5, X3, LG, E1, WF = OW.OF, OW.IF, OW.EA, OW.G5, OW.X3, OW.LG, OW.E1, OW.WF


def legal_images(adj, tv, lcyc, c0, words):
    rm = WF.role_map(adj, c0, tv, lcyc)
    if rm is None:
        return None
    vmap, cmap = rm
    out = []
    for w in words:
        m1 = (tuple(sorted((cmap[w[0][1][0]], cmap[w[0][1][1]]))), vmap[w[0][0]])
        m2 = (tuple(sorted((cmap[w[1][1][0]], cmap[w[1][1][1]]))), vmap[w[1][0]])
        k, fl = LG.legal_commutator(adj, c0, m1, m2, tv)
        if all(fl) and G5.is_proper(adj, k, skip=tv) and k != c0:
            out.append((w, k))
    return out


def direct(adj, tv, k):
    return len({k[u] for u in adj[tv]}) < 4


def gate(adj, tv, k):
    return direct(adj, tv, k) or G5.operational_tau(adj, k, tv) <= 5


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5601 — the 334 in-frame not-hit configurations")
    print("=" * 70)
    moves, words, _ = WF.context_family()
    kills = [eval(k) for k in json.load(open(os.path.join(HERE, '.in_frame_one_word.json')))['kills']]
    graphs = {}
    rows = []
    t0 = time.time()
    for n, gi, v, ct in kills:
        if (n, gi) not in graphs:
            gs = EA.plantri_graphs(n, flags=('-c5',))
            graphs[(n, gi)] = gs[gi]
        adj = graphs[(n, gi)]
        faces, ok = OF.faces_of(adj)
        order = sorted(u for u in adj if u != v)
        pos = {u: i for i, u in enumerate(order)}
        c0 = {u: ct[pos[u]] for u in order}
        lcyc = E1.link_cycle(faces, v)
        assert IF.stuck(adj, v, c0)
        imgs = legal_images(adj, v, lcyc, c0, words)
        n_legal = len(imgs)
        g1 = sum(1 for w, k in imgs if gate(adj, v, k))
        d1 = sum(1 for w, k in imgs if direct(adj, v, k))
        # single-swap null
        nA = gA = dA = 0
        for u in order:
            a = c0[u]
            for b in range(4):
                if b == a:
                    continue
                comp = G5.kempe_chain(adj, c0, u, a, b, exclude={v})
                k = G5.do_swap(c0, comp, a, b)
                if k == c0:
                    continue
                nA += 1
                gA += gate(adj, v, k)
                dA += direct(adj, v, k)
        # BFS over fully-legal words to depth 3
        depth = None
        frontier = [c0]
        seen = {tuple(c0[u] for u in order)}
        for dpt in range(1, 4):
            nxt = []
            for c in frontier:
                im = legal_images(adj, v, lcyc, c, words)
                if im is None:
                    continue
                for w, k in im:
                    if direct(adj, v, k):
                        depth = (dpt, 'direct')
                        break
                    if gate(adj, v, k) and depth is None:
                        depth = (dpt, 'gate')
                        break
                    key = tuple(k[u] for u in order)
                    if key not in seen and len(nxt) < 400:
                        seen.add(key)
                        nxt.append(k)
                if depth:
                    break
            if depth or not nxt:
                break
            frontier = nxt
        rows.append({'n': n, 'gi': gi, 'v': v, 'legal': n_legal, 'gate1': g1, 'direct1': d1,
                     'nullA': nA, 'null_gate': gA, 'null_direct': dA, 'depth': depth,
                     'explored': len(seen)})
    print(f"  {len(rows)} configurations processed [{time.time() - t0:.0f}s]")
    ga = sum(1 for r in rows if r['gate1'] > 0)
    print(f"\n  (a) GATE-PHASE exit by one fully-legal word (tau<=5): {ga}/{len(rows)}; "
          f"direct (must be 0): {sum(1 for r in rows if r['direct1'] > 0)}; legal images per config "
          f"{dict(sorted(Counter(r['legal'] for r in rows).items()))}")
    dd = Counter(r['depth'] for r in rows)
    print(f"\n  (b) WORD-DEPTH to exit (fully-legal words, canonical context re-derived per node): {dict(dd)}")
    print(f"      by n: { {n: dict(Counter(r['depth'] for r in rows if r['n']==n)) for n in sorted({r['n'] for r in rows})} }")
    print(f"\n  (c) SINGLE-SWAP NULL: some single Kempe swap reaches gate phase {sum(1 for r in rows if r['null_gate']>0)}/{len(rows)}; "
          f"reaches a direct exit {sum(1 for r in rows if r['null_direct']>0)}/{len(rows)}; swaps per config median "
          f"{sorted(r['nullA'] for r in rows)[len(rows)//2]}")
    worst = [r for r in rows if r['depth'] is None]
    print(f"\n  NOT REACHED within depth 3 (frontier-capped): {len(worst)}")
    for r in worst[:10]:
        print(f"    {r}")
    deep = sorted(rows, key=lambda r: (r['depth'] is None, r['depth'][0] if r['depth'] else 9), reverse=True)[:6]
    for r in deep:
        print(f"    deepest: {r}")
    json.dump(rows, open(os.path.join(HERE, '.in_frame_334.json'), 'w'), indent=1)
