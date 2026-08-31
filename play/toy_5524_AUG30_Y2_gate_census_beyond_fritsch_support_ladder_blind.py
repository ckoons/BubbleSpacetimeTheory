#!/usr/bin/env python3
"""
Toy 5524 — Y2 (Round 5): GATE CENSUS BEYOND FRITSCH

X3 found (exhaustive, Fritsch): a single commutator anchored at the stuck
link unsticks every stuck coloring, minimal unsticking support ONE vertex.
Y2: does the gate exist at every stuck configuration on the towers, Errera,
Kittell?

*** BLIND PREDICTIONS — registered before running, derived from the charge
picture (deg-5 knots carry charge exactly +-3; gates transport charge
locally; deeper knots should need bigger gates):
  B1 (existence): EVERY stuck case on every gallery graph admits an
      unsticking commutator anchored at its link. 100%.
  B2 (the support ladder): minimal unsticking support grows with the
      graph's rescue depth — Fritsch (depth 2): 1 (known, X3);
      T_3 and Errera (depth 3): >= 2; Kittell (depth 4): >= 3.
*** END BLIND ***

Census per stuck case: all anchored moves (link vertex x containing pair),
all ordered overlapping pairs, commutator = 4-word with dynamic chains;
record: does any commutator make v freeable (<=1 swap); minimal support of
an unsticking commutator.

TESTS (X/Y):
  1. Fritsch replication (X3 consistency): 144/144, min support 1.
  2. B1 on T_3 (exhaustive stuck set, 240 cases).
  3. B1 on Errera (sampled stuck set).
  4. B1 on Kittell (sampled stuck set).
  5. B2 the support ladder as registered.

Elie, 2026-08-30. Millennium week, 4-Color round 5. 5 tests.
"""

import importlib.util
import itertools
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


G5 = load("g5512y", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")
T5 = load("t5515y", "toy_5515_AUG30_E1_kring_tower_family_rescue_depth_vs_k"
          "_cal_F0_absorbed.py")
X3 = load("x5521y", "toy_5521_AUG30_X3_commutator_laboratory_support_locality"
          "_unstick.py")


def stuck_cases_of(faces, adj, tvs, colorings_fn):
    out = []
    for tv in tvs:
        for c in colorings_fn(adj, tv):
            if G5.operational_tau(adj, c, tv) != 6:
                continue
            info = G5.structure_true(faces, adj, c, tv)
            if info is None:
                continue
            swaps, _fl = G5.forced_swaps(adj, c, tv, info)
            succ = sum(1 for (a, b), fv, ch in swaps
                       if G5.operational_tau(
                           adj, G5.do_swap(c, ch, a, b), tv) <= 5)
            if succ == 0:
                out.append((tv, c))
    return out


def gate_census(adj, tv, c):
    """(exists_unstick, min_unstick_support)"""
    mv = []
    for u in adj[tv]:
        cu = c[u]
        for other in range(4):
            if other != cu:
                mv.append((tuple(sorted((cu, other))), u))
    best = None
    for m1, m2 in itertools.permutations(mv, 2):
        if m1[0] == m2[0]:
            continue
        ch1 = G5.kempe_chain(adj, c, m1[1], *m1[0], exclude={tv}) \
            if c[m1[1]] in m1[0] else set()
        ch2 = G5.kempe_chain(adj, c, m2[1], *m2[0], exclude={tv}) \
            if c[m2[1]] in m2[0] else set()
        if not ch1 or not ch2 or not (ch1 & ch2):
            continue
        k = X3.commutator(adj, c, m1, m2, tv)
        s = X3.support(c, k)
        if not s:
            continue
        if not G5.is_proper(adj, k, skip=tv):
            continue
        if X3.freeable(adj, k, tv):
            if best is None or len(s) < best:
                best = len(s)
                if best == 1:
                    break
    return best is not None, best


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5524 — Y2: gate census beyond Fritsch")
    print("=" * 70)

    fri_faces = G5.fritsch_faces()
    fri = G5.adj_from_faces(fri_faces)
    err = G5.errera_adj()
    err_faces, _o, _m = G5.faces_from_adj_triangulation(err)
    kit = G5.kittell_adj()
    kit_faces, _o2, _m2 = G5.faces_from_adj_triangulation(kit)
    t3f = T5.tower_faces(3)
    t3 = T5.adj_from_faces(t3f)

    POPS = [
        ('Fritsch', fri_faces, fri,
         [v for v in sorted(fri) if len(fri[v]) == 5],
         lambda a, tv: G5.exhaustive_colorings(a, tv), 2),
        ('T_3', t3f, t3, [0],
         lambda a, tv: G5.exhaustive_colorings(a, tv), 3),
        ('Errera', err_faces, err, [0, 4],
         lambda a, tv: G5.sampled_colorings(a, tv, 800), 3),
        ('Kittell', kit_faces, kit, [17, 3],
         lambda a, tv: G5.sampled_colorings(a, tv, 1200), 4),
    ]

    results = []
    ladder = {}
    for name, faces, adj, tvs, cfn, depth in POPS:
        stuck = stuck_cases_of(faces, adj, tvs, cfn)
        n_ok = 0
        min_supports = Counter()
        overall_min = None
        for tv, c in stuck:
            ex, ms = gate_census(adj, tv, c)
            if ex:
                n_ok += 1
                min_supports[ms] += 1
                if overall_min is None or ms < overall_min:
                    overall_min = ms
        ladder[name] = (depth, overall_min, n_ok, len(stuck))
        print(f"\n  {name} (depth {depth}): stuck={len(stuck)} "
              f"gate-exists={n_ok}/{len(stuck)} "
              f"min-support dist={dict(sorted(min_supports.items()))} "
              f"overall min={overall_min}")
        results.append((name, n_ok, len(stuck)))

    t1 = (ladder['Fritsch'][2] == ladder['Fritsch'][3] == 144
          and ladder['Fritsch'][1] == 1)
    t2 = ladder['T_3'][2] == ladder['T_3'][3] and ladder['T_3'][3] > 0
    t3_ = ladder['Errera'][2] == ladder['Errera'][3] and ladder['Errera'][3] > 0
    t4 = ladder['Kittell'][2] == ladder['Kittell'][3] and ladder['Kittell'][3] > 0
    # B2 ladder
    t5 = (ladder['Fritsch'][1] == 1
          and (ladder['T_3'][1] or 0) >= 2 and (ladder['Errera'][1] or 0) >= 2
          and (ladder['Kittell'][1] or 0) >= 3)
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Fritsch replication "
          f"(144/144, min 1)")
    print(f"  [{'PASS' if t2 else 'FAIL'}] 2. B1 on T_3 (exhaustive)")
    print(f"  [{'PASS' if t3_ else 'FAIL'}] 3. B1 on Errera")
    print(f"  [{'PASS' if t4 else 'FAIL'}] 4. B1 on Kittell")
    print(f"  [{'PASS' if t5 else 'FAIL'}] 5. B2 support ladder "
          f"(1 / >=2 / >=2 / >=3): "
          f"{[(n, ladder[n][1]) for n in ('Fritsch', 'T_3', 'Errera', 'Kittell')]}")

    res = [t1, t2, t3_, t4, t5]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5524 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(res, 1):
        if not r:
            print(f"  Test {i}: FAIL")
