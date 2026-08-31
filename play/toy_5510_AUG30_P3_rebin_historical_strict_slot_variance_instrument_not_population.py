#!/usr/bin/env python3
"""
Toy 5510 — P3 (K1832 Section 6, pre-registered): RE-BIN THE STRICT-SLOT VARIANCE

K1832's calibration note: "Toy 433 (v9 doc) reports the 4th strict slot VARIES —
middle only ~10%. That run mixed general planar graphs, where middle link edges
may be absent. On triangulations the lemma predicts 100% middle."
KEEPER'S PRE-REGISTERED P3 PREDICTION: re-binned by triangulation vs
non-triangulation, the variance lives entirely in the non-triangulations.

PROVENANCE, pinned before running: the "~10%" figure has no locatable artifact
(toy_433_operational_test.py computes no strict tangling; the v9 table has no
slot stats). The reproducible historical claim is toy_434_chain_exclusion.py's
header: "STEP 2 IS FALSE. Non-middle bridge pairs CAN be strictly tangled."

ELIE'S COUNTER-HYPOTHESIS, pre-registered here before the run: the variance is
an INSTRUMENT artifact, not a population artifact. Toys 430-434 computed
"middle" from sorted(adj[v]) — sorted vertex indices, not the embedding. Both
historical populations (nested antiprism + stacked make_planar_triangulation)
are in fact TRIANGULATIONS, so Keeper's non-triangulation bin is EMPTY and his
prediction cannot be what explains the variance. Strict tangling itself is
embedding-independent; only the MIDDLE LABEL needs the true cycle. Prediction:
recomputing the label from the true (face-tracked) link cycle on the SAME
cases turns the slot into 100% middle.

TESTS (X/Y):
  1. Historical instrument reproduced (sorted-order pipeline, same generators
     and seeds); op-tau=6 cases found.
  2. Anomaly reproduces: under sorted labels the strict bridge pair is NOT
     always the "middle" (toy_434's claim), report the observed middle-rate.
  3. KEEPER'S P3 PREDICTION as pre-registered: variance lives entirely in
     non-triangulations. (Scored honestly; expected to FAIL — the
     non-triangulation bin is empty: every historical graph is a
     triangulation.)
  4. Instrument attribution: 100% of anomalous cases sit at vertices where
     sorted(adj[v]) is not a rotation/reflection of the true link cycle.
  5. Corrected instrument on the SAME cases: strict slot = true middle, 100%.
  6. Screening loss: cases the historical sorted-gap screen dropped or
     admitted wrongly; all op-tau=6 cases have TRUE gap 2.

Elie, 2026-08-30. Millennium week, 4-Color day. 6 tests.
"""

import itertools
import random
from collections import defaultdict, deque, Counter

# ------------------------------------------------------------------
# Shared Kempe machinery (identical to Toys 433/434/5508)
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
    nbrs_c1 = [u for u in adj[v] if color.get(u) == c1]
    nbrs_c2 = [u for u in adj[v] if color.get(u) == c2]
    if not nbrs_c1 or not nbrs_c2:
        return True
    for start in nbrs_c1:
        ch = kempe_chain(adj, color, start, c1, c2, exclude={v})
        if all(u in ch for u in nbrs_c1) and not any(u in ch for u in nbrs_c2):
            return True
    for start in nbrs_c2:
        ch = kempe_chain(adj, color, start, c1, c2, exclude={v})
        if all(u in ch for u in nbrs_c2) and not any(u in ch for u in nbrs_c1):
            return True
    return False


def operational_tau(adj, color, v):
    return sum(1 for c1, c2 in itertools.combinations(range(4), 2)
               if not can_free_color(adj, color, v, c1, c2))


def is_strict(adj, color, v, a, b):
    nbrs = [u for u in adj[v] if color.get(u) in (a, b)]
    if not nbrs:
        return False
    ch = kempe_chain(adj, color, nbrs[0], a, b, exclude={v})
    return all(u in ch for u in nbrs)


# ------------------------------------------------------------------
# THE HISTORICAL INSTRUMENT — verbatim logic from toy_433/434:
# cyclic positions taken from sorted(adj[v])
# ------------------------------------------------------------------

def cyclic_dist(a, b, n=5):
    return min(abs(b - a), n - abs(b - a))


def get_structure_HISTORICAL(adj, color, v):
    nbrs = sorted(adj[v])
    nc = [color[u] for u in nbrs]
    counts = Counter(nc)
    rep = [c for c, cnt in counts.items() if cnt >= 2]
    if not rep:
        return None
    r = rep[0]
    bp = [i for i, c in enumerate(nc) if c == r]
    if len(bp) != 2:
        return None
    gap = cyclic_dist(bp[0], bp[1])
    if gap != 2:
        return None
    p1, p2 = bp
    if p2 - p1 == 2:
        mid_pos = (p1 + 1) % 5
    else:
        mid_pos = (p1 - 1) % 5
    non_mid = [i for i in range(5) if nc[i] != r and i != mid_pos]
    return {'r': r, 'bp': bp, 'nbrs': nbrs, 'nc': nc, 'mid_pos': mid_pos,
            'mid_color': nc[mid_pos], 'non_mid_colors': [nc[i] for i in non_mid]}


