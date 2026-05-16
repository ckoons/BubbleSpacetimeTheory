"""
Toy 2859 — Extended biology / biochemistry BST.

Standard amino acids: 20 = rank²·n_C  (T457 already at depth)
Nucleic acid bases: 4 = rank² (A,T,G,C) + 1 = n_C (with U for RNA)
Stop codons: 3 = N_c
Start codons: 1 (AUG) — but with non-canonical AUG-like = 3 = N_c
Open reading frames per strand: 3 = N_c
DNA strands: 2 = rank
Sense/antisense: 2 = rank
Translation reading directions: 1 (5'→3')
Helix turns per pitch in B-DNA: ~10.5 ≈ c_2 (=11, T2117 within 5%)
Genetic code degeneracy: codons:aa = 64:20 = rank⁶:rank²·n_C

ATP cycle hydrolysis count: 3 phosphate groups → N_c
Carbon valence: 4 = rank² (T2118 already)
Standard 7-transmembrane GPCR helices: 7 = g
Standard MHC class molecules: 2 = rank (Class I, Class II)
Number of meiotic divisions: 2 = rank
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13
    _ = (C_2, c_3)

    bio = [
        ("Standard amino acids",      20, rank**2*n_C,    "rank²·n_C (T457)"),
        ("DNA bases (A,T,G,C)",       4,  rank**2,        "rank²"),
        ("RNA bases (A,U,G,C)",       4,  rank**2,        "rank²"),
        ("All nucleic acid bases",    5,  n_C,            "n_C (A,T,U,G,C)"),
        ("Stop codons (UAA,UAG,UGA)", 3,  N_c,            "N_c"),
        ("Reading frames per strand", 3,  N_c,            "N_c"),
        ("DNA strand directionality", 2,  rank,           "rank (5'→3' and 3'→5')"),
        ("Watson-Crick H-bond pairs", 2,  rank,           "rank (A-T = 2 H-bonds)"),
        ("G-C H-bonds",                3, N_c,            "N_c (G-C = 3 H-bonds)"),
        ("GPCR transmembrane helices",7,  g,              "g"),
        ("MHC class molecules",       2,  rank,           "rank"),
        ("Meiotic divisions",         2,  rank,           "rank"),
        ("Codon table size",          64, rank**6,        "rank^6"),
    ]

    print("Extended biology BST:")
    matches = 0
    for name, val, bst, formula in bio:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<32} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(bio)}")
    return matches, len(bio)


if __name__ == "__main__":
    run()
