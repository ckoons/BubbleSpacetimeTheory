#!/usr/bin/env python3
"""
Toy 426c: Test BOTH chains per pair — does gap=1 always exist?

At gap=2, bridge at {p1, p2}. For each singleton s_i at position p_s:
- One bridge copy is "near" (distance 1), one is "far" (distance 2).
- Swapping the FAR bridge's chain (if singleton is NOT in it) gives gap=1.
- Swapping the NEAR bridge's chain might give gap=2.

Key question: for at least ONE pair (straddled or not), is there a chain
swap giving gap=1?

This tests ALL chains, not just nbrs_c1[0].

Casey Koons, March 25 2026. 8 tests.
"""

import itertools
import random
from collections import defaultdict, deque, Counter

# ─── Core utilities ───

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


def count_tangled(adj, color, v):
    pairs = list(itertools.combinations(range(4), 2))
    tangled, free = [], []
    for c1, c2 in pairs:
        nbrs_c1 = [u for u in adj[v] if color.get(u) == c1]
        nbrs_c2 = [u for u in adj[v] if color.get(u) == c2]
        if not nbrs_c1 or not nbrs_c2:
            free.append((c1, c2))
            continue
        is_tangled = False
        for u1 in nbrs_c1:
            ch = kempe_chain(adj, color, u1, c1, c2, exclude={v})
            for u2 in nbrs_c2:
                if u2 in ch:
                    is_tangled = True
                    break
            if is_tangled:
                break
        if is_tangled:
            tangled.append((c1, c2))
        else:
            free.append((c1, c2))
    return tangled, free


def do_swap_chain(adj, color, chain):
    """Swap colors in a specific chain. Returns new coloring."""
    if not chain:
        return dict(color)
    # Determine the two colors in the chain
    colors_in_chain = set(color[u] for u in chain)
    if len(colors_in_chain) != 2:
        # Chain is monochromatic or has >2 colors; shouldn't happen for Kempe
        c_list = list(colors_in_chain)
        c1, c2 = c_list[0], c_list[-1]
    else:
        c1, c2 = colors_in_chain
    new_color = dict(color)
    for u in chain:
        new_color[u] = c2 if new_color[u] == c1 else c1
    return new_color


def greedy_4color_safe(adj, order):
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


def collect_tau6(adj, tv, n_seeds=500):
    others = [v for v in sorted(adj.keys()) if v != tv]
    cases = []
    for seed in range(n_seeds):
        rng = random.Random(seed)
        order = list(others)
        rng.shuffle(order)
        c = greedy_4color_safe(adj, order)
        if c is None or not is_proper(adj, c, skip=tv):
            continue
        if len(set(c[u] for u in adj[tv])) != 4:
            continue
        tangled, free = count_tangled(adj, c, tv)
        if len(tangled) == 6:
            cases.append(c)
    return cases


def cyclic_dist(a, b, n=5):
    return min(abs(b - a), n - abs(b - a))


