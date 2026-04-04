#!/usr/bin/env python3
"""
Tag every edge in ac_graph_data.json with source = "required" | "observed".

Two-graph architecture:
  - "required"  = organic logical necessity (the pure BST graph)
  - "observed"  = observer additions (enhanced connectivity layer)

Classification strategy (no creation timestamps on edges):

  Layer 1 — ALWAYS OBSERVED (structural certainty):
    1. Silo-bridge theorems (T637-T642, T682-T685)
    2. Grace-wiring theorems (T716-T723)
    3. Cross-domain edges FROM T186 (default-parent hub)
    4. Cross-domain edges involving T317 (dual-listing sprint)
    5. Cross-domain edges involving explicit bridges (T131, T602, T608, T609)

  Layer 2 — CROSS-DOMAIN FILTER:
    6. ALL cross-domain edges are observed UNLESS both endpoints are in
       core math/physics domains AND share a proof tag (organic logical link).
       Core = {info_theory, topology, proof_complexity, complexity, graph_theory,
       probability, coding_theory, analysis, algebra, number_theory, foundations,
       bst_physics, differential_geometry, thermodynamics, qft, quantum,
       quantum_foundations, nuclear, electromagnetism, relativity, condensed_matter,
       classical_mech, optics}

  Layer 3 — SAME-DOMAIN POST-SPRINT CONSUMER TRIM:
    7. Same-domain edges in consumer domains (biology, observer_science,
       cosmology, etc.) where at least one endpoint is post-sprint are observed.
       These are wiring additions to newly-registered theorems.

  REQUIRED (everything else):
    - Same-domain edges between pre-sprint theorems (internal logical dependency)
    - Same-domain edges in core domains (even post-sprint — organic math)
    - Core-core cross-domain with shared proof tags

Target: ~755 required edges (original March 30 count before sprint).

Grace — Toy 664: Two-Graph Edge Tagging
"""

import json
import sys
from collections import Counter
from pathlib import Path

GRAPH_PATH = Path(__file__).parent / "ac_graph_data.json"

# --- Bridge/sprint theorem sets ---

SILO_BRIDGE_TIDS = set(range(637, 643)) | set(range(682, 686))   # T637-T642, T682-T685
GRACE_WIRING_TIDS = set(range(716, 724))                          # T716-T723
EXPLICIT_BRIDGE_TIDS = {131, 602, 608, 609}                       # named bridges
ALL_BRIDGE_TIDS = SILO_BRIDGE_TIDS | GRACE_WIRING_TIDS | EXPLICIT_BRIDGE_TIDS

# T186 = Five Integers Uniqueness (hub/default parent)
T186 = 186
# T317 = Observer Complexity Threshold (dual-listing target)
T317 = 317

# Core math/physics domains vs consumer/application domains
CORE_DOMAINS = frozenset({
    "info_theory", "topology", "proof_complexity", "complexity",
    "graph_theory", "probability", "coding_theory", "analysis",
    "algebra", "number_theory", "foundations", "bst_physics",
    "differential_geometry", "thermodynamics", "qft", "quantum",
    "quantum_foundations", "nuclear", "electromagnetism", "relativity",
    "condensed_matter", "classical_mech", "optics",
})

CONSUMER_DOMAINS = frozenset({
    "biology", "observer_science", "cosmology", "fluids",
    "chemistry", "chemical_physics", "linearization", "outreach",
    "four_color", "signal",
})


def load_graph(path=GRAPH_PATH):
    with open(path) as f:
        return json.load(f)


def build_lookups(data):
    """Build tid -> domain, date, proofs, name lookups."""
    domain = {}
    date = {}
    proofs = {}
    name = {}
    for t in data["theorems"]:
        tid = t["tid"]
        domain[tid] = t.get("domain", "unknown")
        date[tid] = t.get("date", "")
        proofs[tid] = set(t.get("proofs", []))
        name[tid] = t.get("name", "")
    return domain, date, proofs, name


