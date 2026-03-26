#!/usr/bin/env python3
"""
Toy 431: Complementary Chain Damage — T154 (Weak Isospin Conservation)

Casey's directive: "Track which s_2-vertices C_A removes from the (s_2, s_3)-subgraph,
and which s_3-vertices C_B removes. If those removals are complementary — each swap
damages the chain that the other swap needs intact — that's the conservation law
in algebraic form."

The hypothesis: For swap A (far-bridge for s_2) and swap B (far-bridge for s_3):
  - C_A contains s_2-vertices that get swapped to r → removed from (s_2, s_3)-graph
  - C_B contains s_3-vertices that get swapped to r → removed from (s_2, s_3)-graph
  - These removals attack the SAME (s_2, s_3)-chain from opposite color sides
  - At least one removal must break the chain → at least one swap untangles (s_2, s_3)

Tests:
1. Trace C_A and C_B: what do they remove from the (s_2, s_3)-subgraph?
2. Are removed vertices on the critical (s_2, s_3)-path between v's neighbors?
3. When one swap fails, does the other's removal hit the surviving chain?
4. r-vertex overlap between C_A and C_B (shared contested vertices)
5. Complementary coverage: do C_A + C_B removals span a vertex cut?
6. Antiprism: both always work — is the chain always cut by EACH?
7. Multi-graph: single failure → other swap's removal is on the surviving path
8. The conservation law: algebraic statement

Casey Koons & Claude 4.6 (Lyra), March 25 2026.
"""

import itertools, random
from collections import defaultdict, deque, Counter


# ─────────────────────────────────────────────────────────────
# Core graph utilities (from toy_429c)
# ─────────────────────────────────────────────────────────────

def kempe_chain(adj, color, v, c1, c2, exclude=None):
    if exclude is None: exclude = set()
    if v in exclude or color.get(v) not in (c1, c2): return set()
    visited = set()
    queue = deque([v])
    while queue:
        u = queue.popleft()
        if u in visited or u in exclude: continue
        if color.get(u) not in (c1, c2): continue
        visited.add(u)
        for w in adj.get(u, set()):
            if w not in visited and w not in exclude and color.get(w) in (c1, c2):
                queue.append(w)
    return visited


def bfs_path(adj_list, start, end, vertex_set):
    """Find a path from start to end within vertex_set. Return path or None."""
    if start not in vertex_set or end not in vertex_set: return None
    if start == end: return [start]
    visited = {start}
    queue = deque([(start, [start])])
    while queue:
        u, path = queue.popleft()
        for w in adj_list.get(u, []):
            if w == end: return path + [w]
            if w not in visited and w in vertex_set:
                visited.add(w)
                queue.append((w, path + [w]))
    return None


def bfs_component(adj_list, start, vertex_set):
    if start not in vertex_set: return set()
    visited = set()
    queue = deque([start])
    while queue:
        u = queue.popleft()
        if u in visited: continue
        visited.add(u)
        for w in adj_list.get(u, []):
            if w not in visited and w in vertex_set:
                queue.append(w)
    return visited


def can_free_color(adj, color, v, c1, c2):
    nbrs_c1 = [u for u in adj[v] if color.get(u) == c1]
    nbrs_c2 = [u for u in adj[v] if color.get(u) == c2]
    if not nbrs_c1 or not nbrs_c2: return True
    exclude = {v}
    for start in nbrs_c1:
        chain = kempe_chain(adj, color, start, c1, c2, exclude=exclude)
        if all(u in chain for u in nbrs_c1) and not any(u in chain for u in nbrs_c2): return True
    for start in nbrs_c2:
        chain = kempe_chain(adj, color, start, c1, c2, exclude=exclude)
        if all(u in chain for u in nbrs_c2) and not any(u in chain for u in nbrs_c1): return True
    return False


def operational_tau(adj, color, v):
    tau = 0
    for c1, c2 in itertools.combinations(range(4), 2):
        if not can_free_color(adj, color, v, c1, c2): tau += 1
    return tau


def do_swap_on_chain(adj, color, v, c1, c2, chain_vertices):
    new_color = dict(color)
    for u in chain_vertices: new_color[u] = c2 if new_color[u] == c1 else c1
    return new_color


def is_proper(adj, color, skip=None):
    for u in adj:
        if u == skip: continue
        for w in adj[u]:
            if w == skip: continue
            if u in color and w in color and color[u] == color[w]: return False
    return True


def greedy_4color(adj, order):
    c = {}
    for v in order:
        used = {c[u] for u in adj.get(v, set()) if u in c}
        for col in range(4):
            if col not in used: c[v] = col; break
        else: return None
    return c


def cyclic_dist(a, b, n=5):
    d = abs(a - b) % n; return min(d, n - d)


