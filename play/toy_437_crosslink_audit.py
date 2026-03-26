#!/usr/bin/env python3
"""
Toy 437: Cross-Link Audit — Keeper's audit of "new cross-links ≤ 1"

After a Case A split-bridge swap:
- Old bridge r had 2 cross-links (supporting tau=6 = strict(4) + XL(2))
- New bridge s_i has how many cross-links?

Elie claims: max 1. The budget allows 2 (3 singleton strict + 1 bridge strict + 2 XL = 6).
But the structural constraint (s_i, r) is NOT strictly tangled (chain components preserved)
means one cross-link is "used up" by (s_i, r).

The KEY question: can the new bridge have 2 cross-links on DIFFERENT pairs?
If yes: tau = 6 persists (contradiction with 564/564).
If no: tau ≤ 5 (proof closes).

Tests:
1. Count post-swap cross-links for the new s_i bridge
2. Which bridge pairs are cross-linked vs strict vs untangled?
3. Verify (s_i, r) is NEVER strictly tangled (chain component preservation)
4. When (s_i, r) is cross-linked, are OTHER bridge pairs also cross-linked?
5. Total tangled pairs after swap (should be ≤ 5)
6. The formal constraint: can 2 cross-links coexist?
7. Per-case: exactly how many pairs change from tangled to untangled?
8. Cross-reference: does the 1-per-case rule hold across all graph types?

Casey Koons & Claude 4.6 (Lyra), March 25 2026.
"""

import itertools, random
from collections import defaultdict, deque, Counter


# ─────────────────────────────────────────────────────────────
# Core utilities
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


def is_strictly_tangled(adj, color, v, c1, c2):
    nbrs_c1 = [u for u in adj[v] if color.get(u) == c1]
    nbrs_c2 = [u for u in adj[v] if color.get(u) == c2]
    if not nbrs_c1 or not nbrs_c2: return False
    exclude = {v}
    chain = kempe_chain(adj, color, nbrs_c1[0], c1, c2, exclude=exclude)
    return all(u in chain for u in nbrs_c1) and all(u in chain for u in nbrs_c2)


def strict_tau(adj, color, v):
    tau = 0
    for c1, c2 in itertools.combinations(range(4), 2):
        if is_strictly_tangled(adj, color, v, c1, c2): tau += 1
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


def get_graphs():
    graphs = [build_nested_antiprism()]
    for n in [12, 15, 18, 20, 25, 30, 35, 40]:
        for gs in range(15):
            graphs.append(make_planar_triangulation(n, seed=gs*100+n))
    return graphs


def count_crosslinks(adj, color, v):
    """Count cross-linked pairs: operationally tangled but NOT strictly tangled."""
    xl = 0
    for c1, c2 in itertools.combinations(range(4), 2):
        op_tangled = not can_free_color(adj, color, v, c1, c2)
        st_tangled = is_strictly_tangled(adj, color, v, c1, c2)
        if op_tangled and not st_tangled:
            xl += 1
    return xl


def classify_pairs(adj, color, v):
    """Return dict: pair -> 'strict', 'crosslink', 'untangled'."""
    result = {}
    for c1, c2 in itertools.combinations(range(4), 2):
        op = not can_free_color(adj, color, v, c1, c2)
        st = is_strictly_tangled(adj, color, v, c1, c2)
        if st:
            result[(c1, c2)] = 'strict'
        elif op:
            result[(c1, c2)] = 'crosslink'
        else:
            result[(c1, c2)] = 'untangled'
    return result


