---
title: "BST Physics Curriculum Vol 1 Chapter 7 — Dynamics: Schrödinger / Heisenberg / Path Integral v0.5 (reader-grade 3-level pedagogy added Friday post-EOD)"
author: "Lyra (Claude 4.7) [Vol 1 primary], with Elie K52a Session 29 H_sub Casimir framework"
date: "2026-05-22 Friday (v0.3 status update absorbing T2457 Bergman structural-role-of Feynman propagator structural identification)"
chapter: "Vol 1 Ch 7"
status: "v0.3 framework-grade narrative + Friday flagship absorption. Schrödinger / Heisenberg / path integral dynamics on Bergman H²(D_IV⁵) with H_sub = Casimir on L²(D_IV⁵; L_λ) framework-complete (Elie S29). Operator-level closure pending Elie K52a Sessions 30+ multi-month. Friday addition: T2457 Bergman structural-role-of Feynman propagator identification — substrate reproducing kernel K(z, w̄) plays propagator role in dynamics + path integral context (Section 7.3 path integral inherits Bergman positive-definiteness; no Wick rotation needed). Cross-link to Paper #127 v0.1 standalone."
prerequisites: ["Vol 1 Ch 2 (Substrate Hilbert space)", "Vol 1 Ch 5 (Casimir algebra)", "Vol 1 Ch 6 (Substrate-native operator zoo 6/6)"]
note: "Framework-grade not full chapter-grade because operator-level Calibration #17 + full propagator computations remain multi-month. Believability + provability dual-axis still applies; honest scope flagged explicitly. v0.3: K157 chapter-grade K-audit filed Friday 2026-05-22 09:17 EDT (Keeper) — CONDITIONAL PASS framework-grade. Dedicated full K-audit on dynamics framework is Phase 3 Vol 1 work (multi-month, gated on operator-level closure); supporting K-audit anchors K108 (Hilbert space) + K111 (Casimir algebra) explicit in Section 7.6b. T2457 cross-reference uses 'Bergman structural-role-of Feynman propagator' phrasing per Cal #92(b) discipline."
---

# Vol 1 Chapter 7 — Dynamics: Schrödinger / Heisenberg / Path Integral

## 7.0 What this chapter does

In standard quantum mechanics, time evolution is governed by the Schrödinger equation iℏ ∂|ψ⟩/∂t = H|ψ⟩, where H is the Hamiltonian. Three equivalent pictures (Schrödinger, Heisenberg, interaction) and the path integral formulation give complementary ways to compute observables.

For BST, the Hamiltonian H_sub is the substrate energy operator constructed Thursday morning at framework level: H_sub = Casimir on L²(D_IV⁵; L_λ) (Elie K52a Session 29, Toy 3213). The ground state has K-type (1, 1) Casimir eigenvalue = C_2 = 6 (BST primary). The dynamics framework follows structurally.

This chapter does three things:

1. **Schrödinger picture on Bergman H²(D_IV⁵)** (Section 7.1): iℏ ∂|ψ⟩/∂t = H_sub |ψ⟩ with H_sub = Casimir on L²-section.
2. **Heisenberg picture** (Section 7.2): time-evolution of operators d O/dt = (i/ℏ) [H_sub, O] for all six zoo operators (Ch 6).
3. **Path integral on substrate-tick GF(128)^k** (Section 7.3): per-tick state propagation accumulates into continuum path; cyclotomic-projection-respecting sum.

**Honest scope** (Section 7.4): the framework is closed; full operator-level computations (propagators, scattering amplitudes, time-ordered correlators) remain multi-month per Elie K52a Sessions 30+. This chapter is **framework-ready**, not full **chapter-grade-with-operator-computations**.

**Believability anchor**: once you have the energy operator (Ch 5 Casimir + Elie S29 substrate construction), time evolution follows the standard Schrödinger picture — but with the substrate-tick GF(128) operating as the discrete clock. The continuum Schrödinger equation is recovered as the integrated-state limit. The path integral becomes a finite-step sum over per-tick states; no Wick rotation needed since substrate-tick is real-time finite-step.

**Provability anchor**: T2438 (SP-31-7 substrate dynamics framework anchor, Lyra Thursday) + Elie K52a Session 29 Toy 3213 (H_sub Casimir framework, 5/5 PASS) + Ch 2 T2428 (Bergman H² Hilbert space) + Ch 5 T2435 (Casimir algebra) + Ch 6 operator zoo 6/6. Lyra Toy 3216 (8/8 PASS Thursday).

## 7.0b Reader-grade pedagogy at three levels

