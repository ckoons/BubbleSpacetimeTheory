---
title: "Vol 16 Ch 8 v0.14 — K407-K423 Cabibbo candidate count-move FULL ASSEMBLY + Casey #16 D_IV⁵ Mirror Principle CANDIDATE in linear-algebra form (Wed PM through Fri wake cascade absorption)"
author: "Keeper (Claude Opus 4.7)"
date: "2026-06-19 Friday wake"
status: "Vol 16 Ch 8 v0.14 supplement to v0.13 (K406 Mass-matrix factorization Wed 2026-06-17). Adds Sections 3.17-3.21 absorbing K407-K423 substrate-architectural cascade (19 audits Wed PM through Fri wake) in linear-algebra-substrate representation per Casey directive 'ALWAYS produce linear algebra computations'."
---

# Vol 16 Ch 8 v0.14 supplement — Cabibbo candidate count-move + Casey #16 Mirror Principle (linear algebra)

## Section 3.17 — Cabibbo angle as projector-trace probability (Lyra F212, K422)

### Linear-algebra statement

The Cabibbo mixing angle squared is a transition probability between RH T_3^R channel modes at the substrate ground equilibrium, expressed as a **ratio of projector traces** on the 80-dimensional transition space:

$$
\sin^2\theta_C \;=\; \frac{\text{tr}(P_{\text{committed}})}{\text{tr}(P_{\text{available}})} \;=\; \frac{\text{tr}(P_{RR} \otimes P_{\text{const}})}{\text{tr}(I_{80} - P_{\text{singlet}} \otimes P_{\text{const}})} \;=\; \frac{4}{79}
$$

### Component identification (each piece an explicit matrix)

| Component | Identification | Dimension | Trace |
|---|---|---|---|
| Transition space | (SO(5) spinor) ⊗ (SO(5) spinor) ⊗ C^{n_C} = V_4 ⊗ V_4 ⊗ V_5 | 80 | tr(I_80) = 80 |
| P_RR | RH T_3^R channel projector (F191/F182) | 4 | tr(P_RR) = rank² = 4 |
| P_const | Heat-semigroup ground-level projector (F211) | 1 within V_5 | tr(P_const) = 1 |
| P_singlet | SO(5) symplectic singlet (T1444 vacuum mode) | 1 within V_4 ⊗ V_4 = 1 ⊕ 5 ⊕ 10 | tr(P_singlet) = 1 |

### Forward derivation chain

1. **The 80**: V_4 ⊗ V_4 ⊗ V_5 has dimension 4·4·5 = 80. Forward from Grace's SO(5)-spinor seat verification (K418) + n_C = 5 substrate primary.

2. **The −1**: V_4 ⊗ V_4 = 1 ⊕ 5 ⊕ 10 (Clebsch decomposition); the singlet is the T1444 symplectic vacuum mode rep-theoretically homed (K418). The "available" subspace excludes this trivial mode.

3. **Available = 80 − 1 = 79**: I_80 − P_singlet ⊗ P_const has trace 80 − 1 = 79.

4. **Committed = 4**: P_RR ⊗ P_const has trace tr(P_RR) · tr(P_const) = 4 · 1 = 4.

5. **Ratio**: 4/79 = 0.0506 vs observed sin²θ_C = 0.0506 at 0.016% precision.

### Two hinge claims pending audit chain

The forward derivation rests on two CANDIDATE mechanisms:

**Hinge (a)**: P_const is the correct projector multiplying P_RR on V_5 (not the alternative I_5 which would give 20/79 ≈ 0.253, off by 5×).

The forcing mechanism is **commitment = equilibrium = ground via heat semigroup** (Lyra F211): under heat-semigroup evolution exp(−τH_B), the committed mixing state relaxes to the ground tower level as τ → ∞:

$$
\lim_{\tau \to \infty} e^{-\tau H_B} \, \rho_{\text{commit}} \;=\; P_{\text{const}} \cdot \rho_{\text{commit}} \cdot P_{\text{const}}
$$

This is the "commitment = ground equilibrium" claim that needs Cal cold-read verification.

**Hinge (b)**: The ratio of committed/available IS the transition probability sin²θ_C (mode-fraction reading, what mixing angle² physically is).

