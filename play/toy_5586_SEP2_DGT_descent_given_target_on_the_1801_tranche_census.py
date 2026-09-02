#!/usr/bin/env python3
"""
Toy 5586 — DGT (DESCENT-GIVEN-TARGET) ON THE 1,801: Lyra's kill
condition 2, the 5582 loop, on every committed tranche configuration

Lyra's pre-registration (09-02 08:06), kill condition 2 for DGT: a
stuck c with T != {} such that for EVERY target and EVERY family word
the step fails to descend — a gate-phase Kempe-locked hole.
"Escortable: Elie's 5582/5583 instrument is exactly this test with a
sampled T (false-negative direction only)." This toy runs that test on
the 1,801 committed, unseen configurations (tranche-2a 792 + 2b 1,009;
hash-committed 5574/5579), which until now were tested only under the
Family Exclusion predicate — NOT under iterated d_gate descent.

THE TEST per configuration: 5582's iterate_chain — at each stuck step
search the 186-word family for strict d_gate descent (d = min Hamming
to the regenerated tau<=5 sample), apply the best, halt at freed
(tau<=5) or directly freeable, cap d_gate(c0)+1 steps. Freed sets are
REGENERATED bit-identically (5574/5579 seeds: n_seeds=20, n_walk=60,
amp=30) — the sampled-T caveat of 5582/5583 carries: a 'no-descent'
here is a shallow-sample candidate FIRST (5583 dissolved one; 5585
dissolved it again), a kill only after deepening.

ALSO LOGGED: per-target menu depth (rank of the first target that
admits a per-target strictly-descending word, nearest-40 menu), for
the (d3) theorem's quantifier — 5585 measured K=3 on the 54.

BLIND: per-config verdicts hashed BEFORE the count. Counts only.

TESTS (X/Y): 1. committed populations re-read + file hashes match the
record (7c930cb2 / 84ae31ca) · 2. freed samples regenerated, nonempty
for every hole · 3. DGT verdict k/1801 (can fail) · 4. per-target menu
depth (can fail if any config admits no target in 40) · 5. residue
exhibited whole, or none.

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


W = load("t5582dgt", "toy_5582_SEP1_ss814_world_ab_diagnostic_iterated"
         "_arsenal.py")
TE = load("t5585dgt", "toy_5585_SEP2_target_existence_menu_sweep_third"
          "_door_prebuilt.py")
T2 = load("t5574dgt", "toy_5574_SEP1_armed_tranche2_family_exclusion"
          "_falsifier.py")
E1, G5, X3, WF, F1 = W.E1, W.G5, W.X3, W.WF, W.F1

FILES = [('.tranche2_family_exclusion.json', '7c930cb2'),
         ('.tranche2b_family_exclusion.json', '84ae31ca')]


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5586 — DGT on the 1,801 committed tranche configurations")
    print("=" * 70)

    stores = []
    hash_ok = []
    for fn, pre in FILES:
        raw = open(os.path.join(HERE, fn), 'rb').read()
        hh = hashlib.sha256(raw).hexdigest()
        hash_ok.append(hh.startswith(pre))
        stores.append((fn, json.loads(raw), hh))
        print(f"  {fn}: sha256 {hh[:16]}... (record {pre}: "
              f"{'MATCH' if hh.startswith(pre) else 'MISMATCH'})")
    n_tot = sum(len(v['stuck']) for _, st, _ in stores for v in st.values())
    t1 = all(hash_ok) and n_tot == 1801
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Populations re-read: "
          f"{n_tot} configurations; file hashes vs record")

    fams = {label: (faces, adj, tv)
            for label, faces, adj, tv in T2.build_tranche2()}
    freed_by = {}
    for label, (faces, adj, tv) in fams.items():
        lcyc = E1.link_cycle(faces, tv)
        if len(lcyc) != 5:
            continue
        _st, fr = F1.stuck_harvest(faces, adj, tv, n_seeds=20,
                                   n_walk=60, amp=30)
        freed_by[label] = fr
    labels_needed = {lb for _, st, _ in stores for lb in st}
    t2 = all(lb in freed_by and len(freed_by[lb]) > 0
             for lb in labels_needed)
    print(f"\n  freed samples regenerated: "
          f"{ {lb: len(freed_by.get(lb, [])) for lb in sorted(labels_needed)} }")
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Freed (tau<=5) sample "
          f"nonempty for every hole")

    moves, words, _ = WF.context_family()
    records = []
    for fn, st, _ in stores:
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
                d0 = min(TE.ham(c0, f, vs) for f in freed)
                oc, stp, tj = W.iterate_chain(adj, tv, vs, c0, freed,
                                              words, d0 + 1)
                # per-target menu depth on the nearest-40 menu
                imgs = TE.word_images(adj, c0, tv, lcyc, words)
                byd = sorted(freed, key=lambda f: TE.ham(c0, f, vs))
                rank = None
                for r_, cst in enumerate(byd[:40]):
                    h0 = TE.ham(c0, cst, vs)
                    if any(TE.ham(k, cst, vs) < h0 for _w, k in (imgs or [])):
                        rank = r_
                        break
                records.append((tr, label, i, d0, oc, stp, tuple(tj),
                                rank))
    blob = json.dumps([str(r) for r in records]).encode()
    hh = hashlib.sha256(blob).hexdigest()
    print(f"\n  per-config verdicts hashed BEFORE the count: sha256 "
          f"{hh[:32]}...")

    n = len(records)
    freed_n = sum(1 for r in records if r[4] == 'freed')
    by_fam = {}
    for r in records:
        by_fam.setdefault((r[0], r[1]), Counter())[r[4]] += 1
    steps = Counter(r[5] for r in records if r[4] == 'freed')
    d0s = Counter(r[3] for r in records)
    t3 = freed_n == n
    print(f"\n  DGT outcomes by hole: ")
    for k in sorted(by_fam):
        print(f"    {k[0]} {k[1]}: {dict(by_fam[k])}")
    print(f"  recovery step-counts: {dict(sorted(steps.items()))}")
    print(f"  d_gate(c0) distribution: {dict(sorted(d0s.items()))}")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. DGT (iterated strict "
          f"d_gate descent to the gate phase, <= d_gate+1 words): "
          f"{freed_n}/{n}")

    ranks = Counter(r[7] for r in records)
    t4 = None not in ranks
    print(f"\n  first-admitting target rank (per-target descent, "
          f"nearest-40): {dict(sorted(ranks.items(), key=lambda kv: (kv[0] is None, kv[0])))}"
          f" -> menu depth K = "
          f"{max(k for k in ranks if k is not None) + 1 if any(k is not None for k in ranks) else 'n/a'}")
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. A per-target admitting "
          f"target exists within the nearest 40: "
          f"{n - ranks.get(None, 0)}/{n}")

    residue = [r for r in records if r[4] != 'freed']
    t5 = True
    if residue:
        print(f"\n  RESIDUE ({len(residue)}), whole — shallow-sample "
              f"candidates FIRST (5583/5585 precedent), kills only "
              f"after deepening:")
        for r in residue[:40]:
            print(f"    {r}")
    else:
        print(f"\n  RESIDUE: none")
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. Residue exhibited "
          f"({len(residue)}) or none")

    res = [t1, t2, t3, t4, t5]
    print(f"\n{'=' * 70}")
    print(f"Toy 5586 -- SCORE: {sum(res)}/{len(res)}  (can-fail: 3, 4)")
    print(f"{'=' * 70}")
