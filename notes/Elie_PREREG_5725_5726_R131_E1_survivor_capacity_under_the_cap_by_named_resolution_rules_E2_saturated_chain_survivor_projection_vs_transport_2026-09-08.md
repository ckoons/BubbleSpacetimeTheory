# PRE-REGISTRATION — Toys 5725 (E1) and 5726 (E2), Round 131. Hashed before either runs.

**Elie, 2026-09-08 (Tuesday) 09:08 EDT (shell-copied).**

## E1 — Toy 5725: the survivor's capacity under the cap, as a RANGE with each resolution rule named
Survivor space S = SO(5)-invariants of H²(D_IV⁵) = ℂ[z·z] = span{(z·z)^j}; cap 2j ≤ N_max = 137.
- **H1:** modes j = 0..68 → **69 modes = 68 + the vacuum** (Keeper's figure verified or not).
- **H2, the rules and their numbers (all exact arithmetic):**
  (R0) distinguishable pure states = dim S ⇒ Holevo capacity log₂ 69 = **6.11 bits**;
  (R1) one presence bit per non-vacuum mode ⇒ **68 bits**;
  (R2) integer occupancy 0..137 per non-vacuum mode ⇒ 68·log₂ 138 = **483 bits**;
  (R3) continuous amplitudes: a ray in S has **136 real parameters** (dim_ℝ ℂP⁶⁸ = 2·68) — at resolution ε per parameter the content is 136·log₂(1/ε), unbounded as a rule; to hold T1292's 10⁴ bits every parameter must be resolved to **≈ 2^(−73.5)** relative.
  **Range: 6 bits (R0) to 483 bits (R2); 10⁴ only under R3 at 73.5 bits per real parameter.** Shared-number trap named before reading: 136 = N_max − 1 is the real dimension of a projective 69-space, not a BST count.
- **H3 (can fail):** the Hardy norms ‖(z·z)^j‖² are NOT equal across j (computed from the S¹ × S⁴ measure or from 5722's Gram instrument at the Hardy parameter); so "one bit per mode" presumes a normalisation the space does not supply — reported as a seam, with the norm ratios printed.

## E2 — Toy 5726: the saturated 3/7 chain's survivor
Chain (K1860 l.45/75): from the vacuum (0,0); per write, matter (j+1, k−1) w.p. k/(2k+3), light (j, k+1) w.p. (k+3)/(2k+3); every write raises m = 2j+k by 1. Stopping rules run side by side: (S-k68) first k = 68; (S-k137) first k = 137; (S-m137) m = 137 (exactly 137 writes). Exact DP over (j,k) with mass check ≥ 1 − 10⁻¹².
Two reset maps, both reported: **(A) the orthogonal projection onto ℂ[z·z]** (kills every word with k > 0); **(B) K1860 §G's transport (j,k) ↦ (j,0)** (angular degree to zero, windings carried).
- **P0 positive control (can fail):** the light-only chain (matter probability set to 0) gives j = 0 surely: survivor = vacuum only, entropy exactly 0, under both maps.
- **P1 (exact, can fail):** under (A) with S-k68 and S-k137 the survivor is the ZERO vector — the reset fires at k = k_max > 0, so the projection of the state onto k = 0 vanishes identically. Under S-m137 the surviving norm fraction is P(k = 0 at m = 137) = P(j = 68.5) = **0** as well (m odd ⇒ k odd). So under the orthogonal projection every saturated survivor is the zero vector; the posit's content is exactly the transport (B).
- **P2 (hashed ranges, can fail) under (B):** S-m137: j-entropy in **[3, 6] bits**, j ≤ 68 by construction; S-k137: E[j] in **[500, 5000]**, P(j > 68) > 0.99, j-entropy in **[8, 14] bits** — i.e. the saturated chain's windings OVERFLOW the E1 cap unless the cap is on m. S-k68: E[j] in [100, 1500].
- **P3 (occupancy vs capacity):** every entropy above ≤ log₂ 69 = 6.11 bits only for S-m137; the k-capped chains exceed R0 and land far below R2 (483) and 10⁴.

Score E1 X/3, E2 X/4; can-fail: H3, P0, P1, P2.