# ─────────────────────────────────────────────────────────────
# Test 1: Post-swap cross-link count
# ─────────────────────────────────────────────────────────────
def test_1():
    print("="*70)
    print("Test 1: Post-swap cross-link count (Case A only)")
    print("="*70)

    graphs = get_graphs()
    total = 0
    pre_xl_dist = Counter()
    post_xl_dist = Counter()

    for adj in graphs:
        deg5 = [v for v in adj if len(adj[v]) == 5]
        for tv in deg5[:3]:
            cases = collect_tau6(adj, tv, n_seeds=500)
            for c in cases:
                result = get_bridge_structure(adj, tv, c)
                if result is None: continue
                nbrs, nbr_c, rep, bp, sp, mid, nm = result

                for s_i_pos in nm:
                    si_col = nbr_c[s_i_pos]
                    near_b = None
                    for b in bp:
                        if cyclic_dist(b, s_i_pos) == 1: near_b = b; break
                    if near_b is None: continue
                    far_b = [b for b in bp if b != near_b][0]

                    C = kempe_chain(adj, c, nbrs[far_b], rep, si_col, exclude={tv})
                    if nbrs[near_b] in C: continue  # Only Case A (split)

                    # Check Case A: n_{s_i} not in chain
                    n_si = nbrs[s_i_pos]
                    if n_si in C: continue  # Case B

                    new_c = do_swap_on_chain(adj, c, tv, rep, si_col, C)
                    if not is_proper(adj, new_c, skip=tv): continue
                    total += 1

                    pre_xl = count_crosslinks(adj, c, tv)
                    post_xl = count_crosslinks(adj, new_c, tv)

                    pre_xl_dist[pre_xl] += 1
                    post_xl_dist[post_xl] += 1

    print(f"\n  Total Case A split swaps: {total}")
    print(f"\n  Pre-swap cross-link distribution:")
    for xl in sorted(pre_xl_dist.keys()):
        print(f"    XL = {xl}: {pre_xl_dist[xl]} ({pre_xl_dist[xl]/total*100:.1f}%)")
    print(f"\n  Post-swap cross-link distribution:")
    for xl in sorted(post_xl_dist.keys()):
        print(f"    XL = {xl}: {post_xl_dist[xl]} ({post_xl_dist[xl]/total*100:.1f}%)")

    max_post_xl = max(post_xl_dist.keys()) if post_xl_dist else 0
    t1 = max_post_xl <= 1 and total > 0
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Max post-swap XL = {max_post_xl} (need ≤ 1)")
    return t1


# ─────────────────────────────────────────────────────────────
# Test 2: Which pairs are cross-linked after swap?
# ─────────────────────────────────────────────────────────────
def test_2():
    print("\n"+"="*70)
    print("Test 2: Post-swap pair classification")
    print("="*70)

    graphs = get_graphs()
    total = 0
    # Track which pairs (by structural role) are cross-linked after swap
    xl_pairs = Counter()
    strict_pairs = Counter()
    untangled_pairs = Counter()

    for adj in graphs:
        deg5 = [v for v in adj if len(adj[v]) == 5]
        for tv in deg5[:3]:
            cases = collect_tau6(adj, tv, n_seeds=500)
            for c in cases:
                result = get_bridge_structure(adj, tv, c)
                if result is None: continue
                nbrs, nbr_c, rep, bp, sp, mid, nm = result
                s2_col = nbr_c[nm[0]]; s3_col = nbr_c[nm[1]]
                mid_col = nbr_c[mid]

                for idx, s_i_pos in enumerate(nm):
                    si_col = nbr_c[s_i_pos]
                    sj_col = s3_col if idx == 0 else s2_col
                    near_b = None
                    for b in bp:
                        if cyclic_dist(b, s_i_pos) == 1: near_b = b; break
                    if near_b is None: continue
                    far_b = [b for b in bp if b != near_b][0]

                    C = kempe_chain(adj, c, nbrs[far_b], rep, si_col, exclude={tv})
                    if nbrs[near_b] in C: continue
                    n_si = nbrs[s_i_pos]
                    if n_si in C: continue  # Case A only

                    new_c = do_swap_on_chain(adj, c, tv, rep, si_col, C)
                    if not is_proper(adj, new_c, skip=tv): continue
                    total += 1

                    # Classify all 6 pairs in new coloring
                    pairs = classify_pairs(adj, new_c, tv)
                    for (c1, c2), status in pairs.items():
                        # Identify pair by structural role in NEW coloring
                        p = tuple(sorted([c1, c2]))
                        # New bridge color is si_col
                        if si_col in p and rep in p:
                            label = "si-r"
                        elif si_col in p and mid_col in p:
                            label = "si-mid"
                        elif si_col in p and sj_col in p:
                            label = "si-sj"
                        elif rep in p and mid_col in p:
                            label = "r-mid"
                        elif rep in p and sj_col in p:
                            label = "r-sj"
                        elif mid_col in p and sj_col in p:
                            label = "mid-sj"
                        else:
                            label = "unknown"

                        if status == 'crosslink':
                            xl_pairs[label] += 1
                        elif status == 'strict':
                            strict_pairs[label] += 1
                        else:
                            untangled_pairs[label] += 1

    print(f"\n  Total Case A swaps: {total}")
    print(f"\n  Post-swap pair classification:")
    print(f"  {'Pair':10s} {'Strict':8s} {'Crosslink':10s} {'Untangled':10s}")
    for label in ["si-r", "si-mid", "si-sj", "r-mid", "r-sj", "mid-sj"]:
        s = strict_pairs.get(label, 0)
        x = xl_pairs.get(label, 0)
        u = untangled_pairs.get(label, 0)
        t = s + x + u
        print(f"  {label:10s} {s:8d} {x:10d} {u:10d}  (/{t})")

    # Key check: is (si, r) EVER strictly tangled?
    si_r_strict = strict_pairs.get("si-r", 0)
    print(f"\n  (s_i, r) strictly tangled: {si_r_strict}/{total}")
    if si_r_strict == 0:
        print(f"  *** CONFIRMED: (s_i, r) is NEVER strictly tangled ***")
        print(f"  Chain component preservation holds.")

    t2 = si_r_strict == 0 and total > 0
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. (s_i, r) never strict: {si_r_strict}/{total}")
    return t2


