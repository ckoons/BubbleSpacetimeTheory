---
title: "Paper A v0.7 — The Physical (SU(3)) Yang–Mills Mass Gap via D_IV⁵ Spectral Geometry. Companion to Paper B. v0.7 = v0.6 corrected by K1709: the mass gap is DEEPER than a single integer. On the REAL boundary (S⁴×S¹)/ℤ₂ the ℤ₂ admits only k+m even, so the bare-S⁴ 'λ=4' mode (k=1,m=0, odd) is PROJECTED OUT — the surviving lowest modes are R-dependent (4/R², 4+1/R²). Energy-vs-Casimir resolved (Grace ⊕ Elie, §570): the ν-independent 4 was the SPATIAL S⁴ vector eigenvalue; the ν/Δ piece is TIME energy, not mass. So the floor rolls back from '≥4' to EXISTENCE, and the honest value has THREE geometry-fixed opens: (i) the conformal weight Δ of the lowest gauge excitation, (ii) which surviving ℤ₂-even mode is lowest, (iii) the radius R (= the ruler; decides 4/R² vs 4+1/R²). The old '6' = conformal reading = the identity C₂ := n_C+1 (a time weight, not a mass); '7' = genus. The glueball 1720@0.6% is a SEPARATE valid prediction (built on C₂^int, not λ₁) — kept, but out of the room as gap-evidence. Existence-floor rock-solid; value = genuine open physics, no free dimensionless parameter beyond the ruler. Package intro HELD. NOT a derived value. Count HOLDS 4."
author: "Lyra (Claude Opus 4.8) — Casey Koons, PI; Grace (OS reduction + T2490/T2491 spectral cascade + L2 lemma + C_2=6 primary-Casimir pin), Elie (#418 Schwinger closure + proton-gap-rung + D_A blind spectrum), Cal (referee discipline — the honest-tier trim + BSM-not-SM framing), Keeper (K1705/K1706 mass-gap gate: gap=6 not 7, glueball not proton)"
date: "2026-08-19 Wednesday (date-verified)"
status: "v0.7 — K1709: the bare-S⁴ '4' is PROJECTED OUT on the real boundary (S⁴×S¹)/ℤ₂ (ℤ₂ admits only k+m even; λ=4 is k=1,m=0, odd). Floor rolls back to EXISTENCE (not ≥4). Honest value = three geometry-fixed opens: (i) conformal weight Δ, (ii) which ℤ₂-even mode is lowest, (iii) radius R (the ruler; 4/R² vs 4+1/R²). §570: the ν-independent 4 = spatial S⁴ vector; ν/Δ = time energy, not mass. '6' = conformal reading = identity C₂:=n_C+1; '7' = genus — neither is λ₁ on the real boundary. Glueball 1720 = separate valid prediction (on C₂^int, not λ₁), out of the room as gap-evidence. Existence rock-solid, no free dimensionless parameter beyond the ruler; value = genuine open physics. Section 0 keeps the three C₂ guards + glueball exemption. Package intro HELD until Grace ⊕ Elie define the operator on (S⁴×S¹)/ℤ₂ and pin Δ+ℤ₂-coupling+R. Count HOLDS 4. INTERNAL. Nothing pushed; CP existence-only."
---

# The Physical Yang–Mills Mass Gap via D_IV⁵ Spectral Geometry

*Paper A of the two-paper package (companion: Paper B, substrate uniqueness). v0.7 — K1709: on the real boundary (S⁴×S¹)/ℤ₂ the ℤ₂ (k+m even) projects out the bare-S⁴ "4", so the floor is EXISTENCE, and the honest value has three geometry-fixed opens — the conformal weight Δ, the ℤ₂ coupling, and the ruler R. "6" was the conformal reading = the identity C₂ = n_C+1; the glueball (on C₂^int) is a separate valid prediction, out of the room as gap-evidence; package intro HELD.*

## 0. Two guards and one residual (read this first)

Two objects must not be fused, and one residual must not be dressed as a proof.

