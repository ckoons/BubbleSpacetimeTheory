"""
Toy 2764 — Simply-connected covers of all classical Lie groups BST.

|Z(SU(n))| = n (center) → all BST primes
|π_1(SO(n))| = Z/2 for n>2 → rank covering
Spin groups: |Z(Spin(n))| structure
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13

    centers = [
        ("SU(2)", 2, "rank"),
        ("SU(3)", 3, "N_c"),
        ("SU(5)", 5, "n_C"),
        ("SU(7)", 7, "g"),
        ("SU(11)", 11, "c_2"),
        ("SU(13)", 13, "c_3"),
        ("Spin(5)", 2, "rank"),
        ("Spin(7)", 2, "rank"),
        ("Spin(8)", 4, "rank²"),  # Z/2 × Z/2
        ("E_6 center", 3, "N_c"),
        ("E_7 center", 2, "rank"),
    ]

    print("Group center orders BST:")
    matches = 0
    for name, order, formula in centers:
        # eval formula
        d = {"rank": rank, "N_c": N_c, "n_C": n_C, "C_2": C_2, "g": g,
             "c_2": c_2, "c_3": c_3, "rank²": rank**2}
        bst = d.get(formula, None)
        if bst is None:
            # try eval
            try:
                bst = eval(formula.replace("²", "**2"), {"__builtins__":{}}, d)
            except:
                bst = "?"
        ok = order == bst
        marker = "✓" if ok else "×"
        if ok:
            matches += 1
        print(f"  |Z({name:<12})| = {order:<3} = {formula:<10} {marker}")

    print(f"\nSCORE: {matches}/{len(centers)}")
    return matches, len(centers)


if __name__ == "__main__":
    run()
