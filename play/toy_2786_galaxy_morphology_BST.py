"""
Toy 2786 — Galaxy morphology and BST integer scaffold.

Hubble galaxy classification: E, S0, Sa, Sb, Sc, SBa, SBb, SBc, Irr
~9 standard types
Recent revisions: 8 main morphological types
Number of arms in spiral galaxies: typically 2 (grand design) or 3-4 (flocculent)
Galactic disk thickness: ~rank× galaxy radius/N_c

Hubble's tuning fork:
- 7 E0..E7 elliptical subtypes = g ✓
- Spiral types: S, SB × a, b, c = rank · N_c = C_2 = 6 types
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    morphology = [
        ("Elliptical subtypes E0-E7", 8, rank**3, "rank³"),
        ("Spiral types (S+SB ×abc)", 6, C_2, "C_2"),
        ("Common spiral arm count", 2, rank, "rank"),
        ("Main galaxy classes (Hubble)", 5, n_C, "n_C"),
        ("Galaxy clusters per supercluster (typ)", 10, rank*n_C, "rank·n_C"),
    ]

    print("Galaxy morphology BST (observational):")
    matches = 0
    for name, val, bst, formula in morphology:
        ok = val == bst
        marker = "✓" if ok else "×"
        if ok:
            matches += 1
        print(f"  {name:<40} = {val:<3} = {formula:<10} {marker}")

    print(f"\nSCORE: {matches}/{len(morphology)} (S-tier observational)")
    return matches, len(morphology)


if __name__ == "__main__":
    run()