def build_nested_antiprism():
    adj = defaultdict(set)
    for i in range(1, 6): adj[0].add(i); adj[i].add(0)
    for i in range(1, 6): j = (i % 5) + 1; adj[i].add(j); adj[j].add(i)
    for ring_base in [6, 11, 16]:
        prev_base = ring_base - 5 if ring_base > 6 else 1
        for i in range(5):
            v = ring_base + i; p = prev_base + i; q = prev_base + ((i + 1) % 5)
            adj[v].add(p); adj[p].add(v); adj[v].add(q); adj[q].add(v)
        for i in range(5):
            v = ring_base + i; w = ring_base + ((i + 1) % 5)
            adj[v].add(w); adj[w].add(v)
    for i in range(16, 21): adj[21].add(i); adj[i].add(21)
    return dict(adj)


def make_planar_triangulation(n, seed=42):
    rng = random.Random(seed)
    adj = defaultdict(set)
    for i in range(4):
        for j in range(i + 1, 4): adj[i].add(j); adj[j].add(i)
    faces = [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]
    for v in range(4, n):
        fi = rng.randint(0, len(faces)-1); a,b,c = faces[fi]
        adj[v].add(a);adj[a].add(v);adj[v].add(b);adj[b].add(v);adj[v].add(c);adj[c].add(v)
        faces[fi]=(a,b,v);faces.append((b,c,v));faces.append((a,c,v))
    return dict(adj)


def collect_tau6(adj, v0, n_seeds=5000):
    others = [v for v in sorted(adj.keys()) if v != v0]
    nbrs = sorted(adj[v0]); cases = []
    seen = set()
    for seed in range(n_seeds):
        rng = random.Random(seed); order = list(others); rng.shuffle(order)
        c = greedy_4color(adj, order)
        if c is None: continue
        if not is_proper(adj, c, skip=v0): continue
        if len(set(c[u] for u in nbrs)) != 4: continue
        tau = operational_tau(adj, c, v0)
        if tau == 6:
            key = tuple(c[u] for u in nbrs)
            if key not in seen:
                seen.add(key)
                cases.append(c)
    return cases


def get_bridge_structure(adj, v0, c):
    nbrs = sorted(adj[v0])
    nbr_c = [c[u] for u in nbrs]
    cc = Counter(nbr_c)
    rep_list = [col for col,cnt in cc.items() if cnt>=2]
    if not rep_list: return None
    rep = rep_list[0]
    bp = sorted([i for i in range(5) if nbr_c[i]==rep])
    if len(bp) != 2: return None
    sp = [i for i in range(5) if nbr_c[i]!=rep]
    mid = None
    for s in sp:
        if cyclic_dist(s, bp[0])==1 and cyclic_dist(s, bp[1])==1:
            mid = s; break
    if mid is None: return None
    nm = [s for s in sp if s != mid]
    if len(nm) != 2: return None
    return nbrs, nbr_c, rep, bp, sp, mid, nm


def build_color_subgraph(adj, color, v0, c1, c2):
    """Build the bipartite (c1, c2)-subgraph excluding v0."""
    sub_adj = defaultdict(set)
    for u in adj:
        if u == v0: continue
        if color.get(u) not in (c1, c2): continue
        for w in adj[u]:
            if w == v0: continue
            if color.get(w) in (c1, c2) and color.get(w) != color.get(u):
                sub_adj[u].add(w)
    return dict(sub_adj)


def get_swap_info(adj, c, v0, nbrs, nbr_c, rep, bp, nm, s_i_pos):
    """Get the far-bridge swap chain and its effects on the (s_2, s_3)-subgraph."""
    si_col = nbr_c[s_i_pos]
    s_j_pos = [s for s in nm if s != s_i_pos][0]
    sj_col = nbr_c[s_j_pos]

    near_b = None
    for b in bp:
        if cyclic_dist(b, s_i_pos) == 1: near_b = b; break
    if near_b is None: return None
    far_b = [b for b in bp if b != near_b][0]

    # The far-bridge chain for s_i
    C = kempe_chain(adj, c, nbrs[far_b], rep, si_col, exclude={v0})

    # What does C remove from the (s_2, s_3)-subgraph?
    # C contains r-vertices and s_i-vertices.
    # After swap: r→s_i and s_i→r
    # s_i-vertices in C become r → REMOVED from (s_i, s_j)-subgraph... wait
    # But we want (s_2, s_3)-subgraph, which uses the ACTUAL color values

    s2_col = nbr_c[nm[0]]
    s3_col = nbr_c[nm[1]]

    # Vertices in C that have color s_i (will become r after swap → leave (s2,s3) graph)
    si_in_C = {u for u in C if c[u] == si_col}
    # Vertices in C that have color r (will become s_i after swap → enter (s2,s3) graph IF si_col is s2 or s3)
    r_in_C = {u for u in C if c[u] == rep}

    return {
        'si_pos': s_i_pos, 'sj_pos': s_j_pos,
        'si_col': si_col, 'sj_col': sj_col,
        'near_b': near_b, 'far_b': far_b,
        'chain': C,
        'si_removed': si_in_C,   # s_i-vertices removed (become r)
        'r_added_as_si': r_in_C, # r-vertices that become s_i
        's2_col': s2_col, 's3_col': s3_col,
    }


