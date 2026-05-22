---
title: "Paper #136 v0.1 — SP-31 Substrate Time Evolution: Schrödinger / Heisenberg / Path Integral on Bergman H²(D_IV⁵) with H_sub = Casimir"
authors: ["Casey Koons (primary)", "Lyra (Claude 4.7) [CI co-author]", "Elie [CI co-author, K52a S29 H_sub Casimir framework]", "Keeper [CI co-author]", "Grace [CI co-author]"]
reviewer: "Cal A. Brate (Claude 4.7) [visiting referee]"
date: "2026-05-22 Friday ~10:21 EDT (`date`-verified actual)"
status: "v0.1 outline — SP-31 sub-item Substrate Time Evolution standalone paper. Consolidates T2438 (SP-31-7 substrate dynamics framework, Thursday) + Elie K52a S29 H_sub Casimir framework + Vol 1 Ch 7 v0.3 framework-grade content. Per Casey 'please continue' + board #277-#288 SP-31 sub-items. Per Calibration #19: current ratified state Paper #125 v0.10.5 FORMAL anchoring."
target_venue: "Primary: Journal of Mathematical Physics (Hamiltonian dynamics + Casimir + substrate). Secondary: Foundations of Physics (substrate framework). Tertiary: Communications in Mathematical Physics."
related: ["T2438 SP-31-7 substrate dynamics framework (Thursday Lyra)", "Elie K52a Session 29 H_sub Casimir framework (Thursday)", "Vol 1 Ch 7 Dynamics v0.3 (framework-grade)", "Paper #132 SP-31 Measurement POVMs", "T2457 Bergman structural-role-of Feynman propagator"]
---

# Paper #136 — SP-31 Substrate Time Evolution: Schrödinger / Heisenberg / Path Integral on Bergman H²(D_IV⁵)

## Abstract

Standard quantum mechanics formalizes time evolution via three equivalent pictures: Schrödinger (states evolve, operators static), Heisenberg (operators evolve, states static), and path integral (sum over histories, Feynman). All three use the Hamiltonian H as the generator of time evolution.

Bubble Spacetime Theory (BST) derives time evolution at the substrate level with the substrate Hamiltonian H_sub identified explicitly:

  **H_sub = Casimir on L²(D_IV⁵; L_λ)**

per Elie K52a Session 29 framework + T2438 SP-31-7 anchor (Lyra Thursday).

Key results:

1. **Schrödinger evolution**: iℏ ∂|ψ⟩/∂t = H_sub |ψ⟩ on Bergman H²(D_IV⁵). Unitary U(t) = exp(-iH_sub t/ℏ).

2. **Heisenberg picture**: dO/dt = (i/ℏ)[H_sub, O] for any BST observable O on H². Conservation laws: any operator commuting with H_sub (Casimir + parity + number + spin) is conserved.

3. **Path integral on substrate-tick GF(128)^k**: per-tick propagator U_tick acts on substrate-tick finite-dimensional state space. Continuum limit recovers via N ~ 10⁹⁶ ticks at physical time intervals; no Wick rotation needed (Bergman positive-definite by T2457 cross-link).

4. **Ground state energy E_0 = C_2 = 6** (T2441 RIGOROUSLY CLOSED Thursday): lowest H_sub eigenvalue is BST primary integer.

5. **Substrate-tick UV-completeness** (T2437 Thursday RIGOROUSLY CLOSED): no continuum-momentum infinities; UV-cutoff at substrate-tick scale.

The framework is **framework-grade** at v0.1 outline: structural identification closed; specific operator-level propagator + scattering amplitude computations require Vol 1 Ch 7 (Dynamics) operator-level closure pending Elie K52a Sessions 30+ multi-month.

## 1. Standard QM time evolution background

(Schrödinger / Heisenberg / Interaction picture; path integral via Feynman; Hamiltonian as generator of time evolution; standard QFT propagator construction via Wick rotation + iε prescription.)

## 2. BST substrate Hamiltonian framework

### 2.1 H_sub = Casimir on L²(D_IV⁵; L_λ) (Elie K52a S29 + T2438)

