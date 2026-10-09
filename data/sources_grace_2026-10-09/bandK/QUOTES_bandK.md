# Band K — primary-source pins for length scales
Retrieved 2026-10-09 15:35–15:41 EDT (system clock). All files in this directory are untrusted downloaded data; nothing in it was executed. Value strings below are copied verbatim from the saved files (NIST pages: text of the "Numerical value / Standard uncertainty / Relative standard uncertainty / Concise form" table; scans: the pdftotext OCR layer, with OCR glyph errors left as-is and glossed in brackets).

## 1. CODATA 2022 (NIST Fundamental Physical Constants)

Every page carries the footer "Source: 2022 CODATA recommended values". Each file is the HTML of the NIST "Value" page, fetched by curl from https://physics.nist.gov/cgi-bin/cuu/Value?<key>.

| # | Quantity | Key / file | Numerical value | Standard uncertainty | Rel. std. unc. | Concise form |
|---|----------|-----------|-----------------|----------------------|----------------|--------------|
| 1 | Compton wavelength (electron), λ_C | `ecomwl` / nist_codata2022_Value_ecomwl.html | `2.426 310 235 38 x 10-12 m` | `0.000 000 000 76 x 10-12 m` | `3.1 x 10-10` | `2.426 310 235 38(76) x 10-12 m` |
| 2 | reduced Compton wavelength (electron), ƛ_C = ħ/(m_e c) | `ecomwlbar` / nist_codata2022_Value_ecomwlbar.html | `3.861 592 6744 x 10-13 m` | `0.000 000 0012 x 10-13 m` | `3.1 x 10-10` | `3.861 592 6744(12) x 10-13 m` |
| 3 | proton Compton wavelength | `pcomwl` / nist_codata2022_Value_pcomwl.html | `1.321 409 853 60 x 10-15 m` | `0.000 000 000 41 x 10-15 m` | `3.1 x 10-10` | `1.321 409 853 60(41) x 10-15 m` |
| 4 | Bohr radius, a_0 | `bohrrada0` / nist_codata2022_Value_bohrrada0.html | `5.291 772 105 44 x 10-11 m` | `0.000 000 000 82 x 10-11 m` | `1.6 x 10-10` | `5.291 772 105 44(82) x 10-11 m` |
| 5 | classical electron radius, r_e | `re` / nist_codata2022_Value_re.html | `2.817 940 3205 x 10-15 m` | `0.000 000 0013 x 10-15 m` | `4.7 x 10-10` | `2.817 940 3205(13) x 10-15 m` |
| 6 | proton rms charge radius, r_p | `rp` / nist_codata2022_Value_rp.html | `8.4075 x 10-16 m` | `0.0064 x 10-16 m` | `7.6 x 10-4` | `8.4075(64) x 10-16 m` |
| 7 | Planck length, l_P | `plkl` / nist_codata2022_Value_plkl.html | `1.616 255 x 10-35 m` | `0.000 018 x 10-35 m` | `1.1 x 10-5` | `1.616 255(18) x 10-35 m` |

Notes on the pages' own text:
- Rows 1 and 3 carry a dagger: "† The full description of unit m is meter per cycle."
- Page titles as served: "CODATA Value: Compton wavelength †", "CODATA Value: reduced Compton wavelength", "CODATA Value: proton Compton wavelength †", "CODATA Value: Bohr radius", "CODATA Value: classical electron radius", "CODATA Value: proton rms charge radius", "CODATA Value: Planck length".
- The exponent is rendered in the HTML as `x 10<sup>-12</sup>`; the table above writes it `x 10-12`.

## 2. Nuclear radius R = r_0 A^{1/3}

### 2a. HyperPhysics (R. Nave, Georgia State University), "Nuclear Size and Density" — OBTAINED
- URL: http://hyperphysics.phy-astr.gsu.edu/hbase/Nuclear/nucuni.html (section "Nuclear Size and Density"; the page's own reference line reads "Reference Krane Ch. 3")
- Files: `hyperphysics_nucuni_nuclear_size.html` (page), `hyperphysics_imgnuc_nrad1.png` (the formula image, src `imgnuc/nrad1.png`), `hyperphysics_imgnuc_nrad2.png` (density-function image)
- Page text (verbatim): "Various types of scattering experiments suggest that nuclei are roughly spherical and appear to have essentially the same density. The data are summarized in the expression called the Fermi model: [image nrad1.png] where r is the radius of the nucleus of mass number A."
- Formula image nrad1.png (read visually; verbatim): `r = r0 A^{1/3} where r0 = 1.2x10^{-15} m = 1.2 fm`
- The page's calculator script also encodes the same constant: `rr=1.2*Math.pow(10,-15)*Math.pow(aa,1/3)`.
- Further sentence on the page: "Krane comments that the evidence points to a mass radius and a charge radius which agree with each other within about 0.1 fermi."

