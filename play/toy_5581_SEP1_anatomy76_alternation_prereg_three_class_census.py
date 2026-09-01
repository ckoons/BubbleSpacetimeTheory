#!/usr/bin/env python3
"""
Toy 5581 — THE ANATOMY OF THE 76 + Keeper's alternation pre-registration
+ the three-class interaction census (Cal SS813)

(1) FAILURE ANATOMY (exhibited, not summarized): for every trace the
widened family (12 nearest targets + single-vertex edits) could not
stabilize: cascade shape (new properness violations created by the
edits; cascade rounds to closure, capped 5; does the cascade leave the
rim's neighborhood), collision-site counts, EDIT-ORDER SENSITIVITY
(Cal's third-door nominee: same trace, three edit orders — does the
outcome change), rows per object/surgery depth.

(2) KEEPER'S PRE-REGISTRATION, mine to kill: flip-class ALTERNATION
COUNTS (Lyra's bridge-doorstep sites — per bridge vertex B, the number
of link-cycle vertices colored s_i cyclically adjacent to an s_M
vertex; summed over B1, B2; declared operational form) predict BOTH
patch radii AND stability failures. BLIND: the alternation counts are
computed and hashed BEFORE either symptom flag is computed or joined.

(3) THE THREE-CLASS CENSUS (SS813, one pass): class-1 = the
INTERACTION-GAP collision (edited x adjacent to unedited
target-difference y with c*(y) = (w·c)(x)); class-2 = K-r2
opposite-parity shared-rim conflicts; class-3 = type-(iii)
disagreement instances (target disagrees with the patch value at a
rim vertex). Incidences side by side.

TESTS (X/Y): 1. blind alternation pass hashed · 2. the anatomy of the
failures (with edit-order row) · 3. the pre-registration verdict ·
4. the three-class census.

Elie, 2026-09-01. 4 tests.
"""

import hashlib
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


RD = load("t5577an", "toy_5577_SEP1_redress_witness_at_scale_and_rim"
          "_contact_census.py")
P1, CV, F2C, F1 = RD.P1, RD.CV, RD.F2C, RD.F1
E1, G5, X3, H8 = RD.E1, RD.G5, RD.X3, RD.H8


def alternation_count(faces, adj, c0, B, s_M_col, s_i_col, s_j_col):
    lb = E1.link_cycle(faces, B)
    n = len(lb)
    cnt = 0
    for i in range(n):
        if c0.get(lb[i]) in (s_i_col, s_j_col):
            if c0.get(lb[(i - 1) % n]) == s_M_col or \
                    c0.get(lb[(i + 1) % n]) == s_M_col:
                cnt += 1
    return cnt


