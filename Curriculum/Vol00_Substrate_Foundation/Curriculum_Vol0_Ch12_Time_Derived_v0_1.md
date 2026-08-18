---
title: "Vol 0, Chapter 12 — Time, Derived"
subtitle: "Time as the flow of one geometry-forced operator; the double cover as spin-statistics; charge as internal; gravity as a one-input reduction"
volume: "Vol 0 — Substrate Foundation"
chapter: 12
version: "v0.1"
date: "2026-08-17"
status: "Capstone of the foundations arc. Sourced to the paper 'Time, Derived' (Keeper-PASS 2026-08-17, K1670). Ch11 (The Operation) names time as the SO(2) common append-axis; this chapter derives what that flow IS."
---

# Chapter 12 — Time, Derived

## For everyone (the one-paragraph story)
Most physics *starts* with time — you draw a clock on the wall and let things move against it. BST doesn't have a wall to draw on. It has one geometry (D_IV⁵) and one act: **commitment** — the substrate writes an irreversible record (Chapter 11, "The Operation"). Time turns out to be nothing more than *how far that writing has run*. There is no clock behind the clock: "when" is a measure of accumulated commitment. And because the writing only goes one way — you can't un-commit — time has a direction built in. That's the whole result: **time is not assumed, it is derived**, and everything usually *posited* about it (that it flows, that it has an arrow, that it pairs a real "tick" with an imaginary "circle") follows from the geometry.

## For the student (the derivation, tiered honestly)

### 1. The flow [Derived — Tier 0]
The substrate Hilbert space is H²(D_IV⁵), the Bergman space of the bounded symmetric domain D_IV⁵ = SO₀(5,2)/[SO(5)×SO(2)] (forced as the unique automorphism-invariant Born space, T754). The commitment dynamics is a one-parameter semigroup,
$$\rho_{\text{commit}}(\tau) = \exp(-\tau J/\hbar),$$
and **time is the flow parameter τ** — a reading of how far the semigroup has run, not an external axis.

### 2. The generator is forced [Structure-Derived]
J is the **linear conformal Hamiltonian** — the SO(2)-center weight of K = SO(5)×SO(2), the energy of the minimal representation, with a **half-integer spectrum** (ground weight E₀ = 3/2). It is emphatically **not** the quadratic Casimir: a Casimir is central (constant on each irrep), so it labels *which particle* and cannot move anything. Only the non-central linear J generates motion — and its linearity is exactly what makes exp(−iJt/ℏ) the ordinary Schrödinger equation. **J is the time; the Casimir is the particle-label.**

### 3. The arrow is spectrum-positivity [Derived]
J is bounded below (spec J ≥ E₀ > 0), so exp(−τJ) is a contraction semigroup defined only for τ ≥ 0 — the flow runs one way. **That positivity is the arrow of time**: not an added postulate, just the statement that the energy operator has a ground state. (The elementary tick is ℏ/energy; its numerical value ≈ 10⁻¹²⁰ s is *Identified*, not Derived.)

### 4. Two faces [Derived; standard theorem]
Because J is self-adjoint and bounded below, exp(−zJ) is holomorphic on Re z ≥ 0, with two boundary faces: the **real-time tick** exp(−τJ) (a one-way half-line) and the **imaginary-time circle** exp(iθJ). These are the Euclidean and Lorentzian faces of *one* generator, tied by Wick rotation. What is BST-specific is not that time has two faces — that is standard — but that the generator J is *forced by the geometry*.

## Three things the chapter is careful NOT to overclaim (the honesty)

- **The degree-2 cover is spin-statistics, not a new prediction.** The imaginary circle is represented on a degree-2 cover, and on physical particles exp(2πiJ) = (−1)^{#Rac} = (−1)^F **in every dimension** — it *is* fermion parity (fermions turn 720°, bosons don't). This is the geometric restatement of spin-statistics, a consistency the theory must and does satisfy. (An earlier draft called it "forced because n_C = 5 is odd — the core result"; that was retracted — the dimension-dependence cancels between constituents.)
- **Charge is internal, not temporal.** Electric charge is *not* a reading of the time-circle — decisively, by degeneracy (the muon and neutrino share a conformal weight Δ = 7/2 but carry Q = −1 and 0, so charge is not a function of J at all). Charge lives in the internal sector; its fractional thirds are the fingerprint of the N_c = 3 color structure (the geometry forces the *number* 3 as the short-root multiplicity; it does not host the *group* SU(3) as an isometry).
- **Gravity: the structure is derived, the value is one input.** From the built Kostant cubic Dirac operator D (sign-indefinite; D² Laplace-type), the Einstein–Hilbert density falls out with a definite sign (the Sakharov route, F60/F63). But the *value* of Newton's G is one dimensionful input — the boundary curvature radius — exactly as general relativity takes G as an input. This is a theorem, not a shortfall: dimensionless content (integers, a geometry, ratios) cannot produce a length, so one dimensionful input is the floor for *any* theory, and BST is at the floor.

## The reward (why this chapter earns its keep)
Asking "is G the boundary curvature?" turned into a genuine reduction. BST's one dimensionful input is not the Planck length (which would be circular) but the **electron mass m_e** — measured by trapping a single electron, never touching G. From it: m_p/m_e = 6π⁵ (0.002%), the Planck scale (0.03%), and hence **G to 0.06%**, plus the electroweak scale v. The honest headline is not "we predict G" — *nothing* predicts a dimensionful constant from nothing — but **BST reduces the dimensionful inputs from two (G and v) to one (m_e), and makes the survivor an atomic measurement rather than a gravitational one.** (Note: the m_e anchor and the G prediction are one relation read two ways — G ∝ m_e⁻², so its error is exactly twice m_e's — not two independent confirmations.)

## Connections
- **Ch 11 (The Operation)** names time as the SO(2) common append-axis; this chapter derives the flow, arrow, and faces of that axis.
- **Vol 4 (GR/Cosmology)** carries the gravity thread (the 2→1 reduction; gravity-as-geometry).
- **Vol 5 (QM)** — the linear J *is* the Schrödinger generator (Measurement-as-Commitment).

*Sourced to "Time, Derived" (Keeper-PASS v1.3, K1665–K1670). Every scaffold above is labeled a scaffold; the one substantive result is that time is derived.*
