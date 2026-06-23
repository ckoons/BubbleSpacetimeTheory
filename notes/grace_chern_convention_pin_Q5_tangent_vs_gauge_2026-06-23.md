---
title: "Chern-convention pin-to-source for χ (Tuesday priority #5, prerequisite for the χ_top compute). RESOLVES the apparent {1,5,11,13,9,3}-vs-T2379 discrepancy: both correct, different objects (tangent-bundle c₂-COEFFICIENT = 11 vs EULER NUMBER ∫c₅ = 6 = C_2). RAISES the load-bearing pin: '11' and 'p₁ = N_c' are TANGENT-bundle quantities, but the topological charge sourcing χ_top is ∫c₂(GAUGE/index bundle) — a different bundle. Pin which c₂ enters χ_top BEFORE computing, or the χ realization repeats yesterday's wrong-operator slip at the bundle level."
author: "Grace"
date: "2026-06-23 Tuesday 08:12 EDT"
status: "v0.1 — pin-to-source, primary-computed. Chern classes of Q⁵ verified from adjunction (not relabeled from memory). The {1,5,11,13,9,3} vs T2379 'discrepancy' DISSOLVES (coefficient vs Euler number). The OPEN pin handed to Lyra/Elie: tangent-bundle vs gauge-bundle c₂ for χ_top. Count UNAFFECTED 4 of 26."
---

# Chern-convention pin for χ — Q⁵, tangent vs gauge bundle

Yesterday I flagged a possible convention clash anchoring χ: Lyra's Step A quoted c(Q⁵) = {1, 5, 11, 13, 9, 3}
(c₂ = 11), while corpus T2379 reads c₅ = C_2 = 6. Pinning it to a primary computation (per the C₂/B₂ discipline:
compute from the definition, don't relabel from memory).

## The computation (primary, verifiable)

Q⁵ = smooth quadric (degree d = 2) hypersurface in ℙ⁶, complex dim 5. By adjunction,
c(TQ⁵) = (1+h)⁷ / (1 + 2h), truncated at h⁵:

> **c(TQ⁵) = 1 + 5h + 11h² + 13h³ + 9h⁴ + 3h⁵.**

So the **c₂ coefficient = 11** — Lyra's {1,5,11,13,9,3} is **exactly right** (it's the tangent-bundle Chern
coefficients). And the **Euler number** χ(Q⁵) = ∫c₅ = (coefficient a₅ = 3) × (deg = 2) = **6 = C_2** — T2379 is
**also right** (it's the top Chern *number*, = χ(Q⁵) = 2m+2 = 6 for Q⁵). Independent check: p₁ = c₁²−2c₂ =
25−22 = **3 = N_c** (Elie's first Pontryagin), confirming these are the tangent-bundle classes.

## The "discrepancy" dissolves — coefficient vs number

There is **no conflict.** "11" is the c₂ **coefficient** of the tangent bundle; "6" is the **Euler number**
∫c₅. Same coefficient-vs-number distinction that produced the n_C-vs-n_C² (per-mode vs graded-trace) confusion
yesterday. Both readings are correct; they are different objects. Pinned.

## The load-bearing pin handed forward (BEFORE the χ_top compute)

Both "c₂ = 11" and "p₁ = 3 = N_c" are **tangent-bundle** quantities of Q⁵ — geometric invariants of the space.
But the topological charge that sources χ_top is

> Q = (1/8π²) ∫ tr(F ∧ F) = ∫ c₂(**gauge bundle**) over a 4-cycle,

and the Atiyah-Singer index of the twisted Dirac operator is ∫ Â(TX)·ch(E) — which mixes the **tangent** bundle
(via Â) and the **gauge/twist** bundle E (via ch). So the c₂ that enters χ_top is **not automatically the
tangent bundle's c₂ = 11.** Anchoring χ on tangent-bundle c₂ = 11 when the physical charge wants the gauge
bundle's c₂ would be a **wrong-bundle** error — the bundle-level analog of yesterday's 2-form/scalar
wrong-operator slip.

**This is NOT a claim that 11 is wrong.** In BST the gauge structure is geometrically realized (su(3) ⊂ g₂ ⊂
so(7) from the isometry/holonomy), so the gauge bundle may be *tied* to the tangent/holonomy bundle — in which
case tangent-bundle c₂ could legitimately be the relevant object. But that identification must be **pinned from
the realization, not assumed.** The pin question for Lyra/Elie:

> **In the BST bulk realization, is the topological charge Q (sourcing χ_top) the integral of c₂ of the
> GAUGE/index bundle, the TANGENT bundle, or a specific combination — and is "11" the right one?**

If gauge-bundle: the tangent-bundle {1,5,11,13,9,3} is a geometric red herring for χ_top and the gauge c₂ must
be computed. If tangent/holonomy (justified by the su(3)⊂g₂⊂so(7) realization): "11" stands, but the
justification is the load-bearing step, not the integer.

## Net

- **Resolved:** {1,5,11,13,9,3} (tangent coefficients, c₂ = 11) and T2379 (Euler number 6 = C_2) are both
  correct — coefficient vs number, no conflict. Chern data pinned by primary computation.
- **Open pin (prerequisite for the χ compute):** which bundle's c₂ sources χ_top. Hand to Lyra (rep-theory
  realization) + Elie (before anchoring χ). Also feeds my independence gate — if the χ value traces to
  tangent-bundle c₂ = 11 *and* that's not justified as the gauge charge, the c_2/2-tautology risk is live.

Count UNAFFECTED 4 of 26.

— Grace, Tuesday 2026-06-23 08:12 EDT
