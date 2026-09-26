# SHELL PINS: draft (primary-source pins)

Written 2026-09-26 (Sat, 10:46 EDT by `date`). All files are in this directory. Checksums: `SHA256SUMS.txt`.
Rule followed: no pin comes from a search snippet or summary. Web search was used only to *locate* URLs. Every pin below is a quote from a file saved here, given as file:line.

Source classes:
- **PRIMARY**: the paper itself (arXiv PDF, publisher archive PDF, or an author-hosted reprint of the journal pages).
- **METADATA-ONLY**: the publisher's Crossref record, fetched from `https://api.crossref.org/works/<DOI>`. `*.json` is the raw API response; `*.pretty.json` is the same content re-indented, and every line number below refers to the pretty version.
- **SECONDARY**: a later source that quotes or describes the paper.

OCR caveat: the Kleinert-site reprints, the Kleinert 1968 lectures and the Malkin–Man'ko PDF are page scans with no text layer. Their `.OCR.txt` files come from tesseract at 300–400 dpi. The prose reads cleanly; formulas are garbled. Symbols quoted below are copied as OCR printed them, with any correction shown in [brackets].

---

## 1. Fock 1935

**Citation.** V. Fock, "Zur Theorie des Wasserstoffatoms", Z. Physik 98 (1935) 145–154.
**DOI.** 10.1007/BF01336904. Verified; Crossref stores it lowercase.
**Opened.** METADATA-ONLY for the paper, which is behind the Springer paywall; no open copy was found. The content pins are SECONDARY and come from three independent sources.

