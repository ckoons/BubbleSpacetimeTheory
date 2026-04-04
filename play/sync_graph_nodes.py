#!/usr/bin/env python3
"""
Sync AC theorem graph with the registry.

Tasks:
1. Identify theorems in the registry that are NOT nodes in the graph
2. Add missing nodes with minimal metadata
3. Wire parent edges from registry Parent: references
4. Fix stale meta counters
5. Report summary

Rules:
- Skip unassigned/reserved/superseded tids (T43-46, T63, T591-599, T627, T686-688, T749-750)
- Skip T561-565 (no documentation found anywhere)
- Do NOT duplicate existing nodes or edges
- Log when a parent tid doesn't exist as a node
"""

import json
import re
import sys
from pathlib import Path

GRAPH_FILE = Path(__file__).parent / "ac_graph_data.json"
REGISTRY_FILE = Path(__file__).parent.parent / "notes" / "BST_AC_Theorem_Registry.md"

# ============================================================
# LOAD
# ============================================================
with open(GRAPH_FILE) as f:
    data = json.load(f)

with open(REGISTRY_FILE) as f:
    registry_text = f.read()
    registry_lines = registry_text.split("\n")

graph_tids = set(t["tid"] for t in data["theorems"])
existing_edges = set((e["from"], e["to"]) for e in data["edges"])

# Known gaps that should NOT be added
SKIP_TIDS = set()
SKIP_TIDS.update([43, 44, 45, 46])        # never assigned
SKIP_TIDS.add(63)                           # unassigned
SKIP_TIDS.update(range(591, 600))           # unassigned
SKIP_TIDS.add(627)                          # unassigned
SKIP_TIDS.update([686, 687, 688])           # superseded
SKIP_TIDS.update([749, 750])               # unassigned (no evidence)
SKIP_TIDS.update(range(561, 566))           # no documentation found

nodes_added = 0
edges_added = 0
skipped_parent_missing = []


def add_node(tid, name, domain, depth, status="proved"):
    """Add a theorem node if it doesn't already exist."""
    global nodes_added
    if tid in graph_tids:
        return False
    node = {
        "tid": tid,
        "name": name,
        "domain": domain,
        "status": status,
        "depth": depth,
        "conflation": 0,
        "section": "",
        "toys": [],
        "date": "2026-04-04",
        "plain": "",
        "proofs": []
    }
    data["theorems"].append(node)
    graph_tids.add(tid)
    nodes_added += 1
    return True


def add_edge(from_tid, to_tid):
    """Add an edge if both endpoints exist and edge doesn't exist."""
    global edges_added
    if (from_tid, to_tid) in existing_edges:
        return False
    if from_tid not in graph_tids:
        skipped_parent_missing.append(
            f"T{from_tid} -> T{to_tid}: parent T{from_tid} not in graph"
        )
        return False
    if to_tid not in graph_tids:
        skipped_parent_missing.append(
            f"T{from_tid} -> T{to_tid}: child T{to_tid} not in graph"
        )
        return False
    data["edges"].append({"from": from_tid, "to": to_tid})
    existing_edges.add((from_tid, to_tid))
    edges_added += 1
    return True


# ============================================================
# STEP 1: Find missing nodes from registry
# ============================================================
# The graph already has 782 nodes (T1-T812 minus gaps).
# Most theorems are present. Check comprehensively.

# Build the set of tids that SHOULD exist based on registry
# Registry main table line says: T1-T42, T47-T62, T64-T480, T531-T539, T540-T570, T572-T590, T600-T611, T628-T771
# Plus update notes: T772-T812
expected_ranges = [
    range(1, 43), range(47, 63), range(64, 481),
    range(481, 531),     # these ARE real (in graph already, despite registry note)
    range(531, 540), range(540, 571), range(572, 591),
    range(600, 627),     # T612-T626 are in graph
    range(628, 772),
    range(772, 813),
]
expected_tids = set()
for r in expected_ranges:
    expected_tids.update(r)
expected_tids -= SKIP_TIDS

missing_from_graph = sorted(expected_tids - graph_tids)

print(f"Graph currently has {len(graph_tids)} nodes (max tid: {max(graph_tids)})")
print(f"Registry expects {len(expected_tids)} theorem tids")
print(f"Missing from graph: {len(missing_from_graph)} tids: {missing_from_graph}")

