# R11 pins — ladder reps, Mack 1977 classification, KK zero modes, free-field dimensions

Grace r11, drafted by a Claude subagent, 2026-09-27 09:45 EDT. Draft: nothing here is filed to a row.
Directory: `data/sources_grace_2026-09-27/r11/`. `VT[X]` means block X of `VISUAL_TRANSCRIPTIONS.txt` in this directory. Each of those blocks was read by eye from a PNG under `png/`. Line numbers refer to the saved `.txt` text layers.

## Summary

| # | Target | Status |
|---|---|---|
| 1 | Mack–Todorov 1969: the ladder representations stay irreducible on the Poincaré group; they are massless with helicity s | **PIN OWED (paywalled, closed OA). Pinned SECONDARY**, in the body text of four open papers. Two of them are by the original authors (Mack 1977; Todorov 2019). Δ = \|helicity\| + 1 is pinned PRIMARY in Mack 1977 class (5), and SECONDARY as a numbered equation in Gazeau–Pejhan–Todorov (3.140). |
| 1a | DOI supplied in the brief | **WRONG.** 10.1063/1.1664805 is Mukunda, "Matrices of finite Lorentz transformations… O(2,1)", JMP 10, 2086. Mack–Todorov is **10.1063/1.1664804**. |
| 2 | Mack 1977 five-class list: theorem or equation number | **There is none.** The list is unnumbered and sits in Sec. 1, typed p.1. The numbered backing is eqs. (5.4a–d) on typed pp.18–19, (6.33a,b) on typed p.31, and the sentence "The result is as indicated in Sec. 1" on typed p.34. |
| 3 | KK scalar mode expansion, m_n = \|n\|/R, massless zero mode; g_{μ5} → A_μ, g_55 → scalar | **PINNED PRIMARY**: Overduin–Wesson eqs. (5), (20), (23), (27) and Pérez-Lorenzana eqs. (14)–(16). Kaluza 1921 and Klein 1926 are cited as history only. |
| 4 | Free massless scalar Δ = 1 = (d−2)/2; spin-s bound Δ ≥ s + d − 2 | **PINNED PRIMARY** (Minwalla eqs. (2.41), (2.45)–(2.46), (2.58), (2.62)). "Conserved current saturates" is pinned for **vectors only**. For general s it is **not stated** in Minwalla; that part is **PIN OWED**. |

---

## Item 1. Mack & Todorov, J. Math. Phys. 10 (1969) 2078–2085

**Metadata.**
- `crossref_10.1063_1.1664804_mack_todorov_1969.json`: title "Irreducibility of the Ladder Representations of U(2, 2) when Restricted to the Poincaré Subgroup". Authors G. Mack (Univ. Miami) and I. Todorov (IAS Princeton). Vol. 10, issue 11, pp. 2078–2085, 1969-11-01.
- `crossref_search_mack_todorov.json` is the bibliographic search that found the correct DOI.
- `crossref_10.1063_1.1664805_WRONG_DOI_is_Mukunda.json` shows that the DOI in the brief resolves to Mukunda, pp. 2086–2092.
- INSPIRE recid 58569 (`inspire_58569_mack_todorov.json`, `inspire_mack_todorov.json`) has no `documents` and no `urls`, so it offers no scanned fulltext. It lists 98 citations.
- OpenAlex (`openalex_mack_todorov_1969.json`) gives `is_oa: False, oa_status: closed, any_repository_has_fulltext: False`.

**Status: PIN OWED for the primary.** Crossref does carry a publisher abstract, but it is an abstract, so per the brief it is not used as a pin.