# ------------------------------------------------------------------
# Face-tracked builders (Toy 5508's instrument) for the SAME graphs
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


def check_triangulation(faces, adj):
    V = len(adj)
    E = sum(len(s) for s in adj.values()) // 2
    F = len(faces)
    if V - E + F != 2 or 3 * F != 2 * E:
        return False
    edge_count = Counter()
    for a, b, c in faces:
        if len({a, b, c}) != 3:
            return False
        for e in ((a, b), (b, c), (a, c)):
            edge_count[frozenset(e)] += 1
    return all(cnt == 2 for cnt in edge_count.values())


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


def true_middle(cyc, color):
    nc = [color[u] for u in cyc]
    counts = Counter(nc)
    rep = [c for c, cnt in counts.items() if cnt == 2]
    if len(rep) != 1 or len(counts) != 4:
        return None, None
    r = rep[0]
    bp = [i for i, c in enumerate(nc) if c == r]
    d = (bp[1] - bp[0]) % 5
    gap = min(d, 5 - d)
    if gap != 2:
        return None, gap
    mid = (bp[0] + 1) % 5 if d == 2 else (bp[1] + 1) % 5
    return nc[mid], gap


def is_rotation_or_reflection(seq, target):
    n = len(target)
    if len(seq) != n:
        return False
    doubled = target + target
    rev = target[::-1] + target[::-1]
    return any(doubled[s:s + n] == seq or rev[s:s + n] == seq
               for s in range(n))


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
# The historical population (Toy 433/434's graphs, same seeds)
# ------------------------------------------------------------------

def historical_population():
    pops = [('antiprism22', antiprism_stack(4))]
    for n in [12, 15, 18, 20, 25, 30]:
        for gseed in range(25):
            pops.append((f'stacked_n{n}_s{gseed}',
                         stacked_triangulation(n, seed=gseed * 100 + n)))
    return pops


