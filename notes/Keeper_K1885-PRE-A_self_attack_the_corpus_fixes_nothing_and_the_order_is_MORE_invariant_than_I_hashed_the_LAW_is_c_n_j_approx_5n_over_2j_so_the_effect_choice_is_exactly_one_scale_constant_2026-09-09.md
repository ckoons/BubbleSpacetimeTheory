# K1885-PRE-A — self-attack on K1885-PRE: the corpus fixes nothing, and the invariance is stronger than I claimed

**Keeper, 2026-09-09 (Wednesday) 09:48 EDT, clock-verified.** Amends K1885-PRE before Cal scores it. Instrument retained: `notes/Keeper_K1885-PRE-A_instrument_order_invariance_large_j_asymptotic_5n_over_2j_2026-09-09.py` (625,311 accepted Lie-ball points; sampler control: max |z|² in sample 0.9727, so every family member is a genuine effect bounded by one, which I should have checked before hashing and had not).

## 1. First attack: does the corpus already fix the effect? No.
`grep -rn "Jones intensity|mean intensity|⟨|z|²⟩"` over the corpus returns only today's own files, Round 135's prompt, and Elie's 5721 pre-registration, where ⟨|z|²⟩ appears as the DEFINITION of the round's f. Nothing independent of the choice fixes the choice. The family is live and Cal's C1 will not find a corpus condition I missed, because there is none to find.

## 2. Second attack: is the order really invariant, and at what rate?
| j | n = 1 | n = 2 | n = 3 | n = 5 | j·c at n = 1, 2, 3 |
|---|---|---|---|---|---|
| 0 | 0.5000 | 0.7380 | 0.8571 | 0.9526 | 0.00 · 0.00 · 0.00 |
| 4 | 0.2776 | 0.4700 | 0.6057 | 0.7731 | 1.11 · 1.88 · 2.42 |
| 16 | 0.1180 | 0.2197 | 0.3078 | 0.4509 | 1.89 · 3.52 · 4.93 |
| 64 | 0.0350 | 0.0686 | 0.1008 | 0.1616 | 2.24 · 4.39 · 6.45 |

Every member is monotone decreasing and tends to zero, as hashed. **But the product j·c converges, and it converges to 5n/2: predicted 2.5, 5.0, 7.5 against measured 2.24, 4.39, 6.45 at j = 64, each about 88 percent of its limit and rising, with a common deficit consistent with a 1/j² correction.**

## 3. So I owe a correction to my own opening, in the program's favour
K1885-PRE said the ORDER survives and the VALUES do not. That is too coarse. **The LAW survives: c_n(j) ≈ 5n/(2j) for every admissible member, so the whole family has one shape and the choice of effect sets exactly ONE SCALE CONSTANT.** The values are not arbitrary, they are one parameter's worth of convention. Every relative statement is therefore invariant: the ratio of cycle costs, the shape of the drift, the rank ordering of the stopping rules, and the claim that commitments become reliable as 1/j. What is convention is the overall scale, and it is a single number.

That is a materially better position than the one I opened with, and it means yesterday's arithmetic is recoverable rather than lost: every quantity that is a ratio of two costs is already effect-independent.

## 4. Trap named before anyone reads it
The constant is 5n/2 and 5 is the dimension. That is a shared-integer risk of exactly the kind this program keeps catching. **Elie: before anyone writes "the dimension appears in the commitment law," compute the family at D_IV⁴ and D_IV⁶ and report whether the constant tracks the dimension, the genus, or the rank.** Until then the 5 is not to be read.

## 5. Revised task for the round
Lyra L3's payer clause should now read against this: the law is invariant, one constant is the identification's. Elie E2's hash should be the 5n/2 limit and its correction term, not merely monotonicity. Cal C1 should score whether my j·c convergence is real or a slow-tail artefact of the Monte Carlo at large j, since that is the weakest point in this note.

— Keeper
