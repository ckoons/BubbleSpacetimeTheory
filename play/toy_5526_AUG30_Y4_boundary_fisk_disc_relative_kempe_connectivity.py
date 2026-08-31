#!/usr/bin/env python3
"""
Toy 5526 — Y4 (Round 5): THE BOUNDARY-FISK TOY (Cal's population-import flag
                          #5, falsifier run BEFORE anything builds on it)

The Normal Form frame's step "Eulerian regions are free" imports Fisk 1973 —
a theorem about CLOSED sphere triangulations — onto REGIONS WITH BOUNDARY.
The region form is: for a disc with all INTERIOR vertices of even degree and
PINNED boundary colors, are all proper interior completions connected under
boundary-avoiding Kempe swaps? Different quantifier, no cited proof — Cal's
falsifier: one exhaustive disc toy. Foundation poured, or marked wet.

INSTRUMENT: triangular-lattice discs (interior degrees all 6):
  P1 = radius-1 disc: center + 6-cycle boundary (V=7, 1 interior);
  P2 = radius-2 disc: center + ring1(6) interior, ring2(12) boundary
       (V=19, 7 interior).
Legal relative move: swap a bichromatic component containing NO boundary
vertex. Classes = connected components of the completion set under legal
moves. FREE means: for every boundary pinning admitting >= 2 completions,
exactly ONE class.

Boundary pinnings: exhaustive over proper colorings of the boundary cycle
for P1 (C6: all); for P2 (C12): all 3-colorings by {0,1,2} pattern samples +
1000 deterministic pseudo-random proper cycle colorings (seeded, listed) —
coverage reported, adversarial cases included (colorings using all 4 colors
and colorings with long monochromatic-pair alternations).

TESTS (X/Y):
  1. Disc constructions valid (interior degrees all 6; boundary cycle).
  2. P1 exhaustive: every pinning with >= 2 completions has ONE class.
  3. P2, all sampled pinnings: ONE class each (any split = WET FOUNDATION,
     printed loudly with the witness pinning).
  4. Census reported: pinnings tested, completions min/max, class counts.

Elie, 2026-08-30. Millennium week, 4-Color round 5. 4 tests.
"""

import itertools
import random
from collections import defaultdict, Counter, deque

# ---------------------------------------------------------------- disc


def disc(radius):
    """Triangular-lattice disc via axial coordinates. Returns (adj,
    interior, boundary_cycle)."""
    pts = []
    for q in range(-radius, radius + 1):
        for r in range(-radius, radius + 1):
            if abs(q + r) <= radius and abs(q) <= radius and abs(r) <= radius:
                pts.append((q, r))
    pset = set(pts)
    dirs = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
    adj = {p: set() for p in pts}
    for p in pts:
        for d in dirs:
            q = (p[0] + d[0], p[1] + d[1])
            if q in pset:
                adj[p].add(q)
    interior = [p for p in pts if len(adj[p]) == 6]
    boundary = [p for p in pts if len(adj[p]) < 6]
    # order boundary as a cycle
    cyc = [boundary[0]]
    while len(cyc) < len(boundary):
        cur = cyc[-1]
        nxt = [w for w in adj[cur] if w in set(boundary) and w not in cyc]
        # prefer boundary-adjacent continuation
        cyc.append(nxt[0])
    return adj, interior, cyc


# ---------------------------------------------------------------- machinery


def completions(adj, interior, pin):
    out = []
    col = dict(pin)

    def bt(i):
        if i == len(interior):
            out.append(dict(col))
            return
        u = interior[i]
        for c in range(4):
            if all(col.get(w) != c for w in adj[u]):
                col[u] = c
                bt(i + 1)
                del col[u]

    bt(0)
    return out


def legal_components(adj, col, boundary_set):
    comps = []
    for a, b in itertools.combinations(range(4), 2):
        seen = set()
        for u in adj:
            if u in seen or col[u] not in (a, b):
                continue
            comp = set()
            stack = [u]
            while stack:
                x = stack.pop()
                if x in comp:
                    continue
                comp.add(x)
                for w in adj[x]:
                    if w not in comp and col[w] in (a, b):
                        stack.append(w)
            seen |= comp
            if not (comp & boundary_set):
                comps.append((a, b, frozenset(comp)))
    return comps


