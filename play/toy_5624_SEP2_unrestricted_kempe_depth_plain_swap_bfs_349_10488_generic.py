#!/usr/bin/env python3
"""
Toy 5624 — THE UNRESTRICTED KEMPE DEPTH: breadth-first search over
PLAIN Kempe swaps (any seed u ≠ v, any pair containing c(u)) from a
stuck coloring of T−v to the first gate-phase coloring (a colour
absent at v, or τ_v ≤ 5). No commutators, no link-seeding, no menu.
Populations: (A) all 349 two-word-locked witnesses (n = 17..24);
(B) the 10,488 no-direct-exit stuck colorings at n = 24 (5600's kill
list); (C) a generic stratified sample of in-frame stuck colorings
(every k-th, n = 16..22). Per population: the depth distribution and
the maximum; unreached-within-cap reported as a category. Canonical
forms mod S₄ are used as visited keys (swaps commute with relabeling).

Elie, 2026-09-02.
"""

import importlib.util
import json
import os
import sys
import time
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


K = load("t5601ud", "toy_5601_SEP2_in_frame_not_hit_334_gate_phase_depth_bfs"
         "_single_swap_null.py")
OF, IF, EA, G5, X3, E1, WF = K.OF, K.IF, K.EA, K.G5, K.X3, K.E1, K.WF
MAXD = int(os.environ.get('UD_MAXD', '4'))
CAP = int(os.environ.get('UD_CAP', '60000'))


def canon(c, order):
    m = {}
    out = []
    for u in order:
        k = c[u]
        if k not in m:
            m[k] = len(m)
        out.append(m[k])
    return tuple(out)


def gate(adj, tv, c):
    return len({c[u] for u in adj[tv]}) < 4 or G5.operational_tau(adj, c, tv) <= 5


def depth(adj, tv, c0, order):
    """Returns (depth, explored) or (None, explored) if not reached within MAXD/CAP."""
    seen = {canon(c0, order)}
    frontier = [c0]
    for d in range(1, MAXD + 1):
        nxt = []
        for c in frontier:
            for u in order:
                a = c[u]
                for b in range(4):
                    if b == a:
                        continue
                    ch = G5.kempe_chain(adj, c, u, a, b, exclude={tv})
                    k = G5.do_swap(c, ch, a, b)
                    key = canon(k, order)
                    if key in seen:
                        continue
                    seen.add(key)
                    if gate(adj, tv, k):
                        return d, len(seen)
                    if len(seen) < CAP:
                        nxt.append(k)
        if not nxt:
            break
        frontier = nxt
    return None, len(seen)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else 'A'
    print("=" * 70)
    print(f"Toy 5624 — unrestricted Kempe depth [{mode}] MAXD={MAXD} CAP={CAP}")
    print("=" * 70)
    t0 = time.time()
    graphs = {}

    def graph(n, gi):
        if (n, gi) not in graphs:
            graphs[(n, gi)] = EA.plantri_graphs(n, flags=('-c5',))[gi]
        return graphs[(n, gi)]
    dist = Counter()
    expl = []
    rows = []
    if mode == 'A':
        wit = []
        for f in ('.in_frame_26_two_word_locked.json', '.in_frame_23_two_word_locked_n22.json',
                  '.in_frame_44_two_word_locked_n23.json', '.in_frame_256_two_word_locked_n24.json'):
            wit += json.load(open(os.path.join(HERE, f)))
        for W in wit:
            n, gi, v, ct = W['n'], W['graph_index_plantri_c5'], W['v'], W['coloring_mod_S4_sorted_order']
            adj = graph(n, gi)
            order = sorted(u for u in adj if u != v)
            c0 = {u: ct[i] for i, u in enumerate(order)}
            d, ex = depth(adj, v, c0, order)
            dist[(n, d)] += 1
            expl.append(ex)
            rows.append((n, gi, v, d, ex))
    elif mode == 'B':
        kills = [eval(k) for k in json.load(open(os.path.join(HERE, '.in_frame_one_word_n24.json')))['kills']]
        for i, (n, gi, v, ct) in enumerate(kills):
            adj = graph(n, gi)
            order = sorted(u for u in adj if u != v)
            c0 = {u: ct[i2] for i2, u in enumerate(order)}
            d, ex = depth(adj, v, c0, order)
            dist[(n, d)] += 1
            expl.append(ex)
            rows.append((n, gi, v, d, ex))
            if (i + 1) % 500 == 0:
                print(f"    {i+1}/{len(kills)}: {dict(sorted(dist.items(), key=lambda kv: (kv[0][0], kv[0][1] is None, kv[0][1])))}  [{time.time()-t0:.0f}s]", flush=True)
    else:
        step = int(os.environ.get('UD_STEP', '400'))
        k = 0
        for n in range(16, 23):
            for gi, adj in enumerate(EA.plantri_graphs(n, flags=('-c5',))):
                faces, ok = OF.faces_of(adj)
                for v in adj:
                    if len(adj[v]) != 5:
                        continue
                    order = sorted(u for u in adj if u != v)
                    pos = {u: i for i, u in enumerate(order)}
                    sub = {u: {w for w in adj[u] if w != v} for u in adj if u != v}
                    for ct in EA.all_colorings_mod_s4(sub, order):
                        c0 = {u: ct[pos[u]] for u in order}
                        if not IF.stuck(adj, v, c0):
                            continue
                        k += 1
                        if k % step:
                            continue
                        d, ex = depth(adj, v, c0, order)
                        dist[(n, d)] += 1
                        expl.append(ex)
                        rows.append((n, gi, v, d, ex))
    by_n = {}
    for (n, d), c in dist.items():
        by_n.setdefault(n, Counter())[d] += c
    print(f"\n  population {mode}: {len(rows)} configurations  [{time.time()-t0:.0f}s]")
    for n in sorted(by_n):
        print(f"    n={n}: depth {dict(sorted(by_n[n].items(), key=lambda kv: (kv[0] is None, kv[0])))}")
    alld = Counter(d for (n, d) in dist.elements())
    print(f"  ALL: {dict(sorted(alld.items(), key=lambda kv: (kv[0] is None, kv[0])))}; max reached depth "
          f"{max((d for d in alld if d is not None), default=None)}; unreached (>{MAXD} or cap) {alld.get(None, 0)}")
    print(f"  explored colorings per config: median {sorted(expl)[len(expl)//2]} max {max(expl)}")
    json.dump(rows, open(os.path.join(HERE, f'.unrestricted_depth_{mode}.json'), 'w'))