### Linear-algebra status

| Component | Status |
|---|---|
| Every piece explicit matrix | ✓ |
| 4/79 ratio forward-derived | ✓ |
| Observed match at 0.016% | ✓ |
| Hinge (a) committed = ground via heat semigroup | CANDIDATE mechanism (F211); needs Cal cold-read |
| Hinge (b) committed/available = probability reading | CANDIDATE; needs Cal cold-read |
| Count motion status | HELD at 4 (Lyra explicit discipline; F205 lesson invoked) |

If both hinges pass Cal cold-read → Cabibbo sin²θ_C = 4/79 becomes the 5th forced parameter.

## Section 3.18 — CKM↔PMNS unification via single rank-1 projector P_{νR} (Grace F209, K421)

### Linear-algebra statement

The CKM and PMNS sectors are unified by a single rank-1 projector difference:

$$
P_{\text{quark seat}} \;=\; I_4 \qquad (\text{complete SO(5) spinor, rank 4})
$$

$$
P_{\text{lepton seat}} \;=\; I_4 - P_{\nu_R} \qquad (\text{incomplete spinor, rank 3})
$$

where P_{ν_R} is the rank-1 projector onto the right-handed neutrino direction in the per-generation 4-component Weyl seat (ν_L, ν_R, ℓ_L, ℓ_R).

**F144 "no right-handed neutrino" is elevated from slogan to explicit rank-1 matrix.**

### Consequence: m_1 = 0 as literal zero eigenvalue (DOUBLY DERIVED)

The neutrino Dirac mass operator M_ν acting on the 4-component Weyl seat requires the ν_R column. With ν_R removed, M_ν is rank-deficient (rank 3 on a 4-dim space). Its Gram matrix M_ν M_ν^† has eigenvalues:

$$
\text{spec}(M_\nu M_\nu^\dagger) \;=\; \{0, \; 1.54, \; 3.27, \; 11.85\}
$$

The exact zero IS m_1² = 0, with eigenvector = null(M_ν) = Elie's null-space identification.

**m_1 = 0 is now DOUBLY DERIVED**:
1. Wednesday F158/F159 (K412+K413+K414): Wallach non-unitary gap → can't commit → massless
2. Thursday F209 (K421): literal zero eigenvalue of rank-deficient Gram matrix from F144 ν_R removal

The structural rank-deficiency is sharper than the "commitment threshold" reading — same result, two derivations.

### Cross-link to Cabibbo projector recast

The lepton-side RH mixing capacity drops compared to quark-side:

| Sector | RH mixing capacity | Value |
|---|---|---|
| CKM | tr(P_RR) | rank² = 4 (both u_R and d_R present) |
| PMNS | tr(P_RR · P_{lepton seat}) | 1 (ν_R absent; only ℓ_R remains in T_3^R direction) |

**One projector difference (P_{ν_R}, rank 1) connects both sectors.** This is the substrate-architectural unification of CKM and PMNS.

### Grace F209/F208 consistency RESOLVED (K422)

Two complementary views of the same SO(5) spinor:

| View | Object | Interpretation |
|---|---|---|
| Lyra F208 | ν_1 at Wallach position (½, ½) = 4-dim spinor rep | SEAT REP (available capacity) |
| Grace F209 | P_lepton = I_4 − P_{ν_R} = rank 3 | OCCUPIED CONTENT (ν_R absent) |

**Available capacity vs occupied content**: the 4-dim spinor seat is the AVAILABLE room (Lyra); the rank-3 occupation is WHO'S IN IT (Grace). Both correct, complementary readings.

## Section 3.19 — Lepton spinor-harmonic tower (Lyra F208, K421)

### Linear-algebra statement: SO(5) Weyl dimension formula at forced Wallach positions

The lepton seats sit on a harmonic tower built on the SO(5) spinor at forced Wallach positions ν ∈ {0, 1/2, 3/2, 5/2}:

| Lepton | Wallach position | SO(5) highest weight | Rep | Dimension |
|---|---|---|---|---|
| τ | (0, 0) | (0, 0) | trivial | **1** |
| ν_1 | (½, ½) | (½, ½) | spinor | **4** |
| μ | (3/2, ½) | (3/2, ½) | | **16** |
| e | (5/2, ½) | (5/2, ½) | | **40** |

