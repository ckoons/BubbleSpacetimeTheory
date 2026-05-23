---
title: "BST Physics Curriculum Vol 10 Chapter 4 — PDEs + Heat / Wave / Laplace v0.4 (refilled per Cal #104)"
author: "Lyra (Claude 4.7) [Vol 10 primary]"
date: "2026-05-23 Saturday EDT (Cal #104 refill)"
chapter: "Vol 10 Ch 4"
status: "v0.4 chapter-grade narrative refilled. Standard PDE methods + Green's functions; BST cross-link Vol 6 Ch 5 heat kernel on D_IV⁵ LOAD-BEARING; Vol 4 Ch 4 Λ heat-kernel evaluation. Per Calibration #19."
prerequisites: ["Vol 10 Ch 1-3", "Vol 6 Ch 5 LOAD-BEARING heat kernel + partition function", "Vol 4 Ch 4 Λ from Substrate (T1485)"]
related: ["Standard PDE methods: heat + wave + Laplace + Poisson equations", "Green's function method", "Vol 6 Ch 5 heat kernel as Z(β) = Tr(e^{-βCasimir}) on Bergman H²(D_IV⁵)", "Heat-kernel chain Toy 273-639 k=2..20"]
---

# Vol 10 Chapter 4 — PDEs + Heat / Wave / Laplace

## Chapter motivation

Standard graduate PDE methods: linear 2nd-order PDEs classified (elliptic + parabolic + hyperbolic); canonical equations (heat ∂u/∂t = α ∇²u, wave ∂²u/∂t² = c² ∇²u, Laplace ∇²u = 0, Poisson ∇²u = f); separation of variables; Green's function method for inhomogeneous problems; boundary-value problems (Dirichlet + Neumann + mixed). Standard texts: Strauss + Evans + John.

BST cross-link: the **heat kernel on D_IV⁵** plays load-bearing role across BST framework — Vol 6 Ch 5 LOAD-BEARING identifies partition function Z(β) = Tr(e^{−βCasimir}) as heat kernel evaluation on Bergman H²(D_IV⁵); Vol 4 Ch 4 T1485 Λ derivation IS heat-kernel at cosmological scale t_cosmo = 47. Heat-kernel chain Toy 273-639 verifies speaking-pair structure k = 2,...,20 (19 consecutive levels).

## Section 4.0b — Reader-grade 3-level pedagogy

