"""
Toy 2759 — Motzkin numbers M_n BST.

Motzkin: 1, 1, 2, 4, 9, 21, 51, 127, 323, 835, ...
"""

def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13; N_max = 137

    # Motzkin recurrence: M_n = M_{n-1} + sum_{k=0}^{n-2} M_k·M_{n-2-k}
    M = [1, 1]
    for n in range(2, 12):
        s = M[n-1]
        for k in range(n-1):
            s += M[k] * M[n-2-k]
        M.append(s)

    matches = [
        (2, 2,    "rank",                     rank),
        (4, 9,    "N_c²",                     N_c**2),
        (5, 21,   "N_c·g",                    N_c*g),
        (7, 127,  "M_7 Mersenne = N_max-10",  N_max - rank*n_C),
        (9, 835,  "N_max·... check",          None),
    ]

    print("Motzkin BST:")
    matches_ok = 0
    for n, val, formula, bst in matches:
        actual = M[n]
        if bst is not None:
            ok = actual == bst and actual == val
            print(f"  M_{n} = {actual} ?= {formula} = {bst} {'✓' if ok else '×'}")
            if ok:
                matches_ok += 1
        else:
            print(f"  M_{n} = {actual} {formula}")
    print(f"\nSCORE: {matches_ok}/{len(matches)-1}")
    return matches_ok, len(matches)-1


if __name__ == "__main__":
    run()
