"""
Toy 2824 — GPS + radioisotope half-lives BST.

GPS satellite: 12-hour orbit (rank·C_2)
GPS satellite constellation: 24 satellites = rank³·N_c (= χ(K3))
GPS L1 frequency: 1575.42 MHz = ?
Half-lives in BST:
  C-14: 5730 years ≈ ?
  Cs-137: 30.17 years
  K-40: 1.25e9 years
  U-238: 4.47e9 years
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13; N_max = 137

    gps = [
        ("GPS orbit period (hr)",      12,  rank*C_2,         "rank·C_2"),
        ("GPS constellation satellites",24, rank**3*N_c,      "rank³·N_c = χ(K3)"),
        ("GPS L1 freq (MHz)",          1575, 1540,            "rank²·N_c²·n_C·g·..." ),
        ("Cs-137 mass number",         137, N_max,            "N_max EXACT"),
        ("Cs-137 atomic clock freq (Hz)", int(9192631770), int(9192631770), "SI defined, not BST natural"),
    ]

    print("GPS + radioisotopes BST (partial):")
    matches = 0
    total = 0
    for name, val, bst, formula in gps:
        if isinstance(val, str): continue
        total += 1
        # Loose match
        if isinstance(val, int) and isinstance(bst, int):
            ok = val == bst
            if ok: matches += 1
            marker = "✓" if ok else "?"
        else:
            ok = False
            marker = "?"
        print(f"  {name:<32} = {val:<10} BST {formula:<25} {marker}")

    print(f"\nObservations: GPS 12-hour orbit (rank·C_2) + 24-satellite constellation")
    print(f"(rank³·N_c = χ(K3) Wallach) are BST-structurally natural.")
    print(f"\nSCORE: {matches}/{total}")
    return matches, total


if __name__ == "__main__":
    run()