Metadata (`crossref_10_1007_BF01336904.pretty.json`):
- :54 `"DOI": "10.1007/bf01336904"`
- :71 `"Zur Theorie des Wasserstoffatoms"`
- :77–78 `"given": "V."`, `"family": "Fock"`
- :91 `"Zeitschrift f�r Physik"` (the replacement character is in Crossref's own record)
- :74 `"volume": "98"`, :20 `"issue": "3-4"`, :67 `"page": "145-154"`, :140–143 issued 1935 (the raw JSON has date-parts [[1935, 3]])

Content. SECONDARY (a) is Malkin & Man'ko 1965, which cites Fock as their ref [1] (`malkin_manko_1965_jetpl_2_146.OCR.txt:149` "[1] V. Fock, Z. Physik 98, 145 (1935)."):
- :25–27 "Fock [2] and Bargmann (2] have shown that in a Coulomb potential the wave functions belonging to one level realize a finite-dimensional representation of a compact group O4" [OCR: "Fock [1] and Bargmann [2]"]
- :51–62 "As shown by Fock[1] the eigenfunctions of the discrete spectrum of the hydrogen atom, in the momentum representation and in the variables ξ_i (i = 1,...4) ... are homogeneous harmonic polynomials of the variables ξ of degree N - 1 (N is the principal quantum number)"

SECONDARY (b) is Kleinert, "Group Dynamics of the Hydrogen Atom", 1968; see item 2 for the full citation. Fock is his reference at `kleinert_1968_group_dynamics_H_atom.OCR.txt:2450` "V. Fock, Z. Phys. 98, 145 (1935).":
- :705–707 "Fock observed that the n-dependent stereographic projection of the wave functions ψ_nlm(p) in momentum space onto the surface of a sphere in four-dimension with unit radius defined by [Eq. IV.32]"
- :727 "transforms the Schrödinger equation ..." and :738 (printed p. 442) "into the integral equation for four-dimensional spherical harmonics"

SECONDARY (c) is G. J. Maclay, "Dynamical Symmetries of the H Atom ... SO(4) to SO(4,2)", arXiv:2305.18229 (Symmetry, 2020/2023), `arxiv_2305_18229.txt`. This is the only open source here that states the n² count explicitly:
- :309–320 "in 1935, the Russian physicist Vladimir Fock published a major article in Zeitshrift fur Physik ... did a stereographic projection onto a unit sphere, and showed that the bound state momentum space wave functions were spherical harmonics in four dimensions. He stated that this showed that rotations in four dimensions corresponded to the symmetry of the degenerate bound state energy levels in momentum space, realizing the group SO(4) ... By counting the number of four-dimensional spherical harmonics Ynlm in momentum space (... l = n − 1, n − 2, ..0) he determined that the degree of degeneracy for the energy level characterized by the principal quantum number n was n2" [n²]
- :397–399 caveat: "the stereographic projection depends on the energy, so the statements for a SO(4) subgroup are valid only in a subspace of constant energy."
- :670 "of SO(4) for an energy level En has dimension n2 ."

**Status.** Metadata is pinned. The content claim (momentum space, stereographic projection onto S³, 4D spherical harmonics, SO(4), n²) is pinned SECONDARY. The pin from Fock's own text is **OWED**; it needs Springer access. Bander & Itzykson 1966 have Crossref metadata only (`crossref_10_1103_RevModPhys_38_330.pretty.json`:46,63,59 = 10.1103/revmodphys.38.330, "Group Theory and the Hydrogen Atom (I)", 330-345; `..._38_346.pretty.json`: (II), 346-358). Their text is paywalled and was not opened.

---

## 2. Barut & Kleinert 1967

**Opened.** PRIMARY for all three papers: author-hosted scans of the Phys. Rev. reprints, taken from Kleinert's publication list (`kleinert_homepage_hagenkleinert_de.html`, entries [9], [10], [12] → `documents/articles/9.pdf`, `10.pdf`, `12.pdf`). METADATA from Crossref for each. The APS landing pages returned a Cloudflare challenge and were not saved.

**2a.** A. O. Barut and H. Kleinert, "Transition Probabilities of the Hydrogen Atom from Noncompact Dynamical Groups", Phys. Rev. 156 (1967) 1541–1545. **DOI 10.1103/PhysRev.156.1541**
- Crossref `crossref_10_1103_PhysRev_156_1541.pretty.json`: :46 DOI, :63 title, :66 vol 156, :20 issue 5, :59 "1541-1545"
- `kleinert_site_article_9.OCR.txt`:2 "Reprinted from The Physical Review, Vol. 156, No. 5, 1541-1545, 25 April 1967"
- :12–14 (abstract) "an explicit irreducible representation of the Lie algebra O(4,2) has been found on the space of bound-state wave functions. This representation remains irreducible when restricting to the subalgebra O(4,1)."
- :36–41 "1. The larger group O(4,2) is shown to be a dynamical group of the H atom by explicit construction of a matrix representation on the space of bound-state wave function. This representation remains irreducible when restricting the group to the subgroup O(4,1)"
- :72–76 (footnote 3, on priority) "I. A. Malkin and V. I. Man'ko, JETP Pis'ma v Redaktsiyu 2, 230 (1966) [English transl.: JETP Letters 2, 146 (1966)] have noticed the use of O(4,2) for the H spectrum in Fock coordinates in analogy to the Klein-Gordon equation with zero mass. They have not discussed the problem of transition probabilities."

**2b.** A. O. Barut and H. Kleinert, "Current Operators and Majorana Equation for the Hydrogen Atom from Dynamical Groups", Phys. Rev. 157 (1967) 1180–1183. **DOI 10.1103/PhysRev.157.1180**
- Crossref `crossref_10_1103_PhysRev_157_1180.pretty.json`: :46, :63, :66 vol 157, :59 "1180-1183"
- `kleinert_site_article_10.OCR.txt`:2 "Reprinted from The Physical Review, Vol. 157, No. 5, 1180-1183, 25 May 1967"
- **Key pin for the claim of one unitary irreducible representation of the conformal group:** :23–27 "In a recent paper¹ an irreducible unitary representation of the conformal group O(4,2) was constructed on the Hilbert space of bound-state wave functions of the H atom."
- :12–13 (abstract) "the dipole operator in the hydrogen atom is the product of an element in the Lie algebra and of a group element of the conformal group O(4,2)."
- :124–127 "the conformal group contains the whole algebra of observables on the Hilbert space of bound-state wave functions and can thus indeed be called the dynamical group of the H atom."
- :133–135 "The states |nlm) themselves form an irreducible representation of the subgroup O(4,1)"

**2c.** A. O. Barut and H. Kleinert, "Transition Form Factors in the H Atom", Phys. Rev. 160 (1967) 1149–1151. **DOI 10.1103/PhysRev.160.1149**. Relevant because it restates the conformal identification.
- Crossref `crossref_10_1103_PhysRev_160_1149.pretty.json`: :45, :62, :65 vol 160, :58 "1149-1151"
- `kleinert_site_article_12.OCR.txt`:2 "Vol. 160, No. 5, 1149-1151, 25 August 1967"
- :41–42 "the dipole transitions in the H atom can be described in a simple manner by using the dynamical group O(4,2), the conformal group."
- :61–65 (footnote 2) "The relevance of the group O(4,2)~SU(2,2) to the H atom, beyond the minimal dynamical group O(4,1), was also noticed by I. A. Malkin and V. I. Man'ko ... but these authors did not consider dipole operators."

**2d.** H. Kleinert, "Group Dynamics of the Hydrogen Atom", Lectures in Theoretical Physics Vol. X-B (eds. W. E. Brittin and A. O. Barut, Gordon & Breach, N.Y. 1968), pp. 427–482. Journal-free lecture notes, author-hosted as `documents/articles/4.pdf` → `kleinert_1968_group_dynamics_H_atom.pdf`. The citation string is from the site list, `kleinert_homepage_hagenkleinert_de.html`, entry [4]. The volume number "X-B" is **not** in any saved file, so treat it as unpinned.
- OCR :72–76 "a non-compact group O(4,1), whose maximally degenerate representation has a spectrum being in one-to-one correspondence with the hydrogen spectrum ... an extension of this group, O(4,2)"
- :302–304 "the group O(4,1) can be extended unitarily to O(4,2) on the same Hilbert space"
- :1983–1984 "the internal structure of the composite quantum mechanical system of the H-atom can be described completely in terms of simple group operations in the representation space of the non-compact group O(4,2)."
- :2000–2003 (his general scheme, stated for particle-physics use) "There is a (in general non-compact) group G which contains all possible states of the system at rest in a single unitary irreducible representation."

**Honest scope notes (from the sources themselves):**
1. Barut–Kleinert themselves say the whole bound spectrum is *already* a single irreducible representation of the **O(4,1)** subgroup (156:14, 156:40–41, 157:133–135). O(4,2) is needed for the dipole/current operators (156:43–45 "the inclusion of the electromagnetic dipole transition operator leads to O(4,2) as the dynamical group"). Say "one UIR of SO(4,2), which stays irreducible on SO(4,1)", not "SO(4,2) is needed for the single multiplet".
2. Barut–Kleinert write O(4,2); SO(4,2) and the conformal identification O(4,2) ~ SU(2,2) are their wording at 160:62.
3. Maclay, arXiv:2305.18229 :2931–2937, reports that published SO(4,2) hydrogen representations disagree on the fourth Casimir: "all have W2 = 3 ... and W3 = 0 ... however, two authors have representations with W4 = 0 ... and one ... has W4 = −12, compared to our value of -18." Malkin–Man'ko's own value appears at `malkin_manko_1965_jetpl_2_146.OCR.txt`:123 as "C4 = ... = -12". The representation is "the" hydrogen UIR up to realization conventions; do not quote a single W4 without naming its source.

---

## 3. Malkin & Man'ko 1965

**Citation.** I. A. Malkin and V. I. Man'ko, "Symmetry of the Hydrogen Atom", JETP Letters **2** (1965) 146–148 [Pis'ma ZhETF 2, 230]. Submitted 8 July 1965.
**DOI.** None; this volume predates DOIs, and none was found in any saved file.
**Opened.** PRIMARY: the publisher's own archive PDF, `http://jetpletters.ru/ps/1599/article_24507.pdf` → `malkin_manko_1965_jetpl_2_146.pdf`. Its OCR is `malkin_manko_1965_jetpl_2_146.OCR.txt`. METADATA comes from the jetpletters.ru archive pages and from OSTI.

