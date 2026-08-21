# The C₂↔n_C collision family — signature-sweep correction index (Grace, Round 31, 2026-08-21)
*Casey's ask: run the SIGNATURE SWEEP (structural, not a string grep) to find the whole C₂↔n_C collision family. Instrument = toy 5417 (reusable). Correction justified by Elie's 4-way bidisk pin (genus=n_C=5) + Hua 1963 — a structural pin beats the mis-cited exponent. ~27 collisions across ~20 files → coordinated pass, each owner on their files, re-run toy 5417 to verify zero. NOT unilaterally mass-edited (don't-clobber).*

## The signature
For a **D_IV⁵ scalar Bergman kernel**, the π-power (Bergman VOLUME over complex-dim-5 → π^{n_C}=π⁵) and the kernel EXPONENT (genus = n_C = 5) must BOTH be 5. A disagreement flags the collision: the exponent was written as **6 (=n_C+1=C₂)** or **7 (=g)** — the genus conflated with the Casimir or the fermion mode-weight. **Fix: the scalar Bergman kernel exponent is n_C = 5** (K = c·N^{−n_C}, Hua 1963; K1213; Elie bidisk 4-way). Prefactor 1920/π⁵ = K(0,0) is unchanged.

## Class A — N⁻⁶ (conflate genus 5 with C₂=6) → N⁻⁵  [17]
BST_AlphaSquared_LayerProof:50, BST_Arithmetic_Algebra_Spacetime:285, BST_BaryonCircuit_ContactIntegral:474, BST_BoundaryIntegral_Final:53, BST_ClaimB3_KType:414+561, BST_ElectronMass_BergmanUnits:40, BST_Interstasis_Hypothesis:194, BST_LinearAlgebra_Physics:403, BST_MissingLemma_ClebschGordan:36, BST_QFT_Foundations:41+158+603, BST_SchrodingerEquation_Substrate:43, BST_SubstrateContactDynamics:60, BST_TsirelsonBound_Holomorphic:674, BST_Wyler_Connection:75 *(this one EXPLAINS "Factor 6 = n_C+1" — needs a prose fix, not just a digit)*.

## Class B — N⁻⁷ (conflate genus 5 with g=7) → N⁻⁵  [10]
BST_B14_Substrate_Not_Made_Of_Anything:32+58, BST_BSD_Native_Closure_Framework:108, BST_Discretize_Then_Count:44, BST_Nuclear_Physics_Paper:57, BST_Observer_Particle_Synthesis:131, BST_Paper20_QM_Draft:91, BST_Paper20_QM_Is_Geometry_Draft:100, BST_QFT_Foundations:71, BST_YM_AC_Proof:35.
- **★ Fermion-kernel CAVEAT (per-file judgment):** a genuine FERMION discrete-series kernel legitimately has exponent g=7 (K1213 fermion mode-weight). BUT every flagged N⁻⁷ line here carries the **scalar prefactor 1920/π⁵ or the label K_B / "Bergman kernel"** — i.e. it claims to be the SCALAR kernel with the fermion exponent → collision → 5. If any owner's line is genuinely the fermion kernel (different prefactor, explicit "fermion/spinor" label), leave it and note the label.

## Ambiguous / verify (not auto-corrected)
- **BST_SubstrateEngineering_Textbook_Outline:52** ("N^{-g+1}"): uses g → collision, but the exact form (−g+1=−6 vs −(g+1)) needs reading. Fix to −n_C=−5.
- **BST_YangMills_Question1:232** (π^{2,5} vs kernel^1): likely a PARSE ARTIFACT (a stray "^1"), not a Bergman-kernel line — REVIEW, probably a false positive.

## Confirmed FALSE POSITIVES — do NOT "correct" (different objects; the instrument excludes them by design)
- **c_FK / FK-normalized kernel** (π^{9/2}, exponent n_C/rank=5/2 — Keeper Vol16 Ch13): a different convention; 9/2 and 5/2 are consistent. Not a collision.
- **Volume constant** Vol(D_IV⁵)^{−1}=1920/π⁵ (Paper81): the volume, no kernel exponent.
- **g/rank = 7/2** and **ρ = 9/2**: correct different objects (Round 30, left untouched).

## Status + hand-off
- **ElectronMass_Derivation:40 already corrected** (Round 30). **ElectronMass_BergmanUnits:40 (Martin kernel :201 is separate — different kernel, Elie verifying).**
- **@team:** each owner corrects their Class-A/B lines (scalar Bergman exponent → n_C=5), applies the Wyler-Connection prose fix, resolves the two ambiguous lines, and **re-runs `toy_5417` to verify zero collisions.** The instrument is the acceptance test.
- **@Elie:** your Hua-reading is the citation-side confirmation; the structural bidisk pin already licenses the fix now.
**Tier:** hygiene/correction (mechanical instrument + coordinated index). **Edges:** toy 5417, K1213, Hua 1963, Round-30 ElectronMass fix.

---
## ★ CORRECTED & VERIFIED (Round 32, owner-by-owner, sweep-after-fix)
**28 lines corrected** (17 Class-A N⁻⁶ + 10 Class-B N⁻⁷ + SubstrateEngineering N^{-g+1}=−6), each a targeted per-line edit with before/after log (NO mass-sed). The Wyler line got the **prose fix** (its "Factor 6 = n_C+1" reasoning corrected — the exponent is the genus n_C=5, not n_C+1=C₂). **Fermion-kernel guard held:** every Class-B line carried the scalar 1920/π⁵ prefactor or K_B label (all collisions); no genuinely-fermion line was touched. **Sweep-after-fix (new standing rule):** re-ran toy 5417 → the family is CLEARED; the one residual (YangMills:232) was the **K(0,0)=(π⁵/1920)⁻¹ volume-inverse** false positive — instrument refined to exclude exponent-1 artifacts → **clean zero.** The suspicious auto-fixes (B14/BSD/Interstasis) verified: all genuine Bergman-kernel formulas; the integers {3,5,7,6,137} and 137 intact, only the exponent changed.
