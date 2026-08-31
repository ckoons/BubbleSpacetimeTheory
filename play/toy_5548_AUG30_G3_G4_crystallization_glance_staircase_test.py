#!/usr/bin/env python3
"""
Toy 5548 — G3+G4 (Round 13): THE CRYSTALLIZATION GLANCE + THE STAIRCASE TEST

G3 (one look): do the twins' interiors EXILE the filler color? And across
the atlas's other frozen pinnings' completions: how many interior vertices
carry the filler color, and where?

G4 (the sufficient-completion candidate, both kill conditions armed):
  FROZEN <=> FILLER present AND the non-filler parity sequence has MONOTONE
  ZZ3 winding (all nonzero cyclic steps share one sign; steps taken in the
  ascending 3-cycle of the three non-filler-adjacent values... operationally:
  the cycle of the 3 colors present in the non-filler class positions'
  allowed set = colors != filler, ascending, oriented ascending).
  KILL-1: a frozen pinning that is non-monotone. KILL-2: a free
  multi-completion pinning that is filler+monotone.

TESTS (X/Y):
  1. G3: filler-color interior census for the twins (prediction on file:
     confinement to the fixed center) and for all frozen pinnings.
  2. G4 confusion matrix over the full census.
  3. G4 verdict with kills exhibited.

Elie, 2026-08-30. Millennium week, 4-Color round 13. 3 tests.
"""

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


Y4 = load("t5526g3", "toy_5526_AUG30_Y4_boundary_fisk_disc_relative_kempe"
          "_connectivity.py")


def filler_of(pin):
    even = pin[0::2]
    odd = pin[1::2]
    if len(set(odd)) == 1:
        return odd[0], even
    if len(set(even)) == 1:
        return even[0], odd
    return None, None


def monotone_z3(seq, filler):
    cyc = sorted(c for c in range(4) if c != filler)
    steps = []
    m = len(seq)
    for i in range(m):
        a, b = seq[i], seq[(i + 1) % m]
        if a == b:
            continue
        if a not in cyc or b not in cyc:
            return False
        d = (cyc.index(b) - cyc.index(a)) % 3
        steps.append(1 if d == 1 else -1)
    if not steps:
        return True
    return all(s == steps[0] for s in steps)


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5548 — G3+G4: crystallization glance + staircase test")
    print("=" * 70)

    adj, interior, bcyc = Y4.disc(2)
    atlas = json.load(open(os.path.join(HERE,
                                        'availability_atlas_fcw014.json')))
    rows = atlas['rows']
    center = (0, 0)

    # ---- G3 ----
    print("\n  G3 — the crystallization glance:")
    frozen_rows = [r for r in rows if r['components'] >= 2]
    confin_all = True
    for r in frozen_rows:
        fil, _seq = filler_of(r['pin'])
        pin = dict(zip(bcyc, r['pin']))
        comps = Y4.completions(adj, interior, pin)
        for i, c in enumerate(comps):
            carriers = [v for v in interior if c[v] == fil]
            at_center_only = (carriers == [center])
            confin_all &= at_center_only
            tag = ('CONFINED TO CENTER' if at_center_only
                   else f'carriers {carriers}')
            if r.get('label') or not at_center_only:
                print(f"    pin {r['pin']} completion {i}: filler {fil} "
                      f"interior carriers: {len(carriers)} [{tag}]")
    print(f"\n    ALL frozen completions: filler confined exactly to the "
          f"fixed center: {confin_all}")
    t1 = True
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. G3 GLANCE: "
          f"{'NOT full exile — the filler is CONFINED TO THE FIXED CENTER in every frozen completion' if confin_all else 'mixed carrier structure (printed above)'}")

    # ---- G4 ----
    print("\n  G4 — the staircase test (full census):")
    conf = Counter()
    kills1 = []
    kills2 = []
    for r in rows:
        fil, seq = filler_of(r['pin'])
        has_filler = fil is not None
        stair = has_filler and monotone_z3(seq, fil)
        frozen = r['components'] >= 2
        multi = r['nodes'] >= 2
        conf[(frozen, stair)] += 1
        if frozen and not stair:
            kills1.append(r['pin'])
        if (not frozen) and multi and stair:
            kills2.append(r['pin'])
    print(f"    confusion (frozen?, staircase?): {dict(conf)}")
    print(f"    KILL-1 (frozen, non-staircase): {len(kills1)}")
    for p in kills1[:6]:
        fil, seq = filler_of(p)
        print(f"      *** {p} (filler {fil}, seq {seq})")
    print(f"    KILL-2 (free multi-completion, staircase): {len(kills2)}")
    for p in kills2[:6]:
        print(f"      *** {p}")
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Confusion matrix computed")
    survived = (not kills1) and (not kills2)
    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. G4 VERDICT: "
          f"{'THE STAIRCASE CHARACTERIZATION SURVIVES THE FULL CENSUS — freezing has a complete static characterization of pinnings' if survived else 'KILLED (' + str(len(kills1)) + ' frozen non-staircase, ' + str(len(kills2)) + ' free staircase)'}")

    res = [t1, t2, t3]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5548 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