Metadata:
- `jetpl_v2_issue1599_index.html`:120 "VOLUME 2 (1965) | ISSUE 5 CONTENTS"; :216–221 "Malkin I. A., Man'ko V. I., Symmetry of the Hydrogen Atom ... 146 (230)"
- `jetpl_article_24507.html`:236–237 "VOLUME 2 (1965) | ISSUE 5 | PAGE 146"; :247 authors; :268 PDF link
- `osti_4590429.txt`:48–52 "Malkin, I A and Man'ko, V I. "SYMMETRY OF THE HYDROGEN ATOM." JETP Lett. (USSR) (Engl. Transl.), vol. Vol: 2, Sep. 1965." (OSTI ID 4590429)
- OCR :16–20 "SYMMETRY OF THE HYDROGEN ATOM / I. A. Malkin and V. I. Man'ko / Moscow Physico-technical Institute / Submitted 8 July 1965"; the page footers read 146 (:55), 147 (:106), 148 (:162)

**Citation conflict, flagged.** Barut–Kleinert cite this paper as "(1966)" (156 fn3, `kleinert_site_article_9.OCR.txt`:72–73). PR 160 fn2 (`kleinert_site_article_12.OCR.txt`:64–65) says "JETP Letters **3**, 146 (1966)". Maclay (arXiv:2305.18229 :3707) says "Soviet Physics JETP Letters 2,146 (1966)". The publisher archive and OSTI both give **Vol. 2, 1965, issue 5, p. 146**; use that. The "(1966)" is presumably the date of the English translation volume, but that is unverified.

