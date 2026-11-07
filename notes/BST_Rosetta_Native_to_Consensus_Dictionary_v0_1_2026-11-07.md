---
title: "BST Rosetta v0.1: native terms to consensus language"
date: 2026-11-07
status: DRAFT v0.1 for Keeper ratification. Status tags are proposals, not rulings.
authority: notes/BST_PRESENTATION_STATE_BLOCK.md wins over every other file, this one included.
companion: notes/BST_Clarification_Scalar_Spectrum_Goldstone_and_B_Anomaly_Corollary_2026-11-07.md
---

# BST Rosetta v0.1: native terms to consensus language

## Why this exists

BST is easiest to think in its own vocabulary and hardest to referee in it. The plan
(Casey, 2026-11-07) is to define BST natively first, then publish in consensus language.
This file is the bridge between the two. Three rules make it work:

1. **One source of truth.** The native definition lives here once. External papers
   translate from this table and do not improvise. If a paper needs a term that isn't
   here, add a row first.
2. **The translation is a test, not packaging.** If a native claim can't be stated in
   consensus terms, either it is genuinely new (status NEW, so say so in the paper) or it
   is wrong. Two errors this session (Goldstone-needs-topology; electron-as-mediator) were
   caught only at the translation step.
3. **The status column is the product.** It tells a referee exactly where BST matches
   known mathematics, where it borrows an analogy, and where it claims something new.

## Status key

