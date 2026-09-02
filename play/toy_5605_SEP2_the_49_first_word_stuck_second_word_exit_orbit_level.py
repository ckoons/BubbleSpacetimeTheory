#!/usr/bin/env python3
"""
Toy 5605 — THE 49 TWO-WORD-LOCKED WITNESSES: which first words produce
a stuck image, which second words exit, at orbit level

For each of the 49 (n <= 21: 26; n = 22: 23): every fully-legal
family word w1 (in c0's canonical frame) -> image; classify the image
(direct / gate / stuck). For every STUCK image, re-derive the
canonical frame of the image and find every fully-legal w2 whose
image is direct or gate. Report: per witness, the multiset of
(orbit(w1) -> {orbit(w2)}) pairs that exit at depth 2; aggregated
over the 49 at mirror-orbit level; the first-word orbits that NEVER
lead to an exit in two; and whether the first-word images fall into
one or few canonical link types.

Elie, 2026-09-02.
"""

import importlib.util
import json
import os
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


K = load("t5601w", "toy_5601_SEP2_in_frame_not_hit_334_gate_phase_depth_bfs"
         "_single_swap_null.py")
OF, IF, EA, G5, X3, LG, E1, WF = K.OF, K.IF, K.EA, K.G5, K.X3, K.LG, K.E1, K.WF


def mirror(w):
    def mm(m):
        role, pair = m
        role2 = {'B1': 'B2', 'B2': 'B1', 'n_si': 'n_sj', 'n_sj': 'n_si'}.get(role, role)
        pair2 = tuple(sorted({'s_i': 's_j', 's_j': 's_i'}.get(x, x) for x in pair))
        return (role2, pair2)
    return (mm(w[0]), mm(w[1]))


def orb(w):
    return min(str(w), str(mirror(w)))


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5605 — the 49: first-word / second-word anatomy at orbit level")
    print("=" * 70)
    moves, words, _ = WF.context_family()
    wit = json.load(open(os.path.join(HERE, '.in_frame_26_two_word_locked.json'))) + \
        json.load(open(os.path.join(HERE, '.in_frame_23_two_word_locked_n22.json')))
    graphs = {}
    agg_pairs = Counter()
    agg_w1_stuck = Counter()
    agg_w1_exit = Counter()
    per_wit = []
    for W in wit:
        n, gi, v, ct = W['n'], W['graph_index_plantri_c5'], W['v'], W['coloring_mod_S4_sorted_order']
        if (n, gi) not in graphs:
            graphs[(n, gi)] = EA.plantri_graphs(n, flags=('-c5',))[gi]
        adj = graphs[(n, gi)]
        faces, ok = OF.faces_of(adj)
        order = sorted(u for u in adj if u != v)
        c0 = {u: ct[i] for i, u in enumerate(order)}
        lcyc = E1.link_cycle(faces, v)
        imgs = K.legal_images(adj, v, lcyc, c0, words)
        w1_kinds = Counter()
        pairs = set()
        exiting_w1 = set()
        for w1, k1 in imgs:
            if K.gate(adj, v, k1):
                w1_kinds['gate!'] += 1      # must be 0 for a witness
                continue
            w1_kinds['stuck'] += 1
            agg_w1_stuck[orb(w1)] += 1
            im2 = K.legal_images(adj, v, lcyc, k1, words)
            if im2 is None:
                w1_kinds['no-context'] += 1
                continue
            ex = [w2 for w2, k2 in im2 if K.gate(adj, v, k2)]
            if ex:
                exiting_w1.add(orb(w1))
                for w2 in ex:
                    pairs.add((orb(w1), orb(w2)))
        for p in pairs:
            agg_pairs[p] += 1
        for o in exiting_w1:
            agg_w1_exit[o] += 1
        per_wit.append((n, gi, v, dict(w1_kinds), len(exiting_w1), len(pairs)))
    print(f"\n  {len(wit)} witnesses; per witness (n, graph, v, first-word kinds, #first-word orbits "
          f"leading to a 2-word exit, #(w1-orbit, w2-orbit) exit pairs):")
    for r in per_wit:
        print(f"    {r}")
    print(f"\n  first-word orbits producing a STUCK image (count over witnesses × words): "
          f"{len(agg_w1_stuck)} orbits")
    print(f"  first-word orbits that lead to a two-word exit, by #witnesses: ")
    for o, c in agg_w1_exit.most_common():
        print(f"    {c:3d}  {o}")
    never = [o for o in agg_w1_stuck if o not in agg_w1_exit]
    print(f"  first-word orbits that NEVER lead to an exit in two (over all 49): {len(never)}")
    print(f"\n  (w1-orbit -> w2-orbit) exit pairs, by #witnesses (top 25 of {len(agg_pairs)}):")
    for p, c in agg_pairs.most_common(25):
        print(f"    {c:3d}  {p[0]}  ->  {p[1]}")
    json.dump({'pairs': [(p[0], p[1], c) for p, c in agg_pairs.most_common()],
               'w1_exit': agg_w1_exit.most_common()},
              open(os.path.join(HERE, '.the49_word_anatomy.json'), 'w'), indent=1)
