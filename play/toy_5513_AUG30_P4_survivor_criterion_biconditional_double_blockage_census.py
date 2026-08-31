#!/usr/bin/env python3
"""
Toy 5513 — P4 (K1832 round 2): LYRA'S SURVIVOR CRITERION, TESTED BOTH WAYS,
AND THE DOUBLE-BLOCKAGE CENSUS

Lyra's Lemma C (her proved direction): if some pre-swap (s_M,s_x)-path from
n_sM to n_sx avoids the swap chain C_x, the path survives the swap, makes
(s_x, s_M) strict post-swap, and Lemma 3 (TRUE in G−v) forces tau <= 5.

Operationalization (exact): n_sM and n_sx always share a (s_M,s_x)-Kempe
component at tau=6 (singleton pairs are strict). blocked(x) := n_sM and n_sx
are DISCONNECTED in [the (s_M,s_x)-bichromatic subgraph of G−v minus the
vertices of C_x]. Lemma C says: NOT blocked(x) ==> swap-x drops tau.
Contrapositive: swap-x fails ==> blocked(x).

Her residue: the double-blockage configuration, blocked(i) AND blocked(j),
which she could not kill by Jordan/counting. Toy 5512 already showed
double-FAILS exist in profusion on the Kempe-killer gallery (601/1782), and
double-fail ==> double-blockage by the contrapositive — so the residue is
INHABITED and no impossibility proof can close it. This toy measures the
criterion's exactness and the census on both populations.

PRE-REGISTERED, each can-fail:
  A. Lemma C sufficiency: not-blocked(x) ==> swap-x drops tau. 100%.
     (An exception is a bug in her PROOF — highest-value output.)
  B. Mechanism: not-blocked(x) ==> post-swap (s_x, s_M) strict. 100%.
  C. Contrapositive: every swap-x failure has blocked(x) AND post-swap
     (s_x, s_M) non-strict. 100%.
  D. Elie's exactness hypothesis (registered now, before the run):
     blocked(x) <==> swap-x fails — i.e., her sufficient criterion is
     EXACT on real populations. If true, double-blocked == double-fail
     and the census below is the residue's exact inhabitant count.
  E. Census: double-blockage on the extended random population (Toy 5511's
     862) vs the gallery (Toy 5512's 1782). Reported; containment
     double-fail ==> double-blocked verified 100%.

Populations: extended (icosahedron, antiprism22, stacked, flipped — the 862)
+ gallery (Errera, Kittell sampled; Fritsch EXHAUSTIVE — the 1782).

TESTS (X/Y): 1=A, 2=B, 3=C, 4=D, 5=E-containment, 6=census reported with
per-population split.

Elie, 2026-08-30. Millennium week, 4-Color round 2. 6 tests.
"""

import itertools
import random
from collections import defaultdict, deque, Counter

# ---------------------------------------------------------------- machinery


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


def can_free_color(adj, color, v, c1, c2):
    nb1 = [u for u in adj[v] if color.get(u) == c1]
    nb2 = [u for u in adj[v] if color.get(u) == c2]
    if not nb1 or not nb2:
        return True
    for start in nb1:
        ch = kempe_chain(adj, color, start, c1, c2, exclude={v})
        if all(u in ch for u in nb1) and not any(u in ch for u in nb2):
            return True
    for start in nb2:
        ch = kempe_chain(adj, color, start, c1, c2, exclude={v})
        if all(u in ch for u in nb2) and not any(u in ch for u in nb1):
            return True
    return False


def operational_tau(adj, color, v):
    return sum(1 for a, b in itertools.combinations(range(4), 2)
               if not can_free_color(adj, color, v, a, b))


def is_strict(adj, color, v, a, b):
    nbrs = [u for u in adj[v] if color.get(u) in (a, b)]
    if not nbrs:
        return False
    ch = kempe_chain(adj, color, nbrs[0], a, b, exclude={v})
    return all(u in ch for u in nbrs)


def do_swap(color, chain, c1, c2):
    nc = dict(color)
    for u in chain:
        if nc[u] == c1:
            nc[u] = c2
        elif nc[u] == c2:
            nc[u] = c1
    return nc


def is_proper(adj, color, skip=None):
    for u in adj:
        if u == skip:
            continue
        for w in adj[u]:
            if w == skip:
                continue
            if u in color and w in color and color[u] == color[w]:
                return False
    return True


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


# ---------------------------------------------------------------- graphs

