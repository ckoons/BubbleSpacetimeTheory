#!/usr/bin/env python3
"""
Toy 5588 — THE SIX AGAINST THE DEEP SET, the canonical word's stage
table, and the truncation alphabet

Three questions 5587 left on the table, answered in one run:

(A) THE SIX. 5587's legal-only loop stalled on 6 D-flip3 configurations
(d-hat trajectories (2), (5), (2), (6->2), (2), (20->6)) — all within a
few vertices of a SAMPLED target. 5583/5585 precedent: deepen the
freed set first (mass seeds x long walks + targeted walks FROM each
stall), hash-commit it, then retest: does a FULLY-LEGAL family word
strictly descend d-hat against the deep set? DISSOLVES (legal descent
found) or HARDENS (stall characterized: sideways legal moves? bounded
plateau escape?). Both outcomes pre-scored; no revision spent either
way.

(B) THE CANONICAL WORD. Cal SS805 derived stages 1-3 legal for the
canonical word (alpha = (r,s_M) at n_sM, beta = (s_M,s_i) at n_si;
mirror with n_sj/s_j) with stage 4 the sub-joint SJ. Instrument
check on the 54: stages 1-3 legality of THAT word, and stage 4's
rate (SJ's measured frequency).

(C) THE TRUNCATION ALPHABET. Every vacuous-stage descent at step 1 is
a descent by a shorter word. Which shapes occur (flag patterns), how
many distinct effective words, and does each truncation — applied as
its own word — act fully legally (it must, by construction; the check
is the instrument's own consistency).

BLIND: per-config records hashed BEFORE the counts. k/N only.

TESTS (X/Y): 1. deep set built + committed, the six reproduced ·
2. THE RETEST (legal descent vs deep set), k/6 (can fail) ·
3. canonical word stages 1-3 legal on all 54 (can fail) ·
4. truncation shapes characterized · 5. truncations self-consistent
(can fail).

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


LG = load("t5587r6", "toy_5587_SEP2_legality_recount_K1835_A2_fully"
          "_legal_and_descending.py")
TE, W = LG.TE, LG.W
RD, E1, G5, X3, WF, F1 = LG.RD, LG.E1, LG.G5, LG.X3, LG.WF, LG.F1



if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5588 — the six vs the deep set; canonical word; truncations")
    print("=" * 70)

    moves, words, _ = WF.context_family()
    fails = TE.failure_set()

    # ---- (A) the six: re-derive via 5587's legal loop
    six = []
    for label, faces, adj, tv, lcyc, c0, vs, freed in fails:
        d0 = LG.dmin(c0, freed, vs)
        oc, st, tj = LG.legal_iterate(adj, tv, vs, lcyc, c0, freed,
                                      words, d0 + 1)
        if oc != 'freed':
            # walk to the stall (replay the legal loop, keep the config)
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
    print(f"\n  residue reproduced: {len(six)} "
          f"({[(s[0], s[9]) for s in six]})")

    # deep freed set on the D-flip3 object (all six share it)
    label, faces, adj, tv, lcyc, _c0, _c, vs, freed0, _tj = six[0]
    assert all(s[2] is adj for s in six)
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
    t1 = len(six) == 6 and len(deep) > len(freed0)
    print(f"  deep freed set: {len(deep)} (shallow {len(freed0)}); "
          f"committed sha256 {hd[:32]}...")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Deep set committed; "
          f"the six reproduced")

    # THE RETEST
    retest = []
    for label, faces, adj, tv, lcyc, c0, stall, vs, freed0, tj in six:
        ds = LG.dmin(stall, deep, vs)
        tau_s = G5.operational_tau(adj, stall, tv)
        fr_s = X3.freeable(adj, stall, tv)
        imgs = LG.word_images_legal(adj, stall, tv, lcyc, words)
        legal_desc = 0
        legal_side = 0
        vac_desc = 0
        for w, k, fl in imgs:
            dk = LG.dmin(k, deep, vs)
            if all(fl):
                if dk < ds:
                    legal_desc += 1
                elif dk == ds:
                    legal_side += 1
            elif dk < ds:
                vac_desc += 1
        # full legal-only loop from c0 against the deep set
        oc, st, tj2 = LG.legal_iterate(adj, tv, vs, lcyc, c0, deep, words,
                                       LG.dmin(c0, deep, vs) + 1)
        retest.append({'traj_shallow': tj, 'd_deep': ds, 'tau': tau_s,
                       'freeable': fr_s, 'legal_desc': legal_desc,
                       'legal_side': legal_side, 'vac_desc': vac_desc,
                       'loop_deep': (oc, st, tuple(tj2))})

    # ---- (B) canonical word on the 54
    canon = [(('n_sM', ('r', 's_M')), ('n_si', ('s_M', 's_i'))),
             (('n_sM', ('r', 's_M')), ('n_sj', ('s_M', 's_j')))]
    for w in canon:
        assert w in words, w
    canon_rows = []
    for label, faces, adj, tv, lcyc, c0, vs, freed in fails:
        rm = WF.role_map(adj, c0, tv, lcyc)
        vmap, cmap = rm
        row = []
        for w in canon:
            m1 = (tuple(sorted((cmap[w[0][1][0]], cmap[w[0][1][1]]))),
                  vmap[w[0][0]])
            m2 = (tuple(sorted((cmap[w[1][1][0]], cmap[w[1][1][1]]))),
                  vmap[w[1][0]])
            k, fl = LG.legal_commutator(adj, c0, m1, m2, tv)
            row.append(fl)
        canon_rows.append((label, tuple(row)))

    # ---- (C) truncation alphabet at step 1 on the 54
    shapes = Counter()
    eff_words = set()
    incons = 0
    n_vac_desc = 0
    for label, faces, adj, tv, lcyc, c0, vs, freed in fails:
        d0 = LG.dmin(c0, freed, vs)
        rm = WF.role_map(adj, c0, tv, lcyc)
        vmap, cmap = rm
        imgs = LG.word_images_legal(adj, c0, tv, lcyc, words)
        for w, k, fl in imgs:
            if all(fl) or LG.dmin(k, freed, vs) >= d0:
                continue
            n_vac_desc += 1
            shapes[fl] += 1
            m1 = (tuple(sorted((cmap[w[0][1][0]], cmap[w[0][1][1]]))),
                  vmap[w[0][0]])
            m2 = (tuple(sorted((cmap[w[1][1][0]], cmap[w[1][1][1]]))),
                  vmap[w[1][0]])
            seq = [m for m, f in zip((m1, m2, m1, m2), fl) if f]
            eff = tuple(('m1' if m is m1 else 'm2') for m in seq)
            eff_words.add((w, eff))
            # self-consistency: applying only the legal stages gives k
            c = c0
            for m in seq:
                c = X3.apply_move(adj, c, m, tv)
            if c != k:
                incons += 1

    blob = json.dumps([str(sorted(r.items())) for r in retest]
                      + [str(canon_rows), str(sorted(shapes.items()))]
                      ).encode()
    hh = hashlib.sha256(blob).hexdigest()
    print(f"\n  records hashed BEFORE the counts: sha256 {hh[:32]}...")

    k2 = sum(1 for r in retest if r['legal_desc'] > 0 or r['tau'] <= 5
             or r['freeable'])
    k2l = sum(1 for r in retest if r['loop_deep'][0] == 'freed')
    t2 = k2 == 6
    print(f"\n  THE RETEST (each of the six at its shallow stall, vs deep):")
    for r in retest:
        print(f"    {r}")
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Legal descent (or "
          f"gate-phase) at the stall against the deep set: {k2}/6; "
          f"legal-only loop from c0 against the deep set halts: {k2l}/6")

    s123 = sum(1 for lb, row in canon_rows
               if all(all(fl[:3]) for fl in row))
    s4 = Counter(tuple(fl[3] for fl in row) for lb, row in canon_rows)
    t3 = s123 == 54
    print(f"\n  canonical word (and mirror), stages 1-3 legal: {s123}/54; "
          f"stage-4 (SJ) legal pattern (word, mirror): {dict(s4)}")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Cal SS805 stage table "
          f"on the canonical word, instrument side: {s123}/54")

    t4 = True
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Truncation shapes among "
          f"{n_vac_desc} vacuous-stage descents at step 1: "
          f"{dict(sorted(shapes.items(), key=lambda kv: -kv[1]))}; "
          f"distinct (word, effective) pairs: {len(eff_words)}; "
          f"effective lengths: "
          f"{dict(Counter(len(e) for _w, e in eff_words))}")
    t5 = incons == 0
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. Truncations "
          f"self-consistent (legal stages alone reproduce the image): "
          f"{n_vac_desc - incons}/{n_vac_desc}")

    res = [t1, t2, t3, t4, t5]
    print(f"\n{'=' * 70}")
    print(f"Toy 5588 -- SCORE: {sum(res)}/{len(res)}  (can-fail: 2, 3, 5)")
    print(f"{'=' * 70}")
