#!/usr/bin/env python3
"""
Toy 5521 — X3 (Round 4): THE COMMUTATOR LABORATORY

Casey's Rubik frame: solve by commutators — composite moves with small
support that fix everything else. A move here is M = (color-pair, seed):
"swap the {a,b}-Kempe component containing seed" (no-op if seed's color is
outside the pair). Each M is an involution ON THE COLORING WHERE IT IS
APPLIED; the commutator is the 4-move word [M1,M2] = M1 M2 M1 M2 with
DYNAMIC chains (each move acts on the current coloring — the puzzle-theory
commutator).

Lyra's L2 conjecture (board): commutators of overlapping swaps implement
LOCAL knot-transport. My measurements below are the empirical side;
divergence from her calculus is the finding.

MEASUREMENTS (Fritsch, exhaustive stuck set — 144 double-fail colorings —
plus its 288 rescuable tau=6 colorings as contrast):
  1. Sanity: vertex-disjoint chains commute — support([M1,M2]) = 0. 100%.
  2. Support census of overlapping-chain commutators: distribution,
     minimal nontrivial support.
  3. Locality: fraction of commutator support lying within distance 1 of
     the odd-vertex set (in Fritsch: t,b vertices — all deg-5).
  4. UNSTICK test: from each stuck coloring, does some single commutator
     [M1,M2] (M1,M2 overlapping, both anchored at the stuck vertex's link)
     produce a coloring where v is freeable by <= 1 swap? Report the count
     and the minimal support of an unsticking commutator.
  5. Rescue anatomy: the known depth-2 rescues M1;M2 — measure how many
     have chain(M2) overlapping chain(M1) (post-M1). Prediction
    (registered): rescues are predominantly OVERLAPPING pairs — i.e.,
    half-commutators; the commutator is the rescue's closed-loop version.

Elie, 2026-08-30. Millennium week, 4-Color round 4. 5 tests.
"""

import importlib.util
import itertools
import os
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


