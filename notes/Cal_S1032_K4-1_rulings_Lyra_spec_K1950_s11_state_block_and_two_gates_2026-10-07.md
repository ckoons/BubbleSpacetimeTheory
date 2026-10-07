# Cal Section 1032 — Round K4-1 rulings: Lyra's spec, K1950 Section 11, the state-block line, and two gates

**Written 2026-10-07 14:44 EDT.** Rules against my hash 2b8d9322 (S1031, 14:33), which was written before Lyra's spec landed (14:36). Instrument: `play/cal_S1032_K4-1_rulings_true_boundary_base_and_2022_principles_2026-10-07.py` (sha256 459d2660…), 9/9.

## 1. The state-block line (K1950 Section 11a): PASS
> "Its Šilov boundary is (S⁴ × S¹)/ℤ₂, non-orientable through the four-sphere, with the circle's direction global; 'S⁴ × S¹' in older notes is the orientation double cover."
- Each clause checks out:
  - the deck map pushes ∂_θ to ∂_θ [I];
  - its degree on S⁴ is −1 [I];
  - π₁ of the quotient is ℤ, with w₁ = −1 on the generator, so S⁴ × S¹ is the unique connected double cover belonging to ker w₁ — i.e. the orientation double cover.
- Apply as written. Optional, for precision: "(base ℝP⁴)".

## 2. K1950 Section 11b: the circle's direction is global. CONFIRMED. "Fits maximal P violation": STRIKE "fits"
- The circle's direction descends to the true boundary [I]. Casey's "same order always" holds on the physical boundary if the read order is the circle's direction.
- **It cannot be the weak handedness.**
  - Under C the circle's direction is reversed (J ↦ −J, Lyra Section 4). Under the deck map (P-like on S⁴) it is preserved. So it is **CP-odd**.
  - The weak read orientation is **CP-even** (S1031 B) [I].
  - **KL3 FIRES on the circle route.** The circle's direction is the particle/antiparticle factor of o = (particle sign) × (chirality sign). The chirality factor still comes from S⁴ (Pin⁻, T2522), and that factor is not global.
  - Conditional on "deck = P-like". If the physical P also reverses the circle, re-rule.
- A global P-even arrow and a non-global spatial orientation are *compatible with* maximal P violation; they do not explain it. Maximal P violation is a fact about the coupling.

## 3. The 2022 principles read on the TRUE boundary (new; this affects Lyra's Addendum 1 and Keeper's Guide note)
- **The true boundary's own base, ℝP⁴, violates BOTH 2022 premises as literally written** [I]:
  - it is not simply connected (π₁ = ℤ₂);
  - it is not orientable.
  
  BST still conserves charge on it. So the 2022 sentences must be read in the forms the true boundary satisfies:
  - **(P-one-channel′) b₁ = 0: no FREE loops.** A ℤ₂ torsion loop is not a conserved winding family.
  - **(P-fibre) the fibre direction is global.** This replaces "the base must be orientable"; it is what 2022's MECHANISM (fibre reversal kills charge) actually used.
- **Consequences:**
  - (a) Under P-one-channel′, S² and RP² both pass [I]. **Global P-minimal still gives S² on 4 vertices, i.e. K4** [I]. K4 forced-by-principle SURVIVES.
  - (b) **Lyra Addendum 1's "RP² excluded by 2022 orientability (P-orient)" FAILS.** The premise it cites is refuted by the boundary itself. The n = 3 analogue (S² × S¹)/ℤ₂ has base RP² and a global fibre direction.
  - The K6 cage is closed instead by Lyra's OWN original reason: P-loop needs a FREE loop (a phase, not a sign). Under that, the minimum is T² on 7 vertices, ahead of the Klein bottle on 8 and with RP² excluded [I]. **Cite P-loop-free, not 2022.**
  - (c) **Keeper's Guide Vol2 Ch01 note** says the 2022 orientability argument "survives". Its CONCLUSION survives (charge is conserved). Its PREMISE as written ("the substrate base must be orientable") is refuted by the actual boundary. A front-facing note should say both. MODERATE, one sentence.
- **P-transfer must name ONE home for the record**, because the three on the table are different spaces:
  - the 2022 substrate base S²;
  - a closed surface inside ℝP⁴ (a 2-surface inside a 4-dimensional base, not a patch of it);
  - Lyra item 5's S² in the compact dual Q².

## 4. Lyra's spec, item by item (S1031 predictions in brackets)
1. **P-closed, P-minimal: ADMISSIBLE, not smuggled.** [Predicted: global minimality excludes tori. Confirmed; Lyra named P-loop.]
   - "A one-sided edge is a pending commitment" is a genuine information statement.
   - **Name one more input:** *simplicial*. "Triangulated" carries the 4; in the CW category a sphere closes on fewer vertices (S1030 R2).
   - Tier: D_IV⁵ + {P-closed (simplicial), P-minimal, P-transfer}. Can-fail: commitment writes a non-simplicial complex.
2. **C7 reduction: EXACT. And Section 990 DOES reach (D2).**
   - Section 990 showed that one-way writes do not make the representation complex (spin-1 polarization records).
   - "No 3̄" is vacuous when 3 ≅ 3̄, which is the act level by Lyra's own correction.
   - So (D2) adds nothing until K1926's condition holds. **K-C7c collapses into K-C7a: one live line, not two. Positive time contributes nothing independent to C7.** [Predicted: "only singlets commit" owed. It is Lyra's (D3).]
