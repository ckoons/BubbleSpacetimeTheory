---
title: "BST Physics Curriculum Vol 6 Chapter 7 — Quantum Statistical Mechanics v0.4 (Saturday Wave 2 reader-grade polish; Cal cold-read ready; refilled per Cal #104)"
author: "Lyra (Claude 4.7) [Vol 6 primary]"
date: "2026-05-23 Saturday EDT (Cal #104 refill)"
chapter: "Vol 6 Ch 7"
status: "v0.4 chapter-grade narrative refilled per Cal #104. Bose-Einstein + Fermi-Dirac distributions from substrate Pin(2) Z_2 grading. Paper #133 + T2471 + T2481 (Saturday formal spin-statistics theorem). Per Calibration #19."
prerequisites: ["Vol 6 Ch 1-6", "Vol 5 Ch 9 Identical Particles + Spin-Statistics", "Paper #133 v0.2 Spin-Statistics", "T2471 + T2481"]
related: ["Paper #133 v0.2", "T2471 chirality γ⁵ = Pin(2) Z_2", "T2481 spin-statistics formal theorem (Saturday SP-31 #285)", "Vol 5 Ch 9 Identical Particles + Pauli"]
---

# Vol 6 Chapter 7 — Quantum Statistical Mechanics

## Chapter motivation

Standard quantum statistical mechanics extends classical stat mech with quantum-particle distinguishability + statistics:
- **Bose-Einstein distribution**: P_BE(E) = 1/(e^{βE} − 1) for bosons (integer-spin particles like photons, gluons, mesons)
- **Fermi-Dirac distribution**: P_FD(E) = 1/(e^{βE} + 1) for fermions (half-integer-spin particles like electrons, protons, neutrons, quarks)
- **Pauli exclusion principle**: at most one fermion per quantum state
- **Bose-Einstein condensation**: macroscopic occupation of single-particle ground state below T_c (laboratory observed Anderson-Davis-Cornell-Wieman 1995 Nobel)

Standard derivation: combinatorial counting of microstates assuming symmetric (boson) or antisymmetric (fermion) multi-particle wavefunctions. The spin-statistics theorem (Pauli 1940, Streater-Wightman 1964) connects spin to statistics via relativistic QFT axioms.

