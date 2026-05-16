"""
Toy 2814 — Chemistry structural integers BST.

Number of elements naturally occurring: 92 (up to U)
Lanthanides: 15 = N_c·n_C
Actinides: 15 = N_c·n_C
Total f-block: 30 = rank·N_c·n_C
Transition metals: 38 ≈ rank·19 = rank·Ogg19
Halogens: 6 = C_2 (with Ts)
Noble gases: 7 = g (with Og)
Hydrogen valence shells: 4 = rank² (1s, 2s, 2p)
Alkali metals: 6 = C_2
Alkaline earth: 6 = C_2
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13

    chem = [
        ("Lanthanides",          15, N_c*n_C,       "N_c·n_C"),
        ("Actinides",            15, N_c*n_C,       "N_c·n_C"),
        ("f-block total",        30, rank*N_c*n_C,  "rank·N_c·n_C"),
        ("d-block (transition)", 38, rank*(N_c**3-rank**3), "rank·Ogg19"),
        ("Halogens (with Ts)",   6,  C_2,           "C_2"),
        ("Noble gases (with Og)",7,  g,             "g"),
        ("Alkali metals",        6,  C_2,           "C_2 (Li through Fr)"),
        ("Alkaline earth",       6,  C_2,           "C_2"),
        ("Period 2 row",         8,  rank**3,       "rank³"),
        ("Period 4 row",         18, rank*N_c**2,   "rank·N_c²"),
        ("Period 6 row",         32, rank**5,       "rank⁵"),
    ]

    print("Chemistry structural counts BST:")
    matches = 0
    for name, val, bst, formula in chem:
        ok = val == bst
        marker = "✓" if ok else "×"
        if ok:
            matches += 1
        print(f"  {name:<25} = {val:<4} = {formula:<25} {marker}")

    print(f"\nSCORE: {matches}/{len(chem)}")
    return matches, len(chem)


if __name__ == "__main__":
    run()
