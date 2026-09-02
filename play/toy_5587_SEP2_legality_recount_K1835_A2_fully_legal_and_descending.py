#!/usr/bin/env python3
"""
Toy 5587 — THE LEGALITY RE-COUNT (K1835 Finding A2): fully-legal AND
strictly-descending family words, the SAME word — on the 54 and at
the J3 stall (5583's 29)

Keeper A2, verbatim in substance: "A family word whose stage 4 is
illegal is not a move; it cannot be applied. So the word the Assembly
applies must be fully legal AND strictly descending — the same w.
Elie's escort then counts legal-and-descending words per
configuration, not descending words; if the 5583 figure (29
descending words at the former stall) was counted before legality,
it is re-counted after."

THE INSTRUMENT FACT THAT MAKES THIS NECESSARY: X3.apply_move returns
the coloring UNCHANGED when the seed vertex does not carry a color of
the move's pair — an illegal stage is silently a NO-OP. So every
descending-word count to date (5570-5586) admitted words with a
vacuous stage; those are 3-swap (or shorter) words, NOT family words
as defined. This toy tags every stage's legality and re-counts.

POSITIVE CONTROL OF CAL'S STAGE TABLE (SS805): stages 1-3 are DERIVED
legal in the canonical context; stage 4 is the sub-joint SJ. The
instrument can check that: if any stage 1-3 is ever vacuous on a
canonical-context configuration, either the instrument's role map is
not the theorem's or the stage table is wrong — reported either way.

PART A (the 54): at each configuration, the descending words at step
1 split legal / vacuous; then the iterate loop RESTRICTED to fully
legal words (best legal descent per step; halt at freed/freeable; cap
d_gate+1). PART B (the J3 stall, 5583's deep freed set regenerated
bit-identically, seeds unchanged): the 29 re-counted after legality.

BLIND: per-config records hashed BEFORE the counts. k/N only.

TESTS (X/Y): 1. stage 1-3 legality (positive control of the stage
table; can fail) · 2. legal-and-descending exists at step 1, k/54
(can fail) · 3. legality-restricted iterate loop halts, k/54 (can
fail) · 4. J3 stall re-count: legal among the 29 (can fail) · 5. the
vacuous-stage words characterized (which stage; count).

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


W = load("t5582lg", "toy_5582_SEP1_ss814_world_ab_diagnostic_iterated"
         "_arsenal.py")
TE = load("t5585lg", "toy_5585_SEP2_target_existence_menu_sweep_third"
          "_door_prebuilt.py")
RD, E1, G5, X3, WF, F1 = W.RD, W.E1, W.G5, W.X3, W.WF, W.F1


def legal_commutator(adj, col, m1, m2, tv):
    """X3.commutator with a legality flag per stage: a stage is legal
    iff its seed carries a color of its pair at that stage."""
    flags = []
    c = col
    for m in (m1, m2, m1, m2):
        pair, seed = m
        flags.append(c.get(seed) in pair)
        c = X3.apply_move(adj, c, m, tv)
    return c, tuple(flags)


def word_images_legal(adj, c, tv, lcyc, words):
    rm = WF.role_map(adj, c, tv, lcyc)
    if rm is None:
        return None
    vmap, cmap = rm
    out = []
    for w in words:
        m1 = (tuple(sorted((cmap[w[0][1][0]], cmap[w[0][1][1]]))),
              vmap[w[0][0]])
        m2 = (tuple(sorted((cmap[w[1][1][0]], cmap[w[1][1][1]]))),
              vmap[w[1][0]])
        k, flags = legal_commutator(adj, c, m1, m2, tv)
        if not X3.support(c, k):
            continue
        if not G5.is_proper(adj, k, skip=tv):
            continue
        out.append((w, k, flags))
    return out


def dmin(cc, freed, vs):
    return min(TE.ham(cc, f, vs) for f in freed)


def legal_iterate(adj, tv, vs, lcyc, c0, freed, words, cap):
    c = dict(c0)
    d = dmin(c, freed, vs)
    traj = [d]
    for step in range(cap):
        if G5.operational_tau(adj, c, tv) <= 5 or X3.freeable(adj, c, tv):
            return 'freed', step, traj
        imgs = word_images_legal(adj, c, tv, lcyc, words)
        if imgs is None:
            return 'no-context', step, traj
        best = None
        for w, k, fl in imgs:
            if not all(fl):
                continue
            dk = dmin(k, freed, vs)
            if dk < d and (best is None or dk < best[0]):
                best = (dk, k)
        if best is None:
            return 'no-legal-descent', step, traj
        d, c = best
        traj.append(d)
    if G5.operational_tau(adj, c, tv) <= 5 or X3.freeable(adj, c, tv):
        return 'freed', cap, traj
    return 'cap', cap, traj


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5587 — the legality re-count (K1835 A2)")
    print("=" * 70)

    moves, words, _ = WF.context_family()
    fails = TE.failure_set()
    n = len(fails)

    records = []
    stage_vac = Counter()      # which stages vacuous, over all images
    for label, faces, adj, tv, lcyc, c0, vs, freed in fails:
        imgs = word_images_legal(adj, c0, tv, lcyc, words)
        d0 = dmin(c0, freed, vs)
        n_img = len(imgs)
        n_full = sum(1 for _w, _k, fl in imgs if all(fl))
        desc_legal = 0
        desc_vac = 0
        vac_stage_here = Counter()
        s123_bad = 0
        for w, k, fl in imgs:
            for i, f in enumerate(fl):
                if not f:
                    stage_vac[i + 1] += 1
                    vac_stage_here[i + 1] += 1
            if not all(fl[:3]):
                s123_bad += 1
            if dmin(k, freed, vs) < d0:
                if all(fl):
                    desc_legal += 1
                else:
                    desc_vac += 1
        oc, st, tj = legal_iterate(adj, tv, vs, lcyc, c0, freed, words,
                                   d0 + 1)
        records.append({'label': label, 'd0': d0, 'imgs': n_img,
                        'full_legal': n_full, 'desc_legal': desc_legal,
                        'desc_vac': desc_vac, 's123_bad': s123_bad,
                        'vac': dict(vac_stage_here),
                        'loop': (oc, st, tuple(tj))})

    # PART B — the J3 stall, 5583's construction replayed (same seeds)
    ex = json.load(open(os.path.join(HERE, '.j3_exhibit.json')))
    rr = F1.F3T.family_B_right(3, 0)
    faces = rr[0]
    adj = G5.adj_from_faces(faces)
    tv = next(v for v in adj if str(v) == ex['tv'])
    smap = {str(v): v for v in adj}
    c0 = {smap[k]: v for k, v in ex['coloring'].items()}
    lcyc = E1.link_cycle(faces, tv)
    vs = [v for v in sorted(adj, key=str) if v != tv]
    seen = set()
    freed = []

    def add(c):
        key = tuple(c[v] for v in vs)
        if key not in seen:
            seen.add(key)
            if G5.operational_tau(adj, c, tv) <= 5:
                freed.append(dict(c))

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
    _, _, _, _, stuck0, freed0, _ex = next(
        p for p in RD.build_pops() if p[0] == 'D-flip3')
    d0 = dmin(c0, freed0, vs)
    # walk to the stall with the original freed set (5583's greedy)
    c = dict(c0)
    d = dmin(c, freed0, vs)
    stall = None
    for step in range(d0 + 1):
        if G5.operational_tau(adj, c, tv) <= 5 or X3.freeable(adj, c, tv):
            break
        imgs = TE.word_images(adj, c, tv, lcyc, words)
        best = None
        for w, k in imgs:
            dk = dmin(k, freed0, vs)
            if dk < d and (best is None or dk < best[0]):
                best = (dk, k)
        if best is None:
            stall = dict(c)
            break
        d, c = best
    if stall is not None:
        for s in range(400):
            cur = dict(stall)
            for step in range(10):
                rng = random.Random(77000 + s * 131 + step)
                u = rng.choice(vs)
                a = cur[u]
                b = rng.choice([x for x in range(4) if x != a])
                comp = G5.kempe_chain(adj, cur, u, a, b, exclude={tv})
                cur = G5.do_swap(cur, comp, a, b)
                add(cur)
    j3 = {'stall': stall is not None, 'deep': len(freed)}
    if stall is not None:
        ds = dmin(stall, freed, vs)
        imgs = word_images_legal(adj, stall, tv, lcyc, words)
        dl = [(w, fl) for w, k, fl in imgs if dmin(k, freed, vs) < ds]
        j3['d_stall'] = ds
        j3['desc_total'] = len(dl)
        j3['desc_legal'] = sum(1 for _w, fl in dl if all(fl))
        j3['desc_vac_stage'] = dict(Counter(
            i + 1 for _w, fl in dl for i, f in enumerate(fl) if not f))

    blob = json.dumps([str(sorted(r.items())) for r in records]
                      + [str(sorted(j3.items()))]).encode()
    hh = hashlib.sha256(blob).hexdigest()
    print(f"\n  failure set: {n}; per-config records + J3 record hashed "
          f"BEFORE the counts: sha256 {hh[:32]}...")

    # 1. stage 1-3 positive control
    bad123 = sum(r['s123_bad'] for r in records)
    tot_img = sum(r['imgs'] for r in records)
    t1 = bad123 == 0
    print(f"\n  vacuous stages over all supported+proper images on the "
          f"54: {dict(sorted(stage_vac.items()))} (of {tot_img} images)")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Stages 1-3 never "
          f"vacuous (Cal SS805 stage table, instrument side): "
          f"{tot_img - bad123}/{tot_img} images")

    # 2. legal-and-descending at step 1
    k2 = sum(1 for r in records if r['desc_legal'] > 0)
    only_vac = [(r['label'], r['d0'], r['desc_vac']) for r in records
                if r['desc_legal'] == 0 and r['desc_vac'] > 0]
    none_at_all = sum(1 for r in records
                      if r['desc_legal'] == 0 and r['desc_vac'] == 0)
    t2 = k2 == n
    print(f"\n  legal-and-descending words at step 1, by config: "
          f"{sorted(r['desc_legal'] for r in records)}")
    print(f"  descending-but-vacuous words at step 1, by config: "
          f"{sorted(r['desc_vac'] for r in records)}")
    print(f"  configs with ONLY vacuous descents: {len(only_vac)} "
          f"{only_vac[:8]}; with none: {none_at_all}")
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. A fully-legal AND "
          f"strictly-descending word exists at step 1: {k2}/{n}")

    # 3. legality-restricted loop
    lo = Counter(r['loop'][0] for r in records)
    k3 = lo.get('freed', 0)
    steps = Counter(r['loop'][1] for r in records if r['loop'][0] == 'freed')
    t3 = k3 == n
    print(f"\n  legality-restricted iterate outcomes: {dict(lo)}; "
          f"step-counts: {dict(sorted(steps.items()))}")
    res3 = [(r['label'], r['d0'], r['loop']) for r in records
            if r['loop'][0] != 'freed']
    for r in res3[:6]:
        print(f"    residue: {r}")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Legal-only descent "
          f"loop halts within d_gate+1: {k3}/{n} (shallow-sample "
          f"caveat carries, 5583/5585 precedent)")

    # 4. J3 re-count
    t4 = j3.get('stall') and j3.get('desc_legal', 0) > 0
    print(f"\n  J3 stall replayed: {j3}")
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. J3's descending words "
          f"re-counted AFTER legality: "
          f"{j3.get('desc_legal', 0)}/{j3.get('desc_total', 0)} legal")

    # 5. characterization
    t5 = True
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. Vacuous-stage "
          f"characterization: stage histogram {dict(sorted(stage_vac.items()))}; "
          f"fully-legal images per config (of supported+proper): "
          f"{sorted((r['full_legal'], r['imgs']) for r in records)[:12]}...")

    res = [t1, t2, t3, t4, t5]
    print(f"\n{'=' * 70}")
    print(f"Toy 5587 -- SCORE: {sum(res)}/{len(res)}  (can-fail: 1, 2, 3, 4)")
    print(f"{'=' * 70}")