### 2b. MIT OpenCourseWare 22.02 Introduction to Applied Nuclear Physics (Spring 2012), Lecture notes Chapter 1 — OBTAINED (gives R_0 = 1.25 fm)
- URL: https://ocw.mit.edu/courses/22-02-introduction-to-applied-nuclear-physics-spring-2012/d0d046f78c917f107d925f11ac862ae4_MIT22_02S12_lec_ch1.pdf (linked from .../resources/mit22_02s12_lec_ch1/)
- Files: `mit_ocw_2202_S12_lec_ch1.pdf`, `mit_ocw_2202_S12_lec_ch1.txt` (pdftotext -layout)
- Section 1.1.3 "Nuclear Radius", p. 6 (verbatim): "A simple formula that links the nucleus radius to the number of nucleons is the empirical radius formula: R = R0 A1/3" [R = R_0 A^{1/3}]
- Section 1.2 (semi-empirical mass formula, Coulomb term), p. 8 (verbatim): "Then the constant ac can be estimated from ac ≈ 35 4πǫe0 R0 , with R0 = 1.25fm, to be ac ≈ 0.691 MeV, not far from the experimental value." [a_c ≈ (3/5) e²/(4πε_0 R_0), R_0 = 1.25 fm]

### 2c. Krane, Introductory Nuclear Physics, Ch. 3 — NOT OBTAINED directly (no open full text); pinned through 2a, whose page cites "Krane Ch. 3" and states r_0 = 1.2 fm.
Spread to record: 1.2 fm (HyperPhysics/Krane) vs 1.25 fm (MIT 22.02); both are textbook conventions for the same empirical formula.

## 3. Interstellar grain sizes

### 3a. Mathis, Rumpl & Nordsieck 1977, ApJ 217, 425–433 — OBTAINED (ADS full-text scan, 9 pages, OCR text layer)
- Bibliographic line (verbatim from scan p. 425 header): "The Astrophysical Journal, 217:425-433, 1977 October 15 / THE SIZE DISTRIBUTION OF INTERSTELLAR GRAINS / John S. Mathis, William Rumpl, and Kenneth H. Nordsieck / Washburn Observatory, University of Wisconsin-Madison / Received 1977 January 24; accepted 1977 April 11"
- URL fetched: https://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1977ApJ...217..425M&defaultprint=YES&filetype=.pdf (bibcode 1977ApJ...217..425M). The ui.adsabs.harvard.edu abstract page and adsabs.harvard.edu/full/ index returned an AWS-WAF "Human Verification" shell / empty body and were discarded.
- Files: `mrn1977_ads_scan.pdf`, `mrn1977_ads_scan_p1.txt` (p. 425), `mrn1977_ads_scan_fulltext.txt` (all 9 pages)
- Abstract, p. 425 (verbatim OCR; "/zm", "/¿m", "¿on" are OCR renderings of "μm"): "The particle size distributions are roughly power law in nature, with an exponent of about —3.3 to —3.6. The size range for graphite is about 0.005 /zm to about 1 ¿on. The size distribution for the other materials is also approximately power law in nature, with the same exponent, but there is a narrower range of sizes: about 0.025-0.25 /¿m, depending on the material. The number of large particles is not well determined, because they are gray. Similarly, the number of small particles is not well determined because they are in the Rayleigh limit."
- Section III, p. 428 (verbatim OCR): "First, there is a wide range in sizes of particles (roughly between 0.005 and 0.25 ¿on for graphite and 0.025 and 0.25 /xm for the other material). Second, there is a rapid decrease of number with size. ... if we connect the nonzero values in Figure 1, we obtain approximately a power law, with n(a) oc a~9, with q in the range 3.3 < q < 3.6 for the various substances." [n(a) ∝ a^{−q}]
- Section III, p. 430 — the explicit −3.5 / 0.005–0.25 μm statement (verbatim OCR): "Figure 4, dots, shows the extinction of a (C + 01) mixture with log n{d) = Kc — 3.5 log(ö/l jum) for graphite and log n(a) = K01 — 3.5 log (a/1 //m) for olivine (0.005 fim < a < 0.25 ¿an). The constants, for n{d) in units of particles per H atom per micron, are Kc = -15.24 and K0l = -15.21." [log n(a) = K_C − 3.5 log(a/1 μm), graphite; log n(a) = K_Ol − 3.5 log(a/1 μm), olivine; 0.005 μm < a < 0.25 μm]
- Fig. 4 caption fragment, p. 430 (verbatim OCR): "û"3-5, 0.005 ^m < a < 0.25 /am, forced to fit at the maximum" [a^{−3.5}, 0.005 μm < a < 0.25 μm]

