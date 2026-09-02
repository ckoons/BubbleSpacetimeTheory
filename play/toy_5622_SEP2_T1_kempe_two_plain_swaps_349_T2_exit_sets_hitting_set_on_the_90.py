#!/usr/bin/env python3
"""
Toy 5622 — ROUND 103. T1: Kempe's two swaps as PLAIN sequential swaps
(not commutators), both orders, on all 349 locks: after ζ then η, or η
then ζ (ζ = (r,s_i) at B1, η = (r,s_j) at B2 — Kempe's Gadget 5_2 pair,
far-copy seeds), is a colour absent at v? Also the adjacent-seed pair
(δ at B2, γ at B1) both orders, and the four mixed pairs. Count
insertions (direct) and gate-phase (τ<=5) images.
T2: the 90 far-bit-off bridge-fail configurations (5620: bridge-fail
with NOT(F1∧F2∧F3∧F4)): every fully-legal word with a direct/gate
exit; per-orbit exit counts; the exact minimum hitting set at word and
orbit level; the set of words present in EVERY configuration's exit
set (candidates for Lyra's named word).

Elie, 2026-09-02.
"""

import importlib.util
import itertools
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


FC = load("t5620t", "toy_5620_SEP2_far_chain_bits_on_the_1211_bridge_fail_set_cal"
          "_823_decisive_test.py")
TT, H, MF, K, OF, IF, EA, G5, E1, WF = FC.TT, FC.H, FC.MF, FC.K, FC.OF, FC.IF, FC.EA, FC.G5, FC.E1, FC.WF
EB = load("t5595t", "toy_5595_SEP2_EB_hitting_set_minimum_words_growth_curve"
          "_pattern_table.py")


def seeds(adj, tv, lcyc, c):
    vmap, cmap = WF.role_map(adj, c, tv, lcyc)
    r, sM, si, sj = cmap['r'], cmap['s_M'], cmap['s_i'], cmap['s_j']
    nsi, nsj = vmap['n_si'], vmap['n_sj']
    copies = [vmap['B1'], vmap['B2']]
    B2 = next(b for b in copies if nsi in adj[b])
    B1 = next(b for b in copies if b != B2)
    return {'zeta': ((r, si), B1), 'eta': ((r, sj), B2), 'delta': ((r, si), B2), 'gamma': ((r, sj), B1)}


def two_swaps(adj, tv, c, m_a, m_b):
    cur = c
    for (a, b), s in (m_a, m_b):
        if cur[s] not in (a, b):
            return None
        ch = G5.kempe_chain(adj, cur, s, a, b, exclude={tv})
        cur = G5.do_swap(cur, ch, a, b)
    return cur


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5622 — T1 Kempe's two plain swaps on the 349; T2 the 90")
    print("=" * 70)
    t0 = time.time()
    moves, words, _ = WF.context_family()
    wit = []
    for f in ('.in_frame_26_two_word_locked.json', '.in_frame_23_two_word_locked_n22.json',
              '.in_frame_44_two_word_locked_n23.json', '.in_frame_256_two_word_locked_n24.json'):
        wit += json.load(open(os.path.join(HERE, f)))
    graphs = {}
    t1 = Counter()
    pairs = [('zeta', 'eta'), ('eta', 'zeta'), ('delta', 'gamma'), ('gamma', 'delta'),
             ('zeta', 'gamma'), ('gamma', 'zeta'), ('delta', 'eta'), ('eta', 'delta')]
    for W in wit:
        n, gi, v, ct = W['n'], W['graph_index_plantri_c5'], W['v'], W['coloring_mod_S4_sorted_order']
        if (n, gi) not in graphs:
            graphs[(n, gi)] = EA.plantri_graphs(n, flags=('-c5',))[gi]
        adj = graphs[(n, gi)]
        faces, ok = OF.faces_of(adj)
        order = sorted(u for u in adj if u != v)
        c0 = {u: ct[i] for i, u in enumerate(order)}
        lcyc = E1.link_cycle(faces, v)
        sd = seeds(adj, v, lcyc, c0)
        for a, b in pairs:
            img = two_swaps(adj, v, c0, sd[a], sd[b])
            if img is None:
                t1[(a, b, 'illegal-2nd')] += 1
                continue
            direct = len({img[u] for u in adj[v]}) < 4
            gate = direct or G5.operational_tau(adj, img, v) <= 5
            t1[(a, b, 'direct' if direct else ('gate' if gate else 'stuck'))] += 1
    print(f"\n  T1 — two PLAIN swaps on the 349 (pair, order → outcome):")
    for a, b in pairs:
        print(f"    {a:5s} then {b:5s}: direct {t1[(a,b,'direct')]:3d}  gate {t1[(a,b,'gate')]:3d}  stuck {t1[(a,b,'stuck')]:3d}  2nd-illegal {t1[(a,b,'illegal-2nd')]:3d}")
    print(f"  [{time.time()-t0:.0f}s]", flush=True)

    # T2 — regenerate the 90
    ninety = []
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
                    if MF.program(adj, v, lcyc, c0, MF.BRIDGE, MF.MIDDLE) != 'FAIL':
                        continue
                    b = FC.bits(TT.eight_chains(adj, v, lcyc, c0))
                    if all(b[:4]):
                        continue
                    ninety.append((n, gi, v, ct, adj, lcyc, c0, order, b))
    print(f"\n  T2 — far-bit-off bridge-fail configurations regenerated: {len(ninety)} (5620: 90)  [{time.time()-t0:.0f}s]")
    widx = {w: i for i, w in enumerate(words)}
    hs = []
    per_orb = Counter()
    empty = 0
    for n, gi, v, ct, adj, lcyc, c0, order, b in ninety:
        imgs = K.legal_images(adj, v, lcyc, c0, words)
        h = frozenset(widx[w] for w, k in imgs if K.gate(adj, v, k))
        hs.append(h)
        if not h:
            empty += 1
        for i in h:
            per_orb[H.orb(words[i])] += 1
    common = set.intersection(*[set(h) for h in hs if h]) if hs else set()
    s_w, set_w, ex_w = EB.min_hitting_set([h for h in hs if h], len(words))
    orbits = sorted({H.orb(w) for w in words})
    oidx = {o: i for i, o in enumerate(orbits)}
    s_o, set_o, ex_o = EB.min_hitting_set([frozenset(oidx[H.orb(words[i])] for i in h) for h in hs if h], len(orbits))
    print(f"  exit-set sizes: min {min(len(h) for h in hs)} median {sorted(len(h) for h in hs)[len(hs)//2]} max {max(len(h) for h in hs)}; empty {empty}")
    print(f"  words in EVERY exit set: {len(common)} -> {[words[i] for i in sorted(common)][:8]}")
    print(f"  per-orbit exit counts (of {len(ninety)}):")
    for o, c in per_orb.most_common(20):
        print(f"    {c:3d}  {o}")
    print(f"  MIN HITTING SET word-level {s_w} {'(exact)' if ex_w else '(bound)'}: {[words[i] for i in set_w]}")
    print(f"  MIN HITTING SET orbit-level {s_o} {'(exact)' if ex_o else '(bound)'}: {[orbits[i] for i in set_o]}")
    fb = Counter(b for *_, b in ninety)
    print(f"  far-bit patterns of the 90: {dict(fb)}")
    json.dump({'exit_sets': [sorted(h) for h in hs], 'configs': [(n, gi, v, list(ct), list(b)) for n, gi, v, ct, *_, b in ninety]},
              open(os.path.join(HERE, '.the90_exit_sets.json'), 'w'))
    print(f"  [{time.time()-t0:.0f}s]")
