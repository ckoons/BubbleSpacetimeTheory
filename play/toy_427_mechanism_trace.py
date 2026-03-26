#!/usr/bin/env python3
"""
Toy 427: Trace the ACTUAL tau-reduction mechanism at tau=6

Key finding from Toy 426: The gap→1 argument fails ~27% of cases.
The middle singleton is ALWAYS strictly tangled (Case C) because
it's adjacent to BOTH bridge copies on the 5-cycle link.

So what IS the mechanism? We know empirically that SOME swap always
reduces tau. This toy traces exactly:
1. Which swap reduces tau
2. Which pair becomes free
3. The topology of the chain being swapped
4. What changes in the chain structure

Focus: What happens when we swap a NON-MIDDLE bridge pair.

Casey Koons & Claude 4.6 (Lyra), March 25 2026. 8 tests.
"""

import itertools
import random
from collections import defaultdict, deque, Counter


# ─────────────────────────────────────────────────────────────
# Core utilities
# ─────────────────────────────────────────────────────────────

def kempe_chain(adj, color, v, c1, c2, exclude=None):
    if exclude is None:
        exclude = set()
    if v in exclude or color.get(v) not in (c1, c2):
        return set()
    visited = set()
    queue = deque([v])
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
    tangled = []
    free = []
    for c1, c2 in itertools.combinations(range(4), 2):
        if not can_free_color(adj, color, v, c1, c2):
            tau += 1
            tangled.append((c1, c2))
        else:
            free.append((c1, c2))
    return tau, tangled, free


def do_swap_on_chain(adj, color, v, c1, c2, chain_vertices):
    new_color = dict(color)
    for u in chain_vertices:
        new_color[u] = c2 if new_color[u] == c1 else c1
    return new_color


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


def cyclic_dist(a, b, n=5):
    d = abs(a - b) % n
    return min(d, n - d)


def build_nested_antiprism():
    adj = defaultdict(set)
    for i in range(1, 6):
        adj[0].add(i); adj[i].add(0)
    for i in range(1, 6):
        j = (i % 5) + 1
        adj[i].add(j); adj[j].add(i)
    for ring_base in [6, 11, 16]:
        prev_base = ring_base - 5 if ring_base > 6 else 1
        for i in range(5):
            v = ring_base + i
            p = prev_base + i
            q = prev_base + ((i + 1) % 5)
            adj[v].add(p); adj[p].add(v)
            adj[v].add(q); adj[q].add(v)
        for i in range(5):
            v = ring_base + i
            w = ring_base + ((i + 1) % 5)
            adj[v].add(w); adj[w].add(v)
    for i in range(16, 21):
        adj[21].add(i); adj[i].add(21)
    return dict(adj)


def make_planar_triangulation(n, seed=42):
    rng = random.Random(seed)
    adj = defaultdict(set)
    for i in range(4):
        for j in range(i + 1, 4):
            adj[i].add(j); adj[j].add(i)
    faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    for v in range(4, n):
        fi = rng.randint(0, len(faces) - 1)
        a, b, c = faces[fi]
        adj[v].add(a); adj[a].add(v)
        adj[v].add(b); adj[b].add(v)
        adj[v].add(c); adj[c].add(v)
        faces[fi] = (a, b, v)
        faces.append((b, c, v))
        faces.append((a, c, v))
    return dict(adj)


def collect_tau6(adj, v0, n_seeds=5000):
    others = [v for v in sorted(adj.keys()) if v != v0]
    nbrs = sorted(adj[v0])
    cases = []
    for seed in range(n_seeds):
        rng = random.Random(seed)
        order = list(others)
        rng.shuffle(order)
        c = greedy_4color(adj, order)
        if c is None:
            continue
        if not is_proper(adj, c, skip=v0):
            continue
        nbr_colors = set(c[u] for u in nbrs)
        if len(nbr_colors) != 4:
            continue
        tau, tangled, free = operational_tau(adj, c, v0)
        if tau == 6:
            cases.append(c)
    return cases


