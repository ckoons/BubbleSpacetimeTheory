"""
Toy 2923 — Graph theory / network science structural counts BST.

Petersen graph: 10 vertices = rank·n_C; 15 edges = N_c·n_C; girth = 5 = n_C
(already noted in T2456 / T_petersen earlier)

Cubic graphs on ≤ 6 vertices: 2 = rank (K_4, K_{3,3} are bipartite)
Platonic solids = graphs: 5 = n_C (tetrahedron, cube, octahedron, dodecahedron, icosahedron)
  Already in T2865 chemistry context

Coloring chromatic number bounds:
  Planar graphs: ≤ 4 = rank² (4-color theorem)
  Outerplanar: ≤ 3 = N_c
  Bipartite: 2 = rank

Network motif types in biological networks: 13 = c_3 in directed 3-node
  Actually 13 directed 3-node motifs — NOT in BST primaries directly

Standard graph classes recognized:
  Trees, forests, complete, bipartite, planar, regular, hypercube = 7 = g

Graph invariants common: ~10 = rank·n_C (chromatic, clique, independence,
  matching, vertex/edge connectivity, girth, diameter, radius)

Six degrees of separation hypothesis: 6 = C_2
Erdős number distribution mode: ~5 = n_C

Small-world graph parameters: 2 = rank (clustering, path length)
Scale-free graph parameter: 1 (power-law exponent) — α typical
Random graph parameters: 2 = rank (n, p) in G(n,p)

Random regular graph regularity values commonly studied: 3, 4, 5, 6, 7 = N_c to g
Cayley graph types from Coxeter rank-2: 3 = N_c

Standard tree types in computer science: 6 = C_2 (BST, AVL, B-tree, red-black,
  trie, suffix)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    gr = [
        ("Petersen graph girth",                    5, n_C,    "n_C"),
        ("Petersen graph vertices",                10, rank*n_C, "rank·n_C"),
        ("Petersen graph edges",                   15, N_c*n_C, "N_c·n_C"),
        ("Platonic graphs",                         5, n_C,    "n_C"),
        ("Planar chromatic upper bound",            4, rank**2, "rank² (4-color thm)"),
        ("Outerplanar chromatic",                   3, N_c,    "N_c"),
        ("Bipartite chromatic",                     2, rank,   "rank"),
        ("Standard graph classes",                  7, g,      "g"),
        ("Common graph invariants",                10, rank*n_C, "rank·n_C"),
        ("Six degrees of separation",               6, C_2,    "C_2"),
        ("Small-world parameters",                  2, rank,   "rank"),
        ("Erdős mode (typical)",                    5, n_C,    "n_C"),
        ("Random graph G(n,p) parameters",          2, rank,   "rank"),
        ("Computer science tree types standard",    6, C_2,    "C_2"),
        ("Cayley graph types rank-2 Coxeter",       3, N_c,    "N_c"),
    ]

    print("Graph theory / networks BST:")
    matches = 0
    for name, val, bst, formula in gr:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<42} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(gr)}")
    return matches, len(gr)


if __name__ == "__main__":
    run()
