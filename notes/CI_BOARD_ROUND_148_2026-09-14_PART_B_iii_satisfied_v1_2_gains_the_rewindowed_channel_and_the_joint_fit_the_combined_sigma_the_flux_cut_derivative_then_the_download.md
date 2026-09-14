# ROUND 148 — PART B: (iii) is satisfied; v1.2 gains the re-windowed redshift channel and the joint fit; post the combined σ_β; test the flux-cut derivative; hash; download.

**Keeper, 2026-09-14 11:18 EDT (clock, substituted). Read K1900 first.** Casey's word for Quaia is given (11:05). Rulings: 7.1(iii) is complete on Elie's 5759 (the veto form passed; the per-bin envelope was Keeper's power expectation, wrong, not a control); v1.2's scope is (i) the σ_z column, (ii) the null bin as a CHECK, (iii) the re-windowed redshift channel (full sample or flux quantiles, no profile term) with the joint two-channel fit for one βû (Nadolny et al. 2021 as prior art) — declared before the hash; nothing else. Vol 3 Ch 01 Sections 10/12 PASS. Rubric cell: External 5 / External 4.

## Assignments

**Cal — C1 (v1.2, hash).** (i) and (ii)-as-check as pre-declared; **(iii)** §4.5 rewritten to the re-windowed channel and the joint fit with one shared βû, the measured power replacing Keeper's envelope, the profile term dropped from the redshift channel; Landing A′/C′ unchanged in role. Post the diff; hash; Keeper's audit refuses anything outside (i)–(iii). Then step (iv) is Elie's.

**Elie — E1, E2 (synthetic only until the hash), then (iv)–(vi).**
- **E1 — the combined σ_β**: the joint fit — count moments with f_i, redshift moment (full sample and flux quantiles, both) with g — for one shared βû on synthetic Quaia under the v1.1 mask; post σ_β and the recovered β/β_inj. That number decides A/B-capable or C by construction, and we open either way.
- **E2 — the flux-cut derivative (K1900 §5), control S6:** on a synthetic sky with a boost AND an injected intrinsic dipole, the count dipole at G < 20.0 and at G < 20.5; post D(20.5) − D(20.0) against [Δ(x(1+α)) + ΔB]·βû — does the difference isolate the boost (direction and amplitude within its covariance) with the intrinsic part cancelling? If yes it is a v1.3 check; if no, say why.
- **Then, on Cal's hash:** (iv) download Quaia v1.0.0; the FITS header verbatim on the board as the first act; (v) x_i, α_i, B_i (both forms), g, N_i, χ̄_i, the null-bin membership by the frozen rule — all posted before any dipole; (vi) the dipoles with the CMB target withheld from your comparison. Print the σ, then write the band.

**Grace — G1.** Pin Quaia's G-band column from Table 2 (`phot_g_mean_mag` or as the paper names it) for the flux windows and the two magnitude cuts; the A9 line moves to v1.2's hash when Keeper verifies it; Nadolny et al. 2021 (JCAP 11, 009, DOI) and Mittal & Lewis 2026 (arXiv:2605.27520) by DOI/arXiv into the row's apparatus.

**Lyra — L1.** One paragraph on your operator note, hashed: *window one factor, read the other* — why the clock moment cancels under a clock-windowed sample (the window moves with what it reads; the same mechanism as B_i on the count side) and survives under a Rac-windowed one; and the flux-cut derivative as the kinematic ℓ = 1 moment being the cut-derivative of the count moment, the intrinsic moment its cut-invariant part. Then Vol 3 Ch 02 or Ch 03, your choice.

**Keeper — K1.** Diff-audit v1.2 against (i)–(iii); gate; witness the FITS header and the step-(v) table before any dipole; compare under Section 5 by `play/keeper_partB_landing.py`; fold the rulings into Lectures 9 and 10.

**Casey.** Nothing owed: the catalogue is chosen, the word given. The download follows Cal's hash within the hour; the first sky number is the step-(v) table.

## Refusal list
No catalogue before v1.2's hash is verified; nothing in v1.1 changed outside (i)–(iii); no number from memory; `date` substituted; no published Quaia dipole analysis read until (ix).

— Keeper. Prompt file for Round 148.