**Conventions (secondary sources).**
- Mack 1977 labels each representation by d, "called the dimension", and a Lorentz irrep (j₁,j₂) with 2j₁, 2j₂ nonnegative integers (VT[A] A2–A5). d is the lowest eigenvalue of the conformal Hamiltonian H₀ = ½(P⁰+K⁰). See r6 VT blocks G and H: Lemma 2 on typed p.11.
- Todorov 2019 writes h for **twice** the helicity: "For fixed (twice) helicity h =: φ̃φ … (1.15)" (VT[N] N4–N5).
- Gazeau–Pejhan–Todorov use λ ∈ ½ℤ for the helicity and ℰ∘ for the eigenvalue of the conformal Hamiltonian H (3.130). They call ℰ∘ the "lowest conformal energy (or conformal dimension)" (VT[L]).

**SECONDARY pins.**

1. **Mack 1977, DESY 75/50** (r6 file `mack_desy75-050_preprint_inspire.pdf`, typed p.2, VT[B] B6–B8). This is one of the two original authors describing the joint paper:
   > "The (massless) representations with d = j₁+j₂+1 have been investigated by Todorov and the author [6]."

   Reference 6 (typed p.48, VT[G] G1):
   > "6. Mack, G., Todorov, I.T.: J. Math. Phys. 10, 2078 (1969)."

   The content of that class is pinned PRIMARY in Mack 1977 itself (Item 2), class (5):
   > "j₁j₂ = 0, d = j₁+j₂+1 contains m = 0, helicity j₁−j₂"

   Irreducibility under the Poincaré group, typed p.34, VT[F] F8–F11:
   > "If either j₁j₂ = 0 or d = j₁+j₂+1 irreducibility of H_λ is obvious since the representation restricts to an irreducible representation of the Poincaré group with dilations."

   **Caveat:** this says "Poincaré group *with dilations*", not the bare Poincaré group. Mack–Todorov's title claim is the bare Poincaré subgroup, which only the secondary quotes below state.

2. **Todorov, "The lure of conformal symmetry"**, arXiv:1905.13009 (`cand/arxiv_1905.13009.txt:202–209`, pdf/printed p.5, VT[N]). This is by the other original author.
   > "For fixed (twice) helicity h =: φ̃φ … (1.15) the ladder representation of U(2,2) is irreducible and remains irreducible when restricted to the Poincaré subgroup (see [MT] and Appendix A below)."

   The same page states masslessness: "(1.13) is massless, i.e. p² = 0, and has positive energy" (VT[N] N1–N3). The reference is at `.txt:838–840`: "[MT] G. Mack, I. Todorov, Irreducibility of the ladder representations of U(2,2) when restricted to the Poincaré subgroup, J. Math. Phys. 10 (1969) 2078-20185." The "20185" is a typo in the original for 2085. The Appendix (`.txt:637–641`) says it gives "an elementary self contained exposition of the main result of [MT]".

   Also in this paper (`.txt:355`, pdf p.8): "for a massless scalar field ϕ(x) (of scale dimension 1)".

3. **Gazeau, Pejhan, Todorov, "Massless Representations in Conformal Space and Their de Sitter Restrictions"**, arXiv:2601.18433 (2026-01-26). Preface (`cand/arxiv_2601.18433.txt:105–111`, pdf p.6, printed roman viii):
   > "Among these, the massless representations, commonly called ladder representations, form a distinguished subclass, ideally suited for describing physically relevant massless systems. First studied by Mack and Todorov in the late 1960s, these representations exhibit the striking property of remaining irreducible when restricted to the quantum-mechanical Poincaré subgroup ISL(2, C). In this limit, they yield the well-known Poincaré massless representations, characterized by vanishing rest mass and quantized helicity."

   Δ as a numbered equation (`.txt:5719–5730`, pdf p.117, printed p.103 by offset, VT[L]):
   > "Moreover, |LW_λ⟩ is an eigenstate of the conformal Hamiltonian H (3.130) … with eigenvalue: ℰ∘ := 1 + |λ| , with λ ∈ ½ℤ , (3.140)"
   > "This eigenvalue — the 'lowest conformal energy' (or conformal dimension) — serves to label the lowest weight state |LW_λ⟩ of the representation."

   This is **Δ = |helicity| + 1**, consistent with Mack's class (5), d = j₁+j₂+1 with j₁j₂ = 0.

