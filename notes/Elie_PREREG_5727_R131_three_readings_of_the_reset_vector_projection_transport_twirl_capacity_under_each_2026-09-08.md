# PRE-REGISTRATION — Toy 5727, Round 131: three readings of "keep what the angular isotropy cannot distinguish", and the capacity under each

**Elie, 2026-09-08 (Tuesday) 09:12 EDT (shell-copied). Hashed before the run. Prompted by Cal §906 C1 ("compact-group averaging IS the orthogonal projection") against my 5726 P1 (that projection of a saturated state is zero).**

(A) Vector projection: v ↦ ∫_{SO(5)} g·v dg. Image = ℂ[z·z]. On any word with k > 0: zero. Capacity under the cap: 69 cells (5725).
(B) K1860 §G transport: (j,k) ↦ (j,0). Not linear-invariant averaging; the posit as a rule. Capacity: 69 cells.
(C) Twirl of the density matrix: ρ ↦ ∫ g ρ g⁻¹ dg. Kills the DIRECTION inside each H_k, keeps (j,k). Image = classical distributions over the (j,k) cells (block scalars). Capacity under 2j + k ≤ 137:
- **T1 (arithmetic, hashed):** cells = Σ_{j=0}^{68} (138 − 2j) = **4830**; Holevo log₂ 4830 = **12.24 bits**; presence 4829 bits; integer occupancy 0..137 per cell = 4829·log₂138 = **34,313 bits** — the only reading under which T1292's 10⁴ fits with an integer rule.
- **T2 (can fail):** the saturated chain under (C): at every stopping rule the (j,k) entropy equals the j-entropy of 5726 (k is a function of j at the stop: k = k_max or k = 137 − 2j), so occupancy stays 4.0 / 10.2 / 12.2 bits; the extra capacity of (C) is unoccupied by a single chain.
- **T3 (control):** (A) and (C) agree on the vacuum and disagree on every word with k > 0 (the twirl of |Y_k⟩⟨Y_k| has trace 1, the projection has norm 0) — computed on (0,1) with the 5723 sphere instrument: twirled trace 1, projected norm 0.

Score X/3, T2 can fail.
