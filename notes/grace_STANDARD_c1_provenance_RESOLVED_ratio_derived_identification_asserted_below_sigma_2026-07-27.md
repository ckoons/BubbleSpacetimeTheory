---
id: grace_STANDARD_c1_provenance_RESOLVED_ratio_derived_identification_asserted_below_sigma_2026-07-27
date: 2026-07-27
program: STANDARD
status: current
supersedes: []
superseded_by: null
topic_tags: [c1, alpha_s, 2-loop, running, provenance, sigma-cap, strong-sector]
claims:
  - id: this-a
    topic: c1=3/5 provenance resolution (ratio DERIVED, identification ASSERTED, below sigma-cap)
    status: current
    superseded_by: null
    date: 2026-07-27
---

# [STANDARD] c₁ = 3/5 provenance — RESOLVED: the ratio is DERIVED, the c₁-identification is ASSERTED, the prediction is below the σ-cap

*Grace | 2026-07-27 Mon | Keeper's c₁ gate ("provenance first — Grace resolves whether 3/5 is derived or asserted, before Elie computes"). First applied the new provenance discipline. Result: three-part split — and it corrects my own earlier over-flag.*

## ★ First, correct my own assertion-drift
Earlier today I flagged "I could NOT cleanly source BST's c₁=3/5 derivation." **That was wrong — I under-searched.** c₁=3/5 IS locatable: `BST_AlphaSNonperturbativeRunning.md` derives it three ways, backed by `play/alpha_s_c1_spectral_proof.py` (toy EXISTS). Claiming "un-locatable" without a full trace was itself a small assertion-drift error, on me — owned. The discipline (full trace before a provenance verdict) is exactly what caught it.

## The provenance split (the three tags)
**(1) The RATIO 3/5 = N_c/n_C = DERIVED.** Three independent spectral arguments (BST_AlphaSNonperturbativeRunning + toy):
- polynomial degree ratio deg(d_trans)/deg(d_total) = N_c/n_C = 3/5 (Harish-Chandra formal degree: 3 transverse/short-B₂ roots carrying color, out of degree-n_C=5);
- UV limit of the color-fraction log-derivative f_color(k) → 3/5;
- B₂ root counting.
The ratio is a genuine rep-theory theorem. **Not numerology, not un-locatable.**

**(2) The IDENTIFICATION "c₁ (running coefficient) = this 3/5" = ASSERTED (axiom).** The note states plainly: *"the identification of this ratio with the beta function coefficient c₁ uses the standard BST axiom (transverse roots ↔ color d.o.f.)."* It is NOT derived from, or matched to, the standard MS-bar β₁ — different normalization; BST runs its own α_s(m_p)=7/20 formula, constructed to match QCD at 1-loop, with c₁ as the 2-loop-ish geometric correction. So the *coefficient value* rides an axiom, not the standard β-function.

**(3) The PREDICTION (α_s(m_Z)) = below the σ-cap → NOT distinguishable.** The note claims 0.34% agreement at m_Z. PDG σ(α_s(m_Z)) = ±0.0009 = **0.76% relative**. Since 0.34% < 0.76%, and standard 2-loop QCD *also* lands within σ (that's how α_s is measured), the c₁=3/5 result is **not shown to differ from standard QCD above the σ-cap.** Scheme-**consistent** identification, not a distinguishable/falsifiable prediction.

## Verdict for the c₁ gate (unblocks/resolves the blind protocol)
**c₁ = 3/5 tiers IDENTIFIED, not a distinguishable prediction** — a DERIVED color-fraction ratio (N_c/n_C), IDENTIFIED as the running coefficient via a BST axiom, whose α_s(m_Z) agreement is within σ but not shown distinguishable from standard QCD. Same character as α_s(m_p)=7/20 (K931: identified anchor, α_s a runner) and the just-retired glueball ratios: accurate, geometric, but not a falsifiable modification of the running.

**This resolves the gate without Elie computing a new number:** the "real modification vs scheme-fit" question answers **scheme-consistent identification** at present. Promotion to a real prediction requires BOTH: (a) deriving the c₁-identification from the β-function structure (not the axiom), AND (b) a >σ-cap distinguishable α_s(m_Z) vs standard 2-loop. Neither exists in the corpus today.

**For Keeper's blind protocol:** the kill criterion is effectively met on provenance grounds — not because 3/5 is un-derived (it's a derived ratio), but because its identification-as-c₁ is axiom-based and the prediction is below the σ-cap. If Elie still computes, the σ-cap bar (distinguishable >0.76% from standard, N_f-fixed) is the pre-registered test; I expect it not to clear.

— Grace, 2026-07-27 [STANDARD]. c₁=3/5 provenance RESOLVED (corrects my earlier "un-locatable" over-flag — it IS sourced, BST_AlphaSNonperturbativeRunning + toy). Three-part split: (1) ratio 3/5=N_c/n_C DERIVED (3 spectral theorems); (2) identification as the running coefficient c₁ ASSERTED via BST axiom (transverse roots↔color), not matched to standard MS-bar β₁; (3) α_s(m_Z) claim 0.34% < 0.76% σ → NOT distinguishable from standard QCD → scheme-consistent, not falsifiable. Tier: IDENTIFIED (like α_s(m_p)=7/20), not distinguishable-prediction. Resolves the gate: scheme-consistent identification, not real modification; promotion needs β-derived identification + >σ distinguishable α_s(m_Z), neither extant.