def adj_from_faces(faces):
    adj = defaultdict(set)
    for x, y, z in faces:
        adj[x].update((y, z)); adj[y].update((x, z)); adj[z].update((x, y))
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


def errera_adj():
    d = {0: [1, 7, 14, 15, 16], 1: [2, 9, 14, 15], 2: [3, 8, 9, 10, 14],
         3: [4, 9, 10, 11], 4: [5, 10, 11, 12], 5: [6, 11, 12, 13],
         6: [7, 8, 12, 13, 16], 7: [13, 15, 16], 8: [10, 12, 14, 16],
         9: [11, 13, 15], 10: [12], 11: [13], 13: [15], 14: [16]}
    adj = defaultdict(set)
    for u, lst in d.items():
        for w in lst:
            adj[u].add(w)
            adj[w].add(u)
    return dict(adj)


def kittell_adj():
    d = {0: [1, 2, 4, 5, 6, 7], 1: [0, 2, 7, 10, 11, 13],
         2: [0, 1, 11, 4, 14], 3: [16, 12, 4, 5, 14], 4: [0, 2, 3, 5, 14],
         5: [0, 16, 3, 4, 6], 6: [0, 5, 7, 15, 16, 17, 18],
         7: [0, 1, 6, 8, 13, 18], 8: [9, 18, 19, 13, 7],
         9: [8, 10, 19, 20, 13], 10: [1, 9, 11, 13, 20, 21],
         11: [1, 2, 10, 12, 14, 15, 21], 12: [11, 16, 3, 14, 15],
         13: [8, 1, 10, 9, 7], 14: [11, 12, 2, 3, 4],
         15: [6, 11, 12, 16, 17, 21, 22], 16: [3, 12, 5, 6, 15],
         17: [18, 19, 22, 6, 15], 18: [8, 17, 19, 6, 7],
         19: [8, 9, 17, 18, 20, 22], 20: [9, 10, 19, 21, 22],
         21: [10, 11, 20, 22, 15], 22: [17, 19, 20, 21, 15]}
    adj = defaultdict(set)
    for u, lst in d.items():
        for w in lst:
            adj[u].add(w)
            adj[w].add(u)
    return dict(adj)


def fritsch_faces():
    t = [0, 1, 2]
    b = [3, 4, 5]
    a = [6, 7, 8]
    faces = [(t[0], t[1], t[2]), (b[0], b[1], b[2])]
    for i in range(3):
        j = (i + 1) % 3
        faces += [(a[i], t[i], t[j]), (a[i], t[j], b[j]),
                  (a[i], b[j], b[i]), (a[i], b[i], t[i])]
    return faces


def faces_from_adj_triangulation(adj):
    tris = []
    vs = sorted(adj)
    for u in vs:
        for w in adj[u]:
            if w <= u:
                continue
            for x in adj[u] & adj[w]:
                if x <= w:
                    continue
                tris.append((u, w, x))
    edge_count = Counter()
    for f in tris:
        p, q, r = f
        for e in ((p, q), (q, r), (p, r)):
            edge_count[frozenset(e)] += 1
    if any(cnt != 2 for cnt in edge_count.values()):
        return None
    return tris


def link_cycle(faces, v):
    edges = []
    for f in faces:
        if v in f:
            edges.append(tuple(x for x in f if x != v))
    nbr_adj = defaultdict(list)
    for p, q in edges:
        nbr_adj[p].append(q)
        nbr_adj[q].append(p)
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


def structure_true(faces, adj, color, v):
    cyc = link_cycle(faces, v)
    if cyc is None or len(cyc) != 5:
        return None
    nc = [color[u] for u in cyc]
    counts = Counter(nc)
    rep = [c for c, cnt in counts.items() if cnt == 2]
    if len(rep) != 1 or len(counts) != 4:
        return None
    r = rep[0]
    bp = [i for i, c in enumerate(nc) if c == r]
    d = (bp[1] - bp[0]) % 5
    gap = min(d, 5 - d)
    if gap != 2:
        return None
    mid = (bp[0] + 1) % 5 if d == 2 else (bp[1] + 1) % 5
    non_mid = [i for i in range(5) if nc[i] != r and i != mid]
    return {'cyc': cyc, 'nc': nc, 'r': r, 'bp': bp, 'gap': gap,
            'mid_pos': mid, 'mid_color': nc[mid], 'non_mid_pos': non_mid}


