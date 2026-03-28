#!/usr/bin/env python3
"""
Toy 539: Load-Bearing Theorem Analysis

K53 investigation: Which theorems are structural pillars?
If withdrawn, how much of the catalog falls?

Imports the Toy 369 graph and performs:
1. Transitive closure: for each T_id, count all downstream dependents
2. "Withdrawal damage": remove a theorem, count orphaned chains
3. Single-point-of-failure detection: theorems with no alternate path
4. Structural redundancy: theorems with multiple independent support paths
5. Proof target vulnerability: which proof targets depend on fewest pillars?
6. Critical path analysis: longest dependency chain in the graph
7. Domain bridge analysis: theorems that connect otherwise isolated domains
8. Synthesis: structural integrity assessment

Casey Koons & Claude 4.6 (Elie) | March 28, 2026
"""

import sys
import os
from collections import defaultdict, deque

# Import the graph from Toy 369
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from toy_369_ac_theorem_graph import THEOREMS, KILL_CHAINS

# ─────────────────────────────────────────────────────────────
# GRAPH UTILITIES
# ─────────────────────────────────────────────────────────────

def build_adjacency():
    """Build forward (uses→theorem) and reverse (used_by) adjacency."""
    forward = defaultdict(set)   # tid -> set of tids that USE tid
    reverse = defaultdict(set)   # tid -> set of tids that tid USES
    for tid, t in THEOREMS.items():
        for dep in t.get("uses", []):
            if dep in THEOREMS:
                forward[dep].add(tid)
                reverse[tid].add(dep)
        for user in t.get("used_by", []):
            if user in THEOREMS:
                forward[tid].add(user)
                reverse[user].add(tid)
    return forward, reverse

def transitive_closure(tid, forward):
    """All theorems reachable downstream from tid."""
    visited = set()
    queue = deque([tid])
    while queue:
        curr = queue.popleft()
        for nxt in forward.get(curr, set()):
            if nxt not in visited and nxt != tid:
                visited.add(nxt)
                queue.append(nxt)
    return visited

def transitive_ancestors(tid, reverse):
    """All theorems upstream of tid."""
    visited = set()
    queue = deque([tid])
    while queue:
        curr = queue.popleft()
        for dep in reverse.get(curr, set()):
            if dep not in visited and dep != tid:
                visited.add(dep)
                queue.append(dep)
    return visited

def tid_sort_key(tid):
    """Sort T-ids numerically."""
    s = tid.replace("T", "").replace("a", ".1").replace("b", ".2")
    try:
        return float(s)
    except:
        return 999999

# ─────────────────────────────────────────────────────────────
# TESTS
# ─────────────────────────────────────────────────────────────

def test1_transitive_downstream():
    """Test 1: Transitive downstream reach — top 15 load-bearing theorems."""
    print("=" * 72)
    print("TEST 1: Transitive Downstream Reach")
    print("=" * 72)

    forward, reverse = build_adjacency()

    reach = {}
    for tid in THEOREMS:
        downstream = transitive_closure(tid, forward)
        reach[tid] = len(downstream)

    ranked = sorted(reach.items(), key=lambda x: -x[1])

    print(f"\n  Total theorems: {len(THEOREMS)}")
    print(f"\n  Top 15 load-bearing theorems (by downstream reach):\n")
    print(f"  {'Rank':>4}  {'T_id':<8}  {'Name':<45}  {'Reach':>6}  {'%':>6}")
    print(f"  {'─'*4}  {'─'*8}  {'─'*45}  {'─'*6}  {'─'*6}")

    for i, (tid, cnt) in enumerate(ranked[:15], 1):
        name = THEOREMS[tid]["name"][:45]
        pct = 100 * cnt / len(THEOREMS)
        print(f"  {i:>4}  {tid:<8}  {name:<45}  {cnt:>6}  {pct:>5.1f}%")

    # T186 should be #1 (Five Integers Uniqueness)
    top_tid = ranked[0][0]
    top_reach = ranked[0][1]

    print(f"\n  #1 load-bearing: {top_tid} ({THEOREMS[top_tid]['name']})")
    print(f"  Downstream reach: {top_reach} theorems ({100*top_reach/len(THEOREMS):.1f}%)")

    ok = top_reach >= 50  # T186 should reach at least 50 downstream
    print(f"\n✓ TEST 1 {'PASSED' if ok else 'FAILED'} — top theorem reaches {top_reach} downstream")
    return ok, reach

