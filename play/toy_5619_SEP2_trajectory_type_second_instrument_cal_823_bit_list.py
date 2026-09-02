#!/usr/bin/env python3
"""
Toy 5619 — THE TRAJECTORY TYPE, second instrument, Cal §823's bit list
as a POSITION: (a) the 28 c0 eight-chain bits (the free ones reported
by measurement); (b) Lemma T's four bits per bridge word — Δ, Δ′, Q3,
Q4 (Q3: n_sM ~ n_si in the (s_M,s_j)-chains of c4; Q4: n_sM ~ n_sj in
the (s_M,s_i)-chains of c4) — the control that the classifier agrees
with Lemma T (locked ⟹ hard cell, 100%); (c) the three stage-pair bits
X2∩X3, X2∩X4, X3∩X4 per bridge word; (d) the 24 stage-by-c0 bits
X_k ∩ K (k = 2,3,4; K over the eight) per bridge word. All 0/1, no
sizes. Forced entries (Cal's derived list) as the control — reported as
constant or not. Population: all 349 locked + a 1-in-40 stratified
sample of in-frame stuck colorings n = 12..22. Purity of 'locked' by
FULL type and by the (c)+(d) sub-type, weighted by unlocked members.

Elie, 2026-09-02.
"""

import importlib.util
import json
import os
import time
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


TT = load("t5613tr", "toy_5613_SEP2_laneF_type_table_kittell_eight_chain"
          "_intersection_matrix.py")
H = load("t5611tr", "toy_5611_SEP2_H_cut_containment_cross_tab_93_and_bridge"
         "_fail_1211.py")
DL = load("t5597tr", "toy_5597_SEP2_lyra_delta_dichotomy_counts_Wi_Wj_legality"
          "_lemma_control.py")
MF, K, OF, IF, EA, G5, E1, WF = TT.MF, TT.K, TT.OF, TT.IF, TT.EA, TT.G5, TT.E1, TT.WF
NAMES = ['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ']


def same_chain(adj, tv, c, u, w, a, b):
    if c[u] not in (a, b) or c[w] not in (a, b):
        return False
    return w in G5.kempe_chain(adj, c, u, a, b, exclude={tv})


