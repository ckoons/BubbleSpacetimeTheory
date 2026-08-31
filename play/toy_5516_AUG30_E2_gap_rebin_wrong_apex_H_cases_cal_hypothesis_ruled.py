#!/usr/bin/env python3
"""
Toy 5516 — E2 (Round 3): CAL'S GAP-1 HYPOTHESIS ON THE WRONG-APEX H CASES

Cal SS783 F1: K1832 v0.3 carries BOTH "the fan-forcing half of Section 3 is
sound" (Lyra 3.1) AND Toy 5509's P2(i) refutation (2487/4242 wrong-apex
tau=6-in-H) — unreconciled. Cal's hypothesis, pre-registered: Lyra's
eliminations silently import Corollary 1 (gap-2 layout), whose Jordan curve
closes through v and is unproven in H; therefore **wrong-apex tau=6-in-H
cases should be gap-1** (or otherwise outside the elimination layout).
Neither claim gets cited until this toy rules.

INSTRUMENT IDENTITY: this toy IMPORTS Toy 5509 (frozen artifact) and re-runs
its exact hunt — same generators, seeds, and tau machinery — so the
population under adjudication is bit-identical to the one that produced
2487/4242.

TESTS (X/Y):
  1. Population reproduced: the wrong-apex count matches Toy 5509's run
     (same coordinates).
  2. CAL'S HYPOTHESIS scored as pre-registered: wrong-apex ==> bridge
     gap = 1 in G's true link cycle. (PASS iff 100% gap-1.)
  3. Full characterization reported: gap distribution, apex-role split
     (adjacent-to-B_far vs adjacent-to-B_near), tau_s distribution.
  4. THE SEAM NAMED (can-fail): in 100% of wrong-apex cases the pair
     (r, c(apex)) is STRICT in H pre-swap — i.e., Lyra's elimination
     derives the strictness correctly, and what fails is the CONTRADICTION
     step (Lemma 3's bound, false in H). If test 4 passes and test 2
     fails, the reconciliation is: her 3.1 fan-forcing is sound only
     through its strictness half; the elimination's final step imported
     Lemma 3 across the population boundary — same disease, fourth site.

Elie, 2026-08-30. Millennium week, 4-Color round 3. 4 tests.
"""

import importlib.util
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = importlib.util.spec_from_file_location(
    "toy5509", os.path.join(
        HERE, "toy_5509_AUG30_P2_H_repair_pipeline_fan_forced_swap_closes"
              "_plus_deg4_hole_probe.py"))
T9 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(T9)


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5516 — E2: gap re-bin of the wrong-apex tau=6-in-H cases")
    print("=" * 70)

    pops = T9.build_populations()
    print(f"\n  ... re-running Toy 5509's hunt ({len(pops)} graphs x 5 "
          f"apexes) for instrument identity")
    cases, h_valid = T9.hunt_tau6_in_H(pops)
    wrong = []
    mid = 0
    for name, faces, adjG, adjH, diags, v, cyc, apex, col in cases:
        info = T9.structure_from_link(cyc, col)
        if info is None:
            wrong.append((name, adjH, v, cyc, apex, col, None))
            continue
        if info.get('gap') == 2 and apex == info['mid_pos']:
            mid += 1
        else:
            wrong.append((name, adjH, v, cyc, apex, col, info))
    print(f"  cases: {len(cases)}  apex=middle: {mid}  wrong-apex/other: "
          f"{len(wrong)}")

    # Test 1
    t1 = (len(cases) == 4242 and len(wrong) == 2487)
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Population reproduced "
          f"({len(cases)} cases, {len(wrong)} wrong-apex; Toy 5509: "
          f"4242 / 2487)")

    # Tests 2-4
    gap_dist = Counter()
    role_dist = Counter()
    taus_dist = Counter()
    strict_apex = 0
    n_char = 0
    for name, adjH, v, cyc, apex, col, info in wrong:
        if info is None:
            gap_dist['no-structure'] += 1
            continue
        n_char += 1
        gap_dist[info['gap']] += 1
        if info['gap'] == 2:
            # apex role: which non-middle position is it
            bp = info['bp']
            d_far = [min((apex - p) % 5, (p - apex) % 5) for p in bp]
            role = ('adj-to-one-bridge' if 1 in d_far else 'middle?')
            # more precisely: the two non-middle positions are each adjacent
            # to exactly one bridge; classify by whether apex is link-adjacent
            # to the bridge at cyclic distance 2 from the OTHER singleton
            role_dist[tuple(sorted(d_far))] += 1
        import itertools as it
        ts = sum(1 for a, b in it.combinations(range(4), 2)
                 if T9.is_strict_link(adjH, col, cyc, a, b))
        taus_dist[ts] += 1
        r = info['r']
        x = col[cyc[apex]]
        if T9.is_strict_link(adjH, col, cyc, r, x):
            strict_apex += 1

    print("\n" + "=" * 70)
    print("Characterization of the wrong-apex population")
    print("=" * 70)
    print(f"\n  bridge gap distribution (TRUE G-link cycle): {dict(gap_dist)}")
    print(f"  apex distance-to-bridges profile: {dict(role_dist)}")
    print(f"  tau_s-in-H distribution: {dict(sorted(taus_dist.items()))}")
    print(f"  (r, c(apex)) strict in H pre-swap: {strict_apex}/{n_char}")

    n_gap1 = gap_dist.get(1, 0)
    t2 = n_char > 0 and n_gap1 == n_char
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. CAL'S HYPOTHESIS: wrong-apex "
          f"==> gap-1 ({n_gap1}/{n_char} gap-1)")
    if not t2 and gap_dist.get(2, 0) == n_char:
        print("      RULING: REFUTED — every wrong-apex case is gap-2, fully "
              "inside the elimination layout. The seam is not the layout.")
    t3 = n_char > 0
    print(f"  [{'PASS' if t3 else 'FAIL'}] 3. Characterization computed")
    t4 = n_char > 0 and strict_apex == n_char
    print(f"  [{'PASS' if t4 else 'FAIL'}] 4. Seam: (r, c(apex)) strict yet "
          f"tau=6 — Lyra's strictness half holds, the Lemma-3 contradiction "
          f"step is what fails in H")

    results = [t1, t2, t3, t4]
    passed = sum(results)
    print(f"\n{'=' * 70}")
    print(f"Toy 5516 -- SCORE: {passed}/{len(results)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(results, 1):
        if not r:
            print(f"  Test {i}: FAIL")
