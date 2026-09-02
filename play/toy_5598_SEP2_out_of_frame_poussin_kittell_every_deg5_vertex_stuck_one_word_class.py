#!/usr/bin/env python3
"""
Toy 5598 — OUT-OF-FRAME POPULATIONS ADDED: Poussin (15 v) and Kittell
(23 v), EVERY degree-5 vertex — exhaustive colorings of T-v mod S4,
stuck count, the one-word test on every stuck coloring, and
class-insertability.

Soifer (9 v, 20 e) = Fritsch minus one edge (MathWorld): not a
triangulation; as a triangulation it is Fritsch (already exhaustive).
Heawood's 25-vertex map: no verified adjacency in reach — not added.

Poussin from Sage's constructor (smallgraphs.py, verbatim rules);
Kittell from G5 (Sage edge dict). Both checked as triangulations
(3n-6 edges, Euler) before use.

Elie, 2026-09-02.
"""

import importlib.util
import os
import time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


IF = load("t5596of", "toy_5596_SEP2_in_frame_existence_5connected_n12_22_stuck"
          "_configurations_and_class_insertability.py")
EA, G5, X3 = IF.EA, IF.G5, IF.X3
LG = load("t5587of", "toy_5587_SEP2_legality_recount_K1835_A2_fully_legal"
          "_and_descending.py")
E1, WF = LG.E1, LG.WF


def poussin():
    adj = {i: set() for i in range(15)}

    def e(a, b):
        adj[a].add(b)
        adj[b].add(a)
    for a, bs in {2: [7, 8, 3, 4], 1: [7, 6], 0: [6, 5, 4], 3: [5]}.items():
        for b in bs:
            e(a, b)
    for cyc in (list(range(3)), list(range(3, 9)), list(range(9, 14))):
        for i in range(len(cyc)):
            e(cyc[i], cyc[(i + 1) % len(cyc)])
    path = [8, 12, 7, 11, 6, 10, 5, 9, 3, 13, 8, 12]
    for i in range(len(path) - 1):
        e(path[i], path[i + 1])
    for i in range(9, 14):
        e(14, i)
    return adj


def faces_of(adj):
    tris, ok, _m = G5.faces_from_adj_triangulation(adj)
    return tris, ok


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5598 — out-of-frame: Poussin and Kittell, every degree-5 vertex")
    print("=" * 70)
    moves, words, _ = WF.context_family()
    for name, adj in (('Poussin', poussin()), ('Kittell', {k: set(v) for k, v in G5.kittell_adj().items()})):
        n = len(adj)
        m = sum(len(v) for v in adj.values()) // 2
        faces, ok = faces_of(adj)
        degs = Counter(len(v) for v in adj.values())
        print(f"\n  {name}: n={n}, m={m} (3n-6={3*n-6}), triangulation faces ok={ok}, degrees {dict(sorted(degs.items()))}")
        tot = Counter()
        for v in sorted(adj):
            if len(adj[v]) != 5:
                continue
            t0 = time.time()
            order = sorted(u for u in adj if u != v)
            pos = {u: i for i, u in enumerate(order)}
            sub = {u: {w for w in adj[u] if w != v} for u in adj if u != v}
            cols = EA.all_colorings_mod_s4(sub, order)
            st = [ct for ct in cols if IF.stuck(adj, v, {u: ct[pos[u]] for u in order})]
            lcyc = E1.link_cycle(faces, v)
            one = 0
            nocx = 0
            for ct in st:
                c0 = {u: ct[pos[u]] for u in order}
                imgs = LG.word_images_legal(adj, c0, v, lcyc, words)
                if imgs is None:
                    nocx += 1
                    continue
                if any(all(fl) and len({k[u] for u in adj[v]}) < 4 for w, k, fl in imgs):
                    one += 1
            classes, _ = EA.kempe_classes(adj, v, order)
            ins_cls = sum(1 for cl in classes if any(EA.insertable(adj, v, {u: ct[pos[u]] for u in order}) for ct in cl))
            cls_of = {ct: k for k, cl in enumerate(classes) for ct in cl}
            ins_set = {k for k, cl in enumerate(classes) if any(EA.insertable(adj, v, {u: ct[pos[u]] for u in order}) for ct in cl)}
            bad = sum(1 for ct in st if cls_of[ct] not in ins_set)
            tot['pairs'] += 1
            tot['stuck'] += len(st)
            tot['one'] += one
            tot['nocx'] += nocx
            tot['classes'] += len(classes)
            tot['cls_ins'] += ins_cls
            tot['bad'] += bad
            print(f"    v={v}: colorings {len(cols)}, stuck {len(st)}, one-word direct {one}/{len(st)} "
                  f"(no-context {nocx}), classes {len(classes)} sizes {sorted(len(c) for c in classes)}, "
                  f"insertable classes {ins_cls}, stuck-in-non-insertable-class {bad}  [{time.time()-t0:.0f}s]", flush=True)
        print(f"  {name} TOTAL: deg-5 vertices {tot['pairs']}, stuck {tot['stuck']}, ONE-WORD {tot['one']}/{tot['stuck']}, "
              f"classes {tot['classes']} / insertable {tot['cls_ins']}, kills {tot['bad']}")
