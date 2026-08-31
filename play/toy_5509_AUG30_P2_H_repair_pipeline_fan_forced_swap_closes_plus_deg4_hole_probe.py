#!/usr/bin/env python3
"""
Toy 5509 — P2 (K1832 Section 6, pre-registered): THE H-REPAIR PIPELINE

Keeper's Section 3 repair: the induction colors H = (G-v) + 2 non-crossing
pentagon diagonals, never G-v. Every chain, swap, tau computed IN H.

PRE-REGISTERED PREDICTIONS (can-fail), all 5 diagonal choices swept
adversarially (every pentagon triangulation is a fan from one apex):
  (i)   at tau=6 (in H) the two hole diagonals are always the fan from s_M
        — i.e., tau=6 only occurs when the chosen apex IS the middle singleton;
  (ii)  post-split-bridge-swap tau <= 5 in 100% of cases;
  (iii) the second swap always frees a color (v gets properly colored in G).

BEYOND THE PRE-REGISTRATION (flagged as Elie's addition, for Cal's "does the
H-repair leak anywhere" question): the DEG-4 HOLE PROBE. K1832 says "for
deg(v) <= 4, triangulate the smaller hole likewise" — one line. But in H the
quad-hole diagonal (w0,w2) permanently chain-joins the pair (c(w0),c(w2)), so
the classical Kempe deg-4 argument does not transfer verbatim: if (c(w1),c(w3))
is ALSO outside-connected, no single swap frees a color at v. Test 8 hunts for
exactly that configuration. Any hit is a repair leak at the "trivial" case.

Embedding discipline: v's bridge/middle geometry comes from G's TRUE link
cycle (face-tracked, per Toy 5508's instrument); chains run in H.

TESTS (X/Y):
  1. H construction validity (deg-5 holes; new-diagonal bookkeeping).
  2. Prediction (i): tau=6 in H ==> fan apex = middle singleton. 100%.
  3. Fan geometry at tau=6: neither bridge vertex is a diagonal endpoint;
     diagonals are exactly (s_M,s_i),(s_M,s_j).
  4. Middle-strict holds in H at tau=6 (Toy 5508 bridge into H).
  5. Lemma 6 in H: a valid split-bridge swap EXISTS at every tau=6. 100%.
  6. Prediction (ii): ALL valid split-bridge swaps drop tau to <= 5. 100%.
  7. Prediction (iii): second stage always frees a color; final coloring
     proper in G. 100%.
  8. DEG-4 HOLE PROBE: hunt saturated deg-4 insertions in H where NO single
     swap frees a color (both diagonal choices swept). Report loudly.
  9. End-to-end repaired induction: recursively 4-color whole triangulations
     via the H-induction; verify properness; count tau=6 / deg-4 branch hits.

Elie, 2026-08-30. Millennium week, 4-Color day. 9 tests.
"""

import itertools
import random
from collections import defaultdict, deque, Counter

# ------------------------------------------------------------------
# Kempe machinery on an explicit neighbor list (v is ABSENT from H)
# ------------------------------------------------------------------

def kempe_chain(adj, color, start, c1, c2, exclude=None):
    if exclude is None:
        exclude = set()
    if start in exclude or color.get(start) not in (c1, c2):
        return set()
    visited = set()
    queue = deque([start])
    while queue:
        u = queue.popleft()
        if u in visited or u in exclude:
            continue
        if color.get(u) not in (c1, c2):
            continue
        visited.add(u)
        for w in adj.get(u, set()):
            if w not in visited and w not in exclude and color.get(w) in (c1, c2):
                queue.append(w)
    return visited


def can_free_link(adjH, color, link, c1, c2, return_chain=False):
    """Definition 5 at the phantom vertex v whose neighbors are `link`,
    chains in H (v absent)."""
    nb1 = [u for u in link if color.get(u) == c1]
    nb2 = [u for u in link if color.get(u) == c2]
    if not nb1 or not nb2:
        return (True, None) if return_chain else True
    for start in nb1:
        ch = kempe_chain(adjH, color, start, c1, c2)
        if all(u in ch for u in nb1) and not any(u in ch for u in nb2):
            return (True, ch) if return_chain else True
    for start in nb2:
        ch = kempe_chain(adjH, color, start, c1, c2)
        if all(u in ch for u in nb2) and not any(u in ch for u in nb1):
            return (True, ch) if return_chain else True
    return (False, None) if return_chain else False


def tau_link(adjH, color, link):
    return sum(1 for c1, c2 in itertools.combinations(range(4), 2)
               if not can_free_link(adjH, color, link, c1, c2))


