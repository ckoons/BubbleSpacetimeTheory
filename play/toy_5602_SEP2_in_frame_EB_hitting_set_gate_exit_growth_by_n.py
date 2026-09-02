#!/usr/bin/env python3
"""
Toy 5602 — IN-FRAME E-B: the hitting set on the 5-connected census

For every stuck coloring of every -c5 triangulation, n = 12..21
(87,361), the HIT SET = fully-legal family words whose image is in
the gate phase (direct exit OR tau <= 5 — K1838's leaf I or G).
Minimum hitting set (exact branch-and-bound; bounds if capped) at word
and orbit level, per n and cumulative — does the in-frame hitting set
GROW with n? The 26 two-word-locked configurations (5601) have empty
hit sets by definition; they are excluded from the set-cover and
listed.

Elie, 2026-09-02.
"""

import hashlib
import importlib.util
import json
import os
import sys
import time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


K = load("t5601eb", "toy_5601_SEP2_in_frame_not_hit_334_gate_phase_depth_bfs"
         "_single_swap_null.py")
OW, OF, IF, EA, G5, X3, LG, E1, WF = K.OW, K.OF, K.IF, K.EA, K.G5, K.X3, K.LG, K.E1, K.WF
EB = load("t5595eb2", "toy_5595_SEP2_EB_hitting_set_minimum_words_growth"
          "_curve_pattern_table.py")


if __name__ == "__main__":
    ns = [int(x) for x in sys.argv[1:]] or list(range(12, 22))
    print("=" * 70)
    print(f"Toy 5602 — in-frame E-B, n = {ns}")
    print("=" * 70)
    moves, words, _ = WF.context_family()
    widx = {w: i for i, w in enumerate(words)}

    def mirror(w):
        def mm(m):
            role, pair = m
            role2 = {'B1': 'B2', 'B2': 'B1', 'n_si': 'n_sj', 'n_sj': 'n_si'}.get(role, role)
            pair2 = tuple(sorted({'s_i': 's_j', 's_j': 's_i'}.get(x, x) for x in pair))
            return (role2, pair2)
        return (mm(w[0]), mm(w[1]))
    orb_of = {}
    orbits = []
    for i, w in enumerate(words):
        if i in orb_of:
            continue
        j = widx[mirror(w)]
        orb_of[i] = orb_of[j] = len(orbits)
        orbits.append((i, j) if i != j else (i,))

    per_n = {}
    empty = []
    cum = []
    for n in ns:
        gs = EA.plantri_graphs(n, flags=('-c5',))
        t0 = time.time()
        hs = []
        for gi, adj in enumerate(gs):
            faces, ok = OF.faces_of(adj)
            for v in adj:
                if len(adj[v]) != 5:
                    continue
                order = sorted(u for u in adj if u != v)
                pos = {u: i for i, u in enumerate(order)}
                sub = {u: {w for w in adj[u] if w != v} for u in adj if u != v}
                cols = EA.all_colorings_mod_s4(sub, order)
                lcyc = E1.link_cycle(faces, v)
                for ct in cols:
                    c0 = {u: ct[pos[u]] for u in order}
                    if not IF.stuck(adj, v, c0):
                        continue
                    imgs = K.legal_images(adj, v, lcyc, c0, words)
                    h = frozenset(widx[w] for w, k in imgs if K.gate(adj, v, k))
                    if not h:
                        empty.append((n, gi, v))
                    hs.append(h)
        hh = hashlib.sha256(json.dumps([sorted(h) for h in hs]).encode()).hexdigest()
        nonempty = [h for h in hs if h]
        s_w, set_w, ex_w = EB.min_hitting_set(nonempty, len(words))
        s_o, set_o, ex_o = EB.min_hitting_set([frozenset(orb_of[i] for i in h) for h in nonempty], len(orbits))
        cum.extend(nonempty)
        s_c, set_c, ex_c = EB.min_hitting_set(cum, len(words))
        per_n[n] = (len(hs), len(hs) - len(nonempty), s_w, ex_w, s_o, ex_o, s_c, ex_c)
        print(f"  n={n}: stuck {len(hs)}; empty hit sets {len(hs)-len(nonempty)}; hit-set sizes median "
              f"{sorted(len(h) for h in nonempty)[len(nonempty)//2] if nonempty else 0}; "
              f"MIN HITTING SET word {s_w}{'' if ex_w else '(bound)'} orbit {s_o}{'' if ex_o else '(bound)'}; "
              f"CUMULATIVE word {s_c}{'' if ex_c else '(bound)'} = {[words[i] for i in set_c]}; "
              f"hash {hh[:12]}  [{time.time()-t0:.0f}s]", flush=True)
    print(f"\n  empty hit sets (two-word-locked, 5601): {len(empty)} {empty[:30]}")
    print(f"  curve (n: stuck, empty, min_word, exact, min_orbit, exact, cum_word, exact): {per_n}")