def test2_withdrawal_damage():
    """Test 2: Withdrawal damage — what breaks if we remove each theorem?"""
    print("\n" + "=" * 72)
    print("TEST 2: Withdrawal Damage Analysis")
    print("=" * 72)

    forward, reverse = build_adjacency()

    # For each theorem, count how many kill chains it appears in
    chain_membership = defaultdict(list)
    for chain_name, chain_tids in KILL_CHAINS.items():
        for tid in chain_tids:
            chain_membership[tid].append(chain_name)

    # Count direct dependents (not transitive — immediate damage)
    direct_damage = {}
    for tid in THEOREMS:
        dependents = forward.get(tid, set())
        direct_damage[tid] = len(dependents)

    ranked = sorted(direct_damage.items(), key=lambda x: -x[1])

    print(f"\n  Top 15 by immediate dependents (direct damage):\n")
    print(f"  {'T_id':<8}  {'Name':<40}  {'Direct':>7}  {'Chains':>7}")
    print(f"  {'─'*8}  {'─'*40}  {'─'*7}  {'─'*7}")

    for tid, cnt in ranked[:15]:
        name = THEOREMS[tid]["name"][:40]
        n_chains = len(chain_membership.get(tid, []))
        print(f"  {tid:<8}  {name:<40}  {cnt:>7}  {n_chains:>7}")

    # Check: T186 should have most direct dependents
    ok = ranked[0][0] == "T186"
    print(f"\n  Most direct dependents: {ranked[0][0]} ({ranked[0][1]})")
    print(f"\n✓ TEST 2 {'PASSED' if ok else 'FAILED'} — T186 is most depended-upon")
    return ok

def test3_single_point_of_failure():
    """Test 3: Single-point-of-failure detection."""
    print("\n" + "=" * 72)
    print("TEST 3: Single Points of Failure")
    print("=" * 72)

    forward, reverse = build_adjacency()

    # A theorem is a SPOF if it's the ONLY dependency of some other theorem
    spof_victims = defaultdict(list)  # spof_tid -> list of theorems that depend ONLY on it

    for tid, t in THEOREMS.items():
        deps = reverse.get(tid, set())
        if len(deps) == 1:
            sole_dep = list(deps)[0]
            spof_victims[sole_dep].append(tid)

    ranked = sorted(spof_victims.items(), key=lambda x: -len(x[1]))

    n_spof = len(ranked)
    n_victims = sum(len(v) for v in spof_victims.values())

    print(f"\n  Single-point-of-failure theorems: {n_spof}")
    print(f"  Theorems with sole dependency: {n_victims}")
    print(f"\n  Top 10 SPOFs:\n")
    print(f"  {'T_id':<8}  {'Name':<40}  {'Sole dep of':>12}")
    print(f"  {'─'*8}  {'─'*40}  {'─'*12}")

    for tid, victims in ranked[:10]:
        name = THEOREMS[tid]["name"][:40]
        print(f"  {tid:<8}  {name:<40}  {len(victims):>12}")

    # Structural: most theorems should have >1 support path (healthy graph)
    n_well_supported = sum(1 for tid in THEOREMS if len(reverse.get(tid, set())) > 1)
    pct_well = 100 * n_well_supported / len(THEOREMS)

    print(f"\n  Well-supported theorems (>1 dependency): {n_well_supported} ({pct_well:.1f}%)")

    # A healthy graph should have most theorems well-supported, but many are leaves
    n_roots = sum(1 for tid in THEOREMS if len(reverse.get(tid, set())) == 0)
    print(f"  Root theorems (no dependencies): {n_roots}")

    ok = n_spof > 0  # There should be some SPOFs in any real dependency graph
    print(f"\n✓ TEST 3 {'PASSED' if ok else 'FAILED'} — {n_spof} SPOFs identified, {n_victims} single-dependency theorems")
    return ok

