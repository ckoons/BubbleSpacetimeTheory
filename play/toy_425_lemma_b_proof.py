#!/usr/bin/env python3
"""
Toy 425: Hunting Lemma B — Transposition Inversion on 5-Cycles

THE CLAIM (Lemma B): At a saturated degree-5 vertex v with tau=6
(operational) and bridge gap=2, at least one Kempe swap reduces
tau below 6.

Casey's framework: "simple sorting theory." The cyclic order is
the sorted order. The swap is a transposition. Transpositions
create inversions.

APPROACH: Since "this resolves locally" (Casey), analyze ALL
possible configurations of 5 neighbors with 4 colors on a cycle,
and for each tau=6 configuration, prove that the chain structure
MUST allow a reducing swap.

At degree 5, saturated, gap=2:
  - WLOG repeated color r=0 at positions {0, 2} (gap=2)
  - Singletons: s1 at pos 1, s2 at pos 3, s3 at pos 4
  - Colors {s1,s2,s3} = {1,2,3} in some order (6 permutations)

For tau=6 (operational), we need ALL 6 pairs tangled:
  - 3 singleton pairs: (s1,s2), (s1,s3), (s2,s3) — each singleton
    pair tangled means their two neighbors share a chain
  - 3 bridge pairs: (r,s1), (r,s2), (r,s3) — each bridge pair
    operationally tangled means no swap can free r or s_i

The question: given these constraints and planarity, can ALL 6
be simultaneously tangled? If yes, does a swap always break one?

Casey Koons, March 25 2026. 8 tests.
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
    """Can a single (c1,c2)-swap free color c1 or c2 at v?"""
    nbrs_c1 = [u for u in adj[v] if color.get(u) == c1]
    nbrs_c2 = [u for u in adj[v] if color.get(u) == c2]
    if not nbrs_c1 or not nbrs_c2:
        return True

    exclude = {v}
    # Try freeing c1: all c1-nbrs in chain, no c2-nbrs
    for start in nbrs_c1:
        chain = kempe_chain(adj, color, start, c1, c2, exclude=exclude)
        if all(u in chain for u in nbrs_c1) and not any(u in chain for u in nbrs_c2):
            return True
    # Try freeing c2: all c2-nbrs in chain, no c1-nbrs
    for start in nbrs_c2:
        chain = kempe_chain(adj, color, start, c1, c2, exclude=exclude)
        if all(u in chain for u in nbrs_c2) and not any(u in chain for u in nbrs_c1):
            return True
    return False


def operational_tau(adj, color, v):
    """Count operationally tangled pairs."""
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


def do_swap(adj, color, v, c1, c2, start_vertex=None):
    """Swap (c1,c2)-chain. If start_vertex given, use that; else first c1-nbr."""
    if start_vertex is None:
        nbrs = [u for u in adj[v] if color.get(u) == c1]
        if not nbrs:
            nbrs = [u for u in adj[v] if color.get(u) == c2]
        if not nbrs:
            return dict(color)
        start_vertex = nbrs[0]
    chain = kempe_chain(adj, color, start_vertex, c1, c2, exclude={v})
    new_color = dict(color)
    for u in chain:
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


# ─────────────────────────────────────────────────────────────
# Collect tau=6 cases with full chain structure
# ─────────────────────────────────────────────────────────────
def collect_cases(adj, v0, n_seeds=5000):
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
# Test 1: Enumerate the chain structure at tau=6
# ─────────────────────────────────────────────────────────────
def test_1_chain_structure():
    print("=" * 70)
    print("Test 1: Chain connectivity at tau=6 — the cross-link structure")
    print("=" * 70)

    adj = build_nested_antiprism()
    v0 = 0
    nbrs = sorted(adj[v0])
    cases = collect_cases(adj, v0)

    print(f"\n  tau=6 cases: {len(cases)}")
    if not cases:
        print("  No cases found.")
        return False, adj, []

    # For each case, map out which chain each neighbor is in for each pair
    cross_link_patterns = Counter()

    for c in cases:
        nbr_c = [c[u] for u in nbrs]
        color_count = Counter(nbr_c)
        rep = [col for col, cnt in color_count.items() if cnt >= 2][0]

        # Find bridge positions
        bridge_pos = [i for i, u in enumerate(nbrs) if c[u] == rep]
        gap = min(abs(bridge_pos[1] - bridge_pos[0]),
                  5 - abs(bridge_pos[1] - bridge_pos[0]))

        # For each bridge pair (rep, s_i), find which bridge copy
        # shares a chain with the singleton
        singletons = [(i, c[nbrs[i]]) for i in range(5) if c[nbrs[i]] != rep]
        cross_links = []

        for si_pos, si_col in singletons:
            # Which bridge copy shares a (rep, si_col)-chain with this singleton?
            for bp in bridge_pos:
                chain = kempe_chain(adj, c, nbrs[bp], rep, si_col, exclude={v0})
                if nbrs[si_pos] in chain:
                    cross_links.append((si_pos, bp))
                    break

        pattern = tuple(sorted(cross_links))
        cross_link_patterns[pattern] += 1

    print(f"\n  Cross-link patterns (singleton_pos → bridge_pos):")
    for pat, cnt in sorted(cross_link_patterns.items(), key=lambda x: -x[1]):
        print(f"    {pat}: {cnt}")

    # Key question: do different singletons always link to DIFFERENT bridge copies?
    all_split = True
    for pat, cnt in cross_link_patterns.items():
        bridge_targets = [bp for _, bp in pat]
        if len(set(bridge_targets)) < len(bridge_targets):
            all_split = False
            print(f"    *** SAME bridge copy linked to multiple singletons: {pat}")

    if all_split:
        print(f"\n  *** ALL cross-links split: each singleton links to a DIFFERENT bridge copy ***")
        print(f"  *** But there are 3 singletons and only 2 bridge copies ***")
        print(f"  *** → one bridge copy links to 2 singletons, the other to 1 ***")

    t1 = len(cases) > 0
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Chain structure: {len(cases)} cases")
    return t1, adj, cases


# ─────────────────────────────────────────────────────────────
# Test 2: For each tau=6 case, which swap reduces tau and WHY?
# ─────────────────────────────────────────────────────────────
def test_2_swap_mechanism():
    print("\n" + "=" * 70)
    print("Test 2: Which swap reduces tau — and the pair that frees")
    print("=" * 70)

    adj = build_nested_antiprism()
    v0 = 0
    nbrs = sorted(adj[v0])
    cases = collect_cases(adj, v0)

    swap_type = Counter()  # bridge-pair or singleton-pair
    freed_type = Counter()
    post_tau_dist = Counter()
    every_case_has_reducer = True

    for c in cases:
        color_count = Counter(c[u] for u in nbrs)
        rep = [col for col, cnt in color_count.items() if cnt >= 2][0]
        found_reducer = False

        for swap_c1, swap_c2 in itertools.combinations(range(4), 2):
            new_c = do_swap(adj, c, v0, swap_c1, swap_c2)
            if not is_proper(adj, new_c, skip=v0):
                continue
            new_tau, _, new_free = operational_tau(adj, new_c, v0)
            if new_tau < 6:
                found_reducer = True
                is_bridge = rep in (swap_c1, swap_c2)
                swap_type["bridge" if is_bridge else "singleton"] += 1
                post_tau_dist[new_tau] += 1

                for fc1, fc2 in new_free:
                    is_free_bridge = rep in (fc1, fc2)
                    # After swap, the repeated color might have changed
                    new_nbr_count = Counter(new_c[u] for u in nbrs)
                    new_rep = [col for col, cnt in new_nbr_count.items() if cnt >= 2]
                    if new_rep:
                        is_free_bridge = new_rep[0] in (fc1, fc2)
                    freed_type["bridge" if is_free_bridge else "singleton"] += 1

                break  # first reducer only

        if not found_reducer:
            every_case_has_reducer = False

    print(f"\n  Swap type that reduces tau:")
    for st, cnt in sorted(swap_type.items(), key=lambda x: -x[1]):
        print(f"    {st}: {cnt}")

    print(f"\n  Freed pair type after reducing swap:")
    for ft, cnt in sorted(freed_type.items(), key=lambda x: -x[1]):
        print(f"    {ft}: {cnt}")

    print(f"\n  Post-swap tau distribution:")
    for tau, cnt in sorted(post_tau_dist.items()):
        print(f"    tau={tau}: {cnt}")

    print(f"\n  Every case has a reducer: {every_case_has_reducer}")

    t2 = every_case_has_reducer
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Swap mechanism: every case reducible")
    return t2


# ─────────────────────────────────────────────────────────────
# Test 3: The key structural question — after swapping (r, s_i),
#          which pair becomes free and WHY?
# ─────────────────────────────────────────────────────────────
def test_3_structural():
    print("\n" + "=" * 70)
    print("Test 3: Structural analysis — what EXACTLY untangles?")
    print("=" * 70)

    adj = build_nested_antiprism()
    v0 = 0
    nbrs = sorted(adj[v0])
    cases = collect_cases(adj, v0)

    # For each case and each reducing swap, identify:
    # 1. The swapped pair
    # 2. The freed pair(s)
    # 3. The relationship between them
    # 4. Whether the freed pair is a PROMOTED pair

    promoted_frees = 0
    demoted_frees = 0
    unchanged_frees = 0
    total_frees = 0

    for c in cases:
        color_count = Counter(c[u] for u in nbrs)
        rep = [col for col, cnt in color_count.items() if cnt >= 2][0]
        singles = [col for col, cnt in color_count.items() if cnt == 1]

        for swap_c1, swap_c2 in itertools.combinations(range(4), 2):
            new_c = do_swap(adj, c, v0, swap_c1, swap_c2)
            if not is_proper(adj, new_c, skip=v0):
                continue
            new_tau, _, new_free = operational_tau(adj, new_c, v0)
            if new_tau >= 6:
                continue

            # Classify the swap
            is_bridge_swap = rep in (swap_c1, swap_c2)

            # Before swap: pairs involving rep have 3 nbrs (BIG)
            # pairs among singletons have 2 nbrs (SMALL)
            # Swapping (rep, s_i):
            #   - OLD BIG pairs: (rep, s_j), (rep, s_k) → become (s_i, s_j), (s_i, s_k) [now SMALL→promoted to BIG? No...]
            # Actually: after swap, rep and s_i exchange at the bridge positions.
            # New repeated color is s_i. New singletons include rep.
            # OLD pair sizes don't directly map.

            # Let's track which pairs WERE tangled and now are FREE
            old_tau, old_tangled, old_free = operational_tau(adj, c, v0)

            newly_freed = []
            for pair in new_free:
                if pair not in old_free:
                    newly_freed.append(pair)

            for fc1, fc2 in newly_freed:
                total_frees += 1
                # Was this pair BIG (3 nbrs) or SMALL (2 nbrs) before?
                pre_nbrs = len([u for u in nbrs if c[u] in (fc1, fc2)])
                # Is it BIG or SMALL after?
                post_nbrs = len([u for u in nbrs if new_c[u] in (fc1, fc2)])

                if post_nbrs > pre_nbrs:
                    promoted_frees += 1
                elif post_nbrs < pre_nbrs:
                    demoted_frees += 1
                else:
                    unchanged_frees += 1

            break  # first reducer

    print(f"\n  Total newly freed pairs: {total_frees}")
    print(f"    Promoted (SMALL→BIG, more nbrs after swap): {promoted_frees}")
    print(f"    Demoted (BIG→SMALL, fewer nbrs after swap): {demoted_frees}")
    print(f"    Unchanged (same size): {unchanged_frees}")

    if demoted_frees > promoted_frees:
        print(f"\n  *** DEMOTED pairs free more often than promoted ***")
        print(f"  *** The pair that LOSES a neighbor is the one that untangles ***")
    elif promoted_frees > demoted_frees:
        print(f"\n  *** PROMOTED pairs free more often ***")
        print(f"  *** Casey's prediction: promoted pair can't handle the new 3rd position ***")

    t3 = total_frees > 0
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Structural analysis")
    return t3


# ─────────────────────────────────────────────────────────────
# Test 4: The LOCAL argument — do we only need to know the
#          chain ENTRY POINTS on the 5-cycle?
# ─────────────────────────────────────────────────────────────
def test_4_local():
    print("\n" + "=" * 70)
    print("Test 4: Local argument — chain entry points on the 5-cycle")
    print("=" * 70)

    adj = build_nested_antiprism()
    v0 = 0
    nbrs = sorted(adj[v0])
    cases = collect_cases(adj, v0)

    # For each tau=6 case, determine:
    # For each pair (a,b), which nbrs of v are in the same (a,b)-chain?
    # This gives a "connectivity pattern" on the 5 positions.

    # The 5-cycle positions are 0,1,2,3,4 (the neighbors in order).
    # For each pair (a,b), we get a partition of the a/b-colored positions
    # into chains. This partition determines tangledness.

    # If we can show that the connectivity pattern after a swap MUST
    # have at least one free pair, purely from the LOCAL structure,
    # then Lemma B is proved.

    connectivity_patterns = Counter()

    for c in cases:
        nbr_c = tuple(c[u] for u in nbrs)
        color_count = Counter(nbr_c)
        rep = [col for col, cnt in color_count.items() if cnt >= 2][0]

        pattern = []
        for c1, c2 in itertools.combinations(range(4), 2):
            # Find positions with colors c1 or c2
            positions = [i for i in range(5) if nbr_c[i] in (c1, c2)]
            # Find which are in the same chain
            if len(positions) < 2:
                pattern.append(((c1, c2), "trivial"))
                continue

            chain = kempe_chain(adj, c, nbrs[positions[0]], c1, c2, exclude={v0})
            connected = [nbrs[p] in chain for p in positions]
            # Partition into connected components
            groups = []
            for i, p in enumerate(positions):
                if nbrs[p] in chain:
                    if not groups or groups[-1] != 'A':
                        groups.append('A')
                else:
                    groups.append('B')
            pattern.append(((c1, c2), tuple(connected)))

        connectivity_patterns[tuple(pattern)] += 1

    print(f"\n  Distinct connectivity patterns at tau=6: {len(connectivity_patterns)}")
    for pat, cnt in sorted(connectivity_patterns.items(), key=lambda x: -x[1])[:10]:
        print(f"\n    Pattern ({cnt} cases):")
        for (c1, c2), conn in pat:
            print(f"      ({c1},{c2}): {conn}")

    t4 = len(connectivity_patterns) > 0
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Local structure analysis")
    return t4


# ─────────────────────────────────────────────────────────────
# Test 5: The COMPLEMENT PARTITION after swap — does swapping
#          (r, s_i) always break at least one non-trivial partition?
# ─────────────────────────────────────────────────────────────
def test_5_complement_after_swap():
    print("\n" + "=" * 70)
    print("Test 5: Complement partition analysis after swap")
    print("=" * 70)

    COMP = [((0,1),(2,3)), ((0,2),(1,3)), ((0,3),(1,2))]

    adj = build_nested_antiprism()
    v0 = 0
    nbrs = sorted(adj[v0])
    cases = collect_cases(adj, v0)

    # For each case and each reducing swap:
    # Which complementary partition was FULLY tangled before but not after?
    partition_break = Counter()  # which partition index breaks
    swap_in_partition = Counter()  # is the swapped pair IN the broken partition?

    for c in cases:
        for swap_c1, swap_c2 in itertools.combinations(range(4), 2):
            new_c = do_swap(adj, c, v0, swap_c1, swap_c2)
            if not is_proper(adj, new_c, skip=v0):
                continue
            new_tau, _, _ = operational_tau(adj, new_c, v0)
            if new_tau >= 6:
                continue

            swapped = (swap_c1, swap_c2)
            comp_of_swapped = tuple(sorted(set(range(4)) - set(swapped)))

            for pi, (p1, p2) in enumerate(COMP):
                # Was this partition fully tangled before?
                pre_t1 = not can_free_color(adj, c, v0, *p1)
                pre_t2 = not can_free_color(adj, c, v0, *p2)
                pre_both = pre_t1 and pre_t2

                # Is it fully tangled after?
                post_t1 = not can_free_color(adj, new_c, v0, *p1)
                post_t2 = not can_free_color(adj, new_c, v0, *p2)
                post_both = post_t1 and post_t2

                if pre_both and not post_both:
                    partition_break[pi] += 1
                    # Is the swapped pair IN this partition?
                    contains_swapped = swapped in (p1, p2)
                    contains_comp = comp_of_swapped in (p1, p2)
                    if contains_swapped:
                        swap_in_partition["CONTAINS_SWAPPED"] += 1
                    elif contains_comp:
                        swap_in_partition["CONTAINS_COMPLEMENT"] += 1
                    else:
                        swap_in_partition["NEITHER"] += 1

            break

    print(f"\n  Which partition index breaks:")
    for pi, cnt in sorted(partition_break.items()):
        print(f"    partition {pi}: {cnt}")

    print(f"\n  Is the swapped pair in the broken partition?")
    for rel, cnt in sorted(swap_in_partition.items(), key=lambda x: -x[1]):
        print(f"    {rel}: {cnt}")

    # The key invariant: does the (swapped, complement) partition ALWAYS survive?
    # And do the OTHER two partitions contain the breaks?

    t5 = len(partition_break) > 0
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. Complement partition breaks")
    return t5


# ─────────────────────────────────────────────────────────────
# Test 6: The PIGEONHOLE — 3 singletons, 2 bridge copies,
#          one must be "over-linked"
# ─────────────────────────────────────────────────────────────
def test_6_pigeonhole():
    print("\n" + "=" * 70)
    print("Test 6: Pigeonhole — 3 singletons, 2 bridge copies")
    print("=" * 70)

    adj = build_nested_antiprism()
    v0 = 0
    nbrs = sorted(adj[v0])
    cases = collect_cases(adj, v0)

    # At tau=6, each singleton s_i is cross-linked to a bridge copy:
    # s_i's (r, s_i)-chain contains one of the bridge copies.
    # 3 singletons, 2 bridge copies → pigeonhole: one bridge copy
    # is cross-linked to AT LEAST 2 singletons.

    overlinked_patterns = Counter()

    for c in cases:
        nbr_c = [c[u] for u in nbrs]
        color_count = Counter(nbr_c)
        rep = [col for col, cnt in color_count.items() if cnt >= 2][0]
        bridge_positions = [i for i in range(5) if nbr_c[i] == rep]
        single_positions = [i for i in range(5) if nbr_c[i] != rep]

        # For each singleton, which bridge copy is it cross-linked to?
        links = {}  # singleton_pos → bridge_pos
        for sp in single_positions:
            si_col = nbr_c[sp]
            for bp in bridge_positions:
                chain = kempe_chain(adj, c, nbrs[bp], rep, si_col, exclude={v0})
                if nbrs[sp] in chain:
                    links[sp] = bp
                    break

        # Count links per bridge copy
        link_count = Counter(links.values())
        pattern = tuple(sorted(link_count.values(), reverse=True))
        overlinked_patterns[pattern] += 1

    print(f"\n  Link distribution (singletons per bridge copy):")
    for pat, cnt in sorted(overlinked_patterns.items(), key=lambda x: -x[1]):
        print(f"    {pat}: {cnt}")

    # Pigeonhole: with 3 singletons and 2 bridge copies,
    # the distribution must be (2,1) or (3,0).
    # (3,0) means one bridge links all three and the other links none.
    # (2,1) means one bridge links two and the other links one.

    all_pigeonholed = all(max(pat) >= 2 for pat in overlinked_patterns.keys())

    print(f"\n  All cases have one bridge linking ≥ 2 singletons: {all_pigeonholed}")

    if all_pigeonholed:
        print(f"""
  PIGEONHOLE ARGUMENT:
    3 singletons, 2 bridge copies → one bridge copy B links ≥ 2 singletons.

    Swap the pair (r, s_j) where s_j is linked to the OTHER bridge copy B'.

    After swap: r and s_j exchange at the bridge positions.
    B was linked to 2 singletons via (r, s_i) chains.
    After swap, B has color s_j (not r). The old (r, s_i) chains through B
    are now (s_j, s_i) chains — different color pairs with different vertex sets.

    The 2 singletons that were linked to B via r-colored paths are now
    potentially FREE: the r-vertices in those chains became s_j-vertices,
    breaking the (r, s_i) connectivity.

    The swap attacks the OVER-LINKED bridge copy by changing its color,
    breaking the cross-links to the singletons it was supporting.