def traj_bits(adj, tv, lcyc, c0, which):
    """Returns (bits_b, bits_c, bits_d) for bridge word W_which."""
    rm = WF.role_map(adj, c0, tv, lcyc)
    vmap, cmap = rm
    r, sM = cmap['r'], cmap['s_M']
    if which == 'i':
        s_near, s_far = cmap['s_i'], cmap['s_j']
        n_near, n_far = vmap['n_si'], vmap['n_sj']
    else:
        s_near, s_far = cmap['s_j'], cmap['s_i']
        n_near, n_far = vmap['n_sj'], vmap['n_si']
    copies = [vmap['B1'], vmap['B2']]
    C_near = next(b for b in copies if n_near in adj[b])
    C_far = next(b for b in copies if b != C_near)
    n_sM = vmap['n_sM']
    m1 = ((min(r, s_near), max(r, s_near)), C_near)
    m2 = ((min(r, s_far), max(r, s_far)), C_far)
    chains = []
    cur = c0
    for m in (m1, m2, m1, m2):
        pair, seed = m
        ch = G5.kempe_chain(adj, cur, seed, pair[0], pair[1], exclude={tv}) if cur[seed] in pair else set()
        chains.append(frozenset(ch))
        if ch:
            cur = G5.do_swap(cur, ch, pair[0], pair[1])
    X1, X2, X3, X4 = chains
    c4 = cur
    delta = n_far in X3
    dprime = (C_near in X4) and (n_near in X4)
    q3 = same_chain(adj, tv, c4, n_sM, n_near, min(sM, s_far), max(sM, s_far))
    q4 = same_chain(adj, tv, c4, n_sM, n_far, min(sM, s_near), max(sM, s_near))
    bits_b = (delta, dprime, q3, q4)
    bits_c = (bool(X2 & X3), bool(X2 & X4), bool(X3 & X4))
    eight = TT.eight_chains(adj, tv, lcyc, c0)
    bits_d = tuple(bool(Xk & Kc) for Xk in (X2, X3, X4) for Kc in eight)
    return bits_b, bits_c, bits_d


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5619 — trajectory type, second instrument (Cal §823 position)")
    print("=" * 70)
    t0 = time.time()
    locked = {}
    for f in ('.in_frame_26_two_word_locked.json', '.in_frame_23_two_word_locked_n22.json',
              '.in_frame_44_two_word_locked_n23.json', '.in_frame_256_two_word_locked_n24.json'):
        for W in json.load(open(os.path.join(HERE, f))):
            locked[(W['n'], W['graph_index_plantri_c5'], W['v'], tuple(W['coloring_mod_S4_sorted_order']))] = 1
    graphs = {}
    rows = []

    def do(n, gi, v, ct, adj, lcyc, order, is_locked):
        pos = {u: i for i, u in enumerate(order)}
        c0 = {u: ct[pos[u]] for u in order}
        a_bits, _sizes = TT.type_of(TT.eight_chains(adj, v, lcyc, c0))
        bi, ci, di = traj_bits(adj, v, lcyc, c0, 'i')
        bj, cj, dj = traj_bits(adj, v, lcyc, c0, 'j')
        rows.append((n, is_locked, a_bits, bi, bj, ci, cj, di, dj))

    for key in locked:
        n, gi, v, ct = key
        if (n, gi) not in graphs:
            graphs[(n, gi)] = EA.plantri_graphs(n, flags=('-c5',))[gi]
        adj = graphs[(n, gi)]
        faces, ok = OF.faces_of(adj)
        order = sorted(u for u in adj if u != v)
        do(n, gi, v, ct, adj, E1.link_cycle(faces, v), order, 1)
    print(f"  349 locked done [{time.time()-t0:.0f}s]", flush=True)
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
                    if not IF.stuck(adj, v, {u: ct[pos[u]] for u in order}):
                        continue
                    k += 1
                    if k % 40 == 0 and (n, gi, v, tuple(ct)) not in locked:
                        do(n, gi, v, ct, adj, lcyc, order, 0)
    print(f"  sample done: {len(rows) - 349} unlocked rows [{time.time()-t0:.0f}s]", flush=True)

    # control 1: Lemma T agreement — locked ⟹ hard cell (Δ, Δ′=0, Q3, Q4) for both bridge words
    hard = sum(1 for r in rows if r[1] and r[3] == (True, False, True, True) and r[4] == (True, False, True, True))
    print(f"\n  CONTROL (b): locked rows in Lemma T's hard cell for BOTH bridge words: {hard}/349")
    # control 2: forced bits constant
    dcols = list(zip(*[r[7] for r in rows]))
    const_d = [i for i, col in enumerate(dcols) if len(set(col)) == 1]
    ccols = list(zip(*[r[5] for r in rows]))
    print(f"  CONTROL (d): constant stage-by-c0 bits for W_i: {len(const_d)}/24 "
          f"{[(('X2','X3','X4')[i//8] + '∩' + NAMES[i%8], dcols[i][0]) for i in const_d]}")
    print(f"  (c) stage-pair bits W_i (X2X3, X2X4, X3X4) constant? {[len(set(c)) == 1 for c in ccols]}")

    def purity(keyf, label):
        by = defaultdict(lambda: [0, 0])
        for r in rows:
            t = by[keyf(r)]
            t[r[1]] += 1
        lock_types = {k: v for k, v in by.items() if v[1]}
        pure = sum(1 for v in lock_types.values() if v[0] == 0)
        unl_in_lock_types = sum(v[0] for v in lock_types.values())
        print(f"  {label}: types {len(by)}; types holding a locked config {len(lock_types)}; "
              f"PURE (no unlocked member in the sample) {pure}; unlocked sample members inside locked types "
              f"{unl_in_lock_types} of {sum(v[0] for v in by.values())}; worst mixed "
              f"{sorted(((v[0], v[1]) for v in lock_types.values()), reverse=True)[:6]}")
    purity(lambda r: (r[2],), "(a) c0 eight-chain bit-type")
    purity(lambda r: (r[5], r[6], r[7], r[8]), "(c)+(d) trajectory sub-type")
    purity(lambda r: (r[2], r[3], r[4], r[5], r[6], r[7], r[8]), "FULL type (a)+(b)+(c)+(d)")
    purity(lambda r: (r[5], r[6]), "CAL-CORE-like: (c) only, both words")
    json.dump([(r[0], r[1], r[2], list(r[3]), list(r[4]), list(r[5]), list(r[6]), list(r[7]), list(r[8])) for r in rows],
              open(os.path.join(HERE, '.trajectory_type.json'), 'w'))
    print(f"  [{time.time()-t0:.0f}s]")
