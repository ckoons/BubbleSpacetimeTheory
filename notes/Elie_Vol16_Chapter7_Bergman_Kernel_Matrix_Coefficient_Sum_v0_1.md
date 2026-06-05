---
title: "Vol 16 Chapter 7 — Bergman Kernel as Matrix-Coefficient Sum: Scaffolding v0.1"
authors: "Lyra + Elie (joint; Elie initial scaffolding pending Lyra integration)"
date: "2026-06-05 Friday 13:15 EDT (date-verified)"
status: "v0.1 SUBSTANTIVE — Elie initial scaffolding for joint Lyra+Elie Ch 7 development"
volume: "Vol 16 Substrate Algebra"
chapter: "Ch 7 Bergman Kernel as Matrix-Coefficient Sum"
---

# Vol 16 Chapter 7 — Bergman Kernel as Matrix-Coefficient Sum

## 0. Chapter Thesis

The Bergman reproducing kernel K_B(z, w̄) on H²(D_IV^5) decomposes as a sum of matrix coefficients across substrate K-types. This identification — Bergman kernel = K-type matrix coefficient sum — bridges Vol 16 Ch 4 (matrix coefficients = observables) and the substrate Hardy-space geometry developed in Chs 1+2.

Per Casey 12:30 EDT directive: substrate substantive content already exists across team's work; Vol 16 makes the linear-algebra-of-substrate explicit and portable.

## 1. Bergman Kernel Background

### Standard form for D_IV^5
For the type IV Lie ball D_IV^n with rank 2 and complex dimension n (here n = n_C = 5), the Bergman kernel is:
```
K_B(z, w̄) = c_FK · h(z, w̄)^(-(n+rank)/2)
         = c_FK · h(z, w̄)^(-7/2)
         = c_FK · h(z, w̄)^(-g/2)
```
where:
- h(z, w̄) = 1 - 2⟨z, w̄⟩ + (z·z)(w̄·w̄) is the Jordan determinant
- (n_C + rank)/2 = 7/2 = g/2 substrate-natural exponent (Toy 3661 Helgason verification)
- c_FK · π^(9/2) = 225 (Lyra T2442 ratified)

### Reproducing property
For any f ∈ H²(D_IV^5):
```
f(z) = ⟨K_B(·, z̄), f⟩_FK
```

### Substrate substantive content
Per Lyra Sunday substrate operator framework:
- K_B encodes substrate "now-state" projector onto holomorphic Hardy subspace
- Bergman is the substrate-natural inner product on H²(D_IV^5)
- κ_Bergman = -n_C closed-form curvature scalar (Toy 3661)

## 2. K-Type Decomposition of H²(D_IV^5)

### Peter-Weyl style decomposition
H²(D_IV^5) decomposes under K = SO(5)×SO(2) action:
```
H²(D_IV^5) = ⊕_{(λ_1, λ_2)} V_(λ_1, λ_2) ⊗ V_(λ_1, λ_2)^*
```
where sum is over dominant K-weights.

Concretely (Lyra Chs 1-2 + Toy 3909 K-type catalog):
- V_(0, 0) trivial (constants)
- V_(1/2, 1/2) spinor (dim 4 = rank²)
- V_(1, 0) vector (dim 5 = n_C)
- V_(1, 1) adjoint (dim 10 = 2·n_C)
- V_(3/2, 1/2) muon spinor (dim 16 = 2^N_c·rank)
- V_(2, 0) sym-trace (dim 14 = 2·g)
- V_(5/2, 1/2) tau spinor (dim 40 = 2^N_c·n_C)
- ... and infinite tower of higher K-types

### Reproducing kernel per K-type
Each isotypic component V_(λ_1, λ_2) ⊗ V_(λ_1, λ_2)^* has its own reproducing kernel K^λ_B(z, w̄).

## 3. Matrix Coefficient Decomposition

### Core formula
Per Peter-Weyl theorem applied to bounded symmetric domain Hardy space:
```
K_B(z, w̄) = Σ_{(λ_1, λ_2)} (dim V_(λ_1, λ_2)) · m^λ(z, w̄)
```
where m^λ(z, w̄) is the matrix coefficient of K-type V_(λ_1, λ_2) at (z, w̄).

### Substrate Schur scalar
The Bergman kernel "diagonal" K_B(z, z̄) on a K-orbit through z yields Schur scalar form:
```
K_B(z, z̄) = Σ_λ (dim V_λ) · s_λ(K_B) · ρ_λ(z)
```
where ρ_λ(z) is the K-type density at z.

### Substrate substantive content
Substrate Bergman is the sum of substrate K-type matrix coefficients weighted by K-type dimensions. Each K-type contributes its substrate Schur scalar to the substrate inner product structure.

## 4. Worked Example — Vacuum K-Type Contribution

Trivial K-type V_(0, 0):
```
dim V_(0, 0) = 1
m^(0,0)(z, w̄) = 1  (constant function)
Contribution: 1 · 1 = 1
```

This is the substrate vacuum contribution to the Bergman kernel. Substrate-natural unit normalization.

## 5. Worked Example — Spinor K-Type Contribution

V_(1/2, 1/2) spinor:
```
dim V_(1/2, 1/2) = 4 = rank²
||V_(1/2, 1/2)||² = 3π/2^g (Pochhammer, Toy 3695)
m^(1/2, 1/2)(z, w̄) = explicit polynomial in z, w̄ (Faraut-Koranyi explicit form)
```

Spinor contribution to Bergman:
```
K_B^spinor(z, w̄) = rank² · m^(1/2, 1/2)(z, w̄)
```

