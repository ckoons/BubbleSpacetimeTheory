#!/usr/bin/env python3
"""
Toy 5596 — IN-FRAME EXISTENCE FIRST: 5-connected triangulations
(plantri -c5), n = 12..22, every degree-5 vertex v — does T-v have ANY
stuck coloring (tau_v = 6, not directly freeable)? Then, where stuck
colorings exist, class-insertability (every Kempe class of T-v
contains an insertable coloring?).

Frame (K1838, Casey's call pending): a minimal counterexample to 4CT
is internally 6-connected (hence 5-connected, min degree 5). OWL is
needed only there. If no 5-connected triangulation through n = 22 has
a stuck coloring at any degree-5 vertex, the honest sentence is
"in-frame OWL untested" — and the out-of-frame census (2,927) is
evidence about a different class.

ENUMERATION: all proper 4-colorings of T-v mod S4 (5594's enumerator;
cap per (T,v); cap-hit = 'not-enumerated', never counted). Stuck =
tau_v(c) = 6 and not freeable. Per (T, v): #colorings, #stuck, and if
#stuck > 0: classes, classes with an insertable member, and whether
every stuck coloring's class has one.

Elie, 2026-09-02.
"""

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


EA = load("t5594if", "toy_5594_SEP2_EA_class_insertability_kempe_classes"
          "_of_T_minus_v.py")
G5 = EA.G5
X3 = load("x3if", "toy_5521_AUG30_X3_commutator_laboratory_support_"
          + [f for f in os.listdir(HERE) if f.startswith('toy_5521_')][0][len('toy_5521_AUG30_X3_commutator_laboratory_support_'):])


def stuck(adj, v, col):
    return G5.operational_tau(adj, col, v) == 6 and not X3.freeable(adj, col, v)


if __name__ == "__main__":
    ns = [int(x) for x in sys.argv[1:]] or list(range(12, 23))
    print("=" * 70)
    print(f"Toy 5596 — in-frame existence: plantri -c5, n = {ns}")
    print("=" * 70)
    summary = {}
    kills = []
    for n in ns:
        gs = EA.plantri_graphs(n, flags=('-c5',))
        t0 = time.time()
        cnt = Counter()
        stuck_pairs = []
        for gi, adj in enumerate(gs):
            for v in adj:
                if len(adj[v]) != 5:
                    continue
                order = sorted(u for u in adj if u != v)
                pos = {u: i for i, u in enumerate(order)}
                sub = {u: {w for w in adj[u] if w != v} for u in adj if u != v}
                cols = EA.all_colorings_mod_s4(sub, order)
                if len(cols) > EA.CAP_COLORINGS:
                    cnt['not-enumerated'] += 1
                    continue
                cnt['pairs'] += 1
                cnt['colorings'] += len(cols)
                st = [ct for ct in cols if stuck(adj, v, {u: ct[pos[u]] for u in order})]
                cnt['stuck'] += len(st)
                if st:
                    cnt['pairs_with_stuck'] += 1
                    classes, _ = EA.kempe_classes(adj, v, order)
                    cls_of = {}
                    for k, cl in enumerate(classes):
                        for ct in cl:
                            cls_of[ct] = k
                    ins_cls = set()
                    for k, cl in enumerate(classes):
                        if any(EA.insertable(adj, v, {u: ct[pos[u]] for u in order}) for ct in cl):
                            ins_cls.add(k)
                    bad = [ct for ct in st if cls_of[ct] not in ins_cls]
                    cnt['classes'] += len(classes)
                    cnt['classes_ins'] += len(ins_cls)
                    stuck_pairs.append((gi, v, len(st), len(classes), len(ins_cls), len(bad)))
                    if bad:
                        kills.append((n, gi, v, len(bad), len(st), len(classes)))
        summary[n] = dict(cnt)
        print(f"  n={n}: graphs {len(gs)}; (T,v) pairs {cnt['pairs']} "
              f"(not-enumerated {cnt['not-enumerated']}); colorings mod S4 "
              f"{cnt['colorings']}; STUCK colorings {cnt['stuck']} in "
              f"{cnt['pairs_with_stuck']} pairs; classes {cnt['classes']} / "
              f"with insertable member {cnt['classes_ins']}; stuck-in-"
              f"non-insertable-class {sum(p[5] for p in stuck_pairs)}  "
              f"[{time.time() - t0:.0f}s]", flush=True)
        for p in stuck_pairs[:12]:
            print(f"      stuck pair (graph, v, #stuck, #classes, #ins, #bad): {p}", flush=True)
    tot_stuck = sum(s.get('stuck', 0) for s in summary.values())
    print(f"\n  IN-FRAME EXISTENCE: stuck configurations through n={max(ns)}: "
          f"{tot_stuck}; kills (stuck coloring in a class with no insertable "
          f"member): {len(kills)} {kills[:10]}")
    print("  " + ("IN-FRAME OWL UNTESTED — no stuck configuration exists in the frame through this n"
                  if tot_stuck == 0 else
                  "in-frame stuck configurations EXIST — class-insertability rendered above"))
    json.dump({'summary': {str(k): v for k, v in summary.items()}, 'kills': kills},
              open(os.path.join(HERE, '.in_frame_existence.json'), 'w'), indent=1)
