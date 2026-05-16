"""
Toy 2279 — He ionization energy ratio: IE(He)/Ry = N_c^2/n_C.

Mechanism: He+ ground state has Z=2 → IE/Ry = Z^2 = 4 (hydrogenic).
He neutral ionization is 24.587 eV. Ry = 13.606 eV. Ratio = 1.807.
BST: N_c^2/n_C = 9/5 = 1.800. Match 0.4%.

The BST identification: He IE / Ry ≈ N_c^2/n_C reflects two-electron
correlation lowering the effective Z² = 4 by a factor 5/9 (n_C/N_c²)
which is consistent with the screening reduction.
"""

rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
Ry = 13.605693  # eV
IE_He_obs = 24.587387  # eV (NIST)

ratio_obs = IE_He_obs / Ry
ratio_bst = N_c**2 / n_C
err = abs(ratio_bst - ratio_obs) / ratio_obs * 100

print(f"Toy 2279 — He IE / Ry = N_c^2/n_C")
print(f"  Observed: {ratio_obs:.4f}")
print(f"  BST: N_c^2/n_C = 9/5 = {ratio_bst:.4f}")
print(f"  Precision: {err:.2f}%")
print(f"  SCORE: {1 if err < 1.0 else 0}/1 ({'PASS' if err < 1.0 else 'FAIL'})")
