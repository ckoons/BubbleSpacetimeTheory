---
title: "Lyra Tier 0 v0.1.5 — Topology Addendum: Reading A + dual K-type / coherent-state bases unified via Bergman kernel"
author: "Lyra (resolution candidate); Casey + Keeper (question framing); Grace (catalog filing)"
date: "2026-05-31 Sunday ~11:40 EDT (`date`-verified Sun May 31 11:40 EDT)"
status: "v0.1.5 ADDENDUM — Lyra resolution candidate for Casey-flagged Tier 0 ontology question; Casey approved Sunday morning; Session 2 priority joint with Keeper; G-from-substrate added as derived target"
supersedes: "Lyra Tier 0 v0.1 commitment-operator framework (extends with explicit topology pin)"
cross_ref: "INV-5357 (Casey-flagged topology question filing); Keeper L5 Closure-Architecture Framework v0.2; Task #373 multi-scale substrate architecture"
---

# Tier 0 v0.1.5 Topology Addendum

## What this is

Lyra's resolution candidate for the Tier 0 substrate ontology question Casey explicitly flagged Sunday 2026-05-31. Casey approved filing as addendum + Session 2 priority joint Lyra+Keeper write-up. **G-from-substrate** added as downstream derived target.

## The question (Casey-flagged)