| Tag | Meaning | What an external paper does |
|---|---|---|
| **EXACT** | The native term names a standard object with the standard meaning. | Use the standard term. The native term goes in parentheses at most. |
| **ANALOG** | It resembles a standard concept but isn't identical. | Use the standard term plus one sentence on how BST's version differs. |
| **NEW** | No standard counterpart. This is where BST claims something. | Define it from scratch, state its tier, and give its falsifier. |
| **INTERNAL** | A working-hypothesis or team-process term. | Keep it out of external text (Cal Calibration #13). |
| **CONFLICT** | The corpus uses it in incompatible ways. | Resolve it before any external use. See the conflict list. |

---

## A. The object and its integers

| Native term | Precise mathematical object | Consensus physics/math term | Status | Notes |
|---|---|---|---|---|
| D_IV⁵ / APG | SO₀(5,2)/[SO(5)×SO(2)]; Cartan type-IV bounded symmetric domain ("Lie ball") in ℂ⁵ | Hermitian symmetric space of noncompact type, rank 2 | EXACT | APG is BST's name for the object. Use "type IV domain" for physicists and "Lie ball" for analysts. |
| rank = 2 | Real rank of the symmetric space | rank | EXACT | |
| n_C = 5 | Complex dimension | dimension | EXACT | |
| N_c = 3 | Root multiplicity a = n − 2 of the type IV domain (the "characteristic multiplicity") | number of quark colours | NEW (identification) | The math is exact. The identification with colour is numerical, and the bridge to a mechanism is proved absent (state block, F4). Say this every time. |
| g = 7 | p + q = 7, the dimension of the defining representation of SO(5,2) | none | CONFLICT | The genus of D_IV⁵ is **5**, not 7 (state block, swept in September). The seed table still says "Genus" and still has a "genus coincidence" derivation chain. |
| C_2 = 6 | rank × N_c; called "a Casimir eigenvalue" | none | ANALOG, needs specification | State which Casimir operator, on which representation, and in which normalization. Without that, a referee reads it as a relabel of rank × N_c. |
| N_max = 137 | N_c³·n_C + rank | identified with α⁻¹ | NEW (identification) | "Channel capacity" borrows Shannon's word without Shannon's definition. Avoid that phrase externally unless the capacity is computed. |
| The ruler | One dimensionful input (Planck units; m_e is the interior unit) | choice of units / one mass scale | EXACT | |
| One input | Colour count selects the object | one measured dimensionless input | EXACT | bst_this_is.md still says "BST has none" under "Not a model". Reword to match "one input". |

## B. Geometric objects BST uses

| Native term | Precise mathematical object | Consensus term | Status | Notes |
|---|---|---|---|---|
| Bergman kernel K(z,w) | Reproducing kernel of the weighted Bergman space A²(D_IV⁵) | Bergman kernel | EXACT | Vol(D_IV⁵) = π⁵/1920 in the program's normalization. State that normalization. |
| Bergman projection | Orthogonal projection L² → A² | Bergman projection | EXACT | One of four meanings of "projection" (see E). |
| Šilov (Shilov) boundary | (S⁴ × S¹)/ℤ₂ (state block, 2026-10-07) | Shilov boundary | EXACT, with CONFLICT | The seed still says S⁴ × S¹, which is the orientation double cover. **Proposed external phrasing (Lyra to verify):** the Shilov boundary of the type IV domain in ℂⁿ is the conformal compactification of (n−1,1) Minkowski space. For n = 5 that is the compactification of **4+1** dimensions. Physical 3+1 spacetime then needs the SO(5,2) ⊃ SO(4,2) step (F242), so "the Shilov boundary is spacetime" needs that qualifier. |
| Szegő map / boundary trace | Map from A²/H² to L²(Shilov), K-equivariant | Szegő projection, boundary values | EXACT | |
| Wallach set | The set of parameters for which the weighted Bergman space exists as a unitary representation (Faraut–Korányi) | Wallach set | EXACT | |
| "Below the Wallach set" (electron, k = 1) | A parameter outside the Wallach set: not a normalizable bulk state; a boundary value | none | NEW (physical reading of exact math) | Pairs with "proton = first bulk state". See conflict C6. |
| K-type | An irreducible representation of K = SO(5)×SO(2) appearing in a representation of G | K-type | EXACT | |
| λ₂ = 0 / two-row sector | Second component of a K-type's highest weight; zero means spherical (one-row) | none | EXACT math, ANALOG physics | The identification of λ₂ > 0 with SU(3) colour is imported (#108), not derived. |
| Discrete series / Plancherel measure | Harish-Chandra's discrete series; spectral decomposition of L²(G/K) | discrete series; Plancherel measure | EXACT | "The mass spectrum IS the Plancherel measure" is a NEW identification with its own tier. |
| Formal degree d(ν) | Harish-Chandra formal degree | formal degree | EXACT | |
| Strata (bulk / intermediate / Šilov) | Korányi–Wolf boundary orbits; rank + 1 = 3 of them | boundary orbit stratification | EXACT math | "Strata = generations" is NEW; the state block lists it as Derived. |
| B₂ root system | Restricted root system of D_IV⁵ | restricted roots | EXACT | |
| Heat trace R(k) | Seeley–DeWitt coefficients of the heat kernel on D_IV⁵ | heat-kernel coefficients | EXACT | |
| Toeplitz operator per sector | Toeplitz operator on H²(D_IV⁵) with a "condensate" as its symbol | Toeplitz operator | EXACT math, ANALOG physics | "Symbol = condensate" inherits the condensate wording problem (C4). |
| Celestial boundary (S⁴ direction + phase) | A point of the Šilov boundary | none | ANALOG, use with care | In current physics, "celestial sphere/holography" means S² at null infinity of 3+1 spacetime. Use "Šilov boundary point" externally. |

## C. Particles and the spectrum

| Native term | Precise object | Consensus term | Status | Notes |
|---|---|---|---|---|
| Electron = Šilov-boundary state | k = 1, sub-Wallach boundary value | electron | NEW | See C6: K1358 says the reverse. |
| Proton = first bulk state | First holomorphic discrete-series level | proton | NEW | m_p = 6π⁵m_e, listed as Derived. |
| Leptons on the boundary, quarks interior | Schur: the boundary map carries only spherical (λ₂ = 0) K-types, so two-row states have zero boundary overlap | colour confinement of quarks; leptons colour-neutral | NEW | Airtight as math (L1). The physical reading is a claim. The seed's "Particles live on this boundary, not in the bulk" contradicts it (C7). |
| Three generations = rank + 1 strata | Korányi–Wolf orbits | three fermion generations | NEW (Derived per state block) | |
| m_ν1 = 0 | Rank-2 geometric Majorana matrix has a 1-dimensional kernel | lightest neutrino massless | NEW (Derived) | |
| Geometric Majorana mass term | Explicit rank-2 form; no dynamical field | explicit ΔL = 2 Majorana mass | ANALOG | Replaces "Majorana condensate" (C4). Explicit breaking means no Majoron. |
| One Higgs = degree 1 (cross-parity rule) | Selection rule forcing a bidiagonal Yukawa texture | Yukawa texture / one Higgs doublet | NEW | |
| Yukawa ceiling | Cauchy–Schwarz on a normalized Born overlap, so \|y\| ≤ 1 and m_f ≤ v/√2 = 174.1 GeV | none exact | NEW | Similar in spirit to perturbative-unitarity bounds on Yukawa couplings, but derived differently. Say so. |
| Flavour-universal charged current | The current is the identity on generation space, the partial-isometry condition (R51/R52) | lepton/quark universality of the weak coupling; CKM unitarity | EXACT | This is the SM statement. BST's contribution is deriving it, not changing it. |
| Proton = codeword, neutron = 1-error | Hamming(7,4,3) = (g, rank², N_c) | none | INTERNAL | Keep out of physics papers until it computes something. |

## D. What is forbidden

| Native term | Consensus term | Status | Notes |
|---|---|---|---|
| Five-Absence | Excluded beyond-SM states | CONFLICT (count) | The one-pager lists five (no GUT, proton decay, monopoles, sterile ν, SUSY). The state block lists six, adding no W_R/$Z'$. Rename to "the Absences", or fix the count (C8). |
| No W_R / no $Z'$ | No right-handed charged current or extra neutral gauge boson | EXACT | Derived (F582). |
| No sterile neutrinos | No light sterile neutrino | CONFLICT | F583/F584 use exactly two ν_R (C1 in the companion note). |
| Only dynamical scalar = Higgs | One Higgs doublet | EXACT | CONDITIONAL until the Higgs rep-checks close. |

## E. Process vocabulary: the hardest to translate

These words carry most of BST's interpretation, and they are where referees will stop.

| Native term | Corpus meanings found | Consensus nearest | Status | Proposal |
|---|---|---|---|---|
| **Projection** | (1) Bergman projection L² → A²; (2) Szegő projection to the boundary; (3) "the observable universe is the 3D projection of a 2D substrate" (seed); (4) "projection = substrate emission"; (5) Casey 2026-11-07: a state's component in another sector, as in neutron decay | (1), (2) EXACT; (5) projection onto a Fock sector / virtual component; (3), (4) none | CONFLICT (five meanings) | Split into named terms: P_B (Bergman), P_S (Szegő/boundary), "sector projection" for (5). Keep (3) and (4) INTERNAL until defined as maps. |
| **Commit / commitment** | Szegő projection to a boundary point; Wallach-drop ∘ T754-keep; positive-root traversal; one tick of substrate activity; "the sharp finite/divergent sort" | Nearest: measurement, state reduction, registration of an outcome | CONFLICT (several definitions) | Choose one operator definition. The Szegő one is the most precise. Prove the others equivalent or retire them. Externally, use "boundary registration (BST's commit)" plus that definition. |
| **Record** (commitment-record rule) | A particle holds a permanent record iff it is the lightest carrier of a superselected charge. Classes: RECORD / DIE / DRIFT / NO-RECORD | Stability of the lightest charged particle by charge conservation | ANALOG | Exact for the electron (Q is superselected). For the proton, the SM treats B as accidental. BST's claim that B is topological is the NEW part. |
| **Residue** | What balances the books in a transition (e.g. the ν̄ in neutron decay) | Pauli's 1930 neutrino, invented to carry missing energy | ANALOG | Historically exact. Use it. |
| **Mediator** | Carrier of a transition | Exchanged gauge boson (W in β decay) | EXACT if used that way | Note: under the record rule the electron is a record, not the mediator. |
| **Substrate** | The computational structure whose output is physics | none | INTERNAL | The register already rules it out for external text. |
| Absorption → commitment → emission | The substrate's one-way cycle | none | INTERNAL | |
| Tick | ℏ/E for the energy at hand (K1920) | Quantum time scale ℏ/E | EXACT | The Koons tick (t_Planck·α^36 ≈ 10⁻¹²⁰ s) is **retired** but still in the seed (C9). |
| Contact graph | The graph whose configuration space is D_IV⁵ (seed) | none | INTERNAL | |
| Observer / self-referential observation | Structural role of α = 1/137 | none | INTERNAL | |

## F. Method vocabulary

| Native term | Meaning in BST | Consensus term | Status | Notes |
|---|---|---|---|---|
| Tiers | D/I/C/S (CLAUDE.md); Proved/Derived/Identified/Conditional/Structural/Fitted/Runner (K962); Tier 1/2/3 (seed) | levels of evidence | CONFLICT (three vocabularies) | Pick K962 (the most complete) and map the other two onto it once (C10). |
| AC depth / AC(0) | Derivation depth ≤ 2 counting steps | Borrowed from circuit complexity's AC⁰ (constant depth, unbounded fan-in) | ANALOG, risky | Complexity theorists will read AC⁰ literally. Externally, say "derivation depth" and define it. |
| Bucket 1 / Bucket 2 / runner | Bucket 1: a functional of the one measure μ (derived core). Bucket 2: a free boundary modulus (support-free). Runner: scale-dependent | derived quantity / free parameter / running coupling | ANALOG | A clean three-way partition. Translates well. |
| Radial norm on the one ruler | A dimensionless observable computed as a representation norm, times the single scale | dimensionless ratio | ANALOG | |
| RFC / vacuum subtraction ("subtract 1") | Empirical rule: BST product − 1 improves a bare formula | none | NEW | Externally this reads as a correction chosen after the fact. Present it with its tier and how it was pre-registered, or not at all. |
| θ₁₃ rotation, 42 vs 120 correction scales, syndrome decoding | Correction rules | none | NEW | Same caution as RFC. |
| Born = Bergman | K(z,z) = Σ\|φ_k(z)\|² | Born rule | ANALOG | The math identity is exact. Equating it with the Born rule is an interpretation; say so. |
| Ward identity = K*K = K | Idempotency of the reproducing kernel | Ward–Takahashi identities | ANALOG, weak | A referee will ask which Ward identity and for which current. Keep it internal until one is derived. |
| Confinement = Hamming distance 3 | Minimum distance of Hamming(7,4,3) | colour confinement | INTERNAL | The state block says the geometry "forces the kinematics and none of the dynamics". Confinement is dynamics, so this conflicts (C11). |
| Fired and lost | A certified failed prediction (Section E of the falsifier register) | falsified prediction | EXACT | Rare in the field and worth advertising. |
| Pre-registered | Outcomes partitioned in code and hashed before the data | pre-registration | EXACT | |

---

## Conflicts found while building the table (for Keeper)

Numbering continues from C1–C6 in the companion clarification note.

| # | Conflict | Files | Proposed resolution |
|---|---|---|---|
| C7 | "Particles live on this boundary, not in the bulk" vs "proton = first bulk state" | data/bst_seed.md vs the Wallach notes | Rewrite the seed line: leptons are boundary values; hadrons are bulk states. |
| C8 | Five-Absence names five; the state block forbids six | one-pager vs state block | Rename it "the Absences", or add W_R/$Z'$ to the one-pager as #6. |
| C9 | The Koons tick (10⁻¹²⁰ s) is retired but still listed as the substrate clock | bst_this_is.md (retired) vs bst_seed.md (live) | Update the seed to ℏ/E (K1920). |
| C10 | Three tier vocabularies | CLAUDE.md, K962, seed | Adopt K962 and publish one mapping row. |
| C11 | "Yang–Mills mass gap = proton mass" and "confinement = Hamming distance" vs "the geometry supplies no mass gap … none of the dynamics" | seed vs state block | Retire both seed lines, or downgrade them to INTERNAL/Structural with the state-block caveat. |
| C12 | α⁻¹ = 137 "(Wyler integral)" as Master Formula 1 vs "α identified; the Wyler reading certified dead (E1)" | seed vs bst_this_is.md / state block | Rewrite Master Formula 1 as "Identified: 137-class expressions; Wyler reading fired (E1)". |
| C13 | Cabibbo 2/√79 (seed) vs banked 1/√20 (T2530); the curated table also carries a third λ (K1801) | seed, Guide Vol2 Ch02 | Already Lyra's decision (K1801). The seed should follow it. |
| C14 | g = 7 called "Genus" | seed table and derivation chain vs state block (genus = 5) | Finish the September sweep in the seed. |
| C15 | "Projection" has five meanings; "commit" has several | many | Section E proposal: named operators. |

**A pattern worth noting:** most of C7–C14 sit in `data/bst_seed.md`, which CLAUDE.md tells every new CI to load first as "the entire theory kernel." The seed is dated May 10 and predates the September register rewrite. It is currently the main source of stale native definitions entering new sessions. Re-syncing it to the state block is the highest-leverage fix on this list.

## Statements in this file that need verification before external use

- **Shilov boundary as compactified Minkowski space.** The Shilov boundary of the type IV domain in ℂⁿ is (S^{n−1} × S¹)/ℤ₂, the conformal compactification of (n−1,1) Minkowski space. For n = 5 that is 4+1 dimensions. This is standard, but it is cited here from memory. Lyra to confirm against Faraut–Korányi or Hua.
- **The root multiplicity a = n − 2 = 3 for the type IV domain.** Standard; confirm the corpus uses the same convention.
- **The AC⁰ caution.** It is about how readers will take the name, not about BST's mathematics.

## How to extend

Add a row whenever a native term appears in a paper draft. Fill all five columns. If the
consensus column is "none", the status is NEW or INTERNAL. Nothing ships externally with
status CONFLICT.

## Applied 2026-11-07 (Casey's GO, 16:22)

- **C7, C9, C11, C12, C13, C14:** fixed in `data/bst_seed.md`, which is now re-synced to the
  state block. Each changed line carries "(this line said … until 2026-11-07)".
- **C8:** the Five-Absence one-pager now names W_R/$Z'$ as a derived sixth absence. The title is
  kept.
- **C10:** the seed now points to K962 as the canonical tier system and maps D/I/C/S onto it.
  CLAUDE.md is unchanged.
- **Also fixed:** `data/bst_this_is.md` now says "Not a model: tunes nothing; one input, one
  ruler", has the 50-quantity count, and has the verify_bst tally as run today (45/46; 17
  EXACT, 28 PASS, 1 WARN; 4 fired/retired excluded).
- **Still open:** C15 (named operators for "projection" and "commit") is a team decision, not
  an edit. The Šilov boundary / 4+1 Minkowski statement still needs Lyra's check.

- **C16 (found and applied 18:14):** ν₁ was called "the Z₃ Goldstone mode" in
  `data/bst_predictions.json` (pred_003) and `data/bst_particles.json`. Discrete symmetries have
  no Goldstone modes. Both now read "null direction of the rank-2 geometric Majorana matrix,
  protected by Z₃". Use that phrase externally.
