#!/usr/bin/env python3
"""
Toy 5600 — THE IN-FRAME ONE-WORD TEST: every stuck coloring of every
5-connected triangulation (plantri -c5) at every degree-5 vertex,
n = 12..21 — does a fully-legal family word give a direct exit (a
color absent at v)? The 3-word hitting set (5595) is tried first; the
full 186-family only where the three fail. Then: the 3-word set's
in-frame hitting record, and whether the in-frame hitting set grows.

This is OWL measured IN THE FRAME where a minimal counterexample
lives (internally 6-connected ⟹ 5-connected). 5596 found the frame
has stuck colorings (tens of thousands by n = 21); 5591/5593/5598
tested OWL only out-of-frame.

Per n: (T,v) pairs, stuck colorings, hit by the 3 words, hit by the
full family (of the remainder), NOT hit (kill candidates, exhibited),
no-context (role_map None). Records hashed before the counts.

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


OF = load("t5598ow", "toy_5598_SEP2_out_of_frame_poussin_kittell_every_deg5"
          "_vertex_stuck_one_word_class.py")
IF, EA, G5, X3, LG, E1, WF = OF.IF, OF.EA, OF.G5, OF.X3, OF.LG, OF.E1, OF.WF

THREE = [(('B2', ('r', 's_j')), ('B1', ('r', 's_i'))),
         (('B2', ('r', 's_i')), ('B1', ('r', 's_j'))),
         (('n_sM', ('r', 's_M')), ('n_si', ('s_M', 's_i')))]


def direct_by(adj, tv, lcyc, c0, wordlist):
    rm = WF.role_map(adj, c0, tv, lcyc)
    if rm is None:
        return None
    vmap, cmap = rm
    hits = []
    for w in wordlist:
        m1 = (tuple(sorted((cmap[w[0][1][0]], cmap[w[0][1][1]]))), vmap[w[0][0]])
        m2 = (tuple(sorted((cmap[w[1][1][0]], cmap[w[1][1][1]]))), vmap[w[1][0]])
        k, fl = LG.legal_commutator(adj, c0, m1, m2, tv)
        if all(fl) and G5.is_proper(adj, k, skip=tv) and len({k[u] for u in adj[tv]}) < 4:
            hits.append(w)
    return hits


if __name__ == "__main__":
    ns = [int(x) for x in sys.argv[1:]] or list(range(12, 22))
    print("=" * 70)
    print(f"Toy 5600 — in-frame one-word test, plantri -c5, n = {ns}")
    print("=" * 70)
    moves, words, _ = WF.context_family()
    others = [w for w in words if w not in THREE]
    grand = Counter()
    kills = []
    hitwords = Counter()
    for n in ns:
        gs = EA.plantri_graphs(n, flags=('-c5',))
        t0 = time.time()
        cnt = Counter()
        recs = []
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
                cnt['pairs'] += 1
                for ct in cols:
                    c0 = {u: ct[pos[u]] for u in order}
                    if not IF.stuck(adj, v, c0):
                        continue
                    cnt['stuck'] += 1
                    h3 = direct_by(adj, v, lcyc, c0, THREE)
                    if h3 is None:
                        cnt['no-context'] += 1
                        recs.append((gi, v, ct, 'no-context'))
                        continue
                    if h3:
                        cnt['hit3'] += 1
                        for w in h3:
                            hitwords[w] += 1
                        recs.append((gi, v, ct, 'hit3'))
                        continue
                    hf = direct_by(adj, v, lcyc, c0, others)
                    if hf:
                        cnt['hitfull'] += 1
                        for w in hf:
                            hitwords[w] += 1
                        recs.append((gi, v, ct, 'hitfull', str(hf[:2])))
                    else:
                        cnt['NOT-HIT'] += 1
                        recs.append((gi, v, ct, 'NOT-HIT'))
                        kills.append((n, gi, v, ct))
        hh = hashlib.sha256(json.dumps([str(r) for r in recs]).encode()).hexdigest()
        grand.update(cnt)
        print(f"  n={n}: graphs {len(gs)}; pairs {cnt['pairs']}; stuck {cnt['stuck']}; "
              f"hit by the 3 words {cnt['hit3']}; hit by the rest of the family {cnt['hitfull']}; "
              f"NOT HIT {cnt['NOT-HIT']}; no-context {cnt['no-context']}; records sha256 {hh[:16]}  "
              f"[{time.time() - t0:.0f}s]", flush=True)
    print(f"\n  GRAND: stuck {grand['stuck']}; hit3 {grand['hit3']}; hitfull {grand['hitfull']}; "
          f"NOT HIT {grand['NOT-HIT']}; no-context {grand['no-context']}")
    print(f"  ONE-WORD in-frame: {grand['hit3'] + grand['hitfull']}/{grand['stuck']}")
    print(f"  words used beyond the three (top 10): "
          f"{[(w, c) for w, c in hitwords.most_common() if w not in THREE][:10]}")
    for k in kills[:20]:
        print(f"    KILL CANDIDATE: {k}")
    json.dump({'grand': dict(grand), 'kills': [str(k) for k in kills]},
              open(os.path.join(HERE, '.in_frame_one_word.json'), 'w'), indent=1)
