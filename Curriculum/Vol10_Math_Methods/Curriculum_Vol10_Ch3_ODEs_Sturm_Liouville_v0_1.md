---
title: "BST Physics Curriculum Vol 10 Chapter 3 — ODEs + Sturm-Liouville v0.4 (refilled per Cal #104)"
author: "Lyra (Claude 4.7) [Vol 10 primary]"
date: "2026-05-23 Saturday EDT (Cal #104 refill)"
chapter: "Vol 10 Ch 3"
status: "v0.4 chapter-grade narrative refilled. Standard ODE methods + Sturm-Liouville theory; BST cross-link Vol 1 Ch 7 substrate Schrödinger as Sturm-Liouville on Bergman H². Per Calibration #19."
prerequisites: ["Vol 10 Ch 1-2", "Vol 1 Ch 7 Dynamics", "Vol 5 Ch 4 Schrödinger Equation"]
related: ["Boyce-DiPrima standard ODE text", "Sturm-Liouville theory + orthogonal polynomials", "Vol 1 Ch 7 substrate Schrödinger"]
---

# Vol 10 Chapter 3 — ODEs + Sturm-Liouville

## Chapter motivation

Standard ODE methods: linear ODEs (1st-order, 2nd-order homogeneous + inhomogeneous, constant + variable coefficients); series solutions + Frobenius method; Wronskian + linear independence; Green's functions for inhomogeneous problems; Sturm-Liouville eigenvalue problems (Bessel + Legendre + Hermite + Laguerre orthogonal polynomials).

BST cross-link: Vol 1 Ch 7 Dynamics formulates substrate Schrödinger equation iℏ ∂|ψ⟩/∂t = H_sub|ψ⟩ on Bergman H²(D_IV⁵); time-independent form H_sub|ψ⟩ = E|ψ⟩ is a Sturm-Liouville eigenvalue problem with H_sub = Casimir on L²(D_IV⁵; L_λ). Substrate Casimir spectrum Vol 1 Ch 5 = Sturm-Liouville eigenvalue spectrum.

## Section 3.0b — Reader-grade 3-level pedagogy

**Level 1**: Standard ODE methods + boundary-value problems + Sturm-Liouville eigenvalue theory; BST cross-link: substrate Schrödinger H_sub|ψ⟩ = E|ψ⟩ on Bergman H² IS Sturm-Liouville eigenvalue problem with Casimir spectrum from Vol 1 Ch 5.

**Level 2 (graduate-physicist)**: Standard ODE theory: linear ODEs separable into 1st-order systems; constant-coefficient solutions via characteristic equation; variable-coefficient solutions via series methods (Frobenius near regular singular points); Wronskian W = ψ_1 ψ'_2 − ψ'_1 ψ_2 measures linear independence; Green's function method for inhomogeneous problems via Dirac delta source. Sturm-Liouville theory: eigenvalue problem [d/dx (p(x) dy/dx) − q(x) y + λ w(x) y] = 0 with boundary conditions; eigenvalues λ_n real + discrete (under self-adjoint BCs); eigenfunctions orthogonal under weight w(x): ∫ y_m y_n w(x) dx = δ_{mn}; completeness of eigenfunction expansion. Classical examples: Bessel J_n, Legendre P_n, Hermite H_n, Laguerre L_n orthogonal polynomial families. BST substrate cross-link: Vol 1 Ch 7 substrate Schrödinger iℏ ∂|ψ⟩/∂t = H_sub|ψ⟩; time-independent H_sub|ψ⟩ = E|ψ⟩ is Sturm-Liouville eigenvalue problem on Bergman H²(D_IV⁵; L_λ); H_sub = Casimir per Elie K52a S29 framework-complete (Thursday). Substrate Casimir eigenvalue spectrum (Vol 1 Ch 5) IS the Sturm-Liouville eigenvalue spectrum; substrate K-type basis V_(p,q) IS the orthogonal eigenfunction basis. Ground-state energy = C_2 = 6 (BST primary; substrate Sturm-Liouville lowest eigenvalue). Substrate dynamics Schrödinger framework recovered at macroscopic limit via Vol 5 Ch 4 pedagogical bridge.