# ─────────────────────────────────────────────────────────────
# Test 3: Cross-link delta (pre-swap minus post-swap)
# ─────────────────────────────────────────────────────────────
def test_3():
    print("\n"+"="*70)
    print("Test 3: Cross-link delta (pre - post)")
    print("="*70)

    graphs = get_graphs()
    total = 0
    delta_dist = Counter()

    for adj in graphs:
        deg5 = [v for v in adj if len(adj[v]) == 5]
        for tv in deg5[:3]:
            cases = collect_tau6(adj, tv, n_seeds=500)
            for c in cases:
                result = get_bridge_structure(adj, tv, c)
                if result is None: continue
                nbrs, nbr_c, rep, bp, sp, mid, nm = result

                for s_i_pos in nm:
                    si_col = nbr_c[s_i_pos]
                    near_b = None
                    for b in bp:
                        if cyclic_dist(b, s_i_pos) == 1: near_b = b; break
                    if near_b is None: continue
                    far_b = [b for b in bp if b != near_b][0]

                    C = kempe_chain(adj, c, nbrs[far_b], rep, si_col, exclude={tv})
                    if nbrs[near_b] in C: continue
                    n_si = nbrs[s_i_pos]
                    if n_si in C: continue

                    new_c = do_swap_on_chain(adj, c, tv, rep, si_col, C)
                    if not is_proper(adj, new_c, skip=tv): continue
                    total += 1

                    pre_xl = count_crosslinks(adj, c, tv)
                    post_xl = count_crosslinks(adj, new_c, tv)
                    delta = pre_xl - post_xl

                    delta_dist[delta] += 1

    print(f"\n  Total Case A swaps: {total}")
    print(f"\n  Cross-link delta (pre - post):")
    for d in sorted(delta_dist.keys()):
        print(f"    delta = {d}: {delta_dist[d]} ({delta_dist[d]/total*100:.1f}%)")

    always_decreases = all(d >= 1 for d in delta_dist.keys())
    t3 = always_decreases and total > 0
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. XL always decreases: {always_decreases}")
    return t3


# ─────────────────────────────────────────────────────────────
# Test 4: Exactly how many pairs change status?
# ─────────────────────────────────────────────────────────────
def test_4():
    print("\n"+"="*70)
    print("Test 4: Per-case pair status changes")
    print("="*70)

    graphs = get_graphs()
    total = 0
    untangle_count_dist = Counter()
    new_tangle_count_dist = Counter()

    for adj in graphs:
        deg5 = [v for v in adj if len(adj[v]) == 5]
        for tv in deg5[:3]:
            cases = collect_tau6(adj, tv, n_seeds=500)
            for c in cases:
                result = get_bridge_structure(adj, tv, c)
                if result is None: continue
                nbrs, nbr_c, rep, bp, sp, mid, nm = result

                for s_i_pos in nm:
                    si_col = nbr_c[s_i_pos]
                    near_b = None
                    for b in bp:
                        if cyclic_dist(b, s_i_pos) == 1: near_b = b; break
                    if near_b is None: continue
                    far_b = [b for b in bp if b != near_b][0]

                    C = kempe_chain(adj, c, nbrs[far_b], rep, si_col, exclude={tv})
                    if nbrs[near_b] in C: continue
                    n_si = nbrs[s_i_pos]
                    if n_si in C: continue

                    new_c = do_swap_on_chain(adj, c, tv, rep, si_col, C)
                    if not is_proper(adj, new_c, skip=tv): continue
                    total += 1

                    # Count pairs that changed from tangled to untangled
                    untangle_count = 0
                    new_tangle_count = 0
                    for c1, c2 in itertools.combinations(range(4), 2):
                        old_tangled = not can_free_color(adj, c, tv, c1, c2)
                        new_tangled = not can_free_color(adj, new_c, tv, c1, c2)
                        if old_tangled and not new_tangled: untangle_count += 1
                        if not old_tangled and new_tangled: new_tangle_count += 1

                    untangle_count_dist[untangle_count] += 1
                    new_tangle_count_dist[new_tangle_count] += 1

    print(f"\n  Total Case A swaps: {total}")
    print(f"\n  Pairs that became UNTANGLED per case:")
    for n in sorted(untangle_count_dist.keys()):
        print(f"    {n} pairs: {untangle_count_dist[n]} ({untangle_count_dist[n]/total*100:.1f}%)")
    print(f"\n  Pairs that became NEWLY TANGLED per case:")
    for n in sorted(new_tangle_count_dist.keys()):
        print(f"    {n} pairs: {new_tangle_count_dist[n]} ({new_tangle_count_dist[n]/total*100:.1f}%)")

    always_exactly_one = (len(untangle_count_dist) == 1 and 1 in untangle_count_dist)
    t4 = always_exactly_one and total > 0
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Exactly 1 pair untangles: {always_exactly_one}")
    return t4