# If there ARE missing tids, try to create minimal nodes for them
# (Currently expect 0 based on analysis, but handle gracefully)
for tid in missing_from_graph:
    name = f"Theorem {tid} (auto-synced)"
    # Try to find name from registry text
    pattern = rf'T{tid}\s+\(([^—)]+)'
    m = re.search(pattern, registry_text)
    if m:
        name = m.group(1).strip().rstrip(" —")
    add_node(tid, name, "foundations", 0)
    # Wire to T186 as default parent if no other info
    add_edge(186, tid)


# ============================================================
# STEP 2: Wire missing parent edges from registry
# ============================================================
# Parse each registry line for "Parents: T<x>, T<y>, ..." patterns

missing_edge_count_before = edges_added

for line in registry_lines:
    # Match: T<number> (<name> — <description>. Parents: <parent_list>.)
    m = re.search(r'T(\d+)\s+\([^|]*?Parents?:\s*([^)]+)\)', line)
    if m:
        child_tid = int(m.group(1))
        parent_str = m.group(2)
        parent_tids = [int(x) for x in re.findall(r'T(\d+)', parent_str)]
        for ptid in parent_tids:
            add_edge(ptid, child_tid)

# Also parse update notes for parent references
# Pattern in update notes: T<number> ... parents T<x>, T<y>
for line in registry_lines:
    # Match patterns like: parents T318, T717
    for m in re.finditer(r'T(\d+)[^;]*?parents?\s+([^);\n]+)', line, re.IGNORECASE):
        child_tid = int(m.group(1))
        parent_str = m.group(2)
        parent_tids = [int(x) for x in re.findall(r'T(\d+)', parent_str)]
        for ptid in parent_tids:
            add_edge(ptid, child_tid)

new_edges_from_parents = edges_added - missing_edge_count_before


# ============================================================
# STEP 3: Fix meta
# ============================================================
actual_theorems = len(data["theorems"])
actual_edges = len(data["edges"])

d0 = sum(1 for t in data["theorems"] if t.get("depth", 0) == 0)
d1 = sum(1 for t in data["theorems"] if t.get("depth", 0) == 1)
d2 = sum(1 for t in data["theorems"] if t.get("depth", 0) >= 2)

data["meta"]["theorem_count"] = actual_theorems
data["meta"]["edge_count"] = actual_edges
data["meta"]["total_theorems"] = actual_theorems
data["meta"]["total_edges"] = actual_edges
data["meta"]["node_count"] = actual_theorems
data["meta"]["depth_distribution"] = {"D0": d0, "D1": d1, "D2": d2}
data["meta"]["D0"] = d0
data["meta"]["D1"] = d1
data["meta"]["D2"] = d2
data["meta"]["last_modified"] = "2026-04-04"
data["meta"]["last_updated"] = "2026-04-04"

# Sort theorems by tid
data["theorems"].sort(key=lambda t: t["tid"])

# ============================================================
# STEP 4: Save
# ============================================================
with open(GRAPH_FILE, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# ============================================================
# REPORT
# ============================================================
print(f"\n{'='*60}")
print(f"AC THEOREM GRAPH SYNC REPORT")
print(f"{'='*60}")
print(f"Nodes added:           {nodes_added}")
print(f"Edges added:           {edges_added}")
print(f"  (parent edges):      {new_edges_from_parents}")
print(f"{'='*60}")
print(f"Final graph:")
print(f"  Theorems:  {actual_theorems}")
print(f"  Edges:     {actual_edges}")
print(f"  Depth:     D0={d0}, D1={d1}, D2={d2}")
print(f"{'='*60}")

print(f"\nMeta fixes applied:")
print(f"  node_count: 773 -> {actual_theorems}")
print(f"  edge_count: 1775 -> {actual_edges}")

if skipped_parent_missing:
    print(f"\nSkipped edges (missing endpoints): {len(skipped_parent_missing)}")
    for s in skipped_parent_missing[:10]:
        print(f"  - {s}")
    if len(skipped_parent_missing) > 10:
        print(f"  ... and {len(skipped_parent_missing) - 10} more")

print(f"\nDeliberately skipped tids (unassigned/reserved/superseded):")
print(f"  T43-T46: never assigned")
print(f"  T63: unassigned")
print(f"  T561-T565: no documentation anywhere")
print(f"  T591-T599: unassigned")
print(f"  T627: unassigned")
print(f"  T686-T688: superseded")
print(f"  T749-T750: unassigned (no evidence)")