**Level 1**: Standard PDE methods (heat + wave + Laplace + Poisson + Green's function); BST cross-link: heat kernel on Bergman H²(D_IV⁵) = substrate partition function (Vol 6 Ch 5 LOAD-BEARING) + cosmological constant Λ (Vol 4 Ch 4 T1485) — heat-kernel framework underlies thermo + cosmology.

**Level 2 (graduate-physicist)**: Standard PDE classification: linear 2nd-order PDE A u_xx + 2B u_xy + C u_yy + ... = 0 classified by discriminant Δ = B² − AC. Elliptic (Δ < 0): Laplace ∇²u = 0, Poisson ∇²u = f; well-posed boundary-value problems with Dirichlet/Neumann conditions. Parabolic (Δ = 0): heat equation ∂u/∂t = α ∇²u; well-posed initial-value problem. Hyperbolic (Δ > 0): wave equation ∂²u/∂t² = c² ∇²u; well-posed initial-value problem with characteristics. Separation of variables (Fourier series + Bessel functions); Green's function method: G(x, x') satisfies L G = δ(x − x'); solution u(x) = ∫ G(x, x') f(x') dx'. BST substrate cross-link: heat kernel K(t, z, z') on Bergman H²(D_IV⁵) satisfies (∂/∂t + Casimir) K = 0 with K(0, z, z') = δ(z − z'); per Vol 6 Ch 5 LOAD-BEARING Z(β) = Tr(e^{−βCasimir}) = ∫_{D_IV⁵} K(β, z, z) dV(z) heat-kernel trace = partition function. Heat-kernel expansion K(t) = Σ_k a_k(z) t^(k−n/2) (Seeley-DeWitt coefficients) with substrate speaking-pair structure period n_C = 5 verified k = 2,...,20 (Toy 273-639 chain). Cross-link Vol 4 Ch 4 T1485 Λ derivation: same heat-kernel framework at cosmological scale t_cosmo = g² − rank = 47 gives Λ = g · exp(−C_2 · t_cosmo) = 7·exp(−282) at 0.076 dex (99.9% of 122-order hierarchy). Wave + Laplace + Poisson substrate-cartography readings via substrate-tick GF(128)^k discrete operators.

**Level 3 (5th-grader accessible)**: Standard partial differential equations (PDEs) describe how quantities change in multiple variables (space + time). The heat equation describes how temperature spreads through a metal bar; the wave equation describes vibrating strings + EM waves; Laplace equation describes equilibrium states. BST identifies the heat kernel on the substrate D_IV⁵ as the master function — Vol 6 Ch 5 LOAD-BEARING shows the partition function (thermodynamic master formula) IS the heat-kernel trace on Bergman H²; Vol 4 Ch 4 shows the cosmological constant Λ IS the heat-kernel at large scale.

## Section 4.1 — Standard PDE Classification

A u_xx + 2B u_xy + C u_yy + ... = 0; discriminant Δ = B² − AC classifies as elliptic (Δ < 0) / parabolic (Δ = 0) / hyperbolic (Δ > 0).

**Canonical equations**:
- Heat (parabolic): ∂u/∂t = α ∇²u
- Wave (hyperbolic): ∂²u/∂t² = c² ∇²u
- Laplace (elliptic): ∇²u = 0
- Poisson: ∇²u = f

## Section 4.2 — Separation of Variables + Green's Functions

Separation: u(x, y, ...) = X(x) Y(y) ... reduces PDE to system of ODEs (Sturm-Liouville per Vol 10 Ch 3).

Green's function: G(x, x') satisfies L G = δ(x − x') with boundary conditions; solution u(x) = ∫ G(x, x') f(x') dx' for inhomogeneous source f.

## Section 4.3 — Substrate Heat Kernel on Bergman H²(D_IV⁵)

Heat kernel K(t, z, z') on D_IV⁵ satisfies (∂/∂t + Casimir) K = 0 with K(0, z, z') = δ(z − z').

Per Vol 6 Ch 5 LOAD-BEARING: Z(β) = Tr(e^{−βCasimir}) = ∫_{D_IV⁵} K(β, z, z) dV(z) — heat-kernel trace IS partition function.

Heat-kernel expansion: K(t) = Σ_k a_k(z) t^(k − n/2) with Seeley-DeWitt coefficients a_k(z).

## Section 4.4 — Heat-Kernel Chain Toy 273-639 (Speaking-Pair Structure)

Substrate speaking-pair structure with period n_C = 5 verified at heat-kernel levels k = 2, 3, ..., 20 (19 consecutive levels, 4 full periods).

a₁₆ confirmed (Toy 639): ratio(k=16) = −24 = −(n_C² − 1) = −dim SU(5) — uniqueness identity n_C² − 1 = (n_C − 1)! holds ONLY at n_C = 5.

## Section 4.5 — Cross-Link Vol 4 Ch 4 Λ (T1485)

Same heat-kernel framework at cosmological scale t_cosmo = g² − rank = 47:

  Λ / M_Pl⁴ = g · exp(−C_2 · t_cosmo) = 7 · exp(−282)

log₁₀(Λ/M_Pl⁴) = −121.63 vs observed −121.55 → **0.076 dex (99.9% of 122-order hierarchy resolved)**.

## Section 4.6 — Wave + Laplace + Poisson Substrate-Cartography

Wave equation substrate-cartography: substrate-tick GF(128)^k discrete operator framework + Bergman kernel propagation (T2457 Bergman = Feynman propagator structural-role-of, Friday).

Laplace ∇²u = 0 substrate-cartography: harmonic functions on D_IV⁵ + Bergman reproducing kernel.

Poisson ∇²u = f substrate-cartography: Green's function for substrate Casimir operator.

## Section 4.7 — Honest scope + Connection

- Standard PDE methods + Green's functions ✓
- Heat-kernel BST cross-link Vol 6 Ch 5 LOAD-BEARING + Vol 4 Ch 4 ✓
- 19 consecutive heat-kernel speaking-pair levels verified k=2..20
- Open scope: explicit wave + Laplace + Poisson substrate-derivation (multi-week)

**Connection**:
- Vol 6 Ch 5 LOAD-BEARING heat kernel + partition function
- Vol 4 Ch 4 Λ from Substrate (T1485 + heat-kernel at cosmological scale)
- Vol 10 Ch 3 ODEs + Sturm-Liouville (separation reduces to ODEs)
- Vol 11 Ch 3 Wallach K-type (eigenfunction basis)

— Lyra, Vol 10 Ch 4 v0.4 chapter-grade narrative REFILLED per Cal #104, Saturday 2026-05-23 EDT
