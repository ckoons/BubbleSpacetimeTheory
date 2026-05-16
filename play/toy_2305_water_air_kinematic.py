"""
Toy 2305 — Water/air kinematic viscosity: nu(water)/nu(air) = 1/(N_c·n_C) = 1/15.
nu(water, 20°C) ≈ 1.0e-6 m²/s. nu(air, 20°C) ≈ 1.51e-5 m²/s.
Ratio = 0.0662. BST: 1/(N_c·n_C) = 1/15 = 0.0667. Match 0.7%.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
nu_water = 1.0e-6
nu_air = 1.51e-5
ratio_obs = nu_water / nu_air
ratio_bst = 1.0 / (N_c * n_C)
err = abs(ratio_bst - ratio_obs) / ratio_obs * 100
print(f"Toy 2305 — nu(water)/nu(air) = 1/(N_c·n_C) = 1/15 = {ratio_bst:.4f} vs {ratio_obs:.4f}, err {err:.2f}%")
print(f"SCORE: {1 if err < 1.0 else 0}/1")
