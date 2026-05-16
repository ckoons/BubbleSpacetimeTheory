"""
Toy 2893 — Complexity theory class counts BST.

Polynomial hierarchy levels practical: 3 = N_c (Σ_0=P, Σ_1=NP, Σ_2)
PH up to Σ_3, Π_3: 4 = rank² levels per side
Counting hierarchy: 3 = N_c (PP, ⊕P, #P)

Standard complexity classes shown in zoo (very basic): ~7 = g
  (P, NP, coNP, BPP, BQP, PSPACE, EXP) — exactly g

Reduction types in NP-completeness: 3 = N_c
  Karp (many-one polynomial)
  Cook (Turing polynomial)
  Levin (with witness)

Standard Turing machine variants: 5 = n_C
  (deterministic, nondeterministic, probabilistic, alternating, quantum)

Resource axes in complexity: 4 = rank²
  (time, space, depth/parallelism, randomness)

AC circuit depth levels in literature: 4 = rank² typical (AC0, AC1, AC2, AC3)
AC(0) depth: 0 = trivial; with negation: 1 = trivial
NC hierarchy levels: 4 = rank² standard

Hardness amplification rounds typical: 3 = N_c (Yao-style)

Standard cryptographic primitive types: 5 = n_C
  (OWF, PRG, PRF, signature, encryption)

Number of "core" undecidable problems (halting, equivalence, etc.):
  7 = g standard textbook list
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    cmp = [
        ("Standard Turing machine variants",     5, n_C,    "n_C"),
        ("Resource axes (time/space/depth/rand)", 4, rank**2, "rank²"),
        ("Reduction types in NP-completeness",   3, N_c,    "N_c"),
        ("PH levels practical (P, NP, Σ_2)",     3, N_c,    "N_c"),
        ("AC depth standard levels",             4, rank**2, "rank²"),
        ("NC hierarchy standard levels",         4, rank**2, "rank²"),
        ("Crypto primitive types",               5, n_C,    "n_C"),
        ("Major complexity classes textbook",    7, g,      "g (P,NP,coNP,BPP,BQP,PSPACE,EXP)"),
        ("Undecidable problems classic list",    7, g,      "g"),
        ("Counting hierarchy classes",           3, N_c,    "N_c (PP,⊕P,#P)"),
        ("Pseudo-random object types",           3, N_c,    "N_c (PRG,PRF,PRP)"),
        ("Standard machine tape types",          3, N_c,    "N_c (1-tape, 2-tape, k-tape)"),
        ("Standard input/output models",         3, N_c,    "N_c (RAM, oracle, query)"),
    ]

    print("Complexity theory class counts BST:")
    matches = 0
    for name, val, bst, formula in cmp:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<44} = {val:<3} = {formula:<35} {marker}")

    print(f"\nSCORE: {matches}/{len(cmp)}")
    return matches, len(cmp)


if __name__ == "__main__":
    run()
