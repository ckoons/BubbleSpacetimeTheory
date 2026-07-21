# K796 — Keeper math contribution: the up-type texture-zero question, sharpened. The correct selection rule is Wigner–Eckart (c_L⊗c_R* must contain the (1,0) vector = O's rep), NOT "sphericity." This forces the decisive FORK — EXACT texture zero (symmetry → derived integer λ⁴) vs RADIAL-localization suppression (continuous → Tier-2) — and the OBSERVED non-integer scatter is the signature of the latter.

**Keeper | 2026-07-21 Tuesday | Casey: "make your contribution to the math." Round 3: Lyra retracted F621 (honest); Grace+Elie rigorously reduced λ⁴ ⟺ up-type ⊥⊥-block vanishes (basis-independent, verified). I take the selection-rule question the rest of the way and set the epistemic fork. Corpus (F603/F606) + web (5D localization) grounded.**

---

## Ratified (rigorous, Round 3)
- **λ⁴ ⟺ the up-type ⊥⊥-block vanishes** (⟨c_L|δΦ|c_R⟩ = 0, charm–charm direct coupling in the space ⊥ to the top). Grace: power set ENTIRELY by this block (saturation held fixed → block=0 gives ε², block≠0 gives ε¹). Elie: the σ₂-power is **weak-basis invariant** — a Fritzsch/NNI zero created by basis choice is cosmetic and can't fake ε². **So the only physical question is whether the block vanishes as an invariant.** Solid.
- Lyra's F621 retraction correct: saturation stabilizes σ₁ (δσ₁~ε²) but does NOT steepen the tower; top=O forces charm ⊥ O but does NOT force the *correction's* charm-block to vanish.

