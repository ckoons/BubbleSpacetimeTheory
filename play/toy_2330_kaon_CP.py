"""
Toy 2330 — Kaon CP violation: |epsilon_K| ≈ 2.228e-3 (PDG).
BST: |epsilon_K| ≈ 1/(C_2·g·c_2) = 1/462 ≈ 2.16e-3? close to obs.
Or: 2.228e-3 ≈ alpha · g/N_c = (1/137)·(7/3) = 0.0170, no.
Better: 2.228e-3 ≈ (rank·c_2)/N_max² = 22/18769 ≈ 1.17e-3, no.
Try: 2.228e-3 ≈ 1/(rank·n_C·c_2·rank²) = 1/440? Try 1/449 = 2.227e-3.
449 = 4·N_max-99 — not clean. Or 449 prime.
Honest: kaon eps_K depends on CKM phase delta_KM = 1.196 rad which BST
identifies as delta = (chi+rank)/c_2 ≈ 26/11 ≈ 2.36. Off by ~2x — too big.

This one MIGHT not have a clean BST mechanism at I→D precision. /route...
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c_2 = rank * n_C + 1
eps_K_obs = 2.228e-3

# Trial decomposition: 1/(C_2·g·c_2) = 1/462
eps_bst_trial1 = 1.0 / (C_2 * g * c_2)
err1 = abs(eps_bst_trial1 - eps_K_obs) / eps_K_obs * 100

# 1/(rank·C_2·c_2 + rank^N_c·N_c) = 1/(132+24) = 1/156 too big
# 5α³ = 5/(137³) = 1.95e-6 too small

# Best: 1/449 ≈ 2.227e-3. 449 prime. 449 = N_max·N_c + N_c·... = 411+38=449. 411 = 3·137 = N_c·N_max. 449 - N_c·N_max = 38 = rank·c_2·...
# Actually 449 = 411 + 38 = N_c·N_max + 38. 38 = rank·c_2 + rank·rank^N_c·... no.
# 449 = 7·N_max - 510? 510-449=61. 7·137=959. No.

eps_bst_best = 1.0 / 449
err_best = abs(eps_bst_best - eps_K_obs) / eps_K_obs * 100

print(f"Toy 2330 — Kaon |ε_K| ≈ 2.228e-3")
print(f"  BST trial: 1/(C_2·g·c_2) = 1/462 = {eps_bst_trial1:.4e}, err {err1:.2f}% (FAIL >5%)")
print(f"  BST candidate: 1/449 = {eps_bst_best:.4e}, err {err_best:.2f}%")
print(f"  449 has no clean BST decomposition I can find rapidly.")
print(f"  /route exhausted in <10 min: NO clean BST mechanism found at <2%.")
print(f"  Honest verdict: STAYS I-tier (or downgrade S-tier if mechanism absent).")
print(f"SCORE: 0/1 (mechanism not closed)")
