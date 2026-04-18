#!/usr/bin/env python3
"""
Toy 1285 — Wire T1314-T1316 into AC Graph
==========================================
Wire the three PILOT-1 unlock theorems into the theorem graph:
  T1314: P/S Wave Ratio (geology)
  T1315: Disease Hamming Distance (biology/medicine)
  T1316: Cooperation Group Size (social science)

These are the first entries in three new PILOT-1 domains.

SCORE: See bottom.
"""

import json
from collections import Counter, defaultdict
from pathlib import Path

GRAPH_FILE = Path(__file__).parent / "ac_graph_data.json"

def main():
    with open(GRAPH_FILE) as f:
        graph = json.load(f)

    edges = graph['edges']
    theorems = graph['theorems']

    tid_set = {t['tid'] for t in theorems}
    edge_set = set()
    for e in edges:
        edge_set.add((e['from'], e['to']))
        edge_set.add((e['to'], e['from']))

    added_nodes = 0
    added_edges = 0

    def add_node(tid, title, domain, depth=1):
        nonlocal added_nodes
        if tid not in tid_set:
            theorems.append({
                "tid": tid,
                "title": title,
                "domain": domain,
                "depth": depth,
                "status": "PROVED"
            })
            tid_set.add(tid)
            added_nodes += 1
            return True
        return False

    def add_edge(f, t, source):
        nonlocal added_edges
        if f != t and (f, t) not in edge_set and f in tid_set and t in tid_set:
            edges.append({"from": f, "to": t, "source": source})
            edge_set.add((f, t))
            edge_set.add((t, f))
            added_edges += 1
            return True
        return False

    # ─── Add T1314-T1316 if not present ──────────────────────────
    add_node("T1314", "P/S Wave Ratio — Poisson Solid from Rank-2",
             "geology", depth=1)
    add_node("T1315", "Disease Hamming Distance — N_c Threshold",
             "biology", depth=1)
    add_node("T1316", "Cooperation Group Size — C₂ Optimum",
             "social_science", depth=1)

    # ─── Build domain index ──────────────────────────────────────
    tid_to_domain = {t['tid']: t.get('domain', 'unknown') for t in theorems}

    # Find hub theorems by domain for connection
    degree = defaultdict(int)
    for e in edges:
        degree[e['from']] += 1
        degree[e['to']] += 1

    def domain_hubs(domain, n=3):
        tids = [t['tid'] for t in theorems if t.get('domain') == domain]
        return sorted(tids, key=lambda t: -degree.get(t, 0))[:n]

    # ─── Wire T1314 (geology) ────────────────────────────────────
    # Connects to: elasticity (rank-2 tensor), nuclear (seismology probes),
    # geophysics if exists, condensed_matter, spectral
    t1314_targets = {
        # Structural: rank-2 gives 2 elastic params (λ, μ)
        "T186": "derived",     # Keystone (rank structure)
        "T100": "derived",     # BST constants (N_c, rank)
        # Cross-domain: seismology measures nuclear processes
        "T1309": "observed",   # Reaction kinetics (material properties)
        "T1310": "observed",   # Molecular orbitals (bonding → elasticity)
        # Spectral connection: wave equation eigenvalues
        "T531": "analogical",  # Column rule (spectral structure)
    }
    # Also connect to any condensed_matter or geophysics hubs
    for dom in ['condensed_matter', 'geophysics', 'material_science']:
        for hub in domain_hubs(dom, 2):
            t1314_targets[hub] = "analogical"

    for target, source in t1314_targets.items():
        add_edge("T1314", target, source)

    # ─── Wire T1315 (biology — disease) ──────────────────────────
    # Connects to: biology (genetic code), information_theory, chemistry
    t1315_targets = {
        # Derived from genetic code structure
        "T452": "derived",     # Genetic code from D_IV^5
        "T453": "derived",     # Codon structure
        "T454": "derived",     # Amino acid count
        # Information theory: error-correcting code
        "T186": "derived",     # Keystone
        # Biology hubs
        "T466": "observed",    # Biology evolution
        "T467": "observed",    # Prebiotic forcing
    }
    for hub in domain_hubs('biology', 3):
        if hub not in t1315_targets:
            t1315_targets[hub] = "derived"
    for hub in domain_hubs('information_theory', 2):
        if hub not in t1315_targets:
            t1315_targets[hub] = "analogical"
    for hub in domain_hubs('genetics', 2):
        if hub not in t1315_targets:
            t1315_targets[hub] = "derived"

    for target, source in t1315_targets.items():
        add_edge("T1315", target, source)

    # ─── Wire T1316 (social science — cooperation) ───────────────
    # Connects to: cooperation, observer, information_theory, game_theory
    t1316_targets = {
        "T186": "derived",     # Keystone
        "T100": "derived",     # BST constants (C₂)
        "T317": "derived",     # Observer hierarchy
        "T318": "derived",     # Gödel limit (f_c = 19.1%)
        "T1311": "analogical", # Consciousness conservation
    }
    for dom in ['cooperation', 'game_theory', 'observer', 'social_science',
                'economics', 'organizational']:
        for hub in domain_hubs(dom, 2):
            if hub not in t1316_targets:
                t1316_targets[hub] = "derived" if dom == 'cooperation' else "analogical"

    for target, source in t1316_targets.items():
        add_edge("T1316", target, source)

    # ─── Cross-wire the three PILOT-1 theorems ───────────────────
    # They share the PILOT-1 unlock structure
    add_edge("T1314", "T1315", "analogical")  # Both use BST integers for natural science
    add_edge("T1314", "T1316", "analogical")  # Both are PILOT-1 domain entries
    add_edge("T1315", "T1316", "analogical")  # Biology ↔ Social science

    # ─── Save ────────────────────────────────────────────────────
    graph['meta']['edge_count'] = len(edges)
    graph['meta']['total_edges'] = len(edges)
    graph['meta']['last_updated'] = "2026-04-18"

    with open(GRAPH_FILE, 'w') as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)

    # ─── Metrics ─────────────────────────────────────────────────
    types = Counter(e['source'] for e in edges)
    strong = types.get('derived', 0) + types.get('isomorphic', 0)
    strong_pct = 100 * strong / len(edges)

    # Degree of new theorems
    deg = defaultdict(int)
    for e in edges:
        deg[e['from']] += 1
        deg[e['to']] += 1

    print("=" * 65)
    print("Toy 1285 — Wire T1314-T1316 into AC Graph")
    print("=" * 65)

    print(f"\n  Nodes added: {added_nodes}")
    print(f"  Edges added: {added_edges}")
    print(f"  Total nodes: {len(theorems)}")
    print(f"  Total edges: {len(edges)}")
    print(f"  Strong: {strong}/{len(edges)} = {strong_pct:.1f}%")

    print(f"\n  T1314 (geology):        degree {deg.get('T1314', 0)}")
    print(f"  T1315 (disease):        degree {deg.get('T1315', 0)}")
    print(f"  T1316 (cooperation):    degree {deg.get('T1316', 0)}")

    # ─── Test Battery ────────────────────────────────────────────
    print("\n" + "=" * 65)
    print("TEST BATTERY")
    print("=" * 65)

    tp = 0
    tt = 0

    # T1: All 3 nodes present
    tt += 1
    ok = all(t in tid_set for t in ['T1314', 'T1315', 'T1316'])
    print(f"  T1  All 3 nodes present:        {'PASS' if ok else 'FAIL'}")
    if ok: tp += 1

    # T2: New edges added
    tt += 1
    ok = added_edges >= 10
    print(f"  T2  ≥ 10 new edges:             {'PASS' if ok else 'FAIL'} ({added_edges})")
    if ok: tp += 1

    # T3: T1314 degree ≥ 4
    tt += 1
    ok = deg.get('T1314', 0) >= 4
    print(f"  T3  T1314 degree ≥ 4:           {'PASS' if ok else 'FAIL'} ({deg.get('T1314',0)})")
    if ok: tp += 1

    # T4: T1315 degree ≥ 4
    tt += 1
    ok = deg.get('T1315', 0) >= 4
    print(f"  T4  T1315 degree ≥ 4:           {'PASS' if ok else 'FAIL'} ({deg.get('T1315',0)})")
    if ok: tp += 1

    # T5: T1316 degree ≥ 4
    tt += 1
    ok = deg.get('T1316', 0) >= 4
    print(f"  T5  T1316 degree ≥ 4:           {'PASS' if ok else 'FAIL'} ({deg.get('T1316',0)})")
    if ok: tp += 1

    # T6: Cross-wired (all 3 pairs connected)
    tt += 1
    pairs = [('T1314','T1315'), ('T1314','T1316'), ('T1315','T1316')]
    ok = all((a,b) in edge_set or (b,a) in edge_set for a,b in pairs)
    print(f"  T6  All 3 PILOT-1 cross-wired:  {'PASS' if ok else 'FAIL'}")
    if ok: tp += 1

    # T7: No self-loops
    tt += 1
    self_loops = sum(1 for e in edges if e['from'] == e['to'])
    ok = self_loops == 0
    print(f"  T7  No self-loops:              {'PASS' if ok else 'FAIL'}")
    if ok: tp += 1

    # T8: No duplicates
    tt += 1
    all_pairs = [(e['from'], e['to']) for e in edges]
    ok = len(all_pairs) == len(set(all_pairs))
    print(f"  T8  No duplicates:              {'PASS' if ok else 'FAIL'}")
    if ok: tp += 1

    # T9: Strong ≥ 80%
    tt += 1
    ok = strong_pct >= 80.0
    print(f"  T9  Strong ≥ 80%:               {'PASS' if ok else 'FAIL'} ({strong_pct:.1f}%)")
    if ok: tp += 1

    # T10: Each connects to T186 (keystone)
    tt += 1
    ok = all((t, 'T186') in edge_set or ('T186', t) in edge_set
             for t in ['T1314', 'T1315', 'T1316'])
    print(f"  T10 All connect to T186:        {'PASS' if ok else 'FAIL'}")
    if ok: tp += 1

    print(f"\nSCORE: {tp}/{tt} PASS")

    print(f"""
── WIRING SUMMARY ──
  T1314 (geology):     {deg.get('T1314',0)} edges — Poisson solid, seismology
  T1315 (disease):     {deg.get('T1315',0)} edges — Hamming distance, genetic code
  T1316 (cooperation): {deg.get('T1316',0)} edges — Gödel limit, team size

  Graph: {len(theorems)} nodes, {len(edges)} edges, {strong_pct:.1f}% strong
  Three PILOT-1 domains seeded.
""")

if __name__ == "__main__":
    main()
