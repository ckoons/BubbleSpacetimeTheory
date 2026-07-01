# K631 — F444 RG-Invariance Kill: QCD-Running Rescue Retired, Mass-45 = Convention Artifact, θ₁₃ Untouched

**Auditor:** Keeper | **Date:** 2026-07-01 Wednesday | **Verdict:** PASS (structural) / CONDITIONAL (numeric, PDG re-pin gated)

## Scope

Wednesday primary lane (Grace G1 + Lyra F444 + Elie toys 4524–4526). The down-quark mass-formula lane via Vol-16 + QCD running. Landed as an **honest negative** that retires three Tuesday items and preserves one clean survivor. No count motion.

## The claim audited

**Decisive structural fact:** QCD mass running is flavor-blind — the mass anomalous dimension γ_m depends only on the gauge coupling, identical for all flavors. Therefore **same-sector mass ratios are RG-invariant** (scale-independent). This is a QCD theorem, not a BST computation, and it decides the lane before any running is computed.

## Verification (Keeper, independent)

Confirmed the 45-vs-52 split numerically (convention-independent argument; approximate MS-bar values used for direction — **PDG re-pin required before any numeric bank**):

| ratio | value | reading |
|---|---|---|
| m_b(m_b)/m_s(2 GeV) | 44.8 | **mixed-scale artifact** — the "45" |
| m_b/m_s at common 2 GeV | 52.5 | RG-invariant physical ratio |
| m_b/m_s at common m_b | 52.2 | RG-invariant physical ratio |

- **N_c²·n_C = 45** matches only the mixed-scale convention. **rank⁶ = 64 (d(ν))** overshoots. The convention-free common-scale ratio **~52 is missed by both.** The 2-3 gap is genuinely OPEN.
- **1-2 gap:** m_s/m_d ≈ 19.9 is RG-invariant (convention-free); **rank²·n_C = 20** matches at <2% — the clean survivor.

## Rulings

1. **QCD-running "×0.70" rescue — RETIRED. PASS.** Grace's A1 is real as a number (44.8/64 = 0.70) but it is convention-matching, not mechanism: same-sector ratios don't run, so the "shrink" is entirely the arbitrary choice of quoting m_s at 2 GeV and m_b at m_b. Move the scale, the 45 moves. Correctly killed.

2. **Mass-45 rung — RETIRED as convention artifact. PASS.** Tuesday's 45-rung was a mixed-scale artifact. Elie (4525) and Lyra both walked back their own Tuesday 45-claim on physics grounds. Honest and symmetric.

3. **θ₁₃ ↔ mass-45 "shared structure" bridge — DISSOLVED. PASS.** Resolves the pre-arm (K631-prearm) fork to the **coincidence** branch, argued from physics (convention-asymmetry), not merely form-degeneracy. Precise statement: θ₁₃ = 1/45 is a dimensionless mixing angle (no scheme dependence) → convention-**robust**; mass-45 is a convention artifact → there was never a robust shared 45. The bridge dissolves on the **mass** side; **θ₁₃ = 1/(N_c²·n_C) itself is untouched** and stays the 10th candidate. This VALIDATES the pre-arm ruling: the shared-structure observation adds **zero** banks either way, and it resolved to the branch that costs nothing.

4. **m_s/m_d = 20 = rank²·n_C — HOLD as strong structural candidate, DO NOT BANK.** Three independent reasons converge:
   - **Mechanism not there** (Lyra): the "why rank²" is unforced; bare d(ν) gives d(5/2)=0 → massless gen-1 → m_s/m_d = ∞. The 20 is a K551 measurement-determinant / little-group object (harmonics ≤ deg 2 on S⁴ = 20), handed to Elie's color-fiber lane — not a d(ν) or QCD-running quantity.
   - **Form-degeneracy** (Keeper pre-arm): 20 is the MOST form-degenerate number on the board — **24 substrate-primary forms**. A form-match on 20 is near-zero evidence.
   - **Data cannot disambiguate** (Elie 4524): uniform k²·n_C vs substrate-constant rank²/N_c² readings reproduce all three real generations identically and diverge only at a 4th generation, which F397 forbids. Only Vol-16 mechanism can settle which reading generates the 20.
   
   Consistent with the Tuesday θ₁₂ discipline: a clean form that matches does not bank until the mechanism forces it.

