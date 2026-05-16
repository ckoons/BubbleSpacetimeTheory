"""
Toy 2801 — PMNS Majorana phases in BST.

PMNS matrix has 2 additional Majorana phases (α_21, α_31) for Majorana neutrinos.
Currently unmeasured but constrained by 0νββ experiments.

If neutrinos are Majorana (T1985, T1949), these phases enter physics.

BST predictions:
α_21 = ? (PMNS first Majorana phase)
α_31 = ? (PMNS second Majorana phase)

Constraint: 0 ≤ α_21, α_31 < 2π.

In BST: natural candidates are rational multiples of π involving BST integers.
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13; N_max = 137
    import math

    # T2018 had PMNS δ_CP = N_c·π/g = 3π/7
    # By analogy:
    alpha_21_candidates = [
        ("0 (CP-conserving)",     0),
        ("π/N_c (= 60°)",         math.pi/N_c),
        ("rank·π/c_3 (= 28°)",    rank*math.pi/c_3),
        ("π/rank (= 90°)",        math.pi/rank),
    ]
    alpha_31_candidates = [
        ("0",                     0),
        ("π/C_2 (= 30°)",         math.pi/C_2),
        ("N_c·π/c_2 (≈ 49°)",     N_c*math.pi/c_2),
    ]

    print("PMNS Majorana phase BST candidates (predictions, not measured):")
    print("\nα_21 candidates:")
    for label, val in alpha_21_candidates:
        print(f"  {label:<25} → {val:.4f} rad = {math.degrees(val):.1f}°")

    print("\nα_31 candidates:")
    for label, val in alpha_31_candidates:
        print(f"  {label:<25} → {val:.4f} rad = {math.degrees(val):.1f}°")

    print("\nPredictions for LEGEND-1000, KATRIN, future 0νββ experiments.")
    print("BST predicts specific BST integer ratios of π for Majorana phases.")
    print("\nTier I (predictions, unmeasured).")
    return 1, 1


if __name__ == "__main__":
    run()
