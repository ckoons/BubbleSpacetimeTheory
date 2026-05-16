"""
Toy 2293 — Isovector anomalous magnetic moment: μ_p − μ_n = 47/10.

μ_p = +2.7928, μ_n = -1.9130. Difference (isovector) = +4.7058.
BST: 47/10 = 4.700. Match 0.12%.
47 is a Monster Ogg prime (in BST Ogg-7 list).
"""
mu_p = 2.792847350
mu_n = -1.91304273
diff_obs = mu_p - mu_n
diff_bst = 47.0 / 10.0
err = abs(diff_bst - diff_obs) / abs(diff_obs) * 100
print(f"Toy 2293 — μ_p − μ_n (isovector) = 47/10")
print(f"  Observed: {diff_obs:.4f}  BST: {diff_bst:.4f}  err {err:.2f}%")
print(f"  Note: 47 = Monster Ogg prime; 10 = rank·n_C")
print(f"  SCORE: {1 if err < 1.0 else 0}/1 ({'PASS' if err < 1.0 else 'FAIL'})")