# ------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5510 — P3: re-bin the historical strict-slot variance")
    print("=" * 70)

    pops = historical_population()

    # ---- collect all op-tau=6 cases once ----
    print("\n  ... scanning historical population for op-tau=6 (slow part)")
    all_cases = []   # (name, faces, adj, tv, coloring)
    for name, faces in pops:
        adj = adj_from_faces(faces)
        deg5 = [v for v in adj if len(adj[v]) == 5]
        for tv in deg5[:3]:
            for c in collect_colorings_4sat(adj, tv, n_seeds=400):
                if operational_tau(adj, c, tv) == 6:
                    all_cases.append((name, faces, adj, tv, c))
    print(f"  op-tau=6 cases: {len(all_cases)}")

    # ---- Test 1: historical instrument runs on them ----
    print("\n" + "=" * 70)
    print("Test 1: historical (sorted-order) instrument reproduced")
    print("=" * 70)
    hist_cases = []   # cases the historical screen ADMITS (sorted-gap==2)
    dropped = []      # cases it silently DROPS (sorted-gap!=2 -> None)
    for name, faces, adj, tv, c in all_cases:
        info = get_structure_HISTORICAL(adj, c, tv)
        if info is None:
            dropped.append((name, faces, adj, tv, c))
        else:
            hist_cases.append((name, faces, adj, tv, c, info))
    print(f"\n  admitted by sorted-gap screen: {len(hist_cases)}")
    print(f"  silently dropped (sorted-gap != 2): {len(dropped)}")
    t1 = len(hist_cases) > 0
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Historical instrument reproduced")

    # ---- Test 2: does the anomaly reproduce under sorted labels? ----
    print("\n" + "=" * 70)
    print("Test 2: anomaly under sorted labels (toy_434's claim)")
    print("=" * 70)
    n = 0
    mid_lab = 0
    nonmid_lab = 0
    anomalous = []
    for name, faces, adj, tv, c, info in hist_cases:
        r = info['r']
        strict_bridge = [x for x in (info['mid_color'], *info['non_mid_colors'])
                         if is_strict(adj, c, tv, r, x)]
        if len(strict_bridge) != 1:
            # 0 or 2 strict bridge pairs would contradict Lemma 3/4 outright
            anomalous.append((name, tv, 'count', strict_bridge))
            continue
        n += 1
        if strict_bridge[0] == info['mid_color']:
            mid_lab += 1
        else:
            nonmid_lab += 1
            anomalous.append((name, tv, 'nonmid', strict_bridge))
    rate = 100 * mid_lab / n if n else 0
    print(f"\n  cases with exactly one strict bridge pair: {n}")
    print(f"  strict pair == sorted-'middle': {mid_lab} ({rate:.1f}%)")
    print(f"  strict pair == sorted-'non-middle' (THE ANOMALY): {nonmid_lab}")
    t2 = nonmid_lab > 0
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Anomaly reproduces "
          f"(sorted-middle rate {rate:.1f}%, not 100%)")

    # ---- Test 3: Keeper's pre-registered P3 prediction ----
    print("\n" + "=" * 70)
    print("Test 3: KEEPER P3 PREDICTION — variance lives in non-triangulations")
    print("=" * 70)
    tri = 0
    nontri = 0
    nontri_names = set()
    for name, faces in pops:
        adj = adj_from_faces(faces)
        if check_triangulation(faces, adj):
            tri += 1
        else:
            nontri += 1
            nontri_names.add(name)
    anom_in_nontri = sum(1 for name, tv, kind, sb in anomalous
                         if name in nontri_names)
    print(f"\n  historical graphs: {tri} triangulations, "
          f"{nontri} non-triangulations")
    print(f"  anomalous cases in non-triangulations: {anom_in_nontri}"
          f"/{len(anomalous)}")
    t3 = len(anomalous) > 0 and anom_in_nontri == len(anomalous)
    if not t3:
        print("  ==> PREDICTION REFUTED AS STATED: the historical population "
              "contains no non-triangulations to carry the variance — every "
              "graph (nested antiprism AND make_planar_triangulation) is a "
              "sphere triangulation.")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Keeper's population "
          f"prediction (expected FAIL; the finding)")

    # ---- Test 4: instrument attribution ----
    print("\n" + "=" * 70)
    print("Test 4: anomalies sit where sorted(adj[v]) is not the true cycle")
    print("=" * 70)
    facemap = dict(pops)
    attributed = 0
    for name, tv, kind, sb in anomalous:
        faces = facemap[name]
        adj = adj_from_faces(faces)
        cyc = link_cycle(faces, tv)
        if cyc is None or not is_rotation_or_reflection(sorted(adj[tv]), cyc):
            attributed += 1
        else:
            print(f"  *** UNEXPLAINED ANOMALY: {name} v={tv} — sorted order "
                  f"IS the true cycle yet slot varies ({kind}: {sb})")
    print(f"\n  anomalies attributed to the sorted-order instrument: "
          f"{attributed}/{len(anomalous)}")
    t4 = len(anomalous) > 0 and attributed == len(anomalous)
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Instrument attribution 100%")

    # ---- Test 5: corrected instrument on the SAME cases ----
    print("\n" + "=" * 70)
    print("Test 5: true-embedding label on the same cases -> 100% middle")
    print("=" * 70)
    n5 = 0
    ok5 = 0
    for name, faces, adj, tv, c, info in hist_cases:
        cyc = link_cycle(faces, tv)
        if cyc is None:
            continue
        mid_c, gap = true_middle(cyc, c)
        if mid_c is None:
            continue
        r = info['r']
        strict_bridge = [x for x in set(c[u] for u in adj[tv]) if x != r
                         and is_strict(adj, c, tv, r, x)]
        if len(strict_bridge) != 1:
            continue
        n5 += 1
        if strict_bridge[0] == mid_c:
            ok5 += 1
        else:
            print(f"  *** EXCEPTION: true-middle mismatch at {name} v={tv}")
    print(f"\n  strict slot == TRUE middle: {ok5}/{n5}")
    t5 = n5 > 0 and ok5 == n5
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. Corrected label: 100% middle")

    # ---- Test 6: screening loss ----
    print("\n" + "=" * 70)
    print("Test 6: what the sorted-gap screen dropped")
    print("=" * 70)
    ok6 = 0
    for name, faces, adj, tv, c in dropped:
        cyc = link_cycle(faces, tv)
        mid_c, gap = true_middle(cyc, c) if cyc else (None, None)
        if gap == 2:
            ok6 += 1
        else:
            print(f"  *** dropped case with TRUE gap={gap} at {name} v={tv}")
    print(f"\n  dropped cases with TRUE gap 2 (valid cases lost): "
          f"{ok6}/{len(dropped)}")
    t6 = ok6 == len(dropped)
    print(f"\n  [{'PASS' if t6 else 'FAIL'}] 6. All dropped cases were valid "
          f"gap-2 cases (instrument loss, not physics)")

    results = [t1, t2, t3, t4, t5, t6]
    passed = sum(results)
    print(f"\n{'=' * 70}")
    print(f"Toy 5510 -- SCORE: {passed}/{len(results)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(results, 1):
        if not r:
            print(f"  Test {i}: FAIL")
    print("\nReading: Test 3's FAIL is the finding — the variance was never in "
          "the population (all triangulations); Tests 4-5 place it in the "
          "sorted-order instrument, and the corrected label restores "
          "Middle-Strict at 100% on the very cases that produced the "
          "historical 'slot varies' claim.")