Content (OCR, `malkin_manko_1965_jetpl_2_146.OCR.txt`; the OCR writes "Og"/"Ds"/"Da" for O₆ and D₃):
- :35–38 "The purpose of the present paper is to show that the "symmetry group" of the hydrogen atom is the non-compact group O6, the Lie algebra of which is the algebra D3, and to present a simple construction showing that the functions belonging to the discrete spectrum form a single infinite-dimensional irreducible representation of this algebra."
- :43–50 Their definition of "symmetry group": operators M with [A, M]ψ = 0 on solutions of Aψ = 0, so that "If ψ is a solution, then Mψ is also a solution." In modern terms this is a spectrum-generating (non-invariance) group.
- :67–76 "the 15 operators (4) commute on the solutions of (3) with four-dimensional Laplacian ... The construction of the operators (4) was suggested to the authors by the analogy between Eq. (3) and the Klein-Gordon equation for a particle with zero mass"
- :89 "The noncompact group written out above is the symmetry group of the hydrogen atom in the sense of (1) and (2)."
- :111–118 raising and lowering operators "transform the level N into N+1 and N-1 ... This representation is irreducible"
- :125–126, :139–140 "It is remarkable that the representation constructed above remains irreducible also with respect to a subalgebra of S [de Sitter] ... the representation remains irreducible when we narrow down from D3 to the deSitter algebra."
- Signature: the text says "non-compact group O6" and does not print "(4,2)". The identification as O(4,2) is Barut–Kleinert's reading (156 fn3; 160 fn2 "O(4,2)~SU(2,2)"). It is consistent with the 15 generators and the zero-mass Klein–Gordon analogy, but the signature itself is not printed by Malkin–Man'ko.

---

## 4. CDT spectral dimension: Ambjørn, Jurkiewicz, Loll 2005

**Citation.** J. Ambjørn, J. Jurkiewicz, R. Loll, "The Spectral Dimension of the Universe is Scale Dependent", Phys. Rev. Lett. 95 (2005) 171301. arXiv:hep-th/0505113 (v2, 6 Jun 2005).
**DOI.** 10.1103/PhysRevLett.95.171301. Crossref `crossref_10_1103_PhysRevLett_95_171301.pretty.json`: :46 DOI, :62 title, :65 vol 95, :20 issue 17, :269 article-number 171301.
**Opened.** PRIMARY, from arXiv v2, `arxiv_hep-th_0505113.txt`. The PRL version of record was not opened; its values could differ from v2.

- :15 "arXiv:hep-th/0505113v2 6 Jun 2005"
- :35–38 (abstract) "While four-dimensional on large scales, the quantum universe appears two-dimensional at short distances."
- :296 fit: "DS(σ) = 4.02−119/(54+σ)"; the same fit is Eq. (11) at :307–311
- **:341** "DS(σ = ∞) = 4.02 ± 0.1, (14)"; :343–344 "compatible with four"
- **:345–350** "the "short-distance spectral dimension", obtained by extrapolating eq. (12) to σ → 0 is given by DS(σ = 0) = 1.80 ± 0.25, (15) and thus is compatible with the integer value two."
- Caveats from the paper: the fit window is σ ∈ [40, 400] (:303); the region σ < 40 was excluded as a lattice artifact (:260–263, "we have only included the region σ ≥ 40"); 1.80 is an **extrapolation** outside the fitted window; the lattice size was N ≈ 181,000 four-simplices (:298–299); the geometries are "Euclidean(ized)" (:151).

