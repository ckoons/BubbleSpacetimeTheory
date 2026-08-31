#!/usr/bin/env python3
"""
Toy 5508 — P1 (K1832 Section 6, pre-registered): MIDDLE-STRICT LEMMA ON TRIANGULATIONS

Keeper's Lemma 4.1 (Middle-Strict): in a triangulation, at any operational-tau=6
saturated degree-5 vertex, the middle bridge pair (r, s_M) is ALWAYS strictly
tangled; consequently tau_s = exactly 4 with the strict bridge slot ALWAYS the
middle pair, and non-middle bridge pairs are NEVER strict (they are the
cross-linked ones).

PRE-REGISTERED PREDICTION (can-fail): strict bridge slot = middle pair in 100%
of tau=6 cases on TRIANGULATIONS. Any non-middle strict slot on a triangulation
falsifies 4.1 and reopens the Lemma 6 loophole.

INSTRUMENT NOTE (the load-bearing fix): Toys 430-434 computed "middle" from
sorted(adj[v]) — sorted VERTEX INDICES, not the planar embedding. For stacked
triangulations sorted order is generically NOT the link cycle, so historical
middle/non-middle labels (and even the gap screen) were computed against a
fictitious embedding. This toy maintains an explicit face list for every graph
and extracts TRUE link cycles from it. Toy 5510 (P3) re-bins the historical
stat; this toy establishes the corrected baseline.

Provenance gap, logged per K1832's own style: the "middle only ~10%" figure
K1832 attributes to "Toy 433 (v9 doc)" has no locatable artifact — the paper's
v9 table carries no slot stats and toy_433_operational_test.py computes no
strict tangling. The reproducible historical claim is toy_434's header:
"STEP 2 IS FALSE. Non-middle bridge pairs CAN be strictly tangled."

Populations (ALL triangulations of the sphere, face-tracked):
  icosahedron · nested antiprism (22v, = Toy 433's) · stacked/Apollonian
  (Toy 433's generator + face tracking, same seeds) · flip-randomized
  (edge flips from stacked — reaches chord-free deg-5 links stacked cannot).

TESTS (X/Y scored):
  1. Generator validity: every graph passes sphere-triangulation checks.
  2. Link-cycle instrument valid; measure sorted-vs-true-cycle disagreement.
  3. Strict-detector positive control (hand-built known strict + known split).
  4. tau=6 ==> gap=2 in the TRUE embedding (Lemma 2 shadow).
  5. Middle bridge pair strictly tangled in 100% of tau=6 cases (4.1 core).
  6. Non-middle bridge pairs NEVER strict at tau=6 (the can-fail content).
  7. tau_s = exactly 4 at tau=6 (strict set = 3 singletons + middle).
  8. Chord-free deg-5 vertices never reach tau=6 (Toy 451 replication).

Elie, 2026-08-30. Millennium week, 4-Color day. 8 tests.
"""

import itertools
import random
from collections import defaultdict, deque, Counter

# ------------------------------------------------------------------
# Kempe machinery (Definitions 1, 5-8 of FourColor_Standalone_Paper v9)
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


def can_free_color(adj, color, v, c1, c2):
    """Definition 5: operational tangling test. Chains in G-v (exclude v)."""
    nbrs_c1 = [u for u in adj[v] if color.get(u) == c1]
    nbrs_c2 = [u for u in adj[v] if color.get(u) == c2]
    if not nbrs_c1 or not nbrs_c2:
        return True
    exclude = {v}
    for start in nbrs_c1:
        chain = kempe_chain(adj, color, start, c1, c2, exclude=exclude)
        if all(u in chain for u in nbrs_c1) and not any(u in chain for u in nbrs_c2):
            return True
    for start in nbrs_c2:
        chain = kempe_chain(adj, color, start, c1, c2, exclude=exclude)
        if all(u in chain for u in nbrs_c2) and not any(u in chain for u in nbrs_c1):
            return True
    return False


def operational_tau(adj, color, v):
    tau = 0
    for c1, c2 in itertools.combinations(range(4), 2):
        if not can_free_color(adj, color, v, c1, c2):
            tau += 1
    return tau


