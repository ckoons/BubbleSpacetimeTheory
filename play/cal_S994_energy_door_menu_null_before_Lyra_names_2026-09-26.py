#!/usr/bin/env python3
"""Cal Section 994: the ENERGY-DOOR MENU NULL, written after `date` = 14:58 EDT and hashed BEFORE Lyra names her candidate
tilt-parameter invariant (round 8, Lyra item 3; git log at 14:57 shows no Lyra round-8 commit).

ANTECEDENT, verbatim (K1930 Part 2): "It runs only with the invariant named and hashed BEFORE any comparison to α, against a
menu null of D_IV⁵ invariants of the same complexity (Cal owns the null). α stays IDENTIFIED unless a hashed, null-beaten route
says otherwise."

INVARIANT FIRST: the target is the low-energy fine-structure constant α(0), a dimensionless number with no convention.
Target value used here: α⁻¹(0) = 137.035999177 (CODATA 2022; pin owed from the source before any final ruling; the null's
counts are insensitive below 1e-8 relative).

THE MENU (Wyler-type, fixed now): X = 2^a · 3^b · 5^c · 7^d · π^e with a, b, c ∈ {−5, −4.75, …, 5}, d ∈ {−3, …, 3},
e ∈ {−6, …, 6}, all in quarter steps. It contains every product of the five BST integers, the genus, dim 10, |W(B₂)| = 8, 5! and
Hua's volume π⁵/(2⁴·5!), and all their square and fourth roots. It contains Wyler's formula α_W = (9/(8π⁴))(π⁵/(2⁴·5!))^{1/4}
= 2^{−19/4} 3^{7/4} 5^{−1/4} π^{−11/4}.
COMPLEXITY c(X) = Σ |4·exponent| over {2, 3, 5, 7, π} (quarter-step units). Wyler: 19 + 7 + 1 + 0 + 11 = 38.

PASS RULE (for Lyra's candidate, fixed now):
  (R1) the candidate is named as an invariant of D_IV⁵ with its derivation route, and hashed, before its value is compared with α;
  (R2) let ε = |X_cand − α|/α and c = c(X_cand), where c(X) is computed in THIS menu. If the candidate is not a menu monomial
       (a sum, or another constant), its complexity is the monomial complexity of its most complex term plus 4 per extra term;
  (R3) λ(c, ε) = the number of menu forms with complexity ≤ c lying within relative ε of α. PASS iff λ < 0.01.
       With λ ≥ 1, a random menu form does as well: FAIL. Between the two: at threshold, not credited;
  (R4) a candidate equal to 1/N_max = 1/137 exactly is α's already-identified value and is NOT a new route (it adds nothing);
       any post-hoc radiative correction to close a gap counts as an extra term under R2.

PREDICTIONS (for the null itself, before running):
  N1  the menu at complexity ≤ 38 has more than 10⁶ forms;
  N2  at Wyler's own (c = 38, ε(α_W)), λ lies between 0.3 and 3, so Wyler does NOT pass R3 (calibration: the Wyler formula
      is what an unconstrained search of this menu produces);
  N3  λ scales roughly linearly in ε at fixed c (a smooth log-density), so the table below can be read for any candidate.
"""
import numpy as np

ALPHA = 1 / 137.035999177
la = np.log(ALPHA)
q = np.arange(-20, 21) / 4.0      # -5..5 quarter steps
q7 = np.arange(-12, 13) / 4.0     # -3..3
qp = np.arange(-24, 25) / 4.0     # -6..6
L2, L3, L5, L7, LP = np.log([2, 3, 5, 7, np.pi])

A, B, C = np.meshgrid(q, q, q, indexing="ij")
base_log = (A * L2 + B * L3 + C * L5).ravel()
base_cx = (4 * (np.abs(A) + np.abs(B) + np.abs(C))).ravel().astype(int)

eps_grid = [1e-3, 1e-4, 1e-5, 1e-6, 6e-7, 1e-7]
c_grid = [8, 12, 16, 20, 24, 28, 32, 38, 44, 52, 60]
counts = np.zeros((len(c_grid), len(eps_grid)), dtype=np.int64)
total_by_c = np.zeros(len(c_grid), dtype=np.int64)
for d in q7:
    for e in qp:
        lv = base_log + d * L7 + e * LP
        cx = base_cx + int(round(4 * abs(d))) + int(round(4 * abs(e)))
        rel = np.abs(np.expm1(lv - la))
        for i, cmax in enumerate(c_grid):
            m = cx <= cmax
            total_by_c[i] += m.sum()
            for j, eps in enumerate(eps_grid):
                counts[i, j] += np.count_nonzero(m & (rel <= eps))

wy = 9 / (8 * np.pi**4) * (np.pi**5 / (2**4 * 120)) ** 0.25
eps_w = abs(wy - ALPHA) / ALPHA
wy_menu = 2**(-19/4) * 3**(7/4) * 5**(-1/4) * np.pi**(-11/4)
print(f"Wyler α_W⁻¹ = {1/wy:.6f}; menu form agrees: {np.isclose(wy, wy_menu, rtol=1e-14)}; ε_W = {eps_w:.2e}; c_W = 38")
print("forms with complexity ≤ c:", dict(zip(c_grid, total_by_c.tolist())))
print("λ(c, ε) table: rows c, columns ε =", eps_grid)
for i, cmax in enumerate(c_grid):
    print(f"  c ≤ {cmax:3d}: " + "  ".join(f"{counts[i, j]:>7d}" for j in range(len(eps_grid))))
# λ at Wyler's own point, by counting at ε_W directly
lam_w = 0
for d in q7:
    for e in qp:
        lv = base_log + d * L7 + e * LP
        cx = base_cx + int(round(4 * abs(d))) + int(round(4 * abs(e)))
        lam_w += np.count_nonzero((cx <= 38) & (np.abs(np.expm1(lv - la)) <= eps_w))
print(f"λ(38, ε_W) = {lam_w}  (includes Wyler's own form)")
N1 = total_by_c[c_grid.index(38)] > 1e6
N2 = 0.3 <= lam_w <= 3
col = [counts[c_grid.index(60), j] for j in range(len(eps_grid))]
N3 = col[0] > 0 and 3 < col[0] / max(col[1], 1) < 30
print("SCORE", sum([N1, N2, N3]), "/ 3", {"N1": bool(N1), "N2": bool(N2), "N3": bool(N3)})
