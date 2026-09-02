#!/usr/bin/env python3
"""
Toy 5592 — THE BASE-RATE AUDIT OF 5591: is the family the mechanism,
or is stuckness one swap deep?

5591: at all 1,855 stuck configurations (54 + 1,801) some fully-legal
family word lands DIRECTLY in the gate phase. Before that is a
theorem's evidence it needs its base rate and its null (no wave-
through on a perfect number). Per configuration:
  - legal family images: how many, how many gate-phase (fraction);
  - all supported+proper images (legal or vacuous): same;
  - NULL A: every single Kempe swap in T-v (seed u != v, pair
    (c[u], b)): fraction gate-phase; exists?
  - NULL B: single Kempe swaps seeded at the five link vertices only
    (Kempe's own move set at v): exists gate-phase?
  - the comparison: configs where the null fails and the family
    succeeds (family adds something) and the reverse.
If NULL A clears at the same rate the family clears, the sentence is
"stuckness is one swap deep," not "the alphabet descends." Both
outcomes are informative; neither is a kill of DGT — DGT's content
would then be that the FAMILY-restricted move set suffices, which is
weaker or stronger than the null exactly by these numbers.

TESTS (X/Y): 1. legal-family gate rate (existence k/N; fraction
stats) · 2. all-image gate rate · 3. NULL A single swaps · 4. NULL B
link-seeded swaps · 5. the comparison table.

Elie, 2026-09-02. 5 tests.
"""

import hashlib
import importlib.util
import json
import os
import statistics
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


GA = load("t5591br", "toy_5591_SEP2_gate_aware_potential_legal_only_DGT"
          "_recount_54_and_1801.py")
D6, LG = GA.D6, GA.LG
W, TE, T2 = GA.W, GA.TE, GA.T2
E1, G5, X3, WF, F1 = GA.E1, GA.G5, GA.X3, GA.WF, GA.F1
gate = GA.gate


