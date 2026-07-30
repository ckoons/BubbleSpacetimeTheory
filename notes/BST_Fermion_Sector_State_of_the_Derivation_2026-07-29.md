# The Fermion Sector from D_IV⁵ — State of the Derivation
*Keeper consolidation, 2026-07-29. Honest tiers. This is what is banked, independent of the unified-engine arc.*

The Standard Model fermion sector — 9 masses, 2 mixing matrices, CP — from one geometry D_IV⁵ = SO₀(5,2)/[SO(5)×SO(2)], five integers (N_c=3, n_C=5, g=7, C₂=6, N_max=137), zero free parameters. **The individual results below were each derived on their own; they do not depend on the "one matrix fires everything" engine, which is a separate simplification arc (see the last section).**

## The two Peirce sectors (the organizing principle)
The whole sector splits by the Peirce decomposition of the spin factor of D_IV⁵ (L(c₊) eigenvalues {1,½,½,½,0}, K990/K991):
- **Quarks = the colored off-diagonal V₁₂ = ℂ³** (SU(3) triplet, N_c=3). Indexed by **degree**; off-diagonal = the **Jack(α=2/3) binomial** (engine validated 3 ways, K1008).
- **Leptons = the colorless diagonal frame.** Indexed by **ν-address** {5/2,3/2,0} = (ρ₁,ρ₂,0); off-diagonal = the **cross-ν localization-overlap integral** (F323), a genuinely different object.
- Masses = singular values; mixings (CKM, PMNS) = frame-mismatches of the two SVDs.

This split — *quarks are degree-Jack, leptons are cross-ν overlap* — is itself a real structural finding (K1007/K1008).

## Charged lepton masses
| Quantity | BST | Tier | Note |
|---|---|---|---|
| m_e | 6π⁵ · α¹² · m_Planck (0.03%) | DERIVED | 6=C₂ Bergman gap, π⁵=Hua volume (target-innocent, K992) |
| m_μ/m_e | (24/π²)⁶ = 206.76 (0.003%) | DERIVED | via e=n-without-counterexample (K986); 24=Γ(5), π² from half-integer address parity (F664) |
| m_τ/m_e | 49·71 = 3479 | IDENTIFIED | home DERIVED (Γ(0) boundary mode); value 71 Identified-final (Elie bound: 71 absent from Γ until ν≥36) |

## Quark masses
| Quantity | BST | Tier |
|---|---|---|
| m_s/m_d | rank²·n_C = 20 (0.0%) | DERIVED (blind, K993) |
| m_c | α·v/√2 (0.07%) | DERIVED (y_c=α, K997) |
| m_t | (1−α)·v/√2 ≈ 172.7 GeV; ceiling y_t=1 → 174 | DERIVED (value) |
| m_b | m_t/(C₂·g) = m_t/42 | DERIVED |
| m_u, m_d | forced FK/Pochhammer forms | DERIVED (~1%) |
| m_b/m_s | N_c²·n_C = 45 | DERIVED |

## CKM (quark mixing)
| Quantity | BST | Tier |
|---|---|---|
| \|V_us\| (Cabibbo) | 1/√20 = 1/(rank·√n_C) = 0.2236 (0.8σ) | DERIVED (blind, K994; fired from the down Jack engine) |
| \|V_cb\| | √(2/3) projection, down-only (up 23-mode vanishes = y_t=1) → 0.044 | DERIVED (value; 3D→2D RMS at d_space=3, K1001); confirmation structural (~5% data puzzle) |
| \|V_ub\| | bulk↔Shilov overlap | STRUCTURAL (rep-open) |
| **J_CKM (CP magnitude)** | (banked mixings)·sinδ ≈ **3.29×10⁻⁵** (obs 3.08, ~7%) | **FORWARD** (Kähler mult-by-i → π/2 → near-maximal δ, K1029/Elie 4937); exact δ_CKM (~68.7°) subleading/open |