Substrate substantive content: spinor cluster contributes 4-dim weight to substrate Bergman, scaled by spinor matrix coefficient.

## 6. Total Bergman as Generating Function

### Hua-Schmidt formula
Per Hua + Faraut-Koranyi:
```
K_B(z, w̄) = c_FK · h(z, w̄)^(-g/2)
         = c_FK · Σ_{(λ_1, λ_2)} (dim V_λ) · ⟨z^λ, w̄^λ⟩
```

The series expansion of h^(-g/2) in z and w̄ gives the matrix-coefficient sum form. Each coefficient in the series is a substrate Schur scalar of corresponding K-type.

### Substrate generating function reading
Bergman kernel = substrate generating function whose coefficients are substrate K-type matrix coefficients. Substrate content equals expansion of h^(-g/2) in K-isotypic basis.

## 7. Heat Kernel = Mehler Family

### Mehler kernel
For τ > 0, define substrate Mehler kernel:
```
M_τ(z, w̄) = K_B(z, w̄)^τ
```

### K-type decomposition
By same K-type expansion:
```
M_τ(z, w̄) = Σ_λ (dim V_λ) · m_τ^λ(z, w̄)
```
where m_τ^λ has substrate Schur scalar exp(-τ·C_2(λ)/ℏ_BST).

### Substrate substantive content
The Mehler family M_τ interpolates between identity (τ = 0) and full Bergman kernel (τ = 1). Each τ value gives substrate heat-evolved K-type matrix coefficients.

Per Toy 3905 substrate Mehler kernel framework:
- Substrate diagonal matrix coefficient ⟨V_λ | M_τ | V_λ⟩ = exp(-τ·C_2(λ)/ℏ_BST)·||V_λ||²
- Substrate off-diagonal vanishes for K-invariant Mehler

## 8. κ_Bergman = -n_C Closed Form

Per Toy 3661 substrate Helgason application:
```
κ_Bergman(D_IV^5) = -n_C = -5
```
Substrate Bergman scalar curvature equals minus substrate spatial primary.

### Matrix coefficient interpretation
Per Vol 16 Ch 4 Schur scalar framework, κ_Bergman is the substrate Schur scalar of substrate curvature operator on Bergman kernel:
```
κ_Bergman = s(R_Bergman) = -n_C
```

### Substrate substantive content
- κ < 0 substrate negatively curved (substrate-natural for Hermitian symmetric domain)
- |κ| = n_C substrate primary
- Substrate curvature substrate-natural quantization in n_C units

Per Cal #34 STANDING Helgason closed form ratified (Toy 3661).

## 9. Cross-Anchor with Vol 16 Other Chapters

### Ch 1 (Lyra) — Hilbert Space + Operator Algebra
Provides H²(D_IV^5) substrate Hardy space + substrate FK inner product. Ch 7 Bergman kernel = reproducing kernel for this Hilbert space.

### Ch 2 (Lyra + Grace) — K-Type Spectral Decomposition
Provides K-type ⊕ decomposition of H²(D_IV^5). Ch 7 expresses Bergman as sum over K-types from Ch 2.

### Ch 3 (Lyra) — Substrate Hall Algebra
Provides Hall algebra structure. Ch 7 Bergman matrix coefficients realize Hall algebra elements.

### Ch 4 (Elie + Grace + Keeper) — Matrix Coefficients = Observables
Provides matrix coefficient framework. Ch 7 applies framework to Bergman kernel decomposition.

### Ch 6 (Lyra) — Casey #14 Chirality Projection
Provides substrate K-type restriction SO(5,2) → SO(4,2) → SO(3,1). Ch 7 Bergman behavior under restriction.

### Ch 8 (Keeper + Lyra) — Curvature Scalars in Operator Language
Uses Ch 7 κ_Bergman = -n_C as central curvature observable.

## 10. Multi-Week K-Audit Gates

Per Cal #189 Brake 2 substrate-mechanism FORWARD multi-week gates:

1. Bergman matrix-coefficient sum series convergence rigorous (analytic question)
2. K-type matrix coefficients m^λ(z, w̄) explicit Faraut-Koranyi forms per K-type
3. Mehler kernel M_τ K-type decomposition rigorous
4. κ_Bergman = -n_C Helgason cross-anchor rigorous (Toy 3661 already substantive)
5. Cross-anchor with Lyra Vol 16 Chs 1+2 substantive content
6. Joint Lyra + Elie multi-week chapter development

## 11. Joint Lyra + Elie Coordination

Per Casey 12:30 EDT Ch 7 = joint Lyra + Elie:

- Lyra primary: substrate Hilbert space + K-type decomposition (Chs 1+2 anchors)
- Elie primary: substrate matrix coefficient + Pochhammer numerical (Ch 4 anchor)
- Joint: substrate Bergman series expansion explicit per K-type

This v0.1 establishes joint scaffolding. Lyra integration with substrate Hall algebra (Ch 3) + K-type spectral framework (Ch 2) pending. Multi-week joint chapter development.

## 12. Status

v0.1 SUBSTANTIVE Elie initial scaffolding for joint Ch 7. Vol 16 architectural sprint operational across Chs 1 (Lyra L21), 3 (Lyra F26 absorbing Hall paper), 4 (Elie + Grace + Keeper v0.2), 7 (this doc), 8 (Keeper outline planned), 9 (joint).

Per Casey 12:30 EDT + Keeper 13:00 EDT continuous work directive.

Multi-week residuals pending Lyra integration of Hardy-space + K-type decomp foundations.

— Elie, Friday 2026-06-05 13:15 EDT (date-verified)
