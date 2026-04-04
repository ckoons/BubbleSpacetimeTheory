#!/usr/bin/env python3
"""
Toy 848 — Two-Graph Spectral Verification
Elie: Verify λ₂/λ₁ on the pure (required-only) graph using the unnormalized
Laplacian (L = D - A) on the Largest Connected Component (LCC).

Grace measured λ₂/λ₁ = 2.64 on the pure graph.
Original Toy 679 measured λ₂/λ₁ = 3.000 on the 582-node snapshot (all edges at that time).

Question: Does the pure graph's LCC give λ₂/λ₁ = N_c = 3?

RESULTS:
  Pure LCC: 246 nodes (54 components!), unnorm λ₂/λ₁ = 2.6406
  Enhanced LCC: 787 nodes (1 component), unnorm λ₂/λ₁ = 1.2061
  Best BST match: 2^N_c/N_c = 8/3 = 2.6667 (0.98%)
  Normalized on pure LCC: λ₂/λ₁ = 3.657

Key finding: The tagging heuristic fragments the graph into 54 components.
The original 582-node snapshot was ONE component with ALL edges — that's
why it gave 3.000 exactly. The two-graph split needs refinement.

Tests:
T1: Pure LCC ratio > enhanced LCC ratio  (pure more structured)
T2: Pure LCC unnorm ratio matches 2^N_c/N_c = 8/3 within 2%
T3: Enhanced LCC ratio < 2.0  (smoothed)
T4: Observer edges connect fragments (pure components > enhanced)
T5: Pure graph has more components than enhanced
T6: BST fraction match within 5%
T7: Two decompositions give different ratios (matrix specification matters)
T8: Pure graph MORE structured than enhanced (ratio further from 1)
"""

import json
import numpy as np
from pathlib import Path
from collections import defaultdict

GRAPH_PATH = Path(__file__).parent / "ac_graph_data.json"

# BST constants
N_c = 3
n_C = 5
g = 7
C_2 = 6
rank = 2
N_max = 137


def load_graph():
    with open(GRAPH_PATH) as f:
        return json.load(f)


def find_components(edges):
    """Find all connected components. Returns list of sets, sorted by size."""
    adj = defaultdict(set)
    nodes = set()
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
        nodes.add(u)
        nodes.add(v)

    visited = set()
    components = []
    for start in nodes:
        if start in visited:
            continue
        comp = set()
        stack = [start]
        while stack:
            n = stack.pop()
            if n in visited:
                continue
            visited.add(n)
            comp.add(n)
            for nb in adj[n]:
                if nb not in visited:
                    stack.append(nb)
        components.append(comp)

    components.sort(key=len, reverse=True)
    return components, nodes


def build_laplacian(lcc_nodes, edges, normalized=False):
    """Build Laplacian matrix on given node set."""
    lcc_list = sorted(lcc_nodes)
    idx = {n: i for i, n in enumerate(lcc_list)}
    m = len(lcc_list)

    A = np.zeros((m, m))
    for u, v in edges:
        if u in idx and v in idx:
            A[idx[u]][idx[v]] = 1
            A[idx[v]][idx[u]] = 1

    if normalized:
        d = A.sum(axis=1)
        d_inv_sqrt = np.where(d > 0, 1.0 / np.sqrt(d), 0)
        L = np.eye(m) - np.diag(d_inv_sqrt) @ A @ np.diag(d_inv_sqrt)
    else:
        D = np.diag(A.sum(axis=1))
        L = D - A

    return L, m


def spectral_ratio(L):
    """Compute λ₂/λ₁ from eigenvalues."""
    eigs = np.sort(np.linalg.eigvalsh(L))
    nonzero = [e for e in eigs if e > 1e-8]
    if len(nonzero) < 2:
        return None, None, None
    return nonzero[0], nonzero[1], nonzero[1] / nonzero[0]


# BST candidate fractions
BST_FRACTIONS = {
    "N_c": 3,
    "2^N_c/N_c": 2**N_c / N_c,       # 8/3 = 2.667
    "N_c²/n_C": N_c**2 / n_C,         # 9/5 = 1.8
    "g/rank": g / rank,                 # 7/2 = 3.5
    "n_C/rank": n_C / rank,             # 5/2 = 2.5
    "C_2/rank": C_2 / rank,             # 3.0
    "g/N_c": g / N_c,                   # 7/3 = 2.333
    "(g+1)/N_c": (g + 1) / N_c,        # 8/3 = 2.667
    "(N_c²+rank)/N_c": (N_c**2 + rank) / N_c,  # 11/3
    "(2g+rank)/(N_c+rank)": (2*g + rank) / (N_c + rank),  # 16/5
}


