"""
Toy 2316 — 3D SAW susceptibility exponent: γ = g/C_2 = 7/6.
γ(3D SAW) = 1.1568 (Clisby 2010 simulation).
BST: g/C_2 = 7/6 = 1.1667. Match 0.86%.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
gamma_obs = 1.1568
gamma_bst = g / C_2
err = abs(gamma_bst - gamma_obs) / gamma_obs * 100
print(f"Toy 2316 — γ(3D SAW) = g/C_2 = 7/6 = {gamma_bst:.4f} vs {gamma_obs}, err {err:.2f}%")
print(f"SCORE: {1 if err < 1.0 else 0}/1")