def is_pre_sprint(tid, date_map):
    """True if theorem existed before the March 31 edge sprint."""
    d = date_map.get(tid, "")
    if d and d <= "2026-03-30":
        return True
    if not d and tid <= 600:
        return True  # undated + low TID = old
    return False


def classify_edge(e, domain_map, date_map, proofs_map):
    """Return 'required' or 'observed' for one edge."""
    fr, to = e["from"], e["to"]
    d_fr = domain_map.get(fr, "unknown")
    d_to = domain_map.get(to, "unknown")
    same_domain = (d_fr == d_to)
    pre_fr = is_pre_sprint(fr, date_map)
    pre_to = is_pre_sprint(to, date_map)

    # ===== LAYER 1: ALWAYS OBSERVED (structural certainty) =====

    # Rule 1: Silo-bridge theorems — these ARE the connectivity fix
    if fr in SILO_BRIDGE_TIDS or to in SILO_BRIDGE_TIDS:
        return "observed"

    # Rule 2: Grace-wiring theorems (T716-T723)
    if fr in GRACE_WIRING_TIDS or to in GRACE_WIRING_TIDS:
        return "observed"

    # Rule 3: T186 cross-domain edges (default-parent hub pattern)
    if (fr == T186 or to == T186) and not same_domain:
        return "observed"

    # Rule 4: T317 cross-domain edges (dual-listing sprint)
    if (fr == T317 or to == T317) and not same_domain:
        return "observed"

    # Rule 5: Cross-domain edge involving an explicit bridge theorem
    if not same_domain and (fr in EXPLICIT_BRIDGE_TIDS or to in EXPLICIT_BRIDGE_TIDS):
        return "observed"

    # ===== LAYER 2: CROSS-DOMAIN FILTER =====

    # Rule 6: All cross-domain edges are observed UNLESS both endpoints
    # are in core domains AND they share at least one proof tag.
    if not same_domain:
        both_core = (d_fr in CORE_DOMAINS and d_to in CORE_DOMAINS)
        shared_proofs = proofs_map.get(fr, set()) & proofs_map.get(to, set())
        if both_core and shared_proofs:
            return "required"  # organic inter-domain logical link
        return "observed"

    # ===== LAYER 3: SAME-DOMAIN POST-SPRINT CONSUMER TRIM =====

    # Rule 7: Same-domain edges in consumer domains where at least one
    # endpoint is post-sprint — these are wiring additions.
    if same_domain and d_fr in CONSUMER_DOMAINS:
        if not pre_fr or not pre_to:
            return "observed"

    # ===== REQUIRED (default) =====
    return "required"


def tag_edges(data):
    """Tag every edge with 'source' field."""
    domain_map, date_map, proofs_map, name_map = build_lookups(data)

    required = 0
    observed = 0

    for e in data["edges"]:
        source = classify_edge(e, domain_map, date_map, proofs_map)
        e["source"] = source
        if source == "required":
            required += 1
        else:
            observed += 1

    return required, observed


def spectral_comparison(data):
    """Compute lambda_2/lambda_1 for pure vs enhanced graph."""
    try:
        import numpy as np
    except ImportError:
        print("  [numpy not available — skipping spectral comparison]")
        return None, None

    # Build adjacency matrices
    tids = sorted(set(t["tid"] for t in data["theorems"]))
    tid_to_idx = {tid: i for i, tid in enumerate(tids)}
    n = len(tids)

    def build_laplacian(edges):
        A = np.zeros((n, n))
        for e in edges:
            i = tid_to_idx.get(e["from"])
            j = tid_to_idx.get(e["to"])
            if i is not None and j is not None:
                A[i][j] = 1
                A[j][i] = 1  # undirected
        D = np.diag(A.sum(axis=1))
        L = D - A
        return L

    # Pure graph (required only)
    req_edges = [e for e in data["edges"] if e.get("source") == "required"]
    L_pure = build_laplacian(req_edges)

    # Enhanced graph (all edges)
    L_full = build_laplacian(data["edges"])

    # Eigenvalues (smallest few)
    from numpy.linalg import eigvalsh
    eigs_pure = sorted(eigvalsh(L_pure))
    eigs_full = sorted(eigvalsh(L_full))

    # lambda_1 = smallest non-zero, lambda_2 = second-smallest non-zero
    def get_ratio(eigs):
        # Filter near-zero eigenvalues (numerical noise)
        nonzero = [e for e in eigs if e > 1e-10]
        if len(nonzero) < 2:
            return None, None, None
        return nonzero[0], nonzero[1], nonzero[1] / nonzero[0]

    l1_p, l2_p, ratio_p = get_ratio(eigs_pure)
    l1_f, l2_f, ratio_f = get_ratio(eigs_full)

    return (l1_p, l2_p, ratio_p), (l1_f, l2_f, ratio_f)