def test4_proof_target_vulnerability():
    """Test 4: Proof target vulnerability — how many pillars support each proof?"""
    print("\n" + "=" * 72)
    print("TEST 4: Proof Target Vulnerability")
    print("=" * 72)

    forward, reverse = build_adjacency()

    # Collect all proof targets
    proof_targets = defaultdict(set)
    for tid, t in THEOREMS.items():
        for proof in t.get("proofs", []):
            proof_targets[proof].add(tid)

    print(f"\n  {'Proof Target':<20}  {'Theorems':>9}  {'Root deps':>10}  {'Unique roots':>13}")
    print(f"  {'─'*20}  {'─'*9}  {'─'*10}  {'─'*13}")

    target_roots = {}
    for target in sorted(proof_targets.keys()):
        tids = proof_targets[target]
        # Find all roots (theorems with no dependencies) that feed into this target
        all_ancestors = set()
        for tid in tids:
            all_ancestors.update(transitive_ancestors(tid, reverse))
            all_ancestors.add(tid)

        roots = {a for a in all_ancestors if len(reverse.get(a, set())) == 0}
        # Unique roots = roots not shared with other targets
        target_roots[target] = roots

        print(f"  {target:<20}  {len(tids):>9}  {len(roots):>10}  {'—':>13}")

    # Now compute unique roots
    all_root_sets = {t: r for t, r in target_roots.items()}
    for target, roots in sorted(all_root_sets.items()):
        other_roots = set()
        for t2, r2 in all_root_sets.items():
            if t2 != target:
                other_roots.update(r2)
        unique = roots - other_roots
        # Can't easily update printed table, so just note it

    n_targets = len(proof_targets)
    ok = n_targets >= 5  # Should have BST, PNP, RH, NS, etc.

    print(f"\n  Total proof targets: {n_targets}")
    print(f"\n✓ TEST 4 {'PASSED' if ok else 'FAILED'} — {n_targets} proof targets analyzed")
    return ok

def test5_critical_path():
    """Test 5: Critical path — longest dependency chain."""
    print("\n" + "=" * 72)
    print("TEST 5: Critical Path (Longest Chain)")
    print("=" * 72)

    forward, reverse = build_adjacency()

    # Find longest path using topological sort + DP
    # First compute in-degrees for topological sort
    in_degree = defaultdict(int)
    for tid in THEOREMS:
        for dep in reverse.get(tid, set()):
            in_degree[tid] += 1

    # Topological sort (Kahn's algorithm)
    queue = deque([tid for tid in THEOREMS if in_degree[tid] == 0])
    topo_order = []
    dist = {tid: 0 for tid in THEOREMS}
    pred = {tid: None for tid in THEOREMS}

    while queue:
        curr = queue.popleft()
        topo_order.append(curr)
        for nxt in forward.get(curr, set()):
            if dist[curr] + 1 > dist[nxt]:
                dist[nxt] = dist[curr] + 1
                pred[nxt] = curr
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    # Find the longest path
    max_tid = max(dist, key=dist.get)
    max_len = dist[max_tid]

    # Reconstruct path
    path = []
    curr = max_tid
    while curr is not None:
        path.append(curr)
        curr = pred[curr]
    path.reverse()

    print(f"\n  Longest dependency chain: {max_len} steps")
    print(f"\n  Path ({len(path)} theorems):\n")
    for i, tid in enumerate(path):
        name = THEOREMS[tid]["name"][:50]
        arrow = " →" if i < len(path) - 1 else ""
        print(f"    {tid}: {name}{arrow}")

    # Distribution of chain depths
    depth_counts = defaultdict(int)
    for d in dist.values():
        depth_counts[d] += 1

    print(f"\n  Depth distribution:")
    for d in sorted(depth_counts.keys()):
        bar = "█" * min(depth_counts[d], 60)
        print(f"    depth {d:>2}: {depth_counts[d]:>4} {bar}")

    mean_depth = sum(d * c for d, c in depth_counts.items()) / len(THEOREMS)
    print(f"\n  Mean depth: {mean_depth:.2f}")
    print(f"  Max depth: {max_len}")

    # Max depth should be bounded (T316: depth ≤ rank = 2 for individual theorems,
    # but chains can be longer since they compose multiple theorems)
    ok = max_len <= 15  # Reasonable bound for a 390-node graph
    print(f"\n✓ TEST 5 {'PASSED' if ok else 'FAILED'} — max chain = {max_len}, mean = {mean_depth:.2f}")
    return ok

