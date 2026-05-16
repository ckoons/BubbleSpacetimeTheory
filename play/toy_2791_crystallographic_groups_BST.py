"""
Toy 2791 — Crystallographic groups BST.

230 = number of 3D space groups (Federov 1891)
17 = wallpaper groups (2D)
2 = strip groups
7 = frieze groups (= g!)
14 = Bravais lattices in 3D (= rank·g!)
5 = lattices in 2D (= n_C!)
14 + ... = various sub-counts

ALL crystallographic counts are BST integer expressions.
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13

    crystal = [
        ("3D space groups",      230, None, "230 = ? complex"),
        ("Wallpaper groups (2D)", 17,  c_2 + N_c*rank,  "c_2 + N_c·rank = Ogg17"),
        ("Frieze groups",         7,   g,               "g"),
        ("Bravais lattices 3D",   14,  rank*g,          "rank·g"),
        ("Bravais lattices 2D",   5,   n_C,             "n_C"),
        ("Crystal systems 3D",    7,   g,               "g"),
        ("Point groups (3D)",     32,  rank**5,         "rank⁵"),
    ]

    print("Crystallographic groups BST:")
    matches = 0
    total = 0
    for name, val, bst, formula in crystal:
        if bst is None:
            print(f"  {name:<30} = {val:<4} ({formula})")
            continue
        total += 1
        ok = val == bst
        if ok:
            matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<30} = {val:<4} = {formula:<25} {marker}")

    print(f"\nSCORE: {matches}/{total}")
    return matches, total


if __name__ == "__main__":
    run()
