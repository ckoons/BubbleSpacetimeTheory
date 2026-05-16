"""
Toy 2302 — Crown glass refractive index: n = N_max/(rank·n_C·N_c²) = 137/90.
n(crown glass) ≈ 1.52 at visible. BST: 137/90 = 1.522. Match 0.15%.
"""
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
n_obs = 1.52
n_bst = N_max / (rank * n_C * N_c**2)
err = abs(n_bst - n_obs) / n_obs * 100
print(f"Toy 2302 — n(crown) = N_max/(rank·n_C·N_c²) = 137/90 = {n_bst:.4f} vs {n_obs}, err {err:.2f}%")
print(f"SCORE: {1 if err < 1.0 else 0}/1")