def is_strict_link(adjH, color, link, a, b):
    nbrs = [u for u in link if color.get(u) in (a, b)]
    if not nbrs:
        return False
    ch = kempe_chain(adjH, color, nbrs[0], a, b)
    return all(u in ch for u in nbrs)


def do_swap(color, chain, c1, c2):
    nc = dict(color)
    for u in chain:
        if nc[u] == c1:
            nc[u] = c2
        elif nc[u] == c2:
            nc[u] = c1
    return nc


# ------------------------------------------------------------------
# Generators + link cycles (same instrument as Toy 5508)
# ------------------------------------------------------------------

def adj_from_faces(faces):
    adj = defaultdict(set)
    for a, b, c in faces:
        adj[a].update((b, c)); adj[b].update((a, c)); adj[c].update((a, b))
    return dict(adj)


def antiprism_stack(n_rings):
    rings = [[1 + 5 * r + i for i in range(5)] for r in range(n_rings)]
    apex = 1 + 5 * n_rings
    faces = []
    r0 = rings[0]
    for i in range(5):
        faces.append((0, r0[i], r0[(i + 1) % 5]))
    for r in range(n_rings - 1):
        A, B = rings[r], rings[r + 1]
        for i in range(5):
            faces.append((B[i], A[i], A[(i + 1) % 5]))
            faces.append((A[(i + 1) % 5], B[i], B[(i + 1) % 5]))
    last = rings[-1]
    for i in range(5):
        faces.append((apex, last[i], last[(i + 1) % 5]))
    return faces


def stacked_triangulation(n, seed=42):
    rng = random.Random(seed)
    faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    for v in range(4, n):
        fi = rng.randint(0, len(faces) - 1)
        a, b, c = faces[fi]
        faces[fi] = (a, b, v)
        faces.append((b, c, v))
        faces.append((a, c, v))
    return faces


def flipped_triangulation(n, seed=0, flips_factor=6):
    rng = random.Random(seed)
    faces = stacked_triangulation(n, seed=seed + 991)
    faceset = [frozenset(f) for f in faces]
    E = 3 * len(faceset) // 2
    for _ in range(flips_factor * E):
        i = rng.randrange(len(faceset))
        f1 = faceset[i]
        edge = frozenset(rng.sample(sorted(f1), 2))
        js = [j for j, f in enumerate(faceset) if edge < f and j != i]
        if len(js) != 1:
            continue
        j = js[0]
        f2 = faceset[j]
        a, b = sorted(edge)
        c = next(iter(f1 - edge))
        d = next(iter(f2 - edge))
        if c == d:
            continue
        if any(frozenset((c, d)) < f for f in faceset):
            continue
        deg_a = sum(1 for f in faceset if a in f)
        deg_b = sum(1 for f in faceset if b in f)
        if deg_a <= 3 or deg_b <= 3:
            continue
        faceset[i] = frozenset((a, c, d))
        faceset[j] = frozenset((b, c, d))
    return [tuple(sorted(f)) for f in faceset]


def link_cycle(faces, v):
    edges = []
    for f in faces:
        if v in f:
            edges.append(tuple(x for x in f if x != v))
    nbr_adj = defaultdict(list)
    for a, b in edges:
        nbr_adj[a].append(b)
        nbr_adj[b].append(a)
    for u, lst in nbr_adj.items():
        if len(lst) != 2:
            return None
    start = edges[0][0]
    cyc = [start]
    prev, cur = None, start
    while True:
        nxts = [w for w in nbr_adj[cur] if w != prev]
        nxt = nxts[0] if nxts else nbr_adj[cur][0]
        if nxt == cyc[0]:
            break
        cyc.append(nxt)
        prev, cur = cur, nxt
        if len(cyc) > len(nbr_adj) + 1:
            return None
    return cyc if len(cyc) == len(nbr_adj) else None


def greedy_4color(adj, order):
    c = {}
    for v in order:
        used = {c[u] for u in adj.get(v, set()) if u in c}
        for col in range(4):
            if col not in used:
                c[v] = col
                break
        else:
            return None
    return c


def is_proper(adj, color):
    return all(color[u] != color[w] for u in adj for w in adj[u])


# ------------------------------------------------------------------
# H construction (deg-5): (G-v) + fan-from-apex diagonals
# ------------------------------------------------------------------