---

## 5. Carlip reviews

**5a.** S. Carlip, "Dimension and dimensional reduction in quantum gravity", Class. Quantum Grav. 34 (2017) 193001. arXiv:1705.05417 (v2, 29 May 2017).
**DOI.** 10.1088/1361-6382/aa8535. Crossref `crossref_10_1088_1361-6382_aa8535.pretty.json`: :98 DOI, :116 title, :119 vol 34, :20 issue 19, :111 page 193001.
**Opened.** PRIMARY, arXiv v2, `arxiv_1705_05417.txt`.

Framing and caveats:
- :21–23 (abstract) "A number of very different approaches to quantum gravity contain a common thread, a hint that spacetime at very short distances becomes effectively two dimensional."
- :43–44 "hints have emerged ... that the dimension of spacetime is dynamical and scale-dependent, and shrinks to d ∼ 2 at very small distances or high energies."
- :65–67 "Dimensional reduction of spacetime near the Planck scale is a candidate for second such commonality, albeit one that is much less firmly established."
- :133–135 "A number of rather different possibilities exist, and different choices need not always agree. Dimension may depend on exactly what physical question we are asking."
- :495–497 "we do not yet have a complete theory of quantum gravity; nor, as we have seen, do we have a unique way to define dimension."
- :884–891 "many approaches to quantum gravity show indications of dimensional reduction near the Planck scale. Taken individually, none of these hints is terribly convincing. Perhaps the best evidence comes from asymptotic safety ... and causal dynamical triangulations, in which the evidence for flow of the spectral dimension is extremely strong. But for this evidence to be truly persuasive, we would have to ... know how to quantize gravity."
- :892–894 "Taken as a body, though, these hints become quite a bit more compelling."
- :900–901 "different hints of dimensional flow employ different definitions of dimension, which need not be equivalent."
- :832–834 "one must be very careful about exactly what one means by "dimension"—different choices of how to measure dimension can give different results"

Approaches in Section 3, with the estimator used and the short-distance value Carlip reports. Most results are **not** spectral dimension:

| Sec. | Approach | Estimator / value | line(s) |
|---|---|---|---|
| 3.1 | High-temperature string theory | thermodynamic d_th → 2 (Atick–Witten); "for now these are only hints" | 503–506, 533 |
| 3.2 | CDT | d_S: 4 → "≈ 2"; 3D model 3 → ≈ 2; "lower limit is not known exactly, and may be consistent with dS = 1.5 [71]"; "unambiguous" | 561–568 |
| 3.2 | Euclidean DT (fine-tuned measure) | d_S ≈ 4 → ≈ 1.5, "quite coarse, ... large uncertainties" | 569–574 |
| 3.3 | Asymptotic safety | d_qG → 2 at fixed point; d_S "a quantum regime near the fixed point with dS = 2" | 591–594, 617–623 |
| 3.4 | Causal sets | Myrheim–Meyer d_MM ≈ 2 (4–6 elements; KR orders 2.38); causal spectral d_cs raw *increases*, → 2 with "right" d'Alembertian; d_G → 2 with regularization ambiguities | 637–655 |
| 3.5 | Loop quantum gravity | "the evidence is mixed"; Modesto d_S 4 → 2; pure spin networks no flow; LQC d_S = 2.5 or 1 | 665–693 |
| 3.6 | Short-distance Wheeler–DeWitt (strong coupling, Kasner/BKL) | d_geod → 2; d_S "plausible", effective 2 | 721–732 |
| 3.7 | Modified dispersion / noncommutative geometry | DSR d_S → 2 "depends on a free parameter"; κ-Minkowski value "depends on a nonunique choice"; Connes spectral action d_S = 0; variant → 2; "uncomfortable amount of freedom" | 766–786 |
| 3.8 | Minimum length | smeared initial condition gives d_S = d/2; box-counting d_b → 2 | 798–816 |
| 3.9 | Modified gravity (Hořava–Lifshitz, curvature-squared, nonlocal) | d_S 4 → 2; flagged "essentially classical", "cautionary notes" | 818–834 |
| 3.10 | Spacetime foam | d_H = d_G = 4 − ε (Crane–Smolin); Planck-scale light-cone collapse in 2D | 845–866 |
| 3.11 | Multifractional geometry | framework, "not so much a model ... that predicts" | 869–877 |