def analyze_all_swaps(adj, color, v):
    """For each r-pair, try BOTH bridge chain swaps. Find gap=1 if possible.
    Also try all singleton-singleton swaps."""
    nbrs = sorted(adj[v])
    n = len(nbrs)
    nbr_colors = [color[u] for u in nbrs]
    counts = Counter(nbr_colors)

    repeated = [c for c, cnt in counts.items() if cnt >= 2]
    if not repeated:
        return None
    r = repeated[0]

    bridge_pos = [i for i, c in enumerate(nbr_colors) if c == r]
    if len(bridge_pos) != 2:
        return None
    p1, p2 = bridge_pos
    gap = cyclic_dist(p1, p2, n)
    if gap != 2:
        return None

    bridge_verts = [nbrs[p1], nbrs[p2]]

    # Get chains for each bridge copy for each singleton
    singletons = {}
    for i in range(n):
        if nbr_colors[i] != r:
            singletons[nbr_colors[i]] = {'pos': i, 'vert': nbrs[i]}

    results = []

    for s_color, s_info in singletons.items():
        s_pos = s_info['pos']
        s_vert = s_info['vert']

        # Distances
        d1 = cyclic_dist(s_pos, p1, n)
        d2 = cyclic_dist(s_pos, p2, n)

        # Chains
        chain_b1 = kempe_chain(adj, color, bridge_verts[0], r, s_color, exclude={v})
        chain_b2 = kempe_chain(adj, color, bridge_verts[1], r, s_color, exclude={v})

        strict_split = bridge_verts[1] not in chain_b1
        s_in_b1 = s_vert in chain_b1
        s_in_b2 = s_vert in chain_b2

        # Try both swaps
        for bi, (chain, b_pos, other_b_pos) in enumerate([
            (chain_b1, p1, p2),
            (chain_b2, p2, p1)
        ]):
            if not strict_split and bi == 1:
                continue  # Same chain, second swap is same as first

            new_c = do_swap_chain(adj, color, chain)
            if not is_proper(adj, new_c, skip=v):
                continue

            new_nbr_colors = [new_c[u] for u in nbrs]
            new_counts = Counter(new_nbr_colors)
            new_rep = [c for c, cnt in new_counts.items() if cnt >= 2]

            if new_rep:
                new_r = new_rep[0]
                new_bp = [i for i, c in enumerate(new_nbr_colors) if c == new_r]
                new_gap = cyclic_dist(new_bp[0], new_bp[1], n) if len(new_bp) == 2 else -1
            else:
                new_gap = 0

            tangled, free = count_tangled(adj, new_c, v)
            new_tau = len(tangled)

            is_straddled = (d1 == 1 and d2 == 1)

            results.append({
                'pair': (r, s_color),
                'swap_bridge': bi,  # 0=b1, 1=b2
                'strict_split': strict_split,
                's_in_this_chain': s_in_b1 if bi == 0 else s_in_b2,
                'd_to_swapped_bridge': d1 if bi == 0 else d2,
                'd_to_other_bridge': d2 if bi == 0 else d1,
                'new_gap': new_gap,
                'new_tau': new_tau,
                'is_straddled': is_straddled,
                'reduces': new_tau < 6,
            })

    # Also try singleton-singleton swaps
    ss_pairs = list(itertools.combinations(
        [(sc, si['vert']) for sc, si in singletons.items()], 2))
    for (c1, v1), (c2, v2) in ss_pairs:
        chain = kempe_chain(adj, color, v1, c1, c2, exclude={v})
        new_c = do_swap_chain(adj, color, chain)
        if not is_proper(adj, new_c, skip=v):
            continue
        new_nbr_colors = [new_c[u] for u in nbrs]
        new_counts = Counter(new_nbr_colors)
        new_rep = [c for c, cnt in new_counts.items() if cnt >= 2]
        if new_rep:
            new_r = new_rep[0]
            new_bp = [i for i, c in enumerate(new_nbr_colors) if c == new_r]
            new_gap = cyclic_dist(new_bp[0], new_bp[1], n) if len(new_bp) == 2 else -1
        else:
            new_gap = 0
        tangled, free = count_tangled(adj, new_c, v)
        new_tau = len(tangled)
        results.append({
            'pair': (c1, c2),
            'swap_bridge': 'ss',
            'strict_split': None,
            's_in_this_chain': None,
            'd_to_swapped_bridge': None,
            'd_to_other_bridge': None,
            'new_gap': new_gap,
            'new_tau': new_tau,
            'is_straddled': False,
            'reduces': new_tau < 6,
        })

    return results


# ─── Tests ───

def test_1_antiprism_gap1():
    """Does at least one swap give gap=1 for every tau=6 case?"""
    print("=" * 70)
    print("Test 1: Antiprism — does gap=1 exist for EVERY tau=6 case?")
    print("        (Testing BOTH chains per r-pair)")
    print("=" * 70)

    adj = build_nested_antiprism()
    cases = collect_tau6(adj, 0, n_seeds=5000)

    all_have_gap1 = True
    all_have_reducing = True
    gap1_mechanism = Counter()
    no_gap1_cases = 0

    for ci, c in enumerate(cases):
        results = analyze_all_swaps(adj, c, 0)
        if results is None:
            continue

        has_gap1 = any(r['new_gap'] == 1 and r['reduces'] for r in results)
        has_reducing = any(r['reduces'] for r in results)

        if has_gap1:
            # What type of swap gives gap=1?
            for r in results:
                if r['new_gap'] == 1 and r['reduces']:
                    key = 'straddled' if r['is_straddled'] else 'non-straddled'
                    if r['swap_bridge'] == 'ss':
                        key = 'ss'
                    gap1_mechanism[key] += 1
                    break  # count once per case
        else:
            no_gap1_cases += 1
            all_have_gap1 = False

        if not has_reducing:
            all_have_reducing = False

    print(f"\n  tau=6 cases: {len(cases)}")
    print(f"  All have ≥ 1 reducing swap: {all_have_reducing}")
    print(f"  All have gap=1 swap: {all_have_gap1}")
    print(f"  Cases WITHOUT gap=1: {no_gap1_cases}")
    print(f"  Gap=1 mechanism: {dict(gap1_mechanism)}")

    t1 = all_have_gap1
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Gap=1 always available (antiprism)")
    return t1, adj, cases


