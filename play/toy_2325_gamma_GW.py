"""
Toy 2325 — Gravitational-wave spectral index: γ_GW = c_3/n_C + 1 = 18/5 = 3.6.
NANOGrav 15-yr: γ_GW ≈ 3.2-4.6 (consistent with SMBH binary background).
BST: c_3/n_C + 1 = 13/5 + 1 = 18/5 = 3.6. In middle of observed range.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c_3 = 13
gamma_obs_center = 3.9   # midpoint of NANOGrav 15-yr range
gamma_bst = c_3 / n_C + 1
err = abs(gamma_bst - gamma_obs_center) / gamma_obs_center * 100
print(f"Toy 2325 — γ_GW = c_3/n_C + 1 = 18/5 = {gamma_bst} vs {gamma_obs_center} (NANOGrav center), err {err:.2f}%")
print(f"  NANOGrav 15-yr range: 3.2-4.6. BST 3.6 is in range.")
print(f"SCORE: {1 if err < 10.0 else 0}/1")