3. **Bare U(3), with the det phase = the circle's charge: POSITION, admissible.** "Read orientation, det phase and baryon number are ONE object": OVERREACH.
   - The orientation is a ℤ₂ VALUE of the group element; B is the charge LABEL (position vs value).
   - On a B = 1 record, an odd reordering is the global phase −1, which is unobservable. That is consistent with Lyra's item 4.
   - Restate as "live in one U(1)". U(1)_B normalisation is pin-owed.
   - Elie's 5860 prediction D3 (J carries the parity and does not fix which order is positive) is the test. Rule on his result, not his prereg.
4. **Read order = the circle's direction: global, CONFIRMED (Section 2 above).**
   - **The identification with the triangle's cyclic order is NOT supplied by the det route.** The J-flow carries a triple continuously into its reverse (Elie 5860 D2, prereg).
   - **Candidate map, position only:** three values PLACED on the oriented fibre circle get their cyclic order from its direction; reversing the direction reverses it [I]. This fits reading (A) (the writer IS the circle). It is owed: why the values sit on the circle.
   - As the weak handedness: FIRES (Section 2).
5. **The amplitude selects, the record keeps the charge: PASS as a position.** [Predicted: the read order is not recorded.]
6. **The surface in Q²'s S²:** conditional on Elie B1; generic, so "allowed". It conflicts with P-transfer's 2022 base; pick one (Section 3).
7. **T958 reading (A): PASS as a reading.** T958 is unaudited, so picture only. Lyra's question to Casey goes to Casey.
8. **ψ = record + instruction: DEFECT, MODERATE.** [Predicted in S1031 C7; confirmed.]
   - Erased slot (e2) says "the relative phases ρ = vv† forgets". A PURE vv† keeps every relative phase in its off-diagonals [I]; it forgets only the global phase.
   - So for a sphere record the instruction content is empty, and "interference is instructions combining before the write" is wrong as stated: interference lives in vv†.
   - **Choose one:**
     - (i) record = vv† DEPHASED in a named basis. Then (e2) is the off-diagonals, the pointer basis is a stated input, and the Born rule is the diagonal.
     - (ii) instruction = holonomies of genus ≥ 1 records only (plus the global phase).
9. **The K6 cage:** keep it, closed by P-loop-free (Section 3b), not by 2022.

**Torus reconciliation (Lyra Addendum 1, T-i and T-ii): ADMISSIBLE as consistency, with two referee points.**
- Bound neutrons DO decay where the nuclear Q > 0: tritium (12.3 y, pin-owed) and ¹⁴C. "Held by binding" is energetics, which the SM already explains. T-ii is consistency only.
- A free torus record that "unwinds" must give the free-neutron lifetime's scaling. In the SM that is G_F² Q⁵ phase space (Sargent's rule; pin-owed). Otherwise the unwinding relabels β decay (KL4).
- **K-T3 sharpened:** the unwinding is gated by Q-values exactly as in the SM (then it adds nothing), or it predicts a deviation (then that is the test).

## 5. Gate: ElectronMass dated diff (Grace, on disk): CONDITIONAL. PASS once the following five one-line annotations land, with the sixth file in the same push
- The head is correct: A² = π₅, C₂ = 0, K ∝ S^rank, route 2 → α¹⁰, stage 2 Identified, the 0.034% identity kept.
- Both Proved rows are struck. The k > p − 1 = 4 threshold was checked independently.
- **Fixes:**
  1. Derivation.md:413 and :415 still say "exponent 2C₂ structural … not merely motivated". Annotate: Identified, read not derived.
  2. Derivation.md:564: "Total α¹² — Proved (given Step 5)" → "Identified (given Steps 4–5)".
  3. ConjectureC:641: strike "derived … with no free parameters" (Section 946 retired the phrase).
  4. ConjectureC:817, :832, :859: "every step is a proved theorem", "PROVED: A² = π₆", "no free parameters". Annotate as the head.
  5. BergmanUnits:281: "Step 2 (proved): A² = π₆" → π₆ is weighted; A² = π₅.
- **Sixth cascade file**, same push: BST_SpectralGap_ProtonMass.md:109, :121 and :184 ("A² = π₆ … **Proven.**").
- Also: ConjectureC:546 and :833 carry "Wallach k_min = 3", which the 10-01 EHW correction fixed elsewhere.

## 6. Gate: Time, Derived v1.6 (Lyra): CONDITIONAL
- **PASS:** the Section 7 parenthesis matches Section 1026 verbatim, inside Casey's 10-01 GO. The PDF was rebuilt after the md.
- **Condition 1 (process):**
  - The line 99 sentence is **outside the 10-01 GO**. K1947 item 2 covers only the parenthesis. My S1029 sent line 99 "on Casey's word", but the status line (6) puts both under 10-01.
  - **Keeper may rule it under Casey's 10-07 "important cleanups" delegation.** The status line must then name that ruling.
- **Condition 2 (content):** line 99's "(one Rac, one Di, no su(2)_R: the counts differ)" states as closed what K1948 M2 reopened (colour on the Rac changes the count). Insert after "the counts differ": "(on the content as stated; colour placement open, K1948 M2)".
- **Non-blocking, for the next version:**
  - make line 99's "open per K1653" agree with line 62;
  - line 112, "both live on the S¹", predates today's convention: the deck map also acts on S⁴.

## 7. Standing
My referee question is still open: one number SO₀(5,2) alone does not give, and what would make it wrong.
