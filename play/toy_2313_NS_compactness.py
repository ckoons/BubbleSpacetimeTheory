"""
Toy 2313 — Neutron star compactness: β_NS = GM/Rc² ≈ 1/C_2 = 1/6 = 0.167.
For canonical NS (1.4 M☉, 12 km radius): β = GM/Rc² ≈ 0.17.
BST: 1/C_2 = 1/6 = 0.1667. Match within ~2% of observation.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
beta_obs = 0.17
beta_bst = 1.0 / C_2
err = abs(beta_bst - beta_obs) / beta_obs * 100
print(f"Toy 2313 — β_NS = 1/C_2 = {beta_bst:.4f} vs {beta_obs}, err {err:.2f}%")
print(f"SCORE: {1 if err < 5.0 else 0}/1")