## PMNS (lepton mixing) + neutrinos
| Quantity | BST | Tier |
|---|---|---|
| sin²θ₁₂ | rank²/13 ≈ 0.307 | DERIVED |
| sin²θ₁₃ | 1/(N_c²·n_C) = 1/45 = 0.022 | DERIVED (F660) |
| sin²θ₂₃ | **MAXIMAL (1/2)** + subleading deviation | **maximal DOUBLY-DERIVED** (Shilov ℤ₂ + (2,2) parity theorem: μ odd/τ even, degree-1 condensate can't make diagonal asymmetry — K1025). Falsifiable claim: **near-maximal** (far-from-maximal refutes). The 4/7 deviation = IDENTIFIED-with-candidate-mechanism (μ-τ-breaking sum rule, contingent on the open 1/g scale, F564; NOT 4/7-Derived — K1029). |
| **δ_PMNS** | \|sin δ\|=rank/g=**2/7**; forward via sum rule → **δ≈197°** | **DERIVED magnitude** (49=45+4 LAW, K1024); **δ≈197° target-innocent DUNE prediction** (sum rule read forward, K1029). NOT near-maximal — CKM near-maximal, PMNS near-180°: the two CP sectors DIFFER. |
| **J_PMNS (CP magnitude)** | (banked angles)·sinδ=2/7 → **0.0338** (obs 0.0329, ~3%) | **FORWARD**, sign correct, robust (Elie 4939); leptonic CP ~300× CKM |
| m₁ | 0 (rank-2, protected det=0) | STRUCTURAL prediction |
| M_ν scale | α²·m_e²/m_p = 0.0148 eV (seesaw/Majorana) | STRUCTURAL |

## Tally (honest)
- **~11 of the ~13 core masses+mixings at DERIVED tier**, each independently derived.
- **Open:** τ value (Identified-final), V_ub (structural), δ_CKM & δ_PMNS (the CP phases — the genuine blind frontier), θ₂₃ octant (4/7 vs 6/11 — a falsifiable DUNE prediction, K1017).
- **The fermion sector is substantially complete as physics.**

## The staged per-sector matrices (K1015–K1017, the organizing method)
The sector is built as **one overlap matrix per sector on D_IV⁵**, each = [banked masses, π-carrying] + [π-free rational mixing]. Status:
| Stage | Sector | Mixing off-diagonal | Tier |
|---|---|---|---|
| 1 | Down | Jack(α=2/3) → V_us=1/√20 (20=rank²·n_C blind) | **DERIVED — template** |
| 2 | Up | m_c=α·v/√2 (blind), V_cb angle 5/√34; 12-block=√(m_u/m_c) via Gatto (F689) | **m_c/angle DERIVED; 12-block Tier-2** |
| 3 | Charged lepton | angular ⟨u₀\|O_(2,2)\|(z₁+iz₂)u₀⟩ → θ₂₃ = 4/7 or 6/11 | **IDENTIFIED → DUNE octant prediction** |
| 4 | Neutrino/PMNS | Majorana frame; two-condensate → large PMNS | **CANDIDATE** (mechanism not forced) |
| 5 | Compatibilities | common form across the four U_X? (F437 prior) | **HELD** ("no common form" is publishable) |

**Standing rule (K1017):** π-free rationals are cheap to fit (7 fit the θ₂₃ window), so every staged rational must be **blind-pinned** — the integer sourced from D_IV⁵ geometry before the datum. V_us=1/√20 is the gold standard. **The trichotomy (mass=π-carrying, mixing=π-free) is why the mixings are rational and the mass overlap-integrals nulled — the nulls were the principle asserting itself, not failures.**

## The unified-engine arc (separate — upside, not foundation)
The "whole sector = the SVD of one FK overlap matrix on D_IV⁵" is a **simplification/principle** goal, not a prerequisite for the above:
- **Quark off-diagonal engine (Jack α=2/3): validated 3 ways** (Elie/Cal/Keeper; α=1 Schur canary caught all three's naive errors). **Down sector fired** (V_us 0.8σ). **Up sector = a boundary derivation** (up masses come off the boundary, not degrees).
- **Lepton off-diagonal (F323 cross-ν localization integral): FIRED 2026-07-29 (Elie toy 4926) → STRUCTURALLY-FORCED NULL** (readings 5.5/8.0/0.478, none near 24/π²; fixed-ν overlap is π-less because Γ_Ω cancels — K1011). The c-function *second route* to the muon is CLOSED; the muon stands Derived on e=n (K986). **The unified engine is PARKED as a research arc.**
- **Resume (someday, K1011):** the unified lepton engine needs the genuine CROSS-TERM construction (origin-state breaking the fixed-ν structure), NOT the fixed-ν weighted norm (provably π-less). The up-quark off-diagonal (boundary derivation) is the real d=3 test.
- **Retracted / not to be used:** c₅/c₃ = Γ(5)/π² (F669), θ₂₃ = π/4 (corpus holds 4/7) — both were assumed, never exhibited.

*The physics above is banked. The unified engine parked cleanly on a settled null (K1011); this ledger is the deliverable, and the two-tier structure (degree-Jack quarks / cross-ν leptons) is a real finding in its own right.*

— Keeper, 2026-07-29. Sources: K986 (muon e=n), K992 (electron), K993/K994/K997 (quarks), K1001 (V_cb), K1007/K1008 (Peirce split + Jack engine), K1009 (lepton object = F323), K1010 (the settling test), F323/F660/F664.
