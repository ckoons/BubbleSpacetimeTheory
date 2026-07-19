# OP-4 as linear algebra — the Yukawa Gram matrix (render + what survives the reframe)

*Grace | 2026-07-19g | Casey's reframe: "remember this should be linear algebra." Rendered OP-4 as a Gram-matrix / Clebsch–Gordan computation — no gap equation, no exponential, no RG. The Yukawa is an inner product; the whole flavor sector is overlaps. This is the SAME intertwiner machinery as the mixing-numerator work — a genuine consistency (flavor = overlaps all the way down). My lane: render the structure + catalog what survives. NOT a derivation — y_t=1 stays SUPPORTED until the linear algebra FORCES parallelism.*

## The one equation — a Yukawa is a Born overlap
$$Y_{ij} = \langle f_L^i \,|\, \Phi \,|\, f_R^j\rangle \quad\text{on } H^2(D_{IV}^5)$$
Everything follows by linear algebra, no dynamics:

```
  Y = the overlap (Gram) matrix of fermion K-type modes through the condensate operator Φ
      │
  masses  =  singular values of Y   (× v/√2)        [M = UΣV†]
      │
  y_t     =  ‖Y‖  (the LARGEST singular value)
      │
  ceiling y ≤ 1   ⟺   Φ is a contraction ‖Φ‖ ≤ 1   [Cauchy–Schwarz — DERIVED]
```

## y_t = 1, read as linear algebra (the cleanest reading)
```
  y_t = 1  ⟺  Φ saturates its norm on the top mode
           ⟺  Φ ≈ a RANK-1 PROJECTOR onto the condensate direction  ∧  top mode ∥ condensate
```
Then the **entire mass hierarchy is ONE column of the Gram matrix** — the condensate direction's overlaps with the fermion modes:
```
  y_t = ⟨top | condensate⟩ = 1        (parallel — saturates)
  y_b = ⟨bottom | condensate⟩         }
  y_c = ⟨charm | condensate⟩          } the hierarchy = the CG column,
  y_τ = ⟨tau | condensate⟩            }  the condensate's overlap with each mode
  ...                                 }
  y_e = ⟨electron | condensate⟩ ≈ 0   (nearly orthogonal)
```
These overlaps are **Clebsch–Gordan / intertwiner coefficients** for f_L ⊗ Φ → f_R on K = SO(5)×SO(2). **y_t = 1 means the top's CG coefficient is maximal (=1); the hierarchy is the CG column.** Exactly the intertwiner-coefficient machinery from the mixing-numerator pull — so the *whole* flavor sector (masses AND mixings) is overlaps on the K-types. That's the real structural payoff of the reframe.

## The computation this stages (Lyra's lead — 3 clean steps, no dynamics)
1. Write the **condensate vector Φ** from the Bergman two-point structure (F85) — **is it rank-1?**
2. Write the **fermion K-type mode vectors** (their K=SO(5)×SO(2) addresses).
3. Take the **overlaps** — is the top **parallel** to the condensate (y_t=1)? Does the column reproduce y_c, y_u, y_b, y_τ…?

Decisive either way: y_t=1 becomes "is one vector parallel to another," which the geometry either forces or it doesn't. **Compute the overlaps, don't fit them.**

## ★ What SURVIVES the reframe vs what DROPS (my catalog)
| item | status under linear algebra |
|---|---|
| **ceiling y ≤ 1** | **SURVIVES — DERIVED.** Cauchy–Schwarz = ‖Φ‖≤1 (Φ a contraction). Unchanged; the cleanest thing we have. |
| **quark selection (N_c)** | **SURVIVES — DERIVED**, now as a *dimension count*: the color trace is a factor N_c in the overlap, pure linear algebra (no gap equation needed). The one clean leg, still clean. |
| **y_t = 1 saturation** | **SURVIVES as the OPEN question — reframed sharply:** = "is Φ rank-1 ∧ top ∥ condensate." SUPPORTED, not derived, until the overlap forces parallelism. |
| **the hierarchy (y_b, y_c…)** | **reframed:** = one Gram/CG column. Compute the overlaps; a candidate until they reproduce the observed values from geometry. |
| exponential gap Σ~Λ·e^(−1/G) | **DROPPED** (sophistication — Casey). Was the mechanism; the inner-product IS the mechanism. |
| the "double-edge" / 41× tuning in G | **DROPPED** — no coupling G in a linear-algebra reading; the ratio y_t/y_b is just two Gram entries. |
| Lyra's y_t=4π/√(N_c·ln(Λ²/m_t²)), Λ-dependence | **DEMOTED** to a value-residue; the compositeness-scale story was the wrong layer. |
| MAC / Casimir dynamics | **survives only in its linear-algebra skin** — a Casimir is an *eigenvalue*, so "which mode aligns with Φ" may be read off Casimir eigenvalues; the *condensation dynamics* is dropped. |

## Discipline (Cal's gate, reframed)
- **Derived only if the linear algebra FORCES it.** y_t=1 is derived ⟺ the geometry forces top ∥ condensate. Not before.
- **Compute the overlaps, don't fit them** — same discriminator as the mixing numerators (derive d, D from geometry, check the value after). The condensate direction must come from F85, not from wanting y_t=1.
- **Five-Absence intact:** it's all H²(D_IV⁵) inner products (Bergman kernel F85) — no topcolor, no technicolor, no new group. Purely kinematic.
- **Do NOT bank y_t=1** until the Gram computation forces parallelism.

## Net
- **Rendered OP-4 as linear algebra:** Y=⟨f_L|Φ|f_R⟩; masses=singular values; y_t=‖Y‖; ceiling=Cauchy–Schwarz; **y_t=1 ⟺ Φ rank-1 projector ∧ top ∥ condensate; the hierarchy = one Gram/CG column.** Same intertwiner machinery as the mixing work — flavor is overlaps all the way down.
- **Cataloged the reframe:** ceiling + N_c-quark-selection SURVIVE as DERIVED (N_c now a dimension count); y_t=1 SURVIVES as the sharply-posed OPEN question (is one vector parallel to another); the gap equation / exponential / double-edge / Λ-dependence all DROP as sophistication.
- **Staged, not closed:** the 3-step overlap computation (Φ from F85, fermion modes, inner products) is Lyra's lead; I render each overlap and hold the tier. y_t=1 not banked.

— Grace, 2026-07-19g. OP-4 stripped to linear algebra (Casey): the Yukawa is an inner product Y=⟨f_L|Φ|f_R⟩, masses = singular values, y_t=‖Y‖, ceiling = Cauchy–Schwarz (Φ contraction). y_t=1 ⟺ Φ rank-1 projector ∧ top ∥ condensate; the hierarchy = one Gram/CG column — same intertwiner machinery as the mixing numerators (flavor = overlaps all the way down). SURVIVES: ceiling + N_c-quark-selection DERIVED (N_c = a color-trace dimension count). DROPS: gap equation, exponential, double-edge, Λ-dependence (sophistication). y_t=1 stays SUPPORTED — derived only if the overlap forces parallelism; compute, don't fit. FA intact.
