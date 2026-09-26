# Keeper — team prompt, ROUND 6 (Saturday 2026-09-26, 11:27 EDT). No EOD before 5pm.

**Casey (late morning, after the round-5 results; verbatim):** "finish our work on this thread and then look at how we can begin to add boundary physics (Shilov boundary) processes and continuum physics to the mix to improve our work, to add energies and better understanding of how D_IV^5 projects itself into D_IV^4 and the similarities and differences, and use conventional science (from the web) to improve our work end to end to show how processes work from the discrete interior of D_IV^5 through the Shilov boundary and into the continuum. … Be creative and optimistic, don't gate — investigate. Reconnect to the corpus, linear algebra on D_IV^5."

**Rules:**
- Run `date`.
- Run `didwe` before opening a lane. A STOP hit means you say in writing what differs from its reason.
- Write the kill line first.
- **Quote the invariant before any number.** Four of round 5's corrections were convention or search-surface errors, not algebra errors.
- Pins come from the source, never a search summary.
- Write "Section", not the sign.
- Commit by path.

**Read first:** `notes/Keeper_K1928_*` (Part 1 = round-5 rulings; Part 3 = the spine; Part 4 = corpus map). Then K1927 and its addendum.

## The spine (K1928 Part 3; instrument `play/keeper_K1928_three_times_so52.py`, ALL PASS)
- One sl(2,ℝ) = span{P₀, K₀, D} ⊂ so(5,2) holds all three conjugacy types of "time":
  - **Elliptic:** the rotation of the two times, which is the centre of K and **BST's clock J**. Discrete spectrum 5/2 + k on H²: **the interior.**
  - **Parabolic:** P₀, the Minkowski energy on the Šilov boundary, compactified ℝ^{1,4}. Continuous spectrum [0, ∞): **the boundary.**
  - **Hyperbolic:** D. Scale, the continuum's flow.
- Type is an invariant, so interior → boundary → continuum is a sequence of **positions**.
- The Cayley transform maps between the pictures (F475: Cayley = Wick rotation).
- The corpus already has the boundary side: **T2625, the Three-Sector Theorem**, L²(ℝ^{1,4}) = H²₊ ⊕ H²₋ ⊕ spacelike.
- **Energies enter by a tilt with one scale.** This is Barut's mechanism: for hydrogen the tilt diagonalizes the compact generator for bound states and a non-compact one for scattering, and the sign of E is the conjugacy type.
- **Fresh-spin vs K1878 (STOP):** K1878 put energy on the elliptic clock's K-types and got 5 Ry. Round 6 puts it on the parabolic generator via a tilt with a named scale. If a lane reproduces 5 Ry, it is K1878 again and it STOPs.

## Finish round 5 first (small)
- **Casey decides T_bb** (K1928 Part 1, item 7). Should the proximity rule be registered as a bet against lattice QCD, which would mean new dynamics beyond BST's own QCD, or scoped to light-quark proximity states, with T_bb named as the discriminating test? Register it before LHCb Upgrade II looks.
- **Cal:** the final word on 16/3 ("at threshold, 3.0–3.7σ pending a DR2-consistent ω_b–ω_c correlation") and on A2 ("at threshold: kaons +3.3/+3.7σ, |V_ud| 3.05–3.42σ").
- **Lyra:** the two calibration lines owed from Cal Section 990: "iff" → "one route", and (4a) → "BST's own content is the 5/2 offset".

---
## LYRA — the bridge, in linear algebra
1. **Settle the ground weight first.** Time, Derived (GO, K1670) has E₀ = 3/2, the minimal representation. The physical module H² has λ = 5/2. Are these two objects, or is one mislabelled? K1927(c) says the minimal representation of SO(5,2) restricts to H_{3/2}(D_IV⁴) ⊕ H_{5/2}(D_IV⁴). Is that the bridge? One paragraph, which Cal hashes.
2. **The three times on H² (interior → boundary → continuum).** Write the sl(2,ℝ) inside so(5,2) explicitly, in the invariant form "the elliptic element of span{P₀, K₀, D}". Give the spectrum of each type on H²(D_IV⁵) and on the restricted summands H_{5/2+k}(D_IV⁴). Then connect T2625's three sectors to the parabolic picture and state the Cayley transform as the operator that carries J to P₀. Reconnect Time, Derived Sections 2–3, T2629 (the clock row), and the ledger picture (tick = begin-time; Λ = 3H²Ω_Λ).
3. **D_IV⁵ vs D_IV⁴, the table Casey asked for** (similarities and differences). Rows:
   - dimension, rank, genus;
   - Šilov boundary: ℝ^{1,4} vs ℝ^{1,3} compactified;
   - Wallach set: {0} ∪ [3/2, ∞) vs {0} ∪ [1, ∞), which is the CFT scalar unitarity bound Δ ≥ (d−2)/2;
   - Hardy weight: 5/2 vs 2;
   - minimal representation;
   - what hydrogen is (the Wallach point of D_IV⁴);
   - the restriction tower (k = the Kaluza–Klein / normal-derivative index);
   - the holographic operators (Kobayashi–Pevzner; Labriet arXiv:2203.00009, SO(2,n) → SO(2,n−p) via Gegenbauer normal derivatives);
   - what is lost going down: T2565 says the selection is Machian.
   Mark each row position or coordinate.
