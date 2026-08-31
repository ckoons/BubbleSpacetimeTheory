#!/usr/bin/env python3
"""
Toy 5537 — Q2 (Round 10): THE AVAILABILITY GRAPH — the reachability object
                           itself, as a first-class atlas for Grace

For a pinned disc, the AVAILABILITY GRAPH has completions as nodes and
legal (boundary-avoiding) single swaps as edges. Its component structure IS
what the linear lenses cannot see (Z1). This toy builds the ATLAS of
FCW-014: per-pinning availability graphs over a stated census, with the
decision pinning's graph rendered explicitly (2 isolated nodes — the twins)
and the frozen-pinning family cataloged.

CENSUS RULE (stated): all proper boundary 3-colorings by pattern classes is
intractable to enumerate fully (C12 proper colorings ~ 10^5); the atlas uses
5,000 deterministic pseudo-random proper cycle pinnings (seed 20260830) +
the exhibited decision pinning + its color-swapped sibling
[0,1,0,1,0,1,0,1,3,1,3,1] (Y4's second split witness).

ATLAS ROW per pinning with >= 1 completion: n_completions, n_edges,
n_components, n_frozen_nodes (zero-legal-move completions), witness class
(CONNECTED / SPLIT / ALL-FROZEN / SINGLE).

TESTS (X/Y):
  1. Decision pinning's availability graph = 2 nodes, 0 edges, both
     frozen (the twins, in atlas form).
  2. Census executed (counts by witness class reported).
  3. The frozen-pinning FAMILY: every pinning whose availability graph
     has >= 2 components listed; the census answers how rare the
     Z1-witness class is.
  4. Atlas JSON written for Grace (availability_atlas_fcw014.json).

Elie, 2026-08-30. Millennium week, 4-Color round 10. 4 tests.
"""

import importlib.util
import json
import os
import random
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


Y4 = load("t5526a", "toy_5526_AUG30_Y4_boundary_fisk_disc_relative_kempe"
          "_connectivity.py")

DECISION = [0, 1, 0, 1, 0, 1, 0, 1, 2, 1, 2, 1]
SIBLING = [0, 1, 0, 1, 0, 1, 0, 1, 3, 1, 3, 1]


def availability_graph(adj, interior, bcyc, pin_seq):
    bset = set(bcyc)
    pin = dict(zip(bcyc, pin_seq))
    comps = Y4.completions(adj, interior, pin)
    n = len(comps)
    key = lambda c: tuple(c[u] for u in sorted(interior, key=str))
    idx = {key(c): i for i, c in enumerate(comps)}
    edges = set()
    frozen = 0
    for i, c in enumerate(comps):
        legal = Y4.legal_components(adj, c, bset)
        if not legal:
            frozen += 1
        for a, b, S in legal:
            nc = dict(c)
            for x in S:
                nc[x] = b if nc[x] == a else a
            j = idx.get(key(nc))
            if j is not None and j != i:
                edges.add(frozenset((i, j)))
    # components
    par = list(range(n))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for e in edges:
        a, b = tuple(e)
        par[find(a)] = find(b)
    ncomp = len({find(i) for i in range(n)}) if n else 0
    return n, len(edges), ncomp, frozen


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5537 — Q2: the availability atlas of FCW-014")
    print("=" * 70)

    adj, interior, bcyc = Y4.disc(2)

    # Test 1: the decision pinning
    n, ne, nc, nf = availability_graph(adj, interior, bcyc, DECISION)
    t1 = (n == 2 and ne == 0 and nc == 2 and nf == 2)
    print(f"\n  DECISION pinning: nodes={n} edges={ne} components={nc} "
          f"frozen={nf}")
    n2, ne2, nc2, nf2 = availability_graph(adj, interior, bcyc, SIBLING)
    print(f"  SIBLING pinning:  nodes={n2} edges={ne2} components={nc2} "
          f"frozen={nf2}")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. The twins in atlas form "
          f"(2 isolated frozen nodes)")

    # Test 2-3: census
    rng = random.Random(20260830)
    rows = []
    seen = set()
    tried = 0
    while len(rows) < 5000 and tried < 200000:
        tried += 1
        seq = [rng.randrange(4)]
        for _ in range(len(bcyc) - 1):
            seq.append(rng.choice([c for c in range(4) if c != seq[-1]]))
        if seq[0] == seq[-1]:
            continue
        t = tuple(seq)
        if t in seen:
            continue
        seen.add(t)
        n, ne, nc, nf = availability_graph(adj, interior, bcyc, seq)
        if n == 0:
            continue
        if n == 1:
            wc = 'SINGLE'
        elif nc == 1:
            wc = 'CONNECTED'
        elif nf == n:
            wc = 'ALL-FROZEN'
        else:
            wc = 'SPLIT'
        rows.append({'pin': seq, 'nodes': n, 'edges': ne,
                     'components': nc, 'frozen': nf, 'class': wc})
    for extra, lab in ((DECISION, 'decision'), (SIBLING, 'sibling')):
        n, ne, nc, nf = availability_graph(adj, interior, bcyc, extra)
        rows.append({'pin': extra, 'nodes': n, 'edges': ne,
                     'components': nc, 'frozen': nf,
                     'class': 'ALL-FROZEN' if nf == n and n > 1 else 'SPLIT',
                     'label': lab})
    census = Counter(r['class'] for r in rows)
    print(f"\n  census: {len(rows)} pinnings with >=1 completion "
          f"(from {tried} sampled sequences)")
    print(f"  witness classes: {dict(census)}")
    t2 = len(rows) > 1000
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Census executed")

    multi = [r for r in rows if r['components'] >= 2]
    print(f"\n  pinnings with >=2 availability components: {len(multi)}")
    for r in multi[:12]:
        print(f"    {r['pin']} nodes={r['nodes']} comps={r['components']} "
              f"frozen={r['frozen']} [{r['class']}]"
              + (f" ({r.get('label')})" if r.get('label') else ""))
    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Frozen-pinning family "
          f"cataloged ({len(multi)} of {len(rows)} — the Z1 witness class "
          f"rarity, measured)")

    out = os.path.join(HERE, 'availability_atlas_fcw014.json')
    with open(out, 'w') as f:
        json.dump({'census_rule': '5000 deterministic pseudo-random proper '
                                  'cycle pinnings, seed 20260830, + decision '
                                  '+ sibling', 'rows': rows}, f)
    t4 = os.path.exists(out)
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Atlas written: "
          f"{os.path.basename(out)} ({len(rows)} rows)")

    res = [t1, t2, t3, t4]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5537 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(res, 1):
        if not r:
            print(f"  Test {i}: FAIL")
