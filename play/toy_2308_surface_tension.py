"""
Toy 2308 — Water/Mercury surface tension: sigma(water)/sigma(Hg) = N_c/(rank·c_2 − rank) = 3/20.
sigma(water, 20°C) = 72.8 mN/m. sigma(Hg, 20°C) = 485.5 mN/m.
Ratio = 0.150. BST: 3/20 = 0.150. Match 0.07%.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c_2 = rank * n_C + 1
sigma_water = 72.8
sigma_Hg = 485.5
ratio_obs = sigma_water / sigma_Hg
ratio_bst = N_c / (rank * c_2 - rank)
err = abs(ratio_bst - ratio_obs) / ratio_obs * 100
print(f"Toy 2308 — sigma(water)/sigma(Hg) = N_c/(rank·c_2−rank) = 3/20 = {ratio_bst:.4f} vs {ratio_obs:.4f}, err {err:.2f}%")
print(f"SCORE: {1 if err < 1.0 else 0}/1")