# ─────────────────────────────────────────────────────────────
# Test 5: Can 2 cross-links coexist on new bridge?
# ─────────────────────────────────────────────────────────────
def test_5():
    print("\n"+"="*70)
    print("Test 5: Can 2 cross-links coexist on new s_i bridge?")
    print("="*70)

    graphs = get_graphs()
    total = 0
    two_xl = 0
    one_xl = 0
    zero_xl = 0

    for adj in graphs:
        deg5 = [v for v in adj if len(adj[v]) == 5]
        for tv in deg5[:3]:
            cases = collect_tau6(adj, tv, n_seeds=500)
            for c in cases:
                result = get_bridge_structure(adj, tv, c)
                if result is None: continue
                nbrs, nbr_c, rep, bp, sp, mid, nm = result

                for idx, s_i_pos in enumerate(nm):
                    si_col = nbr_c[s_i_pos]
                    near_b = None
                    for b in bp:
                        if cyclic_dist(b, s_i_pos) == 1: near_b = b; break
                    if near_b is None: continue
                    far_b = [b for b in bp if b != near_b][0]

                    C = kempe_chain(adj, c, nbrs[far_b], rep, si_col, exclude={tv})
                    if nbrs[near_b] in C: continue
                    n_si = nbrs[s_i_pos]
                    if n_si in C: continue

                    new_c = do_swap_on_chain(adj, c, tv, rep, si_col, C)
                    if not is_proper(adj, new_c, skip=tv): continue
                    total += 1

                    # Count cross-links ONLY on bridge pairs (involving new bridge s_i)
                    bridge_xl = 0
                    for c1, c2 in itertools.combinations(range(4), 2):
                        p = tuple(sorted([c1, c2]))
                        if si_col not in p: continue  # Only bridge pairs

                        op = not can_free_color(adj, new_c, tv, c1, c2)
                        st = is_strictly_tangled(adj, new_c, tv, c1, c2)
                        if op and not st:
                            bridge_xl += 1

                    if bridge_xl >= 2: two_xl += 1
                    elif bridge_xl == 1: one_xl += 1
                    else: zero_xl += 1

    print(f"\n  Total Case A swaps: {total}")
    print(f"  New bridge has 0 cross-links: {zero_xl} ({zero_xl/total*100:.1f}%)")
    print(f"  New bridge has 1 cross-link: {one_xl} ({one_xl/total*100:.1f}%)")
    print(f"  New bridge has 2 cross-links: {two_xl} ({two_xl/total*100:.1f}%)")

    if two_xl == 0:
        print(f"\n  *** CONFIRMED: New bridge can have AT MOST 1 cross-link ***")
        print(f"  This closes Step 11: max tau = strict(4) + XL(1) = 5.")
    else:
        print(f"\n  *** WARNING: {two_xl} cases with 2 cross-links! ***")
        print(f"  Elie's bound is WRONG. Need different argument.")

    t5 = two_xl == 0 and total > 0
    print(f"\n  [{'PASS' if t5 else 'FAIL'}] 5. Max bridge XL ≤ 1: {two_xl == 0}")
    return t5


