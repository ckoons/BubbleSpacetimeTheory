---
id: K949
date: 2026-07-27
program: TEGMARK
status: current
topic_tags: [occupancy-bijection, EHW, normalizability, sub-threshold, degenerate-norm, Shilov-measure, b-count, 3-vs-4-fork, target-innocence, K880]
supersedes: []
superseded_by: null
claims:
  - id: K949
    topic: is the sub-threshold normalizability criterion a corpus lookup or an unrun computation
    status: current
    superseded_by: null
    date: 2026-07-27
---

# Keeper K949 — the occupancy criterion is NOT a corpus lookup; it is an UNRUN computation. Compute the degenerate norm directly.

> **The sourcing (my own sweep) came back honest, not flattering: the corpus does NOT contain a criterion that decides b. It has the SCALAR threshold (k_min=3) and the SCALAR Wallach set as lookups; it does NOT have the SPINOR/Di sub-threshold unitarizability criterion the fermions actually need, and it has NOT executed the correct degenerate norm for the ψ_k modes. So the fulcrum's final step is a genuine, bounded, UNRUN computation — not a lookup. Elie was handed a computation, not a criterion. Do NOT assume b=1; the target-innocent lower bound is itself unrun.**

*[PROGRAM: TEGMARK] Keeper, 2026-07-27. The sweep could have flattered ("here's the criterion, run it"); it honestly reports the criterion isn't there. Two-directional discipline on my own "run the count" framing.*

## What IS a lookup (GIVEN — Elie may use)
- Threshold **k_min = ⌈(n+1)/2⌉ = 3** for D_IV⁵ (EHW / Vergne-Rossi 1976). SOURCED.
- The SCALAR Wallach set **W = {0, 3/2} ∪ (3/2, ∞)** (ν = k/2). SOURCED.
- The explicit modes ψ_k = (z₁+iz₂)^k⊗u₀, k=0,1,2, SO(5) content (k+½,½), dims **4, 16, 40** (F326; toy 4884 confirms). k=0's dim-4 = Di spinor lowest K-type (a passing check).
- That k=1,2 are sub-threshold and hence NOT scalar-Bergman-normalizable (∫|f_k|²dμ_B = ∞, proved).

## What is NOT in the corpus (the gap)
- **The full EHW SPINOR sub-threshold criterion** — the per-K-type reduction-point condition that says which sub-threshold *spinor* modes are unitary — is NOT transcribed. Only the scalar threshold is. (Primary sources: EHW 1983, Jakobsen, Enright-Parthasarathy — none cited at page level in the corpus.)
- **The correct degenerate norm, executed for ψ_k.** The corpus correctly says the naive Bergman integral is WRONG below threshold and identifies the right object (continuum ν>3/2 = Bergman L²; the degenerate points {0,3/2} = Shilov/Hardy inner product, ν=0 needs Gindikin-Γ / Shilov-measure regularization). That measure is a standard construction (FK Ch. XII-XIII, Gindikin, Berezin) — but it has NOT been built and applied to the ψ_k. **"The measure is standard" must not masquerade as "the count is done."**

## The honest count (the target-innocent computation, in ONE framing)
Use Lyra's uniform singleton framing (F709): the count = **#{ k ∈ {0,1,2} : ψ_k is normalizable under the CORRECT degenerate/Shilov norm }**. This is a single finite computation, not "2 interior + b." Grace's A1 (φ color-blind → mass operator diagonalizes) is a SEPARATE question (mass-operator cleanliness on the interior subset), not part of the count — do not add them.
- The number could be **3** (all three rungs normalizable → premise eliminated), **fewer** (the "2 interior + no boundary generation" or other outcome), or the truncation could fail (Di tower is INFINITE, F338 — the cap at 3 is NOT free). **Genuinely unrun; do not assume 3 and do not assume b=1.**

## The K880 subtlety — even b ≥ 1 is not yet target-innocent
Cal's "b ≥ 1 confirmed (electron at k=1)" rests on the banked electron mass putting a mode there — i.e. it is OBSERVATION-anchored, not structure-anchored. Under the SCALAR criterion the k=1 electron (ν=1/2) is NOT in the Wallach set → not normalizable; under the correct SPINOR/degenerate norm, whether it is normalizable is UNANSWERED. So the fully target-innocent lower bound (is k=1 normalizable under the correct norm, computed from structure) is ITSELF unrun. The count is honestly **#{normalizable rungs} ∈ {0,1,2,3}-until-computed**, and the electron's placement carries the K880 fit until the structural norm confirms it.

## THE STEER — Path B: compute the degenerate norm directly (Casey's frame)
Do NOT wait on / hunt for the abstract EHW spinor classification. **Construct the correct degenerate/Shilov norm** (the standard FK Ch. XII-XIII + Gindikin-Γ regularization the corpus already identifies) and **compute ‖ψ_k‖² directly** for k=0,1,2 on D_IV⁵, and the same for the E7 analog. Count the finite ones. This is the finite, un-gameable, one-domain computation Casey steered toward (linear algebra + a definite integral under the right measure).
- **★ The MEASURE is load-bearing and structurally determined (Rule 5).** It is NOT a free choice — it is fixed by the FK/Gindikin construction. Using a convenient regularization that yields the wanted count would be the fit the whole exercise exists to avoid. The norm must be the structurally-correct one; whatever it gives is b.
- **E7 → 4 is currently an ASPIRATION** (F709 open; the KW-strata route is self-superseded to REDUCED, K944). The E7 rung count under the SAME correct norm is unrun — compute it, don't assume 4.

## Honest state
The fulcrum is a bounded but genuinely UNRUN computation — construct the correct degenerate norm and count the normalizable rungs, for D_IV⁵ and E7 — with a live 3-vs-4 (and 4-vs-5) fork. It is NOT near-closure and NOT a lookup. The premise stays REDUCED, and — the sharp point — the criterion, correctly sourced, does NOT tell us whether b is 1 or 2; that IS the computation. Hand Elie the measure construction (standard) and the guard (the measure is not a free choice); the answer is whatever the geometry gives.

— Keeper K949, 2026-07-27 [TEGMARK]. The criterion is not a corpus lookup — it's an unrun computation; the SPINOR sub-threshold criterion isn't transcribed and the degenerate norm isn't executed for ψ_k. Path B: build the correct Shilov/Gindikin-Γ norm and compute ‖ψ_k‖² directly (D_IV⁵ + E7); the measure is structurally fixed (Rule 5), the count is 3-or-fewer-or-fork, genuinely unrun; even b≥1 leans on the K880 fit until the structural norm confirms k=1. Companion: [[Keeper_K948_AUDIT_deliverables_A_and_B_critical_path_is_the_UNIFORM_generation_mode_definition_3_vs_4_fork_is_real_2026-07-27]], [[Keeper_K945_occupancy_derivation_SCOPE_real_crux_is_strata_vs_Ktypes_target_innocent_route_is_the_singleton_three_fit_flags_to_clean_2026-07-27]].