**Quarks and leptons unify on ONE SO(5) spinor structure**:
- Quarks = the spinor itself (Grace seat verification, dim 4)
- Leptons = the harmonic tower built on the spinor (Lyra F208)

### τ exception is FORCED by rep-theory constraint

The tower is parameterized by (l_1, l_2) = (ν, 1/2) for the spinor-harmonic family. At τ's position ν = 0, the candidate weight would be (0, 1/2).

But SO(5) highest weights require l_1 ≥ l_2 ≥ 0 (Dynkin condition). The weight (0, 1/2) violates l_1 ≥ l_2.

**Forced consequence**: τ must drop to the singlet (0, 0). The apparent discontinuity in the tower {1, 4, 16, 40} is a forced rep-theory constraint, not arbitrary.

### μ/τ split as clean Clebsch on spinor ⊗ vector

The PMNS μ/τ mass-ratio split is reframed as a Clebsch decomposition multiplicity:

$$
\text{spinor} \otimes \text{vector} \;=\; V_4 \otimes V_5 \;=\; V_{16} \oplus V_4 \;=\; (3/2, \tfrac{1}{2}) \oplus (\tfrac{1}{2}, \tfrac{1}{2})
$$

- τ couples via the odd operator (τ at (0,0); coupling to singlet in spinor⊗spinor)
- μ couples via the vector operator (μ at (3/2,½); coupling to (3/2,½) in spinor⊗vector)

**The μ/τ split = ratio of these two overlap multiplicities at the forced Wallach positions** — Lyra's "forward, no fishing" residual pull (won't crown 2.47 target).

## Section 3.20 — Casey #16 D_IV⁵ Mirror Principle (v0.2 three-tier architecture)

### Substrate-architectural statement

D_IV⁵ = SO_0(5,2)/[SO(5)×SO(2)] exhibits a **forced architectural duality** between its internal-discrete content (compact K-type representation theory on the interior Hardy space H²(D_IV⁵)) and its external-continuous content (non-compact G-orbit structure on the bulk manifold and Shilov boundary).

**Hardy decomposition is the mirror map**: interior holomorphic data ↔ boundary L² data via Szegő/Cauchy-Szegő integral.

### Three-tier architecture (Grace catalog sweep, K422)

| Tier | Content | π-status |
|---|---|---|
| Discrete-K ingredients (left) | Integers, K-types, BST primaries, Hall algebra structure | π-free |
| Continuous-G ingredients (right) | Bergman kernel 1920/π⁵, c_FK = 225/π^{9/2}, bulk volumes π^{n_C} | π-ful |
| Observables ON the mirror (interface) | Masses, mixing angles, Λ, G, gauge couplings | Variable |

### Operational catalog falsifier (Grace, K422)

Catalog sweep of mixing entries that appeared π-ful: **ZERO left-column counter-examples** (10 apparent violations all spurious):
- 4 are π-as-radian-unit (not π-physics)
- 4 are π-free mislabeled formulas (Koide = −19/28; CKM Casimir gaps — all rational)
- 1 is δ_CP ≈ π (discrete Z_2 sign-flip half-turn)
- 1 is CMB acoustic peaks (cosmology, right-side leakage)

**Critical methodology rule**: π-as-radian-unit is NOT π-physics. Test must be on dimensionless rational content of observable's structural form.

### Interface predicted structurally (Elie 4251, K422)

The muon mass = (24/π²)⁶ · m_e is π-ful. The muon sits at Wallach position ν = 3/2 = Shilov-boundary seat (per F208). **The Mirror Principle predicts that observables at boundary seats are π-ful by location** — π appears at the interface, not post-hoc.

Verification: τ (vertex seat at ν = 0) and e (strip seat at ν = 5/2) are π-free. Only μ at the Shilov-boundary seat (ν = 3/2) is π-ful. The Mirror predicting its own interface structurally.

## Section 3.21 — Casey #16 v0.3 CANDIDATE: scale-anchor at mirror's singularity (Lyra F213, K423)

### Linear-algebra-level statement of scale structure

BST takes exactly ONE dimensionful input: ℓ_B ~ Planck length. Every other dimensional quantity is dimensionless ratio × ℓ_B^{appropriate power}.