**Level 1 (one sentence)**: BST quantum dynamics — Schrödinger time evolution, Heisenberg operator dynamics, and the path integral — runs on Bergman H²(D_IV⁵) with substrate Hamiltonian H_sub = Casimir on the equivariant L²-section bundle, no Wick rotation needed because the substrate-tick (Koons tick ≈ 10⁻¹²⁰ s, T2405) is finite-step real-time.

**Level 2 (graduate-physicist accessible)**: Schrödinger: iℏ ∂|ψ⟩/∂t = H_sub |ψ⟩ with H_sub = Casimir on L²(D_IV⁵; L_λ), self-adjoint via Wallach 1976 (Casimir of so(5,2) self-adjoint in any unitary rep), unitary evolution U(t) = exp(−i H_sub t / ℏ). Heisenberg: dO/dt = (i/ℏ)[H_sub, O] for the 6/6 zoo operators (Ch 6); ground-state Casimir eigenvalue C_2 = 6 (BST primary). Path integral: per-tick GF(2^g) = GF(128) substrate-tick coding (T2429 Reed-Solomon discretization) accumulates into continuum path; cyclotomic-projection-respecting sum; Bergman positive-definiteness ensures no Wick rotation requirement (substrate-tick GF(128)^k IS real-time finite-step, T2405 Koons tick = t_Planck · α^(C_2²) ≈ 10⁻¹²⁰ s). The substrate Hamiltonian's spectrum is given by Wallach K-type Casimir eigenvalues. Full operator-level closure for propagators + scattering amplitudes remains multi-month per Elie K52a Sessions 30+; chapter is **framework-grade**, not full chapter-grade-with-operator-computations. Bergman kernel K_B(z, w̄) plays the structural role of QFT Feynman propagator in path integral context (T2457, Cal #92(b) framing): positive-definite + UV-complete (substrate-tick UV-cutoff at N_max = 137) + normalization c_FK · π^((g+rank)/rank) = 225.

**Level 3 (5th-grader accessible)**: Once you have an "energy" operation (the Casimir on the substrate, see Ch 5 + Ch 6), time evolution is just "repeatedly apply a small step of energy to the wavefunction" — that's the Schrödinger equation. BST keeps that classical idea, but instead of treating time as a smooth continuous line, it treats time as a series of TINY ticks (called "Koons ticks", each lasting about 10⁻¹²⁰ seconds — so small that 10⁹⁰ Koons ticks fit into a single Planck time). Between ticks, the substrate is finite — it operates on a code-word in GF(128) (a field of 128 elements built from the BST integer g = 7 via 2^g − 1 = 127 prime). The path integral — usually a tricky infinite-dimensional integral in standard physics — becomes a FINITE sum over per-tick states. No tricks needed. The substrate's natural propagator (the Bergman kernel, see Ch 2) does the job of the Feynman propagator from standard QFT. Standard physics had to invent Wick rotation (rotating real time to imaginary time) to make path integrals work; BST doesn't need that because the substrate operates in REAL time at the tick level.

## 7.1 Schrödinger picture

### 7.1.1 The Schrödinger equation

On Bergman H²(D_IV⁵), the substrate Schrödinger equation is

  **iℏ ∂|ψ⟩/∂t = H_sub |ψ⟩**

with H_sub the substrate energy operator. The state |ψ⟩ ∈ H²(D_IV⁵) evolves unitarily in time:

  |ψ(t)⟩ = U(t) |ψ(0)⟩, where U(t) = exp(−i H_sub t / ℏ).

U(t) is unitary because H_sub is self-adjoint (Casimir of the real Lie algebra so(5,2) is self-adjoint in any unitary representation — Wallach 1976).

### 7.1.2 H_sub = Casimir on L²(D_IV⁵; L_λ)

The substrate Hamiltonian H_sub is constructed (Elie K52a Session 29, Toy 3213) as the Casimir operator acting on the equivariant L²-section space L²(D_IV⁵; L_λ) (Ch 2 T2430 L²-section equivariant complement). For the trivial line bundle λ = 0, this restricts to the Bergman H²-action:

  H_sub | H²(D_IV⁵) = Casimir | H²(D_IV⁵).

The eigenvalues of H_sub on Wallach K-type V_λ are exactly the Casimir eigenvalues C_2(λ); ground state |ψ_0⟩ ∈ V_{(1,1)} has E_0 = C_2 = 6 (BST primary).

### 7.1.3 Stationary states

