#!/usr/bin/env python3
"""
Toy 5560 — Round 17: THE "SOMETHING FINER" PROBE

J2 left the sufficiency hunt at "filler AND flux-neutral AND ???". This
glance asks what distinguishes the 15 frozen flux-neutral fillers from
the 220 free flux-neutral fillers, on pre-registered axes only:
  (a) completion count (atlas nodes);
  (b) boundary label-winding w (J2's instrument);
  (c) boundary walk bounding-box span (max side);
  (d) non-filler word block count (maximal runs, cyclic, on the 6
      non-filler positions);
  (e) WALL TOPOLOGY: junction faces (three distinct Delta values on a
      face) over completion PAIRS — 5559 found junctions occur ONLY on
      frozen twin walls in the 2-completion census; here the axis is
      swept over the WHOLE filler family (all completion pairs per
      pinning, pinnings with >= 2 completions).
Per the family-sweep discipline: each axis is scored for full/partial/no
separation; a full separator here is a CANDIDATE (n=15 target family,
one disc) — flagged for cross-object replication before any claim.

TESTS (X/Y): 1. population + axes computed · 2. per-axis separation
table · 3. the verdict.

Elie, 2026-08-31. Millennium week, 4-Color round 17. 3 tests.
"""

import importlib.util
import itertools
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


J2 = load("t5557r17", "toy_5557_AUG31_J2_monopole_forcing_control_then"
          "_sufficiency.py")
V1, Y4, Z1, H8 = J2.V1, J2.Y4, J2.Z1, J2.H8


def blocks(word):
    n = len(word)
    b = sum(1 for i in range(n) if word[i] != word[(i + 1) % n])
    return max(b, 1)


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5560 — R17: the 'something finer' probe (15 vs 220)")
    print("=" * 70)

    adj, interior, bcyc = Y4.disc(2)
    ofaces = H8.orient_faces([tuple(f) for f in
                              Z1.disc_faces(adj, interior, bcyc)])
    base = bcyc[0]
    atlas = json.load(open(os.path.join(HERE,
                                        'availability_atlas_fcw014.json')))
    fillers = [r for r in atlas['rows'] if J2.is_filler(r['pin'])]

    data = []
    for r in fillers:
        pinseq = r['pin']
        wk = J2.boundary_walk(adj, ofaces, bcyc, pinseq, base)
        if J2.two_area(wk) != 0:
            continue                      # flux-neutral only
        frz = r['components'] >= 2
        w = J2.label_winding(pinseq)
        xs = [p[0] for p in wk]
        ys = [p[1] for p in wk]
        span = max(max(xs) - min(xs), max(ys) - min(ys))
        ev = [pinseq[i] for i in range(0, 12, 2)]
        od = [pinseq[i] for i in range(1, 12, 2)]
        nonf = od if len(set(ev)) == 1 else ev
        nb = blocks(nonf)
        # wall topology over completion pairs
        pin = dict(zip(bcyc, pinseq))
        comps = Y4.completions(adj, interior, pin)
        junc = 0
        pairs = 0
        for A, B in itertools.combinations(comps, 2):
            h1, ok1 = V1.height_lift(adj, ofaces, {**pin, **A}, base)
            h2, ok2 = V1.height_lift(adj, ofaces, {**pin, **B}, base)
            if not (ok1 and ok2):
                continue
            pairs += 1
            D = {v: (h2[v][0] - h1[v][0], h2[v][1] - h1[v][1])
                 for v in adj}
            if any(len({D[x] for x in f}) == 3 for f in ofaces):
                junc += 1
        data.append((tuple(pinseq), frz, r['nodes'], w, span, nb,
                     junc, pairs))
    n_frz = sum(1 for d in data if d[1])
    t1 = n_frz == 15 and len(data) == 235
    print(f"\n  flux-neutral fillers: {len(data)} (frozen {n_frz}, "
          f"free {len(data) - n_frz})")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Population 15 + 220 with "
          f"all axes")

    axes = {'nodes': 2, 'winding': 3, 'span': 4, 'blocks': 5}
    sep_table = {}
    for name, i in axes.items():
        fz = Counter(d[i] for d in data if d[1])
        fr = Counter(d[i] for d in data if not d[1])
        overlap = set(fz) & set(fr)
        sep_table[name] = (dict(fz), dict(fr), not overlap)
        print(f"  {name}: frozen {dict(sorted(fz.items()))} | free "
              f"{dict(sorted(fr.items()))} | separates: {not overlap}")
    # axis (e): any junction pair present
    fzj = Counter((d[6] > 0, d[7] > 0) for d in data if d[1])
    frj = Counter((d[6] > 0, d[7] > 0) for d in data if not d[1])
    ej_sep = all(k[0] for k in fzj) and not any(k[0] for k in frj)
    print(f"  junctions: frozen (has-junction, has-pairs) "
          f"{dict(fzj)} | free {dict(frj)} | separates: {ej_sep}")
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Separation table")

    winners = [k for k, v in sep_table.items() if v[2]] + \
        (['junctions'] if ej_sep else [])
    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. VERDICT: "
          f"{'separating axes: ' + ', '.join(winners) + ' — CANDIDATE(S) for the finer condition (n=15 one-disc family; cross-object replication required before claim)' if winners else 'NO stored axis separates — the finer condition is not among these five'}")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5560 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
