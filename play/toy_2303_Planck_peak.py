"""
Toy 2303 — Planck spectrum frequency peak: x_peak = rank + N_c²/c_2 = 31/11.
Wien's displacement (frequency form): x_peak = hν/kT solves x = 3(1−e^{−x}).
Numerical x_peak ≈ 2.821. BST: rank + N_c²/c_2 = 2 + 9/11 = 2.818. Match 0.10%.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c_2 = rank * n_C + 1
x_obs = 2.821
x_bst = rank + N_c**2 / c_2
err = abs(x_bst - x_obs) / x_obs * 100
print(f"Toy 2303 — Planck x_peak = rank + N_c²/c_2 = 31/11 = {x_bst:.4f} vs {x_obs}, err {err:.2f}%")
print(f"SCORE: {1 if err < 1.0 else 0}/1")
