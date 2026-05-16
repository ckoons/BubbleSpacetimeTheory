"""
Toy 2297 — pp-chain Q-value: rank·c_3 + g/(rank·n_C) = 267/10 MeV = 26.7 MeV.

Hydrogen → helium fusion in stars releases 26.73 MeV per 4 protons (pp chain).
BST: rank·c_3 + g/(rank·n_C) = 2·13 + 7/10 = 26.7 MeV. Match 0.11%.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c_3 = 13
Q_pp_obs = 26.731  # MeV (Bahcall 1989)
Q_pp_bst = rank * c_3 + g / (rank * n_C)
err = abs(Q_pp_bst - Q_pp_obs) / Q_pp_obs * 100
print(f"Toy 2297 — pp chain Q = rank·c_3 + g/(rank·n_C) = 267/10 MeV")
print(f"  Observed: {Q_pp_obs:.3f} MeV  BST: {Q_pp_bst:.4f} MeV  err {err:.2f}%")
print(f"  SCORE: {1 if err < 1.0 else 0}/1 ({'PASS' if err < 1.0 else 'FAIL'})")
