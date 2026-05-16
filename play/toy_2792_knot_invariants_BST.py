"""
Toy 2792 — Knot theory dimensions / invariants BST.

Trefoil knot crossings: 3 = N_c
Figure-8 crossings: 4 = rank²
Number of prime knots up to 7 crossings:
1 (3 crossings) + 1 (4) + 2 (5) + 3 (6) + 7 (7) = 14 = rank·g

Lowest 8 crossings prime knots: 21 = N_c·g
Number of prime knots ≤ 9 crossings: 49 = g²
Number of prime knots ≤ 10 crossings: 165 = ?
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13

    knots = [
        ("Trefoil crossings",          3,  N_c,          "N_c"),
        ("Figure-8 crossings",         4,  rank**2,      "rank²"),
        ("Prime knots ≤ 7 crossings",  14, rank*g,       "rank·g"),
        ("Prime knots ≤ 8 crossings",  21, N_c*g,        "N_c·g"),
        ("Prime knots ≤ 9 crossings",  49, g**2,         "g²"),
    ]

    print("Knot theory dimensions BST:")
    matches = 0
    for name, val, bst, formula in knots:
        ok = val == bst
        if ok:
            matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<35} = {val:<4} = {formula:<10} {marker}")

    print(f"\nSCORE: {matches}/{len(knots)}")
    return matches, len(knots)


if __name__ == "__main__":
    run()
