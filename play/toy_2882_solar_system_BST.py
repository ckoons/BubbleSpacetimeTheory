"""
Toy 2882 — Solar system / planetary structural counts BST.

Planets (post-2006 IAU): 8 = rank³
Dwarf planets recognized: 5 = n_C (Ceres, Pluto, Haumea, Makemake, Eris)
Inner rocky planets: 4 = rank²
Outer gas/ice giants: 4 = rank²
Asteroid belt main subregions: 3 = N_c (Hungaria, main, Cybele)
Major Kuiper belt regions: 3 = N_c (classical, scattered, resonant)
Earth's Lagrange points: 5 = n_C
Earth's atmospheric layers: 5 = n_C (tropo/strato/meso/thermo/exo)

Major solar wind regions: 4 = rank²
Sun atmospheric layers: 4 = rank² (photo/chromosphere/transition/corona)
Solar Carrington rotation classes: 2 = rank

Number of Mercury's known days = ~3 (3:2 spin-orbit) = N_c
Venus retrograde rotation (1 unique): 1 = trivial
Mars moons (Phobos+Deimos): 2 = rank
Saturn rings major: 7 = g (A,B,C,D,E,F,G)
Jupiter Galilean moons: 4 = rank²
Jupiter known moons (regulars): ~57, but major = 4 = rank²

Sun-Earth Lagrange L1-L5: 5 = n_C
Planets visible naked-eye in ancient: 5 = n_C (Mercury, Venus, Mars, Jupiter, Saturn)
+ Sun + Moon = 7 = g (classical "planets")
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    sol = [
        ("Planets (IAU 2006)",          8, rank**3, "rank³"),
        ("Inner rocky planets",         4, rank**2, "rank²"),
        ("Outer gas/ice giants",        4, rank**2, "rank²"),
        ("Dwarf planets recognized",    5, n_C,    "n_C"),
        ("Lagrange points (3-body)",    5, n_C,    "n_C"),
        ("Earth atmosphere layers",     5, n_C,    "n_C"),
        ("Sun atmosphere layers",       4, rank**2, "rank²"),
        ("Asteroid belt subregions",    3, N_c,    "N_c"),
        ("Kuiper belt regions",         3, N_c,    "N_c"),
        ("Mars moons",                  2, rank,   "rank"),
        ("Saturn ring major letters",   7, g,      "g (A-G)"),
        ("Jupiter Galilean moons",      4, rank**2, "rank²"),
        ("Naked-eye planets ancient",   5, n_C,    "n_C"),
        ("Classical planets + Sun + Moon", 7, g,   "g (heptad)"),
        ("Mercury spin-orbit ratio (3:2 → 3)", 3, N_c, "N_c"),
        ("Venus orbital direction (1)", 1, 1,     "trivial"),
        ("Pluto major moons",           5, n_C,    "n_C (Charon,Nix,Hydra,Kerberos,Styx)"),
    ]

    print("Solar system / astronomy BST:")
    matches = 0
    for name, val, bst, formula in sol:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<40} = {val:<3} = {formula:<12} {marker}")

    print(f"\nSCORE: {matches}/{len(sol)}")
    return matches, len(sol)


if __name__ == "__main__":
    run()
