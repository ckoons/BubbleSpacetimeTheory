# LEAD (Casey, 2026-08-13) — the Millennium work should be reframed around COMPOSITE numbers and GAPS, not PRIMES

*Filed by Keeper for the scheduled Millennium proof review. This is Casey's steer, expressed as faithfully as I can; the review takes it as a working hypothesis, not a settled thesis.*

## The steer, in one line
> "I think 'prime' is the wrong concept. The work should be about composite numbers and the 'gaps' — similar to spectral gaps, where we show the continuum can't reach without counting." — Casey

## What Casey is correcting
Several current Millennium attempts lean on **primality** as the load-bearing idea:
- $g = 7$ **prime** ("spectral integrity: the genus must be prime or the lattice factorizes"), Mersenne $2^g - 1 = 127$, the Hamming/perfect-code story, $N_{\max} = 2^g + N_c^2 = 137$ prime, the BSD "all $\binom{g}{k}$ odd via Lucas" route, etc.

Casey's claim: **primality is the wrong organizing concept.** It reads as a numerological property of a number, and it's exactly the kind of thing that invites the "why this number" objection. The organizing concept should instead be:

1. **Composite structure** — the number's factorization / how it is *built from parts*, not whether it resists building. A composite carries a counting structure (its factors, its divisor lattice); a prime is defined by the *absence* of one. BST is a theory of *how things are assembled from the five integers* — composites are the native objects; primes are the anomalies.
2. **Gaps as spectral gaps** — the real phenomenon is that a **continuum cannot reach a value without a discrete counting step.** This is literally the Yang-Mills mass gap: the scale-free (continuum) flat $\mathbb{R}^4$ theory *cannot* produce the gap; you need curvature, which is counting/discreteness. The gap is the place where the continuum runs out and counting takes over.

## The unifying picture (the review's job to test)
Reframe each Millennium problem as **"the continuum can't cross this gap without counting":**
- **Yang-Mills** — the exemplar, already in hand: no scale-free continuum manifold has a mass gap (the R⁴ no-go, Weyl criterion); curvature = the counting that opens the gap. *This is the template.*
- **Riemann Hypothesis** — the zeros cannot leave the critical line: a gap the continuum (off-line region) cannot enter. Recast the temperedness/forcing argument as "the continuum of off-line positions is unreachable without a discrete (counting) obstruction."
- **P ≠ NP** — a complexity gap the polynomial continuum cannot cross: the counting step (witness / parity erasure) is what the continuum of polynomial extensions cannot reach.
- **Four-Color** — the forced-fan / pigeonhole step is a counting obstruction; the continuum of colorings can't avoid it.
- **BSD, Hodge, Navier-Stokes** — test whether each has a "continuum-can't-reach-without-counting" spine hiding under the current primality/definitional framing.

## Why this is the right BST frame (connections to the corpus)
- **Casey's Principle**: entropy = force = counting; Gödel = boundary = definition. The gap is exactly where counting becomes *forced* — the boundary between what the continuum reaches and what only counting reaches.
- **The Curvature Principle** ("you can't linearize curvature"): curvature is the discrete/counting content the continuum (linear, scale-free) cannot capture. The mass gap is the first clean instance; the reframe says the others are instances too.
- **Limits are lossy** (integrals preserve, limits destroy): the *continuum limit* is precisely where the counting information is destroyed — so "the continuum can't reach it" is the same statement as "the limit threw away the count."
- **Discrete-first** (derive discrete, recast continuous onto discrete): the reframe *is* discrete-first applied to the Millennium problems — stop asking the continuum to reach the answer; show the count it can't reach without.

## What the review should do with this
1. For each of the seven, ask: **is the real content a spectral-gap / continuum-can't-reach-without-counting statement?** If yes, rewrite the spine that way and see if the "definitions to overcome" (Casey: "the others have definitions to overcome") dissolve into a clean gap statement.
2. **Demote the primality language** wherever it is load-bearing to a *consequence* rather than a *cause* — e.g., $g=7$ being prime is a fact, but the load-bearing thing is the composite/gap structure it sits in, not the primality itself.
3. Keep the honest tiers from K940 / this morning's Guide sweep: YM + 4-color + NS "move the needle"; RH / BSD / P≠NP / Hodge "have definitions to overcome." The reframe is aimed squarely at those definitions.

## The steer reaches past the Millennium proofs — into the uniqueness argument (Keeper, added 2026-08-13)
While sweeping the Guide, Keeper found the reframe touches the **forcing chain that selects D_IV⁵ itself** (Vol2_Framework/Ch01_Foundations, Step 3 / T953). Two of the five minimum-requirement conditions rest on **primality**:
- Condition 3: "the Bergman genus must be **prime**, or the spectral structure factorizes into sub-lattices" (also mislabels g=7 as the "Bergman genus" — settled convention: genus = n_C = 5; g = 7 is the signature).
- Condition 4: "N_max must be **prime** — a composite N_max decomposes the fine-structure constant into interfering sub-channels."

**Both are secretly gap/indecomposability conditions, with primality as a symptom, not a cause:**
- Condition 3 → "the spectral lattice must not factorize" (indecomposability). Primality of g is *sufficient* for that but is not the content — the content is that the continuum can't split the lattice without a counting obstruction.
- Condition 4 → "the fine-structure channel must not decompose into interfering sub-channels." Again a non-factorization / gap statement; N_max prime is the consequence.

So the review should test whether **rewriting conditions 3 and 4 as composite/gap (non-factorization) conditions** (a) removes the "why must these be prime" objection from the uniqueness argument, and (b) is actually the *truer* statement of what the geometry requires. This would strengthen the T953 uniqueness result the same way the reframe strengthens the Millennium proofs — by naming the gap, not the primality. (Do NOT edit these unilaterally: they intersect Grace's catalog-owned g=7-genus relabel and are review-level.)

## Honest status
This is a **research lead**, not a result. It may sharpen several attempts; it may not fit all seven. The review tests it problem by problem. Tier: LEAD (Casey-originated, unworked). Related: [[feedback_curvature_principle]], [[feedback_caseys_principle]], [[feedback_discrete_first_pull_continuous_onto_discrete]], [[feedback_limits_lossy]].

— Keeper, 2026-08-13. Nothing pushed.
