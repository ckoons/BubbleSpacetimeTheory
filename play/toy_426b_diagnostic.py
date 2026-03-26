#!/usr/bin/env python3
"""
Toy 426b: Diagnostic — Which swap reduces tau at tau=6, and WHY?

For each tau=6 case, test all 6 swaps. For each successful swap, analyze:
1. Is it a straddled pair or non-straddled?
2. Does the bridge gap reduce (gap→1)?
3. What's the strict splitting status?
4. If gap stays at 2, what mechanism reduces tau?

Goal: find the universal mechanism that makes at least one swap work.

Casey Koons, March 25 2026.
"""

import itertools
import random
from collections import defaultdict, deque, Counter

# ─── Core utilities (from Toy 421) ───

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


def kempe_chains_tangled(adj, color, v, c1, c2):
    nbrs_c1 = [u for u in adj[v] if color.get(u) == c1]
    nbrs_c2 = [u for u in adj[v] if color.get(u) == c2]
    if not nbrs_c1 or not nbrs_c2:
        return False
    for u1 in nbrs_c1:
        chain = kempe_chain(adj, color, u1, c1, c2, exclude={v})
        for u2 in nbrs_c2:
            if u2 in chain:
                return True
    return False


def count_tangled(adj, color, v):
    pairs = list(itertools.combinations(range(4), 2))
    tangled, free = [], []
    for c1, c2 in pairs:
        if kempe_chains_tangled(adj, color, v, c1, c2):
            tangled.append((c1, c2))
        else:
            free.append((c1, c2))
    return tangled, free


def do_kempe_swap_at(adj, color, v, c1, c2, start_vertex):
    """Swap the chain containing start_vertex."""
    chain = kempe_chain(adj, color, start_vertex, c1, c2, exclude={v})
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


def collect_tau6_cases(adj, target_v, n_seeds=500):
    others = [v for v in sorted(adj.keys()) if v != target_v]
    cases = []
    for seed in range(n_seeds):
        rng = random.Random(seed)
        order = list(others)
        rng.shuffle(order)
        c = greedy_4color_safe(adj, order)
        if c is None:
            continue
        if not is_proper(adj, c, skip=target_v):
            continue
        nbr_c = set(c[u] for u in adj[target_v])
        if len(nbr_c) != 4:
            continue
        tangled, free = count_tangled(adj, c, target_v)
        if len(tangled) == 6:
            cases.append(c)
    return cases


# ─── Analysis ───

def get_cyclic_info(adj, color, v):
    """Get full cyclic structure at v."""
    nbrs = sorted(adj[v])
    n = len(nbrs)
    nbr_colors = [color[u] for u in nbrs]
    color_counts = Counter(nbr_colors)

    repeated = [c for c, cnt in color_counts.items() if cnt >= 2]
    if not repeated:
        return None

    r = repeated[0]
    bridge_pos = [i for i, c in enumerate(nbr_colors) if c == r]
    if len(bridge_pos) != 2:
        return None

    p1, p2 = bridge_pos
    gap = min(abs(p2 - p1), n - abs(p2 - p1))

    # All singletons with their positions
    singletons = {}
    for i in range(n):
        if nbr_colors[i] != r:
            singletons[nbr_colors[i]] = {
                'pos': i,
                'vert': nbrs[i],
                'cyclic_dist_to_b1': min(abs(i - p1), n - abs(i - p1)),
                'cyclic_dist_to_b2': min(abs(i - p2), n - abs(i - p2)),
            }

    # Straddled = between bridge on short arc
    if gap == 2:
        direct_dist = p2 - p1
        if direct_dist == 2:
            between_idx = (p1 + 1) % n
        else:
            between_idx = (p1 - 1) % n
        straddled_color = nbr_colors[between_idx]
    else:
        straddled_color = None

    return {
        'r': r,
        'nbrs': nbrs,
        'nbr_colors': nbr_colors,
        'bridge_pos': (p1, p2),
        'bridge_verts': (nbrs[p1], nbrs[p2]),
        'gap': gap,
        'singletons': singletons,
        'straddled_color': straddled_color,
        'n': n,
    }


