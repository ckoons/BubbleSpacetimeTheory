# Cal Section 1036 — Item 5(h) hashed: Q* = m_e (Casey, K1953), the full one-loop formula, the match rule and its null, before Elie solves

**Written 2026-10-09 12:45 EDT** (from `date`). Read: K1953 only. **I have not solved the equation and no value of the running at or near m_e appears in this file or its instrument.** Instrument: `play/cal_S1036_Qstar_hash_one_loop_vacuum_polarization_formula_limits_only_no_solve_2026-10-09.py` (5/5): verifies the formula's two limits and its monotonicity, prints nothing near m_e.

## 1. The claim under test (Casey, 10-09, via K1953)
The interior value α⁻¹ = N_max = 137 holds at **Q* = m_e**; the measured 137.036 (Thomson limit, Q = 0) is that value seen from the continuum. Direction: QED screening makes α⁻¹ FALL with Q, so α⁻¹(0) > α⁻¹(m_e) is the right sign. The sign alone is not a test.

## 2. The hashed formula (on-shell scheme; one electron loop; no muon, τ or hadronic loop)
Spacelike momentum transfer Q² = −q² > 0 (the t-channel; the convention in which α(0) is the Thomson value):

  **α_eff⁻¹(Q) = α⁻¹(0) − Δ(Q),  Δ(Q) = (2/π) ∫₀¹ dx x(1−x) ln[1 + x(1−x) Q²/m_e²].**

(Peskin–Schroeder eq. 7.91, Π̂₂(q²) = −(2α/π)∫x(1−x) ln[m²/(m² − x(1−x)q²)], with α_eff = α/(1 − Π̂₂) and q² → −Q²; α⁻¹Π̂₂ is independent of α, so Δ carries no α.) Limits, verified by the instrument: Δ(0) = 0; Δ → (1/3π)[ln(Q²/m_e²) − 5/3] for Q ≫ m_e (the leading log plus its constant, which is why the leading log alone is not the formula); Δ increasing in Q.
- Inputs for Elie: α⁻¹(0) = CODATA 2022 (Grace pins the digits); m_e = CODATA (same). Nothing else.
- The muon loop is excluded by declaration: at Q ~ m_e it is suppressed by (m_e/m_μ)² and does not reach the 10⁻³ level needed to move the answer across the match window below.
- Timelike Q² (s-channel) is a different function (it has an imaginary part above 2m_e); **not** the hashed one. If anyone later says "but in the timelike convention…", that is a second test, hashed separately.

## 3. The computation Elie runs, in this order, printing each line before the next
1. Δ(m_e) and α_eff⁻¹(m_e) (the prediction's own value at the named point).
2. Solve α_eff⁻¹(Q) = 137 exactly for Q; print Q/m_e.
3. Print Q/m_e against the four menu points Lyra listed without ranking (m_e, 2m_e, α m_e, α² m_e), as ratios.

## 4. Match rule and null, fixed now
- **Credit (MATCH):** |ln(Q/m_e)| ≤ ln(1.1), i.e. Q within 10 % of the NAMED point m_e. Under a log-uniform null over the menu's own span (α² m_e to 2 m_e, ln-span ≈ 10.5), a ±10 % window has p ≈ 0.019. This window is satisfiable (the formula is continuous and monotone, so exactly one Q solves it).
- **Reported, not credited:** Q within a factor 2 of ANY of the four menu points (four windows of ln 4 each; p ≈ 0.5 on the same span). A factor-2 landing is a clue, not a match.
- **MISS:** anything else. A miss kills "the 0.036 is QED running from an interior 137 at m_e" and leaves K675's curvature term (n_C/N_max) as the only live reading of the 0.036; Keeper's K1953 says so and I agree it is the pincer.
- **Keeper's own calibration** ("a miss by orders of magnitude") is his prediction, not part of the rule; the rule above is the referee's and it is the same whichever way his prediction goes.
- **No second scale after the number.** If Q/m_e lands near some other clean combination (2, π, 1/α, 6π⁵…), that combination is caged on sight; the test was m_e.

## 5. What the test is NOT
It is not a derivation of 137. The 137 is identified (board). A match would make the running reading a calculation of the 0.036 from one named scale; it would not touch the identification of N_max with α⁻¹.

— Cal, 2026-10-09 12:45 EDT. Instrument 5/5, no solve.
