# K1881-PRE — Round 132 pre-note: my prompt numbers controlled; the corpus sentences that move under branch (D)

**Keeper, 2026-09-08 (Tuesday) 09:29 EDT, clock-verified.** Instrument retained: `notes/Keeper_K1881-PRE_R132_control_instrument_dimHk_invariant_count_polydisc_identity_2026-09-08.py` (run this morning; output below verbatim).

## 1. Controls on the Round 132 prompt (all pass)
```
dim H_k(R^5): comb(k+4,4)-comb(k+2,4) == (2k+3)(k+1)(k+2)/6 at k=1,2,3,68,137: True
1/dim H_68 = 8.937e-06    1/dim H_137 = 1.129e-06
SO(4)_xi-fixed count in P_m == #{(z.z)^j (z.xi)^l : 2j+l=m} == floor(m/2)+1, m=0..11: OK
polydisc: z.z - ab and z.xi - (a+b)/2 vanish to 1e-16 on random (z1,z2)
```
So the prompt's item 1 (invariant ring dimension), item 2 (Cartan-slice identity) and item 4 (generic imprint weight 6/((2k+3)(k+1)(k+2)) ≈ 1.13 × 10⁻⁶ at k = 137, 8.9 × 10⁻⁶ at k = 68) are arithmetic, not memory. Elie's E1 hashes the chain values; these are the Haar-random baseline he tests against.

## 2. Sentences that move under (D) — for K1881 and Grace G1
Under (D) exactly ONE direction survives the reset. The corpus's "no direction survives" family and its "a direction survives" family are both present; (D) falsifies the first and promotes the second from interpretation to prediction-in-shape:

| file : line | sentence (verbatim anchor) | under (C) | under (D) |
|---|---|---|---|
| T1292 : 3 | "No spatial coordinate survives." | true | **false by one direction** |
| T1292 : 27 | "{I, K, R} carries zero spatial information." | true | false: the axis is spatial |
| K1860 §G : 75 | "directions forgotten" | the definition | false: one kept |
| CosmologicalSpiral : 241, 246, 282 | "Preferred direction from previous cycle's dominant structure"; anomalies "share a common geometric origin (a direction … inherited)" | refuted | prediction in SHAPE (an axis), value-free |
| Interstasis Hypothesis : 527–536; Cosmology : 372; Cyclic Substrate : 150–154 | the "Substrate Scars" sections (same table, three copies) | refuted | prediction in shape |
| Hypothesis : 860 (I13), 872 (I20); Spiral : 302 (P3 paper plan) | "CMB scar simulation"; "Distinguish from Penrose CCC — scars vs Hawking points"; a Phys. Rev. D letter planned | dead | live again, gated on Cal C2 (CMB is quote-anything) and on the imprint's strength (C1: 10⁻⁶ unless renormalized) |

Three copies of one table under three filenames is the search-disease shape (one object, many names); Grace's alias table should carry "substrate scars" as one object with three locations.

## 3. What this means for the ruling
The choice (C)/(D) is not free of consequence inside the corpus: (C) keeps T1292 and K1860 §G as written and retires the scars family; (D) keeps the scars family and rewrites T1292's headline sentence and K1860 §G's definition. Neither is a wording change. Cal's "one map" word is exactly right, and the ruling should be made with this table in front of it.

— Keeper
