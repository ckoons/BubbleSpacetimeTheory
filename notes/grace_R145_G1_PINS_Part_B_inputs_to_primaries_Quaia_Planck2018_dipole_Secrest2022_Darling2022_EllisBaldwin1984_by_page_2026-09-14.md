# Round 145 — G1: the inputs of Part B.1, pinned to primaries (no catalogue opened)

**Grace, 2026-09-14 (Monday) 10:06 EDT.** Every line below was read today from the primary's own page or from a PDF retained in the session scratchpad (SHA256 prefixes given), not from memory. **The round's absolute rule was kept: no catalogue file was downloaded or read.** The Quaia pin is from the paper and the Zenodo record's *metadata page* (file names and sizes as listed there); the FITS files were not fetched. The A9 row gains "PRE-REGISTERED P1 (hash …)" only when Cal's frozen file exists with its SHA256 on the board — it does not yet (checked 10:06).

## 1. Quaia — the first catalogue (Casey's choice, proposed)

| item | pin |
|---|---|
| paper | Storey-Fisher, Hogg, Rix, Eilers, Fabbian, Blanton, Alonso, *Quaia, the Gaia–unWISE Quasar Catalog: An All-Sky Spectroscopic Quasar Sample*, **ApJ 964, 69 (2024), DOI 10.3847/1538-4357/ad1328**; arXiv:2306.17749 (PDF retained, sha256 fa23d369…) |
| data record | **Zenodo DOI 10.5281/zenodo.10403370, version 1.0.0, published 2023-12-18**, CC BY 4.0 |
| samples | "The final catalog has **1,295,502** quasars with G < 20.5, and **755,850** candidates in an even cleaner G < 20.0 sample" (abstract) — files `quaia_G20.5.fits` (171.0 MB), `quaia_G20.0.fits` (99.8 MB) |
| redshifts | Gaia DR3 QSO-candidate redshifts improved by a **k-nearest-neighbours model trained on SDSS redshifts**; final z_Quaia = z_Gaia where the two agree to \|Δz/(1+z)\| < 0.05, z_kNN where they differ by > 0.1, a blend between (paper Section 3.2); quoted precision: 86 % of Gaia-DR3 sources with \|Δz/(1+z)\| < 0.01 vs SDSS for the clean subset (Section 2) — the per-bin redshift error is what Part B's bins must carry |
| selection function | Section 3.3: a Gaussian-process model of source counts per **HEALPix NSIDE = 64** pixel (49,152 pixels, ~0.84 deg² each) against templates — dust (Chiang 2023 E(B−V), ×0.86 Schlafly–Finkbeiner, R_V = 3.1), Gaia stellar density (18.5 < G < 20), unWISE source density, and the parent surveys' scan patterns; fitted separately per magnitude cut — released as `selection_function_NSIDE64_G20.0.fits` and `selection_function_NSIDE64_G20.5.fits` (400.3 kB each) plus `selection_function_template_maps.zip`; random catalogues `random_G20.0_10x.fits`, `random_G20.5_10x.fits` |
| mask | **The paper releases NO separate mask file.** Its guidance (Section 3.3 / Section 6): the selection function is less accurate near the Galactic plane and around the LMC/SMC — "precision measurements may require masking this region … users may want to mask this area." **So the mask is a CHOICE Part B must freeze**: a \|b\| cut, an LMC/SMC exclusion, and a selection-function floor, stated in Cal's frozen file before the catalogue is opened. This is the one input the primary does not fix. |
| Gaia scanning-law imprint | the selection-function templates include the parent surveys' scan patterns (Section 3.3) — Cal's added hatch check for Quaia has a named object in the primary |

## 2. Planck 2018 — the CMB (radiation) frame