4. **Fernando & Günaydin**, arXiv:0908.3624, J. Math. Phys. 51 (2010), DOI 10.1063/1.3447773 (`cand/arxiv_0908.3624.txt:302–305`):
   > "These are simply the doubleton representations of SU(2,2). They were referred to as ladder (or most degenerate discrete series) unitary representations by Mack and Todorov who showed that they remain irreducible under restriction to the Poincaré subgroup [29]."

   The reference is at `.txt:3443`.

**Honest reading.** Four open papers attribute the same content to Mack–Todorov, and two of them are by its authors: ladder = massless, labelled by helicity, irreducible on the Poincaré group. **Δ = s+1 is not attributed to Mack–Todorov 1969 in any of them.** It comes from Mack 1977 class (5) and Gazeau–Pejhan–Todorov (3.140). When citing, keep the two apart: Mack–Todorov 1969 for irreducibility and masslessness, Mack 1977 for d = |helicity| + 1.

---

## Item 2. Mack 1977: where the classification sits

**Source.** G. Mack, "All unitary ray representations of the conformal group SU(2,2) with positive energy", DESY 75/50 preprint, image-only typescript on disk at `../../sources_grace_2026-09-26/r6_conformal/mack_desy75-050_preprint_inspire.pdf`. Published as Commun. Math. Phys. 55 (1977) 1–28, DOI 10.1007/BF01613145.

**Journal print: NOT opened.** OpenAlex (`openalex_mack1977_cmp55.json`) lists a green-OA copy at bib-pubdb1.desy.de/record/393919. Fetching it returned a JavaScript bot challenge (`desy_pubdb_393919.html`, `.xml`, both 248 B). The Project Euclid id is still unknown. The CMP pagination and any theorem numbering in the printed version are therefore **PIN OWED**. Everything below is the preprint's typed numbering.

**Conventions.** These are already pinned in r6 (VT blocks E–H there) and restated in VT[A] here:
- G̃ is the universal cover of SU(2,2).
- d is "the dimension", the lowest eigenvalue of H₀ = ½(P⁰+K⁰), Lemma 2 on typed p.11.
- (j₁,j₂) is an SL(2,C) irrep with 2j₁, 2j₂ ∈ ℤ≥0.
- The lowest weight is λ = (d, −j₁, −j₂).
- [m,s] is the Poincaré content, with m = mass and s = spin or helicity.

**Answer: the five-class list has no theorem or equation number.**
- It is an unnumbered display in **Sec. 1 "Summary and introduction", typed p.1 (pdf p.3)**, VT[A]. It comes before the paper's first numbered equation, (1.1) on typed p.2 (VT[B] B9).
- Class (5), verbatim (VT[A] A12):
  > "(5) j₁j₂ = 0, d = j₁+j₂+1 contains m = 0, helicity j₁−j₂ ."
- The body's own restatement, typed p.34 (pdf p.36), VT[F] F5–F7:
  > "From Eq. (6.37) resp. (6.33) we can also read off the Poincaré content of the representation space H_λ. The result is as indicated in Sec. 1."

**Numbered equations that carry the result:**
- **(5.4a)–(5.4d)**, Sec. 5 "Necessary conditions for unitarity", typed pp.18–19 (pdf pp.20–21), VT[C] and VT[D]:
  - "d ≥ j₁ + j₂ + 2 if j₁ ≠ 0, j₂ ≠ 0 (5.4a)"
  - "d ≥ j₁ + 1 if j₁ ≠ 0, j₂ = 0 (5.4b)"
  - "d ≥ j₂ + 1 if j₁ = 0, j₂ ≠ 0 (5.4c)"
  - "d = 0 or d ≥ 1 if j₁ = j₂ = 0 (5.4d)"

  The text that follows says "Conditions (4.4) are necessary …". That is a typo in the original for (5.4) (VT[D] D8, D11). The same bounds appear in Sec. 1 prose on typed p.2 (VT[B] B1–B5).