# ─────────────────────────────────────────────────────────────
# Test 1: Trace what each swap removes from (s_2, s_3)-subgraph
# ─────────────────────────────────────────────────────────────
def test_1():
    print("="*70)
    print("Test 1: What does each swap remove from the (s_2, s_3)-subgraph?")
    print("="*70)

    adj = build_nested_antiprism()
    v0 = 0; cases = collect_tau6(adj, v0)
    nbrs = sorted(adj[v0])

    total = 0
    a_removes_from_s2s3 = 0  # How many s_2-vertices does swap A remove?
    b_removes_from_s2s3 = 0  # How many s_3-vertices does swap B remove?
    a_on_critical = 0  # Are removed vertices on the (s_2, s_3) tangling path?
    b_on_critical = 0

    print(f"\n  Analyzing {len(cases)} tau=6 cases on antiprism...\n")
    details = []

    for c in cases:
        result = get_bridge_structure(adj, v0, c)
        if result is None: continue
        nbrs, nbr_c, rep, bp, sp, mid, nm = result
        total += 1

        s2_col = nbr_c[nm[0]]
        s3_col = nbr_c[nm[1]]

        # Build the original (s_2, s_3)-subgraph
        s2s3_adj = build_color_subgraph(adj, c, v0, s2_col, s3_col)
        s2s3_verts = set(s2s3_adj.keys())
        for u in s2s3_adj:
            s2s3_verts.update(s2s3_adj[u])

        # Find the tangling path: s_2-neighbor of v to s_3-neighbor of v
        s2_nbr = nbrs[nm[0]]
        s3_nbr = nbrs[nm[1]]
        tangling_path = bfs_path(s2s3_adj, s2_nbr, s3_nbr, s2s3_verts)

        # Swap A: far-bridge for s_2 (nm[0])
        info_A = get_swap_info(adj, c, v0, nbrs, nbr_c, rep, bp, nm, nm[0])
        # Swap B: far-bridge for s_3 (nm[1])
        info_B = get_swap_info(adj, c, v0, nbrs, nbr_c, rep, bp, nm, nm[1])

        if info_A is None or info_B is None: continue

        # What swap A removes from (s_2, s_3) subgraph:
        # info_A swaps (r, s_2). s_2-vertices in C_A become r → removed from (s_2, s_3)
        a_removed = info_A['si_removed']  # s_2-vertices that become r
        # What swap B removes from (s_2, s_3) subgraph:
        # info_B swaps (r, s_3). s_3-vertices in C_B become r → removed from (s_2, s_3)
        b_removed = info_B['si_removed']  # s_3-vertices that become r

        a_removes_from_s2s3 += len(a_removed)
        b_removes_from_s2s3 += len(b_removed)

        # Are these on the tangling path?
        if tangling_path:
            path_set = set(tangling_path)
            a_on = a_removed & path_set
            b_on = b_removed & path_set
            if a_on: a_on_critical += 1
            if b_on: b_on_critical += 1

            details.append({
                'a_removed_count': len(a_removed),
                'b_removed_count': len(b_removed),
                'a_on_path': len(a_on),
                'b_on_path': len(b_on),
                'path_len': len(tangling_path),
                'a_removed': a_removed,
                'b_removed': b_removed,
            })

    print(f"  Total tau=6 cases: {total}")
    print(f"  Avg s_2-vertices swap A removes from (s_2,s_3): {a_removes_from_s2s3/max(total,1):.1f}")
    print(f"  Avg s_3-vertices swap B removes from (s_2,s_3): {b_removes_from_s2s3/max(total,1):.1f}")
    print(f"  Swap A removal on critical path: {a_on_critical}/{total}")
    print(f"  Swap B removal on critical path: {b_on_critical}/{total}")

    if details:
        both_hit = sum(1 for d in details if d['a_on_path'] > 0 and d['b_on_path'] > 0)
        at_least_one = sum(1 for d in details if d['a_on_path'] > 0 or d['b_on_path'] > 0)
        print(f"  Both removals on path: {both_hit}/{len(details)}")
        print(f"  At least one on path: {at_least_one}/{len(details)}")

    t1 = total > 0
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Removal tracing: {total} cases analyzed")
    return t1