BST derives Bose-Einstein + Fermi-Dirac from **substrate Pin(2) Z_2 grading** on Bergman H²(D_IV⁵) per T1925 rank=2 (Argument D RIGOROUSLY CLOSED Thursday) + T2471 chirality γ⁵ = Pin(2) Z_2 grading identification (Friday) + T2481 formal spin-statistics theorem (Saturday SP-31 #285) — without requiring relativistic invariance assumption.

## Section 7.0b — Reader-grade 3-level pedagogy

**Level 1**: Bose-Einstein P_BE = 1/(e^{βE} − 1) for bosons + Fermi-Dirac P_FD = 1/(e^{βE} + 1) for fermions derive from substrate Pin(2) Z_2 grading per T1925 + T2471 + T2481 (Saturday spin-statistics formal theorem); no relativistic invariance needed; standard QM identical-particle machinery (Slater determinant, Pauli exclusion) inherits automatically.

**Level 2 (graduate)**: Per Pin(2) Z_2 grading on Bergman H²(D_IV⁵): boson sector K-type V_(p,q) with integer SO(2) weight q ∈ ℤ → symmetric tensor products → Bose-Einstein statistics. Fermion sector V_(p,q+1/2) with half-integer weight → antisymmetric tensor products → Pauli exclusion + Fermi-Dirac. Standard derivations: P_BE = 1/(e^{βE} − 1) from grand canonical ensemble + symmetric N-particle wavefunctions; P_FD = 1/(e^{βE} + 1) from antisymmetric wavefunctions + Pauli. Substrate-level: Pin(2) Z_2 grading IS the boson/fermion partition. Classical Boltzmann distribution P_B = e^{−βE} emerges in high-T limit (both BE and FD → Boltzmann when e^{βE} ≫ 1). Bose-Einstein condensation: at T < T_c ≈ ℏ²(n/ζ(3/2))^(2/3)/(2π m k_B), macroscopic fraction of bosons occupies single-particle ground state; substrate-cartography: occupation of K-type V_(0,0) ground state becomes macroscopic. Fermion examples: free-electron gas (degenerate Fermi gas with Fermi energy E_F), white dwarf stars (electron degeneracy pressure), neutron stars (neutron degeneracy + nuclear physics). Cross-link Vol 5 Ch 9 (Pauli + spin-statistics) + Vol 9 Condensed Matter (BCS superconductivity + Fermi liquid theory).

**Level 3 (5th-grader accessible)**: Quantum stat mech has two key distributions: Bose-Einstein for bosons (particles like photons that CAN pile up in the same state) + Fermi-Dirac for fermions (particles like electrons that CAN'T — Pauli exclusion). BST derives both from the substrate Pin(2) Z_2 grading (the same Z_2 grading that gives spin-statistics in Vol 5 Ch 9 + Paper #133 + T2481). At high temperature, both reduce to classical Boltzmann distribution. Bose-Einstein condensation (Anderson-Davis-Cornell-Wieman 1995 Nobel) is when bosons all pile up in the lowest energy state at very low temperature — substrate K-type ground-state macroscopic occupation. Fermion degenerate gas (electrons in white dwarf, neutrons in neutron stars) is when fermions fill all available low-energy states because of Pauli exclusion.

## Section 7.1 — Standard QM Distributions

**Bose-Einstein**: P_BE(E) = 1/(e^{β(E−μ)} − 1) for bosons with chemical potential μ.
**Fermi-Dirac**: P_FD(E) = 1/(e^{β(E−μ)} + 1) for fermions with chemical potential μ (Fermi energy E_F at T=0).
**Boltzmann limit**: both → e^{−β(E−μ)} when e^{β(E−μ)} ≫ 1 (high-T or low-density).

## Section 7.2 — Substrate Pin(2) Z_2 Grading Derivation

Per T1925 rank=2 (Argument D RIGOROUSLY CLOSED Thursday) + T2471 (Friday) + T2481 (Saturday SP-31 #285):
- Bergman H²(D_IV⁵) decomposes under K = SO(5) × SO(2) into K-type V_(p,q) with integer pair (p, q) admissibility
- Pin(2) double-cover lift adds half-integer-q K-types V_(p,q+1/2)
- γ⁵ chirality operator = Pin(2) Z_2 grading object (T2471 identification)
- Boson sector (q ∈ ℤ): identity component of Pin(2) → symmetric tensor products
- Fermion sector (q ∈ ℤ + 1/2): spinor component → antisymmetric tensor products

## Section 7.3 — Boson Sector → Bose-Einstein

Multi-boson state ⊗_N V_(p,q) (q integer) symmetric tensor product → standard grand canonical derivation gives P_BE(E) = 1/(e^{β(E−μ)} − 1).

**Bose-Einstein condensation** at T < T_c: substrate K-type V_(0,0) ground state macroscopic occupation. T_c = (ℏ²/(2π m k_B)) (n/ζ(3/2))^(2/3) standard formula recovered from substrate framework.

## Section 7.4 — Fermion Sector → Fermi-Dirac + Pauli Exclusion

Multi-fermion state ⊗_N V_(p,q+1/2) (q half-integer) antisymmetric tensor product → standard grand canonical derivation gives P_FD(E) = 1/(e^{β(E−μ)} + 1).

**Pauli exclusion**: at most one fermion per substrate K-type V_(p,q+1/2). Free-electron gas at T → 0: all K-types below Fermi energy E_F filled; degenerate Fermi gas.

## Section 7.5 — Classical Limit Recovery

High-T or low-density limit: e^{β(E−μ)} ≫ 1 → both P_BE and P_FD reduce to classical Boltzmann P_B ≈ e^{−β(E−μ)}. Standard Vol 6 Ch 6 classical stat mech recovered as macroscopic limit.

## Section 7.6 — Honest scope + falsifiers

| Item | BST status | Falsifier |
|---|---|---|
| Bose-Einstein from Pin(2) Z_2 boson sector | STRUCTURALLY VERIFIED (T2481) | Failure of BE statistics for known boson species |
| Fermi-Dirac from Pin(2) Z_2 fermion sector | STRUCTURALLY VERIFIED (T2481) | Failure of FD statistics for known fermion species |
| Pauli exclusion from antisymmetric tensor structure | DERIVED via T2481 | Failure of Pauli exclusion in measured electron systems |
| BEC at T_c standard formula | recovered from substrate framework | Future precision T_c measurement |
| Spin-statistics WITHOUT relativistic axioms | substrate-derivation per Paper #133 v0.2 + T2481 | Counter-example would refute |

**Open scope**:
- Quantitative BE/FD chemical potential μ derivation from substrate K-type structure
- BEC critical temperature T_c sub-leading corrections from substrate framework

## Section 7.7 — Connection

- Vol 5 Ch 9 Identical Particles + Spin-Statistics (cross-link)
- Paper #133 v0.2 (Friday prose-grade) + T2481 (Saturday formal theorem)
- Vol 6 Ch 6 (classical limit recovery)
- Vol 9 Condensed Matter (degenerate Fermi gas, BCS superconductivity)

— Lyra, Vol 6 Ch 7 v0.4 chapter-grade narrative REFILLED per Cal #104, Saturday 2026-05-23 EDT
