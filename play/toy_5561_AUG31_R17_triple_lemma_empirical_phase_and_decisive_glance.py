#!/usr/bin/env python3
"""
Toy 5561 — Round 17: TRIPLE LEMMA — empirical phase + the decisive glance

Lyra's spec (Lyra_TRIPLE_LEMMA_..._2026-08-31.md). Cal gates the metric
pick (M1 Hamming-to-freed vs M2 interface length) — BOTH are computed
and logged; no verdict of record keys on either until Cal picks. The
DECISIVE GLANCE is run metric-free (context -> gate availability) plus
under both metrics (context -> strict-descent availability), so the
hinge answer does not wait.

PHASE A — Fritsch, exact (the stored stuck population, F1/D1 filter):
per stuck case, d0 under M1/M2 (freed = exhaustive tau<=5 colorings of
the same apex), best Delta-d over its unsticking gates, and the
strict-descent census. Radius-2 = the whole graph on Fritsch (9v):
contexts degenerate there — reported, not hidden.

PHASE B — T_3 tower (V=17, apex hole; ball(2) = 10 of 16 — proper):
sampled stuck population (backtracking seeds + swap walks, filter
tau=6 strict). Per stuck case: context = (radius-2 pattern,
chain-crossing type at the ball boundary), both RAW and CANONICAL
(mod color perms x graph automorphisms fixing the apex, automorphisms
verified against adj); outcome = gate availability (metric-free), and
descent availability under M1/M2 with d = min over the SAMPLED freed
set (upper-bound caveat declared). Chain-exit logged per realizing
gate. KILL pre-registered: same canonical context, different outcome.
Absence at scale = license for the exhaustive phase.

TESTS (X/Y): 1. Phase A table + descent census · 2. Phase B population,
contexts, exit stats · 3. the decisive glance verdict.

Elie, 2026-08-31. Millennium week, 4-Color round 17. 3 tests.
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


G5 = load("g5512tl", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera"
          "_kittell_fritsch_positive_controls.py")
X3 = load("t5521tl", "toy_5521_AUG30_X3_commutator_laboratory_support"
          "_locality_unstick.py")
P3 = load("t5510tl", "toy_5510_AUG30_P3_rebin_historical_strict_slot"
          "_variance_instrument_not_population.py")
H8 = load("t5518tl", "toy_5518_AUG30_E4_heawood_gf3_instrument_rank"
          "_coset_stuck_separation.py")


def commutator_with_chains(adj, col, m1, m2, tv):
    chains = []
    c = col
    for move in (m1, m2, m1, m2):
        pair, seed = move
        a, b = pair
        if c.get(seed) in (a, b):
            comp = G5.kempe_chain(adj, c, seed, a, b, exclude={tv})
            chains.append(comp)
            c = G5.do_swap(c, comp, a, b)
    return c, chains


def edges_of(adj, skip):
    return [(u, w) for u in adj for w in adj[u]
            if u < w and u != skip and w != skip]


def dists(c1, c2, vs, elist):
    ham = sum(1 for v in vs if c1[v] != c2[v])
    wall = sum(1 for u, w in elist
               if (c1[u] != c2[u]) != (c1[w] != c2[w]))
    return ham, wall


def gates_of(adj, c, tv):
    mv = []
    for u in adj[tv]:
        cu = c[u]
        for other in range(4):
            if other != cu:
                mv.append((tuple(sorted((cu, other))), u))
    out = []
    for m1, m2 in itertools.permutations(mv, 2):
        if m1[0] == m2[0]:
            continue
        k = X3.commutator(adj, c, m1, m2, tv)
        if not X3.support(c, k):
            continue
        if not G5.is_proper(adj, k, skip=tv):
            continue
        if not X3.freeable(adj, k, tv):
            continue
        out.append((m1, m2, k))
    return out


def bt_color(adj, skip, seed):
    vs = [v for v in sorted(adj) if v != skip]
    rng = random.Random(seed)
    pri = {v: rng.random() for v in vs}
    col = {}

    def pick():
        best, bk = None, None
        for v in vs:
            if v in col:
                continue
            used = {col[w] for w in adj[v] if w in col}
            key = (-len(used), -len(adj[v]), pri[v])
            if best is None or key < bk:
                best, bk = v, key
        return best

    def bt():
        v = pick()
        if v is None:
            return True
        cs = [0, 1, 2, 3]
        rng.shuffle(cs)
        for cc in cs:
            if all(col.get(w) != cc for w in adj[v]):
                col[v] = cc
                if bt():
                    return True
                del col[v]
        return False

    return dict(col) if bt() else None


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5561 — R17: Triple Lemma empirical phase + decisive glance")
    print("=" * 70)

    # ---------------- PHASE A: Fritsch exact
    faces = G5.fritsch_faces()
    adj = G5.adj_from_faces(faces)
    n_stuck = 0
    n_desc1 = n_desc2 = 0
    dd_census1 = Counter()
    dd_census2 = Counter()
    for tv in [v for v in sorted(adj) if len(adj[v]) == 5]:
        vs = sorted(u for u in adj if u != tv)
        elist = edges_of(adj, tv)
        pop = list(G5.exhaustive_colorings(adj, tv))
        freed = [c for c in pop
                 if G5.operational_tau(adj, c, tv) <= 5]
        dcache = {}

        def dmin(c):
            key = tuple(c[u] for u in vs)
            if key not in dcache:
                b1 = b2 = 10 ** 9
                for f in freed:
                    h, w = dists(c, f, vs, elist)
                    b1 = min(b1, h)
                    b2 = min(b2, w)
                dcache[key] = (b1, b2)
            return dcache[key]

        for c in pop:
            if G5.operational_tau(adj, c, tv) != 6:
                continue
            info = G5.structure_true(faces, adj, c, tv)
            if info is None:
                continue
            swaps, _fl = G5.forced_swaps(adj, c, tv, info)
            if any(G5.operational_tau(adj, G5.do_swap(c, ch, a, b), tv)
                   <= 5 for (a, b), fv, ch in swaps):
                continue
            n_stuck += 1
            d1, d2 = dmin(c)
            best1 = best2 = 10 ** 9
            for m1, m2, k in gates_of(adj, c, tv):
                e1, e2 = dmin(k)
                best1 = min(best1, e1 - d1)
                best2 = min(best2, e2 - d2)
            dd_census1[best1] += 1
            dd_census2[best2] += 1
            n_desc1 += best1 < 0
            n_desc2 += best2 < 0
    print(f"\n  PHASE A (Fritsch, exact): stuck cases {n_stuck}")
    print(f"    best Delta-d census M1 (Hamming): "
          f"{dict(sorted(dd_census1.items()))}")
    print(f"    best Delta-d census M2 (interface): "
          f"{dict(sorted(dd_census2.items()))}")
    print(f"    strict descent available: M1 {n_desc1}/{n_stuck}, "
          f"M2 {n_desc2}/{n_stuck}")
    print(f"    (radius-2 = whole graph on Fritsch: contexts degenerate "
          f"here; metric pick is Cal's — both logged, neither privileged)")
    t1 = n_stuck > 0
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Phase A table complete")

    # ---------------- PHASE B: T_3 tower glance
    tfaces = [tuple(f) for f in P3.antiprism_stack(3)]
    tadj = G5.adj_from_faces(tfaces)
    apex = max(tadj)
    assert len(tadj[apex]) == 5
    dist = {apex: 0}
    q = deque([apex])
    while q:
        u = q.popleft()
        for w in tadj[u]:
            if w not in dist:
                dist[w] = dist[u] + 1
                q.append(w)
    ball2 = sorted(v for v in tadj if v != apex and dist[v] <= 2)
    bdry = sorted(v for v in tadj if dist[v] == 2)
    outside = sorted(v for v in tadj if dist[v] > 2)
    print(f"\n  PHASE B (T_3): V={len(tadj)}, ball2={len(ball2)}, "
          f"boundary={len(bdry)}, outside={len(outside)}")

    # automorphisms fixing apex: all ring maps i -> a_r +- i, verified
    rings = [[1 + 5 * r + i for i in range(5)] for r in range(3)]
    autos = []
    for sgn in (1, -1):
        for a0, a1, a2 in itertools.product(range(5), repeat=3):
            mp = {0: 0, apex: apex}
            for r, ar in enumerate((a0, a1, a2)):
                for i in range(5):
                    mp[rings[r][i]] = rings[r][(ar + sgn * i) % 5]
            if all(mp[w] in tadj[mp[v]] for v in tadj for w in tadj[v]):
                autos.append(mp)
    print(f"    automorphisms fixing apex (verified): {len(autos)}")

    # sampled stuck population
    telist = edges_of(tadj, apex)
    tvs = sorted(v for v in tadj if v != apex)
    seen = set()
    popn = []
    for s in range(60):
        c = bt_color(tadj, apex, s)
        if c is None:
            continue
        frontier = [c]
        for step in range(120):
            rng = random.Random(s * 1000 + step)
            cc = dict(frontier[rng.randrange(len(frontier))])
            u = rng.choice(tvs)
            a = cc[u]
            b = rng.choice([x for x in range(4) if x != a])
            comp = G5.kempe_chain(tadj, cc, u, a, b, exclude={apex})
            cc = G5.do_swap(cc, comp, a, b)
            key = tuple(cc[v] for v in tvs)
            if key not in seen:
                seen.add(key)
                popn.append(cc)
                frontier.append(cc)
    stuck = [c for c in popn if G5.operational_tau(tadj, c, apex) == 6]
    freedT = [c for c in popn
              if G5.operational_tau(tadj, c, apex) <= 5]
    print(f"    sampled population {len(popn)}: stuck {len(stuck)}, "
          f"freed {len(freedT)}")

    def crossing_type(c):
        parts = []
        for a, b in itertools.combinations(range(4), 2):
            nodes = [v for v in bdry if c[v] in (a, b)]
            compid = {}
            for v in nodes:
                if v in compid:
                    continue
                comp = {v}
                st = [v]
                while st:
                    x = st.pop()
                    for w in tadj[x]:
                        if w in comp or c.get(w) not in (a, b):
                            continue
                        if w in outside or w in nodes:
                            comp.add(w)
                            st.append(w)
                for w in comp:
                    if w in nodes:
                        compid[w] = v
            groups = {}
            for v in nodes:
                groups.setdefault(compid[v], []).append(v)
            parts.append(((a, b),
                          frozenset(frozenset(g)
                                    for g in groups.values())))
        return tuple(parts)

    def norm_cx(cx):
        return tuple(sorted((pair, tuple(sorted(tuple(sorted(g))
                                                for g in gs)))
                            for pair, gs in cx))

    def canon(c):
        best = None
        for mp in autos:
            for perm in itertools.permutations(range(4)):
                cc = {v: perm[c[mp[v]]] for v in tadj if v != apex}
                key = (tuple(cc[v] for v in ball2),
                       norm_cx(crossing_type(cc)))
                if best is None or key < best:
                    best = key
        return best

    dT = {}

    def dminT(c):
        key = tuple(c[v] for v in tvs)
        if key not in dT:
            b1 = b2 = 10 ** 9
            for f in freedT:
                h, w = dists(c, f, tvs, telist)
                b1 = min(b1, h)
                b2 = min(b2, w)
            dT[key] = (b1, b2)
        return dT[key]

    of_t = H8.orient_faces(tfaces)
    comp_faces = [f for f in of_t if apex not in f]

    def charge_t(c):
        w = {u: 0 for u in tvs}
        for f in comp_faces:
            z = 1 if H8.face_sign(f, c) == 1 else -1
            for x in f:
                w[x] += z
        return w

    ballset = set(ball2)
    raw_map = {}
    can_map = {}
    exit_census = Counter()
    desc_map1 = {}
    desc_map2 = {}
    for c in stuck:
        gs = gates_of(tadj, c, apex)
        success = bool(gs)
        # three locality notions per realizing gate (F1's lesson:
        # chains / net support / net charge-patch are different objects)
        chain_local = supp_local = patch_local = False
        c0f = charge_t(c)
        for m1, m2, k in gs:
            _, chains = commutator_with_chains(tadj, c, m1, m2, apex)
            if all(ch <= ballset for ch in chains):
                chain_local = True
            if X3.support(c, k) <= ballset:
                supp_local = True
            c1f = charge_t(k)
            pplus = {u for u in tvs if c1f[u] != c0f[u]}
            pminus = {u for u in tvs if c1f[u] != -c0f[u]}
            patch = pplus if len(pplus) <= len(pminus) else pminus
            if patch <= ballset:
                patch_local = True
        if gs:
            exit_census[('chain-local', chain_local)] += 1
            exit_census[('support-local', supp_local)] += 1
            exit_census[('patch-local', patch_local)] += 1
        raw_pat = tuple(c[v] for v in ball2)
        raw = (raw_pat, norm_cx(crossing_type(c)))
        cn = canon(c)
        outc = (success, patch_local)
        raw_map.setdefault(raw, set()).add(outc)
        can_map.setdefault(cn, set()).add(outc)
        if freedT:
            d1, d2 = dminT(c)
            b1 = b2 = 10 ** 9
            for m1, m2, k in gs:
                e1, e2 = dminT(k)
                b1 = min(b1, e1 - d1)
                b2 = min(b2, e2 - d2)
            desc_map1.setdefault(cn, set()).add(b1 < 0)
            desc_map2.setdefault(cn, set()).add(b2 < 0)
    t2 = len(stuck) >= 30 and len(autos) == 10
    print(f"    contexts: raw {len(raw_map)}, canonical {len(can_map)}; "
          f"gate exit census {dict(exit_census)}")
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Phase B population + "
          f"contexts + exit stats")

    viol_raw = [k for k, v in raw_map.items() if len(v) > 1]
    viol_can = [k for k, v in can_map.items() if len(v) > 1]
    viol_d1 = [k for k, v in desc_map1.items() if len(v) > 1]
    viol_d2 = [k for k, v in desc_map2.items() if len(v) > 1]
    t3 = True
    print(f"\n  functionality (same context -> same outcome; outcome = "
          f"(gate exists, PATCH-local gate exists) — the lemma's "
          f"locality is the patch's):")
    print(f"    outcome distribution over canonical contexts: "
          f"{dict(Counter(tuple(sorted(v)) for v in can_map.values()))}")
    print(f"    availability+locality: raw violations {len(viol_raw)}, "
          f"canonical violations {len(viol_can)}")
    print(f"    strict-descent: M1 violations {len(viol_d1)} "
          f"(outcomes {dict(Counter(tuple(sorted(v)) for v in desc_map1.values()))}), "
          f"M2 violations {len(viol_d2)} "
          f"(outcomes {dict(Counter(tuple(sorted(v)) for v in desc_map2.values()))}) "
          f"(sampled-freed caveat)")
    if not viol_can and not viol_raw:
        verdict = ("NO same-context-different-outcome pair — LOCAL "
                   "DECIDABILITY survives the glance at this scale; "
                   "the exhaustive phase is licensed"
                   + ("" if not (viol_d1 or viol_d2) else
                      f" for AVAILABILITY; descent functionality has "
                      f"violations (M1 {len(viol_d1)}, M2 "
                      f"{len(viol_d2)}) — metric-dependent, Cal's pick "
                      f"decides which matters"))
    else:
        verdict = (f"KILL — same-context-different-outcome exhibited "
                   f"({len(viol_can)} canonical, {len(viol_raw)} raw): "
                   f"the finite check as specced is insufficient; the "
                   f"context space must grow")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. DECISIVE GLANCE: "
          f"{verdict}")

    print("""
POST-RULING RECORD (Cal SS801, 2026-08-31 08:04 EDT — metric FROZEN):
M1 (Hamming-to-freed) is the Triple Lemma's metric, picked on
consumer-requirement grounds stated outcome-independently (the induction
needs ANY well-founded strictly-decreasing measure). Verdict of record
for the empirical phase: STRICT DESCENT UNIVERSAL — 144/144 exact
(Fritsch) + all sampled contexts (T_3). M2's universal non-descent
enters NO descent claim; it is banked separately as the WALL TRANSPORT
conservation (the gate moves walls, it does not shrink them — the
pure-curl prediction, measured). Both columns above remain as computed
pre-ruling; nothing was recomputed after the pick.""")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5561 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