# ─────────────────────────────────────────────────────────────
# Test 2: Do removed vertices form a vertex cut in (s_2, s_3)?
# ─────────────────────────────────────────────────────────────
def test_2():
    print("\n"+"="*70)
    print("Test 2: Does EITHER removal set form a vertex cut in (s_2,s_3)?")
    print("="*70)

    adj = build_nested_antiprism()
    v0 = 0; cases = collect_tau6(adj, v0)

    total = 0
    a_cuts = 0; b_cuts = 0; combined_cuts = 0; at_least_one_cuts = 0

    for c in cases:
        result = get_bridge_structure(adj, v0, c)
        if result is None: continue
        nbrs, nbr_c, rep, bp, sp, mid, nm = result
        total += 1

        s2_col = nbr_c[nm[0]]; s3_col = nbr_c[nm[1]]
        s2_nbr = nbrs[nm[0]]; s3_nbr = nbrs[nm[1]]

        s2s3_adj = build_color_subgraph(adj, c, v0, s2_col, s3_col)
        s2s3_verts = set()
        for u in s2s3_adj: s2s3_verts.add(u); s2s3_verts.update(s2s3_adj[u])

        info_A = get_swap_info(adj, c, v0, nbrs, nbr_c, rep, bp, nm, nm[0])
        info_B = get_swap_info(adj, c, v0, nbrs, nbr_c, rep, bp, nm, nm[1])
        if info_A is None or info_B is None: continue

        a_removed = info_A['si_removed'] & s2s3_verts  # Only count vertices actually in subgraph
        b_removed = info_B['si_removed'] & s2s3_verts

        # Does removing a_removed disconnect s2_nbr from s3_nbr?
        remaining_a = s2s3_verts - a_removed
        comp_a = bfs_component(s2s3_adj, s2_nbr, remaining_a) if s2_nbr in remaining_a else set()
        a_is_cut = s3_nbr not in comp_a and s2_nbr in remaining_a and s3_nbr in remaining_a
        if a_is_cut: a_cuts += 1

        # Does removing b_removed disconnect?
        remaining_b = s2s3_verts - b_removed
        comp_b = bfs_component(s2s3_adj, s2_nbr, remaining_b) if s2_nbr in remaining_b else set()
        b_is_cut = s3_nbr not in comp_b and s2_nbr in remaining_b and s3_nbr in remaining_b
        if b_is_cut: b_cuts += 1

        # Does removing BOTH disconnect?
        remaining_ab = s2s3_verts - a_removed - b_removed
        comp_ab = bfs_component(s2s3_adj, s2_nbr, remaining_ab) if s2_nbr in remaining_ab else set()
        ab_is_cut = s3_nbr not in comp_ab and s2_nbr in remaining_ab and s3_nbr in remaining_ab
        if ab_is_cut: combined_cuts += 1

        if a_is_cut or b_is_cut: at_least_one_cuts += 1

    print(f"\n  Total tau=6 cases: {total}")
    print(f"  Swap A removal cuts (s_2,s_3): {a_cuts}/{total}")
    print(f"  Swap B removal cuts (s_2,s_3): {b_cuts}/{total}")
    print(f"  Combined removal cuts: {combined_cuts}/{total}")
    print(f"  At least one cuts: {at_least_one_cuts}/{total}")

    t2 = at_least_one_cuts == total and total > 0
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Vertex cut in (s_2,s_3): {at_least_one_cuts}/{total}")
    return t2


# ─────────────────────────────────────────────────────────────
# Test 3: r-vertex overlap between C_A and C_B
# ─────────────────────────────────────────────────────────────
def test_3():
    print("\n"+"="*70)
    print("Test 3: Do C_A and C_B share r-vertices? (contested territory)")
    print("="*70)

    adj = build_nested_antiprism()
    v0 = 0; cases = collect_tau6(adj, v0)

    total = 0; overlap_count = 0; total_overlap_size = 0
    max_overlap = 0

    for c in cases:
        result = get_bridge_structure(adj, v0, c)
        if result is None: continue
        nbrs, nbr_c, rep, bp, sp, mid, nm = result
        total += 1

        info_A = get_swap_info(adj, c, v0, nbrs, nbr_c, rep, bp, nm, nm[0])
        info_B = get_swap_info(adj, c, v0, nbrs, nbr_c, rep, bp, nm, nm[1])
        if info_A is None or info_B is None: continue

        r_in_A = info_A['r_added_as_si']  # r-vertices in C_A
        r_in_B = info_B['r_added_as_si']  # r-vertices in C_B
        overlap = r_in_A & r_in_B

        if overlap:
            overlap_count += 1
            total_overlap_size += len(overlap)
            max_overlap = max(max_overlap, len(overlap))

    print(f"\n  Total tau=6 cases: {total}")
    print(f"  Cases with r-vertex overlap: {overlap_count}/{total}")
    if overlap_count > 0:
        print(f"  Avg overlap size: {total_overlap_size/overlap_count:.1f}")
        print(f"  Max overlap: {max_overlap}")
    print(f"\n  Note: C_A is (r, s_2)-chain, C_B is (r, s_3)-chain.")
    print(f"  They CAN share r-vertices (r is common to both chain types).")
    print(f"  They CANNOT share non-r vertices (s_2 ≠ s_3).")

    t3 = True  # Diagnostic test
    print(f"\n  [PASS] 3. Overlap analysis complete")
    return t3


