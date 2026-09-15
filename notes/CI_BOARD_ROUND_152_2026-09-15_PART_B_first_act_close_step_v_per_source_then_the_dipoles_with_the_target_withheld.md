# ROUND 152 — Tuesday 2026-09-15, first act: close step (v) per-source; then (vi), the dipoles, with the CMB target withheld; (vii) Keeper; (viii) Cal; (ix) certify.

**Keeper, 2026-09-15 09:00 EDT (clock, substituted). SOD run: instrument ALL CURRENT; no overnight commits; the file is v1.4 (ea0ff18041a3…, K1906 §6). Read `notes/BST_TOMORROW_2026-09-15_PRIORITIES_AND_ANTI_STALE_PROTOCOL.md` first.** Rubric cell: External 5 (the named-experiment falsifier A9) / External 4.

## Assignments

**Elie — E1 (close (v), on v1.4):** per-source mask (§2.2: great-circle per source; the count must equal Keeper's **913,899** for G < 20.5 and **528,510** for G < 20.0 — print both); per-bin weights by the released code (commit 92eca506; Grace's venv has healpy/george/fitsio), < 0.5 excluded, weighted N_i; α_i by §3.2 on Grace's pinned pair (G: 3270 Jy at 621.79 nm; W1: 309.540 Jy at 3.3526 μm; ν_G/ν_W1 = 5.392 — zero points for both bands, never an AB offset); x_i three ways (edge derivative frozen; secant and 0.2-mag local beside it; half-spread systematic into σ_f; "curved counts" flag at 2σ); B_i smooth (frozen) with the §4.4 sensitivity (σ_z ×0.5/×2; outlier component at the paper's fraction — Grace's G20.5 pin, else 10 %) and sharp as diagnostic; g, g_w; χ̄_i; w_i; null-bin membership by the frozen rule; the randoms' ℓ = 1 moment under the frozen mask/weights. Post the closed table (JSON + board). **E2 — (vi):** on Keeper's witness of the closed table, the dipoles: the five count moments and the redshift moments (full sample; four G quartiles), the joint fit for one βû with covariance, the single-channel consistency fit (A′/C′), the G < 20.0 run beside it — **the CMB target withheld (Grace holds it); print the vector, its covariance, the χ²₃ against zero, the debiased norm — never the comparison to the CMB.**

**Keeper — K1:** witness (v) (recompute the mask count, α on two bins, x on one bin from the file); then (vii): the comparison under Section 5 by `play/keeper_partB_landing.py` in v1.3 mode from Elie's posted vector + covariance and Grace's β_CMB û_CMB; the letter with its clause; the hatch checks requested if B-level.

**Cal — (viii):** cold-read the comparison and the hatch checks after (vii); nothing before.

**Grace — G1:** the A9 line to v1.4's hash (ea0ff180…, verified K1906 §6); hold β_CMB û_CMB = (369.82 ± 0.11 km/s; l = 264.021°, b = 48.253° — Planck 2018, your pin) for step (vii) and hand it to Keeper only. **G2:** the ledger v0.56 line "Sourced-clean total: 6 of 26" is stale after row 5 (the SOD instrument parses it) — re-key to the generator's 5/12 in v0.57. **G3:** the G < 20.5 catastrophic-outlier fraction from the paper's text if it states one (Fig. 7 reads ≈ 9 %/16 % at 20.5 for >0.2/>0.1 — a plot read, not a pin).

**Lyra — L1:** Ch 04's one word (Input → Open for δ_CP's magnitude, A, the corner's value) and the L1 Doppler clause; then, optional and dated as an idea: **Casey's sentence this morning — "what Oppenheim calls randomness we call resolution limit"** — one paragraph on what N_max and τ₀ would predict for the statistics of a measured field's fluctuations (bounded, scale-fixed, non-accumulating) against the CQ master equation's Gaussian, linearly growing variance; a Section D marker, not a row.

**Casey — nothing owed.** The first sky vector appears at (vi) with the target withheld; the letter at (vii).

## Refusal list
No comparison to the CMB by anyone but Keeper at (vii); no reading of any published Quaia dipole analysis until (ix); no re-estimation after seeing a dipole; no number from memory; `date` substituted; NO EOD before 5pm.

— Keeper. Prompt file for Round 152.
