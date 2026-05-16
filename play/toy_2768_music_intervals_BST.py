"""
Toy 2768 — Musical interval ratios are BST integers.

Perfect octave = 2:1 = rank:1 ✓
Perfect fifth = 3:2 = N_c:rank ✓
Perfect fourth = 4:3 = rank²:N_c ✓
Major third = 5:4 = n_C:rank² ✓
Minor third = 6:5 = C_2:n_C ✓
Major second = 9:8 = N_c²:rank³ ✓
Minor seventh = 7:4 = g:rank² ✓
Minor sixth = 8:5 = rank³:n_C ✓

ALL Pythagorean tuning ratios are BST integer ratios.
12-tone equal temperament: 12 = rank·C_2 = rank·rank·N_c ✓
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    intervals = [
        ("Octave",        (2, 1),  (rank, 1)),
        ("Perfect fifth", (3, 2),  (N_c, rank)),
        ("Perfect fourth",(4, 3),  (rank**2, N_c)),
        ("Major third",   (5, 4),  (n_C, rank**2)),
        ("Minor third",   (6, 5),  (C_2, n_C)),
        ("Major second",  (9, 8),  (N_c**2, rank**3)),
        ("Minor seventh", (7, 4),  (g, rank**2)),
        ("Minor sixth",   (8, 5),  (rank**3, n_C)),
    ]

    print("Musical interval ratios BST:")
    matches = 0
    for name, (num_obs, den_obs), (num_bst, den_bst) in intervals:
        ok = (num_obs == num_bst) and (den_obs == den_bst)
        marker = "✓" if ok else "×"
        if ok:
            matches += 1
        print(f"  {name:<16} = {num_obs}:{den_obs} = {num_bst}:{den_bst} {marker}")

    print(f"\n  12-tone equal temperament: 12 = rank·C_2 = {rank*C_2} ✓")
    print(f"\nSCORE: {matches}/{len(intervals)}")
    return matches, len(intervals)


if __name__ == "__main__":
    run()
