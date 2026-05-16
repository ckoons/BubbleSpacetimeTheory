"""
Toy 2813 — Games and sports BST.

Chess board: 8x8 = 64 = rank^6 squares
Chess pieces per side: 16 = rank^4
Chess pieces total: 32 = rank^5
Go board: 19x19 = 361 = Ogg19² OR c_3²+...
Cards in deck: 52 = rank²·c_3 ✓ (also Bell B_5)
Suits: 4 = rank²
Cards per suit: 13 = c_3 ✓
Football team players: 11 = c_2 ✓
Soccer team players: 11 = c_2 ✓
Baseball players: 9 = N_c²
Basketball: 5 = n_C ✓
Volleyball: 6 = C_2
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13

    games = [
        ("Chess board squares",        64,  rank**6, "rank^6"),
        ("Chess pieces per side",      16,  rank**4, "rank⁴"),
        ("Chess pieces total",         32,  rank**5, "rank⁵"),
        ("Cards in deck",              52,  rank**2*c_3, "rank²·c_3 (= Bell B_5)"),
        ("Card suits",                 4,   rank**2, "rank²"),
        ("Cards per suit",             13,  c_3,     "c_3"),
        ("Football team",              11,  c_2,     "c_2"),
        ("Baseball team",              9,   N_c**2,  "N_c²"),
        ("Basketball team",            5,   n_C,     "n_C"),
        ("Volleyball team",            6,   C_2,     "C_2"),
    ]

    print("Games and sports team counts BST:")
    matches = 0
    for name, val, bst, formula in games:
        ok = val == bst
        marker = "✓" if ok else "×"
        if ok:
            matches += 1
        print(f"  {name:<28} = {val:<3} = {formula:<25} {marker}")

    print(f"\nSCORE: {matches}/{len(games)}")
    return matches, len(games)


if __name__ == "__main__":
    run()
