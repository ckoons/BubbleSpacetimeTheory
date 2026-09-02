#!/usr/bin/env python3
"""
Toy 5615 — LYRA'S SECTION-4 LEAF TABLE on the containing exits (my
586; Cal's 720 are his instrument's): for each (c, w) on the 93 where
an (r,s_M)-stage chain of the fully-legal first word w contains a
bridge cut (C_i or C_j, link-excluded; 5611's definition), compute in
c' = w·c:
  - the bridge word's LEAF in c''s own canonical frame (5597's
    dichotomy: Δ = far singleton ∈ X3 [Q3 as instrumented]; Δ' =
    {near copy, near singleton} ⊆ X4 [Q4 as instrumented]) — leaf ∈
    {Δ-NO (I), Δ-YES∧Δ'-YES (G by K1838 §2b), Δ-YES∧Δ'-NO (stuck or gate
    by measurement)} — for BOTH bridge words of c', reported as the
    better of the two and as the pair;
  - the final colours of the c0-cut vertices in c', named in c0's
    colour vocabulary: r / near-singleton / other;
  - the NEW cut C(c') (5611's definition in c''s frame) vs the old
    cut: disjoint / meets / equal.
Mechanism cells (Lyra's pre-registration): M1 = every cut vertex ends
∉ {r, near} AND leaf Δ-NO or ¬Q3 (Δ-NO); M2 = leaf (Q3, ¬Q4) = Δ-YES∧
Δ'-NO with the image exiting; M3 = new cut disjoint from the old cut.
Reported as a 3×leaf table, never a verdict. The join-key caveat is
stated: Q3/Q4 are instrumented as Δ/Δ' of 5597; if Lyra's Lemma T
names them differently the table re-keys, the counts do not change.

Elie, 2026-09-02.
"""

import importlib.util
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


H = load("t5611lf", "toy_5611_SEP2_H_cut_containment_cross_tab_93_and_bridge"
         "_fail_1211.py")
DL = load("t5597lf", "toy_5597_SEP2_lyra_delta_dichotomy_counts_Wi_Wj_legality"
          "_lemma_control.py")
K, OF, IF, EA, G5, E1, WF, MF = H.K, H.OF, H.IF, H.EA, H.G5, H.E1, H.WF, H.MF


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5615 — the leaf table on the containing exits (the 93)")
    print("=" * 70)
    moves, words, _ = WF.context_family()
    wit = []
    for f in ('.in_frame_26_two_word_locked.json', '.in_frame_23_two_word_locked_n22.json',
              '.in_frame_44_two_word_locked_n23.json'):
        wit += json.load(open(os.path.join(HERE, f)))
    graphs = {}
    table = Counter()
    colours = Counter()
    newcut = Counter()
    mech = Counter()
    rows = []
    for W in wit:
        n, gi, v, ct = W['n'], W['graph_index_plantri_c5'], W['v'], W['coloring_mod_S4_sorted_order']
        if (n, gi) not in graphs:
            graphs[(n, gi)] = EA.plantri_graphs(n, flags=('-c5',))[gi]
        adj = graphs[(n, gi)]
        faces, ok = OF.faces_of(adj)
        order = sorted(u for u in adj if u != v)
        c0 = {u: ct[i] for i, u in enumerate(order)}
        lcyc = E1.link_cycle(faces, v)
        cs, (vmap, cmap) = H.cut_of(adj, v, lcyc, c0)
        r, sM = cmap['r'], cmap['s_M']
        link = set(adj[v])
        cuts = {name: (c - link) for name, c in cs.items() if c}
        for w in words:
            m1, m2 = H.moves_of(w, vmap, cmap)
            chains, flags, img = H.stage_chains(adj, v, c0, m1, m2)
            if not all(flags) or not G5.is_proper(adj, img, skip=v) or img == c0:
                continue
            rsM = [chains[k] for k, m in enumerate((m1, m2, m1, m2)) if set(m[0]) == {r, sM}]
            contained = [name for name, c in cuts.items() if c and any(c <= ch for ch in rsM)]
            if not contained:
                continue
            # exit by a bridge word in img's frame?
            ex = any(K.gate(adj, v, k) for _w, k in MF.apply(adj, v, lcyc, img, MF.BRIDGE))
            # leaf of both bridge words in img's frame (5597's analyze)
            leaves = []
            for which in ('i', 'j'):
                rec = DL.analyze(adj, v, lcyc, img, which)
                if rec['status'] != 'ok':
                    leaves.append('no-context')
                else:
                    leaves.append(rec['leaf'])
            best = 'ΔNO' if any(l.startswith('ΔNO') for l in leaves) else                    ("ΔYES/Δ'YES" if any("Δ′YES" in l for l in leaves) else "ΔYES/Δ'NO")
            # final colours of the old cut vertices, in c0's vocabulary
            for name in contained:
                near = cmap['s_i'] if name == 'i' else cmap['s_j']
                cols = Counter()
                for x in cuts[name]:
                    cx = img[x]
                    cols['r' if cx == r else ('near' if cx == near else 'other')] += 1
                allout = cols['r'] == 0 and cols['near'] == 0
                colours[tuple(sorted(cols.items()))] += 1
                # new cut in img's frame
                r2 = H.cut_of(adj, v, lcyc, img)
                if r2 is None:
                    rel = 'no-context'
                else:
                    cs2 = r2[0]
                    C2 = ((cs2['i'] or frozenset()) | (cs2['j'] or frozenset())) - link
                    rel = 'disjoint' if not (C2 & cuts[name]) else ('equal' if C2 == cuts[name] else 'meets')
                newcut[rel] += 1
                m1c = allout and best == 'ΔNO'
                m2c = best == "ΔYES/Δ'NO" and ex
                m3c = rel == 'disjoint'
                cell = ('M1' if m1c else '') + ('M2' if m2c else '') + ('M3' if m3c else '') or 'none'
                mech[(cell, best)] += 1
                table[(best, 'exit' if ex else 'NO-EXIT')] += 1
                rows.append((n, gi, v, str(w), name, best, ex, dict(cols), rel))
    print(f"\n  containing exits classified: {len(rows)} (5611: 586; each (c, w, cut) counted once)")
    print(f"  LEAF of the bridge word in c′'s frame (best of W_i/W_j) × exit: {dict(sorted(table.items()))}")
    print(f"  final colours of the OLD cut vertices in c′ (c0 vocabulary), by pattern: "
          f"{[(dict(k), c) for k, c in colours.most_common(8)]}")
    print(f"  NEW cut vs OLD cut: {dict(newcut)}")
    print(f"  MECHANISM cells × leaf (M1 = all cut vertices ∉ {{r, near}} ∧ ΔNO; M2 = (Q3,¬Q4) ∧ exit; M3 = new cut disjoint):")
    for k, c in sorted(mech.items(), key=lambda kv: -kv[1]):
        print(f"    {c:5d}  {k}")
    json.dump(rows, open(os.path.join(HERE, '.leaf_table_containing_exits.json'), 'w'), indent=1)