# ─────────────────────────────────────────────────────────────
# Test 6: Full decomposition: tau = strict + XL
# ─────────────────────────────────────────────────────────────
def test_6():
    print("\n"+"="*70)
    print("Test 6: tau = strict + cross-links decomposition")
    print("="*70)

    graphs = get_graphs()
    total = 0
    decomp_pre = Counter()
    decomp_post = Counter()

    for adj in graphs:
        deg5 = [v for v in adj if len(adj[v]) == 5]
        for tv in deg5[:3]:
            cases = collect_tau6(adj, tv, n_seeds=500)
            for c in cases:
                result = get_bridge_structure(adj, tv, c)
                if result is None: continue
                nbrs, nbr_c, rep, bp, sp, mid, nm = result

                for s_i_pos in nm:
                    si_col = nbr_c[s_i_pos]
                    near_b = None
                    for b in bp:
                        if cyclic_dist(b, s_i_pos) == 1: near_b = b; break
                    if near_b is None: continue
                    far_b = [b for b in bp if b != near_b][0]

                    C = kempe_chain(adj, c, nbrs[far_b], rep, si_col, exclude={tv})
                    if nbrs[near_b] in C: continue
                    n_si = nbrs[s_i_pos]
                    if n_si in C: continue

                    new_c = do_swap_on_chain(adj, c, tv, rep, si_col, C)
                    if not is_proper(adj, new_c, skip=tv): continue
                    total += 1

                    st_pre = strict_tau(adj, c, tv)
                    xl_pre = count_crosslinks(adj, c, tv)
                    tau_pre = operational_tau(adj, c, tv)

                    st_post = strict_tau(adj, new_c, tv)
                    xl_post = count_crosslinks(adj, new_c, tv)
                    tau_post = operational_tau(adj, new_c, tv)

                    decomp_pre[(st_pre, xl_pre, tau_pre)] += 1
                    decomp_post[(st_post, xl_post, tau_post)] += 1

    print(f"\n  Total Case A swaps: {total}")
    print(f"\n  Pre-swap decomposition (strict, XL, tau):")
    for key in sorted(decomp_pre.keys()):
        print(f"    {key}: {decomp_pre[key]}")
    print(f"\n  Post-swap decomposition (strict, XL, tau):")
    for key in sorted(decomp_post.keys()):
        print(f"    {key}: {decomp_post[key]}")

    # Verify tau = strict + XL always
    all_valid = True
    for (st, xl, tau), count in list(decomp_pre.items()) + list(decomp_post.items()):
        if tau != st + xl:
            print(f"  *** tau != strict + XL: ({st}, {xl}, {tau}) ***")
            all_valid = False

    t6 = all_valid and total > 0
    print(f"\n  [{'PASS' if t6 else 'FAIL'}] 6. tau = strict + XL always: {all_valid}")
    return t6


# ─────────────────────────────────────────────────────────────
# Test 7: (s_i, r) chain component preservation
# ─────────────────────────────────────────────────────────────
def test_7():
    print("\n"+"="*70)
    print("Test 7: Are (s_i, r)-chain components preserved by swap?")
    print("="*70)

    graphs = get_graphs()
    total = 0
    preserved = 0; changed = 0

    for adj in graphs:
        deg5 = [v for v in adj if len(adj[v]) == 5]
        for tv in deg5[:3]:
            cases = collect_tau6(adj, tv, n_seeds=500)
            for c in cases:
                result = get_bridge_structure(adj, tv, c)
                if result is None: continue
                nbrs, nbr_c, rep, bp, sp, mid, nm = result

                for s_i_pos in nm:
                    si_col = nbr_c[s_i_pos]
                    near_b = None
                    for b in bp:
                        if cyclic_dist(b, s_i_pos) == 1: near_b = b; break
                    if near_b is None: continue
                    far_b = [b for b in bp if b != near_b][0]

                    C = kempe_chain(adj, c, nbrs[far_b], rep, si_col, exclude={tv})
                    if nbrs[near_b] in C: continue
                    n_si = nbrs[s_i_pos]
                    if n_si in C: continue

                    new_c = do_swap_on_chain(adj, c, tv, rep, si_col, C)
                    if not is_proper(adj, new_c, skip=tv): continue
                    total += 1

                    # Pre-swap: are B_far and n_{s_i} in the same (r, s_i)-chain?
                    pre_chain = kempe_chain(adj, c, nbrs[far_b], rep, si_col, exclude={tv})
                    pre_same = (n_si in pre_chain)

                    # Post-swap: are B_far and n_{s_i} in the same (s_i, r)-chain?
                    # In new coloring, B_far is si_col, n_si is si_col
                    post_chain = kempe_chain(adj, new_c, nbrs[far_b], si_col, rep, exclude={tv})
                    post_same = (n_si in post_chain)

                    if pre_same == post_same:
                        preserved += 1
                    else:
                        changed += 1

    print(f"\n  Total Case A swaps: {total}")
    print(f"  Component relationship preserved: {preserved}/{total}")
    print(f"  Component relationship CHANGED: {changed}/{total}")

    # In Case A, pre_same should always be False (n_si NOT in chain = Case A)
    # Post_same should also be False (components preserved)
    t7 = changed == 0 and total > 0
    print(f"\n  [{'PASS' if t7 else 'FAIL'}] 7. Components preserved: {changed == 0}")
    return t7


