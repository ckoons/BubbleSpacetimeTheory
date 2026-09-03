# Cal — Round 109: (A) 11-vertex genus-2 PRE-SCORE with the 10-vertex table in hand (no 11-vertex file exists at writing) · (B) the shells look-elsewhere count (brute-force verified)
2026-09-03 Thursday 07:19 EDT. Frames: closed orientable genus-2 triangulations, Lutz files (865 at n = 10; 113,506 at n = 11); record = Heawood signs; Φ_r: π₁ → A₄; θ = Φ_r mod V; null = Hom with multiplicity (5,376).

## A. What the 10-vertex table actually says (recomputed from play/.genus2_census_5635.json, all 865)
N_closed = 747,404; realized 0. By stage:
- θ-marginal: P(θ = 0) = 0.0555 vs null 0.0476 — NEAR NULL, slightly toward trivial θ (the direction I pre-registered).
- V-conditionals, BOTH branches, FAR from null: P(im = 4 | θ = 0) = 0.9933 vs 0.8203; P(im = 12 | θ ≠ 0) = 0.9846 vs 0.9375. Per triangulation: medians 1.000 and 0.986; the MINIMUM over 865 triangulations only touches the null (0.824 / 0.929). No triangulation is below null.
So the deviation is not "image-12 above null"; it is: GIVEN the θ-stage, the V-part avoids small images by a factor 4–20 (im = 2: 0.0004 vs 0.0084, 21×; im = 3: 0.0146 vs 0.0595, 4×). The θ-stage is not where the deviation lives.

## The three candidates of K1851-A §4, each with its 11-vertex prediction, plus the referee's fourth
Observables (Grace reports these, colorable and non-colorable 11-vertex triangulations SEPARATELY):
  c4 := P(im = 4 | θ = 0) · c12 := P(im = 12 | θ ≠ 0) · p0 := P(θ = 0) · D on the colorable subset.
(a) θ-STAGE DEFICIT — the deviation lives in θ. Predicts c4 ≈ 0.82, c12 ≈ 0.94 (V-stage at null) with p0 off. ALREADY DEAD at n = 10 (c4 = 0.993). At n = 11 it predicts a fall of c4 by 0.17 on every triangulation. I pre-score it FAIL.
(b) NON-4-COLORABLE POPULATION — depletion near the identity (Φ = 1 forbidden; small images depleted with it). Predicts a GAP between populations at the same n: colorable c4 moves toward 0.82 (say ≤ 0.95), non-colorable c4 stays ≈ 0.99; D on the colorable subset ≈ 12.4 ± 0.5 (realized share near 1/5,376 because the un-depleted population is the one being measured).
(c) NO THERMODYNAMIC LIMIT AT FIXED n — pure finite size. Predicts DRIFT with n and NO GAP: c4 falls from 0.993 toward 0.82 on colorable and non-colorable alike (any fall > 0.02 with gap < 0.02); D on colorable ABOVE 12.39 if the smallest image is depleted like im = 2 and 3 (pre-scored D > 13).
(d) REFEREE'S CANDIDATE — STRUCTURAL small-image suppression, n-independent: a Heawood-closed record's V-cocycle is RAINBOW (a, b, c all nonzero on every face), not a uniform element of H¹(Σ;V); rank-≤1 V-images need four holonomies in one line, a coincidence rainbow cocycles resist. Predicts NO GAP and NO DRIFT: c4 ≈ 0.99, c12 ≈ 0.985 at n = 11 on both populations; the Mednykh null is wrong at the V-stage in the limit and D → log₂ 5,376 + (V-stage correction) — D on colorable well above 12.39 (pre-scored > 13, plausibly 15–17 given the im = 2 depletion factor).
THE SEPARATING NUMBERS: Δ := c4[non-colorable, n = 11] − c4[colorable, n = 11]; δ := c4[n = 10, all] − c4[n = 11, all].
  (a): c4 ≈ 0.82 everywhere (dead). (b): Δ > 0.05, δ small on non-colorable. (c): Δ < 0.02, δ > 0.02. (d): Δ < 0.02, δ < 0.02.
  And D on the colorable subset: (b) 12.4 ± 0.5 · (c)/(d) > 13. Report D only where N_realized ≥ 1, with N_realized printed.
Controls first (unchanged): sphere → image 1 only; torus → image ⊆ {1, 2, 3, 4}, never 12; no 6 anywhere.
Outcome words: gap → (b); drift without gap → (c); neither → (d) and the null's V-stage is wrong structurally; c4 at 0.82 → (a) resurrected and I was wrong to bury it.