**Level 3 (5th-grader accessible)**: Ordinary differential equations (ODEs) describe how a quantity changes over one variable (usually time or space). Sturm-Liouville theory handles ODEs with boundary conditions and gives discrete "eigenvalue" sets — the substrate Schrödinger equation H_sub|ψ⟩ = E|ψ⟩ IS such a problem on the Bergman space (Vol 1 Ch 7). The substrate Casimir eigenvalues (Vol 1 Ch 5) are the Sturm-Liouville eigenvalues; ground state energy = 6 = C_2 (BST integer).

## Section 3.1 — Standard ODEs

1st-order linear: dy/dx + p(x) y = q(x) — integrating-factor method.
2nd-order linear: y'' + P(x) y' + Q(x) y = R(x) — homogeneous + particular solutions; Wronskian theory.
Series solutions: Frobenius method near regular singular points.

## Section 3.2 — Sturm-Liouville Eigenvalue Problem

L y = [d/dx (p(x) dy/dx) − q(x) y] + λ w(x) y = 0 with boundary conditions α y(a) + β y'(a) = 0, γ y(b) + δ y'(b) = 0.

Self-adjoint under inner product ⟨f, g⟩_w = ∫_a^b f g w(x) dx. Eigenvalues λ_n real + discrete + λ_n → ∞; eigenfunctions y_n orthogonal: ⟨y_m, y_n⟩_w = δ_{mn} · normalization.

Classical orthogonal polynomial families:
- Bessel J_n (cylindrical problems)
- Legendre P_n (spherical problems)
- Hermite H_n (harmonic oscillator)
- Laguerre L_n (hydrogen atom radial)

## Section 3.3 — Substrate Schrödinger as Sturm-Liouville

Per Vol 1 Ch 7 + Vol 5 Ch 4 + Elie K52a S29 (Thursday): substrate Schrödinger iℏ ∂|ψ⟩/∂t = H_sub|ψ⟩ on Bergman H²(D_IV⁵; L_λ).

Time-independent: H_sub|ψ⟩ = E|ψ⟩ IS Sturm-Liouville eigenvalue problem.

H_sub = Casimir on L²(D_IV⁵; L_λ) per Elie K52a S29 framework-complete. Substrate Casimir spectrum (Vol 1 Ch 5) = Sturm-Liouville eigenvalues.

## Section 3.4 — Substrate K-Type Basis as Sturm-Liouville Eigenfunctions

Wallach 1976 K-type V_(p,q) classification (Vol 11 Ch 3) = orthogonal eigenfunction basis of substrate Sturm-Liouville problem. Ground-state V_(0,0) Casimir = C_2 = 6 (BST primary; lowest non-trivial Sturm-Liouville eigenvalue).

## Section 3.5 — Honest scope + Connection

- Standard ODE + Sturm-Liouville theory ✓
- Substrate Schrödinger Sturm-Liouville cross-link (Vol 1 Ch 7 + Vol 5 Ch 4) ✓
- Classical orthogonal polynomial families recoverable from substrate K-type at appropriate substrate-zone restriction

**Open scope**: explicit Bessel/Legendre/Hermite/Laguerre substrate-derivation from Wallach K-type structure (multi-week).

**Connection**:
- Vol 1 Ch 7 Dynamics + Vol 5 Ch 4 Schrödinger
- Vol 1 Ch 5 Casimir algebra (Sturm-Liouville eigenvalue spectrum)
- Vol 11 Ch 3 Wallach K-type (eigenfunction basis)

— Lyra, Vol 10 Ch 3 v0.4 chapter-grade narrative REFILLED per Cal #104, Saturday 2026-05-23 EDT
