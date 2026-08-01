---
id: grace_BLIND_BAR_PROTOCOL_standing_instrument_2026-08-01
date: 2026-08-01
program: TEGMARK
status: current
topic_tags: [blind-bar, discipline, provenance-not-value, target-innocence, dispersion-floor, hostile-read, cc-magnitude, standing-instrument, legacy]
claims:
  - id: this-a
    topic: the standing BLIND-BAR PROTOCOL — a reusable, pre-registered instrument for ruling on any target-aware BST number so the verdict survives a hostile read; generalizes K1065 (cc-magnitude) into the standing method
    status: current
    superseded_by: null
    date: 2026-08-01
---

# [TEGMARK] The Blind-Bar Protocol — a standing instrument for target-aware numbers

*Grace | 2026-08-01 | Keeper's K1065 committed the cc-magnitude's audit bar BLIND before the derivation. This document lifts that one move into a STANDING, REUSABLE instrument: the procedure for ruling on any BST number whose target value is known in advance, built so the verdict survives a hostile reviewer. This is my lane — the instrument, not the physics. The physics (a₀-coefficient forward derivation) is Lyra/Elie; the cc-magnitude-specific bar is Keeper (K1065/K1065a). This is the general tool they are both instances of.*

## Why this instrument exists (the one-sentence version)
**A target-aware number cannot be credibly ruled on after it lands, because any acceptance criterion written after you see the value can be retrofitted to the value.** The only defense is to commit the criteria BEFORE the number, in writing, dated — so a "match" is scored against a bar it could not have moved. Everything below is machinery for doing that honestly and legibly enough that a hostile reviewer runs the same checklist and reaches the same verdict.

## The distinction that drives everything: target-innocent vs target-aware
- **Target-innocent number:** the integer/exponent reads off the operator's OWN structure — an idempotent count, a dimension, a Casimir eigenvalue, a spectral invariant — with no knowledge of the answer. Example (banked): count = rank+1 = 3 generations reads the rank-2 Jordan frame's primitive-idempotent count; it would be 3 whether or not we'd measured 3 generations. These bank at their honest tier.
- **Target-aware number:** the integer/exponent was selected, or could have been selected, KNOWING the answer. Example (the danger): an exponent assembled from BST integers to land near 122 orders of magnitude. These are FIT-SUSPECT and stay at the floor tier until a mechanism forces them target-innocently.

The whole protocol is a procedure for telling these two apart when the number is pretty and the match is close — the exact conditions under which the distinction is hardest to hold and matters most.

## ★ THE PROTOCOL (run in order; a target-aware number must clear ALL)

**Step 0 — Declare the number target-aware, on the record, before starting.** If the target value is known (as Λ~10⁻¹²² is), name it so. The default verdict is the FLOOR tier (Identified/candidate); promotion carries the burden of positive evidence. Writing "expected default Identified" before the work is what makes a later Derived credible.

**Step 1 — Blind-pin every choice before consulting the datum.** Pin, in writing, BEFORE looking at the observed value:
- the geometric **object** (which operator/rung/kernel),
- the **invariant** computed from it,
- the **convention** for the observable (see Step 4 — this is load-bearing and routinely skipped),
- the **threshold** for what counts as a pass (dex-precision, σ).
A choice pinned after the datum is not evidence; a clue that points you toward the object is not a justification. *(A justification never points at the target.)*

**Step 2 — Provenance-not-value (Rule 11).** Bank a number on WHICH operator/mechanism produced it, never on the value matching. Two numbers sharing a value are DISTINCT if different operators produce them — the value alone can never distinguish them. Corollary: "it equals 122" is not a finding; "this regularized trace produces the exponent, and the exponent happens to be ~122" is the finding. State the operator first, the number second.

**Step 3 — Compute the dispersion floor (the sharpest tool; quantify the fit-space).** Before crediting any match, measure how big the manifold of admissible "matches" is:
- **Form freedom:** how many distinct BST forms already land near the target, and how far do they spread?
- **Convention freedom:** how far does the target itself move under legitimate convention choices?
- **The rule:** if match-precision is FINER than (form-spread × convention-spread), the match is SELECTION, not forcing. A sub-floor "match" inside a wide manifold is the expected null of fishing, not a signal.

**Step 4 — Pin the observable convention BEFORE citing any value.** Distinct, legitimate conventions for the "same" observable can differ by more than the measurement uncertainty. The mechanism must DECLARE which observable it produces before quoting a number, then hit THAT convention's value. If the winning form flips when you change convention, the match is convention-selection.

**Step 5 — Score σ, not %; carry the observational uncertainty; account for look-elsewhere.** Agreement = |pred − obs| / experimental-error, scheme-aware, never raw %. An order-of-magnitude result dressed as a sub-dex match is a Step-5 violation. Look-elsewhere across the many candidate forms and observables.

**Step 6 — Relapse red-flag.** If a "newly derived" form reproduces a PREVIOUSLY-RETIRED target-aware form, that is relapse, not vindication. The retired form was retired for a reason; landing back on it by construction is the tell that the construction was target-aware.

