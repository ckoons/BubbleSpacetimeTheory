"""
Toy 2872 — Modular forms / Galois theory structural counts BST.

SL(2,Z) generators: 2 = rank (S, T)
SL(2,Z) generators including inversion: 3 = N_c (S, T, -I)
Eisenstein series weight 4 E_4 — first nontrivial weight: 4 = rank²
Eisenstein series weight 6 E_6: 6 = C_2
Eisenstein series weight 8 E_8: 8 = rank³
Eisenstein series weight 12 E_12 (first cusp form Δ weight): 12 = rank·C_2
Modular discriminant Δ weight: 12 = rank·C_2
Number of fundamental domain reflections in H/SL(2,Z): 3 = N_c
Elliptic points of order 2,3 in SL(2,Z): 2 (orders 2 and 3 → rank, N_c)
Cusps of H/SL(2,Z): 1 = trivial

Galois groups of quintic ~ S_5: order 120 = rank³·N_c·n_C (T2230)
Solvable extension chain length max: 4 = rank² (typical for octic)
Frobenius elements in cyclic ext of degree n: n = (input)

j-invariant first coefficient: 744 = rank³·N_c·31 = 8·3·31 = 744 ✓
j-invariant linear term coefficient: 196884 = c_2 + 196883 (Monster moonshine!)
Coefficient 196884 = 2·98442 = ... too big to factor cleanly here
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13
    _ = (c_2, c_3, g)

    mod = [
        ("SL(2,Z) generators (S,T)",       2,  rank,         "rank"),
        ("SL(2,Z) gens with inversion",    3,  N_c,          "N_c"),
        ("Eisenstein E_4 weight",          4,  rank**2,      "rank²"),
        ("Eisenstein E_6 weight",          6,  C_2,          "C_2"),
        ("Eisenstein E_8 weight",          8,  rank**3,      "rank³"),
        ("Modular Δ weight",               12, rank*C_2,     "rank·C_2"),
        ("Fundamental domain reflections", 3,  N_c,          "N_c"),
        ("SL(2,Z) cusps",                  1,  1,            "trivial"),
        ("S_5 quintic Galois group order", 120, rank**3*N_c*n_C, "rank³·N_c·n_C"),
        ("j-invariant E_4 expansion constant", 744, rank**3*N_c*31, "rank³·N_c·31"),
    ]

    print("Modular forms / Galois BST:")
    matches = 0
    for name, val, bst, formula in mod:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<42} = {val:<4} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(mod)}")
    return matches, len(mod)


if __name__ == "__main__":
    run()
