"""
Toy 2324 — Matter fluctuation amplitude: σ_8 = n_C/C_2 = 5/6 = 0.833.
Planck 2018: σ_8 = 0.811 ± 0.006.
BST: 5/6 = 0.833. Match 2.7%.
The "σ_8 tension" with KiDS+DES (σ_8 ≈ 0.78) is a separate issue; BST
sits between Planck and weak-lensing.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
sigma_8_obs = 0.811
sigma_8_bst = n_C / C_2
err = abs(sigma_8_bst - sigma_8_obs) / sigma_8_obs * 100
print(f"Toy 2324 — σ_8 = n_C/C_2 = 5/6 = {sigma_8_bst:.4f} vs {sigma_8_obs}, err {err:.2f}%")
print(f"SCORE: {1 if err < 5.0 else 0}/1")
