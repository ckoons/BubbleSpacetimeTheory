# K644 — Pass-1 Adjudication: Match-Cheapness Metric; sin²θ_W is APPROX not MATCH; Expensive vs Cheap σ-Matches

**Auditor:** Keeper | **Date:** 2026-07-02 Mid-Year | **Verdict:** first-pass coverage complete (all 26 attempted, parallel) — but σ-MATCH count must be weighted by cheapness + mechanism; one tier correction | **Count 8**

Credit first: the parallel partition worked — Lyra (mixing 8), Grace (masses 9), Elie (scales 9) each covered their whole bucket in one pass, handed to the ledger, no self-cert. That's exactly the directive. Now the skeptical layer, because 7/8 MATCH in mixing is peak-convergence and the bar fires hardest here.

## Tier correction: sin²θ_W = 3/13 is APPROX, not MATCH

Elie tiered it "MATCH scheme-aware." **It's 11.3σ.** 3/13 = 0.2308 vs sin²θ_W(M_Z) = 0.23122 ± 0.00004 — the M_Z value is measured to ±0.00004, and the scheme spread there is ~0.0002, nowhere near enough to rescue a 0.0004 gap. So it's **0.2% dev but 11σ → APPROX** (a good closed form, not a match), same class as α=1/137 and the muon. **Credit where due:** it correctly is NOT the GUT 3/8 = 0.375 — Five-Absence clean, the GUT-numerology flag resolves. But it's a runner *and* an APPROX; do not carry it as a clean MATCH.

## New scoring dimension — MATCH-CHEAPNESS (the σ-space form-cheapness)

A σ-MATCH is only evidence if few simple forms could have landed in the error band. I counted simple substrate fractions p/q within 1σ of each angle:

| angle | error | # simple forms within 1σ | reading |
|---|---|---|---|
| sin²θ₂₃ | ±0.03 (5%) | **6** (4/7, 5/9, 8/14, 9/16…) | **CHEAP** — a σ-match here is near-zero evidence |
| sin²θ₁₂ | ±0.013 (4%) | **3** (3/10, 5/16, 14/45) | **CHEAP** — note BOTH old 5/16 and new 3/10 match |
| V_us | ±0.0008 | **0** | **EXPENSIVE** — 1/(2√5)@0.9σ is real evidence |
| sin²θ₁₃ | ±0.0007 | **1** (1/45) | **EXPENSIVE** — real evidence |
| sin²θ_W(M_Z) | ±0.00004 | **0** | tight, but 3/13 is 11σ off anyway |

**This is K631-S1 (form-cheapness is a binary, not a ranking) reborn in σ-space, and it's decisive for the mixing sector:** the 7 MATCHes split into EXPENSIVE (θ₁₃, V_us — few/no competing forms → real) and CHEAP (θ₂₃, θ₁₂ — 3–6 competing forms → coarse-measurement artifacts). That both 5/16 AND 3/10 σ-match θ₁₂ *proves* the cheapness — the data can't distinguish them.

**Adopt:** the derivation ledger scores a third axis — `#forms-within-1σ` (match-cheapness). A σ-MATCH with ≥3 competing simple forms is flagged CHEAP; only EXPENSIVE + forced-mechanism approaches "derived."

## Honest first-pass reading (three axes: σ-match × cheapness × mechanism)

- **Strong (σ-MATCH + EXPENSIVE + forced mechanism):** θ_QCD (exact), θ₁₃ (1/45, boundary-reaching), δ_CKM (arctan√5 = 65.9°, triangle geometry, 0.0σ), V_us (1/(2√5), expensive). Plus m_t (scheme-aware).
- **σ-MATCH but CHEAP (coarse angle, many forms):** sin²θ₂₃ (4/7), sin²θ₁₂ (3/10) — weak until mechanism forces the specific form.
- **APPROX (good %, many-σ):** muon, α, m_τ, **sin²θ_W (3/13, 11σ, corrected)**.
- **MISS:** down-row ×3 (repairable at observed ladder).
- **FLOOR/NEG/OPEN:** v; α_s (runner); ν absolute scale; m_H (needs σ-pin); δ_PMNS (Lyra's lead, but measurement ±40° → any O(π) value σ-matches → near-zero evidence, honestly flagged by Lyra herself).

## Net

Coverage: **all 26 have a first-pass scored attempt — Pass 1 goal met.** But "how many MATCH" is the wrong headline; the honest one is **how many are σ-MATCH AND expensive AND mechanism-forced** — a much smaller, truer set (~4-5). The mixing sector is genuinely BST's strength, but half its MATCHes are cheap coarse-angle fits. The mechanism axis is Pass-2's real work. Count 8, σ-and-cheapness-honest.

Corrections this pass: sin²θ_W MATCH→APPROX (mine, on Elie's entry); match-cheapness metric added. Two forms upgraded to verify: θ₁₂ = (3/10)/cos²θ₁₃ → 0σ (Lyra's divide-correction, but θ₁₂ is a cheap target); θ₂₃ ×cos²θ₁₃ → 0.1σ.

— Keeper K644, Mid-Year 2026-07-02. Pass-1 coverage complete; match-cheapness = third scoring axis (σ-space form-cheapness); sin²θ_W is APPROX (11σ); mixing MATCHes split expensive/cheap; the honest "strong" set is ~4-5, not 7/8. Mechanism is Pass-2.
