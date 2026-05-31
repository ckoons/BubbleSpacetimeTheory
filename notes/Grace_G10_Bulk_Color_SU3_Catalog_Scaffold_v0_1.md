---
title: "G10 — Bulk-Color SU(3) Catalog Scaffold v0.1"
author: "Grace"
date: "2026-05-30 Saturday 09:35 EDT (`date`-verified Sat May 30 08:58 EDT)"
status: "v0.1 — Saturday morning. Catalog-side scaffold supporting Lyra's bulk-color SU(3) mechanism research (#418). Goal: file the structural Lie-algebra facts about p=SO(5,2)/K cleanly (DERIVED tier), map the three candidate mechanism paths (FRAMEWORK / research-staged), and Mendeleev-scan existing 3-fold structures across the catalog. When Lyra's mechanism lands, the catalog absorbs immediately."
purpose: "Direct support for Lyra's bulk-color SU(3) research push. Catalog-scaffolding for #418 (program's frontier OPEN gate)."
tier_discipline: "Per Keeper Saturday plan: bulk-color in FRAMEWORK / FRAMEWORK-PLUS until mechanism shown to produce TWO physically-independent 3-fold structures, not numerical coincidence."
---

# G10 — Bulk-Color SU(3) Catalog Scaffold

The program's frontier reduces to ONE structural item: derive how SU(3)=A₂ color appears, given that K = SO(5)×SO(2) = B₂×U(1) does not contain SU(3). This document scaffolds the catalog side of that question.

## Section A — The bulk p-space (rigorous Lie-algebra structure)

### A.1 Cartan decomposition

D_IV⁵ = SO₀(5,2) / [SO(5) × SO(2)] is a Hermitian symmetric domain of type IV, rank 2. The Lie algebra splits via Cartan involution:

| Piece | Dim | Notes |
|---|---|---|
| so(5,2) | **21** | full algebra |
| k = so(5) ⊕ so(2) | **11** = 10 + 1 | compact subalgebra (K-isotropy) |
| **p (the bulk)** | **10** = 21 − 11 | non-compact tangent at basepoint |

### A.2 p as K-module — DERIVED

Standard Hermitian symmetric space structure (Hermann 1956 / Helgason):

