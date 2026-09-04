#!/usr/bin/env python3
"""Toy — confirmation of Grace 12:19 from my side: my 5601 depth-2 loop BREAKS on the first image that is
direct-or-gate, and gate ⊇ direct, so a gate-only image met earlier masks a later direct one and the
1,113/58 split is word-enumeration-order dependent. Here: scan EVERY depth-2 image, direct tested on all,
no break. Population: the 1,171 two-word locks at n = 25."""
import importlib.util, os, json, time, glob
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location("t5601", glob.glob(os.path.join(HERE, "toy_5601_SEP2_*.py"))[0])
T = importlib.util.module_from_spec(sp); sp.loader.exec_module(T)
OF, IF, EA, G5, E1, WF = T.OF, T.IF, T.EA, T.G5, T.E1, T.WF
legal_images, direct, gate = T.legal_images, T.direct, T.gate
t0 = time.time()
moves, words, _ = WF.context_family()
W = json.load(open(os.path.join(HERE, '.in_frame_1171_two_word_locked_n25.json')))
print(f"population: {len(W)} two-word locks at n = 25")
graphs = {}
res = Counter(); direct_list = []; per = []
for i, x in enumerate(W):
    n, gi, v, ct = x['n'], x['graph_index_plantri_c5'], x['v'], x['coloring_mod_S4_sorted_order']
    if (n, gi) not in graphs: graphs[(n, gi)] = EA.plantri_graphs(n, flags=('-c5',))[gi]
    adj = graphs[(n, gi)]; faces, ok = OF.faces_of(adj)
    order = sorted(u for u in adj if u != v); pos = {u: i2 for i2, u in enumerate(order)}
    c0 = {u: ct[pos[u]] for u in order}; lcyc = E1.link_cycle(faces, v)
    im1 = legal_images(adj, v, lcyc, c0, words) or []
    nd = ng = 0
    for w1, k1 in im1:                      # first word: by construction none is gate (these are the locks)
        if gate(adj, v, k1): continue
        im2 = legal_images(adj, v, lcyc, k1, words) or []
        for w2, k2 in im2:
            if direct(adj, v, k2): nd += 1
            elif gate(adj, v, k2): ng += 1
    kind = 'direct' if nd else ('gate-only' if ng else 'none')
    res[kind] += 1; per.append({'n': n, 'gi': gi, 'v': v, 'n_direct2': nd, 'n_gateonly2': ng})
    if nd: direct_list.append((n, gi, v))
    if (i + 1) % 200 == 0: print(f"   {i+1}/{len(W)}: {dict(res)}  [{time.time()-t0:.0f}s]", flush=True)
print(f"\nRESULT (every depth-2 image scanned, no break): {dict(res)}")
print(f"  configurations with at least one DIRECT two-word exit: {res['direct']}/{len(W)}")
print(f"  direct images per configuration: median {sorted(p['n_direct2'] for p in per)[len(per)//2]}, "
      f"min {min(p['n_direct2'] for p in per)}, max {max(p['n_direct2'] for p in per)}")
json.dump({'result': dict(res), 'per': per}, open(os.path.join(HERE, '.confirm_1171_direct_n25.json'), 'w'))
print(f"[{time.time()-t0:.0f}s]")
