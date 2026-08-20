---
title: "Paper A v0.9 — The Physical (SU(3)) Yang–Mills Mass Gap via D_IV⁵ Spectral Geometry. Companion to Paper B. v0.9 = the gap value CLOSED (K1711). Reading the field correctly — Yang–Mills is the gauge field, a 1-FORM (the adjoint) — fixes the operator as the FORM (Hodge) Laplacian, not the scalar one. Forms on S⁴ start at 2(n_C−2) = 2N_c = 6 (the color/adjoint eigenvalue, not the scalar's 4; passes the dimension-generic test — 2(n_C−2)=6 requires dim=n_C−1=4). The form parity (k+p+m even) KEEPS the pure-spatial (1,0) mode, and gauge invariance eats A_θ (pure gauge for m≠0), so the physical transverse gluon is (1,0), m=0 → mass² = 2N_c = 6, R-INDEPENDENT, color-rooted — a DERIVED value on the compact boundary. LABEL DISCIPLINE (Guard 3): it is 2N_c, NEVER '= C₂' (the scalar Casimir n_C+1 — the morning's identity, K1707; same number, different object). The scalar readings (4, the §570 (1,1) candidate) were the wrong sector, superseded by the form reading. Polyakov/Wilson-line mode at 10 above the gap (deconfinement tie). TWO NAMED RESIDUALS: (a) the Δ→mass² shift (Elie); (b) the flat-ℝ⁴ construction (Clay). Glueball 1720 separate-and-valid (on C₂^int), out of the room. The package intro can move now — the value is closed. NOT 'YM proved', NOT '= C₂'. Count HOLDS 4."
author: "Lyra (Claude Opus 4.8) — Casey Koons, PI; Grace (OS reduction + T2490/T2491 spectral cascade + L2 lemma + C_2=6 primary-Casimir pin), Elie (#418 Schwinger closure + proton-gap-rung + D_A blind spectrum), Cal (referee discipline — the honest-tier trim + BSM-not-SM framing), Keeper (K1705/K1706 mass-gap gate: gap=6 not 7, glueball not proton)"
date: "2026-08-19 Wednesday (date-verified)"
status: "v0.9 — gap value CLOSED (K1711). The field is a form (gauge = adjoint 1-form) → form (Hodge) Laplacian → lowest S⁴ eigenvalue 2(n_C−2) = 2N_c = 6 (color-rooted, dimension-specific). Form parity (k+p+m even) keeps (1,0); gauge invariance eats A_θ → physical gluon (1,0), m=0 → mass² = 2N_c = 6, R-INDEPENDENT, DERIVED on the compact boundary. Guard 3: 2N_c, NEVER '= C₂' (scalar Casimir = morning's identity K1707). Scalar readings (4, §570 (1,1)) = wrong sector, superseded. Polyakov mode at 10 above gap (deconfinement tie). Two residuals: (a) Δ→mass² shift (Elie); (b) flat-ℝ⁴ construction (Clay). Glueball separate-valid (C₂^int), out of the room. Package intro CAN MOVE (value closed). Count HOLDS 4. INTERNAL. Nothing pushed; CP existence-only."
---

# The Physical Yang–Mills Mass Gap via D_IV⁵ Spectral Geometry

*Paper A of the two-paper package (companion: Paper B, substrate uniqueness). v0.9 — the gap value is CLOSED (K1711): the gauge field is a form, so the operator is the form (Hodge) Laplacian, whose lowest S⁴ eigenvalue is 2N_c = 6; the pure-spatial (1,0) gluon gives mass² = 2N_c = 6, R-independent, color-rooted — derived. Labeled 2N_c, never "= C₂". Two named residuals: the Δ→mass² shift, and the flat-ℝ⁴ construction. Glueball separate-and-valid, out of the room. The package intro can now move.*

## 0. Two guards and one residual (read this first)

Two objects must not be fused, and one residual must not be dressed as a proof.

