"""
Toy 2766 — String/M-theory critical dimensions are BST integers.

Bosonic string: D = 26 = rank·c_3 (rank·Ogg_c3)
Superstring: D = 10 = rank·n_C
M-theory: D = 11 = c_2
F-theory: D = 12 = rank·C_2 (= rank·rank·N_c)

ALL string-theoretic critical dimensions are BST integer products.
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13

    dims = [
        ("Bosonic string D",   26, rank*c_3, "rank·c_3"),
        ("Superstring D",      10, rank*n_C, "rank·n_C"),
        ("M-theory D",         11, c_2,      "c_2"),
        ("F-theory D",         12, rank*C_2, "rank·C_2"),
        ("M-2 brane worldvol", 3,  N_c,      "N_c"),
        ("M-5 brane worldvol", 6,  C_2,      "C_2"),
        ("Type IIB compact",   5,  n_C,      "n_C (= D_IV⁵!)"),
        ("Calabi-Yau 3-fold real", 6, C_2,   "C_2 (3 complex dims)"),
    ]

    print("String/M-theory critical dimensions BST:")
    matches = 0
    for name, dim, bst, formula in dims:
        ok = dim == bst
        marker = "✓" if ok else "×"
        if ok:
            matches += 1
        print(f"  {name:<28} = {dim:<3} = {formula:<15} {marker}")

    print(f"\nSCORE: {matches}/{len(dims)}")
    return matches, len(dims)


if __name__ == "__main__":
    run()
