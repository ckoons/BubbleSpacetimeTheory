"""
Toy 2817 — More cosmological observables BST.

CMB temperature: 2.725 K = ? (Wien)
CMB photon energy: 2.348e-4 eV
CMB power spectrum tilt: n_s ≈ 0.965 = 132/137 (T1962)

Baryon-to-photon ratio: η = 6.1e-10
Recombination redshift: z_rec ≈ 1090 = ?
Last scattering surface optical depth: τ = 0.054 ≈ 1/Ogg19
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13; N_max = 137

    cos = [
        ("CMB n_s",          0.9635,  132/137,           "1 - n_C/N_max (T1962)"),
        ("CMB optical depth τ", 0.054,  1/(N_c**3-rank**3), "1/Ogg19"),
        ("CMB recomb z_rec", 1090,    rank**3*N_max,     "rank³·N_max = 1096 (0.5% off)"),
        ("CMB Sound horizon", 147,    N_max+rank*n_C,    "N_max+rank·n_C (Elie)"),
    ]

    print("Extended cosmological BST:")
    matches = 0
    for name, val, bst, formula in cos:
        if isinstance(val, float) or isinstance(bst, float):
            dev = abs(val - bst) / val * 100
            ok = dev < 5.0
        else:
            ok = val == bst
            dev = 0
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<22} obs={val:<10g} BST={bst:<10g} {formula:<30} {marker}")

    print(f"\nSCORE: {matches}/{len(cos)}")
    return matches, len(cos)


if __name__ == "__main__":
    run()