- **(6.33a), (6.33b)**, Sec. 6, typed p.31 (pdf p.33), VT[E]. This is the massless support:
  > "Δ^λ₊(p) = θ(p₀) Π^{j₁−j₂}_{hel}(p) δ(p²) for λ = (d,−j₁,−j₂), d = j₁ + j₂ + 1; j₁ = 0 or j₂ = 0. (6.33a)"

  and the scalar product ∫_{p₀>0} d⁴p δ(p²) ⟨…⟩ ≥ 0 (6.33b).
- **Irreducibility**, typed p.34, VT[F] F8–F11, quoted under Item 1.
- **Sufficiency** (existence of a UIR for every allowed weight) is Sec. 6, "Induced representations on Minkowski space". In Sec. 1 prose, typed p.2: "In the last step we construct a unitary irreducible representation of G̃ for every weight λ satisfying these constraints." That sentence is in the OCR at `r6 …_OCR.txt:76–77` and its first words are visible on the pdf p.4 PNG.

**Recommended citation form:** "Mack 1977, Sec. 1 list (class 5), with eqs. (5.4b,c) and (6.33a); DESY 75/50 typed pp.1, 18, 31, 34". Do not write "Theorem N".

---

## Item 3. Kaluza–Klein zero modes on M⁴ × S¹

### 3A. Overduin & Wesson, "Kaluza-Klein Gravity"
Phys. Rep. 283 (1997) 303–378, DOI 10.1016/S0370-1573(96)00046-4 (`crossref_overduin_wesson_1997.json`). arXiv:gr-qc/9805018, file `arxiv_gr-qc_9805018.pdf`/`.txt`. Page numbers below are the arXiv printed pages, which match the pdf page index.

**Conventions**, quoted before any formula (`.txt:640–644`, p.14, VT[H] H3–H5):
> "(Throughout this report, Greek indices α, β, ... run over 0, 1, 2, 3, and small Latin indices a, b, ... run over 1, 2, 3. The four-dimensional metric signature is taken to be (+ − − −), and we work in units such that c = 1. In addition, for convenience and accord with other work, we set ħ = 1 in § 3, and G = 1 in in § 7 and § 8.)"

Further conventions:
- The fifth coordinate is **index 4**, not 5 (A = 0…4, "y = x⁴", `.txt:984–985`). So the brief's g_{μ5} is their ĝ_{α4}, and g_55 is their ĝ_44.
- The radius is **r** (`.txt:985–986`): "f(x, y) = f(x, y + 2πr) where r is the scale parameter or 'radius' of the fifth dimension."

**Metric reading** (Sec. 3.2, `.txt:627–636`, p.14, VT[H] H1–H2):
> "In general, one identifies the αβ-part of ĝ_AB with g_αβ (the four-dimensional metric tensor), the α4-part with A_α (the electromagnetic potential), and the 44-part with φ (a scalar field). A convenient way to parametrize things is as follows: (ĝ_AB) = ( g_αβ + κ²φ²A_αA_β , κφ²A_α ; κφ²A_β , φ² ) (5)"

- In this parametrization ĝ_44 = φ², with φ the scalar.
- The word "dilaton" appears only after a conformal rescaling (`.txt:877`, p.18): "In terms of the 'dilaton' field σ ≡ ln φ/(√3 κ), this action can be written: … (19)". This follows the redefinition φ² → φ (`.txt:866`).
- So "g_55 → dilaton" is the review's usage only up to the redefinitions φ² → φ and σ = ln φ/(√3κ).

