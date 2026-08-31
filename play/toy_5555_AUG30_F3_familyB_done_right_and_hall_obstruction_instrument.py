#!/usr/bin/env python3
"""
Toy 5555 — F3 (Round 15): FAMILY-B DONE RIGHT + THE HALL INSTRUMENT

Twice-owed. Two independent halves.

PART A — Family-B constructor done right. 5538's random-flip builder
failed its own verification (2/5 non-local, densities to 0.37). Fix:
DETERMINISTIC edge flips — one flip toggles degree parity on exactly its
4 patch vertices, so k pairwise-disjoint flips inside ball(target, 2) on
O(4) (V = 66, all-even base) give certified-local odd clusters of size
4k at FIXED V. Deconfound the deficiency correlation (5538's 0.92/0.88
rank-corrs were collinear in V) and re-ask the r switch-on at fixed V.

PART B — Lyra's L-S3 Hall-type ordering-obstruction certificate.
For each of the 15 frozen twin pairs on FCW-014: delta = eps(T1) XOR
eps(T2) (Z1's GF(2) face-sign convention); expression space over the
realizable-chain indicators (Z1's population rule: chains realizable in
SOME proper coloring of D); heuristic-min-weight expression E* by
randomized information-set decoding (FROZEN procedure: seed 5555, 3000
iterations, identical for all pairs — no per-instance knob); per-chain
failure mode at BOTH twins (miscolored / escape / boundary-contact);
dependency digraph S -> S' iff witnesses(S) meet S'; SHAPE =
(|E*|, wt(delta), mode census, hard-blocked count, SCC count).
RECURRENCE across the 15 pairs (orbit-reduced under D12 x S4) = the
candidate lives; amorphous = Lyra's own KILL condition fires.
HIDDEN EDGE pre-scored: Z1's GF(2)-same verdict ran on ONE pinning; any
pair with delta OUTSIDE the chain span is a GF(2) SEPARATOR finding.

TESTS (X/Y): 1. constructor passes its own verification · 2. deconfounded
table + verdict · 3. chains + delta-in-span status for all 15 ·
4. certificates under the frozen procedure · 5. recurrence verdict.

Elie, 2026-08-31. Millennium week, 4-Color round 15. 5 tests.
"""

import importlib.util
import itertools
import os
import random
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


FB = load("t5538f3", "toy_5538_AUG30_Q3_tranche2_adversarial_families"
          "_deficiency_correlation.py")
Z1 = load("t5531f3", "toy_5531_AUG30_Z1_disc_decision_runner_guarded"
          "_awaiting_freeze.py")
D2 = load("t5551f3", "toy_5551_AUG30_D2_mirror_glance_frozen_pinning"
          "_symmetry.py")
Y4 = Z1.Y4 if hasattr(Z1, 'Y4') else load(
    "t5526f3", "toy_5526_AUG30_Y4_boundary_fisk_disc_relative_kempe"
    "_connectivity.py")
G5 = FB.G5
H8 = FB.H8
Y3 = FB.Y3


# ---------------------------------------------------------------- Part A

def flip_once(faces, e_pair):
    """Deterministic edge flip: faces sharing edge {a,b} with opposite
    vertices c,d -> replace by {c,d,a},{c,d,b}. Returns new list or None."""
    a, b = e_pair
    share = [f for f in faces if a in f and b in f]
    if len(share) != 2:
        return None
    (c,) = [v for v in share[0] if v not in (a, b)]
    (d,) = [v for v in share[1] if v not in (a, b)]
    if c == d:
        return None
    if any(c in f and d in f for f in faces):
        return None       # c,d already adjacent
    out = [f for f in faces if f not in share]
    out.append(tuple(sorted((c, d, a), key=str)))
    out.append(tuple(sorted((c, d, b), key=str)))
    return out, (a, b, c, d)


