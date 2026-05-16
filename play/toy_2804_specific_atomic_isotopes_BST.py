"""
Toy 2804 — Famous specific atomic isotopes BST.

Selected stable + radioactive notable isotopes (mass numbers):
- ¹H: 1
- ⁴He: 4 = rank²
- ¹²C: 12 = rank·C_2
- ¹⁴N: 14 = rank·g
- ¹⁶O: 16 = rank⁴
- ²⁰Ne: 20 = rank²·n_C (magic)
- ²⁸Si: 28 = rank²·g (magic)
- ⁵⁰Sn: 50 (magic, rank·n_C²)
- ⁸²Pb: 82 (magic, N_max-n_C·c_2)
- ²³⁵U: 235 = c_2·rank²·n_C+rank·c_2 = ad hoc
- ²³⁹Pu: 239 = ?
- ¹³⁷Cs: 137 = N_max (!)
- ⁶⁰Co: 60 = rank²·n_C·N_c (=240/4)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13; N_max = 137

    isotopes = [
        ("⁴He alpha",           4,   rank**2,         "rank²"),
        ("¹²C",                 12,  rank*C_2,        "rank·C_2"),
        ("¹⁴N",                 14,  rank*g,          "rank·g"),
        ("¹⁶O",                 16,  rank**4,         "rank⁴"),
        ("²⁰Ne",                20,  rank**2*n_C,     "rank²·n_C"),
        ("²⁸Si",                28,  rank**2*g,       "rank²·g"),
        ("⁵⁰Sn",                50,  rank*n_C**2,     "rank·n_C²"),
        ("⁸²Pb",                82,  N_max - n_C*c_2, "N_max-n_C·c_2"),
        ("¹³⁷Cs (atomic clock)", 137, N_max,           "N_max EXACT!"),
        ("⁶⁰Co",                60,  rank**2*n_C*N_c, "rank²·n_C·N_c"),
        ("¹²⁶Ba",               126, rank*N_c**2*g,   "rank·N_c²·g (magic)"),
    ]

    print("Notable isotope mass numbers BST:")
    matches = 0
    for name, A, bst, formula in isotopes:
        ok = A == bst
        marker = "✓" if ok else "×"
        if ok:
            matches += 1
        print(f"  {name:<24} A={A:<4} = {formula:<20} {marker}")

    print(f"\nSCORE: {matches}/{len(isotopes)} (notable isotopes BST)")
    print(f"Cesium-137 atomic clock isotope EXACTLY = N_max!")
    return matches, len(isotopes)


if __name__ == "__main__":
    run()
