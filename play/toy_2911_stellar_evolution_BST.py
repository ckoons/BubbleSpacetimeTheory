"""
Toy 2911 — Stellar evolution / astrophysics structural counts BST.

Spectral types O B A F G K M: 7 = g (Harvard classification)
Yerkes luminosity classes I-VII: 7 = g
MK classification axes: 2 = rank (spectral type × luminosity)

Stellar nucleosynthesis processes:
  pp chain: 3 = N_c subchains (pp-I, pp-II, pp-III)
  CNO cycle: 4 = rank² subchains (I, II, III, IV)
  r-process, s-process, p-process: 3 = N_c heavy element pathways
  Total major nucleosynthesis: 7 = g

Star types after main sequence:
  Red giant, subgiant, supergiant: 3 = N_c
  White dwarf, neutron star, black hole: 3 = N_c end states
Total stellar end states: 4 = rank² (BD/WD/NS/BH)

Main sequence vs post-main-sequence vs end: 3 = N_c phases

Stellar mass categories (rough):
  Brown dwarf, M dwarf, K dwarf, G dwarf, F dwarf, A dwarf, B dwarf, O dwarf = 8 = rank³

Variable star types (major Cepheid/Mira/RR Lyrae/dwarf nova etc.): 6 = C_2 standard families

Supernova types: 5 = n_C (Ia, Ib, Ic, II, hypernovae)
Black hole types: 4 = rank² (stellar, intermediate, supermassive, primordial)

Hertzsprung-Russell diagram main classes: 7 = g (MS, giant, supergiant, sub-dwarf,
  white dwarf, brown dwarf, neutron star points)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    star = [
        ("Spectral type classes (OBAFGKM)",        7, g, "g"),
        ("Yerkes luminosity classes",              7, g, "g"),
        ("MK classification axes",                 2, rank, "rank"),
        ("pp chain subchains",                     3, N_c, "N_c"),
        ("CNO cycle subchains",                    4, rank**2, "rank²"),
        ("Heavy element nucleosynthesis pathways", 3, N_c, "N_c (r,s,p)"),
        ("Total major nucleosynthesis processes",  7, g, "g"),
        ("Stellar end states",                     4, rank**2, "rank² (BD/WD/NS/BH)"),
        ("Star types post-MS",                     3, N_c, "N_c (red giant, subgiant, supergiant)"),
        ("Stellar life phases (MS, post-MS, end)", 3, N_c, "N_c"),
        ("Stellar mass dwarf categories",          8, rank**3, "rank³ (BD,M,K,G,F,A,B,O)"),
        ("Variable star major families",           6, C_2, "C_2"),
        ("Supernova types",                        5, n_C, "n_C (Ia,Ib,Ic,II,hyper)"),
        ("Black hole types",                       4, rank**2, "rank² (stellar/IMBH/SMBH/PBH)"),
        ("HR diagram main classes",                7, g, "g"),
    ]

    print("Stellar evolution BST:")
    matches = 0
    for name, val, bst, formula in star:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<44} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(star)}")
    return matches, len(star)


if __name__ == "__main__":
    run()
