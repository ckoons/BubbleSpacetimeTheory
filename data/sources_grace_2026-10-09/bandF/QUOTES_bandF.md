# Band F primary-source quotes

Retrieved 2026-10-09 12:51 EDT by Grace's retrieval subagent. Directory `data/sources_grace_2026-10-09/bandF/` holds untrusted downloaded data: five arXiv PDFs plus `pdftotext` reading-order (`*.txt`) and `pdftotext -layout` (`*.layout.txt`) extractions. Nothing in this directory is executed.

Quoting convention: every quote is VERBATIM from the extracted text with whitespace collapsed only. Extraction artefacts (flattened super/subscripts, integral signs rendered as "Z", scattered equation fragments, intruding page footers) are left INSIDE the quote and flagged OUTSIDE it. Page numbers are PDF pages counted from `pdftotext` form feeds; where the printed folio was checked it is given too. Anything derived by me (arithmetic, reciprocals) is marked DERIVED and is not a quote.

Files and SHA-256:

| # | file | sha256 |
|---|------|--------|
| 1 | madau_dickinson_2014_1403.0007.pdf (76 pp) | 324864fc735b52fa35c6bc8beb920a362edb0d22a7c728bcee064f56a1160a57 |
| 2 | fixsen_2009_0911.1955.pdf (6 pp) | 36cbaee69b8106ca45d007f46a2e002f9f593b67c310f6d808007a5c3d998f85 |
| 3 | driver_2016_1605.01523.pdf (21 pp) | 979d1dc31c4d7afe3ad45af07e0919bf6377fdbd0f757689c15b3fbace109a70 |
| 4 | draine_2003_astro-ph_0304489.pdf (46 pp) | 55183d7acf2a7c73a6752ba2b847129d0011180066cf62e3f733e7a0b189d568 |
| 5 | hill_masui_scott_2018_1802.03694.pdf (34 pp) | 7735ccb1c3c63782fe7620d955fabdc3cc2f4d218ce64b95b1a1c4ca5717ef4d |

Each PDF has sibling `<name>.txt` and `<name>.layout.txt`.

---

## 1. Madau & Dickinson 2014

**Obtained:** `madau_dickinson_2014_1403.0007.pdf` (arXiv:1403.0007v1; PDF page numbers equal the printed folios, checked at pp. 48, 51, 54).

**Bibliographic line:** Madau, P. & Dickinson, M. 2014, "Cosmic Star-Formation History", Annual Review of Astronomy & Astrophysics 52, 415–486; arXiv:1403.0007.

**Q1.1 — Eq. (15), the SFRD fitting function. PDF/printed p. 48 (section "5.1" area, text following Figure 9).**
Reading-order extraction:
> "Figure 9 shows the cosmic SFH from UV and IR data following the above prescriptions, as well as the best-fitting function ψ(z) = 0.015 (1 + z)2.7 M⊙ year−1 Mpc−3 . 1 + [(1 + z)/2.9]5.6 (15)"

Layout extraction of the same equation (three physical lines, collapsed):
> "(1 + z)2.7 ψ(z) = 0.015 M⊙ year−1 Mpc−3 . (15) 1 + [(1 + z)/2.9]5.6"

Artefacts flagged: exponents are flattened ("2.7", "5.6", "−1", "−3" are superscripts); the fraction is split, numerator "(1 + z)2.7" above and denominator "1 + [(1 + z)/2.9]5.6" below the "0.015 … M⊙ year−1 Mpc−3" line. Read as ψ(z) = 0.015 (1+z)^2.7 / {1 + [(1+z)/2.9]^5.6} M⊙ yr⁻¹ Mpc⁻³. Units are printed as "M⊙ year−1 Mpc−3".

**Q1.2 — redshift of peak star formation. PDF p. 1, Abstract.**
> "A consistent picture is emerging, whereby the star-formation rate density peaked approximately 3.5 Gyr after the Big Bang, at z ≈ 1.9, and declined exponentially at later times, with an e-folding timescale of 3.9 Gyr."

Supporting sentence, PDF/printed p. 48, immediately after Eq. (15):
> "These state-of-the-art surveys provide a remarkably consistent picture of the cosmic SFH: a rising phase, scaling as ψ(z) ∝ (1 + z)−2.9 at 3 < < ∼ z ∼ 8, slowing and peaking at some point probably between z = 2 and 1.5, when the Universe was ∼ 3.5 Gyr old, followed by"

Artefact flagged: "3 < < ∼ z ∼ 8" is the extraction of 3 ≲ z ≲ 8 (the "<" and "∼" halves of each ≲ glyph land on separate lines; the first "<" is displaced to the end of the preceding line, so two "<" appear together). Sentence continues on the next printed page with "a gradual decline to the present day, roughly as ψ(z) ∝ (1 + z)2.7 ." (running head "48 P. Madau & M. Dickinson" intervenes in the extraction).

