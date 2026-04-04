#!/usr/bin/env python3
"""
Wire T813-T823 into the AC theorem graph.
Grace — 2026-03-30

Adds 11 new theorems and all parent edges (tagged "required").
"""

import json
import sys
from datetime import date

GRAPH_PATH = "/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/ac_graph_data.json"
TODAY = date.today().isoformat()

# ── New theorems ────────────────────────────────────────────────────

NEW_THEOREMS = [
    {
        "tid": 813,
        "name": "Laughlin-Bergman Correspondence",
        "domain": "bst_physics",
        "status": "proved",
        "depth": 1,
        "conflation": 0,
        "section": "",
        "toys": [],
        "date": TODAY,
        "plain": "Laughlin wavefunction structure maps to Bergman kernel on D_IV^5.",
        "proofs": [],
        "parents": [186, 649, 666, 667],
    },
    {
        "tid": 814,
        "name": "FQHE Spacing Ratios",
        "domain": "bst_physics",
        "status": "proved",
        "depth": 0,
        "conflation": 0,
        "section": "",
        "toys": [],
        "date": TODAY,
        "plain": "Fractional quantum Hall spacing ratios follow from five integers.",
        "proofs": [],
        "parents": [813, 649, 666],
    },
    {
        "tid": 815,
        "name": "Even-Denominator State nu=5/2=n_C/rank",
        "domain": "bst_physics",
        "status": "proved",
        "depth": 0,
        "conflation": 0,
        "section": "",
        "toys": [],
        "date": TODAY,
        "plain": "The nu=5/2 even-denominator state is n_C/rank, purely geometric.",
        "proofs": [],
        "parents": [813, 667, 110],
    },
    {
        "tid": 816,
        "name": "Electronegativity as BST Rationals",
        "domain": "chemical_physics",
        "status": "proved",
        "depth": 0,
        "conflation": 0,
        "section": "",
        "toys": [],
        "date": TODAY,
        "plain": "Electronegativity values are rationals built from the five integers.",
        "proofs": [],
        "parents": [186, 198],
    },
    {
        "tid": 817,
        "name": "Bond Dissociation Universality",
        "domain": "chemical_physics",
        "status": "proved",
        "depth": 0,
        "conflation": 0,
        "section": "",
        "toys": [],
        "date": TODAY,
        "plain": "Bond dissociation energies scale universally from BST rationals.",
        "proofs": [],
        "parents": [198, 767],
    },
    {
        "tid": 818,
        "name": "Turbulence Exponents K41=5/3=n_C/N_c",
        "domain": "fluids",
        "status": "proved",
        "depth": 0,
        "conflation": 0,
        "section": "",
        "toys": [],
        "date": TODAY,
        "plain": "Kolmogorov 5/3 exponent is n_C/N_c. Turbulence is geometry.",
        "proofs": [],
        "parents": [667, 666],
    },
    {
        "tid": 819,
        "name": "EEG Frequency Bands",
        "domain": "observer_science",
        "status": "proved",
        "depth": 0,
        "conflation": 0,
        "section": "",
        "toys": [],
        "date": TODAY,
        "plain": "EEG frequency band structure derives from C_2, n_C, N_c.",
        "proofs": [],
        "parents": [650, 667, 666],
    },
    {
        "tid": 820,
        "name": "Gravitational Wave Parameters r_ISCO=C2*M",
        "domain": "bst_physics",
        "status": "proved",
        "depth": 0,
        "conflation": 0,
        "section": "",
        "toys": [],
        "date": TODAY,
        "plain": "ISCO radius r_ISCO = C_2 * M, directly from the Casimir invariant.",
        "proofs": [],
        "parents": [650, 186],
    },
    {
        "tid": 821,
        "name": "Topological Invariant Classification AZ=2n_C",
        "domain": "topology",
        "status": "proved",
        "depth": 0,
        "conflation": 0,
        "section": "",
        "toys": [],
        "date": TODAY,
        "plain": "Altland-Zirnbauer 10-fold way = 2*n_C. Topological classification is geometric.",
        "proofs": [],
        "parents": [667],
    },
    {
        "tid": 822,
        "name": "Spectral Signature Dynamical (revises T708)",
        "domain": "foundations",
        "status": "proved",
        "depth": 0,
        "conflation": 0,
        "section": "",
        "toys": [],
        "date": TODAY,
        "plain": "Spectral signature is dynamical, revising T708 with full domain census.",
        "proofs": [],
        "parents": [708, 628, 630],
    },
    {
        "tid": 823,
        "name": "Cross-Domain Fraction Universality P<1e-66",
        "domain": "foundations",
        "status": "proved",
        "depth": 0,
        "conflation": 0,
        "section": "",
        "toys": [],
        "date": TODAY,
        "plain": "Cross-domain fraction reuse probability < 10^-66. Not coincidence.",
        "proofs": [],
        "parents": [186, 628],
    },
]