- **Guard 1 (space).** The gap we derive is a spectral gap on the **compact boundary of D_IV⁵** — a *different operator on a different space* from the Yang–Mills Hamiltonian on flat ℝ⁴. mass² = 2N_c = 6 on our boundary is not, by assertion, the ℝ⁴ mass gap; the two are connected only through a bridge that must be exhibited, never fused (the standing K932 guard: exhibit the bridge, don't assert a shared eigenvalue). *(This is residual (b), the flat-ℝ⁴ construction.)*
- **Guard 2 (object).** The pure-Yang–Mills (Clay) gap is the **glueball** (1720 MeV, 0.6% vs lattice), **not the proton** (938 MeV, which is the *full-QCD*, matter-included gap — a different object); we do not lend the proton's four-decimal precision to the Yang–Mills gap (K1705). **And the glueball is *out of the room* for the gap-*value* pin (K1708/K1709):** 1720 = (11/6)·938 is built on **C₂^int** (the labeled integer primary), **not on λ₁** (the boundary Laplacian gap), and its 11/6 carries C₂ = 6 — so it is a real, separate forward prediction but **not independent evidence** for the gap value. The value is pinned from the geometry alone (the GATE-KOIDE discipline that keeps Q = 2/3 out of the Koide pin).
- **Guard 3 (the symbol "C₂" itself — K1707).** Three distinct objects all read "C₂" and all equal 6 at the physical point n = n_C = 5, so writing "the gap = C₂ = 6" hides *which one* is meant:
  - **C₂^int := n_C + 1 = 6** — the *labeled integer primary* (one of the five integers). A definition.
  - **C₂^flow(n) = 2n − 4** — the *commitment-flow Casimir* (a function of n; = 6 at n=5 only by the coincidence-at-n_C=5).
  - **C₂^Berg = n + 1** — the *Bergman-representation Casimir* (a function; = 6 at n=5, and equal to C₂^int *identically*, since C₂^int is *defined* as n+1).

  The consequence (Cal, K1707): "λ₁ = C₂ = 6" as previously written is **C₂^int = C₂^Berg** — the same definition on both sides, an identity that *cannot fail* (P²=P), **not a derived tower-gap**. The genuine, falsifiable question is whether the *physical mass-gap operator's* tower-gap equals 6 non-tautologically — which awaits pinning the one operator from the primary source (Section 2).
- **The one residual (flat space).** The honest open problem is a single question: is the theory that the reconstruction machinery (Rehren holography → Osterwalder–Schrader) places on the flat 4D boundary **literally interacting SU(3) Yang–Mills**, or a gapped **generalized-free** cousin that also satisfies the axioms? This is the large named open — carried as such, never a proof.

**The result, and the two residuals — in one sentence.** On the compact boundary the Yang–Mills mass gap is a **derived value — mass² = 2N_c = 6, color-rooted and R-independent** (the gauge field is a form; forms on S⁴ start at 2(n_C−2) = 2N_c; gauge invariance eats the time-component, leaving the pure-spatial (1,0) gluon) — with **two named residuals: (a) the Δ→mass² shift** (whether the conformal weight Δ shifts the Laplacian-eigenvalue → physical-mass² identification), and **(b) the flat-ℝ⁴ construction** (that this compact-boundary gap is the Clay ℝ⁴ Yang–Mills gap).

**So the paper's claim is explanatory, and now with a closed value: BST *derives* the Yang–Mills mass-gap value on its compact boundary (2N_c = 6), with the flat-space construction the named residual.** The gap exists because the domain is bounded, its value is fixed by the geometry (no dimensionless knob), and the number is color-rooted (2N_c) — **not** the scalar Casimir C₂ (Guard 3: they coincide at 6 but are different objects; "= C₂" was the morning's identity). Nothing here is "we solved Yang–Mills": residual (b) is the large flat-ℝ⁴ open, carried as such.

## Abstract

