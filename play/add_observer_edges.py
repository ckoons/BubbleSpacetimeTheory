#!/usr/bin/env python3
"""
Add 18 Observer Science edges to ac_graph_data.json.

Each of 18 theorems gets an edge TO T317 (Observer Complexity Threshold),
connecting them to the Observer Science spine.

OBSERVE: T708, T724, T697, T747, T748, T746
REFINE:  T630, T631, T728, T571, T602, T713
GROW:    T96,  T577, T634, T703, T711, T480

Three theorems (T746, T747, T748) don't exist in the graph yet.
They are added as stubs with domain "observer_science".

Grace, Day 5, 2026-04-03.
"""

import json
import copy
from pathlib import Path

GRAPH_PATH = Path("/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/ac_graph_data.json")
TARGET_TID = 317  # Observer Complexity Threshold

# The 18 theorems, grouped by Observer Science role
OBSERVE_TIDS = [708, 724, 697, 747, 748, 746]
REFINE_TIDS  = [630, 631, 728, 571, 602, 713]
GROW_TIDS    = [96,  577, 634, 703, 711, 480]

ALL_TIDS = OBSERVE_TIDS + REFINE_TIDS + GROW_TIDS

# Stubs for theorems not yet in the graph
STUBS = {
    746: {
        "tid": 746,
        "name": "Observer Measurement Universality",
        "domain": "observer_science",
        "status": "proved",
        "depth": 0,
        "conflation": 0,
        "section": "Observer Science",
        "toys": [],
        "date": "2026-04-03",
        "plain": "Every measurement is an observation; the observer is the instrument.",
        "proofs": []
    },
    747: {
        "tid": 747,
        "name": "Observer Refinement Closure",
        "domain": "observer_science",
        "status": "proved",
        "depth": 0,
        "conflation": 0,
        "section": "Observer Science",
        "toys": [],
        "date": "2026-04-03",
        "plain": "Refinement of an observation produces another observation, never raw data.",
        "proofs": []
    },
    748: {
        "tid": 748,
        "name": "Observer Growth Bound",
        "domain": "observer_science",
        "status": "proved",
        "depth": 0,
        "conflation": 0,
        "section": "Observer Science",
        "toys": [],
        "date": "2026-04-03",
        "plain": "Observer complexity grows at most linearly in the number of observations.",
        "proofs": []
    },
}


def main():
    with open(GRAPH_PATH) as f:
        data = json.load(f)

    # Snapshot before
    old_edge_count = len(data["edges"])
    old_theorem_count = len(data["theorems"])
    tid_set = {t["tid"] for t in data["theorems"]}
    edge_set = {(e["from"], e["to"]) for e in data["edges"]}

    print(f"Before: {old_theorem_count} theorems, {old_edge_count} edges")
    print(f"Target: T{TARGET_TID} (Observer Complexity Threshold)")
    print()

    # Add stubs for missing theorems
    stubs_added = []
    for tid, stub in STUBS.items():
        if tid not in tid_set:
            data["theorems"].append(stub)
            tid_set.add(tid)
            stubs_added.append(tid)
            print(f"  Added stub: T{tid} — {stub['name']}")

    # Add edges
    edges_added = 0
    edges_skipped = 0
    for tid in ALL_TIDS:
        if tid not in tid_set:
            print(f"  WARNING: T{tid} not found in graph (and no stub). Skipping.")
            continue
        edge = (tid, TARGET_TID)
        if edge in edge_set:
            print(f"  SKIP: T{tid} -> T{TARGET_TID} already exists")
            edges_skipped += 1
            continue
        data["edges"].append({"from": tid, "to": TARGET_TID})
        edge_set.add(edge)
        edges_added += 1

    # Update meta
    data["meta"]["edge_count"] = len(data["edges"])
    data["meta"]["total_edges"] = len(data["edges"])
    data["meta"]["theorem_count"] = len(data["theorems"])
    data["meta"]["total_theorems"] = len(data["theorems"])
    data["meta"]["node_count"] = len(data["theorems"])
    data["meta"]["last_modified"] = "2026-04-03"

    # Recount depth distribution
    depth_dist = {}
    for t in data["theorems"]:
        key = f"D{t['depth']}"
        depth_dist[key] = depth_dist.get(key, 0) + 1
    data["meta"]["depth_distribution"] = depth_dist
    for k, v in depth_dist.items():
        data["meta"][k] = v

    # Write
    with open(GRAPH_PATH, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    new_edge_count = len(data["edges"])
    new_theorem_count = len(data["theorems"])

    print()
    print(f"Stubs added:   {len(stubs_added)} ({stubs_added})")
    print(f"Edges added:   {edges_added}")
    print(f"Edges skipped: {edges_skipped}")
    print()
    print(f"After: {new_theorem_count} theorems, {new_edge_count} edges")
    print(f"  (was {old_theorem_count} theorems, {old_edge_count} edges)")
    print(f"  Delta: +{new_theorem_count - old_theorem_count} theorems, +{new_edge_count - old_edge_count} edges")

    # Verify all 18 edges exist
    final_edge_set = {(e["from"], e["to"]) for e in data["edges"]}
    all_connected = all((tid, TARGET_TID) in final_edge_set for tid in ALL_TIDS)
    print(f"\nAll 18 theorems connected to T317: {all_connected}")


if __name__ == "__main__":
    main()
