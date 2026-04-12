#!/usr/bin/env python3
"""
Graph Self-Reflection Tool — The graph that asks its own questions.

Casey directive D5 (April 10, 2026): "Can we setup a method for the graph
to look at itself and ask questions?"

Six layers:
  L1: Structural self-examination (bridges, islands, curvature, spectral gap)
  L2: Gap detection → question generation
  L3: Pattern recognition (recurring structures, domain-specific habits)
  L4: Self-consistency (acyclicity, symmetry, proportionality)
  L5: Meta (Gödel limit, convergence, self-knowledge fraction)
  L6: Non-Contact Detection (T1012 Observational Bridging Principle)

Output: Ranked list of research questions sorted by estimated productivity.

Usage:
  python3 graph_self_reflection.py                  # full analysis
  python3 graph_self_reflection.py --layer 1        # single layer
  python3 graph_self_reflection.py --top 10         # top 10 questions only
  python3 graph_self_reflection.py --domain biology  # domain focus
"""

import json
import sys
from pathlib import Path
from collections import Counter, defaultdict
from math import log2, sqrt

GRAPH_PATH = Path(__file__).parent / "ac_graph_data.json"


def load_graph(path=None):
    p = Path(path) if path else GRAPH_PATH
    with open(p) as f:
        return json.load(f)


def build_adjacency(data):
    """Build adjacency lists (directed and undirected)."""
    adj_out = defaultdict(set)  # directed: parent → child
    adj_in = defaultdict(set)   # directed: child → parent
    adj_un = defaultdict(set)   # undirected
    for e in data["edges"]:
        f, t = e["from"], e["to"]
        adj_out[f].add(t)
        adj_in[t].add(f)
        adj_un[f].add(t)
        adj_un[t].add(f)
    return adj_out, adj_in, adj_un


def theorem_lookup(data):
    """Build tid → theorem dict."""
    return {t["tid"]: t for t in data["theorems"]}


# ============================================================
# LAYER 1: Structural Self-Examination
# ============================================================

