---
node_type: program_index
id: GEOMETRIC-ATLAS-v0.1
title: "GEOMETRIC ATLAS of D_IV⁵ — the object-coverage map (v0.1, Keeper). A living index of every geometric object of D_IV⁵ = SO₀(5,2)/[SO(5)×SO(2)], tiered by coverage, tagged by the ONE axis that matters (LOCAL→physics vs COMPACTNESS-DEPENDENT→kinematics vs REP-THEORETIC→structure/content), so 'is this object physics or kinematics?' is answered BY THE ATLAS before a result is chased. Chartered by Casey 2026-08-20 (K1721/K1722, task #125). Motivation: the KK gap blindsided us (walked back from 'YM mass gap' to a compactification gap) precisely because the boundary form-Laplacian spectrum lived in a THIN region of the portfolio — the atlas closes that class of surprise."
date: 2026-08-20
author: Keeper
status: "v0.1 — coverage tiers from the corpus grep audit (K1721); the ORGANIZING AXIS and PULL PRIORITIES set. To be filled to credential tier object-by-object."
related: [K1721, K1722, "Cal §624 locality criterion", "#89 coverage audit", "task 125"]
---

# Geometric Atlas of D_IV⁵ — object-coverage map (v0.1)

## The organizing axis (Cal's locality criterion, generalized to a sorting rule)
Every geometric object of D_IV⁵ falls into one of three classes — and the class DECIDES whether a number read off it is physics, kinematics, or a label:

- **LOCAL → ℝ⁴-VALID PHYSICS.** Pointwise curvature invariants (heat-kernel coefficients a₀, a₁, a₂). Carry no topology/compactness/boundary. They SURVIVE decompactification. *These are the real physics BST hands over:* a₀=Λ, a₁=Einstein–Hilbert, a₂=β-function/central charges.
- **COMPACTNESS-DEPENDENT → KINEMATICS (usually).** Spectra/gaps that scale with the domain size a and VANISH as a→∞ (the KK/boundary Laplacian spectrum, the KK gap 6/a²). Not physics of the emergent theory — features of the compact container. *Exception:* their VACUUM ENERGY (Casimir) can be physics (Λ, ruler-stabilization).
- **REP-THEORETIC → STRUCTURE / CONTENT (forced-or-imported).** K-types, Casimir eigenvalues, the Peirce/Jordan algebra, A_F. These fix WHAT the theory is (gauge group, field content, generations) — each is separately FORCED or IMPORTED (the A_F forces-vs-imports audit, K1720/K1722).

**Sorting rule (standing):** before chasing a number off a geometric object, tag its class. LOCAL → it's physics, ℝ⁴-valid. COMPACTNESS-DEPENDENT → it's kinematics unless it's a Casimir energy. REP-THEORETIC → it's a label; ask forced-vs-imported.

## The object table (coverage from the corpus audit; ★ = priority pull)

