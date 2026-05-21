---
title: "BST Physics Curriculum Vol 1 Chapter 9 — Scattering and the S-matrix v0.1 (framework-grade)"
author: "Lyra (Claude 4.7) [Vol 1 primary], with dependency on Elie K52a operator-level closure (multi-month)"
date: "2026-05-21 Thursday morning"
chapter: "Vol 1 Ch 9"
status: "v0.1 framework-grade narrative. Scattering amplitudes on substrate-tick + Bergman H²(D_IV⁵) at framework level; operator-level S-matrix computations gated on Elie K52a Sessions 30+ multi-month. Believability + provability dual-axis per Cal review discipline; honest scope flagged for multi-month dependencies."
prerequisites: ["Vol 1 Ch 2 (Substrate Hilbert Space)", "Vol 1 Ch 5 (Casimir algebra)", "Vol 1 Ch 6 (Operator zoo 6/6 framework-complete)", "Vol 1 Ch 7 (Dynamics framework-ready)", "Vol 1 Ch 10 (Renormalization: UV-complete)"]
note: "Framework-grade not full chapter-grade because operator-level S-matrix + propagator computations remain multi-month. Believability + provability dual-axis still applies; honest scope flagged explicitly."
---

# Vol 1 Chapter 9 — Scattering and the S-matrix

## 9.0 What this chapter does

In standard QFT, the S-matrix is the most important object: it encodes the probability amplitudes for particle scattering processes that experiment measures. The S-matrix is constructed from Feynman diagrams via the LSZ reduction formula, with infinities regularized by renormalization (Ch 10) and time evolution by the Hamiltonian (Ch 7).

In BST, the analogous structure is **scattering amplitudes on substrate-tick states**: at each Koons tick (T2405), the substrate updates per-tick states in GF(128)^k; the S-matrix is the limit of per-tick propagation operators acting on initial and final asymptotic states in Bergman H²(D_IV⁵) (Ch 2 T2428).

This chapter establishes the **framework-grade structure** for BST scattering theory:

1. **The substrate-tick S-matrix** (Section 9.1): definition + LSZ-analog reduction
2. **Asymptotic states on Bergman H²** (Section 9.2): in-states and out-states in the K-type basis
3. **Tree-level amplitudes from Casimir spectrum** (Section 9.3): leading contributions from Wallach K-type eigenstates
4. **Loop corrections via cyclotomic chain** (Section 9.4): no UV divergences; corrections finite-step (Ch 10 T2437)
5. **Cross-sections + observable amplitudes** (Section 9.5): connection to experimentally measured cross-sections

**Framework-grade scope** (honest per Cal Mode 1):
- The structural construction is closed at framework level
- Explicit operator-level S-matrix elements ⟨ψ_f | S | ψ_i⟩ for specific physical processes (e.g., e⁻ + e⁻ → e⁻ + e⁻ scattering) remain multi-month per Elie K52a Sessions 30+
- This chapter is the **scaffold**; the specific computations are pending

