#!/usr/bin/env python3
"""
Toy 5590 — THE PATH-DEPENDENT LEGAL STALL, EXHIBITED: wall or plateau
under fully-legal words only

5588's sixth: from c0 (D-flip3, shallow trajectory 20->6) the
legal-only loop against the 38,111-element deep set walks to a
configuration at d-hat = 2, tau = 6, with ZERO fully-legal strictly-
descending family words — while a different stall of the same c0 has
five. First exhibit where greedy-min and "exists a descending word"
part company. This toy: (1) rebuilds the deep set bit-identically and
re-walks to the stall; (2) saves the coloring (.legal_stall_exhibit.
json) beside .j3_exhibit.json; (3) characterizes it under LEGAL
words: descending / sideways / ascending counts; the two nearest deep
targets and their difference sets; (4) the plateau probe — BFS over
legal sideways moves (bounded frontier), escape = legal descent or
gate phase — WALL or PLATEAU; (5) the vacuous-word view: which 3-swap
truncations descend here (the alphabet question, instantiated).

TESTS (X/Y): 1. deep set + stall reproduced (hash) · 2. exhibit
saved · 3. legal characterization · 4. WALL / PLATEAU (informative
either way) · 5. truncation descents listed.

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


R6 = load("t5588ex", "toy_5588_SEP2_residue6_deep_set_canonical_word_stage"
          "_table_truncation_alphabet.py")
LG, TE, W = R6.LG, R6.TE, R6.W
RD, E1, G5, X3, WF, F1 = R6.RD, R6.E1, R6.G5, R6.X3, R6.WF, R6.F1


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5590 — the path-dependent legal stall, exhibited")
    print("=" * 70)

    moves, words, _ = WF.context_family()
    fails = TE.failure_set()
    six = []
    for label, faces, adj, tv, lcyc, c0, vs, freed in fails:
        d0 = LG.dmin(c0, freed, vs)
        oc, st, tj = LG.legal_iterate(adj, tv, vs, lcyc, c0, freed,
                                      words, d0 + 1)
        if oc != 'freed':
            c = dict(c0)
            d = d0
            for _ in range(st):
                imgs = LG.word_images_legal(adj, c, tv, lcyc, words)
                best = None
                for w, k, fl in imgs:
                    if not all(fl):
                        continue
                    dk = LG.dmin(k, freed, vs)
                    if dk < d and (best is None or dk < best[0]):
                        best = (dk, k)
                d, c = best
            six.append((label, faces, adj, tv, lcyc, c0, c, vs, freed,
                        tuple(tj)))
    label, faces, adj, tv, lcyc, _c0, _c, vs, freed0, _tj = six[0]
    # deep set, 5588's construction verbatim
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
    for si, s6 in enumerate(six):
        stall = s6[6]
        for s in range(400):
            cur = dict(stall)
            for step in range(10):
                rng = random.Random(88000 + si * 100003 + s * 131 + step)
                u = rng.choice(vs)
                a = cur[u]
                b = rng.choice([x for x in range(4) if x != a])
                comp = G5.kempe_chain(adj, cur, u, a, b, exclude={tv})
                cur = G5.do_swap(cur, comp, a, b)
                add(cur)
    blob = json.dumps(sorted(str(tuple(f[v] for v in vs))
                             for f in deep)).encode()
    hd = hashlib.sha256(blob).hexdigest()

    # find the sixth: the one whose legal loop vs deep does not halt
    target = None
    for s6 in six:
        c0 = s6[5]
        dd = LG.dmin(c0, deep, vs)
        oc, st, tj = LG.legal_iterate(adj, tv, vs, lcyc, c0, deep, words,
                                      dd + 1)
        if oc != 'freed':
            # re-walk to the stall
            c = dict(c0)
            d = dd
            for _ in range(st):
                imgs = LG.word_images_legal(adj, c, tv, lcyc, words)
                best = None
                for w, k, fl in imgs:
                    if not all(fl):
                        continue
                    dk = LG.dmin(k, deep, vs)
                    if dk < d and (best is None or dk < best[0]):
                        best = (dk, k)
                d, c = best
            target = (s6[9], c0, c, tuple(tj))
            break
    t1 = target is not None and hd.startswith('cd2cfee8')
    print(f"\n  deep set {len(deep)} sha256 {hd[:16]}... (5588: cd2cfee8); "
          f"stall found: {target is not None}")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Deep set + stall reproduced")
    if target is None:
        raise SystemExit("stall not reproduced")
    tj_shallow, c0, stall, tj_deep = target

    ds = LG.dmin(stall, deep, vs)
    ex = {'object': label, 'tv': str(tv),
          'c0': {str(v): c0[v] for v in c0},
          'stall': {str(v): stall[v] for v in stall},
          'traj_shallow': list(tj_shallow), 'traj_deep': list(tj_deep),
          'd_deep': ds, 'deep_hash': hd}
    with open(os.path.join(HERE, '.legal_stall_exhibit.json'), 'w') as f:
        json.dump(ex, f, indent=1)
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Exhibit saved "
          f"(.legal_stall_exhibit.json): shallow traj {tj_shallow}, deep "
          f"traj {tj_deep}, d_deep {ds}, tau {G5.operational_tau(adj, stall, tv)}")

    imgs = LG.word_images_legal(adj, stall, tv, lcyc, words)
    legal = [(w, k) for w, k, fl in imgs if all(fl)]
    vac = [(w, k, fl) for w, k, fl in imgs if not all(fl)]
    cls = Counter()
    side = []
    for w, k in legal:
        dk = LG.dmin(k, deep, vs)
        cls['desc' if dk < ds else 'side' if dk == ds else 'asc'] += 1
        if dk == ds:
            side.append(k)
    near = sorted(deep, key=lambda f: TE.ham(stall, f, vs))[:2]
    diffs = [[str(v) for v in vs if stall[v] != f[v]] for f in near]
    rm = WF.role_map(adj, stall, tv, lcyc)
    t3 = cls['desc'] == 0
    print(f"\n  legal images {len(legal)} of {len(imgs)}: {dict(cls)}; "
          f"nearest two targets differ on {diffs}; roles "
          f"{ {k: str(v) for k, v in rm[0].items()} } colors {rm[1]}")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Legal characterization "
          f"(zero legal descents confirmed at the stall)")

    # plateau probe over legal sideways moves
    frontier = [dict(stall)]
    seen2 = {tuple(stall[v] for v in vs)}
    escaped = None
    rounds = 0
    for depth in range(6):
        rounds = depth + 1
        nxt = []
        for cc in frontier:
            im2 = LG.word_images_legal(adj, cc, tv, lcyc, words)
            if im2 is None:
                continue
            for w, k, fl in im2:
                if not all(fl):
                    continue
                key = tuple(k[v] for v in vs)
                if key in seen2:
                    continue
                dk = LG.dmin(k, deep, vs)
                if dk < ds or G5.operational_tau(adj, k, tv) <= 5 or \
                        X3.freeable(adj, k, tv):
                    escaped = (rounds, dk)
                    break
                if dk == ds and len(nxt) < 150:
                    seen2.add(key)
                    nxt.append(k)
            if escaped:
                break
        if escaped or not nxt:
            break
        frontier = nxt
    t4 = True
    verdict = (f"PLATEAU — legal sideways iteration escapes in {escaped[0]} "
               f"round(s) to d̂={escaped[1]} ({len(seen2)} plateau configs "
               f"explored): descent is non-strict here, bounded plateau"
               if escaped else
               f"WALL — no legal descent and no legal sideways escape in "
               f"{rounds} round(s) ({len(seen2)} plateau configs): a genuine "
               f"legal-locked candidate against 38k targets")
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. {verdict}")

    vd = Counter()
    for w, k, fl in vac:
        if LG.dmin(k, deep, vs) < ds:
            vd[fl] += 1
    t5 = True
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. Vacuous-stage (3-swap) "
          f"descents at the stall by shape: {dict(vd)} (total "
          f"{sum(vd.values())})")

    res = [t1, t2, t3, t4, t5]
    print(f"\n{'=' * 70}")
    print(f"Toy 5590 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
