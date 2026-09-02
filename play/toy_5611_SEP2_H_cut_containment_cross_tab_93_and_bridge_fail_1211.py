#!/usr/bin/env python3
"""
Toy 5611 — H_cut (K1840, pre-registered before this count): THE CUT
C(c) := X4(c) ∩ X3(c) of the bridge word at c, and whether the exiting
first words' stage chains CONTAIN it

Populations: (A) the 93 two-word-locked witnesses (n = 17, 21, 22, 23);
(B) the BRIDGE-FAIL set — every in-frame stuck coloring n <= 22 where
bridge-then-middle fails (5608: 1,211), regenerated here; (C) a matched
depth-1 sample for kappa (next stuck coloring with a one-word gate exit
on the same (T, v), one per witness).

Per configuration c: the two bridge words W_i, W_j in c's frame; their
stage chains X1..X4 (the chains actually swapped); C_i = X3 ∩ X4 of
W_i, C_j likewise; C = C_i ∪ C_j; kappa = |C| (and |C_i|, |C_j|).
For every fully-legal first word w (186-family, c's frame): U(w) =
union of w's four stage chains; containment class: FULL (C ⊆ U),
PARTIAL (C ∩ U ≠ ∅, not all), NONE; and exit: EXIT-B (a bridge word in
w·c's frame reaches the gate phase), EXIT-ANY (any fully-legal word
does), or NO-EXIT. Cross-tab containment × exit, per first-word orbit
and overall. Control: non-exiting legal words must miss C at a rate
that separates. Also kappa(M·c) = |C| recomputed in the image's frame
for each exiting M (predicted 0 by K1840). Also the three named counts
per configuration: W_legal(c), Im(c) = distinct images, W_acting(c).

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


MF = load("t5608hc", "toy_5608_SEP2_middle_first_rule_in_frame_middle_word_then"
          "_bridge_word.py")
K, OF, IF, EA, G5, X3, LG, E1, WF = MF.K, MF.OF, MF.IF, MF.EA, MF.G5, MF.X3, MF.LG, MF.E1, MF.WF
MIDDLE, BRIDGE = MF.MIDDLE, MF.BRIDGE
WI = (('B1', ('r', 's_i')), ('B2', ('r', 's_j')))
WJ = (('B1', ('r', 's_j')), ('B2', ('r', 's_i')))


def mirror(w):
    def mm(m):
        role, pair = m
        role2 = {'B1': 'B2', 'B2': 'B1', 'n_si': 'n_sj', 'n_sj': 'n_si'}.get(role, role)
        pair2 = tuple(sorted({'s_i': 's_j', 's_j': 's_i'}.get(x, x) for x in pair))
        return (role2, pair2)
    return (mm(w[0]), mm(w[1]))


def orb(w):
    return min(str(w), str(mirror(w)))


def moves_of(w, vmap, cmap):
    m1 = (tuple(sorted((cmap[w[0][1][0]], cmap[w[0][1][1]]))), vmap[w[0][0]])
    m2 = (tuple(sorted((cmap[w[1][1][0]], cmap[w[1][1][1]]))), vmap[w[1][0]])
    return m1, m2


def stage_chains(adj, tv, c, m1, m2):
    chains = []
    flags = []
    cur = c
    for m in (m1, m2, m1, m2):
        pair, seed = m
        if cur.get(seed) not in pair:
            flags.append(False)
            chains.append(frozenset())
            continue
        flags.append(True)
        ch = G5.kempe_chain(adj, cur, seed, pair[0], pair[1], exclude={tv})
        chains.append(frozenset(ch))
        cur = G5.do_swap(cur, ch, pair[0], pair[1])
    return chains, flags, cur


def cut_of(adj, tv, lcyc, c):
    rm = WF.role_map(adj, c, tv, lcyc)
    if rm is None:
        return None
    vmap, cmap = rm
    cs = {}
    for name, w in (('i', WI), ('j', WJ)):
        m1, m2 = moves_of(w, vmap, cmap)
        chains, flags, img = stage_chains(adj, tv, c, m1, m2)
        cs[name] = (chains[2] & chains[3]) if all(flags) else None
    return cs, (vmap, cmap)


def analyze(adj, tv, lcyc, c0, words):
    res = cut_of(adj, tv, lcyc, c0)
    if res is None:
        return None
    cs, (vmap, cmap) = res
    Ci, Cj = cs['i'], cs['j']
    C = (Ci or frozenset()) | (Cj or frozenset())
    rows = []
    images = set()
    n_acting = 0
    for w in words:
        m1, m2 = moves_of(w, vmap, cmap)
        chains, flags, img = stage_chains(adj, tv, c0, m1, m2)
        if not all(flags):
            continue
        if not G5.is_proper(adj, img, skip=tv):
            continue
        if img == c0:
            continue
        n_acting += 1
        order = sorted(adj, key=str)
        images.add(tuple(img[u] for u in order if u != tv))
        U = chains[0] | chains[1] | chains[2] | chains[3]
        if not C:
            cont = 'C-empty'
        elif C <= U:
            cont = 'FULL'
        elif C & U:
            cont = 'PARTIAL'
        else:
            cont = 'NONE'
        # exit classification in the image's frame
        if K.gate(adj, tv, img):
            ex = 'EXIT-1'
        else:
            imB = MF.apply(adj, tv, lcyc, img, BRIDGE)
            if any(K.gate(adj, tv, k) for _w, k in imB):
                ex = 'EXIT-B'
            else:
                imA = K.legal_images(adj, tv, lcyc, img, words)
                ex = 'EXIT-ANY' if any(K.gate(adj, tv, k) for _w, k in imA) else 'NO-EXIT'
        # kappa of the image (predicted 0 for exiting middle words)
        r2 = cut_of(adj, tv, lcyc, img)
        kap_img = None
        if r2 is not None:
            cs2 = r2[0]
            kap_img = len((cs2['i'] or frozenset()) | (cs2['j'] or frozenset()))
        rows.append((orb(w), cont, ex, kap_img, len(C & U), len(C)))
    return {'kappa': len(C), 'ki': None if Ci is None else len(Ci), 'kj': None if Cj is None else len(Cj),
            'W_legal': len(rows), 'Im': len(images), 'W_acting': n_acting, 'rows': rows}


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5611 — H_cut: the cut C = X3 ∩ X4 of the bridge word, containment vs exit")
    print("=" * 70)
    moves, words, _ = WF.context_family()
    t0 = time.time()
    # (A) the 93
    wit = []
    for f in ('.in_frame_26_two_word_locked.json', '.in_frame_23_two_word_locked_n22.json',
              '.in_frame_44_two_word_locked_n23.json'):
        wit += json.load(open(os.path.join(HERE, f)))
    graphs = {}

    def graph(n, gi):
        if (n, gi) not in graphs:
            graphs[(n, gi)] = EA.plantri_graphs(n, flags=('-c5',))[gi]
        return graphs[(n, gi)]
    popA = []
    popC = []
    for W in wit:
        n, gi, v, ct = W['n'], W['graph_index_plantri_c5'], W['v'], W['coloring_mod_S4_sorted_order']
        adj = graph(n, gi)
        faces, ok = OF.faces_of(adj)
        order = sorted(u for u in adj if u != v)
        pos = {u: i for i, u in enumerate(order)}
        c0 = {u: ct[i] for i, u in enumerate(order)}
        lcyc = E1.link_cycle(faces, v)
        popA.append((n, gi, v, adj, lcyc, c0))
        sub = {u: {w for w in adj[u] if w != v} for u in adj if u != v}
        cols = EA.all_colorings_mod_s4(sub, order)
        i0 = cols.index(tuple(ct)) if tuple(ct) in cols else 0
        for j in list(range(i0 + 1, len(cols))) + list(range(0, i0)):
            c1 = {u: cols[j][pos[u]] for u in order}
            if not IF.stuck(adj, v, c1):
                continue
            if any(K.gate(adj, v, k) for w, k in K.legal_images(adj, v, lcyc, c1, words)):
                popC.append((n, gi, v, adj, lcyc, c1))
                break
    print(f"  (A) {len(popA)} witnesses loaded; (C) matched depth-1 {len(popC)}  [{time.time()-t0:.0f}s]", flush=True)

    # (B) the bridge-fail set, regenerated n = 12..22
    ns = [int(x) for x in sys.argv[1:]] or list(range(12, 23))
    popB = []
    for n in ns:
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
                    if MF.program(adj, v, lcyc, c0, BRIDGE, MIDDLE) == 'FAIL':
                        popB.append((n, gi, v, adj, lcyc, c0))
    print(f"  (B) bridge-fail set regenerated: {len(popB)} (5608: 1,211)  [{time.time()-t0:.0f}s]", flush=True)

    def run(pop, tag):
        tab = Counter()
        tab_orb = {}
        kap = []
        kap_img_exit = Counter()
        counts = []
        per_cfg_ok = 0
        for n, gi, v, adj, lcyc, c0 in pop:
            r = analyze(adj, v, lcyc, c0, words)
            if r is None:
                continue
            kap.append(r['kappa'])
            counts.append((r['W_legal'], r['Im'], r['W_acting']))
            cfg_exit_words = [row for row in r['rows'] if row[2] in ('EXIT-B', 'EXIT-ANY', 'EXIT-1')]
            if cfg_exit_words and all(row[1] == 'FULL' for row in cfg_exit_words if row[2] == 'EXIT-B'):
                per_cfg_ok += 1
            for o, cont, ex, kimg, ncap, nc in r['rows']:
                tab[(cont, ex)] += 1
                tab_orb.setdefault(o, Counter())[(cont, ex)] += 1
                if ex in ('EXIT-B', 'EXIT-1') and kimg is not None:
                    kap_img_exit[kimg] += 1
        hh = hashlib.sha256(json.dumps(sorted((str(k), c) for k, c in tab.items())).encode()).hexdigest()
        print(f"\n  === {tag}: {len(kap)} configurations; cross-tab hashed {hh[:16]}")
        print(f"  kappa = |C| distribution: {dict(sorted(Counter(kap).items()))}")
        print(f"  W_legal / Im / W_acting per configuration — medians: "
              f"{sorted(c[0] for c in counts)[len(counts)//2]} / {sorted(c[1] for c in counts)[len(counts)//2]} / "
              f"{sorted(c[2] for c in counts)[len(counts)//2]}; ranges W_legal {min(c[0] for c in counts)}-{max(c[0] for c in counts)}, "
              f"Im {min(c[1] for c in counts)}-{max(c[1] for c in counts)}")
        print(f"  CROSS-TAB containment × exit (first-word instances): ")
        for cont in ('FULL', 'PARTIAL', 'NONE', 'C-empty'):
            print(f"    {cont:8s}: " + ", ".join(f"{ex} {tab[(cont, ex)]}" for ex in ('EXIT-1', 'EXIT-B', 'EXIT-ANY', 'NO-EXIT')))
        print(f"  kappa(M·c) for exiting first words (EXIT-1/EXIT-B): {dict(sorted(kap_img_exit.items()))}")
        print(f"  per-orbit (orbit: FULL-exitB / PARTIAL-exitB / NONE-exitB / FULL-noexit / PARTIAL-noexit / NONE-noexit):")
        for o, t in sorted(tab_orb.items(), key=lambda kv: -(kv[1][('FULL', 'EXIT-B')] + kv[1][('PARTIAL', 'EXIT-B')]))[:14]:
            print(f"    {o[:70]:70s} {t[('FULL','EXIT-B')]:4d} {t[('PARTIAL','EXIT-B')]:4d} {t[('NONE','EXIT-B')]:4d} | "
                  f"{t[('FULL','NO-EXIT')]:4d} {t[('PARTIAL','NO-EXIT')]:4d} {t[('NONE','NO-EXIT')]:4d}")
        return tab, kap

    tabA, kapA = run(popA, "(A) THE 93")
    tabB, kapB = run(popB, "(B) THE BRIDGE-FAIL SET")
    kapC = []
    for n, gi, v, adj, lcyc, c1 in popC:
        r = cut_of(adj, v, lcyc, c1)
        if r:
            cs = r[0]
            kapC.append(len((cs['i'] or frozenset()) | (cs['j'] or frozenset())))
    print(f"\n  (C) matched depth-1 sample kappa distribution: {dict(sorted(Counter(kapC).items()))} "
          f"(vs the 93: {dict(sorted(Counter(kapA).items()))})")
    json.dump({'A': [(str(k), c) for k, c in tabA.items()], 'B': [(str(k), c) for k, c in tabB.items()],
               'kapA': kapA, 'kapB': kapB, 'kapC': kapC},
              open(os.path.join(HERE, '.h_cut.json'), 'w'), indent=1)
    print(f"\n  [{time.time()-t0:.0f}s]")