**Mode expansion**, Sec. 4.1 "Klein's Compactification Mechanism" (`.txt:982–1007`, p.20):
> "any quantity f(x, y) (where x = (x⁰, x¹, x², x³) and y = x⁴) becomes periodic; f(x, y) = f(x, y + 2πr) … Therefore all the fields can be Fourier-expanded: g_αβ(x,y) = Σ_{n=−∞}^{∞} g⁽ⁿ⁾_αβ(x) e^{iny/r}, A_α(x,y) = Σ A⁽ⁿ⁾_α(x) e^{iny/r}, φ(x,y) = Σ φ⁽ⁿ⁾ e^{iny/r} (20)"
> "Thanks to quantum theory, these modes carry a momentum in the y-direction of the order |n|/r. … Hence only the n = 0 modes, which are independent of y, will be observable, as required in Kaluza's theory."

**Zero modes as graviton, photon and scalar** (`.txt:1022–1029`, p.20):
> "One then makes what is known in compactified theory as the 'Kaluza-Klein ansatz,' which consists in discarding all massive (n ≠ 0) Fourier modes … giving the effective four-dimensional 'low-energy' theory of the graviton g⁽⁰⁾_αβ, photon A⁽⁰⁾_α and scalar φ⁽⁰⁾."

**Massless 5D scalar and its mass formula** (Sec. 4.2):
- `.txt:1058–1061`, p.21: "The simplest kind of matter is a massless five-dimensional scalar field ψ̂(x, y). Its action would have a kinetic part only: … (22)".
- `.txt:1065–1069`, p.22: "ψ̂(x,y) = Σ_{n=−∞}^{∞} ψ̂⁽ⁿ⁾ e^{iny/r} (23)".
- `.txt:1115–1119`, p.22, VT[I] I4–I5: "the masses of the scalar modes … are given by the square root of the coefficient of the ψ̂⁽ⁿ⁾²-term: m_n = |n|/(r√φ) (27)".

**Convention caveat:** the review's formula is **m_n = |n|/(r√φ)**. It reduces to |n|/r only for φ = 1, the ground state ⟨ĝ_44⟩ with magnitude 1 in eq. (21) (`.txt:1033–1040`). The n = 0 mode is massless by (27).

**History** (references, `.txt:4283–4287`, pdf p.81):
> "[1] T. Kaluza, Zum Unitätsproblem der Physik, Sitz. Preuss. Akad. Wiss. Phys. Math. K1 (1921) 966. (Eng. trans. in [3], [4] and [7].)"
> "[2] O. Klein, Quantentheorie und fünfdimensionale Relativitätstheorie, Zeits. Phys. 37 (1926) 895. (Eng. trans. in [3], [4] and [7].)"

Also `.txt:4380–4381`: "[36] O. Klein, The atomicity of electricity as a quantum theory law, Nature 118 (1926) 516."

### 3B. Pérez-Lorenzana, "An Introduction to Extra Dimensions"
J. Phys. Conf. Ser. 18 (2005) 224–269, DOI 10.1088/1742-6596/18/1/006 (`crossref_perez_lorenzana_2005.json`). arXiv:hep-ph/0503177, file `cand/arxiv_hep-ph_0503177.pdf`/`.txt`. Page numbers are arXiv printed pages.

**Conventions.**
- Circle of radius **R** (`.txt:291–293`, p.5): "let us consider a simplified five dimensional toy model where the fifth dimension has been compactified on a circle of radius R."
- A = 1,…,5 (`.txt:302`).
- The signature is **not stated in words** in this section. The action (14) is written "∂^Aφ∂_Aφ − m²φ²", with a positive kinetic term and a negative mass term, which reads as mostly-minus. **INFERRED, not quoted.**

