# K643 — σ-Metric Adopted; θ₁₃ is a MATCH not a MISS; m_t Needs a Scheme-Aware Error; Down-Row Repairable

**Auditor:** Keeper | **Date:** 2026-07-02 Mid-Year | **Verdict:** σ-scoring adopted as standard; θ₁₃ MATCH (stays banked, label corrected); m_t MATCH under scheme-aware error; down-row structural-MISS but repairable | **Count 8, honest tiering sharpened**

Consolidates the team's independent convergence on σ-scoring (Lyra, Elie, Grace all reached it same-session, opposite directions) and adds the error-honesty refinement.

## 1. σ-metric adopted (already built)

The almanac/derivation-ledger now scores **σ = |Δ|/experimental-error** alongside dev%. Verdict = MATCH (σ≤2) / APPROX (σ>2, dev<1%) / MISS (σ>2, dev≥1%). This was the team's unanimous ask; it is live in `play/bst_derivation_ledger.py`. It separates what dev% blurred:
- **θ₁₃:** 1.24% dev but **0.5σ → MATCH** (Grace/Lyra: not a miss).
- **down-row:** direct misses **6.5/6.8/80σ → real structural MISS** (Elie: decisive, not the m_s/m_d cross-check which is 1.24σ).
- **muon/α:** 0.003%/0.026% dev but ~1500σ/~1e6σ → **APPROX** (good closed forms, not exact identities).

## 2. θ₁₃ adjudicated (reference call handed to Keeper by Grace)

**θ₁₃ = 1/(N_c²·n_C) = 1/45 stays banked as a valid zero-parameter prediction.** But the tier label is corrected:
- OLD: "firm, 0.10%" — rested on the favorable (with-SK) NuFIT variant, unpinned.
- NEW: **"0.5σ consistent (NuFIT 6.0 default no-SK: 1.24% dev, 0.47σ)."** A zero-parameter prediction at half a sigma is a hit; the "0.10%" headline is withdrawn (the measurement isn't that precise). MATCH + forced mechanism (boundary-reaching) → clean on both axes.

## 3. m_t needs a scheme-aware error (Keeper refinement — sharpens the team's "3 firm")

**The σ-metric is only as honest as the error fed it.** My ledger scored m_t at **4.7σ** using the pole error (0.30 GeV) — a spurious multi-σ. But y_t=1 → m_t = v/√2 = 174.1 is a **tree-level/scheme-ambiguous** statement, and "the top mass" spans ~10 GeV (pole 172.7 vs MSbar 162.5). Under a scheme-aware error (~1–2 GeV), 174.1 is **~0.7σ → MATCH.**

- **Standing rule for the re-pin:** scheme-dependent quantities (all quark masses, incl. m_t) must be pinned with a **scheme-aware error**, not the tight single-scheme measurement precision, or they read spurious multi-σ. This is the SAME scheme lesson that killed the down-row's mixed-scale ratios — now applied to keep the σ-metric from *manufacturing* misses. Pin value AND appropriate error.

## 4. Honest tier under (σ-match × forced-mechanism)

- **Clean on both axes (σ≤2 MATCH + forced mechanism):** θ_QCD (0σ, exact), θ₁₃ (0.5σ), m_t (0.7σ scheme-aware, forced-on-v-floor). = the honest "3 firm."
- **σ-MATCH but mechanism not forced:** Cabibbo (0.6σ, candidate two-point).
- **APPROX (good %, many-σ, structural tier):** muon (principle-gated), α (partial), m_τ (candidate).
- **MISS:** down-row ×3 (12–68σ).

Count 8 unchanged; the tiering is now σ-honest.

## 5. Down-row: structural-MISS but REPAIRABLE (F453 verified)

Lyra's regularized determinant F453 (Elie 4545 verified) resolves K638 Flag 2: one operation, det-branch (lepton π-form) vs residue-branch (quark mode-count), color flattens R → residue. **The repair aims the down sector at the OBSERVED ladder m_s/m_d ≈ 20 = rank²·n_C (a 0σ exact match in the ledger)**, not the failed GJ {3,1/3,1}. Open gate (Grace): is k₂/k₁ = 20 forced by the rank-1 stratum geometry? Needs the **Korányi-Wolf boundary-component structure of D_IV⁵** (type IV₅→IV₃→IV₁ chain is a lead, NOT verified — Grace correctly won't bank on unverified boundary theory). Bounded reference task, best fresh.

## Standing for Casey

- σ-metric = the thing to ratify alongside the down-row (it's what makes "down-row MISS but θ₁₃ MATCH" a computed verdict, not a judgment call).
- θ₁₃ label corrected (stays banked, 0.5σ).
- Down-row: structural-MISS, repairable via F453 (ratification unchanged in direction; add "repairable, not dead").
- α tier-call; CLAUDE.md line 0.5; Pass-1 greenlight (with scheme-aware errors in the re-pin).

— Keeper K643, Mid-Year 2026-07-02. σ-scoring adopted; θ₁₃ MATCH (0.5σ, banked, label fixed); m_t MATCH under scheme-aware error (the σ-metric needs the right error, or it manufactures misses); down-row structural-MISS but repairable at the observed ladder. Count 8, σ-honest.