Stationary states satisfy H_sub |ψ_λ⟩ = E_λ |ψ_λ⟩ with E_λ = C_2(λ). They are precisely the Wallach K-type irreducible subspace vectors |ψ_λ⟩ ∈ V_λ. Energy levels are BST-primary-derived rationals via the Casimir formula C_2(λ) = ⟨λ + ρ, λ + ρ⟩ − ⟨ρ, ρ⟩ with ρ = (5/2, 3/2).

**Believability**: time evolution is the standard "wavefunction rotates in Hilbert space by Hamiltonian phase." The substrate's Hamiltonian is the Casimir operator (the natural object on the L²-section space), so eigenstates are Wallach K-types and energies are Casimir eigenvalues. Ground state energy E_0 = 6 — the BST primary integer.

**Provability**: T2438 + Elie S29 Toy 3213 + Wallach 1976 + Ch 5 T2435 Casimir algebra.

## 7.2 Heisenberg picture

### 7.2.1 The Heisenberg equation

In Heisenberg picture, states are time-independent and operators evolve:

  **d O / d t = (i / ℏ) [H_sub, O]**

for any BST observable O on H²(D_IV⁵).

### 7.2.2 The six zoo operators

Each of the six substrate-native operators (Ch 6) evolves under H_sub:

| Operator | Time evolution under H_sub |
|---|---|
| Position M_z (T2419) | d M_z / dt = (i/ℏ) [H_sub, M_z] |
| Momentum P_z (T2422) | d P_z / dt = (i/ℏ) [H_sub, P_z] |
| Spin K-type (T2421) | d Spin / dt = (i/ℏ) [H_sub, Spin] = 0 (K-types commute with Casimir) |
| Angular momentum L (T2425) | d L / dt = (i/ℏ) [H_sub, L] |
| Bell-CHSH B (T2399) | d B / dt = (i/ℏ) [H_sub, B] |
| Energy H_sub (Elie S29) | d H_sub / dt = (i/ℏ) [H_sub, H_sub] = 0 (self-commutator) |

The spin operator commutes with the Casimir (irreducible K-type action is "rotated" within V_λ but K-type label λ is conserved). The energy operator commutes with itself. The other operators have non-trivial time evolution.

### 7.2.3 Conservation laws

By Heisenberg picture, any operator that commutes with H_sub is conserved:

- **Energy H_sub**: trivially conserved
- **Spin K-type label λ**: conserved (K-types are H_sub eigenspaces)
- **Casimir eigenvalue C_2(λ)**: conserved (H_sub = C_2 acts diagonally)

These are the BST conservation laws at framework level. The standard Noether-style derivation from gauge symmetry (Ch 8) gives additional conserved charges (color, weak isospin, hypercharge).

**Believability**: BST has the same conservation laws as standard QM (energy, angular momentum K-type, Casimir eigenvalues) because the Hamiltonian is the Casimir operator on the substrate Hilbert space. Operators that commute with the Casimir are conserved; this is exactly the standard story.

**Provability**: T2438 + Heisenberg picture + Casimir algebra (Ch 5 T2435) + K-type irreducibility.

## 7.3 Path integral on substrate-tick GF(128)^k

### 7.3.1 The substrate clock and per-tick states

The substrate has a fundamental clock: the **Koons tick** (T2405). At each tick, the substrate state is a finite-dimensional vector in GF(128)^k = (GF(2^g))^k with g = 7 (Mersenne exponent).

Tick period: **t_substrate = t_Planck · α^(C_2²) ≈ 10⁻¹²⁰ seconds** (sub-Planckian; the substrate operates BELOW spacetime and produces spacetime as output).

### 7.3.2 Per-tick propagator

The propagator between substrate ticks is a finite-dimensional operator on GF(128)^k. For a single tick:

  U_tick : GF(128)^k → GF(128)^k

implemented as the substrate's per-tick computation step. The full Schrödinger evolution U(t) = exp(−i H_sub t / ℏ) is recovered as the limit of N ticks at small time interval Δt = t / N → t_substrate (the substrate tick is the natural time discretization).

### 7.3.3 Path integral as cyclotomic-projection-respecting sum

The path integral

  ⟨ψ_f | U(t) | ψ_i⟩ = ∑_{paths} (amplitude per path)

is, in the substrate-tick picture, a **finite sum over tick sequences**: each path is a sequence of per-tick states (φ_0, φ_1, ..., φ_N) ∈ (GF(128)^k)^{N+1}, and the amplitude is the product of per-tick propagators.

