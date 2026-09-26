# Keeper — team prompt, ROUND 7 (Saturday 2026-09-26, 12:43 EDT). No EOD before 5pm.

**Casey (standing brief for today):** from the discrete interior of D_IV⁵ through the Šilov boundary into the continuum; energies; how D_IV⁵ projects into D_IV⁴. Be creative and optimistic, don't gate — investigate. Reconnect to the corpus; linear algebra on D_IV⁵.

**Rules:**
- Run `date`.
- Run `didwe` before opening a lane.
- Write the kill line first.
- **Quote the invariant before any number, and restate a colleague's antecedent verbatim before endorsing or correcting.** Keeper broke the second rule this morning (K1928 amendment).
- Pins come from the source; a search summary carried a stale PDG mass today.
- Write "Section", not the sign.
- Commit by path.

**Read first:** `notes/Keeper_K1929_*` (Part 1 = round-6 rulings; Part 2 = Casey's Fock question; Part 3 = the three findings). Then read K1928's second amendment (A2 certified FIRED; four Keeper corrections).

## The spine for round 7: one boundary, two realizations
- **Compact realization:** the Šilov boundary is (S⁴ × S¹)/ℤ₂, the conformal compactification of ℝ^{1,4}. J rotates the S¹, so the spectrum is **discrete**. This is Fock's mechanism (a stereographic sphere) one dimension up.
- **Flat realization:** ℝ^{1,4}. The generator is P₀, and the spectrum is **continuous**.
- **The interior** is what both reconstruct (Szegő exponent 5/2).
- **The frame:** choosing the sl(2,ℝ) leaves **SO(4)** (instrument, ALL PASS), so SO(5,2) ⊃ SL(2,ℝ) × SO(4). That is hydrogen's radial × angular structure with **four** space dimensions.
- **The minimal representation (λ = 3/2) should be hydrogen in four space dimensions:** ν = 3/2 + m, degeneracies 1, 5, 14, 30. **To be verified.**
- **Discrete → continuum** is the R → ∞ limit (Stephanov's deconstruction).
- **Segal's lesson is binding:** the compact realization is never read as a cosmological redshift.

## Waiting on Casey
1. **Time, Derived:** Lyra's two one-line fixes (line 19 "Bergman" → Hardy H²; line 26 carrier → the Rac). Keeper and Cal recommend GO.
2. **The register's local model** (qwen3:30b-a3b is gone): trial qwen3.6:35b against the 11 controls, yes or no?

---
## LYRA
1. **Fock through the boundary (K1929 Part 2).**
   - Write the compact/flat pair as linear algebra: J on L²(S¹) ⊗ harmonics(S⁴) vs P₀ on ℝ^{1,4}. State the conformal compactification as the stereographic map it is.
   - Say exactly where Fock's S³ sits (the SO(4) restriction of S⁴'s harmonics, K1927(b)).
   - Answer Casey in one paragraph: bound = compact realization, continuum = flat realization, and no "exterior".
   - Mark each clause position or coordinate. Reconnect F475, T2625, F222.
2. **The frame SL(2,ℝ) × SO(4).**
   - Is this the dual pair behind your 5808 decomposition ⊕ D⁺_{5/2+i+2m} ⊗ (i/2, i/2)?
   - Write the radial/angular split, and name what the SO(4) becomes after the descent (T2545: (3,1)).
   - Is "the frame = the Machian input of T2565" one choice or two?
3. **Hydrogen in four space dimensions** (K1929 Part 3(b)).
   - State the correspondence: minimal representation of SO(5,2) ↔ d = 4 Coulomb bound spectrum (ν = 3/2 + m).
   - Then say how the projection D_IV⁵ → D_IV⁴ acts on it: the minimal representation restricts to H_{3/2} ⊕ H_{5/2} and never contains 3-space hydrogen (λ = 1). That is, 4-space hydrogen does not contain 3-space hydrogen. **Is that a statement about Gauss's law (1/r² potentials differ by dimension) in representation language?**
   - Menu risk: every D_IV^n has its own d = n − 1 hydrogen. Write the result as a recapitulation.
4. **Processes = boundary correlators.**
   - The two-point function from the Szegő kernel h^{−5/2}, in the flat realization (a Δ = 5/2 conformal two-point function in 5D) and in the compact realization (a discrete sum over the clock ladder).
   - The 4D restriction: the sum over Δ = 5/2 + k.
   - Where does the ruler R enter?
5. **Time, Derived:** apply your two fixes the moment Casey says GO. Cal gate-reads them.

## ELIE (hash first, controls first)
1. **Hydrogen in d = 4 (verifies K1929 Part 3(b)).**
   - Solve the d-dimensional Coulomb problem exactly or symbolically for d = 3, 4, 5.
   - Check the ν offsets (d−1)/2 and the level degeneracies against the minimal representation of SO(d+1, 2): weights (d−1)/2 + m, K-types = harmonics in d+1 variables.
   - **Control:** d = 3 must give λ = 1 and n² (K1927). **Kill:** a mismatch at d = 4.
2. **Deconstruction toy:** BST's boundary two-point function at finite R, as a discrete sum over the clock ladder 5/2 + k with Hardy multiplicities.
   - Show that its R → ∞ limit converges to the Δ = 5/2 generalized-free-field Källén–Lehmann density, then do the 4D restriction.
   - **Controls:** the minimal representation (λ = 3/2) must give the free massless field in 5D (the unitarity bound). A wrong multiplicity must fail to converge.
3. **Closure gap (Addendum 1, still owed):** freeze the unit blind (Cal hashes). Test whether |δ| is mass-independent (a window) or tracks μ (one-pion exchange / ordinary QCD) on Grace's 17-state class. Null first.
4. Carried: nothing else.

## GRACE (pins from the source)
1. **Nieto 1979** (Am. J. Phys. 47, 1067–1072): the d-dimensional Coulomb levels and degeneracies, text pin. **Bars et al.** (arXiv:2001.08818, hydrogen and oscillator via hidden SO(d,2)): what they say about SO(d+1,2) and d-dimensional hydrogen.
2. **Fock 1935:** the stereographic-projection passage (you found the scan). Pin the lines for Lyra's paragraph.
3. **Stephanov 2007 deconstruction:** the spacing → 0 limit statement and the density formula. **Källén–Lehmann density for a scalar of dimension Δ in d dimensions:** pin the exponent (Δ − d/2) from a source.
4. **Exotics:**
   - the width-scaled test (the next instrument you named);
   - **X(6900)'s χ_c0χ_c1 threshold:** Keeper pinned PDG 2026 at 3415.50 ± 0.19 + 3510.67 ± 0.05 = 6926.17 MeV, so δ ≈ −28 MeV. It was named after reading, so it stays out of A14's count. Decide whether a quarkonium-pair class can be fixed in advance for a future count;
   - the combined LHCb–ATLAS–CMS X(6900) parameters (arXiv:2604.18061).
5. **Register:** A2's certified word (K1928 amendment); Segal's line in T2632 (done); a row for "compact/flat realization = discrete/continuous" once Cal rules.

## CAL (adversarial after)
1. K1929 Part 2 (Fock through the compact boundary): position or coordinate? What does it NOT license? (The redshift, per Segal; anything else?)
2. K1929 Part 3(b): hash Elie's d = 4 hydrogen prereg. Is "the Wallach seed = 4-space hydrogen's ground ν" a recapitulation or a menu?
3. Hash Elie's deconstruction toy and the closure-gap unit.
4. Gate-read Time, Derived's two fixes when Casey says GO.

## KEEPER
Fold results into the scorecard; certify register words; EOD on Casey's word.
