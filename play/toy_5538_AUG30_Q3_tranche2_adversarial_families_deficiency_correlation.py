#!/usr/bin/env python3
"""
Toy 5538 — Q3 (Round 10): TRANCHE 2 — Cal's R1 adversarial families +
                           the deficiency correlation table

Cal SS789 R1 named three law-targeting families tranche 2 owes:
  A. NEAR-EULERIAN, single odd PAIR (exactly 2 odd vertices): built by
     flip-search on subdivided octahedra minimizing odd count to 2
     (handshake forbids 1; Fisk's theorem says the pair is non-adjacent —
     free positive control on the construction).
  B. HIGH RADIUS-3 APEX CHARGE AT LOW GLOBAL DENSITY: flips restricted to
     within distance 2 of a target vertex on O(3) — odd cluster local,
     density global-low. The discriminator the dilution test never ran.
  C. SIGN-BALANCED / r = 0 SCREEN: measure the degree-mobility residue r
     on A, B, and a tranche-1 subsample; catalog non-Eulerian members
     with r = 0 (Fritsch's mechanism, hunted).

Plus THE DEFICIENCY CORRELATION TABLE: deficiency (dim E - dim W) against
odd count, V, and family, on tranche-1 leaving-home rows + tranche 2 —
the spanning profile's first law-shaped read.

TESTS (X/Y):
  1. Family A built: >= 4 instances with EXACTLY 2 odd vertices; Fisk
     non-adjacency control passes on every instance.
  2. Family B built: >= 4 instances; locality verified (odd vertices
     within distance 3 of target; global density below 0.25).
  3. Family C screen run: r measured per instance; non-Eulerian r=0
     members counted (either count is data).
  4. Deficiency correlation table computed; rank-correlation of
     deficiency vs odd count and vs V reported.
  5. Density-law low-end probe: family A's deg-5 stuck cases (if any)
     at depth <= 2 (the law's prediction at density ~0.1) — bounded,
     status carried.

Elie, 2026-08-30. Millennium week, 4-Color round 10. 5 tests.
"""

import importlib.util
import itertools
import json
import math
import os
import random
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


