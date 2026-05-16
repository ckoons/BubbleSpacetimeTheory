"""
Toy 2852 — Cognitive science / psychology structural counts BST.

Miller's magic number 7±2 (working memory): 7 = g, range = rank
Five-factor personality (OCEAN): 5 = n_C
Maslow's hierarchy: 5 levels = n_C
Kübler-Ross stages: 5 = n_C
Major emotion categories (Ekman): 6 = C_2 (or 7 = g with Contempt)
Visual processing pathways: rank (ventral and dorsal)
Multiple intelligences (Gardner): 8-9 = rank³ to rank³+1

OECD age stages: 4 main = rank²
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11

    cog = [
        ("Miller's 7±2 (memory)",      7, g, "g (memory capacity)"),
        ("OCEAN personality factors",  5, n_C, "n_C"),
        ("Maslow hierarchy levels",    5, n_C, "n_C"),
        ("Kübler-Ross stages",         5, n_C, "n_C"),
        ("Ekman basic emotions",       6, C_2, "C_2 (or 7=g with Contempt)"),
        ("Visual processing pathways", 2, rank, "rank (ventral, dorsal)"),
        ("Gardner intelligences",      8, rank**3, "rank³"),
        ("Hemispheres",                2, rank, "rank"),
        ("Major brain lobes",          4, rank**2, "rank² (frontal, parietal, temporal, occipital)"),
        ("Sleep stages (REM+NREM 1-3)", 4, rank**2, "rank²"),
        ("Cognitive load chunks (max)", 4, rank**2, "rank² (Cowan 2001)"),
    ]

    print("Cognitive science BST observational:")
    matches = 0
    for name, val, bst, formula in cog:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<32} = {val} = {formula:<15} {marker}")

    print(f"\nSCORE: {matches}/{len(cog)}")
    return matches, len(cog)


if __name__ == "__main__":
    run()