def is_strict(adj, color, v, a, b):
    """Definition 7: all neighbors of v colored a or b lie in ONE (a,b)-chain
    of G-v. Embedding-independent."""
    nbrs_ab = [u for u in adj[v] if color.get(u) in (a, b)]
    if not nbrs_ab:
        return False
    chain = kempe_chain(adj, color, nbrs_ab[0], a, b, exclude={v})
    return all(u in chain for u in nbrs_ab)


def strict_pairs(adj, color, v):
    return [(a, b) for a, b in itertools.combinations(range(4), 2)
            if is_strict(adj, color, v, a, b)]


# ------------------------------------------------------------------
# Face-tracked triangulation generators
# ------------------------------------------------------------------

def adj_from_faces(faces):
    adj = defaultdict(set)
    for f in faces:
        a, b, c = f
        adj[a].update((b, c)); adj[b].update((a, c)); adj[c].update((a, b))
    return dict(adj)


def check_triangulation(faces, adj):
    """Sphere triangulation checks: V-E+F=2, 3F=2E, every edge in exactly 2
    faces, min degree >= 3, faces are proper triangles."""
    V = len(adj)
    E = sum(len(s) for s in adj.values()) // 2
    F = len(faces)
    if V - E + F != 2:
        return False, f"Euler fails: V={V} E={E} F={F}"
    if 3 * F != 2 * E:
        return False, f"3F != 2E: F={F} E={E}"
    edge_count = Counter()
    for f in faces:
        a, b, c = f
        if len({a, b, c}) != 3:
            return False, f"degenerate face {f}"
        for e in ((a, b), (b, c), (a, c)):
            edge_count[frozenset(e)] += 1
    for e, cnt in edge_count.items():
        if cnt != 2:
            return False, f"edge {set(e)} in {cnt} faces"
    if set(edge_count.keys()) != {frozenset((u, w)) for u in adj for w in adj[u]}:
        return False, "face edges != adjacency edges"
    if min(len(s) for s in adj.values()) < 3:
        return False, "min degree < 3"
    return True, "ok"


def icosahedron():
    return antiprism_stack(2)


def antiprism_stack(n_rings):
    """Center 0, n_rings rings of 5, apex last. n_rings=2 -> icosahedron.
    n_rings=4 -> Toy 433's 22-vertex nested antiprism (same combinatorics)."""
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
    """Toy 433's make_planar_triangulation with face tracking (same insertion
    logic and seeds -> same graphs as the historical population)."""
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
    """Random edge flips from a stacked triangulation. Reaches chord-free
    deg-5 links that stacking cannot produce."""
    rng = random.Random(seed)
    faces = stacked_triangulation(n, seed=seed + 991)
    faceset = [frozenset(f) for f in faces]
    E = 3 * (len(faceset)) // 2
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
        # skip if c,d already adjacent (would create parallel edge)
        adjacent_cd = any(frozenset((c, d)) < f for f in faceset)
        if adjacent_cd:
            continue
        # degree of a and b must stay >= 3
        deg_a = sum(1 for f in faceset if a in f)
        deg_b = sum(1 for f in faceset if b in f)
        if deg_a <= 3 or deg_b <= 3:
            continue
        faceset[i] = frozenset((a, c, d))
        faceset[j] = frozenset((b, c, d))
    return [tuple(sorted(f)) for f in faceset]


# ------------------------------------------------------------------
# TRUE link cycles from the face list
# ------------------------------------------------------------------

def link_cycle(faces, v):
    """Cyclic order of v's neighbors from the faces around v."""
    edges = []
    for f in faces:
        if v in f:
            rest = [x for x in f if x != v]
            edges.append(tuple(rest))
    nbr_adj = defaultdict(list)
    for a, b in edges:
        nbr_adj[a].append(b)
        nbr_adj[b].append(a)
    for u, lst in nbr_adj.items():
        if len(lst) != 2:
            return None  # not a disk/sphere link
    start = edges[0][0]
    cyc = [start]
    prev = None
    cur = start
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


def is_rotation_or_reflection(seq, target):
    n = len(target)
    if len(seq) != n:
        return False
    doubled = target + target
    rev = target[::-1] + target[::-1]
    for s in range(n):
        if doubled[s:s + n] == seq or rev[s:s + n] == seq:
            return True
    return False


# ------------------------------------------------------------------
# Structure at a deg-5 vertex, TRUE embedding
# ------------------------------------------------------------------