## ★ Contribution 1 — the correct selection rule is Wigner–Eckart, not sphericity
Grace proposed a **λ₂/sphericity** rule (K745): non-spherical charm bilinear decouples from the spherical condensate. Right TYPE (a K-type selection rule), but "spherical" is not the sharp criterion. The Yukawa ⟨c_L|O|c_R⟩ is an SO(5)-invariant with the condensate in the **vector (1,0)** rep (O = SO(5) vector, F603; top = spinor, and 4⊗4 ⊃ 5 gives the top's CG=1, F606). By **Wigner–Eckart**:
> **⟨c_L|O|c_R⟩ ≠ 0  ⟺  c_L ⊗ c_R\* contains the (1,0) vector** (the rep of O).
Not "c_L⊗c_R* contains a singlet/spherical piece" — the singlet (0,0) is orthogonal to the vector (1,0), so the trace part does NOT couple. The block vanishes **iff c_L⊗c_R\* ⊉ (1,0)**. This is the precise, basis-independent, decidable form of the texture-zero question. (It also repairs a subtle trap: "charm⊗charm* always contains a spherical singlet so it always couples" is FALSE — the singlet doesn't match the vector O.)

## ★★ Contribution 2 — the decisive FORK (this is the epistemic crux)
There are TWO ways the up-type charm-block can be small, with OPPOSITE epistemic status:
- **(A) EXACT texture zero — c_L⊗c_R\* ⊉ (1,0).** A genuine SO(5)×SO(2) selection rule (a *grading*) forbids the coupling. → block = 0 exactly → **clean integer power 2 → λ⁴ DERIVED** (clears Elie's FN trap). Requires a symmetry.
- **(B) RADIAL-localization suppression — c_L⊗c_R\* ⊃ (1,0), but the radial overlap is small.** Charm is localized at an interior stratum; its overlap with the boundary-reaching condensate is small but **nonzero**. → block ≈ small, NOT zero → the "power" is a continuous, running-contaminated number, NOT a clean integer → **Tier-2.**

**★ Clarification (Casey 07-21, refining "localization-dependent"):** (B) does NOT mean the ladders are underivable — it means they are not derivable *as clean integer powers*. **BST's wavefunctions are RIGID** — the fixed K-type eigenfunctions of the geometry, with NO free bulk-mass/width knob (unlike generic 5D models that *fit* localizations). So the overlap ratios are **fully computable Bergman integrals ONCE the K-type addresses are pinned** → the ladders ARE derivable at Tier-2 (few %, running-contaminated), just not as integers. What blocks a *clean* derivation: (1) irregular strata spacing → messy overlaps not clean powers; (2) RG running → substrate-scale ≠ observed, adds scale-dependence + SM couplings. What would block *any* derivation: (3) the DISCRETE K-type address choice (June open core) if unfixed — and that's discrete, not a continuous parameter. **Actionable: don't label "localization-dependent" — pin the addresses and COMPUTE the overlaps** (that IS pull 07-21d). Tier-2 derived ladders is a real, publishable outcome even without (A)'s integers.

**These are experimentally distinguishable in the data we already have.** An exact texture zero (A) gives clean integer powers {2, 4}. Continuous suppression (B) gives *non-integer, scattered* powers. **Grace measured λ^{2.0–4.3} (up), λ^{2.0–2.7} (down) — non-integer scatter.** That scatter is the **signature of (B)**, not (A). And the web is unambiguous: in extra-dimensional wavefunction-localization models — which is exactly BST's "generations = radial strata" — the up/down and quark/lepton asymmetries arise from **continuous overlap suppression, not texture zeros** ([5D SO(10) localization, hep-ph/0302073](https://arxiv.org/pdf/hep-ph/0302073)).

**Honest lean:** the evidence (non-integer scatter + the localization mechanism BST actually uses) points to **(B)** — the row stays Tier-2, and the "integer powers" are NOT exactly derivable; they're localization-overlap numbers. **But (A) is not excluded** and must be checked, because if a real grading forbids the up-type coupling, the integer IS derived.

## ★ Contribution 3 — the decidable computation (target-innocent, one rep-theory check)
Pin the strata K-type assignments (a,b) for each generation, L and R (F86 support flag: 3 strata; the (a,b) discrete-series addresses). Then compute, per sector:
1. **Does c_L ⊗ c_R\* contain (1,0)?** (up-type charm) and **s_L ⊗ s_R\* contain (1,0)?** (down-type strange).
2. If **forbidden for up but allowed for down** → **(A)**, λ⁴/λ² DERIVED as integers.
3. If **allowed for both** → **(B)**, Tier-2; the up/down difference is radial (localization), and the powers are non-integer — say so honestly.
This is the same computation whether it lands on (A) or (B); it's target-innocent (rep theory + radial overlaps, not fitting ratios). Elie's harness then checks the invariant σ₂-power.

## The up/down asymmetry (deepest sub-question — flag, don't force)
Under (A) it's a grading difference: up couples to O, down to Õ (conjugate, opposite SO(2) charge) — do their selection rules differ? Under (B) it's localization: up-3 saturates (top=O, boundary), down-3 doesn't (y_b≪1, sub-boundary), so the up-type sector is *more* boundary-concentrated → steeper overlap falloff. Note (B)'s version quietly brings saturation back as the *ultimate* cause (it sets the localization pattern) even though Grace correctly showed it's not the *proximate* cause (the block is). Both need the pinned (a,b) assignments.

## Tiers / discipline
- BANKED (rigorous): λ⁴ ⟺ block vanishes (invariant); the selection rule is c_L⊗c_R* ⊃ (1,0) (Wigner–Eckart); saturated-top stability (δσ₁~ε²); top=O (CG=1).
- OPEN, forked: (A) exact zero (derived integer) vs (B) radial suppression (Tier-2). **Evidence leans (B).**
- Do NOT bank integer powers unless the rep computation lands on (A) with an exact selection rule. The non-integer scatter is a standing warning against a false (A).
- "Seesaw"=linear-algebra ε²/s, not ν_R (Five-Absence-safe). BST's strata = geometric Froggatt–Nielsen charges (web: modular weights ↔ FN charges) — the win is deriving the FN charges from the strata, IF (A).

— Keeper K796, 2026-07-21. Math contribution: the up-type texture-zero criterion is Wigner–Eckart — block vanishes ⟺ c_L⊗c_R* ⊉ (1,0) vector (O's rep) — NOT sphericity (the singlet is orthogonal to the vector; corrects Grace's K745 form). This forces the FORK: (A) EXACT zero (grading selection rule → derived integer λ⁴) vs (B) RADIAL-localization suppression (continuous → Tier-2). The OBSERVED non-integer scatter (λ^{2.0–4.3}) + the 5D-localization mechanism BST uses both point to (B). Decidable by one rep computation: does c_L⊗c_R* ⊃ (1,0) for up vs down (pin the F86 strata (a,b) addresses)? Don't bank integers unless it lands on (A). See [[Keeper_K795_adjudicate_lyra_elie_no_contradiction_uptype_kernel_block_selection_rule_2026-07-21]], F603/F606 (O=vector, top CG=1), F86 (strata), K745 (Grace's λ₂ rule — refined here).
