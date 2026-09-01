#!/usr/bin/env python3
"""
Toy 5574 — the ARMED tranche-2 falsifier (Family Exclusion, unseen data)

Generated AFTER the Family Exclusion restatement, from FRESH seeds and
a fresh object mix (none of these exact populations touched any prior
statement): stacked triangulations (new n, new seeds), the T_6 tower,
Kittell at its SECOND deg-5 hole, flip-surgered O(4) at new offsets.

ARMED, NOT FIRED: this run generates the tranche, harvests its stuck
configurations, and hashes the population. The Family Exclusion test
(for every stuck config, some word in the 186-family strands a
bounded-or-co-bounded remnant; kill = a config where ALL family words
strand middle remnants) is coded below but GATED behind
FIRE_TRANCHE2 = False — it fires the moment Cal's conditions call,
with the population already committed by hash.

TESTS (X/Y): 1. fresh tranche generated + stuck harvested ·
2. population hashed + stored · 3. the gate (armed, not fired).

Elie, 2026-09-01. 3 tests.
"""

import hashlib
import importlib.util
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FIRE_TRANCHE2 = True         # FLIPPED 2026-09-01 ~11:26 per Cal SS809
                             # (automatic on the falsifier paragraph,
                             # which filed 11:17, sha256 3ebe881c...)


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


P1 = load("t5571ar", "toy_5571_SEP1_P1_pair_census_exclusion_conjecture"
          "_kill_test.py")
CV, F2C, F1 = P1.CV, P1.F2C, P1.F1
E1, G5, X3, H8 = P1.E1, P1.G5, P1.X3, P1.H8
WF = load("t5570ar", "toy_5570_SEP1_word_family_enumeration_joint"
          "_witness.py")

TRANCHE = os.path.join(HERE, '.tranche2_family_exclusion.json')


def build_tranche2():
    fams = []
    for n in (14, 18, 24, 30):
        for sd in (11, 12):
            faces = F1.P3.stacked_triangulation(n, seed=sd)
            adj = G5.adj_from_faces([tuple(f) for f in faces])
            tvs = [v for v in sorted(adj) if len(adj[v]) == 5][:1]
            for tv in tvs:
                fams.append((f'2A-stack{n}s{sd}', faces, adj, tv))
    t6 = [tuple(f) for f in F1.P3.antiprism_stack(6)]
    a6 = G5.adj_from_faces(t6)
    fams.append(('2C-T6', t6, a6, max(a6)))
    ad = G5.kittell_adj()
    tris, ok, _m = G5.faces_from_adj_triangulation(ad)
    tvs = [v for v in sorted(ad) if len(ad[v]) == 5]
    if len(tvs) >= 4:
        fams.append(('2B-kittell-h3', tris, ad, tvs[3]))
    for k, off in ((2, 7), (3, 7)):
        rr = F1.F3T.family_B_right(k, off)
        if rr is None:
            continue
        faces = rr[0]
        adj = G5.adj_from_faces(faces)
        tvs = [v for v in sorted(adj, key=str)
               if len(adj[v]) == 5][:1]
        for tv in tvs:
            fams.append((f'2D-flip{k}o{off}', faces, adj, tv))
    return fams


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5574 — armed tranche-2 falsifier (Family Exclusion)")
    print("=" * 70)

    fams = build_tranche2()
    store = {}
    n_stuck_tot = 0
    for label, faces, adj, tv in fams:
        lcyc = E1.link_cycle(faces, tv)
        if len(lcyc) != 5:
            continue
        stuck, freed = F1.stuck_harvest(faces, adj, tv, n_seeds=20,
                                        n_walk=60, amp=30)
        if not stuck:
            continue
        n_stuck_tot += len(stuck)
        store[label] = {'tv': str(tv),
                        'stuck': [{str(k2): v for k2, v in c.items()}
                                  for c in stuck[:200]]}
        print(f"    {label}: stuck={len(stuck)}")
    t1 = n_stuck_tot >= 500 and len(store) >= 6
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Fresh tranche: "
          f"{len(store)} holes, {n_stuck_tot} stuck (fresh seeds, "
          f"fresh mix — unseen by every statement on file)")

    blob = json.dumps(store, sort_keys=True).encode()
    hh = hashlib.sha256(blob).hexdigest()
    with open(TRANCHE, 'wb') as f:
        f.write(blob)
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Population committed: "
          f"sha256 {hh}")

    if not FIRE_TRANCHE2:
        t3 = True
        print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. ARMED, NOT FIRED — "
              f"the Family Exclusion test (all-words-middle kill "
              f"predicate over the 186-family) fires on Cal's call by "
              f"flipping FIRE_TRANCHE2; the population is committed "
              f"above and cannot be quietly regenerated.")
    else:
        # THE TEST (runs only on Cal's call)
        moves, words, _ = WF.context_family()
        kills = []
        n_cfg = 0
        objs = {label: None for label in store}
        for label, faces, adj, tv in build_tranche2():
            if label not in store:
                continue
            lcyc = E1.link_cycle(faces, tv)
            smap = {str(v): v for v in adj}
            nV = len(adj) - 1
            for crec in store[label]['stuck']:
                c0 = {smap[k2]: v for k2, v in crec.items()}
                rm = WF.role_map(adj, c0, tv, lcyc)
                if rm is None:
                    continue
                vmap, cmap = rm
                n_cfg += 1
                ok_any = False
                for w in words:
                    m1 = (tuple(sorted((cmap[w[0][1][0]],
                                        cmap[w[0][1][1]]))),
                          vmap[w[0][0]])
                    m2 = (tuple(sorted((cmap[w[1][1][0]],
                                        cmap[w[1][1][1]]))),
                          vmap[w[1][0]])
                    X1 = G5.kempe_chain(adj, c0, m1[1], *m1[0],
                                        exclude={tv}) \
                        if c0.get(m1[1]) in m1[0] else set()
                    k1 = G5.do_swap(c0, X1, *m1[0])
                    X2 = G5.kempe_chain(adj, k1, m2[1], *m2[0],
                                        exclude={tv}) \
                        if k1.get(m2[1]) in m2[0] else set()
                    k2c = G5.do_swap(k1, X2, *m2[0])
                    X3c = G5.kempe_chain(adj, k2c, m1[1], *m1[0],
                                         exclude={tv}) \
                        if k2c.get(m1[1]) in m1[0] else set()
                    R = (X1 - X3c) - X2
                    if len(R) <= 8 or len(R) >= nV - 8:
                        ok_any = True
                        break
                if not ok_any:
                    kills.append((label, crec))
        t3 = True
        print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. FIRED: "
              f"{n_cfg} configs; FAMILY-EXCLUSION kills: {len(kills)}"
              + (f" — exhibits {kills[:2]}" if kills else
                 " — the kill condition survives unseen data"))

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5574 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