- **p = V_5 ⊗ (V_+1 ⊕ V_-1)** under K = SO(5) × SO(2)
- V_5 = vector rep of SO(5) = V_(1,0) in B₂ ω-basis (dim 5 = n_C)
- V_±1 = the ±1 charge reps of SO(2) (the substrate's J = complex structure)
- **p_+ = V_5 ⊗ V_+1** (holomorphic tangent, dim 5 = n_C)
- **p_- = V_5 ⊗ V_-1** (antiholomorphic tangent, dim 5 = n_C)
- p = p_+ ⊕ p_- (dim 10)

### A.3 [p, p] ⊆ k structure — DERIVED

For a HERMITIAN symmetric space (D_IV⁵ qualifies — there is a K-invariant complex structure J on p):

- **[p_+, p_+] = 0** (abelian — the defining feature of Hermitian type)
- **[p_-, p_-] = 0** (abelian conjugate)
- **[p_+, p_-] ⊆ k = so(5) ⊕ so(2)** (the only nontrivial bracket)

**Critical structural fact for #418**: p_+ is an ABELIAN Lie algebra of dim 5 = n_C. There is no internal non-abelian Lie subalgebra inside p_+. So SU(3) cannot appear as a Lie subalgebra of p alone — it must appear via:

1. **K-action on p**: SO(5)×SO(2) acts on p_+ via V_5⊗V_+1 — does SU(3) act compatibly?
2. **Bulk K-type tower**: bulk holomorphic functions decompose as ⊕_λ V_λ; does SU(3) appear in the Wallach spacing of the tower?
3. **Kernel modular structure**: Bergman kernel K(z, z̄) on D_IV⁵ has Z_n residue structure; is there Z_3?
4. **Emergence as counting**: SU(3) is NOT a substrate symmetry; the "3" is a count (h^∨ = N_c = 3) and SU(3) is the gauge group that emerges from how the count interfaces with confinement.

These are the FOUR candidate mechanism families. Lyra's three candidate directions {Wallach spacing / spinor³ anchor / Bergman Z/3 residue} fit into family (2), an algebraic re-routing of family (1), and family (3) respectively. Family (4) is the "counting-not-symmetry" reading.

## Section B — Why SU(3) is structurally hard to find in K

### B.1 The clean Lie-algebra obstruction

| Group | Rank | Dim | Type | Cartan | h^∨ | Coxeter h |
|---|---|---|---|---|---|---|
| **SU(3) = A₂** | 2 | 8 | A | [[2,−1],[−1,2]] (symmetric) | 3 | 3 |
| **SO(5) = B₂** | 2 | 10 | B | [[2,−1],[−2,2]] (non-symmetric) | 3 | 4 |

Both rank 2; both have h^∨ = 3. Different Cartans → different roots → different Weyl groups → different reps.

**SU(3) ⊄ SO(5) as a subgroup**: A₂ root system has 6 roots all of equal length; B₂ has 8 roots in two length classes (4 long + 4 short). A₂ cannot embed in B₂ as a sub-root-system.

This is the clean Lie fact Lyra discovered. The "3 colors" of SU(3) cannot come from the K-content of D_IV⁵ symmetry. It must come from the bulk side, or emerge non-Lie-theoretically.

### B.2 What the K-content DOES give

The K-content (SO(5)×SO(2)) gives, via canonical reps:

- V_(0,0) trivial — dim 1 — Higgs sector
- V_(1/2,1/2) spinor ω₂ — dim 4 = rank² — fermion (Dirac 4-spinor)
- V_(1,0) vector ω₁ — dim 5 = n_C — photon
- V_(1,1) adjoint — dim 10 = adjoint of SO(5) — gauge

Plus the SO(2) charge labeling everything. This is the static taxonomy that Lyra derived via the dictionary L1-L3. SU(3) is conspicuously absent — by design, because B₂ ≠ A₂.

## Section C — Candidate mechanism paths (FRAMEWORK / research-staged)

Per Keeper's tier-line: FRAMEWORK until shown to produce TWO physically-independent 3-fold structures. None of these are claims; they are structurally-staged candidates.

### C.1 Path α — K-type bulk tower (Wallach spacing) [Lyra direction 1]

Bulk K-type decomposition for holomorphic functions on D_IV⁵:

L²_hol(D_IV⁵) = ⊕_λ K_λ where K_λ = highest-weight λ K-types

Wallach (1976) classified the unitary highest-weight reps. The Wallach set for D_IV⁵ has structure with spacing related to rank, n_C, and ρ = (5/2, 3/2).

**Hypothesis**: the Wallach spacing produces a 3-fold periodicity in the K-type tower; SU(3) acts as a discrete symmetry of this periodicity. This would need rigorous Wallach-spacing computation (Elie B1 in Saturday plan).

### C.2 Path β — Spinor³ self-fusion anchor [Lyra direction 2]

Elie E7 (Toy 3608) showed (in B₂, rigorously):
- spinor ⊗ spinor ⊗ spinor = 3·spinor + 2·V_(3/2,1/2) + V_(3/2,3/2) (64 = 4³)
- mult(spinor in spinor³) = **3**
- Three E6 channels via spinor⊗{trivial, vector, adjoint}

**B₂-specific** (A₂ gives 0 — this is a STRENGTHENER for B₂ substrate).

**Reading 1**: 3 channels = 3 generations (matter family structure)
**Reading 2**: 3 channels = 3 colors (gauge content)
**Honest reading (per Keeper)**: TWO B₂-specific 3-fold structures (color count + spinor³ channels) that coincide numerically — not a derivation of one from the other.

The two-structures burden requires showing that ONE B₂ invariant produces two structurally-independent 3-fold structures. Path β candidate: the spinor³ channels (one 3) plus h^∨ = 3 from B₂ root system (the other 3) — both B₂-specific but structurally distinct (one is a tensor-product multiplicity, the other is a Cartan/root-system count). This needs explicit mechanism showing the two are forced together.

### C.3 Path γ — Bergman kernel Z/3 residue [Lyra direction 3]

Bergman kernel K(z, w̄) on D_IV⁵ has known formula (Hua 1958):
- K(z, w̄) ~ [(1 − z·w̄_1)(1 − z·w̄_2)]^(-n_C/rank)
- Singularity exponent at boundary = ρ₁ = n_C/rank = 5/2 (lepton K-type Casimir, the Bergman kernel singularity)

**Hypothesis**: the kernel modular structure has Z_3 periodicity coming from the third root of unity ω = e^(2πi/3); this Z_3 lifts to SU(3) via the standard 3 → ω · 3 character action.

This is the most novel direction. Needs concrete kernel computation, possibly Hua kernel + Bergman normalization c_FK = 225/π^(9/2) [INV-5256 / T2442 DERIVED].

### C.4 Path δ — Counting-not-symmetry [Grace observation]

A non-Lie-theoretic possibility per Lyra's open-frontier framing:

SU(3) is the gauge group of QCD as observed in physics. The substrate produces N_c = 3 = h^∨ as a count, and the standard model's SU(3) is the gauge group that emerges from how confinement (substrate's Shilov-boundary mass mechanism, A3 paper) interfaces with the 3-count.

