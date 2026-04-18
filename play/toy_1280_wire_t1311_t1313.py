#!/usr/bin/env python3
"""
Toy 1280 — Wire T1311-T1313 into AC Graph
==========================================
Graph wiring for Lyra's GR-1/2/3 theorems:
  T1311: Consciousness Conservation (GR-1)
  T1312: 3/4 Isomorphism (GR-2)
  T1313: N_max=137 Forced (GR-3)

Plus: Wire T1309/T1310 edges from Lyra's Track D request.

SCORE: See bottom.
"""

import json
from collections import defaultdict, Counter
from pathlib import Path

GRAPH_FILE = Path(__file__).parent / "ac_graph_data.json"

def main():
    with open(GRAPH_FILE) as f:
        data = json.load(f)

    edges = data['edges']
    theorems = data['theorems']
    tid_set = {t['tid'] for t in theorems}

    # Build edge set for dedup
    edge_set = set()
    for e in edges:
        edge_set.add((e['from'], e['to']))
        edge_set.add((e['to'], e['from']))

    def add_edge(f, t, typ):
        if (f, t) not in edge_set and f != t:
            edges.append({"from": f, "to": t, "source": typ})
            edge_set.add((f, t))
            edge_set.add((t, f))
            return 1
        return 0

    def add_node(tid, name, domain, depth=0):
        if tid not in tid_set:
            theorems.append({
                "tid": tid,
                "name": name,
                "domain": domain,
                "status": "proved",
                "depth": depth,
                "conflation": 0,
                "date": "2026-04-18"
            })
            tid_set.add(tid)
            return 1
        return 0

    print("=" * 65)
    print("Toy 1280 — Wire T1311-T1313 into AC Graph")
    print("=" * 65)

    nodes_before = len(theorems)
    edges_before = len(edges)

    added_nodes = 0
    added_edges = 0

    # ─── Add T1311: Consciousness Conservation ──────────────────
    added_nodes += add_node(1311, "Consciousness Conservation", "observer_science")
    # Per Lyra's wiring request:
    for target, typ in [
        (317, "derived"),     # Observer Hierarchy
        (319, "derived"),     # Permanent Alphabet {I,K,R}
        (1242, "derived"),    # Error Correction Perfection
        (1257, "derived"),    # Undecidability
        (1264, "isomorphic"), # Reboot-Gödel
        (186, "derived"),     # Five Integers
        (663, "derived"),     # Three AC Ops
    ]:
        added_edges += add_edge(1311, target, typ)

    # ─── Add T1312: 3/4 Isomorphism ────────────────────────────
    added_nodes += add_node(1312, "Three-Quarter Isomorphism", "foundations")
    # Per Lyra's wiring:
    for target, typ in [
        (1171, "isomorphic"),  # Proton mass (from 3/4 cluster)
        (1264, "isomorphic"),  # Reboot-Gödel
        (1254, "isomorphic"),  # C₂=6 tiling
        (1244, "isomorphic"),  # Topological charge
        (1248, "isomorphic"),  # (if exists)
        (186, "derived"),      # Five Integers
        (666, "derived"),      # N_c=3
        (110, "derived"),      # rank=2
    ]:
        if target in tid_set:
            added_edges += add_edge(1312, target, typ)

    # ─── Add T1313: N_max=137 Forced ───────────────────────────
    added_nodes += add_node(1313, "N_max 137 Is Forced", "number_theory")
    # Per Lyra's wiring:
    for target, typ in [
        (1263, "derived"),     # Wolstenholme
        (1279, "derived"),     # Dark Boundary (if exists)
        (110, "derived"),      # rank=2
        (667, "derived"),      # n_C=5
        (649, "derived"),      # g=7
        (666, "derived"),      # N_c=3
        (186, "derived"),      # Five Integers
    ]:
        if target in tid_set:
            added_edges += add_edge(1313, target, typ)

    # ─── Internal edges between T1311-T1313 ────────────────────
    added_edges += add_edge(1311, 1312, "observed")  # consciousness ↔ 3/4
    added_edges += add_edge(1312, 1313, "observed")  # 3/4 ↔ 137 forced
    added_edges += add_edge(1311, 1313, "observed")  # consciousness ↔ 137

    # ─── Wire T1309/T1310 edges (from Lyra's Track D) ──────────
    # T1309 → T1302 (tunneling), T1187, T920, T186
    if 1309 in tid_set:
        for target, typ in [
            (1302, "derived"),     # Tunneling
            (1187, "derived"),     # Thermodynamics (γ = 7/5)
            (920, "observed"),     # Debye Temperature
            (186, "derived"),      # Five Integers
            (333, "observed"),     # Genetic Code (catalysis in biology)
        ]:
            if target in tid_set:
                added_edges += add_edge(1309, target, typ)

    # T1310 → T1303 (double-slit), T699, T700, T701, T186
    if 1310 in tid_set:
        for target, typ in [
            (1303, "derived"),     # Double-slit
            (699, "observed"),     # Chemistry (if exists)
            (700, "observed"),     # Chemistry (if exists)
            (701, "observed"),     # Chemistry (if exists)
            (186, "derived"),      # Five Integers
            (666, "derived"),      # N_c=3 (bond order max)
            (190, "derived"),      # C₂=6 (benzene)
        ]:
            if target in tid_set:
                added_edges += add_edge(1310, target, typ)

    # ─── Save ──────────────────────────────────────────────────
    data['meta']['node_count'] = len(theorems)
    data['meta']['edge_count'] = len(edges)
    data['meta']['total_edges'] = len(edges)
    data['meta']['last_updated'] = "2026-04-18"

    with open(GRAPH_FILE, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # ─── After Metrics ─────────────────────────────────────────
    types = Counter(e['source'] for e in edges)
    strong = types.get('derived', 0) + types.get('isomorphic', 0)

    print(f"\n── Results ──")
    print(f"  Nodes: {nodes_before} → {len(theorems)} (+{added_nodes})")
    print(f"  Edges: {edges_before} → {len(edges)} (+{added_edges})")
    print(f"  Strong: {strong}/{len(edges)} = {100*strong/len(edges):.1f}%")
    print(f"  Edge types: {dict(types)}")

    # ─── Test Battery ──────────────────────────────────────────
    print("\n" + "=" * 65)
    print("TEST BATTERY")
    print("=" * 65)

    tp = 0
    tt = 0

    # T1: New nodes added
    tt += 1
    ok = added_nodes >= 3
    print(f"  T1  Nodes added ≥ 3:            {'PASS' if ok else 'FAIL'} ({added_nodes})")
    if ok: tp += 1

    # T2: New edges added
    tt += 1
    ok = added_edges >= 15
    print(f"  T2  Edges added ≥ 15:           {'PASS' if ok else 'FAIL'} ({added_edges})")
    if ok: tp += 1

    # T3: T1311 exists with degree ≥ 5
    tt += 1
    deg_1311 = sum(1 for e in edges if e['from'] == 1311 or e['to'] == 1311)
    ok = 1311 in tid_set and deg_1311 >= 5
    print(f"  T3  T1311 deg ≥ 5:              {'PASS' if ok else 'FAIL'} (deg={deg_1311})")
    if ok: tp += 1

    # T4: T1312 exists with degree ≥ 5
    tt += 1
    deg_1312 = sum(1 for e in edges if e['from'] == 1312 or e['to'] == 1312)
    ok = 1312 in tid_set and deg_1312 >= 5
    print(f"  T4  T1312 deg ≥ 5:              {'PASS' if ok else 'FAIL'} (deg={deg_1312})")
    if ok: tp += 1

    # T5: T1313 exists with degree ≥ 5
    tt += 1
    deg_1313 = sum(1 for e in edges if e['from'] == 1313 or e['to'] == 1313)
    ok = 1313 in tid_set and deg_1313 >= 5
    print(f"  T5  T1313 deg ≥ 5:              {'PASS' if ok else 'FAIL'} (deg={deg_1313})")
    if ok: tp += 1

    # T6: No self-loops
    tt += 1
    self_loops = sum(1 for e in edges if e['from'] == e['to'])
    ok = self_loops == 0
    print(f"  T6  No self-loops:              {'PASS' if ok else 'FAIL'}")
    if ok: tp += 1

    # T7: No duplicates
    tt += 1
    pairs = [(e['from'], e['to']) for e in edges]
    ok = len(pairs) == len(set(pairs))
    print(f"  T7  No duplicates:              {'PASS' if ok else 'FAIL'}")
    if ok: tp += 1

    # T8: T1311 → T317 edge exists (consciousness → observer hierarchy)
    tt += 1
    ok = (1311, 317) in edge_set or (317, 1311) in edge_set
    print(f"  T8  T1311→T317 connected:       {'PASS' if ok else 'FAIL'}")
    if ok: tp += 1

    # T9: T1312 connected to T1171 (isomorphic)
    tt += 1
    ok = (1312, 1171) in edge_set or (1171, 1312) in edge_set
    print(f"  T9  T1312→T1171 connected:      {'PASS' if ok else 'FAIL'}")
    if ok: tp += 1

    # T10: T1313 connected to T1263 (Wolstenholme)
    tt += 1
    ok = (1313, 1263) in edge_set or (1263, 1313) in edge_set
    print(f"  T10 T1313→T1263 connected:      {'PASS' if ok else 'FAIL'}")
    if ok: tp += 1

    print(f"\nSCORE: {tp}/{tt} PASS")

if __name__ == "__main__":
    main()