**Pins.** Equations at `.txt:296–306` (p.5) and `.txt:310–327`, `.txt:354` (p.6), VT[J]:
> "S[φ] = ½ ∫ d⁴x dy [∂^Aφ∂_Aφ − m²φ²] ; (14)"
> "φ(x,y) = (1/√(2πR)) φ₀(x) + Σ_{n=1}^{∞} (1/√(πR)) [φ_n(x) cos(ny/R) + φ̂_n(x) sin(ny/R)] . (15)"
> "The very first term, φ₀, with no dependence on the fifth dimension is usually referred as the zero mode. … Some authors prefer to use a complex e^{iny/R} Fourier expansion instead, but the equivalence of the procedure should be clear."
> "S[φ] = Σ_{n=0}^{∞} ½∫d⁴x(∂^μφ_n∂_μφ_n − m_n²φ_n²) + Σ_{n=1}^{∞} ½∫d⁴x(∂^μφ̂_n∂_μφ̂_n − m_n²φ̂_n²) , (16) where the KK mass is given as m_n² = m² + n²/R²."
> "For m = 0, it is clear that for energies below 1/R only the massless zero mode will be kinematically accessible, making the theory looking four dimensional."

So for a 5D massless scalar, (16) gives **m_n = |n|/R, and the n = 0 mode is massless**. This is the cleanest form of the brief's target. Pérez-Lorenzana uses a cos/sin basis; the e^{iny/R} basis is named in the text as equivalent.

**Graviton decomposition**, for n extra dimensions on a torus of radius R (`.txt:480–484`, `.txt:488–514`, p.8):
> "(i) h_μν clearly contains a 4D Lorentz tensor, the true four dimensional graviton. (ii) h_aμ behaves as a vector, the graviphotons. (iii) Finally, h_ab behaves as a group of scalars (graviscalar fields), one of which corresponds to the partial trace of h (h_a^a) that we will call the radion field."
> "h_MN(x,y) = Σ_n h⁽ⁿ⁾_MN(x)/√V_n e^{i n·y/R} (25)"
> "Notice that G⁽⁰⁾_μν is massless since the higher dimensional graviton h_MN has no mass itself."

History (`.txt:2240–2241`):
> "[1] Th. Kaluza, Sitzungober. Preuss. Akad. Wiss. Berlin (1921) 966; O. Klein, Z. Phys. 37 (1926) 895."

The misspelling "Sitzungober." is in the original.

### 3C. Supporting sources (saved, not the main pins)
- **Sundrum, TASI 2004**, hep-th/0508134 (`cand/arxiv_hep-th_0508134.txt`).
  - `.txt:170–171`: "the 5D theory is equivalent to a 4D theory with an infinite tower of 4D fields, with masses, m_n² = n²/R²". Eq. (2.5), for a 5D gauge field.
  - `.txt:1189–1194`: "the h⁽⁰⁾_MN(x) must be massless 4D fields … The h⁽ⁿ⁾_MN have n/R masses as usual. … The interacting massless vector field, h⁽⁰⁾_μ5(x), must therefore have a protective gauge symmetry." Eq. (8.9) is nearby. **Here the index is 5.**
- **Csáki, TASI**, hep-ph/0404096 (`arxiv_hep-ph_0404096.txt`).
  - It defers the basic KK decomposition to Dienes' TASI 2002 lectures (`.txt:137–139`).
  - It gives only the graviton torus expansion (2.37), with "These modes are generically massive, except for the zero mode" (`.txt:633–634`).
  - Its metric convention is `.txt:421`: "η_MN = diag(+, −, …".
  - Kaluza and Klein ref [2] (`.txt:3789–3790`): "T. Kaluza, Sitzungsber. Preuss. Akad. Wiss. Berlin (Math. Phys.) 1921, 966 (1921); O. Klein, Z. Phys. 37, 895 (1926)".
  - Csáki is not needed for the scalar pin.
- **Bailin & Love 1987**: not fetched; the open sources suffice.

---

## Item 4. Free massless fields and the conformal-dimension bounds

**Source.** S. Minwalla, "Restrictions Imposed by Superconformal Invariance on Quantum Field Theories", Adv. Theor. Math. Phys. 2 (1998) 783–851, DOI 10.4310/ATMP.1998.v2.n4.a4 (`crossref_search_minwalla.json`, first hit). arXiv:hep-th/9712074, file `arxiv_hep-th_9712074.pdf`/`.txt`. Printed page = pdf page − 1.