def build_H5(adjG, cyc, v, apex_pos):
    """H adjacency = adj(G-v) + the 2 fan diagonals from cyc[apex_pos].
    Returns (adjH, diagonals, n_new)."""
    adjH = {u: set(w for w in nb if w != v) for u, nb in adjG.items() if u != v}
    k = apex_pos
    d1 = (cyc[k], cyc[(k + 2) % 5])
    d2 = (cyc[k], cyc[(k + 3) % 5])
    n_new = 0
    for a, b in (d1, d2):
        if b not in adjH[a]:
            adjH[a].add(b)
            adjH[b].add(a)
            n_new += 1
    return adjH, (d1, d2), n_new


def structure_from_link(cyc, color):
    """Bridge geometry from the TRUE cycle + a coloring of the link."""
    nc = [color[u] for u in cyc]
    counts = Counter(nc)
    rep = [c for c, cnt in counts.items() if cnt == 2]
    if len(rep) != 1 or len(counts) != 4:
        return None
    r = rep[0]
    bp = [i for i, c in enumerate(nc) if c == r]
    d = (bp[1] - bp[0]) % 5
    gap = min(d, 5 - d)
    info = {'nc': nc, 'r': r, 'bp': bp, 'gap': gap}
    if gap == 2:
        mid = (bp[0] + 1) % 5 if d == 2 else (bp[1] + 1) % 5
        non_mid = [i for i in range(5) if nc[i] != r and i != mid]
        info.update({'mid_pos': mid, 'mid_color': nc[mid], 'non_mid_pos': non_mid})
    return info


def split_bridge_swaps(adjH, color, cyc, info):
    """All valid Lemma-6 split-bridge swaps: for each non-middle cross-linked
    bridge pair, each bridge copy whose (r,s_i)-chain excludes n_si.
    Returns list of (pair, chain, tag) and a flags dict for lemma checks."""
    r = info['r']
    B = [cyc[i] for i in info['bp']]
    out = []
    flags = {'lemma5_violation': 0, 'crosslinked_nonmid': 0}
    for pos in info['non_mid_pos']:
        x = info['nc'][pos]
        n_x = cyc[pos]
        # operational tangling is given (tau=6); strictness decides cross-link
        if is_strict_link(adjH, color, cyc, r, x):
            continue  # strict, not cross-linked (should not happen non-middle)
        flags['crosslinked_nonmid'] += 1
        ch0 = kempe_chain(adjH, color, B[0], r, x)
        ch1 = kempe_chain(adjH, color, B[1], r, x)
        if B[1] in ch0:
            flags['lemma5_violation'] += 1
            continue
        for bi, ch in ((0, ch0), (1, ch1)):
            if n_x not in ch:
                out.append(((r, x), ch, f'far=B{bi}_pair_r{r}s{x}'))
    return out, flags


def free_and_place(adjG, adjH, color, cyc, v):
    """Second stage: free a color at the link with <=1 swap, place v.
    Returns (final_color_of_G, freed) or (None, None)."""
    link_colors = {color[u] for u in cyc}
    work = dict(color)
    if len(link_colors) < 4:
        freed = next(c for c in range(4) if c not in link_colors)
    else:
        freed = None
        for c1, c2 in itertools.combinations(range(4), 2):
            ok, ch = can_free_link(adjH, work, cyc, c1, c2, return_chain=True)
            if ok and ch is not None:
                work = do_swap(work, ch, c1, c2)
                rem = {work[u] for u in cyc}
                if len(rem) < 4:
                    freed = next(c for c in range(4) if c not in rem)
                    break
                work = dict(color)  # revert, try next pair
        if freed is None:
            return None, None
    final = dict(work)
    final[v] = freed
    # properness in G
    for u in adjG:
        for w in adjG[u]:
            if final[u] == final[w]:
                return None, None
    return final, freed


# ------------------------------------------------------------------
# Populations
# ------------------------------------------------------------------

def build_populations():
    pops = [('icosahedron', antiprism_stack(2)), ('antiprism22', antiprism_stack(4))]
    for n in [12, 15, 18, 20, 25]:
        for gseed in range(15):
            pops.append((f'stacked_n{n}_s{gseed}',
                         stacked_triangulation(n, seed=gseed * 100 + n)))
    for n in [16, 20, 24, 30]:
        for gseed in range(6):
            pops.append((f'flipped_n{n}_s{gseed}',
                         flipped_triangulation(n, seed=gseed)))
    return pops