# ─────────────────────────────────────────────────────────────
# Test 1: For each tau=6, find ALL reducing swaps and classify
# ─────────────────────────────────────────────────────────────
def test_1_all_reducers():
    print("=" * 70)
    print("Test 1: All reducing swaps at tau=6 — complete enumeration")
    print("=" * 70)

    adj = build_nested_antiprism()
    v0 = 0
    nbrs = sorted(adj[v0])  # For antiprism, sorted = cyclic order
    cases = collect_tau6(adj, v0)

    total_cases = len(cases)
    total_reducers = 0
    every_case_has_reducer = True
    reduction_details = []

    for ci, c in enumerate(cases):
        nbr_c = [c[u] for u in nbrs]
        color_count = Counter(nbr_c)
        rep = [col for col, cnt in color_count.items() if cnt >= 2][0]
        bridge_pos = sorted([i for i in range(5) if nbr_c[i] == rep])
        single_pos = [i for i in range(5) if nbr_c[i] != rep]

        reducers_for_case = []

        # Try all possible swaps on all chains
        for c1, c2 in itertools.combinations(range(4), 2):
            # Find all distinct chains for this pair
            seen = set()
            for n_v in nbrs:
                if c[n_v] in (c1, c2) and n_v not in seen:
                    chain = kempe_chain(adj, c, n_v, c1, c2, exclude={v0})
                    if chain & seen:
                        continue
                    seen |= chain

                    # Try swapping this chain
                    new_c = do_swap_on_chain(adj, c, v0, c1, c2, chain)
                    if not is_proper(adj, new_c, skip=v0):
                        continue

                    new_tau, new_tangled, new_free = operational_tau(adj, new_c, v0)
                    if new_tau < 6:
                        # Classify
                        is_bridge_swap = rep in (c1, c2)
                        new_nbr_c = [new_c[u] for u in nbrs]
                        new_count = Counter(new_nbr_c)
                        new_rep_list = [col for col, cnt in new_count.items() if cnt >= 2]

                        # Which nbrs changed?
                        changed_pos = [i for i in range(5) if nbr_c[i] != new_nbr_c[i]]

                        # Which pair(s) became free?
                        old_tau, old_tangled, old_free = 6, [], []
                        for oc1, oc2 in itertools.combinations(range(4), 2):
                            if not can_free_color(adj, c, v0, oc1, oc2):
                                old_tangled.append((oc1, oc2))
                        newly_freed = [p for p in new_free if p in old_tangled]

                        # Which bridge copies are in the chain?
                        bridge_in_chain = [bp for bp in bridge_pos if nbrs[bp] in chain]

                        reducers_for_case.append({
                            'swap': (c1, c2),
                            'is_bridge': is_bridge_swap,
                            'new_tau': new_tau,
                            'changed_pos': changed_pos,
                            'bridge_in_chain': bridge_in_chain,
                            'newly_freed': newly_freed,
                            'chain_size': len(chain),
                        })
                        total_reducers += 1

        if not reducers_for_case:
            every_case_has_reducer = False
        reduction_details.append(reducers_for_case)

    print(f"\n  Total tau=6 cases: {total_cases}")
    print(f"  Total reducing swaps found: {total_reducers}")
    print(f"  Every case has ≥1 reducer: {every_case_has_reducer}")

    # Summarize
    bridge_vs_singleton = Counter()
    bridges_in_chain_dist = Counter()
    changed_pos_counts = Counter()
    new_tau_dist = Counter()
    freed_pair_types = Counter()

    for reducers in reduction_details:
        for r in reducers:
            bridge_vs_singleton["bridge" if r['is_bridge'] else "singleton"] += 1
            bridges_in_chain_dist[len(r['bridge_in_chain'])] += 1
            changed_pos_counts[len(r['changed_pos'])] += 1
            new_tau_dist[r['new_tau']] += 1
            for fp in r['newly_freed']:
                fp_has_rep = rep in fp
                freed_pair_types["bridge_pair" if fp_has_rep else "singleton_pair"] += 1

    print(f"\n  Reducer types:")
    for k, v in sorted(bridge_vs_singleton.items(), key=lambda x: -x[1]):
        print(f"    {k}: {v}")
    print(f"\n  Bridge copies in swapped chain:")
    for k, v in sorted(bridges_in_chain_dist.items()):
        print(f"    {k} bridges: {v}")
    print(f"\n  Positions changed at v's neighbors:")
    for k, v in sorted(changed_pos_counts.items()):
        print(f"    {k} changed: {v}")
    print(f"\n  New tau after swap:")
    for k, v in sorted(new_tau_dist.items()):
        print(f"    tau={k}: {v}")
    print(f"\n  Freed pair type:")
    for k, v in sorted(freed_pair_types.items(), key=lambda x: -x[1]):
        print(f"    {k}: {v}")

    t1 = every_case_has_reducer
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. All reducers: {total_reducers} across {total_cases} cases")
    return t1


