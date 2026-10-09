# Band J — Mössbauer effect: recoil taken by the whole crystal; Lamb–Mössbauer factor; recoil-energy condition

Retrieved 2026-10-09 15:44 EDT (clock run before writing). Directory: `data/sources_grace_2026-10-09/bandJ/`.
All files in this directory are untrusted downloaded data; text was extracted with `pdftotext` / `pdftotext -layout` (and tesseract OCR for the Nobel lecture, whose embedded text layer is letter-spaced garbage). Quotes below are verbatim from the extraction with whitespace collapsed only; extraction artefacts are kept INSIDE the quotes and flagged OUTSIDE in `[...]`. Where an equation was checked against the page image, that is stated.

## Files in this directory

| file | what | sha256 (pdf) |
|---|---|---|
| `mossbauer_nobel_lecture_1961.pdf` (+ `.txt`, `.layout.txt`, `.ocr.txt`) | Item 1. Nobel lecture, 18 pp. (printed pp. 584–601; PDF page = printed page − 583). `.txt`/`.layout.txt` are the letter-spaced embedded layer (unusable); `.ocr.txt` is tesseract 5.5.2 OCR at 300 dpi, `=== PAGE nn ===` markers = PDF page. | `ae14fa61…cd3e5` |
| `frauenfelder_1962_mossbauer_effect_archive.pdf` (+ `.txt`, `.layout.txt`, `_djvu.txt`) | Items 2, 3, 4. Full scan (356 PDF pp.) of Frauenfelder 1962 from archive.org id `mssbauereffec00frau` (University of Florida copy; NOT lending-restricted; direct download). Contains the textbook review (pp. 1–98) AND the reprints: Mössbauer Z. Physik 1958 in full German (pp. 101–120) + English translation of its Sec. 3 (pp. 121–126), Naturwiss. 1958 translation (pp. 127–129), Lipkin Ann. Phys. 1960 (pp. 161–168). Printed page p is PDF page p + 18 for the body. | `4790ff70…b762314` |
| `arxiv_2404.18683_stepanenko2024_Os187_mossbauer.pdf` (+ `.txt`, `.layout.txt`) | Item 5 (SECONDARY). arXiv:2404.18683v2, published Sci. Adv. 11, eads3406 (2025). | `92a1139b…bd212a` |
| `QUOTES_bandJ.md` | this file | |

Not obtained (publisher paywalls, HTTP 403/HTML stub returned, no mirror found): Springer PDF of Z. Physik 151, 124 (DOI 10.1007/BF01344210) — but the full paper is reprinted in Frauenfelder (see Item 2); ScienceDirect PDF of Ann. Phys. 9, 332 — but the full paper is reprinted in Frauenfelder (see Item 3); Gütlich–Bill–Trautwein 2011 Ch. 1 (Springer returned HTML, not a sample chapter). Wertheim 1964 not searched further because Frauenfelder 1962 was obtained in full.

Quote count: 35 numbered quote blocks (Item 1: 9; Item 2: 6 + 2 from the Naturwiss. translation; Item 3: 6; Item 4: 9; Item 5: 3); a few blocks hold two passages from the same page. Five equations were checked against the page image (Nobel Eqs. (1)–(3); Frauenfelder Eq. (56); Lipkin Eq. (15)).

---

## Item 1 — R. L. Mössbauer, Nobel Lecture, 11 Dec 1961 — OBTAINED

