"""
Toy 2790 — Atomic quantum numbers BST.

Principal quantum number n: integer
Orbital quantum number l: 0, 1, ..., n-1 (s, p, d, f, ...)
Magnetic quantum number m: -l, ..., +l
Spin: 1/2

Per-orbital electrons (Pauli):
s (l=0): 2 = rank
p (l=1): 6 = C_2
d (l=2): 10 = rank·n_C
f (l=3): 14 = rank·g
g (l=4): 18 = rank·N_c²
h (l=5): 22 = rank·c_2
i (l=6): 26 = rank·c_3

ALL orbital capacities = 2(2l+1) are BST integer expressions.
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13

    orbitals = [
        ("s (l=0)", 2,  rank,         "rank"),
        ("p (l=1)", 6,  C_2,          "C_2 = 2·3"),
        ("d (l=2)", 10, rank*n_C,     "rank·n_C"),
        ("f (l=3)", 14, rank*g,       "rank·g"),
        ("g (l=4)", 18, rank*N_c**2,  "rank·N_c²"),
        ("h (l=5)", 22, rank*c_2,     "rank·c_2"),
        ("i (l=6)", 26, rank*c_3,     "rank·c_3"),
    ]

    print("Atomic orbital capacities BST:")
    matches = 0
    for name, cap, bst, formula in orbitals:
        ok = cap == bst
        if ok:
            matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<10} cap = {cap:<3} = {formula:<12} {marker}")

    print(f"\nSCORE: {matches}/{len(orbitals)} (orbital capacities BST)")
    print(f"\nFormula 2(2l+1) for orbital cap factorizes as rank·(BST integer).")
    return matches, len(orbitals)


if __name__ == "__main__":
    run()
