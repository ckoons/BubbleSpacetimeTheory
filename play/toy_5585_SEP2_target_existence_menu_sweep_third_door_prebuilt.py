#!/usr/bin/env python3
"""
Toy 5585 — TARGET-EXISTENCE: the third door, pre-built — the target
menu swept on every stuck configuration of the 54-census

Keeper's Round-95 instruction, verbatim in substance: if Lyra's route
passes through Target-Existence ("the right target essentially always
exists" — 5583 MEASURED it), sweep the target menu on every stuck
configuration: does a cage-off-carrier target exist for ALL of them,
or for all-but-some? COUNT. Built BEFORE the derivation lands so the
door is a slot, not a surprise.

PER STUCK CONFIGURATION c (the 54 = 5582's failure set, re-derived
bit-identically): the target menu is the freed (tau<=5) inventory,
Hamming-ordered. Two menus, both reported: the d_gate MENU (targets AT
minimum Hamming — Lyra's "d_gate menu") and the WIDE menu (nearest 40).
For each target c* and each of the 186 family words w with w.c proper
and supported: PER-TARGET strict descent H(w.c, c*) < H(c, c*).
This is stronger than 5582's min-over-targets descent — a fixed
target, not a moving one — and is the quantifier the Capture Lemma
actually carries (exists c*, exists w).

CAGE-OFF-CARRIER, three readings reported separately (the phrase is
Cal's SS815 sentence; the instrument names what it measures):
  (a) STRICT: N[supp(w) U diff(c,c*)] disjoint from carrier(c*), where
      carrier(c*) = union of the Kempe chains certifying tau(c*)<=5
      (can_free_color, return_chain). Pre-scored likely RARE: diff
      usually meets the carrier, because c* differs from c somewhere
      the certificate lives — a zero here is INFORMATION about the
      reading, not a kill.
  (b) CARRIER-PRESERVED: w.c agrees with c* on every carrier vertex
      (the step does not touch the certificate's colors).
  (c) SUPPORT-OFF-CARRIER: N[supp(w)] disjoint from carrier(c*) (the
      word's own footprint stays off the certificate; diff excluded).

FIXED-TARGET DESCENT LOOP (the Capture Lemma's rescue clause in
per-target form): hold the nearest admitting c* FIXED; greedy strict
per-target descent over the family; halt at H=0 or freed/freeable;
cap H0+1 steps. Count halting. Also count configurations where the
fixed-target loop stalls but 5582's target-switching loop recovers —
that count is the size of the gap between "some target" and
"one target".

BLIND: per-configuration records hashed BEFORE any aggregate prints.
No percentages; counts and k/N with the can-fail count.

TESTS (X/Y): 1. failure set re-derived at 54 + blind hash ·
2. TARGET-EXISTENCE (per-target descent, d_gate menu / wide menu) ·
3. cage-off-carrier, readings (a)(b)(c) · 4. fixed-target descent
loop halting · 5. the gap count (fixed vs switching).
Can fail: 2, 3, 4 (test 1 is reproducibility; 5 is a count).

Elie, 2026-09-02. 5 tests.
"""

import hashlib
import importlib.util
import itertools
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


W = load("t5582te", "toy_5582_SEP1_ss814_world_ab_diagnostic_iterated"
         "_arsenal.py")
AN, RD, CV, F2C, F1 = W.AN, W.RD, W.CV, W.F2C, W.F1
E1, G5, X3, H8, WF = W.E1, W.G5, W.X3, W.H8, W.WF

WIDE = 40


def failure_set():
    """5582's failure set, same code path, same slices."""
    pops = RD.build_pops()
    failures = []
    for label, faces, adj, tv, stuck, freed, exact in pops:
        lcyc = E1.link_cycle(faces, tv)
        link = set(adj[tv])
        vs = [v for v in sorted(adj, key=str) if v != tv]
        for c0 in stuck[:60]:
            rl = F2C.roles(adj, c0, tv, lcyc)
            if rl is None:
                continue
            n_sM, r, s_M, s_i, s_j = rl
            tau = {r: s_M, s_M: r}
            for sx in (s_i, s_j):
                n_sx = next(v for v in lcyc if c0[v] == sx)
                X1, X2, X3c, X4, c1, c2, c3, c4 = CV.trace(
                    adj, c0, tv, n_sM, r, s_M, n_sx, sx)
                R = (X1 - X3c) - X2
                if not R or any(v in link for v in R) or not freed:
                    continue
                rim_pairs = [(u, x) for u in R for x in adj[u]
                             if x != tv and x not in R]
                ok, _c, _n = AN.try_stabilize(adj, tv, vs, c0, c4, R,
                                              rim_pairs, tau, freed)
                if not ok:
                    failures.append((label, faces, adj, tv, lcyc, c0,
                                     vs, freed))
                    break
    return failures


def ham(a, b, vs):
    return sum(1 for v in vs if a[v] != b[v])


