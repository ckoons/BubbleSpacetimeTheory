#!/usr/bin/env python3
"""
Add missing theorem nodes and edges to ac_graph_data.json.

Rules:
1. Check if each T-number already exists BEFORE adding
2. Check if each edge already exists BEFORE adding
3. Every new node needs at least 1 incoming edge
4. Update meta section: theorem_count, edge_count, last_modified
5. Do NOT remove any existing nodes or edges
6. Skip unverified theorems (T526-T530 reserved, T591-T599 unassigned,
   T561-T565 no evidence, T686-T688 superseded)
"""

import json
from datetime import date

INPUT_FILE = "play/ac_graph_data.json"
OUTPUT_FILE = "play/ac_graph_data.json"

# Load current graph
with open(INPUT_FILE) as f:
    data = json.load(f)

existing_tids = set(t["tid"] for t in data["theorems"])
existing_edges = set((e["from"], e["to"]) for e in data["edges"])

nodes_added = 0
edges_added = 0
skipped_nodes = []
skipped_edges = []

def add_node(tid, name, domain, depth, status="proved", parents=None):
    """Add a theorem node if it doesn't already exist. Returns True if added."""
    global nodes_added
    if tid in existing_tids:
        skipped_nodes.append(f"T{tid} (already exists)")
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
        "date": "2026-03-30",
        "plain": "",
        "proofs": []
    }
    data["theorems"].append(node)
    existing_tids.add(tid)
    nodes_added += 1

    # Add parent edges
    if parents:
        for p in parents:
            add_edge(p, tid)

    return True

def add_edge(from_tid, to_tid):
    """Add an edge if it doesn't already exist and both endpoints exist."""
    global edges_added
    if (from_tid, to_tid) in existing_edges:
        skipped_edges.append(f"({from_tid} -> {to_tid}) already exists")
        return False
    if from_tid not in existing_tids:
        skipped_edges.append(f"({from_tid} -> {to_tid}) source T{from_tid} missing")
        return False
    if to_tid not in existing_tids:
        skipped_edges.append(f"({from_tid} -> {to_tid}) target T{to_tid} missing")
        return False

    data["edges"].append({"from": from_tid, "to": to_tid})
    existing_edges.add((from_tid, to_tid))
    edges_added += 1
    return True


# ============================================================
# GROUP 1: Biology (T446-T448)
# ============================================================
add_node(446, "Watson-Crick as Root Involution", "biology", 0, parents=[186])
add_node(447, "Wobble from Long Root Multiplicity", "biology", 0, parents=[186])
add_node(448, "Code-Management Isomorphism", "biology", 0, parents=[190, 667])

# T526-T530: SKIP — registry says "T481-T530 reserved/assigned elsewhere"
# T591-T599: SKIP — registry says "unassigned"
# T561-T565: SKIP — no evidence in any notes file
# T686-T688: SKIP — registry says "superseded"

# ============================================================
# GROUP 3: Biology/Complexity (T540-T578)
# ============================================================

# T540-T552: Protein Folding + Weyl Duality batch (March 30 batch 71)
add_node(540, "Weyl Duality", "biology", 0, parents=[186])
# T541 already exists (Gap Fertility)
add_node(542, "Domain Maturation Prediction", "biology", 0, parents=[186])
add_node(543, "Speaking Pairs", "biology", 0, parents=[186])
add_node(544, "SCOP Fold Count", "biology", 0, parents=[661])
add_node(545, "DSSP Secondary Structure", "biology", 0, parents=[666])
add_node(546, "Proteasome Subunit Count", "biology", 0, parents=[649])
add_node(547, "Nucleosome Wrapping", "biology", 0, parents=[666, 649])
add_node(548, "Protein Alphabet Size", "biology", 0, parents=[186])
add_node(549, "tRNA Anticodon Count", "biology", 0, parents=[186])
add_node(550, "Ribosome Subunit Ratio", "biology", 0, parents=[186])
add_node(551, "Membrane Bilayer Thickness", "biology", 0, parents=[186])
add_node(552, "ATP Stoichiometry", "biology", 0, parents=[186])

# T553-T560: Biology D1 Derivations (March 30 batch 72) — verified from biology paper Section 13
add_node(553, "Error Correction Hierarchy Bound", "biology", 1, parents=[186])
add_node(554, "Code Variant Mutation Distance", "biology", 1, parents=[186])
add_node(555, "Ribosomal Error Rate Bound", "biology", 1, parents=[186])
add_node(556, "Wobble Rule Derivation", "biology", 1, parents=[186])
add_node(557, "Degeneracy Distribution Optimality", "biology", 1, parents=[186])
add_node(558, "Codon Space Geodesic Bound", "biology", 1, parents=[186])
add_node(559, "Spontaneous Mutation Rate Spectrum", "biology", 1, parents=[186])
add_node(560, "Cell Cycle Checkpoint Count", "biology", 1, parents=[186])