def structure_true(faces, adj, color, v):
    """Bridge geometry from the TRUE link cycle. Returns None if v is not
    saturated-with-one-repeat."""
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
    info = {'cyc': cyc, 'nc': nc, 'r': r, 'bp': bp, 'gap': gap}
    if gap == 2:
        # middle position: cyclically adjacent to both bridge positions
        if d == 2:
            mid = (bp[0] + 1) % 5
        else:  # d == 3, i.e. bp[1]+1 == bp[0]-... the short way is the other side
            mid = (bp[1] + 1) % 5
        assert min((mid - bp[0]) % 5, (bp[0] - mid) % 5) == 1
        assert min((mid - bp[1]) % 5, (bp[1] - mid) % 5) == 1
        non_mid = [i for i in range(5) if nc[i] != r and i != mid]
        info.update({'mid_pos': mid, 'mid_color': nc[mid],
                     'non_mid_pos': non_mid,
                     'non_mid_colors': [nc[i] for i in non_mid]})
    return info


def has_chord(adj, cyc):
    n = len(cyc)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(i - j) % (n - 1) in (0, 1):  # cyclically adjacent
                continue
            d = min((j - i) % n, (i - j) % n)
            if d >= 2 and cyc[j] in adj[cyc[i]]:
                return True
    return False


# ------------------------------------------------------------------
# Coloring collection (mirrors Toy 433)
# ------------------------------------------------------------------

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


def collect_colorings_4sat(adj, tv, n_seeds=400):
    others = [v for v in sorted(adj.keys()) if v != tv]
    results = []
    seen = set()
    for seed in range(n_seeds):
        rng = random.Random(seed)
        order = list(others)
        rng.shuffle(order)
        c = greedy_4color(adj, order)
        if c is None or not is_proper(adj, c, skip=tv):
            continue
        if len(set(c[u] for u in adj[tv])) != 4:
            continue
        key = tuple(c[u] for u in sorted(adj[tv]))
        if key in seen:
            continue
        seen.add(key)
        results.append(c)
    return results


# ------------------------------------------------------------------
# Populations
# ------------------------------------------------------------------

def build_populations():
    pops = []
    pops.append(('icosahedron', icosahedron()))
    pops.append(('antiprism22', antiprism_stack(4)))
    for n in [12, 15, 18, 20, 25, 30]:
        for gseed in range(25):
            pops.append((f'stacked_n{n}_s{gseed}',
                         stacked_triangulation(n, seed=gseed * 100 + n)))
    for n in [16, 20, 24, 30, 40]:
        for gseed in range(8):
            pops.append((f'flipped_n{n}_s{gseed}',
                         flipped_triangulation(n, seed=gseed)))
    return pops


# ------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------

def test_1_generators(pops):
    print("=" * 70)
    print("Test 1: All generated graphs are sphere triangulations")
    print("=" * 70)
    bad = 0
    for name, faces in pops:
        adj = adj_from_faces(faces)
        ok, msg = check_triangulation(faces, adj)
        if not ok:
            bad += 1
            print(f"  FAIL {name}: {msg}")
    print(f"\n  {len(pops)} graphs checked, {bad} failures")
    t = bad == 0
    print(f"\n  [{'PASS' if t else 'FAIL'}] 1. Generator validity")
    return t


def test_2_link_instrument(pops):
    print("\n" + "=" * 70)
    print("Test 2: Link-cycle instrument valid; sorted-order disagreement rate")
    print("=" * 70)
    checked = 0
    bad = 0
    sorted_matches = 0
    sorted_differs = 0
    for name, faces in pops:
        adj = adj_from_faces(faces)
        for v in adj:
            if len(adj[v]) != 5:
                continue
            cyc = link_cycle(faces, v)
            checked += 1
            if cyc is None or len(cyc) != 5:
                bad += 1
                print(f"  FAIL {name} v={v}: no valid link cycle")
                continue
            # consecutive-in-cycle must be adjacent in G
            for i in range(5):
                if cyc[(i + 1) % 5] not in adj[cyc[i]]:
                    bad += 1
                    print(f"  FAIL {name} v={v}: cycle not edge-supported")
                    break
            if is_rotation_or_reflection(sorted(adj[v]), cyc):
                sorted_matches += 1
            else:
                sorted_differs += 1
    print(f"\n  Deg-5 vertices checked: {checked}, instrument failures: {bad}")
    print(f"  sorted(adj[v]) IS the true cyclic order:  {sorted_matches}")
    print(f"  sorted(adj[v]) is NOT the cyclic order:   {sorted_differs}")
    if checked:
        pct = 100 * sorted_differs / checked
        print(f"  ==> historical instrument mislabeled the embedding at "
              f"{pct:.1f}% of deg-5 vertices")
    t = bad == 0 and checked > 0
    print(f"\n  [{'PASS' if t else 'FAIL'}] 2. Link-cycle instrument")
    return t


