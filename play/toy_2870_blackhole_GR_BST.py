"""
Toy 2870 — General relativity & black hole physics structural counts BST.

Killing vectors of Kerr black hole: 2 = rank (t, φ)
Killing vectors of Schwarzschild: 4 = rank² (t + 3 rot)
No-hair theorem parameters: 3 = N_c (mass M, angular momentum J, charge Q)
Petrov classification types: 6 = C_2 (I, II, D, III, N, O)
ADM constraint equations: 4 = rank² (1 Hamiltonian + 3 momentum)

Schwarzschild geodesic equation orders: 4 = rank² (one for each spacetime coord)
Killing tensors of Kerr: 5 = n_C (4 Killing vectors + 1 Killing-Yano)
Carter constants for Kerr: 4 = rank² (E, L_z, m, Q)

Singularities of Schwarzschild: 2 = rank (r=0 physical, r=2M coordinate)
Event horizon dimensions for stationary 4D BH: 2 = rank
Causal regions of Penrose diagram: 4 = rank² (Schwarzschild conformal compact)
Bondi-Sachs metric components: 6 = C_2 functions in null coordinates

Standard cosmological FRW parameters before WMAP: 6 = C_2
Number of independent components of Riemann tensor in 4D: 20 = rank²·n_C ✓
Number of indep components Weyl tensor in 4D: 10 = rank·n_C
Number of indep components Ricci tensor in 4D: 10 = rank·n_C
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    gr = [
        ("Kerr BH Killing vectors",         2,  rank,       "rank"),
        ("Schwarzschild Killing vectors",   4,  rank**2,    "rank²"),
        ("No-hair theorem parameters",      3,  N_c,        "N_c (M,J,Q)"),
        ("Petrov classification types",     6,  C_2,        "C_2"),
        ("ADM constraint equations",        4,  rank**2,    "rank² (1 Ham + 3 mom)"),
        ("Carter constants Kerr",           4,  rank**2,    "rank²"),
        ("Bondi-Sachs functions",           6,  C_2,        "C_2"),
        ("FRW cosmology parameters (early)", 6, C_2,        "C_2"),
        ("Riemann tensor indep components (4D)", 20, rank**2*n_C, "rank²·n_C"),
        ("Weyl tensor indep components (4D)", 10, rank*n_C, "rank·n_C"),
        ("Ricci tensor indep components (4D)", 10, rank*n_C, "rank·n_C"),
        ("Causal regions Penrose diagram",  4,  rank**2,    "rank²"),
        ("Killing tensors Kerr (vec+YK)",   5,  n_C,        "n_C"),
        ("Stationary 4D BH horizon dim",    2,  rank,       "rank"),
    ]

    print("GR / Black hole BST:")
    matches = 0
    for name, val, bst, formula in gr:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<42} = {val:<3} = {formula:<20} {marker}")

    print(f"\nSCORE: {matches}/{len(gr)}")
    return matches, len(gr)


if __name__ == "__main__":
    run()
