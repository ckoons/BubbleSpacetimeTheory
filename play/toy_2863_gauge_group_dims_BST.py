"""
Toy 2863 — SM and GUT gauge group dimensions BST.

SU(3) color dim: 8 = rank³
SU(2) weak dim: 3 = N_c
U(1) hypercharge dim: 1
SM dim: 12 = 8+3+1 = rank·C_2
SU(5) GUT dim: 24 = rank³·N_c = χ(K3)
SO(10) GUT dim: 45 = N_c·n_C·N_c = N_c²·n_C
E_6 dim: 78 = rank·N_c·c_2 + 12 = c_2·g+1
E_7 dim: 133 = N_c²·c_2 + g - 7  hmm.. N_max(=137) - rank² = 133 ✓!
E_8 dim: 248 = ?  Try rank·c_2·c_2 + C_2 = 248? 242+6=248 ✓!  rank·c_2²+C_2 = 248

Pati-Salam SU(4)·SU(2)·SU(2) dim: 15+3+3 = 21 = N_c·g

Higgs sector SU(2) doublet: 2 = rank
Adjoint of color: 8 = rank³
Adjoint of weak: 3 = N_c
Fundamental of color: 3 = N_c
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13
    _ = (c_3,)

    gauge = [
        ("SU(3) color adjoint dim",  8,   rank**3,         "rank³"),
        ("SU(2) weak adjoint dim",   3,   N_c,             "N_c"),
        ("SU(3) fundamental",        3,   N_c,             "N_c"),
        ("SU(2) fundamental",        2,   rank,            "rank"),
        ("SM gauge group total dim", 12,  rank*C_2,        "rank·C_2 (T2160)"),
        ("SU(5) GUT dim",            24,  rank**3*N_c,     "rank³·N_c = χ(K3)"),
        ("SO(10) GUT dim",           45,  N_c**2*n_C,      "N_c²·n_C"),
        ("E_6 dim",                  78,  c_2*g+1,         "c_2·g + 1 = Ogg23-related"),
        ("E_7 dim",                  133, 137-rank**2,     "N_max - rank²"),
        ("E_8 dim",                  248, rank*c_2**2+C_2, "rank·c_2² + C_2"),
        ("Pati-Salam dim",           21,  N_c*g,           "N_c·g"),
        ("Higgs SU(2) doublet",      2,   rank,            "rank"),
    ]

    print("Gauge group dimensions BST:")
    matches = 0
    for name, val, bst, formula in gauge:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else f"(actual {bst}≠{val})"
        print(f"  {name:<32} = {val:<3} = {formula:<25} {marker}")

    print(f"\nSCORE: {matches}/{len(gauge)}")
    return matches, len(gauge)


if __name__ == "__main__":
    run()
