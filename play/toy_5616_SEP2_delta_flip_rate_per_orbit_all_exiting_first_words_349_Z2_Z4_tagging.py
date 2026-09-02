#!/usr/bin/env python3
"""
Toy 5616 — THE Δ-FLIP TABLE on EVERY exiting first word of all 349
two-word-locked witnesses (n = 17..24), and Z2 / Z4 tagging per cut
vertex for Lyra's Net-Colour Lemma

At each witness c0 (bridge-locked: both bridge words' leaves are
Δ-YES ∧ Δ′-NO, stuck), for EVERY fully-legal first word w with image
c' = w·c0 that a bridge word exits from (EXIT-B): the bridge words'
leaves in c''s own frame (5597's Δ, Δ′): Δ-flip := some bridge word
of c' is Δ-NO. Reported per first-word ORBIT: exits, Δ-flips, flip
rate; plus the non-exiting words as control (their Δ pattern).
Z2/Z4 tagging: for the CONTAINING exits (an (r,s_M)-stage chain of w
contains a bridge cut), per cut vertex x: x ∈ Z2 (stage-2 chain of w),
x ∈ Z4 (stage-4 chain), and x's final colour in c0's vocabulary
(r / near / other). Net-Colour Lemma predictions: x ∈ Z2 ∖ Z4 → ends
s_M ('other'); x ∈ Z2 ∩ Z4 → returns to r. Tabulated as a 4-cell
membership × colour table, never a verdict.

Elie, 2026-09-02.
"""

import json
import os
import importlib.util
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


LT = load("t5615df", "toy_5615_SEP2_lyra_leaf_table_containing_exits_M1_M2_M3.py")
H, DL = LT.H, LT.DL
K, OF, IF, EA, G5, E1, WF, MF = LT.K, LT.OF, LT.IF, LT.EA, LT.G5, LT.E1, LT.WF, LT.MF


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5616 — Δ-flip per first-word orbit on all 349; Z2/Z4 tagging")
    print("=" * 70)
    moves, words, _ = WF.context_family()
    wit = []
    for f in ('.in_frame_26_two_word_locked.json', '.in_frame_23_two_word_locked_n22.json',
              '.in_frame_44_two_word_locked_n23.json', '.in_frame_256_two_word_locked_n24.json'):
        wit += json.load(open(os.path.join(HERE, f)))
    graphs = {}
    per_orb = defaultdict(Counter)
    zz = Counter()
    zz_by_stage = Counter()
    base_leaf = Counter()
    n_w = 0
    for W in wit:
        n, gi, v, ct = W['n'], W['graph_index_plantri_c5'], W['v'], W['coloring_mod_S4_sorted_order']
        if (n, gi) not in graphs:
            graphs[(n, gi)] = EA.plantri_graphs(n, flags=('-c5',))[gi]
        adj = graphs[(n, gi)]
        faces, ok = OF.faces_of(adj)
        order = sorted(u for u in adj if u != v)
        c0 = {u: ct[i] for i, u in enumerate(order)}
        lcyc = E1.link_cycle(faces, v)
        n_w += 1
        # base leaves (control: must be Δ-YES∧Δ′-NO stuck for both bridge words)
        for which in ('i', 'j'):
            rec = DL.analyze(adj, v, lcyc, c0, which)
            base_leaf[rec.get('leaf', rec['status'])] += 1
        cs, (vmap, cmap) = H.cut_of(adj, v, lcyc, c0)
        r, sM = cmap['r'], cmap['s_M']
        link = set(adj[v])
        cuts = {name: (c - link) for name, c in cs.items() if c}
        for w in words:
            m1, m2 = H.moves_of(w, vmap, cmap)
            chains, flags, img = H.stage_chains(adj, v, c0, m1, m2)
            if not all(flags) or not G5.is_proper(adj, img, skip=v) or img == c0:
                continue
            o = H.orb(w)
            ex = any(K.gate(adj, v, k) for _w, k in MF.apply(adj, v, lcyc, img, MF.BRIDGE))
            leaves = []
            for which in ('i', 'j'):
                rec = DL.analyze(adj, v, lcyc, img, which)
                leaves.append(rec.get('leaf', rec['status']))
            flip = any(l.startswith('ΔNO') for l in leaves)
            dyy = any('Δ′YES' in l for l in leaves)
            t = per_orb[o]
            t['legal'] += 1
            if ex:
                t['exit'] += 1
                t['exit&flip'] += flip
                t['exit&Δ′YES-only'] += (dyy and not flip)
                t['exit&neither'] += (not flip and not dyy)
            else:
                t['noexit'] += 1
                t['noexit&flip'] += flip
            # Z2/Z4 tagging on containing exits
            rsM_idx = [k for k, m in enumerate((m1, m2, m1, m2)) if set(m[0]) == {r, sM}]
            for name, C in cuts.items():
                if not C:
                    continue
                if not any(C <= chains[k] for k in rsM_idx):
                    continue
                near = cmap['s_i'] if name == 'i' else cmap['s_j']
                Z2, Z4 = chains[1], chains[3]
                for x in C:
                    col = 'r' if img[x] == r else ('near' if img[x] == near else 'other')
                    cell = ('Z2' if x in Z2 else '¬Z2') + ('∩Z4' if x in Z4 else '∖Z4')
                    zz[(cell, col)] += 1
                    zz_by_stage[(tuple(rsM_idx), cell, col)] += 1
    print(f"\n  witnesses {n_w}; base leaves (both bridge words at c0): {dict(base_leaf)}")
    print(f"\n  Δ-FLIP PER FIRST-WORD ORBIT (legal, exit, exit&Δ-flip, flip rate | exit&Δ′YES-only, exit&neither | noexit, noexit&flip):")
    for o, t in sorted(per_orb.items(), key=lambda kv: -kv[1]['exit']):
        rate = t['exit&flip'] / t['exit'] if t['exit'] else float('nan')
        print(f"    {o[:64]:64s} {t['legal']:5d} {t['exit']:5d} {t['exit&flip']:5d} {rate:5.2f} | {t['exit&Δ′YES-only']:4d} {t['exit&neither']:4d} | {t['noexit']:4d} {t['noexit&flip']:4d}")
    tot_exit = sum(t['exit'] for t in per_orb.values())
    tot_flip = sum(t['exit&flip'] for t in per_orb.values())
    print(f"  ALL exits {tot_exit}; Δ-flips {tot_flip}; Δ′-YES-only {sum(t['exit&Δ′YES-only'] for t in per_orb.values())}; neither {sum(t['exit&neither'] for t in per_orb.values())}")
    print(f"\n  Z2/Z4 TAGGING per cut vertex on containing exits (cell, final colour): ")
    for cell in ('Z2∩Z4', 'Z2∖Z4', '¬Z2∩Z4', '¬Z2∖Z4'):
        print(f"    {cell:8s}: r {zz[(cell,'r')]:4d}  near {zz[(cell,'near')]:4d}  other {zz[(cell,'other')]:4d}")
    print(f"  by (r,s_M)-stage positions of w: {dict(zz_by_stage.most_common(12))}")
    json.dump({'per_orb': {o: dict(t) for o, t in per_orb.items()}, 'zz': [(k, c) for k, c in zz.items()]},
              open(os.path.join(HERE, '.delta_flip_table.json'), 'w'), indent=1)
