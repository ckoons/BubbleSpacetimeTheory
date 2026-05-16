"""
Toy 2789 — First 30 primes and BST integer expressions.

First 30 primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113

How many factor through BST integers (Ogg + simple sums + Heegner)?
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13; N_max = 137

    bst_known = {
        2: "rank", 3: "N_c", 5: "n_C", 7: "g", 11: "c_2", 13: "c_3",
        17: "c_2+N_c·rank", 19: "N_c³-rank³", 23: "rank²·C_2-1",
        29: "rank²·g+1", 31: "M_{n_C}", 37: "N_c·c_3-rank",
        41: "c_3·N_c+rank", 43: "rank²·c_2-1 (Heegner)",
        47: "rank²·c_2+N_c", 53: "rank²·c_3+1",
        59: "c_2·n_C+rank²", 61: "?",
        67: "c_3·n_C+rank (Heegner)", 71: "rank²·C_2·N_c-1",
        73: "N_c·c_3+rank·c_3·... = c_3·c_2-g·... probably not clean",
        79: "c_3·g-c_2-rank = 91-13 = 78 → no",
        83: "rank·N_max-N_c·c_2·n_C+rank²+rank·N_c-rank+rank = ad hoc",
        89: "?", 97: "?", 101: "?", 103: "?", 107: "?", 109: "?", 113: "?"
    }

    primes_30 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

    print("First 30 primes BST decomposability:")
    bst_count = 0
    for p in primes_30:
        formula = bst_known.get(p, "?")
        if "?" not in formula and "no" not in formula and "not clean" not in formula and "ad hoc" not in formula:
            bst_count += 1
            print(f"  {p:<4}: {formula} ✓")
        else:
            print(f"  {p:<4}: {formula}")

    rate = bst_count / 30 * 100
    print(f"\nSCORE: {bst_count}/30 = {rate:.0f}% of first 30 primes BST-expressible")
    print(f"All 15 Ogg primes (≤71) are BST. Above 71: pattern weakens.")
    return bst_count, 30


if __name__ == "__main__":
    run()
