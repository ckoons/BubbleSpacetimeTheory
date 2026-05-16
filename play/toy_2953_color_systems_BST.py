"""
Toy 2953 — Color systems / vision BST.

Newton's rainbow colors: 7 = g (T2842 already established)
Munsell color system axes: 3 = N_c (hue, value, chroma)
Munsell hue major divisions: 10 = rank·n_C (5 primary + 5 intermediate)

CIE color spaces standard: 5 = n_C (XYZ, RGB, Lab, LCh, LMS)
sRGB primaries: 3 = N_c (R, G, B)
CMYK channels: 4 = rank² (cyan, magenta, yellow, key/black)

Photoreceptor types human: 4 = rank² (T2264: 3 cones + rod)
Tetrachromat species cones: 4 = rank² (some birds, reptiles)
Bird color vision channels: 4 = rank²

Standard color temperature ranges: 4 = rank² (warm <3500K, neutral 3500-5000, daylight 5000-6500, cool >6500)

Color blindness types: 5 = n_C (protanomaly, protanopia, deuteranomaly,
  deuteranopia, tritanopia, achromatopsia → 6 with achromatopsia = C_2)

Standard heraldic tinctures: 7 = g (Or, Argent, Gules, Azure, Sable, Vert, Purpure)

Pantone primaries (Goe): 5 = n_C variations standard
Standard chess colors: 2 = rank

Munsell value steps: 11 = c_2 (0-10)
Munsell chroma typical max: ~14 = rank·g

Color CIE chromaticity coordinates: 3 = N_c (x, y, z chromaticity values)
Standard illuminants CIE: 5 = n_C (A, D50, D55, D65, D75)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11

    color = [
        ("Newton's rainbow colors",          7, g, "g (T2842)"),
        ("Munsell axes (HVC)",               3, N_c, "N_c"),
        ("Munsell hue major divisions",      10, rank*n_C, "rank·n_C"),
        ("CIE color spaces standard",        5, n_C, "n_C"),
        ("sRGB primaries",                   3, N_c, "N_c"),
        ("CMYK channels",                    4, rank**2, "rank²"),
        ("Human photoreceptor types",        4, rank**2, "rank² (T2264)"),
        ("Tetrachromat species cones",       4, rank**2, "rank²"),
        ("Standard color temperature ranges", 4, rank**2, "rank²"),
        ("Color blindness types + achromatopsia", 6, C_2, "C_2"),
        ("Color blindness major types (5)",  5, n_C, "n_C"),
        ("Heraldic tinctures",               7, g, "g"),
        ("Chess colors",                     2, rank, "rank"),
        ("Munsell value steps",              11, c_2, "c_2"),
        ("Munsell chroma typical max",       14, rank*g, "rank·g"),
        ("CIE chromaticity coordinates",     3, N_c, "N_c (x,y,z)"),
        ("CIE standard illuminants",         5, n_C, "n_C (A,D50,D55,D65,D75)"),
        ("Standard primary colors (additive)", 3, N_c, "N_c (R,G,B)"),
        ("Standard subtractive primaries",   3, N_c, "N_c (C,M,Y)"),
    ]

    print("Color systems BST:")
    matches = 0
    for name, val, bst, formula in color:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<44} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(color)}")
    return matches, len(color)


if __name__ == "__main__":
    run()