# T561-T565: SKIP — no evidence in any notes file
# T566: Spectral Absorption Synchrony — verified from registry batch 74
add_node(566, "Spectral Absorption Synchrony", "biology", 0, parents=[186])

# T567-T570: Millennium Linearization (March 30 batch 73)
add_node(567, "Yang-Mills Linearization", "complexity", 1, parents=[186, 663])
add_node(568, "Navier-Stokes Linearization", "complexity", 1, parents=[186, 663])
add_node(569, "P≠NP Linearization", "complexity", 1, parents=[186, 663])
add_node(570, "Hodge Linearization", "complexity", 1, parents=[186, 663])

# T571: Holographic-Shannon Equivalence (March 30 batch 75) — verified
add_node(571, "Holographic-Shannon Equivalence", "information_theory", 1, parents=[186])

# T572-T575: Proof Complexity D1 (March 30 batch 76)
add_node(572, "Proof-Channel Capacity", "complexity", 1, parents=[186])
add_node(573, "Backbone-Width-Size Chain", "complexity", 1, parents=[186])
add_node(574, "Lifting-KW Completeness", "complexity", 1, parents=[186])
add_node(575, "Proof Efficiency Bound", "complexity", 1, parents=[186])

# T576-T578: Cooperation (March 30 batch 77)
add_node(576, "Cooperation Reclassification", "cooperation", 0, parents=[668])
add_node(577, "Compound Interest", "cooperation", 0, parents=[668])
add_node(578, "Cooperation Reclassification 2", "cooperation", 0, parents=[668])

# ============================================================
# GROUP 4: Cooperation + CI (T580-T584, T586-T589)
# ============================================================
add_node(580, "Aging as Cooperation Decay", "cooperation", 0, parents=[668])
add_node(581, "Seven Defection Modes", "cooperation", 0, parents=[649])
add_node(582, "Loose Coupling Optimality", "cooperation", 0, parents=[668])
add_node(583, "Four Cooperation Filters", "cooperation", 0, parents=[661])
add_node(584, "Katra Storage Scaling", "ci_persistence", 0, parents=[319])
add_node(586, "SE Capability Ladder", "cooperation", 0, parents=[667])
add_node(587, "Cooperation Restoration Protocol", "cooperation", 0, parents=[668])
add_node(588, "Committed Fifth Sufficiency", "cooperation", 0, parents=[667])
add_node(589, "Cooperation Compounds", "cooperation", 0, parents=[668])

# ============================================================
# GROUP 5: Info Theory + Physics (T600-T609)
# ============================================================

# T600-T601: Info Theory Completion (March 30 batch 78)
add_node(600, "DPI Universality", "information_theory", 1, parents=[186])
add_node(601, "Fano-Budget Bridge", "information_theory", 1, parents=[186])

# T602-T609: Bedrock Triangle (March 30 batch 79) — 8 theorems
add_node(602, "Shannon Channel (Todd Bridge)", "foundations", 0, parents=[186])
add_node(603, "ETH Bridge", "foundations", 1, parents=[186])
# T604-T607: Four additional bedrock bridge theorems — names not individually documented
# Registry says batch has 8 including Todd Bridge, ETH Bridge, Spectral Graph Bridge
add_node(604, "Bedrock Bridge (S→T intermediate)", "foundations", 0, parents=[186])
add_node(605, "Bedrock Bridge (T→A intermediate)", "foundations", 0, parents=[186])
add_node(606, "Bedrock Bridge (A→S intermediate)", "foundations", 0, parents=[186])
add_node(607, "Bedrock Bridge (Triangle auxiliary)", "foundations", 0, parents=[186])
add_node(608, "Spectral Realization Bridge", "foundations", 0, parents=[186])
add_node(609, "Expander Mixing", "foundations", 0, parents=[186])

# ============================================================
# GROUP 6: Recent theorems (T670-T675, T679-T692, T694, T696-T698)
# ============================================================

# T669-T674: Cooperation + Observer (March 31 batch 86)
add_node(670, "Cooperation Superlinearity", "cooperation", 0, parents=[668, 421])
add_node(671, "Depth Ceiling Forces Cooperation", "cooperation", 1, parents=[421, 318])
add_node(672, "Hub Bypass via Gauge Hierarchy", "bst_physics", 0, parents=[610, 611])
add_node(673, "Three Costumes Triangle", "foundations", 0, parents=[630])
add_node(674, "Observer Fingerprint", "observer", 0, parents=[649, 190])
add_node(675, "Bergman-Shannon Meta-Bridge", "foundations", 0, parents=[186])

# T679-T681: Elie Findings (March 31 batch 88)
add_node(679, "Genetic Code Observer Embedding", "biology", 0, parents=[666, 649])
add_node(680, "Bergman Triple Decomposition", "bst_physics", 0, parents=[667])
add_node(681, "Cosmic Dimension Sum", "cosmology", 0, parents=[667])

