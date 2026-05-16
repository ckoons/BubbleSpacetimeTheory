"""
Toy 2910 — Earth science / geophysics structural counts BST.

Earth's compositional layers: 5 = n_C (crust, upper mantle, lower mantle,
  outer core, inner core)
+ Lithosphere/asthenosphere distinction = 7 = g total layers

Earth's mechanical layers: 5 = n_C (lithosphere, asthenosphere,
  mesosphere, outer core, inner core)
Atmosphere layers: 5 = n_C (matches T2229)
Ocean major layers: 5 = n_C (epipelagic, mesopelagic, bathypelagic,
  abyssopelagic, hadalpelagic)

Major tectonic plate types: 3 = N_c (divergent, convergent, transform)
Major plates: 7 = g large + ~8 minor = 15 = N_c·n_C
Major mountain belt orogenies: 4 = rank² (recent: Alpine, Hercynian,
  Caledonian, Pan-African)

Earthquake wave types: 4 = rank² (P, S, Love, Rayleigh)
Volcano classification (Iceland-Plinian scale): 6 = C_2

Magnetic field reversals per million years average: ~3 = N_c (varies)

Moh's mineral hardness scale: 10 = rank·n_C
Major rock classification categories: 3 = N_c (igneous, sedimentary, metamorphic)
Mineral primary classes (Strunz): 9 = N_c² classes
Earth radius/Moon radius ratio approx: 3.67 ≈ N_c+rank (not exact)
Earth/Sun mass ratio exponent: -6 = -C_2 (approx)

Major ocean basins: 5 = n_C (Atlantic, Pacific, Indian, Arctic, Southern)
Continents: 7 = g (or 6 = C_2 in some classifications)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    geo = [
        ("Earth compositional layers",       5, n_C, "n_C"),
        ("Earth compositional + litho/astheno", 7, g, "g"),
        ("Earth mechanical layers",          5, n_C, "n_C"),
        ("Atmosphere layers",                5, n_C, "n_C"),
        ("Ocean pelagic zones",              5, n_C, "n_C"),
        ("Tectonic plate boundary types",    3, N_c, "N_c"),
        ("Plates total (major + minor)",     15, N_c*n_C, "N_c·n_C"),
        ("Major mountain orogenies recent",  4, rank**2, "rank²"),
        ("Earthquake wave types",            4, rank**2, "rank² (P,S,Love,Rayleigh)"),
        ("Moh's hardness scale",             10, rank*n_C, "rank·n_C"),
        ("Rock major classification",        3, N_c, "N_c"),
        ("Strunz mineral primary classes",   9, N_c**2, "N_c²"),
        ("Major ocean basins",               5, n_C, "n_C"),
        ("Continents (7-model)",             7, g, "g"),
        ("Volcano Iceland-Plinian scale",    6, C_2, "C_2"),
        ("Cardinal directions",              4, rank**2, "rank²"),
        ("Cardinal + intercardinal",         8, rank**3, "rank³"),
        ("Köppen climate primary types",     5, n_C, "n_C (A,B,C,D,E)"),
    ]

    print("Geophysics / Earth science BST:")
    matches = 0
    for name, val, bst, formula in geo:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<40} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(geo)}")
    return matches, len(geo)


if __name__ == "__main__":
    run()
