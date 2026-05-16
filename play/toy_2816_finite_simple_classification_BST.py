"""
Toy 2816 — Classification of finite simple groups (CFSG) structural counts BST.

26 sporadic groups = rank·c_3 ✓
4 infinite families: cyclic, alternating, Lie-type chevalley, Lie-type twisted

Total infinite families of finite simple groups: 18 = rank·N_c² (counting all Lie variants)
Or: 4 main families = rank²
17 isomorphism classes of Lie-type: c_2+N_c·rank = Ogg17
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13

    cfsg = [
        ("Sporadic groups",             26, rank*c_3, "rank·c_3"),
        ("Main infinite families",      4,  rank**2,  "rank²"),
        ("Lie-type isomorphism classes",17, c_2+N_c*rank, "Ogg17"),
    ]

    print("CFSG structural counts BST:")
    matches = 0
    for name, val, bst, formula in cfsg:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<30} = {val:<3} = {formula:<15} {marker}")

    print(f"\nSCORE: {matches}/{len(cfsg)}")
    return matches, len(cfsg)


if __name__ == "__main__":
    run()
