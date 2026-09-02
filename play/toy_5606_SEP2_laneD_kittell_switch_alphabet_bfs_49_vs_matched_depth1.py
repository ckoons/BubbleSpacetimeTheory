#!/usr/bin/env python3
"""
Toy 5606 — LANE D: breadth-first search in KITTELL'S SWITCH ALPHABET
from each of the 49 two-word-locked witnesses and a matched depth-1
sample, to the first gate-phase coloring

Kittell's eight chains (Gethner et al. 2009, Definition 5, link v1..v5
colored G,R,G,B,Y; v1,v3 the G-copies, v2 = R between them, v4 = B
adjacent to v3, v5 = Y adjacent to v1):
  alpha: RB from v2|v4 · beta: RY from v2|v5 · gamma: GY from v1|v5 ·
  delta: GB from v3|v4 · epsilon: BY from v4|v5 · zeta: GB from v1|v4 ·
  eta: GY from v3|v5 · theta: RG from v2|v1.
In our roles: G = r (copies B1, B2), R = s_M (n_sM), B and Y = the two
singletons; which singleton is adjacent to which copy is read off the
link at EVERY node (the frame is re-derived per node: One-Context).
Each chain with each seed option is one Kempe swap; a node's
generator set is these <= 16 swaps. BFS over STUCK nodes; stop at the
first gate-phase coloring (direct or tau <= 5). Report: switch
distance per start; orbit size = number of distinct stuck colorings
reachable by the switch alphabet before exit is forced (BFS closure
over stuck nodes, capped); the matched depth-1 sample = for each
witness, a depth-1 stuck coloring on the SAME (T, v) (first one in
canonical enumeration order after the witness), same statistics.

Elie, 2026-09-02.
"""

import importlib.util
import json
import os
import time
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


K = load("t5601d", "toy_5601_SEP2_in_frame_not_hit_334_gate_phase_depth_bfs"
         "_single_swap_null.py")
OF, IF, EA, G5, X3, LG, E1, WF = K.OF, K.IF, K.EA, K.G5, K.X3, K.LG, K.E1, K.WF
CAP = 20000


def kittell_generators(adj, tv, lcyc, c):
    """The <=16 single swaps of Kittell's eight chains at a stuck node."""
    rm = WF.role_map(adj, c, tv, lcyc)
    if rm is None:
        return None
    vmap, cmap = rm
    r, sM = cmap['r'], cmap['s_M']
    B1, B2, nM = vmap['B1'], vmap['B2'], vmap['n_sM']
    # v1, v3 = copies; v2 = n_sM; v4 adjacent to v3, v5 adjacent to v1
    v1, v3 = B1, B2
    v4 = next(u for u in (vmap['n_si'], vmap['n_sj']) if u in adj[v3])
    v5 = next(u for u in (vmap['n_si'], vmap['n_sj']) if u in adj[v1])
    G, R, Bc, Y = r, sM, c[v4], c[v5]
    chains = [((R, Bc), (nM, v4)), ((R, Y), (nM, v5)), ((G, Y), (v1, v5)),
              ((G, Bc), (v3, v4)), ((Bc, Y), (v4, v5)), ((G, Bc), (v1, v4)),
              ((G, Y), (v3, v5)), ((R, G), (nM, v1))]
    gens = []
    for (a, b), seeds in chains:
        for s in seeds:
            if c[s] in (a, b):
                gens.append((s, a, b))
    return gens


def bfs_switch(adj, tv, lcyc, c0, order):
    key0 = tuple(c0[u] for u in order)
    seen = {key0}
    q = deque([(c0, 0)])
    dist = None
    while q:
        c, d = q.popleft()
        gens = kittell_generators(adj, tv, lcyc, c)
        if gens is None:
            continue
        for s, a, b in gens:
            ch = G5.kempe_chain(adj, c, s, a, b, exclude={tv})
            k = G5.do_swap(c, ch, a, b)
            key = tuple(k[u] for u in order)
            if key in seen:
                continue
            if K.gate(adj, tv, k):
                if dist is None:
                    dist = d + 1
                continue          # exits are not expanded
            seen.add(key)
            if len(seen) < CAP:
                q.append((k, d + 1))
    return dist, len(seen)


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5606 — Lane D: Kittell switch-alphabet BFS, the 49 vs matched depth-1")
    print("=" * 70)
    moves, words, _ = WF.context_family()
    wit = json.load(open(os.path.join(HERE, '.in_frame_26_two_word_locked.json'))) + \
        json.load(open(os.path.join(HERE, '.in_frame_23_two_word_locked_n22.json')))
    graphs = {}
    rows = []
    t0 = time.time()
    for W in wit:
        n, gi, v, ct = W['n'], W['graph_index_plantri_c5'], W['v'], W['coloring_mod_S4_sorted_order']
        if (n, gi) not in graphs:
            graphs[(n, gi)] = EA.plantri_graphs(n, flags=('-c5',))[gi]
        adj = graphs[(n, gi)]
        faces, ok = OF.faces_of(adj)
        order = sorted(u for u in adj if u != v)
        pos = {u: i for i, u in enumerate(order)}
        c0 = {u: ct[i] for i, u in enumerate(order)}
        lcyc = E1.link_cycle(faces, v)
        dW, oW = bfs_switch(adj, v, lcyc, c0, order)
        # matched depth-1 sample on the same (T, v): first stuck coloring after ct with a one-word gate exit
        sub = {u: {w for w in adj[u] if w != v} for u in adj if u != v}
        cols = EA.all_colorings_mod_s4(sub, order)
        i0 = cols.index(tuple(ct)) if tuple(ct) in cols else 0
        match = None
        for j in list(range(i0 + 1, len(cols))) + list(range(0, i0)):
            c1 = {u: cols[j][pos[u]] for u in order}
            if not IF.stuck(adj, v, c1):
                continue
            im = K.legal_images(adj, v, lcyc, c1, words)
            if any(K.gate(adj, v, k) for w, k in im):
                match = c1
                break
        dM, oM = bfs_switch(adj, v, lcyc, match, order) if match else (None, None)
        rows.append((n, gi, v, dW, oW, dM, oM))
        print(f"    n={n} g={gi} v={v}: WITNESS switch-distance {dW}, orbit(stuck, capped {CAP}) {oW} | "
              f"MATCHED depth-1: distance {dM}, orbit {oM}", flush=True)
    print(f"\n  [{time.time() - t0:.0f}s] switch-distance histogram — witnesses: "
          f"{dict(sorted(Counter(r[3] for r in rows).items(), key=lambda kv: (kv[0] is None, kv[0])))}; "
          f"matched depth-1: {dict(sorted(Counter(r[5] for r in rows).items(), key=lambda kv: (kv[0] is None, kv[0])))}")
    print(f"  orbit sizes — witnesses: min {min(r[4] for r in rows)} median {sorted(r[4] for r in rows)[len(rows)//2]} "
          f"max {max(r[4] for r in rows)}; matched: min {min(r[6] for r in rows if r[6])} median "
          f"{sorted(r[6] for r in rows if r[6])[len(rows)//2]} max {max(r[6] for r in rows if r[6])}")
    json.dump(rows, open(os.path.join(HERE, '.laneD_switch_bfs.json'), 'w'), indent=1)
