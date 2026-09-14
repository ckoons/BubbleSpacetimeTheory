# ROUND 149 — PART B: download on v1.2 (header first); v1.3 = x at the threshold + the vector, not the norm; then step (v).

**Keeper, 2026-09-14 12:20 EDT (clock, substituted). Read K1903 first.** Quaia is A/B-capable (joint σ_β c = 149 km/s, Elie 5760). Two control-forced corrections are declared for v1.3 before any per-bin factor or dipole is computed: (i) x_i at the selection limit (quadratic fit in the 0.5-mag window, derivative at the edge — Secrest et al. arXiv:2501.06450 p. 2, "at the threshold"); (ii) Section 5's A/B comparison on the fitted vector by χ²₃ (Elie: norm bias 1.20 at S/N 2.5). Rubric cell: External 5 / External 4.

## Assignments

**Elie — E1 (now, on v1.2): step (iv).** Download Quaia v1.0.0 (Zenodo 10.5281/zenodo.10403370); post the FITS header verbatim as the first act; report any header–Table 2 mismatch. Compute nothing else until v1.3's hash. **E2 (synthetic, no freeze):** the ΔA·ŵ rerun of S6 with A scaled between the cuts by the frozen profile's n(z) ratio — post the residual along ŵ⊥ in σ. **E3 (synthetic, no freeze):** on the E1 synthetic Quaia, x_i by the linear 0.5-mag fit vs the quadratic-at-the-edge form, per bin, and the β̂/β_inj each gives — so the size of correction (i) is a posted number before the sky.

**Cal — C1: v1.3.** Items (i) and (ii) as K1903 §2 states them, K1901 §3's §1 number; nothing else; scope in §9b; post the diff; hash. One word on Elie's question is folded in: the 0.5-mag window stays as the window; the estimator inside it changes to the edge derivative.

**Keeper — K1.** Verify v1.3 from the file; diff-audit against (i)–(ii); witness the FITS header; then the step-(v) table (x_i both forms, α_i, B_i both forms, g and g_w, null-bin membership, N_i, χ̄_i) before any dipole; landing by `keeper_partB_landing.py` in v1.3 mode. K1902 (row 5) stays open for Cal's answer.

**Grace — G1.** Table 2's exact published magnitude limits (20.0 / 20.5 as printed) — one line; the A9 line's hash to v1.2 now and v1.3 when verified; the two prior-art pins of K1903 into the row's apparatus (Secrest et al. 2025 review arXiv:2501.06450; Siewert et al. 2021 A&A 653, A9).

**Lyra — L1.** Vol 3 Ch 03 (forces/cosmology) in the Section-13 shape; the one line in Ch 02's "what would make this wrong" naming E4. **L2 (one paragraph, if it is true):** the kinematic moment as a derivative at the window edge — the same edge whose motion is B_i — in the operator picture: is x_i the boundary derivative of the Rac factor's count law, and B_i the boundary derivative of the clock window, so that f_i − 2 is one boundary term read on two factors? If not, say where it breaks.

**Casey.** Nothing owed. The first sky object on the board is a FITS header; the first sky number waits on v1.3.

## Refusal list
No per-bin factor and no dipole before v1.3's hash; the download itself on v1.2 (a recording); nothing in v1.2 changed outside (i)–(ii) + §1's number; no number from memory; `date` substituted; no published Quaia dipole analysis until step (ix); the CMB target withheld from Elie at (vi).

— Keeper. Prompt file for Round 149.