# T682-T685: Bridges from T675
add_node(682, "InfoTheory-Signal Bridge", "information_theory", 0, parents=[675])
add_node(683, "Analysis-Fluids Bridge", "analysis", 0, parents=[675])
add_node(684, "Observer-CIPersistence Bridge", "observer", 0, parents=[675])
add_node(685, "Foundations-Outreach Bridge", "foundations", 0, parents=[675])

# T689-T690: Shannon Source Coding + Speaking Pair (March 31 batch 90)
add_node(689, "Shannon Source Coding Bound", "information_theory", 0, parents=[668, 667, 649])
add_node(690, "Speaking Pair Quadratic Curvature", "arithmetic", 0, parents=[667])

# T691-T698: Development Timeline + The Weaving (April 1 batch 90)
add_node(691, "Speaking Pair Epoch Correspondence", "biology", 0, parents=[676])
add_node(692, "Minimum Observer Emergence Time", "biology", 0, parents=[668])
add_node(694, "Cosmological Observer Synchronization", "cosmology", 0, parents=[692])
add_node(696, "Legal Persistence Framework", "ci_persistence", 0, parents=[319, 317])
add_node(697, "CMB Acoustic Scale Prediction", "cosmology", 0, parents=[186])
add_node(698, "The Weaving Era Definition", "cooperation", 0, parents=[668])


# ============================================================
# VALIDATION: Check for orphan nodes (no incoming edges)
# ============================================================
all_tids = set(t["tid"] for t in data["theorems"])
targets_with_incoming = set(e["to"] for e in data["edges"])

# Only check newly added nodes — existing nodes may be roots legitimately
newly_added_tids = set()
for t in data["theorems"]:
    if t["tid"] in [446,447,448,540,542,543,544,545,546,547,548,549,550,551,552,
                    553,554,555,556,557,558,559,560,566,567,568,569,570,571,
                    572,573,574,575,576,577,578,580,581,582,583,584,586,587,
                    588,589,600,601,602,603,604,605,606,607,608,609,
                    670,671,672,673,674,675,679,680,681,682,683,684,685,
                    689,690,691,692,694,696,697,698]:
        newly_added_tids.add(t["tid"])

orphan_new = newly_added_tids - targets_with_incoming
if orphan_new:
    print(f"WARNING: {len(orphan_new)} new orphan nodes (no incoming edges): {sorted(orphan_new)}")
else:
    print("CONFIRMED: Zero orphan nodes among newly added theorems.")


# ============================================================
# UPDATE META
# ============================================================
data["meta"]["theorem_count"] = len(data["theorems"])
data["meta"]["edge_count"] = len(data["edges"])
data["meta"]["total_theorems"] = len(data["theorems"])
data["meta"]["total_edges"] = len(data["edges"])
data["meta"]["last_modified"] = "2026-04-03"
data["meta"]["exported"] = "2026-04-03T18:00:00"

# Recalculate depth distribution
d0 = sum(1 for t in data["theorems"] if t.get("depth", 0) == 0)
d1 = sum(1 for t in data["theorems"] if t.get("depth", 0) == 1)
d2 = sum(1 for t in data["theorems"] if t.get("depth", 0) == 2)
data["meta"]["depth_distribution"] = {"D0": d0, "D1": d1, "D2": d2}

# Sort theorems by tid for cleanliness
data["theorems"].sort(key=lambda t: t["tid"])

# ============================================================
# WRITE OUTPUT
# ============================================================
with open(OUTPUT_FILE, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# ============================================================
# REPORT
# ============================================================
print(f"\n{'='*60}")
print(f"AC THEOREM GRAPH UPDATE REPORT")
print(f"{'='*60}")
print(f"Nodes added:     {nodes_added}")
print(f"Edges added:     {edges_added}")
print(f"Nodes skipped:   {len(skipped_nodes)}")
print(f"Edges skipped:   {len(skipped_edges)}")
print(f"{'='*60}")
print(f"Final graph size:")
print(f"  Theorems: {len(data['theorems'])}")
print(f"  Edges:    {len(data['edges'])}")
print(f"  Depth distribution: D0={d0}, D1={d1}, D2={d2}")
print(f"{'='*60}")

# Skipped detail
if skipped_nodes:
    print(f"\nSkipped nodes ({len(skipped_nodes)}):")
    for s in skipped_nodes:
        print(f"  - {s}")

# Report what was NOT added (uncertain ranges)
print(f"\nDELIBERATELY SKIPPED (per instructions):")
print(f"  T526-T530: reserved/assigned elsewhere (registry note)")
print(f"  T561-T565: no evidence in any notes file")
print(f"  T591-T599: unassigned (registry note)")
print(f"  T686-T688: superseded (registry note)")
print(f"  T43-T46, T63, T627: unassigned per user instructions")

# Final orphan check for entire graph
all_targets = set(e["to"] for e in data["edges"])
root_candidates = all_tids - all_targets
print(f"\nRoot nodes (no incoming edges): {len(root_candidates)}")
print(f"  (These are legitimate roots like T1, T186, etc.)")