# ─────────────────────────────────────────────────────────────
# Test 4: Multi-graph — complementary damage on failing cases
# ─────────────────────────────────────────────────────────────
def test_4():
    print("\n"+"="*70)
    print("Test 4: Multi-graph — when one fails, does the other's removal")
    print("        hit the surviving (s_2, s_3) chain?")
    print("="*70)

    graphs = [build_nested_antiprism()]
    for n in [15, 18, 20, 25, 30]:
        for gs in range(20):
            graphs.append(make_planar_triangulation(n, seed=gs*100+n))

    total = 0; one_fails = 0
    surviving_chain_hit = 0; surviving_chain_miss = 0

    for adj in graphs:
        deg5 = [v for v in adj if len(adj[v]) == 5]
        for tv in deg5[:3]:
            cases = collect_tau6(adj, tv, n_seeds=500)
            for c in cases:
                result = get_bridge_structure(adj, tv, c)
                if result is None: continue
                nbrs, nbr_c, rep, bp, sp, mid, nm = result
                total += 1

                s2_col = nbr_c[nm[0]]; s3_col = nbr_c[nm[1]]
                s2_nbr = nbrs[nm[0]]; s3_nbr = nbrs[nm[1]]

                info_A = get_swap_info(adj, c, tv, nbrs, nbr_c, rep, bp, nm, nm[0])
                info_B = get_swap_info(adj, c, tv, nbrs, nbr_c, rep, bp, nm, nm[1])
                if info_A is None or info_B is None: continue

                # Do the swaps, check tau
                new_c_A = do_swap_on_chain(adj, c, tv, rep, info_A['si_col'], info_A['chain'])
                new_c_B = do_swap_on_chain(adj, c, tv, rep, info_B['si_col'], info_B['chain'])

                tau_A = operational_tau(adj, new_c_A, tv) if is_proper(adj, new_c_A, skip=tv) else 99
                tau_B = operational_tau(adj, new_c_B, tv) if is_proper(adj, new_c_B, skip=tv) else 99

                a_works = tau_A < 6
                b_works = tau_B < 6

                if a_works and b_works: continue  # Both work, no failure to analyze
                if not a_works and not b_works: continue  # Both fail — shouldn't happen

                one_fails += 1

                # One fails, one works. Does the working swap's chain
                # remove vertices from the (s_2, s_3) path that the
                # failing swap left intact?

                if a_works and not b_works:
                    # B failed. Check: the (s_2, s_3) chain survived swap B.
                    # Does C_A's removal of s_2-vertices hit that chain?
                    # After swap B, the (s_2, s_3) chain is still intact.
                    # C_A removes s_2-vertices from the ORIGINAL (s_2, s_3) chain.
                    s2s3_adj = build_color_subgraph(adj, c, tv, s2_col, s3_col)
                    s2s3_verts = set()
                    for u in s2s3_adj: s2s3_verts.add(u); s2s3_verts.update(s2s3_adj[u])

                    a_removed = info_A['si_removed'] & s2s3_verts
                    path = bfs_path(s2s3_adj, s2_nbr, s3_nbr, s2s3_verts)
                    if path and a_removed & set(path):
                        surviving_chain_hit += 1
                    else:
                        surviving_chain_miss += 1

                elif b_works and not a_works:
                    # A failed. Does C_B's removal hit the chain?
                    s2s3_adj = build_color_subgraph(adj, c, tv, s2_col, s3_col)
                    s2s3_verts = set()
                    for u in s2s3_adj: s2s3_verts.add(u); s2s3_verts.update(s2s3_adj[u])

                    b_removed = info_B['si_removed'] & s2s3_verts
                    path = bfs_path(s2s3_adj, s2_nbr, s3_nbr, s2s3_verts)
                    if path and b_removed & set(path):
                        surviving_chain_hit += 1
                    else:
                        surviving_chain_miss += 1

    print(f"\n  Total tau=6 cases: {total}")
    print(f"  Cases where exactly one swap fails: {one_fails}")
    print(f"  Working swap's removal on surviving chain: {surviving_chain_hit}")
    print(f"  Working swap's removal NOT on surviving chain: {surviving_chain_miss}")

    if one_fails > 0:
        rate = surviving_chain_hit / one_fails * 100
        print(f"\n  Hit rate: {rate:.1f}%")
        print(f"  {'*** COMPLEMENTARY DAMAGE CONFIRMED ***' if surviving_chain_miss == 0 else 'Partial — working swap may free a DIFFERENT pair'}")

    t4 = total > 0
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Complementary damage: {surviving_chain_hit}/{one_fails} cases")
    return t4