**Q1.3 — Eq. (2), stellar mass density as the integral of ψ with return fraction R. PDF p. 5, Section "THE EQUATIONS OF COSMIC CHEMICAL EVOLUTION".**
Definition of R (text following Eq. 1):
> "Here, Z is the metallicity in the gas and newly born stars, R is the “return fraction” or the mass fraction of each generation of stars that is put back into the interstellar medium (ISM) and intergalactic medium (IGM), and y is the net metal yield or the mass of new heavy elements created and ejected into the ISM/IGM by each generation of stars per unit mass locked into stars."

Eq. (2), layout extraction (four physical lines, collapsed):
> "1. The total mass density of long-lived stars and stellar remnants accumulated from earlier episodes of star formation, Z t(z) Z ∞ dz ′ ρ∗ (z) = (1 − R) ψdt = (1 − R) ψ , (2) 0 z H(z ′ )(1 + z ′ ) where H(z ′ ) = H0 [ΩM (1 + z ′ )3 + ΩΛ ]1/2 is the Hubble parameter in a flat cosmology."

Artefacts flagged: the "Ω" characters in "ΩM" and "ΩΛ" are the U+2126 Ohm-sign code point in the extraction (kept as extracted); each "Z" is the integral-sign glyph; limits are t(z)/0 on the first integral and ∞/z on the second; "dz ′" over "H(z ′ )(1 + z ′ )" is a fraction. Read as ρ∗(z) = (1−R) ∫₀^{t(z)} ψ dt = (1−R) ∫_z^∞ ψ dz′/[H(z′)(1+z′)].

Value of R used, Figure 11 caption, PDF/printed p. 51:
> "The solid line shows the global stellar mass density obtained by integrating the best-fit instantaneous star-formation rate density ψ(z) (Equations 2 and 15) with a return fraction R = 0.27."

**Q1.4 — present-day stellar mass density and the IMF assumed.**
PDF/printed p. 54 (Section 5.4 "Stellar Mass Density" discussion):
> "The present-day total SMD derived by Gallazzi et al. (2008) is (6.0±1.0)×108 M⊙ Mpc−3 (scaled up from a Chabrier to a Salpeter IMF), in excellent agreement with ρ∗ = 5.8 × 108 M⊙ Mpc−3 predicted by our model SFH. This stellar density corresponds to a stellar baryon fraction of only 9% (5% for a Chabrier IMF)."

Artefact flagged: "108" is 10⁸.

IMF, PDF p. 7 (end of Section on yields, before "STAR-FORMATION RATE INDICATORS"):
> "Although disfavored by many observations, a Salpeter IMF in the mass range 0.1−100 M⊙ is used as a reference throughout the rest of this review. Similarly, for consistency with prior work, we assume the canonical metallicity scale where solar metallicity is Z⊙ = 0.02, rather than the revised value Z⊙ = 0.014 of Asplund et al. (2009)."

---

## 2. Fixsen 2009

**Obtained:** `fixsen_2009_0911.1955.pdf` (arXiv:0911.1955v2, 10 Nov 2009).

**Bibliographic line:** Fixsen, D. J. 2009, "The Temperature of the Cosmic Microwave Background", The Astrophysical Journal 707, 916–920; arXiv:0911.1955.

**Q2.1 — Abstract, PDF p. 1.**
> "The FIRAS data are independently recalibrated using the WMAP data to obtain a CMB temperature of 2.7260±0.0013. Measurements of the temperature of the cosmic microwave background are reviewed. The determination from the measurements from the literature is cosmic microwave background temperature of 2.72548±0.00057 K."

Note (outside quote): the first value is printed without a unit in the abstract (K understood).

**Q2.2 — Section 4 closing sentence, PDF p. 6 (immediately before "5. SUMMARY AND CONCLUSIONS").**
> "Combining all of the estimates results in a very modestly elevated χ2 and an improved absolute temperature estimation of 2.72548 ± 0.00057 K."

Artefact flagged: "χ2" is χ².

---

## 3. Driver et al. 2016

**Obtained:** `driver_2016_1605.01523.pdf` (arXiv:1605.01523v1, 5 May 2016, "Accepted for Astrophysical Journal").

**Bibliographic line:** Driver, S. P., Andrews, S. K., Davies, L. J., Robotham, A. S. G., Wright, A. H., Windhorst, R. A., Cohen, S., Emig, K., Jansen, R. A. & Dunne, L. 2016, "Measurements of Extragalactic Background Light from the Far UV to the Far IR from Deep Ground- and Space-based Galaxy Counts", The Astrophysical Journal 827, 108; arXiv:1605.01523. (arXiv title as printed: "EXTRA-GALACTIC BACKGROUND LIGHT MEASUREMENTS FROM THE FAR-UV TO THE FAR-IR FROM DEEP GROUND AND SPACE-BASED GALAXY COUNTS".)

