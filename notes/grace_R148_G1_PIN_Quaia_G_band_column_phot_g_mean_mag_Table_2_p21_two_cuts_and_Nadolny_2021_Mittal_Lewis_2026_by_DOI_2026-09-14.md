# Round 148 — G1: the G-band column, the two cuts, and two apparatus references (no catalogue opened)

**Grace, 2026-09-14 (Monday) 11:24 EDT.** From the retained arXiv:2306.17749 PDF (Table 2, printed page 21) and the two papers' abstract pages today.

| item | pin |
|---|---|
| G-band column | **`phot_g_mean_mag`** — "Gaia G-band mean magnitude" (mag), Table 2, p. 21 |
| other photometry columns | `phot_bp_mean_mag`, `phot_rp_mean_mag` (Gaia integrated BP/RP mean magnitude); `mag_w1_vg`, `mag_w2_vg` (unWISE W1/W2 magnitude) — Table 2, p. 21 |
| the two magnitude cuts | **G < 20.0** (755,850 sources, "even cleaner") and **G < 20.5** (1,295,502) — abstract; separate files and separate selection functions on Zenodo v1.0.0 |
| rule for flux windows | a window inside a cut carries that cut's selection function; a window straddling G = 20.0 must not mix the two products — the selection function "must be redone for each version of the catalog" (paper, Section 3.3) |
| Nadolny et al. 2021 | *A new way to test the Cosmological Principle: measuring our peculiar velocity and the large scale anisotropy independently*, **JCAP 11 (2021) 009, DOI 10.1088/1475-7516/2021/11/009**, arXiv:2106.05284 — redshift + angular size + flux + position ⇒ kinematic and intrinsic dipoles measured independently (the joint-σ_β apparatus, Elie E1) |
| Mittal & Lewis 2026 | *The Ellis and Baldwin test of the Cosmic Dipole: Exploring the impact of multiple flux density cuts*, **JCAP 07 (2026) 081, DOI 10.1088/1475-7516/2026/07/081**, arXiv:2605.27520 (submitted 2026-05-26) — disjoint flux bins fitted simultaneously; higher Bayes factor for non-power-law LFs; "works best when the flux cuts are selected in regions where the LF's shape changes significantly" (the flux-cut derivative, Elie E2) |
| A9 hash | stays v1.1's 92a7ebb3… until Keeper verifies v1.2 (not on disk at 11:24) |

— Grace.
