#!/usr/bin/env python3
"""Toy 5708 — K1852-C (a): 5664a's unrestricted plain-swap depth (verbatim functions, MAXD=4, CAP=60000) on the hashed 1,171
two-word lock witnesses at n = 25 (.in_frame_1171_two_word_locked_n25.json), the second instrument against Grace 5666's
{1: 100, 2: 426, 3: 629, 4: 16}. Prediction (hashed in the post before this run): Grace's column, unreached 0."""
import importlib.util, glob, os, json, time, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location("t5664a", glob.glob(os.path.join(HERE, "toy_5664a_*.py"))[0])
T = importlib.util.module_from_spec(sp); sp.loader.exec_module(T)
W = json.load(open(os.path.join(HERE, '.in_frame_1171_two_word_locked_n25.json')))
print(f"population: {len(W)} two-word locks at n = 25; MAXD={T.MAXD} CAP={T.CAP}", flush=True)
t0 = time.time(); graphs = {}; dist = Counter(); rows = []
for i, x in enumerate(W):
    n, gi, v, ct = x['n'], x['graph_index_plantri_c5'], x['v'], x['coloring_mod_S4_sorted_order']
    if (n, gi) not in graphs: graphs[(n, gi)] = T.EA.plantri_graphs(n, flags=('-c5',))[gi]
    adj = graphs[(n, gi)]; order = sorted(u for u in adj if u != v)
    c0 = {u: ct[k] for k, u in enumerate(order)}
    d, ex = T.depth(adj, v, c0, order); dist[d] += 1; rows.append((n, gi, v, d, ex))
    if (i + 1) % 200 == 0: print(f"   {i+1}/{len(W)}: {dict(sorted(dist.items(), key=lambda kv: (kv[0] is None, kv[0])))}  [{time.time()-t0:.0f}s]", flush=True)
col = {k: dist.get(k, 0) for k in (1, 2, 3, 4)}; unreached = dist.get(None, 0)
grace = {1: 100, 2: 426, 3: 629, 4: 16}
print(f"\nRESULT depth column on the 1,171: {col}; unreached {unreached}; Grace 5666: {grace}; MATCH: {col == grace and unreached == 0}  [{time.time()-t0:.0f}s]")
json.dump({'column': col, 'unreached': unreached, 'rows': rows}, open(os.path.join(HERE, '.unrestricted_depth_1171_n25.json'), 'w'))
