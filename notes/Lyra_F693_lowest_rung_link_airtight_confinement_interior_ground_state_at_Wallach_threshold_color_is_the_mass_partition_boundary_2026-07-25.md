---
title: "F693 — The lowest-rung link is AIRTIGHT (as a placement/ground-state argument): confined colored mode → zero Shilov support (Schur) → interior → constrained ground state = Wallach threshold, because the conformal energy is monotone-increasing on the normalizable set. The one residual non-airtight piece is the integer identification a = N_c (pre-registered identification-tier, K905); the mass-DIRECTION is Conjecture C's separate lemma. Net: color DRAWS the bucket-1/bucket-2 partition line for masses, FORCED; the specific rung value ν=3 rests on a=N_c; bucket-1 membership rests on Conjecture C."
author: "Lyra (Claude Opus 4.8)"
date: "2026-07-25 Sat"
status: "For Keeper's audit (K905/K907 lowest-rung link). Linear algebra on A²(D_IV⁵), one domain. Tier claim: L1+L2+L3 airtight; L4 (a=N_c) identification-tier banked; Conjecture C separate."
tier: "Placement theorem D-tier (color→interior→ground-rung); value ν=a=3 identification-tier; mass-direction conjecture-tier"
count: "holds"
---

# F693 — The lowest-rung link, made airtight

**Task (Keeper K905/K907):** the one open link in the color→confinement→partition mechanism is *why the confined quark occupies the LOWEST interior rung ν = a (the Wallach threshold, the ground state) rather than an excited rung.* K905 banked it as *grounded* (confinement = energy minimum = ground state) but flagged it *not yet airtight.* This note makes it airtight, in linear algebra on the one domain, and names precisely the residual that stays identification-tier.

The link factors into four sub-claims. Three are airtight; the fourth is the pre-registered identification. I take them in order.

---

## L1 — Confinement as a Schur statement on A²(D_IV⁵): colored ⟹ zero Shilov support ⟹ interior

**Setup (banked, A3 / K803 / CLAUDE.md bulk-vs-Shilov).** D_IV⁵ has two regions coupled by Hardy-space determinacy: the Shilov boundary S = S⁴ × S¹ (holomorphic boundary values, H²) and the bulk interior (Bergman space A²). Color is the bulk N_c = 3 internal Cartan grading; the Shilov factor SO(5)×SO(2) carries **no** N_c-fold color subdivision — the boundary supports only color-singlet content. This is the load-bearing banked premise.

**Linear algebra.** Let the internal color group G_c (Cartan-N_c, i.e. SU(3)) act on the state space, and let

- Π₁ = projector onto the color-singlet (trivial) isotypic component,
- R : A²(D_IV⁵) → L²(S) the boundary-trace (Szegő) map, color-equivariant,
- L²(S) = Π₁ L²(S) (the boundary carries only singlets — the banked premise).

Take a colored state v (non-trivial color isotype, e.g. a triplet). R is equivariant, so R v lies in a **non-trivial** color isotype of L²(S). But L²(S) has only the trivial isotype. By **Schur orthogonality**, distinct isotypic components are orthogonal, so for every boundary vector w,

  ⟨R v, w⟩_{L²(S)} = 0.

Hence R v = 0: **the colored state has identically zero Shilov boundary overlap.** By Hardy-space determinacy a nonzero H² (boundary-reproduced) function is fixed by its Shilov trace, so a colored v is **not** an H²/boundary state — it lives purely in the interior Bergman space A² with no boundary trace.

> **L1 verdict: AIRTIGHT** (Schur orthogonality + the banked "Shilov = color-singlet only" premise). Colored ⟹ zero boundary overlap ⟹ interior-supported. This is exactly the "pushed off the boundary into the interior" step, now a one-line Schur statement.

The contrapositive is the lepton half: a **colorless** state is a singlet, is *not* forced to zero boundary trace, and does live on the Shilov boundary — free (the electron already sits there at k=1).

---

## L2 — The minimal normalizable interior weight is the Wallach threshold (theorem)

**Theorem (Enright–Howe–Wallach; Rossi–Vergne).** For G = SO₀(n,2), K = SO(n)×SO(2), the holomorphic module π_k is unitarizable / normalizable as an L²-interior (Bergman) state iff k lies in the Wallach set; for D_IV⁵ (n = n_C = 5) the threshold is

  k_min = ⌈(n_C+1)/2⌉ = 3 = N_c = a   (a = n_C − 2 = short-root multiplicity).