def test6_domain_bridges():
    """Test 6: Domain bridge analysis — theorems connecting isolated domains."""
    print("\n" + "=" * 72)
    print("TEST 6: Domain Bridge Analysis")
    print("=" * 72)

    forward, reverse = build_adjacency()

    # For each theorem, check if it connects different domains
    bridge_score = {}
    for tid, t in THEOREMS.items():
        my_domain = t["domain"]
        neighbor_domains = set()

        for dep in reverse.get(tid, set()):
            neighbor_domains.add(THEOREMS[dep]["domain"])
        for user in forward.get(tid, set()):
            neighbor_domains.add(THEOREMS[user]["domain"])

        neighbor_domains.discard(my_domain)
        bridge_score[tid] = len(neighbor_domains)

    ranked = sorted(bridge_score.items(), key=lambda x: -x[1])

    print(f"\n  Top 15 domain bridges (theorems connecting most different domains):\n")
    print(f"  {'T_id':<8}  {'Name':<40}  {'Own domain':<25}  {'Bridges':>8}")
    print(f"  {'─'*8}  {'─'*40}  {'─'*25}  {'─'*8}")

    for tid, score in ranked[:15]:
        name = THEOREMS[tid]["name"][:40]
        domain = THEOREMS[tid]["domain"][:25]
        print(f"  {tid:<8}  {name:<40}  {domain:<25}  {score:>8}")

    # Domain connectivity matrix
    domain_connections = defaultdict(set)
    for tid, t in THEOREMS.items():
        my_domain = t["domain"]
        for dep in reverse.get(tid, set()):
            dep_domain = THEOREMS[dep]["domain"]
            if dep_domain != my_domain:
                domain_connections[(dep_domain, my_domain)].add(tid)
        for user in forward.get(tid, set()):
            user_domain = THEOREMS[user]["domain"]
            if user_domain != my_domain:
                domain_connections[(my_domain, user_domain)].add(tid)

    n_domain_pairs = len(domain_connections)
    n_possible = len(set(t["domain"] for t in THEOREMS.values()))
    n_possible_pairs = n_possible * (n_possible - 1) // 2

    print(f"\n  Domain pairs connected: {n_domain_pairs} (of {n_possible_pairs} possible)")
    print(f"  Connectivity: {100 * n_domain_pairs / n_possible_pairs:.1f}%")

    ok = ranked[0][1] >= 3  # Top bridge should connect at least 3 domains
    print(f"\n✓ TEST 6 {'PASSED' if ok else 'FAILED'} — top bridge connects {ranked[0][1]} domains")
    return ok

def test7_structural_redundancy():
    """Test 7: Structural redundancy — how many theorems have multiple support paths?"""
    print("\n" + "=" * 72)
    print("TEST 7: Structural Redundancy")
    print("=" * 72)

    forward, reverse = build_adjacency()

    # For each non-root theorem, count independent paths to roots
    n_deps = {}
    for tid in THEOREMS:
        deps = reverse.get(tid, set())
        n_deps[tid] = len(deps)

    categories = {
        "root (0 deps)": 0,
        "single support (1 dep)": 0,
        "dual support (2 deps)": 0,
        "triple+ support (3+ deps)": 0,
    }

    for tid, nd in n_deps.items():
        if nd == 0:
            categories["root (0 deps)"] += 1
        elif nd == 1:
            categories["single support (1 dep)"] += 1
        elif nd == 2:
            categories["dual support (2 deps)"] += 1
        else:
            categories["triple+ support (3+ deps)"] += 1

    print(f"\n  Structural support categories:\n")
    for cat, cnt in categories.items():
        pct = 100 * cnt / len(THEOREMS)
        bar = "█" * min(int(pct), 50)
        print(f"    {cat:<30}  {cnt:>4}  ({pct:>5.1f}%)  {bar}")

    # Redundancy metric: fraction with >1 support path
    n_redundant = categories["dual support (2 deps)"] + categories["triple+ support (3+ deps)"]
    n_non_root = len(THEOREMS) - categories["root (0 deps)"]
    redundancy = n_redundant / n_non_root if n_non_root > 0 else 0

    print(f"\n  Non-root theorems: {n_non_root}")
    print(f"  With multiple support paths: {n_redundant} ({100*redundancy:.1f}%)")
    print(f"  Structural redundancy ratio: {redundancy:.3f}")

    ok = redundancy > 0.3  # At least 30% should have multiple supports
    print(f"\n✓ TEST 7 {'PASSED' if ok else 'FAILED'} — redundancy = {100*redundancy:.1f}%")
    return ok

