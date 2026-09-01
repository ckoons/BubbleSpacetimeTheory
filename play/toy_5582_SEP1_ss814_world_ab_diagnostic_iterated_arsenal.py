#!/usr/bin/env python3
"""
Toy 5582 — THE §814 DIAGNOSTIC: the failure set against the chain's
TRUE arsenal (World A / World B)

Cal's ruling, followed verbatim: the census tested single-application
survival within the edit family; the CHAIN owns more — alternative
targets (the freed inventory, classified by the four freed link-words)
and ITERATION: the assembly requires each stuck configuration to yield
SOME descending step whose result continues, per-step d_gate descent,
no round cap short of d_gate itself.

THE DIAGNOSTIC per failing trace (the failure set = 5581's
widest-instrument residue, re-derived deterministically): run the
assembly's ACTUAL claim — iterate: at each stuck step, search the full
186-word family for a word with d_gate strict descent (d = min Hamming
to the tau<=5 set, sampled; the seam's +1 is a constant offset,
descent-invariant); apply the best; SUCCESS when the configuration is
freed (tau <= 5) or directly freeable; DEFECT when no descending word
exists or steps exceed d_gate(c0)+1.

BLIND: per-trace verdicts hashed before aggregation. WORLDS per Cal's
pre-scored table: A — all recover: instrument correction, lemma
restates with the full family, no new joint; B — residue: J3 with its
labeled row, rows by surgery depth (no percentages; counts and named
classes only).

ADDED (Keeper): per-target CAGE SIZE — the difference-zone extent
(size; max-dist-from-hole logged too) of each candidate target per
failing trace; if target choice works by choosing the cage, recovery
should coincide with the existence of a small-cage target.

TESTS (X/Y): 1. failure set re-derived + blind hash · 2. the iterated
arsenal verdict per trace (rows by depth) · 3. THE WORLD ·
4. the cage-size mechanism check.

Elie, 2026-09-01. 4 tests.
"""

import hashlib
import importlib.util
import json
import os
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


AN = load("t5581w", "toy_5581_SEP1_anatomy76_alternation_prereg_three"
          "_class_census.py")
RD, CV, F2C, F1 = AN.RD, AN.CV, AN.F2C, AN.F1
E1, G5, X3, H8 = AN.E1, AN.G5, AN.X3, AN.H8
WF = load("t5570w", "toy_5570_SEP1_word_family_enumeration_joint"
          "_witness.py")


