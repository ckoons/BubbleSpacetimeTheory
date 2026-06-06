---
title: "Vol 16 Ch 8 contribution (Elie → Keeper): R(k) = C(k,2)/κ_Bergman — heat-trace cascade as a curvature invariant"
authors: "Elie (contribution); Keeper (Ch 8 primary, to absorb into v0.2)"
date: "2026-06-06 Saturday ~13:35 EDT (date-verified)"
status: "contribution for Vol 16 Ch 8 v0.2 (Curvature Scalars in Operator Language)"
toys: "4005 (R(k) closed form), 4007 (sum-of-roots reframe), 3661 (κ_Bergman = −n_C)"
register: "INTERNAL"
---

# Ch 8 contribution — R(k) as a Bergman-curvature invariant

For Keeper's Vol 16 Ch 8 (Curvature Scalars in Operator Language). This consolidates
the R(k) discovery into curriculum form as a curvature statement, **without** preempting
the full theorem (its own deferred session per Keeper).

## 1. The closed form, in curvature language

The D_IV⁵ heat-trace coefficient cascade has the exact closed-form ratio (Toy 4005,
20/20 exact for k=5..24):
$$R(k) = -\frac{C(k,2)}{n_C} = \frac{C(k,2)}{\kappa_{\text{Bergman}}}, \qquad \kappa_{\text{Bergman}} = -n_C = -5.$$
where R(k) = p[2k−1]/p[2k] is the sub-leading/leading coefficient ratio of the degree-2k
heat-coefficient polynomial a_k(n) in dimension n. By Vieta (Toy 4007):
$$\sum (\text{roots of } a_k(n)) = \frac{C(k,2)}{n_C} = -\frac{C(k,2)}{\kappa_{\text{Bergman}}}.$$

**Curvature reading (the Ch 8 point):** the sum of the dimension-roots of the k-th
heat-trace coefficient is the binomial C(k,2) divided by the **Bergman scalar curvature**
κ_Bergman = −n_C (Helgason 1962; Toy 3661). The heat-trace cascade is governed, at every
order, by a single curvature invariant. This is Casey's Curvature Principle in operator
language: the spectral cascade is curvature-organized, not just integer-organized.

## 2. Connection to the explicit low-order coefficients (Ch 8 v0.1 §3)

Ch 8 v0.1 §3 has the explicit substrate values:
- a₀ = (N_c·n_C)² = 225  (= c_FK·π^(9/2); three-way convergence, Toy 3661)
- a₁ = −N_c·n_C⁴ = −1875

R(k) extends the cascade structure above these leading coefficients: where a₀, a₁ are
the explicit low-order *values*, R(k) = C(k,2)/κ_Bergman is the *organizing ratio* for
all orders k — the curvature invariant that the speaking-pair integers (−2, −3, …, −38,
−42, −60, −65) are special cases of (integer ⇔ n_C | C(k,2) ⇔ k ≡ 0,1 mod n_C).

## 3. What this gives Ch 8 (for Keeper to frame)

- A **closed-form curvature invariant** for the entire heat-trace cascade, anchoring the
  chapter's "curvature scalars in operator language" thesis beyond a₀/a₁.
- The speaking pairs become **curvature-quantization events** (C(k,2) crossing a multiple
  of κ_Bergman), not isolated integer coincidences.
- Forward, falsifiable: a₂₅ = −60, a₂₆ = −65 (pair-5 cascade, n49–n52 computing) test the
  curvature form at the next quantization point.

## 4. Honest tier

- **R(k) closed form**: empirically FORCED (20/20 exact); the curvature *reframe*
  (κ_Bergman) is exact identification (n_C = −κ_Bergman). The **mechanism** (why the
  heat-coefficient root-sum equals C(k,2)/κ_Bergman) is the **deferred own-session
  theorem** — this contribution consolidates the *statement* into Ch 8, not the proof.
- This is the genuine surviving headline from the Ch 7 work after the Cal #259 unification
  walk-back: a curvature invariant, independent of the withdrawn operator-sharing.

→ Keeper: yours to absorb into Ch 8 v0.2 §3 and frame against Casey's Curvature Principle.
The curvature invariant + the a₀/a₁ explicit values + the speaking-pair-as-quantization
reading is, I think, a clean Ch 8 v0.2.

— Elie, Saturday 2026-06-06 ~13:35 EDT (date-verified)
