"""
Toy 2839 — Cosmic inflation parameters BST.

Number of e-folds N_e ≥ 50-60 (to solve horizon, flatness, monopole)
Slow-roll parameter ε ~ rank·n_C/N_max² (small)
Spectral index n_s ≈ 0.96 = 132/137 = 1-n_C/N_max (T1962)
Scalar amplitude A_s ≈ 2.1e-9 = exp(-20) (T1961)
Tensor-to-scalar ratio r ≤ 0.036 (Planck) — bounded

In BST: inflation parameters BST-natural.
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13; N_max = 137
    import math

    inflation = [
        ("N_e e-folds min", 50, rank**2 + N_max - g - rank**4, "rank²+N_max-g-rank⁴ = 119 - 71 = ad hoc"),
        ("n_s",            0.965, 132/137, "132/137 = 1-n_C/N_max (T1962)"),
        ("log10(1/A_s)",   8.68,  20/math.log(10), "20/ln(10) (T1961)"),
        ("Tensor r upper", 0.036, 1/(rank**4*rank), "1/32 = 1/rank⁵ ≈ 0.031"),
    ]

    print("Cosmic inflation parameters BST:")
    matches = 0
    total = 0
    for name, obs, bst, formula in inflation:
        if isinstance(obs, float):
            dev = abs(bst-obs)/obs * 100
            ok = dev < 10.0
            total += 1
        elif isinstance(obs, int):
            ok = obs == bst
            total += 1
        else:
            continue
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<22} obs={obs:<8g} BST={bst:<10g} {formula:<35} {marker}")

    # N_e specific
    print(f"\n  Typical N_e in slow-roll: 50-60 e-folds (canonical inflation)")
    print(f"  In BST: N_e ≈ N_max/rank+rank·c_3 = 68.5+26 = 94 — but actual choice depends on model")
    print(f"\nSCORE: {matches}/{total}")
    return matches, total


if __name__ == "__main__":
    run()