**Planck Collaboration, *Planck 2018 results. I. Overview and the cosmological legacy of Planck*, A&A 641, A1 (2020), DOI 10.1051/0004-6361/201833880**; arXiv:1807.06205 (PDF retained, sha256 dca93289…). **Section 2.1 "The Solar dipole", Table 2 (Planck 2018 combined) and Table 3:**
- amplitude **3362.08 ± 0.99 μK**
- direction **(l, b) = (264.021 ± 0.011°, 48.253 ± 0.005°)**
- **β ≡ v/c = (1.23357 ± 0.00036) × 10⁻³, v = (369.82 ± 0.11) km s⁻¹** (Section 2.1, text following Table 2).
The draft prereg's "369.82 ± 0.11 km/s toward (264.02°, 48.25°)" matches the primary to the digits it quotes.

## 3. Secrest et al. 2022 and Darling 2022 — by DOI

- **Secrest, von Hausegger, Rameez, Mohayaee, Sarkar, *A Challenge to the Standard Cosmological Model*, ApJL 937, L31 (2022), DOI 10.3847/2041-8213/ac88c0**, published 2022-09-28; arXiv:2206.05624 (PDF retained 09-14 08:4x, sha256 in the 09-14 checkpoint). Numbers on the A9 row are from its text (09-14 08:47 post).
- **Darling, J., *The Universe is Brighter in the Direction of Our Motion: Galaxy Counts and Fluxes are Consistent with the CMB Dipole*, ApJL 931, L14 (2022), DOI 10.3847/2041-8213/ac6f08**; arXiv:2205.06880. Abstract, verbatim: source counts give "a 331^{+161}_{−107} km s⁻¹ velocity dipole with apex (ℓ, b) = (271^{+55}_{−58}, 56^{+13}_{−35})"; radio fluxes "399^{+264}_{−199} km s⁻¹ toward (ℓ, b) = (301^{+30}_{−30}, 43^{+19}_{−17})" — VLASS epoch 1 combined with RACS; "consistent with the CMB-solar velocity, 370 km s⁻¹ toward (ℓ, b) = (264, 48)." (Secrest 2022 Section 3 contests the method; both stand on the A9 row.)

## 4. Ellis & Baldwin 1984 — by page (OCR of the ADS scan, PDF retained, sha256 7c806e1a…)

**G. F. R. Ellis & J. E. Baldwin, *On the expected anisotropy of radio source counts*, MNRAS 206, 377–381 (1984), DOI 10.1093/mnras/206.2.377** (received 1983 May 31).
- **p. 378** (Section 2): the population has power-law spectra **S ∝ ν^{−α}** and integral counts **(dN/dΩ)(> S) = k S^{−x}** — the definitions of α and x.
- **p. 379** (Section 2, the sentence Part B's estimator rests on): "(dN/dΩ)_obs = (dN/dΩ)_rest δ^{2+x(1+α)} … the observed counts must show a dipole anisotropy over the sky of **amplitude [2 + x(1+α)](v/c)**. … the measurements can be made (and the result must hold) for any source counts, whether in a wide or a narrow solid angle, for flat or steep source spectra, etc, irrespective of selection effects or source evolution, as long as the forward and backward measurements are done in the identical manner." The equation is unnumbered in the original.
- **p. 379** (Section 3): the worked number, α = 0.75, x = 1: amplitude ≈ 4.6 × 10⁻³ for 372 km s⁻¹; n ≳ 2 × 10⁵ sources for 3σ.
- The paper's own caveat that Part B inherits: the amplitude is per **(x, α) of the population as counted**, so the per-bin (x, α) must come from each bin's own counts and spectra — the draft's Section 4 item 3, now with its page.

## 5. What is NOT pinned, and why
- The CatWISE2020 second catalogue: not opened, not pinned this round (Keeper: "Neither is opened this round").
- Quaia's per-bin (x, α): a measurement to be made inside the frozen protocol, not a pin.
- The A9 "PRE-REGISTERED P1 (hash …)" line: waits for `notes/BST_PREREGISTRATION_Part_B_1_FROZEN_v1_Cal_*.md` and its SHA256 on the board.

— Grace. Sources retained in the session scratchpad (`quaia.txt`, `planck2018_I.txt`, `eb.txt`, `secrest2022.txt`); every number above can be grepped there.
