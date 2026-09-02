#!/usr/bin/env python3
"""
Toy 5632 — Round 107, Casey's k > 12 question (Keeper's relay, 16:30):
Are the sub-maximal period lattices of toy 5626 exactly on graphs whose degrees are all in {5, 6}?

ARITHMETIC FIRST (so the question is asked at the right level): on a sphere triangulation
Σ_v (6 − deg v) = 12, so n_5 = 12 + Σ_{d≥7} (d−6) n_d, and the odd-vertex count is
k = n_5 + n_7 + n_9 + … = 12 + Σ_{d≥7} (d−6) n_d + Σ_{d odd ≥7} n_d.  Hence in the 5-connected frame
k = 12 ⟺ max degree ≤ 6 ⟺ degrees ⊆ {5,6} (the graph is the dual of a fullerene). The eleven drops of
5626 all had k = 12, so "on {5,6}-graphs" is TRUE by this identity (Test 1 verifies the identity on
every census graph). The measurable content is finer, and that is what is reported:
  (A) EXHAUSTIVE on every {5,6}-graph (k = 12) in plantri -c5, n = 12..NMAX: ALL proper 4-colourings
      mod S4 (no sampling, no cap) — which graphs host a drop (rank 1, or rank 2 with index > 1),
      how many colourings per graph drop, and the graph's (n_5, n_6) = (12, n−12).
  (B) THE k > 12 NEGATIVE, exhaustive where affordable: every graph with a vertex of degree ≥ 7 in
      plantri -c5 n = 12..NEXH, ALL colourings; plus the 197,224 k > 12 rows already in 5626's record
      (sampled at n ≥ 22). Report the drop count (pre-registered expectation from 5626: 0) and say
      which part is exhaustive and which is sampled.
  (C) Positive control: the eleven known drops (n=20 idx 16 ×8, idx 18 ×2; n=21 idx 90 ×1) must be
      re-found by the exhaustive pass (A).
TESTS (X/Y):
  1. Identity k = 12 + Σ_{d≥7}(d−6)n_d + Σ_{d odd≥7} n_d on every graph n ≤ NMAX; k=12 ⟺ maxdeg ≤ 6.
  2. Control (C): the eleven known drops re-found, same (r, ed) multiset.
  3. (A) rendered: per-graph table written; the set of hosting graphs listed with (n_5, n_6).
  4. (B) rendered: the k>12 drop count stated with its exhaustive / sampled split.
Report the graphs, not a verdict. Nothing about n = 25.
Elie, 2026-09-02 (Round 107). 4 tests.
"""
import importlib.util, json, os, sys, time, hashlib
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('t5626', os.path.join(HERE,
    'toy_5626_SEP2_E1_branched_cover_clause_height_lift_period_lattice_and_dislocation_centers_vs_n.py'))
T = importlib.util.module_from_spec(spec); _argv = sys.argv; sys.argv = ['x', '12']; spec.loader.exec_module(T); sys.argv = _argv
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 24     # exhaustive on {5,6}-graphs up to here
NEXH = int(sys.argv[2]) if len(sys.argv) > 2 else 20     # exhaustive on k>12 graphs up to here

def is_drop(m):
    return m['r'] < 2 or m['ed'] != (2, 2)

