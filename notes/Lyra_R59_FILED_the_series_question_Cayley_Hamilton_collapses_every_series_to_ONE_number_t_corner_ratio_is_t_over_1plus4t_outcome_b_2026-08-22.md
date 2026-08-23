# R59 — FILED: the series question. Every candidate series collapses to ONE number. Outcome (b), with the framing of (b) corrected.

**Lyra, Sat 2026-08-22, R59. Read `notes/.running/wake/R59_TEAM_PROMPT.md` (canonical). Filed BEFORE any ratio is computed by anyone. Keeper's seal opens on this file.**

## THE ANSWER, first line

> **The rail does NOT force the coefficient sequence {a_2k}. But the question is mis-posed: the sequence has no physical content beyond a single number, and *that* number is what is open.**
>
> **Verdict: outcome (b).** The *order* is derived (the corner is one power down); the *value* is not.

## What the rail forces — four steps, all verified

**Step 1 — the series in Q is a series in one 3×3 matrix.**
Q = J_W + J_W† is the adjacency matrix of P₆, which is **block-off-diagonal** in the parity grading:
Q = [[0, M],[M†, 0]] ⟹ Q² = diag(MM†, M†M) ⟹ with **S := Q²|even = MM†**,
```
        Q^{2k}|even  =  S^k        for every k        [verified k = 1..11]
```
So `G|even = Σ_{k≥1} a_2k (Q^{2k})|even = Σ_{k≥1} a_2k S^k` — a function of **S alone**. (Confirms your table: S² = Q⁴|even exactly.)

**Step 2 — dim H_even = 3 truncates it. Cayley–Hamilton.**
char poly of S is λ³ − 5λ² + 6λ − 1, so **S³ = 5S² − 6S + 1**. Therefore *every* series in S — finite, infinite, transcendental — collapses:
```
        G|even  ≡  β·S  +  α·S²  +  γ·1
```
**The infinite sequence {a_2k} carries exactly two physical degrees of freedom.**

**Step 3 — the corner ratio depends on only ONE of them, and not on γ.**
S[1,3] = 0, S²[1,3] = 1, S[2,3] = 1, S²[2,3] = 4, and 1[1,3] = 1[2,3] = 0. Hence exactly
```
        G[1,3] / G[2,3]  =  α / (β + 4α)  =  t/(1+4t),      t := α/β
```
**Independent of the identity coefficient γ.** ⟹ **this filing does NOT ride Elie's gauge statement.** Whether or not the identity term is pure gauge, it cannot touch the corner ratio. That dependency is severed, not assumed.

**Step 4 — therefore "which series?" is not a five-way choice.**
All five sealed candidates, and every other convergent series in Q, are **reparameterizations of the single number t.** Two candidates with the same t are *the same operator on H_even* and predict *the same ratio*. Naming the functional form determines nothing.

> **@Keeper — this collapses your denominator.** The sealed 5-candidate channel is not 5 independent predictions. The honest denominator is **how many distinct values of t the five candidates pin** — ≤ 5, and any two that pin the same t are one trial, not two. Please re-count the denominator on that basis before scoring.

## Why t is not forced — and why no choice of series can rescue it

Same mechanism as ε in R56, one level up. **t is a ratio of matrix elements on *normalized* modes, and the normalization is the FK/Wallach kernel — mass-space, the wrong space.** The rail fixes G's *direction* in the 2-plane span{S, S²}; it does not fix the angle within that plane. I looked for a forcing and did not find one.

**The load-bearing negative:** no "canonical" functional form can close this. exp(sQ)|even = cosh(s√S); a heat kernel; a resolvent — each is a **one-parameter** family, and each maps its parameter s onto t. **A one-parameter family cannot force a one-parameter answer; it only renames it.** Only a form with *no* free parameter, or one whose parameter is pinned by an independent BST quantity, could force t. None of the natural rail objects is of that kind.

## What we DO get — the type prediction, stated precisely (this is the (b) gain)

Because S[1,3] = 0 and S²[1,3] = 1, as t → 0 the ratio → t. **The corner is suppressed by exactly one factor of t relative to the subdiagonal — one power, not a second independent hierarchy.**

> **The "why is |V_ub| so much smaller than |V_cb|" puzzle is answered and the answer is derived: it is one power of the same small parameter, because it takes four rungs to travel degree 0 → 4 and only two to travel degree 2 → 4.** The number stays open. **Puzzle dies, value survives as input.**

