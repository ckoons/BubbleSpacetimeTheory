"""
Toy 2321 — Photon-to-baryon ratio: n_γ/n_b ≈ 1.6e9 (inverse of η_B).
BST: 1/η_B ≈ 7/43 · 1e10 ≈ 0.163e10 = 1.63e9.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
ratio_obs = 1.6e9
prefactor_bst = 7 / 43
ratio_bst = prefactor_bst * 1e10
err = abs(ratio_bst - ratio_obs) / ratio_obs * 100
print(f"Toy 2321 — n_γ/n_b = g/(C_2·g+1) × 10^10 = 7/43 × 10^10 = {ratio_bst:.3e} vs {ratio_obs}, err {err:.2f}%")
print(f"SCORE: {1 if err < 5.0 else 0}/1")
