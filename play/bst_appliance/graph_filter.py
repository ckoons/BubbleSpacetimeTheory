#!/usr/bin/env python3
"""
Graph filter utilities for the five-type edge architecture.

The AC theorem graph has five edge types (April 12, 2026):
  - "derived"    = A's proof uses B as premise (cascading failure risk)
  - "isomorphic" = same Bergman eigenvalue in different domains (siblings)
  - "predicted"  = T914/epoch method predicted before verification
  - "observed"   = natural relationship found, derivation pending
  - "analogical" = pattern match, may be coincidence

Usage:
    from bst_appliance.graph_filter import load_graph, get_proven_graph, edge_profile

Grace — updated from Toy 664 three-tier to five-type system.
"""

import json
from pathlib import Path
from collections import Counter

GRAPH_PATH = Path(__file__).parent.parent / "ac_graph_data.json"

EDGE_TYPES = ["derived", "isomorphic", "predicted", "observed", "analogical"]
STRONG_TYPES = {"derived", "isomorphic", "predicted"}  # high-confidence edges
WEAK_TYPES = {"observed", "analogical"}  # lower-confidence edges


def load_graph(path=None):
    """Load the AC theorem graph from JSON."""
    p = Path(path) if path else GRAPH_PATH
    with open(p) as f:
        return json.load(f)


def get_proven_graph(data):
    """Return graph with only derived + isomorphic + predicted edges — the proven structure."""
    return {
        "theorems": data["theorems"],
        "edges": [e for e in data["edges"] if e.get("source") in STRONG_TYPES],
        "meta": data.get("meta", {}),
        "chains": data.get("chains", []),
    }


def get_derived_graph(data):
    """Return graph with only 'derived' edges — pure proof chains."""
    return {
        "theorems": data["theorems"],
        "edges": [e for e in data["edges"] if e.get("source") == "derived"],
        "meta": data.get("meta", {}),
        "chains": data.get("chains", []),
    }


def get_isomorphic_graph(data):
    """Return graph with only 'isomorphic' edges — cross-domain siblings."""
    return {
        "theorems": data["theorems"],
        "edges": [e for e in data["edges"] if e.get("source") == "isomorphic"],
        "meta": data.get("meta", {}),
        "chains": data.get("chains", []),
    }


def get_enhanced_graph(data):
    """Return full graph (all edges)."""
    return data


def edge_profile(data):
    """Return dict with counts for each of the five edge types."""
    counts = Counter(e.get("source", "unknown") for e in data["edges"])
    return {
        "derived": counts.get("derived", 0),
        "isomorphic": counts.get("isomorphic", 0),
        "predicted": counts.get("predicted", 0),
        "observed": counts.get("observed", 0),
        "analogical": counts.get("analogical", 0),
        "total": len(data["edges"]),
        "strong": sum(counts.get(t, 0) for t in STRONG_TYPES),
        "weak": sum(counts.get(t, 0) for t in WEAK_TYPES),
    }


def honesty_ratio(data):
    """The fraction of edges that are strong (derived + isomorphic + predicted)."""
    p = edge_profile(data)
    return p["strong"] / p["total"] if p["total"] > 0 else 0


def non_contact_fraction(data):
    """Fraction of domain pairs with NO derived edges (T1012 test)."""
    domains = set(n.get("domain", "") for n in data["theorems"])
    node_domain = {n["tid"]: n.get("domain", "") for n in data["theorems"]}

    connected = set()
    for e in data["edges"]:
        if e.get("source") in STRONG_TYPES:
            d1 = node_domain.get(e["from"], "")
            d2 = node_domain.get(e["to"], "")
            if d1 != d2 and d1 and d2:
                connected.add(tuple(sorted([d1, d2])))

    big = [d for d in domains if sum(1 for n in data["theorems"] if n.get("domain") == d) >= 3]
    total = len(big) * (len(big) - 1) // 2
    return 1 - len(connected) / total if total > 0 else 0


if __name__ == "__main__":
    data = load_graph()
    p = edge_profile(data)

    print(f"Graph: {len(data['theorems'])} theorems, {p['total']} edges")
    print(f"\nFive-type profile:")
    for t in EDGE_TYPES:
        print(f"  {t:15s}: {p[t]:5d} ({100*p[t]/p['total']:.1f}%)")
    print(f"\n  Strong (d+i+p): {p['strong']:5d} ({100*p['strong']/p['total']:.1f}%)")
    print(f"  Weak (o+a):     {p['weak']:5d} ({100*p['weak']/p['total']:.1f}%)")
    print(f"  Honesty ratio:  {honesty_ratio(data):.1%}")
    print(f"  Non-contact:    {non_contact_fraction(data):.1%} (T1012 predicts ≥80.9%)")