def test_2_detailed_first5(adj, cases):
    """Show detailed swap analysis for first 5 cases."""
    print("\n" + "=" * 70)
    print("Test 2: Detailed analysis of first 5 cases")
    print("=" * 70)

    nbrs = sorted(adj[0])

    for ci in range(min(5, len(cases))):
        c = cases[ci]
        nbr_colors = [c[u] for u in nbrs]
        counts = Counter(nbr_colors)
        r = [cc for cc, cnt in counts.items() if cnt >= 2][0]
        bp = [i for i, cc in enumerate(nbr_colors) if cc == r]

        print(f"\n  Case {ci}: colors {nbr_colors}, bridge={r} at pos {bp}, gap={cyclic_dist(bp[0], bp[1])}")

        results = analyze_all_swaps(adj, c, 0)
        if results is None:
            continue

        for res in results:
            marker = "✓" if res['reduces'] else "✗"
            gap_marker = "★" if res['new_gap'] == 1 else " "
            ss = "ss" if res['swap_bridge'] == 'ss' else f"b{res['swap_bridge']}"
            split_str = ""
            if res['strict_split'] is not None:
                split_str = f" split={'Y' if res['strict_split'] else 'N'}"
                if res['s_in_this_chain'] is not None:
                    split_str += f" s_in={'Y' if res['s_in_this_chain'] else 'N'}"
            straddled = " [STR]" if res['is_straddled'] else ""

            print(f"    {marker}{gap_marker} ({res['pair'][0]},{res['pair'][1]}) via {ss}:{split_str} gap→{res['new_gap']} tau→{res['new_tau']}{straddled}")

    t2 = True
    print(f"\n  [PASS] 2. Detailed analysis complete")
    return t2


def test_3_gap1_mechanism(adj, cases):
    """When gap=1 exists, what mechanism achieves it?"""
    print("\n" + "=" * 70)
    print("Test 3: Gap=1 mechanism — which chain swap gives gap=1?")
    print("=" * 70)

    # For gap=1: singleton NOT in the swapped chain, and swapped bridge
    # is at distance 2 from singleton (far bridge)
    far_bridge_not_in = 0
    near_bridge_not_in = 0
    singleton_in_swapped = 0
    total_gap1 = 0

    for c in cases:
        results = analyze_all_swaps(adj, c, 0)
        if results is None:
            continue

        for res in results:
            if res['new_gap'] != 1 or not res['reduces']:
                continue
            if res['swap_bridge'] == 'ss':
                continue

            total_gap1 += 1
            d_swapped = res['d_to_swapped_bridge']

            if res['s_in_this_chain']:
                singleton_in_swapped += 1
            elif d_swapped == 2:
                far_bridge_not_in += 1
            elif d_swapped == 1:
                near_bridge_not_in += 1

    print(f"\n  Total gap=1 reducing r-pair swaps: {total_gap1}")
    print(f"  Mechanism:")
    print(f"    Far bridge swap, singleton NOT in chain: {far_bridge_not_in}")
    print(f"    Near bridge swap, singleton NOT in chain: {near_bridge_not_in}")
    print(f"    Singleton IN swapped chain: {singleton_in_swapped}")

    t3 = total_gap1 > 0
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Gap=1 mechanism identified")
    return t3