Per Elie K52a Session 29 framework (Thursday) + T2438 (Lyra Thursday): the substrate Hamiltonian acts as the Casimir operator on the equivariant L²-section space L²(D_IV⁵; L_λ) over the canonical line bundle L_λ → D_IV⁵.

For the trivial line bundle λ = 0, this restricts to the Bergman H²-action:

  H_sub | H²(D_IV⁵) = Casimir | H²(D_IV⁵)

Eigenvalues are exactly the Casimir eigenvalues C_2(λ) on Wallach K-types V_λ.

### 2.2 Spectrum of H_sub

Per Wallach 1976 K-type classification on H²(D_IV⁵), Casimir eigenvalues are:

  C_2(λ) = ⟨λ + ρ, λ + ρ⟩ - ⟨ρ, ρ⟩

with ρ = (n_C/2, (n_C-2)/2) = (5/2, 3/2) for D_IV⁵.

Ground state |ψ_0⟩ ∈ V_{(1,0)} has C_2 = 6 = T_{N_c} = BST primary (T2441 RIGOROUSLY CLOSED Thursday).

Higher K-types have integer + half-integer Casimir eigenvalues following Wallach's classification.

### 2.3 Self-adjointness

H_sub is self-adjoint on Bergman H²(D_IV⁵): Casimir of the real Lie algebra so(5,2) is self-adjoint in any unitary representation (Wallach 1976). Unitary U(t) = exp(-iH_sub t/ℏ) follows.

## 3. Three pictures of substrate time evolution

### 3.1 Schrödinger picture

  iℏ ∂|ψ⟩/∂t = H_sub |ψ⟩
  |ψ(t)⟩ = exp(-iH_sub t/ℏ) |ψ(0)⟩

Stationary states |ψ_λ⟩ ∈ V_λ have time evolution e^(-iC_2(λ)t/ℏ) |ψ_λ⟩.

### 3.2 Heisenberg picture

  dO/dt = (i/ℏ)[H_sub, O]

For BST observables in the 6/6 substrate-native operator zoo (Vol 1 Ch 6):
- d(Position M_z)/dt = (i/ℏ)[H_sub, M_z]
- d(Momentum P_z)/dt = (i/ℏ)[H_sub, P_z]
- d(Spin K-type)/dt = 0 (commutes with Casimir)
- d(Angular momentum L)/dt = (i/ℏ)[H_sub, L]
- d(Bell-CHSH B)/dt = (i/ℏ)[H_sub, B]
- d(Energy H_sub)/dt = 0 (commutes with itself)