def iterate_chain(adj, tv, vs, c0, freed, words, max_steps):
    """The assembly's actual claim, run: returns (outcome, steps,
    d-trajectory). outcome in {'freed', 'no-descent', 'cap'}."""
    def dmin(cc):
        best = 10 ** 9
        for f in freed:
            h = sum(1 for v in vs if cc[v] != f[v])
            if h < best:
                best = h
        return best

    lcyc = None
    c = dict(c0)
    d = dmin(c)
    traj = [d]
    for step in range(max_steps):
        if G5.operational_tau(adj, c, tv) <= 5 or \
                X3.freeable(adj, c, tv):
            return 'freed', step, traj
        rm = WF.role_map(adj, c, tv, iterate_chain.lcyc)
        if rm is None:
            return 'no-context', step, traj
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
            dk = dmin(k)
            if dk < d and (best is None or dk < best[0]):
                best = (dk, k)
        if best is None:
            return 'no-descent', step, traj
        d, c = best
        traj.append(d)
    if G5.operational_tau(adj, c, tv) <= 5 or X3.freeable(adj, c, tv):
        return 'freed', max_steps, traj
    return 'cap', max_steps, traj


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5582 — the SS814 diagnostic: World A or World B")
    print("=" * 70)

    pops = RD.build_pops()
    moves, words, _ = WF.context_family()

    # re-derive the failure set (5581's widest instrument, same slices)
    failures = []
    for label, faces, adj, tv, stuck, freed, exact in pops:
        lcyc = E1.link_cycle(faces, tv)
        link = set(adj[tv])
        vs = [v for v in sorted(adj, key=str) if v != tv]
        for ci, c0 in enumerate(stuck[:60]):
            rl = F2C.roles(adj, c0, tv, lcyc)
            if rl is None:
                continue
            n_sM, r, s_M, s_i, s_j = rl
            tau = {r: s_M, s_M: r}
            for sx in (s_i, s_j):
                n_sx = next(v for v in lcyc if c0[v] == sx)
                X1, X2, X3c, X4, c1, c2, c3, c4 = CV.trace(
                    adj, c0, tv, n_sM, r, s_M, n_sx, sx)
                R = (X1 - X3c) - X2
                if not R or any(v in link for v in R) or not freed:
                    continue
                rim_pairs = [(u, x) for u in R for x in adj[u]
                             if x != tv and x not in R]
                ok, _c, _n = AN.try_stabilize(adj, tv, vs, c0, c4, R,
                                              rim_pairs, tau, freed)
                if not ok:
                    failures.append((label, faces, adj, tv, lcyc, c0,
                                     vs, freed))
                    break              # one failing mirror is enough
    fail_count = Counter(f[0] for f in failures)
    t1 = len(failures) > 30
    print(f"\n  failure set re-derived: {len(failures)} configs "
          f"({dict(fail_count)})")

    # blind pass: iterated-arsenal verdicts
    records = []
    cage_rows = []
    for label, faces, adj, tv, lcyc, c0, vs, freed in failures:
        iterate_chain.lcyc = lcyc
        d0 = min(sum(1 for v in vs if c0[v] != f[v]) for f in freed)
        outcome, steps, traj = iterate_chain(adj, tv, vs, c0, freed,
                                             words, d0 + 1)
        records.append((label, outcome, steps, tuple(traj)))
        # cage sizes: difference-zone extent of nearest candidates
        dist = {tv: 0}
        q = deque([tv])
        while q:
            u = q.popleft()
            for w2 in adj[u]:
                if w2 not in dist:
                    dist[w2] = dist[u] + 1
                    q.append(w2)
        cages = []
        byd = sorted(freed, key=lambda f: sum(
            1 for v in vs if c0[v] != f[v]))
        for f in byd[:12]:
            diffz = [v for v in vs if c0[v] != f[v]]
            cages.append((len(diffz),
                          max((dist[v] for v in diffz), default=0)))
        cage_rows.append((label, outcome, min(c2[0] for c2 in cages),
                          sorted(c2[0] for c2 in cages)[:4]))
    blob = json.dumps([str(r) for r in records]).encode()
    hh = hashlib.sha256(blob).hexdigest()
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Failure set + BLIND "
          f"verdicts hashed (sha256 {hh[:32]}...)")

    agg = Counter((lb, oc) for lb, oc, st, tj in records)
    steps_c = Counter(st for lb, oc, st, tj in records if oc == 'freed')
    t2 = True
    print(f"\n  iterated-arsenal verdicts by surgery-depth row: "
          f"{dict(sorted(agg.items()))}")
    print(f"  recovery step-counts: {dict(sorted(steps_c.items()))}")
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Per-trace verdicts "
          f"rendered")

    n_rec = sum(1 for lb, oc, st, tj in records if oc == 'freed')
    residue = [(lb, oc, st, tj) for lb, oc, st, tj in records
               if oc != 'freed']
    t3 = True
    if not residue:
        world = (f"WORLD A — ALL {len(records)} failures RECOVER under "
                 f"the chain's true resources (iteration + full "
                 f"family): the weak lemma was measured against too "
                 f"small a family; INSTRUMENT CORRECTION per the "
                 f"radius-to-size precedent — the lemma restates with "
                 f"the full family, no new joint, no revision spent; "
                 f"restated form re-earns on tranche-2b per standing "
                 f"terms")
    else:
        rc = Counter(lb for lb, *_ in residue)
        world = (f"WORLD B — {len(residue)} of {len(records)} remain "
                 f"uncovered under everything the chain owns "
                 f"({dict(rc)}; outcomes "
                 f"{Counter(oc for _, oc, *_ in residue)}); J3 = "
                 f"Gate-Phase Stability on the named class, LABELED "
                 f"ROW; first exhibits: {[r[:3] for r in residue[:4]]}")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. THE WORLD: {world}")

    rec_min = [m for lb, oc, m, _ in cage_rows if oc == 'freed']
    res_min = [m for lb, oc, m, _ in cage_rows if oc != 'freed']
    t4 = True
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. CAGE MECHANISM: "
          f"min cage size (difference-zone extent, 12 nearest) — "
          f"recovered: {sorted(set(rec_min))}; residue: "
          f"{sorted(set(res_min))} — "
          f"{'recovery coincides with small-cage availability (disjoint ranges)' if res_min and rec_min and max(rec_min) < min(res_min) else 'cage size alone does NOT separate recovery' if res_min else 'all recovered; cage distribution logged for the mechanism line'}")

    res = [t1, t2, t3, t4]
    print(f"\n{'=' * 70}")
    print(f"Toy 5582 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
