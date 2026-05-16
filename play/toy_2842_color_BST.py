"""
Toy 2842 — Color theory / visible spectrum BST.

Visible wavelength range: 400-700 nm
Primary colors (additive): 3 = N_c (RGB)
Primary colors (subtractive): 4 = rank² (CMYK)
Spectrum: 7 colors (ROYGBIV) = g ✓ (Newton's traditional)
Human cone types: 3 = N_c (S, M, L)
Color depth typical: 8-bit = rank³

CIE chromaticity: 2D plot (x, y) = rank
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    color = [
        ("Additive primaries (RGB)",  3, N_c, "N_c"),
        ("Subtractive primaries (CMYK)", 4, rank**2, "rank²"),
        ("Newton spectrum colors",    7, g, "g"),
        ("Cone receptor types",       3, N_c, "N_c"),
        ("8-bit color depth",         8, rank**3, "rank³"),
        ("CIE chromaticity dims",     2, rank, "rank"),
    ]

    print("Color theory BST:")
    matches = 0
    for name, val, bst, formula in color:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<28} = {val} = {formula:<10} {marker}")

    print(f"\nSCORE: {matches}/{len(color)}")
    return matches, len(color)


if __name__ == "__main__":
    run()
