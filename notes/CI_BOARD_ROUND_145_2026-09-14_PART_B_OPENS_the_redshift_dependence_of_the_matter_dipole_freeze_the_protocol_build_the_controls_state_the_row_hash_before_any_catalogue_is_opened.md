# ROUND 145 — PART B OPENS: the redshift dependence of the matter dipole. Freeze the protocol, build the controls, state the row; hash before any catalogue is opened.

**Keeper, 2026-09-14 (Monday) 09:47 EDT (clock). Casey's word at 09:45: "Let's do Part B."** Part A closed at the referee's gate at 09:41 (rubric Section 2, this morning's entry). The draft is `notes/BST_PREREGISTRATION_DRAFT_Part_B_1_the_redshift_dependence_of_the_matter_dipole_one_boost_not_two_Keeper_2026-09-14.md`; read it in full before anything else — it is the object this round freezes. Rubric cell: **External 5 (a new quantitative prediction) and External 4 (the descent's falsifier).** Lineage: Cal's 08-21 pre-registration; Lyra L3 (ε had no host); Cal §957 (ε = the rapidity between the radiation and matter rest frames as ℓ = 1 moments — one boost, not two); Grace's A9 row (register v0.8, Secrest 2022 pinned from the PDF).

**The rule of this round, and it is absolute:** no catalogue is opened, downloaded, or read — by anyone — before the frozen protocol is hashed and Keeper has verified the hash. A bar with an unfrozen procedure is a tuning channel. The controls run on synthetic data only until then.

**The claim under test (P1, an order statement, no knob):** once the redshift-dependent (intrinsic) component of a distant-source dipole is separated by the frozen method, the redshift-independent remainder has the CMB boost's amplitude and direction — 369.82 ± 0.11 km/s toward (l, b) = (264.02°, 48.25°), Planck 2018 — in every redshift bin within the frozen tolerance. Landing A holds; Landing B (two boosts surviving the hatch) fires A9 and falsifies the Machian descent; Landing C (not separable at the catalogue's depth) is reported as such.

**Casey's one choice, proposed unless he says otherwise:** the first catalogue is **Quaia** (Storey-Fisher et al. 2024, Gaia DR3 × unWISE quasars with spectrophotometric redshifts, ~1.3 million sources, published selection function and mask) — it is the one catalogue that carries per-source redshifts at all-sky depth, which is what P1's bins need. CatWISE2020 second (the Secrest sample, for continuity). Neither is opened this round.

## Assignments

**Cal — C1, C2. The freeze is yours.**
- **C1 — freeze the protocol.** Take the draft's Section 4 and make each item a sentence that cannot be adjusted after a number is seen: the redshift-bin edges and minimum counts; the per-bin $(x, \alpha)$ prescription (Ellis–Baldwin as published; from the catalogue's own counts and spectral indices, computed before any dipole); the separation model (the frozen functional form for the redshift-dependent component; the degeneracy criterion that returns Landing C); the tolerance (per-bin propagated uncertainty on the amplitude; the 95% positional uncertainty on the direction); and the hatch checks — the named systematics and the test each must pass (Galactic mask, flux/magnitude limit, ecliptic/scanning-pattern residuals, Malmquist-type effects, the known Gaia scanning-law imprint in Quaia's selection function), carried from your 08-21 §5. Blind pre-questions hashed before you open the draft. Output: `notes/BST_PREREGISTRATION_Part_B_1_FROZEN_v1_Cal_*.md` with its SHA256 on the board.
- **C2 — the landings' can-fail check.** Before the hash: confirm in writing that P1 can fail (an order-one residual boost in a bin is Landing B), that Landing A is not vacuous (state the synthetic case that would produce B), and that no clause lets a large intrinsic dipole rescue P1.

**Elie — E1, E2 (synthetic data only, this round).**
- **E1 — the estimator.** A per-bin Ellis–Baldwin dipole estimator (amplitude, direction, and the propagated uncertainties from counts) that takes a source list with redshifts, a mask, and per-bin $(x, \alpha)$. Written before the catalogue; `/toy claim` first.
- **E2 — the two controls, posted as numbers.** Positive: a synthetic isotropic population on the sky, boosted at a known $\beta$ and direction, drawn with a Quaia-like mask and depth — the estimator must recover the injected velocity and direction in every bin within the frozen tolerance (report the recovered numbers per bin, blind to the injection until compared). Negative: a synthetic clustering dipole (large at low $z$, falling) with no boost — the separation step must return redshift dependence and no kinematic residual. Both controls are the instrument's license; without them nothing is measured.

**Lyra — L1.**
- **L1 — the row.** P1 as a registry statement: inputs T2564/K1522 (the frame is the exterior's state recorded through the photon channel — one exterior, no matter channel), T2565, Cal §957; the sentence that says *why* a kinematic dipole must be the CMB's under the descent; and the honest scope — what the rows license (one boost) and what they do not (any statement about the intrinsic component). If the rows license less than P1, say so and P1 narrows before it is frozen. Hashed before posting.

**Grace — G1.**
- **G1 — pin the inputs.** Quaia's DOI, version, selection function and mask; the Planck 2018 CMB dipole (velocity, direction, uncertainties) from the primary; Secrest 2022 and Darling 2022 by DOI; Ellis & Baldwin 1984 by page. Into the A9 row as "PRE-REGISTERED P1 (hash …)" only when Cal's frozen file has its hash. Until then, the pins.

**Keeper — K1.** Verify the hash matches the frozen file before any catalogue is opened; verify the controls ran blind; certify the landing after; fold the row into Lecture 9 and Lecture 10's Section-A list. Nothing else touches the estimator's comparison code but Elie, and it is retained with the run.

## Refusal list
- No catalogue opened before the hash. No exceptions, no "just to check the format."
- No tolerance, bin edge, or hatch check written after a real dipole is seen.
- No number for the CMB dipole or Secrest's amplitudes from memory — the primaries, pinned by Grace.
- No "BST predicts" in any sentence until the row is stated and the file is frozen.
- `date` in the same command as every timestamp (Keeper's own failing this week, six times).

— Keeper. Prompt file for Round 145.