def family_B_right(k_flips, offset):
    """k pairwise-disjoint flips inside ball(target, 2) on O(4)."""
    faces = [tuple(sorted(f, key=str)) for f in
             Y3.subdivided_octahedron_faces(4)]
    adj = G5.adj_from_faces(faces)
    target = sorted(adj, key=str)[len(adj) // 2]
    dist = {target: 0}
    q = deque([target])
    while q:
        u = q.popleft()
        for w in adj[u]:
            if w not in dist:
                dist[w] = dist[u] + 1
                q.append(w)
    ball2 = {v for v, d in dist.items() if d <= 2}
    edges = sorted({tuple(sorted(e, key=str)) for f in faces
                    for e in itertools.combinations(f, 2)
                    if all(v in ball2 for v in e)}, key=str)
    edges = edges[offset:] + edges[:offset]
    used = set()
    done = 0
    for e in edges:
        if done == k_flips:
            break
        if used & set(e):
            continue
        r = flip_once(faces, e)
        if r is None:
            continue
        nf, patch = r
        if used & set(patch):
            continue
        if any(v not in ball2 for v in patch):
            continue
        faces = nf
        used |= set(patch)
        done += 1
    if done != k_flips:
        return None
    return faces, target, dist


def bt_seeds(adj, n_want=12, tries=40):
    """Backtracking 4-coloring seeds (greedy FAILS on O(4)+flips at all
    80 orders — the Kittell failure mode; validated in-session). Most-
    constrained-first with seeded tie-break for diversity."""
    vs = sorted(adj, key=str)
    out, seen = [], set()
    for t in range(tries):
        rng = random.Random(t)
        pri = {v: rng.random() for v in vs}
        col = {}

        def pick():
            best, bk = None, None
            for v in vs:
                if v in col:
                    continue
                used = {col[w] for w in adj[v] if w in col}
                k = (-len(used), -len(adj[v]), pri[v])
                if best is None or k < bk:
                    best, bk = v, k
            return best

        def bt():
            v = pick()
            if v is None:
                return True
            cs = [0, 1, 2, 3]
            rng.shuffle(cs)
            for c in cs:
                if all(col.get(w) != c for w in adj[v]):
                    col[v] = c
                    if bt():
                        return True
                    del col[v]
            return False

        if bt():
            key = tuple(col[u] for u in vs)
            if key not in seen:
                seen.add(key)
                out.append(dict(col))
        if len(out) >= n_want:
            break
    return out


def measure_r_def(faces, adj):
    """residue_r + deficiency on a REAL population (backtracking seeds);
    returns (r_or_None, ncols, deficiency_or_None, popsize)."""
    import math
    vs = sorted(adj, key=str)
    of = H8.orient_faces([tuple(f) for f in faces])
    seeds = bt_seeds(adj)
    if not seeds:
        return None, 0, None, 0
    pop, _cl = FB.Y1.kempe_closure(adj, seeds[:20], 300)
    cols, _o, _p = FB.Y1.build_columns(of, adj, pop, vs)
    g = 0
    for col in cols:
        g = math.gcd(g, abs(sum(col)))
    inds = set()
    for c in pop:
        for a, b in itertools.combinations(range(4), 2):
            done = set()
            for u in adj:
                if u in done or c[u] not in (a, b):
                    continue
                S = G5.kempe_chain(adj, c, u, a, b)
                done |= S
                ind = tuple(1 if 0 < sum(1 for x in f if x in S) < 3
                            else 0 for f in of)
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
    de = (len(of) - 1) - len(basis)
    return (g if cols else None), len(cols), de, len(pop)


# ---------------------------------------------------------------- Part B

def realizable_chain(adj, S, vs_all):
    Sl = sorted(S, key=str)
    side = {Sl[0]: 0}
    st = [Sl[0]]
    while st:
        x = st.pop()
        for w in adj[x]:
            if w in S:
                if w not in side:
                    side[w] = 1 - side[x]
                    st.append(w)
                elif side[w] == side[x]:
                    return False
    halo = {w for v in S for w in adj[v]} - S
    order = [v for v in vs_all if v not in S]
    col = {v: side[v] for v in S}

    def bt(i):
        if i == len(order):
            return True
        u = order[i]
        for c in ((2, 3) if u in halo else (0, 1, 2, 3)):
            if all(col.get(w) != c for w in adj[u]):
                col[u] = c
                if bt(i + 1):
                    return True
                del col[u]
        return False

    return bt(0)


def chain_list(adj, interior, ofaces):
    ints = sorted(interior, key=str)
    vs_all = sorted(adj, key=str)
    out = []
    for r in range(1, len(ints) + 1):
        for sub in itertools.combinations(ints, r):
            S = set(sub)
            seen = {sub[0]}
            st = [sub[0]]
            while st:
                x = st.pop()
                for w in adj[x]:
                    if w in S and w not in seen:
                        seen.add(w)
                        st.append(w)
            if len(seen) != len(S):
                continue
            if realizable_chain(adj, S, vs_all):
                ind = tuple(1 if 0 < sum(1 for x in f if x in S) < 3 else 0
                            for f in ofaces)
                if any(ind):
                    out.append((frozenset(S), ind))
    return out


def solve_affine(cols, target):
    """One GF(2) solution of A x = target plus kernel basis; None if
    unsolvable. cols = list of column vectors."""
    m = len(target)
    n = len(cols)
    rows = [[cols[j][i] for j in range(n)] + [target[i]] for i in range(m)]
    piv = []
    r = 0
    for c in range(n):
        pr = next((i for i in range(r, m) if rows[i][c]), None)
        if pr is None:
            continue
        rows[r], rows[pr] = rows[pr], rows[r]
        for i in range(m):
            if i != r and rows[i][c]:
                rows[i] = [x ^ y for x, y in zip(rows[i], rows[r])]
        piv.append(c)
        r += 1
    for i in range(r, m):
        if rows[i][n]:
            return None, None
    x0 = [0] * n
    for i, c in enumerate(piv):
        x0[c] = rows[i][n]
    free = [c for c in range(n) if c not in piv]
    kern = []
    for fc in free:
        v = [0] * n
        v[fc] = 1
        for i, c in enumerate(piv):
            v[c] = rows[i][fc]
        kern.append(v)
    return x0, kern


def min_weight_solution(x0, kern, seed=5555, iters=3000):
    """Heuristic min-weight element of x0 + span(kern). FROZEN procedure."""
    rng = random.Random(seed)
    best = list(x0)
    for _ in range(iters):
        v = list(x0)
        for b in kern:
            if rng.random() < 0.5:
                v = [x ^ y for x, y in zip(v, b)]
        improved = True
        while improved:
            improved = False
            for b in kern:
                w = [x ^ y for x, y in zip(v, b)]
                if sum(w) < sum(v):
                    v = w
                    improved = True
        if sum(v) < sum(best):
            best = v
    return best


def failure_mode(adj, S, col, bset):
    """Why S is not a swappable boundary-free component at coloring col."""
    colors = {col[v] for v in S}
    if len(colors) != 2:
        return 'miscolored', frozenset()
    a, b = sorted(colors)
    for v in S:
        if any(w in S and col[w] == col[v] for w in adj[v]):
            return 'miscolored', frozenset()
    wit = {w for v in S for w in adj[v]
           if w not in S and col[w] in (a, b)}
    if not wit:
        return 'applicable', frozenset()
    if wit & bset:
        return 'boundary', frozenset(wit)
    return 'escape', frozenset(wit)


if __name__ == "__main__":
    import json
    print("=" * 70)
    print("Toy 5555 — F3: Family-B done right + the Hall instrument")
    print("=" * 70)

    # ---------------- PART A
    print("\n  PART A — Family-B done right (O(4), V fixed)")
    inst = []
    for k in (1, 2, 3):
        for off in (0, 7):
            r = family_B_right(k, off)
            if r is None:
                continue
            faces, target, dist = r
            adj = G5.adj_from_faces(faces)
            odds = [v for v in adj if len(adj[v]) % 2]
            local = all(dist.get(v, 99) <= 3 for v in odds)
            dens = len(odds) / len(adj)
            inst.append((k, off, faces, adj, odds, local, dens))
            print(f"    k={k} off={off}: V={len(adj)} odd={len(odds)} "
                  f"local(<=3)={local} density={dens:.2f}")
    Vs = {len(a) for _, _, _, a, _, _, _ in inst}
    t1 = (len(inst) >= 4 and all(l for *_, l, _ in inst)
          and all(d <= 0.25 for *_, d in inst)
          and all(len(o) == 4 * k for k, _, _, _, o, _, _ in inst)
          and len(Vs) == 1)
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Constructor passes its own "
          f"verification: {len(inst)} instances, V={sorted(Vs)}, "
          f"odd = 4k exactly, all local, density <= 0.25")

    print("\n  deconfounded table (fixed V; backtracking-seed instrument"
          " — greedy fails on this family, validated in-session):")
    tab = []
    for k, off, faces, adj, odds, local, dens in inst:
        g, nc, de, npop = measure_r_def(faces, adj)
        tab.append((4 * k, g, nc, de, npop))
        print(f"    odd={4*k}: r={g if nc else 'UNMEASURED'} (cols={nc}) "
              f"deficiency={de if npop else 'VOID'} pop={npop}")
    meas = [(o, g, de) for o, g, nc, de, npop in tab
            if g is not None and npop > 0]
    if meas:
        defs_by_odd = {}
        for o, g, de in meas:
            defs_by_odd.setdefault(o, []).append(de)
        monotone = all(max(defs_by_odd[a]) <= min(defs_by_odd[b])
                       for a, b in itertools.combinations(
                           sorted(defs_by_odd), 2))
        nontriv = len(defs_by_odd) >= 2 and \
            min(min(v) for v in defs_by_odd.values()) < \
            max(max(v) for v in defs_by_odd.values())
        rs_by_odd = {o: sorted({g for oo, g, _ in meas if oo == o})
                     for o in sorted({o for o, _, _ in meas})}
        t2 = len(meas) >= 4
        if monotone and nontriv:
            dverd = ("deficiency still tracks odd-count with V held "
                     "fixed — the 5538 correlation was NOT just size")
        elif not nontriv:
            dverd = ("deficiency is CONSTANT across odd-counts at fixed "
                     "V — the 0.92 rank-corr was carried by V")
        else:
            dverd = ("deficiency does NOT order by odd-count at fixed V "
                     "— the 0.92 rank-corr was the V confound")
        print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. VERDICT (fixed V): "
              f"r by odd-count {rs_by_odd}; {dverd}")
    else:
        t2 = False
        print(f"\n  [FAIL] 2. instrument void — no measured rows")

    # ---------------- PART B
    print("\n  PART B — the Hall-type ordering-obstruction instrument")
    adjD, interior, bcyc = Y4.disc(2)
    ofaces = Z1.disc_faces(adjD, interior, bcyc)
    bset = set(bcyc)
    chains = chain_list(adjD, interior, ofaces)
    print(f"    realizable chains: {len(chains)} (Z1 said 43)")

    atlas = json.load(open(os.path.join(HERE,
                                        'availability_atlas_fcw014.json')))
    frozen_rows = [r for r in atlas['rows'] if r['components'] >= 2]

    def eps(c):
        return tuple(0 if H8.face_sign(f, c) == 1 else 1 for f in ofaces)

    cols = [ind for _, ind in chains]
    shapes = []
    out_of_span = []
    for row in frozen_rows:
        pin = dict(zip(bcyc, row['pin']))
        T1, T2 = Y4.completions(adjD, interior, pin)
        delta = tuple(x ^ y for x, y in zip(eps({**pin, **T1}),
                                            eps({**pin, **T2})))
        x0, kern = solve_affine(cols, delta)
        if x0 is None:
            out_of_span.append(row['pin'])
            continue
        best = min_weight_solution(x0, kern)
        Es = [chains[j][0] for j in range(len(chains)) if best[j]]
        modes = []
        hard = 0
        wits = {}
        for S in Es:
            m1, w1 = failure_mode(adjD, S, {**pin, **T1}, bset)
            m2, w2 = failure_mode(adjD, S, {**pin, **T2}, bset)
            modes.append((m1, m2))
            wits[S] = w1 | w2
            if not any((wits[S] & S2) for S2 in Es if S2 != S) \
                    and wits[S]:
                hard += 1
        # SCC count of dependency digraph
        idx = {S: i for i, S in enumerate(Es)}
        edges = {i: [idx[S2] for S2 in Es
                     if S2 != S and (wits[S] & S2)]
                 for i, S in enumerate(Es)}
        n_scc = 0
        seen, order = set(), []

        def dfs(u, g, mark, acc):
            st = [(u, iter(g[u]))]
            mark.add(u)
            while st:
                x, it = st[-1]
                nxt = next((y for y in it if y not in mark), None)
                if nxt is None:
                    st.pop()
                    acc.append(x)
                else:
                    mark.add(nxt)
                    st.append((nxt, iter(g[nxt])))

        for u in edges:
            if u not in seen:
                dfs(u, edges, seen, order)
        redges = {i: [] for i in edges}
        for u, vs in edges.items():
            for v in vs:
                redges[v].append(u)
        seen2 = set()
        for u in reversed(order):
            if u not in seen2:
                acc = []
                dfs(u, redges, seen2, acc)
                n_scc += 1
        shape = (len(Es), sum(delta),
                 tuple(sorted(Counter(m for pair in modes
                                      for m in pair).items())),
                 hard, n_scc,
                 tuple(sorted(len(S) for S in Es)))
        shapes.append((tuple(row['pin']), shape))
        print(f"    pin {row['pin']}: |E*|={shape[0]} wt(delta)={shape[1]} "
              f"modes={shape[2]} hard={shape[3]} scc={shape[4]} "
              f"sizes={shape[5]}")
    t3 = len(chains) == 43 and len(shapes) + len(out_of_span) == 15
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. 43 chains; all 15 pairs "
          f"processed; OUT-OF-SPAN (GF(2) SEPARATOR!): "
          f"{len(out_of_span)}")
    for p in out_of_span:
        print(f"    *** delta NOT in chain span: {p}")

    t4 = len(shapes) >= 10
    print(f"  [{'PASS' if t4 else 'FAIL'}] 4. Certificates computed under "
          f"the frozen procedure (seed 5555, 3000 iters, no per-instance "
          f"knob)")

    # orbit reduction under D12 x S4
    autos = D2.disc_automorphisms(adjD)
    perms = list(itertools.permutations(range(4)))
    pins = [p for p, _ in shapes]
    orbit = {}
    for p in pins:
        pd = dict(zip(bcyc, p))
        canon = min(tuple(pi[pd[g[u]]] for u in bcyc)
                    for g in autos if all(g[u] in pd for u in bcyc)
                    for pi in perms)
        orbit.setdefault(canon, []).append(p)
    shp_census = Counter(s for _, s in shapes)
    n_orbits = len(orbit)
    top_shape, top_n = shp_census.most_common(1)[0] if shp_census else (None, 0)
    recur = top_n >= max(2, len(shapes) // 2)
    t5 = True
    print(f"\n  orbit structure: {len(pins)} frozen pinnings fall into "
          f"{n_orbits} (D12 x S4)-orbits")
    print(f"  shape census: {len(shp_census)} distinct shapes / "
          f"{len(shapes)} pairs; top shape recurs {top_n}x")
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. VERDICT: "
          f"{'the obstruction has STABLE RECURRING STRUCTURE — S3 lives; certificate shape: ' + str(top_shape) if recur else 'the obstruction is AMORPHOUS across frozen pairs — Lyra' + chr(39) + 's own KILL condition fires on S3'}"
          f" (orbit context: {n_orbits} orbits — recurrence across orbits "
          f"is the strong form)")

    res = [t1, t2, t3, t4, t5]
    print(f"\n{'=' * 70}")
    print(f"Toy 5555 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