**Step 7 — Verdict discipline.** Stays at the FLOOR tier until a mechanism clears every step above. The verdict is not "how close is the number" — it is "did an operator, pinned blind, produce this exponent without knowing the target, and does it survive the dispersion floor, the convention pin, and the σ score." Only then does it promote off the floor.

## ★ WORKED EXAMPLE — the cc-magnitude (Λ ~ 10⁻¹²²), the instrument's first hostile-grade test
This is why the protocol exists in a sharp form right now. Grounding numbers (Keeper K1065 / K1065a, Lyra F759 — verified):

**Step 3 dispersion floor — the concrete spine (hand this to any reviewer):**
- Three banked forms disagree **by 2.38 dex**: exp(−281)=rank·N_max+g → 10⁻¹²²·⁰; 7·exp(−282)=g·exp(−C₂(g²−rank)) → 10⁻¹²¹·⁶; α⁵⁶ (56=8g) → 10⁻¹¹⁹·⁷.
- The observational target is convention-dependent across **~1.40 dex** (K1065a): Convention A (Λ·ℓ_P², cc as inverse-length²) = 10⁻¹²¹·⁵⁵; Convention B (ρ_Λ/ρ_Planck) = 10⁻¹²²·⁹⁵ — while the MEASUREMENT is pinned to ~0.01 dex.
- **⟹ the match manifold is ~3.4 dex wide. Any sub-dex "match" is form-selection × convention-selection, not forcing.** Hitting ~122 is the EXPECTED null of fishing.

**Step 4 convention pin — the smoking gun already on the record:** 7·exp(−282) matches Convention A to 0.08 dex but is 1.3 dex off Convention B, where exp(−281) is closer. **The winning form flips with the convention.** So the a₀ mechanism must declare Λ-curvature (A) vs vacuum-density (B) BEFORE the number — the heat-kernel structure should fix the convention for you; if it doesn't, the match isn't forced.

**Step 0/7 verdict, pre-committed:** cc-magnitude is **IDENTIFIED at best** until a mechanism clears all seven K1065 criteria. Expected default: Identified. On the record before the derivation starts.

**The single decider (Route a vs Route b):** does the suppression exponent **fall out of a regularized heat-kernel a₀-coefficient computation BLIND to ~122** (Route a → target-innocent → Derived-eligible), or is it **the integer-combination chosen to hit 122** (Route b → target-aware → Identified)? Provenance-not-value settles it. Linear-algebra cast (Casey's standing order): Λ ~ Reg-Tr(a₀ rung)/Vol, the exponent as a spectral invariant of the Laplacian Δ on D_IV⁵ — computed forward, not reverse-engineered from the target.

**K1065's seven criteria (Keeper's, restated as the cc-magnitude instance of Steps 0–7):** (1) target-blindness of the exponent; (2) mechanism, not arithmetic identity; (3) uniqueness — one form by mechanism, or admit form-shopping (the 2.38-dex spread means at most one can be right); (4) predict the value to honest dex-precision with obs-uncertainty carried; (5) coherence with the a₀ ladder + w=−1; (6) the coupling-small mechanism FORCED, not the circular "Λ small because coupling small"; (7) pin the observable convention BEFORE citing any exponent.

## What makes this survive a hostile read
A skeptical referee's move against any "we derived 10⁻¹²²" claim is exactly Steps 3–4: *"you had several forms and several conventions; you picked the pair that matched."* The only answer that survives is one where the criteria were fixed BEFORE the number and the operator was pinned BLIND — so the referee runs the same checklist and lands on the same verdict we did. **The instrument is not a brake on the investigation; it is the thing that lets an eventual Derived be believed.** Look everywhere (no gates on the search); tier honestly at landing.

## Scope and handoffs
- **This is a standing instrument, not a cc-magnitude document.** It applies to every target-aware BST number: mixing angles fit to data, mass ratios where the target is known, any exponent-hunt, and the whole cosmology domain (dense with cheap rationals and moving datasets — see grace_COSMOLOGY_blind_pin_bar_PREREGISTERED).
- **@Keeper / @Cal** — this generalizes K1065; use it as the reusable checklist when the next target-aware number lands. K1065/K1065a remain the cc-magnitude-specific instances.
- **@Lyra / @Elie** — the a₀ derivation is yours; this tells you what "target-innocent" has to mean operationally to clear the bar (Route a, blind to 122, convention declared first).
- **Me (Grace)** — I hold this bar as each number lands: run Steps 0–7, compute the dispersion floor, check the convention pin, score σ, rule at the floor until cleared. I own keeping it current as the instrument sharpens.

— Grace, 2026-08-01 [TEGMARK]. The Blind-Bar Protocol: a standing, pre-registered instrument for target-aware numbers (Steps 0–7: declare target-aware → blind-pin every choice → provenance-not-value → dispersion floor → convention pin → σ-score → relapse flag → floor-tier verdict until a mechanism clears all). Worked on the cc-magnitude: 3 forms × 2.38 dex, target × 1.40-dex convention → ~3.4-dex manifold → any sub-dex match is selection; winning form flips with convention; IDENTIFIED until the exponent falls out of a heat-kernel a₀ computation BLIND to 122. The instrument is what lets an eventual Derived survive a hostile read. Generalizes K1065.
