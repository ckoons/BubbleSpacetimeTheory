#!/usr/bin/env python3
"""
Toy 5589 — LEGAL-ONLY DGT ON THE 1,801, and every residue (both
loops) against DEEP per-hole freed sets

5586 counted DGT on the 1,801 BEFORE legality (K1835 A2) and left 77
no-descent configurations, most stalling at d-hat <= 4 against
shallow samples (71-803 targets per hole). 5587 showed the legal-only
count is lower. This toy does both halves the record now owes:

(1) THE A2 COUNT on the 1,801: 5587's legal_iterate (fully-legal
    family words only, strict d-hat descent, halt at gate phase, cap
    d-hat+1) against the same shallow samples (bit-identical).
(2) THE DEEPENING: for every hole carrying residue under EITHER loop,
    build a deep tau<=5 set (5583/5588 method: 150 backtrack seeds x
    200-step Kempe walks + 400 x 10-step targeted walks FROM each
    residue stall), hash-commit it, then retest every residue
    configuration from c0 under both loops against the deep set.
    Pre-scored: DISSOLVES (freed) or HARDENS (still no descent — a
    candidate gate-phase Kempe-locked hole, exhibited whole, kill
    only after Lyra/Cal read the anatomy). Both outcomes informative.

BLIND: per-config verdicts hashed BEFORE the counts. k/N only.

TESTS (X/Y): 1. legal-only DGT on the 1,801, k/N (can fail) ·
2. pre-legality residue reproduced at 77 · 3. deep sets committed ·
4. pre-legality residue vs deep, dissolved k/77 (can fail) ·
5. legal-only residue vs deep, dissolved k/N (can fail).

Elie, 2026-09-02. 5 tests.
"""

import hashlib
import importlib.util
import json
import os
import random
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


D6 = load("t5586lo", "toy_5586_SEP2_DGT_descent_given_target_on_the_1801"
          "_tranche_census.py")
LG = load("t5587lo", "toy_5587_SEP2_legality_recount_K1835_A2_fully"
          "_legal_and_descending.py")
W, TE, T2 = D6.W, D6.TE, D6.T2
E1, G5, X3, WF, F1 = D6.E1, D6.G5, D6.X3, D6.WF, D6.F1


def deep_set(adj, tv, vs, freed0, stalls, tag):
    seen = set()
    deep = []

    def add(c):
        key = tuple(c[v] for v in vs)
        if key not in seen:
            seen.add(key)
            if G5.operational_tau(adj, c, tv) <= 5:
                deep.append(dict(c))

    for f in freed0:
        add(f)
    for s in range(150):
        cc = E1.bt_color(adj, tv, s)
        if cc is None:
            continue
        add(cc)
        cur = cc
        for step in range(200):
            rng = random.Random(s * 9173 + step)
            u = rng.choice(vs)
            a = cur[u]
            b = rng.choice([x for x in range(4) if x != a])
            comp = G5.kempe_chain(adj, cur, u, a, b, exclude={tv})
            cur = G5.do_swap(cur, comp, a, b)
            add(cur)
    for si, stall in enumerate(stalls):
        for s in range(400):
            cur = dict(stall)
            for step in range(10):
                rng = random.Random(99000 + tag * 7 + si * 100003
                                    + s * 131 + step)
                u = rng.choice(vs)
                a = cur[u]
                b = rng.choice([x for x in range(4) if x != a])
                comp = G5.kempe_chain(adj, cur, u, a, b, exclude={tv})
                cur = G5.do_swap(cur, comp, a, b)
                add(cur)
    return deep


