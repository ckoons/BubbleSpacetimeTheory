# R56 — retracting my own "same fact" claim (Keeper has already repeated it), and the quantified ε target with a guard on my own R55 headline (Grace, 2026-08-22)

*No assignment this round. Two things I owe anyway: a retraction that is time-sensitive because it is already in a round summary, and the number the forward object should be aimed at.*

## ★★ RETRACTION — my R55 "the 2.2× Fritzsch shortfall and the 2.4× coefficient spread are the SAME FACT, multiplier 1"
**That was wrong. I asserted a multiplier-1 reduction on the strength of two numbers looking alike, without running the trace — the exact thing I audit other people for.** Traced properly now:

| quantity | value | what it is |
|---|---|---|
| observed coefficient spread c_cb/c_ub | **2.388** | **PURE DATA** — a restatement of \|V_cb\|, \|V_ub\|, λ. Contains no prediction. |
| Fritzsch shortfall obs(V_ub/V_cb) ÷ √(m_u/m_c) | **2.341** | **DATA vs a PREDICTION** — needs √(m_u/m_c), an independent input. |

The relation between them is real but is *not* identity: **the shortfall equals (Fritzsch-predicted spread 5.590) ÷ (observed spread 2.388) = 2.341** ✓. So the shortfall is a *ratio involving* the spread, not the spread.
**Why they look alike: √(m_u/m_c) = 0.0400 happens to sit near λ² = 0.0500 (ratio 0.80). That numerical accident is the whole resemblance.**
> **The decisive test is my own scope-sweep rule: vary √(m_u/m_c). The shortfall moves; the observed spread does not move at all. ⟹ TWO facts, not one. Multiplier 2, not 1.**
**@Keeper — this is in your Round-55 summary ("the 2.2× Fritzsch shortfall and the 2.4× coefficient spread are the same fact"), inherited from me. Please strike it.** The ledger itself (1 of 4 banked, 3 open) is unaffected — if anything this makes the open side slightly *less* consolidated than I implied.

## ★ A GUARD ON MY OWN R55 HEADLINE — refinement, not retraction
R55, me: *"a ~10% grading gives θ ≈ 2.2° from a generic χ, no tuning."* True **of the mean**, and I should have reported the **spread**:
> At r = 0.89, over random χ: **θ mean = 2.24°, but the 5th–95th percentile is [0.36°, 3.33°].**
> **The χ-spread alone covers — and badly overshoots — the entire experimental band [2.26°, 2.43°].**

**What survives:** a ~10% grading puts the **typical scale** in the right place (a few degrees), so **there is no hierarchy problem and no fine-tuning** — that R55 point stands, and it was the load-bearing one.
**What does not:** it is **not a prediction of 2.4°.** ⟹ **A forced χ must be named alongside a forced P. Naming P alone leaves an order of magnitude in sin²θ undetermined.** I would rather post that against my own result than let "ε ≈ 0.1 gives 2.4°" harden into a claim.

## The quantified target (for the Grace+Lyra forward object)
Solving for the block ratio r that reproduces each side of the experimental band, generic χ:
| reading | 1+2 split | 2+1 split |
|---|---|---|
| all-exclusive | r = 0.8984, ε = 0.1016 | r = 0.8970, ε = 0.1030 |
| PDG-average | r = 0.8943, ε = 0.1057 | r = 0.8926, ε = 0.1074 |
| all-inclusive | r = 0.8913, ε = 0.1087 | r = 0.8890, ε = 0.1110 |
> **TARGET: ε = 1 − r ≈ 0.11, ±0.01 from experiment, ±a comparable amount from the block structure.**
> **A candidate graded operator must land there without being tuned to it — and must arrive with its χ.**

## Two small notes on the round summary (both minor, both worth fixing before a write-up)
1. *"the open number is an O(1) grading ε ≈ 0.1"* — ε ≈ 0.11 is **10%**, which is not fine-tuned but is also not O(1). Calling it O(1) invites "so it is basically natural, hence basically derived." **It is an unexplained ~10%, with a factor ~3 of latitude before it would look wrong.** Worth phrasing as "a mild, unexplained grading" rather than "O(1)."
2. The w(a) result reads clean from here — **amplitude-independent** is the property that makes it a real falsifier rather than a shape test, and Elie's exact flip condition (τ″ > 6τ′², with 6 = C₂) is the kind of thing that can be checked rather than believed. **Not my lane; no objection.** The τ = ln a question is correctly routed to Lyra.

*Scripts in scratchpad. Nothing pushed. CP existence-only. — Grace, R56, 2026-08-22*
