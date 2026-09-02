#!/usr/bin/env python3
"""
Toy 5597 — LYRA'S DICHOTOMY, ESCORTED: Δ / Δ′ counts for W_i and W_j
on the 2,927, with the Legality Lemma as positive control

Lyra (DGT derivation, 09-02): W_i := (C_i,(r,s_i)) · (C_j,(r,s_j)),
where C_i is the r-copy link-adjacent to n_si and C_j the r-copy
link-adjacent to n_sj (pinned by ADJACENCY, not by the instrument's
B1/B2 label — quote the invariant, not the coordinate). W_j = mirror.
Lemma L: both words fully legal at every stuck configuration (control:
4/4 stages on all, both words; one illegal stage = re-open).
Lemma D: after stages 1-2, Δ := "far singleton n_sj lies in the
(r,s_i)-chain of C_i" (membership in X3). Δ-NO ⟹ the image has s_i
absent from v's link (directly insertable). Δ-YES ⟹ second dichotomy
Δ′ := {C_i, n_si} ⊆ X4; both branches saturated gap-2; τ undecided.

MEASURED per configuration, per word: stage flags; link word after
each stage vs Lyra's forced predictions (c1, c2 forced; c3/c4 per
branch); Δ; on Δ-NO whether s_i is absent (must be, by Lemma D); on
Δ-YES: Δ′, and the image's τ (≤5 or 6) and direct-insertability.
Leaf labels: ΔNO-INS · ΔYES/Δ′NO-{ins,gate,stuck} · ΔYES/Δ′YES-{...}.
Coverage: configurations where W_i OR W_j gives a direct/gate exit.

Populations: the deduplicated 2,927 (5595's assembly). BLIND: records
hashed before counts.

Elie, 2026-09-02.
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


EB = load("t5595dl", "toy_5595_SEP2_EB_hitting_set_minimum_words_growth"
          "_curve_pattern_table.py")
LG, TE, D6, T2 = EB.LG, EB.TE, EB.D6, EB.T2
RD = EB.RD
E1, G5, X3, WF, F1 = EB.E1, EB.G5, EB.X3, EB.WF, EB.F1


def assemble():
    configs = []
    seen = set()

    def push(pop, label, faces, adj, tv, c0):
        vs = sorted((u for u in adj if u != tv), key=str)
        key = (label, str(tv), tuple(c0[u] for u in vs))
        if key in seen:
            return
        seen.add(key)
        configs.append((pop, label, adj, tv, E1.link_cycle(faces, tv), c0))
    for label, faces, adj, tv, stuck, freed, exact in RD.build_pops():
        for c0 in stuck:
            if G5.operational_tau(adj, c0, tv) != 6 or X3.freeable(adj, c0, tv):
                continue
            push(label, label, faces, adj, tv, c0)
    for label, faces, adj, tv, lcyc, c0, vs, freed in TE.failure_set():
        push('the54', label, faces, adj, tv, c0)
    fams = {label: (faces, adj, tv) for label, faces, adj, tv in T2.build_tranche2()}
    for fn, pre in D6.FILES:
        raw = open(os.path.join(HERE, fn), 'rb').read()
        assert hashlib.sha256(raw).hexdigest().startswith(pre)
        st = json.loads(raw)
        tr = '2a' if 'tranche2_' in fn else '2b'
        for label, blk in st.items():
            faces, adj, tv = fams[label]
            smap = {str(v): v for v in adj}
            for crec in blk['stuck']:
                push(tr, label, faces, adj, tv, {smap[k]: v for k, v in crec.items()})
    return configs


def analyze(adj, tv, lcyc, c0, which):
    """which = 'i' or 'j'. Returns a record dict."""
    rm = WF.role_map(adj, c0, tv, lcyc)
    if rm is None:
        return {'status': 'no-context'}
    vmap, cmap = rm
    r, sM = cmap['r'], cmap['s_M']
    # the two singletons and their adjacent copies, by link adjacency
    if which == 'i':
        s_near, s_far = cmap['s_i'], cmap['s_j']
        n_near, n_far = vmap['n_si'], vmap['n_sj']
    else:
        s_near, s_far = cmap['s_j'], cmap['s_i']
        n_near, n_far = vmap['n_sj'], vmap['n_si']
    copies = [vmap['B1'], vmap['B2']]
    C_near = next(b for b in copies if n_near in adj[b])
    C_far = next(b for b in copies if b != C_near)
    if n_far not in adj[C_far]:
        return {'status': 'adjacency-mismatch'}
    n_sM = vmap['n_sM']
    order = [C_far, n_sM, C_near, n_near, n_far]      # Lyra's (p0..p4)
    inv = {r: 'r', sM: 's_M', s_near: 's_n', s_far: 's_f'}

    def link_word(c):
        return tuple(inv.get(c[u], '?') for u in order)
    m1 = ((min(r, s_near), max(r, s_near)), C_near)
    m2 = ((min(r, s_far), max(r, s_far)), C_far)
    chains = []
    flags = []
    cur = c0
    stages = []
    for m in (m1, m2, m1, m2):
        pair, seed = m
        legal = cur.get(seed) in pair
        flags.append(legal)
        if legal:
            ch = G5.kempe_chain(adj, cur, seed, pair[0], pair[1], exclude={tv})
            cur = G5.do_swap(cur, ch, pair[0], pair[1])
        else:
            ch = set()
        chains.append(ch)
        stages.append(link_word(cur))
    img = cur
    rec = {'status': 'ok', 'flags': tuple(flags), 'stages': tuple(stages),
           'c1_ok': stages[0] == ('r', 's_M', 's_n', 'r', 's_f'),
           'c2_ok': stages[1] == ('s_f', 's_M', 's_n', 's_f', 'r'),
           'delta': n_far in chains[2]}
    lk = {img[u] for u in adj[tv]}
    rec['direct'] = len(lk) < 4
    rec['absent'] = tuple(sorted(inv.get(x, '?') for x in range(4) if x not in lk))
    rec['tau'] = G5.operational_tau(adj, img, tv)
    rec['proper'] = G5.is_proper(adj, img, skip=tv)
    if not rec['delta']:
        rec['c4_ok'] = stages[3] == ('r', 's_M', 's_f', 'r', 's_f')
        rec['leaf'] = 'ΔNO-' + ('INS' if rec['direct'] else 'NOT-INS!')
    else:
        rec['dprime'] = (C_near in chains[3]) and (n_near in chains[3])
        pred = ('r', 's_M', 's_f', 'r', 's_n') if rec['dprime'] else ('r', 's_M', 'r', 's_f', 's_n')
        rec['c4_ok'] = stages[3] == pred
        state = 'ins' if rec['direct'] else ('gate' if rec['tau'] <= 5 else 'stuck')
        rec['leaf'] = f"ΔYES/Δ′{'YES' if rec['dprime'] else 'NO'}-{state}"
    return rec


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5597 — Lyra's dichotomy escorted: Δ/Δ′ for W_i, W_j")
    print("=" * 70)
    configs = assemble()
    n = len(configs)
    recs = []
    for pop, label, adj, tv, lcyc, c0 in configs:
        ri = analyze(adj, tv, lcyc, c0, 'i')
        rj = analyze(adj, tv, lcyc, c0, 'j')
        recs.append((pop, label, ri, rj))
    hh = hashlib.sha256(json.dumps([str(r) for r in recs]).encode()).hexdigest()
    print(f"\n  {n} configurations; records hashed BEFORE the counts: sha256 {hh[:32]}...")
    stat = Counter((r[2]['status'], r[3]['status']) for r in recs)
    print(f"  status: {dict(stat)}")
    ok = [r for r in recs if r[2]['status'] == 'ok' and r[3]['status'] == 'ok']
    m = len(ok)

    # 1. Lemma L control
    legal_i = sum(1 for r in ok if all(r[2]['flags']))
    legal_j = sum(1 for r in ok if all(r[3]['flags']))
    t1 = legal_i == m and legal_j == m
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. LEMMA L (positive control): fully "
          f"legal W_i {legal_i}/{m}, W_j {legal_j}/{m}; illegal-stage histogram "
          f"W_i {dict(Counter(i+1 for r in ok for i, f in enumerate(r[2]['flags']) if not f))} "
          f"W_j {dict(Counter(i+1 for r in ok for i, f in enumerate(r[3]['flags']) if not f))}")

    # 2. forced link words c1, c2
    c1 = sum(1 for r in ok if r[2]['c1_ok'] and r[3]['c1_ok'])
    c2 = sum(1 for r in ok if r[2]['c2_ok'] and r[3]['c2_ok'])
    t2 = c1 == m and c2 == m
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Forced link words: c₁ as derived "
          f"{c1}/{m}; c₂ as derived {c2}/{m} (both words)")
    if not t2:
        bad = [(r[0], r[1], r[2]['stages'][:2]) for r in ok if not (r[2]['c1_ok'] and r[2]['c2_ok'])][:5]
        print(f"    mismatches (W_i): {bad}")

    # 3. Δ counts and Lemma D
    for w, idx in (('W_i', 2), ('W_j', 3)):
        dno = [r for r in ok if not r[idx]['delta']]
        dyes = [r for r in ok if r[idx]['delta']]
        dno_ins = sum(1 for r in dno if r[idx]['direct'])
        dno_c4 = sum(1 for r in dno if r[idx]['c4_ok'])
        leaves = Counter(r[idx]['leaf'] for r in ok)
        c4y = sum(1 for r in dyes if r[idx]['c4_ok'])
        print(f"\n  {w}: Δ-NO {len(dno)}/{m} (image directly insertable {dno_ins}/{len(dno)}; "
              f"c₄ link as derived {dno_c4}/{len(dno)}) · Δ-YES {len(dyes)}/{m} "
              f"(c₄ link as derived {c4y}/{len(dyes)})")
        print(f"    leaves: {dict(sorted(leaves.items()))}")
    t3 = all(r[2]['direct'] for r in ok if not r[2]['delta']) and \
        all(r[3]['direct'] for r in ok if not r[3]['delta'])
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. LEMMA D: every Δ-NO image is "
          f"directly insertable (both words)")

    # 4. Δ-YES-AND-STUCK class
    ys_i = sum(1 for r in ok if r[2]['delta'] and r[2]['tau'] == 6 and not r[2]['direct'])
    ys_j = sum(1 for r in ok if r[3]['delta'] and r[3]['tau'] == 6 and not r[3]['direct'])
    both_stuck = sum(1 for r in ok if all(r[k]['delta'] and r[k]['tau'] == 6 and not r[k]['direct'] for k in (2, 3)))
    cover = sum(1 for r in ok if any(r[k]['direct'] or r[k]['tau'] <= 5 for k in (2, 3)))
    cover_direct = sum(1 for r in ok if any(r[k]['direct'] for k in (2, 3)))
    t4 = both_stuck == 0
    print(f"\n  Δ-YES ∧ STUCK images: W_i {ys_i}/{m}, W_j {ys_j}/{m}; configurations where "
          f"BOTH words land stuck: {both_stuck}/{m}")
    print(f"  coverage by {{W_i, W_j}}: direct {cover_direct}/{m}; direct-or-gate {cover}/{m}")
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. The Δ-YES-AND-STUCK class for BOTH "
          f"words is empty: {m - both_stuck}/{m} configurations covered by "
          f"W_i or W_j (can fail)")
    bypop = {}
    for r in ok:
        k = r[0]
        bypop.setdefault(k, [0, 0])
        bypop[k][0] += 1
        bypop[k][1] += any(r[kk]['direct'] or r[kk]['tau'] <= 5 for kk in (2, 3))
    print(f"  by population (n, covered): {bypop}")
    unc = [(r[0], r[1], r[2]['leaf'], r[3]['leaf']) for r in ok
           if not any(r[kk]['direct'] or r[kk]['tau'] <= 5 for kk in (2, 3))]
    for u in unc[:12]:
        print(f"    uncovered: {u}")
    res = [t1, t2, t3, t4]
    print(f"\n{'=' * 70}")
    print(f"Toy 5597 -- SCORE: {sum(res)}/{len(res)}  (can-fail: 1, 2, 3, 4)")
    print(f"{'=' * 70}")