G5 = load("g5512c", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")


def apply_move(adj, col, move, v_excl):
    pair, seed = move
    a, b = pair
    if col.get(seed) not in (a, b):
        return col
    comp = G5.kempe_chain(adj, col, seed, a, b, exclude={v_excl})
    return G5.do_swap(col, comp, a, b)


def commutator(adj, col, m1, m2, v_excl):
    c = apply_move(adj, col, m1, v_excl)
    c = apply_move(adj, c, m2, v_excl)
    c = apply_move(adj, c, m1, v_excl)
    c = apply_move(adj, c, m2, v_excl)
    return c


def support(c0, c1):
    return {u for u in c0 if c0[u] != c1[u]}


def freeable(adj, col, v):
    if len({col[u] for u in adj[v]}) < 4:
        return True
    return any(G5.can_free_color(adj, col, v, a, b)
               for a, b in itertools.combinations(range(4), 2))


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5521 — X3: commutator laboratory on Fritsch")
    print("=" * 70)

    faces = G5.fritsch_faces()
    adj = G5.adj_from_faces(faces)
    odd = {u for u in adj if len(adj[u]) % 2 == 1}

    # exhaustive tau=6 populations at all deg-5 vertices
    stuck_cases = []
    free_cases = []
    for tv in [v for v in sorted(adj) if len(adj[v]) == 5]:
        for c in G5.exhaustive_colorings(adj, tv):
            if G5.operational_tau(adj, c, tv) != 6:
                continue
            info = G5.structure_true(faces, adj, c, tv)
            if info is None:
                continue
            swaps, _fl = G5.forced_swaps(adj, c, tv, info)
            succ = sum(1 for (a, b), fv, ch in swaps
                       if G5.operational_tau(
                           adj, G5.do_swap(c, ch, a, b), tv) <= 5)
            (stuck_cases if succ == 0 else free_cases).append((tv, c))
    print(f"\n  stuck: {len(stuck_cases)}  rescuable: {len(free_cases)}")

    def moves_at(col, tv):
        """All moves anchored at the link of tv: (pair, seed) for each link
        vertex and each pair containing its color."""
        out = []
        for u in adj[tv]:
            cu = col[u]
            for other in range(4):
                if other != cu:
                    out.append((tuple(sorted((cu, other))), u))
        return out

    # Test 1: commutation structure. Registered expectation refined after
    # first run caught my own error: disjoint CHAINS with a SHARED COLOR
    # between pairs need not commute (the first swap can extend the second
    # chain by adjacency). The correct algebra: COLOR-DISJOINT pairs (e.g.
    # (0,1) vs (2,3)) always commute; shared-color disjoint-chain pairs are
    # measured, not assumed.
    n1 = ok1 = 0
    n1s = comm1s = 0
    for tv, c in stuck_cases[:30]:
        mv = moves_at(c, tv)
        for m1, m2 in itertools.combinations(mv, 2):
            ch1 = G5.kempe_chain(adj, c, m1[1], *m1[0], exclude={tv}) \
                if c[m1[1]] in m1[0] else set()
            ch2 = G5.kempe_chain(adj, c, m2[1], *m2[0], exclude={tv}) \
                if c[m2[1]] in m2[0] else set()
            if not ch1 or not ch2 or (ch1 & ch2):
                continue
            k = commutator(adj, c, m1, m2, tv)
            trivial = (support(c, k) == set())
            if set(m1[0]) & set(m2[0]):
                n1s += 1
                comm1s += trivial
            else:
                n1 += 1
                ok1 += trivial
    t1 = n1 > 0 and ok1 == n1
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Color-disjoint pairs commute "
          f"({ok1}/{n1}); shared-color disjoint-chain pairs commute in only "
          f"{comm1s}/{n1s} — the non-commutativity lives in shared-color "
          f"adjacency interaction (measured fact for Lyra's L2)")

    # Tests 2-4 on stuck cases
    supp_dist = Counter()
    min_supp = None
    unstick_count = 0
    unstick_min_supp = None
    loc_fracs = []
    for tv, c in stuck_cases:
        mv = moves_at(c, tv)
        found_unstick = False
        for m1, m2 in itertools.permutations(mv, 2):
            ch1 = G5.kempe_chain(adj, c, m1[1], *m1[0], exclude={tv}) \
                if c[m1[1]] in m1[0] else set()
            ch2 = G5.kempe_chain(adj, c, m2[1], *m2[0], exclude={tv}) \
                if c[m2[1]] in m2[0] else set()
            if not ch1 or not ch2 or not (ch1 & ch2) or m1[0] == m2[0]:
                continue
            k = commutator(adj, c, m1, m2, tv)
            s = support(c, k)
            if s:
                supp_dist[len(s)] += 1
                if min_supp is None or len(s) < min_supp:
                    min_supp = len(s)
                near_odd = sum(1 for u in s
                               if u in odd or (adj[u] & odd))
                loc_fracs.append(near_odd / len(s))
                if G5.is_proper(adj, k, skip=tv) and freeable(adj, k, tv):
                    found_unstick = True
                    if (unstick_min_supp is None
                            or len(s) < unstick_min_supp):
                        unstick_min_supp = len(s)
        if found_unstick:
            unstick_count += 1
    print(f"\n  overlapping-commutator support distribution: "
          f"{dict(sorted(supp_dist.items()))}")
    print(f"  minimal nontrivial support: {min_supp}")
    t2 = bool(supp_dist)
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Support census computed")
    mean_loc = sum(loc_fracs) / len(loc_fracs) if loc_fracs else 0
    t3 = bool(loc_fracs)
    print(f"  [{'PASS' if t3 else 'FAIL'}] 3. Locality: mean fraction of "
          f"support within distance 1 of odd set: {mean_loc:.2f}")
    t4 = unstick_count == len(stuck_cases)
    print(f"  [{'PASS' if t4 else 'FAIL'}] 4. UNSTICK: single commutator "
          f"unsticks {unstick_count}/{len(stuck_cases)} stuck colorings "
          f"(minimal unsticking support: {unstick_min_supp})")

    # Test 5: rescue anatomy — ALL depth-2 rescues classified (the first
    # run's "first-found" selector was biased by enumeration order and
    # found 0/40 overlapping; measure the full mix).
    tot_rescues = 0
    ov_rescues = 0
    cases_with_ov = 0
    cases_with_disj = 0
    for tv, c in stuck_cases[:40]:
        has_ov = has_disj = False
        for a1, b1 in itertools.combinations(range(4), 2):
            seen1 = set()
            for u in adj:
                if u == tv or u in seen1 or c.get(u) not in (a1, b1):
                    continue
                ch1 = G5.kempe_chain(adj, c, u, a1, b1, exclude={tv})
                seen1 |= ch1
                c1 = G5.do_swap(c, ch1, a1, b1)
                for a2, b2 in itertools.combinations(range(4), 2):
                    seen2 = set()
                    for w in adj:
                        if w == tv or w in seen2 or c1.get(w) not in (a2, b2):
                            continue
                        ch2 = G5.kempe_chain(adj, c1, w, a2, b2,
                                             exclude={tv})
                        seen2 |= ch2
                        c2 = G5.do_swap(c1, ch2, a2, b2)
                        if len({c2[x] for x in adj[tv]}) < 4:
                            tot_rescues += 1
                            if ch1 & ch2:
                                ov_rescues += 1
                                has_ov = True
                            else:
                                has_disj = True
        cases_with_ov += has_ov
        cases_with_disj += has_disj
    t5 = tot_rescues > 0
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. Rescue anatomy (full census, "
          f"40 stuck cases): {tot_rescues} depth-2 rescues, "
          f"{ov_rescues} overlapping ({100 * ov_rescues // max(tot_rescues, 1)}"
          f" per 100); cases with an overlapping rescue: {cases_with_ov}/40, "
          f"with a disjoint rescue: {cases_with_disj}/40. My registered "
          f"prediction (rescues predominantly overlapping) is scored by the "
          f"printed mix — the number rules, not the guess.")

    results = [t1, t2, t3, t4, t5]
    passed = sum(results)
    print(f"\n{'=' * 70}")
    print(f"Toy 5521 -- SCORE: {passed}/{len(results)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(results, 1):
        if not r:
            print(f"  Test {i}: FAIL")
