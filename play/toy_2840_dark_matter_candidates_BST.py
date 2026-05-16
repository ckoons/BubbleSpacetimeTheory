"""
Toy 2840 — Dark matter candidates BST.

Grace T1971: m_DM = 5 GeV = n_C·GeV (BST natural)
Ω_DM h² = 0.120 (Planck)
Ω_DM/Ω_b = 5.33 ≈ rank⁴/N_c (T1966)

DM mass candidates in BST:
- WIMP: 5 GeV (BST natural T1971)
- Sterile ν: keV-mass range
- Axion: μeV mass range (but BST has no axion needed, T1964)
- Dark photon: from "Wallach shadow" T1966
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13; N_max = 137

    dm = [
        ("WIMP DM mass (GeV)",    5,    n_C,         "n_C (Grace T1971)"),
        ("Ω_DM/Ω_b",              5.33, rank**4/N_c, "rank⁴/N_c = 16/3 (T1966)"),
        ("DM/total mass-energy",  0.27, N_c/c_2,     "N_c/c_2 = 0.273"),
        ("Ω_DM h²",               0.120,N_c/(rank*c_2), "N_c/(rank·c_2)·... rough"),
    ]

    print("Dark matter BST:")
    matches = 0
    for name, obs, bst, formula in dm:
        if isinstance(obs, int) or isinstance(obs, float):
            if isinstance(bst, int):
                ok = obs == bst
            else:
                ok = abs(obs-bst)/obs < 0.05
            if ok: matches += 1
            marker = "✓" if ok else "×"
            print(f"  {name:<22} obs={obs:<8g} BST={bst:<10g} {formula:<30} {marker}")

    print(f"\nSCORE: {matches}/{len(dm)}")
    return matches, len(dm)


if __name__ == "__main__":
    run()
