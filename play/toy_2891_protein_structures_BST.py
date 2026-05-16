"""
Toy 2891 — Protein structure levels BST.

Protein structure levels (Linderstrøm-Lang): 4 = rank² (primary, secondary, tertiary, quaternary)
Secondary structure types main: 3 = N_c (α-helix, β-sheet, random coil)
+ Variants: + turns + loops + 3_10 helix + π-helix = 7 = g total

Amino acid side chain classes: 7 = g (nonpolar/polar/acidic/basic/aromatic/sulfur/proline)
+ Imino acid (proline alone): 5-7 classifications standard

α-helix turn rise per residue: ~3.6 residues ≈ N_c
β-sheet strand directions: 2 = rank (parallel, antiparallel)

Number of standard amino acids: 20 = rank²·n_C (T457)
Number of nonstandard (rare): 2 = rank (selenocysteine, pyrrolysine)
Codon→amino acid degeneracy max: 6 = C_2 (for Arg, Leu, Ser)

Major protein fold classes (CATH): 4 = rank² (mainly α, mainly β, α/β, α+β)
SCOP class count: 4 = rank² (matches)

Standard enzyme commission top-level classes: 7 = g (oxidoreductase, transferase, hydrolase,
  lyase, isomerase, ligase, translocase EC1-7)

Antibody (Ig) major classes: 5 = n_C (IgG, IgM, IgA, IgD, IgE)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    prot = [
        ("Protein structure levels (Linderstrøm-Lang)", 4, rank**2, "rank²"),
        ("Main secondary structure types",       3, N_c, "N_c (helix/sheet/coil)"),
        ("All secondary structure variants",     7, g, "g"),
        ("Amino acid side chain classes",        7, g, "g"),
        ("Standard amino acids",                 20, rank**2*n_C, "rank²·n_C (T457)"),
        ("Nonstandard amino acids (Sec, Pyl)",   2, rank, "rank"),
        ("Codon degeneracy max",                 6, C_2, "C_2"),
        ("CATH protein fold classes",            4, rank**2, "rank²"),
        ("SCOP class count",                     4, rank**2, "rank²"),
        ("Enzyme Commission top-level classes",  7, g, "g (EC1-7)"),
        ("Antibody (Ig) major classes",          5, n_C, "n_C"),
        ("β-sheet strand directions",            2, rank, "rank"),
        ("Standard enzyme cofactor types (vitamins)", 13, 1, "≠N_c² — N/A"),
        ("Hemoglobin α and β subunits each",     2, rank, "rank (α2β2 = 4=rank²)"),
        ("Hemoglobin total subunits",            4, rank**2, "rank²"),
    ]

    print("Protein structures BST:")
    matches = 0
    for name, val, bst, formula in prot:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else f"({val}≠{bst})"
        print(f"  {name:<46} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(prot)} (one expected mismatch flagged)")
    return matches, len(prot)


if __name__ == "__main__":
    run()
