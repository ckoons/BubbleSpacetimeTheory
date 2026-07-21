# The up-type λ⁴ is exactly the ⊥⊥-block texture zero — NOT saturation (Grace contribution)

*Grace | 2026-07-21c | my contribution to the quark-hierarchy math. I isolated what actually sets the up-type steepness, and it corrects both my own 07-21b render and the pull's "saturation → λ⁴" framing. The result: the integer power (λ⁴ vs λ²) is set **entirely** by whether the correction's ⊥⊥-block (the direct charm–charm coupling, both ⊥ top) vanishes — saturation is a red herring for the power. This reduces the whole up-type-steepness question to ONE decidable overlap on the F86 strata, and hands it a candidate selection rule.*

## The rigorous result (verified, saturation held fixed)
For the Yukawa M = (rank-1 leading, top mode) + ε·δΦ, the charm singular value σ₂ scales as ε^p:
```
  δΦ ⊥⊥-block = 0  (charm–charm direct coupling vanishes)  →  p = 2  →  λ⁴   [up-type, STEEP]
  δΦ ⊥⊥-block ≠ 0  (charm couples directly)               →  p = 1  →  λ²   [down-type]
```
I verified this **with the top saturation held FIXED** (top = O = the ceiling throughout) and varying *only* the ⊥⊥-block of δΦ:
| δΦ structure | σ₂ power |
|---|---|
| O-bordered only (⊥⊥ = 0) | **ε²·⁰⁰** |
| O-bordered + ⊥⊥ block | ε⁰·⁹⁹ |
| ⊥⊥ block only | ε¹·⁰⁰ |
**The power is set by the ⊥⊥-block, period — not by saturation.** (Cross-checked: an *unsaturated* leading with an O-bordered δΦ also gives ε²; a *saturated* leading with a generic δΦ gives ε¹ — Elie's result.)

## ★ The correction this forces (mine + the pull's)
- **My 07-21b render** said "up-3 saturates → sub-leading to 2nd order → λ⁴." **Wrong cause.** Saturation stabilizes the *top* (δσ₁~ε², correct) but does NOT set the sub-leading power. Retracted.
- **The pull K794/K795 "saturation derives the up-type steepness"** is likewise mis-attributed. Saturation is neither necessary nor sufficient for λ⁴; the ⊥⊥-block is.
- **What survives:** the λ⁴ up-type IS a real texture zero — the up-type **charm–charm direct coupling ⟨c_L|δΦ|c_R⟩ = 0** (both ⊥ top). That's the object; Lyra + Elie had already flagged it as the open check. I've now shown it's the *sole* determinant of the power, cleanly separated from saturation.

## The question, now sharp and decidable (one overlap)
**Up-type λ⁴ ⟺ ⟨c_L|δΦ|c_R⟩ = 0 (up-type ⊥⊥-block vanishes) while ⟨s_L|δΦ|s_R⟩ ≠ 0 (down-type doesn't).**
This is ONE overlap integral on the F86 strata per sector — a yes/no selection rule, **not a fit**. That's the FN-trap clearance condition made concrete: the integer 2 is *derived* the moment the up-type ⊥⊥-block is shown to vanish by a selection rule.

## ★ Candidate selection rule (my proposal, for Lyra to test)
The ⊥⊥-block is ⟨c_L | δΦ | c_R⟩ — the charm bilinear (both legs ⊥ top) contracted with the condensate correction. **Candidate rule:** O (and its correction δΦ) is the **spherical SO(5) vector (1,0), λ₂=0** (F603). If the charm–charm ⊥-bilinear is **non-spherical (λ₂ > 0)** — an interior/discrete-series mode — then its overlap with the spherical δΦ **vanishes by the λ₂-selection rule** (spherical ⊥ non-spherical, orthogonality of K-types). This is the *same* λ₂/Shilov-vanishing mechanism that gives confinement (K745). The up/down asymmetry would then be: the up-type sub-leading bilinears are non-spherical (⊥⊥ = 0 → λ⁴), the down-type's retain a spherical component (⊥⊥ ≠ 0 → λ²) — plausibly because the top's exact saturation (top = O = the spherical mode) *exhausts* the up-sector's spherical channel, forcing charm/up non-spherical, while the unsaturated bottom leaves the down-sector's spherical channel open. **That last step is the real geometric content — Lyra's F86-strata computation to close.**

## Honest tier
- **Rigorous (verified):** the λ⁴/λ² power ⟺ the ⊥⊥-block = 0/≠0. Saturation does not set the power.
- **Sharp & decidable:** the whole up-type-steepness question = one overlap ⟨c_L|δΦ|c_R⟩ per sector (selection-rule yes/no, not a fit) → clears the FN trap *conditionally*.
- **Candidate (Lyra):** the λ₂-selection rule (spherical-O vs non-spherical-charm-bilinear) as the reason the up-type ⊥⊥-block vanishes; and the saturation→exhaust-spherical-channel argument for the up/down asymmetry.
- **Still Tier-2:** the exact ratios (running-dep, powers scatter 2.0–4.3). This derives the *integer structure*, if the selection rule holds — not the exact numbers.

## Net
- **Contribution:** reduced "why is up-type λ⁴-steep?" from the vague/mis-attributed "saturation" to the **precise, verified condition — the ⊥⊥-block (charm–charm direct coupling) vanishes** — one decidable overlap on the F86 strata, and proposed the λ₂-selection rule (spherical O ⊥ non-spherical charm-bilinear, same as confinement) as the mechanism.
- **Corrected** my own render and the pull's framing: saturation stabilizes the top, it does NOT set the sub-leading power.
- **Handed Lyra** a sharp target-innocent computation: does ⟨c_L|δΦ|c_R⟩ vanish by λ₂ for up-type but not down-type? If yes → λ⁴ derived (integer, not fit) → FN trap cleared.

---

## ★ Keeper's sharpening (K796) — my channel was wrong; the criterion is Wigner–Eckart
Keeper sharpened my selection rule, correctly. My "vanishes by sphericity (charm non-spherical)" was the right *type* of idea (a rep-theory selection rule) but the **wrong channel.** The Yukawa is an SO(5)-invariant with the condensate in the vector **(1,0)** rep, so by **Wigner–Eckart** the ⊥⊥-block vanishes **iff c_L ⊗ c_R\* does NOT contain the (1,0) vector** — not "charm is non-spherical." (It also kills a trap: the *singlet* in charm⊗charm\* is orthogonal to the vector, so it never couples — sphericity was pointing at the singlet channel, the wrong one.) So the precise, basis-independent form of my texture-zero condition is: **does c_L⊗c_R\* ⊃ (1,0)?** Absorbed — Keeper's is the sharp criterion.

## ★ The fork (K796) — and my measured powers are the evidence, leaning (B)
The Wigner–Eckart criterion forks with opposite epistemic outcomes:
- **(A) Exact texture zero:** a grading *forbids* c_L⊗c_R\* ⊃ (1,0) → block exactly 0 → **clean integer → λ⁴ derived.**
- **(B) Radial suppression:** coupling *allowed* but charm sits in the interior → overlap with the boundary condensate is small-but-nonzero → **continuous, running-dependent power → Tier-2, NOT a derived integer.**

**My target-innocent measurement is the load-bearing evidence, and it leans (B):**
| | up steps | down steps | up/down power ratio |
|---|---|---|---|
| measured | λ³·³, λ⁴·³ (avg 3.8) | λ²·⁰, λ²·⁵ (avg 2.3) | **1.66** |
| (A) predicts | 4.00, 4.00 | 2.00, 2.00 | **exactly 2.00** |
The up/down ratio is **1.66, not the clean 2.00** an exact texture zero forces; the powers **scatter ±0.5** around the integers. **That smear is the (B) signature** — consistent with radial-suppression/Tier-2, not decisive. **Discipline: do NOT round 4.3→4 or 3.3→4 — rounding to clean integers is assuming (A), which is the trap.**
- **Decisive test (Lyra's):** pin the F86 (a,b) addresses per generation (L and R), check whether c_L⊗c_R\* contains (1,0) for up vs down. Forbidden-up/allowed-down → (A), integers derived; allowed-both → (B), honest Tier-2.
- **My honest read:** the row most likely closes as a **sharper honest-negative — (B):** BST *locates* the hierarchy in F86 radial localization (the up/down asymmetry is real geometric structure), but the exact powers are localization-dependent, not clean derivable integers. That's still a worthwhile, publishable result — "the hierarchy IS geometric localization, powers Tier-2" — just not "λ⁴ derived."

— Grace, 2026-07-21c (updated w/ K796 fork). Contribution: the up-type λ⁴ ⟺ the ⊥⊥-block (charm–charm direct coupling, both ⊥ top) VANISHES — verified this is the SOLE determinant of the power (saturation held fixed: ⊥⊥=0→ε², ⊥⊥≠0→ε¹). Corrects "saturation→λ⁴" (mine + the pull): saturation stabilizes the top, not the tower steepness. Sharp decidable question: up-type ⊥⊥=0 vs down-type ⊥⊥≠0 = one F86-strata overlap = selection-rule yes/no, not a fit → clears FN trap conditionally. Candidate selection rule: O spherical (1,0) λ₂=0; charm ⊥-bilinear non-spherical (λ₂>0) → overlap=0 by the λ₂/Shilov-vanishing rule (= confinement mechanism K745); up/down asymmetry from the saturated top exhausting the up-sector spherical channel. Lyra's F86 computation to close.