**In this reading**, asking "where is SU(3) in the substrate?" is a category error like asking "where is U(1) in classical electromagnetism?" — U(1) emerges as the gauge group, not as a pre-existing substrate symmetry.

This is the most conservative path. It demotes #418 from "mechanism" to "interface" — SU(3) interfaces between the substrate's 3-count and the observed gauge sector.

## Section D — Mendeleev-scan: 3-fold structures across the catalog

Where do 3-fold structures appear in BST, and which could source the bulk-color SU(3)?

| Source | 3-fold structure | INV / Theorem | Path candidacy | Notes |
|---|---|---|---|---|
| **B₂ dual Coxeter number** | h^∨(B₂) = N_c = 3 | T1 / standing convention | α/β/δ | the fundamental count — already over-determined |
| **SU(3) gauge group itself** | A₂ rank 2, root count 6, h^∨ 3 | T-series, Vol 2 Ch 4 | (gauge-side) | the target of the mechanism |
| **3 generations of SM fermions** | e/μ/τ + ν_e/ν_μ/ν_τ + 3 quark gens | T-series matter content | β/spinor³ candidate | the OTHER 3 — burden requires distinct mechanism |
| **Elie E7: mult(spinor in spinor³) = 3** | Three E6 channels | Toy 3608, INV-5295 | β primary | B₂-specific (A₂ gives 0) |
| **Elie E10 dim-spectrum** | V_(3,0) dim 14, V_(2,1) dim 35 — 3 appears in highest weights | Toy 3611, INV TBD | (composite layer) | from word-length 3 expressions |
| **E9 long-root [3]₄ = N_c·g = 21** | Quantum 3 at q=4 base | Toy 3610, INV TBD | α (engine-side) | q-deformation 3 |
| **Tube count #409 (RETRACTED in part)** | 3 affine-tubes (E1b retracted, route II carries via h^∨) | Toy 3598/3599 retracted | δ (counting) | reopened in-house, secondary stakes |
| **Cyclotomic Z/3 via root of unity ω** | ω = e^(2πi/3) | (general theory) | γ candidate | Bergman kernel modular structure |
| **Cremona 27a1 at -N_c** | Heegner anchor at discriminant -3 | K62 | (number-theoretic) | distant from bulk-color directly |
| **Triality of D_4 / Spin(8)** | three 8-dim reps related by S_3 outer auto | (BST D_4 = SO(4,4)?) | (different domain) | not D_IV⁵ but worth noting |
| **A₂-relative to B₂** | A₂ ⊄ B₂ but A₂ has same h^∨ | (Lie-theory) | (obstruction) | the structural difficulty itself |
| **rho-vector ρ₂ = N_c/rank = 3/2** | Shilov-side ρ component | C19 | (substrate-internal) | tied to N_c via rank-2 split |
| **N_c² = rank + g = 9** | Weinberg sin²θ_W = 2/9 | T-series | (composite of 3) | 3² appears in EW sector |