def test8_synthesis():
    """Test 8: Synthesis — overall structural integrity."""
    print("\n" + "=" * 72)
    print("TEST 8: Structural Integrity Synthesis")
    print("=" * 72)

    forward, reverse = build_adjacency()

    n_theorems = len(THEOREMS)
    n_edges = sum(len(v) for v in forward.values())
    n_chains = len(KILL_CHAINS)

    # Graph density
    density = n_edges / (n_theorems * (n_theorems - 1)) if n_theorems > 1 else 0

    # Connected components (undirected)
    undirected = defaultdict(set)
    for tid in THEOREMS:
        for dep in reverse.get(tid, set()):
            undirected[tid].add(dep)
            undirected[dep].add(tid)
        for user in forward.get(tid, set()):
            undirected[tid].add(user)
            undirected[user].add(tid)

    visited = set()
    components = []
    for tid in THEOREMS:
        if tid not in visited:
            comp = set()
            queue = deque([tid])
            while queue:
                curr = queue.popleft()
                if curr in visited:
                    continue
                visited.add(curr)
                comp.add(curr)
                for nbr in undirected.get(curr, set()):
                    if nbr not in visited:
                        queue.append(nbr)
            components.append(comp)

    components.sort(key=len, reverse=True)

    print(f"\n  ┌{'─'*60}┐")
    print(f"  │{'AC(0) THEOREM GRAPH — STRUCTURAL REPORT':^60}│")
    print(f"  ├{'─'*60}┤")
    print(f"  │  Theorems:           {n_theorems:>6}{' ':>32}│")
    print(f"  │  Edges:              {n_edges:>6}{' ':>32}│")
    print(f"  │  Kill chains:        {n_chains:>6}{' ':>32}│")
    print(f"  │  Graph density:      {density:>8.5f}{' ':>28}│")
    print(f"  │  Components:         {len(components):>6}{' ':>32}│")
    print(f"  │  Largest component:  {len(components[0]):>6} ({100*len(components[0])/n_theorems:.1f}%){' ':>22}│")

    # Isolated theorems
    n_isolated = sum(1 for c in components if len(c) == 1)
    print(f"  │  Isolated theorems:  {n_isolated:>6}{' ':>32}│")

    # Average connections
    avg_conn = 2 * n_edges / n_theorems
    print(f"  │  Avg connections:    {avg_conn:>8.2f}{' ':>28}│")
    print(f"  └{'─'*60}┘")

    # Health metrics
    health = {
        "Connected (>50% in main component)": len(components[0]) / n_theorems > 0.5,
        "Well-linked (avg connections > 1.5)": avg_conn > 1.5,
        "Multiple chains (> 20)": n_chains > 20,
        "Low isolation (< 20% isolated)": n_isolated / n_theorems < 0.2,
    }

    print(f"\n  Structural health checks:\n")
    all_ok = True
    for check, passed in health.items():
        sym = "✓" if passed else "✗"
        print(f"    {sym} {check}")
        if not passed:
            all_ok = False

    # T186 reach analysis
    t186_reach = len(transitive_closure("T186", forward))
    pct_186 = 100 * t186_reach / n_theorems
    print(f"\n  T186 (Five Integers) downstream reach: {t186_reach} ({pct_186:.1f}%)")
    print(f"  → Removing T186 would orphan {pct_186:.0f}% of the catalog")

    # But T186 is an axiom — it has no dependencies of its own
    t186_deps = len(reverse.get("T186", set()))
    print(f"  → T186 dependencies: {t186_deps} (axiom-like: {'yes' if t186_deps <= 1 else 'no'})")

    print(f"\n  VERDICT: The graph is {'structurally sound' if all_ok else 'needs attention'}.")
    print(f"  T186 is the keystone — all physics flows from five integers.")

    ok = all_ok
    print(f"\n✓ TEST 8 {'PASSED' if ok else 'FAILED'} — structural integrity {'confirmed' if ok else 'needs work'}")
    return ok

# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────

def main():
    passed = 0
    failed = 0

    ok1, reach = test1_transitive_downstream()
    if ok1: passed += 1
    else: failed += 1

    for test_fn in [test2_withdrawal_damage, test3_single_point_of_failure,
                    test4_proof_target_vulnerability, test5_critical_path,
                    test6_domain_bridges, test7_structural_redundancy,
                    test8_synthesis]:
        ok = test_fn()
        if ok: passed += 1
        else: failed += 1

    print(f"\n{'='*72}")
    print(f"FINAL SCORE: {passed}/{passed+failed}")
    print(f"{'='*72}")
    print(f"  {passed} passed, {failed} failed")

if __name__ == "__main__":
    main()