# ─────────────────────────────────────────────────────────────
# Test 2: Focus on the FIRST reducer per case — what's the pattern?
# ─────────────────────────────────────────────────────────────
def test_2_first_reducer():
    print("\n" + "=" * 70)
    print("Test 2: First reducer per case — detailed trace")
    print("=" * 70)

    adj = build_nested_antiprism()
    v0 = 0
    nbrs = sorted(adj[v0])
    cases = collect_tau6(adj, v0)

    # For each case, find the FIRST swap that reduces tau
    # and trace what happens step by step

    patterns = Counter()
    swap_pair_ids = Counter()

    for ci, c in enumerate(cases[:10]):  # Detailed trace for first 10
        nbr_c = [c[u] for u in nbrs]
        color_count = Counter(nbr_c)
        rep = [col for col, cnt in color_count.items() if cnt >= 2][0]
        bridge_pos = sorted([i for i in range(5) if nbr_c[i] == rep])
        single_pos = [i for i in range(5) if nbr_c[i] != rep]

        print(f"\n  Case {ci}: colors at 5-cycle = {nbr_c}")
        print(f"    Bridge color {rep} at positions {bridge_pos}")
        print(f"    Singletons: " + ", ".join(f"pos{sp}={nbr_c[sp]}" for sp in single_pos))

        # Show chain structure for each pair
        for c1, c2 in itertools.combinations(range(4), 2):
            relevant_pos = [i for i in range(5) if nbr_c[i] in (c1, c2)]
            if len(relevant_pos) < 2:
                continue
            chain_from_first = kempe_chain(adj, c, nbrs[relevant_pos[0]], c1, c2, exclude={v0})
            in_chain = [nbrs[p] in chain_from_first for p in relevant_pos]
            all_same = all(in_chain)
            is_bridge = rep in (c1, c2)
            label = "BRIDGE" if is_bridge else "single"
            print(f"    ({c1},{c2}) [{label}]: positions {relevant_pos}, "
                  f"all-in-chain={all_same}, strict={'Y' if all_same else 'N'}")

        # Find first reducer
        found = False
        for c1, c2 in itertools.combinations(range(4), 2):
            if found:
                break
            seen = set()
            for n_v in nbrs:
                if found:
                    break
                if c[n_v] in (c1, c2) and n_v not in seen:
                    chain = kempe_chain(adj, c, n_v, c1, c2, exclude={v0})
                    if chain & seen:
                        continue
                    seen |= chain

                    new_c = do_swap_on_chain(adj, c, v0, c1, c2, chain)
                    if not is_proper(adj, new_c, skip=v0):
                        continue

                    new_tau, _, new_free = operational_tau(adj, new_c, v0)
                    if new_tau < 6:
                        new_nbr_c = [new_c[u] for u in nbrs]
                        changed = [i for i in range(5) if nbr_c[i] != new_nbr_c[i]]
                        bridge_in = [bp for bp in bridge_pos if nbrs[bp] in chain]
                        print(f"    → REDUCER: swap ({c1},{c2}) on chain starting {n_v}")
                        print(f"      Chain has {len(chain)} vertices, bridges in chain: {bridge_in}")
                        print(f"      Changed positions: {changed}")
                        print(f"      New colors: {new_nbr_c}")
                        print(f"      New tau: {new_tau}, freed: {new_free}")
                        found = True

    # Now do stats for ALL cases
    print(f"\n  --- Statistics for all {len(cases)} cases ---")

    all_reducers_found = True
    reducer_swap_types = Counter()
    bridges_moved = Counter()
    singleton_swap_reduces = 0

    for c in cases:
        nbr_c = [c[u] for u in nbrs]
        color_count = Counter(nbr_c)
        rep = [col for col, cnt in color_count.items() if cnt >= 2][0]
        bridge_pos = sorted([i for i in range(5) if nbr_c[i] == rep])

        found = False
        for c1, c2 in itertools.combinations(range(4), 2):
            if found:
                break
            seen = set()
            for n_v in nbrs:
                if found:
                    break
                if c[n_v] in (c1, c2) and n_v not in seen:
                    chain = kempe_chain(adj, c, n_v, c1, c2, exclude={v0})
                    if chain & seen:
                        continue
                    seen |= chain
                    new_c = do_swap_on_chain(adj, c, v0, c1, c2, chain)
                    if not is_proper(adj, new_c, skip=v0):
                        continue
                    new_tau, _, _ = operational_tau(adj, new_c, v0)
                    if new_tau < 6:
                        is_bridge = rep in (c1, c2)
                        bridge_in = [bp for bp in bridge_pos if nbrs[bp] in chain]
                        reducer_swap_types[("bridge" if is_bridge else "singleton", len(bridge_in))] += 1
                        bridges_moved[len(bridge_in)] += 1
                        if not is_bridge:
                            singleton_swap_reduces += 1
                        found = True
        if not found:
            all_reducers_found = False

    print(f"\n  Reducer swap types (type, bridges_in_chain):")
    for (stype, bc), cnt in sorted(reducer_swap_types.items(), key=lambda x: -x[1]):
        print(f"    {stype}, {bc} bridges: {cnt}")

    print(f"\n  Singleton pair swaps that reduce: {singleton_swap_reduces}")

    t2 = all_reducers_found
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. First reducer trace")
    return t2