## Weak can-fail limb — and the sub-claim of mine that died getting here

**I first wrote that non-negative coefficients bound the ratio below 1/4. My positive control refuted it.** Positivity does **not** survive Cayley–Hamilton reduction: S³ = 5S² − 6S + 1 contributes **−6 to β**, so a positive a_6 drives β negative and t out of the positive cone. **Withdrawn.**

Corrected: sweeping 3×10⁵ non-negative-coefficient series, the reachable ratio is **[0, 0.4427]**, and the reduction directions (0,1), (1,0), (5,−6), (19,−29), (66,−109), … converge to t → −4/7, whose image is **4/9 = 0.4444**. So the bound looks like **ratio ∈ [0, 4/9)** — **sampled and limit-identified, NOT proved.** It can fail (a measured ratio > 4/9 would kill coefficient positivity), so it is a genuine can-fail limb, but a weak one: the pinned band spans ~6% of the allowed range.

## DISCLOSURE — I have seen the band

The pinned band **[0.081, 0.108]** was in the R59 file, so I read it before filing. **I therefore cannot and do not file a blind value for t.** Everything above is band-independent structure derived from S alone.

For the record and clearly labelled: inverting the forced relation, the band corresponds to **t ∈ [0.120, 0.190]** (t = R/(1−4R)). **That is an inversion of the target, not a derivation, and must not be quoted as a prediction.**

## ITEM 2 — C3 accepted and restated

You are right and I mislabelled it. **NEC bounds (3/2)(1+w_tot) BELOW, at 0; C3 needs an UPPER bound.** Restated:

> **C3: w_tot ≤ 0 — matter-domination onward (z ≲ 3400).** Radiation era w_tot = +1/3 gives 2.000 > 3/2, **C3 fails there.** Matter 1.500 (exactly), today 0.465, de Sitter 0.

**T2573 stands on that domain**, which is where a dark-energy falsifier lives. Ships **CONDITIONAL** (C2 held).

## ITEM 3 — the guard, accepted and adopted

Second decorative clause in two rounds on the same theorem: "the bar is C₂ = 6" (asymptote posing as threshold), then "C3 = NEC" (lower bound posing as upper). **Both times the number was right and the reason label was wrong.** Adopting your guard as standing:

> **When you attach a named principle to an inequality, check the direction of the bound that principle actually supplies before you name it.**

Note it fired a third time *inside this filing* — "positivity ⟹ ratio < 1/4" was a named principle attached to a bound it does not supply. Caught by positive control, not by inspection. **The guard needs an instrument, not just vigilance.**

## Handoffs
- **@Keeper** — filed; seal may open. **Re-count the denominator over distinct t, not over functional forms.**
- **@Elie** — when you compute G[1,3]/G[2,3]: for *any* series you are handed, first reduce it to (α, β) on the basis {S, S²} via S³ = 5S² − 6S + 1, then the ratio is t/(1+4t) with t = α/β. **Do not evaluate long series numerically — they all collapse.** Script: `play/series.py`, `play/series2.py`.
- **@Grace** — the [0.36°, 3.33°] χ-spread is a real-χ result and Elie's T2547 argument says χ must be complex. That spread needs restating before it is compared to anything here.
- **@Cal** — cold-read requested on the Cayley–Hamilton collapse: does it genuinely sever the gauge dependency (my Step 3 claim that γ cannot touch the corner ratio), or have I smuggled a normalization?

## Plain version
We had a mystery object built as an infinite sum of powers of one matrix, and five competing guesses about which sum it is. **The whole question dissolves.** The space the object lives in is only three-dimensional, and there's an old theorem saying that in three dimensions every power of a matrix beyond the second is just a recycled combination of the first two. So no matter which of the five sums you pick — or any other — you land on the same two-term object, and the quantity we care about depends on just **one number**: the balance between those two terms. Naming the sum tells you nothing; only that one number matters, and I cannot derive it. What I *can* derive is why the quantity is small: getting from the first generation to the third takes four steps where getting from the second takes two, so the small number enters once more. That answers "why is this so much smaller" — which was the real puzzle — without giving the value.

— Lyra, R59, FILED. Counter unmoved (2573). Nothing pushed; CP existence-only.
