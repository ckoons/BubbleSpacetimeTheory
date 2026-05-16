"""
Toy 2306 — N2 dissociation energy: D(N2) = M_g/c_3 = 127/13 eV = 9.769 eV.
Observed D_0(N2) = 9.79 eV (NIST). Match 0.21%.
M_g = 2^g - 1 = 127 (Mersenne); c_3 = 13.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c_3 = 13
M_g = 2**g - 1
D_obs = 9.79
D_bst = M_g / c_3
err = abs(D_bst - D_obs) / D_obs * 100
print(f"Toy 2306 — D(N2) = M_g/c_3 = 127/13 eV = {D_bst:.4f} eV vs {D_obs}, err {err:.2f}%")
print(f"SCORE: {1 if err < 1.0 else 0}/1")
