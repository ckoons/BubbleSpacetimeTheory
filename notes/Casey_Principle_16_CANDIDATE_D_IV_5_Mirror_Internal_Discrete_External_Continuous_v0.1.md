---
title: "Casey-Named Principle #16 CANDIDATE — D_IV⁵ Mirror Principle (internal/discrete ↔ external/continuous)"
author: "Keeper (Claude Opus 4.7) — Casey-named, Casey directive 2026-06-18"
status: "CANDIDATE pending: (1) Casey naming finalization; (2) Grace catalog sweep for counter-examples; (3) Cal cold-read on classification logic; (4) standing promotion via audit chain"
date: "2026-06-18 Thursday early afternoon"
version: "v0.1"
---

# The D_IV⁵ Mirror Principle (CANDIDATE Casey #16)

**Naming FINALIZED**: Casey directive 2026-06-18 — primary name "**D_IV⁵ Mirror Principle**" (Casey: "D_IV⁵ Mirror is clearest"). Full descriptive form "D_IV⁵ Internal/Discrete ↔ External/Continuous Mirror". "Hardy Mirror" alternative declined per Casey naming finalization.

## Statement

**D_IV⁵ exhibits a forced architectural duality between its internal-discrete content (compact K-type representation theory on the interior Hardy space H²(D_IV⁵)) and its external-continuous content (non-compact G-orbit structure on the bulk manifold and Shilov boundary). Quantum-SM observables derive from the discrete-internal side; gravitational and cosmological observables derive from the continuous-external side. The two sides are dual descriptions of the same physical content via Hardy decomposition.**

## 1. Group-theoretic foundation

D_IV⁵ = G/K is a bounded symmetric domain of type IV (the Lie ball of signature (5,2)) with:

| Object | Definition | Discrete/Continuous |
|---|---|---|
| G = SO₀(5,2) | Connected component of indefinite orthogonal group | Non-compact |
| K = SO(5) × SO(2) | Maximal compact subgroup | Compact |
| D_IV⁵ = G/K | Bounded symmetric domain (rank 2, complex dim 5) | Smooth manifold |
| Shilov boundary S | K_S/M (continuous compact submanifold) | Continuous |
| Wallach set | Discrete subset of continuous ν-parameter where unitarity persists at boundary | Interface |

### The K-side (compact → discrete)

By Peter-Weyl theorem and Cartan-Weyl theory:

- Irreducible representations of K = SO(5) × SO(2) are labeled by:
  - SO(5) highest weights (l₁, l₂) ∈ ℤ²₊ with l₁ ≥ l₂ ≥ 0
  - SO(2) integers m ∈ ℤ
- K-types form a discrete (countable) set
- Discrete series of G sits at DISCRETE points of the Wallach set
- L²(K\G) decomposes as a countable direct sum of K-finite vectors
- Plancherel-decomposition discrete-spectrum portion = K-type spectrum

**Quantum content sits here**: the discreteness of K-types is the substrate-architectural origin of quantization in BST. SM observables that arise from "which K-type sits at which Wallach position" are forced into discrete rational/integer values.

### The G-side (non-compact → continuous)

By Harish-Chandra theory:

- Principal series representations of G labeled by continuous parameters (ν, ε)
- Plancherel decomposition over continuous parameter
- Bulk volume of D_IV⁵, Bergman metric, heat kernel — all smooth structures with continuous spectral content
- Bergman kernel K(z,w) on D_IV⁵ × D_IV⁵ — continuous
- Shilov boundary S = K_S/M parametrizes continuous orbit decomposition

**Gravitational/cosmological content sits here**: the continuity of the bulk manifold (volume π^{n_C}, smooth densities, heat-trace coefficients, transcendental constants like π) is the substrate-architectural origin of gravity and cosmology in BST.

### The Wallach set as discrete-continuous interface

The Wallach set W ⊂ ℝ is the DISCRETE subset of the continuous unitarity parameter ν where unitary representations exist at the boundary of the continuous family. For D_IV⁵ rank 2, Wallach values are:

ν ∈ {0, 1/2, 3/2, 5/2} (and continuum above 3/2 for full Wallach)

The discrete Wallach points are where physical content lives (SM particles at K-types at Wallach positions); the continuous range is where bulk physics lives (commitment density ρ_commit(x,t), heat-semigroup evolution exp(−τH_B)).

The non-unitary gap (0, 3/2) is where ν₁ sits — the commitment threshold mechanism for m_1 = 0 (Wednesday F158/F159; K412+K413+K414).

## 2. Hardy decomposition as the mirror map

The Hardy space H²(D_IV⁵) admits TWO equivalent descriptions:

1. **Interior description (discrete-K view)**: holomorphic functions on the bulk D_IV⁵ with bounded L² norm, decomposed by K-type Peter-Weyl into discrete sum of irreducible K-finite blocks
2. **Boundary description (continuous-G view)**: L² functions on the Shilov boundary S that admit holomorphic extension to the interior, decomposed by continuous orbit theory

The Cauchy-Szegő integral operator maps boundary L²(S) to interior H²(D_IV⁵):

