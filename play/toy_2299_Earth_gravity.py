"""
Toy 2299 — Earth surface gravity: g_⊕ = rank·n_C − 1/n_C = 49/5 m/s² = 9.8 m/s².

Observed g (45° latitude, sea level): 9.80665 m/s².
BST: rank·n_C − 1/n_C = 10 − 0.2 = 9.800 m/s². Match 0.07%.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
g_obs = 9.80665
g_bst = rank * n_C - 1.0 / n_C
err = abs(g_bst - g_obs) / g_obs * 100
print(f"Toy 2299 — g(Earth) = rank·n_C − 1/n_C = 49/5 m/s²")
print(f"  Observed: {g_obs:.4f} m/s²  BST: {g_bst:.4f} m/s²  err {err:.2f}%")
print(f"  SCORE: {1 if err < 1.0 else 0}/1 ({'PASS' if err < 1.0 else 'FAIL'})")
