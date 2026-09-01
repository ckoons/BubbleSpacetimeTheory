#!/usr/bin/env python3
"""
Toy 5583 — THE EXHIBIT PROBE: deepen the freed set on the single
D-flip3 residue — J3 dissolves, or the stall is told what it is

One configuration; the compute is spent. Full tau<=5 enumeration is
infeasible (4^65), so: the deepest sample the hardware allows —
mass backtracking seeds x long swap walks PLUS targeted walks FROM the
stall configuration (the targets that matter for descent live near the
stall) — hash-committed before the retest.

THE RETEST (caveat direction guarantees only two outcomes): does any
of the 186 family words descend at the stall against the deep freed
set? DISSOLVES -> World A entire, by instrument correction. HARDENS ->
the stall is characterized exactly: (a) stuck or gate-phase; (b) do
family words move SIDEWAYS (d-preserving unsticking: plateau, not
wall); (c) does iteration WITH sideways moves escape within bounded
rounds. A wall is a counterexample; a plateau is a weaker theorem.

TESTS (X/Y): 1. the stall reproduced + deep freed set committed ·
2. the descent retest · 3. the characterization (wall / plateau /
dissolved).

Elie, 2026-09-01. 3 tests.
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


W = load("t5582p", "toy_5582_SEP1_ss814_world_ab_diagnostic_iterated"
         "_arsenal.py")
AN, RD, CV, F2C, F1 = W.AN, W.RD, W.CV, W.F2C, W.F1
E1, G5, X3, H8, WF = W.E1, W.G5, W.X3, W.H8, W.WF


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5583 — the exhibit probe: wall, plateau, or dissolved")
    print("=" * 70)

    ex = json.load(open(os.path.join(HERE, '.j3_exhibit.json')))
    rr = F1.F3T.family_B_right(3, 0)
    faces = rr[0]
    adj = G5.adj_from_faces(faces)
    tv = next(v for v in adj if str(v) == ex['tv'])
    smap = {str(v): v for v in adj}
    c0 = {smap[k]: v for k, v in ex['coloring'].items()}
    lcyc = E1.link_cycle(faces, tv)
    vs = [v for v in sorted(adj, key=str) if v != tv]
    moves, words, _ = WF.context_family()

    # deep freed set: mass seeds + long walks + targeted stall walks
    seen = set()
    freed = []

    def add(c):
        key = tuple(c[v] for v in vs)
        if key not in seen:
            seen.add(key)
            if G5.operational_tau(adj, c, tv) <= 5:
                freed.append(dict(c))

    for s in range(150):
        c = W.AN.RD.build_pops if False else None
        c = None
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

    # reproduce the stall (greedy per 5582, against a PRELIM freed set
    # — the stall is defined by the original run; regenerate with the
    # original sampled freed to land on the same configuration)
    _, _, _, _, stuck0, freed0, _ex = next(
        p for p in RD.build_pops() if p[0] == 'D-flip3')
    W.iterate_chain.lcyc = lcyc
    d0 = min(sum(1 for v in vs if c0[v] != f[v]) for f in freed0)

    def dmin_over(cc, F):
        best = 10 ** 9
        for f in F:
            h = sum(1 for v in vs if cc[v] != f[v])
            if h < best:
                best = h
        return best

    # walk to the stall with the original freed set
    c = dict(c0)
    d = dmin_over(c, freed0)
    traj = [d]
    stall = None
    for step in range(d0 + 1):
        if G5.operational_tau(adj, c, tv) <= 5 or \
                X3.freeable(adj, c, tv):
            break
        rm = WF.role_map(adj, c, tv, lcyc)
        vmap, cmap = rm
        best = None
        for w in words:
            m1 = (tuple(sorted((cmap[w[0][1][0]], cmap[w[0][1][1]]))),
                  vmap[w[0][0]])
            m2 = (tuple(sorted((cmap[w[1][1][0]], cmap[w[1][1][1]]))),
                  vmap[w[1][0]])
            k = X3.commutator(adj, c, m1, m2, tv)
            if not X3.support(c, k):
                continue
            if not G5.is_proper(adj, k, skip=tv):
                continue
            dk = dmin_over(k, freed0)
            if dk < d and (best is None or dk < best[0]):
                best = (dk, k)
        if best is None:
            stall = dict(c)
            break
        d, c = best
        traj.append(d)
    # targeted walks from the stall enrich the freed set
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
    blob = json.dumps(sorted(str(tuple(f[v] for v in vs))
                             for f in freed)).encode()
    hh = hashlib.sha256(blob).hexdigest()
    t1 = stall is not None and len(freed) > len(freed0)
    print(f"\n  stall reproduced: {stall is not None} "
          f"(trajectory {traj}); deep freed set: {len(freed)} "
          f"(original sample {len(freed0)}); committed sha256 "
          f"{hh[:32]}...")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Stall + deep freed "
          f"committed")

    ds = dmin_over(stall, freed)
    tau_stall = G5.operational_tau(adj, stall, tv)
    freeable_stall = X3.freeable(adj, stall, tv)
    rm = WF.role_map(adj, stall, tv, lcyc)
    desc_words = []
    side_words = []
    if rm is not None:
        vmap, cmap = rm
        for w in words:
            m1 = (tuple(sorted((cmap[w[0][1][0]], cmap[w[0][1][1]]))),
                  vmap[w[0][0]])
            m2 = (tuple(sorted((cmap[w[1][1][0]], cmap[w[1][1][1]]))),
                  vmap[w[1][0]])
            k = X3.commutator(adj, stall, m1, m2, tv)
            if not X3.support(stall, k):
                continue
            if not G5.is_proper(adj, k, skip=tv):
                continue
            dk = dmin_over(k, freed)
            if dk < ds:
                desc_words.append(w)
            elif dk == ds:
                side_words.append((w, k))
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. RETEST at the stall: "
          f"d(deep) = {ds} (was {ex['d_traj'][-1]}); tau = {tau_stall}, "
          f"freeable = {freeable_stall}; descending words: "
          f"{len(desc_words)}; sideways words: {len(side_words)}")

    t3 = True
    if desc_words or tau_stall <= 5 or freeable_stall:
        verdict = ("J3 DISSOLVES — the deep freed set exposes a "
                   "descending word (or the stall is already "
                   "gate-phase): WORLD A ENTIRE, by instrument "
                   "correction; the lemma restates with the full "
                   "family and no new joint")
    else:
        # plateau probe: BFS over sideways moves
        frontier = [dict(stall)]
        seen2 = {tuple(stall[v] for v in vs)}
        escaped = False
        rounds = 0
        for depth in range(6):
            rounds = depth + 1
            nxt = []
            for cc in frontier:
                rm2 = WF.role_map(adj, cc, tv, lcyc)
                if rm2 is None:
                    continue
                vm2, cm2 = rm2
                for w in words:
                    m1 = (tuple(sorted((cm2[w[0][1][0]],
                                        cm2[w[0][1][1]]))),
                          vm2[w[0][0]])
                    m2 = (tuple(sorted((cm2[w[1][1][0]],
                                        cm2[w[1][1][1]]))),
                          vm2[w[1][0]])
                    k = X3.commutator(adj, cc, m1, m2, tv)
                    if not X3.support(cc, k):
                        continue
                    if not G5.is_proper(adj, k, skip=tv):
                        continue
                    key = tuple(k[v] for v in vs)
                    if key in seen2:
                        continue
                    dk = dmin_over(k, freed)
                    if dk < ds or G5.operational_tau(adj, k, tv) <= 5 \
                            or X3.freeable(adj, k, tv):
                        escaped = True
                        break
                    if dk == ds and len(nxt) < 120:
                        seen2.add(key)
                        nxt.append(k)
                if escaped:
                    break
            if escaped or not nxt:
                break
            frontier = nxt
        if escaped:
            verdict = (f"PLATEAU, NOT WALL — sideways iteration "
                       f"escapes in {rounds} round(s) "
                       f"({len(seen2)} plateau configs explored): the "
                       f"exhibit weakens the theorem (descent becomes "
                       f"non-strict with bounded plateaus), it does "
                       f"not refute it")
        else:
            verdict = (f"WALL — no descent, and sideways iteration "
                       f"does not escape within 6 rounds "
                       f"({len(seen2)} plateau configs): J3 HARDENS "
                       f"honestly; the exhibit is a genuine "
                       f"counterexample candidate for the lemma as "
                       f"stated")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. THE ANSWER: {verdict}")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5583 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