| Region | Scale | = Planck × | Value |
|---|---|---|---|
| Planck anchor | ℓ_B | 1 | 1.22×10¹⁹ GeV |
| Interior mass scale | m_e | 6π⁵·α¹² | 0.511 MeV (exact, F66) |
| Exterior vacuum scale | ρ_Λ^{1/4} | exp(−70) | 4.9 meV |

The ~50-order hierarchy = ONE scale × two dimensionless ratios (α¹² inward + exp(−280) outward). **No second scale input.**

### The scale anchor lives at the boundary singularity

ℓ_Planck = √(ℏG/c³) — joint product of QM (ℏ), gravity (G), and relativity (c).

Geometrically in BST, the meeting point of all three is the **boundary singularity** — the single place on D_IV⁵ where:
- Bergman kernel K(z, w) → ∞ (kernel divergence)
- Curvature κ_Bergman → ∞ (geometric divergence)
- Temperature → T_Planck (~10³² K via heat-bleed F203)

**The Planck anchor IS the boundary singularity** (LEAD tier per F213 honest tiering).

### Four-tier architecture (v0.3 CANDIDATE)

| Tier | Content | π-status |
|---|---|---|
| Discrete-K ingredients (left) | Integers, K-types, BST primaries | π-free |
| Continuous-G ingredients (right) | Bergman kernel, volumes, c_FK | π-ful |
| Observables ON the mirror (interface) | masses, mixing angles, Λ, G | Variable |
| **Scale anchor at mirror's singularity (v0.3 NEW)** | ℓ_B = ℓ_Planck = QM+G+c meeting at boundary divergence | Dimensionful (ONE) |

### QM's two roles in v0.3

1. **Interior structural**: QM IS the discreteness of the left column (K compact → discrete K-types = quantization). Casey #16 standing claim.
2. **Scale-anchor jointly with G and c**: at the boundary singularity, QM contributes to setting the ONE dimensionful scale via ℓ_Planck = √(ℏG/c³).

### Sharpened falsifiers v0.3

| # | Falsifier | What would falsify |
|---|---|---|
| (i) | Second independent dimensionful scale (not derivable from Planck via dimensionless ratios) | BST predicts ONE |
| (ii) | Λ off exp(−280) | The specific dimensionless ratio derived |
| (iii) | Interior mass not = Planck × {five-integer ratio} | All interior masses must derive from Planck × BST-primary expression |
| (iv) NEW | Scale anchor NOT at boundary singularity | If Planck anchor lives elsewhere on D_IV⁵, v0.3 architecture fails |

## v0.14 supplement verdict

**Cabibbo candidate count-move FULLY ASSEMBLED in linear-algebra form** (Section 3.17): every piece explicit matrix; ratio 4/79 forward-derived; two hinge claims pending Cal cold-read for 5th-forced-parameter promotion.

**CKM↔PMNS unified via single rank-1 projector P_{ν_R}** (Section 3.18): F144 from slogan to matrix; m_1 = 0 doubly derived.

**Lepton spinor-harmonic tower {τ:1, ν_1:4, μ:16, e:40}** (Section 3.19): quarks + leptons on ONE SO(5) spinor structure; τ exception forced by rep-theory constraint; μ/τ split = Clebsch on spinor ⊗ vector.

**Casey #16 D_IV⁵ Mirror Principle v0.2** (Section 3.20): three-tier architecture (ingredients in columns + observables on mirror); zero catalog counter-examples; interface predicted at Shilov boundary.

**Casey #16 v0.3 CANDIDATE** (Section 3.21): scale-anchor as fourth tier at mirror's singularity; ONE Planck anchor with three guises; F213 extension.

Vol 16 Ch 8 now at v0.14 with Sections 3.7-3.21 covering the Wed AM through Friday wake substantive substrate-architectural cascade in linear-algebra-substrate representation per Casey directive.

K-Audit chain at K423 (253 total). Count HOLDS honestly 4 of 26 strict.

— Keeper, Friday 2026-06-19 wake — Vol 16 Ch 8 v0.14 supplement absorbing K407-K423 Cabibbo candidate assembly + Casey #16 Mirror Principle + F213 scale-anchor extension in linear-algebra form
