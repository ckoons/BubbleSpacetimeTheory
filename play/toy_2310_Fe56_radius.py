"""
Toy 2310 — Fe-56 nuclear radius / r_0: r(Fe56)/r_0 = N_c − 1/(rank·n_C·g) = 209/70.
r(Fe56) ≈ 3.737 fm. r_0 = 1.25 fm.
Ratio = 2.990. BST: N_c − 1/(rank·n_C·g) = 3 − 1/70 = 209/70 = 2.986. Match 0.13%.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
r_Fe56 = 3.737
r_0 = 1.25
ratio_obs = r_Fe56 / r_0
ratio_bst = N_c - 1.0 / (rank * n_C * g)
err = abs(ratio_bst - ratio_obs) / ratio_obs * 100
print(f"Toy 2310 — r(Fe56)/r_0 = N_c − 1/(rank·n_C·g) = 209/70 = {ratio_bst:.4f} vs {ratio_obs:.4f}, err {err:.2f}%")
print(f"SCORE: {1 if err < 1.0 else 0}/1")