**Believability anchor**: scattering amplitudes are built from the substrate-tick states (the substrate's "computing units") + the energy operator (Ch 7). Once those are in hand, the S-matrix is the standard quantum-mechanical construction: probability amplitudes for transitions from initial to final asymptotic states. BST's contribution is that the per-tick states are finite-dimensional (GF(128)^k), so loop integrals become finite sums.

**Provability anchor**: framework-grade closure via T2428 (Ch 2 Hilbert space) + T2435 (Ch 5 Casimir algebra) + T2438 (Ch 7 dynamics framework) + T2437 (Ch 10 UV-completeness) + Elie S29 H_sub Casimir framework. Operator-level closure pending Elie K52a Sessions 30+ multi-month.

## 9.1 The substrate-tick S-matrix

### 9.1.1 Standard QFT S-matrix

In standard QFT, the S-matrix is defined as

  S = T exp(−i ∫ H_int dt)

where T is time-ordering and H_int is the interaction Hamiltonian. LSZ reduction extracts the on-shell amplitudes from time-ordered correlators of field operators.

### 9.1.2 Substrate construction

The BST analog is built on the substrate-tick framework (Ch 7 T2438):

  **S_BST = lim_{N → ∞} U_tick^N**

where U_tick is the per-tick propagator on GF(128)^k (Ch 2 T2429), and N is the number of Koons ticks elapsed between asymptotic-in and asymptotic-out times.

In practice, N is finite at any physical time interval (substrate-tick = 10⁻¹²⁰ s; physical scattering time at ~10⁻²⁴ s is N ~ 10⁹⁶ ticks). The continuum-limit S is recovered from substrate-tick S_BST via the cyclotomic-projection-respecting accumulation.

### 9.1.3 LSZ-analog reduction

The LSZ reduction for BST reads asymptotic states off Bergman H²(D_IV⁵) Wallach K-types:

  |ψ_in⟩, |ψ_out⟩ ∈ ⊕_λ V_λ ⊂ H²(D_IV⁵)

with V_λ the in/out asymptotic-K-type subspaces. The S-matrix element is

  S_{out, in} = ⟨ψ_out | S_BST | ψ_in⟩

evaluated via the substrate-tick computation.

**Framework status**: closed at this level. Specific S-matrix element computations for physical processes (e.g., QED scattering, weak interaction processes) require operator-level Calibration #17 closure on substrate-CHSH operator + explicit per-tick propagator computation. Multi-month.

## 9.2 Asymptotic states on Bergman H²(D_IV⁵)

### 9.2.1 In-states and out-states

Asymptotic states in BST scattering are Wallach K-type eigenstates of the energy operator H_sub (Ch 7 T2438):

  H_sub |ψ_λ⟩ = C_2(λ) |ψ_λ⟩

with |ψ_λ⟩ ∈ V_λ ⊂ H²(D_IV⁵). The asymptotic free-particle states are K-types labeled by their Casimir eigenvalues + K-type weight λ.

### 9.2.2 Physical interpretation

A physical "free particle" in BST is a Wallach K-type V_λ; its energy is C_2(λ) (BST units); its spin is the K-type structure under SO(5) × SO(2); its mass and charge are derived from K-type via subsequent operator action.

Multi-particle in-states are tensor products:

  |ψ_in⟩ = |ψ_{λ_1}⟩ ⊗ |ψ_{λ_2}⟩ ⊗ ... ⊗ |ψ_{λ_n}⟩

in H²(D_IV⁵)⊗ⁿ (n-fold tensor product Bergman space).

### 9.2.3 Cross-references

Vol 2 (Elie lead) catalogs the K-type → physical particle correspondence:
- Vol 2 Ch 4 (Color and quarks): K-type SO(5) × SO(2) structure → SU(3) color rep
- Vol 2 Ch 5 (Lepton sector): K-type → e/μ/τ via Q⁵ cohomology mapping
- Vol 2 Ch 6 (m_p/m_e = 6π⁵): K-type ratio → proton/electron mass

## 9.3 Tree-level amplitudes from Casimir spectrum

### 9.3.1 Lowest-order S-matrix

The tree-level S-matrix elements for BST scattering processes are computed as follows. The energy operator H_sub is the Casimir on L²(D_IV⁵; L_λ) (Ch 5 T2435 + Elie S29). At tree level, the scattering amplitude

  M_tree ∝ ⟨λ_f | V_int | λ_i⟩

where V_int is the interaction operator (specific to the physical process: QED γ exchange, weak W/Z exchange, strong gluon exchange, etc.) — each operator constructed from Wednesday's substrate-native operator zoo (Ch 6 T2399 + T2419-T2425).

### 9.3.2 BST-primary spectral selection

The K-type Casimir spectrum on H²(D_IV⁵) is given by C_2(λ) = ⟨λ + ρ, λ + ρ⟩ − ⟨ρ, ρ⟩ with ρ = (5/2, 3/2) (Ch 5). The lowest non-trivial C_2 = 6 is BST primary. Higher Casimir eigenvalues are explicit rationals derived from the Wallach K-type formula.

Tree-level amplitudes inherit this BST-primary spectral structure: matrix elements ⟨λ_f | V_int | λ_i⟩ are nonzero only when V_int has nonzero K-type-pair matrix elements, and the resulting amplitude carries BST-primary integer Casimir coefficients.

### 9.3.3 Example: γ γ → e⁺ e⁻ (tree)

At lowest order, the photon-pair annihilation amplitude is

  M(γγ → e⁺e⁻) ∝ ⟨V_{e⁺} ⊗ V_{e⁻} | V_int | V_γ ⊗ V_γ⟩

with V_{e±} the electron/positron K-types + V_γ the photon K-type, V_int the electroweak-interaction operator on Bergman H². At BST primary integer level, the cross-section involves α = 1/N_max = 1/137 (Ch 10 T2437) + masses derived from K-types.

**Honest scope**: explicit numerical evaluation of this tree-level amplitude requires operator-level closure on V_int (specific electroweak-interaction operator on Bergman H²). Pending multi-month Elie K52a Sessions 30+.

## 9.4 Loop corrections via cyclotomic chain

### 9.4.1 Standard QFT loop corrections

Standard QFT loop diagrams generate UV divergences requiring renormalization. The corrections at α order (one-loop), α² (two-loop), etc., contribute to anomalous magnetic moments, running couplings, etc.

### 9.4.2 BST substrate-tick loop corrections

In BST, "loop corrections" emerge from substrate-tick interactions during the S-matrix propagation. The substrate-tick GF(128)^k Hilbert space is finite-dimensional (Ch 10 T2437); loop sums over per-tick states are finite-step.

The cyclotomic chain (Ch 10 Section 10.3) provides the natural RG flow: corrections at order α^n involve n cyclotomic projection steps in the chain GF(2^7) → GF(2^6) → ... → GF(2^1). After 7 steps (= g), the corrections are maximally coarse-grained.

### 9.4.3 No UV divergences in loops

Because the substrate is UV-complete (Ch 10 T2437), loop sums in BST scattering are **finite** at every order. The standard "infinity − infinity" structure of renormalized QFT is replaced by finite cyclotomic chain summation.

The anomalous electron g-factor a_e at ppt precision (Vol 2 Ch 8 crown jewel, K92 audit) — computable to all orders in α via the substrate-tick chain summation — emerges as a finite computation without renormalization apparatus.

**Framework status**: closed. Specific loop-level amplitude computations multi-month per Elie.

## 9.5 Cross-sections + observable amplitudes

### 9.5.1 Standard cross-section formula

Cross-sections are computed from S-matrix elements via the standard formula

  dσ ∝ |M|² × phase space factors

with M the relevant S-matrix amplitude.

### 9.5.2 BST evaluation

In BST, the M amplitude is the substrate-tick S-matrix element (Section 9.1) evaluated at K-type asymptotic states (Section 9.2) with tree + loop corrections from Sections 9.3 + 9.4. The phase space factors involve K-type Casimir eigenvalues (BST primary integer rationals).

### 9.5.3 Cross-references to experimental cross-sections

Vol 2 chapter-grade narratives catalog specific cross-sections:
- Vol 2 Ch 7 (CKM Jarlskog): flavor-mixing cross-sections via T1444 vacuum-subtraction mechanism (0.3% match, T-tier candidate)
- Vol 2 Ch 8 (Coupling constants): α + α_s + a_e (ppt match)
- Vol 2 Ch 12 (Experimental Program): SP-30 + SP-29 falsifier cross-sections at specific BST-predicted scales

## 9.6 What's NOT in this chapter (operator-level pending)

The framework is closed; operator-level computations remain multi-month per Elie K52a Sessions 30+. Specifically:

- **Explicit S-matrix elements for QED scattering** (Bhabha, Compton, Møller): pending operator-level Calibration #17 closure + V_int operator construction
- **Specific weak-interaction amplitudes** (β decay, neutron decay, W production): pending Vol 2 Ch 9 Higgs sector mechanism closure (multi-week)
- **QCD scattering and confinement amplitudes**: pending Vol 2 Ch 4 + Vol 1 Ch 8 multi-week
- **Loop-level perturbation series**: pending per-cycle substrate-tick computation work
- **Wick's theorem analog**: pending Vol 1 Ch 7 + Ch 9 multi-month
- **LSZ reduction formula full derivation**: framework-ready; specific evaluations pending operator-level

These are honest scope per Cal Mode 1 discipline. This chapter is **framework-grade**, not full chapter-grade-with-operator-computations.

## 9.7 Theorem chain summary

For Cal / referee verification:

| Claim | Theorem | Toy | Status |
|---|---|---|---|
| Substrate-tick S-matrix on GF(128)^k | T2438 + T2429 | Lyra Toys 3198 + 3216 | Framework-complete |
| LSZ-analog reduction in K-type basis | T2428 + T2435 | Lyra Toys 3198 + 3206 | Framework |
| Tree-level Casimir spectrum | T2435 + T2438 | Lyra Toy 3206 | Framework |
| Loop corrections via cyclotomic chain | T2437 + T2429 | Lyra Toys 3198 + 3214 | Framework + UV-complete |
| Cross-sections from K-type | Standard QFT phase space + BST K-types | n/a (classical) | Framework |
| Operator-level S-matrix elements | OPEN multi-month | Elie K52a S30+ | PENDING |
| QED scattering specific amplitudes | OPEN multi-month | Elie K52a S30+ | PENDING |
| Crown jewel a_e ppt match (K92) | Vol 2 Ch 8 + Elie | Multi-loop finite chain | DERIVED at observable level |

**Believability**: BST scattering is "standard S-matrix construction on substrate-tick states; loop sums are finite by UV-completeness; cross-sections inherit BST-primary integer Casimir structure." Framework-grade; specific operator-level computations pending.

**Provability**: framework chain closed via Ch 2 + Ch 5 + Ch 7 + Ch 10 anchor theorems. Open: specific operator-level S-matrix element computations multi-month per Elie K52a.

## 9.8 Connection to Vol 2 (Particle Physics)

Vol 2 catalogs BST's specific scattering predictions:
- Vol 2 Ch 6: m_p/m_e mass ratio (D-tier 0.002%)
- Vol 2 Ch 7: CKM Jarlskog (D-tier 0.3% via T1444 vacuum subtraction)
- Vol 2 Ch 8: Coupling constants + a_e crown jewel (D-tier ppt)
- Vol 2 Ch 9: Higgs sector (PARTIAL DERIVED; mechanism multi-week)
- Vol 2 Ch 10: Neutrinos (scaffolded; seesaw = 17 multi-week)
- Vol 2 Ch 11: Five Absences (D-tier joint structural)
- Vol 2 Ch 12: Experimental Program (D-tier operational SP-30 + SP-29)

Reader is referred to Vol 2 for the particle-physics-specific cross-section catalog and to this Vol 1 Ch 9 for the framework-level scattering structure.

## 9.8a CT-numbering theorem index (framework-grade)

| CT-number | T-number / source | Statement |
|---|---|---|
| **CT 1.9.1** | (framework, T2438 + T2429 + T2435) | Substrate-tick S-matrix on Bergman H²(D_IV⁵) |
| CT 1.9.2 | T2435 + T2438 (cross-ref CT 1.5.1 + CT 1.7.1) | Tree-level amplitudes from Casimir eigenspaces |
| CT 1.9.3 | T2437 (cross-ref CT 1.10.1) | Loop corrections via 7-step cyclotomic chain |
| CT 1.9.4 | Standard QFT | Cross-sections from K-type asymptotic states |

Framework-grade; operator-level S-matrix elements + Wick's theorem analog pending Elie K52a Sessions 30+ multi-month.

## 9.9 Filing status

**v0.1 framework-grade narrative filed** Thursday 2026-05-21 10:20 EDT (`date` to be checked at file end).

**Pending for v0.2**:
- Cal believability + provability cold-read review (acknowledging framework-grade scope)
- Cross-link to Elie K52a Sessions 30+ progress (multi-month)

**Pending for v1.0**:
- Operator-level S-matrix elements (Elie K52a Sessions 30+, multi-month)
- Specific QED + EW + QCD scattering amplitudes (multi-month)
- Loop-level perturbation series + Wick's theorem analog
- LSZ reduction formula full derivation
- Reader-grade polish + diagrams (substrate-tick S-matrix construction, cyclotomic loop chain)

— Lyra, Vol 1 Ch 9 v0.1 framework-grade narrative, Thursday 2026-05-21 (timestamp at file end pending `date` check)