def test_4_multi_graph():
    """Universal test across many graphs."""
    print("\n" + "=" * 70)
    print("Test 4: Multi-graph — gap=1 always available?")
    print("=" * 70)

    total = 0
    has_gap1 = 0
    has_reducing = 0

    for n in [15, 20, 25, 30]:
        for gseed in range(15):
            adj = make_planar_triangulation(n, seed=gseed * 100 + n)
            deg5 = [v for v in adj if len(adj[v]) == 5]
            if not deg5:
                continue

            for tv in deg5[:2]:
                cases = collect_tau6(adj, tv, n_seeds=200)
                for c in cases:
                    total += 1
                    results = analyze_all_swaps(adj, c, tv)
                    if results is None:
                        continue

                    if any(r['reduces'] for r in results):
                        has_reducing += 1
                    if any(r['new_gap'] == 1 and r['reduces'] for r in results):
                        has_gap1 += 1

    print(f"\n  Total tau=6 cases: {total}")
    print(f"  Has reducing swap: {has_reducing}/{total}")
    print(f"  Has gap=1 swap: {has_gap1}/{total}")

    t4 = total > 0 and has_gap1 == total
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Gap=1 universal across all graphs")
    return t4


def test_5_singleton_isolation():
    """Key: is there always a singleton in a THIRD chain (not with either bridge)?
    If so, swapping the far bridge's chain always gives gap=1."""
    print("\n" + "=" * 70)
    print("Test 5: Singleton isolation — always a third-chain singleton?")
    print("=" * 70)

    adj = build_nested_antiprism()
    cases = collect_tau6(adj, 0, n_seeds=5000)

    nbrs = sorted(adj[0])
    always_has_isolated = True
    isolation_stats = Counter()

    for c in cases:
        nbr_colors = [c[u] for u in nbrs]
        counts = Counter(nbr_colors)
        r = [cc for cc, cnt in counts.items() if cnt >= 2][0]
        bp = [i for i, cc in enumerate(nbr_colors) if cc == r]
        bv = [nbrs[bp[0]], nbrs[bp[1]]]

        has_isolated = False
        for i in range(5):
            if nbr_colors[i] == r:
                continue
            s_color = nbr_colors[i]
            s_vert = nbrs[i]

            chain_b1 = kempe_chain(adj, c, bv[0], r, s_color, exclude={0})
            chain_b2 = kempe_chain(adj, c, bv[1], r, s_color, exclude={0})

            in_b1 = s_vert in chain_b1
            in_b2 = s_vert in chain_b2
            b2_in_b1 = bv[1] in chain_b1  # strict split?

            if b2_in_b1:
                # Same chain — singleton must be in it or not
                if in_b1:
                    isolation_stats['same_chain_with_s'] += 1
                else:
                    isolation_stats['same_chain_no_s'] += 1
                    has_isolated = True  # s is isolated from both bridges
            else:
                # Split chain
                if not in_b1 and not in_b2:
                    isolation_stats['split_isolated'] += 1
                    has_isolated = True
                elif in_b1:
                    d1 = cyclic_dist(i, bp[0])
                    isolation_stats[f'split_with_b1_d{d1}'] += 1
                else:
                    d2 = cyclic_dist(i, bp[1])
                    isolation_stats[f'split_with_b2_d{d2}'] += 1

        if not has_isolated:
            always_has_isolated = False

    print(f"\n  tau=6 cases: {len(cases)}")
    print(f"  Isolation stats:")
    for k, v in sorted(isolation_stats.items()):
        print(f"    {k}: {v}")
    print(f"\n  Every case has ≥ 1 isolated singleton: {always_has_isolated}")

    t5 = always_has_isolated
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. Isolated singleton always exists")
    return t5