def analyze_swap(adj, color, v, c1, c2, info):
    """Analyze what a specific (c1, c2) swap does."""
    r = info['r']
    n = info['n']
    nbrs = info['nbrs']
    b1_vert, b2_vert = info['bridge_verts']
    p1, p2 = info['bridge_pos']

    # Find which neighbors are involved
    nbrs_c1 = [nbrs[i] for i in range(n) if info['nbr_colors'][i] == c1]
    nbrs_c2 = [nbrs[i] for i in range(n) if info['nbr_colors'][i] == c2]

    involves_r = (r in (c1, c2))

    # Check strict splitting for this pair
    if involves_r:
        s_color = c2 if c1 == r else c1
        chain_b1 = kempe_chain(adj, color, b1_vert, c1, c2, exclude={v})
        chain_b2 = kempe_chain(adj, color, b2_vert, c1, c2, exclude={v})
        strict_split = b2_vert not in chain_b1

        s_info = info['singletons'].get(s_color)
        if s_info:
            s_vert = s_info['vert']
            s_with_b1 = s_vert in chain_b1
            s_with_b2 = s_vert in chain_b2
        else:
            s_with_b1 = s_with_b2 = False
    else:
        strict_split = None  # Not applicable
        s_with_b1 = s_with_b2 = None

    # Do the swap (through first c1-neighbor)
    if nbrs_c1:
        new_c = do_kempe_swap_at(adj, color, v, c1, c2, nbrs_c1[0])
    elif nbrs_c2:
        new_c = do_kempe_swap_at(adj, color, v, c1, c2, nbrs_c2[0])
    else:
        return None

    if not is_proper(adj, new_c, skip=v):
        return None

    # Analyze result
    new_nbr_colors = [new_c[u] for u in nbrs]
    new_counts = Counter(new_nbr_colors)
    new_repeated = [c for c, cnt in new_counts.items() if cnt >= 2]

    if new_repeated:
        new_r = new_repeated[0]
        new_bridge_pos = [i for i, c in enumerate(new_nbr_colors) if c == new_r]
        if len(new_bridge_pos) == 2:
            np1, np2 = new_bridge_pos
            new_gap = min(abs(np2 - np1), n - abs(np2 - np1))
        else:
            new_gap = -1  # ≥3 copies, color freed
    else:
        new_gap = 0
        new_r = None

    # Compute new tau
    new_tangled, new_free = count_tangled(adj, new_c, v)
    new_tau = len(new_tangled)

    return {
        'pair': (c1, c2),
        'involves_r': involves_r,
        'strict_split': strict_split,
        's_with_b1': s_with_b1,
        's_with_b2': s_with_b2,
        'new_gap': new_gap,
        'new_tau': new_tau,
        'reduces': new_tau < 6,
        'gap_reduced': new_gap == 1 if new_gap >= 0 else True,
    }


