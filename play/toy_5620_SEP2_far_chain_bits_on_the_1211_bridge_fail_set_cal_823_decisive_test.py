#!/usr/bin/env python3
"""
Toy 5620 — Cal §823 item 4, the DECISIVE TEST pre-registered: the five
far-chain bits on the 1,211 BRIDGE-FAIL set (n <= 22; 5608/5611's
regeneration), which is NOT the locked set. Bits (far-copy seed rule,
5613's eight chains): F1 = alpha∩zeta ≠ ∅, F2 = beta∩eta ≠ ∅,
F3 = epsilon∩zeta ≠ ∅, F4 = epsilon∩eta ≠ ∅, F5 = (delta∩gamma ≠ ∅) ∨
(zeta∩eta ≠ ∅). If the condition holds on the bridge-fail set too, the
derivation should cite only Lemma T and the bridge words; if it fails
there, "locked" is doing work beyond the bridge words. Also reported:
the same bits on the 349 (must be 349/349 — the control) and on a
1-in-50 sample of all in-frame stuck colorings (the base rate).

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


TT = load("t5613fc", "toy_5613_SEP2_laneF_type_table_kittell_eight_chain"
          "_intersection_matrix.py")
H = load("t5611fc", "toy_5611_SEP2_H_cut_containment_cross_tab_93_and_bridge"
         "_fail_1211.py")
MF, K, OF, IF, EA, G5, E1, WF = TT.MF, TT.K, TT.OF, TT.IF, TT.EA, TT.G5, TT.E1, TT.WF
A, B, G_, D, E, Z, ETA, TH = range(8)


def bits(ch):
    f1 = bool(ch[A] & ch[Z]); f2 = bool(ch[B] & ch[ETA]); f3 = bool(ch[E] & ch[Z]); f4 = bool(ch[E] & ch[ETA])
    f5 = bool(ch[D] & ch[G_]) or bool(ch[Z] & ch[ETA])
    return (f1, f2, f3, f4, f5)


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5620 — far-chain bits on the bridge-fail set (decisive test)")
    print("=" * 70)
    t0 = time.time()
    # the 349 (control)
    wit = []
    for f in ('.in_frame_26_two_word_locked.json', '.in_frame_23_two_word_locked_n22.json',
              '.in_frame_44_two_word_locked_n23.json', '.in_frame_256_two_word_locked_n24.json'):
        wit += json.load(open(os.path.join(HERE, f)))
    graphs = {}
    cw = Counter()
    for W in wit:
        n, gi, v, ct = W['n'], W['graph_index_plantri_c5'], W['v'], W['coloring_mod_S4_sorted_order']
        if (n, gi) not in graphs:
            graphs[(n, gi)] = EA.plantri_graphs(n, flags=('-c5',))[gi]
        adj = graphs[(n, gi)]
        faces, ok = OF.faces_of(adj)
        order = sorted(u for u in adj if u != v)
        c0 = {u: ct[i] for i, u in enumerate(order)}
        lcyc = E1.link_cycle(faces, v)
        cw[bits(TT.eight_chains(adj, v, lcyc, c0))] += 1
    print(f"  CONTROL the 349: {dict(cw)}  (all-True required)  [{time.time()-t0:.0f}s]", flush=True)
    # bridge-fail set + base-rate sample, n = 12..22
    cb = Counter()
    cs = Counter()
    nb = 0
    nsamp = 0
    k = 0
    for n in range(12, 23):
        for gi, adj in enumerate(EA.plantri_graphs(n, flags=('-c5',))):
            faces, ok = OF.faces_of(adj)
            for v in adj:
                if len(adj[v]) != 5:
                    continue
                order = sorted(u for u in adj if u != v)
                pos = {u: i for i, u in enumerate(order)}
                sub = {u: {w for w in adj[u] if w != v} for u in adj if u != v}
                lcyc = E1.link_cycle(faces, v)
                for ct in EA.all_colorings_mod_s4(sub, order):
                    c0 = {u: ct[pos[u]] for u in order}
                    if not IF.stuck(adj, v, c0):
                        continue
                    k += 1
                    bf = MF.program(adj, v, lcyc, c0, MF.BRIDGE, MF.MIDDLE) == 'FAIL'
                    if bf or k % 50 == 0:
                        b = bits(TT.eight_chains(adj, v, lcyc, c0))
                        if bf:
                            cb[b] += 1
                            nb += 1
                        if k % 50 == 0:
                            cs[b] += 1
                            nsamp += 1
    allT = (True,) * 5
    print(f"\n  BRIDGE-FAIL SET ({nb}; 5608: 1,211): far-chain condition (F1..F4 all true) holds on "
          f"{sum(c for b, c in cb.items() if all(b[:4]))}/{nb}; all five bits {cb.get(allT, 0)}/{nb}")
    print(f"    patterns (F1,F2,F3,F4,F5): {dict(cb.most_common(8))}")
    print(f"  BASE RATE (1-in-50 sample of all in-frame stuck, {nsamp}): F1..F4 all true "
          f"{sum(c for b, c in cs.items() if all(b[:4]))}/{nsamp}; all five {cs.get(allT, 0)}/{nsamp}")
    print(f"    patterns: {dict(cs.most_common(8))}  [{time.time()-t0:.0f}s]")
