"""
Toy 2871 — Electromagnetism structural counts BST.

Maxwell's equations: 4 = rank² (Gauss-E, Gauss-B, Faraday, Ampère-Maxwell)
Maxwell tensor F^μν components independent: 6 = C_2 (3 E + 3 B)
Stress-energy tensor symmetric 4×4 components: 10 = rank·n_C
Photon polarization states (physical): 2 = rank (transverse)
Photon polarization states (gauge): 4 = rank² (Lorenz gauge)
Lorentz group dimension: 6 = C_2 (3 rotations + 3 boosts)
Poincaré group dimension: 10 = rank·n_C (6 Lorentz + 4 translation)

Electric multipole orders to dipole: rank+1 = N_c (monopole, dipole)
Magnetic multipole orders: N_c (dipole, quadrupole, octupole standardly)
Faraday's law components: 3 = N_c
Maxwell stress tensor components: 9 = N_c²
Magnetic moment quantum numbers: 4 = rank² (n,ℓ,m_ℓ,m_s) → atomic
Bohr magneton dimensionless powers in α expansion: 2 = rank (μ_B = eℏ/2m)

Larmor precession frequencies: 2 = rank (electron, proton couples)
Number of macroscopic EM media classes: 4 = rank² (vac, dielectric, magnetic, conducting)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    em = [
        ("Maxwell's equations",              4,  rank**2,  "rank²"),
        ("F^μν indep components",            6,  C_2,      "C_2"),
        ("Stress-energy T^μν symmetric",     10, rank*n_C, "rank·n_C"),
        ("Photon physical polarizations",    2,  rank,     "rank"),
        ("Photon Lorenz-gauge polarizations", 4, rank**2,  "rank²"),
        ("Lorentz group dimension",          6,  C_2,      "C_2"),
        ("Poincaré group dimension",         10, rank*n_C, "rank·n_C"),
        ("Faraday's law components",         3,  N_c,      "N_c"),
        ("Maxwell stress tensor components", 9,  N_c**2,   "N_c²"),
        ("Bohr magneton μ_B parameters",     2,  rank,     "rank (e and ℏ/2m)"),
        ("Macroscopic EM media classes",     4,  rank**2,  "rank²"),
        ("Magnetic monopole charge quantization Dirac", 2, rank, "rank (eg=ħc/2)"),
    ]

    print("Electromagnetism BST:")
    matches = 0
    for name, val, bst, formula in em:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<42} = {val:<3} = {formula:<15} {marker}")

    print(f"\nSCORE: {matches}/{len(em)}")
    return matches, len(em)


if __name__ == "__main__":
    run()