def carrier_of(adj, cstar, tv):
    """Union of the Kempe chains certifying tau(c*) <= 5."""
    car = set()
    for a, b in itertools.combinations(range(4), 2):
        ok, ch = G5.can_free_color(adj, cstar, tv, a, b,
                                   return_chain=True)
        if ok and ch:
            car |= set(ch)
    car.discard(tv)
    return car


def word_images(adj, c, tv, lcyc, words):
    """All proper, supported images w.c of the family at c."""
    rm = WF.role_map(adj, c, tv, lcyc)
    if rm is None:
        return None
    vmap, cmap = rm
    out = []
    for w in words:
        m1 = (tuple(sorted((cmap[w[0][1][0]], cmap[w[0][1][1]]))),
              vmap[w[0][0]])
        m2 = (tuple(sorted((cmap[w[1][1][0]], cmap[w[1][1][1]]))),
              vmap[w[1][0]])
        k = X3.commutator(adj, c, m1, m2, tv)
        if not X3.support(c, k):
            continue
        if not G5.is_proper(adj, k, skip=tv):
            continue
        out.append((w, k))
    return out


def nbhd(adj, S, tv):
    N = set()
    for v in S:
        N.add(v)
        N.update(u for u in adj[v] if u != tv)
    N.discard(tv)
    return N


