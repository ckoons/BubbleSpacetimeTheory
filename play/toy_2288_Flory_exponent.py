"""
Toy 2288 — Flory exponent in 3D self-avoiding walks: nu = N_c/n_C = 3/5.

Standard Flory mean-field estimate: nu = 3/(d+2) for d-dim SAW.
For d=3: nu_Flory = 3/5 = 0.600.
BST: N_c/n_C = 3/5 = 0.600. Match exactly.

Modern simulation: nu = 0.5876 (Clisby 2010). 2.06% from Flory.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
nu_simulation = 0.5876   # Clisby 2010
nu_Flory = 3 / 5
nu_bst = N_c / n_C
err_Flory = abs(nu_bst - nu_Flory) / nu_Flory * 100
err_sim = abs(nu_bst - nu_simulation) / nu_simulation * 100
print(f"Toy 2288 — 3D SAW Flory exponent nu = N_c/n_C = 3/5")
print(f"  Flory:      {nu_Flory:.4f}  BST: {nu_bst:.4f}  err {err_Flory:.2f}%")
print(f"  Simulation: {nu_simulation:.4f}  BST: {nu_bst:.4f}  err {err_sim:.2f}%")
print(f"  Match to Flory mean-field: EXACT.")
print(f"  SCORE: {1 if err_sim < 5.0 else 0}/1 ({'PASS' if err_sim < 5.0 else 'FAIL'})")