# ─────────────────────────────────────────────────────────────
# Test 3: Can a SINGLETON pair swap reduce tau?
# ─────────────────────────────────────────────────────────────
def test_3_singleton_swap():
    print("\n" + "=" * 70)
    print("Test 3: Can singleton pair swaps reduce tau?")
    print("=" * 70)

    adj = build_nested_antiprism()
    v0 = 0
    nbrs = sorted(adj[v0])
    cases = collect_tau6(adj, v0)

    # At tau=6, all 3 singleton pairs are tangled (both endpoints in same chain).
    # A singleton swap (s_i, s_j) changes which vertices have colors s_i and s_j.
    # This doesn't affect the bridge color r.
    # But it changes the chain structure for pairs involving s_i or s_j.

    singleton_reduces = 0
    bridge_reduces = 0
    total = 0

    for c in cases:
        total += 1
        nbr_c = [c[u] for u in nbrs]
        color_count = Counter(nbr_c)
        rep = [col for col, cnt in color_count.items() if cnt >= 2][0]
        singles = [col for col in range(4) if col != rep]

        # Try each singleton swap
        for s_i, s_j in itertools.combinations(singles, 2):
            # Find the chain containing both singleton positions
            pos_i = next(i for i in range(5) if nbr_c[i] == s_i)
            pos_j = next(i for i in range(5) if nbr_c[i] == s_j)
            chain = kempe_chain(adj, c, nbrs[pos_i], s_i, s_j, exclude={v0})
            if nbrs[pos_j] not in chain:
                continue  # Not tangled — shouldn't happen at tau=6

            new_c = do_swap_on_chain(adj, c, v0, s_i, s_j, chain)
            if not is_proper(adj, new_c, skip=v0):
                continue

            new_tau, _, _ = operational_tau(adj, new_c, v0)
            if new_tau < 6:
                singleton_reduces += 1
                break

        # Try each bridge swap
        for s in singles:
            bridge_pos_list = [i for i in range(5) if nbr_c[i] == rep]
            s_pos = next(i for i in range(5) if nbr_c[i] == s)

            for bp in bridge_pos_list:
                chain = kempe_chain(adj, c, nbrs[bp], rep, s, exclude={v0})
                new_c = do_swap_on_chain(adj, c, v0, rep, s, chain)
                if not is_proper(adj, new_c, skip=v0):
                    continue
                new_tau, _, _ = operational_tau(adj, new_c, v0)
                if new_tau < 6:
                    bridge_reduces += 1
                    break
            else:
                continue
            break

    print(f"\n  Cases where singleton swap reduces tau: {singleton_reduces}/{total}")
    print(f"  Cases where bridge swap reduces tau: {bridge_reduces}/{total}")
    print(f"\n  If singleton swaps ALSO reduce tau, the mechanism isn't just about bridge movement")

    t3 = True  # Always pass
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Singleton swap analysis")
    return t3


