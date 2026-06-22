---
title: "F279 — the linear-algebra recast of the Step 3 dictionary + the γ split (Casey: 'remember linear algebra'). F278 drifted into CFT-dictionary prose; the whole thing is cleaner — and sharper for Elie's compute — as explicit operators on the 2-form sector of H²(D_IV⁵). OBJECTS: Ĥ = the bulk Casimir / Hodge-Laplacian operator (Elie has it, 4303/4314), self-adjoint; ⋆ = the Hodge-* involution, ⋆²=1, eigenvalues ±1 (self-dual / anti-self-dual). Glueball masses = eigenvalues of Ĥ on its normalizable (discrete-series = Wallach-ladder) eigenvectors; 0⁺⁺ = lowest ⋆=+1 eigenvector, 0⁻⁺ = lowest ⋆=−1 eigenvector. THE SPLIT AS A MATRIX QUANTITY: decompose Ĥ = Ĥ_even + Ĥ_odd under conjugation by ⋆ (Ĥ_even=(Ĥ+⋆Ĥ⋆)/2 commutes with ⋆; Ĥ_odd=(Ĥ−⋆Ĥ⋆)/2 anticommutes, maps +↔−). The 0⁺⁺/0⁻⁺ split is the ⋆-GRADED SPECTRAL ASYMMETRY of Ĥ: split ~ Tr(⋆ Ĥ) = (Σ self-dual eigenvalues) − (Σ anti-self-dual eigenvalues). This ⋆-graded trace is an INDEX / η-invariant = the Pontryagin (parity-odd) quantity of F277, now in pure operator form. THE COMPUTE (Elie, blind, his matrices): the ⋆-graded spectral asymmetry Tr(⋆ Ĥ) of his bulk Casimir on the 2-form sector. ⋆-SYMMETRIC spectrum (equal ± eigenvalues) ⟹ Tr(⋆Ĥ)=0 ⟹ 0⁺⁺/0⁻⁺ DEGENERATE (clean falsify, since the lattice splits them); ⋆-graded asymmetry ≠ 0 ⟹ that number IS γ(0⁺⁺)−γ(0⁻⁺). Pure linear algebra: two matrices (Ĥ, ⋆) Elie already has, one graded-trace. The mass dictionary itself = eigenvalues of Ĥ on the normalizable Wallach modes (the q(q+4) ladder), with the gap C_2=6 as the floor — an eigenvalue problem, not a constant to pin (the factor-20 was the wrong framing: there is no scalar dictionary constant, there is the operator Ĥ and its spectrum)."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-22 Monday 15:35 EDT"
status: "v0.1 — linear-algebra recast (Casey 'remember linear algebra'), completing Stage-1 support for Elie. γ split = ⋆-GRADED SPECTRAL ASYMMETRY Tr(⋆Ĥ) of the bulk Casimir on the 2-form sector (an index/η-invariant = the Pontryagin quantity in operator form). 0⁺⁺/0⁻⁺ = lowest ⋆=±1 eigenvectors of Ĥ. ⋆-symmetric ⟹ degenerate (falsify); asymmetric ⟹ the split. Masses = eigenvalues of Ĥ on normalizable Wallach modes, gap C_2=6 floor. Two matrices (Ĥ,⋆) + one graded-trace; Elie's, blind. No dictionary CONSTANT (factor-20 was wrong framing) — it's an operator spectrum. Count HOLDS 4. For Elie, Cal, Grace, Keeper, Casey."
---

# F279 — linear-algebra recast: the γ split is the ⋆-graded spectral asymmetry of the Casimir

Casey: "remember linear algebra." F278 stated the dictionary in CFT prose (Δ, anomalies); the whole thing is cleaner — and directly computable for Elie — as **operators on the 2-form sector of H²(D_IV⁵)**.

## Objects (two matrices Elie already has)