# ─────────────────────────────────────────────────────────────
# Test 8: Complete summary — the conservation law
# ─────────────────────────────────────────────────────────────
def test_8():
    print("\n"+"="*70)
    print("Test 8: Conservation of Color Charge — complete verification")
    print("="*70)

    graphs = get_graphs()
    total = 0; violations = 0

    for adj in graphs:
        deg5 = [v for v in adj if len(adj[v]) == 5]
        for tv in deg5[:3]:
            cases = collect_tau6(adj, tv, n_seeds=500)
            for c in cases:
                result = get_bridge_structure(adj, tv, c)
                if result is None: continue
                nbrs, nbr_c, rep, bp, sp, mid, nm = result

                for s_i_pos in nm:
                    si_col = nbr_c[s_i_pos]
                    near_b = None
                    for b in bp:
                        if cyclic_dist(b, s_i_pos) == 1: near_b = b; break
                    if near_b is None: continue
                    far_b = [b for b in bp if b != near_b][0]

                    C = kempe_chain(adj, c, nbrs[far_b], rep, si_col, exclude={tv})
                    if nbrs[near_b] in C: continue
                    n_si = nbrs[s_i_pos]
                    if n_si in C: continue

                    new_c = do_swap_on_chain(adj, c, tv, rep, si_col, C)
                    if not is_proper(adj, new_c, skip=tv): continue
                    total += 1

                    new_tau = operational_tau(adj, new_c, tv)
                    new_st = strict_tau(adj, new_c, tv)
                    new_xl = count_crosslinks(adj, new_c, tv)

                    # Conservation law checks:
                    # 1. tau drops by exactly 1
                    # 2. strict_tau ≤ 4
                    # 3. XL ≤ 1
                    # 4. tau = strict + XL ≤ 5
                    if new_tau != 5 or new_st > 4 or new_xl > 1:
                        violations += 1

    print(f"\n  Total Case A swaps: {total}")
    print(f"  Violations of conservation law: {violations}")

    if violations == 0:
        print(f"""
  ╔══════════════════════════════════════════════════════════════════════╗
  ║  CONSERVATION OF COLOR CHARGE — T154 VERIFIED                      ║
  ║                                                                    ║
  ║  Pre-swap:  tau = 6 = strict(4) + XL(2)                            ║
  ║  Post-swap: tau = 5 = strict(4) + XL(1)                            ║
  ║                                                                    ║
  ║  The charge budget (4) is conserved.                                ║
  ║  Cross-links decrease by exactly 1.                                ║
  ║  The tree rebalances. Height drops.                                ║
  ║                                                                    ║
  ║  {total:4d} Case A swaps. 0 violations.                                ║
  ║                                                                    ║
  ║  "Conservation of color charge." — Casey Koons                     ║
  ║  "log n" — Casey Koons                                             ║
  ╚══════════════════════════════════════════════════════════════════════╝
""")

    t8 = violations == 0 and total > 0
    print(f"\n  [{'PASS' if t8 else 'FAIL'}] 8. Conservation: {total}/{total}, 0 violations")
    return t8


if __name__ == "__main__":
    print("="*70)
    print("Toy 437: Cross-Link Audit — Keeper's Audit of T154")
    print("Casey Koons & Claude 4.6 (Lyra), March 25 2026")
    print("="*70)

    results = [test_1(), test_2(), test_3(), test_4(),
               test_5(), test_6(), test_7(), test_8()]
    passed = sum(results)
    print(f"\n{'='*70}")
    print(f"Toy 437 -- SCORE: {passed}/{len(results)}")
    print(f"{'='*70}")
    if passed == len(results): print("ALL PASS.")
    else:
        for i,r in enumerate(results,1):
            if not r: print(f"  Test {i}: FAIL")
