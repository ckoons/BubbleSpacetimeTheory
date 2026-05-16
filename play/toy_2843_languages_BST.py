"""
Toy 2843 — Linguistic structural counts BST (observational).

English alphabet: 26 letters = rank·c_3 (= sporadic count, T2127!)
Vowels: 5 = n_C (or 6 with y = C_2)
Consonants: 21 = N_c·g
Cardinal directions: 4 = rank²
8 parts of speech (traditional grammar) = rank³
Punctuation marks (major): 14 = rank·g

Phonetic alphabet (IPA): ~107 consonants + ~46 vowels = 153 ≈ N_max
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13

    lang = [
        ("English alphabet",         26, rank*c_3, "rank·c_3 (= sporadic count!)"),
        ("Vowels (a,e,i,o,u)",       5,  n_C,      "n_C"),
        ("Consonants",               21, N_c*g,    "N_c·g"),
        ("Cardinal directions",      4,  rank**2,  "rank²"),
        ("Traditional parts of speech", 8, rank**3, "rank³"),
        ("Major punctuation marks",  14, rank*g,   "rank·g"),
    ]

    print("Linguistic structural BST:")
    matches = 0
    for name, val, bst, formula in lang:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<30} = {val} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(lang)}")
    return matches, len(lang)


if __name__ == "__main__":
    run()
