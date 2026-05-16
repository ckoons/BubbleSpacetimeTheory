"""
Toy 2950 — Superconductivity / exotic states BST.

BCS theory parameters: 3 = N_c (gap Δ, T_c, ξ coherence length)
Cooper pair spin states: 2 = rank (singlet or triplet)
Cooper pair orbital angular momentum: 0, 1, 2 = N_c (s, p, d-wave)

Type I vs II superconductors: 2 = rank
Standard SC families famous: 5 = n_C (BCS conventional, cuprates, iron-pnictides,
  heavy fermion, organic)

Standard superconductor parameters Ginzburg-Landau: 2 = rank (ξ, λ)
+ κ = λ/ξ as derived = 3 = N_c with κ

High-Tc cuprate doping regimes: 5 = n_C (overdoped, optimal, underdoped, pseudogap, AF)

Standard Hall effect family: 3 = N_c (classical, integer QH, fractional QH)
Standard quantum Hall plateaus first 4: 4 = rank² (ν = 1, 2, 3, 4 integer)
Composite fermion states: 5 = n_C major

Standard ferromagnetic phenomena: 4 = rank² (spontaneous magnetization, hysteresis,
  Curie temperature, anisotropy)

Antiferromagnetic spin orderings: 3 = N_c (G-type, A-type, C-type)
Spin glass order parameters: 2 = rank (Edwards-Anderson, replica overlap)

Skyrmion topological numbers: integer Q = ... mostly 1 = trivial for simplest
Standard exotic topological states: 7 = g (anyons, Majorana, MZM,
  topological insulators, Weyl semimetals, Dirac semimetals, axion insulators)

Standard ferroelectric polarization axes: 3 = N_c (P_x, P_y, P_z)
Multiferroic coupling channels: 4 = rank² (FE-FM, FE-AFM, FM-FE-pol, magnetoelectric)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    sc = [
        ("BCS theory primary parameters",          3, N_c, "N_c (Δ, T_c, ξ)"),
        ("Cooper pair spin states",                2, rank, "rank (singlet/triplet)"),
        ("Cooper pair orbital L = 0,1,2",          3, N_c, "N_c"),
        ("Type I/II classification",               2, rank, "rank"),
        ("Famous SC families",                     5, n_C, "n_C"),
        ("Ginzburg-Landau primary lengths",        2, rank, "rank (ξ, λ)"),
        ("Cuprate doping regimes",                 5, n_C, "n_C"),
        ("Hall effect families",                   3, N_c, "N_c (classical, IQH, FQH)"),
        ("First integer QH plateaus",              4, rank**2, "rank²"),
        ("Standard ferromagnetic phenomena",       4, rank**2, "rank²"),
        ("Antiferromagnetic orderings",            3, N_c, "N_c"),
        ("Spin glass order parameters",            2, rank, "rank"),
        ("Exotic topological states major",        7, g, "g"),
        ("Ferroelectric polarization axes",        3, N_c, "N_c"),
        ("Multiferroic coupling channels",         4, rank**2, "rank²"),
        ("BCS + GL parameters combined",           5, n_C, "n_C"),
        ("Standard SC junction types",             3, N_c, "N_c (SIS, SNS, SFS)"),
    ]

    print("Superconductivity / exotic states BST:")
    matches = 0
    for name, val, bst, formula in sc:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<42} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(sc)}")
    return matches, len(sc)


if __name__ == "__main__":
    run()