def hunt_tau6_in_H(pops, n_seeds=300, max_deg5=2):
    """For every (graph, deg-5 v, apex choice, coloring of H): collect
    saturated tau_H=6 cases."""
    cases = []
    h_valid = {'built': 0, 'bad': 0}
    for name, faces in pops:
        adjG = adj_from_faces(faces)
        deg5 = [v for v in sorted(adjG) if len(adjG[v]) == 5]
        for v in deg5[:max_deg5]:
            cyc = link_cycle(faces, v)
            if cyc is None:
                continue
            for apex in range(5):
                adjH, diags, n_new = build_H5(adjG, cyc, v, apex)
                h_valid['built'] += 1
                # H sanity: diagonals present, v absent
                if v in adjH or any(b not in adjH[a] for a, b in diags):
                    h_valid['bad'] += 1
                    continue
                seen = set()
                order_base = sorted(adjH.keys())
                for seed in range(n_seeds):
                    rng = random.Random(seed)
                    order = list(order_base)
                    rng.shuffle(order)
                    col = greedy_4color(adjH, order)
                    if col is None or not is_proper(adjH, col):
                        continue
                    if len({col[u] for u in cyc}) != 4:
                        continue
                    key = tuple(col[u] for u in cyc)
                    if key in seen:
                        continue
                    seen.add(key)
                    if tau_link(adjH, col, cyc) == 6:
                        cases.append((name, faces, adjG, adjH, diags, v, cyc,
                                      apex, col))
    return cases, h_valid


# ------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------

def test_1_H_validity(h_valid):
    print("=" * 70)
    print("Test 1: H construction validity")
    print("=" * 70)
    print(f"\n  H graphs built: {h_valid['built']}, invalid: {h_valid['bad']}")
    t = h_valid['bad'] == 0 and h_valid['built'] > 0
    print(f"\n  [{'PASS' if t else 'FAIL'}] 1. H construction")
    return t


def test_2_3_fan_forced(cases):
    print("\n" + "=" * 70)
    print("Tests 2-3: tau=6 in H ==> apex is the middle singleton; fan geometry")
    print("=" * 70)
    n = 0
    apex_mid = 0
    bad_geom = 0
    apex_hist = Counter()
    for name, faces, adjG, adjH, diags, v, cyc, apex, col in cases:
        info = structure_from_link(cyc, col)
        if info is None or info['gap'] != 2:
            bad_geom += 1
            print(f"  *** EXCEPTION (geometry): {name} v={v} apex={apex} "
                  f"info={'None' if info is None else info['gap']}")
            continue
        n += 1
        rel = 'MIDDLE' if apex == info['mid_pos'] else (
            'BRIDGE' if apex in info['bp'] else 'NON-MID-SINGLETON')
        apex_hist[rel] += 1
        if apex == info['mid_pos']:
            apex_mid += 1
        else:
            print(f"  *** EXCEPTION (i): tau=6 with apex={rel} at {name} v={v} "
                  f"apex_pos={apex} mid_pos={info['mid_pos']} nc={info['nc']}")
        # fan geometry: bridge vertices are not diagonal endpoints
        B = {cyc[i] for i in info['bp']}
        for a, b in diags:
            if a in B or b in B:
                bad_geom += 1
                print(f"  *** EXCEPTION (geom): diagonal touches bridge at "
                      f"{name} v={v}")
    print(f"\n  tau=6-in-H cases: {n}   apex relation: {dict(apex_hist)}")
    t2 = n > 0 and apex_mid == n
    t3 = n > 0 and bad_geom == 0
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Prediction (i): apex = s_M "
          f"({apex_mid}/{n})")
    print(f"  [{'PASS' if t3 else 'FAIL'}] 3. Fan geometry clean "
          f"({bad_geom} exceptions)")
    return t2, t3


def test_4_middle_strict_H(cases):
    print("\n" + "=" * 70)
    print("Test 4: Middle-strict holds in H at tau=6")
    print("=" * 70)
    n = 0
    ok = 0
    for name, faces, adjG, adjH, diags, v, cyc, apex, col in cases:
        info = structure_from_link(cyc, col)
        if info is None or info['gap'] != 2:
            continue
        n += 1
        if is_strict_link(adjH, col, cyc, info['r'], info['mid_color']):
            ok += 1
        else:
            print(f"  *** EXCEPTION: middle NOT strict in H at {name} v={v}")
    t = n > 0 and ok == n
    print(f"\n  Middle strict in H: {ok}/{n}")
    print(f"\n  [{'PASS' if t else 'FAIL'}] 4. Middle-strict in H")
    return t


