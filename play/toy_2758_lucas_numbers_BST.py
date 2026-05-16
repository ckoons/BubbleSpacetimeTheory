"""
Toy 2758 — Lucas numbers L_n BST (extends Fibonacci/Pell/Bell family).

Lucas: 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, ...
"""

import math


def run():
    tests = []
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13; N_max = 137

    def lucas(n):
        a, b = 2, 1
        for _ in range(n):
            a, b = b, a+b
        return a

    matches = []
    matches.append((0, 2, "rank", rank))
    matches.append((2, 3, "N_c", N_c))
    matches.append((3, 4, "rank²", rank**2))
    matches.append((4, 7, "g", g))
    matches.append((5, 11, "c_2", c_2))
    matches.append((6, 18, "rank·N_c²", rank*N_c**2))
    matches.append((7, 29, "Ogg29 = rank²·g+1", rank**2*g+1))
    matches.append((8, 47, "Ogg47 = rank²·c_2+N_c", rank**2*c_2+N_c))
    matches.append((9, 76, "rank²·19 = rank²·(N_c³-rank³)", rank**2*(N_c**3-rank**3)))
    matches.append((10, 123, "N_c·41 = N_c·Ogg41", N_c*(c_3*N_c+rank)))
    matches.append((11, 199, "N_max + rank·31 = N_max + rank·M_{n_C}", N_max + rank*(2**n_C-1)))

    print("Lucas BST:")
    matches_ok = 0
    for n, val, formula, bst in matches:
        actual = lucas(n)
        ok = actual == bst and actual == val
        if ok:
            matches_ok += 1
        print(f"  L_{n} = {actual} ?= {formula} = {bst} {'✓' if ok else '×'}")

    print(f"\nSCORE: {matches_ok}/{len(matches)}")
    return matches_ok, len(matches)


if __name__ == "__main__":
    run()
