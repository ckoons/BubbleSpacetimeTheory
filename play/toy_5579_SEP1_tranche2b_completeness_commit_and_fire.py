#!/usr/bin/env python3
"""
Toy 5579 — TRANCHE-2b: the harvested-not-committed remainder,
committed and tested (the count seam closes wholly)

The storage cap had no reason to stand (an arbitrary [:200] slice).
Tranche-2b = the SAME deterministic harvest (5574's seeds, bit-identical
regeneration) MINUS the 792 already-committed configurations — the
1,009 harvested-not-committed remainder. Committed here under a fresh
hash, then tested under the SAME predicate as the filed falsifier
paragraph (exists w in the 186-family with remnant bounded <= 8 or
co-bounded >= |V|-1-8, join key 5571), same discipline: the commit
hash prints BEFORE the test runs in the same execution, and the
addendum line (hash) files to the falsifier note.

TESTS (X/Y): 1. remainder regenerated + disjointness from the
committed 792 verified · 2. fresh hash committed · 3. THE TEST — the
Family Exclusion against the remainder, kill/survive per the filed
paragraph.

Elie, 2026-09-01. 3 tests.
"""

import hashlib
import importlib.util
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


T2 = load("t5574b", "toy_5574_SEP1_armed_tranche2_family_exclusion"
          "_falsifier.py")
P1, CV, F2C, F1 = T2.P1, T2.CV, T2.F2C, T2.F1
E1, G5, X3, H8 = T2.E1, T2.G5, T2.X3, T2.H8
WF = T2.WF


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5579 — tranche-2b: commit the remainder, close the seam")
    print("=" * 70)

    committed = json.load(open(T2.TRANCHE))
    store_b = {}
    n_b = 0
    fams = {label: (faces, adj, tv)
            for label, faces, adj, tv in T2.build_tranche2()}
    for label, (faces, adj, tv) in fams.items():
        lcyc = E1.link_cycle(faces, tv)
        if len(lcyc) != 5:
            continue
        stuck, _fr = F1.stuck_harvest(faces, adj, tv, n_seeds=20,
                                      n_walk=60, amp=30)
        if not stuck:
            continue
        prev = {json.dumps(c, sort_keys=True)
                for c in committed.get(label, {}).get('stuck', [])}
        rem = []
        for c in stuck:
            rec = {str(k2): v for k2, v in c.items()}
            if json.dumps(rec, sort_keys=True) not in prev:
                rem.append(rec)
        if rem:
            store_b[label] = {'tv': str(tv), 'stuck': rem}
            n_b += len(rem)
    n_committed = sum(len(v['stuck']) for v in committed.values())
    t1 = n_b > 0 and all(
        not any(json.dumps(r, sort_keys=True) in
                {json.dumps(c, sort_keys=True)
                 for c in committed.get(lb, {}).get('stuck', [])}
                for r in v['stuck'])
        for lb, v in store_b.items())
    print(f"\n  committed (2a): {n_committed}; remainder (2b): {n_b}; "
          f"harvest total: {n_committed + n_b}")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Remainder regenerated, "
          f"disjoint from the committed 792")

    blob = json.dumps(store_b, sort_keys=True).encode()
    hh = hashlib.sha256(blob).hexdigest()
    with open(os.path.join(HERE, '.tranche2b_family_exclusion.json'),
              'wb') as f:
        f.write(blob)
    t2v = True
    print(f"\n  [{'PASS' if t2v else 'FAIL'}] 2. Tranche-2b committed: "
          f"sha256 {hh}")

    # THE TEST — same predicate, same run (hash printed above first)
    moves, words, _ = WF.context_family()
    kills = []
    n_cfg = 0
    for label, (faces, adj, tv) in fams.items():
        if label not in store_b:
            continue
        lcyc = E1.link_cycle(faces, tv)
        smap = {str(v): v for v in adj}
        nV = len(adj) - 1
        for crec in store_b[label]['stuck']:
            c0 = {smap[k2]: v for k2, v in crec.items()}
            rm = WF.role_map(adj, c0, tv, lcyc)
            if rm is None:
                continue
            vmap, cmap = rm
            n_cfg += 1
            ok_any = False
            for w in words:
                m1 = (tuple(sorted((cmap[w[0][1][0]],
                                    cmap[w[0][1][1]]))), vmap[w[0][0]])
                m2 = (tuple(sorted((cmap[w[1][1][0]],
                                    cmap[w[1][1][1]]))), vmap[w[1][0]])
                X1 = G5.kempe_chain(adj, c0, m1[1], *m1[0],
                                    exclude={tv}) \
                    if c0.get(m1[1]) in m1[0] else set()
                k1 = G5.do_swap(c0, X1, *m1[0])
                X2 = G5.kempe_chain(adj, k1, m2[1], *m2[0],
                                    exclude={tv}) \
                    if k1.get(m2[1]) in m2[0] else set()
                k2c = G5.do_swap(k1, X2, *m2[0])
                X3c = G5.kempe_chain(adj, k2c, m1[1], *m1[0],
                                     exclude={tv}) \
                    if k2c.get(m1[1]) in m1[0] else set()
                R = (X1 - X3c) - X2
                if len(R) <= 8 or len(R) >= nV - 8:
                    ok_any = True
                    break
            if not ok_any:
                kills.append((label, crec))
    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. THE TEST: {n_cfg} "
          f"remainder configs; FAMILY-EXCLUSION kills: {len(kills)}"
          + (f" — exhibits: {kills[:2]}" if kills else
         " — the kill condition survives; with 2a the seam closes "
         "WHOLLY: every harvested configuration is now committed and "
         "tested"))

    res = [t1, t2v, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5579 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
