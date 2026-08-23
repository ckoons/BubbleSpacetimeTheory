# The CKM sector — PARTIALLY DERIVED, explicit-split ledger (Grace, CLOSING artifact, 2026-08-22)

*Per the standing rule: **PD is a real external tier ONLY in explicit-split form.** This is that form, updated to the sector's closing state after the K1800 seal opened. Every line states which side it is on and why. Confirmed against the corpus, not from memory. Supersedes the 14:39 checkpoint version.*

## DERIVED
| item | value / content | provenance |
|---|---|---|
| **Skeleton** — which entries vanish at first order; the cross-parity selection rule | even↔odd bridge; direct overlap vanishes ⟹ mixing must be a current matrix element | K1324 (three blind routes); K1182/K1183 |
| **Hierarchy ordering** — the λ-POWERS | \|V_ub\| ≪ \|V_cb\| ≪ \|V_us\| ≪ 1 with the correct powers | Cal §551; K1629 |
| **θ₁₂ (Cabibbo)** | **V_us = 1/√20 = 0.22361** (obs 0.2245) — blind, forward, frame-independent | **T2530**, from the Derived m_s/m_d = 20 (T2529) |
| **CP violation — EXISTENCE** | J ≠ 0 forced | T2547 — **existence only** |
| **Flavor-universality = the partial-isometry condition** | V = A†JB unitary ⟺ the current couples all three generations equally ⟹ **CKM = U_up†U_down is the forced survivor** | R52; gates `gate_partial_isometry_intrinsic.py`, `..._mixing.py` |
| ★ **THE ORDER OF THE SPLIT** *(new — R59/R60)* | **The (1,3) corner is suppressed by exactly ONE power of t relative to the (2,3) subdiagonal, because 0→4 takes four rungs on P₆ and 2→4 takes two.** Every series — finite, infinite, transcendental — collapses to G\|even = βS + αS² + γ·1 (Q^{2k}\|even = S^k, k=1…11; char poly λ³−5λ²+6λ−1, Cayley–Hamilton residual 0.00e+00), giving corner ratio **t/(1+4t)** with γ genuinely absent. ⟹ **"Why is \|V_ub\| so much smaller than \|V_cb\|?" is answered, not fitted.** | Lyra (series), Keeper (verified exactly), Grace R57 (pre-registered as a prediction of TYPE) |

## ★ NEGATIVE — pre-registered, sealed, opened (a banked asset, not an absence)
| | |
|---|---|
| **All five candidate series MISS the pinned band [0.081, 0.108]** | S1 pure Q⁴ 0.2500 (2.65×) · S2 Q²+Q⁴ 0.2000 (2.12×) · S3 exp(Q²)−1 0.3276 (3.47×) · S4 resolvent trunc 0.3158 (3.34×) · S5 pure Q⁶ 0.3571 (3.78×) |
| status | Sealed **SHA256 43ad5eb3…f43488**, hash verified intact, opened only after Lyra filed the series in writing. **All five high, none close.** |

**This is the strongest form of negative the program produces — the procedure was frozen before the number existed.** *(The procedure-freeze itself came out of this sector: a bar handed alongside an unfrozen procedure is a tuning channel.)*

## INPUT — NOT DERIVED (three parameters)
| item | status |
|---|---|
| **V_cb** | **VALUE RETIRED, POSITION KEPT.** The ~0.044 RMS-projection value is dead: its license was *"a ~5% match against ~5%-uncertain data"* and the data sharpened — **+10.6% = 8.9σ vs exclusive 39.77×10⁻³; +4.4% = 3.61σ vs the independently-pulled inclusive 42.16 ± 0.51×10⁻³; outside the union band at both ends, with no pre-registered side.** **KEPT at Identified:** V_cb is a *down-sector-only* reading because the up 23-mode refracts past the boundary (radius 1.225 > 1) and vanishes → the top decouples (K711/K1001/K1012). **A position has no measurement as its license, so sharper data cannot kill it.** |
| **The magnitude of the split** | **OPEN.** Observed ratio ≈ 0.093 ⟺ **t ∈ [0.120, 0.190]** at P₆. **The ORDER is derived; the VALUE is not.** |
| **δ_CP magnitude** | **OPEN.** T2547 banks existence only. |

> ## **COUNT: 1 of 4 CKM parameters DERIVED. 3 OPEN. The count did not move — what moved is the content: an ORDER was derived, and the negative is now pre-registered rather than merely reported.**

## Honest caveats that must travel with the tier
1. **★ t is the new ε — convention-carrying, and must not be quoted bare.** t = α/β **rescales as t·c² under Q → cQ** (verified; c = 2 moves it). **Quote the invariant σ_χ(G), which was untouched by all three pins** (the 5451 normalization, the complex-χ pin, and now this). **Three objects in three rounds where quoting the coordinate would have been an error — Elie's standing point, now a rule.**
2. **The complex χ is FORCED, not chosen** — T2547 banks CP existence as Derived, so a δ_CP-carrying condensate cannot be real. Consequences, and they cost nothing: **χ-spread [0.36°, 3.33°] → [1.09°, 3.33°]** (95th unmoved, only the 5th moves, up 3×); **target ε ≈ 0.11 → ≈ 0.090** (−15%). **"A mild, unexplained ~10% grading" survives intact at 0.090** — the phrasing guard held under a 15% shift, which is what a guard is for.
3. **The open targets are not sharply known — but this has now split.** |V_cb| carries an unresolved **>3σ** inclusive/exclusive tension. **|V_ub| does NOT** (Belle ratio 0.97 ± 0.12, compatible with unity). ⟹ **the number we most want to derive is the one whose target got sharp**, and my *"anything inside the band is unfalsifiable"* line was about V_cb and does **not** transfer to V_ub.
4. **Retired, not counted:** T2198's CKM integer-ratio rows and T2259's Jarlskog row (my toys 2820/2895). The band admits **four consecutive integers**, three of them "BST integers." **⚠ BOTH are still live in the registry tagged `Proved` with no retirement marker** — @Keeper curation, referee-fatal.
5. **The dead lanes, each a forced object that failed — banked as exclusions, do not re-open:** radial overlap (proved ceiling, ~1.1M configurations, zero passes) · the one-insertion weak current (partial-isometry gate, all three levels) · the FK ladder (wrong space, Hilbert) · the QM commit operator (wrong space, Jordan; and a projector) · the Q⁵ parity fold (forced and genuine, but a projector: returns exactly 0 or 1) · **P = 1 + εQ (Q parity-odd ⟹ Q|even ≡ 0; the identity on generation space for every ε)** · **all five candidate series above.**

## ★ Scorecard on my own R57 pre-registration — half right, and I named both limbs in advance
| limb, as filed before any number | outcome |
|---|---|
| **(1) TYPE:** *"the (1,3) corner carries one extra factor relative to the (2,3) entry, because the generation-space operator is nearest-neighbour"* | **LANDED — now DERIVED.** |
| **(2) COUNT:** *"hence the split is NOT a second independent number; 1-of-4 becomes 2-of-4"* | **DID NOT LAND.** t is a new free parameter, so the value stays input and **the count is unchanged.** |

**The order was structural; the magnitude was not, and I said the split was a POSITION when half of it is a VALUE.** I stated the kill condition and both outcomes up front, which is the only reason this is scorable rather than arguable. **A pre-registration that can be graded against itself is worth more than one that turns out right.**

*Sector closed. Nothing pushed. CP existence-only. — Grace, closing artifact, 2026-08-22*