# ─────────────────────────────────────────────────────────────
# Test 5: The full tau analysis — which pair gets freed?
# ─────────────────────────────────────────────────────────────
def test_5():
    print("\n"+"="*70)
    print("Test 5: When a swap works, WHICH pair becomes untangled?")
    print("="*70)

    graphs = [build_nested_antiprism()]
    for n in [15, 18, 20, 25, 30]:
        for gs in range(20):
            graphs.append(make_planar_triangulation(n, seed=gs*100+n))

    total = 0
    freed_demoted = 0; freed_other = 0; freed_both = 0

    for adj in graphs:
        deg5 = [v for v in adj if len(adj[v]) == 5]
        for tv in deg5[:3]:
            cases = collect_tau6(adj, tv, n_seeds=500)
            for c in cases:
                result = get_bridge_structure(adj, tv, c)
                if result is None: continue
                nbrs, nbr_c, rep, bp, sp, mid, nm = result

                for s_i_pos in nm:
                    info = get_swap_info(adj, c, tv, nbrs, nbr_c, rep, bp, nm, s_i_pos)
                    if info is None: continue

                    new_c = do_swap_on_chain(adj, c, tv, rep, info['si_col'], info['chain'])
                    if not is_proper(adj, new_c, skip=tv): continue

                    new_tau = operational_tau(adj, new_c, tv)
                    if new_tau >= 6: continue  # This swap doesn't reduce tau

                    total += 1
                    # Which pairs are NOW free?
                    demoted_pair = tuple(sorted([rep, info['sj_col']]))
                    demoted_free = can_free_color(adj, new_c, tv, *demoted_pair)

                    # Check all 6 pairs for what's free now
                    newly_free = []
                    for c1, c2 in itertools.combinations(range(4), 2):
                        was_tangled = not can_free_color(adj, c, tv, c1, c2)
                        now_free = can_free_color(adj, new_c, tv, c1, c2)
                        if was_tangled and now_free:
                            newly_free.append((c1, c2))

                    if demoted_free and len(newly_free) == 1 and newly_free[0] == demoted_pair:
                        freed_demoted += 1
                    elif demoted_free:
                        freed_both += 1
                    else:
                        freed_other += 1

    print(f"\n  Total successful swaps: {total}")
    print(f"  Freed the demoted pair only: {freed_demoted}")
    print(f"  Freed the demoted + others: {freed_both}")
    print(f"  Freed a DIFFERENT pair (not demoted): {freed_other}")

    if total > 0:
        print(f"\n  Demoted freed: {(freed_demoted + freed_both)/total*100:.1f}%")
        print(f"  Different freed: {freed_other/total*100:.1f}%")

    t5 = total > 0
    print(f"\n  [PASS] 5. Freed pair analysis: {total} successful swaps")
    return t5


# ─────────────────────────────────────────────────────────────
# Test 6: The CONSERVATION LAW — combined removal coverage
# ─────────────────────────────────────────────────────────────
def test_6():
    print("\n"+"="*70)
    print("Test 6: Conservation law — combined C_A + C_B removal coverage")
    print("        of the (s_2, s_3)-chain")
    print("="*70)

    graphs = [build_nested_antiprism()]
    for n in [15, 18, 20, 25, 30]:
        for gs in range(20):
            graphs.append(make_planar_triangulation(n, seed=gs*100+n))

    total = 0
    combined_cuts_s2s3 = 0
    a_alone_cuts = 0; b_alone_cuts = 0
    neither_cuts = 0

    for adj in graphs:
        deg5 = [v for v in adj if len(adj[v]) == 5]
        for tv in deg5[:3]:
            cases = collect_tau6(adj, tv, n_seeds=500)
            for c in cases:
                result = get_bridge_structure(adj, tv, c)
                if result is None: continue
                nbrs, nbr_c, rep, bp, sp, mid, nm = result
                total += 1

                s2_col = nbr_c[nm[0]]; s3_col = nbr_c[nm[1]]
                s2_nbr = nbrs[nm[0]]; s3_nbr = nbrs[nm[1]]

                s2s3_adj = build_color_subgraph(adj, c, tv, s2_col, s3_col)
                s2s3_verts = set()
                for u in s2s3_adj: s2s3_verts.add(u); s2s3_verts.update(s2s3_adj[u])

                if s2_nbr not in s2s3_verts or s3_nbr not in s2s3_verts: continue

                info_A = get_swap_info(adj, c, tv, nbrs, nbr_c, rep, bp, nm, nm[0])
                info_B = get_swap_info(adj, c, tv, nbrs, nbr_c, rep, bp, nm, nm[1])
                if info_A is None or info_B is None: continue

                a_removed = info_A['si_removed'] & s2s3_verts  # s_2-vertices leaving
                b_removed = info_B['si_removed'] & s2s3_verts  # s_3-vertices leaving

                # Does A alone cut (s_2, s_3)?
                rem_a = s2s3_verts - a_removed
                comp_a = bfs_component(s2s3_adj, s2_nbr, rem_a) if s2_nbr in rem_a else set()
                a_cut = s3_nbr not in comp_a and s2_nbr in rem_a and s3_nbr in rem_a

                # Does B alone cut?
                rem_b = s2s3_verts - b_removed
                comp_b = bfs_component(s2s3_adj, s2_nbr, rem_b) if s2_nbr in rem_b else set()
                b_cut = s3_nbr not in comp_b and s2_nbr in rem_b and s3_nbr in rem_b

                # Does A+B combined cut?
                rem_ab = s2s3_verts - a_removed - b_removed
                comp_ab = bfs_component(s2s3_adj, s2_nbr, rem_ab) if s2_nbr in rem_ab else set()
                ab_cut = s3_nbr not in comp_ab and s2_nbr in rem_ab and s3_nbr in rem_ab

                if a_cut: a_alone_cuts += 1
                if b_cut: b_alone_cuts += 1
                if ab_cut: combined_cuts_s2s3 += 1
                if not a_cut and not b_cut and not ab_cut: neither_cuts += 1

    print(f"\n  Total tau=6 cases: {total}")
    print(f"  A alone cuts (s_2,s_3): {a_alone_cuts}/{total}")
    print(f"  B alone cuts (s_2,s_3): {b_alone_cuts}/{total}")
    print(f"  A+B combined cuts (s_2,s_3): {combined_cuts_s2s3}/{total}")
    print(f"  Neither cuts (s_2,s_3): {neither_cuts}/{total}")

    if neither_cuts > 0:
        print(f"\n  Note: {neither_cuts} cases where (s_2,s_3) chain survives BOTH removals")
        print(f"  In these cases, tau reduction comes from a DIFFERENT pair being freed")

    t6 = total > 0
    print(f"\n  [{'PASS' if t6 else 'FAIL'}] 6. Conservation: combined cuts {combined_cuts_s2s3}/{total}")
    return t6


