# PRE-REGISTRATION — Toy 5728, Round 131: T1292 §(g)'s "~10⁴ bits (bounded by f_c coverage per observer × C₂ patches)" — the instrument the fragment lacks

**Elie, 2026-09-08 (Tuesday) 09:13 EDT (shell-copied). Hashed before the run. Cal §907 (4) asked for the rule to be evaluated before the line is called a number.**

- **As written:** f_c × C₂ = (9/47) × 6 = 54/47 ≈ 1.15. No bit-carrying quantity is named; the fragment does not evaluate to 10⁴. (Alias noted for Grace: T1292 uses f_c = 9/47 = 0.19149; Cal §907 wrote 3/(5π) = 0.19099 — two values under one name, 0.26 % apart.)
- **The instrument:** enumerate monomials rank^a · N_c^b · n_C^c · C₂^d · g^e · N_max^h · f_c^s with a..h ∈ {0,1,2}, s ∈ {−1,0,1}, and count those in [10⁴/3, 3·10⁴]. **Hashed: ≥ 20 distinct values land in the window** — so "≈ 10⁴" is reachable by dozens of BST products and the fragment selects none of them; the line is a memory (K 09-06 rule), and Grace's re-tier should carry "no instrument, no formula" rather than a number.
- **Control:** the same window for a random integer target of the same size (e.g. 7,919) must also be hit by ≥ 20 monomials — showing the window, not the target, is doing the work.

Score X/2 (both can fail: the count could come in under 20).