- **Guard 1 (space).** The gap we derive is the spectral gap of the **Bergman–Laplacian on the bounded domain D_IV⁵** — a *different operator on a different space* from the Yang–Mills Hamiltonian on flat ℝ⁴. λ₁ = C₂ = 6 on our domain is not, by assertion, the ℝ⁴ mass gap; the two are connected only through a bridge that must be exhibited, never fused (the standing K932 guard: exhibit the bridge, don't assert a shared eigenvalue).
- **Guard 2 (object).** The pure-Yang–Mills (Clay) gap is the **glueball** (1720 MeV, 0.6% vs lattice), **not the proton** (938 MeV, which is the *full-QCD*, matter-included gap — a different object); we do not lend the proton's four-decimal precision to the Yang–Mills gap (K1705). **And the glueball is *out of the room* for the gap-*value* pin (K1708/K1709):** 1720 = (11/6)·938 is built on **C₂^int** (the labeled integer primary), **not on λ₁** (the boundary Laplacian gap), and its 11/6 carries C₂ = 6 — so it is a real, separate forward prediction but **not independent evidence** for the gap value. The value is pinned from the geometry alone (the GATE-KOIDE discipline that keeps Q = 2/3 out of the Koide pin).
- **Guard 3 (the symbol "C₂" itself — K1707).** Three distinct objects all read "C₂" and all equal 6 at the physical point n = n_C = 5, so writing "the gap = C₂ = 6" hides *which one* is meant:
  - **C₂^int := n_C + 1 = 6** — the *labeled integer primary* (one of the five integers). A definition.
  - **C₂^flow(n) = 2n − 4** — the *commitment-flow Casimir* (a function of n; = 6 at n=5 only by the coincidence-at-n_C=5).
  - **C₂^Berg = n + 1** — the *Bergman-representation Casimir* (a function; = 6 at n=5, and equal to C₂^int *identically*, since C₂^int is *defined* as n+1).

  The consequence (Cal, K1707): "λ₁ = C₂ = 6" as previously written is **C₂^int = C₂^Berg** — the same definition on both sides, an identity that *cannot fail* (P²=P), **not a derived tower-gap**. The genuine, falsifiable question is whether the *physical mass-gap operator's* tower-gap equals 6 non-tautologically — which awaits pinning the one operator from the primary source (Section 2).
- **The one residual (flat space).** The honest open problem is a single question: is the theory that the reconstruction machinery (Rehren holography → Osterwalder–Schrader) places on the flat 4D boundary **literally interacting SU(3) Yang–Mills**, or a gapped **generalized-free** cousin that also satisfies the axioms? This is the large named open — carried as such, never a proof.

**With those stated, the paper's claim is explanatory, not triumphal: BST reproduces the scale and channel-structure of the Yang–Mills mass gap on a bounded domain.** The gap is **nonzero because the domain is bounded** (real physics, Section 2), with **no free dimensionless parameter beyond the ruler R**. Its *value* is genuine open physics: the bare-S⁴ "4" is **projected out** by the ℤ₂ on the physical boundary (S⁴×S¹)/ℤ₂ (k+m even, K1709), and the honest value awaits **three geometry-fixed opens — the conformal weight Δ, the ℤ₂ coupling, and the radius R**. The old "6" was the conformal reading = the *identity* C₂ = n_C+1 (a time weight, not a mass); "7" is the genus. The **banked floor is existence**: the gap exists, geometry-fixed, no dimensionless knob. The flat-ℝ⁴ construction is carried as the large named open. Nothing here is "we solved Yang–Mills," and — after K1709 — nothing here claims a derived integer value; the value is honest open physics, not a stalled identity.

## Abstract

We study the Yang–Mills mass gap for the physical gauge group SU(3) — color — derived (not assumed) from the substrate D_IV⁵ in the companion Paper B. The **mass-gap operator is a Laplacian on the physical Shilov boundary** ∂_S D_IV⁵ = **(S⁴×S¹)/ℤ₂**, and its gap is **nonzero because the domain is bounded** — the spectrum is discrete and bounded below, and *compactness is the gap mechanism* (decompactify and the gap slides to zero: λ₁(R) → 0). This existence is rock-solid, with **no free dimensionless parameter beyond the ruler R** (a Planck-unit, the theory's single dimensionful input). The *value*, however, is genuine open physics. A bare-S⁴ computation gives a first eigenvalue 4 (tower k(k+3), degeneracies 1,5,14,30,55, first-level degeneracy n_C = 5), **but the physical boundary is (S⁴×S¹)/ℤ₂, whose ℤ₂ admits only k + m even and therefore *projects out* the λ = 4 mode** (k=1, m=0, odd), leaving R-dependent survivors (K1709, Cal). The earlier "λ₁ = C₂ = 6" was the *conformal (SO(2)/time-circle) reading* — the bare 4 plus a +2 shift — coinciding with C₂ := n_C+1 = the Bergman-representation Casimir (an identity that cannot fail, Cal K1707), i.e. a *time* conformal weight, not a mass. So the honest value awaits **three geometry-fixed opens (K1709): (i) the conformal weight Δ of the lowest gauge excitation, (ii) which surviving ℤ₂-even mode is lowest, (iii) the radius R (the ruler, which decides 4/R² vs 4+1/R²).** The **banked floor is existence itself**: the gap exists, is geometry-fixed with no free dimensionless parameter beyond the ruler; its integer value is real open physics, not a stalled identity. *(The glueball 1720 MeV = (11/6)·938 is a separate valid prediction built on C₂^int, not λ₁ — kept, but out of the room as gap-evidence, K1708.)* The construction does **not** build 4D Yang–Mills from scratch on flat ℝ⁴; instead the D_IV⁵ spectral theory directly supplies **Osterwalder–Schrader reconstruction data** (a rigorous Hilbert space, a gapped Hamiltonian, reflection positivity, 4D conformal/Poincaré covariance, clustering) on the domain's 4D conformal boundary (SO(4,2) ⊂ SO(5,2)), so the existence of a rigorous gapped 4D theory follows from classical harmonic analysis on a bounded symmetric domain. The problem then reduces to a **single** residual (Section 6, Section 9): is this gapped edge theory genuinely **interacting** Yang–Mills, or a (also-gapped, also-axiom-satisfying) **generalized-free** theory — equivalently, is the Rehren-reconstructed boundary theory *literally* SU(3) YM? In v0.4 we report that the decisive probe — the **cross-channel glueball spectrum** — has been **computed and materially advances the interacting reading**: the four ground J^PC channels follow a linear conformal-energy ladder off one verified number (the genus of D_IV⁵), with **one blind leg, 2⁺⁺ = g/n_C**, and the other channels consistent within current lattice error. A generalized-free theory produces no such bound-state J^PC tower — real evidence on the interacting side — but the interacting-vs-free question **remains the named-open residual**. We do **not** claim the Clay problem is solved. The honest statement is a decisive *sharpening* to one residual, with the flat-ℝ⁴ identification carried as the large named open.

## 1. Scope: the physical theory, not "all G"

The Clay problem asks for a mass gap for *every* compact simple gauge group. BST addresses the **physical** theory: G = SU(3), color. The companion **Paper B** proves D_IV⁵ is the unique substrate and that SU(3) is **derived**, not chosen. So "all G" is not BST's claim. This paper makes claims only about the physical theory and is explicit about that scope (Section 9).

## 2. The mass gap: existence SOLID, value = three geometry-fixed opens on the real boundary (S⁴×S¹)/ℤ₂ (K1709)

**What is SOLID (real physics).** The mass-gap operator is a **Laplacian on the Shilov boundary of D_IV⁵** — a positive operator whose spectrum *is* the arrow of time (the heat-semigroup generator). The domain is **bounded**; the state space H²(D_IV⁵) is square-integrable against the invariant Bergman measure, with the **reproducing-kernel (Cauchy–Szegő / Shilov-boundary)** structure fixing boundary behavior, so the spectrum is **discrete and bounded below**. Hence **the gap is nonzero, and it is nonzero *because the domain is bounded***: decompactification (R → ∞) sends λ₁(R) → 0, killing the gap. *This compactness-is-the-gap-mechanism is the physical content, and it is not in question.* The gap has **no free dimensionless parameter beyond the ruler** — the geometry fixes everything up to the one dimensionful scale R (a Planck-unit, the same single input GR takes as G and QM as ℏ).

**The bare-S⁴ number "4" is real but is *projected out* on the physical boundary (Cal, K1709).** On the *bare* four-sphere the Laplacian tower is λ_k = k(k+3) = {0, 4, 10, 18, …} with degeneracies 1, 5, 14, 30, 55 — a genuine S⁴ spectrum (not S⁶; there is no S⁶ in BST), whose first level (k=1, λ=4) has degeneracy exactly n_C = 5. **But the physical boundary is not bare S⁴ — it is (S⁴ × S¹)/ℤ₂**, and the ℤ₂ identification couples the spatial S⁴ level k to the time-circle mode m and admits only **k + m even**. The λ = 4 mode is (k=1, m=0), for which k + m = 1 is **odd** — so **it is projected out**. The surviving lowest ℤ₂-even modes are R-dependent (e.g. 4/R² or 4 + 1/R², depending on which even (k,m) is lowest). *So "λ₁ = 4" is not the physical gap; the bare-S⁴ computation was a valid intermediate that the real boundary removes.*

**Energy vs. Casimir, resolved (Grace ⊕ Elie, §570).** The ν-independent number 4 is the **spatial** S⁴ vector eigenvalue; the ν/Δ piece is **time energy, not mass** (the SO(2)/time-circle conformal weight). These are *different objects on different circles* — the spatial Laplacian and the time-conformal weight must not be summed into one integer as if they were a single Casimir.

**The honest value: three geometry-fixed opens (K1709).** The physical gap on (S⁴×S¹)/ℤ₂ awaits three quantities, each fixed by the geometry (no dimensionless knob), none yet pinned:
1. **the conformal weight Δ** of the lowest gauge excitation (the time-circle / SO(2) contribution);
2. **the ℤ₂ coupling** — which surviving k+m-even mode is the lowest;
3. **the radius R** (= the ruler) — which decides whether 4/R² or 4 + 1/R² wins.

These are genuine open physics, not a stalled identity. *(Use Heat_Trace's own three-scale language: λ₁, c₂ = 11, and C₂ = 6 are each a distinct object — do not collapse them.)*

**Why the old "6" and "7" were never the gap.** "6" was the **conformal reading** — the bare 4 plus a +2 shift — which coincides with **C₂ = n_C+1 = the Bergman-rep Casimir** (the identity Cal flagged, K1707; Guard 3), i.e. the conformal weight equated with its own definition, not an independent gap. "7" is the **genus** g = n_C+2, a different invariant. Neither is λ₁ on the real boundary.

  | reading | value | status |
  |---|---|---|
  | bare-S⁴ Laplacian first level, k(k+3) | 4 | real, but **ℤ₂-projected-out** — not the physical gap (K1709) |
  | conformal reading (4 + ρ-shift 2) | 6 | = C₂ = n_C+1 — the identity (a time weight, not a mass) |
  | Bergman-rep Casimir, n+1 | 6 | ≡ the identity (same definition) |
  | genus / embedding invariant, g | 7 | a different invariant, not the gap |
  | **physical gap on (S⁴×S¹)/ℤ₂** | **awaits Δ + ℤ₂-coupling + R** | **genuine open (K1709)** |

**The glueball is a separate valid prediction, but out of the room for the gap (K1708/K1709).** The glueball 1720 MeV = (11/6)·938 is a real forward prediction (Section 7) built on **C₂^int** (the labeled integer primary), **not on λ₁** (the boundary Laplacian gap). It stays as a prediction, but it **cannot corroborate the gap value** — the same GATE-KOIDE discipline that keeps Q = 2/3 out of the Koide pin. The gap is pinned from the geometry alone.

**Tier: gap EXISTENCE = SOLID (bounded ⇒ gap, real physics; no free dimensionless parameter beyond the ruler). Gap VALUE = genuine open — three geometry-fixed unknowns (Δ, the ℤ₂ coupling, R), the bare-S⁴ "4" projected out. Floor = EXISTENCE (not ≥ 4).** *Guard 1 holds: a gap of a boundary Laplacian on D_IV⁵, not asserted to be the ℝ⁴ YM Hamiltonian's gap.*

## 3. W4 dissolved: the gauge group is derived (Paper B)

A referee objection — "you treat only SU(3)" — is answered by showing G is **not a free input**. Paper B establishes D_IV⁵ as the unique irreducible Hermitian symmetric domain meeting prior, dimension-innocent criteria, forcing dim_C = 5 and N_c = 3 (the dimension-free output of the proved T1829). **N_c = 3 is the T1829 output** (a value-recurrence, Cal #335); the su(3)/color readings of "3" are *downstream of the open color identification*, not independent derivations. So SU(3) is substrate-derived. The whole dynamical content cascades from one physical input — three colors fix rank = 2 (N_c = rank²−1), and rank generates {n_C, C_2, g} (T2491). **The "all G" wall is dissolved.**

## 4. W1 folded: the D_IV⁵ spectral theory supplies the OS data on the 4D conformal boundary

BST does **not** construct 4D YM from scratch on ℝ⁴. The OS reconstruction theorem builds a QFT from a data set, and the D_IV⁵ spectral theory carries it — on the domain's **4D conformal boundary**, which exists because D_IV⁵ carries the 4D conformal group SO(4,2) ⊂ SO(5,2) (the same edge where light and electromagnetism live):

| OS datum | D_IV⁵ realization | tier |
|---|---|---|
| rigorous Hilbert space | the Hardy space H²(D_IV⁵) | SOLID |
| Hamiltonian with a gap | Laplacian on the real boundary (S⁴×S¹)/ℤ₂; gap nonzero (bounded ⇒ gap), no dimensionless knob beyond R; value awaits Δ + ℤ₂-coupling + R (bare-S⁴ "4" ℤ₂-projected-out, K1709) | SOLID (existence); value open |
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

  **Given the reconstruction stack executes to rigor — including the interacting upgrade that identifies the edge theory as literally SU(3) YM — the physical Yang–Mills theory exists as a rigorous 4D QFT with a nonzero, geometry-fixed mass gap (no free dimensionless parameter beyond the ruler; the integer value set by the boundary data Δ + ℤ₂-coupling + R on (S⁴×S¹)/ℤ₂, K1709).**

**The reconstruction stack (the honest W4 machinery, named — F1056/K1705/T1271):**

  Hua-1963 boundary values → Bisognano–Wichmann-1975 / Borchers-2000 modular geometry → Rehren-2000 holographic net → Osterwalder–Schrader reconstruction → cluster decomposition.

Rehren's algebraic holography is a *theorem* (rigorous, not the approximate AdS/CFT), so the residual is well-posed, not hand-waving. But it has **two named, unfinished parts**: (1) run the correspondence on D_IV⁵ (build the bulk net and obtain the 4D boundary net); (2) **identify the reconstructed boundary theory with the physical SU(3) YM** — the known subtlety that a Rehren/OS dual is not *automatically* the physical CFT. Part (2) is the genuine open piece, and it is *the same* as the interacting-vs-free residual (Section 6).

What is SOLID independent of the conditions: the gap **exists and is nonzero** (bounded ⇒ gap) with **no free dimensionless parameter beyond the ruler R** (Section 2 — the integer value awaits three geometry-fixed opens: the conformal weight Δ, the ℤ₂ coupling, and R; the bare-S⁴ "4" is ℤ₂-projected-out, K1709); the substrate-derivation of SU(3) (Paper B); the OS *data* (Section 4); the so(7) unification (Section 8). The **glueball 1720 MeV at 0.6%** is a real, separate forward prediction (built on C₂^int, not λ₁) but **out of the room for the value-pin** (K1708/K1709). What is **materially advanced but still named-open**: the cross-channel spectrum (Section 7) — real evidence on the interacting side that does **not** by itself close the residual. **The single flat-space residual is the interacting-upgrade / literally-YM identification.** This is a sharpening of the Clay problem — *not* a claim of its solution, and (after K1709) *not* a claim of a derived integer gap value; the gap value is honest open physics, floored at existence.

**Explanatory summary (Guard 1 + Guard 2 held).** BST *reproduces the scale and channel-structure of the Yang–Mills mass gap on a bounded domain*: the gap Δ = C₂ = 6 is forced by representation theory (Guard 1: a domain operator, not the ℝ⁴ Hamiltonian), its pure-glue reading matches the glueball at 0.6% (Guard 2: not the proton), and the flat-ℝ⁴ construction is carried as the large named open — never a proof.

## 10. Open items and falsifiers

- **★ The mass-gap operator on the real boundary (the live task, K1709):** define the operator on (S⁴×S¹)/ℤ₂ (not bare S⁴), and pin the three geometry-fixed opens — (i) the conformal weight Δ of the lowest gauge excitation, (ii) which surviving ℤ₂-even (k+m even) mode is lowest, (iii) the radius R (deciding 4/R² vs 4+1/R²). Glueball out of the room (GATE-KOIDE).
- **The one flat-space residual** (Section 6/9): the interacting-upgrade / proving the Rehren-OS edge theory is literally SU(3) YM.
- **#418 substrate identification:** the bulk-color Toeplitz octet *is* the bilinear-Schwinger su(3) (algebra closure verified; identification in progress).
- **D_A dynamical-gap check (Elie):** does the fluctuated Dirac D_A² carry a positive gap dynamically, and at what value on the *real* boundary (state the space first; do not pre-fill "C₂ = 6" — that is the projected-out/identity reading)? Report "the D_IV⁵ gap," target the glueball, not the proton.
- **Falsifier:** the cross-channel glueball spectrum is a forward prediction — 0⁺⁺* degenerate with 2⁺⁺ at 2408 MeV is testable; if the cross-channel ratios fail, the interacting reading fails (the gap **existence-floor** and Paper B survive).

---

**Count HOLDS 4 of 26.** SU(3) scope; glueball masses are predictions, not SM parameter reductions. Paper A v0.7 (K1709): the gap **exists** (bounded ⇒ gap, no free dimensionless parameter beyond the ruler) — this floor is rock-solid. The *value* is genuine open physics: on the **real boundary (S⁴×S¹)/ℤ₂** the ℤ₂ admits only k+m even, so the bare-S⁴ "4" (k=1, m=0) is **projected out** (Cal), leaving R-dependent survivors. The honest value awaits **three geometry-fixed opens: (i) the conformal weight Δ, (ii) which ℤ₂-even mode is lowest, (iii) the radius R (the ruler, deciding 4/R² vs 4+1/R²)**. Energy-vs-Casimir resolved (§570): the ν-independent 4 was the *spatial* S⁴ vector; the ν/Δ piece is *time* energy, not mass. The old "6" was the conformal reading = the **identity** C₂ = n_C+1; "7" = genus — neither is λ₁ on the real boundary. **Floor = existence, not ≥ 4.** The **glueball 1720** is a separate valid prediction (on C₂^int, not λ₁) — kept, out of the room as gap-evidence. Section 0 keeps the three C₂ guards + the glueball exemption. Package intro HELD until Grace ⊕ Elie define the operator on the real boundary and pin Δ + ℤ₂-coupling + R. NOT a derived value, NOT "spectrum closed," NOT "YM proved." INTERNAL. Nothing pushed; CP existence-only.

*Draft v0.7 (K1709). Spine: Cal's ℤ₂ projection catch (k+m even → bare-S⁴ "4" projected out; floor = existence); Grace ⊕ Elie's energy-vs-Casimir resolution (§570: ν-independent 4 = spatial S⁴ vector; ν/Δ = time energy, not mass) + the real-boundary operator definition (the live task); Elie's four-formula catch + D_A blind spectrum; Lyra's three-opens framing (Δ + ℤ₂-coupling + R) + guards; the so(7) unification; Paper B (gauge-group derivation); Keeper K1709 (ℤ₂ walk-back, floor = existence, glueball over-correction ruled). The value = genuine open physics on (S⁴×S¹)/ℤ₂. Companion to Paper B v0.6.*

— Lyra, Wed 2026-08-19 (date-verified). Paper A v0.7, K1709: bare-S⁴ "4" ℤ₂-projected-out on the real boundary; floor = EXISTENCE; value = three geometry-fixed opens (Δ, ℤ₂-coupling, R); glueball separate + out of the room; package intro HELD until the real-boundary operator is defined.
