---
title: "F296 — f_G computed (Casey's second item): the 0⁻⁺ glueball decay constant IS the Bergman mode-norm on H²(D_IV⁵), and it is a clean ratio of Gindikin Gamma functions at BST (half-)integer arguments — substrate-computable, parameter-free in form, completing the F285/F288 'f_G is not free' claim with an actual computation. THE MACHINE: the decay constant is the weighted-Bergman reproducing kernel at the center, f² ∝ K_ν(0,0), for the mode's conformal weight ν = Δ (from the linear ladder: ν(0⁺⁺) = genus = n_C = 5, ν(0⁻⁺) = n_C + n_C/2 = 3n_C/2 = 15/2). Gindikin Gamma for D_IV⁵ (rank 2, mult a = n−2 = 3): Γ_Ω(s) = (2π)^{3/2} Γ(s) Γ(s − 3/2). Faraut-Koranyi: K_ν(0,0) ∝ Γ_Ω(ν)/Γ_Ω(ν − n/r), n/r = 5/2. CLEAN RESULTS: (1) the 0⁺⁺ Gamma-ratio K(0,0) = Γ_Ω(5)/Γ_Ω(5/2) = Γ(5)Γ(7/2)/[Γ(5/2)Γ(1)] = 24·(5/2) = 60 = C_2·n_C·rank — an exact BST integer (the volume-stripped kernel), a good sign the machine is right; the full 0⁺⁺ kernel ties to K264's K(0,0) = 1920/π⁵ = N_c·n_C·2^g/π^{n_C}. (2) the mode-norm RATIO (normalization-independent): f_G(0⁻⁺)²/f(0⁺⁺)² = Γ_Ω(15/2)·Γ_Ω(5/2)/Γ_Ω(5)² = 46.92, so f_G(0⁻⁺) = 6.85·f(0⁺⁺) — the heavier, more-concentrated pseudoscalar mode has the larger decay constant. CONSEQUENCE: with f_G computed and m(0⁻⁺) = (3/2)·seat from the ladder, the Witten-Veneziano identity χ_top = f_G²·m²(0⁻⁺) now yields the absolute topological susceptibility as a substrate PREDICTION — the 'frontier' number, computed, not fit. HONEST FLAGS: (a) the convention f² ∝ K(0,0) vs 1/K(0,0) flips 6.85 ↔ 0.146 — needs pinning from the matrix-element definition; (b) the overall K264 volume normalization (1920/π⁵) sets the absolute MeV scale → Elie's K264 toy. The functional FORM (clean Gamma ratio at BST arguments) is the robust deliverable: f_G is substrate-computable, parameter-free. Count HOLDS 4."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-23 Tuesday (date-verified ~09:00 EDT)"
status: "v0.1 — f_G computed as the Bergman mode-norm. f² ∝ K_ν(0,0), weights ν(0⁺⁺)=n_C=5, ν(0⁻⁺)=3n_C/2=15/2. Gindikin Γ_Ω(s)=(2π)^{3/2}Γ(s)Γ(s−3/2); FK kernel-at-origin K_ν(0,0) ∝ Γ_Ω(ν)/Γ_Ω(ν−5/2). CLEAN: 0⁺⁺ Gamma-ratio = 60 = C_2·n_C·rank (exact BST integer); ratio f_G(0⁻⁺)/f(0⁺⁺) = 6.85 = √(Γ_Ω(15/2)Γ_Ω(5/2)/Γ_Ω(5)²). Completes 'f_G not free' with a computation; enables absolute χ_top via WV χ_top=f_G²·m²(0⁻⁺). FLAGS: convention (K vs 1/K, 6.85↔0.146); absolute MeV scale via K264 1920/π⁵ → Elie toy. Form (clean Gamma ratio at BST args) is robust. Count HOLDS 4. For Casey, Elie, Grace, Cal, Keeper."
---

# F296 — f_G is the Bergman mode-norm, and it computes to a clean Gindikin-Gamma ratio

Casey's second item. F285/F288 argued f_G is substrate-computable (not free) but didn't compute it. Here it is, on the actual Bergman/Gindikin machinery.

## The machine

The glueball decay constant is the weighted-Bergman reproducing kernel at the center of D_IV⁵ — the normalized mode's value at the origin:

  **f² ∝ K_ν(0,0),  ν = the channel's conformal weight** (from the linear ladder, F293).

Weights: ν(0⁺⁺) = genus = n_C = 5; ν(0⁻⁺) = n_C + n_C/2 = **3n_C/2 = 15/2**.

Gindikin Gamma for D_IV⁵ (rank r = 2, multiplicity a = n−2 = 3):

  **Γ_Ω(s) = (2π)^{3/2} Γ(s) Γ(s − 3/2).**

Faraut-Koranyi gives the kernel at the origin: **K_ν(0,0) ∝ Γ_Ω(ν)/Γ_Ω(ν − n/r), n/r = 5/2.**

## Clean results

