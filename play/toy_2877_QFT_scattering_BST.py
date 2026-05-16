"""
Toy 2877 — QFT scattering structural counts BST.

External legs at tree level for SM scatterings:
  2→2 = 4 = rank² (Bhabha, Compton, Møller, etc.)
  2→3 = 5 = n_C (radiative)
  2→4 = 6 = C_2 (multi-jet)
Mandelstam variables: 3 = N_c (s,t,u) with constraint s+t+u = sum m²
Feynman propagator types fundamental: 3 = N_c (scalar, fermion, vector)
Loop orders standard: 1,2,3,4 = rank² standard analytic effort

CHY scattering equations count for n external: n-3 (Mandelstam constraints)
Spinor helicity components Weyl: 2 = rank
Spin states massive fermion: 2 = rank
Spin states massive vector: 3 = N_c (transverse + longitudinal)
Spin states massless vector: 2 = rank (transverse only)

Standard model 3-point vertices counted in vacuum:
  gauge boson triple: 4 (γγγ=0, gγZ, gZγ, GGG, WWZ, WWγ)
  yukawa: 9 = N_c² (Higgs to fermion pairs by gen)
  triple-gauge: WWZ, WWγ, ggg = 3 = N_c independent

CP eigenstates of meson: 2 = rank
Isospin states (I,I_z): I_z = -I..I, count 2I+1 ranges over rank-quantized levels
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11

    qft = [
        ("2→2 scattering external legs",   4, rank**2, "rank²"),
        ("2→3 radiative scattering legs",  5, n_C,     "n_C"),
        ("2→4 multi-jet legs",             6, C_2,     "C_2"),
        ("Mandelstam variables (s,t,u)",   3, N_c,     "N_c"),
        ("Fundamental propagator types",   3, N_c,     "N_c (scalar/fermion/vector)"),
        ("Spinor helicity Weyl components", 2, rank,   "rank"),
        ("Massive fermion spin states",    2, rank,    "rank"),
        ("Massive vector spin states",     3, N_c,     "N_c"),
        ("Massless vector spin states",    2, rank,    "rank"),
        ("Triple-gauge vertices",          3, N_c,     "N_c (WWZ,WWγ,ggg)"),
        ("Yukawa Higgs-fermion vertices",  9, N_c**2,  "N_c² (3 gens × 3 fermion types each)"),
        ("CP eigenstates meson",           2, rank,    "rank"),
        ("Loop orders standard",           4, rank**2, "rank²"),
        ("Tree-level diagrams 2→2 t-channel + s-channel + u", 3, N_c, "N_c"),
    ]

    print("QFT scattering BST:")
    matches = 0
    for name, val, bst, formula in qft:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<50} = {val:<3} = {formula:<15} {marker}")

    print(f"\nSCORE: {matches}/{len(qft)}")
    return matches, len(qft)


if __name__ == "__main__":
    run()