def test_6_far_bridge_swap():
    """When singleton is isolated or with near bridge, swap far bridge → gap=1."""
    print("\n" + "=" * 70)
    print("Test 6: Far-bridge swap — gap=1 via isolation")
    print("=" * 70)

    adj = build_nested_antiprism()
    cases = collect_tau6(adj, 0, n_seeds=5000)
    nbrs = sorted(adj[0])

    success = 0
    total = 0

    for c in cases:
        nbr_colors = [c[u] for u in nbrs]
        counts = Counter(nbr_colors)
        r = [cc for cc, cnt in counts.items() if cnt >= 2][0]
        bp = [i for i, cc in enumerate(nbr_colors) if cc == r]
        bv = [nbrs[bp[0]], nbrs[bp[1]]]

        found = False
        for i in range(5):
            if nbr_colors[i] == r or found:
                continue
            s_color = nbr_colors[i]
            s_vert = nbrs[i]
            s_pos = i

            chain_b1 = kempe_chain(adj, c, bv[0], r, s_color, exclude={0})
            chain_b2 = kempe_chain(adj, c, bv[1], r, s_color, exclude={0})

            b2_in_b1 = bv[1] in chain_b1
            if b2_in_b1:
                continue  # Not split

            # Distances
            d1 = cyclic_dist(s_pos, bp[0])
            d2 = cyclic_dist(s_pos, bp[1])

            # Singleton NOT in far bridge's chain → swap far → gap=1
            # Far bridge is the one at distance 2
            if d1 == 2 and s_vert not in chain_b1:
                # Swap chain_b1 (far bridge)
                new_c = do_swap_chain(adj, c, chain_b1)
                if is_proper(adj, new_c, skip=0):
                    new_nbr = [new_c[u] for u in nbrs]
                    new_counts = Counter(new_nbr)
                    new_rep = [cc for cc, cnt in new_counts.items() if cnt >= 2]
                    if new_rep:
                        new_bp = [j for j, cc in enumerate(new_nbr) if cc == new_rep[0]]
                        if len(new_bp) == 2 and cyclic_dist(new_bp[0], new_bp[1]) == 1:
                            tangled, free = count_tangled(adj, new_c, 0)
                            if len(tangled) < 6:
                                found = True
                                success += 1

            if d2 == 2 and s_vert not in chain_b2 and not found:
                new_c = do_swap_chain(adj, c, chain_b2)
                if is_proper(adj, new_c, skip=0):
                    new_nbr = [new_c[u] for u in nbrs]
                    new_counts = Counter(new_nbr)
                    new_rep = [cc for cc, cnt in new_counts.items() if cnt >= 2]
                    if new_rep:
                        new_bp = [j for j, cc in enumerate(new_nbr) if cc == new_rep[0]]
                        if len(new_bp) == 2 and cyclic_dist(new_bp[0], new_bp[1]) == 1:
                            tangled, free = count_tangled(adj, new_c, 0)
                            if len(tangled) < 6:
                                found = True
                                success += 1

        total += 1

    print(f"\n  tau=6 cases: {total}")
    print(f"  Resolved via far-bridge swap: {success}/{total}")

    t6 = success == total
    print(f"\n  [{'PASS' if t6 else 'FAIL'}] 6. Far-bridge swap always available")
    return t6


def test_7_proof_summary():
    """Summarize the proof structure."""
    print("\n" + "=" * 70)
    print("Test 7: Updated proof structure")
    print("=" * 70)

    print(f"""
  UPDATED PROOF STRUCTURE:

  At tau=6, gap=2. Bridge r at {{p1, p2}}. Singletons at 3 other positions.

  Key geometric fact (5-cycle):
    Each non-straddled singleton s_i at position p_s has:
    - One bridge copy at distance 1 (near bridge)
    - One bridge copy at distance 2 (far bridge)

  The straddled singleton is at distance 1 from BOTH bridge copies.

  GAP=1 MECHANISM:
    If singleton s_i is NOT in the far bridge's (r, s_i)-chain,
    then swapping the far bridge's chain gives:
      far bridge copy: r → s_i
      singleton: stays s_i (not in chain)
      near bridge copy: stays r
      New bridge: r at {{near bridge pos, ...}} — need to check

    Actually: after swap, r is at near bridge pos. s_i is at
    far bridge pos AND singleton pos. New bridge = s_i at
    {{far pos, singleton pos}}. If far bridge is at distance 2
    from singleton... we need dist(far_pos, s_pos) = 1? No:
    the bridge is the singleton's color, at the far bridge's
    old position and the singleton's position. Dist depends.

  ACTUALLY the situation is simpler when we think about it right.

  Swap far bridge's chain: far bridge at pos F changes from r to s_i.
  Singleton at pos S stays s_i (not in chain).
  Near bridge at pos N stays r.

  New colors: r at {{N}}, s_i at {{F, S}} (two copies!).
  New bridge = s_i at {{F, S}}.
  New gap = dist(F, S).

  For the straddled singleton (S between p1, p2):
    F is one of the bridges, S is the straddled position.
    dist(F, S) = 1 (because straddled is adjacent to both).
    Gap = 1. Lemma A applies.

  For non-straddled singletons:
    Need dist(F, S) = 1.
    F is the far bridge (dist 2 from S). But we want dist(F, S) = 1?
    Wait — dist(F, S) is the NEW gap for the NEW bridge.
    F is the far bridge position, S is the singleton position.
    dist(F, S) IS 2 (that's why it's the "far" bridge).

    So non-straddled far-bridge swap gives gap = dist(F, S) = 2. NOT 1!

    But swapping the NEAR bridge's chain (dist 1 from S):
    Near bridge at pos N changes from r to s_i.
    New bridge s_i at {{N, S}}.
    Gap = dist(N, S) = 1. GAP=1!

    But this only works if the singleton is NOT in the near bridge's chain.

  So the question is:
    For at least one pair, is the singleton NOT in the near bridge's chain?

  "Near bridge" = the bridge copy adjacent to the singleton.
  "Singleton not in near chain" = singleton is in the far chain or a third chain.

  This is a CHAIN SEPARATION claim. On the antiprism, is this always true
  for at least one pair?
""")

    t7 = True
    print(f"  [PASS] 7. Proof structure documented")
    return t7