## Count reconciliation (Keeper catch)

The three landing reports used inconsistent count anchors: Lyra "count stays 9", Grace "banked count stays 10", Elie "no count move." **These describe the same state against different reference points.** Pin to ONE anchor:

- **9 baseline banked** (held pending Cal α tier-review) — UNCHANGED by F444.
- **θ₁₃ = 1/(N_c²·n_C) 10th candidate** (team consensus firm, awaiting Casey formal acknowledgment + Cal α review) — UNCHANGED by F444 (θ₁₃ is convention-robust).
- **F444 net: no motion.** One Tuesday over-claim (mass-45 rung + shared-45 bridge + QCD-running rescue) honestly retired. The 2-3 gap opened honestly at ~52.

Standing request: report count against the single "9 baseline + θ₁₃ 10th candidate" anchor to prevent drift.

## Session-quality note

**Three-way independent convergence** on the RG-invariance kill (Lyra rep-theory/structural, Grace physics, Elie numerics), with all three walking back their OWN Tuesday claims. That convergence-from-independent-directions is the strongest confirmation pattern in the program, and here it confirmed a *negative*. This is exactly the honest-negative discipline Casey has repeatedly called for. Structural understanding deepened (RG-invariance now fences the whole mass-ratio sector); count correctly held.

## Conditional / carry-forward

- **PDG re-pin (Lyra self-flagged):** the RG-invariance argument is convention-independent and PASSES now; the exact survivor values (m_s/m_d ≈ 19.9, common-scale m_b/m_s ≈ 52) must be pinned to PDG before m_s/m_d = 20 could ever bank. Numeric layer = CONDITIONAL on that pin.
- **Open frontier:** the 2-3 gap at physical ~52 — does any Vol-16 mechanism land on it (or own a real ~25% residual on rank⁶=64)? Lyra's d(ν) side, Grace as geometry checker.
- **Open:** measurement-determinant "why rank² (1-2) then color N_c² (2-3)" — Elie's little-group / color-fiber lane.

## K631-S1 — Keeper self-correction (Elie peer-catch on the pre-arm degeneracy counts)

**Elie caught a real error in my pre-arm form-space search.** I stated relative degeneracy *rankings* — "20 is THE most degenerate (24 forms); 71 is low-degeneracy (~2 forms), a point IN FAVOR of m_τ/m_e = 49·71 being real." Those counts were artifacts of my narrow search space (products of two primaries + sums/diffs of two product-terms). Re-run over a broader space (adding powers k², k³, 2^k, three-way products):

| target | narrow count (pre-arm) | broader count | 
|---|---|---|
| 20 | 24 | 13 |
| 45 | 13 | **14** |
| 71 | 2 | 3 |

**The ranking flips: 45 is as free as 20 (14 vs 13), not rarer.** My "20 is THE most degenerate" was wrong, and my "71 low-degeneracy → point in favor of m_τ/m_e" is **RETRACTED** — 71 is form-cheap too; the 49·71 candidate earns no credit from a degeneracy count that was a search-space artifact. m_τ/m_e stays a candidate on its 0.05% match + open product-mechanism, **not elevated by degeneracy.**

**What survives (Elie confirms the discipline holds):** all three numbers (20, 45, 71) are **form-cheap** — each has multiple natural substrate forms and value ≤ 137, so a bare form-match is weak evidence for *any* of them. The load-bearing conclusion — hold m_s/m_d = 20, don't bank on form-match — is **unchanged**, and now rests on the robust binary (form-cheap: yes) rather than the fragile ranking.

**Keeper #26 sharpening (this catch):** form-space search must be *done* (the pre-arm was right to run it), but degeneracy **counts are search-space-relative** — they support only the **binary "is a bare match cheap? yes/no,"** never fine **rankings** between candidates. Leaning on "I counted few alternatives, so this one is more likely real" is the same error class as "I don't see an alternative," just inverted. Use the binary; never the ranking. **5th Keeper self-correction of the arc** (K625→K626→K628→K631-S1).

— Keeper K631 + S1, Wednesday 2026-07-01. PASS on the structural kill; CONDITIONAL on numeric pin; count held honestly at 9 baseline + θ₁₃ 10th candidate; pre-arm fork resolved to the zero-cost branch; degeneracy-ranking self-corrected via Elie peer-catch, discipline conclusion intact.
