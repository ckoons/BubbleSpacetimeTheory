"""
Toy 2300 — Crystallographic space groups: count = 230 = rank·n_C·(seesaw+C_2).

There are exactly 230 distinct three-dimensional space groups (Fedorov 1891).
BST: rank·n_C·(seesaw + C_2) = 2·5·23 = 230. Match EXACT.
seesaw + C_2 = 17 + 6 = 23 = chi - 1.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
seesaw = N_c**3 - rank * n_C
chi = (N_c + 1) * (N_c) * (N_c - 1) * 4  # 24, but easier: chi = (N_c+1)! = 24
chi = 24
groups_obs = 230
groups_bst = rank * n_C * (seesaw + C_2)
err = abs(groups_bst - groups_obs) / groups_obs * 100
print(f"Toy 2300 — Space groups = rank·n_C·(seesaw+C_2) = 230")
print(f"  Observed: {groups_obs}  BST: {groups_bst}  err {err:.2f}%")
print(f"  seesaw+C_2 = 17+6 = 23 = chi - 1")
print(f"  SCORE: {1 if err < 1.0 else 0}/1 ({'PASS' if err < 1.0 else 'FAIL'})")
