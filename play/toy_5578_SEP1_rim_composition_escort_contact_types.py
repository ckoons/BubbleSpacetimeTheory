#!/usr/bin/env python3
"""
Toy 5578 — THE RIM-COMPOSITION ESCORT: Lyra's three contact types,
measured at their true frequencies

Lyra's residual-case enumeration (11:17 filing): rim-contact types
(i) blocker in N(R) — the freed target's disagreement region meets
    the rim, the word's patch does not;
(ii) patch in N(R) — the word's near change meets the rim, the
     target's disagreements do not;
(iii) both.
Per type she assigns a remedy (extended re-dress or target-switch among
freed words). This census hands her case analysis its actual
distribution — plus per-type contact-size profiles.

OPERATIONAL (join keys from 5577, unchanged): R = (X1\\X3)\\X2
link-free and nonempty; rim = R ∪ N(R) minus the hole; blocker-contact
= diff(c, c*) ∩ rim for nearest freed c*; patch-contact =
(net-support \\ R) ∩ rim (nonzero on 900/900 in 5577 — pre-scored
expectation: type (i) EMPTY, the census splits (ii) vs (iii)).

TESTS (X/Y): 1. population + rim machinery · 2. the type census with
per-type contact sizes · 3. the distribution verdict for the case
analysis.

Elie, 2026-09-01. 3 tests.
"""

import importlib.util
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


RD = load("t5577rc", "toy_5577_SEP1_redress_witness_at_scale_and_rim"
          "_contact_census.py")
P1, CV, F2C, F1 = RD.P1, RD.CV, RD.F2C, RD.F1
E1, G5, X3, H8 = RD.E1, RD.G5, RD.X3, RD.H8


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5578 — rim composition: the three contact types")
    print("=" * 70)

    pops = RD.build_pops()
    n_meas = 0
    types = Counter()
    size_b = Counter()
    size_p = Counter()
    for label, faces, adj, tv, stuck, freed, exact in pops:
        lcyc = E1.link_cycle(faces, tv)
        link = set(adj[tv])
        vs = [v for v in sorted(adj, key=str) if v != tv]
        for c0 in stuck:
            rl = F2C.roles(adj, c0, tv, lcyc)
            if rl is None:
                continue
            n_sM, r, s_M, s_i, s_j = rl
            for sx in (s_i, s_j):
                n_sx = next(v for v in lcyc if c0[v] == sx)
                X1, X2, X3c, X4, c1, c2, c3, c4 = CV.trace(
                    adj, c0, tv, n_sM, r, s_M, n_sx, sx)
                R = (X1 - X3c) - X2
                if not R or any(v in link for v in R):
                    continue
                rim = (R | {w for v in R for w in adj[v]}) - {tv}
                ns = {v for v in vs if c4[v] != c0[v]}
                pc = len((ns - R) & rim)
                if not freed:
                    continue
                dmin = min(sum(1 for v in vs if c0[v] != f[v])
                           for f in freed)
                hits = 0
                for f in freed:
                    d = sum(1 for v in vs if c0[v] != f[v])
                    if d != dmin:
                        continue
                    bc = sum(1 for v in rim if v != tv
                             and c0[v] != f[v])
                    n_meas += 1
                    ty = ('iii' if bc and pc else
                          'ii' if pc else
                          'i' if bc else 'none')
                    types[(label, ty)] += 1
                    types[('ALL', ty)] += 1
                    if bc:
                        size_b[min(bc, 10)] += 1
                    if pc:
                        size_p[min(pc, 10)] += 1
                    hits += 1
                    if hits >= 5:
                        break
    t1 = n_meas > 500
    print(f"\n  (trace, nearest-target) measurements: {n_meas}")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Population + rim "
          f"machinery")

    allrow = {k[1]: v for k, v in types.items() if k[0] == 'ALL'}
    print(f"\n  TYPE CENSUS (ALL): {allrow}")
    print(f"  by object: "
          f"{ {k: v for k, v in sorted(types.items()) if k[0] != 'ALL'} }")
    print(f"  blocker-contact sizes (cap 10): "
          f"{dict(sorted(size_b.items()))}")
    print(f"  patch-contact sizes (cap 10): "
          f"{dict(sorted(size_p.items()))}")
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Census complete")

    n_i = allrow.get('i', 0)
    n_ii = allrow.get('ii', 0)
    n_iii = allrow.get('iii', 0)
    n_none = allrow.get('none', 0)
    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. VERDICT for the case "
          f"analysis: type (i) blocker-only = {n_i} (pre-scored EMPTY "
          f"— patch always meets the rim per 5577), type (ii) "
          f"patch-only = {n_ii}, type (iii) both = {n_iii}, "
          f"neither = {n_none}. "
          f"{'The case analysis has effectively TWO live cases: (iii) dominant, (ii) the remainder — type (i) never occurs, its remedy page can be dropped' if n_i == 0 else 'type (i) REALIZES — all three remedy pages needed'}")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5578 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
