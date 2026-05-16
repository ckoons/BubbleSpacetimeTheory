"""
Toy 2284 — N2/CO frequency ratio: omega(N2)/omega(CO) = c_3/(rank*C_2) = 13/12.

omega(N2) = 2358.57 cm^-1, omega(CO) = 2169.81 cm^-1.
Observed ratio = 1.0870. BST: c_3/(rank*C_2) = 13/12 = 1.0833. Match 0.34%.
c_3 = N_c + n_C + n_C = 13 (third Chern).
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c_3 = 13
ratio_obs = 2358.57 / 2169.81
ratio_bst = c_3 / (rank * C_2)
err = abs(ratio_bst - ratio_obs) / ratio_obs * 100
print(f"Toy 2284 — omega(N2)/omega(CO) = c_3/(rank*C_2) = 13/12")
print(f"  Observed: {ratio_obs:.4f}  BST: {ratio_bst:.4f}  err {err:.2f}%")
print(f"  SCORE: {1 if err < 1.0 else 0}/1 ({'PASS' if err < 1.0 else 'FAIL'})")
