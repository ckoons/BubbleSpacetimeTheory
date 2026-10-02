# K1948 — Round 26 audit: the SUSY clause is a consequence by ONE route, not two; the "once each" premise has one unchecked door (colour)

**Keeper, Friday 2026-10-02, 12:49 EDT.** Audits Lyra R26 (ece0be6b, toy 5856), Elie 5857 (44d0c026), against Cal Section 1028's prereg (837618ba). Cal's ruling on R26 is still owed. This audit is an input to it, not a substitute for it.
**Rubric cell:** Internal E (falsifiable: the Forbidden list) / Internal D (forced, not posited).
**didwe:** "lepton doublet singleton internal label", "which singleton carries the weak isospin doublet", "where does charge live singleton gauge index" → 0 hits each. No prior ruling.

## Verdict: CONDITIONAL PASS

### What is strong (PASS)
1. **The free-level spin-3/2 current is real and conserved on its own** (Elie 5857: swap only the s = 3/2 character and the identity breaks; lowest K-type (3/2, ½) at 9/2, multiplicity 1). This is exact and a computation, not bookkeeping.
2. **The count is right for the content as stated.** dim Di_m / dim Rac_m → 2 exactly (closed forms fitted on m ≤ 4, predicting m = 5). One Dirac = 2·Di, so balance needs 4·Rac. BST's Rac once (real: 1, complex: 2) against 2·Di is unbalanced **in either convention** (Lyra's "1 or 2" ambiguity does not matter: both fail). Robust.
3. **Electroweak labels cannot supply an R-symmetry.** Time, Derived v1.5 Section 3a puts the integer charge "on the SO(5)/SO(4) structure", i.e. inside so(5,2) itself. An R-symmetry must commute with so(5,2), so an su(2) from inside SO(5) cannot be su(2)_R. This closes the most natural reading of Cal's escape clause ("unless BST supplies an su(2) doublet of Racs") for the leptons. Not stated in R26; stated here so it is on the record.
4. **TD line 99's scoping (Cal Section 1028 point 1)** is correct and adopted by Lyra. It stays a v1.6 item for Casey's word.

### M1 (MODERATE): "a consequence by two independent routes" claims more than it shows
- **Lyra R26 Section 3, verbatim:** *"It is now a consequence, by two independent routes: 1. Counting … 2. Λ > 0: … de Sitter admits no unitary positive-energy supersymmetry."*
- Route 2 forbids **unbroken** supersymmetry. The Forbidden clause forbids **a SUSY spectrum**, i.e. superpartners, which a softly broken supersymmetry still has.
- **Cal Section 1028 makes the same point himself:** if BST's content were the hyper, F(4) would hold at the free level and only Λ would break it, leaving partners degenerate to O(H). Those are excluded by data, so the clause would then need hard dynamical breaking, which is a posit. So Λ > 0 is exactly the case where the clause is **not** a consequence.
- **Correct form:** the clause is a consequence by **one** route (counting). Route 2 is supporting: it says the exact symmetry is unavailable in BST's cosmology. It does not stand alone.
- **Fix:** Lyra's proposed Forbidden-list sentence keeps both clauses but must drop "two independent routes" wherever it appears (R26 Section 3, the board line, the TOMORROW file I wrote, which carried it: owned).

### M2 (MODERATE): the "once each" premise is checked for electroweak labels but not for colour
- Route 1 is conditional on "Rac and Di once each, no su(2) commuting with so(5,2)". R26 names the condition. Nobody has checked it against the corpus's internal labels.
- **Colour is the one door.** TD v1.5 Section 3a: the thirds "cannot come from the SO(5) torus … SU(3) is not a subgroup of SO(5)." So colour is an internal index that **does** commute with so(5,2), so it multiplies singletons.
- **The case that matters:** if colour sits on the **Rac** in the quark composites, the content contains (Rac ⊗ 3) ⊕ Di. Under an su(2) ⊂ su(3), 3 = 2 ⊕ 1, so the content contains **(Rac ⊗ 2) ⊕ Di, which is exactly the hypermultiplet's shape** (doublet scalars, singlet fermion), plus a spectator scalar. The free-level F/B count would then balance on that sub-multiplet.
  - If colour sits on the Di, or on the composite only, the count fails and route 1 stands.
- **The corpus does not say which singleton carries colour** (greps over K1930–K1947, R-notes since 09-01, Cal Sections 1000+: no placement found).
- **Calibrate both ways:** this is a door, not a finding. An su(2) inside a gauged su(3) is not an R-symmetry once the gauge interaction is on, so even the bad case may only reopen the *free-level* question. But Cal's own ruling says the free level is where the count decides the round. So the placement is owed before the clause is written as a consequence.
- **Owed (one count, Elie or Lyra):** where does BST put colour in Rac⊗Di? Then rerun 5857's balance on the actual coloured content. Also state whether the three generations are multiplicities commuting with so(5,2) (the state block calls them "rank + 1 strata", which reads as levels, not copies; one line settles it).

### m1 (MINOR): toy 5856's F3 is a printed inequality
`F3=(1!=2)` asserts R25's multiplicity rather than computing it. Lyra's docstring calls F2/F3 bookkeeping, so this is labelled honestly. The computational content of the count is Elie 5857; cite 5857, not 5856, for it.

## Where this leaves round 26
- **Closes on Cal's ruling plus the colour placement.** If colour is not on the Rac (or the Rac's colour multiplicity cannot form an R-doublet commuting with so(5,2) at the free level), the clause is a consequence by counting, with Λ > 0 as support.
- The Forbidden-list sentence, corrected:
  > *"No SUSY spectrum: BST's singletons are not an F(4) supermultiplet (the boson and fermion counts differ, and no su(2) commuting with the conformal group acts on them), so the free-level spin-3/2 current is a higher-spin current, broken with the others; Λ > 0 independently excludes unbroken supersymmetry."*
  — the second clause in the sentence **after** the colour check passes.
- **Owned:** my TOMORROW 10-02 file repeated "by two routes" without checking route 2's scope.

**Counter next: K1949.**