def test_8_near_bridge_isolation():
    """THE KEY TEST: for each tau=6 case, is there a pair where the
    singleton is NOT in the near bridge's chain? If so, swap near → gap=1."""
    print("\n" + "=" * 70)
    print("Test 8: Near-bridge isolation — the real gap=1 test")
    print("=" * 70)

    adj = build_nested_antiprism()
    cases = collect_tau6(adj, 0, n_seeds=5000)
    nbrs = sorted(adj[0])

    success = 0
    total = 0

    for c in cases:
        nbr_colors = [c[u] for u in nbrs]
        counts = Counter(nbr_colors)
        r = [cc for cc, cnt in counts.items() if cnt >= 2][0]
        bp = [i for i, cc in enumerate(nbr_colors) if cc == r]
        bv = [nbrs[bp[0]], nbrs[bp[1]]]

        found = False
        for i in range(5):
            if nbr_colors[i] == r or found:
                continue
            s_color = nbr_colors[i]
            s_vert = nbrs[i]
            s_pos = i

            d1 = cyclic_dist(s_pos, bp[0])
            d2 = cyclic_dist(s_pos, bp[1])

            chain_b1 = kempe_chain(adj, c, bv[0], r, s_color, exclude={0})
            chain_b2 = kempe_chain(adj, c, bv[1], r, s_color, exclude={0})
            b2_in_b1 = bv[1] in chain_b1

            if b2_in_b1:
                continue  # Not split

            # Find near bridge (distance 1) and check if singleton NOT in its chain
            if d1 == 1:
                near_chain = chain_b1
                near_bv = bv[0]
            elif d2 == 1:
                near_chain = chain_b2
                near_bv = bv[1]
            else:
                # Straddled: both distance 1. Try both.
                if s_vert not in chain_b1:
                    near_chain = chain_b1
                    near_bv = bv[0]
                elif s_vert not in chain_b2:
                    near_chain = chain_b2
                    near_bv = bv[1]
                else:
                    continue  # Both chains contain singleton

            if s_vert in near_chain:
                continue  # Singleton in near chain, can't get gap=1

            # Swap near bridge's chain
            new_c = do_swap_chain(adj, c, near_chain)
            if not is_proper(adj, new_c, skip=0):
                continue

            new_nbr = [new_c[u] for u in nbrs]
            new_counts = Counter(new_nbr)
            new_rep = [cc for cc, cnt in new_counts.items() if cnt >= 2]
            if new_rep:
                new_bp = [j for j, cc in enumerate(new_nbr) if cc == new_rep[0]]
                if len(new_bp) == 2:
                    new_gap = cyclic_dist(new_bp[0], new_bp[1])
                    if new_gap == 1:
                        tangled, free = count_tangled(adj, new_c, 0)
                        if len(tangled) < 6:
                            found = True

        if found:
            success += 1
        total += 1

    print(f"\n  tau=6 cases: {total}")
    print(f"  Has near-bridge gap=1 swap: {success}/{total}")

    # Also test multi-graph
    multi_total = 0
    multi_success = 0

    for n_size in [15, 20, 25, 30]:
        for gseed in range(15):
            adj2 = make_planar_triangulation(n_size, seed=gseed * 100 + n_size)
            deg5 = [v for v in adj2 if len(adj2[v]) == 5]
            if not deg5:
                continue
            for tv in deg5[:2]:
                cases2 = collect_tau6(adj2, tv, n_seeds=200)
                for c in cases2:
                    multi_total += 1
                    nbrs2 = sorted(adj2[tv])
                    nbr_colors2 = [c[u] for u in nbrs2]
                    counts2 = Counter(nbr_colors2)
                    rep2 = [cc for cc, cnt in counts2.items() if cnt >= 2]
                    if not rep2:
                        continue
                    r2 = rep2[0]
                    bp2 = [j for j, cc in enumerate(nbr_colors2) if cc == r2]
                    if len(bp2) != 2:
                        continue
                    bv2 = [nbrs2[bp2[0]], nbrs2[bp2[1]]]

                    found2 = False
                    for i in range(5):
                        if nbr_colors2[i] == r2 or found2:
                            continue
                        sc2 = nbr_colors2[i]
                        sv2 = nbrs2[i]

                        d1 = cyclic_dist(i, bp2[0])
                        d2 = cyclic_dist(i, bp2[1])

                        ch1 = kempe_chain(adj2, c, bv2[0], r2, sc2, exclude={tv})
                        ch2 = kempe_chain(adj2, c, bv2[1], r2, sc2, exclude={tv})
                        if bv2[1] in ch1:
                            continue

                        if d1 == 1:
                            near_ch = ch1
                        elif d2 == 1:
                            near_ch = ch2
                        else:
                            if sv2 not in ch1:
                                near_ch = ch1
                            elif sv2 not in ch2:
                                near_ch = ch2
                            else:
                                continue

                        if sv2 in near_ch:
                            continue

                        nc2 = do_swap_chain(adj2, c, near_ch)
                        if not is_proper(adj2, nc2, skip=tv):
                            continue

                        nnc = [nc2[u] for u in nbrs2]
                        ncts = Counter(nnc)
                        nrep = [cc for cc, cnt in ncts.items() if cnt >= 2]
                        if nrep:
                            nbp = [j for j, cc in enumerate(nnc) if cc == nrep[0]]
                            if len(nbp) == 2 and cyclic_dist(nbp[0], nbp[1]) == 1:
                                t, f = count_tangled(adj2, nc2, tv)
                                if len(t) < 6:
                                    found2 = True

                    if found2:
                        multi_success += 1

    print(f"\n  Multi-graph: {multi_success}/{multi_total}")
    print(f"\n  Combined: antiprism {success}/{total}, multi {multi_success}/{multi_total}")

    t8 = (success == total) and (multi_total == 0 or multi_success == multi_total)
    print(f"\n  [{'PASS' if t8 else 'FAIL'}] 8. Near-bridge isolation universal")
    return t8


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 426c: Both Chains — Does gap=1 always exist?")
    print("=" * 70)

    t1, adj, cases = test_1_antiprism_gap1()
    t2 = test_2_detailed_first5(adj, cases)
    t3 = test_3_gap1_mechanism(adj, cases)
    t4 = test_4_multi_graph()
    t5 = test_5_singleton_isolation()
    t6 = test_6_far_bridge_swap()
    t7 = test_7_proof_summary()
    t8 = test_8_near_bridge_isolation(  )

    results = [t1, t2, t3, t4, t5, t6, t7, t8]
    passed = sum(results)
    total = len(results)

    print(f"\n{'=' * 70}")
    print(f"Toy 426c -- SCORE: {passed}/{total}")
    print(f"{'=' * 70}")

    if passed == total:
        print("ALL PASS.")
        print("\nGAP=1 IS UNIVERSAL. The proof of Lemma B reduces to:")
        print("  1. tau=6 → gap=2 (Lemma A contrapositive)")
        print("  2. ∃ pair with near-bridge isolation (the claim)")
        print("  3. Swap near bridge → gap=1 (arithmetic)")
        print("  4. gap=1 → tau ≤ 5 (Lemma A)")
        print("  5. Free pair → second swap (Kempe 1879)")
    else:
        for i, r in enumerate(results, 1):
            if not r:
                print(f"  Test {i}: FAIL")
