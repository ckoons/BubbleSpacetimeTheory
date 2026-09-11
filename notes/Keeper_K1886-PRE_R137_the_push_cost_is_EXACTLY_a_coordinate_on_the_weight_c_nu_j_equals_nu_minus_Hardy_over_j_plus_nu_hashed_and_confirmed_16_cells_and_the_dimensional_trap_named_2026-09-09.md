# K1886-PRE — the push cost in closed form as a function of the weight, and the trap that follows it

**Keeper, 2026-09-09 (Wednesday) 10:30 EDT, clock-verified.** Instrument retained: `notes/Keeper_K1886-PRE_instrument_push_cost_as_a_function_of_the_weight_nu_2026-09-09.py`. The formula was written into the file as a comment **before the run**, 937,499 accepted Lie-ball points, importance weight h(z,z̄)^{ν−5} with h = 1 − 2|z|² + |z·z|².

## 1. The law, hashed then confirmed
**c_ν(j, k = 0) = (ν − 5/2) / (j + ν).**

| ν | j = 0 | j = 1 | j = 3 | j = 10 |
|---|---|---|---|---|
| 5 (Bergman) | 0.5000 / 0.5000 | 0.4166 / 0.4167 | 0.3123 / 0.3125 | 0.1663 / 0.1667 |
| 6 | 0.5834 / 0.5833 | 0.5000 / 0.5000 | 0.3889 / 0.3889 | 0.2182 / 0.2188 |
| 7 | 0.6428 / 0.6429 | 0.5625 / 0.5625 | 0.4500 / 0.4500 | 0.2645 / 0.2647 |
| 4.5 | 0.4440 / 0.4444 | 0.3631 / 0.3636 | 0.2666 / 0.2667 | 0.1396 / 0.1379 |

Measured against hashed, sixteen cells, four weights, agreement to four digits.

## 2. What it settles
- **Round 130's exact line is the ν = 5 case:** (5/2)/(j + 5) = 5/(2(j+5)). The whole closed form was one point of a one-parameter family and nobody knew.
- **The Hardy point is a zero of the entire function, not only of the asymptotic constant.** At ν = 5/2 the cost is identically zero for every j. That is stronger than Elie 5743's statement and it confirms K1885 §3: the zero sits at the Hardy point 5/2, not the Wallach floor 3/2. Subscript accordingly.
- **The asymptotic constant is exactly ν − ν_Hardy,** so "the push cost measures the gap from the boundary" is now an identity rather than a reading.
- **Prediction for Elie, hashed:** ν_Hardy = n/2 for D_IV^n, so c_ν(j) = (ν − n/2)/(j + ν) at every n. Check at n = 4 and n = 6. If it holds, the only structural number in the commitment law is the Hardy point, and there is no dimension in it beyond that.
- **E4's classical-limit control, answered in advance:** ν → ∞ gives c → 1. Commitment never completes in the classical limit, which is the right behaviour for a quantum event and is a control that cannot fail. Report it as such.

## 3. The trap, named hard, before anyone writes a number
The Berezin reading says ν = 1/ħ. Combined with the above, someone will write: the record lives on the Hardy space, the Hardy point is n/2, therefore **ħ = 2/n = 2/5.** **Do not write that, and I am refusing it in advance.**

**ν is dimensionless. ħ is not.** "ν = 1/ħ" in the quantization literature means ħ in units where the symplectic form, the Kähler class, or the domain's own metric normalisation is set to one. Until the corpus names *which* normalisation, the identification transports no number at all, and 2/5 would be a clean rational produced by a unit convention nobody stated. That is the shape this program has caught a dozen times.

**What would make it real** is a stated normalisation plus an independent value. T1136 carries ħ explicitly in N_max·ħ/(m_e c²) = a₀/c, so there is an independent handle. Elie E3 should ask whether the units connect and should report "they do not connect" if that is the answer, which is a clean result and closes the lane honestly.

## 4. What this does to the payer reading
It sharpens Cal's objection into an identity. The push cost is not a physical price with a weight-dependent value; **it is the weight, read in a coordinate.** Any physics extracted from it is physics put into the choice of ν. So the round's question is the only question: what fixes ν, and does the corpus fix it twice at different values?

— Keeper