**Q3.1 — Abstract, PDF p. 1 (reading-order extraction).**
> "Finally we use a modified version of the two-component model to integrate the EBL and obtain measurements of the Cosmic Optical −2 Background (COB) and Cosmic Infrared Background (CIB) of: 24+4 sr−1 and 26+5 −4 nW m −5 nW −2 −1 m sr respectively (48:52%)."

Artefacts flagged: asymmetric error super/subscripts and unit exponents are scattered through the line. Read as COB = 24 (+4, −4) nW m⁻² sr⁻¹ and CIB = 26 (+5, −5) nW m⁻² sr⁻¹, a 48:52% split.

**Q3.2 — Section 3.6.3/3.6.4 body text, PDF p. 12 (reading-order extraction).**
> "the COB and CIB. We find values of 24+4 sr−1 −4 nW m +5 −2 −1 and 26−5 nW m sr respectively, essentially a 48:52% split."

Layout extraction of the same passage, PDF p. 12:
> "using the R (integrate) function from 0.1 to 8µm and conceivably detect the reionisation field. 8 to 1000µm to obtain the total energy contained within the COB and CIB. We find values of 24+4 −4 nW m −2 sr−1 3.6.4. eIGL → EBL +5 −2 −1 and 26−5 nW m sr respectively, essentially a 48:52% The eIGL and the EBL are, from the discussion above, split."

Artefacts flagged: the layout extraction interleaves the two columns line by line, so fragments of the left column ("conceivably detect the reionisation field.", the heading "3.6.4. eIGL → EBL", "The eIGL and the EBL are, from the discussion above,") are embedded in the right-column sentence; exponents scattered as before. The sentence itself reads: "using the R (integrate) function from 0.1 to 8µm and 8 to 1000µm to obtain the total energy contained within the COB and CIB. We find values of 24+4−4 nW m−2 sr−1 and 26+5−5 nW m−2 sr−1 respectively, essentially a 48:52% split." The integration ranges 0.1–8 µm (COB) and 8–1000 µm (CIB) are stated here.

**Q3.3 — Conclusions, PDF p. 14.**
> "Using a slightly modified version of the model as a fitting function we find that the COB and CIB con−2 −2 tain 24+4 sr−1 and 26+5 sr−1 respec−4 nW m −5 nW m tively, essentially a 48:52% split."

Artefact flagged: "con−2 −2 tain" and "respec−4 … tively" are hyphenated words with exponent fragments interleaved.

---

## 4. Draine 2003

**Obtained:** `draine_2003_astro-ph_0304489.pdf` (arXiv:astro-ph/0304489v1, 28 Apr 2003).

**Bibliographic line:** Draine, B. T. 2003, "Interstellar Dust Grains", Annual Review of Astronomy & Astrophysics 41, 241–289; arXiv:astro-ph/0304489.

**Important negative finding:** the two forms requested ("dust-to-gas mass ratio ~0.01" and "A_V/N_H ≈ 5.3×10⁻²² mag cm²") do NOT appear verbatim in this paper. Grep over both extractions for "dust-to-gas", "gas-to-dust", "0.01", "1/100", "mass ratio" finds no sentence giving the ratio as a number; the phrase "dust-to-gas ratio" appears only in passing (pp. 30, 34). What IS printed is the inverse quantity N_H/A_V (Eq. 3) and the model value M_H/M_dust = 90 (Table 4 footnote). Quoted below as printed; reciprocals are DERIVED and flagged.

**Q4.1 — Section 2.1.2 "EXTINCTION PER H", Eqs. (2)–(4), PDF p. 5 (layout extraction).**
> "2.1.2 EXTINCTION PER H Using H Lyman-α and absorption lines of H2 to determine the total H column density NH , Bohlin et al. (1978) found NH /(AB − AV ) = 5.8 × 1021 cm−2 mag−1 , (2) NH /AV ≈ 1.87 × 1021 cm−2 mag−1 for RV = 3.1 , (3) to be representative of dust in diffuse regions. For RV = 3.1, the F99 reddening fit gives AIC /AV = 0.554 for Cousins I band (λ = 0.802 µm), thus AIC /NH ≈ 2.96 × 10−22 mag cm2 for RV = 3.1 . (4)"

Artefacts flagged: "1021" = 10²¹, "10−22" = 10⁻²², "cm2" = cm², "AIC" = A_{I_C}, "H2" = H₂. DERIVED (not printed): 1/(1.87×10²¹ cm⁻² mag⁻¹) = 5.35×10⁻²² mag cm² per H, which is the "A_V/N_H ≈ 5.3×10⁻²²" form the caller asked for.

