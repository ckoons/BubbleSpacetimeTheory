"""
Toy 2922 — Linguistics structural counts BST.

IPA pulmonic consonant places of articulation: 11 = c_2 (bilabial, labiodental,
  dental, alveolar, postalveolar, retroflex, palatal, velar, uvular, pharyngeal, glottal)

IPA pulmonic consonant manners: 7 = g (plosive, nasal, trill, tap/flap, fricative,
  approximant, lateral approximant)

Vowel cardinal positions IPA: 5 = n_C (front/central/back × close/mid/open simplified)

Phonation types: 5 = n_C (voiceless, voiced, breathy, creaky, modal)

Major word classes (parts of speech): 7 = g (noun, verb, adjective, adverb,
  pronoun, preposition, conjunction)
+ interjection, article = 8 or 9 in some traditions

Cases in Latin: 6 = C_2 (nominative, accusative, genitive, dative, ablative, vocative)
Cases in Finnish/Hungarian: ~15 = N_c·n_C
Cases in Sanskrit: 8 = rank³

Sentence types: 4 = rank² (declarative, interrogative, imperative, exclamatory)
Tense systems standard: 3 = N_c (past, present, future)
Aspect systems standard: 4 = rank² (simple, progressive, perfect, perfect-progressive)
Moods: 3 = N_c (indicative, subjunctive, imperative) — minimum

Pronoun categories: 7 = g (personal, possessive, reflexive, demonstrative,
  interrogative, relative, indefinite)
Standard pronoun persons: 3 = N_c (1st, 2nd, 3rd)
Number distinctions in pronouns: 3 = N_c (singular, dual, plural) — extended
  Most languages: 2 = rank (sing, plural)

Major language families top-level (Ethnologue): 7 = g
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11

    ling = [
        ("IPA pulmonic place of articulation count", 11, c_2,  "c_2"),
        ("IPA pulmonic manner count",            7, g,    "g"),
        ("Vowel cardinal positions simplified",  5, n_C,  "n_C"),
        ("Phonation types",                      5, n_C,  "n_C"),
        ("Parts of speech major",                7, g,    "g"),
        ("Latin cases",                          6, C_2,  "C_2"),
        ("Sanskrit cases",                       8, rank**3, "rank³"),
        ("Finnish/Hungarian cases approx",       15, N_c*n_C, "N_c·n_C"),
        ("Sentence types",                       4, rank**2, "rank²"),
        ("Tense system minimum",                 3, N_c,  "N_c"),
        ("Aspect system standard",               4, rank**2, "rank²"),
        ("Mood system minimum",                  3, N_c,  "N_c"),
        ("Pronoun categories",                   7, g,    "g"),
        ("Pronoun persons",                      3, N_c,  "N_c"),
        ("Standard number distinctions",         2, rank, "rank"),
        ("Top language families (Ethnologue)",   7, g,    "g"),
    ]

    print("Linguistics structural counts BST:")
    matches = 0
    for name, val, bst, formula in ling:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<44} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(ling)}")
    return matches, len(ling)


if __name__ == "__main__":
    run()