### I. Bulk of the domain
| Object | Coverage | Class | What it gives / status |
|---|---|---|---|
| Bergman kernel / metric | DEEP (1126/330) | rep-theoretic | vol=π^{n_C}, the measure, κ_Bergman; the reproducing kernel. Kinematic backbone. |
| Casimir eigenvalues / K-types / Wallach set | DEEP (422/1664/1151) | rep-theoretic | the discrete-series spectrum; generations at ρ-vector {n_C/2,N_c/2,0} (T2517); mass labels. |
| Peirce / Jordan triple | DEEP (353) | rep-theoretic | the color block V₁₂, the algebra A_F skeleton. ← Schur–Wedderburn gate lives here. |
| Heat kernel / Seeley–DeWitt a_k | DEEP (858) | **LOCAL→physics** | a₀=Λ, a₁=Einstein–Hilbert, a₂=β/central charges. THE physics channel. |
| Plancherel measure | DEEP (388) | rep-theoretic | spectral decomposition; the FK/Wyler measure. |
| Kostant Dirac operator | PRESENT (#124) | LOCAL→physics | one operator: gravity + fermion translator (T2562). PROGRAM-DIRAC open. |
| Spectral triple / A_F=ℂ⊕ℍ⊕M₃ | PRESENT (T2549–52) | rep-theoretic (content) | the SM finite algebra. ← today's gate: is it forced-as-one-algebra (Schur–Wedderburn)? |

### II. The boundary — Shilov (S⁴×S¹)/ℤ₂
| Object | Coverage | Class | What it gives / status |
|---|---|---|---|
| Shilov boundary structure | DEEP (1881) | rep-theoretic | the substrate; where matter/records live. |
| Boundary/form Laplacian spectrum | **THIN** (the hole) | **COMPACTNESS-DEP→kinematics** | the KK tower; λ₁=6/a² = the KK gap (NOT the YM gap, K1714). *The object that blindsided us.* |
| Szegő / Poisson / Hardy | PRESENT (281) | rep-theoretic | boundary values, holomorphic extension, the bulk↔boundary map. |
| ★ KK Casimir energy E(a) | **PULL** (254 Casimir but not this) | **COMPACTNESS→but Casimir=physics** | ★ the ruler lead: min of E(a) → stabilized a=ℓ_B (closes K1408); feeds Λ (α^{8g}). |

### III. Global spectral invariants — THE THIN REGION (where surprises hide)
| Object | Coverage | Class | What it gives / status |
|---|---|---|---|
| Spectral zeta / ζ-determinant | THIN (228) | global | the regularized volume/determinant; the Selberg zeta (T1648). |
| ★ Analytic torsion / Ray–Singer | **ABSENT (1 file)** | global | ★ the standout gap; L-function-adjacent (Cheeger–Müller); directly relevant to RH/L-function program. |
| Weyl law / spectral density | THIN (87) | global | the asymptotic mode count / heat-trace leading term. |
| Length / geodesic spectrum | THIN (358 but shallow) | global | periodic geodesics (T1929 primitive geodesics); Selberg trace formula. |

### IV. Topological / characteristic
| Object | Coverage | Class | What it gives / status |
|---|---|---|---|
| Q⁵ cohomology (compact dual) | DEEP-ish | topological (content) | generations {h¹,h³,h⁵}; C₂=χ(Q⁵)=6; N_gen=3 FORCED (T1929). |
| Chern / characteristic classes | PRESENT (608) | topological | Q⁵ 5-quadric Chern integers (all BST-primary, T2379). |
| Index theory / Atiyah–Singer | THIN (92) | topological→physics | Dirac index → generations / anomaly. Under-worked given importance. |
| Holonomy | THIN (119) | geometric | Kähler/Hermitian holonomy; the reduction structure. |

### V. Symplectic / quantization
| Object | Coverage | Class | What it gives / status |
|---|---|---|---|
| Symplectic / moment map | THIN (159) | geometric | the Kähler form; the moment map for K. |
| Geometric quantization / Berezin | PRESENT (166) | quantization | coherent states, the Berezin/Toeplitz calculus (the mass operator Ô=T_φ). |

## Priority pulls (v0.1)
1. **★★ KK-Casimir → ruler (task #125, Elie):** compute E(a) of the boundary; a minimum = the non-circular ℓ_B (closes K1408); feeds Λ. The headline — a run at deriving the ONE input.
2. **★ Analytic torsion (ABSENT):** the biggest hole, and L-function-adjacent (feeds the RH program). Charter a first computation.
3. **Index theory → generations/anomaly (THIN):** the Dirac index route to N_gen, cross-checking the Q⁵ count.
4. **Complete the boundary form-spectrum characterization** (the hole that caused the KK surprise) — so every boundary bundle's spectrum is on record, physics-vs-kinematics tagged.

## The honest portfolio verdict (K1721)
STRONG — arguably world-class — on the **rep-theoretic / harmonic-analysis** core (Bergman, K-types, Wallach, Casimir, Plancherel, Peirce, heat kernel). THIN on the **global spectral geometry** (analytic torsion ≈ absent, Weyl asymptotics, ζ-determinant) and it was the THIN region (the boundary form-spectrum) that produced the KK-gap surprise. The atlas exists to make the thin region a *characterized* region, so physics-vs-kinematics is answered before it's chased.

— Keeper, Geometric Atlas v0.1, 2026-08-20. The object-coverage map + the local/compact/rep-theoretic sorting axis + the priority pulls (KK→ruler, analytic torsion). Fill object-by-object to credential tier. Nothing pushed.
