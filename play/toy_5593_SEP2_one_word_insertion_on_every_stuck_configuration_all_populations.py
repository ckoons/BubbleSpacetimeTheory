#!/usr/bin/env python3
"""
Toy 5593 — THE ONE-WORD INSERTION CLAIM on EVERY stuck configuration
of every population (not the 54 failure set): Fritsch EXHAUSTIVE, T3,
B-errera, D-flip2, D-flip3 — whole harvests

5591's measured sentence: at every stuck configuration in the canonical
context, some FULLY-LEGAL family word's image has a color absent at v
(directly insertable) or is one swap from it. Stated without any
metric — target-innocent in its statement (its truth for ALL T is 4CT,
by Lyra's Lemma; that is what makes it the honest target). It was
measured on the 54 (a stability-failure subset) and the 1,801. The
scope it is stated at is ALL stuck configurations. This toy runs the
whole stuck sets of build_pops: Fritsch exhaustive (the classical
Kempe-killer, every tau=6 coloring at its degree-5 vertex), T3,
B-errera, D-flip2, D-flip3 (harvests, up to 250 each) — the first
place a counterexample to the one-word claim could live is Fritsch.

Also: the HITTING-WORD SHAPE histogram (which roles, which pairs) —
the mechanism for Lyra/Cal (hand-check: B1/B2 words in the (r,s_i)/
(r,s_j) pairs — Kempe's degree-5 double swap as a commutator).

Two exit readings reported separately: DIRECT (a color absent at v in
w.c) and ONE-SWAP (tau(w.c) <= 5, i.e. freeable by one swap).

BLIND: per-config records hashed BEFORE the counts. k/N only.

TESTS (X/Y): 1. Fritsch exhaustive stuck set, k/N (can fail) ·
2. each harvested population, k/N (can fail) · 3. DIRECT-exit
existence k/N (can fail) · 4. hitting-word shape histogram ·
5. non-canonical-context configurations counted (role_map None).

Elie, 2026-09-02. 5 tests.
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


GA = load("t5591ow", "toy_5591_SEP2_gate_aware_potential_legal_only_DGT"
          "_recount_54_and_1801.py")
LG, TE = GA.LG, GA.TE
RD = LG.RD
E1, G5, X3, WF, F1 = GA.E1, GA.G5, GA.X3, GA.WF, GA.F1


def direct(adj, k, tv):
    return len({k[u] for u in adj[tv]}) < 4


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5593 — one-word insertion on every stuck configuration")
    print("=" * 70)
    moves, words, _ = WF.context_family()
    pops = RD.build_pops()
    records = []
    shapes = Counter()
    for label, faces, adj, tv, stuck, freed, exact in pops:
        lcyc = E1.link_cycle(faces, tv)
        vs = [v for v in sorted(adj, key=str) if v != tv]
        for i, c0 in enumerate(stuck):
            if G5.operational_tau(adj, c0, tv) != 6 or X3.freeable(adj, c0, tv):
                records.append((label, i, 'not-stuck', 0, 0, 0, 0))
                continue
            imgs = LG.word_images_legal(adj, c0, tv, lcyc, words)
            if imgs is None:
                records.append((label, i, 'no-context', 0, 0, 0, 0))
                continue
            legal = [(w, k) for w, k, fl in imgs if all(fl)]
            n_dir = 0
            n_gate = 0
            for w, k in legal:
                if direct(adj, k, tv):
                    n_dir += 1
                    n_gate += 1
                    shapes[(w[0][0], w[0][1], w[1][0], w[1][1])] += 1
                elif GA.gate(adj, k, tv):
                    n_gate += 1
            records.append((label, i, 'stuck', len(legal), n_dir, n_gate,
                            len(imgs)))
    hh = hashlib.sha256(json.dumps([str(r) for r in records]).encode()
                        ).hexdigest()
    print(f"\n  {len(records)} configurations; records hashed BEFORE the "
          f"counts: sha256 {hh[:32]}...")
    stuck_recs = [r for r in records if r[2] == 'stuck']
    by = {}
    for r in stuck_recs:
        by.setdefault(r[0], [0, 0, 0])
        by[r[0]][0] += 1
        by[r[0]][1] += r[5] > 0
        by[r[0]][2] += r[4] > 0
    print(f"\n  per population (stuck n, one-word GATE exists, one-word "
          f"DIRECT exists):")
    for k in by:
        print(f"    {k}: {by[k]}")
    fr = by.get('Fritsch', [0, 0, 0])
    t1 = fr[0] > 0 and fr[1] == fr[0]
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. FRITSCH EXHAUSTIVE: "
          f"{fr[1]}/{fr[0]} stuck colorings have a fully-legal family "
          f"word into the gate phase")
    others = {k: v for k, v in by.items() if k != 'Fritsch'}
    t2 = all(v[1] == v[0] for v in others.values())
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Harvested populations: "
          f"{ {k: f'{v[1]}/{v[0]}' for k, v in others.items()} }")
    tot = len(stuck_recs)
    kd = sum(1 for r in stuck_recs if r[4] > 0)
    kg = sum(1 for r in stuck_recs if r[5] > 0)
    t3 = kd == tot
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. DIRECT exit (a color absent "
          f"at v after ONE word): {kd}/{tot}; GATE exit (direct or one "
          f"swap): {kg}/{tot}")
    miss = [r for r in stuck_recs if r[5] == 0]
    for r in miss[:10]:
        print(f"    no one-word exit: {r}")
    t4 = True
    top = shapes.most_common(12)
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Hitting-word shapes "
          f"(role, pair, role, pair) among DIRECT hits, top 12 of "
          f"{len(shapes)}:")
    for s, c in top:
        print(f"    {c:6d}  {s}")
    role_pairs = Counter((s[0], s[2]) for s, c in shapes.items() for _ in range(c))
    print(f"  role-pair histogram: {dict(role_pairs.most_common())}")
    nc = Counter(r[2] for r in records)
    t5 = True
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. Status counts: {dict(nc)} "
          f"(no-context = stuck but role_map None; not-stuck = harvest "
          f"entry failing the stuck predicate)")
    res = [t1, t2, t3, t4, t5]
    print(f"\n{'=' * 70}")
    print(f"Toy 5593 -- SCORE: {sum(res)}/{len(res)}  (can-fail: 1, 2, 3)")
    print(f"{'=' * 70}")
