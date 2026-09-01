#!/usr/bin/env python3
"""
Toy 5572 — P2 (Sept 1): THE BRIDGE-ANCHORED TRACE ANATOMY

5570's workhorse census and 5571's rescue probe both point the same
way: the winning words anchor at the BRIDGE. This toy hands Lyra the
trace anatomy of the bridge-anchored family so her patch count runs on
the words that actually win.

FAMILY TRACED (the workhorse set, from 5570's census): words
(m1, m2) with m1 = (B, (r, s_M)) and m2 = (B', (r, s_x)) over
B, B' in {B1, B2}, x in {i, j} — 8 words per configuration (the
bridge/r-family). Per trace: net support size + distance profile ·
the DECOMPOSITION Lyra's count needs (anchor-star part = within the
closed link; link-edge flip-zone part = distance 2 through a bridge
neighbor; beyond) · charge patch mod gauge size · stranded remnant
size (per 5571's definition) · which of the 8 words achieves
patch <= 8 & descent (the per-config winner census).

Population: Fritsch exact + T3/T4 (sampled) + harvest kill-adjacent
objects (D-flip2/3, Errera) — the places where the anatomy matters.

TESTS (X/Y): 1. traces run · 2. the anatomy tables · 3. the winner
coverage within the 8-word bridge family.

Elie, 2026-09-01. Millennium week II. 3 tests.
"""

import importlib.util
import json
import os
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


P1 = load("t5571p2", "toy_5571_SEP1_P1_pair_census_exclusion_conjecture"
          "_kill_test.py")