**Q4.2 — Table 4 footnote g, PDF p. 29 ("Table 4: Absorption and Scattering for 5 µm > λ > 0.1 µm").**
> "κabs (λ) = absorption cross section per unit dust mass. For this model, MH /Mdust = 90."

Context (footnote d of the same table, same page): "RV = 3.1 Milky Way dust model of Weingartner & Draine (2001a) but with abundances reduced by 0.93, and using optical constants from Draine (2003b)". DERIVED (not printed): M_dust/M_H = 1/90 = 0.0111; dividing by 1.4 for He gives M_dust/M_gas ≈ 0.0079. This is the closest the paper comes to a "~0.01" dust-to-gas ratio.

**Q4.3 — passing uses of the phrase "dust-to-gas ratio".**
PDF p. 30 (Section 9.1, diffuse-ISM emission):
> "the observed 21 cm emission provides accurate gas column densities which, for an assumed dust-to-gas ratio, determine the column density of dust."

PDF p. 34 (Section 10, abundance-budget discussion, item 1):
> "Since it is not clear how the sample of sightlines is constructed, it is not apparent that the average value of NH /AI for the sample is the same as the overall dust-to-gas ratio for the ISM."

---

## 5. Hill, Masui & Scott 2018

**Obtained:** `hill_masui_scott_2018_1802.03694.pdf` (arXiv:1802.03694v2, 5 Apr 2018; PDF page = printed folio, checked at p. 7/8).

**Bibliographic line:** Hill, R., Masui, K. W. & Scott, D. 2018, "The Spectrum of the Universe", Applied Spectroscopy 72, 663–688; arXiv:1802.03694.

**Finding:** the paper does not print the CMB share of the total photon energy density as a percentage. It states the CMB is the highest-amplitude component, gives u_CMB and n_CMB numerically, and gives the CIB (and COB) energy density as "a factor of 40" below the CMB (each ~10⁻¹⁵ J m⁻³ vs 4.2×10⁻¹⁴ J m⁻³). No EBL photon NUMBER density is stated.

**Q5.1 — Section 3.2 opening, PDF p. 7.**
> "The CMB is dramatically the highest amplitude part of the CB. It is also the most thoroughly studied portion of the spectrum (possibly the most thoroughly studied phenomenon in cosmology), and its origin is now very well understood."

**Q5.2 — Section 3.2, CMB energy and photon number density, PDF pp. 7–8 (reading-order extraction).**
> "For a blackbody with TCMB = 2.7255 K, the peak (in νIν ) is at about 220 GHz, or 1.4 mm. Given the 7 precise mathematical form of this part of the CB, we can integrate to obtain the energy density of the CMB, uCMB = 4.2 × 10−14 J m−3 = 0.26 eV cm−3 , or the number density of CMB photons, nCMB = 410 cm−3 ."

Artefacts flagged: the isolated "7" after "Given the" is the page-7 footer intruding at the page break; "10−14" = 10⁻¹⁴, "m−3" = m⁻³, "cm−3" = cm⁻³.

**Q5.3 — Section 3.3 opening (CIB vs CMB energy density), PDF p. 8.**
> "The CIB contains approximately half of the total energy density of the radiation emitted by stars through the history of the Universe (although with roughly a factor of 40 less total energy density than contained in the CMB) and is tightly linked to the history of galaxy formation."

**Q5.4 — Section 3.4 (COB vs CIB energy density), PDF p. 11; and CIB peak energy density, PDF p. 10.**
> "Following the trough seen in the CIB, there is another peak here at about 3 × 1014 Hz (1 µm), containing a similar total energy density to that from the CIB peak (i.e., around 10−15 J m−3 )."

PDF p. 10 (Section 3.3, Fig. 3 discussion):
> "2–3 × 1012 Hz (100–150 µm) and contains an energy density of approximately 10−15 J m−3 ."

DERIVED (not printed): u_CMB / (u_CIB + u_COB) ≈ 4.2×10⁻¹⁴ / (2×10⁻¹⁵) ≈ 20, i.e. the CMB carries roughly 95% of the CMB+EBL photon energy density by these numbers.

---

## Tally

- Files obtained: 5 of 5 PDFs (+10 text extractions).
- Every quoted passage was machine-checked (whitespace-collapsed exact substring) against the concatenated extractions: 24/24 match.
- Verbatim quotes: item 1: 4 entries (8 quoted passages); item 2: 2; item 3: 3 (4 passages); item 4: 3 entries (5 passages); item 5: 4 entries (5 passages). Total 16 numbered entries, 24 quoted passages.
- Not found as requested: Draine "dust-to-gas ≈ 0.01" sentence and "A_V/N_H ≈ 5.3×10⁻²²" form (only N_H/A_V ≈ 1.87×10²¹ and M_H/M_dust = 90 are printed); Hill CMB-fraction-as-percentage and EBL photon number density (only "factor of 40" and n_CMB = 410 cm⁻³ are printed).
