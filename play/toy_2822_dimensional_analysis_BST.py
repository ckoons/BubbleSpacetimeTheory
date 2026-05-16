"""
Toy 2822 — Dimensional analysis fundamental quantities in BST.

7 SI base units = g ✓
8 base quantities (with angle) = rank³
3 dimensions of space = N_c ✓
4 dimensions spacetime = rank² ✓
5 forces (counting gravity, EM, weak, strong, Higgs) = n_C ✓ (or 4 = rank²)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13

    dim = [
        ("SI base units",         7, g, "g"),
        ("Base quantities total", 8, rank**3, "rank³"),
        ("Space dimensions",      3, N_c, "N_c"),
        ("Spacetime dimensions",  4, rank**2, "rank²"),
        ("SM forces (no gravity)",4, rank**2, "rank² = EM+weak+strong+Higgs"),
        ("Fundamental forces",    5, n_C, "n_C (with gravity)"),
        ("Quark generations",     3, N_c, "N_c (T1922, T2003)"),
        ("Lepton generations",    3, N_c, "N_c (T1922, T2003)"),
    ]

    print("Dimensional analysis BST:")
    matches = 0
    for name, val, bst, formula in dim:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<25} = {val} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(dim)}")
    return matches, len(dim)


if __name__ == "__main__":
    run()
