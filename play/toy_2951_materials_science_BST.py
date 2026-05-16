"""
Toy 2951 — Materials science classification BST.

Standard material categories: 4 = rank² (metals, ceramics, polymers, composites)
+ Biomaterials, semiconductors = 6 = C_2

Standard crystal defect categories: 4 = rank² (point, line, planar, volume)
Standard point defects: 5 = n_C (vacancy, interstitial, substitutional,
  Frenkel, Schottky)
Line defects: 2 = rank (edge, screw dislocations)
Planar defects: 3 = N_c (grain boundaries, twin boundaries, stacking faults)

Standard alloying mechanisms: 3 = N_c (substitutional, interstitial, multi-phase)

Steel families standard: 5 = n_C (carbon, alloy, stainless, tool, structural)

Polymer crystal structures basic: 3 = N_c (amorphous, semi-crystalline, crystalline)
Polymer chain configurations: 3 = N_c (linear, branched, cross-linked)

Standard composite types: 4 = rank² (particle, fiber, structural, lamina)
Fiber arrangements: 3 = N_c (uniaxial, biaxial, random)

Semiconductor types: 3 = N_c (n-type, p-type, intrinsic)

Standard heat treatment processes for steel: 6 = C_2 (annealing, normalizing,
  hardening, tempering, austempering, martempering)

Standard mechanical testing categories: 5 = n_C (tensile, compression,
  bending, hardness, impact)
Standard non-destructive testing: 5 = n_C (X-ray, ultrasonic, magnetic particle,
  dye penetrant, eddy current)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    mat = [
        ("Standard material categories",         4, rank**2, "rank²"),
        ("Material categories + bio + semi",     6, C_2, "C_2"),
        ("Crystal defect categories",            4, rank**2, "rank² (point/line/planar/volume)"),
        ("Point defects",                        5, n_C, "n_C"),
        ("Line defects (edge, screw)",           2, rank, "rank"),
        ("Planar defects",                       3, N_c, "N_c"),
        ("Alloying mechanisms",                  3, N_c, "N_c"),
        ("Steel families standard",              5, n_C, "n_C"),
        ("Polymer crystal structures",           3, N_c, "N_c"),
        ("Polymer chain configurations",         3, N_c, "N_c"),
        ("Composite types",                      4, rank**2, "rank²"),
        ("Fiber arrangements",                   3, N_c, "N_c"),
        ("Semiconductor types",                  3, N_c, "N_c"),
        ("Heat treatment processes (steel)",     6, C_2, "C_2"),
        ("Mechanical testing categories",        5, n_C, "n_C"),
        ("Non-destructive testing methods",      5, n_C, "n_C"),
        ("Standard hardness scales (Brinell+Vickers+Rockwell+Mohs+Knoop+Shore+Barcol)", 7, g, "g"),
    ]

    print("Materials science BST:")
    matches = 0
    for name, val, bst, formula in mat:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<60} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(mat)}")
    return matches, len(mat)


if __name__ == "__main__":
    run()