def test_5_6_7_swap_pipeline(cases):
    print("\n" + "=" * 70)
    print("Tests 5-7: split-bridge swap exists; ALL drop tau<=5; second stage")
    print("=" * 70)
    n = 0
    have_swap = 0
    all_drop = 0
    completed = 0
    total_swaps = 0
    swap_fail = 0
    l5_viol = 0
    for name, faces, adjG, adjH, diags, v, cyc, apex, col in cases:
        info = structure_from_link(cyc, col)
        if info is None or info['gap'] != 2:
            continue
        n += 1
        swaps, flags = split_bridge_swaps(adjH, col, cyc, info)
        l5_viol += flags['lemma5_violation']
        if not swaps:
            print(f"  *** EXCEPTION (Lemma 6): NO split-bridge swap at "
                  f"{name} v={v} apex={apex}")
            continue
        have_swap += 1
        case_all_drop = True
        one_completed = False
        for (c1, c2), ch, tag in swaps:
            total_swaps += 1
            nc = do_swap(col, ch, c1, c2)
            if not is_proper(adjH, nc):
                swap_fail += 1
                case_all_drop = False
                print(f"  *** EXCEPTION: swap breaks properness {name} v={v} {tag}")
                continue
            t_after = tau_link(adjH, nc, cyc)
            if t_after > 5:
                swap_fail += 1
                case_all_drop = False
                print(f"  *** EXCEPTION (ii): post-swap tau={t_after} at "
                      f"{name} v={v} apex={apex} {tag}")
                continue
            if not one_completed:
                final, freed = free_and_place(adjG, adjH, nc, cyc, v)
                if final is not None:
                    one_completed = True
                else:
                    print(f"  *** EXCEPTION (iii): cannot free/place at "
                          f"{name} v={v} {tag}")
        if case_all_drop:
            all_drop += 1
        if one_completed:
            completed += 1
    print(f"\n  Usable tau=6 cases: {n}")
    print(f"  Split-bridge swap exists: {have_swap}/{n}   "
          f"(Lemma 5 violations: {l5_viol})")
    print(f"  All swaps drop tau<=5:    {all_drop}/{n}   "
          f"({total_swaps} swaps, {swap_fail} failures)")
    print(f"  Second stage completes:   {completed}/{n}")
    t5 = n > 0 and have_swap == n and l5_viol == 0
    t6 = n > 0 and all_drop == n
    t7 = n > 0 and completed == n
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. Lemma 6 in H (swap exists)")
    print(f"  [{'PASS' if t6 else 'FAIL'}] 6. Prediction (ii): tau drops")
    print(f"  [{'PASS' if t7 else 'FAIL'}] 7. Prediction (iii): completion")
    return t5, t6, t7


def test_8_deg4_probe(pops, n_seeds=250):
    print("\n" + "=" * 70)
    print("Test 8: DEG-4 HOLE PROBE (Elie addition — repair-leak hunt)")
    print("=" * 70)
    checked = 0
    stuck1 = []          # no single swap frees
    stuck2 = 0           # not even two swaps free
    for name, faces in pops:
        adjG = adj_from_faces(faces)
        deg4 = [v for v in sorted(adjG) if len(adjG[v]) == 4]
        for v in deg4[:2]:
            cyc = link_cycle(faces, v)
            if cyc is None or len(cyc) != 4:
                continue
            for dpos in range(2):  # diagonal (w0,w2) or (w1,w3)
                adjH = {u: set(w for w in nb if w != v)
                        for u, nb in adjG.items() if u != v}
                a, b = cyc[dpos], cyc[dpos + 2]
                if b not in adjH[a]:
                    adjH[a].add(b)
                    adjH[b].add(a)
                seen = set()
                base = sorted(adjH.keys())
                for seed in range(n_seeds):
                    rng = random.Random(seed)
                    order = list(base)
                    rng.shuffle(order)
                    col = greedy_4color(adjH, order)
                    if col is None or not is_proper(adjH, col):
                        continue
                    if len({col[u] for u in cyc}) != 4:
                        continue
                    key = (dpos, tuple(col[u] for u in cyc))
                    if key in seen:
                        continue
                    seen.add(key)
                    checked += 1
                    freeable = any(can_free_link(adjH, col, cyc, c1, c2)
                                   for c1, c2 in
                                   itertools.combinations(range(4), 2))
                    if freeable:
                        continue
                    stuck1.append((name, v, dpos))
                    print(f"  *** SINGLE-SWAP STUCK: {name} v={v} "
                          f"diag={dpos} link_colors="
                          f"{[col[u] for u in cyc]}")
                    # two-swap search: every chain swap, then re-test
                    resolved = False
                    for c1, c2 in itertools.combinations(range(4), 2):
                        comps = []
                        seen_u = set()
                        for u in adjH:
                            if u in seen_u or col.get(u) not in (c1, c2):
                                continue
                            comp = kempe_chain(adjH, col, u, c1, c2)
                            seen_u |= comp
                            comps.append(comp)
                        for comp in comps:
                            nc = do_swap(col, comp, c1, c2)
                            if len({nc[u] for u in cyc}) < 4 or any(
                                    can_free_link(adjH, nc, cyc, d1, d2)
                                    for d1, d2 in
                                    itertools.combinations(range(4), 2)):
                                resolved = True
                                break
                        if resolved:
                            break
                    if not resolved:
                        stuck2 += 1
                        print(f"  *** TWO-SWAP STUCK (HARD LEAK): {name} v={v}")
    print(f"\n  Saturated deg-4-in-H colorings checked: {checked}")
    print(f"  Single-swap stuck: {len(stuck1)}   two-swap stuck: {stuck2}")
    if stuck1:
        print("  ==> K1832's 'triangulate the smaller hole likewise' is NOT "
              "a one-liner: the classical deg-4 Kempe argument does not "
              "transfer verbatim to H.")
    t = checked > 0
    print(f"\n  [{'PASS' if t else 'FAIL'}] 8. Probe executed "
          f"(finding: {len(stuck1)} single-swap-stuck, {stuck2} hard)")
    return t, len(stuck1), stuck2