**File:** `mossbauer_nobel_lecture_1961.pdf` (nobelprize.org, https://www.nobelprize.org/uploads/2018/06/mossbauer-lecture.pdf). Quotes from `mossbauer_nobel_lecture_1961.ocr.txt`.
**Bibliographic line:** Rudolf L. Mössbauer, "Recoilless nuclear resonance absorption of gamma radiation", Nobel Lecture, December 11, 1961, in *Nobel Lectures, Physics 1942–1962*, Elsevier, Amsterdam, 1964, pp. 584–601.

**Does it say the LATTICE/crystal takes the recoil?** YES, explicitly and twice: recoil *momentum* "is always taken up by the crystal as a whole" (p. 592); recoil *energy* "is taken up by the crystal partly in the form of translational energy and partly in the form of internal energy", the translational part being negligible "because of the enormous mass of the crystal as a whole in comparison to the mass of a single nucleus" (pp. 590–591). It does NOT write f = exp(−k²⟨x²⟩); he says explicitly he develops the picture "without presenting the mathematical formulation of the theory" (p. 592) and names the probability "the Debye-Waller factor" (p. 594).

**Q1.1 (p. 585, PDF 2) — recoil energy of a free nucleus, Eq. (1):**
> "For simplicity, we shall first consider a nuclear transition of a free nucleus at rest. The gamma quantum emitted in the transition imparts a recoil momentum # to the emitting nucleus and consequently a kinetic energy which is given by AE = $2/2M = E,?/2Mc? (1) where M is the mass of the nucleus and c is the velocity of light. The energy liberated in this nuclear transition is divided, in accordance with the law of conservation of momentum, the larger part being carried away by the emitted quantum, the other part going to the emitting nucleus in the form of recoil energy."

[OCR artefacts: "#" = vector p; "$2" = p⃗²; "E,?" = E₀²; "Mc?" = Mc². Image-verified reading of Eq. (1): ΔE = p⃗²/2M = E₀²/2Mc². Note: M here is the mass of the NUCLEUS.]

**Q1.2 (p. 590, PDF 7) — his first (classical, failed) idea: recoil to a cluster of neighbours:**
> "Therefore, I first attempted to explain the observed anomalous resonance absorption by assuming that the recoil momentum was not transferred to the single nucleus. It should rather be transferred to an assembly of nuclei or atoms which include nearest or next-nearest neighbours surrounding the nucleus under consideration. After the failure of this and other attempted explanations, based on a purely classical point of view, I turned my attention to a quantum-mechanical treatment of the problem."

**Q1.3 (pp. 590–591, PDF 7–8) — recoil ENERGY goes to the crystal; crystal mass makes translational part negligible (page 591 image-verified):**
> "The recoil energy appearing in the emission or absorption of a quantum by a nucleus bound in a crystal is taken up by the crystal partly in the form of translational energy and partly in the form of internal energy. The resultant increase in translational energy is always negligible because of the enormous mass of the crystal as a whole in comparison to the mass of a single nucleus. An increase in the internal energy leads to changes in the occupation numbers of the individual crystal oscillators. Because of the quantization of the oscillator energies, the crystal can absorb the recoil energy only in discrete amounts."

**Q1.4 (p. 591, PDF 8) — zero-phonon possibility:**
> "As a consequence of the quantization of the oscillators, there also exists in principle the possibility that the gamma transition takes place with none of the crystal oscillators changing their states."

**Q1.5 (p. 591, PDF 8) — Lamb's neutron theory applied:**
> "Significant was the calculation of the probability of nuclear transitions leaving the lattice state unchanged - that is, transitions in which no recoil energy is transferred to the lattice in the form of internal energy. [...] Lamb® had, as early as 1939, developed a theory for the resonance capture of slow neutrons in crystals. [...] It remained only to apply this Lamb's theory to the analogous problem of the resonance absorption of gamma radiation."

[OCR artefact: "Lamb®" = Lamb⁵ (ref. 5 = W. E. Lamb, Jr., Phys. Rev. 55, 190 (1939), p. 601).]

**Q1.6 (p. 592, PDF 9) — recoil MOMENTUM always taken by the crystal as a whole (image-verified):**
> "Here the notation «recoilless» relates only to recoil energy transferred in a nuclear transition, and not to the transferred momentum. The value of this transferred momentum is determined by the energy of the gamma quantum and is essentially a constant, independent of any change in the internal state of motion of the crystal. This momentum is, therefore, transferred to the lattice in all emission or absorption processes, even in the recoilless processes. It is always taken up by the crystal as a whole, and therefore the corresponding translational velocity is negligibly small."

**Q1.7 (p. 592, PDF 9) — mean recoil energy, Eq. (2), and the two Einstein-model cases (image-verified):**
> "What are the conditions under which the recoilless nuclear resonance absorption can be observed? In answering this question, I wish to develop here, without presenting the mathematical formulation of the theory, a detailed picture [...] It can be shown that in a transition of a nucleus bound in a crystal, Eq. (1) is no longer valid for the individual process but holds in the means over many processes; that is, instead of Eq. (1), we now have AE = E,?/2Me (2) [...] It is instructive to consider the two limiting cases, in which the mean recoil energy is either large or small in comparison to the transition energy of the Einstein oscillator: AE > hw (case 1) AE <hw (case 2) In case 1, many oscillator transitions are required to take up the energy contribution AE in the lattice. [...] The probability of a nuclear transition taking place without any oscillator transition - that is, the probability of a recoilless process - is correspondingly small. The situation is entirely different in case 2."

[Image-verified reading: Eq. (2) is ΔĒ = E₀²/2Mc² (overbar = mean); cases are ΔĒ > ħω (case 1), ΔĒ < ħω (case 2). M is still the nuclear mass; the crystal mass enters only via the negligible translational term of Q1.3/Q1.6.]

**Q1.8 (p. 594, PDF 11) — the condition E_R < kθ, Eq. (3) (image-verified):**
> "The essential condition for a high probability of recoilless nuclear transitions now has the form E3/2Mc < k0 (3) The condition given here is quite restrictive because it limits the observation of recoilless resonance absorption to nuclear transitions of relatively low energy; the upper limit lies at about 150 keV. If AE = E3/2 Mc? is small in comparison to the upper energy limit of the frequency spectrum, the percentage of recoilless processes that occur is high even at room temperature."

[Image-verified reading: E₀²/2Mc² < kθ (3), with ħω_g = kθ, ω_g the upper limit of the vibrational spectrum (p. 594, "limiting frequency wg is related, approximately, to the characteristic temperature 0 of the crystal by the equation hg = ké").]

**Q1.9 (p. 594, PDF 11) — the probability named "Debye-Waller factor"; Fig. 6 caption p. 595:**
> "the next step was to compute the probability of the effect in a general form. This probability, also known as the Debye-Waller factor, in analogy with the terminology used in X-ray scattering, is, as I have already pointed out, strongly dependent on the temperature and the energy of the nuclear transition."
> (p. 595, Fig. 6 caption) "Fractions of recoil-free nuclear transitions (Debye-Waller factors) in “Fe and “Re, shown as functions of the temperature."

[OCR artefact: “Fe, “Re = ⁵⁷Fe, ¹⁸⁷Re.]

---

## Item 2 — R. L. Mössbauer, Z. Physik 151, 124 (1958) — OBTAINED (full German text, as reprint in Frauenfelder 1962, pp. 101–120; English translation of its Sec. 3 "Theorie", pp. 121–126)

**File:** `frauenfelder_1962_mossbauer_effect_archive.pdf`, PDF pp. 119–144. Springer's own PDF (DOI 10.1007/BF01344210) NOT obtained (HTML stub, HTTP 200 but not a PDF).
**Bibliographic line:** R. L. Mössbauer, "Kernresonanzfluoreszenz von Gammastrahlung in Ir¹⁹¹", Z. Physik 151, 124–143 (1958) (eingegangen 9. Januar 1958). Reprinted in Frauenfelder (1962) pp. 101–120; Frauenfelder page = Z. Physik page − 23.

**Does it say the LATTICE/crystal takes the recoil?** YES, as recoil *energy taken as internal energy of the crystal*, quantized, depending on the excitation probabilities of the lattice vibrations (Z. Physik p. 126); it does not use the phrase "als Ganzes". The companion Naturwissenschaften 45, 538 (1958) letter (translated in Frauenfelder p. 127) does say "the solid as a whole can take up the recoil momentum" (Q2.7).

[OCR artefacts throughout the German: "ü"→"ii"/"u", "ß"→"B", "ö"→"o"; e.g. "RiickstoBenergie" = Rückstoßenergie, "fiir" = für, "muB" = muß, "Festkorper" = Festkörper. Kept verbatim inside quotes.]

**Q2.1 (Z. Physik p. 124 = Frauenfelder p. 101, PDF 119) — abstract:**
> "Die Kernresonanzabsorption der dem Zerfall von Os 191 folgenden 129 keV- Gammastrahlung in Ir191 wird untersucht. Der Wirkungsquerschnitt fiir die Resonanzabsorption wird als Funktion der Temperaturen von Quelle und Absorber im Temperaturbereich 90° K< T< 370° K gemessen. Die Lebenszeit r des 129 keV-Niveaus in Ir191 ergibt sich zu (3,6+ J|g) 1CT 10 sec. Der Absorptionsquerschnitt zeigt bei tiefen Temperaturen einen starken Anstieg als Folge der Kristallbindung der Absorber- und Praparatsubstanzen. Die Theorie von Lamb uber die Resonanzabsorption langsamer Neutronen in Kristallen wird auf die Kernresonanzabsorption von Gammastrahlung ubertragen. Bei tiefen Temperaturen ergibt sich eine starke Abhangigkeit des Wirkungsquerschnittes fiir die Kernabsorption von der Frequenzverteilung im Schwingungsspektrum des Festkorpers."

[OCR: "(3,6+ J|g) 1CT 10 sec" = (3,6 +1,3/−0,9)·10⁻¹⁰ sec (error values not legible in OCR; verify on PDF p. 119 image if needed).]

**Q2.2 (Z. Physik p. 124 = Frauenfelder p. 101, PDF 119) — recoil-energy loss defeats resonance for nuclei:**
> "Die Quanten erfahren bei ihrer Emission bzw. Absorption Energieverluste infolge Abgabe von RuckstoBenergie an die emittierenden bzw. absorbierenden Kerne, was zu einer Verschiebung der Emissionslinie gegeniiber der Absorptionslinie fuhrt. Bei Kernubergangen ist, umgekehrt wie bei optischen Obergangen, die durch den RiickstoBenergieverlust der Quanten bedingte Linienverschiebung immer groB gegen die naturliche Linienbreite, d.h. die Resonanzbedingung ist verletzt."

**Q2.3 (Z. Physik p. 126 = Frauenfelder p. 103, PDF 121) — Eq. (1) R = E²/2mc² and the crystal taking the recoil energy as internal energy, quantized:**
> "Ein freier Kern der Masse m ubernimmt bei Emission eines Quants der Energie E eine RiickstoBenergie R, die gegeben ist durch R = Ej2mcK (1) Im Falle einer chemischen Bindung des Kernes in einem Kristall muB der Kristall die RiickstoBenergie als innere Energie aufnehmen. Wegen der Quantelung der inneren Energie konnen jedoch beim RiickstoB nur diskrete Energien aufgenommen werden und die RiickstoBenergie hangt ab von den Wahrscheinlichkeiten flir die Anregung der Gitterschwingungen des Kristalles."

[OCR: "R = Ej2mcK" = R = E²/2mc² (translation p. 121, PDF 139, confirms: "Here R is the recoil energy as given by (1) (see the German original, p. 126)"). Reading: "A free nucleus of mass m takes over, on emission of a quantum of energy E, a recoil energy R given by R = E²/2mc² (1). In the case of chemical binding of the nucleus in a crystal the crystal must take up the recoil energy as internal energy. Because of the quantization of the internal energy, however, only discrete energies can be taken up in the recoil, and the recoil energy depends on the probabilities for excitation of the lattice vibrations of the crystal."]

**Q2.4 (Z. Physik pp. 126–127 = Frauenfelder pp. 103–104, PDF 121–122) — condition: recoil energy vs. upper limit ħω_g of the phonon spectrum:**
> "Bei Temperaturen T, die groB sind gegen die Debyesche Temperatur des Kristalles, ist die statistische Geschwindigkeitsverteilung der Kerne unabhangig von der Bindung und es erfolgt eine ungehinderte Ubertragung der vollen RiickstoBenergie nach (1). Mit abnehmender Temper atur gelangt eine zunehmende Anzahl vorzugsweise der hochfrequenten Schwingungsoszillatoren des Kristalles in den Grundzustand. Diese Oszillatoren konnen keine Energie mehr abgeben und die Linienform wird unsymmetrisch, wenn die RiickstoBenergie nicht groB ist gegen die obere Grenzenergie % co g des Schwingungsspektrums des Kristalles."

[OCR: "% co g" = ħω_g.]

**Q2.5 (Z. Physik p. 127 = Frauenfelder p. 104, PDF 122) — numbers for Ir¹⁹¹:**
> "Bei der Resonanzfluoreszenz des 129keV Niveaus in Ir 191 ist R = 0,046 eV und £(9 = 0,025 eV. Der Fall schwacher Bindung in der Definition nach Lamb [5] ist hier bei Temperaturen T<200°K nicht mehr realisiert."

[OCR: "£(9" = kΘ.]

**Q2.6 (translation of Sec. 3, Frauenfelder p. 121, PDF 139) — the Lamb line-shape function g_a(μ) with nuclear mass m and all 3N normal modes:**
> "In these equations E is the resonance energy, co s the frequency of the s-th normal mode of the crystal, m the nuclear mass, p the momentum of the photon, e the unit polarization vector, 3N the number of degrees of freedom of the crystal, and ~a s the average occupation number of the s-th oscillator, a s = l/[exp (nu> s /kT) - 1] (5)"
> (footnote) "t Translation of Sec. 3 of the article from Z. Physik, 151, 124 (1958) which is reproduced in its entirety preceding this translation."

[The 1958 paper does not isolate a closed-form f = exp(−k²⟨x²⟩); its recoil-free line emerges as the exp[g_∞(T)] term of Eq. (17) (Frauenfelder p. 125, PDF 143): "exp[g w (T)] W n (E) = W (E) + (E I Eq)2 + r2/4 (17)", i.e. a line of natural width Γ at E₀ with weight exp[g_∞(T)] = the recoil-free fraction, with g_∞(T) = −(6R/kΘ)(T/Θ)²∫… (Eq. (8), p. 123, OCR garbled).]

**Q2.7 (BONUS: Naturwissenschaften 45, 538 (1958), English translation, Frauenfelder p. 127, PDF 145) — the solid as a whole takes the recoil momentum:**
> "With the help of a theory developed by Lamb, 4 this effect was attributed to the fact that in solids the recoil momentum does not always produce a change in the vibrational state of the crystal lattice. Instead, for a fraction of the gamma transitions, the solid as a whole can take up the recoil momentum. Thus, according to this theory, the emission and absorption spectra contain very strong lines of natural width superimposed upon a broad distribution resulting from the thermal motion of the atoms bound in the crystal lattice. Because of the vanishingly small recoil energy losses, these lines appear undisplaced at the resonance energy position"

**Q2.8 (same, Frauenfelder p. 127, PDF 145, footnote):**
> "t Translation of article in Naturwissenschaften, 45, 538 (1958)."

---

## Item 3 — H. J. Lipkin, Ann. Phys. 9, 332 (1960) — OBTAINED (full reprint in Frauenfelder 1962, pp. 161–168)

**File:** `frauenfelder_1962_mossbauer_effect_archive.pdf`, PDF pp. 179–186. ScienceDirect PDF NOT obtained (HTTP 403).
**Bibliographic line:** Harry J. Lipkin, "Some Simple Features of the Mössbauer Effect", Annals of Physics 9, 332–339 (1960). Reprinted in Frauenfelder (1962) pp. 161–168; Frauenfelder page = Ann. Phys. page − 171.

**Does it say the LATTICE/crystal takes the recoil?** YES — "The recoil momentum is taken by the crystal as a whole, with negligible energy transfer" (p. 332), and the transition matrix element is taken "between initial and final states of the whole lattice, rather than of the free nucleus" (p. 333). Gives the zero-phonon probability in the harmonic crystal as exp{−Σ_s (2n_s+1)(ħK)²a²_Ls/2Mħω_s} (Eq. (15), p. 336) — the Lamb–Mössbauer factor in normal-mode form — with M the NUCLEAR mass (footnote 3), and the sum rule that the MEAN energy transfer equals the free recoil energy (ħK)²/2M (p. 335).

**Q3.1 (Ann. Phys. p. 332 = Frauenfelder p. 161, PDF 179) — abstract and the key sentence:**
> "A simple description is given of the change in the state of a crystal lattice upon emission or absorption of a nuclear gamma ray. A sum rule is derived for the average energy transfer to the lattice. The probability of zero energy transfer is calculated. The results are general and do not assume a particular model for the crystal."
> "Recent experiments by Mossbauer (1) and others {2) have shown that it is possible for nuclei bound in crystal lattices to emit or absorb gamma radiation having an energy equal to that of the nuclear transition. The recoil momentum is taken by the crystal as a whole, with negligible energy transfer, and there is an appreciable probability, although small, that there is no energy transfer to or from the lattice vibrations."

**Q3.2 (p. 333 = Frauenfelder p. 162, PDF 180) — the operator exp(iK·X) and the whole-lattice matrix element:**
> "For the emission of a gamma ray of momentum hK, the above requirements are satisfied only if the operator A has the form A = exp(iK -X)a(q), (2) [...] Let us now consider the emission or absorption of a gamma ray by a nucleus bound in a crystal. The operator describing the transition is the same operator A, but we must now take the matrix element between initial and final states of the whole lattice, rather than of the free nucleus. Because the crystal forces are very weak compared to the internal nuclear forces, we can assume that the binding forces act only upon the center-of-mass motion of the nucleus and do not perturb the internal degrees of freedom."

[OCR: "hK" = ħK.]

**Q3.3 (p. 334 = Frauenfelder p. 163, PDF 181) — Eq. (5):**
> "We therefore have P(nf m) = , I (n f | exp^X-X L ) 2 | n«) (5) . | The proportionality constant turns out to be unity, as can be verified by substituting (5) into (4) and evaluating the sum by closure."

[Reading: P(n_f, n_i) = |⟨n_f| exp(iK·X_L) |n_i⟩|² (5).]

**Q3.4 (p. 335 = Frauenfelder p. 164, PDF 182) — the sum rule: mean energy transfer = free recoil energy:**
> "The sum rule (7) says that the average energy transferred to the lattice is just the energy which the individual nucleus would have if it recoiled freely. 2 Note that the Mossbauer transitions in which no energy is transferred to the lattice [E(n f ) = E(rii)] do not contribute to the sum rule. Thus if we want an appreciable probability that there be no energy transfer to the lattice the sum rule requires an appreciable probability for an energy transfer which is greater than that which a freely recoiling nucleus would receive* We will tend to get an increased Mossbauer effect when the nucleus can transfer energy to high frequency modes; i.e., in a crystal with a high Debye temperature."

[Eq. (7), p. 334 (OCR garbled): Σ_f [E(n_f) − E(n_i)] |⟨n_f|exp(iK·X_L)|n_i⟩|² = (ħK)²/2M, from the double commutator (6b) "{[H,exp(iK-X L )], exp(-iK-X L )} = -(hK) /M".]

**Q3.5 (p. 336 = Frauenfelder p. 165, PDF 183) — Eq. (15), zero-phonon probability, harmonic crystal (IMAGE-VERIFIED), and footnote 3 on the mass:**
> "P({n s \,{ns}) « exp E {~(2n + l)[(^) /2MMfll) 2 s (15) s neglecting the higher order terms."
> "3 The mass M is the mass of the nucleus emitting the 7-ray. This relation is valid even if the crystal consists of different types of atoms having different atomic masses."

[Image-verified reading of Eq. (15): P({n_s},{n_s}) ≈ exp Σ_s {−(2n_s + 1)[(ħK)²/2Mħω_s] a²_Ls}, where a_Ls are the normal-mode expansion coefficients of the emitting nucleus's coordinate, e_K·X_L = Σ_s a_Ls ξ_s (Eq. (8)) with Σ_s a²_Ls = 1 (Eq. (9)). Since ⟨ξ_s²⟩ = (n_s+½)ħ/Mω_s, this is exactly exp(−K²⟨(e_K·X_L)²⟩) = exp(−k²⟨x²⟩). Footnote 3 is exact: the mass in the exponent is the NUCLEAR mass, not the crystal's; the crystal's mass enters only through the (negligible) translational recoil of Q3.1.]

**Q3.6 (p. 337 = Frauenfelder p. 166, PDF 184) — interpretation; Debye-model limit (17a,b):**
> "The factor (%K) /2Mho) is just the ratio of the free recoil energy to the energy of the sth lattice vibration normal mode. If the lattice is in its lowest state (at 0°K), every n s is zero and the exponent in (15) is just the ratio of the free recoil energy to some average lattice vibration energy ho) Av denned by -1 (/kd A v) = z2 als/hus (16) [...] We see that the probability of an effect (15) decreases very rapidly if the free recoil energy increases above this average lattice energy."
> "The results (15) and (16) are general in that they apply to any crystal in which the forces are harmonic. The particular case of the Debye model has been considered by Visscher (5). We can get his result by setting a Ls = constant and taking a density of lattice modes which is proportional to w s . For this case = %(fta> max = % /C0. (17a) Thus P({n },K}) Deby e = exp s r=o° - y2 (hK) /2Mke 2 { } (17b)"

[OCR: "(%K) /2Mho)" = (ħK)²/2Mħω_s; "(ħω_Av)⁻¹ = Σ_s a²_Ls/ħω_s (16)"; (17a) ħω_Av(Debye) = (2/3)ħω_max = (2/3)kθ; (17b) P_Debye(T=0) = exp{−(3/2)(ħK)²/2Mkθ} — "y2" is OCR for 3/2 (consistent with Frauenfelder Eq. (33), Q4.6).]

---

## Item 4 — H. Frauenfelder, *The Mössbauer Effect* (W. A. Benjamin, 1962) — OBTAINED (full text)

**File:** `frauenfelder_1962_mossbauer_effect_archive.pdf` (archive.org `mssbauereffec00frau`, University of Florida copy, public download, no lending restriction; the two `internetarchivebooks` copies `mssbauereffect00frau` and `bwb_S0-BXA-031` ARE lending-restricted and were not used). Body printed page p = PDF page p + 18.
**Bibliographic line:** Hans Frauenfelder, *The Mössbauer Effect: A Review — with a Collection of Reprints* (Frontiers in Physics, ed. D. Pines), W. A. Benjamin, Inc., New York, 1962.

**Does it say the LATTICE/crystal takes the recoil?** YES, in the most explicit textbook form: "The momentum is unchanged, but it is eventually taken up by the solid as a whole" with the argument that neither the single nucleus nor the phonons can carry it, "The momentum hence must go into translational motion of the entire crystal" (pp. 20–21); "the entire crystal must be considered as the quantum mechanical system in which the decay occurs" (p. 23). Gives f = exp(−⟨x²⟩/ƛ²) classically (Eq. (30), p. 19) and quantum-mechanically f = |⟨L_i|e^{ik·X}|L_i⟩|² (Eq. (49), p. 30) → f = exp(−⟨L_i|X_k²|L_i⟩/ƛ²) (Eq. (56), p. 32, ƛ = λ/2π = 1/k, i.e. f = exp(−k²⟨x_k²⟩)), Einstein f = exp(−R/ħω_E) (Eq. (51)), Debye T=0 f = exp(−3R/2kθ_D) (Eq. (33)); names it "Lamb-Mössbauer factor" (p. 31).

**Q4.1 (p. 3, PDF 21) — recoil energy, Eqs. (1), (2), (1'):**
> "Consider a free atomic or nuclear system, of mass M, with two levels A and B, separated by an energy E r If the system decays from B to A by emission of a photon of energy E , momentum conservation demands that the momentum p of the photon and the momentum P of the recoiling system be equal and opposite. The recoiling system hence receives an energy R, given by 2 P2 p 2M 2M Ey 2Mc (1) 2 [...] The recoil energy is thus very small compared to the gamma- ray energy. Energy conservation connects E E and R: Er = Ey + R (2) Since R is very small compared to Ey, and since, as will be obvious later, one needs to know R only to moderate accuracy, Ey can be replaced by the transition energy E r in (l): R = E 2 /2Mc 2 (10"

[Reading: R = P²/2M = p²/2M = E_γ²/2Mc² (1); E_r = E_γ + R (2); R = E_r²/2Mc² (1').]

**Q4.2 (p. 19, PDF 37) — classical result, Eq. (30):**
> "Usually one introduces the mean- square deviation of the vibrating atom from its equilibrium position by the definition <x2 > = (1/2)2 x2m . (29) m and writes instead of (28) lnf e- -<x2 >/X 2 This equation is exact in the limit N— *> (Van Kranendonk 1961), so that the final result can be written i = exp(-<x2 >/*2 ) (30) [...] 2. Equation (30) allows a simple physical interpretation. The continuously emitted electromagnetic wave comes from a region of linear dimensions <x2 >. If this linear dimension increases beyond the wavelength fr= A/27T, pieces of the wave train emitted from different points in this region interfere destructively, and the fraction f of photons emitted without energy loss decreases rapidly."

[Reading: ⟨x²⟩ = ½Σ_m x_m² (29); f = exp(−⟨x²⟩/ƛ²) (30), ƛ = λ/2π; i.e. f = exp(−k²⟨x²⟩).]

**Q4.3 (pp. 20–21, PDF 38–39) — Sec. 2-41 Momentum Conservation: the solid as a whole takes the momentum:**
> "Assume that the nucleus of an atom which is imbedded in a solid decays by gamma emission. If free, the nucleus would receive a recoil momentum p and a recoil energy R, given by (1). How does the binding of the atom in the solid affect recoil momentum and recoil energy ? The answer to the first question is straightforward: The momentum is unchanged, but it is eventually taken up by the solid as a whole. In order to justify this statement, consider the two other possibilities, trans lational motion of the nucleus and phonons (lattice vibrations). The momentum cannot go into translational motion of the nucleus. The energy required to leave a lattice site is at least of the order of 10 ev; the energy available, however, never exceeds a few tenths of an ev. (Even if the recoil were larger, the nucleus would finally come to rest and transfer its momentum to the solid.) Lattice vibrations, on the other hand, cannot take up momentum. They can be represented as standing waves or as the sum of running waves. To each wave with its momentum pointing in one direction will be a corresponding one with its momentum pointing in the opposite direction. The expectation value of the momentum for lattice vibrations vanishes. [...] The momentum hence must go into translational motion of the entire crystal. If the crystal is glued to a larger body, for instance the earth, this larger body takes up the momentum. [...] (Incidentally, the nearly complete separation of the energy transfer from the momentum transfer which occurs in the Mossbauer effect appears also in many classical problems, such as when one shoots a bullet into a very heavy pendulum.)"

**Q4.4 (p. 21, PDF 39) — Sec. 2-42 Energy Conservation:**
> "The discussion of the energy conservation is more complicated, since the transition energy can be shared among the gamma ray, the individual atom, lattice vibrations, and the solid as a whole. Two of these four parts can be dispensed with quickly. The individual atom does not leave its lattice site (see Sec. 2-41) and hence cannot acquire translational energy. The energy that goes into motion of the entire solid is extremely small and will be neglected. The transition energy, for all practical purposes, is thus shared between the gamma ray and the phonons. A Mossbauer transition occurs if the state of the lattice remains unchanged, and the gamma ray gets the entire transition energy."

**Q4.5 (pp. 21–22, PDF 39–40) — Einstein solid: condition R small vs. phonon energy; Eq. (31):**
> "For the Einstein solid, the problem is very simple. The smallest amount of energy that can be given to the solid is equal to Eg =-ncoE = keg- ^ tne ener SY R U- e »> the recoil energy of zfree nucleus) is small compared to this excitation energy, the probability of emission of a phonon will be small, the lattice will not be excited and the gamma ray will escape with the full transition energy. The calculation (Sec. 2-5) shows indeed that the probability f for a transition without energy loss is given by f = exp(-R/k0 E ) (31)"

[OCR garble: "E_E = ħω_E = kθ_E. If the energy R (i.e., the recoil energy of a free nucleus) is small compared to this excitation energy, ..."; f = exp(−R/kθ_E) (31).]

**Q4.6 (p. 23, PDF 41) — Debye solid Eq. (33) and "the entire crystal must be considered as the quantum mechanical system":**
> "The proper calculation (see Reprints on theory) justifies these considerations and shows that the fraction f of transitions without change in the lattice states is given by an expression similar to (31), but with E replaced by (2/3)6d: f = exp(- 3R/2k0 D ) (33) Equations (31) and (33) are valid only at zero absolute temperature, where all lattice oscillators are in their ground state. [...] Even though the energies characteristic for the solid are much smaller than the nuclear transition energy, and the nuclear decay occurs in one nucleus only, the entire crystal must be considered as the quantum mechanical system in which the decay occurs. Any statement according to which one can separate the decay into a first step, in which the nucleus decays, and a second step, in which the recoil energy is, or is not, given to the solid, is misleading. The process is indivisible and if by a measurement one separates the two steps, the Mossbauer effect is destroyed."

[Reading: θ_E replaced by (2/3)θ_D; f = exp(−3R/2kθ_D) (33).]

**Q4.7 (p. 30, PDF 48) — quantum result Eq. (49) and Einstein check Eq. (51):**
> "f=|<L i |e ik,X |L i >| 2 (49) Equation (49) has been the starting point for most calculations of the fraction f of gamma rays emitted or absorbed without energy loss. [...] Inserting this wave function into (49) and using the fact that one is dealing with a one-dimensional problem, i.e., that k-X kX, yields after integration f = exp (--h2 k2/2Mfta>) = exp (-R/nu) E ) (51) This result agrees with (31), which was quoted earlier without proof."

[Reading: f = |⟨L_i|e^{ik·X}|L_i⟩|² (49); f = exp(−ħ²k²/2Mħω) = exp(−R/ħω_E) (51). Note Fig. 2-3 caption p. 28: "The origin is fixed at the c.m. of the entire crystal."]

**Q4.8 (pp. 31–32, PDF 49–50) — Lamb–Mössbauer factor named; Eqs. (55), (56) (p. 32 IMAGE-VERIFIED):**
> "This Debye-Waller factor exp(-2W) has many similarities with the Lamb-Mdssbauer factor f it is interesting to compare these and also note the differences. [...] The essential similarity lies in the appearance of the mean-square deviation of the radiating or scattering atoms from its equilibrium position. For crystals with harmonic lattice forces, it can be shown that the expression (49) can be transformed to f = exp(-<Li|(k.X) 2 |Li») (55) or"
> (p. 32) "f = exp(-<L i |Xk|L i >/* 2 ) (56) Here X^ is the component of the coordinate vector X in the direction of the emitted photon. Equation (56) is derived in Petzold's paper (Petzold 1961) and the steps leading from (49) to (55) can be found in a paper by Van Hove. 32 33 Incidentally, (56) agrees with the classically derived Eq. (30) and the remarks made there apply also to (56)."

[Image-verified: (56) reads f = exp(−⟨L_i|X_k²|L_i⟩/ƛ²), X_k the component of X along the photon direction, ƛ = λ/2π — i.e. f = exp(−k²⟨x_k²⟩), the Lamb–Mössbauer factor.]

**Q4.9 (p. 84, PDF 102) — which mass: host-lattice atoms, not the impurity nucleus (model statement):**
> "The mean- square deviation <X 2 > of the impurity atom is in a first approximation the same as that of the normal lattice atoms. In the Debye approximation, the Lamb-Mossbauer factor f is thus given by Eq. (53), with R = E 2/2mc 2 If this description is correct, then the fraction f should be determined by the mass m of the atoms in the host lattice, and not by the mass M of the impurity atom. This conclusion has, however, not yet been substantiated by experiments."

---

## Item 5 — SECONDARY (open access): Stepanenko et al., arXiv:2404.18683 / Sci. Adv. 11, eads3406 (2025) — OBTAINED

**File:** `arxiv_2404.18683_stepanenko2024_Os187_mossbauer.pdf` (arXiv, 24 pp.).
**Bibliographic line:** I. Stepanenko, Z. Huang, L. Ungur, D. Bessas, A. Chumakov, I. Sergueev, G. E. Büchel, A. A. Al-Kahtani, L. F. Chibotaru, J. Telser, V. B. Arion, "New tool for extraction of ¹⁸⁷Os Mössbauer parameters with biologically relevant detection sensitivity", Science Advances 11, eads3406 (2025), DOI 10.1126/sciadv.ads3406; arXiv:2404.18683v2. (Chumakov/Sergueev = ESRF/DESY nuclear-resonance beamline authors.)

**Does it say the LATTICE/crystal takes the recoil?** NO explicit "crystal as a whole" sentence — it is a modern applications paper, cited here only for the formula pair f_LM and ⟨u²⟩ = −ln f_LM/k² (i.e. f = exp(−k²⟨u²⟩)) and for naming f_LM "the probability of the recoilless absorption". Flag: SECONDARY, formula only.

**Q5.1 (arXiv PDF p. 8) — f_LM from the phonon DOS with E_R the recoil energy of the free nucleus:**
> "Firstly, the probability of the recoilless absorption, known as Lamb-Mӧssbauer factor, can be extracted using Equation (1), 1 + e− E dE f LM = exp − ER g ( E ) − E , (1) 1− e E where ER = 0.274 meV, is the recoil energy for an 187Os isolated nucleus and β = 1/kBT, where kB is the Boltzmann constant and T is the temperature at which g(E) is measured. The calculated fLM for Os in K2[187OsO2(OH)4] is 0.55(1) at room temperature."

[Layout-extraction garble of Eq. (1): f_LM = exp[−E_R ∫ g(E) (1+e^{−βE})/(E(1−e^{−βE})) dE].]

**Q5.2 (arXiv PDF p. 8) — mean-square displacement ⟨u²⟩ = −ln f_LM / k²:**
> "From the Lamb-Mӧssbauer factor, the purely incoherent mean-square atomic displacement parameter, u2Os, is − ln ( f LM ) u 2 Os = , (2), k2 where k = 4.959 Å−1 is the wave number of the resonant photons. The Os mean square atomic displacement in K2[187OsO2(OH)4] at room temperature is 243(1) pm2."

[Reading: u²_Os = −ln(f_LM)/k² (2) ⇔ f_LM = exp(−k²⟨u²⟩).]

**Q5.3 (arXiv PDF p. 12):**
> "transition and the large nuclear mass of 187Os resulted in a high recoil free fraction, fLM = 0.95(1),"

Other open-access candidates checked and NOT retained (no explicit whole-crystal sentence, or formulas only as images): Dauphas et al., SciPhon, J. Synchrotron Rad. 25, 1581 (2018) (PMC6140397; XML obtained, PDF 403, equations embedded as images — text says "The Lamb–Mössbauer factor is the ratio of recoil-free to total nuclear resonant absorption" and "The Lamb–Mössbauer factor is calculated from the mean square displacement through [equation (37)]"); Wang et al., Crystals 11, 909 (2021) (PMC9109880; NRVS review, no recoil-to-crystal statement). arXiv API searches are metadata-only, so phrase searches for "crystal as a whole" return nothing there.

---

## Summary table — who says the LATTICE/CRYSTAL takes the recoil

| source | whole-crystal statement | f formula | E_R condition |
|---|---|---|---|
| Mössbauer Nobel 1961 | YES: momentum "always taken up by the crystal as a whole" (p. 592); energy to crystal, translational part negligible by "enormous mass of the crystal as a whole" (pp. 590–591) | not written; "Debye-Waller factor" (p. 594), Fig. 6 (p. 595) | E₀²/2Mc² < kθ, Eq. (3) p. 594; ≲150 keV |
| Mössbauer Z. Phys. 1958 | YES (energy): "muß der Kristall die Rückstoßenergie als innere Energie aufnehmen", quantized, via lattice vibrations (ZP p. 126) | recoil-free line = exp[g_∞(T)] weight, Eq. (17) (transl. p. 125) | R vs. ħω_g (ZP pp. 126–127); R = 0.046 eV, kΘ = 0.025 eV for Ir¹⁹¹ |
| Mössbauer Naturwiss. 1958 (transl.) | YES: "the solid as a whole can take up the recoil momentum" (Frauenfelder p. 127) | — | — |
| Lipkin 1960 | YES: "The recoil momentum is taken by the crystal as a whole, with negligible energy transfer" (p. 332); whole-lattice matrix element (p. 333) | Eq. (15) p. 336: exp Σ_s{−(2n_s+1)(ħK)²a²_Ls/2Mħω_s}; M = nuclear mass (fn. 3) | sum rule: mean transfer = (ħK)²/2M (p. 335); effect when free recoil ≲ ħω_Av (p. 337) |
| Frauenfelder 1962 | YES: "taken up by the solid as a whole", "translational motion of the entire crystal" (pp. 20–21); "entire crystal must be considered as the quantum mechanical system" (p. 23) | Eq. (30) p. 19, (49) p. 30, (55) p. 31, (56) p. 32: f = exp(−⟨X_k²⟩/ƛ²); Einstein (31)/(51); Debye (33) | R small vs. ħω_E (p. 21–22); R = E²/2Mc² (p. 3) |
| Stepanenko 2025 (secondary) | no | f_LM Eq. (1); ⟨u²⟩ = −ln f_LM/k² Eq. (2) (p. 8) | E_R = free-nucleus recoil energy (p. 8) |
