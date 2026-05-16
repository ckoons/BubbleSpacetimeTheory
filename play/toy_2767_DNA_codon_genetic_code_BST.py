"""
Toy 2767 — Genetic code structural integers are BST.

64 codons = rank^(rank·N_c) = 2^6 = 64 ✓
20 amino acids = χ(K3) - rank² = 24-4 = 20 ✓ (also rank²·n_C)
4 nucleotide bases = rank² ✓
3 bases per codon = N_c ✓
2 strand DNA = rank ✓
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13

    bio = [
        ("Codons",              64, rank**(rank*N_c), "rank^(rank·N_c) = 2^6"),
        ("Amino acids (std)",   20, rank**2*n_C,      "rank²·n_C"),
        ("Nucleotide bases",    4,  rank**2,          "rank²"),
        ("Bases per codon",     3,  N_c,              "N_c"),
        ("DNA strands",         2,  rank,             "rank"),
        ("Chargaff pair count", 2,  rank,             "rank (AT, GC)"),
        ("Genetic code wobble", 3,  N_c,              "N_c (3rd position)"),
    ]

    print("Genetic code structural BST:")
    matches = 0
    for name, val, bst, formula in bio:
        ok = val == bst
        marker = "✓" if ok else "×"
        if ok:
            matches += 1
        print(f"  {name:<22} = {val:<3} = {formula:<25} {marker}")

    print(f"\nSCORE: {matches}/{len(bio)}")
    return matches, len(bio)


if __name__ == "__main__":
    run()