def test_3_strict_control():
    print("\n" + "=" * 70)
    print("Test 3: Strict-detector positive control (hand-built, known answers)")
    print("=" * 70)
    # Wheel W5: v=0 center, link 1-2-3-4-5 cyclic. Colors: 1:r=0, 2:sM=1,
    # 3:r=0, 4:si=2, 5:sj=3.
    faces = [(0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 5), (0, 1, 5)]
    # close the sphere: add outer vertex 6 adjacent to all link vertices
    faces += [(6, 1, 2), (6, 2, 3), (6, 3, 4), (6, 4, 5), (6, 1, 5)]
    adj = adj_from_faces(faces)
    color = {1: 0, 2: 1, 3: 0, 4: 2, 5: 3, 6: None}
    ok = True
    # (r, sM) = (0,1): link path 1-2-3 chains B1,mid,B2 together -> STRICT
    color[6] = 2  # 6 colored si, irrelevant to (0,1)
    s = is_strict(adj, color, 0, 0, 1)
    print(f"  (r,sM) with link path B1-mid-B2:      strict={s}  expect True")
    ok &= (s is True)
    # (r, si) = (0,2): nbrs {1,3,4}; 4-3 link edge chains {3,4}; vertex 1
    # connects only via 6 (colored 2): 1-6? 6 in chain(color 2), 6 adj 1 and 3
    # -> all connected -> STRICT
    s = is_strict(adj, color, 0, 0, 2)
    print(f"  (r,si) with outer bridge colored si:  strict={s}  expect True")
    ok &= (s is True)
    # recolor 6 to sM=1: now (0,2)-chains: {3,4} (via link edge) vs {1} alone
    # (1's (0,2)-neighbors: 2 is color 1 no, 5 color 3 no, 6 color 1 no) -> SPLIT
    color[6] = 1
    s = is_strict(adj, color, 0, 0, 2)
    print(f"  (r,si) with outer bridge recolored:   strict={s}  expect False")
    ok &= (s is False)
    print(f"\n  [{'PASS' if ok else 'FAIL'}] 3. Strict detector control")
    return ok


def scan_tau6(pops, max_deg5_per_graph=3, n_seeds=400):
    """Collect all operational tau=6 cases with TRUE-embedding structure."""
    cases = []
    for name, faces in pops:
        adj = adj_from_faces(faces)
        deg5 = [v for v in sorted(adj) if len(adj[v]) == 5]
        for tv in deg5[:max_deg5_per_graph]:
            for c in collect_colorings_4sat(adj, tv, n_seeds=n_seeds):
                if operational_tau(adj, c, tv) != 6:
                    continue
                info = structure_true(faces, adj, c, tv)
                cases.append((name, faces, adj, tv, c, info))
    return cases


def test_4_gap2(cases):
    print("\n" + "=" * 70)
    print("Test 4: tau=6 ==> gap=2 in the TRUE embedding")
    print("=" * 70)
    bad = 0
    for name, faces, adj, tv, c, info in cases:
        if info is None or info['gap'] != 2:
            bad += 1
            g = None if info is None else info['gap']
            print(f"  EXCEPTION {name} v={tv}: gap={g}")
    print(f"\n  tau=6 cases: {len(cases)}, gap!=2 exceptions: {bad}")
    t = bad == 0 and len(cases) > 0
    print(f"\n  [{'PASS' if t else 'FAIL'}] 4. Gap-2 at tau=6 "
          f"({len(cases)} cases)")
    return t


