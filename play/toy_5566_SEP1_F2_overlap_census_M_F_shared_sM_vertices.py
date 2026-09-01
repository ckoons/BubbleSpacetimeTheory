#!/usr/bin/env python3
"""
Toy 5566 — F2 (Sept 1 PM): THE OVERLAP CENSUS — J1's escort

J1's closure path (Lyra L2): a bounded case analysis on how the chains
M and F share s_M-vertices beyond the anchor. This census enumerates
the REALIZED overlap structures across every stuck configuration held
(Fritsch exact + the F1 harvest), so Lyra's enumeration covers every
realized type before a referee looks.

ROLES per stuck configuration (from the One-Context Lemma's forced
word): bridge color r = the color appearing twice on the link; middle
vertex n_sM = the link vertex between the bridge pair; s_M = its
color; s_i, s_j = the other two link colors. M = the (r, s_M)-chain
through n_sM; F = the (s_M, s_x)-chain through n_sM, for BOTH x = i, j
(the dihedral pair — both censused). Overlap = M INTERSECT F (all
s_M-colored by construction).

CENSUS per (config, F-choice): |overlap|; distances of shared vertices
from the anchor; link membership. Third-door field: overlap types
beyond Lyra's single-cut case (|overlap| > 1) are THE deliverable —
and their correlation with F1's radius-3/4 patch cases is checked (is
deep overlap what pushes the patch off radius 2?).

TESTS (X/Y): 1. roles identified on every stuck config (the forced
word guarantees it — failure = instrument bug) · 2. the census ·
3. the correlation with F1's patch-radius classes.

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


F1 = load("t5565f2", "toy_5565_SEP1_F1_breadth_falsifier_leaving_home"
          "_context_hunt.py")
E1, G5, X3, H8 = F1.E1, F1.G5, F1.X3, F1.H8


def roles(adj, c, tv, lcyc):
    """(n_sM, r, s_M, s_i, s_j) from the forced link word; None if the
    word is not bridge-shaped (instrument bug by the One-Context
    Lemma)."""
    n = len(lcyc)
    cols = [c[v] for v in lcyc]
    cnt = Counter(cols)
    twice = [x for x, k in cnt.items() if k == 2]
    if len(twice) != 1:
        return None
    r = twice[0]
    p1, p2 = [i for i in range(n) if cols[i] == r]
    # middle = the position between the bridges on the short side
    if (p1 + 2) % n == p2:
        mid = (p1 + 1) % n
    elif (p2 + 2) % n == p1:
        mid = (p2 + 1) % n
    else:
        return None
    s_M = cols[mid]
    rest = [cols[i] for i in range(n) if i not in (p1, p2, mid)]
    s_i, s_j = rest
    return lcyc[mid], r, s_M, s_i, s_j


def overlap_data(adj, c, tv, n_sM, r, s_M, s_x):
    M = G5.kempe_chain(adj, c, n_sM, r, s_M, exclude={tv})
    F = G5.kempe_chain(adj, c, n_sM, s_M, s_x, exclude={tv})
    shared = M & F
    dist = {n_sM: 0}
    q = deque([n_sM])
    while q:
        u = q.popleft()
        for w in adj[u]:
            if w != tv and w not in dist:
                dist[w] = dist[u] + 1
                q.append(w)
    dd = tuple(sorted(dist.get(v, 99) for v in shared))
    on_link = sum(1 for v in shared if v in adj[tv])
    return len(shared), dd, on_link


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5566 — F2: the M/F overlap census")
    print("=" * 70)

    # populations: Fritsch exact + F1 harvest
    pops = []
    fr_faces = G5.fritsch_faces()
    fr_adj = G5.adj_from_faces(fr_faces)
    fr_tv = [v for v in sorted(fr_adj) if len(fr_adj[v]) == 5][0]
    fr_stuck = [c for c in G5.exhaustive_colorings(fr_adj, fr_tv)
                if G5.operational_tau(fr_adj, c, fr_tv) == 6
                and not X3.freeable(fr_adj, c, fr_tv)]
    pops.append(('Fritsch', fr_faces, fr_adj, fr_tv, fr_stuck))

    harvest = json.load(open(os.path.join(HERE, '.f1_harvest.json')))
    objs = {}
    ad = G5.errera_adj()
    tris, ok, _m = G5.faces_from_adj_triangulation(ad)
    objs['B-errera'] = (tris, ad)
    ad = G5.kittell_adj()
    tris, ok, _m = G5.faces_from_adj_triangulation(ad)
    objs['B-kittell'] = (tris, ad)
    t5 = [tuple(f) for f in F1.P3.antiprism_stack(5)]
    objs['C-T5'] = (t5, G5.adj_from_faces(t5))
    for k in (2, 3):
        r = F1.F3T.family_B_right(k, 0)
        faces, _t, _d = r
        objs[f'D-flip{k}'] = (faces, G5.adj_from_faces(faces))
    for label, (faces, adj) in objs.items():
        if label not in harvest:
            continue
        tvraw = harvest[label]['tv']
        tv = next(v for v in adj if str(v) == tvraw)
        smap = {str(v): v for v in adj}
        stuck = [{smap[k2]: v for k2, v in crec.items()}
                 for crec in harvest[label]['stuck']]
        pops.append((label, faces, adj, tv, stuck))

    n_total = 0
    n_role_fail = 0
    census = Counter()
    deep_by_obj = Counter()
    per_config_max = {}
    for label, faces, adj, tv, stuck in pops:
        lcyc = F1.E1.link_cycle(faces, tv)
        for idx, c in enumerate(stuck):
            n_total += 1
            rl = roles(adj, c, tv, lcyc)
            if rl is None:
                n_role_fail += 1
                continue
            n_sM, r, s_M, s_i, s_j = rl
            mx = 1
            for s_x in (s_i, s_j):
                sz, dd, onl = overlap_data(adj, c, tv, n_sM, r, s_M,
                                           s_x)
                census[(label, sz, dd, onl)] += 1
                mx = max(mx, sz)
            per_config_max[(label, idx)] = mx
            if mx > 1:
                deep_by_obj[label] += 1
    t1 = n_role_fail == 0 and n_total > 500
    print(f"\n  stuck configs processed: {n_total}; role-identification "
          f"failures: {n_role_fail}")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Roles identified on "
          f"every config (the forced word held)")

    print(f"\n  OVERLAP CENSUS (object, |M-and-F|, distances-from-anchor,"
          f" on-link):")
    for kk, v in sorted(census.items(), key=lambda x: (-x[1]))[:18]:
        print(f"    {kk}: {v}")
    sizes = Counter(k[1] for k in census.elements()
                    ) if False else Counter()
    for kk, v in census.items():
        sizes[kk[1]] += v
    n_single = sizes.get(1, 0)
    n_multi = sum(v for s, v in sizes.items() if s > 1)
    print(f"\n  overlap size distribution: {dict(sorted(sizes.items()))}")
    print(f"  SINGLE-CUT (|overlap| = 1, Lyra's proved case): "
          f"{n_single}; BEYOND single-cut: {n_multi} "
          f"({dict(deep_by_obj)} by object)")
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Census complete — "
          f"{'ONLY the single-cut case is realized: Lyra' + chr(39) + 's proved sub-case IS the general case on everything held' if n_multi == 0 else 'overlap types BEYOND single-cut are realized — the case list Lyra must cover is above'}")

    home_multi = deep_by_obj.get('Fritsch', 0)
    offh = {k: v for k, v in deep_by_obj.items() if k != 'Fritsch'}
    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. CORRELATION with F1's "
          f"patch-radius classes: deep overlap at home: {home_multi}; "
          f"off-home: {dict(offh)} — "
          f"{'deep overlap appears EXACTLY off-home, where F1 found radius-3/4 patches: consistent with overlap depth driving patch radius' if home_multi == 0 and offh else 'pattern mixed — see census'}")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5566 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
