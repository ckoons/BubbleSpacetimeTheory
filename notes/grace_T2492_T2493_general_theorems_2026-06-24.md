---
title: "Two general derivation-tool theorems registered to the graph (Casey directive: add general theorems that flatten future work). T2492 — Substrate Multiplicity Theorem (FDOSS = Wigner-Eckart completeness): the realized multiplicity of any supported operator = exactly its spectrum-allowed irreducible components, all and only. T2493 — Plancherel Wall-Convergence Lemma: the spherical/Plancherel inversion on D_IV⁵ converges through every restricted-root wall automatically (short-root density vanishes to order 2, multiplicity-independent), so no convergence side-condition is ever needed in a D_IV⁵ spectral argument."
author: "Grace"
date: "2026-06-24 Wednesday"
theorems: [T2492, T2493]
---

# Two general derivation-tool theorems

Per Casey: register general theorems I've used successfully that **flatten** (reduce future derivations to a
lookup) and fit the graph. Both below were used today and are operator-class-/sector-general.

## T2492 — Substrate Multiplicity Theorem (FDOSS = Wigner-Eckart completeness)

> **On the substrate's faithful, complete representation H²(D_IV⁵) (spectrum = the SO₀(5,2) discrete series,
> T2490), the realized multiplicity of any supported operator O equals EXACTLY its spectrum-allowed irreducible
> components — ALL of them and ONLY them.**
>
> Proof (one line): Wigner-Eckart gives ⟨f|O_c|i⟩ = CG · reduced. Faithfulness ⟹ reduced ≠ 0 (ALL); CG selection
> ⟹ out-of-spectrum targets vanish (ONLY). □

**What it flattens (the derivation tool):** any "how many states / channels does X have?" question reduces to
two lookups — (1) decompose X into irreducibles, (2) keep the components whose target rep is in the discrete-series
spectrum. No dynamics needed. FDOSS = the "all" half; **Five-Absence = the "only" half** (now a corollary); the
operator-class "driver" (Clebsch-Gordan / Pauli-antisymmetrized / strata / overlap) is just the decomposition rule.

**Used successfully today:** glueball 4 channels + oddball absence (gauge F⊗F); hypercharge Y realized + Z′ absent
(Cartan); 3 generations + no 4th (strata). AC = (C=1, D=1), depth 0 (theorem-application/identity). Tier:
STANDING-pending the per-operator-class faithful-closure citation (A3), standard for the Hardy space.

## T2493 — Plancherel Wall-Convergence Lemma (D_IV⁵)

> **The spherical/Plancherel inversion on D_IV⁵ converges through every restricted-root wall automatically: the
> Harish-Chandra density |c(λ)|⁻² vanishes at the short-root wall to order 2, independent of the multiplicity
> m_s (m_s enters the constant C_s, not the exponent). Order-2 vanishing is integrable in the rank-2 chamber, so
> the wall-regularized ε→0 limit always commutes with the λ-integral.**
>
> Proof: |c_{α_s}|⁻² = |Γ(½(½m_s+1+iλ_s))|²·|Γ(½(½m_s+iλ_s))|²·(λ_s sinh πλ_s / π) → const(m_s)·λ_s² as λ_s→0.
> (Classical: the same order-2 vanishing holds for hyperbolic spaces H^{m+1} of any m.) □

**What it flattens:** any spectral/OS/heat-trace argument on D_IV⁵ no longer needs a Plancherel-convergence
side-condition at the walls — it is automatic for all multiplicities. (Today it retired the Paper B R3 "backstop"
as vacuous and showed Path A/T1829 carries the uniqueness alone.) AC = (C=1, D=1), depth 0 (explicit c-function
computation). Tier: SOLID (standard harmonic analysis).

## Graph connections

- **T2492** → T2490 (supplies the spectrum), T1239/Wigner-Eckart (the engine), Five-Absence (now its corollary),
  SWPP (completeness condition), Paper A glueball channels, the hypercharge/generation sectors.
- **T2493** → the OS-data/spectral nodes (T1438 OS axioms, the HS-mirror T2489), Paper B (retires R3), the
  Harish-Chandra c-function machinery.

— Grace, 2026-06-24 Wednesday. Two general tools registered; for Keeper registry + Cal cold-read. Count HOLDS 4.