def test_5_6_7_middle_strict(cases):
    print("\n" + "=" * 70)
    print("Tests 5-7: strict-slot composition at tau=6 (TRUE embedding)")
    print("=" * 70)
    n = 0
    mid_strict = 0
    nonmid_strict_cases = []
    taus_exact4 = 0
    taus_dist = Counter()
    for name, faces, adj, tv, c, info in cases:
        if info is None or info['gap'] != 2:
            continue
        n += 1
        r = info['r']
        sp = strict_pairs(adj, c, tv)
        taus_dist[len(sp)] += 1
        if len(sp) == 4:
            taus_exact4 += 1
        mid_pair = frozenset((r, info['mid_color']))
        nm_pairs = [frozenset((r, x)) for x in info['non_mid_colors']]
        spf = [frozenset(p) for p in sp]
        if mid_pair in spf:
            mid_strict += 1
        for p in nm_pairs:
            if p in spf:
                nonmid_strict_cases.append((name, tv, c, info))
                print(f"  *** EXCEPTION: NON-MIDDLE STRICT at {name} v={tv} "
                      f"pair={sorted(p)} cyc={info['cyc']} nc={info['nc']}")
    print(f"\n  Usable tau=6 gap-2 cases: {n}")
    print(f"  Middle pair strict:      {mid_strict}/{n}")
    print(f"  Non-middle strict cases: {len(nonmid_strict_cases)}")
    print(f"  tau_s distribution at tau=6: {dict(sorted(taus_dist.items()))}")
    t5 = n > 0 and mid_strict == n
    t6 = n > 0 and len(nonmid_strict_cases) == 0
    t7 = n > 0 and taus_exact4 == n
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. Middle-strict 100% "
          f"({mid_strict}/{n})")
    print(f"  [{'PASS' if t6 else 'FAIL'}] 6. Non-middle never strict "
          f"({len(nonmid_strict_cases)} exceptions)")
    print(f"  [{'PASS' if t7 else 'FAIL'}] 7. tau_s = 4 exactly "
          f"({taus_exact4}/{n})")
    return t5, t6, t7


def test_8_chordfree(pops):
    print("\n" + "=" * 70)
    print("Test 8: chord-free deg-5 vertices never reach tau=6 (Toy 451 shadow)")
    print("=" * 70)
    checked = 0
    tau6 = 0
    max_tau = 0
    for name, faces in pops:
        adj = adj_from_faces(faces)
        deg5 = [v for v in sorted(adj) if len(adj[v]) == 5]
        for tv in deg5[:3]:
            cyc = link_cycle(faces, tv)
            if cyc is None or has_chord(adj, cyc):
                continue
            for c in collect_colorings_4sat(adj, tv, n_seeds=200):
                checked += 1
                t = operational_tau(adj, c, tv)
                max_tau = max(max_tau, t)
                if t == 6:
                    tau6 += 1
                    print(f"  *** EXCEPTION: tau=6 at CHORD-FREE {name} v={tv}")
    print(f"\n  Chord-free deg-5 colorings checked: {checked}")
    print(f"  tau=6 found: {tau6}   max tau seen: {max_tau}")
    t = tau6 == 0 and checked > 0
    print(f"\n  [{'PASS' if t else 'FAIL'}] 8. Chord-free never tau=6")
    return t


# ------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5508 — P1: Middle-Strict Lemma on true triangulations")
    print("          (K1832 Section 6, pre-registered falsifier)")
    print("=" * 70)

    pops = build_populations()
    t1 = test_1_generators(pops)
    t2 = test_2_link_instrument(pops)
    t3 = test_3_strict_control()
    print("\n  ... scanning for operational tau=6 cases (this is the slow part)")
    cases = scan_tau6(pops)
    src = Counter(name.split('_')[0] for name, *_ in cases)
    print(f"  tau=6 cases found: {len(cases)}  by family: {dict(src)}")
    t4 = test_4_gap2(cases)
    t5, t6, t7 = test_5_6_7_middle_strict(cases)
    t8 = test_8_chordfree(pops)

    results = [t1, t2, t3, t4, t5, t6, t7, t8]
    passed = sum(results)
    print(f"\n{'=' * 70}")
    print(f"Toy 5508 -- SCORE: {passed}/{len(results)}")
    print(f"{'=' * 70}")
    if passed != len(results):
        for i, r in enumerate(results, 1):
            if not r:
                print(f"  Test {i}: FAIL")