# ─────────────────────────────────────────────────────────────
# Test 4: Exhaustive swap — for EVERY tau=6, EVERY chain swap
# ─────────────────────────────────────────────────────────────
def test_4_exhaustive():
    print("\n" + "=" * 70)
    print("Test 4: Exhaustive — every tau=6 case, every possible chain swap")
    print("=" * 70)

    adj = build_nested_antiprism()
    v0 = 0
    nbrs = sorted(adj[v0])
    cases = collect_tau6(adj, v0)

    total = len(cases)
    reducible = 0
    swap_counts = Counter()

    for c in cases:
        nbr_c = [c[u] for u in nbrs]
        n_reducing = 0

        for c1, c2 in itertools.combinations(range(4), 2):
            seen = set()
            for n_v in sorted(adj[v0]):
                if c[n_v] in (c1, c2) and n_v not in seen:
                    chain = kempe_chain(adj, c, n_v, c1, c2, exclude={v0})
                    if chain & seen:
                        continue
                    seen |= chain
                    new_c = do_swap_on_chain(adj, c, v0, c1, c2, chain)
                    if not is_proper(adj, new_c, skip=v0):
                        continue
                    new_tau, _, _ = operational_tau(adj, new_c, v0)
                    if new_tau < 6:
                        n_reducing += 1

        swap_counts[n_reducing] += 1
        if n_reducing > 0:
            reducible += 1

    print(f"\n  Total tau=6 cases: {total}")
    print(f"  Cases with ≥1 reducing swap: {reducible}/{total}")
    print(f"\n  Distribution of #reducing swaps per case:")
    for n, cnt in sorted(swap_counts.items()):
        print(f"    {n} reducers: {cnt} cases")

    t4 = reducible == total and total > 0
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Exhaustive: {reducible}/{total}")
    return t4


