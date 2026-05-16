"""
Toy 2281 — N2/O2 vibrational frequency ratio: omega(N2)/omega(O2) = N_c/rank.

Mechanism: Diatomic vibrational frequency omega = sqrt(k/mu), where k is
the bond strength and mu is reduced mass. N_2 has triple bond, O_2 has
double bond + slightly heavier. omega(N_2) ≈ 2358 cm^-1, omega(O_2) ≈ 1580
cm^-1. Ratio = 1.493.
BST: N_c/rank = 3/2 = 1.500. Match 0.5%.
"""

rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
omega_N2 = 2358.57  # cm^-1
omega_O2 = 1580.19  # cm^-1
ratio_obs = omega_N2 / omega_O2
ratio_bst = N_c / rank

err = abs(ratio_bst - ratio_obs) / ratio_obs * 100

print(f"Toy 2281 — omega(N2)/omega(O2) = N_c/rank = 3/2")
print(f"  Observed: {ratio_obs:.4f}")
print(f"  BST: {ratio_bst:.4f}")
print(f"  Precision: {err:.2f}%")
print(f"  SCORE: {1 if err < 1.0 else 0}/1 ({'PASS' if err < 1.0 else 'FAIL'})")