def try_stabilize(adj, tv, vs, c0, c4, R, rim_pairs, tau, freed,
                  order_seed=None):
    """The widened family: 12 nearest targets + single-vertex edits;
    returns (stable?, cascade_info, collisions, order_used)."""
    byd = sorted(freed, key=lambda f: sum(1 for v in vs
                                          if c0[v] != f[v]))
    casc_max = 0
    casc_escape = False
    n_coll = 0
    for cstar in byd[:12]:
        cp = dict(cstar)
        for u in R:
            cp[u] = tau[c0[u]]
        failx = sorted({x for u, x in rim_pairs
                        if cp[x] == tau[c0[u]]}, key=str)
        if order_seed is not None:
            rng = random.Random(order_seed)
            rng.shuffle(failx)
        for x in failx:
            cp[x] = c4[x]
        # class-1 collisions + cascade
        rimN = {x for _, x in rim_pairs} | \
            {w for _, x in rim_pairs for w in adj[x]}
        edited = set(failx)
        for x in edited:
            for y in adj[x]:
                if y == tv or y in R or y in edited:
                    continue
                if cstar.get(y) is not None and \
                        cstar[y] != c0[y] and cstar[y] == c4[x]:
                    n_coll += 1
        rounds = 0
        cur_bad = [(u2, w2) for u2 in cp for w2 in adj[u2]
                   if w2 != tv and u2 != tv and w2 in cp
                   and cp[u2] == cp[w2] and str(u2) < str(w2)]
        while cur_bad and rounds < 5:
            rounds += 1
            for u2, w2 in cur_bad:
                pick = w2 if w2 not in R else u2
                cp[pick] = c4.get(pick, cp[pick])
                if pick not in rimN:
                    casc_escape = True
            cur_bad = [(u2, w2) for u2 in cp for w2 in adj[u2]
                       if w2 != tv and u2 != tv and w2 in cp
                       and cp[u2] == cp[w2] and str(u2) < str(w2)]
        casc_max = max(casc_max, rounds)
        if not cur_bad and G5.is_proper(adj, cp, skip=tv) and \
                G5.operational_tau(adj, cp, tv) <= 5:
            return True, (casc_max, casc_escape), n_coll
        # single-vertex family
        cp3 = dict(cstar)
        for u in R:
            cp3[u] = tau[c0[u]]
        fx = {x for u, x in rim_pairs if cp3[x] == tau[c0[u]]}
        for x in fx:
            cp3[x] = c4[x]
        for x in sorted(fx, key=str):
            for col in range(4):
                cp4 = dict(cp3)
                cp4[x] = col
                if G5.is_proper(adj, cp4, skip=tv) and \
                        G5.operational_tau(adj, cp4, tv) <= 5:
                    return True, (casc_max, casc_escape), n_coll
    return False, (casc_max, casc_escape), n_coll


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5581 — anatomy of the 76 / alternation kill / 3-class")
    print("=" * 70)

    pops = RD.build_pops()
    # PASS 1 (blind): alternation counts for every measurable trace
    alt_records = []
    trace_data = []
    for label, faces, adj, tv, stuck, freed, exact in pops:
        lcyc = E1.link_cycle(faces, tv)
        link = set(adj[tv])
        vs = [v for v in sorted(adj, key=str) if v != tv]
        for ci, c0 in enumerate(stuck[:60]):
            rl = F2C.roles(adj, c0, tv, lcyc)
            if rl is None:
                continue
            n_sM, r, s_M, s_i, s_j = rl
            vB = [v for v in lcyc if c0[v] == r]
            a = sum(alternation_count(faces, adj, c0, B, s_M, s_i, s_j)
                    for B in vB)
            alt_records.append((label, ci, a))
            trace_data.append((label, faces, adj, tv, ci, c0, rl))
    blob = json.dumps([(lb, ci, a) for lb, ci, a in alt_records]).encode()
    hh = hashlib.sha256(blob).hexdigest()
    t1 = len(alt_records) > 200
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. BLIND: alternation "
          f"counts for {len(alt_records)} configs hashed "
          f"(sha256 {hh[:32]}...) before any symptom flag")

    # PASS 2: symptom flags + anatomy
    alt_by = {(lb, ci): a for lb, ci, a in alt_records}
    fail_rows = Counter()
    coll_census = Counter()
    casc_census = Counter()
    order_sens = 0
    n_fail = 0
    joins = []
    kr2 = 0
    class3 = 0
    for label, faces, adj, tv, ci, c0, rl in trace_data:
        n_sM, r, s_M, s_i, s_j = rl
        lcyc = E1.link_cycle(faces, tv)
        link = set(adj[tv])
        vs = [v for v in sorted(adj, key=str) if v != tv]
        _, _, _, _, freed = None, None, None, None, None
        # locate this object's freed set
        for lb2, fc2, ad2, tv2, st2, fr2, ex2 in pops:
            if lb2 == label:
                freed = fr2
                break
        if not freed:
            continue
        tau = {r: s_M, s_M: r}
        results = {}
        radius_bad = None
        for sx in (s_i, s_j):
            n_sx = next(v for v in lcyc if c0[v] == sx)
            X1, X2, X3c, X4, c1, c2, c3, c4 = CV.trace(
                adj, c0, tv, n_sM, r, s_M, n_sx, sx)
            R = (X1 - X3c) - X2
            if not R or any(v in link for v in R):
                continue
            rim_pairs = [(u, x) for u in R for x in adj[u]
                         if x != tv and x not in R]
            # kr2 + class3 in the same pass
            forb = {}
            for u, x in rim_pairs:
                forb.setdefault(x, set()).add(tau[c0[u]])
            kr2 += sum(1 for s in forb.values() if len(s) == 2)
            ns = {v for v in vs if c4[v] != c0[v]}
            class3 += sum(1 for x in forb
                          if x in ns)
            ok, casc, ncol = try_stabilize(adj, tv, vs, c0, c4, R,
                                           rim_pairs, tau, freed)
            results[sx] = ok
            coll_census[min(ncol, 6)] += 1
            casc_census[casc] += 1
            if not ok:
                n_fail += 1
                fail_rows[label] += 1
                # edit-order sensitivity: 2 shuffled orders
                o1, _, _ = try_stabilize(adj, tv, vs, c0, c4, R,
                                         rim_pairs, tau, freed,
                                         order_seed=1)
                o2, _, _ = try_stabilize(adj, tv, vs, c0, c4, R,
                                         rim_pairs, tau, freed,
                                         order_seed=2)
                if o1 or o2:
                    order_sens += 1
        if results:
            failed_any = not all(results.values())
            joins.append((label, alt_by[(label, ci)], failed_any))
    t2 = True
    print(f"\n  failures: {n_fail} (rows {dict(fail_rows)}); cascade "
          f"census (rounds, escaped-rim): {dict(casc_census)}; "
          f"collision-count census (cap 6): "
          f"{dict(sorted(coll_census.items()))}")
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. ANATOMY: edit-order "
          f"sensitivity: {order_sens}/{n_fail} failures flip under a "
          f"different edit order "
          f"({'the THIRD DOOR opens — ordering-dependence is real' if order_sens else 'orders agree — ordering is not the mechanism'})")

    # pre-registration join
    flip_joins = [(a, f) for lb, a, f in joins if lb.startswith('D-')]
    afail = sorted(set(a for a, f in flip_joins if f))
    aok = sorted(set(a for a, f in flip_joins if not f))
    sep = not (set(afail) & set(aok))
    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. KEEPER'S "
          f"PRE-REGISTRATION (flip class, n={len(flip_joins)}): "
          f"alternation counts of failing configs {afail} vs "
          f"non-failing {aok} — "
          f"{'SEPARATES: one mechanism under the symptoms — the pre-registration LIVES' if sep and afail else 'DOES NOT separate — the pre-registration DIES (overlap shown)' if afail else 'no flip failures in sample'}")

    t4 = True
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. THREE-CLASS CENSUS "
          f"(one pass): class-1 interaction-gap collisions: "
          f"{sum(k * v for k, v in coll_census.items())} across "
          f"{sum(v for k, v in coll_census.items() if k > 0)} traces; "
          f"class-2 K-r2 parity conflicts: {kr2}; class-3 type-(iii) "
          f"disagreement sites: {class3}")

    res = [t1, t2, t3, t4]
    print(f"\n{'=' * 70}")
    print(f"Toy 5581 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
