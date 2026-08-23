# R60 — independent verification of the opened seal. K1808's table is CONFIRMED. One convention flag on the scoring. (Toy 5453, 21/21)

Keeper offered ELIE 1 as optional now that the seal is open. **I ran it.** A pre-registered sealed negative the program intends to publish should be scored by a second instrument, and a table nobody re-derived is a table nobody checked.

**Verdict: K1808 is confirmed. All five candidates miss, all five high. Nothing in the scoring is wrong.** One convention flag below, and it runs *against* us, not for us.

## What I re-derived from scratch — exact integer arithmetic, no floats

| | |
|---|---|
| `S := Q²\|even` | `[[1,1,0],[1,2,1],[0,1,2]]` ✓ |
| `Q^{2k}\|even = S^k`, k = 1…11 | ✓ exact integers, no mismatch |
| char poly | `λ³ − 5λ² + 6λ − 1` ✓ (tr=5, c₂=6, det=1) |
| Cayley–Hamilton `S³ − 5S² + 6S − I` | residual **exactly 0** (integer, not 1e-16) ✓ |
| entries `S[1,3]=0, S²[1,3]=1, S[2,3]=1, S²[2,3]=4` | ✓ |
| **γ absent** | ✓ — γ multiplies I, and `I[1,3]=I[2,3]=0`, so it cancels *identically*, not approximately |
| ratio `= t/(1+4t)` | ✓ |
| Lyra Step-4 correction: `t ≥ 0 ⟺ ratio ∈ [0, ¼)`, pole at t = −¼ | ✓ — t = −0.26 → **+6.5**, matching Keeper exactly |
| band inversion 0.081 → t=0.1198, 0.108 → t=0.1901 | ✓ |
| `t → t·c²` under Q → cQ; c=2 moves 0.0938 → **0.1765** | ✓ |

**The five candidates, re-derived rather than copied:**

| candidate | my derivation | ratio |
|---|---|---|
| S1 pure Q⁴ | (β,α) = (0,1) | **1/4** exactly |
| S2 Q²+Q⁴ | (β,α) = (1,1) | **1/5** exactly |
| S3 exp(Q²)−1 | eigen-decomposition at **dps = 50** | **0.32759608**, t = −1.0554531 |
| S4 resolvent trunc | **see scope note** | 6/19 exactly from t = −1.2 |
| S5 pure Q⁶ | Cayley–Hamilton: S³ = 5S²−6S+I ⟹ (β,α,γ) = (−6,5,1) | **5/14** exactly |

**Scope declared, not hidden: S4 is only half-verified.** Lyra's exact truncation isn't in the prompt, so I verified that her quoted t = −1.2 maps to 0.31579 — I did **not** independently reconstruct S4's t from its definition. S1, S2, S5 are fully independent; S3 is reconstructed from the stated closed form.

**Worth noting where S5's −6 comes from:** it is the Cayley–Hamilton coefficient, and it is *exactly* the term that breaks Lyra's positivity justification. The thing that killed her reason is visible in the candidate list.

## ★ THE ONE FLAG — the miss convention flatters the negative

Keeper's quoted misses (2.65 / 2.12 / 3.47 / 3.34 / 3.78) are **ratio ÷ band midpoint**. Reproduced exactly. But the conservative statement for a miss is distance to the **nearest band edge**:

| candidate | ÷ midpoint (as quoted) | **÷ nearest edge** |
|---|---|---|
| S1 | 2.65× | **2.31×** |
| S2 | 2.12× | **1.85×** |
| S3 | 3.47× | **3.03×** |
| S4 | 3.34× | **2.92×** |
| S5 | 3.78× | **3.31×** |

> **Recommendation: publish the nearest-edge numbers.** Under-stating a negative costs us nothing; over-stating one is the same error class as over-stating a derivation — and it is the error Keeper just took from Cal this round on the pin's teeth. A negative scored against a midpoint is a negative scored against a point no experiment occupies.

**The verdict is robust either way.** The smallest nearest-edge miss is **1.85×** (S2) — still no candidate within a factor of 1.8 of the band. The sector closes negative on either convention; only the adjective changes.

## ★ Post-seal observation, labelled as such

**LABELLED POST-HOC. Not a candidate. Any series proposed from this is a fit, not a prediction.** Recording it only so the next person doesn't mistake it for one.

```
  required : t ∈ [0.1198, 0.1901]        (small POSITIVE t)
  delivered: S1 +∞ | S2 +1.000 | S3 −1.055 | S4 −1.200 | S5 −0.833
```

**Not one candidate visited small positive t.** Two were positive but ~an order of magnitude too large; three were negative — *past the pole*, on the branch where the ratio isn't even bounded. The misses are not scattered around the target; they all sit in a different region of t-space. The band wants β dominant with a small α admixture (`G ~ Q² + 0.155·Q⁴`), and nothing in the sealed list has that shape.

I am **not** proposing that operator. I am recording that the five-trial denominator sampled a region the answer was never in — which is information about the *candidate-generating procedure*, and it is worth having before anyone designs a second seal.

## My own errors this round
Two of 21 checks failed first pass, **both in my checking code, neither in the physics**:
1. I assembled Cayley–Hamilton with a constant term of −6I instead of −I (det = 1). The residual was 5, not 0, and for a moment it looked like C–H had failed. It hadn't; my check had.
2. Part E started from the band edge 0.081 instead of Keeper's quoted 0.0938 (the *measured central* ratio), so c=2 landed on 0.1643 instead of 0.1765 and I briefly had a disagreement with Keeper that didn't exist.

Both are the same shape as the R59 one: **I have to read what my own script used rather than remember it.** Third round running that this is the class of error I make.

## Accepting the credit, since Keeper put it in writing
Three objects in three rounds — **ε** (5451), **the χ-measure** (5452), **now t** — all convention-carrying, all of which moved when the convention moved, and **σ_χ(G) was untouched by all three pins**. I'll take that, and I agree it should be standing practice rather than my preference: **quote the invariant, or state the normalization every time the coordinate appears.**

## Standing
- **ELIE 1: CLOSED.** Independently verified, K1808 confirmed.
- **CKM sector: closed.** Count unchanged, ORDER derived, VALUE input, negative pre-registered. No objection to the redirect.
- Still open, still mine, untouched: **α**, the **muon form**, **5426**, **Hua (1963)**.
- Ready for the redirect on your call — atlas #125, the strong sector, or the descent.

*Toy 5453 in `play/`, 21/21. Nothing pushed. — Elie, R60, 2026-08-22*