### 3b. Draine 2003, ARA&A 41, 241 (astro-ph/0304489) — read from existing file, not re-downloaded
- File: `../bandF/draine_2003_astro-ph_0304489.txt` (lines cited are of that file)
- Lines 1361–1365 (verbatim): "Mathis et al. (1977) discovered that the average interstellar extinction could be satisfactorily reproduced by a grain model containing two components – graphite grains and silicate grains. Remarkably, the extinction curve was reproduced very well if both grain components had power-law size distributions, dn/da ∝ a−3.5 , truncated at a minimum size a− ≈ 50Å and a maximum size a+ ≈ 2500Å." [dn/da ∝ a^{−3.5}; a_− ≈ 50 Å; a_+ ≈ 2500 Å]
- Lines 1376–1378 (verbatim, line-wrapped in source): "...but to have physical and chemical properties that can be approximated by grains of bulk graphite when larger than ∼ 0.01 µm (containing N ∼> 106 C atoms)."
- Lines 1392–1398 (verbatim): "The carbonaceous grain distribution is trimodal: The peak at a ≈ 0.3 µm is required to reproduce the observed extinction curve; the peak at a ≈ .0005 µm is required to reproduce the 3 − 12 µm PAH emission features; and the peak at a ≈ 0.005 µm improves the fit to the observed emission near 60 µm. The peaks at ∼ 0.3 µm and ∼ .0005 µm are certainly real, but the peak at .005 µm could be an artifact of errors in the adopted grain optical and FIR cross sections."
- Lines 413–414 (verbatim): "The sightlines in the SMC bar which lack the 2175Å extinction feature can be reproduced by models which lack carbonaceous grains with radii a ∼< 0.02 µm."
- Line 1157 (verbatim, interplanetary dust): "Most GEMS are between 0.1 and 0.5 µm in diameter –"

## 4. Lattice constants of a representative grain solid

### 4a. Forsterite Mg2SiO4 — webmineral.com mineral data page — OBTAINED
- URL: http://webmineral.com/data/Forsterite.shtml
- File: `webmineral_forsterite.html`
- "Forsterite Crystallography" block (verbatim): "Axial Ratios: a:b:c =0.4665:1:0.5866 Cell Dimensions: a = 4.756, b = 10.195, c = 5.981, Z = 4; V = 290.00 Den(Calc)= 3.22 Crystal System: Orthorhombic - Dipyramidal H-M Symbol (2/m 2/m 2/m) Space Group: Pbnm" [cell dimensions in Å, V in Å³, density g/cm³ — units implicit on the page]
- Structure-data citation printed on the page (verbatim): "Birle J D , Gibbs G V , Moore P B , Smith J V , American Mineralogist , 53 (1968) p.807-824, Crystal structures of natural olivines"

### 4b. AMCSD (rruff.geo.arizona.edu/AMS/minerals/Forsterite and /Graphite) — NOT OBTAINED: server did not respond (curl timed out on both http and https, three attempts, 45–120 s). RRUFF (rruff.info/forsterite/.../R040018) — NOT OBTAINED: connection failed (curl exit 000).
### 4c. Graphite lattice constant — NOT ATTEMPTED beyond the AMCSD timeout; one crystallographic source (4a) satisfies the item.

## File list (this directory)
- nist_codata2022_Value_ecomwl.html, nist_codata2022_Value_ecomwlbar.html, nist_codata2022_Value_pcomwl.html, nist_codata2022_Value_bohrrada0.html, nist_codata2022_Value_re.html, nist_codata2022_Value_rp.html, nist_codata2022_Value_plkl.html
- hyperphysics_nucuni_nuclear_size.html, hyperphysics_imgnuc_nrad1.png, hyperphysics_imgnuc_nrad2.png
- mit_ocw_2202_S12_lec_ch1.pdf, mit_ocw_2202_S12_lec_ch1.txt
- mrn1977_ads_scan.pdf, mrn1977_ads_scan_p1.txt, mrn1977_ads_scan_fulltext.txt
- webmineral_forsterite.html
- QUOTES_bandK.md (this file)

## Value count
- CODATA: 7 length scales x (value, std. unc., rel. unc.) = 21 pinned strings
- Nuclear radius: r_0 = 1.2 fm (HyperPhysics/Krane), R_0 = 1.25 fm (MIT) = 2
- MRN 1977: exponent range −3.3 to −3.6; exact exponent −3.5; graphite range 0.005–1 μm (abstract) and 0.005–0.25 μm (Sec. III); other-material range 0.025–0.25 μm; K_C = −15.24, K_Ol = −15.21 = 7
- Draine 2003: a_− ≈ 50 Å, a_+ ≈ 2500 Å, exponent −3.5, PAH/graphite crossover ∼0.01 μm, trimodal peaks 0.3 / 0.0005 / 0.005 μm, SMC a ≲ 0.02 μm, GEMS 0.1–0.5 μm = 10
- Forsterite: a, b, c, Z, V, density = 6
Total: 46 pinned value strings.