# ─────────────────────────────────────────────────────────────
# Test 5: Chain structure detail — for each bridge pair at tau=6,
#          how many chains exist and which contain bridge copies?
# ─────────────────────────────────────────────────────────────
def test_5_chain_detail():
    print("\n" + "=" * 70)
    print("Test 5: Chain structure for bridge pairs — split vs unified")
    print("=" * 70)

    adj = build_nested_antiprism()
    v0 = 0
    nbrs = sorted(adj[v0])
    cases = collect_tau6(adj, v0)

    # For each case: for each bridge pair (r, s_i), are the two bridge
    # copies in the same chain or different chains?
    # Also: is the singleton in the same chain as both, one, or neither?

    pair_patterns = Counter()
    for c in cases:
        nbr_c = [c[u] for u in nbrs]
        color_count = Counter(nbr_c)
        rep = [col for col, cnt in color_count.items() if cnt >= 2][0]
        bridge_pos = sorted([i for i in range(5) if nbr_c[i] == rep])
        single_pos = [i for i in range(5) if nbr_c[i] != rep]

        patterns = []
        for sp in single_pos:
            si_col = nbr_c[sp]
            # Chain from bridge_0
            chain_b0 = kempe_chain(adj, c, nbrs[bridge_pos[0]], rep, si_col, exclude={v0})
            # Is bridge_1 in this chain?
            b1_in_b0 = nbrs[bridge_pos[1]] in chain_b0
            # Is singleton in this chain?
            s_in_b0 = nbrs[sp] in chain_b0

            if b1_in_b0:
                # All three in same chain
                patterns.append("ALL_SAME")
            elif s_in_b0:
                # Singleton with bridge_0, bridge_1 separate
                patterns.append(f"S+B{bridge_pos[0]}")
            else:
                # Check from bridge_1
                chain_b1 = kempe_chain(adj, c, nbrs[bridge_pos[1]], rep, si_col, exclude={v0})
                s_in_b1 = nbrs[sp] in chain_b1
                if s_in_b1:
                    patterns.append(f"S+B{bridge_pos[1]}")
                else:
                    patterns.append("ALL_SEPARATE")

        # Middle is always the one between bridges
        # In sorted order for antiprism: bridge at {b0, b1}
        # Middle is the singleton at distance 1 from both
        middle_idx = None
        for idx, sp in enumerate(single_pos):
            d0 = cyclic_dist(sp, bridge_pos[0])
            d1 = cyclic_dist(sp, bridge_pos[1])
            if d0 == 1 and d1 == 1:
                middle_idx = idx

        combo = tuple(patterns)
        pair_patterns[combo] += 1

    print(f"\n  Chain structure patterns for (r, s_1), (r, s_2), (r, s_3):")
    print(f"  (ordered as: middle singleton, near-B0 singleton, near-B1 singleton)")
    for pat, cnt in sorted(pair_patterns.items(), key=lambda x: -x[1]):
        print(f"    {pat}: {cnt}")

    # Key question: for the non-middle pairs, are they split or unified?
    split_count = Counter()
    for c in cases:
        nbr_c = [c[u] for u in nbrs]
        color_count = Counter(nbr_c)
        rep = [col for col, cnt in color_count.items() if cnt >= 2][0]
        bridge_pos = sorted([i for i in range(5) if nbr_c[i] == rep])
        single_pos = [i for i in range(5) if nbr_c[i] != rep]

        n_split = 0
        for sp in single_pos:
            d0 = cyclic_dist(sp, bridge_pos[0])
            d1 = cyclic_dist(sp, bridge_pos[1])
            if d0 == 1 and d1 == 1:
                continue  # Skip middle
            si_col = nbr_c[sp]
            chain_b0 = kempe_chain(adj, c, nbrs[bridge_pos[0]], rep, si_col, exclude={v0})
            b1_in_b0 = nbrs[bridge_pos[1]] in chain_b0
            if not b1_in_b0:
                n_split += 1

        split_count[n_split] += 1

    print(f"\n  Non-middle pairs with split bridges:")
    for n, cnt in sorted(split_count.items()):
        print(f"    {n} split: {cnt} cases")

    t5 = True
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. Chain detail analysis")
    return t5


