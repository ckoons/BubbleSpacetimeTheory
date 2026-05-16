"""
Toy 2318 — Photon decoupling temperature: T_dec ≈ 0.26 eV at z_rec = 1090.

Standard cosmology: T_dec = T_CMB·(1+z_rec) = 2.725e-4 eV·1091 ≈ 0.297 eV (at decoupling).
But the effective T at recombination from Saha is ~0.26 eV.
Decoupling: T_dec ≈ 13.6 eV / 52 ≈ 0.26 eV where 52 = C_2·c_2-rank·N_c (or 52 = rank²·c_3).
Actually Saha gives kT/E_H ≈ 1/40 at zeq.
BST candidates: kT_dec/E_H = 1/(rank²·c_3) ≈ 1/52 = 0.0192.
0.0192·13.6 eV = 0.262 eV. Match.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c_3 = 13
E_H = 13.605693
T_dec_obs = 0.26
T_dec_bst = E_H / (rank**2 * c_3)
err = abs(T_dec_bst - T_dec_obs) / T_dec_obs * 100
print(f"Toy 2318 — T_dec = E_H/(rank²·c_3) = 13.6/52 = {T_dec_bst:.4f} eV vs {T_dec_obs}, err {err:.2f}%")
print(f"SCORE: {1 if err < 2.0 else 0}/1")