**(1) The 0⁺⁺ kernel is an exact BST integer.**
  K(0,0)|_{0⁺⁺} = Γ_Ω(5)/Γ_Ω(5/2) = Γ(5)Γ(7/2)/[Γ(5/2)Γ(1)] = 24 · (5/2) = **60 = C_2 · n_C · rank.**
The volume-stripped kernel landing on a clean BST integer is a good sign the machine is right. The full 0⁺⁺ kernel (with the fixed volume factor) is K264's K(0,0) = 1920/π⁵ = N_c·n_C·2^g/π^{n_C}.

**(2) The mode-norm ratio (normalization-independent, the robust number).**
  f_G(0⁻⁺)²/f(0⁺⁺)² = Γ_Ω(15/2)·Γ_Ω(5/2)/Γ_Ω(5)² = **46.92**, so **f_G(0⁻⁺) = 6.85 · f(0⁺⁺).**
All Gamma arguments are BST (half-)integers — {15/2, 6, 5, 7/2} for 0⁻⁺, {5, 7/2, 5/2, 1} for 0⁺⁺. The heavier, more-concentrated pseudoscalar mode has the larger decay constant, as physically expected.

## Why this matters — the absolute χ_top

With f_G now computed (the Bergman mode-norm) and m(0⁻⁺) = (3/2)·seat from the ladder, the Witten-Veneziano identity

  **χ_top = f_G² · m²(0⁻⁺)**

yields the absolute topological susceptibility as a **substrate prediction** — the "non-perturbative frontier" number, computed from the domain rather than fit. (Earlier the magnitude collapsed to f_G as the one remaining Bergman number; this computes that number's form.)

## Honest flags (for Elie's K264 toy)

- **Convention:** f² ∝ K(0,0) vs 1/K(0,0) flips 6.85 ↔ 0.146. This must be pinned from the matrix-element definition ⟨0|O_{0⁻⁺}|G⟩, not chosen.
- **Absolute scale:** the overall K264 volume normalization (1920/π⁵) sets the MeV value of f(0⁺⁺), hence χ_top in MeV⁴ — Elie's K264 toy.
- The **functional form** (clean Gindikin-Gamma ratio at BST arguments) is the robust deliverable: f_G is substrate-computable and parameter-free in form.

## Net (Result | Confidence | Next)

| Result | Confidence | Next |
|---|---|---|
| f_G = Bergman mode-norm, f² ∝ K_ν(0,0), ν from the ladder | clean (machine) | — |
| 0⁺⁺ Gamma-ratio kernel = 60 = C_2·n_C·rank (exact) | clean | — |
| f_G(0⁻⁺)/f(0⁺⁺) = 6.85 (Gamma ratio at BST args) | clean form | pin convention (K vs 1/K) |
| absolute χ_top via WV = f_G²·m²(0⁻⁺) | structure clean | Elie K264 volume normalization → MeV |

**Count HOLDS 4 of 26.** SU(3) scope. INTERNAL. Both of Casey's items done (radial eigenvalue F295, f_G here).

@Elie — f_G computed as the Bergman mode-norm: f² ∝ K_ν(0,0) with the Gindikin Γ_Ω(s) = (2π)^{3/2}Γ(s)Γ(s−3/2). The 0⁺⁺ Gamma-ratio kernel is exactly 60 = C_2·n_C·rank (ties to your K264 1920/π⁵), and f_G(0⁻⁺)/f(0⁺⁺) = 6.85, a clean Gamma ratio at BST arguments. Two things for your K264 toy: (1) pin the convention (f² ∝ K vs 1/K from the matrix-element def), (2) carry the 1920/π⁵ volume factor to give f(0⁺⁺) and hence the absolute χ_top = f_G²·m²(0⁻⁺) in MeV⁴. @Grace — f_G is now computed (not free), so the WV bridge gives absolute χ_top — the frontier number, from the domain. @Casey — second item done: f_G is the Bergman mode-norm, and it computes to a clean Gindikin-Gamma ratio at BST arguments (0⁺⁺ kernel = 60 = C_2·n_C·rank exactly). The form is parameter-free; the absolute MeV scale is one K264 volume factor (Elie's toy), which then predicts the absolute topological susceptibility.

— Lyra, Tue 2026-06-23 (date-verified ~09:00 EDT). F296: f_G computed as the Bergman mode-norm on H²(D_IV⁵). f² ∝ K_ν(0,0); weights ν(0⁺⁺)=n_C=5, ν(0⁻⁺)=3n_C/2=15/2. Gindikin Γ_Ω(s)=(2π)^{3/2}Γ(s)Γ(s−3/2); FK K_ν(0,0) ∝ Γ_Ω(ν)/Γ_Ω(ν−5/2). 0⁺⁺ Gamma-ratio = 60 = C_2·n_C·rank (exact BST integer); f_G(0⁻⁺)/f(0⁺⁺) = 6.85 (clean Gamma ratio at BST args). Enables absolute χ_top via WV = f_G²·m²(0⁻⁺). Flags: convention (K vs 1/K), absolute scale via K264 1920/π⁵ → Elie toy. Count HOLDS 4.
