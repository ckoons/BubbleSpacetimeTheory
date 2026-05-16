"""
Toy 2845 — Visual/literary arts structural counts BST (observational).

Sonnet lines: 14 = rank·g
Haiku syllables: 17 (5-7-5) = c_2+N_c·rank = Ogg17!
Sonata movements: 4 = rank²
Major scale notes: 7 = g
Chromatic scale: 12 = rank·C_2 (T2160 12-EDO)
Symphony orchestra sections: 4 = rank²

Rule of thirds (visual): 3 = N_c
Golden ratio (visual): φ = (1+√n_C)/rank (T2098)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13

    arts = [
        ("Sonnet lines (Shakespearean)", 14, rank*g, "rank·g"),
        ("Haiku syllables (5-7-5 sum)",  17, c_2+N_c*rank, "Ogg17 = c_2+N_c·rank"),
        ("Sonata movements (classical)", 4,  rank**2, "rank²"),
        ("Major scale notes",            7,  g, "g"),
        ("Chromatic scale notes",        12, rank*C_2, "rank·C_2"),
        ("Symphony orchestra sections",  4,  rank**2, "rank²"),
        ("Rule of thirds divisions",     3,  N_c, "N_c"),
    ]

    print("Visual/literary arts BST:")
    matches = 0
    for name, val, bst, formula in arts:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<32} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(arts)}")
    return matches, len(arts)


if __name__ == "__main__":
    run()