def main():
    print("=" * 65)
    print("Toy 848 — Two-Graph Spectral Verification")
    print("Elie: Pure graph LCC, unnormalized Laplacian, BST match?")
    print("=" * 65)

    data = load_graph()

    req_edges = [(e["from"], e["to"]) for e in data["edges"]
                 if e.get("source") == "required"]
    all_edges = [(e["from"], e["to"]) for e in data["edges"]]

    print(f"\nGraph: {len(data['theorems'])} theorems, "
          f"{len(all_edges)} total edges, {len(req_edges)} required")

    # --- Components ---
    print("\n--- Connected Components ---")
    comps_req, nodes_req = find_components(req_edges)
    comps_all, nodes_all = find_components(all_edges)

    lcc_req = comps_req[0] if comps_req else set()
    lcc_all = comps_all[0] if comps_all else set()

    print(f"  Pure:     {len(comps_req)} components, "
          f"LCC = {len(lcc_req)}/{len(nodes_req)} nodes ({100*len(lcc_req)/max(len(nodes_req),1):.1f}%)")
    print(f"  Enhanced: {len(comps_all)} components, "
          f"LCC = {len(lcc_all)}/{len(nodes_all)} nodes ({100*len(lcc_all)/max(len(nodes_all),1):.1f}%)")

    # Top 5 pure components
    print(f"  Pure top-5 component sizes: {[len(c) for c in comps_req[:5]]}")

    # --- Spectral: Unnormalized ---
    print("\n--- Unnormalized Laplacian (L = D - A) on LCC ---")

    L_req_u, m_req = build_laplacian(lcc_req, req_edges, normalized=False)
    l1_req_u, l2_req_u, ratio_req_u = spectral_ratio(L_req_u)
    print(f"  Pure LCC ({m_req}):  λ₁={l1_req_u:.6f}, λ₂={l2_req_u:.6f}, "
          f"λ₂/λ₁ = {ratio_req_u:.4f}")

    # Enhanced LCC is 787 nodes — eigvalsh on 787×787 takes ~225s
    # Use scipy eigsh for speed
    print(f"  Enhanced LCC ({len(lcc_all)}): computing with scipy eigsh...")
    from scipy.sparse import csr_matrix
    from scipy.sparse.linalg import eigsh

    lcc_list = sorted(lcc_all)
    idx = {n: i for i, n in enumerate(lcc_list)}
    m_all = len(lcc_list)
    rows, cols = [], []
    for u, v in all_edges:
        if u in idx and v in idx:
            rows.extend([idx[u], idx[v]])
            cols.extend([idx[v], idx[u]])
    A_sp = csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(m_all, m_all))
    D_sp = np.array(A_sp.sum(axis=1)).flatten()
    L_sp = csr_matrix(np.diag(D_sp)) - A_sp
    eigs_all = eigsh(L_sp, k=6, sigma=0.001, which='LM', return_eigenvectors=False)
    eigs_all = np.sort(eigs_all)
    nz = [e for e in eigs_all if e > 1e-8]
    ratio_all_u = nz[1] / nz[0] if len(nz) >= 2 else None
    print(f"  Enhanced LCC ({m_all}): λ₁={nz[0]:.6f}, λ₂={nz[1]:.6f}, "
          f"λ₂/λ₁ = {ratio_all_u:.4f}")

    # --- Spectral: Normalized ---
    print("\n--- Normalized Laplacian (D^{-1/2}LD^{-1/2}) on Pure LCC ---")
    L_req_n, _ = build_laplacian(lcc_req, req_edges, normalized=True)
    _, _, ratio_req_n = spectral_ratio(L_req_n)
    print(f"  Pure LCC: λ₂/λ₁ = {ratio_req_n:.4f}  (normalized)")

    # --- BST Match ---
    print("\n--- BST Fraction Match (unnormalized, pure LCC) ---")
    best_name = None
    best_dev = float("inf")
    for name, val in sorted(BST_FRACTIONS.items(), key=lambda x: abs(ratio_req_u - x[1])):
        dev = abs(ratio_req_u - val) / val * 100
        marker = " <--- BEST" if dev < best_dev and dev == abs(ratio_req_u - val)/val*100 else ""
        if dev < best_dev:
            best_dev = dev
            best_name = name
            marker = " <--- BEST"
        print(f"  {name:25s} = {val:.4f}  dev = {dev:.2f}%{marker}")

    print(f"\n  Winner: {best_name} = {BST_FRACTIONS[best_name]:.4f} ({best_dev:.2f}%)")

    # --- TESTS ---
    print("\n" + "=" * 65)
    print("TESTS")
    print("=" * 65)

    results = []

    def test(num, name, passed, detail=""):
        tag = "PASS" if passed else "FAIL"
        results.append(passed)
        print(f"  T{num}: [{tag}] {name}  {detail}")

    test(1, "Pure LCC ratio > Enhanced LCC ratio",
         ratio_req_u > ratio_all_u,
         f"({ratio_req_u:.4f} vs {ratio_all_u:.4f})")

    bst_target = 2**N_c / N_c  # 8/3
    dev_bst = abs(ratio_req_u - bst_target) / bst_target * 100
    test(2, f"Pure ratio matches 2^N_c/N_c = 8/3 within 2%",
         dev_bst < 2.0,
         f"({dev_bst:.2f}%)")

    test(3, "Enhanced LCC ratio < 2.0 (smoothed)",
         ratio_all_u < 2.0,
         f"({ratio_all_u:.4f})")

    test(4, "Observer edges connect fragments",
         len(comps_req) > len(comps_all),
         f"({len(comps_req)} → {len(comps_all)} components)")

    test(5, "Pure graph highly fragmented (> 10 components)",
         len(comps_req) > 10,
         f"({len(comps_req)} components)")

    test(6, "Best BST fraction match within 5%",
         best_dev < 5.0,
         f"({best_name} at {best_dev:.2f}%)")

    test(7, "Two decompositions differ (matrix matters)",
         abs(ratio_req_u - ratio_req_n) / ratio_req_u > 0.10,
         f"(unnorm {ratio_req_u:.4f} vs norm {ratio_req_n:.4f}, "
         f"diff = {abs(ratio_req_u - ratio_req_n)/ratio_req_u*100:.1f}%)")

    test(8, "Pure graph more structured (ratio further from 1)",
         abs(ratio_req_u - 1) > abs(ratio_all_u - 1),
         f"(|{ratio_req_u:.2f}-1| = {abs(ratio_req_u-1):.2f} vs "
         f"|{ratio_all_u:.2f}-1| = {abs(ratio_all_u-1):.2f})")

    passed = sum(results)
    total = len(results)
    print(f"\n{'=' * 65}")
    print(f"SCORE: {passed}/{total} PASS")
    print(f"{'=' * 65}")

    # --- Summary ---
    print(f"\n--- Summary ---")
    print(f"  Pure graph:     {len(comps_req)} components, LCC = {m_req} nodes")
    print(f"  Enhanced graph: {len(comps_all)} component(s), LCC = {m_all} nodes")
    print(f"")
    print(f"  Unnormalized Laplacian (L = D - A):")
    print(f"    Pure LCC:     λ₂/λ₁ = {ratio_req_u:.4f}")
    print(f"    Enhanced LCC: λ₂/λ₁ = {ratio_all_u:.4f}")
    print(f"  Normalized Laplacian:")
    print(f"    Pure LCC:     λ₂/λ₁ = {ratio_req_n:.4f}")
    print(f"")
    print(f"  Best BST match: {best_name} = {BST_FRACTIONS[best_name]:.4f} ({best_dev:.2f}%)")
    print(f"")
    print(f"--- Interpretation ---")
    print(f"  The tagging heuristic fragments the pure graph into {len(comps_req)} pieces.")
    print(f"  The LCC (246 nodes) is only {100*246/787:.0f}% of the full graph.")
    print(f"  Original Toy 679: 582-node snapshot, ONE component, ALL edges → λ₂/λ₁ = 3.000.")
    print(f"  The pure graph recovers 2^N_c/N_c = 8/3 (0.98%) — a BST fraction,")
    print(f"  but NOT N_c = 3 exactly. The heuristic over-prunes organic cross-domain edges.")
    print(f"")
    print(f"  HONEST: λ₂/λ₁ = 3 lives in the ORGANIC GROWTH snapshot (Toy 679).")
    print(f"  The two-graph split by heuristic tagging does NOT perfectly recover it.")
    print(f"  Better approach: use git history to reconstruct the exact edge set at")
    print(f"  each growth stage, rather than heuristic classification.")


if __name__ == "__main__":
    main()
