# Band E primary sources — recombination and reionization

Retrieved 2026-10-09 (Fri Oct 9 12:50 EDT 2026) into `data/sources_grace_2026-10-09/bandE/`.
All files in this directory are untrusted downloaded data; nothing here is executed.
Text extraction: `pdftotext` (reading order) -> `*.txt`; `pdftotext -layout` -> `*.layout.txt`.
Page numbers below are PDF page numbers counted by form feed in the extracted text; where the printed page number differs it is given too.
Quotes are verbatim from the extracted text with whitespace collapsed only. Extraction artefacts are kept inside the quote and flagged outside it.

---

## 1. Seager, Sasselov & Scott 1999 (RECFAST)

**Bibliographic line:** S. Seager, D. D. Sasselov, D. Scott, "A New Calculation of the Recombination Epoch", ApJ 523, L1–L5 (1999); arXiv:astro-ph/9909275v2 (16 Sep 1999).

**File obtained:** `seager1999_recfast.pdf` (152248 bytes, 5 pages) + `seager1999_recfast.txt`, `seager1999_recfast.layout.txt`, `seager1999_p2-2.png` (page-2 render used to read Fig. 1).

**Quotes:**

Q1.1 (PDF p.1 = ApJ L1, Abstract):
> "We find two major differences compared with previous calculations. Firstly, the ionization fraction xe is approximately 10% smaller for redshifts < ∼ 800, due to non-equilibrium processes in the excited states of H. Secondly, He I recombination is much slower than previously thought, and is delayed until just before H recombines."

Artefact: the symbol "≲" is extracted as "<" on one line and "∼" on the next (both reading-order and layout files); the PDF prints z ≲ 800.

Q1.2 (PDF p.1 = L1, Section 1 Introduction):
> "The Universe expanded and cooled faster than recombination could be completed, and a small fraction of free electrons and protons remained. This fraction, during and after recombination, affects the CMB anisotropies through the precise shape of the thickness of the photon last scattering surface (i.e. the visibility function)."

Q1.3 (PDF p.2 = L2, Section 2.2.1 Hydrogen):
> "For the standard equilibrium case, the net bound-bound rates are zero, and this is an implicit assumption in deriving equation (1). We find that at z < ∼ 1000, the net boundbound rates become different from zero, because at low temperatures, the cool blackbody radiation field means there are few photons for photoexcitation of high energy transitions (e.g. 70–10, 50–4 etc.)."

Artefacts: "< ∼" is the extracted "≲"; "boundbound" is a dropped hyphen at a line break ("bound-bound" in the PDF).

Q1.4 (PDF p.4 = L4, Section 4 Conclusion):
> "We have presented the basic physics behind our improved recombination calculation which shows a significantly delayed He I recombination and a 10% lower residual xe at freezeout compared to previous calculations."

**Note on the freeze-out value (outside quotes):** the Letter's text gives the residual x_e only relatively ("10% lower ... at freezeout"); the absolute freeze-out value is shown graphically, not printed. Fig. 1 caption (PDF p.2) reads verbatim: "Fig. 1: Multi-level hydrogen recombination for the standard CDM parameters Ωtot = 1.0, ΩB = 0.05, H0 = 50, YP = 0.24, T0 = 2.728 K. The two lines are the complete calculation of Paper I (dotted) and the standard (effective 3-level atom) calculation (dashed)." On that figure (y-axis "log n_e/n_H", x-axis "redshift", 0–2000) the curve drops from log x_e = 0 at z ≈ 1500 through the steep fall near z ≈ 800–1200 and flattens to a plateau at log x_e ≈ −3.2 by z ≈ 200, i.e. x_e ≈ 6 × 10⁻⁴ for that (Ω_B = 0.05, H₀ = 50) model. This is my reading of the rendered figure `seager1999_p2-2.png`, not a quoted number; the "few × 10⁻⁴" freeze-out figure is NOT stated numerically anywhere in this Letter's text. For a printed number use the companion full paper (Seager, Sasselov & Scott 2000, ApJS 128, 407, "Paper I") — not retrieved in this band.