def color_by_H_induction(faces, depth=0):
    """The repaired induction, end-to-end. Returns (coloring, stats) or
    (None, stats) if stuck."""
    stats = Counter()
    adj = adj_from_faces(faces)
    if len(adj) <= 4:
        return {u: i for i, u in enumerate(sorted(adj))}, stats
    v = min(adj, key=lambda u: len(adj[u]))
    deg = len(adj[v])
    cyc = link_cycle(faces, v)
    if cyc is None:
        stats['no_link'] += 1
        return None, stats
    star = [f for f in faces if v in f]
    rest = [f for f in faces if v not in f]
    adjGv = {u: set(w for w in nb if w != v) for u, nb in adj.items() if u != v}

    def new_diag(a, b):
        return b not in adjGv[a]

    if deg == 3:
        facesH = rest + [tuple(cyc)]
        diags = []
    elif deg == 4:
        choice = None
        for dpos in range(2):
            a, b = cyc[dpos], cyc[dpos + 2]
            if new_diag(a, b):
                choice = dpos
                break
        if choice is None:
            stats['deg4_no_new_diag_skip'] += 1
            return None, stats
        a, b = cyc[choice], cyc[choice + 2]
        w1, w3 = cyc[(choice + 1) % 4], cyc[(choice + 3) % 4]
        facesH = rest + [(a, w1, b), (a, w3, b)]
        diags = [(a, b)]
    else:  # deg == 5
        choice = None
        for apex in range(5):
            d1 = (cyc[apex], cyc[(apex + 2) % 5])
            d2 = (cyc[apex], cyc[(apex + 3) % 5])
            if new_diag(*d1) and new_diag(*d2):
                choice = apex
                break
        if choice is None:
            stats['deg5_no_new_diags_skip'] += 1
            return None, stats
        k = choice
        facesH = rest + [(cyc[k], cyc[(k + 1) % 5], cyc[(k + 2) % 5]),
                         (cyc[k], cyc[(k + 2) % 5], cyc[(k + 3) % 5]),
                         (cyc[k], cyc[(k + 3) % 5], cyc[(k + 4) % 5])]
        diags = [(cyc[k], cyc[(k + 2) % 5]), (cyc[k], cyc[(k + 3) % 5])]

    colH, sub = color_by_H_induction(facesH, depth + 1)
    stats.update(sub)
    if colH is None:
        return None, stats
    adjH = adj_from_faces(facesH)
    link_cols = {colH[u] for u in cyc}
    if len(link_cols) < 4:
        freed = next(c for c in range(4) if c not in link_cols)
        colG = dict(colH)
        colG[v] = freed
        return colG, stats
    stats[f'deg{deg}_saturated'] += 1
    work = dict(colH)
    t = tau_link(adjH, work, cyc) if deg == 5 else None
    if deg == 5 and t == 6:
        stats['tau6_branch'] += 1
        info = structure_from_link(cyc, work)
        if info is None or info['gap'] != 2:
            stats['tau6_bad_structure'] += 1
            return None, stats
        swaps, flags = split_bridge_swaps(adjH, work, cyc, info)
        if not swaps:
            stats['tau6_no_swap_STUCK'] += 1
            return None, stats
        (c1, c2), ch, tag = swaps[0]
        work = do_swap(work, ch, c1, c2)
    # free a color with <=1 swap
    link_now = {work[u] for u in cyc}
    if len(link_now) == 4:
        freed = None
        for c1, c2 in itertools.combinations(range(4), 2):
            ok, ch = can_free_link(adjH, work, cyc, c1, c2, return_chain=True)
            if ok and ch is not None:
                cand = do_swap(work, ch, c1, c2)
                if len({cand[u] for u in cyc}) < 4:
                    work = cand
                    freed = next(c for c in range(4)
                                 if c not in {cand[u] for u in cyc})
                    break
        if freed is None:
            stats[f'deg{deg}_STUCK'] += 1
            return None, stats
    else:
        freed = next(c for c in range(4) if c not in link_now)
    colG = dict(work)
    colG[v] = freed
    return colG, stats


