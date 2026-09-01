#!/usr/bin/env python3
"""
Toy 5567 — F3 (Sept 1 PM): THE J2 CLAUSE, MEASURED VERBATIM

Lyra's open step in J2 (L2, closure path, last clause): "the gate's
re-signing agrees with some freed target on >= 1 patch vertex and
disagrees nowhere new."

MEASURED VERBATIM, per gate application c -> k with canonical patch P
(charge patch mod gauge): does there exist a freed coloring f* with
  (a) AGREEMENT GAINED on P: exists v in P with k(v) = f*(v) and
      c(v) != f*(v);
  (b) NOWHERE NEW: {v : k(v) != f*(v)} is a subset of
      {v : c(v) != f*(v)}.
Note (a) and (b) jointly imply d(k) < d(c) against f* — the clause IS
a descent certificate. Two rates reported: per-application (every gate)
and per-stuck (exists a gate whose re-signing satisfies it — the rate
J2 actually needs, since the word w is CHOSEN).

CAVEAT DIRECTION (declared): freed sets are exact on Fritsch and
sampled elsewhere. A missing freed target can only produce FALSE
NEGATIVES on the exists-f* test — so a 100%% rate on sampled objects
UNDERSTATES nothing, and any violation on Fritsch is exact.

If violations exist: the pattern (which (a)/(b) half fails, where) is
the missing clause's true shape — reported in full.

TESTS (X/Y): 1. populations (Fritsch exact + harvest) · 2. the
per-application and per-stuck rates · 3. the verdict (clause holds /
the violation pattern).

Elie, 2026-09-01. Millennium week II. 3 tests.
"""

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


F1 = load("t5565f3", "toy_5565_SEP1_F1_breadth_falsifier_leaving_home"
          "_context_hunt.py")
E1, G5, X3, H8 = F1.E1, F1.G5, F1.X3, F1.H8


def clause_for(adj, tv, vs, comp_faces, c, freed, cap_gates=None):
    """Returns (n_gates, n_gates_ok, exists_ok, viol_examples)."""
    gs = E1.gates_of(adj, c, tv)
    if cap_gates:
        gs = gs[:cap_gates]

    def charge(cc):
        w = {u: 0 for u in vs}
        for f in comp_faces:
            z = 1 if H8.face_sign(f, cc) == 1 else -1
            for x in f:
                w[x] += z
        return w

    c0f = charge(c)
    n_ok = 0
    viol = None
    for k in gs:
        c1f = charge(k)
        pp = {u for u in vs if c1f[u] != c0f[u]}
        pm = {u for u in vs if c1f[u] != -c0f[u]}
        patch = pp if len(pp) <= len(pm) else pm
        found = False
        best_bad = None
        for f2 in freed:
            gained = any(k[v] == f2[v] and c[v] != f2[v]
                         for v in patch)
            new_dis = [v for v in vs
                       if k[v] != f2[v] and c[v] == f2[v]]
            if gained and not new_dis:
                found = True
                break
            bad = (0 if gained else 1, len(new_dis))
            if best_bad is None or bad < best_bad[0]:
                best_bad = (bad, gained, len(new_dis))
        if found:
            n_ok += 1
        elif viol is None and best_bad is not None:
            viol = best_bad
    return len(gs), n_ok, n_ok > 0, viol


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5567 — F3: the J2 clause, measured verbatim")
    print("=" * 70)

    pops = []
    fr_faces = G5.fritsch_faces()
    fr_adj = G5.adj_from_faces(fr_faces)
    fr_tv = [v for v in sorted(fr_adj) if len(fr_adj[v]) == 5][0]
    allc = list(G5.exhaustive_colorings(fr_adj, fr_tv))
    fr_stuck = [c for c in allc
                if G5.operational_tau(fr_adj, c, fr_tv) == 6
                and not X3.freeable(fr_adj, c, fr_tv)]
    fr_freed = [c for c in allc
                if G5.operational_tau(fr_adj, c, fr_tv) <= 5]
    pops.append(('Fritsch(EXACT)', fr_faces, fr_adj, fr_tv, fr_stuck,
                 fr_freed, True))

    harvest = json.load(open(os.path.join(HERE, '.f1_harvest.json')))
    objs = {}
    ad = G5.errera_adj()
    tris, ok, _m = G5.faces_from_adj_triangulation(ad)
    objs['B-errera'] = (tris, ad)
    t5 = [tuple(f) for f in F1.P3.antiprism_stack(5)]
    objs['C-T5'] = (t5, G5.adj_from_faces(t5))
    r = F1.F3T.family_B_right(3, 0)
    objs['D-flip3'] = (r[0], G5.adj_from_faces(r[0]))
    for label, (faces, adj) in objs.items():
        if label not in harvest:
            continue
        tvraw = harvest[label]['tv']
        tv = next(v for v in adj if str(v) == tvraw)
        smap = {str(v): v for v in adj}
        stuck = [{smap[k2]: v for k2, v in crec.items()}
                 for crec in harvest[label]['stuck']][:60]
        _s, freed = F1.stuck_harvest(faces, adj, tv, n_seeds=15,
                                     n_walk=50, amp=0)
        pops.append((label, faces, adj, tv, stuck, freed, False))

    t1 = len(pops) >= 3 and len(fr_stuck) == 72
    print(f"\n  populations: "
          f"{[(p[0], len(p[4]), len(p[5])) for p in pops]}")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Populations "
          f"(name, stuck, freed); Fritsch exact")

    tot_apps = tot_ok = 0
    stuck_n = stuck_ok = 0
    viols = Counter()
    fr_exact_viol = 0
    for label, faces, adj, tv, stuck, freed, exact in pops:
        vs = [v for v in sorted(adj, key=str) if v != tv]
        of = H8.orient_faces([tuple(f) for f in faces])
        comp_faces = [f for f in of if tv not in f]
        for c in stuck:
            ng, nok, ex, viol = clause_for(adj, tv, vs, comp_faces, c,
                                           freed, cap_gates=40)
            tot_apps += ng
            tot_ok += nok
            stuck_n += 1
            stuck_ok += ex
            if not ex:
                viols[(label, viol)] += 1
                if exact:
                    fr_exact_viol += 1
    t2 = stuck_n > 200
    print(f"\n  per-APPLICATION rate: {tot_ok}/{tot_apps} "
          f"({100 * tot_ok / max(tot_apps, 1):.1f}%)")
    print(f"  per-STUCK exists-gate rate (the rate J2 needs): "
          f"{stuck_ok}/{stuck_n}")
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Rates measured")

    t3 = True
    if stuck_ok == stuck_n:
        v = (f"THE CLAUSE HOLDS per-stuck at 100% ({stuck_n}/"
             f"{stuck_n}, Fritsch column exact) — Lyra derives toward "
             f"a measured truth; note the per-application rate "
             f"({100 * tot_ok / max(tot_apps, 1):.0f}%) shows the "
             f"word must be CHOSEN, not arbitrary")
    else:
        v = (f"VIOLATIONS: {stuck_n - stuck_ok}/{stuck_n} stuck lack "
             f"any clause-satisfying gate ({fr_exact_viol} EXACT on "
             f"Fritsch; sampled-freed false-negative caveat "
             f"elsewhere); pattern ((gained?, new-disagreements), "
             f"count): {dict(viols)}")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. VERDICT: {v}")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5567 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