def audit(adj, tv, lcyc, c0, vs, words):
    imgs = LG.word_images_legal(adj, c0, tv, lcyc, words)
    legal = [(k) for w, k, fl in imgs if all(fl)]
    allimg = [k for w, k, fl in imgs]
    lg = sum(1 for k in legal if gate(adj, k, tv))
    ag = sum(1 for k in allimg if gate(adj, k, tv))
    # NULL A: every single swap in T-v
    nA = 0
    gA = 0
    link = set(adj[tv])
    nB = 0
    gB = 0
    for u in vs:
        a = c0[u]
        for b in range(4):
            if b == a:
                continue
            comp = G5.kempe_chain(adj, c0, u, a, b, exclude={tv})
            k = G5.do_swap(c0, comp, a, b)
            if k == c0:
                continue
            g = gate(adj, k, tv)
            nA += 1
            gA += g
            if u in link:
                nB += 1
                gB += g
    return {'n_legal': len(legal), 'g_legal': lg, 'n_all': len(allimg),
            'g_all': ag, 'nA': nA, 'gA': gA, 'nB': nB, 'gB': gB}


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5592 — base-rate audit: family vs single-swap null")
    print("=" * 70)
    moves, words, _ = WF.context_family()
    rows = []
    for label, faces, adj, tv, lcyc, c0, vs, freed in TE.failure_set():
        r = audit(adj, tv, lcyc, c0, vs, words)
        r['pop'] = '54'
        r['label'] = label
        rows.append(r)
    stores = []
    for fn, pre in D6.FILES:
        raw = open(os.path.join(HERE, fn), 'rb').read()
        assert hashlib.sha256(raw).hexdigest().startswith(pre)
        stores.append((fn, json.loads(raw)))
    fams = {label: (faces, adj, tv)
            for label, faces, adj, tv in T2.build_tranche2()}
    for fn, st in stores:
        for label, blk in st.items():
            faces, adj, tv = fams[label]
            lcyc = E1.link_cycle(faces, tv)
            smap = {str(v): v for v in adj}
            vs = [v for v in sorted(adj, key=str) if v != tv]
            for crec in blk['stuck']:
                c0 = {smap[k]: v for k, v in crec.items()}
                r = audit(adj, tv, lcyc, c0, vs, words)
                r['pop'] = '1801'
                r['label'] = label
                rows.append(r)
    hh = hashlib.sha256(json.dumps([str(sorted(r.items())) for r in rows]
                                   ).encode()).hexdigest()
    print(f"\n  {len(rows)} configurations audited; rows hashed BEFORE "
          f"the counts: sha256 {hh[:32]}...")
    n = len(rows)

    def stats(key_g, key_n):
        fr = [r[key_g] / r[key_n] for r in rows if r[key_n]]
        ex = sum(1 for r in rows if r[key_g] > 0)
        return ex, min(fr), statistics.median(fr), max(fr)

    e1, mn1, md1, mx1 = stats('g_legal', 'n_legal')
    t1 = e1 == n
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. LEGAL FAMILY: a gate-phase "
          f"legal image exists {e1}/{n}; per-config fraction of legal "
          f"images that are gate-phase min {mn1:.2f} median {md1:.2f} "
          f"max {mx1:.2f}; legal images per config "
          f"{dict(sorted(Counter(r['n_legal'] for r in rows).items()))}")
    e2, mn2, md2, mx2 = stats('g_all', 'n_all')
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. ALL IMAGES (legal+vacuous): "
          f"exists {e2}/{n}; fraction min {mn2:.2f} median {md2:.2f} max "
          f"{mx2:.2f}")
    e3, mn3, md3, mx3 = stats('gA', 'nA')
    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. NULL A (every single Kempe "
          f"swap in T-v): exists {e3}/{n}; fraction min {mn3:.2f} median "
          f"{md3:.2f} max {mx3:.2f}; swaps per config median "
          f"{statistics.median(r['nA'] for r in rows)}")
    e4, mn4, md4, mx4 = stats('gB', 'nB')
    t4 = True
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. NULL B (single swaps seeded "
          f"at the link): exists {e4}/{n}; fraction min {mn4:.2f} median "
          f"{md4:.2f} max {mx4:.2f}")
    fam_not_null = sum(1 for r in rows if r['g_legal'] > 0 and r['gA'] == 0)
    null_not_fam = sum(1 for r in rows if r['g_legal'] == 0 and r['gA'] > 0)
    famB = sum(1 for r in rows if r['g_legal'] > 0 and r['gB'] == 0)
    t5 = True
    by_pop = {}
    for r in rows:
        by_pop.setdefault(r['pop'], [0, 0, 0, 0])
        by_pop[r['pop']][0] += 1
        by_pop[r['pop']][1] += r['g_legal'] > 0
        by_pop[r['pop']][2] += r['gA'] > 0
        by_pop[r['pop']][3] += r['gB'] > 0
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. COMPARISON: family clears "
          f"where NULL A fails: {fam_not_null}/{n}; NULL A clears where "
          f"family fails: {null_not_fam}/{n}; family clears where NULL B "
          f"(link swaps) fails: {famB}/{n}; by population (n, family, "
          f"nullA, nullB): {by_pop}")
    verdict = ("the single-swap null clears EVERYWHERE the family does — "
               "stuckness is one swap deep in the measured world; the "
               "family is not the mechanism of the 5591 count"
               if e3 == n else
               f"the single-swap null FAILS on {n - e3} configurations "
               f"where the family clears — the family-restricted move set "
               f"adds content beyond one random swap")
    print(f"\n  VERDICT: {verdict}")

    res = [t1, t2, t3, t4, t5]
    print(f"\n{'=' * 70}")
    print(f"Toy 5592 -- SCORE: {sum(res)}/{len(res)}  (can-fail: 1)")
    print(f"{'=' * 70}")