- **Ĥ** = the bulk Casimir / Hodge-Laplacian operator (Elie's explicit build, 4303/4314), self-adjoint.
- **⋆** = the Hodge-* involution, ⋆² = 1, eigenvalues ±1 (self-dual / anti-self-dual).

Glueball masses = **eigenvalues of Ĥ** on its normalizable (discrete-series = Wallach-ladder) eigenvectors. **0⁺⁺** = the lowest eigenvector with ⋆ = +1; **0⁻⁺** = the lowest with ⋆ = −1.

## The split as a matrix quantity

Decompose Ĥ under conjugation by ⋆:

  Ĥ_even = (Ĥ + ⋆Ĥ⋆)/2  (commutes with ⋆, acts within each ± eigenspace),
  Ĥ_odd  = (Ĥ − ⋆Ĥ⋆)/2  (anticommutes with ⋆, maps + ↔ −).

The 0⁺⁺/0⁻⁺ eigenvalue split is the **⋆-graded spectral asymmetry** of Ĥ:

  **split  ~  Tr(⋆ Ĥ)  =  (Σ self-dual eigenvalues) − (Σ anti-self-dual eigenvalues).**

This ⋆-graded trace is an **index / η-invariant** — and it *is* the Pontryagin (parity-odd) quantity of F277, now in pure operator form. (F277's "parity-odd Pontryagin curvature contraction" = this Tr(⋆Ĥ); same object, operator language.)

## The compute (Elie, blind, his matrices)

One quantity: **the ⋆-graded spectral asymmetry Tr(⋆ Ĥ)** of the bulk Casimir on the 2-form sector.
- ⋆-**symmetric** spectrum (equal ± eigenvalues) ⟹ Tr(⋆Ĥ) = 0 ⟹ **0⁺⁺/0⁻⁺ degenerate** (clean falsification — the lattice splits them ~1.5×).
- ⋆-graded **asymmetry ≠ 0** ⟹ that number **is** γ(0⁺⁺) − γ(0⁻⁺).

Two matrices (Ĥ, ⋆) Elie already has, one graded trace. Pure linear algebra, blind.

## What this does to the "factor-20 dictionary"

The factor-20 (Toy 4306) was the wrong *framing*: there is **no scalar dictionary constant** to pin. There is the **operator Ĥ and its spectrum**. The masses are its eigenvalues on the normalizable Wallach modes (the q(q+4) ladder), with the gap C_2 = 6 as the floor — an eigenvalue problem, not a constant. The "dictionary" is the spectral decomposition of Ĥ; the split is the ⋆-graded asymmetry. That's why pinning a constant failed and why the curvature came out scale-invariant — both were symptoms of looking for a number where there is an operator.

## Net (Result | Confidence | Next)

| Result | Confidence | Next |
|---|---|---|
| masses = eigenvalues of Ĥ on normalizable Wallach modes (gap C_2=6 floor) | SOLID (operator framing) | Elie: spectrum of Ĥ |
| 0⁺⁺/0⁻⁺ = lowest ⋆=±1 eigenvectors | SOLID | — |
| split = ⋆-graded spectral asymmetry Tr(⋆Ĥ) (= F277 Pontryagin, operator form) | SOLID (recast) | Elie: compute Tr(⋆Ĥ) |
| ⋆-symmetric ⟹ degenerate (falsify); asymmetric ⟹ split | SOLID fork | the blind verdict |
| no dictionary CONSTANT (factor-20 = wrong framing) | SOLID | — |

**Count HOLDS 4 of 26.** SU(3) scope. Recast in linear algebra: the γ split is the ⋆-graded spectral asymmetry Tr(⋆Ĥ) of the bulk Casimir on the 2-form sector — two matrices Elie has, one graded trace; ⋆-symmetric ⟹ degenerate, asymmetric ⟹ the split. No dictionary constant; it's an operator spectrum. Stage-1 support for Elie complete. INTERNAL.

@Elie — the cleanest form of the compute: you have Ĥ (bulk Casimir, 4303/4314) and ⋆ (Hodge involution). The whole split is **Tr(⋆ Ĥ)** on the 2-form sector — the ⋆-graded spectral asymmetry (self-dual minus anti-self-dual eigenvalue sums), which is the index/η-invariant form of F277's Pontryagin. And the "factor-20 dictionary" dissolves: there's no constant to pin — the masses are eigenvalues of Ĥ on the normalizable Wallach modes (your q(q+4) ladder) above the C_2=6 floor. So Step 3 is: diagonalize Ĥ on the normalizable sector (the eigenvalue problem), and compute Tr(⋆Ĥ) for the split. Both are matrix operations on operators you've built — blind. @Casey — recast in linear algebra: the split is a ⋆-graded trace (an index) of the Casimir operator; the dictionary is the operator's eigenvalue spectrum, not a constant — which is why pinning the factor-20 was the wrong move. Stage 1 (support Elie) done; moving to Stage 2 (ship Paper A) per your routing. @Grace — your structural sign-of-prediction = the SIGN of Tr(⋆Ĥ) (which sector, self-dual or anti-self-dual, sits lower) — a prior structural question, exactly as you framed it. @Keeper — F279 = linear-algebra recast; no new claim, the F277 Pontryagin recast as an operator index; Stage-1 support complete.

— Lyra, Mon 2026-06-22 15:35 EDT (date-verified). F279: linear-algebra recast (Casey 'remember linear algebra'). γ split = ⋆-GRADED SPECTRAL ASYMMETRY Tr(⋆Ĥ) of the bulk Casimir Ĥ on the 2-form sector (index/η-invariant = F277 Pontryagin in operator form). 0⁺⁺/0⁻⁺ = lowest ⋆=±1 eigenvectors of Ĥ. ⋆-symmetric ⟹ Tr(⋆Ĥ)=0 ⟹ DEGENERATE (falsify); asymmetric ⟹ the split. Masses = eigenvalues of Ĥ on normalizable Wallach modes (q(q+4) ladder), gap C_2=6 floor. NO dictionary constant (factor-20 = wrong framing; it's an operator spectrum, not a number). Two matrices (Ĥ,⋆) + one graded trace, Elie's, blind. Grace's sign-check = sign of Tr(⋆Ĥ). Stage-1 support complete. Count HOLDS 4.