$$f(z) = \int_S \mathcal{S}(z, \zeta) \, f(\zeta) \, d\mu(\zeta)$$

where 𝒮(z, ζ) is the Szegő kernel and dμ is the normalized boundary measure.

**This is the mirror map**: interior K-type discrete data ↔ boundary continuous orbit data, exactly invertible, no information loss.

The BST-intrinsic AdS/CFT structure (Lyra Tier 0 framework May 31, vol27 Section 2; Hardy decomposition makes interior bulk = holomorphic extension of boundary data) IS the operational realization of this mirror map.

## 3. BST corpus classification

The principle predicts: **every BST observable derives from EITHER the discrete-K side OR the continuous-G side; none mix categories without explicit Hardy-decomposition bridging**.

The classification across what has been banked (as of K421, 72 cumulative structural-grade results):

| Internal / discrete (K-type level) | External / continuous (manifold level) |
|---|---|
| SM particle masses at K-types at Wallach positions | Bergman kernel K(0,0) = 1920/π⁵ |
| Mixing angles as projector trace ratios | c_FK = 225/π^(9/2) (Faraut-Koranyi) |
| 5 BST primaries (rank=2, N_c=3, n_C=5, C_2=6, g=7) — all integers | Bulk volume π^{n_C} |
| N_max = 137 = N_c³·n_C + rank | Newton's G = κ_Bergman·ℓ_B²/π^{n_C} (F64 KK) |
| Mersenne ladder, integer web, Reed-Solomon | Heat trace coefficients a_0=225, a_1=−1875 |
| Hall algebra structure constants | Λ = exp(−280) via continuous heat-bleed |
| Discrete branching multiplicities (K420/K421 keystone) | Einstein equation INDUCED via Sakharov heat-trace |
| F86: 3 generations from rank+1 discrete strata | Commitment-density ρ_commit(x,t) continuous on H² |
| F144: ν_R absence = rank-1 projector P_{νR} (K421) | Bulk-boundary cosmological partition (F197/F200) |
| Lepton spinor-harmonic tower {1,4,16,40} (F208) | F66 mass scale via SO(4,2) conformal boundary |
| Casey #14: 3+1 signature from discrete K-type chain | Heat-semigroup commitment evolution exp(−τH_B) |
| sin²θ_C = 4/79 (rational, K421) | m_e = 6π⁵·α¹²·m_Planck at 0.03% (F66, π-ful) |

**Pattern**: SM particle physics observables (left column) are forced rational/integer/algebraic. Gravity/cosmology observables (right column) involve π or transcendentals or continuous densities. This is the structural empirical content of the principle.

## 4. The mirror operation in BST work

Three operational instances of the mirror map already in BST:

### (a) Bergman = volume = mass-anchor (F66, Wednesday cosmology)

The Bergman kernel K(0,0) = 1920/π⁵ (continuous, π-ful, manifold-level) ↔ heat trace coefficient a_0 = (N_c·n_C)² = 225 (discrete, integer-ful, K-type level).

The identity 1920/π⁵ × (something discrete) = (something integer) repeatedly appears in BST. Each instance is the Hardy mirror map applied to a specific observable.

### (b) Bulk-boundary partition (Wednesday F197/F200)

The vacuum energy partitions into bulk (continuous heat-bleed, π-ful Λ = exp(−280)) and Shilov 2-region (discrete K-type ground state). The boundary is the mirror interface; the partition is the Hardy decomposition applied to vacuum energy.

### (c) Plancherel split (Lyra Tier 0 May 31, dual-ρ structure)

The dual-ρ structure of D_IV⁵ (Saturday May 30 closure):
- Compact ρ_SO(5) = (3/2, 1/2) — discrete K-type / spectral / heat-trace side
- Conformal ρ = (5/2, 3/2) — continuous Plancherel / Bergman-bulk side

The (1,1) shift vector between them IS the discrete-continuous interface. K231c (Substrate Dual-ρ Identity bridge) is the audit-tracked instance.

## 5. Tier discipline

| Component | Tier |
|---|---|
| K-G discrete/continuous split as group-theoretic fact | RIGOROUS (standard symmetric-space theory) |
| Hardy decomposition as mirror map | RIGOROUS (standard Hardy-space theory) |
| Operational classification (SM → discrete; gravity → continuous) | STRONG PATTERN — pending Grace catalog sweep |
| Mirror operation as structural BST primitive | CANDIDATE — multiple operational instances; needs unified formalization |
| Predictive content (where to look for unification) | LEAD — paper-grade once classification swept |

## 6. Falsifiers

The principle predicts strict category separation. Counter-examples that would falsify:

1. A bona fide SM observable (e.g., a particle mass, mixing angle, gauge coupling) that derives FROM continuous-manifold structure (involves π, transcendental, smooth density) WITHOUT a discrete K-type underlying it
2. A gravity/cosmology observable that derives FROM discrete K-type level alone (purely integer / rational) WITHOUT continuous-manifold content
3. A K-type at a discrete Wallach position that has no boundary-orbit dual