def forced_swap_for(adj, color, v, info, q):
    """The forced split-bridge swap for non-middle position q. Returns
    (pair, chain) or None if the pair is strict (not cross-linked)."""
    cyc, nc, r = info['cyc'], info['nc'], info['r']
    x = nc[q]
    if is_strict(adj, color, v, r, x):
        return None
    dists = [min((q - p) % 5, (p - q) % 5) for p in info['bp']]
    far_p = info['bp'][0] if dists[0] == 2 else info['bp'][1]
    ch = kempe_chain(adj, color, cyc[far_p], r, x, exclude={v})
    return (r, x), ch


def blocked(adj, color, v, info, q, chain):
    """blocked(x): n_sM and n_sx disconnected in the (s_M,s_x)-bichromatic
    subgraph of G−v minus the swap chain's vertices."""
    cyc, nc = info['cyc'], info['nc']
    sM_v = cyc[info['mid_pos']]
    sM_c = info['mid_color']
    x_c = nc[q]
    n_x = cyc[q]
    avoid = set(chain) | {v}
    if sM_v in avoid or n_x in avoid:
        return True
    comp = kempe_chain(adj, color, sM_v, sM_c, x_c, exclude=avoid)
    return n_x not in comp


# ---------------------------------------------------------------- scans

def sampled_colorings(adj, tv, n_seeds):
    others = [x for x in sorted(adj) if x != tv]
    seen = set()
    out = []
    for seed in range(n_seeds):
        rng = random.Random(seed)
        order = list(others)
        rng.shuffle(order)
        c = greedy_4color(adj, order)
        if c is None or not is_proper(adj, c, skip=tv):
            continue
        if len({c[u] for u in adj[tv]}) != 4:
            continue
        key = tuple(c[u] for u in sorted(adj) if u != tv)
        if key in seen:
            continue
        seen.add(key)
        out.append(c)
    return out


def exhaustive_colorings(adj, tv):
    others = [x for x in sorted(adj) if x != tv]
    out = []
    col = {}

    def bt(i):
        if i == len(others):
            if len({col[u] for u in adj[tv]}) == 4:
                out.append(dict(col))
            return
        u = others[i]
        for c in range(4):
            if all(col.get(w) != c for w in adj[u] if w != tv):
                col[u] = c
                bt(i + 1)
                del col[u]

    bt(0)
    return out


def collect_cases():
    """(population_tag, name, faces, adj, tv, coloring, info)"""
    cases = []
    pops = [('random', 'icosahedron', antiprism_stack(2)),
            ('random', 'antiprism22', antiprism_stack(4))]
    for n in [12, 15, 18, 20, 25, 30]:
        for gseed in range(25):
            pops.append(('random', f'stacked_n{n}_s{gseed}',
                         stacked_triangulation(n, seed=gseed * 100 + n)))
    for n in [16, 20, 24, 30, 40]:
        for gseed in range(8):
            pops.append(('random', f'flipped_n{n}_s{gseed}',
                         flipped_triangulation(n, seed=gseed)))
    for tag, name, faces in pops:
        adj = adj_from_faces(faces)
        deg5 = [x for x in sorted(adj) if len(adj[x]) == 5]
        for tv in deg5[:3]:
            for c in sampled_colorings(adj, tv, 400):
                if operational_tau(adj, c, tv) != 6:
                    continue
                info = structure_true(faces, adj, c, tv)
                if info is not None:
                    cases.append((tag, name, adj, tv, c, info))
    # gallery
    err = errera_adj()
    kit = kittell_adj()
    fri_faces = fritsch_faces()
    fri = adj_from_faces(fri_faces)
    gal = [('Errera', faces_from_adj_triangulation(err), err, 'sampled'),
           ('Kittell', faces_from_adj_triangulation(kit), kit, 'sampled'),
           ('Fritsch', fri_faces, fri, 'exhaustive')]
    for name, faces, adj, mode in gal:
        deg5 = [x for x in sorted(adj) if len(adj[x]) == 5]
        for tv in deg5:
            cols = (exhaustive_colorings(adj, tv) if mode == 'exhaustive'
                    else sampled_colorings(adj, tv, 3000))
            for c in cols:
                if operational_tau(adj, c, tv) != 6:
                    continue
                info = structure_true(faces, adj, c, tv)
                if info is not None:
                    cases.append(('gallery', name, adj, tv, c, info))
    return cases


# ---------------------------------------------------------------- main