def test_9_end_to_end():
    print("\n" + "=" * 70)
    print("Test 9: End-to-end repaired H-induction on whole triangulations")
    print("=" * 70)
    total = 0
    proper = 0
    stuck = 0
    skipped = 0
    agg = Counter()
    graphs = [('icosahedron', antiprism_stack(2)), ('antiprism22', antiprism_stack(4)),
              ('antiprism32', antiprism_stack(6))]
    for n in [15, 20, 30, 40, 60]:
        for s in range(10):
            graphs.append((f'stacked_n{n}_s{s}', stacked_triangulation(n, seed=s * 7 + n)))
    for n in [16, 20, 28, 40]:
        for s in range(5):
            graphs.append((f'flipped_n{n}_s{s}', flipped_triangulation(n, seed=s + 50)))
    for name, faces in graphs:
        adj = adj_from_faces(faces)
        col, stats = color_by_H_induction(faces)
        agg.update(stats)
        total += 1
        if col is None:
            if any('skip' in k for k in stats):
                skipped += 1
            else:
                stuck += 1
                print(f"  *** STUCK: {name}  stats={dict(stats)}")
            continue
        if all(col[u] != col[w] for u in adj for w in adj[u]):
            proper += 1
        else:
            stuck += 1
            print(f"  *** IMPROPER: {name}")
    print(f"\n  Graphs: {total}  properly 4-colored: {proper}  "
          f"stuck/improper: {stuck}  skipped (pre-existing diagonals): {skipped}")
    print(f"  Branch stats: {dict(agg)}")
    if agg.get('tau6_branch', 0) == 0:
        print("  NOTE: tau=6 branch never fired end-to-end here; that branch "
              "is covered by the directed hunt (Tests 2-7).")
    t = stuck == 0 and proper > 0
    print(f"\n  [{'PASS' if t else 'FAIL'}] 9. End-to-end induction")
    return t


# ------------------------------------------------------------------
# Post-mortem: classify the failures and brute-force the witnesses
# ------------------------------------------------------------------