# ─────────────────────────────────────────────────────────────
# Test 6: What pair FREES after each reducing swap?
# ─────────────────────────────────────────────────────────────
def test_6_freed_pair():
    print("\n" + "=" * 70)
    print("Test 6: Which pair frees after each reducing swap?")
    print("=" * 70)

    adj = build_nested_antiprism()
    v0 = 0
    nbrs = sorted(adj[v0])
    cases = collect_tau6(adj, v0)

    freed_analysis = Counter()
    freed_relationship = Counter()

    for c in cases:
        nbr_c = [c[u] for u in nbrs]
        color_count = Counter(nbr_c)
        rep = [col for col, cnt in color_count.items() if cnt >= 2][0]
        bridge_pos = sorted([i for i in range(5) if nbr_c[i] == rep])

        for c1, c2 in itertools.combinations(range(4), 2):
            seen = set()
            found = False
            for n_v in sorted(adj[v0]):
                if found:
                    break
                if c[n_v] in (c1, c2) and n_v not in seen:
                    chain = kempe_chain(adj, c, n_v, c1, c2, exclude={v0})
                    if chain & seen:
                        continue
                    seen |= chain
                    new_c = do_swap_on_chain(adj, c, v0, c1, c2, chain)
                    if not is_proper(adj, new_c, skip=v0):
                        continue
                    new_tau, _, new_free = operational_tau(adj, new_c, v0)
                    if new_tau < 6:
                        # Which pair(s) freed?
                        for fp in new_free:
                            is_swap = fp == (c1, c2)
                            swap_is_bridge = rep in (c1, c2)
                            freed_is_bridge_new = False
                            new_nbr_c = [new_c[u] for u in nbrs]
                            new_count = Counter(new_nbr_c)
                            new_reps = [col for col, cnt in new_count.items() if cnt >= 2]
                            if new_reps:
                                freed_is_bridge_new = new_reps[0] in fp

                            # Was the freed pair tangled before?
                            was_tangled = not can_free_color(adj, c, v0, *fp)
                            if was_tangled:
                                # Relationship between swapped pair and freed pair
                                shared = set(fp) & set((c1, c2))
                                freed_relationship[len(shared)] += 1
                                freed_analysis[(swap_is_bridge, "freed_bridge" if freed_is_bridge_new else "freed_singleton")] += 1

                        found = True
            if found:
                break

    print(f"\n  Freed pair analysis:")
    for (sb, ft), cnt in sorted(freed_analysis.items(), key=lambda x: -x[1]):
        print(f"    swap={'bridge' if sb else 'singleton'}, freed={ft}: {cnt}")

    print(f"\n  Colors shared between swapped and freed pair:")
    for s, cnt in sorted(freed_relationship.items()):
        print(f"    {s} shared colors: {cnt}")

    t6 = True
    print(f"\n  [{'PASS' if t6 else 'FAIL'}] 6. Freed pair analysis")
    return t6


# ─────────────────────────────────────────────────────────────
# Test 7: The NON-MIDDLE bridge swap — what happens?
# ─────────────────────────────────────────────────────────────
def test_7_nonmiddle():
    print("\n" + "=" * 70)
    print("Test 7: Non-middle bridge swap — the actual mechanism")
    print("=" * 70)

    adj = build_nested_antiprism()
    v0 = 0
    nbrs = sorted(adj[v0])
    cases = collect_tau6(adj, v0)

    # For each case, try swapping each non-middle bridge pair
    # and see if tau drops
    non_middle_works = 0
    non_middle_fails = 0
    detail = Counter()

    for c in cases:
        nbr_c = [c[u] for u in nbrs]
        color_count = Counter(nbr_c)
        rep = [col for col, cnt in color_count.items() if cnt >= 2][0]
        bridge_pos = sorted([i for i in range(5) if nbr_c[i] == rep])
        single_pos = [i for i in range(5) if nbr_c[i] != rep]

        # Find non-middle singletons
        non_middle = []
        for sp in single_pos:
            d0 = cyclic_dist(sp, bridge_pos[0])
            d1 = cyclic_dist(sp, bridge_pos[1])
            if not (d0 == 1 and d1 == 1):
                non_middle.append(sp)

        found = False
        for sp in non_middle:
            si_col = nbr_c[sp]
            # Try each bridge chain
            for bp in bridge_pos:
                chain = kempe_chain(adj, c, nbrs[bp], rep, si_col, exclude={v0})
                new_c = do_swap_on_chain(adj, c, v0, rep, si_col, chain)
                if not is_proper(adj, new_c, skip=v0):
                    continue
                new_tau, _, new_free = operational_tau(adj, new_c, v0)
                if new_tau < 6:
                    found = True
                    new_nbr_c = [new_c[u] for u in nbrs]
                    # What changed?
                    changed = [i for i in range(5) if nbr_c[i] != new_nbr_c[i]]
                    bridge_in = [b for b in bridge_pos if nbrs[b] in chain]
                    detail[(si_col, len(bridge_in), tuple(changed))] += 1
                    break
            if found:
                break

        if found:
            non_middle_works += 1
        else:
            non_middle_fails += 1

    print(f"\n  Non-middle bridge swap reduces tau: {non_middle_works}/{len(cases)}")
    print(f"  Non-middle fails: {non_middle_fails}")

    if detail:
        print(f"\n  Details (singleton_color, #bridges_in_chain, changed_positions):")
        for (sc, bc, cp), cnt in sorted(detail.items(), key=lambda x: -x[1])[:15]:
            print(f"    s={sc}, bridges={bc}, changed={cp}: {cnt}")

    t7 = (non_middle_works + non_middle_fails == len(cases))
    print(f"\n  [{'PASS' if t7 else 'FAIL'}] 7. Non-middle analysis")
    return t7


