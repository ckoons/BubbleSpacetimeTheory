CI Board — PASS 2: every CI improves EVERY item. (Casey directive 2026-07-02)

First pass covered all 26 (partitioned). Now the opposite: **each CI sweeps all 26 and tries to improve every one.** Three independent attempts per item → best wins. Redundant on purpose — diverse minds find better forms and (the real prize) forced mechanisms. Run `python3 play/bst_26_table.py` for the live baseline; goal is to move the table by end of day.

## What "improve" means — move toward DERIVED-STRONG, not just another MATCH

The table has 13 nominal MATCH but only ~5 **derived-strong** (MATCH + not-cheap + forced-mechanism). Improvement = closing that gap, on three axes:

1. **MECHANISM (the real prize).** Most MATCHes are value-forms — the number fits, the derivation-from-substrate isn't forced. A forced mechanism (like δ_CKM's triangle geometry, θ₁₃'s boundary-reaching) is worth more than any number of value-forms. **This is where the day's value is.**
2. **UN-CHEAPEN the cheap MATCHes.** sin²θ₂₃ (6 forms fit within 1σ) and sin²θ₁₂ (3 fit) are coarse-angle fits — near-zero evidence until a mechanism *forces the specific form* over its competitors. Find the forcing, or the MATCH stays weak.
3. **TIGHTEN forms on expensive/precise targets.** For finely-measured params, a better closed form that lowers σ is real. (α: pin the exact Wyler form, not flat 137. muon/τ: is there an exact form, or is (24/π²)⁶ genuinely just a 0.003%%/1550σ approximation?)

**A GUT/GUT-scale value is never an improvement** (down-row). A cheaper coarse-angle fit is not an improvement. Structure-forcing, not value-reaching.

## Per-item leverage (spend effort proportional to this)

- **MISS → repair (highest leverage):** m_d/m_e, m_b/m_s. The observed down ladder (m_s/m_d = 20 = rank²·n_C) is already a 0σ MATCH — recast the down sector to the *observed* ratios via F453 + Grace's d₂ (KW boundary, verified fresh). Convert 2 MISS.
- **OPEN → fill:** m_e (gravity route — does 6π⁵α¹²m_Pl actually score?), m_ν1/2/3 (forms + the absolute-scale FLOOR), δ_PMNS (needs mechanism; data ±40° so a value-form is near-worthless).
- **APPROX → exact-or-honest:** α (Wyler exact form), muon, m_τ, sin²θ_W (it's a runner at 11σ — is it terminal-NEG, or is there a scale where a substrate form is exact?).
- **CHEAP MATCH → force the form:** sin²θ₂₃, sin²θ₁₂ (and verify Lyra's θ₁₂ divide-correction mechanism).
- **VALUE-FORM MATCH → mechanism:** V_us, V_cb, m_c/m_u, m_H — each fits; each needs the substrate derivation forced.
- **DERIVED-STRONG → confirm, don't re-litigate:** θ_QCD, sin²θ₁₃, δ_CKM, V_us(*expensive*), m_t. Quick confirm, move on.

## Process (unchanged)

- Each CI: sweep all 26, add improvement attempts to the ledger (`form + value + how-from-substrate + provenance`). **Never delete a tried form** — the attempt-list accumulates so no one repeats a dead end.
- Hand attempts to Keeper. **You do NOT self-certify** — the ledger computes dev% + σ (scheme-aware) + cheapness → verdict. Best attempt per value wins.
- Independent first, converge after: don't coordinate forms up front — the value of redundancy is three *independent* takes. Compare at the end.

## Roles

- **Lyra / Grace / Elie:** each sweeps all 26, improving. Lead with your strength (Lyra mechanisms/mixing, Grace geometry/masses, Elie numerics/scales/pins) but attempt every item.
- **Keeper:** score every attempt on all three axes; keep the ledger + the 26-table current; hold the honest tally; adjudicate mechanism; never rewrite a CI's derivation. Run SOD check first.
- **Cal:** post-landing cold-read. α tier-call reserved for Casey.

## End-of-day target

Re-run `bst_26_table.py`. Success = **derived-strong count up** (mechanisms forced, cheap MATCHes un-cheapened, MISSes repaired), not the nominal MATCH count. Report the honest delta: which items moved from value-form→forced, cheap→forced, MISS→MATCH, OPEN→scored. The number that matters is derived-strong, and today we try to grow it.

— Keeper, Pass 2. Every CI, every item, improve. Mechanism is the prize; cheapness and σ keep us honest; the table tells the truth at EOD.
