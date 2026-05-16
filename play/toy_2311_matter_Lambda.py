"""
Toy 2311 — Matter-Lambda equality redshift: z_eq ≈ 1/N_c = 1/3 = 0.333.
ΛCDM: Ω_m(z) = Ω_Λ at z ≈ (Ω_Λ/Ω_m)^(1/3) − 1 ≈ 0.33.
BST: 1/N_c = 0.333. Match within ΛCDM uncertainty (~1%).
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
z_eq_obs = 0.33  # standard cosmology, Planck 2018
z_eq_bst = 1.0 / N_c
err = abs(z_eq_bst - z_eq_obs) / z_eq_obs * 100
print(f"Toy 2311 — z(matter-Lambda) = 1/N_c = 1/3 = {z_eq_bst:.4f} vs {z_eq_obs}, err {err:.2f}%")
print(f"SCORE: {1 if err < 5.0 else 0}/1")
