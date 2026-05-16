"""
Toy 2844 — Buckminsterfullerene C_60 + related BST.

C_60: 60 carbon atoms = rank²·n_C·N_c (= Stefan-Boltzmann denom T2049!)
Faces: 32 = rank⁵
12 pentagons + 20 hexagons = 32 faces total
Edges: 90 = rank·N_c²·n_C
Vertices: 60 = rank²·n_C·N_c

C_70, C_80, C_84, C_540, C_960 also discovered.

C_60 truncated icosahedron has icosahedral symmetry group I_h (order 120 = rank³·N_c·n_C).
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    bucky = [
        ("C_60 vertices",            60, rank**2*n_C*N_c, "rank²·n_C·N_c"),
        ("C_60 faces",               32, rank**5,         "rank⁵"),
        ("C_60 pentagons",           12, rank*C_2,        "rank·C_2"),
        ("C_60 hexagons",            20, rank**2*n_C,     "rank²·n_C"),
        ("C_60 edges",               90, rank*N_c**2*n_C, "rank·N_c²·n_C"),
        ("Icosahedral group order",  120, rank**3*N_c*n_C,"rank³·N_c·n_C"),
    ]

    print("Buckminsterfullerene C_60 BST:")
    matches = 0
    for name, val, bst, formula in bucky:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<28} = {val:<4} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(bucky)}")
    print(f"Buckminsterfullerene structural counts ALL BST integer products.")
    return matches, len(bucky)


if __name__ == "__main__":
    run()
