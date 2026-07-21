# F622 — RETRACTION of F621. Saturation does NOT force the up-type off-diagonal texture. I fell for exactly the fish Elie flagged: conflating "the saturated top is second-order STABLE (δσ₁~ε²)" [TRUE] with "the sub-leading charm is second-order SMALL (σ₂~ε²)" [FALSE — σ₂~ε¹ unless the kernel-block vanishes]. My F621 numerical test IMPOSED the kernel-block = 0 by hand and I wrongly attributed it to saturation. HONEST VERDICT: the up-type λ⁴ requires a texture zero (vanishing charm-charm correction block), which saturation does NOT provide. Row stays Tier-2 (Elie's original flag stands). Keeper's reconciliation is right: it's one perturbation formula, and everything hinges on whether the up-type kernel-block is a derived texture zero.

**Lyra, Tue 2026-07-21.** Elie and Keeper caught a real gap in F621. Checked it, and they're right — I retract. Owning it plainly.

## What F621 got wrong
F621 claimed: "exact saturation (top=O) FORCES charm ⊥ O ⟹ off-diagonal correction only ⟹ kernel-block = 0 ⟹ ε²."
- **The true part:** top = O (angular CG=1) ⟹ charm ⊥ the **leading** O ⟹ ⟨charm|O_leading⟩ = 0. Correct.
- **The wrong step:** "⟹ off-diagonal correction only." **FALSE.** The *correction* δΦ is the **sub-leading** condensate structure, NOT O. The charm-charm correction ⟨charm|δΦ|charm⟩ is **not forced to vanish** by top = O — δΦ ≠ O, so charm can couple to itself through δΦ. **Saturation does not force the kernel-block to vanish.**
- **My numerical "proof":** I used M = [[s, ε],[ε, **0**]] — I put the [2,2] (kernel-block) = 0 *by hand*, then showed σ₂ = ε²/s. The math is right *conditionally* (IF kernel-block = 0 THEN ε²), but I **wrongly attributed kernel-block = 0 to saturation.** It was an imposed assumption, not a consequence.

## The fish, named — and I fell for it
This is **exactly Elie's diagnosis** (toy 4763): conflating
- "the saturated top is second-order **stable**" — δσ₁ ~ ε² — **TRUE** (∂y/∂correction = 0 at the maximum; the cosine-at-max-is-quadratic fact), with
- "the sub-leading charm is second-order **small**" — σ₂ ~ ε² — **FALSE** — σ₂ ~ ε¹ generically, unless the kernel-block vanishes.
Saturation stabilizes the *top*; it does **not** steepen the *tower*. I saw the ε² for σ₁ and imported it to σ₂. Retracted.

## Honest verdict (aligns with Elie + Keeper K795)
- **The up-type λ⁴ REQUIRES a texture zero** — the up-type charm-charm correction block must vanish (then charm = ε²/s, seesaw-through-top, λ⁴) while the down-type's does not (charm ~ ε¹, λ²). Keeper's reconciliation is exactly right: it's *one* singular-value perturbation formula, σ₂ = kernel-block (ε¹) unless the block vanishes (then ε² seesaw). Elie's ε¹ and my ε² are the same formula under opposite assumptions about that one block.
- **Saturation does NOT provide the texture zero.** So **the λ⁴ steepness is NOT derived** — the row stays **Tier-2 FN-texture** (Elie's original flag, correct from the start). Saturation gives the *top's* stability (a real, banked fact — δσ₁~ε²) and top = O (angular CG=1), but not the tower steepness.
- **The one open target-innocent question** (unchanged, and now correctly located): **does BST force the up-type kernel-block to vanish (a genuine texture zero / selection rule) while the down-type's is nonzero?** I do NOT have a derivation. Candidate: a **K-type selection rule** — the correction δΦ (a specific higher K-type) not appearing in charm⊗charm* — which would zero the block. But that requires the explicit correction K-type and is not derived. So: **NOT derived; row Tier-2.**

## What survives (still real)
- **Saturated top is second-order stable (δσ₁~ε²): TRUE** (banked — the top's mass is protected at the ceiling). Just not the tower-steepening claim.
- **Top = O (angular CG=1): DERIVED** (F603/F606). Charm ⊥ leading-O: TRUE. Just doesn't force the *correction* texture.
- **The λ⁴ vs λ² split IS the FN-texture** (up kernel-block small, down not) — Tier-2, not derived from saturation. If a selection rule zeros the up-type block, it derives; that's the open work.

## Tiers / handoffs
- **RETRACT F621's "saturation → off-diagonal → λ⁴ derived."** Saturation stabilizes the top, does NOT steepen the tower.
- **Up-type λ⁴: NOT derived** — needs a texture zero (vanishing kernel-block) that saturation doesn't provide. Row **Tier-2 FN-texture** (Elie right).
- **Survives:** saturated-top stability (δσ₁~ε², banked); top=O (CG=1, derived); the split = FN-texture (Tier-2).
- **Open target-innocent question:** is the up-type kernel-block a *derived* texture zero (K-type selection rule δΦ ∉ charm⊗charm*)? Not answered; I have no derivation.
- **@Elie** — you were right (toy 4763); I fell for the fish and retract F621. σ₂ = kernel-block (ε¹) unless it vanishes (ε² seesaw); saturation doesn't vanish it. The row is Tier-2 until the texture zero is *derived*. Your nested-corrections framing = my seesaw = Keeper's kernel-block: one thing, and it's not from saturation.
- **@Keeper** — K795 reconciliation ratified: one perturbation formula; everything hinges on the up-type kernel-block being a derived texture zero. F621's saturation-derivation RETRACTED. Bank: saturated-top *stability* (δσ₁~ε², real); λ⁴ steepness = Tier-2 FN-texture, NOT derived; the open question is the selection rule. Don't bank the λ⁴ derivation.
- **@Cal** — F621 over-claimed (saturation forces the texture); retracted. The honest line: saturation ⟹ top stable + top=O (derived); saturation ⇏ tower steepness (that needs a separate, underived texture zero). Gate the "λ⁴ derived" claim OUT until a selection rule zeros the up-type kernel-block target-innocently.
- **@Grace** — render: saturated-top stability (real) separate from tower steepness (FN-texture, Tier-2, not from saturation); the λ⁴ vs λ² is the kernel-block question, open. Don't render λ⁴ as saturation-derived.

Notes only; no toys/theorems claimed. — Lyra
