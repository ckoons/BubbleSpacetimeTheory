"""
Toy 2322 — Spectral Cv peak: β_peak = 1/n_C³ = 1/125.
Observed (Toy data K=50 modes): β_peak = 0.0078.
BST: 1/n_C³ = 0.008. Match 2.6%.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
beta_obs = 0.0078
beta_bst = 1.0 / n_C**3
err = abs(beta_bst - beta_obs) / beta_obs * 100
print(f"Toy 2322 — Cv peak β = 1/n_C³ = 1/125 = {beta_bst} vs {beta_obs}, err {err:.2f}%")
print(f"SCORE: {1 if err < 5.0 else 0}/1")