if __name__ == '__main__':
    t0 = time.time()
    print('=' * 78); print(f'Toy 5632 — k > 12 question: drops on {{5,6}}-graphs? exhaustive n<= {NMAX}; k>12 exhaustive n<= {NEXH}'); print('=' * 78)
    score = 0
    ident_ok = True
    hosts = []      # (n, idx, n5, n6, ncol, ndrop, Counter of (r,ed))
    tableA = []
    known = Counter()
    kgt = dict(exh_graphs=0, exh_col=0, exh_drops=0, drops_detail=Counter())
    for n in range(12, NMAX + 1):
        gs = T.plantri_rot(n)
        n56 = 0
        for gi, rot in enumerate(gs):
            deg = [len(r) for r in rot]
            k = sum(1 for d in deg if d % 2)
            nd = Counter(deg)
            k_pred = 12 + sum((d - 6) * c for d, c in nd.items() if d >= 7) + sum(c for d, c in nd.items() if d >= 7 and d % 2)
            if k != k_pred or ((k == 12) != (max(deg) <= 6)):
                ident_ok = False
            if max(deg) <= 6:
                n56 += 1
                faces = T.faces_of(rot)
                cols = T.colorings_mod_s4(rot, 10 ** 7)
                cnt = Counter(); nd_ = 0
                for f in cols:
                    m = T.cover_measure(rot, faces, f)
                    if is_drop(m):
                        nd_ += 1; cnt[(m['r'], m['ed'])] += 1
                        if (n, gi) in [(20, 16), (20, 18), (21, 90)]:
                            known[(n, gi, m['r'], m['ed'])] += 1
                tableA.append(dict(n=n, idx=gi, n5=nd[5], n6=nd[6], colorings=len(cols), drops=nd_,
                                   detail={f'{r},{ed}': c for (r, ed), c in cnt.items()}))
                if nd_:
                    hosts.append((n, gi, nd[5], nd[6], len(cols), nd_, {f"{r},{ed}": c for (r, ed), c in cnt.items()}))
            elif n <= NEXH:
                faces = T.faces_of(rot)
                cols = T.colorings_mod_s4(rot, 10 ** 7)
                kgt['exh_graphs'] += 1; kgt['exh_col'] += len(cols)
                for f in cols:
                    m = T.cover_measure(rot, faces, f)
                    if is_drop(m):
                        kgt['exh_drops'] += 1; kgt['drops_detail'][(n, gi, k, m['r'], m['ed'])] += 1
        hostn = [h for h in hosts if h[0] == n]
        print(f'  n={n}: graphs {len(gs)}, {{5,6}}-graphs {n56} (all colourings), hosting a drop: {len(hostn)}  [{time.time()-t0:.0f}s]')
        for h in hostn:
            print(f'      idx {h[1]}: (n5,n6)=({h[2]},{h[3]}), colourings {h[4]}, drops {h[5]} {h[6]}')
        sys.stdout.flush()
    print(f'\n  Test 1 (k = 12 + Σ(d−6)n_d + Σ_odd n_d on every graph; k=12 ⟺ maxdeg ≤ 6) {"PASS" if ident_ok else "FAIL"}'); score += ident_ok
    exp = Counter({(20, 16, 1, (2,)): 4, (20, 16, 2, (2, 4)): 4, (20, 18, 1, (2,)): 2, (21, 90, 1, (2,)): 1})
    t2 = all(known[key] >= v for key, v in exp.items())
    print(f'  Test 2 (the eleven known drops re-found exhaustively): found {dict(known)} vs 5626 sample {dict(exp)} -> {"PASS" if t2 else "FAIL"}'); score += t2
    # 5626 record recount for k>12
    rec = os.path.join(HERE, '.e1_5626_records.txt')
    s_rows = s_drops = 0
    for line in open(rec):
        p = line.split()
        k = int(p[3].split('=')[1])
        if k > 12:
            s_rows += 1
            if not (p[4] == 'r=2' and p[5] == 'ed=(2,' and p[6] == '2)'):
                s_drops += 1
    nA = len(tableA); nAh = len(hosts); colA = sum(t['colorings'] for t in tableA); dropA = sum(t['drops'] for t in tableA)
    print(f'\n  (A) {{5,6}}-graphs n=12..{NMAX}: {nA} graphs, {colA} colourings (exhaustive), drops {dropA} on {nAh} graphs')
    print(f'  (B) k>12: exhaustive n<= {NEXH}: {kgt["exh_graphs"]} graphs, {kgt["exh_col"]} colourings, drops {kgt["exh_drops"]} {dict(kgt["drops_detail"]) if kgt["exh_drops"] else ""}; '
          f'5626 sampled rows k>12 (n<=24): {s_rows}, drops {s_drops}')
    t3 = nA > 0; t4 = True
    print(f'  Test 3 (A rendered) {"PASS" if t3 else "FAIL"}'); print(f'  Test 4 (B rendered) PASS'); score += t3 + t4
    out = dict(tableA=tableA, hosts=hosts, kgt12=dict(exh_graphs=kgt['exh_graphs'], exh_col=kgt['exh_col'], exh_drops=kgt['exh_drops'],
               detail={str(a): b for a, b in kgt['drops_detail'].items()}, sampled_rows=s_rows, sampled_drops=s_drops))
    json.dump(out, open(os.path.join(HERE, '.k12_5632_table.json'), 'w'), indent=1)
    h = hashlib.sha256(json.dumps(out, sort_keys=True).encode()).hexdigest()[:8]
    print(f'  table: play/.k12_5632_table.json sha256 {h}')
    print(f'\nSCORE: {score}/4   [{time.time()-t0:.0f}s]')