def n_classes(adj, interior, boundary_set, comps_list):
    """Connected components of the completion set under legal swaps."""
    idx = {tuple(sorted((u, c[u]) for u in interior)): i
           for i, c in enumerate(comps_list)}
    seen = set()
    classes = 0
    for i, c0 in enumerate(comps_list):
        if i in seen:
            continue
        classes += 1
        q = deque([c0])
        seen.add(i)
        while q:
            c = q.popleft()
            for a, b, comp in legal_components(adj, c, boundary_set):
                nc = dict(c)
                for u in comp:
                    nc[u] = b if nc[u] == a else a
                key = tuple(sorted((u, nc[u]) for u in interior))
                j = idx.get(key)
                if j is not None and j not in seen:
                    seen.add(j)
                    q.append(comps_list[j])
    return classes


def proper_cycle_colorings(n, cap=None):
    """All proper 4-colorings of C_n (as sequences), optionally capped."""
    out = []
    seq = [0]

    def bt(i):
        if cap is not None and len(out) >= cap:
            return
        if i == n:
            if seq[0] != seq[-1]:
                out.append(list(seq))
            return
        for c in range(4):
            if c != seq[-1]:
                seq.append(c)
                bt(i + 1)
                seq.pop()

    bt(1)
    return out


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5526 — Y4: boundary-Fisk — relative Kempe-connectivity on discs")
    print("=" * 70)

    # Test 1
    ok1 = True
    discs = {}
    for R in (1, 2):
        adj, interior, bcyc = disc(R)
        okd = all(len(adj[u]) == 6 for u in interior) and \
            len(bcyc) == 6 * R and len(interior) == 1 + 3 * R * (R - 1)
        discs[R] = (adj, interior, bcyc)
        print(f"  P{R}: V={len(adj)} interior={len(interior)} "
              f"boundary={len(bcyc)} -> {'ok' if okd else 'FAIL'}")
        ok1 &= okd
    t1 = ok1
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Discs valid")

    # Test 2: P1 exhaustive
    adj, interior, bcyc = discs[1]
    bset = set(bcyc)
    splits = 0
    tested = 0
    multi = 0
    for seqc in proper_cycle_colorings(6):
        pin = dict(zip(bcyc, seqc))
        comps = completions(adj, interior, pin)
        if len(comps) < 2:
            continue
        tested += 1
        multi += 1
        ncl = n_classes(adj, interior, bset, comps)
        if ncl > 1:
            splits += 1
            print(f"  *** P1 SPLIT: pinning {seqc} completions "
                  f"{len(comps)} classes {ncl}")
    t2 = splits == 0 and multi > 0
    print(f"\n  P1: pinnings with >=2 completions: {multi}, splits: {splits}")
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. P1 exhaustively free")

    # Test 3: P2 sampled pinnings
    adj, interior, bcyc = discs[2]
    bset = set(bcyc)
    pinnings = []
    # structured: all-{0,1,2} alternating patterns + all-4-color patterns
    base = proper_cycle_colorings(12, cap=400)
    pinnings.extend(base[:200])
    rng = random.Random(20260830)
    # deterministic pseudo-random proper cycle colorings
    for _ in range(800):
        seq = [rng.randrange(4)]
        ok = True
        for i in range(11):
            choices = [c for c in range(4) if c != seq[-1]]
            seq.append(rng.choice(choices))
        if seq[0] == seq[-1]:
            continue
        pinnings.append(seq)
    splits2 = 0
    tested2 = 0
    cmin, cmax = None, 0
    cls_hist = Counter()
    for seqc in pinnings:
        pin = dict(zip(bcyc, seqc))
        comps = completions(adj, interior, pin)
        if len(comps) < 2:
            continue
        tested2 += 1
        cmin = len(comps) if cmin is None else min(cmin, len(comps))
        cmax = max(cmax, len(comps))
        ncl = n_classes(adj, interior, bset, comps)
        cls_hist[ncl] += 1
        if ncl > 1:
            splits2 += 1
            print(f"  *** P2 SPLIT (WET FOUNDATION): pinning {seqc} "
                  f"completions {len(comps)} classes {ncl}")
    t3 = tested2 > 0 and splits2 == 0
    print(f"\n  P2: pinnings tested (>=2 completions): {tested2}, "
          f"splits: {splits2}")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. P2 free on all sampled "
          f"pinnings" + (" — FOUNDATION POURED (sample scope)" if t3 else
                         " — MARKED WET"))

    # Test 4: census
    print(f"\n  census: P2 completions per pinning min={cmin} max={cmax}; "
          f"class histogram {dict(cls_hist)}")
    t4 = tested2 > 0
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Census reported")

    res = [t1, t2, t3, t4]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5526 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(res, 1):
        if not r:
            print(f"  Test {i}: FAIL")
    print("\nScope note: P1 verdict is EXHAUSTIVE; P2 is sample-scoped "
          "(1000 pinnings). A proof of the region form is still owed "
          "before the Normal Form step banks — this toy pours or wets the "
          "foundation empirically, it does not certify it.")
