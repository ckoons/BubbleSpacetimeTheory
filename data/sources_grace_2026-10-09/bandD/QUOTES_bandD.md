# Band D primary-source quotes — retrieved 2026-10-09

Directory: `data/sources_grace_2026-10-09/bandD/` (untrusted downloaded data; nothing here is executed).
Each PDF has two sibling extractions: `<name>.txt` (`pdftotext -layout`) and `<name>_raw.txt` (`pdftotext`, reading order; two-column papers read correctly here). Quotes below are copied verbatim from the `_raw.txt` files, with whitespace collapsed only. Where the PDF font encoding mangles a glyph, the mangled form is kept inside the quote and decoded in a note outside it.

---

## 1. Abdo et al. 2009 (Fermi LAT/GBM), GRB 090510 Lorentz-invariance limit

**File obtained:** `abdo2009_GRB090510_Nature.pdf` (4 pp., Nature reprint, doi:10.1038/nature08574; from https://www.openu.ac.il/personal_sites/yoni-granot/papers/GRB090510_Nature.pdf). Extractions: `abdo2009_GRB090510_Nature.txt`, `abdo2009_GRB090510_Nature_raw.txt`.

**Bibliographic line:** A. A. Abdo et al. (Fermi LAT and Fermi GBM Collaborations), "A limit on the variation of the speed of light arising from quantum gravity effects", Nature 462, 331–334 (19 November 2009), doi:10.1038/nature08574; arXiv:0908.1832.

**Glyph key for this extraction (font substitution in the PDF):** `5` = "=", `3` = "×", `6` = "±", `2` = "−" (minus, incl. exponents, e.g. `GeV21` = GeV⁻¹, `10233` = 10⁻³³), `,` = "<", `.` = ">", `#` = "≤", `;` = "≡", `j` = "|", `jDt/DEj` = |Δt/ΔE|, `j1` = ξ₁, `MQG,1` = M_QG,1, `EPlanck`/`MPlanck`/`lPlanck` = E_Planck / M_Planck / l_Planck, `tem`/`tstart`/`th` = t_em / t_start / t_h.

**Quote A1 (abstract, p. 331):**
> Here we report the detection of emission up to 31 GeV from the distant and short GRB 090510. We find no evidence for the violation of Lorentz invariance, and place a lower limit of 1.2EPlanck on the scale of a linear energy dependence (or an inverse wavelength dependence), subject to reasonable assumptions about the emission (equivalently we have an upper limit of lPlanck/1.2 on the length scale of the effect). Our results disfavour quantum-gravity theories3,6,7 in which the quantum nature of space–time on a very small scale linearly alters the speed of light.

**Quote A2 (emission assumption and the weaker "limit b" number, pp. 332–333; the sentence runs across the page break, and the marker [...] stands for the p. 332 footer and the Table 1 block that the extraction interleaves there):**
> No high-energy photon has ever been detected before the onset of the low-energy emission in a GRB. Therefore, it is highly unlikely that the 31-GeV photon was emitted before the observed onset of [...] GRB 090510. This implies j1 . 1.19 (limit b in Table 1), which we consider our most conservative limit with this method. While the underlying assumption on tem is very reasonable, it is still an assumption; if for some reason tem were to be before tstart, this limit would be weakened by a factor of (th 2 tem)/(th 2 tstart).

Decoded: ξ₁ > 1.19 (limit b); weakening factor (t_h − t_em)/(t_h − t_start).

**Quote A3 (headline conservative limit, p. 333):**
> Our most secure and conservative new limit, j1 . 1.2, is much stronger than the previous best limit of this kind (j1 . 0.1 from GRB080916C; ref. 18) and fundamentally more meaningful. Given that in most quantum gravity scenarios MQG,n # MPlanck, even our most conservative limits greatly reduce the parameter space for n 5 1 models19,20. Our other limits, and especially our least conservative limit of j1 . 102, make such theories highly implausible

Decoded: ξ₁ > 1.2 (most secure/conservative); ξ₁ > 0.1 (GRB 080916C); M_QG,n ≤ M_Planck; n = 1; least conservative ξ₁ > 102.

**Supplementary verbatim lines (same file):**
- p. 331 (limit a, DisCan method): > We obtain a robust upper limit of jDt/ DEj , 30 ms GeV21 (at the 99% confidence level) on possible linear energy dispersion of either sign, or j1 ; MQG,1/MPlanck . 1.22 (limit a in Table 1).
  Decoded: |Δt/ΔE| < 30 ms GeV⁻¹ (99% CL); ξ₁ ≡ M_QG,1/M_Planck > 1.22.
- p. 333 (text): > We stress here that our most conservative limits, a and b in Table 1, rely on very different and largely independent analysis, yet still give a very similar limit, of j1 . 1.2.
- p. 333 (Table 1 caption): > Limit b relies on the 31-GeV photon, and conservatively uses the 1s lower limit on its energy (28.0 GeV) and the 1s lower limit on the redshift (z 5 0.900). Limit b assumes that the 31-GeV photon was not emitted before the onset of any emission detected by Fermi, so that tstart is set to the onset of the first small isolated GRB spike, 30 ms before the GBM trigger time.
  Decoded: 1σ lower limits; z = 0.900.

Summary of numbers as printed: limit a ξ₁ > 1.22 (dispersion fit, 99% CL); limit b ξ₁ > 1.19 (31-GeV photon emitted after first GRB spike); headline "most secure and conservative" ξ₁ > 1.2; less secure association limits ξ₁ > 1.33 and ξ₁ > 102 (p. 333).

---

## 2. Rideout & Sorkin 2000, classical sequential growth dynamics for causal sets

**File obtained:** `rideout_sorkin_grqc9904062.pdf` (28 pp., arXiv:gr-qc/9904062v3, 26 Jun 2004, from https://arxiv.org/pdf/gr-qc/9904062). Extractions: `rideout_sorkin_grqc9904062.txt`, `rideout_sorkin_grqc9904062_raw.txt`. Page numbers below are the arXiv v3 printed page numbers (equal to PDF page numbers), not the PRD pagination.

**Bibliographic line:** D. P. Rideout and R. D. Sorkin, "A classical sequential growth dynamics for causal sets", Phys. Rev. D 61, 024002 (2000), arXiv:gr-qc/9904062.

Both conditions are stated in Section 3, "Physical requirements on the dynamics" (pp. 9–12), as the second and third of four conditions (internal temporality; discrete general covariance; Bell causality; Markov sum rule).

**Quote R1 (discrete general covariance, Section 3, p. 9):**
> The condition of discrete general covariance As we have been emphasizing, the “external time” in which the causal set grows (equivalently the induced labeling of the resulting poset) is not meant to carry any physical information. We interpret this in the present context as being the condition that the net probability of forming any particular n-element causet C is independent of the order of birth we attribute to its elements. Thus, if γ is any path through the poset P of finite causal sets that originates at the empty causet and terminates at C, then the product of the transition probabilities along the links of γ must be the same as for any other path arriving at C. (So general covariance in this setting is a type of path independence).

**Quote R2 (Bell causality, physical statement, Section 3, p. 10):**
> The physical idea behind our condition is that events occurring in some part of a causal set C should be influenced only by the portion of C lying to their past. In this way, the order relation constituting C will be causal in the dynamical sense, and not only in name. In terms of our sequential growth dynamics, we make this precise as the requirement that the ratio of the transition probabilities leading to two possible children of a given causet depend only on the triad consisting of the two corresponding precursor sets and their union.

**Quote R3 (Bell causality, Eq. (2), Section 3, pp. 10–11; the displayed fraction is extracted as stacked lines, and the marker [...] stands for footnotes 6–7 and the page break that the extraction interleaves between "transition" and "C → C1"):**
> Thus, let C → C1 designate a transition from C ∈ Cn to C1 ∈ Cn+1 , and similarly for C → C2 . Then, the Bell causality condition can be expressed as the equality of two ratios7 : prob(C → C1 ) prob(B → B1 ) = prob(C → C2 ) prob(B → B2 ) (2) where B ∈ Cm , m ≤ n, is the union of the precursor set of C → C1 with the precursor set of C → C2 , B1 ∈ Cm+1 is B with an element added in the same manner as in the transition [...] C → C1 , and B2 ∈ Cm+1 is B with an element added in the same manner as in the transition C → C2 .8 (Notice that if the union of the precursor sets is the entire parent causet, then the Bell causality condition reduces to a trivial identity.)

Eq. (2) as typeset: prob(C→C1)/prob(C→C2) = prob(B→B1)/prob(B→B2).

**Supplementary verbatim lines (same file):**
- p. 3 (Introduction, the label-gauge statement): > The relevant notion of gauge invariance (which we will call “discrete general covariance”) is then captured by the statement that the labels carry no physical meaning.
- p. 9 (kinematics): > Let us emphasize once more that the labels 0, 1, 2, etc. are not supposed to be physically significant. Rather, the “external time” that they record is just a way to conceptualize the process, and any two birth sequences related to each other by a permutation of their labels are to be regarded as physically identical.
- p. 11 (spectator form of Bell causality): > Bell causality says that the spectators can be deleted without affecting relative probabilities.

---

## 3. Hestenes 1990, Zitterbewegung interpretation of quantum mechanics

**File obtained:** `hestenes1990_ZBW_I_QM.pdf` (17 pp., author's reprint from https://davidhestenes.net/geocalc/pdf/ZBW_I_QM.pdf; header line reads "In: Found. Physics., Vol. 20, No. 10, (1990) 1213–1232."). Extractions: `hestenes1990_ZBW_I_QM.txt`, `hestenes1990_ZBW_I_QM_raw.txt`. Page numbers below are the reprint's own printed pages 1–17 (the journal pagination 1213–1232 is not reproduced in this file).

**Bibliographic line:** D. Hestenes, "The Zitterbewegung Interpretation of Quantum Mechanics", Found. Phys. 20 (10), 1213–1232 (1990).

**Quote H1 (abstract, reprint p. 1):**
> Abstract. The zitterbewegung is a local circulatory motion of the electron presumed to be the basis of the electron spin and magnetic moment. A reformulation of the Dirac theory shows that the zitterbewegung need not be attributed to interference between positive and negative energy states as originally proposed by Schroedinger. Rather, it provides a physical interpretation for the complex phase factor in the Dirac wave function generally. Moreover, it extends to a coherent physical interpretation of the entire Dirac theory, and it implies a zitterbewegung interpretation for the Schroedinger theory as well.

**Quote H2 (phase factor as the zbw rotation, reprint p. 12, Section 5):**
> The key ingredients of this interpretation are the energy momentum operators pµ deﬁned by (35) and the complex phase factor in the wave function. The imaginary unit i in both is a bivector for a plane in space, the “spin plane” in which the zbw circulation takes place. The phase factor literally represents a physical rotation, a zbw rotation. Operating on the phase factor, the pµ , computes the rotation rates of the phase in time and space directions, identifying them with the energy and momentum.

**Quote H3 (zbw frequency and radius, reprint p. 1, Introduction; equation numbers (1), (2) extracted inline):**
> In analyzing free-particle wave packet solutions of the Dirac equation, Schroedinger noted the existence of “interference” between positive and negative energy states oscillating with circular frequency ω0 = 2mc2 /h̄ = 1.6 × 1021 s−1 (1) He interpreted this as a ﬂuctuation in the position of the electron with radius λ̄0 = c/ω0 = h̄/2mc = 1.9 × 10−13 m (2)

Typeset: ω₀ = 2mc²/ħ = 1.6 × 10²¹ s⁻¹; λ̄₀ = c/ω₀ = ħ/2mc = 1.9 × 10⁻¹³ m.

**Supplementary verbatim lines (same file):**
- reprint p. 2 (Introduction): > I shall show that the complex phase factor in the electron wave function can be associated directly with the zbw. I call this the zbw interpretation of quantum mechanics.
- reprint p. 11 (after Eq. (64)): > where ω0 = | Ω | is the zbw frequency with the value given by (1). Thus e1 and e2 rotate with the zbw frequency in the plane of the spin S.
- reprint p. 11 (after Eq. (69)): > The diameter of the helix is the electron Compton wavelength 2λ0 = 2c/ω0 = h̄/mc, as suggested by Eq. (2).
- reprint p. 15 (Eq. (95)): > κ1 = κ2 = ω0 = 2mc2 /h̄

---

## Tally
- Files: 3 PDFs obtained (0 not obtained), 6 extracted .txt files, this QUOTES file.
- Primary quotes: 9 (3 per source). Supplementary verbatim lines: 10 (Abdo 3, Rideout–Sorkin 3, Hestenes 4).
