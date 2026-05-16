"""
Toy 2292 — Hyperfine/Lamb ratio: HF(H)/Lamb = rank^2/N_c = 4/3.

HF(H) = 1420.405 MHz (21-cm line). Lamb shift L(2S-2P) = 1057.845 MHz.
Ratio = 1.343. BST: rank^2/N_c = 4/3 = 1.333. Match 0.74%.

The ratio 4/3 is the QCD Casimir C_F for the fundamental representation
of SU(N_c), which equals rank^2/N_c in BST identification.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
HF_H = 1420.405
Lamb = 1057.845
ratio_obs = HF_H / Lamb
ratio_bst = rank**2 / N_c
err = abs(ratio_bst - ratio_obs) / ratio_obs * 100
print(f"Toy 2292 — HF(H)/Lamb = rank^2/N_c = 4/3 (Casimir C_F)")
print(f"  Observed: {ratio_obs:.4f}  BST: {ratio_bst:.4f}  err {err:.2f}%")
print(f"  SCORE: {1 if err < 1.0 else 0}/1 ({'PASS' if err < 1.0 else 'FAIL'})")
