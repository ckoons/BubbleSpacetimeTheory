#!/usr/bin/env python3
"""
Toy 5608 — MIDDLE-FIRST, measured in frame: Casey's ranging shot as a
two-word PROGRAM — first the middle canonical word (n_sM,(r,s_M))·
(n_si,(s_M,s_i)) or its mirror, then, in the image's own canonical
frame, a bridge word (B1,(r,s_i))(B2,(r,s_j)) or its mirror — on every
stuck coloring of every 5-connected triangulation n = 12..22, and on
the 93 two-word-locked witnesses. Compared with the reverse order
(bridge first, then middle) and with "any fully-legal word then any".

Per configuration: EXIT-1 = the first word already reaches the gate
phase (direct or tau <= 5); EXIT-2 = the second word does, in the
image's frame; FAIL = neither orientation/branch exits within two.
Words are applied only when fully legal (Lemma L covers the bridge
words; the middle word carries SJ — its legality is measured here).

Elie, 2026-09-02.
"""

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


K = load("t5601mf", "toy_5601_SEP2_in_frame_not_hit_334_gate_phase_depth_bfs"
         "_single_swap_null.py")
OF, IF, EA, G5, X3, LG, E1, WF = K.OF, K.IF, K.EA, K.G5, K.X3, K.LG, K.E1, K.WF

MIDDLE = [(('n_sM', ('r', 's_M')), ('n_si', ('s_M', 's_i'))),
          (('n_sM', ('r', 's_M')), ('n_sj', ('s_M', 's_j')))]
BRIDGE = [(('B1', ('r', 's_i')), ('B2', ('r', 's_j'))),
          (('B1', ('r', 's_j')), ('B2', ('r', 's_i'))),
          (('B2', ('r', 's_j')), ('B1', ('r', 's_i'))),
          (('B2', ('r', 's_i')), ('B1', ('r', 's_j')))]


def apply(adj, tv, lcyc, c, wordlist):
    """Images of the fully-legal words of wordlist at c (frame re-derived)."""
    rm = WF.role_map(adj, c, tv, lcyc)
    if rm is None:
        return []
    vmap, cmap = rm
    out = []
    for w in wordlist:
        m1 = (tuple(sorted((cmap[w[0][1][0]], cmap[w[0][1][1]]))), vmap[w[0][0]])
        m2 = (tuple(sorted((cmap[w[1][1][0]], cmap[w[1][1][1]]))), vmap[w[1][0]])
        k, fl = LG.legal_commutator(adj, c, m1, m2, tv)
        if all(fl) and G5.is_proper(adj, k, skip=tv) and k != c:
            out.append((w, k))
    return out


def program(adj, tv, lcyc, c0, first, second):
    im1 = apply(adj, tv, lcyc, c0, first)
    if not im1:
        return 'no-legal-first'
    if any(K.gate(adj, tv, k) for w, k in im1):
        return 'exit-1'
    for w, k in im1:
        im2 = apply(adj, tv, lcyc, k, second)
        if any(K.gate(adj, tv, k2) for w2, k2 in im2):
            return 'exit-2'
    return 'FAIL'


if __name__ == "__main__":
    ns = [int(x) for x in sys.argv[1:]] or list(range(12, 23))
    print("=" * 70)
    print(f"Toy 5608 — MIDDLE-FIRST in frame, n = {ns}, and the 93")
    print("=" * 70)
    # the 93 witnesses first
    wit = []
    for f in ('.in_frame_26_two_word_locked.json', '.in_frame_23_two_word_locked_n22.json',
              '.in_frame_44_two_word_locked_n23.json'):
        wit += json.load(open(os.path.join(HERE, f)))
    graphs = {}
    cw = Counter()
    cwr = Counter()
    for W in wit:
        n, gi, v, ct = W['n'], W['graph_index_plantri_c5'], W['v'], W['coloring_mod_S4_sorted_order']
        if (n, gi) not in graphs:
            graphs[(n, gi)] = EA.plantri_graphs(n, flags=('-c5',))[gi]
        adj = graphs[(n, gi)]
        faces, ok = OF.faces_of(adj)
        order = sorted(u for u in adj if u != v)
        c0 = {u: ct[i] for i, u in enumerate(order)}
        lcyc = E1.link_cycle(faces, v)
        cw[program(adj, v, lcyc, c0, MIDDLE, BRIDGE)] += 1
        cwr[program(adj, v, lcyc, c0, BRIDGE, MIDDLE)] += 1
    print(f"\n  THE 93 WITNESSES — middle-then-bridge: {dict(cw)}; bridge-then-middle: {dict(cwr)}", flush=True)

    grand = Counter()
    grandr = Counter()
    fails = []
    for n in ns:
        gs = EA.plantri_graphs(n, flags=('-c5',))
        t0 = time.time()
        cnt = Counter()
        cntr = Counter()
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
                    r = program(adj, v, lcyc, c0, MIDDLE, BRIDGE)
                    cnt[r] += 1
                    if r == 'FAIL' or r == 'no-legal-first':
                        fails.append((n, gi, v, ct, r))
                    cntr[program(adj, v, lcyc, c0, BRIDGE, MIDDLE)] += 1
        grand.update(cnt)
        grandr.update(cntr)
        print(f"  n={n}: stuck {sum(cnt.values())}; MIDDLE-then-BRIDGE {dict(cnt)}; BRIDGE-then-MIDDLE {dict(cntr)}  [{time.time()-t0:.0f}s]", flush=True)
    tot = sum(grand.values())
    print(f"\n  GRAND n={ns[0]}..{ns[-1]}: stuck {tot}; middle-then-bridge exits within two: "
          f"{grand['exit-1'] + grand['exit-2']}/{tot} (exit-1 {grand['exit-1']}, exit-2 {grand['exit-2']}, "
          f"no-legal-first {grand['no-legal-first']}, FAIL {grand['FAIL']}); bridge-then-middle: "
          f"{grandr['exit-1'] + grandr['exit-2']}/{tot} (FAIL {grandr['FAIL']})")
    for f in fails[:15]:
        print(f"    middle-first failure: {f}")
    json.dump({'grand': dict(grand), 'grandr': dict(grandr), 'fails': [str(f) for f in fails]},
              open(os.path.join(HERE, '.middle_first.json'), 'w'), indent=1)