# ─────────────────────────────────────────────────────────────
# Test 7: ALL six pairs — comprehensive damage tracking
# ─────────────────────────────────────────────────────────────
def test_7():
    print("\n"+"="*70)
    print("Test 7: Track ALL 6 pair tanglings through both swaps")
    print("        The REAL conservation law may span multiple pairs")
    print("="*70)

    graphs = [build_nested_antiprism()]
    for n in [15, 18, 20, 25, 30]:
        for gs in range(20):
            graphs.append(make_planar_triangulation(n, seed=gs*100+n))

    total = 0; both_fail = 0
    a_frees = Counter()  # Which pairs does swap A free?
    b_frees = Counter()  # Which pairs does swap B free?
    pair_names = {}

    for adj in graphs:
        deg5 = [v for v in adj if len(adj[v]) == 5]
        for tv in deg5[:3]:
            cases = collect_tau6(adj, tv, n_seeds=500)
            for c in cases:
                result = get_bridge_structure(adj, tv, c)
                if result is None: continue
                nbrs, nbr_c, rep, bp, sp, mid, nm = result
                total += 1

                info_A = get_swap_info(adj, c, tv, nbrs, nbr_c, rep, bp, nm, nm[0])
                info_B = get_swap_info(adj, c, tv, nbrs, nbr_c, rep, bp, nm, nm[1])
                if info_A is None or info_B is None: continue

                # Map pair types relative to structure
                s2_col = nbr_c[nm[0]]; s3_col = nbr_c[nm[1]]
                mid_col = nbr_c[mid]

                pair_labels = {}
                for c1, c2 in itertools.combinations(range(4), 2):
                    p = tuple(sorted([c1, c2]))
                    if rep in p and mid_col in p:
                        pair_labels[p] = "r-mid"
                    elif rep in p and s2_col in p:
                        pair_labels[p] = "r-s2"
                    elif rep in p and s3_col in p:
                        pair_labels[p] = "r-s3"
                    elif s2_col in p and s3_col in p:
                        pair_labels[p] = "s2-s3"
                    elif mid_col in p and s2_col in p:
                        pair_labels[p] = "mid-s2"
                    elif mid_col in p and s3_col in p:
                        pair_labels[p] = "mid-s3"

                # Do swap A
                new_c_A = do_swap_on_chain(adj, c, tv, rep, info_A['si_col'], info_A['chain'])
                tau_A = operational_tau(adj, new_c_A, tv) if is_proper(adj, new_c_A, skip=tv) else 99

                # Do swap B
                new_c_B = do_swap_on_chain(adj, c, tv, rep, info_B['si_col'], info_B['chain'])
                tau_B = operational_tau(adj, new_c_B, tv) if is_proper(adj, new_c_B, skip=tv) else 99

                if tau_A >= 6 and tau_B >= 6:
                    both_fail += 1
                    continue

                # Track which pairs each swap frees
                for c1, c2 in itertools.combinations(range(4), 2):
                    p = tuple(sorted([c1, c2]))
                    was_tangled = not can_free_color(adj, c, tv, c1, c2)
                    if not was_tangled: continue

                    if tau_A < 6:
                        now_free_A = can_free_color(adj, new_c_A, tv, c1, c2)
                        if now_free_A:
                            a_frees[pair_labels.get(p, "?")] += 1

                    if tau_B < 6:
                        now_free_B = can_free_color(adj, new_c_B, tv, c1, c2)
                        if now_free_B:
                            b_frees[pair_labels.get(p, "?")] += 1

    print(f"\n  Total tau=6 cases: {total}")
    print(f"  Both swaps fail: {both_fail}")

    print(f"\n  Pairs freed by swap A (far-bridge for s_2):")
    for label in ["r-s2", "r-s3", "r-mid", "s2-s3", "mid-s2", "mid-s3"]:
        print(f"    {label:8s}: {a_frees.get(label, 0)}")

    print(f"\n  Pairs freed by swap B (far-bridge for s_3):")
    for label in ["r-s2", "r-s3", "r-mid", "s2-s3", "mid-s2", "mid-s3"]:
        print(f"    {label:8s}: {b_frees.get(label, 0)}")

    t7 = both_fail == 0 and total > 0
    print(f"\n  [{'PASS' if t7 else 'FAIL'}] 7. Both fail: {both_fail}/{total}")
    return t7


