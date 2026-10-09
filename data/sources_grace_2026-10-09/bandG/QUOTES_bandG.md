# Band G primary sources — verbatim quotes

Retrieved 2026-10-09 12:48–12:52 EDT. Directory: `data/sources_grace_2026-10-09/bandG/`.
Rules applied: quotes are verbatim from the `pdftotext` extraction (reading order unless noted `[-layout]`); only whitespace was collapsed; extraction artefacts are kept INSIDE the quote and flagged OUTSIDE it. Page numbers are given as `PDF p.N` (physical page index in the downloaded file, computed from form feeds) and, where visible, the printed page number. Nothing in this directory was executed.

Files (all in this directory):

| file | what |
|---|---|
| `furlanetto_oh_briggs_2006_astro-ph0608032.pdf` (+ `.txt`, `.layout.txt`) | arXiv:astro-ph/0608032, 207 pp. |
| `pritchard_loeb_2012_arXiv1109.6012.pdf` (+ `.txt`, `.layout.txt`) | arXiv:1109.6012, 64 pp. |
| `wild_1952_ApJ115_206_ads.pdf` (+ `.txt`, `.layout.txt`) | ADS full-text scan, 16 pp., OCR text layer (via `https://ui.adsabs.harvard.edu/link_gateway/1952ApJ...115..206W/ADS_PDF`; the `adsabs.harvard.edu/full/` and `articles.adsabs.harvard.edu/pdf/` URLs returned 202 manifest / 504) |
| `verner_etal_1996_astro-ph9601009.pdf` (+ `.txt`, `.layout.txt`) | arXiv:astro-ph/9601009, 24 pp. |
| `nist_asd_HI_lyman_alpha.html` (+ `.txt`, tag-stripped) | NIST ASD lines query exactly as given in the task (A_out=0: A_ki column only) |
| `nist_asd_HI_lyman_alpha_fik.html` (+ `.txt`) | same query with `f_out=on&S_out=on` added, so that f_ik is shown (the task's URL has no f_ik column; ASD exposes it as a checkbox, not via A_out) |

---

## 1. Furlanetto, Oh & Briggs 2006

**File obtained:** `furlanetto_oh_briggs_2006_astro-ph0608032.pdf`
**Bibliographic line:** S. R. Furlanetto, S. P. Oh, F. H. Briggs, "Cosmology at low frequencies: The 21 cm transition and the high-redshift Universe", Physics Reports 433 (2006) 181–301; arXiv:astro-ph/0608032. Page numbers below are the arXiv preprint's.

**Q1.1 — T_* (PDF p.22, printed p.21–22, Section 2.1, around Eq. 11):**
> "where gi is the statistical weight (here g0 = 1 and g1 = 3), E10 = 5.9×10−6 eV is the energy splitting, and T⋆ ≡ E10 /kB = 0.068 K is the equivalent temperature. Because all astrophysical applications have TS ≫ T∗ , approximately three of four atoms find themselves in the excited state."

Artefacts flagged: the star subscript is extracted as `T⋆` and `T∗` for the same symbol; superscripts are flattened (`10−6`).

**Q1.2 — A₁₀ (PDF p.22, printed p.22, Section 2.1, Eq. 14 and following sentence):**
> "σ01 ≡ 3c2 A10 , 8πν 2 (14) A10 = 2.85 × 10−15 s−1 is the spontaneous emission coefficient of the 21 cm transition, NHI is the column density of HI (here the factor 1/4 accounts for the fraction of HI atoms in the hyperfine singlet state), and φ(ν) is the line profile"

Artefacts flagged: fraction in Eq. (14) flattened to "3c2 A10 , 8πν 2" (i.e. 3c²A₁₀/8πν²); subscripts flattened.

**Q1.3 — spin-temperature equation with coupling coefficients (PDF p.24, printed p.23–24, Section 2.2, Eqs. 19–22):**
> "Three competing processes determine TS : (1) absorption of CMB photons (as well as stimulated emission); (2) collisions with other hydrogen atoms, free electrons, and protons; and (3) scattering of UV photons. We let C10 and P10 be the de-excitation rates (per atom) from collisions and UV scattering, respectively; they will be examined in detail in the following sections. We also let C01 and P01 be the corresponding excitation rates. The spin temperature is then determined in equilibrium by 8 n1 (C10 + P10 + A10 + B10 ICMB ) = n0 (C01 + P01 + B01 ICMB ) , (19) where B01 and B10 are the appropriate Einstein coefficients and ICMB is the energy flux of CMB photons. With the Rayleigh-Jeans approximation, equation (19) can be rewritten as [67] TS−1 = Tγ−1 + xc TK−1 + xα Tc−1 , 1 + xc + xα (20) where xc and xα are coupling coefficients for collisions and UV scattering, respectively, and TK is the gas kinetic temperature."

Same equation in `-layout` extraction (`furlanetto_oh_briggs_2006_astro-ph0608032.layout.txt` l.1100–1102), whitespace collapsed:
> "TS−1 = Tγ−1 + xc TK−1 + xα Tc−1 , (20) 1 + xc + xα"

Artefacts flagged: "8" after "in equilibrium by" is a footnote marker; the fraction bar of Eq. (20) is lost (numerator "Tγ−1 + xc TK−1 + xα Tc−1", denominator "1 + xc + xα"); "−1" are superscripts.

**Q1.4 — when the signal is in absorption, dark ages (PDF p.81, printed p.81, Section 5 "The Dark Ages"):**
> "As discussed in §3, the IGM thermally decouples from the CMB at z ∼ 200, cooling adiabatically so that TK < Tγ . However, until z ∼ 30 it remains sufficiently dense that collisions drive TS → TK . Since TS < Tγ , the IGM can be seen in 21 cm absorption against the CMB, with a peak signal at z ∼ 80."

Supporting (PDF p.47, printed p.47, Section 3.1, after Eq. 67):
> "Thus for redshifts z . 70, TS → Tγ ; by z ∼ 30 the IGM essentially becomes invisible. [...] The signal peaks (in absorption) at z ∼ 80, where TK is small but collisional coupling still efficient."

Artefact flagged: "z . 70" is the extraction of z ≲ 70; "[...]" marks my elision of three sentences (not part of the quote).

**Q1.5 — cosmic-dawn absorption trough (PDF p.66, printed p.66, Section 3.5.2, discussion of Fig. 7c, Pop II fiducial model):**
> "Figure 7c contains an even more striking feature at higher redshifts. At z ∼ 30, the IGM is nearly invisible even though TK ≪ Tγ (see Fig. 6). However, as the first galaxies form, the Wouthuysen-Field effect drives TS → TK . Because zc > zh , this produces a relatively strong absorption signal (δTb ≈ −80 mK) over the range z ∼ 21–14 (or ν ∼ 70–95 MHz). However, the IGM still heats up well before reionization begins in earnest, making δT ¯ b nearly independent of TS throughout reionization."

Artefact flagged: "δT ¯ b" is the extraction of \bar{δT_b}. Note: the z ∼ 21–14 range is model-dependent (their fiducial Pop II parameters), as the text's "Because zc > zh" indicates.

---

## 2. Pritchard & Loeb 2012

**File obtained:** `pritchard_loeb_2012_arXiv1109.6012.pdf`
**Bibliographic line:** J. R. Pritchard, A. Loeb, "21 cm cosmology in the 21st century", Reports on Progress in Physics 75 (2012) 086901; arXiv:1109.6012. Page numbers below are the arXiv preprint's (header "CONTENTS n").

**Q2.1 — δT_b equation (PDF p.7, printed p.7, Section 2.1, Eqs. 5–7), `-layout` extraction, whitespace collapsed; the reading-order extraction scrambles the fraction stacks:**
> "TS − TR δTb = (1 − e−τν ) (5) 1+z TS − TR ≈ τ (6) 1+z 1/2 Ωb h2 0.15 1 + z ≈ 27xHI (1 + δb ) 0.023 Ωm h2 10 TS − TR ∂r vr × mK, (7) TS (1 + z)H(z) Here xHI is the neutral fraction of hydrogen, δb is the fractional overdensity in baryons, and the final term arises from the velocity gradient along the line of sight ∂r vr ."

Artefacts flagged: all fraction bars and bracket groupings are lost; the printed Eq. (7) reads δT_b ≈ 27 x_HI (1+δ_b) (Ω_b h²/0.023) [(0.15/Ω_m h²)(1+z)/10]^{1/2} [(T_S − T_R)/T_S] [∂_r v_r/((1+z)H(z))] mK. Note the authors write T_R (background radiation temperature), not T_γ, in this equation; the preceding sentence (reading-order extraction, same page) is:
> "The optical depth of this transition is small at all relevant redshifts, yielding a differential brightness temperature"

**Q2.2 — global-signal history, bullet list (PDF p.12–13, printed p.12–13, Section 2.4 / Fig. 3 discussion):**
> "• 200 . z . 1100: The residual free electron fraction left after recombination allows Compton scattering to maintain thermal coupling of the gas to the CMB, setting TK = Tγ . The high gas density leads to effective collisional coupling so that TS = Tγ and we expect T̄b = 0 and no detectable 21 cm signal. • 40 . z . 200: In this regime, the gas cools adiabatically so that TK ∝ (1 + z)2 leading to TK < Tγ and collisional coupling sets TS < Tγ , leading to T̄b < 0 and an early absorption signal. At this time, Tb fluctuations are sourced by density fluctuations, potentially allowing the initial conditions to be probed [32, 22]. • z? . z . 40: As the expansion continues, decreasing the gas density, collisional coupling becomes ineffective and radiative coupling to the CMB sets TS = Tγ , and there is no detectable 21 cm signal. • zα . z . z? : Once the first sources switch on at z? , they emit both Lyα photons and X-rays. In general, the emissivity required for Lyα coupling is significantly less than that for heating TK above Tγ . We therefore expect a regime where the spin temperature is coupled to cold gas so that TS ∼ TK < Tγ and there is an absorption signal."

Artefacts flagged: " . " renders ≲; "z?" renders z_⋆ (the first-source redshift); "(1 + z)2" is a square; page break between "significantly" and "less" ("CONTENTS 13" header removed as whitespace).

**Q2.3 — continuation, heating/emission phase (PDF p.13, printed p.13):**
> "• zh . z . zα : After Lyα coupling saturates, fluctuations in the Lyα flux no longer affect the 21 cm signal. By this point, heating becomes significant and gas temperature fluctuations source Tb fluctuations. While TK remains below Tγ we see a 21 cm signal in absorption, but as TK approaches Tγ hotter regions may begin to be seen in emission. Eventually by a redshift zh the gas will be heated everywhere so that T̄K = Tγ . • zT . z . zh : After the heating transition, TK > Tγ and we expect to see a 21 cm signal in emission."

**Q2.4 — global-signal summary, Fig. 4 discussion (PDF p.22–23, printed p.22–23, Section 3.6):**
> "At high redshift, 10 z . 200, the gas temperature cools adiabatically faster than the CMB (since the residual fraction of free electrons is insufficient to couple the two temperatures). At the same time, collisional coupling is effective at coupling spin and gas temperatures leading to the absorption trough seen at the right of the lower panel. The details of this trough are fixed by cosmology and therefore may be predicted relatively robustly. The minima of this trough corresponds to the point at which collisional coupling starts to become relatively ineffective. Once star formation begins, the spin and gas temperatures again become tightly coupled leading to a second, potentially deeper, absorption trough. The minimum of this trough corresponds to the point when X-ray heating switches on heating the gas above the CMB temperature leading to an emission signal. The signal then reaches the curve for a saturated signal (TS TCMB ) briefly before the ionization of neutral hydrogen diminishes it."

Artefacts flagged: "10 z . 200" lost the ≲ glyphs (printed 10 ≲ z ≲ 200); "(TS TCMB )" lost ≫.

Also (Section 2.1, PDF p.7): A₁₀ in this paper, for cross-check with item 1 and 3:
> "where A10 = 2.85 × 10−15 s−1 is the spontaneous Rdecay rate of the spin-flip transition"

Artefact flagged: "Rdecay" is a stray integral sign from the next line merged into the word "decay".

---

## 3. Wild 1952

**File obtained:** `wild_1952_ApJ115_206_ads.pdf` — ADS full-text scan with OCR text layer (16 pages, pp. 206–221). OBTAINED; Gould 1994 fallback not needed.
**Bibliographic line:** J. P. Wild, "The Radio-Frequency Line Spectrum of Atomic Hydrogen and Its Applications in Astronomy", Astrophysical Journal 115 (1952) 206–221. Received September 8, 1951.

**Q3.1 — transition probability of the 1420 Mc/sec line (PDF p.5, printed p.210, Section II b, text following Eq. 12):**
> "We therefore adopt result (12) and, in conjunction with equations (3) and (11), obtain for the transition probability of the 1420 Mc/sec line, A2\ = 2.85 X 10“15 sec-1 . The natural half-width of this line has the minute value of 5 X 10-16 c/sec ( = ^42i/ 27r) and would be quite insignificant in comparison with extraneous causes of line broadening under all conditions encountered in practice."

Artefacts flagged (OCR of a 1952 scan): "A2\" = A₂₁; "10“15" = 10⁻¹⁵; "^42i/ 27r" = A₂₁/2π; "10-16" = 10⁻¹⁶.

**Q3.2 — Table 2 (PDF p.5, printed p.210):**
> "TABLE 2 Hyperfine-Structure Lines FOR W = 1 AND 2 Level l2Sl/2. 22Si/2 • 222Pi/2. 2 P3/2. Frequency (Mc/Sec) Transition Probability (Sec-1) 1420.4 177.5 59.2 23.7 2.85X10"15"

Artefacts flagged: "W" = n; the level labels are OCR of 1²S₁/₂, 2²S₁/₂, 2²P₁/₂, 2²P₃/₂; the single transition-probability entry 2.85×10⁻¹⁵ sec⁻¹ belongs to the 1420.4 Mc/sec row (the other three rows have no entry in the OCR; in the layout extraction they are likewise blank).

**Q3.3 — the line-strength input (PDF p.4–5, printed p.209–210, Eq. 12):**
> "Recently, however, Ewen13 and Purcell (personal communication)14 have found the strength of this line to be S2i=Sß2. (12)"

Artefact flagged: OCR; printed S₂₁ = 3β² (the "S" before "ß2" is a misread "3"; cf. Shklovsky's "£21 = f ß2" just above, which is S₂₁ = (something)β², the fraction unreadable in OCR). Treat the numeric line strength as pin-owed to the scan image if needed; the A₂₁ value itself (Q3.1) is cleanly OCR'd.

---

## 4. Verner, Ferland, Korista & Yakovlev 1996

**File obtained:** `verner_etal_1996_astro-ph9601009.pdf`
**Bibliographic line:** D. A. Verner, G. J. Ferland, K. T. Korista, D. G. Yakovlev, "Atomic Data for Astrophysics. II. New Analytic Fits for Photoionization Cross Sections of Atoms and Ions", Astrophysical Journal 465 (1996) 487–498; arXiv:astro-ph/9601009. Page numbers below are the preprint's ("– n –").

**Q4.1 — fit formula, Eq. (1) (PDF p.4, printed "– 4 –", Section 3):**
> "We propose to describe the photoionization cross sections σ(E) from the outer shells of atoms and ions in question (Sect. 2) by the fitting formula: σ(E) = σ0 F (y) Mb, h 2 F (y) = (x − 1) x= E − y0 , E0 2 + yw i y 0.5P −5.5 y= 1+ q x2 + y12 , q y/ya −P , (1) where E is photon energy in eV, and σ0 , E0 , yw , ya , P , y0 and y1 are the fit parameters (1 Mb = 10−18 cm2 )."

Artefacts flagged: the display equation is scrambled by reading order; "h ... i" are the extracted square brackets; "q" is the extracted √. The printed form is F(y) = [(x−1)² + y_w²] y^{0.5P−5.5} (1 + √(y/y_a))^{−P}, x = E/E₀ − y₀, y = √(x² + y₁²).

**Q4.2 — meaning of the parameters (PDF p.4, same section):**
> "The fit parameter P determines the power-law cross section behavior σ(E) ∝ E 0.5P −3.5 in the energy interval E2 ≪ E ≪ Ea behind the dip (provided Ea ≫ E2 ), where Ea = ya E0 is the upper boundary of this interval. Finally Eq. (1) reproduces the correct non-relativistic high-energy asymptote, σ(E) ∝ E −3.5 , for E ≫ Ea ."

**Q4.3 — Table 1 header and hydrogen row (PDF p.21, printed "– 21 –"), `-layout` extraction l.399–402, whitespace collapsed:**
> "TABLE 1 Fit parameters for photoionization cross sections a Ion Z N Eth , eV Emax , eV E0 , eV 0 , Mb ya P yw y0 y1 Notes H I 1 1 1.360+1 5.000+4 4.298 1 5.475+4 3.288+1 2.963+0 0.000+0 0.000+0 0.000+0 A"

Table notes (PDF p.24, printed "– 24 –"):
> "Notes to Table 1 A, B, C, D, E, F { classes of accuracy (see text). a 1.360+1 denotes 1 360 101 ."

Class A defined in text (PDF p.5, Section 3):
> "A. Hydrogenic cross sections. They are known exactly, and rms accuracy of the fits is better than 0.2%."

Artefacts flagged: the column header "0 , Mb" has lost the σ glyph (printed σ₀, Mb); in the H I row the E₀ entry "4.298 1" has lost its minus sign — the printed value is 4.298−1, i.e. E₀ = 0.4298 eV (the same sign-drop occurs for every negative exponent in the table, e.g. He I y₀ "4.434 1"); footnote "a" printed as 1.360+1 denotes 1.360×10¹; "{" is the extracted em-dash. So, as printed: Z=1, N=1, E_th = 1.360×10¹ eV, E_max = 5.000×10⁴ eV, E₀ = 4.298×10⁻¹ eV, σ₀ = 5.475×10⁴ Mb, y_a = 3.288×10¹, P = 2.963, y_w = y₀ = y₁ = 0, accuracy class A.

**Threshold cross section ≈ 6.3×10⁻¹⁸ cm²:** NOT STATED in this paper. Grep of the full text for "6.3", "threshold cross section", "ground state" finds no such sentence; the only "6.3xx" strings are table entries for other ions. (Evaluating their Eq. 1 with the H I row at E = E_th = 13.6 eV gives x = 31.64, y = x, F = 30.64² × 31.64^{−4.0185} × (1 + 0.981)^{−2.963} = 1.159×10⁻⁴, σ = 5.475×10⁴ × 1.159×10⁻⁴ Mb = 6.35 Mb = 6.3×10⁻¹⁸ cm² — this is my arithmetic (python, 2026-10-09), not a quote.)

---

## 5. NIST Atomic Spectra Database, H I lines 1215–1216 Å

**Files obtained:** `nist_asd_HI_lyman_alpha.html` (the task's URL verbatim; A_ki column) and `nist_asd_HI_lyman_alpha_fik.html` (same query plus `f_out=on&S_out=on`, which adds the f_ik and S_ik columns). Tag-stripped text in the sibling `.txt` files.
**Bibliographic line (as the page prints it):** Kramida, A., Ralchenko, Yu., Reader, J., and NIST ASD Team (2024). NIST Atomic Spectra Database (ver. 5.12), [Online]. Available: https://physics.nist.gov/asd [2026, October 9]. National Institute of Standards and Technology, Gaithersburg, MD. DOI: https://doi.org/10.18434/T4W30F. Transition probabilities: "Wiese & Fuhr 2009, Jitrik & Bunge 2004. The data of Jitrik & Bunge 2004 have been scaled to the CODATA-2018 values of the fundamental constants by A. Kramida for the release of ASD v. 5.10 in October 2022."

**Q5.1 — column header and rows (from `nist_asd_HI_lyman_alpha_fik.txt`, whitespace collapsed; "H I : 4 Lines of Data Found"; λ "in : vacuum below 2000 Å"):**
> "Observed Wavelength Vac (Å) Unc. (Å) Ritz Wavelength Vac (Å) Unc. (Å) Rel. Int. (?) A ki (s −1 ) f ik S ik (a.u.) Acc. E i (cm −1 ) E k (cm −1 ) Lower Level Conf., Term, J Upper Level Conf., Term, J Type TP Ref. Line Ref."

Row 1 (1s ²S₁/₂ – 2p ²P°₃/₂):
> "1 215.6699 0.0020 1 215.668237310 0.000000006 6.2647e+08 2.7760e-01 2.2220e+00 AAA 0.0000000000 - 82 259.2850014 1 s 2 S 1 / 2 2 p 2 P° 3 / 2 T7771 L12020"

Row 2 (1s ²S₁/₂ – 2p ²P°₁/₂):
> "1 215.6699 0.0020 1 215.673644608 0.000000004 6.2648e+08 1.3880e-01 1.1110e+00 AAA 0.0000000000 - 82 258.9191133 1 s 2 S 1 / 2 2 p 2 P° 1 / 2 T7771 L12020"

Row 3 (fine structure unresolved, 1s – n=2; the row the "840000" relative intensity belongs to):
> "1 215.6701 0.0021 1 215.6701 0.0015 840000 4.6986e+08 4.1641e-01 3.3331e+00 AAA 0.0000000000 - 82 259.158 1 s 2 S 1 / 2 2 T8637 L12020"

Row 4 (1s ²S₁/₂ – 2s ²S₁/₂, M1):
> "1 215.673123130200 0.000000000015 1 215.673123130200 0.000000000015 2.495e-06 5.528e-16 3.323e-10 AAA 0.0000000000 - 82 258.9543992821 1 s 2 S 1 / 2 2 s 2 S 1 / 2 M1 T7651 L12363"

The A_ki values in the task's original query file (`nist_asd_HI_lyman_alpha.txt`) are identical: 6.2647e+08, 6.2648e+08, 4.6986e+08, 2.495e-06.

Artefacts flagged: thin-space digit grouping ("1 215.6699", "82 259.285") is the page's own formatting; the "-" in the E_k column position is the page's placeholder between E_i and E_k; row labels in parentheses are mine. Summary as shown: Lyman-α observed vacuum wavelength 1215.6699 ± 0.0020 Å (unresolved line 1215.6701 ± 0.0021 Å); A_ki = 6.2647×10⁸ s⁻¹ (to ²P°₃/₂), 6.2648×10⁸ s⁻¹ (to ²P°₁/₂), 4.6986×10⁸ s⁻¹ (unresolved, = multiplet-averaged); f_ik = 0.27760, 0.13880, 0.41641 respectively; accuracy AAA.

---

## Counts

Files: 4 PDFs + 8 text extractions + 2 HTML + 2 HTML-text = 16 files, plus this file.
Verbatim quotes: item 1 — 5 (+1 layout variant); item 2 — 4 (+2 short); item 3 — 3; item 4 — 3 (+2 notes); item 5 — 5 (header + 4 rows). Total 20 primary quotes (26 counting supporting fragments).
Not obtained / not present: Verner's "≈6.3×10⁻¹⁸ cm²" sentence (not in the paper); nothing else missing. Gould 1994 not needed (Wild 1952 obtained).