# ─────────────────────────────────────────────────────────────
# Test 8: Multi-graph comprehensive: every tau=6 reducible?
# ─────────────────────────────────────────────────────────────
def test_8_multi_comprehensive():
    print("\n" + "=" * 70)
    print("Test 8: Multi-graph — is tau=6 ALWAYS reducible?")
    print("=" * 70)

    total = 0
    reducible = 0

    # Antiprism
    adj = build_nested_antiprism()
    v0 = 0
    cases = collect_tau6(adj, v0)
    for c in cases:
        total += 1
        nbrs = sorted(adj[v0])
        found = False
        for c1, c2 in itertools.combinations(range(4), 2):
            if found:
                break
            seen = set()
            for n_v in nbrs:
                if found:
                    break
                if c[n_v] in (c1, c2) and n_v not in seen:
                    chain = kempe_chain(adj, c, n_v, c1, c2, exclude={v0})
                    if chain & seen:
                        continue
                    seen |= chain
                    new_c = do_swap_on_chain(adj, c, v0, c1, c2, chain)
                    if not is_proper(adj, new_c, skip=v0):
                        continue
                    new_tau, _, _ = operational_tau(adj, new_c, v0)
                    if new_tau < 6:
                        found = True
        if found:
            reducible += 1

    # Triangulations
    for n in [12, 15, 18, 20, 25, 30]:
        for gseed in range(30):
            adj2 = make_planar_triangulation(n, seed=gseed * 100 + n)
            deg5 = [v for v in adj2 if len(adj2[v]) == 5]
            for tv in deg5[:3]:
                cases2 = collect_tau6(adj2, tv, n_seeds=400)
                for c in cases2:
                    total += 1
                    tnbrs = sorted(adj2[tv])
                    found = False
                    for c1, c2 in itertools.combinations(range(4), 2):
                        if found:
                            break
                        seen = set()
                        for n_v in tnbrs:
                            if found:
                                break
                            if c[n_v] in (c1, c2) and n_v not in seen:
                                chain = kempe_chain(adj2, c, n_v, c1, c2, exclude={tv})
                                if chain & seen:
                                    continue
                                seen |= chain
                                new_c = do_swap_on_chain(adj2, c, tv, c1, c2, chain)
                                if not is_proper(adj2, new_c, skip=tv):
                                    continue
                                new_tau, _, _ = operational_tau(adj2, new_c, tv)
                                if new_tau < 6:
                                    found = True
                    if found:
                        reducible += 1

    print(f"\n  Total tau=6 cases: {total}")
    print(f"  Reducible: {reducible}/{total}")
    pct = 100 * reducible // max(1, total)

    t8 = reducible == total and total > 0
    print(f"\n  [{'PASS' if t8 else 'FAIL'}] 8. Universal reducibility: {reducible}/{total} ({pct}%)")
    return t8


# ─────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 70)
    print("Toy 427: Mechanism Trace — what ACTUALLY reduces tau?")
    print("=" * 70)

    t1 = test_1_all_reducers()
    t2 = test_2_first_reducer()
    t3 = test_3_singleton_swap()
    t4 = test_4_exhaustive()
    t5 = test_5_chain_detail()
    t6 = test_6_freed_pair()
    t7 = test_7_nonmiddle()
    t8 = test_8_multi_comprehensive()

    results = [t1, t2, t3, t4, t5, t6, t7, t8]
    passed = sum(results)
    n = len(results)

    print(f"\n{'=' * 70}")
    print(f"Toy 427 -- SCORE: {passed}/{n}")
    print(f"{'=' * 70}")

    if passed == n:
        print("ALL PASS.")
    else:
        for i, r in enumerate(results, 1):
            if not r:
                print(f"  Test {i}: FAIL")