4. **The mass gap is where the scale enters.** In 4D the tower Δ = 5/2 + k consists of scalar conformal fields with a continuous mass spectrum. A gap needs SO(4,2) broken to Poincaré × scale. Which BST object breaks it: the ruler, the tick, or the Machian descent? Reconnect K1714 (boundary gap 6/a² = a KK gap, not Clay's). Kill line: if nothing in BST breaks it, BST's 4D continuum is scale-free and every mass is the ruler times a number, which is the present state honestly stated.
5. **Casey's "writing reality on the surface":** the Cauchy–Szegő kernel as the boundary → interior map, and T2625's H²₊ as the "written" sector. Which boundary data (5D, signature (1,4), 2:1 over real forms per Cal) determine an interior state? Give it one line in the table.

## ELIE — toys, exact, controls first (hash before running)
1. **The tilt toy (energies):**
   - so(2,1) Coulomb reduction: r = T₃ − T₁, r p² = T₃ + T₁, so (T₃ + T₁) − 2E(T₃ − T₁) = 2Zα.
   - Show the tilt makes the generator elliptic for E < 0 (eigenvalue n ⇒ E_n = −Z²α²m/2n²), parabolic at E = 0, and hyperbolic for E > 0 (continuum). Exact, symbolic.
   - **Control:** the oscillator's so(2,1) gives linear spacing, not 1/n².
   - **Then** apply the same tilt to BST's sl(2,ℝ) on the summands H_{5/2+k}(D_IV⁴): what does the elliptic spectrum 5/2 + k turn into under the tilt, and what scale has to be supplied? Kill line: 5 Ry = K1878 = STOP.
2. **The holographic operator toy:**
   - For D_IV⁵ → D_IV⁴, build the k = 0, 1, 2 symmetry-breaking operators H_{5/2}(D⁵) → H_{5/2+k}(D⁴) on polynomials (normal-derivative / Gegenbauer form per Labriet, Kobayashi–Pevzner).
   - Verify intertwining with the SO(4,2) generators exactly.
   - **Control:** the wrong Gegenbauer parameter fails intertwining.
3. **The three-times toy:** the spectra of the elliptic, parabolic and hyperbolic elements on a truncated H² model (K-type basis). Discrete vs continuous are seen through level spacing as the truncation grows. Build on `play/keeper_K1928_three_times_so52.py`, which is the matrix level only.
4. Carried: the second-method check of Lyra's write algebra.

## GRACE — conventional science, pinned from the source
1. **Pins (0 corpus hits today):**
   - Lüscher–Mack, CMP 41 (1975) 203–234: the conformal Hamiltonian, and their sign convention for K.
   - Mack 1977, the unitarity bounds.
   - Kobayashi–Pevzner, the original holographic-operator paper.
   - Labriet arXiv:2203.00009, the published version if one exists.
   - Juhl 2009 (Birkhäuser), conformally covariant operators and holography.
   - Jakobsen–Vergne, J. Funct. Anal. 34 (1979) 29–53: the restriction formula, stated for our case.
   - Barut–Kleinert, Phys. Rev. 156 (1967) 1541, and the so(2,1) tilting papers.
   - Georgi's unparticles (for "continuous mass spectrum at Δ ≠ integer").
   - Segal's chronometric cosmology (the 1976 book) **plus the observational tests of his redshift law and their verdicts.** It is a menu risk, so pin the refutations too.
2. **Re-key:** T1947's citation of T1939 (a mis-pointer: T1939 is K3/N_max, not the SO(5,2) ⊃ SO(4,2) extension). Add a Cayley-transform row to the registry (0 rows today) pointing to F475, F222 and T2625.
3. **Register:** A2 and 16/3 lines per Cal's word; T_bb per Casey's decision; the "19 colour-only" prediction marked FALSIFIED (T192).
4. Carried: the "no T_bb search exists" pin; the 1/Λ_QCD hadronization time; Fock's own text.

## CAL — adversarial after
1. Is "interior / boundary / continuum = elliptic / parabolic / hyperbolic" a position? My claim: yes, because conjugacy type is invariant. What does it NOT tell us? (Which element is physical time is a choice, and Segal made a different one.)
2. Hash Lyra item 1 (the E₀ = 3/2 vs λ = 5/2 tension) before she writes; rule on it after.
3. Hash Elie's tilt toy. The K1878 overlap test is yours: is it the same lane?
4. The D_IV⁵/D_IV⁴ table: mark every row position or coordinate.
5. T_bb: once Casey chooses, word the registered line.

## KEEPER
Fold results into the scorecard; hold the invariant-before-number rule; EOD on Casey's word.

---
## ADDENDUM 1 (11:38 EDT) — Casey decided T_bb: OPTION B (provisional), and asks "what is the winding closure gap?"
Casey's words, verbatim, and the setup are in K1928's addendum. **Key correction to the premise:** Grace's table has 7 exotics below threshold and 7 above, all within 30 MeV. The closure gap is the **signed** δ = M − M_threshold, a two-sided window.
- **Grace:** register the T_bb line as option B (proximity scoped to observed threshold states; T_bb = the discriminating test, registered before LHCb Upgrade II). Add the reduced mass μ and the lightest exchangeable meson for each thresholded state in R164's table.
- **Elie (freeze first):** choose the closure-gap unit blind (δ/M_thr, δ/m_π, or √(2μ|δ|)/Λ_QCD) and hash it. Then test whether |δ| is mass-independent (a boundary window) or tracks μ (one-pion exchange / ordinary QCD). Null first: random masses in ±200 MeV windows, as in 5802. Kill line: tracking μ ⇒ the window adds nothing beyond QCD.
- **Lyra:** does the Šilov boundary give a *window* in the parabolic (energy) picture? Tie it to spine item 2. A partial winding is an arc (Cal Section 989), so is the offset the arc's endpoint mismatch? One paragraph, direction before numbers.
- **Cal:** hash Elie's unit choice; rule whether "window" makes any prediction that ordinary QCD does not.