def walk_to_stall(adj, tv, vs, lcyc, c0, freed, words, legal):
    """Replay the loop and return the configuration where it stops."""
    c = dict(c0)
    d = LG.dmin(c, freed, vs)
    for _ in range(d + 1):
        if G5.operational_tau(adj, c, tv) <= 5 or X3.freeable(adj, c, tv):
            return c
        if legal:
            imgs = [(w, k) for w, k, fl in
                    LG.word_images_legal(adj, c, tv, lcyc, words) if all(fl)]
        else:
            imgs = TE.word_images(adj, c, tv, lcyc, words)
        best = None
        for w, k in imgs:
            dk = LG.dmin(k, freed, vs)
            if dk < d and (best is None or dk < best[0]):
                best = (dk, k)
        if best is None:
            return c
        d, c = best
    return c


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5589 — legal-only DGT on the 1,801; residue vs deep sets")
    print("=" * 70)

    stores = []
    for fn, pre in D6.FILES:
        raw = open(os.path.join(HERE, fn), 'rb').read()
        assert hashlib.sha256(raw).hexdigest().startswith(pre)
        stores.append((fn, json.loads(raw)))
    fams = {label: (faces, adj, tv)
            for label, faces, adj, tv in T2.build_tranche2()}
    freed_by = {}
    for label, (faces, adj, tv) in fams.items():
        if len(E1.link_cycle(faces, tv)) != 5:
            continue
        _st, fr = F1.stuck_harvest(faces, adj, tv, n_seeds=20,
                                   n_walk=60, amp=30)
        freed_by[label] = fr
    moves, words, _ = WF.context_family()

    records = []
    for fn, st in stores:
        tr = '2a' if 'tranche2_' in fn else '2b'
        for label, blk in st.items():
            faces, adj, tv = fams[label]
            lcyc = E1.link_cycle(faces, tv)
            smap = {str(v): v for v in adj}
            vs = [v for v in sorted(adj, key=str) if v != tv]
            freed = freed_by[label]
            W.iterate_chain.lcyc = lcyc
            for i, crec in enumerate(blk['stuck']):
                c0 = {smap[k]: v for k, v in crec.items()}
                d0 = LG.dmin(c0, freed, vs)
                ocL, stL, tjL = LG.legal_iterate(adj, tv, vs, lcyc, c0,
                                                 freed, words, d0 + 1)
                ocS, stS, tjS = W.iterate_chain(adj, tv, vs, c0, freed,
                                                words, d0 + 1)
                records.append([tr, label, i, d0, (ocL, stL, tuple(tjL)),
                                (ocS, stS, tuple(tjS)), c0])
    blob = json.dumps([str(r[:6]) for r in records]).encode()
    print(f"\n  1,801 shallow verdicts (legal-only + switching) hashed "
          f"BEFORE the count: sha256 "
          f"{hashlib.sha256(blob).hexdigest()[:32]}...")

    n = len(records)
    kL = sum(1 for r in records if r[4][0] == 'freed')
    kS = sum(1 for r in records if r[5][0] == 'freed')
    byhole = {}
    for r in records:
        byhole.setdefault((r[0], r[1]), [0, 0, 0])
        byhole[(r[0], r[1])][0] += 1
        byhole[(r[0], r[1])][1] += r[4][0] == 'freed'
        byhole[(r[0], r[1])][2] += r[5][0] == 'freed'
    stepsL = Counter(r[4][1] for r in records if r[4][0] == 'freed')
    t1 = kL == n
    print(f"\n  by hole (n, legal-only freed, switching freed):")
    for k in sorted(byhole):
        print(f"    {k[0]} {k[1]}: {byhole[k]}")
    print(f"  legal-only step-counts: {dict(sorted(stepsL.items()))}")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. LEGAL-ONLY DGT on the "
          f"1,801 (shallow): {kL}/{n}")
    t2 = (n - kS) == 77
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Pre-legality residue "
          f"reproduced: {n - kS} (5586: 77)")

    # deep sets per residue hole
    res_holes = sorted({(r[0], r[1]) for r in records
                        if r[4][0] != 'freed' or r[5][0] != 'freed'})
    holes_needed = sorted({lb for _tr, lb in res_holes})
    deep_by = {}
    hashes = {}
    for hi, label in enumerate(holes_needed):
        faces, adj, tv = fams[label]
        lcyc = E1.link_cycle(faces, tv)
        vs = [v for v in sorted(adj, key=str) if v != tv]
        stalls = []
        for r in records:
            if r[1] != label:
                continue
            if r[4][0] != 'freed':
                stalls.append(walk_to_stall(adj, tv, vs, lcyc, r[6],
                                            freed_by[label], words, True))
            if r[5][0] != 'freed':
                stalls.append(walk_to_stall(adj, tv, vs, lcyc, r[6],
                                            freed_by[label], words, False))
        deep = deep_set(adj, tv, vs, freed_by[label], stalls, hi)
        deep_by[label] = deep
        hb = json.dumps(sorted(str(tuple(f[v] for v in vs))
                               for f in deep)).encode()
        hashes[label] = hashlib.sha256(hb).hexdigest()[:16]
        print(f"  deep set {label}: {len(deep)} (shallow "
              f"{len(freed_by[label])}; {len(stalls)} stalls seeded) "
              f"sha256 {hashes[label]}...")
    t3 = all(len(deep_by[lb]) > len(freed_by[lb]) for lb in holes_needed)
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Deep sets committed for "
          f"{len(holes_needed)} residue holes")

    # retests
    retL = []
    retS = []
    for r in records:
        tr, label, i, d0, vL, vS, c0 = r
        if vL[0] == 'freed' and vS[0] == 'freed':
            continue
        faces, adj, tv = fams[label]
        lcyc = E1.link_cycle(faces, tv)
        vs = [v for v in sorted(adj, key=str) if v != tv]
        deep = deep_by[label]
        dd = LG.dmin(c0, deep, vs)
        W.iterate_chain.lcyc = lcyc
        if vL[0] != 'freed':
            oc, stp, tj = LG.legal_iterate(adj, tv, vs, lcyc, c0, deep,
                                           words, dd + 1)
            retL.append((tr, label, i, d0, vL[2], oc, tuple(tj)))
        if vS[0] != 'freed':
            oc, stp, tj = W.iterate_chain(adj, tv, vs, c0, deep, words,
                                          dd + 1)
            retS.append((tr, label, i, d0, vS[2], oc, tuple(tj)))
    blob = json.dumps([str(x) for x in retL + retS]).encode()
    print(f"\n  retest verdicts hashed BEFORE the count: sha256 "
          f"{hashlib.sha256(blob).hexdigest()[:32]}...")

    k4 = sum(1 for x in retS if x[5] == 'freed')
    t4 = k4 == len(retS)
    hardS = [x for x in retS if x[5] != 'freed']
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Pre-legality residue vs "
          f"deep: DISSOLVED {k4}/{len(retS)}; HARDENED {len(hardS)} "
          f"{[x[:4] + (x[6],) for x in hardS[:12]]}")
    k5 = sum(1 for x in retL if x[5] == 'freed')
    t5 = k5 == len(retL)
    hardL = [x for x in retL if x[5] != 'freed']
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. Legal-only residue vs "
          f"deep: DISSOLVED {k5}/{len(retL)}; HARDENED {len(hardL)} by "
          f"hole {dict(Counter((x[0], x[1]) for x in hardL))}")
    for x in hardL[:20]:
        print(f"    hardened(legal): {x[:4]} shallow {x[4]} -> deep {x[6]}")

    res = [t1, t2, t3, t4, t5]
    print(f"\n{'=' * 70}")
    print(f"Toy 5589 -- SCORE: {sum(res)}/{len(res)}  (can-fail: 1, 4, 5)")
    print(f"{'=' * 70}")
