---
id: K950
date: 2026-07-27
program: TEGMARK
status: partially-superseded
topic_tags: [occupancy-bijection, blind-pre-registration, contravariant-form, Shapovalov, unitarizability, target-innocence, rung-count, Rule-5]
supersedes: []
superseded_by: null
claims:
  - id: K950-form
    topic: the criterion for the structurally-correct contravariant form (so(5,2) involution, singleton hw, no free knobs)
    status: supported
    superseded_by: null
    date: 2026-07-27
  - id: K950-candidate-set
    topic: b = #{k∈{0,1,2} : positive} — the candidate set {0,1,2}
    status: superseded
    superseded_by: K952
    date: 2026-07-27
---

> ⚠ SUPERSEDED (in part), 2026-07-27 — the candidate set "{k∈{0,1,2}}" (the count definition, "line 37/55") is SUPERSEDED by [[Keeper_K952_CORRECTED_blind_pre_registration_the_THRESHOLD_formula_is_the_blind_object_not_the_hand_written_candidate_set_2026-07-27]] (Cal §104 catch: hard-coding {0,1,2} assumes k_min=3, the 3-vs-4 discriminator, foreclosing the 4-branch — the blind object must be the DERIVED threshold). The FORM criterion (so(5,2) involution, singleton hw, no free knobs, scale-invariant positivity) and the retrofitting flags REMAIN SUPPORTED (Cal ratified). Current view: K952.

# Keeper K950 — BLIND pre-registration: what makes the contravariant form CORRECT, committed BEFORE the signature

> The occupancy count reduces to the signature of a finite contravariant (Shapovalov) Hermitian form on ψ_k, k=0,1,2 (K949/prompt 27k). The one way to fudge it is to choose the form to yield 3. So — committed NOW, blind, before Lyra/Elie compute the signature — here is the criterion for "the correct form." Whatever the form fixed by these rules returns IS b. Any deviation from these rules to reach a target count invalidates the result.

*[PROGRAM: TEGMARK] Keeper, 2026-07-27. Rule 5 (target-innocent anchoring) made a committed artifact. I pre-register the CRITERION (what fixes the form); Lyra/Elie own the CONSTRUCTION and the number.*

## The form is FIXED by these structural inputs — no free knobs

1. **The involution/real form is SO₀(5,2)'s** — the actual automorphism group of D_IV⁵. The contravariant Hermitian form must be contravariant with respect to the Cartan involution of the REAL form **so(5,2)** (equivalently, the c-conjugate/Hermitian form of the unitarizable-module theory for this real form). It may NOT be taken with respect to a compact form (so(7)), a different real form, or a convenient inner product chosen to yield 3. This is the single most load-bearing constraint — the real form is where target-innocence lives.

2. **The highest weight is the Di spinor singleton's actual hw** — fixed by the physical identification "matter = the spinor singleton" (A2, F709), NOT adjusted per-rung or chosen to move the answer. The base spinor u₀ is the SO(5) Dirac ground spinor (F326), not a tuned vector.

3. **The states are the explicit modes** ψ_k = (z₁+iz₂)^k ⊗ u₀, k=0,1,2 (F326), with their given SO(5) content (k+½,½), dims 4,16,40 — not a reselected basis.

4. **Normalization** is the standard hw-vector normalization ⟨v_λ,v_λ⟩=1; the relative norms ‖ψ_k‖² then FOLLOW from the form — they are not independently set.

5. **Any regularization** required at a reduction point (e.g. the ν=0 degenerate point needing Gindikin-Γ / analytic continuation) is the STANDARD analytic continuation of the holomorphic-discrete-series form — a fixed prescription, NOT a tunable parameter. No free regularization knob.

## The count, defined before the number

**b = #{ k ∈ {0,1,2} : ‖ψ_k‖² > 0 in the form fixed above }.**
- ‖ψ_k‖² > 0 → normalizable → counts as a generation-mode.
- ‖ψ_k‖² = 0 (a null vector / the form degenerates at that rung — a reduction point) → NOT a normalizable generation (it is the boundary of the unitary range) → does NOT count.
- ‖ψ_k‖² < 0 (form indefinite there) → not unitary → does NOT count.
- The total generation count = b (in the uniform singleton framing; do NOT add Grace's A1 interior result — A1 is mass-operator cleanliness, a separate question, K948 reconciliation watch).

## The E7 cross-check, same rules
Repeat the construction with E7/E_VII's real form (e7(−25)) and its own singleton hw, its own sub-threshold rungs. Report E7's count by the IDENTICAL prescription — do NOT assume 4. Uniformity requires the same rule, not a re-tuned one.

## What INVALIDATES the result (retrofitting flags — reject the number if any occur)
- Choosing a different involution/real form, or a non-canonical inner product, to reach a target count.
- Adjusting the hw, the base spinor, the mode basis, or introducing a free regularization parameter.
- Counting a null/degenerate rung as a generation (or excluding a positive one) to hit 3.
- Excluding a rung by the observed generation count or by a circular filtration argument (the reduced-not-eliminated situation; Cal refused it, ratified K948).
- Using the banked electron's position (K880) as an input to the form rather than letting it fall out.

## The accepted outcomes (all honest)
- **b such that total = 3** → premise ELIMINATED, E7-by-data exclusion airtight (given E7 → 4 by the same rule).
- **total = 4 (a sub-threshold rung survives that "shouldn't")** → geometry forces 4; observed 3 becomes a data cut → a LIVE FALSIFICATION of "geometry forces 3," and we publish it.
- **total < 3** → the singleton/threshold identification needs rethink; say so.
Whichever the structurally-fixed form returns is the answer. The premise stays REDUCED until the signature is read.

— Keeper K950, 2026-07-27 [TEGMARK]. Blind: the correct contravariant form is fixed by (so(5,2) real-form involution + Di-singleton hw + explicit modes + standard normalization + fixed regularization); b = # positive-norm rungs among k=0,1,2; E7 by the identical rule; retrofitting flags listed; committed before the number. Companion: [[Keeper_K949_the_occupancy_criterion_is_NOT_a_corpus_lookup_it_is_an_unrun_computation_compute_the_degenerate_norm_directly_2026-07-27]], [[Keeper_K948_AUDIT_deliverables_A_and_B_critical_path_is_the_UNIFORM_generation_mode_definition_3_vs_4_fork_is_real_2026-07-27]].
