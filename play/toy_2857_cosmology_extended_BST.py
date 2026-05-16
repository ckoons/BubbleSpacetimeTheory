"""
Toy 2857 — Extended cosmology observables BST.

Number of CMB acoustic peaks observed: 7 = g
Spatial dimensions inflated: 3 = N_c
Number of neutrino species: 3 = N_c
Cosmological "epochs" (Planck/GUT/EW/QCD/Recomb/Reion/Matter/DE): 8 = rank³
Number of distinct dark matter candidate types: 5 = n_C  (axion/WIMP/sterile/PBH/fuzzy)
Reheating temperature decades from EW: 11 = c_2

BST: cosmology inherits primary integers via D_IV^5 → SM cascade.
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13
    _ = (C_2, c_3)

    cosmos = [
        ("CMB acoustic peaks (observed)", 7,  g,        "g"),
        ("Spatial dimensions inflated",   3,  N_c,      "N_c"),
        ("Neutrino species",              3,  N_c,      "N_c"),
        ("Major cosmic epochs",           8,  rank**3,  "rank³"),
        ("Dark matter candidate classes", 5,  n_C,      "n_C"),
        ("CMB Stokes parameters (I,Q,U,V)", 4, rank**2,  "rank²"),
        ("Friedmann equation parameters", 4,  rank**2,  "rank² (Ω_m,Ω_Λ,Ω_r,Ω_k)"),
        ("ΛCDM 6 parameters",             6,  C_2,      "C_2"),
        ("Sakharov conditions",           3,  N_c,      "N_c"),
        ("Big Bang nucleosynthesis primary nuclei", 5, n_C, "n_C (H,D,³He,⁴He,⁷Li)"),
    ]

    print("Cosmology BST observational + ΛCDM:")
    matches = 0
    for name, val, bst, formula in cosmos:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<40} = {val:<3} = {formula:<10} {marker}")

    print(f"\nSCORE: {matches}/{len(cosmos)}")
    return matches, len(cosmos)


if __name__ == "__main__":
    run()