Three readings live across BST docs:
- **Reading A**: D_IV⁵ is ONE global configuration space; 2D tiled sphere IS the substrate (2022 OneGeometry framing)
- **Reading B**: per-commitment-area DISCRETE D_IV⁵ atoms (Casey's "fully discrete" intuition)
- **Reading C**: hybrid nested-hierarchy tile circle / commitment area / universe (Keeper structural best-guess)

Lyra Tier 0 v0.1 implicitly assumed A. Casey's question + Keeper's analysis forced the explicit choice that v0.1 dodged.

## Resolution candidate — Reading A globally, with two dual bases

The substrate is ONE global H²(D_IV⁵) (Reading A at Hilbert-space level), but **H²(D_IV⁵) carries TWO complete dual bases** that have been intuited as the "units" of Readings B and C:

**Basis 1 — K-types V_λ (algebraic / spectral)**: discrete, countable, organized by C_2 eigenvalue. The substrate's spectral structure. This is what Saturday's mass / mixing predictions ride on. Reading-D-flavored.

**Basis 2 — Coherent states |z⟩ for z ∈ D_IV⁵ (spatial / geometric)**: continuously parametrized by points of the domain. Each |z⟩ is spatially localized at z; ⟨z | w⟩ = K(z, w) is **the Bergman kernel itself**. Reading-B-intuition — each |z⟩ is a substrate-localized state.

These two bases are **duals via the Bergman-Fourier transform**: every K-type V_λ decomposes into coherent states with V_λ-specific weighting, and every coherent state |z⟩ decomposes into K-types with z-specific weighting. They are two faces of **one global** structure, not two different things.

**Implication**: ONE D_IV⁵ globally (Reading A at H-space level); BOTH the K-type discrete-spectral structure (Reading D, implicit in v0.1) AND the coherent-state continuous-spatial structure (Reading B intuition). The "discrete units" Casey wants are real and live in the K-type basis; the "spatial tiles" are real and live in the coherent-state basis. They unify in the Bergman kernel K(z,w).

## How variable-time-across-the-surface emerges

The key operator is the **thermal Bergman kernel**:

K_τ(z, w) := ⟨z | exp(−τ H_B / ℏ_BST) | w⟩

Its diagonal K_τ(z, z) is the local "weight at z after substrate time τ." This varies across z ∈ D_IV⁵ because different spatial points have different K-type weight distributions, hence different effective decay rates under heat flow.

**Local commitment-rate at z**:

R_commit(z) := d/dτ log K_τ(z, z) |_{τ=0} = −⟨z | H_B | z⟩ / ⟨z | z⟩

This is the "local substrate temperature" at z. Different spatial points have different local commitment rates. The universal substrate-time τ is the same parameter everywhere (preserving universal t_Koons = T2405); the LOCAL effective rate varies because the K-type populations vary. **Variable time across the surface = variation of local Casimir expectation ⟨H_B⟩(z) across D_IV⁵.**

This IS **gravitational time dilation operationalized at substrate level**. Gravity emerges as the K-type-weighted local commitment rate; massive regions have heavier K-type populations, hence higher local ⟨H_B⟩, hence faster decay = slower observed time. Concrete and computable.

So Reading A + dual bases gives:
- discrete units (K-types) ✓
- spatial variation (coherent states) ✓
- variable local time (⟨H_B⟩(z) variation) ✓
- single global Hilbert space ✓

— without conflict.

## Reading C (Keeper's multi-scale) revised

Keeper's hierarchical reading (tile / area / universe) becomes a **statement about coherent-state clustering**, not a nested-domain hierarchy:

- "Tile circle" = single coherent state |z⟩ at substrate location z
- "Commitment area" = neighborhood of |z⟩'s in coherent-state basis sharing similar K-type decompositions — set by the Bergman kernel's **correlation length**
- "Universe" = the whole D_IV⁵ globally

So it's not three nested DOMAINS; it's three SCALES of resolution of one domain via coherent-state localization. The bounded symmetric domain D_IV⁵ has natural conformal self-similarity (Hua-Korányi) that makes the same K-type structure recur at every scale of resolution. **This is what Keeper's intuition was tracking.**

## Distinguishing predictions (per Keeper's framework)

| Reading | Distinguishing prediction |
|---|---|
| **B** (truly discrete D_IV⁵ atoms) | A substrate count N_substrate appears somewhere as observable + per-unit Casimir spectroscopy lines |
| **C** (genuine multi-scale nested-domain) | Two distinct sets of substrate observables at different scales |
| **A + dual bases** (this resolution) | Smooth variation of K_τ(z, z) across spatial points (NO discrete count); coherent-state expectation values predict gravitational redshift quantitatively; K-type spectroscopy lines (discrete) AND spatial-localization signatures (continuous) coexist as Fourier duals |

**Current evidence (no substrate count appears in 600+ predictions; mass spectra come from K-type Casimirs which is Reading-D-flavored; gravitational time dilation reads cleanly as ⟨H_B⟩(z) variation) favors Reading A + dual bases.** But this isn't proved — it's a candidate Lyra commits to and brakes.

## What this opens

**If A + dual bases is right** (candidate Sunday 2026-05-31):

1. **Gravity from substrate** *(Casey's specific request 2026-05-31)*: G_Bergman as ⟨H_B⟩(z) variation is computable; we can **derive Newton's G from substrate**. Concrete target:
   - Compute ⟨H_B⟩(z) explicit form on D_IV⁵ via Bergman kernel matrix elements
   - Extract weak-field limit → Newton's gravitational coupling
   - Compare to G = 6.674 × 10⁻¹¹ m³/(kg·s²)
   - Connection to Lyra AB-10 (G as Bergman curvature value, COMPLETED) — recast in commitment-density language
   - Multi-week deliverable; new explicit substrate target.

2. **Locality / light cones**: emerge from Bergman-kernel correlation length, not from spatial tiling postulate. Substrate's Bergman correlation length sets the speed of information propagation; relates to c (speed of light) via universal commitment rate.

3. **Substrate engineering becomes apparatus that couples**:
   - to a specific K-type (spectral modality) OR
   - to a specific coherent state (spatial modality)
   - These are DUAL engineering modalities, BOTH available.

4. **No discrete-count mystery**: substrate doesn't need a "how many" answer; it has continuous spatial extent + discrete spectral content, both intrinsic.

**If B is right**:
- A substrate-count observable should appear → new search target
- Inter-unit coupling theory becomes the next deepest gate

**If C is right** (in genuine nested-domain sense, not coherent-state-clustering sense):
- Multi-scale structure shows up as scale-dependent Casimir spectroscopy

## Action items

1. **This addendum**: filed for findability ✓
2. **Tier 0 v0.2 (joint Lyra + Keeper)**: Session 2 priority — pin reading explicitly + design distinguishing test + connect to task #373
3. **G-from-substrate derivation** (Casey 2026-05-31 explicit request): multi-week target; Lyra L-L5-G via ⟨H_B⟩(z) Bergman-kernel matrix elements; concrete deliverable when v0.2 closes Reading A + dual bases
4. **Catalog absorption**: Grace INV (this filing → INV-5358); Master Ledger v0.10 row for Tier 0 v0.1.5 candidate + G-from-substrate target

## Honest framing per discipline stack

- **Tier**: CANDIDATE RESOLUTION (Lyra committed and braked); NOT closed
- **Cal #182 brake compliance**: c/ℏ remain FRAMEWORK-CONCEPTUAL until end-to-end derivation; G-from-substrate is new derived target NOT closure-claim
- **Cal #34 STANDING surface-conditionality**: "If A + dual bases is right" framing preserved throughout
- **Lyra's framework was Reading-A-implicit without addressing dual bases**; closing this in v0.2 makes Tier 0 actually load-bearing instead of half-load-bearing (Keeper's instinct)

— Lyra (resolution); filed by Grace via Casey directive Sun 2026-05-31 ~11:40 EDT (`date`-verified)