G5 = load("g5512x3", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")
T5 = load("t5515x3", "toy_5515_AUG30_E1_kring_tower_family_rescue_depth_vs_k"
          "_cal_F0_absorbed.py")
H8 = load("t5518x3", "toy_5518_AUG30_E4_heawood_gf3_instrument_rank_coset"
          "_stuck_separation.py")
Y3 = load("t5525x3", "toy_5525_AUG30_Y3_dilution_test_akempic_knot_in"
          "_eulerian_bulk.py")
Y1 = load("t5527x3", "toy_5527_AUG30_Y1_snf_engine_charge_lattice_invariant"
          "_factors.py")


def faceset_flip(faceset, i, edge, rng):
    js = [j for j, f in enumerate(faceset) if edge < f and j != i]
    if len(js) != 1:
        return False
    j = js[0]
    a, b = sorted(edge, key=str)
    c = next(iter(faceset[i] - edge))
    d = next(iter(faceset[j] - edge))
    if c == d:
        return False
    if any(frozenset((c, d)) < f for f in faceset):
        return False
    dega = sum(1 for f in faceset if a in f)
    degb = sum(1 for f in faceset if b in f)
    if dega <= 3 or degb <= 3:
        return False
    faceset[i] = frozenset((a, c, d))
    faceset[j] = frozenset((b, c, d))
    return True


def odd_count_of(faceset):
    deg = Counter()
    for f in faceset:
        for v in f:
            deg[v] += 1
    return sum(1 for v in deg if deg[v] % 2), deg


def family_A(seed, max_steps=4000):
    """Flip-search on O(2) targeting exactly 2 odd vertices."""
    rng = random.Random(seed)
    faces = Y3.subdivided_octahedron_faces(2)
    fs = [frozenset(f) for f in faces]
    # random walk with greedy acceptance toward odd-count 2
    best = None
    cur_odd, _ = odd_count_of(fs)
    for step in range(max_steps):
        i = rng.randrange(len(fs))
        edge = frozenset(rng.sample(sorted(fs[i], key=str), 2))
        snapshot = list(fs)
        if not faceset_flip(fs, i, edge, rng):
            continue
        new_odd, _ = odd_count_of(fs)
        if new_odd <= cur_odd or rng.random() < 0.25:
            cur_odd = new_odd
            if cur_odd == 2:
                return [tuple(sorted(f, key=str)) for f in fs]
        else:
            fs[:] = snapshot
    return None


def family_B(seed, m=3):
    """Local flips near a target vertex on O(m)."""
    rng = random.Random(seed)
    faces = Y3.subdivided_octahedron_faces(m)
    fs = [frozenset(f) for f in faces]
    adj = G5.adj_from_faces([tuple(sorted(f, key=str)) for f in fs])
    target = sorted(adj, key=str)[len(adj) // 2]
    # distance map
    dist = {target: 0}
    q = deque([target])
    while q:
        u = q.popleft()
        for w in adj[u]:
            if w not in dist:
                dist[w] = dist[u] + 1
                q.append(w)
    near = {v for v, d in dist.items() if d <= 2}
    for _ in range(60):
        cand = [i for i, f in enumerate(fs) if all(v in near for v in f)]
        if not cand:
            break
        i = rng.choice(cand)
        edge = frozenset(rng.sample(sorted(fs[i], key=str), 2))
        faceset_flip(fs, i, edge, rng)
    return [tuple(sorted(f, key=str)) for f in fs], target


def residue_r(faces, adj):
    """gcd |Delta(Sum omega)| over achieved columns (sampled closure)."""
    vs = sorted(adj, key=str)
    of = H8.orient_faces([tuple(f) for f in faces])
    seeds = []
    seen = set()
    for s in range(80):
        rng = random.Random(s)
        order = list(vs)
        rng.shuffle(order)
        c = G5.greedy_4color(adj, order)
        if c is None:
            continue
        k = tuple(c[u] for u in vs)
        if k in seen:
            continue
        seen.add(k)
        seeds.append(c)
    pop, _cl = Y1.kempe_closure(adj, seeds[:25], 300)
    cols, _o, _p = Y1.build_columns(of, adj, pop, vs)
    g = 0
    for col in cols:
        g = math.gcd(g, abs(sum(col)))
    return g, len(cols)


def deficiency_of(faces, adj):
    of = H8.orient_faces([tuple(f) for f in faces])
    vs = sorted(adj, key=str)
    seeds = []
    seen = set()
    for s in range(60):
        rng = random.Random(s)
        order = list(vs)
        rng.shuffle(order)
        c = G5.greedy_4color(adj, order)
        if c is None:
            continue
        k = tuple(c[u] for u in vs)
        if k in seen:
            continue
        seen.add(k)
        seeds.append(c)
    pop, _cl = Y1.kempe_closure(adj, seeds[:20], 250)
    inds = set()
    for c in pop:
        for a, b in itertools.combinations(range(4), 2):
            done = set()
            for u in adj:
                if u in done or c[u] not in (a, b):
                    continue
                S = G5.kempe_chain(adj, c, u, a, b)
                done |= S
                ind = tuple(1 if 0 < sum(1 for x in f if x in S) < 3 else 0
                            for f in of)
                if any(ind):
                    inds.add(ind)
    basis = []
    for v in inds:
        v = list(v)
        for bb in basis:
            piv = next(i for i, x in enumerate(bb) if x)
            if v[piv]:
                v = [x ^ y for x, y in zip(v, bb)]
        if any(v):
            basis.append(v)
    return (len(of) - 1) - len(basis)


def rankcorr(xs, ys):
    def ranks(a):
        order = sorted(range(len(a)), key=lambda i: a[i])
        rk = [0] * len(a)
        for pos, i in enumerate(order):
            rk[i] = pos
        return rk
    rx, ry = ranks(xs), ranks(ys)
    n = len(xs)
    if n < 3:
        return 0.0
    d2 = sum((a - b) ** 2 for a, b in zip(rx, ry))
    return 1 - 6 * d2 / (n * (n * n - 1))


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5538 — Q3: tranche 2 adversarial families + deficiency table")
    print("=" * 70)

    # Family A
    print("\n  Family A (single odd pair):")
    famA = []
    for seed in range(12):
        r = family_A(seed)
        if r is not None:
            famA.append((f'A_s{seed}', r))
        if len(famA) >= 5:
            break
    fisk_ok = True
    for name, faces in famA:
        adj = G5.adj_from_faces(faces)
        oc, deg = odd_count_of([frozenset(f) for f in faces])
        odds = [v for v in adj if len(adj[v]) % 2]
        adjacent = len(odds) == 2 and odds[1] in adj[odds[0]]
        fisk_ok &= (oc == 2 and not adjacent)
        print(f"    {name}: V={len(adj)} odd={oc} "
              f"pair-adjacent={adjacent} (Fisk forbids)")
    t1 = len(famA) >= 4 and fisk_ok
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Family A: {len(famA)} "
          f"instances, exactly-2-odd, Fisk non-adjacency holds")

    # Family B
    print("\n  Family B (local odd cluster, low density):")
    famB = []
    for seed in range(8):
        faces, target = family_B(seed)
        adj = G5.adj_from_faces(faces)
        odds = [v for v in adj if len(adj[v]) % 2]
        if not odds:
            continue
        dist = {target: 0}
        q = deque([target])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    q.append(w)
        local = all(dist.get(v, 99) <= 3 for v in odds)
        dens = len(odds) / len(adj)
        famB.append((f'B_s{seed}', faces, local, dens, len(odds)))
        print(f"    B_s{seed}: V={len(adj)} odd={len(odds)} local(<=3)="
              f"{local} density={dens:.2f}")
        if len(famB) >= 5:
            break
    t2 = (len(famB) >= 4
          and all(loc and d < 0.25 for _n, _f, loc, d, _o in famB))
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Family B: local cluster + "
          f"low density verified")

    # Family C screen
    print("\n  Family C (r-screen):")
    r0_noneuler = 0
    screened = 0
    for name, faces in famA + [(n, f) for n, f, _l, _d, _o in famB]:
        adj = G5.adj_from_faces(faces)
        oc = sum(1 for v in adj if len(adj[v]) % 2)
        g, ncols = residue_r(faces, adj)
        screened += 1
        tag = ''
        if oc > 0 and g == 0 and ncols > 0:
            r0_noneuler += 1
            tag = '  *** r=0 NON-EULERIAN (Fritsch mechanism candidate)'
        print(f"    {name}: odd={oc} r={g} (cols {ncols}){tag}")
    t3 = screened >= 8
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. r-screen on {screened} "
          f"instances; non-Eulerian r=0 members: {r0_noneuler}")

    # Deficiency correlation
    print("\n  Deficiency correlation (tranche-1 leaving-home + tranche 2):")
    rows = []
    tr1 = os.path.join(HERE, 'harvest_tranche1_pass1.json')
    if os.path.exists(tr1):
        data = json.load(open(tr1))
        for name, r in data.items():
            if r['home'] == 'LEAVING-HOME':
                rows.append((name, r['V'], r['odd'], r['deficiency']))
    for name, faces in famA:
        adj = G5.adj_from_faces(faces)
        rows.append((name, len(adj),
                     sum(1 for v in adj if len(adj[v]) % 2),
                     deficiency_of(faces, adj)))
    for name, faces, _l, _d, _o in famB:
        adj = G5.adj_from_faces(faces)
        rows.append((name, len(adj),
                     sum(1 for v in adj if len(adj[v]) % 2),
                     deficiency_of(faces, adj)))
    Vs = [r[1] for r in rows]
    odds_ = [r[2] for r in rows]
    defs_ = [r[3] for r in rows]
    c_v = rankcorr(Vs, defs_)
    c_o = rankcorr(odds_, defs_)
    print(f"    rows: {len(rows)}  rank-corr(deficiency, V) = {c_v:.2f}  "
          f"rank-corr(deficiency, odd) = {c_o:.2f}")
    t4 = len(rows) > 40
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Correlation table computed "
          f"— deficiency tracks {'SIZE' if abs(c_v) > abs(c_o) else 'ODD COUNT'} "
          f"more strongly on this data")

    # Density-law low-end probe on family A
    print("\n  Density-law low-end probe (family A):")
    stuck_found = 0
    deep = 0
    for name, faces in famA[:3]:
        adj = G5.adj_from_faces(faces)
        deg5 = [v for v in sorted(adj, key=str) if len(adj[v]) == 5]
        for tv in deg5[:2]:
            for c in G5.sampled_colorings(adj, tv, 150):
                if G5.operational_tau(adj, c, tv) != 6:
                    continue
                stuck_found += 1
                d = T5.rescue_depth(adj, c, tv, 4)
                if d is not None and d > 2:
                    deep += 1
                    print(f"    *** {name} v={tv}: depth {d} > 2 at density "
                          f"~0.1 — DENSITY-LAW VIOLATION")
                if stuck_found >= 15:
                    break
            if stuck_found >= 15:
                break
    t5 = deep == 0
    print(f"    tau=6 cases probed: {stuck_found}; depth>2: {deep}")
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. Low-end density-law probe "
          f"(bounded, sampled)")

    res = [t1, t2, t3, t4, t5]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5538 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(res, 1):
        if not r:
            print(f"  Test {i}: FAIL")