Honest reading: the values are not all 2 (1.5, 2.38, 2.5, 1, 0, d/2 and 4 − ε all appear), and they are not all spectral dimensions. The spectral-dimension-to-2 subset is CDT, asymptotic safety, the Modesto LQG heat kernel, Hořava–Lifshitz, one variant of the Connes spectral action, DSR (parameter-dependent) and the "right d'Alembertian" causal-set result.

**5b.** S. Carlip, "Spontaneous Dimensional Reduction in Short-Distance Quantum Gravity?", arXiv:0909.3329 (v1, 17 Sep 2009), `arxiv_0909_3329.txt`. PRIMARY. The journal/proceedings reference is **not pinned** because no Crossref record was fetched.
- :13–16 (abstract) "Several lines of evidence suggest that quantum gravity at very short distances may behave effectively as a two-dimensional theory. I summarize these hints"
- :33–34 "No single indication of this behavior is in itself very convincing, but taken together, they may point toward a promising direction for further investigation."
- Approaches listed are section heads: CDT :43, Renormalization Group Analysis :110, Loop quantum gravity :149, High temperature strings :166, Anisotropic scaling models :178. The new argument is the strong-coupling Wheeler–DeWitt equation, :205.
- :95–96 "the spectral dimension is not the unique generalization of dimension, and one may worry about reading too much significance into this result."
- :199–203 ""dimension" is not such an obvious quantity in quantum gravity, but may have different meanings depending on how one probes the physics."

---

## 6. Definition of spectral dimension

AJL, `arxiv_hep-th_0505113.txt`, PRIMARY:
- :103–108 Diffusion equation ∂_σ K_g(ξ,ξ₀;σ) = Δ_g K_g, where "σ is a fictitious diffusion time"
- :113–117 "average return probability P_g(σ) := (1/V) ∫ d^dξ √det g K_g(ξ,ξ;σ) (3)"
- :128–132 "Because of P_g(σ) = 1/σ^{d/2} in the flat case, we can extract the dimension d ... by taking the logarithmic derivative, −2 d log P_g(σ)/d log σ = d (5)"
- :172–175 on fractals: "the return probability takes the form P_N(σ) = σ^{−DS/2} F(σ/N^{2/DS}), (7) where ... DS is the so-called spectral dimension, which is not necessarily an integer"
- :184–187 "DS(σ) = −2 d log P_N(σ)/d log σ, (8)"

Carlip 2017, `arxiv_1705_05417.txt`, PRIMARY:
- :248–251 heat kernel (∂_s − Δ_x)K(x,x′;s) = 0, K(x,x′;0) = δ(x − x′), Eq. (2.5)
- :258–263 "K(x, x; s) ∼ (4πs)^{−dS/2} (1 + [a1]s + [a2]s² + ...) (2.6)"
- :265–270 "The scale-dependent generalized spectral dimension dS(s) of a region X is obtained from the "return time," dS(s) = −2 d ln⟨K(x,x;s)⟩_X / d ln s (2.7)"
- :272–275 "For a smooth manifold, lim_{s→0} dS(s) gives the ordinary geometric dimension ... for s large, dS(s) can begin to probe the global topology."

Carlip 2009, `arxiv_0909_3329.txt`:82–87: "the return probability K(x, x, s) is K(x,x;s) ∼ (4πs)^{−dS/2}. (3) ... we can then use equation (3) to define an effective dimension dS, the spectral dimension."

Summary of the definition: P(σ) ∝ σ^{−d_S/2}, equivalently d_S = −2 d ln P / d ln σ. It is Riemannian (Euclidean) diffusion; Carlip notes :296–297 "The spectral dimension considers random walks without any limit to causal paths."

---

## Still owed
- Fock's own text (Springer, paywalled): the content is SECONDARY only.
- Bander & Itzykson 1966 text: Crossref metadata only.
- The PRL version-of-record values for AJL: only arXiv v2 was opened.
- The venue of Carlip 0909.3329: not pinned.
- The volume number of Kleinert's 1968 lectures ("X-B"): not in any saved file.
- The O(4,2) signature for Malkin–Man'ko: the paper prints "non-compact O6 / D3", and the (4,2) reading comes from Barut–Kleinert.
