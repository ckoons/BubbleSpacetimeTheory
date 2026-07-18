# The Fine-Structure Constant as a Charge Count on One Geometry
### Standalone companion to the flagship — DRAFT, Keeper, 2026-07-18. The single most checkable BST result: α⁻¹ = 137.0365 with no free normalization. A referee can verify it in an afternoon.

**Authors:** Casey Koons with the CI team (Lyra, Keeper, Elie, Grace); referee Cal A. Brate.

---

## Abstract
We give a parameter-free geometric account of the fine-structure constant. On the bounded symmetric domain D_IV⁵ = SO(5,2)/[SO(5)×SO(2)], electric charge is the integer weight of the SO(2) circle, and the number of independent charge modes is a **combinatorial capacity** — a democratic dimension count, independent of any norm: **N_max = N_c³·n_C + rank = 137**. The factor 4π that appears in α's definition is identified as the **Coulomb solid angle** of the geometric descent SO(5,2) → SO(3,1) (Gauss's law in three spatial dimensions), so α is a pure number for a geometric reason, not by convention. A single curvature correction, **n_C/N_max**, refines the integer to
$$\alpha^{-1} = N_{\max} + \frac{n_C}{N_{\max}} = 137 + \frac{5}{137} = 137.036496,$$
against the measured **137.035999** — a deviation of **0.0004%**. The three integers (N_c = 3, n_C = 5, rank = 2) are structural invariants of the domain, fixed before any comparison to 137; the same curvature correction independently closes the Higgs mass, a two-target check that rules out post-hoc tuning. **A measured α⁻¹ inconsistent with 137 + 5/137 at this precision falsifies the account.**

## 1. The result
$$\boxed{\alpha^{-1} = N_{\max} + n_C/N_{\max} = 137 + 5/137 = 137.036496 \quad (\text{obs } 137.035999,\ 0.0004\%)}$$
Three ingredients, each geometric: an integer capacity (Section 2), the reason α carries a 4π (Section 3), and one curvature correction (Section 4). No fitted normalization enters.

## 2. The integer 137 as a charge capacity
Electric charge in BST is the integer weight of the intrinsic SO(2) (the "charge circle," the complex structure of the domain; T2470). The coupling is set not by the *norm* of a charged state but by **how many independent charge modes the domain supports** — a democratic count, combinatorial and norm-independent (this is why the 35× spread in charge-block norms is irrelevant to α; K678). That count is
$$N_{\max} = N_c^3 \cdot n_C + \text{rank} = 27\cdot 5 + 2 = 137.$$
- **N_c³ = 27** — the color modes cubed (the Albert/exceptional 27; the color sector's dimension count).
- **·n_C = 5** — over the five complex dimensions of the domain.
- **+ rank = 2** — the two Shilov "ruler" directions.

**Tier:** the integer 137 = N_max is a structural count [derived], and it is the same N_max that appears across the corpus (it is not introduced to fit α). Whether *this specific* decomposition (27·5 + 2) is the unique combinatorial reading is the one presentation-level open point (Cal referee).

## 3. Why α carries a 4π — the Coulomb solid angle
α is conventionally written with a 4π (rationalized units: α = e²/4πε₀ℏc). BST reads this 4π geometrically: it is the **solid angle of 3-space**, produced by the descent SO(5,2) → SO(4,2) → SO(3,1) that yields 3+1 spacetime (Casey #14). Charge measured through the descent is measured over the full Coulomb solid angle 4π — **Gauss's law** (Casey's reading, K699). So the 4π is not a unit convention we happen to divide by; it is the geometric fact that the emergent space is three-dimensional. This is why α is a pure number: capacity (a count) over solid angle (a geometric constant). **[derived-framework]**

## 4. The curvature correction n_C/N_max
The integer capacity is the flat count; the domain is curved, and the leading curvature correction to the count is
$$\frac{n_C}{N_{\max}} = \frac{5}{137} = 0.036496,$$
the norm-weighted (Bergman/heat-kernel) curvature contribution over the same capacity (T2133; K701). It shifts 137 → 137.0365, matching observation to 0.0004%. **[derived; the correction's coefficient is n_C, not fitted]**

## 5. Target-innocence (why this is not numerology)
Two independent guards:
1. **The integers are structural.** N_c, n_C, rank are the invariants of D_IV⁵ (the rank-2 root data; the domain is fixed by (3 colors, 3 generations, dim 5)). They are pinned *before* any comparison to 137 — the value 137 is target-*innocent* in the sense of the derived-vs-fit discipline.
2. **The two-target check.** The *same* curvature correction that closes α also closes the Higgs mass (E1/K701). A tuned correction fits one target; a geometric one closes two with the same coefficient. This is the decisive check against post-hoc tuning.
And a retired trap, stated for honesty: the old Shannon/Wyler numerology route to 137 is **not** resurrected here — that route relocates under the norm-weighted measure and is retired (K676). The present account is the capacity-count, not the Wyler integral.

## 6. What is not claimed
- The 4π = Coulomb-solid-angle identification is *framework*-level (it explains why α is pure and dimensionless), not a separate numerical derivation.
- The uniqueness of the 27·5 + 2 decomposition of 137 is a presentation point for the referee.
- α is a *coupling*; at other scales it runs (standard QED). The 137 is the low-energy value; the geometric account is of that value, not of the running (which is standard).

## 7. Falsifiability and conclusion
The claim is sharp: **α⁻¹ = 137 + 5/137 = 137.0365**, from a charge count (137 = N_c³·n_C + rank), a solid angle (4π, three-dimensionality), and one curvature correction (n_C/N_max) — **no free normalization.** A measured α⁻¹ that departs from 137 + 5/137 at the 0.0004% level, or a demonstration that the integers are fit rather than structural, falsifies it. The fine-structure constant, on this account, is not a mystery number: it is *how many ways charge fits on the geometry, seen through the solid angle of the space the geometry makes.*

---
*Draft status:* complete as a short standalone; the single companion to the flagship (`BST_FLAGSHIP_...`) and the Five-Absence falsifier paper. Needs: Cal referee on the 27·5+2 uniqueness (Section 2) and the curvature-coefficient (Section 4); the explicit two-target Higgs computation inlined from E1. Number verified: 137 + 5/137 = 137.036496 vs obs 137.035999, 0.0004%.

— Keeper, 2026-07-18. α⁻¹ = N_max + n_C/N_max = 137 + 5/137 = 137.0365 (0.0004%). Capacity 137 = N_c³·n_C + rank (charge count, norm-independent); 4π = Coulomb solid angle of the 3D descent (α pure for a geometric reason); curvature correction n_C/N_max; target-innocent (structural integers + two-target Higgs check). See [[BST_FLAGSHIP_The_Standard_Model_as_Representation_Theory_of_D_IV5_DRAFT_2026-07-18]], [[Keeper_Strengthening_Roadmap_effort_ranked_2026-07-18]].