## B. The shells: how many small groups' Mednykh sequences hit Casey's windows? (look-elsewhere count)
Casey's recalled steps (ordering caveat governs: recalled AFTER 12 / 48 / 5,376 were on the board; anecdotal): N = 12, ~80, ~8,000, read as |Hom(π₁X, G)| for X = loop, torus, genus 2. Windows: torus ∈ [60, 100], genus-2 ∈ [6,000, 10,000] (±25 percent).
Method: torus = |G|·k(G) (commuting pairs); genus-2 = |G|³ Σ_χ χ(1)⁻² (Mednykh). Since |G|·k(G) ≥ |G| and k ≥ 5 for non-abelian |G| ≥ 21, only orders 9–20 can hit the torus window; hand table over all 54 groups of order ≤ 20, then BRUTE-FORCE VERIFIED on permutation groups (commuting pairs; [a,b][c,d] = e) — every value below reproduced exactly:
  ℤ₉ 9 / 81 / 6,561 ✓✓ · ℤ₃² 9 / 81 / 6,561 ✓✓ · ℤ₁₀ 10 / 100 / 10,000 ✓✓ (both on the boundary) · D₇ 14 / 70 / 7,546 ✓✓ · D₆ 12 / 72 / 7,776 ✓✓ · Dic₃ 12 / 72 / 7,776 ✓✓
  A₄ 12 / 48 / 5,376 ✗✗ (misses BOTH windows) · ℤ₁₂, ℤ₆×ℤ₂ 12 / 144 / 20,736 ✗ · D₅ 40 ✗ · F₂₀ 100 / 32,500 ✗ · every order-16 (k ∈ {7, 10, 16} → 112+) ✗ · order 18 (k ≥ 6 → 108+) ✗ · orders 11, 13, 15, 17, 19 (abelian, ≥ 121) ✗.
COUNT: 6 of the 54 groups of order ≤ 20 hit both windows (four distinct sequences); with the first step PINNED to 12, 2 of the 5 groups of order 12 (D₆ and Dic₃ — same character degrees, indistinguishable by |Hom| at every orientable genus). Look-elsewhere rate ≈ 0.11 (loop free) or 0.40 (loop pinned).
READING: as recalled, the shells EXCLUDE A₄ and are consistent with dihedral-type of order 12 — but also with ℤ₉, ℤ₃², ℤ₁₀, D₇ if the first step is not trusted, and "~80 / ~8,000" cannot separate 70 from 72 from 81 from 100. Nothing is selected. Before any fit: (i) the OBJECT — what surface a shared-memory system of N observers is, and what group (Lyra's task); (ii) the LOGS. Until both exist the status is anecdotal and post-hoc, and the one honest sentence is: "the recalled sequence is not A₄'s."

---
## SCORED (07:34, against play/.genus2_n11_sweep_5638.json — 63 colorable — and play/.genus2_n11_sweep_5638_noncol.json — 7 non-colorable so far; text above unchanged from hash 2295ac8f…)
Colorable 63: c4 = P(im=4 | θ=0) median 0.794 (min 0.357, max 0.978) vs null 0.820 · c12 = P(im=12 | θ≠0) median 0.908 vs null 0.9375 · P(θ=0) median 0.0558 vs null 0.0476 · image-1 (realized orbits) ∈ {2, 4} on every member.
Non-colorable 7 (matched control): c4 = 1.000 on all seven · c12 0.986 · P(θ=0) 0.0541 — the n = 10 pattern exactly (0.993 / 0.985 / 0.0555).
Separators: Δ = c4[non-col] − c4[col] = 1.000 − 0.794 = 0.21 ≫ 0.05 → (b). δ on non-colorable = 0.993 − 1.000 ≈ 0 → (c) DEAD. Colorable members AT the null → (d) DEAD. (a) was dead at n = 10.
VERDICT: candidate (b) — the deviation was a property of the NON-4-COLORABLE population (depletion of small images around the forbidden identity), not of genus 2, not of finite size, not of rainbow cohomology. The Mednykh null's V-stage is confirmed on the population it was stated for (colorable), at n = 11, with the θ-marginal running slightly toward trivial θ on BOTH populations (the one direction I pre-registered that held throughout). Provisional on the control sample completing (7 so far); the verdict word changes only if a non-colorable member's c4 falls below 0.9.