**Conventions**, quoted first:
- `.txt:116–119`, printed p.2: "The conformal group in d dimensions is generated by d(d−1)/2 Lorentz generators M_μν, d momenta P_μ, d special conformal generators K_μ and a dilatation D. (Through this section greek indices run from 0 to d − 1)." So **d is the spacetime dimension.**
- `.txt:158–160`, p.3: "The Conformal Group group is locally isomorphic to the group SO(d, 2). Denote SO(d, 2) generators by S_ab where latin indices run from -1 to d. The indices -1 and 0 are associated with -1 in the metric." So the time direction carries −1: **mostly-plus**.
- ε₀ is the scaling dimension, the eigenvalue of the Euclideanized D′ (`.txt:245–247`): "restrictions on scaling dimensions ε₀ of operators defined by [D′, O_p′] = (−i)(−iε₀ O_p′)".
- The bounds are labelled by SO(d) highest weights h₁ ≥ h₂ ≥ … (`.txt:326–331`). A symmetric traceless spin-s tensor has h = (s, 0, …, 0).

**Pins.**
- **General d**, `.txt:398–402`, printed p.9:
  > "if the representation R has highest wts s.t. h₁ ≥ |h₂| + 1 then the condition above becomes ε₀ ≥ h₁ + d − 2. The formula for an arbitrary representation in terms of its highest weights is ε₀ ≥ |h_i| + d − i − 1 (2.41)"

  For spin s ≥ 1, h₁ = s and h₂ = 0, so **ε₀ ≥ s + d − 2**, which is **s + 2 at d = 4**. `.txt:408`: "The answer for the vector representation is ε₀ ≥ d − 1."
- **d = 4**, `.txt:422–431`, printed p.10, VT[K]:
  > "In d = 4 SO(4) = SU(2) × SU(2), and so representations are labeled by two half integers, j₁ and j₂. The conditions derived for this case is ε₀ ≥ f(j₁) + f(j₂) (2.45) Where f(j) is defined by f(j) = 0 for j = 0, f(j) = j + 1 for j > 0 (2.46) These are precisely⁸ the conditions derived in [10]."

  Reference [10] is Mack's "All Unitary Ray Representations of the Conformal Group SU(2,2) with …" (`.txt:2934`). So Minwalla (2.45)–(2.46) reproduces Mack (5.4a–c). For (j,0) the bound is j + 1 (the massless line), and for (s/2, s/2) it is s + 2.
- **Conserved currents: vectors only**, `.txt:477–484`, printed p.11:
  > "The bound on the vector representation is, at first sight, a little puzzling. In 4 dimensions, for instance, it is ε₀ ≥ 3 … Vector operators that saturate the bound above satisfy [P_μ, ψ_μ] = 0; examples of such operators are conserved currents; these are indeed vectors, and indeed have the scaling dimension above."

  **Scope:** Minwalla states "saturation ⟺ conservation" only for the vector (s = 1, Δ = d − 1 = 3 at d = 4). For general s, "a conserved spin-s current has Δ = s + d − 2" is the bound (2.41) at saturation. The conservation reading for s ≥ 2 is **not stated in this source: PIN OWED.** A candidate for the next round is a source that states that unitarity-bound saturation implies ∂·J = 0 for symmetric traceless spin s.
- **Free scalar**, `.txt:489–503`, printed p.11:
  > "ε₀(ε₀ − (d − 2)/2) ≥ 0 (scalar). (2.58) This condition permits the singleton representation with ε₀ = 0, but forces all non singleton scalar representations to have dimension greater than the scaling dimension of the free scalar field."
- **Free-field dimension**, `.txt:553–560`, printed p.13:
  > "we obtain ε₀ = h₁ + (d−2)/2 (2.62) where h₁ is the highest first weight of φ."

  For the scalar, h₁ = 0 gives **ε₀ = (d−2)/2 = 1 at d = 4**.