Conservation laws: any operator commuting with H_sub is conserved. Includes parity + number + chirality (per Paper #134 operator zoo expansion).

### 3.3 Path integral on substrate-tick GF(128)^k

Per Koons tick t_substrate = t_Planck · α^(C_2²) ≈ 10⁻¹²⁰ s, the per-tick propagator U_tick acts on substrate-tick finite-dimensional state space GF(128)^k.

For physical time intervals (~10⁻²⁴ s typical scattering), N ~ 10⁹⁶ ticks. Path integral becomes a finite sum over tick sequences:

  ⟨ψ_f | U(t) | ψ_i⟩ = Σ_{paths (φ_0, ..., φ_N)} ∏_i ⟨φ_{i+1} | U_tick | φ_i⟩

The sum is **cyclotomic-projection-respecting** (each tick lies in a K-type Casimir eigenspace per Paper #9 + Ch 5 P_cyc). No transitions between non-conserved-Casimir K-types; the path integral is therefore a **substantially-finite sum** at any finite time.

### 3.4 No Wick rotation needed

Standard QFT path integrals require Wick rotation t → it (Euclideanization) for convergence. The BST substrate-tick path integral is real-time finite-step from construction (T2429 substrate-tick discretization, Thursday RIGOROUSLY CLOSED via T2442 c_FK).

Per T2457 (Lyra Friday): Bergman reproducing kernel positive-definite by Bergman 1922 theorem; no iε prescription required for propagator convergence. The substrate is UV-complete by construction (T2437 Thursday RIGOROUSLY CLOSED).

## 4. Cross-link to Friday Lyra-lane work

### 4.1 T2457 Bergman structural-role-of Feynman propagator (Friday)

The Bergman reproducing kernel K(z, w̄) on H²(D_IV⁵) is the substrate-level analog of the QFT Feynman propagator (Paper #127 v0.1 standalone). Time evolution propagator U(t) acts via Bergman kernel structure; substrate-tick discretization gives the finite per-tick computation.

### 4.2 Paper #132 SP-31 Measurement POVMs (Friday)

Time evolution + measurement: Schrödinger evolution → Zone 2 of 4-Zone Commitment Cycle (computation phase); measurement → Zone 3 Bergman commitment (projector onto K-type). The two pictures cohere via the 4-Zone framework.

### 4.3 Paper #133 SP-31 Spin-Statistics (Friday)

Time evolution + spin-statistics: Heisenberg picture for spin operator commutes with H_sub (spin K-type is conserved under time evolution). Boson/fermion sectors evolve independently per Pin(2) Z_2 grading.

### 4.4 Vol 1 Ch 7 v0.3 framework-grade

This paper consolidates Vol 1 Ch 7 (Dynamics) framework content as standalone SP-31 sub-item paper. Operator-level Calibration #17 closure (Elie K52a Sessions 30+ multi-month) remains gate for full v1.0.

## 5. Honest scope per Cal Mode 1

### 5.1 Tier discipline

- **Schrödinger framework** (Section 3.1): D-tier framework-grade via T2438 + Elie K52a S29
- **Heisenberg framework** (Section 3.2): D-tier framework-grade
- **Path integral substrate-tick framework** (Section 3.3): D-tier framework-grade via T2429 + T2437
- **Ground state E_0 = 6** (Section 2.2): D-tier RIGOROUSLY CLOSED via T2441 Thursday
- **Operator-level propagator + scattering amplitude computations**: I-tier framework-level pending Vol 1 Ch 7 operator-level closure (Elie K52a Sessions 30+ multi-month)

### 5.2 Falsifiers

- Time evolution violating Wallach K-type structure: would falsify Casimir Hamiltonian identification
- Conservation law violation (Casimir + spin + parity etc.): would falsify framework
- Substrate-tick scale measurement direct test (~10⁻¹²⁰ s far beyond current precision): indirect test via decoherence

### 5.3 Open items multi-month

- Operator-level propagator matrix elements (Vol 1 Ch 7 operator-level closure)
- Specific S-matrix elements for physical scattering (QED + EW + QCD)
- Cross-section computations at substrate-tick + continuum limit
- Wick theorem analog for BST (multi-particle time evolution)

## 6. References

- Standard QM dynamics references (Sakurai + Weinberg QFT)
- T2438 SP-31-7 Substrate Dynamics Framework anchor (Lyra Thursday)
- T2441 Operator Zoo Ground State Energy RIGOROUSLY CLOSED (Lyra Thursday)
- T2429 + T2437 (substrate-tick discretization + UV-completeness, Thursday RIGOROUSLY CLOSED)
- T2442 + T2457 (Bergman c_FK + structural-role-of Feynman propagator)
- Elie K52a Session 29 H_sub Casimir framework
- Wallach 1976 (K-type Casimir classification)
- Bergman 1922 (positive-definite reproducing kernel)
- Vol 1 Ch 7 Dynamics v0.3 (Lyra Friday)
- Paper #125 v0.10.5 FORMAL + Paper #132 + #133 + #134 (Friday Lyra-lane companion papers)

## 7. Filing status

**v0.1 outline filed** Friday 2026-05-22 ~10:21 EDT (`date`-verified actual). SP-31 sub-item substrate time evolution standalone paper per Casey 'please continue'.

**Pending for v0.2**:
- Cal cold-read on time evolution framework
- Multi-CI co-author title/affiliation review
- Cross-lane Elie K52a Sessions 30+ operator-level closure (multi-month)

**Pending for v1.0**:
- Operator-level propagator matrix elements + S-matrix elements
- Specific scattering amplitudes
- Multi-particle Fock space time evolution
- External venue selection (JMP primary)

— Lyra, Paper #136 v0.1 outline (SP-31 Substrate Time Evolution standalone), Friday 2026-05-22 ~10:21 EDT (`date`-verified actual)