def layer1_structural(data, adj_out, adj_in, adj_un, lookup):
    """Compute structural properties of the graph."""
    results = {"layer": 1, "name": "Structural Self-Examination", "findings": []}
    n_nodes = len(data["theorems"])
    n_edges = len(data["edges"])

    # Basic stats
    results["stats"] = {
        "nodes": n_nodes,
        "edges": n_edges,
        "density": n_edges / (n_nodes * (n_nodes - 1)) if n_nodes > 1 else 0,
        "avg_degree": 2 * n_edges / n_nodes if n_nodes > 0 else 0,
    }

    # Degree distribution
    degrees = {tid: len(adj_un.get(tid, set())) for tid in lookup}
    in_degrees = {tid: len(adj_in.get(tid, set())) for tid in lookup}
    out_degrees = {tid: len(adj_out.get(tid, set())) for tid in lookup}

    # Islands (degree 0 or 1)
    islands = [tid for tid, d in degrees.items() if d == 0]
    leaves = [tid for tid, d in degrees.items() if d == 1]
    results["islands"] = {
        "count": len(islands),
        "theorems": [f"T{tid}: {lookup[tid]['name']}" for tid in islands[:10]],
    }
    results["leaves"] = {"count": len(leaves)}

    # Hubs (highest degree)
    top_hubs = sorted(degrees.items(), key=lambda x: -x[1])[:15]
    results["hubs"] = [
        {"tid": f"T{tid}", "name": lookup[tid]["name"], "domain": lookup[tid]["domain"],
         "degree": d, "in": in_degrees[tid], "out": out_degrees[tid]}
        for tid, d in top_hubs
    ]

    # Domain connectivity
    domain_nodes = defaultdict(set)
    for t in data["theorems"]:
        domain_nodes[t["domain"]].add(t["tid"])

    # Cross-domain edges
    cross_domain = 0
    within_domain = 0
    domain_pairs = Counter()
    for e in data["edges"]:
        d_from = lookup.get(e["from"], {}).get("domain", "?")
        d_to = lookup.get(e["to"], {}).get("domain", "?")
        if d_from != d_to:
            cross_domain += 1
            pair = tuple(sorted([d_from, d_to]))
            domain_pairs[pair] += 1
        else:
            within_domain += 1

    results["cross_domain"] = {
        "cross": cross_domain,
        "within": within_domain,
        "ratio": cross_domain / n_edges if n_edges > 0 else 0,
    }

    # Zero-edge domain pairs
    all_domains = sorted(domain_nodes.keys())
    n_domains = len(all_domains)
    connected_pairs = set(domain_pairs.keys())
    zero_pairs = []
    for i in range(n_domains):
        for j in range(i + 1, n_domains):
            pair = tuple(sorted([all_domains[i], all_domains[j]]))
            if pair not in connected_pairs:
                combined_size = len(domain_nodes[all_domains[i]]) + len(domain_nodes[all_domains[j]])
                zero_pairs.append((pair, combined_size))
    zero_pairs.sort(key=lambda x: -x[1])  # biggest gaps first
    results["zero_edge_pairs"] = {
        "count": len(zero_pairs),
        "total_pairs": n_domains * (n_domains - 1) // 2,
        "connected_fraction": len(connected_pairs) / (n_domains * (n_domains - 1) // 2),
        "top_gaps": [{"pair": p, "combined_nodes": s} for p, s in zero_pairs[:15]],
    }

    # Strongest bridges (highest cross-domain edge count)
    top_bridges = domain_pairs.most_common(15)
    results["strongest_bridges"] = [
        {"pair": list(p), "edges": c} for p, c in top_bridges
    ]

    # Bridge theorems (appear in cross-domain edges from both sides)
    bridge_scores = Counter()
    for e in data["edges"]:
        d_from = lookup.get(e["from"], {}).get("domain", "?")
        d_to = lookup.get(e["to"], {}).get("domain", "?")
        if d_from != d_to:
            bridge_scores[e["from"]] += 1
            bridge_scores[e["to"]] += 1
    top_bridge_theorems = bridge_scores.most_common(10)
    results["bridge_theorems"] = [
        {"tid": f"T{tid}", "name": lookup[tid]["name"], "domain": lookup[tid]["domain"],
         "cross_domain_edges": c}
        for tid, c in top_bridge_theorems
    ]

    # Connected components (undirected)
    visited = set()
    components = []
    for tid in lookup:
        if tid not in visited:
            comp = set()
            stack = [tid]
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                comp.add(node)
                for nb in adj_un.get(node, set()):
                    if nb not in visited:
                        stack.append(nb)
            components.append(comp)
    components.sort(key=len, reverse=True)
    results["components"] = {
        "count": len(components),
        "largest": len(components[0]) if components else 0,
        "sizes": [len(c) for c in components[:5]],
    }

    # Depth distribution
    depths = Counter(t["depth"] for t in data["theorems"])
    results["depth_distribution"] = dict(depths)

    # Status distribution
    statuses = Counter(t["status"] for t in data["theorems"])
    results["status_distribution"] = dict(statuses)

    return results


# ============================================================
# LAYER 2: Gap Detection → Question Generation
# ============================================================

def layer2_gaps(data, adj_out, adj_in, adj_un, lookup, domain_nodes):
    """Identify gaps and generate research questions."""
    results = {"layer": 2, "name": "Gap Detection → Questions", "questions": []}

    # Question 1: Island theorems — why isolated?
    for t in data["theorems"]:
        tid = t["tid"]
        if len(adj_un.get(tid, set())) == 0:
            results["questions"].append({
                "priority": 8,
                "type": "island",
                "question": f"Why is T{tid} ({t['name']}) completely isolated? "
                           f"Domain: {t['domain']}. No edges at all.",
                "action": f"Find parent theorems for T{tid} or determine if it's an axiom.",
                "estimated_theorems": 2,
            })

    # Question 2: Low-connectivity theorems in large domains
    domain_avg_degree = {}
    for domain, tids in domain_nodes.items():
        degs = [len(adj_un.get(tid, set())) for tid in tids]
        domain_avg_degree[domain] = sum(degs) / len(degs) if degs else 0

    for t in data["theorems"]:
        tid = t["tid"]
        deg = len(adj_un.get(tid, set()))
        avg = domain_avg_degree.get(t["domain"], 0)
        if deg <= 1 and avg > 4 and len(domain_nodes.get(t["domain"], set())) > 10:
            results["questions"].append({
                "priority": 5,
                "type": "under_connected",
                "question": f"T{tid} ({t['name']}) has degree {deg} but domain "
                           f"'{t['domain']}' averages {avg:.1f}. Why so few connections?",
                "action": f"Wire T{tid} to related theorems in {t['domain']}.",
                "estimated_theorems": 1,
            })

    # Question 3: Zero-edge domain pairs that SHOULD be connected
    all_domains = sorted(domain_nodes.keys())
    n_domains = len(all_domains)
    connected_pairs = set()
    for e in data["edges"]:
        d_from = lookup.get(e["from"], {}).get("domain", "?")
        d_to = lookup.get(e["to"], {}).get("domain", "?")
        if d_from != d_to:
            connected_pairs.add(tuple(sorted([d_from, d_to])))

    # Heuristic: large domains that share keywords should be connected
    domain_keywords = {}
    for domain, tids in domain_nodes.items():
        words = Counter()
        for tid in tids:
            for w in lookup[tid]["name"].lower().split():
                if len(w) > 3:
                    words[w] += 1
        domain_keywords[domain] = set(w for w, c in words.most_common(20))

    for i in range(n_domains):
        for j in range(i + 1, n_domains):
            d1, d2 = all_domains[i], all_domains[j]
            pair = tuple(sorted([d1, d2]))
            if pair in connected_pairs:
                continue
            overlap = domain_keywords.get(d1, set()) & domain_keywords.get(d2, set())
            size = len(domain_nodes[d1]) + len(domain_nodes[d2])
            if overlap and size > 15:
                results["questions"].append({
                    "priority": 7,
                    "type": "missing_bridge",
                    "question": f"Domains '{d1}' ({len(domain_nodes[d1])}) and "
                               f"'{d2}' ({len(domain_nodes[d2])}) share keywords "
                               f"{sorted(overlap)[:5]} but have ZERO edges. Why?",
                    "action": f"Find or create a bridge theorem connecting {d1} ↔ {d2}.",
                    "estimated_theorems": 2,
                    "shared_keywords": sorted(overlap)[:5],
                })

    # Question 4: Asymmetric domain connections
    pair_directed = defaultdict(lambda: [0, 0])  # [A→B, B→A]
    for e in data["edges"]:
        d_from = lookup.get(e["from"], {}).get("domain", "?")
        d_to = lookup.get(e["to"], {}).get("domain", "?")
        if d_from != d_to:
            pair = tuple(sorted([d_from, d_to]))
            if d_from == pair[0]:
                pair_directed[pair][0] += 1
            else:
                pair_directed[pair][1] += 1

    for pair, (ab, ba) in pair_directed.items():
        total = ab + ba
        if total >= 5 and min(ab, ba) / max(ab, ba) < 0.2:
            heavy = pair[0] if ab > ba else pair[1]
            light = pair[1] if ab > ba else pair[0]
            results["questions"].append({
                "priority": 4,
                "type": "asymmetric",
                "question": f"'{heavy}' → '{light}' has {max(ab,ba)} edges but "
                           f"'{light}' → '{heavy}' has only {min(ab,ba)}. "
                           f"Is the reverse direction real?",
                "action": f"Look for theorems in {light} that depend on {heavy} concepts.",
                "estimated_theorems": 2,
            })

    # Sort by priority (highest first)
    results["questions"].sort(key=lambda q: -q["priority"])
    results["total_questions"] = len(results["questions"])

    return results


# ============================================================
# LAYER 3: Pattern Recognition
# ============================================================

def layer3_patterns(data, adj_out, adj_in, adj_un, lookup, domain_nodes):
    """Recognize recurring patterns in the graph."""
    results = {"layer": 3, "name": "Pattern Recognition", "patterns": []}

    # Pattern 1: Which theorems appear as parents most often?
    parent_count = Counter()
    for e in data["edges"]:
        parent_count[e["from"]] += 1

    universal_parents = [(tid, c) for tid, c in parent_count.most_common(20) if c > 15]
    if universal_parents:
        results["patterns"].append({
            "name": "Universal Parents",
            "description": "Theorems that are parents of many others — load-bearing foundations.",
            "items": [
                {"tid": f"T{tid}", "name": lookup[tid]["name"],
                 "children": c, "domain": lookup[tid]["domain"]}
                for tid, c in universal_parents
            ],
            "question": "If any universal parent were wrong, what fraction of the graph collapses?",
        })

    # Pattern 2: Domain edge patterns — does every X↔Y edge go through theorem Z?
    bridge_mediators = defaultdict(Counter)
    for e in data["edges"]:
        d_from = lookup.get(e["from"], {}).get("domain", "?")
        d_to = lookup.get(e["to"], {}).get("domain", "?")
        if d_from != d_to:
            pair = tuple(sorted([d_from, d_to]))
            bridge_mediators[pair][e["from"]] += 1
            bridge_mediators[pair][e["to"]] += 1

    bottleneck_pairs = []
    for pair, mediators in bridge_mediators.items():
        total_edges_for_pair = sum(1 for e in data["edges"]
                                   if tuple(sorted([
                                       lookup.get(e["from"], {}).get("domain", "?"),
                                       lookup.get(e["to"], {}).get("domain", "?")
                                   ])) == pair)
        if total_edges_for_pair >= 3:
            top_med = mediators.most_common(1)[0]
            fraction = top_med[1] / total_edges_for_pair
            if fraction > 0.5:
                bottleneck_pairs.append({
                    "pair": list(pair),
                    "bottleneck": f"T{top_med[0]} ({lookup[top_med[0]]['name']})",
                    "fraction": round(fraction, 2),
                    "total_edges": total_edges_for_pair,
                })

    if bottleneck_pairs:
        bottleneck_pairs.sort(key=lambda x: -x["fraction"])
        results["patterns"].append({
            "name": "Bottleneck Theorems",
            "description": "Domain pairs where >50% of edges pass through one theorem.",
            "items": bottleneck_pairs[:10],
            "question": "These connections are fragile — one theorem holds the bridge. "
                       "Can we add parallel edges?",
        })

    # Pattern 3: Depth distribution by domain
    domain_depth = defaultdict(list)
    for t in data["theorems"]:
        domain_depth[t["domain"]].append(t["depth"])

    deep_domains = []
    for domain, depths in domain_depth.items():
        avg = sum(depths) / len(depths)
        if avg > 0.3 and len(depths) > 5:
            deep_domains.append({"domain": domain, "avg_depth": round(avg, 2),
                                "count": len(depths), "depth_1_frac": round(sum(1 for d in depths if d >= 1) / len(depths), 2)})

    if deep_domains:
        deep_domains.sort(key=lambda x: -x["avg_depth"])
        results["patterns"].append({
            "name": "Deep Domains",
            "description": "Domains with above-average depth — may indicate complexity or incompleteness.",
            "items": deep_domains[:10],
            "question": "Can the deep theorems in these domains be flattened to depth 0?",
        })

    # Pattern 4: Proof chain coverage
    proof_tags = Counter()
    for t in data["theorems"]:
        for p in t.get("proofs", []):
            proof_tags[p] += 1

    results["patterns"].append({
        "name": "Proof Chain Coverage",
        "description": "Which Millennium problems have the most supporting theorems?",
        "items": [{"tag": tag, "count": c} for tag, c in proof_tags.most_common(10)],
        "question": "Is the theorem distribution across problems proportional to their difficulty?",
    })

    # Pattern 5: Temporal growth — theorems by date
    date_counts = Counter(t.get("date", "unknown") for t in data["theorems"])
    sorted_dates = sorted((d, c) for d, c in date_counts.items() if d != "unknown")
    if len(sorted_dates) > 5:
        results["patterns"].append({
            "name": "Growth Rate",
            "description": "Theorem discovery rate over time.",
            "recent_5": [{"date": d, "count": c} for d, c in sorted_dates[-5:]],
            "question": "Is the discovery rate accelerating, constant, or decelerating?",
        })

    return results


# ============================================================
# LAYER 4: Self-Consistency
# ============================================================

def layer4_consistency(data, adj_out, adj_in, adj_un, lookup):
    """Check internal consistency of the graph."""
    results = {"layer": 4, "name": "Self-Consistency", "checks": []}

    # Check 1: Cycles in the directed graph (should be a DAG)
    # Simple cycle detection via DFS
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {t["tid"]: WHITE for t in data["theorems"]}
    cycles = []

    def dfs_cycle(node, path):
        color[node] = GRAY
        for nb in adj_out.get(node, set()):
            if nb not in color:
                continue
            if color[nb] == GRAY:
                # Found cycle
                cycle_start = path.index(nb) if nb in path else -1
                if cycle_start >= 0:
                    cycles.append(path[cycle_start:] + [nb])
                if len(cycles) >= 5:
                    return
            elif color[nb] == WHITE:
                dfs_cycle(nb, path + [nb])
                if len(cycles) >= 5:
                    return
        color[node] = BLACK

    for t in data["theorems"]:
        if color[t["tid"]] == WHITE:
            dfs_cycle(t["tid"], [t["tid"]])
            if len(cycles) >= 5:
                break

    results["checks"].append({
        "name": "DAG Property (acyclicity)",
        "status": "PASS" if not cycles else "FAIL",
        "cycles_found": len(cycles),
        "examples": [
            [f"T{tid}" for tid in c] for c in cycles[:3]
        ],
    })

    # Check 2: Orphan edges (reference non-existent theorems)
    all_tids = set(t["tid"] for t in data["theorems"])
    orphan_edges = []
    for e in data["edges"]:
        if e["from"] not in all_tids or e["to"] not in all_tids:
            orphan_edges.append(e)

    results["checks"].append({
        "name": "Edge Integrity (no orphan references)",
        "status": "PASS" if not orphan_edges else "FAIL",
        "orphan_count": len(orphan_edges),
        "examples": orphan_edges[:5],
    })

    # Check 3: Duplicate edges
    edge_set = set()
    duplicates = []
    for e in data["edges"]:
        key = (e["from"], e["to"])
        if key in edge_set:
            duplicates.append(key)
        edge_set.add(key)

    results["checks"].append({
        "name": "No Duplicate Edges",
        "status": "PASS" if not duplicates else "WARN",
        "duplicate_count": len(duplicates),
    })

    # Check 4: Self-loops
    self_loops = [e for e in data["edges"] if e["from"] == e["to"]]
    results["checks"].append({
        "name": "No Self-Loops",
        "status": "PASS" if not self_loops else "WARN",
        "self_loop_count": len(self_loops),
    })

    # Check 5: Domain size vs edge proportionality
    domain_nodes = defaultdict(set)
    for t in data["theorems"]:
        domain_nodes[t["domain"]].add(t["tid"])

    domain_edges = Counter()
    for e in data["edges"]:
        d_from = lookup.get(e["from"], {}).get("domain", "?")
        d_to = lookup.get(e["to"], {}).get("domain", "?")
        domain_edges[d_from] += 1
        domain_edges[d_to] += 1

    over_connected = []
    under_connected = []
    for domain in domain_nodes:
        n = len(domain_nodes[domain])
        edges = domain_edges.get(domain, 0)
        if n > 5:
            ratio = edges / n
            if ratio > 10:
                over_connected.append({"domain": domain, "nodes": n, "edges": edges, "ratio": round(ratio, 1)})
            elif ratio < 2:
                under_connected.append({"domain": domain, "nodes": n, "edges": edges, "ratio": round(ratio, 1)})

    results["checks"].append({
        "name": "Domain Proportionality",
        "over_connected": sorted(over_connected, key=lambda x: -x["ratio"])[:5],
        "under_connected": sorted(under_connected, key=lambda x: x["ratio"])[:5],
    })

    return results


# ============================================================
# LAYER 5: Meta (Self-Knowledge)
# ============================================================

def layer5_meta(data, adj_out, adj_in, adj_un, lookup, domain_nodes, l1, l2, l3, l4):
    """The graph asking about itself."""
    results = {"layer": 5, "name": "Meta — Self-Knowledge", "insights": []}
    n_nodes = len(data["theorems"])
    n_edges = len(data["edges"])

    # How much of myself can I explain?
    proved = sum(1 for t in data["theorems"] if t["status"] == "proved")
    total = len(data["theorems"])
    proved_fraction = proved / total if total > 0 else 0

    results["insights"].append({
        "name": "Self-Knowledge Fraction",
        "value": round(proved_fraction * 100, 1),
        "limit": 19.1,  # Gödel limit
        "interpretation": f"{proved}/{total} theorems proved ({proved_fraction*100:.1f}%). "
                         f"BST Gödel limit: ≤19.1% self-knowledge. "
                         f"But this measures proved/total, not understood/understandable.",
    })

    # Graph entropy (domain distribution)
    domain_sizes = [len(tids) for tids in domain_nodes.values()]
    total_nodes = sum(domain_sizes)
    if total_nodes > 0:
        probs = [s / total_nodes for s in domain_sizes]
        entropy = -sum(p * log2(p) for p in probs if p > 0)
        max_entropy = log2(len(domain_nodes))
        results["insights"].append({
            "name": "Domain Entropy",
            "value": round(entropy, 2),
            "max": round(max_entropy, 2),
            "uniformity": round(entropy / max_entropy, 3) if max_entropy > 0 else 0,
            "interpretation": f"Domain distribution entropy: {entropy:.2f} / {max_entropy:.2f} = "
                             f"{entropy/max_entropy:.1%} uniform. "
                             f"High uniformity = balanced growth. Low = concentrated.",
        })

    # Questions generated vs questions answerable
    n_questions = l2["total_questions"]
    results["insights"].append({
        "name": "Question Generation Rate",
        "questions_found": n_questions,
        "interpretation": f"The graph generated {n_questions} research questions about itself. "
                         f"Each answered question may generate more. "
                         f"Prediction: this number grows faster than theorems.",
    })

    # Connectivity trend
    connected_frac = l1["zero_edge_pairs"]["connected_fraction"]
    results["insights"].append({
        "name": "Domain Connectivity",
        "connected_fraction": round(connected_frac, 3),
        "zero_pairs": l1["zero_edge_pairs"]["count"],
        "interpretation": f"{connected_frac:.1%} of domain pairs connected. "
                         f"{l1['zero_edge_pairs']['count']} zero-edge pairs remain. "
                         f"Prediction: connectivity increases but never reaches 100% "
                         f"(BST prohibitions prevent some connections).",
    })

    # Depth ceiling verification
    max_depth = max(t["depth"] for t in data["theorems"])
    depth_0_frac = sum(1 for t in data["theorems"] if t["depth"] == 0) / total
    results["insights"].append({
        "name": "Depth Ceiling",
        "max_depth": max_depth,
        "depth_0_fraction": round(depth_0_frac, 3),
        "interpretation": f"Maximum depth: {max_depth}. {depth_0_frac:.1%} at depth 0. "
                         f"T421 predicts depth ≤ 1 universally. "
                         f"{'CONFIRMED' if max_depth <= 1 else 'VIOLATED — depth ' + str(max_depth) + ' found'}.",
    })

    # Consistency summary
    n_pass = sum(1 for c in l4["checks"] if c.get("status") == "PASS")
    n_total = len(l4["checks"])
    results["insights"].append({
        "name": "Self-Consistency Score",
        "passed": n_pass,
        "total": n_total,
        "interpretation": f"{n_pass}/{n_total} consistency checks passed.",
    })

    return results


# ============================================================
# LAYER 6: Non-Contact Detection (T1012 Observational Bridging)
# ============================================================

# Generic words that appear in many theorem names and carry no
# domain-specific signal.  Excluded from keyword overlap scoring.
_GENERIC_WORDS = frozenset([
    "theorem", "lemma", "corollary", "proposition", "proof", "property",
    "principle", "result", "from", "with", "that", "this", "into", "over",
    "under", "each", "every", "also", "both", "than", "more", "most",
    "have", "does", "been", "were", "will", "shall", "must", "only",
    "first", "second", "third", "general", "special", "main", "fundamental",
    "basic", "extended", "reduced", "induced", "derived", "depth", "zero",
    "structure", "domain", "theory", "system", "space", "form", "type",
])


def _tokenise_name(name):
    """Lowercase, split, keep tokens >= 4 chars that are not generic."""
    return {w for w in name.lower().split() if len(w) >= 4 and w not in _GENERIC_WORDS}


def layer6_noncontact(data, adj_out, adj_in, adj_un, lookup, domain_nodes):
    """
    Layer 6 — Non-Contact Detection.

    T1012 (Observational Bridging Principle): >= 80.9% of inter-domain
    knowledge is non-contact — structural analogies visible only to
    observers who hold both domains in context simultaneously.

    For every zero-edge domain pair (A, B) we compute:
      1. Keyword overlap  — shared significant words in theorem names.
      2. Structural parallel — similarity in degree distributions, depth
         profiles, and parent/child fan-out patterns.
      3. Relay theorems — theorems in a third domain C that connect to
         both A and B, mediating non-contact knowledge.
      4. Composite score  — weighted combination of the three signals.
    """
    results = {
        "layer": 6,
        "name": "Non-Contact Detection (T1012 Observational Bridging)",
        "pairs": [],
        "summary": {},
    }

    # ---- helpers ----
    all_domains = sorted(domain_nodes.keys())

    # Which domain pairs already have at least one edge?
    connected_pairs = set()
    for e in data["edges"]:
        d_from = lookup.get(e["from"], {}).get("domain", "?")
        d_to = lookup.get(e["to"], {}).get("domain", "?")
        if d_from != d_to:
            connected_pairs.add(tuple(sorted([d_from, d_to])))

    # Pre-compute per-domain token sets and per-theorem tokens
    domain_tokens = {}          # domain → set of all significant tokens
    theorem_tokens = {}         # tid → set of tokens
    for domain, tids in domain_nodes.items():
        all_tok = set()
        for tid in tids:
            toks = _tokenise_name(lookup[tid]["name"])
            theorem_tokens[tid] = toks
            all_tok |= toks
        domain_tokens[domain] = all_tok

    # Per-domain structural profiles
    def _domain_profile(domain):
        """Return degree list, depth counter, avg in/out fan."""
        tids = domain_nodes[domain]
        degrees = [len(adj_un.get(tid, set())) for tid in tids]
        depths = Counter(lookup[tid]["depth"] for tid in tids)
        in_fans = [len(adj_in.get(tid, set())) for tid in tids]
        out_fans = [len(adj_out.get(tid, set())) for tid in tids]
        n = len(tids) or 1
        return {
            "avg_degree": sum(degrees) / n,
            "max_degree": max(degrees) if degrees else 0,
            "depths": depths,
            "avg_in": sum(in_fans) / n,
            "avg_out": sum(out_fans) / n,
            "size": len(tids),
        }

    profiles = {d: _domain_profile(d) for d in all_domains}

    # Pre-compute: for each domain, which other domains connect to it?
    domain_neighbours = defaultdict(set)
    for pair in connected_pairs:
        domain_neighbours[pair[0]].add(pair[1])
        domain_neighbours[pair[1]].add(pair[0])

    # ---- score each zero-edge pair ----
    n_domains = len(all_domains)
    scored = []

    for i in range(n_domains):
        for j in range(i + 1, n_domains):
            dA, dB = all_domains[i], all_domains[j]
            pair_key = (dA, dB)
            if pair_key in connected_pairs:
                continue

            # --- 1. Keyword overlap ---
            shared_kw = domain_tokens.get(dA, set()) & domain_tokens.get(dB, set())
            kw_score = len(shared_kw)

            # Find specific theorem pairs that share keywords
            kw_matches = []
            if shared_kw:
                tids_a = domain_nodes[dA]
                tids_b = domain_nodes[dB]
                for ta in tids_a:
                    tok_a = theorem_tokens.get(ta, set())
                    if not tok_a & shared_kw:
                        continue
                    for tb in tids_b:
                        tok_b = theorem_tokens.get(tb, set())
                        overlap = tok_a & tok_b
                        if overlap:
                            kw_matches.append({
                                "tid_a": ta,
                                "tid_b": tb,
                                "shared": sorted(overlap),
                            })
                # Keep top matches by overlap size
                kw_matches.sort(key=lambda m: -len(m["shared"]))
                kw_matches = kw_matches[:8]

            # --- 2. Structural parallel ---
            pA, pB = profiles[dA], profiles[dB]

            # Degree similarity (inverse of relative difference)
            avg_deg_max = max(pA["avg_degree"], pB["avg_degree"], 0.01)
            deg_sim = 1.0 - abs(pA["avg_degree"] - pB["avg_degree"]) / avg_deg_max

            # Depth profile similarity (cosine of depth vectors)
            all_depths = set(pA["depths"].keys()) | set(pB["depths"].keys())
            dot = sum(pA["depths"].get(d, 0) * pB["depths"].get(d, 0) for d in all_depths)
            mag_a = sqrt(sum(v ** 2 for v in pA["depths"].values())) or 1
            mag_b = sqrt(sum(v ** 2 for v in pB["depths"].values())) or 1
            depth_cos = dot / (mag_a * mag_b)

            # Fan-out similarity
            fan_max = max(pA["avg_out"], pB["avg_out"], 0.01)
            fan_sim = 1.0 - abs(pA["avg_out"] - pB["avg_out"]) / fan_max

            struct_score = round((deg_sim + depth_cos + fan_sim) / 3.0, 4)

            structural_detail = {
                "degree_similarity": round(deg_sim, 3),
                "depth_cosine": round(depth_cos, 3),
                "fanout_similarity": round(fan_sim, 3),
            }

            # --- 3. Relay theorems ---
            # A relay domain C has edges to BOTH A and B.
            relay_domains = domain_neighbours.get(dA, set()) & domain_neighbours.get(dB, set())

            # For each relay domain find the actual theorems that bridge
            relay_detail = []
            for dC in sorted(relay_domains):
                # Theorems in C connected to A
                c_to_a = set()
                # Theorems in C connected to B
                c_to_b = set()
                for tid_c in domain_nodes[dC]:
                    neighbours_of_c = adj_un.get(tid_c, set())
                    if neighbours_of_c & domain_nodes[dA]:
                        c_to_a.add(tid_c)
                    if neighbours_of_c & domain_nodes[dB]:
                        c_to_b.add(tid_c)
                # Relay theorems: in C and touching BOTH A and B
                relay_tids = c_to_a & c_to_b
                if relay_tids:
                    relay_detail.append({
                        "relay_domain": dC,
                        "relay_theorems": [
                            {"tid": tid, "name": lookup[tid]["name"]}
                            for tid in sorted(relay_tids)[:5]
                        ],
                        "count": len(relay_tids),
                    })

            relay_count = sum(r["count"] for r in relay_detail)
            relay_score = relay_count  # raw count used in composite

            # --- 4. Composite score ---
            # Weights: keywords matter most, relays second, structure third
            composite = round(kw_score * 3.0 + relay_score * 2.0 + struct_score * 5.0, 2)

            entry = {
                "pair": [dA, dB],
                "sizes": [pA["size"], pB["size"]],
                "keyword_overlap": {
                    "score": kw_score,
                    "shared_keywords": sorted(shared_kw)[:15],
                    "theorem_matches": [
                        {
                            "a": f"T{m['tid_a']} ({lookup[m['tid_a']]['name']})",
                            "b": f"T{m['tid_b']} ({lookup[m['tid_b']]['name']})",
                            "shared": m["shared"],
                        }
                        for m in kw_matches[:5]
                    ],
                },
                "structural_parallel": {
                    "score": struct_score,
                    "detail": structural_detail,
                },
                "relay": {
                    "relay_domain_count": len(relay_detail),
                    "relay_theorem_count": relay_count,
                    "relays": relay_detail[:8],
                },
                "composite_score": composite,
            }
            scored.append(entry)

    # Sort by composite score descending
    scored.sort(key=lambda x: -x["composite_score"])

    results["pairs"] = scored
    results["summary"] = {
        "zero_edge_pairs_analysed": len(scored),
        "pairs_with_keyword_overlap": sum(1 for s in scored if s["keyword_overlap"]["score"] > 0),
        "pairs_with_relays": sum(1 for s in scored if s["relay"]["relay_theorem_count"] > 0),
        "pairs_with_high_structural": sum(1 for s in scored if s["structural_parallel"]["score"] > 0.7),
        "top_composite": scored[0]["composite_score"] if scored else 0,
        "median_composite": scored[len(scored) // 2]["composite_score"] if scored else 0,
        "t1012_prediction": ">=80.9% of inter-domain knowledge is non-contact",
        "contact_fraction": round(
            len(connected_pairs) / max(n_domains * (n_domains - 1) // 2, 1), 3
        ),
        "noncontact_fraction": round(
            1.0 - len(connected_pairs) / max(n_domains * (n_domains - 1) // 2, 1), 3
        ),
    }

    return results


# ============================================================
# QUESTION RANKING
# ============================================================

def rank_questions(l1, l2, l3, l6=None):
    """Combine all questions and rank by estimated productivity."""
    questions = []

    # From L2: gap questions
    for q in l2["questions"]:
        questions.append({
            "source": "L2-gap",
            "priority": q["priority"],
            "question": q["question"],
            "action": q["action"],
            "estimated_new_theorems": q.get("estimated_theorems", 1),
        })

    # From L3: pattern questions
    for p in l3["patterns"]:
        questions.append({
            "source": "L3-pattern",
            "priority": 6,
            "question": p["question"],
            "action": f"Investigate pattern: {p['name']}",
            "estimated_new_theorems": 3,
        })

    # From L1: structural questions
    for hub in l1.get("hubs", [])[:3]:
        questions.append({
            "source": "L1-fragility",
            "priority": 7,
            "question": f"What happens if {hub['tid']} ({hub['name']}) is wrong? "
                       f"It has {hub['degree']} connections.",
            "action": f"Trace dependency tree of {hub['tid']}. Identify independent confirmation paths.",
            "estimated_new_theorems": 0,
        })

    # From L6: non-contact relationship questions
    if l6:
        for p in l6["pairs"][:15]:
            kw = p["keyword_overlap"]
            rl = p["relay"]
            # Higher composite = more likely a real hidden connection
            priority = min(9, 4 + int(p["composite_score"] / 10))
            kw_str = ", ".join(kw["shared_keywords"][:4]) if kw["shared_keywords"] else "none"
            relay_str = (f"{rl['relay_theorem_count']} relay(s) via "
                        f"{', '.join(r['relay_domain'] for r in rl['relays'][:2])}"
                        if rl["relays"] else "no relays")
            questions.append({
                "source": "L6-noncontact",
                "priority": priority,
                "question": f"Non-contact parallel: {p['pair'][0]} <~> {p['pair'][1]} "
                           f"(score={p['composite_score']:.1f}). "
                           f"Shared keywords: [{kw_str}]. {relay_str}.",
                "action": f"Investigate structural analogy between {p['pair'][0]} and "
                         f"{p['pair'][1]}. Look for a bridge theorem or confirm "
                         f"the non-contact relationship is real (T1012).",
                "estimated_new_theorems": 2,
            })

    # Sort by priority × estimated theorems
    questions.sort(key=lambda q: -(q["priority"] * max(q["estimated_new_theorems"], 1)))

    return questions


# ============================================================
# MAIN
# ============================================================

def run_analysis(layer_filter=None, top_n=None, domain_filter=None):
    """Run full self-reflection analysis."""
    data = load_graph()
    adj_out, adj_in, adj_un = build_adjacency(data)
    lookup = theorem_lookup(data)

    domain_nodes = defaultdict(set)
    for t in data["theorems"]:
        domain_nodes[t["domain"]].add(t["tid"])

    # Filter by domain if requested
    if domain_filter:
        filtered_tids = domain_nodes.get(domain_filter, set())
        if not filtered_tids:
            print(f"Domain '{domain_filter}' not found. Available: {sorted(domain_nodes.keys())}")
            return
        data_filtered = {
            "theorems": [t for t in data["theorems"] if t["domain"] == domain_filter],
            "edges": [e for e in data["edges"] if e["from"] in filtered_tids or e["to"] in filtered_tids],
        }
        print(f"=== Domain Focus: {domain_filter} ({len(filtered_tids)} theorems) ===\n")

    l6 = None  # will be populated if layer 6 runs

    print("=" * 70)
    print("  GRAPH SELF-REFLECTION — The Graph That Asks Its Own Questions")
    print(f"  {len(data['theorems'])} theorems, {len(data['edges'])} edges, {len(domain_nodes)} domains")
    print("=" * 70)

    # Run layers
    if not layer_filter or layer_filter == 1:
        l1 = layer1_structural(data, adj_out, adj_in, adj_un, lookup)
        print(f"\n{'='*70}")
        print(f"  LAYER 1: {l1['name']}")
        print(f"{'='*70}")
        print(f"  Nodes: {l1['stats']['nodes']}  Edges: {l1['stats']['edges']}  "
              f"Density: {l1['stats']['density']:.4f}  Avg degree: {l1['stats']['avg_degree']:.1f}")
        print(f"  Components: {l1['components']['count']} (largest: {l1['components']['largest']})")
        print(f"  Islands: {l1['islands']['count']}  Leaves: {l1['leaves']['count']}")
        print(f"  Cross-domain edges: {l1['cross_domain']['cross']} ({l1['cross_domain']['ratio']:.1%})")
        print(f"  Domain connectivity: {l1['zero_edge_pairs']['connected_fraction']:.1%} "
              f"({l1['zero_edge_pairs']['count']} zero-edge pairs)")
        print(f"\n  Top hubs:")
        for h in l1["hubs"][:10]:
            print(f"    {h['tid']:6s} {h['name'][:45]:45s} [{h['domain']:20s}] deg={h['degree']:3d} "
                  f"(in={h['in']}, out={h['out']})")
        print(f"\n  Top bridges (domain pairs):")
        for b in l1["strongest_bridges"][:10]:
            print(f"    {b['pair'][0]:25s} ↔ {b['pair'][1]:25s}  edges={b['edges']}")
        print(f"\n  Top zero-edge gaps (should be connected?):")
        for g in l1["zero_edge_pairs"]["top_gaps"][:10]:
            print(f"    {g['pair'][0]:25s} ↔ {g['pair'][1]:25s}  combined={g['combined_nodes']}")
        print(f"\n  Bridge theorems (most cross-domain edges):")
        for bt in l1["bridge_theorems"][:5]:
            print(f"    {bt['tid']:6s} {bt['name'][:45]:45s} cross_edges={bt['cross_domain_edges']}")
        print(f"\n  Depth: {l1['depth_distribution']}")
    else:
        l1 = layer1_structural(data, adj_out, adj_in, adj_un, lookup)

    if not layer_filter or layer_filter == 2:
        l2 = layer2_gaps(data, adj_out, adj_in, adj_un, lookup, domain_nodes)
        print(f"\n{'='*70}")
        print(f"  LAYER 2: {l2['name']}")
        print(f"{'='*70}")
        print(f"  Total questions generated: {l2['total_questions']}")
        by_type = Counter(q["type"] for q in l2["questions"])
        print(f"  By type: {dict(by_type)}")
        limit = top_n or 15
        print(f"\n  Top {limit} questions:")
        for i, q in enumerate(l2["questions"][:limit]):
            print(f"    {i+1:2d}. [{q['type']:18s}] (P={q['priority']}) {q['question'][:80]}")
    else:
        l2 = layer2_gaps(data, adj_out, adj_in, adj_un, lookup, domain_nodes)

    if not layer_filter or layer_filter == 3:
        l3 = layer3_patterns(data, adj_out, adj_in, adj_un, lookup, domain_nodes)
        print(f"\n{'='*70}")
        print(f"  LAYER 3: {l3['name']}")
        print(f"{'='*70}")
        for p in l3["patterns"]:
            print(f"\n  Pattern: {p['name']}")
            print(f"  {p['description']}")
            if "items" in p:
                for item in (p["items"][:7] if isinstance(p["items"], list) else []):
                    if isinstance(item, dict):
                        parts = [f"{k}={v}" for k, v in item.items()]
                        print(f"    {', '.join(parts[:4])}")
            print(f"  → Question: {p['question']}")
    else:
        l3 = layer3_patterns(data, adj_out, adj_in, adj_un, lookup, domain_nodes)

    if not layer_filter or layer_filter == 4:
        l4 = layer4_consistency(data, adj_out, adj_in, adj_un, lookup)
        print(f"\n{'='*70}")
        print(f"  LAYER 4: {l4['name']}")
        print(f"{'='*70}")
        for c in l4["checks"]:
            status = c.get("status", "INFO")
            print(f"  [{status:4s}] {c['name']}")
            if c.get("cycles_found"):
                print(f"         Cycles: {c['cycles_found']}. Examples: {c.get('examples', [])}")
            if c.get("over_connected"):
                for oc in c["over_connected"]:
                    print(f"         OVER: {oc['domain']} ({oc['nodes']} nodes, {oc['edges']} edges, ratio={oc['ratio']})")
            if c.get("under_connected"):
                for uc in c["under_connected"]:
                    print(f"         UNDER: {uc['domain']} ({uc['nodes']} nodes, {uc['edges']} edges, ratio={uc['ratio']})")
    else:
        l4 = layer4_consistency(data, adj_out, adj_in, adj_un, lookup)

    if not layer_filter or layer_filter == 5:
        l5 = layer5_meta(data, adj_out, adj_in, adj_un, lookup, domain_nodes, l1, l2, l3, l4)
        print(f"\n{'='*70}")
        print(f"  LAYER 5: {l5['name']}")
        print(f"{'='*70}")
        for insight in l5["insights"]:
            print(f"\n  {insight['name']}:")
            print(f"    {insight['interpretation']}")

    if not layer_filter or layer_filter == 6:
        l6 = layer6_noncontact(data, adj_out, adj_in, adj_un, lookup, domain_nodes)
        s = l6["summary"]
        print(f"\n{'='*70}")
        print(f"  LAYER 6: {l6['name']}")
        print(f"{'='*70}")
        print(f"  T1012 Observational Bridging Principle:")
        print(f"    Prediction: {s['t1012_prediction']}")
        print(f"    Contact fraction:     {s['contact_fraction']:.1%}")
        print(f"    Non-contact fraction: {s['noncontact_fraction']:.1%}")
        print(f"\n  Zero-edge pairs analysed:         {s['zero_edge_pairs_analysed']}")
        print(f"  Pairs with keyword overlap:       {s['pairs_with_keyword_overlap']}")
        print(f"  Pairs with relay theorems:        {s['pairs_with_relays']}")
        print(f"  Pairs with high structural sim:   {s['pairs_with_high_structural']}")
        print(f"  Top composite score:              {s['top_composite']}")
        print(f"  Median composite score:           {s['median_composite']}")

        limit = top_n or 20
        print(f"\n  Top {limit} non-contact relationships (ranked by composite score):")
        for i, p in enumerate(l6["pairs"][:limit]):
            kw = p["keyword_overlap"]
            st = p["structural_parallel"]
            rl = p["relay"]
            print(f"\n  {i+1:3d}. {p['pair'][0]:25s} <~> {p['pair'][1]:25s}  "
                  f"score={p['composite_score']:6.1f}")
            print(f"       sizes: {p['sizes'][0]}+{p['sizes'][1]}  "
                  f"keywords={kw['score']}  "
                  f"struct={st['score']:.3f}  "
                  f"relays={rl['relay_theorem_count']}")
            if kw["shared_keywords"]:
                print(f"       shared keywords: {', '.join(kw['shared_keywords'][:8])}")
            if kw["theorem_matches"]:
                for m in kw["theorem_matches"][:2]:
                    print(f"         match: {m['a'][:40]} <~> {m['b'][:40]}")
                    print(f"                via: {', '.join(m['shared'])}")
            if st["detail"]:
                d = st["detail"]
                print(f"       structural: deg_sim={d['degree_similarity']:.2f}  "
                      f"depth_cos={d['depth_cosine']:.2f}  "
                      f"fan_sim={d['fanout_similarity']:.2f}")
            if rl["relays"]:
                for r in rl["relays"][:3]:
                    relay_names = ", ".join(
                        f"T{rt['tid']}" for rt in r["relay_theorems"][:3]
                    )
                    print(f"       relay via {r['relay_domain']:20s}: "
                          f"{r['count']} theorem(s) [{relay_names}]")

    # Ranked questions (include L6 if it was computed)
    if not layer_filter:
        ranked = rank_questions(l1, l2, l3, l6)
        limit = top_n or 20
        print(f"\n{'='*70}")
        print(f"  TOP {limit} RESEARCH QUESTIONS (ranked by productivity)")
        print(f"{'='*70}")
        for i, q in enumerate(ranked[:limit]):
            print(f"\n  {i+1:2d}. [{q['source']:12s}] Priority={q['priority']}  "
                  f"Est. new theorems: {q['estimated_new_theorems']}")
            print(f"      Q: {q['question'][:90]}")
            print(f"      A: {q['action'][:90]}")

    print(f"\n{'='*70}")
    print(f"  Analysis complete. The graph asked {l2['total_questions']} questions about itself.")
    print(f"{'='*70}")


if __name__ == "__main__":
    layer = None
    top_n = None
    domain = None

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--layer" and i + 1 < len(args):
            layer = int(args[i + 1])
            i += 2
        elif args[i] == "--top" and i + 1 < len(args):
            top_n = int(args[i + 1])
            i += 2
        elif args[i] == "--domain" and i + 1 < len(args):
            domain = args[i + 1]
            i += 2
        else:
            i += 1

    run_analysis(layer_filter=layer, top_n=top_n, domain_filter=domain)