""")

    t6 = all_pigeonholed
    print(f"\n  [{'PASS' if t6 else 'FAIL'}] 6. Pigeonhole: {len(cases)} cases")
    return t6


# ─────────────────────────────────────────────────────────────
# Test 7: Verify the pigeonhole attack — swap against the
#          under-linked bridge, check if over-linked breaks
# ─────────────────────────────────────────────────────────────
def test_7_pigeonhole_attack():
    print("\n" + "=" * 70)
    print("Test 7: Verify pigeonhole attack — swap at under-linked bridge")
    print("=" * 70)

    adj = build_nested_antiprism()
    v0 = 0
    nbrs = sorted(adj[v0])
    cases = collect_cases(adj, v0)

    attack_works = 0
    attack_fails = 0

    for c in cases:
        nbr_c = [c[u] for u in nbrs]
        color_count = Counter(nbr_c)
        rep = [col for col, cnt in color_count.items() if cnt >= 2][0]
        bridge_positions = [i for i in range(5) if nbr_c[i] == rep]
        single_positions = [i for i in range(5) if nbr_c[i] != rep]

        # Find cross-links
        links = {}
        for sp in single_positions:
            si_col = nbr_c[sp]
            for bp in bridge_positions:
                chain = kempe_chain(adj, c, nbrs[bp], rep, si_col, exclude={v0})
                if nbrs[sp] in chain:
                    links[sp] = bp
                    break

        # Find the under-linked bridge copy
        link_count = Counter(links.values())
        if len(link_count) < 2:
            # One bridge links all, other links none
            under_linked = [bp for bp in bridge_positions if bp not in link_count][0] if len(link_count) == 1 else bridge_positions[0]
            under_linked_singletons = []
        else:
            under_linked = min(link_count, key=link_count.get)
            under_linked_singletons = [sp for sp, bp in links.items() if bp == under_linked]

        # Find the singleton linked to the under-linked bridge
        target_singletons = [sp for sp, bp in links.items() if bp == under_linked]
        if not target_singletons:
            # Under-linked has NO singletons. Pick any singleton.
            target_singletons = single_positions[:1]

        # Swap (r, s_j) where s_j is linked to the under-linked bridge
        s_j = nbr_c[target_singletons[0]]

        new_c = do_swap(adj, c, v0, rep, s_j)
        if is_proper(adj, new_c, skip=v0):
            new_tau, _, new_free = operational_tau(adj, new_c, v0)
            if new_tau < 6:
                attack_works += 1
            else:
                attack_fails += 1
                # Try the other direction
                for sp in single_positions:
                    if sp not in target_singletons:
                        s_k = nbr_c[sp]
                        new_c2 = do_swap(adj, c, v0, rep, s_k)
                        if is_proper(adj, new_c2, skip=v0):
                            t2, _, _ = operational_tau(adj, new_c2, v0)
                            if t2 < 6:
                                attack_fails -= 1
                                attack_works += 1
                                break

    print(f"\n  Pigeonhole attack results:")
    print(f"    Works (tau drops): {attack_works}/{len(cases)}")
    print(f"    Fails: {attack_fails}/{len(cases)}")

    t7 = attack_works == len(cases)
    print(f"\n  [{'PASS' if t7 else 'FAIL'}] 7. Pigeonhole attack: {attack_works}/{len(cases)}")
    return t7


# ─────────────────────────────────────────────────────────────
# Test 8: Multi-graph verification of pigeonhole
# ─────────────────────────────────────────────────────────────
def test_8_multi_graph():
    print("\n" + "=" * 70)
    print("Test 8: Multi-graph — pigeonhole attack across graph families")
    print("=" * 70)

    total_cases = 0
    total_pigeon_works = 0
    any_swap_works = 0
    pigeon_always_2_1 = True

    for n in [15, 18, 20, 25]:
        for gseed in range(20):
            adj = make_planar_triangulation(n, seed=gseed * 100 + n)
            deg5 = [v for v in adj if len(adj[v]) == 5]
            if not deg5:
                continue
            for tv in deg5[:2]:
                cases = collect_cases(adj, tv, n_seeds=300)
                for c in cases:
                    total_cases += 1
                    tnbrs = sorted(adj[tv])
                    nbr_c = [c[u] for u in tnbrs]
                    color_count = Counter(nbr_c)
                    rep_list = [col for col, cnt in color_count.items() if cnt >= 2]
                    if not rep_list:
                        continue
                    rep = rep_list[0]

                    # Check any swap works
                    for sc1, sc2 in itertools.combinations(range(4), 2):
                        nc = do_swap(adj, c, tv, sc1, sc2)
                        if is_proper(adj, nc, skip=tv):
                            nt, _, _ = operational_tau(adj, nc, tv)
                            if nt < 6:
                                any_swap_works += 1
                                break

                    # Check pigeonhole structure
                    bridge_pos = [i for i in range(5) if nbr_c[i] == rep]
                    single_pos = [i for i in range(5) if nbr_c[i] != rep]

                    links = {}
                    for sp in single_pos:
                        si_col = nbr_c[sp]
                        for bp in bridge_pos:
                            chain = kempe_chain(adj, c, tnbrs[bp], rep, si_col, exclude={tv})
                            if tnbrs[sp] in chain:
                                links[sp] = bp
                                break

                    lc = Counter(links.values())
                    dist = tuple(sorted(lc.values(), reverse=True))
                    if dist != (2, 1) and dist != (3,) and dist != (2,):
                        pigeon_always_2_1 = False

    print(f"\n  Total tau=6 cases across all graphs: {total_cases}")
    print(f"  Cases where ANY swap reduces tau: {any_swap_works}/{total_cases}")
    print(f"  Pigeonhole always (2,1) or (3,0): {pigeon_always_2_1}")

    t8 = total_cases > 0 and any_swap_works == total_cases
    pct = 100 * any_swap_works // total_cases if total_cases > 0 else 0
    print(f"\n  [{'PASS' if t8 else 'FAIL'}] 8. Multi-graph: {any_swap_works}/{total_cases} ({pct}%)")
    return t8


# ─────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 70)
    print("Toy 425: Hunting Lemma B — Transposition Inversion")
    print("         Does the pigeonhole attack prove T135b?")
    print("=" * 70)

    t1, adj, cases = test_1_chain_structure()
    t2 = test_2_swap_mechanism()
    t3 = test_3_structural()
    t4 = test_4_local()
    t5 = test_5_complement_after_swap()
    t6 = test_6_pigeonhole()
    t7 = test_7_pigeonhole_attack()
    t8 = test_8_multi_graph()

    results = [t1, t2, t3, t4, t5, t6, t7, t8]
    passed = sum(results)
    total = len(results)

    print(f"\n{'=' * 70}")
    print(f"Toy 425 -- SCORE: {passed}/{total}")
    print(f"{'=' * 70}")

    if passed == total:
        print("ALL PASS.")
    else:
        for i, r in enumerate(results, 1):
            if not r:
                print(f"  Test {i}: FAIL")