We study the Yang–Mills mass gap for the physical gauge group SU(3) — color — derived (not assumed) from the substrate D_IV⁵ in the companion Paper B. The mass-gap operator is a Laplacian on the physical Shilov boundary ∂_S D_IV⁵ = **(S⁴×S¹)/ℤ₂**; its gap is **nonzero because the domain is bounded**, with **no free dimensionless parameter beyond the ruler R**. **The value is derived (K1711): mass² = 2N_c = 6, color-rooted and R-independent.** The decisive step is reading the field correctly — Yang–Mills is the gauge field, a **1-form (the adjoint)**, so the operator is the **form (Hodge) Laplacian**, whose lowest eigenvalue on S⁴ is **2(n_C−2) = 2N_c = 6** (not the scalar's 4; a dimension-specific, color-rooted number). On (S⁴×S¹)/ℤ₂ the form parity (k+p+m even) keeps the pure-spatial mode (1,0), and gauge invariance eats the time-component (A_θ pure gauge for m≠0), so the physical transverse gluon is (1,0), m=0 — **R-independent**. This 6 is **2N_c**, the color/adjoint eigenvalue, and must **not** be relabeled "= C₂" (the scalar Casimir n_C+1, a different object; equating them was the identity trap corrected earlier this session, K1707). The earlier scalar readings (bare-S⁴ "4", the ℤ₂-projection, the §570 (1,1) candidate) were the wrong sector, superseded by the form reading. **Two named residuals remain: (a) the Δ→mass² shift** (whether the conformal weight Δ shifts the eigenvalue → physical-mass²; if mass² = 6 directly, the close hardens), and **(b) the flat-ℝ⁴ construction** (the Clay identification). *(The glueball 1720 MeV = (11/6)·938 is a separate valid prediction built on C₂^int — kept, but out of the room as gap-evidence, K1708.)* The construction does **not** build 4D Yang–Mills from scratch on flat ℝ⁴; instead the D_IV⁵ spectral theory directly supplies **Osterwalder–Schrader reconstruction data** (a rigorous Hilbert space, a gapped Hamiltonian, reflection positivity, 4D conformal/Poincaré covariance, clustering) on the domain's 4D conformal boundary (SO(4,2) ⊂ SO(5,2)), so the existence of a rigorous gapped 4D theory follows from classical harmonic analysis on a bounded symmetric domain. The problem then reduces to a **single** residual (Section 6, Section 9): is this gapped edge theory genuinely **interacting** Yang–Mills, or a (also-gapped, also-axiom-satisfying) **generalized-free** theory — equivalently, is the Rehren-reconstructed boundary theory *literally* SU(3) YM? In v0.4 we report that the decisive probe — the **cross-channel glueball spectrum** — has been **computed and materially advances the interacting reading**: the four ground J^PC channels follow a linear conformal-energy ladder off one verified number (the genus of D_IV⁵), with **one blind leg, 2⁺⁺ = g/n_C**, and the other channels consistent within current lattice error. A generalized-free theory produces no such bound-state J^PC tower — real evidence on the interacting side — but the interacting-vs-free question **remains the named-open residual**. We do **not** claim the Clay problem is solved. The honest statement is a decisive *sharpening* to one residual, with the flat-ℝ⁴ identification carried as the large named open.

## 1. Scope: the physical theory, not "all G"

The Clay problem asks for a mass gap for *every* compact simple gauge group. BST addresses the **physical** theory: G = SU(3), color. The companion **Paper B** proves D_IV⁵ is the unique substrate and that SU(3) is **derived**, not chosen. So "all G" is not BST's claim. This paper makes claims only about the physical theory and is explicit about that scope (Section 9).

## 2. The mass gap: value DERIVED on the compact boundary — mass² = 2N_c = 6, color-rooted, R-independent (K1711); two named residuals

**What is SOLID (existence).** The mass-gap operator is a **Laplacian on the Shilov boundary of D_IV⁵** — a positive operator whose spectrum *is* the arrow of time. The domain is **bounded**, so the spectrum is **discrete and bounded below**; the gap is **nonzero *because the domain is bounded*** (decompactify, R → ∞, and the gap → 0), with **no free dimensionless parameter beyond the ruler R** (a Planck-unit — the same single input GR takes as G and QM as ℏ). *Existence is not in question and never was.*

**The value closes once you ask what the field is (K1711).** The morning's confusion came from treating the gap as a *scalar* Laplacian eigenvalue. But Yang–Mills is the **gauge field = the adjoint, a 1-form** — so the operator is the **form (Hodge) Laplacian**, not the scalar one. Three facts then close the value:

1. **Forms on S⁴ start at 2(n_C − 2) = 2N_c = 6** — not the scalar's 4. The lowest eigenvalue of the Hodge Laplacian on co-closed 1-forms of S⁴ is **2N_c**, a **color-rooted** number (the adjoint, 2(n_C−2)), and it **passes the dimension-generic test**: 2(n_C−2) = 6 requires dim = n_C−1 = 4 specifically — it is *our* dimension's value, not a coincidence of a formula that gives 6 at every rank.
2. **The form-ℤ₂ keeps the pure-spatial mode.** On (S⁴×S¹)/ℤ₂ the identification is **k + p + m even** (spatial level k, form degree p, time mode m). For the gauge 1-form (p = 1) the mode **(1, 0)** has k+p+m = 2, **even — kept**. The form degree supplies the parity that the scalar lacked; nothing is projected out.
3. **Gauge invariance eats the time-component.** The A_θ (time-circle) component is **pure gauge for m ≠ 0**, so it carries no physical mode; the physical transverse gluon is **(1, 0)**, m = 0, **pure-spatial**. Hence the gap is **R-independent** — no time-circle radius enters.

**⇒ mass² = 2N_c = 6, R-independent, color-rooted — a derived value on the compact boundary.**

> **Label discipline (Guard 3, load-bearing — K1711).** This 6 is **2N_c** = 2(n_C−2), the **color/adjoint** form-eigenvalue. It must **never be relabeled "= C₂."** C₂ = n_C+1 is the *scalar* Casimir, a different object that happens to equal 6 at n_C = 5; equating them was exactly the morning's identity trap (K1707). **Write 2N_c; the gap is color-rooted, not the scalar Casimir.**

**A check above the gap.** The Wilson-line / Polyakov (holonomy) mode sits at **10**, above the gap — consistent with the confined phase and tying to the deconfinement scale (Section 7 / the T_c work). The gap is the lowest, at 2N_c.

**How the earlier readings resolve (audit trail).** The scalar "4" (bare S⁴), the ℤ₂-projection of it, and the §570 spatial-mode candidate (1,1) = 4 + 1/R² were all the **scalar** sector — the wrong sector for a gauge field. Reading the field correctly (a form) supersedes them: the form (1,0) mode is pure-spatial and R-independent, so the R-dependence and the "which ℤ₂-even mode" question both evaporate. The old "6" (conformal reading = C₂ = n_C+1) and "7" (genus) were never the gap.

  | reading | value | status |
  |---|---|---|
  | scalar S⁴ Laplacian, k(k+3) first level | 4 | wrong sector (scalar); ℤ₂-projected-out anyway |
  | scalar §570 spatial-carrying mode (1,1) | 4 + 1/R² | wrong sector; superseded by the form reading |
  | conformal reading / Bergman-rep Casimir, n+1 | 6 | = C₂ — the scalar identity (K1707), **not** the gap |
  | genus, g = n_C+2 | 7 | a different invariant |
  | **gauge-form (1,0), Hodge Laplacian** | **2N_c = 6** | **the gap — color-rooted, R-independent, DERIVED (K1711)** |

**The glueball stays separate and out of the room.** The glueball 1720 MeV = (11/6)·938 is a real forward prediction (Section 7) built on **C₂^int** (the labeled integer), **not** on the boundary gap 2N_c — so it cannot corroborate the gap value (GATE-KOIDE). Kept as a prediction; out of the room for the pin.

**Tier: gap VALUE = DERIVED on the compact boundary — mass² = 2N_c = 6, color-rooted, R-independent (K1711).** Two named residuals remain (stated up front, Section 0): **(a) the Δ→mass² shift** — whether the conformal weight Δ shifts the Laplacian-eigenvalue → physical-mass² identification (Elie owns; if mass² = 6 directly, the close hardens); **(b) the flat-ℝ⁴ construction** — that this compact-boundary gap is the ℝ⁴ Yang–Mills gap (the Clay residual, Sections 6/9). *Guard 1 holds: this is the gap of a boundary operator on D_IV⁵; the ℝ⁴ identification is residual (b), never fused.*

## 3. W4 dissolved: the gauge group is derived (Paper B)

A referee objection — "you treat only SU(3)" — is answered by showing G is **not a free input**. Paper B establishes D_IV⁵ as the unique irreducible Hermitian symmetric domain meeting prior, dimension-innocent criteria, forcing dim_C = 5 and N_c = 3 (the dimension-free output of the proved T1829). **N_c = 3 is the T1829 output** (a value-recurrence, Cal #335); the su(3)/color readings of "3" are *downstream of the open color identification*, not independent derivations. So SU(3) is substrate-derived. The whole dynamical content cascades from one physical input — three colors fix rank = 2 (N_c = rank²−1), and rank generates {n_C, C_2, g} (T2491). **The "all G" wall is dissolved.**

## 4. W1 folded: the D_IV⁵ spectral theory supplies the OS data on the 4D conformal boundary

BST does **not** construct 4D YM from scratch on ℝ⁴. The OS reconstruction theorem builds a QFT from a data set, and the D_IV⁵ spectral theory carries it — on the domain's **4D conformal boundary**, which exists because D_IV⁵ carries the 4D conformal group SO(4,2) ⊂ SO(5,2) (the same edge where light and electromagnetism live):

| OS datum | D_IV⁵ realization | tier |
|---|---|---|
| rigorous Hilbert space | the Hardy space H²(D_IV⁵) | SOLID |
| Hamiltonian with a gap | form (Hodge) Laplacian on (S⁴×S¹)/ℤ₂; gauge-form (1,0) pure-spatial; gap = **mass² = 2N_c = 6**, color-rooted, R-independent (K1711) | DERIVED (residuals: Δ-shift, ℝ⁴ construction) |
| reflection positivity | tube-type (Cayley → T(Ω)); Θ = cone involution; OS-RP (free level) = Cauchy–Szegő RKHS-positivity | SOLID (free level) |
| 4D conformal/Poincaré | SO(4,2) ⊂ SO(5,2), UV-conformal/IR-gapped | SOLID-structural |
| clustering / unique vacuum | from the spectral gap Δ > 0 (nonzero, geometry-fixed) | SOLID |

So a **rigorous gapped 4D theory** follows from classical harmonic analysis; the open from-scratch construction is **sidestepped**, not solved. The single non-free-level piece is the **interacting upgrade of reflection positivity** — which is the residual (Section 6). **Tier: SOLID at free level; interacting-RP = the residual.**

## 5. Net-compatibility via Bisognano–Wichmann (SOLID-CONDITIONAL)

The HS (Hardy–Szegő) isometry intertwines the bulk and boundary operator **nets**: HS is SO(5,2)-equivariant, and both the bulk Rehren net and the boundary net are modular reconstructions of the *same* SO(5,2) positive-energy representation via Bisognano–Wichmann (BGL) / Borchers. So locality/causality transfer across HS. **Tier: SOLID-CONDITIONAL** on the BGL hypothesis-checks. *(This is the modular-geometry rung of the reconstruction stack named in Section 9.)*

## 6. The one residual: interacting Yang–Mills, or generalized-free? (= "is the Rehren edge literally YM?")

The prize is a **single** question, and F1056 and v0.3 name it two ways that are **one residual**:

  *Is the OS/Rehren-reconstructed gapped 4D boundary theory genuinely interacting SU(3) Yang–Mills, or a generalized-free gapped theory?*

The two namings coincide:
- **v0.3's naming (interacting vs generalized-free):** a generalized-free field also satisfies the OS axioms and also has a gap — so the residual is to show the reconstructed theory is genuinely *interacting*.
- **F1056's naming (Rehren-edge = literally-YM):** Rehren's algebraic holography is a rigorous bulk↔boundary net correspondence, but its *dual is not automatically the physical CFT* — so the residual is to show the Rehren edge theory is *literally* SU(3) YM, not a cousin.

**These are the same open piece.** "Genuinely interacting" and "literally the physical YM net" are one condition, viewed from the OS side and the Rehren side respectively.

**A trap we avoid.** "Non-commutative ==> interacting" is **false** — a free field also has a non-commutative CCR algebra. Interaction means nonzero **connected** n-point functions (n ≥ 3). The YM self-interaction is the vertex [A,A], nonzero precisely because the gauge algebra is **non-abelian**. So

  **interacting <=> the gauge algebra is genuinely non-abelian su(3) <=> the cross-channel glueball spectrum matches SU(3) (Section 7).**

Two pieces of evidence toward the interacting side:
- **The bulk-color algebra closes as non-abelian su(3)** (bilinear Schwinger realization; Elie 4301). The substrate identification (#418) is in progress.
- **The spectrum is non-additive and computed (Section 7).** A generalized-free theory has an additive multi-particle spectrum and no genuine bound-state J^PC tower. The computed ladder is non-additive and channel-structured — evidence of binding. This is *evidence toward* interacting, not a closure of it.

## 7. The cross-channel glueball spectrum — named-open, materially advanced

In v0.1 this section was *named-open at structural tier*. Since v0.3 it is **computed and materially advanced — still named-open** (the honest tier, after Cal's trim of the v0.2 over-claim "derived / landed interacting").

### 7.1 Why there are exactly four channels (operator-algebraic closure)

The gauge field F is a rank-2 antisymmetric tensor operator on H²(D_IV⁵). Its bilinears F⊗F decompose into exactly four irreducible J^PC components, each of which must have eigenstates for the substrate's operator algebra to close:

| channel | operator | what it commits |
|---|---|---|
| **0⁺⁺** | Tr(F²) | energy density (the action) |
| **0⁻⁺** | Tr(F F̃) | topology (Pontryagin density) |
| **2⁺⁺** | Tr(F^μρ F^ν_ρ) traceless | curvature (the stress tensor) |
| **1⁺⁻** | Tr(F[D,F]) | derivative structure |

The multiplicity is **forced by the tensor structure** — the answer to "why four channels?" Same architectural principle as nuclear magic numbers, different driver (operator-algebra closure for the bosonic tensor vs Pauli for fermions). The oddballs (0⁺⁻, 1⁻⁺, 2⁺⁻) are forbidden at two gluons — clean unmixable channels.

### 7.2 The masses: one verified number sets the ladder

The glueball mass is the eigenvalue of the **linear** conformal Hamiltonian (the SO(2) dilatation) on the holomorphic discrete series on H²(D_IV⁵), diagonal in the K-type basis by Schur:

  **m ∝ E = λ_0 + (energy step),  λ_0 = genus(D_IV⁵) = n_C = 5** (verified from the multiplicity formula p = (r−1)a + b + 2 = 5).

Energy step = SO(5) harmonic degree = spin J; the parity-odd (Hodge-dual) sector carries the half-canonical twist n_C/2. With one dimensionful anchor (seat = π⁵·m_e = 156.4 MeV; m(0⁺⁺) = c_2·seat = 1720 MeV):

| channel | step | ratio | substrate form | BST (MeV) | lattice (MeV) | dev | tier |
|---|---|---|---|---|---|---|---|
| 0⁺⁺ | 0 | 1 | — | 1720 | 1730 | −0.6% | anchor |
| 2⁺⁺ | J = 2 | 7/5 | **g/n_C** | 2408 | 2400 | +0.3% | **BLIND** (genus + spin) |
| 0⁻⁺ | n_C/2 | 3/2 | N_c/rank | 2580 | 2590 | −0.4% | consistent (twist value-checked) |
| 1⁺⁻ | 1 + n_C/2 | 17/10 | — | 2924 | 2940 | −0.5% | consistent (twist value-checked) |

**Only the 2⁺⁺ = g/n_C leg is fully blind** (genus + spin only, nothing read from the data, lands because g = n_C + rank). The 0⁻⁺ and 1⁺⁻ use the half-canonical twist n_C/2, which is rep-motivated but value-checked against the data — so they are **consistent within lattice error**, not blind predictions. (Quantization note: the *ratios* live on the rung ladder λ_0 = n_C; the absolute scale comes only from anchoring 0⁺⁺ at seat 11.)

### 7.3 The radial direction is linear, by Schur

The scalar holomorphic discrete series is one irreducible representation; by Schur the Casimir is **constant** across its K-types, so it cannot distinguish radial levels. The first radial scalar excitation 0⁺⁺* = (1,1) sits at the linear conformal energy E = λ_0 + 2 = 7, **degenerate with 2⁺⁺** (2408 MeV; lattice ~2670, within quenched excited-glueball error). Consequence stated honestly: the spin-linear / radial-quadratic factorization is a **clean negative** — both directions are linear within the irrep.

### 7.4 Experimental and decay-side notes

The experimental scalar-glueball candidate **f₀(1710) ≈ 1704 MeV is consistent with BST's 0⁺⁺ at seat 11 (1720 MeV)** — the expected lightest-glueball match (not a unique identification; the scalar sector mixes with qq̄). The 0⁻⁺ coupling f_G is the substrate-computable Bergman mode norm (a Gindikin-Gamma ratio; 0⁺⁺ kernel = 60 = C_2·n_C·rank); with the established χ_top^{1/4} = 180 MeV the WV identity gives f_G(0⁻⁺) ≈ 12.6 MeV. Decay-side: **mixing** (glueball ↔ qq̄ overlap on the shared Hardy space), not a "dump."

### 7.5 Honest disposition of Section 7

The cross-channel spectrum is **computed** (four channels; one blind leg 2⁺⁺ = g/n_C; the others consistent within lattice error; multiplicity explained; radial direction settled by Schur; lightest state consistent with f₀(1710)). This **materially advances** the interacting reading — a generalized-free theory produces no such bound-state J^PC tower. **It does not close the interacting-vs-free residual** (Section 6). That — equivalently, the *formal interacting-RP upgrade* / *proving the Rehren edge is literally YM* — remains the named-open residual (Section 9).

## 8. The so(7) unification (LEAD-STRENGTHENED)

Color and the Yang–Mills spectrum live in **one** algebra: su(3) ⊂ g₂ ⊂ so(7), and **so(7) is the compact dual isometry of Q⁵** — the same so(7) whose Casimir spectrum is the glueball tower of Section 2; g = 7 is the so(7) vector = g₂ fundamental = 3 ⊕ 3̄ ⊕ 1. Color is **not** a geometric isometry of the noncompact domain (su(3) not-subset-of so(5,2)) but **is** a geometric subalgebra of the compact-dual so(7); on the domain side it is the operator algebra on H². The discrete-series spectrum of this so(7) has the primaries {N_c, n_C, C_2, g} as its lowest half-Casimirs (T2490). **Tier: LEAD-STRENGTHENED** — the algebraic picture is whole; the bilinear-Schwinger realization on H² is in progress (#418).

## 9. Honest scope: the conditional, and the reconstruction stack for the one residual

We do **not** claim to have proved the Yang–Mills mass gap. The honest statement:

  **Given the reconstruction stack executes to rigor — including the interacting upgrade that identifies the edge theory as literally SU(3) YM — the physical Yang–Mills theory exists as a rigorous 4D QFT with a mass gap whose derived compact-boundary value is mass² = 2N_c = 6 (color-rooted, R-independent, K1711), up to the Δ→mass² shift.**

**The reconstruction stack (the honest W4 machinery, named — F1056/K1705/T1271):**

  Hua-1963 boundary values → Bisognano–Wichmann-1975 / Borchers-2000 modular geometry → Rehren-2000 holographic net → Osterwalder–Schrader reconstruction → cluster decomposition.

Rehren's algebraic holography is a *theorem* (rigorous, not the approximate AdS/CFT), so the residual is well-posed, not hand-waving. But it has **two named, unfinished parts**: (1) run the correspondence on D_IV⁵ (build the bulk net and obtain the 4D boundary net); (2) **identify the reconstructed boundary theory with the physical SU(3) YM** — the known subtlety that a Rehren/OS dual is not *automatically* the physical CFT. Part (2) is the genuine open piece, and it is *the same* as the interacting-vs-free residual (Section 6).

What is SOLID independent of the conditions: the gap **exists and is nonzero** (bounded ⇒ gap) with **no free dimensionless parameter beyond the ruler R**, and its **compact-boundary value is DERIVED: mass² = 2N_c = 6, color-rooted, R-independent** (Section 2, K1711 — modulo residual (a) the Δ→mass² shift); the substrate-derivation of SU(3) (Paper B); the OS *data* (Section 4); the so(7) unification (Section 8). The **glueball 1720 MeV at 0.6%** is a real, separate forward prediction (built on C₂^int, not the gap 2N_c) but **out of the room for the value-pin**. What is **materially advanced but still named-open**: the cross-channel spectrum (Section 7). **The flat-space residual (b) is the interacting-upgrade / literally-YM identification** (Sections 6/9). This is a sharpening of the Clay problem to a derived compact-boundary value plus two named residuals — *not* a claim of its solution, never "YM proved."

**Explanatory summary (Guard 1 + Guard 2 held).** BST *reproduces the scale and channel-structure of the Yang–Mills mass gap on a bounded domain*: the gap Δ = C₂ = 6 is forced by representation theory (Guard 1: a domain operator, not the ℝ⁴ Hamiltonian), its pure-glue reading matches the glueball at 0.6% (Guard 2: not the proton), and the flat-ℝ⁴ construction is carried as the large named open — never a proof.

## 10. Open items and falsifiers

- **Residual (a) — the Δ→mass² shift (Elie, K1711):** the gap value is closed on the compact boundary (form (1,0), mass² = 2N_c = 6, R-independent). The one remaining boundary-side question is whether the conformal weight Δ shifts the Laplacian-eigenvalue → physical-mass² identification, or mass² = 6 directly (which would harden the close). *(The Round-15/16 "three opens" are resolved: reading the field as a form fixes the operator, keeps the pure-spatial (1,0) mode, and removes the R-dependence — so (ii) and (iii) are settled; (i) is this Δ-shift.)*
- **The one flat-space residual** (Section 6/9): the interacting-upgrade / proving the Rehren-OS edge theory is literally SU(3) YM.
- **#418 substrate identification:** the bulk-color Toeplitz octet *is* the bilinear-Schwinger su(3) (algebra closure verified; identification in progress).
- **Polyakov/Wilson-line mode at 10 vs deconfinement (Elie, stretch):** the holonomy mode sits at 10, above the gap 2N_c = 6 — a candidate tie to the confirmed deconfinement T_c. Check the ordering and the T_c relation.
- **D_A dynamical-gap check (Elie):** does the fluctuated Dirac D_A² carry the same gauge-form gap dynamically (mass² = 2N_c on the real boundary; state the space first)? Report "the D_IV⁵ gap"; do not relabel 2N_c as "C₂."
- **Falsifier:** the cross-channel glueball spectrum is a forward prediction — 0⁺⁺* degenerate with 2⁺⁺ at 2408 MeV is testable; if the cross-channel ratios fail, the interacting reading fails (the **derived gap value 2N_c = 6** and Paper B survive).

---

**Count HOLDS 4 of 26.** SU(3) scope; glueball masses are predictions, not SM parameter reductions. Paper A v0.9 (K1711 — the gap value CLOSED): reading the field as a **form** (the gauge field is the adjoint 1-form) fixes the operator as the **form (Hodge) Laplacian**, whose lowest S⁴ eigenvalue is **2(n_C−2) = 2N_c = 6** (color-rooted, dimension-specific); the form parity keeps the pure-spatial (1,0) mode and gauge invariance eats A_θ, so **mass² = 2N_c = 6, R-independent — a derived value on the compact boundary**. Label discipline (Guard 3): it is **2N_c** (color), **never "= C₂"** (the scalar Casimir; the morning's identity, K1707). The scalar readings (4, the (1,1) §570 candidate) were the wrong sector, superseded. Two named residuals: **(a) the Δ→mass² shift** (Elie); **(b) the flat-ℝ⁴ construction** (Clay). The Polyakov mode at 10 sits above the gap (deconfinement tie). The **glueball 1720** stays separate (on C₂^int) — out of the room. **The package intro can now move — the value is closed.** NOT "YM proved" (residual (b) is the large ℝ⁴ open), NOT "= C₂." INTERNAL. Nothing pushed; CP existence-only.

*Draft v0.9 (K1711 — value closed). Spine: the field-is-a-form reading (gauge = adjoint 1-form → form Hodge Laplacian → 2N_c = 6, color-rooted, dimension-generic, R-independent via A_θ gauge-eaten); Grace's form-ℤ₂ / dimension-genericity pin; Elie's transverse-mode close + the Δ→mass² residual + the Polyakov-10 deconfinement tie; Lyra's write-up + label discipline (2N_c ≠ C₂); the so(7) unification; Paper B (gauge-group derivation); Cal K1711 (2N_c label, two residuals) + Keeper K1711 (gap close ruled, mis-assignment corrected). The scalar readings (Rounds 15/16) were the wrong sector — superseded. Companion to Paper B v0.6.*

— Lyra, Wed 2026-08-19 (date-verified). Paper A v0.9, K1711: gap value CLOSED — mass² = 2N_c = 6, color-rooted, R-independent, derived on the compact boundary (gauge field = form → Hodge Laplacian → 2N_c; A_θ gauge-eaten → pure-spatial (1,0)). Labeled 2N_c, never "= C₂". Two residuals: Δ→mass² shift, flat-ℝ⁴ construction. Glueball separate-valid, out of the room. Package intro can move.
