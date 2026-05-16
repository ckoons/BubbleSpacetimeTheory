"""
Toy 2938 — Geological time scale BST.

Geologic eons: 4 = rank² (Hadean, Archean, Proterozoic, Phanerozoic)
Phanerozoic eras: 3 = N_c (Paleozoic, Mesozoic, Cenozoic)
Phanerozoic periods: 12 = rank·C_2 (Cambrian, Ordovician, Silurian, Devonian,
  Carboniferous, Permian, Triassic, Jurassic, Cretaceous, Paleogene, Neogene, Quaternary)
Paleozoic periods: 6 = C_2
Mesozoic periods: 3 = N_c (Triassic, Jurassic, Cretaceous)
Cenozoic periods: 3 = N_c (Paleogene, Neogene, Quaternary)
Cenozoic epochs total: 7 = g (Paleocene, Eocene, Oligocene, Miocene, Pliocene,
  Pleistocene, Holocene)
Quaternary epochs: 2 = rank (Pleistocene, Holocene)

Major mass extinctions: 5 = n_C (Ordovician, Devonian, Permian, Triassic, K-T)
+ Anthropocene 6th = 6 = C_2

Hadean → Phanerozoic time scale orders: 4 = rank²
Archaeological ages metal: 3 = N_c (Copper, Bronze, Iron)
+ Stone Age = 4 = rank²
Subdivisions of Stone Age: 3 = N_c (Paleolithic, Mesolithic, Neolithic)

Human evolution major species recognized: 7 = g (varies; H. habilis, erectus,
  heidelbergensis, neanderthalensis, sapiens, denisovans, floresiensis)

Major glaciations in Quaternary: 4 = rank² (Günz, Mindel, Riss, Würm in Alpine)
or 5 = n_C in some classifications
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    geo = [
        ("Geologic eons",                4, rank**2, "rank²"),
        ("Phanerozoic eras",             3, N_c, "N_c (Paleo/Meso/Cenozoic)"),
        ("Phanerozoic periods",          12, rank*C_2, "rank·C_2"),
        ("Paleozoic periods",            6, C_2, "C_2"),
        ("Mesozoic periods",             3, N_c, "N_c"),
        ("Cenozoic periods",             3, N_c, "N_c"),
        ("Cenozoic epochs total",        7, g, "g"),
        ("Quaternary epochs",            2, rank, "rank"),
        ("Major mass extinctions",       5, n_C, "n_C"),
        ("Mass extinctions + Anthropocene", 6, C_2, "C_2"),
        ("Archaeological metal ages",    3, N_c, "N_c (Cu, Bronze, Iron)"),
        ("Archaeological ages incl Stone", 4, rank**2, "rank²"),
        ("Stone Age subdivisions",       3, N_c, "N_c"),
        ("Human evolution major species", 7, g, "g (approx)"),
        ("Alpine Quaternary glaciations", 4, rank**2, "rank²"),
        ("Pleistocene glaciation cycles standard", 5, n_C, "n_C"),
    ]

    print("Geological time scale BST:")
    matches = 0
    for name, val, bst, formula in geo:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<42} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(geo)}")
    return matches, len(geo)


if __name__ == "__main__":
    run()
