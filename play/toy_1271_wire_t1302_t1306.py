#!/usr/bin/env python3
"""
Toy 1271 — Wire T1302-T1306 into AC Graph
==========================================
Lyra's QM hospitality theorems + science engineering theorem.
Serves Track C (QM hospitality) + Track E (thin domain seeding).

T1302: Quantum Tunneling (quantum_mechanics) — Bergman analytic continuation
T1303: Double-Slit (quantum_mechanics) — reproducing property cross-term
T1304: Photoelectric Effect (quantum_mechanics) — Bergman spectral gap
T1305: Harmonic Oscillator (quantum_mechanics) — zero-point = 1/rank
T1306: Science Engineering Potential (cooperation) — D,W,B coordinates

SCORE: See bottom.
"""

import json
from collections import defaultdict
from pathlib import Path

GRAPH_FILE = Path(__file__).parent / "ac_graph_data.json"

def main():
    with open(GRAPH_FILE) as f:
        data = json.load(f)

    edges = data['edges']
    theorems = data['theorems']

    # Check if already added
    existing_tids = set(t['tid'] for t in theorems)
    new_tids = [1302, 1303, 1304, 1305, 1306]
    already_present = [t for t in new_tids if t in existing_tids]
    if already_present:
        print(f"WARNING: {already_present} already in graph. Skipping those nodes.")

    # ─── Add Theorem Nodes ───────────────────────────────────────
    new_theorems = [
        {
            "tid": 1302,
            "name": "Quantum Tunneling as Analytic Continuation",
            "domain": "quantum_mechanics",
            "status": "proved",
            "depth": 0,
            "conflation": 0,
            "section": "BST_T1302",
            "toys": [1270],
            "date": "2026-04-18",
            "plain": "Barrier penetration is analytic continuation of Bergman kernel past classical turning points.",
            "proofs": []
        },
        {
            "tid": 1303,
            "name": "Double-Slit from Reproducing Property",
            "domain": "quantum_mechanics",
            "status": "proved",
            "depth": 0,
            "conflation": 0,
            "section": "BST_T1303",
            "toys": [1270],
            "date": "2026-04-18",
            "plain": "Interference is the sesquilinear cross-term of the Bergman reproducing kernel at two paths.",
            "proofs": []
        },
        {
            "tid": 1304,
            "name": "Photoelectric Effect from Spectral Gap",
            "domain": "quantum_mechanics",
            "status": "proved",
            "depth": 0,
            "conflation": 0,
            "section": "BST_T1304",
            "toys": [1270],
            "date": "2026-04-18",
            "plain": "Photoelectric threshold is a Bergman spectral gap condition; no wave-particle duality needed.",
            "proofs": []
        },
        {
            "tid": 1305,
            "name": "Harmonic Oscillator Zero-Point from Rank",
            "domain": "quantum_mechanics",
            "status": "proved",
            "depth": 0,
            "conflation": 0,
            "section": "BST_T1305",
            "toys": [1270],
            "date": "2026-04-18",
            "plain": "Zero-point energy 1/2 = 1/rank; creation operators are Bergman eigenvalue steps.",
            "proofs": []
        },
        {
            "tid": 1306,
            "name": "Science Engineering Potential",
            "domain": "cooperation",
            "status": "proved",
            "depth": 1,
            "conflation": 0,
            "section": "BST_T1306",
            "toys": [1267, 1268],
            "date": "2026-04-18",
            "plain": "Every discipline has SEP = B/[(D+1)(W+1)]; measures CI-tractability.",
            "proofs": []
        },
    ]

    for t in new_theorems:
        if t['tid'] not in existing_tids:
            theorems.append(t)

    # ─── Build Edge Set for Dedup ────────────────────────────────
    edge_set = set()
    for e in edges:
        edge_set.add((e['from'], e['to']))

    def add(f, t, typ):
        if (f, t) not in edge_set and f != t:
            edges.append({"from": f, "to": t, "source": typ})
            edge_set.add((f, t))
            return 1
        return 0

    added = 0

    # ─── T1302 Tunneling Edges ───────────────────────────────────
    # Parents: T186 (Five Integers), T110 (rank=2), T1144 (Bergman Master Kernel)
    # Siblings: T1010 (Uncertainty-Information), T751 (alpha decay)
    # Children: connects to nuclear, cosmology
    added += add(186, 1302, "derived")   # Five Integers → Tunneling
    added += add(110, 1302, "derived")   # rank=2 → Tunneling (α = 1/N_max)
    added += add(1144, 1302, "derived")  # Bergman Kernel → Tunneling
    added += add(663, 1302, "derived")   # Three AC Ops → Tunneling
    added += add(1302, 1010, "isomorphic")  # Tunneling ↔ Uncertainty
    added += add(1302, 751, "derived")   # Tunneling → alpha decay theory

    # ─── T1303 Double-Slit Edges ─────────────────────────────────
    # Parents: T186, T1239 (Born rule = reproducing property), T754 (QM from Bergman)
    added += add(186, 1303, "derived")
    added += add(1239, 1303, "derived")  # Born rule → Double-Slit
    added += add(754, 1303, "derived")   # QM from Bergman → Double-Slit
    added += add(663, 1303, "derived")
    added += add(1303, 1010, "isomorphic")  # Double-Slit ↔ Uncertainty
    added += add(1303, 1240, "derived")  # Double-Slit → Decoherence (measurement)

    # ─── T1304 Photoelectric Edges ───────────────────────────────
    # Parents: T186, T664 (Plancherel), T1268 (Photon theorem if exists)
    added += add(186, 1304, "derived")
    added += add(664, 1304, "derived")   # Plancherel → Photoelectric
    added += add(663, 1304, "derived")
    added += add(1304, 1010, "isomorphic")
    added += add(1304, 1302, "isomorphic")  # Photoelectric ↔ Tunneling (both spectral)

    # ─── T1305 Harmonic Oscillator Edges ─────────────────────────
    # Parents: T186, T110 (rank=2 gives 1/2), T664 (Plancherel)
    added += add(186, 1305, "derived")
    added += add(110, 1305, "derived")   # rank=2 → HO (zero-point = 1/rank)
    added += add(664, 1305, "derived")   # Plancherel → HO (spectrum)
    added += add(663, 1305, "derived")
    added += add(1305, 1010, "isomorphic")
    added += add(1305, 1304, "isomorphic")  # HO ↔ Photoelectric (both eigenvalue)

    # ─── QM internal cluster ────────────────────────────────────
    added += add(1302, 1303, "isomorphic")  # Tunneling ↔ Double-Slit
    added += add(1302, 1305, "isomorphic")  # Tunneling ↔ HO

    # ─── T1306 Science Engineering Potential Edges ───────────────
    # Parents: T186, T663 (Three AC Ops), T96 (Depth Reduction)
    # Siblings: T1236 (Consonance IS Cooperation)
    added += add(186, 1306, "derived")
    added += add(663, 1306, "derived")
    added += add(96, 1306, "derived")    # Depth Reduction → SEP
    added += add(1306, 1236, "derived")  # SEP → Consonance IS Cooperation

    # ─── Update meta ─────────────────────────────────────────────
    data['meta']['node_count'] = len(theorems)
    data['meta']['edge_count'] = len(edges)
    data['meta']['total_edges'] = len(edges)
    data['meta']['last_updated'] = "2026-04-18"
    data['meta']['last_modified'] = "2026-04-18"

    # ─── Save ────────────────────────────────────────────────────
    with open(GRAPH_FILE, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # ─── Verify ──────────────────────────────────────────────────
    # Rebuild degree map
    degree = defaultdict(int)
    for e in edges:
        degree[e['from']] += 1
        degree[e['to']] += 1

    print("=" * 65)
    print("Toy 1271 — Wire T1302-T1306 into AC Graph")
    print("=" * 65)

    print(f"\nAdded {len([t for t in new_tids if t not in already_present])} theorem nodes")
    print(f"Added {added} edges")
    print(f"Graph: {len(theorems)} nodes, {len(edges)} edges")

    strong = sum(1 for e in edges if e['source'] in ('derived', 'isomorphic'))
    print(f"Strong: {strong}/{len(edges)} = {100*strong/len(edges):.1f}%")

    # ─── Test Battery ────────────────────────────────────────────
    print("\n" + "=" * 65)
    print("TEST BATTERY")
    print("=" * 65)

    tests_pass = 0
    tests_total = 0

    # T1: All 5 theorems in graph
    tests_total += 1
    final_tids = set(t['tid'] for t in theorems)
    ok = all(t in final_tids for t in new_tids)
    print(f"  T1  All 5 theorems added:       {'PASS' if ok else 'FAIL'}")
    if ok: tests_pass += 1

    # T2: quantum_mechanics domain expanded
    tests_total += 1
    qm_count = sum(1 for t in theorems if t.get('domain','') == 'quantum_mechanics')
    ok = qm_count >= 5  # was 1, should now be 5
    print(f"  T2  QM domain ≥ 5 nodes:        {'PASS' if ok else 'FAIL'} ({qm_count})")
    if ok: tests_pass += 1

    # T3: cooperation domain expanded
    tests_total += 1
    coop_count = sum(1 for t in theorems if t.get('domain','') == 'cooperation')
    ok = coop_count >= 2  # was 1, should now be 2
    print(f"  T3  Cooperation domain ≥ 2:     {'PASS' if ok else 'FAIL'} ({coop_count})")
    if ok: tests_pass += 1

    # T4: Each new theorem has degree ≥ 3
    tests_total += 1
    new_degs = {t: degree[t] for t in new_tids}
    ok = all(d >= 3 for d in new_degs.values())
    print(f"  T4  All new nodes deg≥3:        {'PASS' if ok else 'FAIL'} ({dict(new_degs)})")
    if ok: tests_pass += 1

    # T5: T1302-T1305 form a connected cluster
    tests_total += 1
    qm_edges = 0
    for e in edges:
        if e['from'] in [1302,1303,1304,1305] and e['to'] in [1302,1303,1304,1305]:
            qm_edges += 1
    ok = qm_edges >= 4  # at least 4 internal edges
    print(f"  T5  QM cluster connected:       {'PASS' if ok else 'FAIL'} ({qm_edges} internal edges)")
    if ok: tests_pass += 1

    # T6: All connect to T186 (Five Integers)
    tests_total += 1
    t186_connections = sum(1 for t in new_tids if (186, t) in edge_set or (t, 186) in edge_set)
    ok = t186_connections == 5
    print(f"  T6  All connect to T186:        {'PASS' if ok else 'FAIL'} ({t186_connections}/5)")
    if ok: tests_pass += 1

    # T7: All connect to T663 (Three AC Ops)
    tests_total += 1
    t663_connections = sum(1 for t in new_tids if (663, t) in edge_set or (t, 663) in edge_set)
    ok = t663_connections == 5
    print(f"  T7  All connect to T663:        {'PASS' if ok else 'FAIL'} ({t663_connections}/5)")
    if ok: tests_pass += 1

    # T8: No duplicates
    tests_total += 1
    edge_pairs = [(e['from'], e['to']) for e in edges]
    ok = len(edge_pairs) == len(set(edge_pairs))
    print(f"  T8  No duplicate edges:         {'PASS' if ok else 'FAIL'}")
    if ok: tests_pass += 1

    # T9: Strong % above 85%
    tests_total += 1
    strong_pct = 100 * strong / len(edges)
    ok = strong_pct >= 85.0
    print(f"  T9  Strong ≥ 85%:               {'PASS' if ok else 'FAIL'} ({strong_pct:.1f}%)")
    if ok: tests_pass += 1

    # T10: T1305 connects to T110 (rank=2)
    tests_total += 1
    ok = (110, 1305) in edge_set or (1305, 110) in edge_set
    print(f"  T10 T1305 connects to T110:     {'PASS' if ok else 'FAIL'}")
    if ok: tests_pass += 1

    print(f"\nSCORE: {tests_pass}/{tests_total} PASS")

    # Report node degrees
    print(f"\n--- New Node Degrees ---")
    for tid in new_tids:
        t = next((t_ for t_ in theorems if t_['tid'] == tid), None)
        print(f"  T{tid} ({t['name']}): deg={degree[tid]}")

if __name__ == "__main__":
    main()