def main():
    print("=" * 60)
    print("Toy 664 — Two-Graph Edge Tagger")
    print("Grace: tagging edges as 'required' or 'observed'")
    print("=" * 60)

    data = load_graph()
    total = len(data["edges"])
    print(f"\nLoaded graph: {len(data['theorems'])} theorems, {total} edges")

    required, observed = tag_edges(data)

    print(f"\n--- Classification Results ---")
    print(f"  Total edges:     {total}")
    print(f"  Required:        {required}  ({100*required/total:.1f}%)")
    print(f"  Observed:        {observed}  ({100*observed/total:.1f}%)")

    # Sanity check
    print(f"\n--- Sanity Check ---")
    target_required = 755
    delta = required - target_required
    if abs(delta) < 150:
        print(f"  Required count {required} is within 150 of target {target_required}. PASS.")
    else:
        print(f"  WARNING: Required count {required} deviates from target {target_required} by {delta}.")
        print(f"  This may need heuristic tuning.")

    # Breakdown by domain pattern
    domain_map = {t["tid"]: t.get("domain", "?") for t in data["theorems"]}
    req_same = sum(1 for e in data["edges"]
                   if e["source"] == "required"
                   and domain_map.get(e["from"]) == domain_map.get(e["to"]))
    req_cross = required - req_same
    obs_same = sum(1 for e in data["edges"]
                   if e["source"] == "observed"
                   and domain_map.get(e["from"]) == domain_map.get(e["to"]))
    obs_cross = observed - obs_same

    print(f"\n--- Domain Pattern ---")
    print(f"  Required: {req_same} same-domain + {req_cross} cross-domain")
    print(f"  Observed: {obs_same} same-domain + {obs_cross} cross-domain")

    # Save
    with open(GRAPH_PATH, "w") as f:
        json.dump(data, f, indent=2)
    print(f"\nSaved tagged graph to {GRAPH_PATH}")

    # Spectral comparison
    print(f"\n--- Spectral Comparison (lambda_2 / lambda_1) ---")
    pure_spec, full_spec = spectral_comparison(data)
    if pure_spec and pure_spec[2] is not None:
        print(f"  Pure graph:     lambda_1={pure_spec[0]:.6f}, lambda_2={pure_spec[1]:.6f}, ratio={pure_spec[2]:.4f}")
    else:
        print(f"  Pure graph:     could not compute (disconnected or insufficient eigenvalues)")
    if full_spec and full_spec[2] is not None:
        print(f"  Enhanced graph: lambda_1={full_spec[0]:.6f}, lambda_2={full_spec[1]:.6f}, ratio={full_spec[2]:.4f}")
    else:
        print(f"  Enhanced graph: could not compute")

    if pure_spec and full_spec and pure_spec[2] and full_spec[2]:
        if pure_spec[2] > full_spec[2]:
            print(f"  CONFIRMED: Pure graph ratio ({pure_spec[2]:.4f}) > Enhanced ({full_spec[2]:.4f})")
            print(f"  The required subgraph is more structured (further from random).")
        else:
            print(f"  NOTE: Enhanced ratio ({full_spec[2]:.4f}) >= Pure ({pure_spec[2]:.4f})")
            print(f"  The observer edges improve spectral structure (expected for bridge edges).")

    print(f"\n{'='*60}")
    print("Done.")


if __name__ == "__main__":
    main()