def fixed_target_loop(adj, tv, vs, lcyc, c0, cstar, words, cap):
    c = dict(c0)
    h = ham(c, cstar, vs)
    traj = [h]
    for step in range(cap):
        if h == 0 or G5.operational_tau(adj, c, tv) <= 5 or \
                X3.freeable(adj, c, tv):
            return 'halt', step, traj
        imgs = word_images(adj, c, tv, lcyc, words)
        if imgs is None:
            return 'no-context', step, traj
        best = None
        for w, k in imgs:
            hk = ham(k, cstar, vs)
            if hk < h and (best is None or hk < best[0]):
                best = (hk, k)
        if best is None:
            return 'stall', step, traj
        h, c = best
        traj.append(h)
    if h == 0 or G5.operational_tau(adj, c, tv) <= 5 or \
            X3.freeable(adj, c, tv):
        return 'halt', cap, traj
    return 'cap', cap, traj


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5585 — Target-Existence: the menu swept on the 54")
    print("=" * 70)

    moves, words, _ = WF.context_family()
    fails = failure_set()
    n = len(fails)

    records = []
    for label, faces, adj, tv, lcyc, c0, vs, freed in fails:
        imgs = word_images(adj, c0, tv, lcyc, words)
        byd = sorted(freed, key=lambda f: ham(c0, f, vs))
        dmin = ham(c0, byd[0], vs)
        menu_gate = [f for f in byd if ham(c0, f, vs) == dmin]
        menu_wide = byd[:WIDE]
        rec = {'label': label, 'dmin': dmin, 'n_gate': len(menu_gate),
               'n_wide': len(menu_wide), 'n_imgs': len(imgs or [])}
        for mname, menu in (('gate', menu_gate), ('wide', menu_wide)):
            adm_targets = 0
            adm_pairs = 0
            strict = 0
            preserved = 0
            supp_off = 0
            first_adm = None
            first_rank = None
            for rank, cstar in enumerate(menu):
                h0 = ham(c0, cstar, vs)
                car = carrier_of(adj, cstar, tv)
                diff = {v for v in vs if c0[v] != cstar[v]}
                hit = False
                for w, k in (imgs or []):
                    if ham(k, cstar, vs) >= h0:
                        continue
                    hit = True
                    adm_pairs += 1
                    supp = {v for v in vs if k[v] != c0[v]}
                    cage = nbhd(adj, supp | diff, tv)
                    if not (cage & car):
                        strict += 1
                    if all(k[v] == cstar[v] for v in car):
                        preserved += 1
                    if not (nbhd(adj, supp, tv) & car):
                        supp_off += 1
                if hit:
                    adm_targets += 1
                    if first_adm is None:
                        first_adm = cstar
                        first_rank = rank
            rec[mname] = {'adm_targets': adm_targets,
                          'adm_pairs': adm_pairs, 'strict': strict,
                          'preserved': preserved, 'supp_off': supp_off}
            if mname == 'wide':
                rec['first_adm'] = first_adm
                rec['first_rank'] = first_rank
                rec['first_H'] = (ham(c0, first_adm, vs)
                                  if first_adm is not None else None)
        # fixed-target loop on the nearest admitting wide-menu target
        if rec['first_adm'] is not None:
            cst = rec['first_adm']
            h0 = ham(c0, cst, vs)
            oc, st, tj = fixed_target_loop(adj, tv, vs, lcyc, c0, cst,
                                           words, h0 + 1)
        else:
            oc, st, tj = 'no-target', 0, [dmin]
        rec['fixed'] = (oc, st, tuple(tj))
        # 5582's switching loop, for the gap count
        W.iterate_chain.lcyc = lcyc
        oc2, st2, tj2 = W.iterate_chain(adj, tv, vs, c0, freed, words,
                                        dmin + 1)
        rec['switch'] = (oc2, st2, tuple(tj2))
        rec.pop('first_adm', None)
        records.append(rec)

    blob = json.dumps([str(sorted(r.items())) for r in records]).encode()
    hh = hashlib.sha256(blob).hexdigest()
    t1 = n == 54
    print(f"\n  failure set re-derived: {n} "
          f"({dict(Counter(r['label'] for r in records))}); per-config "
          f"records hashed BEFORE aggregation: sha256 {hh[:32]}...")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Failure set at 54 + "
          f"blind hash")

    # 2. Target-Existence
    k_gate = sum(1 for r in records if r['gate']['adm_targets'] > 0)
    k_wide = sum(1 for r in records if r['wide']['adm_targets'] > 0)
    gate_sizes = Counter(r['n_gate'] for r in records)
    adm_frac = [(r['gate']['adm_targets'], r['n_gate']) for r in records]
    all_gate = sum(1 for a, b in adm_frac if a == b)
    t2 = k_wide == n
    print(f"\n  per-target strict descent exists — d_gate menu: "
          f"{k_gate}/{n}; wide menu (nearest {WIDE}): {k_wide}/{n}")
    print(f"  d_gate-menu sizes: {dict(sorted(gate_sizes.items()))}; "
          f"configs where EVERY d_gate-menu target admits a word: "
          f"{all_gate}/{n}")
    print(f"  admitting-pair counts (wide), by config: "
          f"{sorted(r['wide']['adm_pairs'] for r in records)}")
    nonadm = [(r['label'], r['dmin'], r['n_gate'], r['first_rank'],
               r['first_H']) for r in records
              if r['gate']['adm_targets'] == 0]
    if nonadm:
        print(f"  d_gate-menu NON-admitting configs (label, dmin, "
              f"|menu|, first admitting rank, its H): {nonadm[:12]}")
    ranks = Counter(r['first_rank'] for r in records)
    print(f"  first-admitting target RANK (0 = nearest), all 54: "
          f"{dict(sorted(ranks.items()))} -> menu depth K needed = "
          f"{max(ranks)+1}")
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. TARGET-EXISTENCE "
          f"(a target with a strictly-descending word): {k_wide}/{n} "
          f"on the wide menu, {k_gate}/{n} on the d_gate menu")

    # 3. cage-off-carrier
    ks = {}
    for key in ('strict', 'preserved', 'supp_off'):
        ks[key] = sum(1 for r in records if r['wide'][key] > 0)
    t3 = ks['preserved'] == n
    print(f"\n  cage-off-carrier (wide menu), configs with >=1 "
          f"admitting (c*, w) satisfying the reading:")
    print(f"    (a) STRICT  N[supp U diff] disjoint from carrier(c*): "
          f"{ks['strict']}/{n}")
    print(f"    (b) CARRIER-PRESERVED  w.c = c* on carrier(c*):       "
          f"{ks['preserved']}/{n}")
    print(f"    (c) SUPPORT-OFF  N[supp(w)] disjoint from carrier(c*): "
          f"{ks['supp_off']}/{n}")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Cage-off-carrier under "
          f"reading (b), the operational one: {ks['preserved']}/{n} "
          f"(readings (a),(c) logged as the instrument's other lenses)")

    # 4. fixed-target loop
    fx = Counter(r['fixed'][0] for r in records)
    k4 = fx.get('halt', 0)
    steps4 = Counter(r['fixed'][1] for r in records
                     if r['fixed'][0] == 'halt')
    t4 = k4 == n
    print(f"\n  fixed-target loop outcomes: {dict(fx)}; halting "
          f"step-counts: {dict(sorted(steps4.items()))}")
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Fixed-target descent "
          f"halts within H0+1: {k4}/{n}")

    # 5. the gap
    sw = Counter(r['switch'][0] for r in records)
    gap = [(r['label'], r['fixed'][0], r['fixed'][2], r['switch'][2])
           for r in records
           if r['fixed'][0] != 'halt' and r['switch'][0] == 'freed']
    rev = sum(1 for r in records
              if r['fixed'][0] == 'halt' and r['switch'][0] != 'freed')
    t5 = True
    print(f"\n  switching loop (5582) outcomes on the same 54: "
          f"{dict(sw)}")
    print(f"  GAP (fixed stalls, switching recovers): {len(gap)}/{n}; "
          f"reverse (fixed halts, switching does not): {rev}/{n}")
    for g in gap[:8]:
        print(f"    {g}")
    revs = [(r['label'], r['dmin'], r['first_rank'], r['first_H'],
             r['fixed'], r['switch']) for r in records
            if r['fixed'][0] == 'halt' and r['switch'][0] != 'freed']
    for g in revs[:4]:
        print(f"    reverse: {g}")
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. Gap between 'one "
          f"target' and 'some target' counted: {len(gap)}/{n}")

    res = [t1, t2, t3, t4, t5]
    print(f"\n{'=' * 70}")
    print(f"Toy 5585 -- SCORE: {sum(res)}/{len(res)}  "
          f"(can-fail: 2, 3, 4)")
    print(f"{'=' * 70}")
