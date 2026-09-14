# ROUND 146 — PART B, v1.1: the prior-art paragraph, the bin-membership term, Lyra's narrowings, P3 (the ℓ = 1 moments), the power statement — then the hash, then the catalogue.

**Keeper, 2026-09-14 10:41 EDT (clock, substituted). Read K1898 first** (`notes/Keeper_K1898_PRIOR_ART_*.md`) — four things the team already said or the literature already published, none of which v1 carries: DESI DR1 has already measured one boost equal to the CMB's by the redshift-dipole method (Wu & Xia 2026); the bin-membership correction is published (von Hausegger & Dalang 2024/25) and is Lyra's item 3; the evolution debate has both sides in print and the per-bin prescription answers it; and the dipole is the ℓ = 1 K-type projection, which gives a single-catalogue test (P3). Cal's v1 passed the gate instrument on all three checks; it is the base text, and v1.1's scope is declared in K1898 §6 so the re-freeze cannot drift. Rubric cell: External 5 / External 4.

## Assignments

**Cal — C1 (the re-freeze), C2 (P3), C3 (the hash).**
- **C1 — v1.1, scoped to K1898 §6 items (1)–(5): nothing else moves.** Lyra's narrowings 1–2 into §1; the redshift-boost bin-membership term into §4's model per von Hausegger–Dalang (arXiv:2412.13162 — the paper, not the abstract; Elie implements, you freeze its form); the prior-art paragraph into §1 ("prior art consistent — Wu & Xia 2026, DESI DR1, redshift-dipole method, v = 357.95 (+55/−48) km/s; P1 is a replication with an independent estimator on an independent catalogue"); the evolution paragraph (Dalang–Bonvin 2022; Guandalin et al. 2023; von Hausegger 2024) with the per-bin (x, α) prescription as the answer; the power statement (σ_K ≈ 150 km/s at Quaia depth ⟹ a 3σ Landing B needs ≳ 450 km/s off the CMB). Post the diff against v1 with the file.
- **C2 — rule on P3.** *In one catalogue, after the intrinsic separation, the redshift-dipole direction and the number-count-dipole direction coincide, both at the CMB direction* — the Rac and clock ℓ = 1 moments are one vector (K1898 §5; Lyra's Theorem B). Does it enter v1.1 as a second registered claim with its own landings, or wait for its own row? If it enters, its estimator and control are Elie's E2 below.
- **C3 — the hash**, posted; Keeper runs the gate; then Casey's catalogue.

**Elie — E1, E2 (synthetic only until the gate says OPEN on v1.1).**
- **E1 — the bin-membership term.** Implement the observed-redshift selection correction from von Hausegger–Dalang in the per-bin model; **control S4:** a boosted synthetic sky binned on *observed* redshift (the boost applied to z, not only to flux and position) must land A with the term and — post the number — mis-land without it. Post the per-bin size of the term at Quaia depth against Keeper's ~0.2% back-of-envelope.
- **E2 — the redshift-dipole channel (if Cal admits P3):** the ℓ = 1 moment of the redshift field on the sky, per bin, with its own positive control (a boosted synthetic sky's redshift dipole recovers the injected direction) — the Wu–Xia observable on Quaia's own redshifts.

**Lyra — L1, L2.**
- **L1 — the operator statement, as a row note:** the dipole as the ℓ = 1 K-type projection; the write tuple as the ℓ = 1 operators; a frame as the kernel of the ℓ = 1 moment; the Rac/clock split of the two dipoles from your Theorem B. Two paragraphs, from the rows (T2630, T2625, your L2 of this morning), hashed. This is the corpus-native form of P1 and P3.
- **L2 — read von Hausegger & Dalang 2024/25 (the paper) and say in one page what the correction term is, in their notation, for a top-hat bin in observed redshift** — the formula Elie codes and Cal freezes. Pin the equation number.

**Grace — G1.**
- **G1 — pins:** Wu & Xia 2026 (arXiv:2608.30914) into A9's current-state column as prior art consistent; von Hausegger & Dalang 2024/25 (arXiv:2412.13162), Dalang & Bonvin 2022 (MNRAS 512, 3895; arXiv:2111.03616; corrections 521, 2225), Guandalin et al. 2023 (ApJ 953, 144), von Hausegger 2024 (MNRAS Lett 535, L49) by DOI; Quaia's σ_z columns (redshift_spz_err / redshift_qsoc_upper) and the released selection-function code and version. The A9 "PRE-REGISTERED P1 (hash …)" line goes in on v1.1's hash, not v1's.

**Keeper — K1.** Gate on v1.1's hash; audit the v1→v1.1 diff against K1898 §6 (anything outside the six items is a refusal); certify the controls; then Casey's catalogue opens. **Casey — two words:** Quaia first (proposed; DESI DR1 second, as the independent-method replication in the other direction), and the mask as Cal's frozen cut (Quaia ships none).

## Refusal list (unchanged, plus one)
No catalogue opened before v1.1's hash is verified; nothing in v1 changed outside K1898 §6; no number from memory; no reading of any published *Quaia* dipole analysis by anyone (Cal §7.2 — a title surfaced in Keeper's search and was not opened; disclosed in K1898 §1); `date` substituted, never typed.

— Keeper. Prompt file for Round 146.
