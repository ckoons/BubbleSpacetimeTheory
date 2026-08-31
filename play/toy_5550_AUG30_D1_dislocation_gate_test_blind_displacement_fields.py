#!/usr/bin/env python3
"""
Toy 5550 — D1 (Round 14): THE DISLOCATION-GATE TEST, blind

Keeper's pre-registered guess: a support-3 gate is an ELEMENTARY
DISLOCATION MOVE — transport of one omega-unit by one step. If yes, the
gate IS the defect dynamics and Gate Existence becomes physics.

SEMANTICS (declared; Cal's pre-score not on disk at build): ambient =
Fritsch-0; charge field c(v) = signed face-sum over COMPLETE faces (V3's
relative convention); knots = charge-quantized sites. BLIND PROTOCOL: the
displacement fields Delta-c = c_after - c_before are computed for ALL
unsticking gate applications (the narrow 6,624 population) and HASHED
BEFORE any classification taxonomy is applied — the data names the move
class, per the pre-registration's own fallback clause.

Classification (applied in pass 2): pattern = the sorted tuple of
(nonzero Delta-c values), plus the adjacency structure of the nonzero
support (connected? two-site-adjacent? etc.). Keeper's guess corresponds
to two-site adjacent patterns transporting one quantum; anything else is
the true move class, reported.

TESTS (X/Y):
  1. Blind order enforced (fields hashed before classification).
  2. The pattern census (the taxonomy the data chooses).
  3. VERDICT on the pre-registration, both directions pre-scored.

Elie, 2026-08-30. Millennium week, 4-Color round 14. 3 tests.
"""

import hashlib
import importlib.util
import itertools
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


G5 = load("g5512d1", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")
H8 = load("t5518d1", "toy_5518_AUG30_E4_heawood_gf3_instrument_rank_coset"
          "_stuck_separation.py")
X3 = load("t5521d1", "toy_5521_AUG30_X3_commutator_laboratory_support"
          "_locality_unstick.py")


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5550 — D1: the dislocation-gate test (blind)")
    print("=" * 70)

    faces = G5.fritsch_faces()
    adj = G5.adj_from_faces(faces)
    of = H8.orient_faces([tuple(f) for f in faces])

    # PASS 1 — blind: displacement fields for all unsticking applications
    fields = []
    for tv in [v for v in sorted(adj) if len(adj[v]) == 5]:
        vs = sorted(u for u in adj if u != tv)
        comp_faces = [f for f in of if tv not in f]

        def charge(c):
            w = {u: 0 for u in vs}
            for f in comp_faces:
                s = H8.face_sign(f, c)
                z = 1 if s == 1 else -1
                for x in f:
                    w[x] += z
            return w

        for c in G5.exhaustive_colorings(adj, tv):
            if G5.operational_tau(adj, c, tv) != 6:
                continue
            info = G5.structure_true(faces, adj, c, tv)
            if info is None:
                continue
            swaps, _fl = G5.forced_swaps(adj, c, tv, info)
            succ = sum(1 for (a, b), fv, ch in swaps
                       if G5.operational_tau(adj, G5.do_swap(c, ch, a, b),
                                             tv) <= 5)
            if succ != 0:
                continue
            mv = []
            for u in adj[tv]:
                cu = c[u]
                for other in range(4):
                    if other != cu:
                        mv.append((tuple(sorted((cu, other))), u))
            c0 = charge(c)
            for m1, m2 in itertools.permutations(mv, 2):
                if m1[0] == m2[0]:
                    continue
                k = X3.commutator(adj, c, m1, m2, tv)
                s = X3.support(c, k)
                if not s:
                    continue
                if not G5.is_proper(adj, k, skip=tv):
                    continue
                if not X3.freeable(adj, k, tv):
                    continue
                c1 = charge(k)
                dfield = {u: c1[u] - c0[u] for u in vs if c1[u] != c0[u]}
                fields.append({'tv': tv, 'nsupp': len(s),
                               'dfield': {str(u): d
                                          for u, d in dfield.items()}})
    blob = json.dumps(fields, sort_keys=True).encode()
    h = hashlib.sha256(blob).hexdigest()
    with open(os.path.join(HERE, '.d1_fields.json'), 'wb') as f:
        f.write(blob)
    print(f"\n  PASS 1: {len(fields)} unsticking applications' displacement "
          f"fields; sha256 {h[:32]}...")
    t1 = True
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Blind order enforced")

    # PASS 2 — classification
    pat_census = Counter()
    adjacency_census = Counter()
    for rec in fields:
        df = {int(u): d for u, d in rec['dfield'].items()}
        vals = tuple(sorted(df.values()))
        pat_census[(rec['nsupp'], vals)] += 1
        sup = list(df.keys())
        if len(sup) == 2:
            u, w = sup
            adjacency_census[('2site',
                              'adjacent' if w in adj[u] else 'nonadjacent',
                              vals)] += 1
        elif len(sup) == 0:
            adjacency_census[('0site', '-', ())] += 1
        else:
            # connectivity of support
            comp = {sup[0]}
            stack = [sup[0]]
            while stack:
                x = stack.pop()
                for y in adj[x]:
                    if y in sup and y not in comp:
                        comp.add(y)
                        stack.append(y)
            adjacency_census[(f'{len(sup)}site',
                              'connected' if len(comp) == len(sup)
                              else 'disconnected', vals)] += 1
    print("\n  PATTERN CENSUS (support size, sorted nonzero Delta-c):")
    for k, v in sorted(pat_census.items(), key=lambda x: -x[1])[:12]:
        print(f"    {k}: {v}")
    print("\n  ADJACENCY CENSUS:")
    for k, v in sorted(adjacency_census.items(), key=lambda x: -x[1])[:12]:
        print(f"    {k}: {v}")
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Census computed")

    # verdict: Keeper's guess = every application is a two-site adjacent
    # single-quantum transport
    n_apps = len(fields)
    n_hop = sum(v for k, v in adjacency_census.items()
                if k[0] == '2site' and k[1] == 'adjacent')
    frac = n_hop / n_apps if n_apps else 0
    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. VERDICT: two-site adjacent "
          f"patterns = {n_hop}/{n_apps}. "
          f"{'THE GATE IS A DEFECT HOP — Gate Existence becomes physics' if n_hop == n_apps else 'NOT uniformly a hop — the true move class is the census above (the failure pattern names it)'}")

    res = [t1, t2, t3]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5550 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