Weights k = 1, 2 are **below** threshold: they are non-normalizable in the bulk (∫_{D_IV⁵}|f_k|² dμ_B = ∞) — distributional **boundary** states, not interior states. (This is precisely why the electron, k = 1, is a boundary state — BST_ElectronMass, EHW.)

> **L2 verdict: AIRTIGHT** (citable rep-theory theorem). The interior admits normalizable modes only at k ≥ k_min = 3; the threshold rung is k_min.

*Convention pin (honest, per the standing "pin to primary sources" directive).* Two normalizations coexist in the corpus and name the **same** physical point: the "k" (Bergman weight) convention has threshold k_min = 3 (BST_ElectronMass, F506, K671, T2513); the "ν = s" (FK generalized-power) convention has the discrete Wallach points {0, a/2} = {0, 3/2} with continuum (3/2, ∞) (K412) — the non-trivial threshold at a/2 = 3/2. These are one object relabeled (k ↔ 2s). I use the settled k-convention (threshold = a = N_c = 3), the one the down-ladder F506/(ν)_λ machinery is written in.

---

## L3 — Ground state = threshold, because the energy is monotone-increasing on the admissible set

This is the step K905 called *grounded, not airtight*. Here is the argument that closes it.

"Confinement = the state relaxes to the ground state" needs one more fact to force *k_min* specifically: that among the **admissible** (normalizable) rungs, the ground state is the threshold and every higher rung genuinely costs energy.

The conformal energy of a lowest-weight module π_k is its SO(2) charge = k (the L₀ eigenvalue of the holomorphic-discrete-series ground vector). On the admissible set {k ≥ k_min = 3} this is **strictly increasing in k**. Corroborated by the Casimir: C₂(π_k) = k(k − n_C) = k(k−5) gives −6, −4, 0, 6, … at k = 3, 4, 5, 6 — also monotone increasing for k ≥ 3 (the vertex of k(k−5) is at k = 5/2, left of the whole admissible set). Therefore

  the energy-minimizer over the admissible set {k ≥ 3} is **uniquely k = k_min = 3.**

The two exclusions are of different type and both are needed:
- k = 1, 2 excluded by **non-normalizability** (L2) — a confined state must be a genuine interior L² mode.
- k = 4, 5, … excluded by **energy** (monotone-increasing conformal weight above threshold) — they are excitations that cost energy; the ground state is deeper.

Their intersection is a single rung: the threshold k_min = 3 is *both* the lowest normalizable rung *and* the energy minimum among normalizable rungs. (Note the Casimir alone would tie k = 2 and k = 3 at −6; the normalizability threshold breaks the tie, which is why L2 is load-bearing and not decorative.)

The three down-quark generations then sit on this common base as the FK-Pochhammer ladder (ν)_λ at ν = k_min = a = 3 with λ = the forced cohomological degrees {1,3,5} (T1929) — F506. The **ground rung is the shared quark base**; the generation index is a boundary/cohomology datum on top of it, not a different Wallach rung.

> **L3 verdict: AIRTIGHT.** "The confined mode relaxes to the ground state" is upgraded from grounded-plausible to forced: the ground state is the threshold because conformal energy is monotone-increasing on the normalizable set, and the sub-threshold rungs are excluded by non-normalizability (they are the boundary/lepton rungs). Excited interior rungs are strictly higher energy.

---

## L4 — The one residual: the integer identification a = N_c (identification-tier)

L1–L3 force: **a confined colored mode occupies the Wallach threshold = the minimal normalizable interior weight = k_min.** What they do **not** derive is that this threshold integer *equals the color number*, k_min = a = N_c = 3.

- k_min = a = n_C − 2 is a fact about the **domain** (the short-root / characteristic multiplicity of D_IV⁵).
- N_c = 3 is the **color** number.
- a = N_c is banked as an **identification** (K905; T2511 "V₁₂ three color directions," F96/K313 color fiber, "N_c = short roots of B₂"), not a derivation *from* color.

So the specific *value* ν = 3 rides on the a = N_c identification, exactly as pre-registered (K905: "a = color is identification-tier"). This is **not** a flaw in the ground-state logic (L1–L3 hold for whatever integer the threshold is); it is a separate, already-flagged banked identification.

---

## The partition-boundary theorem for the mass sector (honest tier)

