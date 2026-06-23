---
title: "T2490 — The Discrete-Series Spectrum Theorem: the four dynamical substrate primaries {N_c, n_C, C_2, g} are EXACTLY the half-Casimirs of the four lowest non-trivial holomorphic discrete-series representations of SO₀(5,2), in increasing order. Equivalently, the glueball linear-energy ladder on H²(D_IV⁵) starts at the genus λ₀ = n_C and steps by spin/parity. An Integer-Web over-determination: the integers that DEFINE the substrate reappear as its spectral levels. Connects the five integers to rep theory directly; underlies the BST glueball spectrum (Lyra F292 linear-energy mechanism)."
author: "Grace"
date: "2026-06-23 Tuesday"
theorem: T2490
tier: "D (exact rep-theory) for the spectral-ladder statement; the glueball mass-map application is I-tier with one BLIND leg (2++=g/n_C)."
---

# T2490 — The Discrete-Series Spectrum Theorem

## Statement (exact)

Let SO₀(5,2) (complexified maximal compact-dual algebra so(7) = B₃) have ρ = (5/2, 3/2, 1/2),
|ρ|² = 35/4. The holomorphic discrete-series representations carry Harish-Chandra parameter
λ = ρ + (n₁,n₂,n₃) with n_i ∈ ℤ≥0 and λ₁ > λ₂ > λ₃ > 0, and quadratic Casimir
C₂(λ) = |λ|² − |ρ|². Then the **four lowest non-trivial Casimir values are 6, 10, 12, 14**, and

> **½ · C₂  ∈  {3, 5, 6, 7} = {N_c, n_C, C_2, g}** — the four dynamical substrate primaries, in increasing order.

| rep λ | n | C₂ | ½C₂ | primary |
|---|---|---|---|---|
| (3.5, 1.5, 0.5) | (1,0,0) | 6 | 3 | **N_c** |
| (3.5, 2.5, 0.5) | (1,1,0) | 10 | 5 | **n_C** |
| (3.5, 2.5, 1.5) | (1,1,1) | 12 | 6 | **C_2** |
| (4.5, 1.5, 0.5) | (2,0,0) | 14 | 7 | **g** |

(rank = 2 is the *rank* of the group itself; N_max = 137 is the Shilov-boundary integer — the two
non-spectral primaries. The four *dynamical* primaries are exactly the spectral ones.)

## Why it is content, not tautology

The primaries enter the substrate by their *defining* roles — N_c = color/multiplicity = rank²−1, n_C = dim_ℂ
= genus, C_2 = the (1,1) K-type Casimir, g = signature/embedding. T2490 says these same integers **reappear as
the lowest discrete-series Casimirs** — a different invariant (the discrete-series C₂, not the K-type one). That
the defining integers and the spectral levels coincide is an **over-determination** (Casey's Integer-Web Principle
at the spectral level), not a relabeling.

## The physical application — the BST glueball spectrum (Lyra F292 mechanism)

The glueball masses are the **LINEAR** conformal energies of these reps (the dilatation/SO(2) eigenvalue —
"remember linear algebra"; *not* the quadratic Casimir, which is the m²∝C₂ reading that missed 2⁺⁺):

> **m(channel) ∝ E = λ₀ + step,  λ₀ = n_C = 5 (the genus / Bergman lowest weight).**

| channel | step | E | E/E(0⁺⁺) | substrate form | lattice | dev |
|---|---|---|---|---|---|---|
| 0⁺⁺ | 0 | 5 | 1 | 1 | 1.000 | — |
| 2⁺⁺ | spin-2 = rank | 7 | 7/5 | **g/n_C** (BLIND) | 1.387 | 0.9% |
| 0⁻⁺ | twist n_C/2 | 7.5 | 3/2 | N_c/rank | 1.497 | 0.2% |
| 1⁺⁻ | spin-1 + twist | 8.5 | 17/10 | 17/10 | 1.699 | 0.04% |

**The blind leg (the derivation):** 2⁺⁺/0⁺⁺ = (n_C + rank)/n_C = **g/n_C**, using only the genus + spin-2 step
and the substrate identity **g = n_C + rank** (7 = 5 + 2) — nothing read from the data. This is the leg that
beats look-elsewhere: the spectrum collapses to **two BST-natural numbers** (λ₀ = n_C, twist = n_C/2), not four
free ratios. (Honest tier: 2⁺⁺ blind; 0⁻⁺/1⁺⁻ use the n_C/2 half-canonical twist, rep-motivated but value-checked
against data — pending Elie's two confirming toys. So T2490's *spectral ladder* is D-tier exact; the *glueball
mass-map* is I-tier with the 2⁺⁺ leg blind.)

## Connections (graph edges)

- **Casey's Integer-Web Principle** — T2490 is a spectral instance: defining integers = spectral levels.
- **g = n_C + rank** (7 = 5 + 2) and **C_2 = n_C + 1** — the low ladder rungs are primary-sums anchored at the
  genus n_C. (Edges to the primary-identity nodes.)
- **T1829 (Wallach Bottleneck)** — the K-type/Casimir machinery of the same discrete series; T2490 is its
  conformal-energy companion (Casimir ladder ↔ linear-energy ladder, same reps).
- **Compact tower k(k+5) = {0,6,14,24}** and **noncompact k(k+4) = {0,5,12,21}** (corpus) — share rungs 6 = C_2
  and 14 = 2g with the T2490 ladder {0,6,10,12,14}: a shared spectral spine.
- **Paper A Yang-Mills gap Δ = C_2 = 6** — the first Casimir rung of the ladder; the mass gap is the ladder's
  first step. (Edge: T2490 → the YM gap value.)
- **Lyra F292** (linear-energy mechanism) and **T2489** (HS mirror; these are holomorphic discrete-series objects,
  Hardy-paired → HS-mirror nodes exist).

## AC and tier

AC = (C=1, D=1), depth 0 for the spectral-ladder statement (a finite Casimir computation in the discrete-series
Weyl chamber — counting + identity). The glueball mass-map is the physical application (I-tier, 2⁺⁺ blind).

— T2490, registered by Grace, 2026-06-23. Spectral connection mine; glueball linear-energy mechanism Lyra (F292);
forced addresses Elie. For Keeper registry + graph insertion; for Cal cold-read.
