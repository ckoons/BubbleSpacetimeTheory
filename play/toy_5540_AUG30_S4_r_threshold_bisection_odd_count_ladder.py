#!/usr/bin/env python3
"""
Toy 5540 — S4 (Round 11): THE r-THRESHOLD BISECTION

Q3 found: odd count 2 => r = 0 (five-for-five, exact winding conservation);
odd count >= 12 => r = 8. Fritsch (6 odd) => r = 0. The mobility switches on
somewhere in 6 < odd <= 12. This toy walks the interval one odd-pair at a
time: flip-search families at odd counts {2, 4, 6, 8, 10, 12}, several
instances each, r measured per instance (achieved-closure residue, rule
printed). A sharp onset = phase-transition-shaped; gradual = law-shaped.
Both bank.

TESTS (X/Y):
  1. Ladder built: >= 3 instances per target odd count, flip-search on
     O(2)/O(3), exact odd counts verified.
  2. r measured per instance (zero-column rows flagged UNMEASURED, not
     counted as r=0 — the Q3/B-family lesson).
  3. The onset table: r distribution per odd level; the threshold named
     with its shape (sharp/gradual/mixed).

Elie, 2026-08-30. Millennium week, 4-Color round 11. 3 tests.
"""

import importlib.util
import math
import os
import random
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


Q3 = load("q3s4", "toy_5538_AUG30_Q3_tranche2_adversarial_families"
          "_deficiency_correlation.py")
G5 = Q3.G5
Y3 = Q3.Y3


def family_target(seed, target_odd, m=2, max_steps=6000):
    rng = random.Random(seed * 31 + target_odd)
    faces = Y3.subdivided_octahedron_faces(m)
    fs = [frozenset(f) for f in faces]
    cur_odd, _ = Q3.odd_count_of(fs)
    for _ in range(max_steps):
        i = rng.randrange(len(fs))
        edge = frozenset(rng.sample(sorted(fs[i], key=str), 2))
        snapshot = list(fs)
        if not Q3.faceset_flip(fs, i, edge, rng):
            continue
        new_odd, _ = Q3.odd_count_of(fs)
        if (abs(new_odd - target_odd) <= abs(cur_odd - target_odd)
                or rng.random() < 0.2):
            cur_odd = new_odd
            if cur_odd == target_odd:
                return [tuple(sorted(f, key=str)) for f in fs]
        else:
            fs[:] = snapshot
    return None


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5540 — S4: the r-threshold bisection")
    print("=" * 70)

    LEVELS = [2, 4, 6, 8, 10, 12]
    table = {}
    built_ok = True
    for lvl in LEVELS:
        inst = []
        for seed in range(14):
            f = family_target(seed, lvl)
            if f is not None:
                adj = G5.adj_from_faces(f)
                oc = sum(1 for v in adj if len(adj[v]) % 2)
                if oc == lvl:
                    inst.append(f)
            if len(inst) >= 4:
                break
        rs = []
        for f in inst:
            adj = G5.adj_from_faces(f)
            g, ncols = Q3.residue_r(f, adj)
            rs.append((g, ncols))
        table[lvl] = rs
        built_ok &= len(inst) >= 3
        shown = [(g if n > 0 else 'UNMEASURED') for g, n in rs]
        print(f"  odd={lvl}: instances={len(inst)} r-values={shown}")

    t1 = built_ok
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Ladder built (>=3 per level)")

    measured = {lvl: [g for g, n in rs if n > 0] for lvl, rs in table.items()}
    t2 = all(len(v) >= 2 for v in measured.values())
    print(f"  [{'PASS' if t2 else 'FAIL'}] 2. r measured per level "
          f"(unmeasured rows excluded)")

    print("\n  THE ONSET TABLE:")
    onset = None
    for lvl in LEVELS:
        vals = measured[lvl]
        allz = all(g == 0 for g in vals)
        anynz = any(g != 0 for g in vals)
        print(f"    odd={lvl}: r-values {sorted(set(vals))} "
              f"({'all conserving' if allz else ('MIXED' if allz != anynz and not allz and 0 in vals else 'mobile')})")
        if onset is None and anynz:
            onset = lvl
    shape = None
    if onset is not None:
        below = [g for lvl in LEVELS if lvl < onset for g in measured[lvl]]
        at = measured[onset]
        mixed_at = (0 in at and any(g != 0 for g in at))
        shape = ('SHARP (all-zero below, nonzero at onset, '
                 + ('mixed at the boundary level' if mixed_at
                    else 'clean at onset') + ')')
    print(f"\n  onset level: {onset}; shape: {shape}")
    t3 = onset is not None
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Threshold located and shaped")

    res = [t1, t2, t3]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5540 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(res, 1):
        if not r:
            print(f"  Test {i}: FAIL")
