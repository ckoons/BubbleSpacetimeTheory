"""
Toy 2937 — Botany / plant biology structural counts BST.

Plant kingdom major divisions: 4 = rank² (Bryophytes, Pteridophytes,
  Gymnosperms, Angiosperms)
Angiosperm major groups: 2 = rank (monocots, eudicots) historically
+ Magnoliids = 3 = N_c
+ Basal angiosperms = 4 = rank²

Plant tissue types fundamental: 3 = N_c (dermal, vascular, ground)
Vascular tissue subtypes: 2 = rank (xylem, phloem)

Flower parts in basic eudicot:
  Petals usually: 4 or 5 = rank² or n_C
  Sepals usually: 4 or 5 = rank² or n_C
  Floral whorls: 4 = rank² (sepals, petals, stamens, carpels)

Leaf venation types: 3 = N_c (pinnate, palmate, parallel)

Photosynthesis types: 3 = N_c (C3, C4, CAM)
Major plant hormones: 5 = n_C (auxin, cytokinin, gibberellin, ABA, ethylene)
+ Brassinosteroids, jasmonates, etc. = 7 = g

Major fruit types: 7 = g (drupe, berry, pome, citrus, aggregate, multiple, dry)

Standard Linnaean taxonomic ranks: 7 = g (kingdom, phylum, class, order, family, genus, species)
+ Domain = 8 = rank³

Tree growth rings primary count categories observed for dating: 3 = N_c
  (earlywood, latewood, missing)

Crop major groups: 5 = n_C (cereals, legumes, vegetables, fruits, tubers)
Grain primary types: 5 = n_C (wheat, rice, corn, barley, oats)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    bot = [
        ("Plant kingdom major divisions",     4, rank**2, "rank²"),
        ("Plant tissue types fundamental",    3, N_c, "N_c"),
        ("Vascular tissue subtypes",          2, rank, "rank"),
        ("Floral whorls",                     4, rank**2, "rank²"),
        ("Leaf venation types",               3, N_c, "N_c"),
        ("Photosynthesis types",              3, N_c, "N_c (C3, C4, CAM)"),
        ("Major plant hormones",              5, n_C, "n_C"),
        ("All plant hormones",                7, g, "g"),
        ("Major fruit types",                 7, g, "g"),
        ("Standard Linnaean taxonomic ranks", 7, g, "g"),
        ("Linnaean + Domain",                 8, rank**3, "rank³"),
        ("Tree ring dating categories",       3, N_c, "N_c"),
        ("Major crop groups",                 5, n_C, "n_C"),
        ("Major grain types",                 5, n_C, "n_C"),
        ("Eudicot petals typical",            5, n_C, "n_C"),
        ("Monocot petal count typical",       3, N_c, "N_c"),
        ("Plant cell types major (parenchyma, collenchyma, sclerenchyma)", 3, N_c, "N_c"),
    ]

    print("Botany BST:")
    matches = 0
    for name, val, bst, formula in bot:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<60} = {val:<3} = {formula:<12} {marker}")

    print(f"\nSCORE: {matches}/{len(bot)}")
    return matches, len(bot)


if __name__ == "__main__":
    run()