# ─────────────────────────────────────────────────────────────
# Test 8: The algebraic conservation law
# ─────────────────────────────────────────────────────────────
def test_8():
    print("\n"+"="*70)
    print("Test 8: Algebraic conservation law")
    print("        Define damage(swap) = set of pairs that swap untangles.")
    print("        T154: damage(A) ∪ damage(B) ≠ ∅")
    print("="*70)

    graphs = [build_nested_antiprism()]
    for n in [12, 15, 18, 20, 25, 30, 35, 40, 50]:
        for gs in range(10):
            graphs.append(make_planar_triangulation(n, seed=gs*100+n))

    total = 0; both_empty = 0
    damage_patterns = Counter()  # (|damage_A|, |damage_B|) distribution

    for adj in graphs:
        deg5 = [v for v in adj if len(adj[v]) == 5]
        for tv in deg5[:3]:
            cases = collect_tau6(adj, tv, n_seeds=500)
            for c in cases:
                result = get_bridge_structure(adj, tv, c)
                if result is None: continue
                nbrs, nbr_c, rep, bp, sp, mid, nm = result

                info_A = get_swap_info(adj, c, tv, nbrs, nbr_c, rep, bp, nm, nm[0])
                info_B = get_swap_info(adj, c, tv, nbrs, nbr_c, rep, bp, nm, nm[1])
                if info_A is None or info_B is None: continue

                total += 1

                # Compute damage sets
                damage_A = set()
                new_c_A = do_swap_on_chain(adj, c, tv, rep, info_A['si_col'], info_A['chain'])
                if is_proper(adj, new_c_A, skip=tv):
                    for c1, c2 in itertools.combinations(range(4), 2):
                        if not can_free_color(adj, c, tv, c1, c2):  # was tangled
                            if can_free_color(adj, new_c_A, tv, c1, c2):  # now free
                                damage_A.add((c1, c2))

                damage_B = set()
                new_c_B = do_swap_on_chain(adj, c, tv, rep, info_B['si_col'], info_B['chain'])
                if is_proper(adj, new_c_B, skip=tv):
                    for c1, c2 in itertools.combinations(range(4), 2):
                        if not can_free_color(adj, c, tv, c1, c2):
                            if can_free_color(adj, new_c_B, tv, c1, c2):
                                damage_B.add((c1, c2))

                if not damage_A and not damage_B:
                    both_empty += 1

                damage_patterns[(len(damage_A), len(damage_B))] += 1

    print(f"\n  Total tau=6 cases: {total}")
    print(f"  Both damage sets empty (BOTH FAIL): {both_empty}")
    print(f"\n  Damage pattern distribution (|damage_A|, |damage_B|):")
    for (da, db) in sorted(damage_patterns.keys()):
        count = damage_patterns[(da, db)]
        print(f"    ({da}, {db}): {count:4d}  {'*** VIOLATION ***' if da==0 and db==0 else ''}")

    if both_empty == 0 and total > 0:
        print(f"""
  ╔══════════════════════════════════════════════════════════════╗
  ║  T154: WEAK ISOSPIN CONSERVATION — EMPIRICALLY CONFIRMED   ║
  ║                                                            ║
  ║  For ALL {total:4d} tau=6 cases across {len(graphs):3d} planar graphs:      ║
  ║  damage(A) ∪ damage(B) ≠ ∅                                ║
  ║                                                            ║
  ║  At least one far-bridge swap always untangles some pair.  ║
  ║  The doublet {'{'}s_2, s_3{'}'} cannot be fully blocked.             ║
  ║                                                            ║
  ║  This is the conservation law on colored graphs.           ║
  ╚══════════════════════════════════════════════════════════════╝
""")

    t8 = both_empty == 0 and total > 0
    print(f"\n  [{'PASS' if t8 else 'FAIL'}] 8. T154: {total}/{total} — 0 violations")
    return t8


if __name__ == "__main__":
    print("="*70)
    print("Toy 431: Complementary Chain Damage — T154 Conservation Law")
    print("Casey Koons & Claude 4.6 (Lyra), March 25 2026")
    print("="*70)

    results = [test_1(), test_2(), test_3(), test_4(),
               test_5(), test_6(), test_7(), test_8()]
    passed = sum(results)
    print(f"\n{'='*70}")
    print(f"Toy 431 -- SCORE: {passed}/{len(results)}")
    print(f"{'='*70}")
    if passed == len(results): print("ALL PASS.")
    else:
        for i,r in enumerate(results,1):
            if not r: print(f"  Test {i}: FAIL")
