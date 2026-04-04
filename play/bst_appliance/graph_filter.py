#!/usr/bin/env python3
"""
Graph filter utilities for the two-graph architecture.

The AC theorem graph has two edge layers:
  - "required"  = organic logical dependencies (the pure BST graph)
  - "observed"  = observer additions (bridges, hubs, connectivity fixes)

Usage:
    from bst_appliance.graph_filter import load_graph, get_pure_graph, get_enhanced_graph

Grace — Toy 664
"""

import json
from pathlib import Path

GRAPH_PATH = Path(__file__).parent.parent / "ac_graph_data.json"


def load_graph(path=None):
    """Load the AC theorem graph from JSON."""
    p = Path(path) if path else GRAPH_PATH
    with open(p) as f:
        return json.load(f)


def get_pure_graph(data):
    """Return graph with only 'required' edges — the organic BST structure."""
    return {
        "theorems": data["theorems"],
        "edges": [e for e in data["edges"] if e.get("source") == "required"],
        "meta": data.get("meta", {}),
        "chains": data.get("chains", []),
    }


def get_enhanced_graph(data):
    """Return full graph (all edges) — required + observed."""
    return data


def get_observed_graph(data):
    """Return graph with only 'observed' edges — the observer layer."""
    return {
        "theorems": data["theorems"],
        "edges": [e for e in data["edges"] if e.get("source") == "observed"],
        "meta": data.get("meta", {}),
        "chains": data.get("chains", []),
    }


def edge_counts(data):
    """Return dict with required/observed/total edge counts."""
    req = sum(1 for e in data["edges"] if e.get("source") == "required")
    obs = sum(1 for e in data["edges"] if e.get("source") == "observed")
    return {"required": req, "observed": obs, "total": len(data["edges"])}


def strip_tags(data):
    """Return a copy with source tags removed from edges (for export)."""
    import copy
    d = copy.deepcopy(data)
    for e in d["edges"]:
        e.pop("source", None)
    return d


if __name__ == "__main__":
    data = load_graph()
    counts = edge_counts(data)
    print(f"Graph: {len(data['theorems'])} theorems, {counts['total']} edges")
    print(f"  Required: {counts['required']}")
    print(f"  Observed: {counts['observed']}")

    pure = get_pure_graph(data)
    print(f"\nPure graph: {len(pure['edges'])} edges")

    obs = get_observed_graph(data)
    print(f"Observed graph: {len(obs['edges'])} edges")
