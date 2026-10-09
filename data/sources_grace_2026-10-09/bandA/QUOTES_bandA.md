# Band A primary sources — verbatim quotes

Retrieved 2026-10-09. Every quote below is copied from the sibling `.txt` extracted with `pdftotext -layout` (or, where marked, from the HTML->text / JSON / tesseract sibling), with only whitespace collapsed. OCR errors in the 1934 scan are reproduced as-is inside quotes; glosses are outside the quotes. Page numbers are the printed journal pages (Fermi, Urbantke) or the PDF page of the arXiv preprint (CMS, Mosseri–Dandoloff, Cisowski).

Network notes (why two items are incomplete): `mathnet.ru` resets TCP connections from this network on both 80 and 443 (also refused for WebFetch and a reader proxy; no Wayback snapshot). `royalsocietypublishing.org` serves a Cloudflare JS challenge (HTTP 403) to curl, WebFetch and a reader proxy, for both the DOI landing page and the article-PDF URL. `archive.org` holds a scan of Proc. R. Soc. A vol. 139 (1933) as item `bwb_T5-BCA-087_139` but it is `access-restricted-item: true` (lending only); the `_djvu.txt` download and the search-inside endpoint both return 403 "Item not available".

---

## 1. Holevo 1973 — PARTIAL (English abstract only; full PDF NOT OBTAINED)

**Files:** `holevo_1973_PIT_9_3_contents_abstracts_iitp.html` (raw page), `holevo_1973_PIT_9_3_contents_abstracts_iitp.txt` (tags stripped). Source: the IITP (Institute for Information Transmission Problems, publisher of the journal) contents page for the English translation volume, http://www.pit-contents.iitp.ru/3-73-abstracts.html.

**NOT OBTAINED:** the article body. The Russian original PDF (mathnet.ru, Probl. Peredachi Inf. 9:3 (1973) 3–11, "Full-text PDF (789 kB)" per the mathnet record) is unreachable from this network (connection reset by peer; no archived copy). The English translation (Problems of Information Transmission 9(3):177–183) is not hosted by Springer/MAIK for 1973 and no open copy was found. So the page-located statement of the inequality and the log d consequence inside the paper body are **not verified here**; only the translation's abstract (which states the inequality) is quoted.

**Bibliographic line:** A. S. Holevo, "Bounds for the Quantity of Information Transmitted by a Quantum Communication Channel", Problems of Information Transmission 9(3):177–183 (1973) [translation of Problemy Peredachi Informatsii 9(3):3–11 (1973)].

Quote 1 (IITP contents page, entry header; translation pp. 177–183):
> "Bounds for the Quantity of Information Transmitted by a Quantum Communication Channel A. S. Holevo pp. 177–183"