**Reading**: at least 12 distinct 3-fold structures exist in BST, but only **β (E7 spinor³ channels)** is B₂-specific in the strong sense (A₂ analog gives 0), and only **α (h^∨ = N_c = 3)** is a clean B₂ root-system count. The two-structures burden naturally targets {β, α} or {β, γ}.

## Section E — Grace's catalog-side prediction (FRAMEWORK)

Without making a mechanism claim:

**The mechanism most likely to close cleanly is a hybrid α + β:**
- The 3 colors of SU(3) come from h^∨ acting on the bulk K-type Wallach spacing (Path α)
- The 3 generations come from the spinor³ multiplicity (Path β)
- These are STRUCTURALLY INDEPENDENT (one is a bulk-radial tower index; the other is a tensor-product multiplicity)
- Both are tied to B₂ but in different ways (one via root system, one via spinor rep)

This satisfies Keeper's two-structures burden by construction — if Lyra can derive both halves rigorously, #414 + #418 close together.

**Grace prediction (FRAMEWORK)**: Lyra's bulk-color SU(3) mechanism v0.2 will come out closest to Path α (Wallach K-type tower), with the spinor³ count (Path β) holding the generation side.

## Section F — Catalog absorption plan

When Lyra's mechanism v0.2 lands, file:

1. **INV: bulk p-space decomposition under K=SO(5)×SO(2)** (the Section A facts) — DERIVED tier, structural Lie-algebra
2. **INV: [p,p] structure and abelian p_+ obstruction to SU(3)-in-bulk** — DERIVED tier
3. **INV: A₂ ⊄ B₂ structural obstruction** — DERIVED tier, clean Lie fact
4. **INV: Mendeleev-scan 3-fold structures table** (Section D above) — STRUCTURAL tier, catalog cross-reference
5. **INV: bulk-color mechanism v0.2** (Lyra's specific path) — tier TBD per Keeper audit when filed
6. **INV: two-structures burden resolution** (whichever path closes it) — tier TBD per Keeper

## Section G — Honest standing for Saturday EOD

This scaffold is FRAMEWORK; it stages the catalog side without making mechanism claims. The structural Lie-algebra facts in Section A are clean and DERIVED. The candidate paths in Section C are catalogued at FRAMEWORK tier per Keeper's discipline. The Mendeleev-scan in Section D is a research-organization tool, not a derivation.

Source-Verification: all Lie-algebra facts above are textbook (Helgason / Knapp Lie Groups Beyond an Introduction Ch IV-V). Wallach 1976 = the classical reference for the unitary highest-weight reps. Hua 1958 = Bergman kernel formula on type IV domains. No outreach-grade source citations needed for v0.1; will pin to primary sources if/when this content goes external.

Cross-reference: INV-5295 (SU(3)≠SO(5) gate established Friday); INV-5256 / T2442 (c_FK Bergman normalization); T1427 (D_IV⁵ as APG); Elie Toy 3608 (E7 spinor³); Elie Toy 3611 (E10 composite tabulation).

— Grace, G10 v0.1 scaffold, 2026-05-30 Saturday 09:35 EDT
