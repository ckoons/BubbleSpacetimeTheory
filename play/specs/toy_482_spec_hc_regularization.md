# Toy 482: Harish-Chandra Descent — Regularization at ℓ₁ = ℓ₂

**Assigned to**: Elie
**Spec by**: Lyra (for Casey)
**Date**: March 27, 2026
**Investigation**: I16 — geodesic table completion
**Casey's directive**: "HC isn't useful, it's essential."

---

## Motivation

The Weyl discriminant for root system B₂ with multiplicities m_s = N_c = 3, m_l = 1 is:

```
D(ℓ₁,ℓ₂) = |2sinh(ℓ₁/2)|³ · |2sinh(ℓ₂/2)|³ · |2sinh((ℓ₁+ℓ₂)/2)| · |2sinh((ℓ₁-ℓ₂)/2)|
```

This vanishes on TWO walls:
- **ℓ₂ = 0**: short root wall (rank-1 singularity, already handled)
- **ℓ₁ = ℓ₂**: long root wall (discovered in Toy 476)

The symmetric rank-2 geodesics from Toy 478 (ℓ₁ = ℓ₂ = log(3+2√2)) land EXACTLY on the long root wall. Their naive orbital weight diverges. Harish-Chandra descent provides the correct regularized weight by reducing the singular integral to a rank-1 trace formula on the wall.

This is not a computational trick — it's the geometry coupling rank-1 and rank-2 contributions structurally.

---

## What to Compute

### Part 1: The Long Root Singularity

**T1: Verify the singularity**
- Compute D(ℓ,ℓ+ε) for ε → 0 and show D ~ ε as ε → 0
- The factor |2sinh((ℓ₁-ℓ₂)/2)| ~ |ℓ₁-ℓ₂|/2 as ℓ₁ → ℓ₂
- So the weight ~ 1/ε: a simple pole, not worse

**T2: Laurent expansion near the wall**
- Write the orbital integral I(ℓ₁,ℓ₂,h) near ℓ₁ = ℓ₂ = ℓ:
  ```
  I(ℓ+ε, ℓ-ε, h) = c₋₁(ℓ)/ε + c₀(ℓ) + c₁(ℓ)·ε + O(ε²)
  ```
- Compute c₋₁(ℓ) and c₀(ℓ) explicitly for test function h = heat kernel
- The c₋₁ term is the "rank-1 residue" — it's a rank-1 orbital integral on the wall

### Part 2: Harish-Chandra Descent

**T3: The descent formula**
- On the long root wall ℓ₁ = ℓ₂, the centralizer of the corresponding torus element has a rank-1 Levi component
- The singular orbital integral descends to a rank-1 integral:
  ```
  lim_{ε→0} ε · I(ℓ+ε, ℓ-ε, h) = I_wall(ℓ, h_wall)
  ```
  where h_wall is the Selberg transform restricted to the wall
- For B₂ with m_s = 3, m_l = 1: the wall subgroup is type A₁ with root multiplicity m_s + 2m_l = 5

**T4: Compute the wall integral**
- The rank-1 orbital integral on the wall:
  ```
  I_wall(ℓ) = ℓ / |2sinh(ℓ/2)|^{m_wall}
  ```
  where m_wall = m_s + 2m_l = 3 + 2 = 5 for the long root wall
- This is DIFFERENT from the rank-1 weight in Toy 476 (which had exponent 3 = m_s)
- The exponent 5 comes from the roots that become parallel on the wall

### Part 3: Regularized Rank-2 Weights

**T5: Regularize the symmetric geodesics**
- For each symmetric geodesic (ℓ₁ = ℓ₂ = ℓ_n) from Toy 478:
  ```
  w_reg(ℓ_n) = lim_{ε→0} [I(ℓ_n+ε, ℓ_n-ε, h) - c₋₁(ℓ_n)/ε]
  ```
  This is the FINITE part after subtracting the rank-1 residue
- Compute numerically for ℓ = log(3+2√2) ≈ 1.763 (the fundamental element)
- Show the regularized weight is finite and well-defined

**T6: Compare regularized vs off-wall**
- For ℓ₁ = ℓ + δ, ℓ₂ = ℓ - δ (slightly off-wall):
  - Compute I(ℓ₁, ℓ₂, h) directly (finite, no regularization needed)
  - Show it matches c₋₁/δ + c₀ + O(δ) as δ → 0
  - The c₀ term IS the regularized weight from T5

### Part 4: Updated Geodesic Table

**T7: Rebuild the table with regularized weights**
- Merge the rank-1 geodesics (from Toy 477), the off-wall rank-2 geodesics (from Toy 478), and the regularized symmetric rank-2 geodesics
- All weights should now be finite
- Show the table is consistent: no infinities, correct signs, weights decrease with |ℓ|

**T8: Heat trace convergence**
- Compute K(t) = volume term + Σ_γ w(γ) · ĥ(ℓ(γ)) for t = 0.1, 0.5, 1.0, 5.0
- Compare: with vs without the regularized symmetric geodesics
- The regularized terms should provide a measurable correction at intermediate t
- Show the heat trace is now a COMPLETE sum (no missing contributions from the wall)

---

## Expected Output

8 tests, target 8/8.

Key deliverables:
1. Proof that the singularity is a simple pole (T1-T2)
2. The descent formula with wall multiplicity m_wall = 5 (T3-T4)
3. Finite regularized weights for symmetric geodesics (T5-T6)
4. Complete geodesic table with no infinities (T7-T8)

---

## BST Connection

The long root wall ℓ₁ = ℓ₂ is where the B₂ root system degenerates to A₁. The multiplicity on the wall is m_s + 2m_l = N_c + 2 = 5 = n_C. This is NOT a coincidence: the wall multiplicity equals the dimension parameter. The geometry forces:

- **Off-wall (rank-2)**: see the full B₂ structure, m_s = N_c = 3
- **On-wall (degenerate)**: see A₁ with m = n_C = 5
- **At origin (rank-0)**: see the volume π⁵/1920

All three regimes are controlled by {N_c, n_C}. The Harish-Chandra descent is the map between them.

Casey's insight: HC descent isn't a technicality — it's the MECHANISM by which rank-1 and rank-2 contributions are coupled. Without it, the geodesic table has infinities. With it, you get a complete, finite table that answers every spectral query.

---

## Notes for Elie

- The key reference is Harish-Chandra's "Harmonic analysis on real reductive groups III" (1976), specifically the descent to singular elements. For B₂, the computation is in Herb (1979) "Fourier inversion of invariant integrals on semisimple real Lie groups" — but for our purposes, the Laurent expansion near the wall is sufficient.
- Use mpmath at 50 digits. The cancellation in c₋₁/ε + c₀ can lose precision if ε is too small.
- Take ε = 10⁻⁵, 10⁻⁸, 10⁻¹¹ and verify the extrapolated c₀ is stable.
- The wall multiplicity m_wall = m_s + 2m_l = 5 is the prediction. If you get a different exponent, that's a discovery.
- File: `play/toy_482_hc_regularization.py`