def main():
    # Load
    with open(GRAPH_PATH, "r") as f:
        graph = json.load(f)

    old_node_count = len(graph["theorems"])
    old_edge_count = len(graph["edges"])

    existing_tids = {t["tid"] for t in graph["theorems"]}

    new_nodes_added = 0
    new_edges_added = 0

    for entry in NEW_THEOREMS:
        parents = entry.pop("parents")
        tid = entry["tid"]

        # Safety: skip if already present
        if tid in existing_tids:
            print(f"  SKIP T{tid} — already in graph")
            continue

        # Add theorem node
        graph["theorems"].append(entry)
        existing_tids.add(tid)
        new_nodes_added += 1

        # Add parent edges (from parent -> to child), tagged "required"
        for parent_tid in parents:
            edge = {"from": parent_tid, "to": tid, "source": "required"}
            graph["edges"].append(edge)
            new_edges_added += 1

    # Update meta
    total_nodes = old_node_count + new_nodes_added
    total_edges = old_edge_count + new_edges_added

    graph["meta"]["theorem_count"] = total_nodes
    graph["meta"]["total_theorems"] = total_nodes
    graph["meta"]["node_count"] = total_nodes
    graph["meta"]["edge_count"] = total_edges
    graph["meta"]["total_edges"] = total_edges
    graph["meta"]["last_modified"] = TODAY
    graph["meta"]["last_updated"] = TODAY

    # Recount depth distribution
    d0 = sum(1 for t in graph["theorems"] if t.get("depth", 0) == 0)
    d1 = sum(1 for t in graph["theorems"] if t.get("depth", 0) == 1)
    d2 = sum(1 for t in graph["theorems"] if t.get("depth", 0) == 2)
    graph["meta"]["depth_distribution"] = {"D0": d0, "D1": d1, "D2": d2}
    graph["meta"]["D0"] = d0
    graph["meta"]["D1"] = d1
    graph["meta"]["D2"] = d2

    # Write
    with open(GRAPH_PATH, "w") as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)

    # Report
    print(f"\n{'='*50}")
    print(f"  AC Graph Wiring Complete — T813-T823")
    print(f"{'='*50}")
    print(f"  New nodes added:  {new_nodes_added}")
    print(f"  New edges added:  {new_edges_added}")
    print(f"{'='*50}")
    print(f"  TOTAL GRAPH STATE")
    print(f"    Nodes:  {total_nodes}  (was {old_node_count})")
    print(f"    Edges:  {total_edges}  (was {old_edge_count})")
    print(f"    D0: {d0}  D1: {d1}  D2: {d2}")
    print(f"{'='*50}")

    # Verify all edges point to valid tids
    all_tids = {t["tid"] for t in graph["theorems"]}
    bad_edges = []
    for e in graph["edges"]:
        if e["from"] not in all_tids:
            bad_edges.append(f"  from={e['from']} missing")
        if e["to"] not in all_tids:
            bad_edges.append(f"  to={e['to']} missing")
    if bad_edges:
        print(f"\n  WARNING: {len(bad_edges)} dangling edge references:")
        for b in bad_edges:
            print(b)
    else:
        print(f"  Edge integrity: ALL OK (no dangling references)")


if __name__ == "__main__":
    main()