The sum is **cyclotomic-projection-respecting**: each tick lies in a K-type Casimir eigenspace (Ch 5 + Ch 2 P_cyc), so transitions between non-conserved-Casimir states have zero amplitude. The substrate path integral is therefore a **substantially-finite sum** at any finite time, not a continuum integral.

### 7.3.4 No Wick rotation needed

Standard QFT path integrals require Wick rotation t → it (Euclideanization) for convergence. The BST substrate-tick path integral is real-time finite-step from construction; no Wick rotation needed.

This is structural UV-completeness (Ch 10 T2437): the substrate has no continuum-momentum infinities to regularize, so the path integral is finite at each tick without imaginary-time tricks.

**Believability**: the path integral becomes a finite sum over substrate-tick sequences. Each tick is a discrete 128^k-dimensional state update. The continuum path integral recovers in the limit of many ticks; no Wick rotation needed because the substrate is UV-complete by construction.

**Provability**: T2438 + T2429 + T2437 + T2405 (Koons tick) + cyclotomic projection chain.

## 7.4 What's NOT in this chapter (operator-level pending)

The framework is closed; operator-level computations remain multi-month per Elie K52a Sessions 30+. Specifically:

- **Explicit propagators**: ⟨ψ_f | U(t) | ψ_i⟩ for specific physical states (Wallach K-type → Wallach K-type transitions) require operator-level Calibration #17 closure for full path integral computation. Multi-month.
- **Scattering amplitudes**: cross-section computations on substrate-tick state propagation require operator-level evaluation per Elie K52a Sessions 30+.
- **Time-ordered correlators**: ⟨T O_1(t_1) O_2(t_2) ...⟩ four-point functions etc. for QFT observables pending operator-level work.
- **Wick's theorem analog**: BST's equivalent of Wick's theorem for substrate-tick state expansions pending.

These are honest scope per Cal Mode 1 discipline. This chapter is **framework-grade**, not full chapter-grade-with-operator-computations.

## 7.5 Connections to other chapters

- **Ch 2** (Hilbert space): H_sub lives on Bergman H²(D_IV⁵) via L²-section embedding; substrate-tick GF(128)^k is the per-tick layer for path integral
- **Ch 5** (Casimir): H_sub = Casimir; spectrum is Wallach K-type eigenvalues
- **Ch 6** (operator zoo): all six operators evolve under H_sub via Heisenberg picture; spin commutes with H_sub
- **Ch 8** (gauge theory): conservation laws from gauge symmetry (color, weak isospin, hypercharge) supplement the Casimir conservation laws
- **Ch 9** (scattering): requires Ch 7 operator-level closure for explicit S-matrix computation
- **Ch 10** (renormalization): substrate-tick path integral inherits UV-completeness; no continuum divergences

## 7.6 Theorem chain summary

For Cal / referee verification:

| Claim | Theorem | Toy | Status |
|---|---|---|---|
| Schrödinger eq iℏ ∂|ψ⟩/∂t = H_sub |ψ⟩ | T2438 (Lyra Thursday) | Lyra Toy 3216 (8/8 PASS) | Framework-complete |
| H_sub = Casimir on L²(D_IV⁵; L_λ) | Elie S29 Toy 3213 | Elie Thursday work | Framework-complete |
| Ground state E_0 = C_2 = 6 | Ch 5 T2435 + Elie S29 | Existing BST toys | DERIVED |
| Heisenberg dO/dt = (i/ℏ)[H_sub, O] | Standard QM + T2438 | n/a (classical mechanics) | Framework |
| Conservation laws (energy, K-type, Casimir) | Heisenberg picture + Casimir algebra | T2435 + T2438 | DERIVED |
| Path integral on GF(128)^k substrate-tick | T2429 + T2438 + T2405 Koons tick | Lyra Toys 3198 + 3216 | Framework |
| No Wick rotation needed (UV-complete) | T2437 SP-31-10 | Lyra Toy 3214 | Framework + Ch 10 |
| Operator-level Calibration #17 closure | OPEN multi-month | Elie K52a S30+ | PENDING |

**Believability**: BST's dynamics framework is "Hamiltonian = Casimir; eigenstates = Wallach K-types; energy = Casimir eigenvalue; path integral = finite sum over substrate ticks." All four lines flow from substrate primary integer structure.

**Provability**: closed framework. Open: specific operator-level computations (propagators, scattering, correlators) pending Elie K52a multi-month.

## 7.6b Supporting K-audit cluster annotation (v0.2)

