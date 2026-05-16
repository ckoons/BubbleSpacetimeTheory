"""
Toy 2864 — Atomic spectroscopy: quantum number bounds BST.

Principal quantum number n: 1,2,3,... bounded by n_max ~ N_max=137 for stable
Azimuthal/orbital ℓ: 0..n-1, ranges over n distinct values
Magnetic m_ℓ: -ℓ..+ℓ, 2ℓ+1 values
Spin s: 1/2, m_s ∈ {-1/2, +1/2} = 2 values = rank
Atomic shells filled in periodic table (K..Q): 7 = g
Subshells (s,p,d,f,g): 5 = n_C  (only s,p,d,f used in nature; g pre-stable)
Subshell orbital counts: s=1, p=3, d=5, f=7 → ratio (s,p,d,f) = (1,N_c,n_C,g) ✓ BST cascade!
Maximum electrons per subshell: 2, 6, 10, 14 = rank·{1,N_c,n_C,g} = rank·BST cascade

Periodic table periods: 7 = g ✓
Periodic table groups: 18 = ?  rank·g + rank² = 14+4 = 18 ✓; or c_2·rank-rank-rank = no
                       Try: 18 = 2·g+rank² = 14+4 = 18 ✓
Lanthanides count: 15 = c_2·N_c-rank·c_2-... try N_c·n_C = 15 ✓ EXACT
Actinides count: 15 = N_c·n_C ✓
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13

    spec = [
        ("Spin (m_s values)",          2, rank,    "rank"),
        ("Periodic table periods",     7, g,       "g"),
        ("Periodic table groups",      18, rank*g+rank**2, "rank·g + rank²"),
        ("Subshell types in nature",   4, rank**2, "rank² (s,p,d,f)"),
        ("Subshell types theoretical (incl g)", 5, n_C, "n_C (s,p,d,f,g)"),
        ("Orbitals in s subshell",     1, 1,       "trivial"),
        ("Orbitals in p subshell",     3, N_c,     "N_c"),
        ("Orbitals in d subshell",     5, n_C,     "n_C"),
        ("Orbitals in f subshell",     7, g,       "g"),
        ("Electrons in s",             2, rank,    "rank"),
        ("Electrons in p",             6, C_2,     "C_2"),
        ("Electrons in d",             10, rank*n_C, "rank·n_C"),
        ("Electrons in f",             14, rank*g,  "rank·g"),
        ("Lanthanides count",          15, N_c*n_C, "N_c·n_C"),
        ("Actinides count",            15, N_c*n_C, "N_c·n_C"),
        ("Halogens (Group 17)",        5, n_C,    "n_C (F,Cl,Br,I,At)"),
        ("Noble gases (Group 18)",     6, C_2,    "C_2 (He,Ne,Ar,Kr,Xe,Rn)"),
        ("Alkali metals (Group 1)",    6, C_2,    "C_2 (Li,Na,K,Rb,Cs,Fr)"),
    ]

    print("Atomic spectroscopy + periodic table BST:")
    matches = 0
    for name, val, bst, formula in spec:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else f"(want {val} got {bst})"
        print(f"  {name:<40} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(spec)}")
    return matches, len(spec)


if __name__ == "__main__":
    run()