def post_mortem():
    """Not scored — the analysis that explains the FAILs above.

    Classification key: (apex relation, tau_s in H, swap outcome).
    Findings this section verifies by exhaustive swap enumeration:
      - Lemma 3 (tau_s <= 4 at tau=6) FAILS in H: tau_s = 5 and even 6 occur,
        including at the CORRECT middle apex. Root cause: Lemma 3's Jordan
        curve closes THROUGH v, and v does not exist in H — the fan diagonals
        are drawn where v used to sit. tau=6-in-H is a different population
        than tau=6-in-(G-v) (P1's tau_s=4 862/862 does not cover it).
      - tau_s = 6 cases (icosahedron): ALL pairs strict, no cross-link exists,
        the split-bridge machinery has nothing to act on (Lemma 4 dies with
        Lemma 3).
      - Witnesses below are stuck under exhaustive 1-, 2- AND 3-swap search.
    """
    print("\n" + "=" * 70)
    print("POST-MORTEM (not scored): failure classification + hard witnesses")
    print("=" * 70)
    pops = [('icosahedron', antiprism_stack(2)), ('antiprism22', antiprism_stack(4))]
    for n in [12, 15, 18, 20]:
        for gseed in range(8):
            pops.append((f'stacked_n{n}_s{gseed}',
                         stacked_triangulation(n, seed=gseed * 100 + n)))
    cases, _ = hunt_tau6_in_H(pops, n_seeds=200, max_deg5=2)
    stats = Counter()
    for name, faces, adjG, adjH, diags, v, cyc, apex, col in cases:
        info = structure_from_link(cyc, col)
        if info is None or info['gap'] != 2:
            continue
        rel = 'MID' if apex == info['mid_pos'] else 'NONMID'
        ts = sum(1 for a, b in itertools.combinations(range(4), 2)
                 if is_strict_link(adjH, col, cyc, a, b))
        swaps, _fl = split_bridge_swaps(adjH, col, cyc, info)
        nd = sum(1 for (c1, c2), ch, tag in swaps
                 if is_proper(adjH, do_swap(col, ch, c1, c2))
                 and tau_link(adjH, do_swap(col, ch, c1, c2), cyc) <= 5)
        out = ('no_swap' if not swaps else
               'all_drop' if nd == len(swaps) else
               'some_drop' if nd else 'none_drop')
        stats[(rel, ts, out)] += 1
    for k in sorted(stats):
        print(f"  {k}: {stats[k]}")
    print("  Only (MID, tau_s=4, all_drop) is the configuration K1832 "
          "Section 3 analyzed; every other row is outside its lemma chain.")

    def all_swaps(adjH, col):
        out = []
        for a, b in itertools.combinations(range(4), 2):
            seen = set()
            for u in adjH:
                if u in seen or col.get(u) not in (a, b):
                    continue
                c = kempe_chain(adjH, col, u, a, b)
                seen |= c
                out.append((a, b, frozenset(c)))
        return out

    def rescue_depth(adjH, col, cyc, depth):
        seen = {tuple(sorted(col.items()))}
        q = deque([(col, 0)])
        while q:
            c, d = q.popleft()
            if len({c[u] for u in cyc}) < 4:
                return d
            if d == depth:
                continue
            for a, b, comp in all_swaps(adjH, c):
                nc = do_swap(c, comp, a, b)
                key = tuple(sorted(nc.items()))
                if key not in seen:
                    seen.add(key)
                    q.append((nc, d + 1))
        return None

    witnesses = [('MID-apex tau_s=5', 4, 0, 1, [2, 0, 2, 3, 1]),
                 ('MID-apex tau_s=6 icosahedron', 2, 0, 0, [1, 3, 0, 2, 3])]
    for label, rings, v, apex, target in witnesses:
        faces = antiprism_stack(rings)
        adjG = adj_from_faces(faces)
        cyc = link_cycle(faces, v)
        adjH, diags, _n = build_H5(adjG, cyc, v, apex)
        found = None
        for seed in range(300):
            rng = random.Random(seed)
            order = sorted(adjH)
            rng.shuffle(order)
            col = greedy_4color(adjH, order)
            if (col and is_proper(adjH, col)
                    and [col[u] for u in cyc] == target
                    and tau_link(adjH, col, cyc) == 6):
                found = col
                break
        if found is None:
            print(f"  {label}: witness not refound (seed drift?)")
            continue
        r = rescue_depth(adjH, found, cyc, 3)
        print(f"  WITNESS {label}: link={target} diagonals={diags} "
              f"rescue depth within 3 swaps: {r} "
              f"{'(HARD OBSTRUCTION)' if r is None else ''}")


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5509 — P2: The H-repair pipeline (K1832 Section 3/6)")
    print("=" * 70)

    pops = build_populations()
    print(f"\n  ... hunting tau=6 in H across {len(pops)} graphs x 5 apex "
          f"choices (slow part)")
    cases, h_valid = hunt_tau6_in_H(pops)
    fam = Counter(name.split('_')[0] for name, *_ in cases)
    print(f"  tau=6-in-H cases found: {len(cases)}  by family: {dict(fam)}")

    t1 = test_1_H_validity(h_valid)
    t2, t3 = test_2_3_fan_forced(cases)
    t4 = test_4_middle_strict_H(cases)
    t5, t6, t7 = test_5_6_7_swap_pipeline(cases)
    t8, n_stuck1, n_stuck2 = test_8_deg4_probe(pops)
    t9 = test_9_end_to_end()

    results = [t1, t2, t3, t4, t5, t6, t7, t8, t9]
    passed = sum(results)
    print(f"\n{'=' * 70}")
    print(f"Toy 5509 -- SCORE: {passed}/{len(results)}")
    print(f"{'=' * 70}")
    if passed != len(results):
        for i, r in enumerate(results, 1):
            if not r:
                print(f"  Test {i}: FAIL")
    print(f"\nDeg-4 probe finding: {n_stuck1} single-swap-stuck, "
          f"{n_stuck2} two-swap-stuck (0/0 = classical argument transfers).")

    post_mortem()
