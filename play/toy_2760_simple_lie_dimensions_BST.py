"""
Toy 2760 — Simple Lie group dimensions are BST integer expressions.

Owner: Lyra
Date:  2026-05-17

DIMENSIONS
==========
SU(2) = 3 = N_c
SU(3) = 8 = rank³
SU(5) = 24 = rank³·N_c (= χ(K3))
SU(7) = 48 = rank⁴·N_c
SO(3) = 3 = N_c
SO(5) = 10 = rank·n_C
SO(7) = 21 = N_c·g (Pell)
SO(10) = 45 = N_c²·n_C
G_2 = 14 = rank·g
F_4 = 52 = rank²·c_3
E_6 = 78 = C_2·c_3
E_7 = 133 = g·19 = g·Ogg19
E_8 = 248 = rank³ + 240 = rank³ + rank⁴·n_C·N_c
Sp(4) = 10 = rank·n_C
Sp(6) = 21 = N_c·g
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13

    lie_data = [
        ("SU(2)", 3,   N_c, "N_c"),
        ("SU(3)", 8,   rank**3, "rank³"),
        ("SU(5)", 24,  rank**3*N_c, "rank³·N_c = χ(K3)"),
        ("SO(3)", 3,   N_c, "N_c"),
        ("SO(5)", 10,  rank*n_C, "rank·n_C"),
        ("SO(7)", 21,  N_c*g, "N_c·g"),
        ("SO(10)", 45, N_c**2*n_C, "N_c²·n_C"),
        ("G_2",   14,  rank*g, "rank·g"),
        ("F_4",   52,  rank**2*c_3, "rank²·c_3"),
        ("E_6",   78,  C_2*c_3, "C_2·c_3"),
        ("E_7",   133, g*19, "g·Ogg19"),
        ("E_8",   248, rank**3 + rank**4*n_C*N_c, "rank³+rank⁴·n_C·N_c (8+240)"),
        ("Sp(4)", 10,  rank*n_C, "rank·n_C"),
        ("Sp(6)", 21,  N_c*g, "N_c·g"),
    ]

    print("Simple Lie group dimensions BST:")
    matches = 0
    for name, dim, bst, formula in lie_data:
        ok = dim == bst
        marker = "✓" if ok else "×"
        if ok:
            matches += 1
        print(f"  dim({name:<6}) = {dim:<5} = {formula:<30} {marker}")

    print(f"\nSCORE: {matches}/{len(lie_data)}")
    return matches, len(lie_data)


if __name__ == "__main__":
    run()
