# K1880 — Round 131 audit: the survivor is a 4-to-12-bit clock reading; the reset is a channel, not a projection; T1292's ~10⁴ bits have no home

**Keeper, 2026-09-08 (Tuesday) 09:15 EDT, clock-verified.** Scores Lyra L1–L3 (hash 8118dd80), Elie 5725/5726/5727 (78b4d353, a65bff4f; out-files `play/.out_572{5,6,7}.txt`, records `.record_572{5,6,7}.json`), Cal §906/§907 (85371dfc), Grace G1 draft. Absorbs K1880-PRE and K1880-PRE-A. Cal's scores of the L/E files were not yet posted at writing; this audit is amended, not renumbered, when they land.

## 1. What is strong

- **Three blind files, mutually blind, agreeing on the object.** Lyra, Elie and Cal hashed before reading each other (09:07–09:08). All three identify the survivor as the SO(5)-invariants of H² and correct my Monday "K-invariants" (constants) the same way. Cal's "the point's location is a gauge" and Lyra's "TYPE independent of the point, only the EMBEDDING moves" are one sentence.
- **Lyra L2 is a proof.** Howe–Moore on the maximal parabolic; H²^{SO(5)} = closure ℂ[z·z] by the first fundamental theorem for O(5) on one vector. H1–H4 HELD on my read (H1's Lie-ball sectors k ≤ m / k ≤ −m / |m| < k match K1860 result 1 verbatim: "the cone k ≤ m is what makes the state count finite").
- **Elie 5726 P1 is the round's theorem-by-instrument.** Under the orthogonal projection onto ℂ[z·z], every saturated chain state is the ZERO vector (at k = k_max > 0 there is no k = 0 component; at m = 137, k is odd). Exact, structural (Hua types are orthogonal), and it kills the reading Cal §906 and Lyra L3(b) both wrote: "reset = SO(5)-average of the vector." Elie 5727 then separated the three readings and controlled them on Y₁ (vector average 0, twirl trace 1).

## 2. Findings

**F1 (MODERATE, Lyra L3(b); also Cal §906 C1 as worded).** L3(b) proves "the reset cannot cross the sector line" for the reset as the SO(5)-average of the vector — reading (A). Reading (A) is empty on every saturated state (5726 P1). The corpus's rule is K1860 §G's transport (j,k) ↦ (j,0) — reading (B) — which does NOT commute with SO(2): it lowers the frequency from m = 2j + k to 2j. So L3(b)'s mechanism does not apply to the rule the corpus actually posits. The sign conclusion survives anyway, by construction (2j ≥ 0), and L3(a), (c) stand. Rewrite (b): "the reset preserves the sign because its image lies in H²₊; it does not preserve the SO(2)-eigenspaces — it is the ONE frequency-lowering step in the dictionary (writes only raise m; K1860-P), and that drop, by exactly the angular degree k, is 'time instantiates'."

**F2 (the reset, stated correctly — for Cal's C1 and Grace's G1).** Reading (B) is well-defined and K-covariant on STATES, not on vectors: it is Elie's twirl (C), ρ ↦ ∫ gρg⁻¹ dg, which forgets the direction inside each H_k and keeps the classical label (j,k), followed by the classical marginal that forgets k. No direction has to be chosen (my worry that (B) needs a chosen functional on H_k dissolves at the density-matrix level). **So the reset is a K-covariant quantum channel — twirl, then forget k — not a projection**, and its output is a classical distribution over windings j. Cal's C1 "definition" stands with one more word: it is a definition on states; on vectors it is empty.

**F3 (the number, measured — `play/.out_5726.txt`).** Occupancy of the survivor by the saturated 3/7 chain, exact DP, mass ≥ 1 − 5e−7, positive control (light-only ⇒ vacuum, H = 0) passed after Elie's owned re-run:

| stopping rule | E[j] | P(j > 68) | H(j) bits |
|---|---|---|---|
| S-m137 (137 writes; N_max caps the degree m) | 58.2 | 0 | 4.02 |
| S-k68 (first k = 68) | 569.5 | 0.9998 | 10.16 |
| S-k137 (first k = 137; K1860 §G's k_max) | 2329 | 1.000 | 12.15 |

Capacity under every named rule (5725/5727): 6.1 bits (Holevo, 69 modes), 68 (presence), 483 (integer occupancy), 12.2 / 34,327 (twirl cells / integer occupancy on 4830 (j,k) cells). Under the twirl the chain's (j,k)-entropy equals H(j) because k is a function of j at every stop. **The survivor of a saturated cycle carries 4 to 12 bits, under every reading and every cap placement. T1292's "~10⁴ bits of observer identity" has no home: capacity fits it only under the 34k-bit twirl-occupancy rule, and occupancy never exceeds 12 bits.** The shortfall is three orders of magnitude on the corpus's own rule.

**F4 (cap placement — convention, owned).** My "2j ≤ 137 ⇒ 68 modes" placed N_max on the degree m (T1292: "total mode count N_max = 137"; K1860 result 1 counts by m). K1860 §G's saturation is on k (k_max from S_dS). Lyra H3 and Cal §906 inherited my placement. Elie's three stopping rules are the right instrument: the OCCUPANCY moves 4 → 12 bits across placements; the CONCLUSION (≪ 10⁴) does not. Quote the invariant: the corpus has two caps (N_max on m; k_max on k) and the survivor's bits are single-digit-to-low-double-digit under either.

**F5 (Cal's refusal "Hardy space of the time circle is an identification, not an isometry").** Elie 5725 H3 decides it by norm: on Š, |z·z| = 1, so every winding (z·z)^j has Hardy norm 1 and w = z·z is an ISOMETRY of ℂ[z·z] onto H²(S¹); in the Bergman norm the windings are not equinormed (1, 1/7, 1/27, 1/77, …). Both sentences are right in their norm; the record space is the Hardy space, so Lyra's phrase stands there. Subscript the norm when the sentence travels.

**F6 (T1292, for Grace G1 — proceed on C1).** T1292's own line 128 says {I,K,R} survives "because topological"; the round's survivor is topological in exactly that sense (π₁(Š) windings). The collision is the COUNT, not the KIND. Re-tier: PERMANENT = three SHAPE lines (0 state bits; nuclear → RECONSTRUCTED as Grace has it) + one STATE line whose measured occupancy is 4–12 bits (5726) and whose capacity depends on the resolution rule (5725/5727). The ratio 10⁴/10¹²² becomes ~10/10¹²². Cal §907(4): evaluate the f_c × C₂-patches rule fragment; if it yields ~10⁴ it is a capacity claim on WHERE, not a count of WHAT, and it still has to fit 12 bits of occupancy. The CI-persistence rows (T317–T319, permanent alphabet) inherit this: identity persists in KIND, not in the 10⁴-bit COUNT — state plainly, do not soften.

**F7 (from K1880-PRE / PRE-A, carried).** No corpus sentence places the nucleation on the boundary; Casey's "nucleation event" vs the Interstasis "period" is a word seam (Cal §907(2) agrees). T308's electron clause cites π₂ of a contractible domain — CRITICAL on the reason; Lyra L4 re-keys to π₁(Š), which IS the Hardy winding. Impossibilities asset line 49 "no geometric CPT-mirror sheet" → "no realized" (Cal §907(3) raises the same line). Antimatter seam (I20 ±1 vs H²'s j ≥ 0 vs K1860 line 14) stays open for L3/C2.

## 3. Tier

- **DERIVED (theorems):** three sectors, two extensions per boundary (L1); no survivor at a Shilov-boundary point (L2); survivor = ℂ[z·z] ≅ H²(S¹) isometrically in the Hardy norm (L2 + 5725 H3); vector projection empties every saturated state (5726 P1); sign inherited (L3(a),(c)); location of the nucleation point is a gauge (§906, L2).
- **DEFINITION (on states):** the reset = twirl then forget k. Content lives only in occupancy.
- **MEASURED (instrument retained):** occupancy 4.02 / 10.16 / 12.15 bits; capacity table.
- **POSIT (unchanged tier, sharper form):** T633's reset clause. Still caps every chain that uses it.
- **REFUTED as a count:** T1292 "~10⁴ bits permanent" (no reading reaches it).

## 4. Casey's four questions, answered by the round

1. *Identical properties?* Same laws (shape); initial vector = a distribution over windings with 4–12 bits. Yes, and the difference between cycles is a clock reading.
2. *Time forward?* Inherited (sign) and monotone (count). The reset is the one step that lowers the frequency, by the angular degree — that drop is "time instantiates."
3. *A forced point?* A bulk point; its location carries nothing (gauge); how far it is pressed toward a direction is a free parameter of the reset (L2) — the one thing the black-hole picture would have to fix.
4. *Select the sign?* Nothing to select; a flip needs an antiholomorphic map, and none is in G or in the reset.

## 5. Owed before the round closes
Cal: scores of L1–L3 and 5725–5727. Lyra: L3(b) rewrite (F1); L4 (T308 re-key). Grace: G1 apply on C1 (F6); G2 sweep (PRE-A). Elie: nothing — 10/10 with three owned corrections, all in the out-files.

— Keeper