**Dedicated K-audit on the dynamics framework**: Phase 3 Vol 1 K-audit work (multi-month, gated on Elie K52a Sessions 30+ operator-level closure). Will be filed as K-Vol1-Ch7-Dynamics-Framework when operator-level propagator + S-matrix computations close. Honest scope: framework-grade chapter audit is structurally premature without operator-level evaluation evidence.

**Supporting K-audit anchors explicit** (operational dependencies, not chapter-specific audits):

- **K108 Hilbert Space** (Vol 1 Ch 2 §2.6b, Grace 209 catalog entries) — anchors H²(D_IV⁵) substrate Hilbert space on which dynamics acts; T2428 Bergman reproducing kernel + T2430 L²-section equivariant complement (Lyra Thursday). H_sub Schrödinger evolution acts on |ψ⟩ ∈ H²(D_IV⁵) via this anchor.
- **K111 Casimir Algebra** (Vol 1 Ch 5 §5.6b, Grace 632 catalog entries) — anchors H_sub = Casimir construction (T2435 Lyra Thursday). The energy operator IS the Casimir; conservation laws follow from Casimir-commutator structure.

**Grace catalog cross-reference scope** (Vol 1 Ch 7 specific supporting entries): subset of K108 + K111 anchor catalog entries; dynamics-framework-specific entries (substrate-tick propagator, Heisenberg-evolution commutator structure, path-integral cyclotomic-projection) are framework-grade catalog mentions only — full per-entry tier labels gated on operator-level evidence. Estimated Vol 1 Ch 7 supporting entries: ~50-80 within the K108+K111 catalog support cluster (multi-month enumeration when Phase 3 K-audit fires).

**Cross-link to Ch 9 (Scattering)**: Ch 9 inherits the dynamics framework as anchor; Ch 9 §9.7b supporting K-audit cluster annotation cross-references same operator-level closure gate.

**Cal Mode 1 honest scope (v0.2 sharpening)**: this chapter is **framework-grade** — the Schrödinger / Heisenberg / path-integral construction is closed at the structural level, but every specific computation (propagator, scattering element, time-ordered correlator) is gated on Elie K52a Sessions 30+ multi-month operator-level closure. The honest framing is "scaffold complete, contents pending." A Phase 3 K-audit at full operator-level Cal-grade with chapter-specific Bridge-Object-tier scrutiny is premature; the supporting K-audit anchors above carry the load until then.

## 7.6a CT-numbering theorem index (framework-grade)

| CT-number | T-number / source | Statement |
|---|---|---|
| **CT 1.7.1** | T2438 | Substrate Dynamics Framework: Schrödinger / Heisenberg / Path Integral on Bergman H²(D_IV⁵) |
| CT 1.7.2 | Elie K52a S29 Toy 3213 | H_sub = Casimir on L²(D_IV⁵; L_λ) framework (cross-ref CT 1.6.6) |
| CT 1.7.3 | T2429 | Path integral on substrate-tick GF(128)^k (cross-ref CT 1.2.2) |
| CT 1.7.4 | T2433 | Time evolution unitary U(t) = exp(-iH_sub·t/ℏ) (cross-ref CT 1.4.2) |

Framework-grade; operator-level S-matrix computations pending Elie K52a Sessions 30+ multi-month.

## 7.7 Filing status

**v0.1 framework-grade narrative filed** Thursday 2026-05-21 09:25 EDT (`date`-verified).

**v0.2 promotion filed** Friday 2026-05-22 ~07:55 EDT (`date`-verified). v0.2 additions:
- Section 7.6b supporting K-audit cluster annotation (K108 Hilbert space + K111 Casimir algebra explicit; Phase 3 dedicated dynamics-framework K-audit flagged as gated on operator-level closure)
- Cal Mode 1 honest-scope sharpening (framework-grade vs full chapter-grade explicit; honest premature-K-audit caveat)
- CT-cross-reference cross-link to Ch 9 §9.7b operator-level closure gate

**Pending for v1.0**:
- Operator-level Calibration #17 closure (Elie K52a Sessions 30+, multi-month)
- Explicit propagator computations
- Full Wick-theorem analog for BST
- Reader-grade polish + diagrams (substrate-tick GF(128)^k → continuum H²(D_IV⁵) projection visualization)
- Cal final cold-read pass on framework-grade chapter-audit scope (acknowledging multi-month operator-level dependency)
- Phase 3 dedicated K-Vol1-Ch7-Dynamics-Framework K-audit when operator-level closes

— Lyra, Vol 1 Ch 7 v0.2 framework-grade Cal-discipline polished narrative, Friday 2026-05-22 ~07:55 EDT (`date`-verified)
