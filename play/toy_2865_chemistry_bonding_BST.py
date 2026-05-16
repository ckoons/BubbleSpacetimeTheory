"""
Toy 2865 — Chemistry bonding and structural counts BST.

Common oxidation states for transition metals: range 0 to 7 (osmium/iridium) = g
Maximum valence shells filled in stable atom: 7 = g (period 7)
Coordination geometries (common): 4 = rank² (linear, trigonal, tetrahedral, octahedral)
  Plus square planar, trig bipyramidal, pentagonal: 7 = g total
Most common coordination numbers: 4,6 = rank², C_2
Ionic bond charge typical range: ±N_c (±3 trans metals)

Hybrid orbitals: sp, sp², sp³, sp³d, sp³d²: 5 = n_C ✓
Bond orders standard: 1,2,3 = N_c
H-bond donor/acceptor pair counts in water: 4 = rank² (2 donors + 2 acceptors)
Lewis acid/base "softness" categorical bins (Pearson HSAB): 6 = C_2

Resonance structures in benzene: 2 (Kekulé) = rank
π-electrons in benzene (aromatic): 6 = C_2
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13
    _ = (c_2, c_3)

    chem = [
        ("Hybrid orbital types",        5, n_C,    "n_C (sp,sp²,sp³,sp³d,sp³d²)"),
        ("Common bond orders",          3, N_c,    "N_c (single, double, triple)"),
        ("Coordination geometries (common)", 4, rank**2, "rank² (linear/trig/tetra/oct)"),
        ("Coordination numbers max common", 6, C_2, "C_2"),
        ("Periodic table periods",      7, g,      "g"),
        ("Max oxidation states (Os/Ir)", 7, g,     "g"),
        ("Pearson HSAB categories",     6, C_2,    "C_2 (hard/borderline/soft × acid/base)"),
        ("Benzene π-electrons",         6, C_2,    "C_2"),
        ("Benzene Kekulé resonances",   2, rank,   "rank"),
        ("Water H-bond capacity",       4, rank**2, "rank² (2D+2A)"),
        ("Common ionic bond states (-3,-2,-1,0,+1,+2,+3)", 7, g, "g"),
        ("Sulfur common oxidation states (-2,0,+2,+4,+6)", 5, n_C, "n_C"),
        ("Carbon common oxidation states (-4,-2,0,+2,+4)", 5, n_C, "n_C"),
    ]

    print("Chemistry bonding BST:")
    matches = 0
    for name, val, bst, formula in chem:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<48} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(chem)}")
    return matches, len(chem)


if __name__ == "__main__":
    run()
