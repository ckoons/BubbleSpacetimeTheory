#!/usr/bin/env python3
"""
Toy 5591 — THE CORRECTED FLOOR: gate-aware potential, legal-only DGT
re-count on the 54 and the 1,801 (shallow samples, blind)

5590 found the instrument's blind spot: the loop valued a sampled
distance, so an image that is ITSELF in the gate phase (tau <= 5 or
directly freeable) but absent from the sample read as d-hat = 10 and
was never taken. d_gate(k) := 0 for k in T is the definition, not a
new rule. Corrected loop: among fully-legal, supported, proper images,
take any gate-phase image at once (halt); otherwise strict descent of
d-hat = min Hamming to the shallow sample; cap d-hat(c0)+1.

False-negative direction only: this can only RAISE 5587's 48/54 and
5586/5589's counts. Whatever remains is the honest shallow-sample floor
under K1835 A2's legality clause.

TESTS (X/Y): 1. the 54, corrected legal-only (can fail) · 2. the
1,801, corrected legal-only (can fail) · 3. residue exhibited by hole
with d-hat at the stall · 4. gate-hit accounting (how many halts came
from the correction itself).

Elie, 2026-09-02. 4 tests.
"""

import hashlib
import importlib.util
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


D6 = load("t5586ga", "toy_5586_SEP2_DGT_descent_given_target_on_the_1801"
          "_tranche_census.py")
LG = load("t5587ga", "toy_5587_SEP2_legality_recount_K1835_A2_fully"
          "_legal_and_descending.py")
W, TE, T2 = D6.W, D6.TE, D6.T2
E1, G5, X3, WF, F1 = D6.E1, D6.G5, D6.X3, D6.WF, D6.F1


def gate(adj, c, tv):
    return G5.operational_tau(adj, c, tv) <= 5 or X3.freeable(adj, c, tv)


def corrected_legal_iterate(adj, tv, vs, lcyc, c0, freed, words, cap):
    c = dict(c0)
    d = LG.dmin(c, freed, vs)
    traj = [d]
    for step in range(cap):
        if gate(adj, c, tv):
            return 'freed', step, traj, False
        imgs = LG.word_images_legal(adj, c, tv, lcyc, words)
        if imgs is None:
            return 'no-context', step, traj, False
        best = None
        for w, k, fl in imgs:
            if not all(fl):
                continue
            if gate(adj, k, tv):
                traj.append(0)
                return 'freed', step + 1, traj, True
            dk = LG.dmin(k, freed, vs)
            if dk < d and (best is None or dk < best[0]):
                best = (dk, k)
        if best is None:
            return 'no-legal-descent', step, traj, False
        d, c = best
        traj.append(d)
    if gate(adj, c, tv):
        return 'freed', cap, traj, False
    return 'cap', cap, traj, False


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5591 — gate-aware potential: the corrected legal-only floor")
    print("=" * 70)
    moves, words, _ = WF.context_family()

    # the 54
    fails = TE.failure_set()
    rec54 = []
    for label, faces, adj, tv, lcyc, c0, vs, freed in fails:
        d0 = LG.dmin(c0, freed, vs)
        oc, st, tj, byg = corrected_legal_iterate(adj, tv, vs, lcyc, c0,
                                                  freed, words, d0 + 1)
        rec54.append((label, d0, oc, st, tuple(tj), byg))
    h54 = hashlib.sha256(json.dumps([str(r) for r in rec54]).encode()
                         ).hexdigest()
    print(f"\n  the 54: verdicts hashed BEFORE the count: sha256 {h54[:32]}...")
    k1 = sum(1 for r in rec54 if r[2] == 'freed')
    g1 = sum(1 for r in rec54 if r[5])
    t1 = k1 == 54
    print(f"  outcomes: {dict(Counter(r[2] for r in rec54))}; halts via a "
          f"gate-phase image: {g1}; step-counts: "
          f"{dict(sorted(Counter(r[3] for r in rec54 if r[2] == 'freed').items()))}")
    res54 = [r for r in rec54 if r[2] != 'freed']
    for r in res54:
        print(f"    residue: {r}")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. The 54, legal-only, "
          f"gate-aware: {k1}/54 (5587 floor was 48/54)")

    # the 1,801
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
    recs = []
    for fn, st in stores:
        tr = '2a' if 'tranche2_' in fn else '2b'
        for label, blk in st.items():
            faces, adj, tv = fams[label]
            lcyc = E1.link_cycle(faces, tv)
            smap = {str(v): v for v in adj}
            vs = [v for v in sorted(adj, key=str) if v != tv]
            freed = freed_by[label]
            for i, crec in enumerate(blk['stuck']):
                c0 = {smap[k]: v for k, v in crec.items()}
                d0 = LG.dmin(c0, freed, vs)
                oc, stp, tj, byg = corrected_legal_iterate(
                    adj, tv, vs, lcyc, c0, freed, words, d0 + 1)
                recs.append((tr, label, i, d0, oc, stp, tuple(tj), byg))
    hh = hashlib.sha256(json.dumps([str(r) for r in recs]).encode()
                        ).hexdigest()
    print(f"\n  the 1,801: verdicts hashed BEFORE the count: sha256 "
          f"{hh[:32]}...")
    n = len(recs)
    k2 = sum(1 for r in recs if r[4] == 'freed')
    g2 = sum(1 for r in recs if r[7])
    byhole = {}
    for r in recs:
        byhole.setdefault((r[0], r[1]), Counter())[r[4]] += 1
    t2 = k2 == n
    for k in sorted(byhole):
        print(f"    {k[0]} {k[1]}: {dict(byhole[k])}")
    print(f"  step-counts: "
          f"{dict(sorted(Counter(r[5] for r in recs if r[4] == 'freed').items()))}; "
          f"halts via a gate-phase image: {g2}")
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. The 1,801, legal-only, "
          f"gate-aware: {k2}/{n}")

    residue = [r for r in recs if r[4] != 'freed']
    t3 = True
    print(f"\n  residue {len(residue)}: d-hat at stall distribution "
          f"{dict(sorted(Counter(r[6][-1] for r in residue).items()))}")
    for r in residue[:30]:
        print(f"    {r[:7]}")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Residue exhibited by hole")
    t4 = True
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Gate-hit accounting: "
          f"{g1}/54 and {g2}/{n} halts came through an unsampled "
          f"gate-phase image (the 5590 correction)")

    res = [t1, t2, t3, t4]
    print(f"\n{'=' * 70}")
    print(f"Toy 5591 -- SCORE: {sum(res)}/{len(res)}  (can-fail: 1, 2)")
    print(f"{'=' * 70}")