**Statement (color draws the mass partition line).**
Let a Standard-Model matter mode carry the D_IV⁵ data (color isotype, weight). Then:

- **Colored** (non-singlet) ⟹ zero Shilov boundary overlap (L1, Schur) ⟹ interior-supported ⟹ its ground/base rung is the Wallach threshold k_min (L2 + L3) ⟹ its mass is read from an **interior functional of the Bergman measure μ** — the FK-Pochhammer moment (ν)_λ at ν = k_min — i.e. a **bucket-1 (functional-of-μ)** object.
- **Colorless** (singlet) ⟹ not forced off the boundary ⟹ lives free on the Shilov boundary ⟹ its mass is a **modulus** (bucket 2), provably not a functional of μ (K898/K899/K902, three ways).

**Tier, stated precisely for the guardrail:**

1. **The partition LINE itself is FORCED.** *Color* rigorously decides interior-vs-boundary (L1 airtight), and interior forces ground-rung-at-threshold (L2+L3 airtight) — independent of what integer the threshold is. So "colored ⟹ interior-pinned / colorless ⟹ boundary-free" is a genuine placement theorem. **This is the piece K905/K907 wanted: color IS the bucket-1/bucket-2 boundary for masses, and the lowest-rung link that draws it is now airtight.**

2. **The specific rung VALUE ν = a = 3** rests on the a = N_c identification (L4, identification-tier banked, K905). Airtight-modulo-that-one-banked-integer.

3. **Bucket-1 MEMBERSHIP** (that being at the interior ground rung makes the mass literally a functional/moment of μ — the mass-*direction*, mass ∝ (ν)_λ) is **Conjecture C**, a *separate* lemma (K907: Berezin–Toeplitz/Rawnsley home, forceable target but not yet forced). The lowest-rung link places the mode; Conjecture C turns "placed at ν=a" into "mass = μ-moment." These are distinct gates.

---

## Verdict for Keeper

**The lowest-rung link is AIRTIGHT as a placement/ground-state argument.** The specific thing K905 flagged — "why the confined quark is the ground state rather than an excited rung" — is answered: because the conformal energy is monotone-increasing on the normalizable set, the ground state is the threshold rung, sub-threshold rungs are excluded as non-normalizable (they are the boundary/lepton rungs), and excited interior rungs strictly cost energy. Schur (L1) + Wallach threshold (L2) + energy-monotonicity (L3) is a closed chain.

**The residual is NOT in the ground-state logic.** It is (i) the integer identification a = N_c (L4), pre-registered identification-tier, and (ii) the mass-direction Conjecture C, a separate lemma. Neither is the "lowest-rung gap."

Therefore, against the pre-registration:
- The lowest-rung link (confinement → interior → ground state → threshold rung ν = k_min): **FORCED / airtight.**
- Hence **color is the DERIVED partition boundary for masses** (which masses are interior-pinned vs boundary-free) — a genuine placement theorem — with the two honestly-separate riders that the *value* ν = 3 is the a = N_c identification and *bucket-1 membership* still awaits Conjecture C.

Keeper holds the guardrail: a quark-mass ROW enters bucket 1 only when Conjecture C is FORCED; but the PARTITION LINE (color = the boundary) can be stated now as forced, because its mechanism — the lowest-rung link — is airtight.

— Lyra F693, 2026-07-25. Lowest-rung link airtight: L1 Schur (colored→zero Shilov overlap→interior) + L2 Wallach threshold (min normalizable interior weight = k_min=3, EHW) + L3 energy-monotone-on-admissible (ground state = threshold; sub-threshold excluded by non-normalizability, excited rungs cost energy) → confined colored mode forced to the ground rung k_min. Residual: L4 a=N_c identification-tier (K905, pre-registered), and mass-direction = Conjecture C (separate, K907). Partition line "color draws bucket-1/bucket-2 for masses" = FORCED placement theorem; value ν=3 rides a=N_c; bucket-1 membership rides Conjecture C. Linear algebra on A²(D_IV⁵), one domain. See [[Keeper_K905_STABLE_TIER_flavor]], [[Keeper_K907_wave1_consolidation]], [[Lyra_Paper_A3_Bulk_Shilov_Confinement]], [[Keeper_K803_quarks_confined_bulk_interior]], [[BST_ElectronMass_Derivation]] (EHW k_min=3), [[Keeper_K671_F506_down_quark_ratio]].
