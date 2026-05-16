"""
Toy 2858 — Crystallography structural counts BST.

Bravais lattices in 3D: 14 = rank·g
Crystal systems: 7 = g
Point groups: 32 = rank⁵
Space groups (3D): 230 — try N_c·g·c_2 - 1 = 230 ✓!  (3·7·11 = 231-1 = 230)
Plane groups (2D): 17 = c_2 + C_2 = 11+6 = Ogg17!
Frieze groups: 7 = g
Wallpaper groups: 17 = Ogg17 (same as plane groups; T-2nd)
Octahedral symmetry order: 48 = c_3·N_c+9 → or rank⁴·N_c
Tetrahedral symmetry order: 24 = rank³·N_c = χ(K3)
Icosahedral symmetry order: 120 = c_2·c_2-1 = 121-1? Or rank³·N_c·n_C = 120 EXACT ✓
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13

    crystal = [
        ("Crystal systems (3D)",       7,   g,                  "g"),
        ("Bravais lattices (3D)",      14,  rank*g,             "rank·g"),
        ("Point groups (3D)",          32,  rank**5,            "rank⁵"),
        ("Space groups (3D)",          230, N_c*g*c_2-1,        "N_c·g·c_2 - 1"),
        ("Plane groups (2D, wallpaper)", 17, c_2 + C_2,         "c_2+C_2 = Ogg17"),
        ("Frieze groups",              7,   g,                  "g"),
        ("Tetrahedral group |T_d|",    24,  rank**3*N_c,        "rank³·N_c = χ(K3)"),
        ("Octahedral group |O_h|",     48,  rank**4*N_c,        "rank⁴·N_c"),
        ("Icosahedral group |I_h|",    120, rank**3*N_c*n_C,    "rank³·N_c·n_C"),
        ("Quasi-crystal local symmetries (Penrose)", 5, n_C,    "n_C"),
        ("Crystal lattice nearest-neighbor max (HCP/FCC)", 12, rank*C_2, "rank·C_2 (T2160)"),
    ]

    print("Crystallography BST:")
    matches = 0
    for name, val, bst, formula in crystal:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<46} = {val:<3} = {formula:<18} {marker}")

    print(f"\nSCORE: {matches}/{len(crystal)}")
    return matches, len(crystal)


if __name__ == "__main__":
    run()