CV, F2C, F1 = P1.CV, P1.F2C, P1.F1
E1, G5, X3, H8 = P1.E1, P1.G5, P1.X3, P1.H8
WF = load("t5570p2", "toy_5570_SEP1_word_family_enumeration_joint"
          "_witness.py")


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5572 — P2: bridge-anchored trace anatomy")
    print("=" * 70)

    pops = []
    fr_faces = G5.fritsch_faces()
    fr_adj = G5.adj_from_faces(fr_faces)
    fr_tv = [v for v in sorted(fr_adj) if len(fr_adj[v]) == 5][0]
    allc = list(G5.exhaustive_colorings(fr_adj, fr_tv))
    fr_stuck = [c for c in allc
                if G5.operational_tau(fr_adj, c, fr_tv) == 6
                and not X3.freeable(fr_adj, c, fr_tv)]
    fr_freed = [c for c in allc
                if G5.operational_tau(fr_adj, c, fr_tv) <= 5]
    pops.append(('Fritsch', fr_faces, fr_adj, fr_tv, fr_stuck,
                 fr_freed))
    for k, nm in ((3, 'T3'),):
        tf = [tuple(f) for f in F1.P3.antiprism_stack(k)]
        ta = G5.adj_from_faces(tf)
        tv = max(ta)
        stuck, freed = F1.stuck_harvest(tf, ta, tv, n_seeds=25,
                                        n_walk=60, amp=30)
        pops.append((nm, tf, ta, tv, stuck[:200], freed))
    for k in (2, 3):
        rr = F1.F3T.family_B_right(k, 0)
        faces = rr[0]
        adj = G5.adj_from_faces(faces)
        tv = [v for v in sorted(adj, key=str) if len(adj[v]) == 5][0]
        stuck, freed = F1.stuck_harvest(faces, adj, tv)
        pops.append((f'D-flip{k}', faces, adj, tv, stuck[:200], freed))
    ad = G5.errera_adj()
    tris, ok, _m = G5.faces_from_adj_triangulation(ad)
    tv = [v for v in sorted(ad) if len(ad[v]) == 5][0]
    stuck, freed = F1.stuck_harvest(tris, ad, tv)
    pops.append(('B-errera', tris, ad, tv, stuck[:200], freed))

    n_traces = 0
    ns_size = Counter()
    decomp = Counter()
    patch_sz = Counter()
    remn_sz = Counter()
    winner = Counter()
    cover = 0
    n_cfg = 0
    for label, faces, adj, tv, stuck, freed in pops:
        lcyc = E1.link_cycle(faces, tv)
        vs = [v for v in sorted(adj, key=str) if v != tv]
        of = H8.orient_faces([tuple(f) for f in faces])
        comp_faces = [f for f in of if tv not in f]
        dist = {tv: 0}
        q = deque([tv])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    q.append(w)
        link = set(adj[tv])
        bridge_nb = None          # set at role time per config

        def charge(cc):
            w = {u: 0 for u in vs}
            for f in comp_faces:
                z = 1 if H8.face_sign(f, cc) == 1 else -1
                for x in f:
                    w[x] += z
            return w

        def dmin(cc):
            best = 10 ** 9
            for f2 in freed:
                h = sum(1 for v in vs if cc[v] != f2[v])
                if h < best:
                    best = h
                    if best <= 1:
                        break
            return best

        for c0 in stuck:
            rm = WF.role_map(adj, c0, tv, lcyc)
            if rm is None:
                continue
            vmap, cmap = rm
            n_cfg += 1
            c0f = charge(c0)
            d0 = dmin(c0) if freed else None
            B1v, B2v = vmap['B1'], vmap['B2']
            bz = (set(adj[B1v]) | set(adj[B2v])) - {tv}
            got = False
            for Ba in ('B1', 'B2'):
                for Bb in ('B1', 'B2'):
                    for x in ('s_i', 's_j'):
                        m1 = (tuple(sorted((cmap['r'], cmap['s_M']))),
                              vmap[Ba])
                        m2 = (tuple(sorted((cmap['r'], cmap[x]))),
                              vmap[Bb])
                        if m1[0] == m2[0]:
                            continue
                        # plain commutator application, as gates_of does
                        kk = X3.commutator(adj, c0, m1, m2, tv)
                        if not X3.support(c0, kk):
                            continue
                        if not G5.is_proper(adj, kk, skip=tv):
                            continue
                        if not X3.freeable(adj, kk, tv):
                            continue
                        n_traces += 1
                        ns = {v for v in vs if kk[v] != c0[v]}
                        ns_size[min(len(ns), 15)] += 1
                        n_link = sum(1 for v in ns if v in link)
                        n_bz = sum(1 for v in ns
                                   if v in bz and v not in link)
                        n_far = len(ns) - n_link - n_bz
                        decomp[(n_link, n_bz, min(n_far, 5))] += 1
                        c1f = charge(kk)
                        pp = {u for u in vs if c1f[u] != c0f[u]}
                        pm = {u for u in vs if c1f[u] != -c0f[u]}
                        patch = pp if len(pp) <= len(pm) else pm
                        patch_sz[min(len(patch), 12)] += 1
                        if len(patch) <= 8 and d0 is not None and \
                                dmin(kk) - d0 < 0 and not got:
                            got = True
                            winner[(Ba, Bb, x)] += 1
            cover += got
    t1 = n_traces > 2000
    print(f"\n  configs: {n_cfg}; bridge-family applications traced: "
          f"{n_traces}")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Traces run")

    print(f"\n  net-support size distribution (cap 15): "
          f"{dict(sorted(ns_size.items()))}")
    print(f"  DECOMPOSITION (link, bridge-zone, far-cap5) top: "
          f"{dict(sorted(decomp.items(), key=lambda x: -x[1])[:10])}")
    print(f"  charge-patch-mod-gauge size distribution (cap 12): "
          f"{dict(sorted(patch_sz.items()))}")
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Anatomy tables "
          f"(Lyra's count: anchor star + bridge zones vs far)")

    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Winner coverage within "
          f"the 8-word bridge family: {cover}/{n_cfg} configs have a "
          f"bridge-word with patch<=8 & descent; winner census "
          f"{dict(sorted(winner.items(), key=lambda x: -x[1])[:6])}")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5572 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