if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5513 — P4: survivor criterion both ways + double-blockage census")
    print("=" * 70)

    print("\n  ... collecting tau=6 cases on both populations (slow part)")
    cases = collect_cases()
    tags = Counter(tag for tag, *_ in cases)
    print(f"  cases: {dict(tags)}  total {len(cases)}")

    nA = nA_ok = 0          # not-blocked -> tau drops
    nB = nB_ok = 0          # not-blocked -> post-swap (s_x,s_M) strict
    nC = nC_ok = 0          # fail -> blocked & post nonstrict
    nD = nD_ok = 0          # blocked <-> fail
    contain_ok = True
    census = Counter()
    exceptionsA = []
    for tag, name, adj, tv, c, info in cases:
        per_swap = []
        for q in info['non_mid_pos']:
            fs = forced_swap_for(adj, c, tv, info, q)
            if fs is None:
                print(f"  *** STRUCTURE EXCEPTION (non-middle strict) "
                      f"{name} v={tv}")
                continue
            (r, x), ch = fs
            blk = blocked(adj, c, tv, info, q, ch)
            nc2 = do_swap(c, ch, r, x)
            t_after = operational_tau(adj, nc2, tv)
            fail = t_after > 5
            sM_c = info['mid_color']
            post_strict = is_strict(adj, nc2, tv, x, sM_c)
            per_swap.append((blk, fail))
            # A
            if not blk:
                nA += 1
                if not fail:
                    nA_ok += 1
                else:
                    exceptionsA.append((name, tv, q))
                    print(f"  *** LEMMA-C SUFFICIENCY EXCEPTION {name} v={tv} "
                          f"q={q} — not blocked yet swap fails")
                # B
                nB += 1
                if post_strict:
                    nB_ok += 1
                else:
                    print(f"  *** MECHANISM EXCEPTION {name} v={tv} q={q} — "
                          f"not blocked yet (s_x,s_M) not strict post-swap")
            # C
            if fail:
                nC += 1
                if blk and not post_strict:
                    nC_ok += 1
                else:
                    print(f"  *** CONTRAPOSITIVE EXCEPTION {name} v={tv} q={q}")
            # D
            nD += 1
            if blk == fail:
                nD_ok += 1
        if len(per_swap) == 2:
            dblk = per_swap[0][0] and per_swap[1][0]
            dfail = per_swap[0][1] and per_swap[1][1]
            census[(tag, 'double_blocked')] += dblk
            census[(tag, 'double_fail')] += dfail
            census[(tag, 'cases')] += 1
            if dfail and not dblk:
                contain_ok = False
                print(f"  *** CONTAINMENT VIOLATION {name} v={tv}")

    print(f"\n  A. Lemma C sufficiency:      {nA_ok}/{nA}")
    print(f"  B. Mechanism (post strict):  {nB_ok}/{nB}")
    print(f"  C. Contrapositive on fails:  {nC_ok}/{nC}")
    print(f"  D. blocked <-> fail exact:   {nD_ok}/{nD}")
    print(f"  E. census:")
    for tag in ('random', 'gallery'):
        print(f"     {tag}: cases={census[(tag, 'cases')]} "
              f"double_blocked={census[(tag, 'double_blocked')]} "
              f"double_fail={census[(tag, 'double_fail')]}")

    t1 = nA > 0 and nA_ok == nA
    t2 = nB > 0 and nB_ok == nB
    t3 = nC > 0 and nC_ok == nC
    t4 = nD > 0 and nD_ok == nD
    t5 = contain_ok
    t6 = census[('gallery', 'cases')] > 0 and census[('random', 'cases')] > 0
    for i, (t, lab) in enumerate([
            (t1, "Lemma C sufficiency 100% (her proved direction)"),
            (t2, "Mechanism: survivor path -> post-swap strict 100%"),
            (t3, "Contrapositive on failures 100%"),
            (t4, "Exactness: blocked <-> fail (Elie hypothesis)"),
            (t5, "Containment double-fail -> double-blocked 100%"),
            (t6, "Census on both populations reported")], 1):
        print(f"  [{'PASS' if t else 'FAIL'}] {i}. {lab}")

    results = [t1, t2, t3, t4, t5, t6]
    passed = sum(results)
    print(f"\n{'=' * 70}")
    print(f"Toy 5513 -- SCORE: {passed}/{len(results)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(results, 1):
        if not r:
            print(f"  Test {i}: FAIL")
    print("\nReading: the double-blockage residue is INHABITED (gallery"
          " census above) — Lyra's route 1 cannot close by impossibility;"
          " the criterion's exactness (test 4) tells her whether blocked-ness"
          " is the right wall to attack or only a sufficient shadow of it.")