def main():
    print("=" * 70)
    print("Toy 426b: Diagnostic — Which swap works, and WHY?")
    print("=" * 70)

    # ── Part 1: Antiprism analysis ──
    print("\n" + "=" * 70)
    print("PART 1: Nested antiprism — detailed swap analysis")
    print("=" * 70)

    adj = build_nested_antiprism()
    V0 = 0
    cases = collect_tau6_cases(adj, V0, n_seeds=5000)

    print(f"\n  tau=6 cases: {len(cases)}")

    # Track statistics
    reducing_swaps = Counter()  # pair type → count
    mechanism = Counter()
    all_have_reducing = True

    # Per-pair strict splitting stats
    pair_split_counts = Counter()
    pair_total_counts = Counter()

    # Gap→1 analysis
    gap1_when_split = 0
    gap2_when_split = 0
    total_split = 0

    # Singleton-singleton analysis
    ss_reduces = 0
    ss_total = 0

    for ci, c in enumerate(cases):
        info = get_cyclic_info(adj, c, V0)
        if info is None or info['gap'] != 2:
            continue

        has_reducing = False

        for c1, c2 in itertools.combinations(range(4), 2):
            result = analyze_swap(adj, c, V0, c1, c2, info)
            if result is None:
                continue

            if result['involves_r']:
                pair_total_counts['r-pair'] += 1
                if result['strict_split']:
                    pair_split_counts['r-pair'] += 1
                    total_split += 1
                    if result['gap_reduced']:
                        gap1_when_split += 1
                    else:
                        gap2_when_split += 1
            else:
                pair_total_counts['ss-pair'] += 1
                ss_total += 1
                if result['reduces']:
                    ss_reduces += 1

            if result['reduces']:
                has_reducing = True
                if result['involves_r']:
                    if result['strict_split']:
                        if result['gap_reduced']:
                            mechanism['r-pair, split, gap→1'] += 1
                        else:
                            mechanism['r-pair, split, gap=2'] += 1
                    else:
                        if result['new_tau'] < 6:
                            mechanism['r-pair, same-chain, tau-drops'] += 1
                        else:
                            mechanism['r-pair, same-chain, tau=6'] += 1
                else:
                    mechanism['ss-pair reduces'] += 1

        if not has_reducing:
            all_have_reducing = False

    print(f"\n  Every case has ≥ 1 reducing swap: {all_have_reducing}")
    print(f"\n  Mechanism breakdown (counting individual reducing swaps):")
    for mech, count in sorted(mechanism.items(), key=lambda x: -x[1]):
        print(f"    {mech}: {count}")

    print(f"\n  Strict splitting for r-pairs: {pair_split_counts['r-pair']}/{pair_total_counts['r-pair']}")
    print(f"  When split, gap→1: {gap1_when_split}/{total_split}")
    print(f"  When split, gap=2: {gap2_when_split}/{total_split}")
    print(f"  Singleton-singleton pairs that reduce: {ss_reduces}/{ss_total}")

    # ── Detailed first-case analysis ──
    print(f"\n  --- First 5 cases, detailed ---")
    for ci in range(min(5, len(cases))):
        c = cases[ci]
        info = get_cyclic_info(adj, c, V0)
        if info is None:
            continue

        print(f"\n  Case {ci}: colors {info['nbr_colors']}, bridge={info['r']} at pos {info['bridge_pos']}, gap={info['gap']}")
        print(f"    Straddled color: {info['straddled_color']}")
        print(f"    Singletons: ", end="")
        for sc, si in info['singletons'].items():
            print(f"{sc}@pos{si['pos']}(d_b1={si['cyclic_dist_to_b1']},d_b2={si['cyclic_dist_to_b2']}) ", end="")
        print()

        for c1, c2 in itertools.combinations(range(4), 2):
            result = analyze_swap(adj, c, V0, c1, c2, info)
            if result is None:
                continue

            marker = "✓" if result['reduces'] else "✗"
            split_str = f"split={'Y' if result['strict_split'] else 'N'}" if result['strict_split'] is not None else "ss"
            print(f"    {marker} ({c1},{c2}): {split_str}, gap→{result['new_gap']}, tau→{result['new_tau']}")

    # ── Part 2: Multi-graph ──
    print("\n\n" + "=" * 70)
    print("PART 2: Multi-graph — mechanism distribution")
    print("=" * 70)

    multi_mechanism = Counter()
    multi_total = 0
    multi_all_have = True

    # Track: does EVERY case have at least one r-pair with split + gap→1?
    always_has_gap_reduction = True
    # Track: does EVERY case have at least one reducing swap of ANY kind?
    always_has_something = True

    for n in [15, 20, 25, 30]:
        for gseed in range(15):
            adj2 = make_planar_triangulation(n, seed=gseed * 100 + n)
            deg5 = [v for v in adj2 if len(adj2[v]) == 5]
            if not deg5:
                continue

            for tv in deg5[:2]:
                cases2 = collect_tau6_cases(adj2, tv, n_seeds=200)

                for c in cases2:
                    info = get_cyclic_info(adj2, c, tv)
                    if info is None or info['gap'] != 2:
                        continue
                    multi_total += 1

                    has_reducing = False
                    has_gap_reduction = False

                    for c1, c2 in itertools.combinations(range(4), 2):
                        result = analyze_swap(adj2, c, tv, c1, c2, info)
                        if result is None:
                            continue

                        if result['reduces']:
                            has_reducing = True
                            if result['involves_r'] and result['strict_split'] and result['gap_reduced']:
                                has_gap_reduction = True
                                multi_mechanism['r-pair, split, gap→1'] += 1
                            elif result['involves_r'] and result['strict_split']:
                                multi_mechanism['r-pair, split, gap=2'] += 1
                            elif result['involves_r']:
                                multi_mechanism['r-pair, same-chain'] += 1
                            else:
                                multi_mechanism['ss-pair'] += 1

                    if not has_reducing:
                        always_has_something = False
                    if not has_gap_reduction:
                        always_has_gap_reduction = False

    print(f"\n  Total tau=6 cases: {multi_total}")
    print(f"  Every case has ≥ 1 reducing swap: {always_has_something}")
    print(f"  Every case has gap-reduction swap: {always_has_gap_reduction}")
    print(f"\n  Mechanism breakdown:")
    for mech, count in sorted(multi_mechanism.items(), key=lambda x: -x[1]):
        print(f"    {mech}: {count}")

    # ── Part 3: The universal question ──
    print("\n\n" + "=" * 70)
    print("PART 3: The universal mechanism question")
    print("=" * 70)

    # Check: for EVERY tau=6 case across ALL graphs, is there at least one
    # swap where strict splitting holds AND gap→1?

    universal_gap1 = True  # Can we always find a split+gap→1 swap?
    universal_ss = True    # Do singleton-singleton swaps always reduce?

    # Recheck antiprism
    for c in collect_tau6_cases(build_nested_antiprism(), 0, n_seeds=5000):
        info = get_cyclic_info(build_nested_antiprism(), c, 0)
        if info is None or info['gap'] != 2:
            continue

        found_gap1 = False
        found_ss_reduce = False

        adj_a = build_nested_antiprism()
        for c1, c2 in itertools.combinations(range(4), 2):
            result = analyze_swap(adj_a, c, 0, c1, c2, info)
            if result is None:
                continue
            if result['involves_r'] and result.get('strict_split') and result.get('gap_reduced') and result['reduces']:
                found_gap1 = True
            if not result['involves_r'] and result['reduces']:
                found_ss_reduce = True

        if not found_gap1:
            universal_gap1 = False
        if not found_ss_reduce:
            universal_ss = False

    print(f"\n  Gap-reduction route (split + gap→1) always available: {universal_gap1}")
    print(f"  Singleton-singleton swap always reduces: {universal_ss}")

    if not universal_gap1:
        print(f"\n  Gap-reduction does NOT work universally.")
        print(f"  Need Lyra's demotion mechanism for cases without split+gap→1.")

    if universal_ss:
        print(f"\n  INTERESTING: singleton-singleton swaps ALWAYS reduce tau!")
        print(f"  This would be a different proof route entirely.")

    print(f"""
  SUMMARY:
  The reducing swap mechanism is NOT always gap-reduction.
  Multiple mechanisms coexist:
  1. Gap-reduction (split + gap→1 + Lemma A) — works when available
  2. Same-chain r-pair swap — tau drops despite gap=2
  3. Singleton-singleton swap — can reduce tau independently

  The question: what's the UNIVERSAL mechanism?

  Lyra's pigeonhole/demotion (Toy 425) works 100% empirically.
  The gap-reduction route works when strict splitting is available.
  We need the mechanism that covers ALL cases.
""")


if __name__ == "__main__":
    main()
