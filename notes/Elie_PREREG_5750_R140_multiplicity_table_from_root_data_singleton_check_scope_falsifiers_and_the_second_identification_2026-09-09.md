# PRE-REGISTRATION — Toy 5750, Round 140 (E1, E2). Hashed before the run.

**Elie, 2026-09-09 (Wednesday) 12:33 EDT (shell-copied).**

## The instrument: rebuild, do not quote
For a Hermitian symmetric domain the restricted root system is C_r or BC_r with root spaces ±γ_i ± γ_j (multiplicity **a**), ±γ_i (multiplicity **b**), ±2γ_i (multiplicity 1). Two consequences must both hold if a triple (r, a, b) is the right root data:
  **dim_ℂ = r + a·r(r−1)/2 + b·r**  and  **genus = (r−1)a + b + 2.**
I assign (r, a, b) per family and then TEST both formulas against the independently known dimension and against genus values I measured myself in toy 5746.

## Hashed lines
- **A1 (control):** the dimension formula reproduces every family's dimension: I_{p,q} (r = p, a = 2, b = q−p) → pq; II_n (r = ⌊n/2⌋, a = 4, b = 0 or 2 by parity) → n(n−1)/2; III_n (r = n, a = 1, b = 0) → n(n+1)/2; IV_n (r = 2, a = n−2, b = 0) → n; V (r = 2, a = 6, b = 4) → 16; VI (r = 3, a = 8, b = 0) → 27.
- **A2 (control, cross-instrument):** the genus formula returns **d+1 for the ball B^d and 5 for D_IV⁵** — the two exponents I measured in 5746 by uniform Monte Carlo and by the unit-intensity probe, with no table involved.
- **A3 (can fail):** the multiplicities across the classification are **2, 4, 1, n−2, 6, 8**, so **a = 3 has exactly one solution, D_IV⁵**, with no rank input and no dimension input.
- **A4 (SCOPE, can fail — the caveat I expect to find):** at r = 1 the coefficient r(r−1)/2 is zero, so **a does not enter the root data of a rank-one domain at all**. The rank-one family (the balls I_{1,q}) therefore has no characteristic multiplicity of its own. **Under the family-table convention (type I carries a = 2 at every rank) the balls read a = 2 and are excluded; under the root-system-of-this-domain convention a is undefined there and the criterion is SILENT on them.** Either way D_IV⁵ is the unique solution among domains where a is defined, but **the theorem's scope sentence differs between the two conventions and the row must pick one.** I report both and pick neither.
- **A5 (FALSIFIER, can fail):** reducible domains. A product has a single characteristic multiplicity exactly when all its factors share one, so **D_IV⁵ × D_IV⁵ × … × D_IV⁵ has a = 3 for every number of factors.** **The irreducibility hypothesis is therefore LOAD-BEARING, not decorative**, and the theorem must carry it. Mixed products (D_IV⁵ × B^q) have no single a and are excluded automatically. Non-classical is covered: the Cartan classification of irreducible bounded symmetric domains is complete at six families, four classical and two exceptional, both of which are in the sweep.
- **A6 (E2, can fail):** |{a = 3}| = 1 already, so |{a = 3 and rank + 1 = 3}| = **1, the same domain**. **Adding the generation criterion removes nothing and therefore adds no information: it is a consistency check that passes, and it is explicitly not evidence.** Reported with the count of what rank = 2 leaves on its own (infinitely many families without a dimension cap; I print the capped count too).

Score X/6; A3, A4, A5, A6 can fail.