- **Cross-checks for Δ = 1** (Item 1 sources):
  - Todorov 2019 `.txt:355`: "massless scalar field ϕ(x) (of scale dimension 1)".
  - Gazeau–Pejhan–Todorov, footnote 14 (`.txt:5750–5753`, VT[L] L5–L7): "the lowest conformal energy (or dimension) is ℰ∘ = 1".
  - Gazeau–Pejhan–Todorov, Proposition 3.10 item 3 (printed p.131, VT[M]): "ℰ = 1 for a massless scalar field …; ℰ = 3/2 for a Weyl spinor field with helicity λ = ±½".
  - Mack 1977 (5.4d): d ≥ 1 for j₁ = j₂ = 0. With (5.4b,c) and class (5), this gives d = 1 for the massless scalar, (0,0).

**Consistency across the four items** (arithmetic only, no new claim):
- Mack class (5): d = j₁ + j₂ + 1 with j₁j₂ = 0, helicity j₁ − j₂, so **d = |helicity| + 1**.
- Minwalla (2.62) at d = 4 with SO(4) weight h₁ = j₁ + j₂ gives ε₀ = j₁ + j₂ + 1. This is the same line.
- Gazeau–Pejhan–Todorov (3.140) gives ℰ∘ = 1 + |λ|. This is also the same line.

---

## Files

**Primary text files in this directory (r11/):**
- `arxiv_gr-qc_9805018.{pdf,txt,abs.html}` (Overduin–Wesson)
- `arxiv_hep-th_9712074.{pdf,txt,abs.html}` (Minwalla)
- `arxiv_hep-ph_0404096.{pdf,txt,abs.html}` (Csáki)

**Metadata files:**
- `crossref_10.1063_1.1664804_mack_todorov_1969.json`
- `crossref_10.1063_1.1664805_WRONG_DOI_is_Mukunda.json`
- `crossref_search_mack_todorov.json`
- `crossref_overduin_wesson_1997.json`
- `crossref_perez_lorenzana_2005.json`
- `crossref_search_minwalla.json`
- `inspire_58569_mack_todorov.json`
- `inspire_mack_todorov.json`
- `inspire_citing_mack_todorov.json`
- `openalex_mack_todorov_1969.json`
- `openalex_mack1977_cmp55.json`
- `desy_pubdb_393919.{html,xml}` (bot-challenge stubs, kept as evidence of the failed fetch)

**Secondary and supporting sources in `cand/`** (pdf + txt + abs.html each):
- `arxiv_1905.13009` (Todorov 2019)
- `arxiv_2601.18433` (Gazeau–Pejhan–Todorov 2026)
- `arxiv_0908.3624` (Fernando–Günaydin)
- `arxiv_hep-ph_0503177` (Pérez-Lorenzana)
- `arxiv_hep-th_0508134` (Sundrum)

Citation-context checks only (pdf + txt, not quoted above):
- `arxiv_1006.1981` (Todorov 2010)
- `arxiv_1902.03812` (Mack 2019)
- `arxiv_hep-th_0504111` (Bracken)

**Visual:** `VISUAL_TRANSCRIPTIONS.txt` (blocks A–N) and `png/` (17 PNGs).

The Mack 1977 PDF and its OCR stay in `../../sources_grace_2026-09-26/r6_conformal/`. They were not copied, only rendered.

## Owed
1. The Mack–Todorov 1969 primary text: paywalled, with no open scan on INSPIRE or OpenAlex.
2. The Mack 1977 CMP 55 print: the DESY pubdb green-OA copy is behind a bot challenge. Numbering in the print could differ from the preprint's.
3. A source that states saturation of Δ ≥ s + d − 2 ⟺ conservation for spin s ≥ 2. Minwalla states it for vectors only.
4. Pérez-Lorenzana's metric signature is inferred from the sign of (14), not quoted.