Quote 2 (IITP contents page, the translation's abstract, LaTeX as served; translation p. 177):
> "Abstract—Certain bounds are derived for the quantity of information transmitted by a quantum channel. It is proved that if at least two of the set of density operators $\rho_0,\ldots,\rho_n$ do not commute, then $J(\pi)<\mathcal H\bigl(\sum\limits_\alpha\pi_\alpha\rho_\alpha\bigr) -\sum\limits_\alpha\pi_\alpha\mathcal H(\rho_\alpha)$, where $J(\pi)$ is the upper bound of the quantity of information with respect to all generalized measurements at the channel output for a fixed distribution $\pi=(\pi_0,\ldots,\pi_n)$ at the input. A sharper upper bound for $J(\pi)$ is explicitly stated."

Gloss (not a quote): in modern notation this is I ≤ S(Σ p_i ρ_i) − Σ p_i S(ρ_i), strict when the ρ_i do not all commute. The abstract does not state the log d consequence; that step (S(ρ) ≤ log d for a d-dimensional ρ) is not sourced here.

---

## 2. Sargent 1933 — PARTIAL (publisher-deposited abstract only; full text NOT OBTAINED, paywalled/bot-blocked)

**File:** `sargent_1933_rspa.1933.0045_crossref_record.json` (Crossref metadata record deposited by The Royal Society, including the abstract field).

**Correction to the request:** the DOI is 10.1098/rspa.1933.0045 (vol. 139, issue 839, pp. 659–673, published 3 March 1933). DOI rspa.1933.0027 is a different paper (Harkness & Heard, "The stark effect for xenon", 139(838):416–435).

**NOT OBTAINED:** the article body. Royal Society site returns a Cloudflare challenge (403) to all automated fetches; the archive.org scan of the volume is lending-restricted. Consequently **the sentence stating a fifth-power law could not be located or verified in Sargent's own text.** Note that the abstract (below) claims only that "a relation between the maximum energy ... and its disintegration constant appears to exist"; the explicit fifth-power statement in the primary literature retrieved here is Fermi's (item 3, Z. Phys. 88 p. 173: F(η₀) ~ η₀⁵/24 for small η₀).

**Bibliographic line:** B. W. Sargent, "The maximum energy of the β-Rays from uranium X and other bodies", Proceedings of the Royal Society of London. Series A 139(839):659–673 (3 March 1933), doi:10.1098/rspa.1933.0045.

Quote 1 (Crossref `abstract` field = publisher-deposited opening text of the paper; p. 659):
> "It is now generally accepted that the disintegration electrons from radioactive nuclei have a continuous distribution with energy. The end-points of these distribution curves, representing the maximum kinetic energies carried by the β-rays, have been determined in a considerable number of cases and appear to be quite definite. The purpose of this paper is twofold. First, new experimental work on the β-rays from uranium X will be presented in sections 2, 3 and 4. This includes a determination of the end-point of its normal β-ray spectrum, which was found to be 2·32 million volts, and a search for β-rays having energies from 3 to 7 million volts. None were found, and an upper limit on their number was determined. Secondly, a critical survey of the data on the end-points of a number of [3-ray spectra with a list of preferred values will be given in section 5. It will then be shown, in section 6, that a relation between the maximum energy emitted in a spectrum of β-rays and its disintegration constant appears to exist."

---

## 3. Fermi phase-space integral f(Z, E₀) and the free-neutron value

### 3a. Fermi 1934 — OBTAINED (scan with OCR layer)

**Files:** `fermi_1934_zphys88_161_saarland_scan.pdf` (17 pp., pp. 161–177; from https://www.nssp.uni-saarland.de/lehre/Vorlesung/Kernphysik_SS19/History/Papers/Fermi_1.pdf), `fermi_1934_zphys88_161_saarland_scan.txt` (embedded OCR layer via pdftotext), `fermi_1934_p173_tesseract_ocr.txt` (re-OCR of p. 173 at 400 dpi, because the embedded layer dropped the exponent in the small-argument limit of eq. (46)).

**Bibliographic line:** E. Fermi, "Versuch einer Theorie der β-Strahlen. I", Zeitschrift für Physik 88:161–177 (1934), received 16 January 1934.

Quote 1 (title/abstract block, p. 161, embedded OCR):
> "V e r s u c h einer Theorie der p-Strahlen. I1). Von E. Fermi in Rom. M.it 3 Abbildungen. (Eingegangen am 16. Januar 1934.) Eine quantitative Theorie des fl-Zerfalls wird vorgesehlagen, in weleher man die Existenz des Neutrinos annimmt, und die Emission der Elektronen und Neutrinos aus einem Kern beim ~-Zeffall mit einer ~hnliehen Methode behandelt, wie die Emission eines Lichtquants aus einem angeregten Atom in der Strah- lungstheorie. Formeln fiir die Lebensdauer und fiir die Form des emittierten kontinuierlichen/~-Strahlenspektrums werden abgeleitet und mit der Effahrung verglichen."

Quote 2 (p. 173, tesseract re-OCR; the definition of the lifetime integral F(η₀), eq. (45)–(46), and its fifth-power small-argument limit — OCR garbles the formula lines but the prose is clean):
> "Die reziproke Lebensdauer erhalt man aus (44) durch Integration von 7 = 0 bis 7 = 3; man findet: 2 , = 1,75-10% g? [es U,dt| F(m); (45) wo F (yn) = Wit R + 43 — 1) + 78 + osss|— dame m4 78 + Vi+n =F tog(n. + Vi-+ ma) )}-6 Fir kleine Argumente verhalt sich F (y») wie 5/24; fir groBere Argu- mente sind die Werte von F' in der folgenden Tabelle zusammengestellt."

Gloss (not a quote): the printed line reads "Für kleine Argumente verhält sich F(η₀) wie η₀⁵/24"; η₀ is the maximum momentum of the emitted β-rays in units mc (p. 172: "wo η₀ den in Einheiten mc gemessenen maximalen Impuls der emittierten β-Strahlen darstellt"). The same sentence in the embedded OCR layer (p. 173) reads: "Fi~r kleine Argumente verh~lt sieh F (~o) wie ~ / 2 4 ; ffir grSBere Argu- mente sind die Werte yon F in der folgenden Tabelle zusammenges~ellt."

Quote 3 (p. 175, embedded OCR; the lifetime–endpoint relation and the Sargent grouping, with the Sargent citation footnote):
> "Formel (45) gibt eine Beziehung zwischen dem maximalen Impuls der enfittierten,8-Strahlen und der Lebensdauer der fl-strahlenden Substanz: In dieser Beziehung tritt zwar noch ein unbel~anntes Element auf, n~mlich das Integral v* u~ d ~, (50) ffir dessen Auswertung eine Kenntnis der Eigenfunktionen des Protons und des Neutrons im Kern notwendig w/ire. Lm Falle der erlaubten Uber- giinge ist jedoeh (50) yon der GrS~enordnung 1. Man kann also erwarten, dal~ das Produkt ~F (V0) (51) ffir alle erlaubten ~Tberg/inge dieselbe GrbSenordnung hat."

and (p. 175):
> "Aus der Tabelle sind die zwei erwarteten Gruppen ohne weiteres er- kennbar; eine solehe Eiuteilung ist fibrigens bereits yon S a r g e u t 1) auf empirischem Wege festgestellt worden. Die Werte yon 17o sind aus der genannten Arbeit yon S a r g e n t genommen"
> "1) B. W. S a r g e n t , Proc. Roy. Soe. London (A) 139, 659, 1933."

### 3b. Czarnecki–Marciano–Sirlin 2004 — OBTAINED (arXiv)

**Files:** `czarnecki_marciano_sirlin_2004_hep-ph_0406324.pdf`, `.txt` (16 pp.).

**Bibliographic line:** A. Czarnecki, W. J. Marciano, A. Sirlin, "Precision measurements and CKM unitarity", Phys. Rev. D 70:093006 (2004), arXiv:hep-ph/0406324.

Quote 1 (PDF p. 2, Section II):
> "Our analysis of the radiative corrections to neutron beta decay builds on the results of earlier studies, particularly the classic work by Wilkinson [13]. They included O(α) radiative corrections as well as effects due to the final state electromagnetic ep interaction embodied in the Fermi function."

Quote 2 (PDF p. 2, eqs. (5)–(6); the standard free-neutron phase-space value):
> "where f is a phase space factor, f = 1.6887, (6) which includes a relatively large Fermi function contribution [13] (∼ 5.6%) as well as smaller nucleon mass, size and recoil corrections. It has been somewhat updated in eq. (6) to incorporate slight nucleon mass shifts."

Gloss (not a quote): eq. (5) on the same page is 1/τ_n = G_μ² |V_ud|² m_e⁵ (1+3g_A²)(1+RC) f / (2π³); the layout extraction scrambles the fraction so it is not quoted. Ref. [13] there is Wilkinson, Nucl. Phys. A377 (1982) 474.

**NOT OBTAINED (not required once 3a+3b were in hand):** Konopinski 1943 RMP 15:209 (APS paywall) and Wilkinson 1982 NPA 377:474 (Elsevier paywall; ScienceDirect returns 403 to automated fetch). Neither was downloaded.

---

## 4. Hopf fibration S³ → S² for the two-amplitude state / polarization — OBTAINED

### 4a. Mosseri & Dandoloff 2001 — OBTAINED (arXiv)

**Files:** `mosseri_dandoloff_2001_quant-ph_0108137.pdf`, `.txt` (10 pp.).

**Bibliographic line:** R. Mosseri, R. Dandoloff, "Geometry of entangled states, Bloch spheres and Hopf fibrations", J. Phys. A: Math. Gen. 34:10243–10252 (2001), arXiv:quant-ph/0108137.

Quote 1 (PDF p. 1, abstract):
> "The single qubit Hilbert space is the 3-dimensional sphere S 3 . The S 2 base space of a suitably oriented S 3 Hopf fibration is nothing but the Bloch sphere, while the circular fibres represent the qubit overall phase degree of freedom."

Quote 2 (PDF p. 2, Section 2.1–2.2):
> "The single qubit Hilbert space is the unit sphere S 3 embedded in R4 ."
> "The simplest, and most famous, example of a non trivial fibration is the Hopf fibration of S 3 by great circles S 1 and base space S 2 . For the qubit Hilbert space purpose, the fibre represents the global phase degree of freedom, and the base S 2"
> (continues PDF p. 3:) "is identified as the Bloch sphere."

Quote 3 (PDF p. 3, the Hopf map written out):
> "To describe this fibration in an analytical form, we go back to the definition of 2 2 S 3 as pairs of complex numbers (α, β) which satisfy |α| + |β| = 1. The Hopf map 3 2 is defined as the composition of a map h1 from S to R (+∞), followed by an inverse stereographic map from R2 to S 2 :"
> "The first map h1 clearly shows that the full S 3 great circle, parametrized by (α exp iϕ, β exp iϕ) is mapped on the same single point with complex coordinate C."

(Gloss: the stray "2 2" and "3 2" tokens are the superscripts of |α|², |β|², S³, R² displaced by the layout extraction; the PDF reads |α|²+|β|²=1 and h1: S³ → R²(+∞).) The word "polarization" does not occur in this paper; it is stated for a qubit/Bloch sphere, which is the same object as the Poincaré sphere.

### 4b. Urbantke 2003 — OBTAINED (Wayback copy of a university-hosted PDF)

**Files:** `urbantke_2003_hopf_seven_times_JGP46_125.pdf`, `.txt` (publisher typeset, 26 pp.; from http://web.archive.org/web/20260102074725/https://www.fuw.edu.pl/~suszek/pdf/Urbantke2003.pdf; the live host was unreachable).

**Bibliographic line:** H. K. Urbantke, "The Hopf fibration—seven times in physics", Journal of Geometry and Physics 46:125–150 (2003), doi:10.1016/S0393-0440(02)00121-3.

Quote 1 (p. 127, Section 2; the inner-product angle brackets around "z, z" are non-printing glyphs in the extraction, so the quote is split there):
> "One notes that a pure state determines the state vector only up to a non-zero complex factor,"
> "a phase factor eiα , α real, remains undetermined."

Quote 2 (p. 127):
> "We can also get a geometric picture of the state vectors z themselves by looking at C2 as being R4 , taking the real and imaginary parts of z1 , z2 (in some order) as its real components. Then the assignment z → R(z) gives us a map R4 → S2 ⊂ R3 , and restricting to normalized z, z† z = 1, whose realifications fill the 3-sphere S3 ⊂ R4 , we get a map S3 → S2 . This is the Hopf map: if the real components of z are numbered suitably and the definition of R(z) is written out explicitly in terms of them, the above expression for the latter becomes literally identical to Hopf’s original formulae."

Quote 3 (pp. 127–128):
> "The inverse images of the points on the Bloch 2-sphere under the Hopf map are “phase circles” on the 3-sphere. The 2-parameter"
> (p. 128:) "system of phase circles on the 3-sphere so obtained constitute its Hopf fibration."

Note: Urbantke's seven cases do not include optical polarization by name (no occurrence of "polariz" or "Poincaré sphere"; "Poincaré" there refers to the Poincaré group). The two-level/Bloch-sphere case is the mathematically identical statement.

### 4c. Cisowski, Götte & Franke-Arnold 2022 — OBTAINED (arXiv); the explicit *polarization → Poincaré sphere* statement

**Files:** `cisowski_etal_2022_arXiv_2202.04356_geometric_phases_light.pdf`, `..._light.txt` (layout), `..._light_readingorder.txt` (plain `pdftotext`, because the two-column layout extraction cuts the right column; quotes below are from the reading-order file).

**Bibliographic line:** C. Cisowski, J. B. Götte, S. Franke-Arnold, "Geometric phases of light: insights from fibre bundle theory", Rev. Mod. Phys. 94:031001 (2022), arXiv:2202.04356 (dated May 10, 2022).

Quote 1 (PDF p. 5, Section IV.B "From Poincaré to Hopf"):
> "When fully polarized light propagates along a fixed direction, say z, it becomes analogous to a two-state (qubit) system: |ψi = α |0i + β |1i , (4) where |0i and |1i are the eigenstates of the Pauli spin operator σz , and α and β are complex parameters with | α |2 + | β |2 = 1 to ensure normalization. The state vector |ψi lives in the two-dimensional Hilbert space, denoted by H2 . This space is our total space E, which can be pictured as a hypersphere S3 embedded in R4 , represented in orange (left shaded area) in Fig.5.a."

Quote 2 (PDF p. 5):
> "This set of equivalent state vectors form a fibre, which can be pictured as a circle S1 parametrized by φ (C in Fig. 5). For a two-state system, the state space is the projective Hilbert space CP1 , which is an ordinary sphere, known as S2 by mathematicians. The state space is obtained by mapping each quantum state (circle) in the total space onto a point on the sphere. This mapping is performed by the Hopf map, which maps a circle onto a point p in a plane R2 (+∞), then maps this point onto a point p’ on the sphere via an inverse stereographic projection, as illustrated in Fig. 5.a (Mosseri and Dandoloff, 2001). This is how the Poincaré sphere, and all spheres representing two-state systems, are constructed."

Quote 3 (PDF p. 5):
> "The PB phase then corresponds to the holonomy of the connection AAA on a fibre bundle where the base space is CP1 (the Poincaré sphere), a fibre is a set of equivalent states vectors, the group structure is U(1), and the total space is H2 . This fibre bundle is known as the Hopf fibration, and it is capable of describing all two-state systems, not just polarization."

### 4d. Also downloaded (supplementary, not quoted)

`torres_del_castillo_rubalcava_2013_arXiv_1303.4496.pdf` / `.txt` — G. F. Torres del Castillo, I. Rubalcava-García, "The Jones vector as a spinor and its representation on the Poincaré sphere", arXiv:1303.4496 (Rev. Mex. Fís. 57 (2011) 406). Treats the Jones vector as an SU(2) spinor on the Poincaré sphere; does not use the word "Hopf", so not quoted for the fibration statement.

---

## Tally

Obtained in full: Fermi 1934 (scan), Czarnecki–Marciano–Sirlin 2004, Mosseri–Dandoloff 2001, Urbantke 2003, Cisowski et al. 2022, Torres del Castillo–Rubalcava 2013.
Abstract only: Holevo 1973 (IITP English abstract), Sargent 1933 (Crossref-deposited abstract).
Not obtained: Holevo 1973 body (Russian or English), Sargent 1933 body, Konopinski 1943, Wilkinson 1982.
Verbatim quotes: 22 quote strings, each machine-verified 2026-10-09 as a whitespace-collapsed substring of its named source file (Holevo 2, Sargent 1, Fermi 5, CMS 2, Mosseri–Dandoloff 5, Urbantke 4, Cisowski 3).
