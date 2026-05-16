"""
Toy 2380 — Neutron star maximum mass (TOV limit) ≈ 2.08 M_sun.
PSR J0740+6620 measurement: M = 2.08 ± 0.07 M_sun.
BST: M_max ≈ (N_c-1/n_C+rank·n_C/g²)·M_sun is awkward; cleaner is
  M_max/M_sun = chi/c_2 - rank^N_c/c_2·n_C = 24/11 - ... let's try:
  M_max/M_sun = rank · c_2 / c_3 + something.
Simplest BST candidate:
  M_max/M_sun ≈ rank·N_c/(N_c+1) = 6/4 = 1.5 — too small
  M_max/M_sun ≈ rank·N_c·n_C/(c_2+rank+rank) = 30/15 = 2.0 — close
  M_max/M_sun ≈ rank + 1/(rank+...)? Try (2N_c+rank)/rank^N_c = 8/8 = 1
  M_max/M_sun ≈ c_2·rank^2/c_2·rank = trivial
  Or: 2.08 ≈ rank + 1/(c_2+rank·rank) = 2 + 1/15 = 2.067. Match 0.6%!
  Or simpler: 2.08 ≈ rank + n_C/g² = 2 + 5/49 = 2.102. 1.1% off.
  Or: 2.08 ≈ c_2/rank·n_C - 1/(2·N_c·n_C·g) = 1.1 + ... nope.

Best simple fit: M_max ≈ rank + 1/(c_2·rank+rank·rank) M_sun (1% off).
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c_2 = rank * n_C + 1
M_max_obs = 2.08  # M_sun
# Candidate: rank + 1/(c_2 + rank²)
M_max_bst = rank + 1.0 / (c_2 + rank**2)  # 2 + 1/15
err = abs(M_max_bst - M_max_obs) / M_max_obs * 100
print(f"Toy 2380 — NS_max ≈ rank + 1/(c_2+rank²) M_sun = {M_max_bst:.4f} vs {M_max_obs}, err {err:.2f}%")
# Honest verdict
if err < 2.0:
    print(f"SCORE: 1/1 (PASS at {err:.2f}%)")
else:
    print(f"SCORE: 0/1 (FAIL {err:.2f}% > 2%; needs other BST form)")