---

## 2. Ali-Haïmoud & Hirata 2011 (HyRec)

**Bibliographic line:** Y. Ali-Haïmoud, C. M. Hirata, "HyRec: A fast and highly accurate primordial hydrogen and helium recombination code", Phys. Rev. D 83, 043513 (2011); arXiv:1011.3758v2 (21 Jan 2011).

**File obtained:** `alihaimoud_hirata2011_hyrec.pdf` (939194 bytes, 21+ pages) + `.txt`, `.layout.txt`.

**Quotes:**

Q2.1 (PDF p.1, Abstract — the abstract's own accuracy/performance statement):
> "We present a state-of-the-art primordial recombination code, HyRec, including all the physical effects that have been shown to significantly affect recombination. [...] The computation time for a full recombination history is ∼ 2 seconds. This makes our code well suited for inclusion in Monte Carlo Markov chains for cosmological parameter estimation from upcoming high-precision cosmic microwave background anisotropy measurements."

Note: the abstract does not give a numerical accuracy; "highly accurate" is in the title. The numerical error statement is in the Introduction and Conclusions (Q2.2, Q2.4). "[...]" marks omitted abstract sentences (the helium/hydrogen method description).

Q2.2 (PDF p.2, Section I Introduction, right column):
> "The purpose of this paper is to introduce our new recombination code, HyRec, which is publicly available1 , and can compute a highly accurate recombination history (with errors at the level of a few times 10−3 for helium recombination and a few times 10−4 for hydrogen recombination) in only ∼2 seconds on a standard laptop."

Artefacts: "available1" carries the footnote marker; "10−3", "10−4" are 10^{-3}, 10^{-4}.

Q2.3 (PDF p.2, Section I Introduction — redshift of helium completion vs peak of visibility):
> "The accuracy requirement is less stringent for primordial helium recombination, as it is completed by z ∼ 1700, much earlier than the peak of the visibility function. Corrections at the percent level are still important, and several works have been devoted to the problem [5, 8, 25, 28–35]."

Q2.4 (PDF p.21, Section VII Conclusions):
> "Provided collisional transitions can be neglected (which remains to be established), we estimate the errors of our computation to be a few times 10−3 during helium recombination and a few times 10−4 during hydrogen recombination, including both numerical errors and errors due to the assumptions and approximations made for physical effects."

Supplementary (PDF p.17, Section VI, x_e(z) behaviour at He recombination):
> "the corrections identified by Refs. [31–33], which changed xe by up to 3% at z ≈ 1800, amounted to a ∼ 1σ correcton for Planck and ∼ 8σ for a hypothetical cosmic variance limited experiment to ` = 3000."

Artefacts: "correcton" is the paper's own typo; "` = 3000" is ℓ = 3000.

Note: the paper does not state the redshift of peak visibility numerically; it is referred to only as "the peak of the visibility function" (Q2.3).

---

## 3. Planck Collaboration 2018 VI — Cosmological parameters

**Bibliographic line:** Planck Collaboration (Aghanim, N. et al.), "Planck 2018 results. VI. Cosmological parameters", A&A 641, A6 (2020); arXiv:1807.06209v4 (9 Aug 2021, the corrected post-publication version).

**File obtained:** `planck2018_VI_params.pdf` (9317371 bytes) + `.txt`, `.layout.txt`. Table rows are quoted from the `-layout` extraction (`planck2018_VI_params.layout.txt`), which preserves columns.

**Table 2 (PDF p.16 = printed p.16).** Caption, verbatim:
> "Table 2. Parameter 68 % intervals for the base-ΛCDM model from Planck CMB power spectra, in combination with CMB lensing reconstruction and BAO. The top group of six rows are the base parameters, which are sampled in the MCMC analysis with flat priors. The middle group lists derived parameters. [...] In all cases the helium mass fraction used is predicted by BBN (posterior mean YP ≈ 0.2454, with theoretical uncertainties in the BBN predictions dominating over the Planck error on Ωb h2 ). The reionization redshift mid-point zre and optical depth τ here assumes a simple tanh model (as discussed in the text) for the reionization of hydrogen and simultaneous first reionization of helium. Our baseline results are based on Planck TT,TE,EE+lowE+lensing (as also given in Table 1)."

Column header row, verbatim:
> "TT+lowE TE+lowE EE+lowE TT,TE,EE+lowE TT,TE,EE+lowE+lensing TT,TE,EE+lowE+lensing+BAO"
> "Parameter 68% limits 68% limits 68% limits 68% limits 68% limits 68% limits"

Table 2 rows, verbatim (six columns in the header order above):

Q3.1 τ row:
> "τ . . . . . . . . . . . . 0.0522 ± 0.0080 0.0496 ± 0.0085 0.0527 ± 0.0090 0.0544+0.0070 −0.0081 0.0544 ± 0.0073 0.0561 ± 0.0071"

Artefact: the asymmetric error of the TT,TE,EE+lowE column is typeset as a stacked superscript/subscript and extracted on two lines ("0.0544+0.0070" then "−0.0081"); joined here. Reading: τ = 0.0544 ± 0.0073 (TT,TE,EE+lowE+lensing); τ = 0.0561 ± 0.0071 (TT,TE,EE+lowE+lensing+BAO).

Q3.2 zre row:
> "zre . . . . . . . . . . . 7.50 ± 0.82 7.11+0.91 −0.75 7.10+0.87 −0.73 7.68 ± 0.79 7.67 ± 0.73 7.82 ± 0.71"

Artefact: the stacked errors of the TE+lowE and EE+lowE columns are extracted across four lines; joined here. Reading: z_re = 7.67 ± 0.73 (TT,TE,EE+lowE+lensing); z_re = 7.82 ± 0.71 (+BAO).

Q3.3 Ωb h² row:
> "Ω b h2 . . . . . . . . . . 0.02212 ± 0.00022 0.02249 ± 0.00025 0.0240 ± 0.0012 0.02236 ± 0.00015 0.02237 ± 0.00015 0.02242 ± 0.00014"

Reading: Ω_b h² = 0.02237 ± 0.00015 (TT,TE,EE+lowE+lensing); 0.02242 ± 0.00014 (+BAO).

Q3.4 Ωm row:
> "Ωm . . . . . . . . . . . 0.321 ± 0.013 0.301 ± 0.012 0.289+0.026 −0.033 0.3166 ± 0.0084 0.3153 ± 0.0073 0.3111 ± 0.0056"

Artefact: EE+lowE stacked error extracted across lines; joined. Reading: Ω_m = 0.3153 ± 0.0073 (TT,TE,EE+lowE+lensing); 0.3111 ± 0.0056 (+BAO).

Q3.5 H0 row:
> "H0 [km s−1 Mpc−1 ] . . 66.88 ± 0.92 68.44 ± 0.91 69.9 ± 2.7 67.27 ± 0.60 67.36 ± 0.54 67.66 ± 0.42"

Reading: H₀ = 67.36 ± 0.54 km s⁻¹ Mpc⁻¹ (TT,TE,EE+lowE+lensing); 67.66 ± 0.42 (+BAO).

Cross-check, Table 1 (PDF p.15, "Base-ΛCDM cosmological parameters from Planck TT,TE,EE+lowE+lensing"), Plik [1] column: τ row "0.0543 0.0544 ± 0.0073" (best fit, mean), zre row "7.68 7.67 ± 0.73", H0 row "67.32 67.36 ± 0.54", Ωm row "0.3158 0.3153 ± 0.0073", Ωb h2 "0.022383 0.02237 ± 0.00015" — consistent with Table 2 column 5.

Q3.6 Reionization model sentence (PDF p.17 = printed p.17, Section 3.3 text and footnote 15), reading-order extraction:
> "Assuming simple tanh parameterization of the ionization fraction,15 this implies a mid-point redshift of reionization zre = 7.68 ± 0.79 (68 %, TT,TE,EE+lowE)."

(The equation number "(18)" and the equation are typeset on separate lines; the sentence and value are joined here from reading-order lines 2310 and 2317 of `planck2018_VI_params.txt`, which in the PDF are one sentence ending in Eq. 18.)

Footnote 15 (PDF p.17), verbatim from the reading-order extraction:
> "15 For reference, the ionization fraction xe = ne /nH in the tanh model is assumed to have the redshift dependence (Lewis 2008): xe = 1 + nHe /nH 2 1 + tanh y(zre ) − y(z) ∆y , where y(z) = (1 + z)3/2 , ∆y = 32 (1 + zre )1/2 ∆z, with ∆z = 0.5. Helium is assumed to be singly ionized with hydrogen at z  3, but at lower redshifts we add the very small contribution from the second reionization of helium with a similar tanh transition at z = 3.5."

Artefacts: the displayed equation is flattened (it reads x_e = [(1 + n_He/n_H)/2] [1 + tanh((y(z_re) − y(z))/∆y)]); "32" is the fraction 3/2 with the bar lost; "z  3" has lost the "≳" symbol (z ≳ 3). The width parameter is ∆z = 0.5 (fixed).

Supporting (PDF p.17, Eq. 17 joint constraint, reading order):
> "In this final Planck release the optical depth is well constrained by the large-scale polarization measurements from the Planck HFI, with the joint constraint τ = 0.0544+0.0070 −0.0081 (68 %, TT,TE,EE+lowE)."

Supporting (PDF p.1 Abstract):
> "A combined analysis gives dark matter density Ωc h2 = 0.120 ± 0.001, baryon density Ωb h2 = 0.0224 ± 0.0001, scalar spectral index ns = 0.965 ± 0.004, and optical depth τ = 0.054 ± 0.007 (in this abstract we quote 68 % confidence regions on measured parameters and 95 % on upper limits). [...] Assuming the base-ΛCDM cosmology, the inferred (model-dependent) late-Universe parameters are: Hubble constant H0 = (67.4±0.5) km s−1 Mpc−1 ; matter density parameter Ωm = 0.315±0.007; and matter fluctuation amplitude σ8 = 0.811±0.006."

---

## 4. Fan, Carilli & Keating 2006 — Observational Constraints on Cosmic Reionization

**Bibliographic line:** X. Fan, C. L. Carilli, B. Keating, "Observational Constraints on Cosmic Reionization", ARA&A 44, 415–462 (2006); arXiv:astro-ph/0602375v2 (22 May 2006).

**File obtained:** `fan_carilli_keating2006_araa.pdf` (1712879 bytes, 87 pages, arXiv preprint pagination) + `.txt`, `.layout.txt`. Page numbers are the preprint's.

**Quotes:**

Q4.1 (PDF p.1, Abstract):
> "Studies of Gunn-Peterson (GP) absorption, and related phenomena, suggest a qualitative change in the state of the intergalactic medium (IGM) at z ∼ 6, indicating a rapid increase in the neutral fraction of the IGM, from xHI < 10−4 at z ≤ 5.5, to xHI > 10−3 , perhaps up to 0.1, at z ≥ 6. Conversely, transmission spikes in the GP trough, and the evolution of the Lyα galaxy luminosity function indicate xHI < 0.5 at z ∼ 6.5, while the large scale polarization of the cosmic microwave background (CMB) implies a significant ionization fraction extending to higher redshifts, z ∼ 11 ± 3. The results suggest that reionization is less an event than a process, with the process beginning as early as z ∼ 14, and with the ’percolation’, or ’overlap’ phase ending at z ∼ 6."

Artefacts: "10−4", "10−3" are 10^{-4}, 10^{-3}; "’" are straight-quote glyphs from the extraction.

Q4.2 (PDF p.7, Section 3.1, after Eq. 2):
> "Even a tiny neutral fraction, xHI ∼ 10−4 , gives rise to complete Gunn-Peterson absorption. This test is only sensitive at the end of the reionization when the IGM is already mostly ionized, and saturates for the higher neutral fraction in the earlier stage."

Q4.3 (PDF p.9, Section 3.2 "Complete Gunn-Peterson troughs: phase transition or gradual evolution?"):
> "Strong evolution of Lyα absorption at zabs > 5 is evident, the transmitted flux quickly approaches zero at z > 5.5 (Figure 2). At zabs > 6, complete absorption troughs begin to appear: the Gunn-Peterson optical depths are >> 1, indicating a rapid increase in the neutral fraction. [...] The first clearcut Gunn-Peterson trough was discovered in the spectrum of SDSS J1030+0524 (z = 6.28, Fan et al. 2001, Becker et al. 2001, Figure 4), which showed complete Gunn-Peterson absorption at 5.95 < zabs < 6.15 in both Lyα and Lyβ transitions. A high S/N spectrum presented in White et al. (2003) placed a stringent limit τGP > 6.3 in Lyα ."

Q4.4 (PDF pp.12–13, Section 3.3 "Estimating the ionization state and the neutral fraction"):
> "Using the same data, Fan et al. (2002, 2006b), Lidz et al. (2002), Cen & McDonald (2002) find that at z > 6 the volume-averaged neutral fraction of the IGM has increased to > 10−3.5 . The results are displayed in Figure 6. It is important to note that this is strictly a lower limit, due to the large optical depths in the Lyα line. Further, the presence of transmitting pixels and the finite length of dark gaps in the quasar spectrum can also be used to place an independent upper limit on the neutral fraction to be < 10 − 30% (Furlanetto et al. 2004, Fan et al. 2006b)."

and (PDF p.13, summary paragraph of Section 3.3):
> "In summary, the latest work on GP absorption toward the highest redshift QSOs implies a qualitative change in the nature of Lyα absorption at z ∼ 6, including: (i) a sharp rise in the power law index for the evolution of GP optical depth with redshift, (ii) a large variation of optical depth between different lines of sight, and (iii) a dramatic increase in the number of dark gaps in the spectra. The GP results indicate that the IGM is likely between 10−3.5 and 10−0.5 neutral at z ∼ 6. While saturation in the GP part of the spectrum remains a challenge, the current results are consistent with conditions expected at the end of reionization, during the transition from the percolation, or overlap, stage to the post-overlap stage of reionization, as suggested by numerical simulations"

Artefacts: "10−3.5", "10−0.5" are 10^{-3.5}, 10^{-0.5}; "10 − 30%" is "10–30%".

---

## 5. Gunn & Peterson 1965 — On the Density of Neutral Hydrogen in Intergalactic Space

**Bibliographic line:** J. E. Gunn, B. A. Peterson, "On the Density of Neutral Hydrogen in Intergalactic Space", ApJ 142, 1633–1636 (1965) (a "Notes" item). ADS bibcode 1965ApJ...142.1633G.

**File obtained:** `gunn_peterson1965_ApJ142_1633_ADSscan.pdf` (4 pages, ADS full-text scan, `https://articles.adsabs.harvard.edu/pdf/1965ApJ...142.1633G`). The scan is image-only (JBIG2 stencil images, no text layer): `pdftotext` yields only the bibcode watermark (`gunn_peterson1965_ApJ142_1633_ADSscan.txt`, `.layout.txt`). I rendered the pages at 300 dpi (`gp1965_p1-1.png`, `gp1965_p-2.png`, `gp1965_p-3.png`, `gp1965_p-4.png`) and OCR'd them with tesseract (`gunn_peterson1965_ApJ142_1633_ADSscan.p{1,2,3,4}.ocr.txt`). I checked the quoted passages against the page images by eye; the OCR text is quoted as produced and the image reading is given outside the quote.

**The paper has no abstract** (it is a one-and-a-half-page Note under the heading "NOTES"). The opening paragraph is quoted in its place.

Q5.1 (p.1633, opening paragraph; OCR of page image):
> "Recent spectroscopic observations by Schmidt (1965) of the quasi-stellar source 3C 9, which is reported by him to have a redshift of 2.01, and for which Lyman-a is in the visible spectrum, make possible the determination of a new very low value for the density of neutral hydrogen in intergalactic space. It is observed that the continuum of the source continues (though perhaps somewhat weakened) to the blue of Ly-a; the line as seen on the plates has some structure but no obvious asymmetry. Consider, however, the fate of photons emitted to the blue of Ly-a. As we move away from the source along the line of sight, the source becomes redshifted to observers locally at rest in the expansion, and for one such observer, the frequency of any such photon coincides with the rest frequency of Ly-a in his frame and can be scattered by neutral hydrogen in his vicinity."

OCR artefact: "Ly-a" / "Lyman-a" is "Ly-α" / "Lyman-α" on the page. Otherwise verified word-for-word against `gp1965_p1-1.png`.

Q5.2 (p.1634, result; OCR of page image):
> "best estimates place the depression at about 40 per cent, which corresponds to an optical depth of about }. This yields, for go = }, a number density n, = 6 X 10~" cm™, or a mass density p, = 1 X 10-*4 gm cm7*—a figure five orders of magnitude below the limit (for the present density, which should be 27 times smaller because of the expansion) obtained from 21-cm observations by Field (1962)."

OCR artefacts (read from `gp1965_p-2.png`): "}" is "½" (both occurrences: optical depth of about ½; q₀ = ½); "go" is "q₀"; "n, = 6 X 10~" cm™" is "n_s = 6 × 10⁻¹¹ cm⁻³"; "p, = 1 X 10-*4 gm cm7*" is "ρ_s = 1 × 10⁻³⁴ gm cm⁻³".

Q5.3 (p.1634, conclusion paragraph; OCR of page image):
> "We are thus led to the conclusion that either the present cosmological ideas about the density are grossly incorrect, and that space is very nearly empty, or that the matter exists in some other form. Oort has shown that only about 1 per cent of the go = 3 density is accounted for by galaxies, and it has been generally assumed that the remainder exists as an intergalactic gas which is presumably mostly or entirely hydrogen. It is possible that this interpretation is still valid but that essentially all of the hydrogen is ionized; this conclusion can be defended if we are allowed to make the intergalactic eléctron temperature high enough."

OCR artefacts: "go = 3" is "q₀ = ½"; "eléctron" is "electron".

---

## File list

| File | Source | Bytes |
|---|---|---|
| seager1999_recfast.pdf (+ .txt, .layout.txt, seager1999_p2-2.png) | arXiv:astro-ph/9909275 | 152248 |
| alihaimoud_hirata2011_hyrec.pdf (+ .txt, .layout.txt) | arXiv:1011.3758 | 939194 |
| planck2018_VI_params.pdf (+ .txt, .layout.txt) | arXiv:1807.06209 | 9317371 |
| fan_carilli_keating2006_araa.pdf (+ .txt, .layout.txt) | arXiv:astro-ph/0602375 | 1712879 |
| gunn_peterson1965_ApJ142_1633_ADSscan.pdf (+ .txt, .layout.txt [watermark only], p1–p4 .ocr.txt, gp1965_p1-1.png, gp1965_p-2/3/4.png) | ADS full-text scan 1965ApJ...142.1633G | see `ls -l` |

MD5 of the PDFs as downloaded 2026-10-09:
- seager1999_recfast.pdf cbb3c83abec3c9f05037b4464d394f70
- alihaimoud_hirata2011_hyrec.pdf 706dba9e9f6801fcc6f46d8d90d1e5ad
- planck2018_VI_params.pdf dc68f185ade3f38366ab9e223629fd31
- fan_carilli_keating2006_araa.pdf ccbd48c9c1c9190c02bab7413d5ee078
- gunn_peterson1965_ApJ142_1633_ADSscan.pdf 71b64b99ecf453c3f792c0dbf2a9808b

Quote count: Seager 4 (+1 caption note); HyRec 4 (+1 supplementary); Planck 6 numbered (5 table rows + 1 model sentence) + footnote 15 + 2 supporting; Fan 4 (Q4.4 has two parts); Gunn & Peterson 3. Total numbered quotes: 21.