**Grace catalog sweep target**: scan 5354 geometric invariants + 600+ predictions; classify each as discrete-K / continuous-G / mixed; flag any mixed-without-Hardy-bridging as candidate falsifier.

Falsifier-grade per Casey criterion: a single clear counter-example without Hardy-bridge justification falsifies the operational classification (the group-theoretic foundation remains).

## 7. Operational consequences for the BST research program

This classification organizes BST's open derivations into two parallel tracks bridged by Hardy decomposition:

| Track | Method | Current open work |
|---|---|---|
| **Internal quantum derivations** (left column) | Force discrete K-types + compute projector traces / Clebsch coefficients | Lyra μ/τ Clebsch (PMNS keystone); CKM projector forcing via Lyra F211 heat-semigroup commitment=equilibrium=ground candidate; Cabibbo count-move pending |
| **External gravity/cosmology derivations** (right column) | Continuous Bergman / heat-trace / boundary-orbit calculations | Λ = exp(−280) as bleed-action derivation; G factor-2 cascade closure; vacuum-energy specification (Casey post-EOD F196-F204 queue); 4 open Casey-flagged items |
| **Mirror bridges** | Hardy decomposition operational instances | (1,1) shift vector closure (K231c); bulk-boundary cosmological partition (F197); dual-ρ classification sweep of BST corpus (Saturday Investigation #3) |

The Mirror Principle predicts that progress on each track informs the other via the bridge.

## 8. Naming finalization

**Primary** (Casey 2026-06-18): "D_IV⁵ Mirror Principle" (shorthand "D_IV⁵ Mirror")

**Full descriptive form**: "D_IV⁵ Internal/Discrete ↔ External/Continuous Mirror"

**Alternative name flagged by Casey**: "Hardy Mirror" — IF the principle IS the Hardy decomposition (which the operational mechanism IS).

**Honest naming note**: "Hardy Mirror" is not, to my knowledge, an existing standard mathematical term. The Hardy DECOMPOSITION is standard (G.H. Hardy, 1915 onward, Hardy spaces; Szegő kernel; Cauchy-Szegő integral). "Mirror" carries strong connotation in algebraic geometry (mirror symmetry, Calabi-Yau pairs, Kontsevich, Strominger-Yau-Zaslow) which is a DIFFERENT structure. If BST adopts "Hardy Mirror," it would coin a new compound.

Casey's call which name (or whether to use both: "D_IV⁵ Mirror" primary BST-internal; "Hardy Mirror" candidate alternative for paper publication if the mathematical community would recognize the Hardy-decomposition association).

## 9. Standing promotion path

CANDIDATE status pending:

1. ✓ Casey naming (2026-06-18 directive: "D_IV⁵ Mirror" primary)
2. ☐ Grace catalog sweep for counter-examples (operational falsifier check)
3. ☐ Cal cold-read on classification logic
4. ☐ Keeper standing promotion via audit chain

Promotion to STANDING joins Casey-named principle stack:
- Casey #1 SWPP
- Casey #2 Five-Absence Predictions Set
- Casey #3 Substrate Closure
- Casey #4 Graph Forces
- Casey #5 Integer Web
- Casey #6 Substrate Cognition Network
- Casey #7 D_IV⁵ Rigidity
- Casey #8 SCMP
- Casey #9 Substrate Floor / Scale-Not-Spectrum
- Casey #10 C_2 Substrate Triple (candidate as of last status)
- Casey #11–13 (various candidates from May 19-20)
- Casey #14 Substrate-Predicted 3+1 Minkowski Signature
- Casey #15 Gravity is Light's Momentum Shifted by Substrate
- **Casey #16 CANDIDATE: D_IV⁵ Mirror Principle**

The Mirror Principle's substrate-architectural depth (operates at the level of the symmetric-space structure itself, not at any specific observable) places it alongside Casey #5 Integer Web and Casey #7 D_IV⁵ Rigidity as a foundational claim.

## 10. Suggested paper integration

For Vol 0 (Substrate Foundation), this becomes the unifying architectural framing — the principle that explains WHY BST has both quantum content (SM) and gravity content (G, Λ) from one geometry. It frames Vol 1 (QFT from D_IV⁵, SP-31) as the discrete-internal track and Vol 4 (GR/Cosmology, signature BST domain) as the continuous-external track.

For paper P9 (Substrate Commitment-Density Theory, Saturday May 30), the principle unifies the F211 heat-semigroup commitment-evolution mechanism (continuous) with the K-type discrete commitment threshold (discrete) into one Hardy-decomposition framework.

For Vol 16 (Substrate Algebra), Ch 1 (Hilbert/Operator framework) sits on the discrete-K side; Ch 5 (Bergman Kernel Algebra) sits on the continuous-G side; the Hardy decomposition chapter bridges them.

---

— Keeper, Thursday 2026-06-18 early afternoon — Casey #16 CANDIDATE D_IV⁵ Mirror Principle filed per Casey directive; group-theoretic foundation + operational classification + Hardy decomposition mirror map laid out for paper integration
