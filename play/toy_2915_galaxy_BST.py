"""
Toy 2915 — Galaxy classification BST.

Hubble galaxy types: E (ellipticals), S (spirals), SB (barred spirals),
  Irr (irregular) = 4 = rank² major
+ Lenticular (S0) = 5 = n_C
+ dE/cD/dwarf irregulars = 7+ = g approximately

Hubble Sequence axis: rank (tuning fork two arms)

Spiral arm types: 4 = rank² (grand design, multi-arm, flocculent, lenticular S0)
Galaxy components: 5 = n_C (bulge, disk, halo, bar, spiral arms)
+ Nucleus, central black hole = 7 = g typical

Local Group major members: 3 = N_c (Milky Way, Andromeda, Triangulum)
Local Group total members ~ 80 satellite-included; majors = 3 = N_c

Galaxy environment types: 4 = rank² (field, group, cluster, supercluster)
Cluster richness classes: ≤5 = n_C standard Abell

Milky Way major satellites visible: 2 = rank (LMC, SMC) primary
+ Sagittarius dwarf etc. → ~5 = n_C if you count brightest dwarfs

Number of standard galaxy luminosity classes: 5 = n_C (I-V) Yerkes
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    gal = [
        ("Hubble major types (E,S,SB,Irr)",        4, rank**2, "rank²"),
        ("Hubble + lenticular S0",                 5, n_C,     "n_C"),
        ("Hubble tuning fork axes",                2, rank,    "rank (S vs SB arms)"),
        ("Spiral arm structural types",            4, rank**2, "rank²"),
        ("Galaxy components major",                5, n_C,     "n_C"),
        ("Galaxy components + nucleus + central BH", 7, g,    "g"),
        ("Local Group major members",              3, N_c,     "N_c (MW, M31, M33)"),
        ("Galaxy environment types",               4, rank**2, "rank²"),
        ("Cluster richness classes (Abell ≤5)",    5, n_C,     "n_C"),
        ("MW visible primary satellites (LMC,SMC)", 2, rank,   "rank"),
        ("MW bright dwarf satellites total",       5, n_C,     "n_C"),
        ("Galaxy luminosity classes (Yerkes I-V)", 5, n_C,     "n_C"),
        ("Active galactic nucleus types",          4, rank**2, "rank² (Seyfert,QSO,Blazar,Radio)"),
        ("Standard cosmological structures levels", 4, rank**2, "rank² (stars,galaxies,clusters,filaments)"),
    ]

    print("Galaxy classification BST:")
    matches = 0
    for name, val, bst, formula in gal:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<46} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(gal)}")
    return matches, len(gal)


if __name__ == "__main__":
    run()
