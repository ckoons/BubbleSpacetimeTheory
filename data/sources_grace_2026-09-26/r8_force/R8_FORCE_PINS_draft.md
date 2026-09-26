# R8 force pins: power-law ISL bounds and unparticle potential exponents (DRAFT)

Written 2026-09-26 15:02 EDT (clock checked with `date`). All paths are relative to this directory. Line numbers are from `pdftotext -layout`. If an equation is garbled in the text layer, it was read from a rendered PNG; see `VISUAL_TRANSCRIPTIONS.txt` (VT#n).

**Convention key.** Two conventions appear below, and they are compatible:
- Adelberger 2007: V_k = −G M_a M_b/r · β_k (1 mm/r)^{k−1}. The **total** r-exponent is k.
- Unparticle papers: the extra term is ∝ 1/r^{2d_U−1}. Ungravity is written as −Gm1m2/r·[1+(R_G/r)^{2d_U−2}].
- So **k = 2d_U − 1** (equivalently k−1 = 2d_U−2). Deshpande et al. state this explicitly, and so do Wu et al. At d_U = 5/2 this gives **k = 4**, and the total r-exponent is **−4**.

---

## 1. Adelberger, Heckel, Hoedl, Hoyle, Kapner, Upadhye, PRL 98, 131104 (2007), arXiv:hep-ph/0611223v3

- Files: `hep-ph_0611223.pdf`, `.txt`, and `_abs.html`. Crossref: `crossref_10_1103_PhysRevLett_98_131104.json` (DOI 10.1103/PhysRevLett.98.131104, issued 2007-03-29). Rendered page: `hep-ph_0611223_p3-3.png` (VT#1).
- **Parametrization.** From `.txt:179` ("We constrained power-law interactions of the form"), with Eq. (18) at `.txt:182-185`. The equation is garbled in the text layer, so it was read visually (VT#1):
  > V^k_ab(r) = −G (M_a M_b / r) β_k (1 mm / r)^{k−1}   (18)
  > "by fitting the combined data of Ref. [1] with a function that contained the Newtonian term and a single power-law term with k = 2, 3, 4, or 5." (`.txt:188-190`)
  - r0 is fixed at **1 mm**.
  - Eq. 18 is the extra term by itself. It is not written as "[1 + …]".
  - The sign is attractive for β_k > 0.
  - The total r-exponent is k.
  - Cross-check within the paper: its k = 3 two-pseudoscalar potential, Eq. (19), goes as 1/r^3 (`.txt:248-251`).
- **Bounds.** Table I, `.txt:202-211`: "TABLE I: 68% confidence laboratory constraints on power-law potentials from this work and previous[14, 15] results."

  | k | \|β_k\| this work (68% CL) | previous |
  |---|---|---|
  | 2 | 4.5 × 10⁻⁴ | 1.3 × 10⁻³ [15] |
  | 3 | 1.3 × 10⁻⁴ | 2.8 × 10⁻³ [14] |
  | 4 | **4.9 × 10⁻⁵** | 2.9 × 10⁻³ [14] |
  | 5 | 1.5 × 10⁻⁵ | 2.3 × 10⁻³ [14] |

  **The CL is 68%, not 95%.** The paper's Yukawa, chameleon and fat-graviton limits are 95%; only the power-law table is 68%.
- **Eöt-Wash web page.** Files: `eotwash_isl.html`, with the stripped text in `eotwash_isl.txt`.
  - The page says **nothing about power-law bounds**. Its only results statement is at `eotwash_isl.txt:45`: "95% confidence level constraints on a Yukawa violation of the gravitational inverse-square law … detailed in 'New Test of the Gravitational 1/r2 Law at Seperations down to 52 um,'"
  - The words "power", "β" and "unparticle" do not appear on the page.
  - Footer: "© 1987-2023" (`:48`).

## 2. Lee, Adelberger, Cook, Fleischer, Heckel, PRL 124, 101101 (2020), arXiv:2002.11761v1

- Files: `2002.11761.pdf`, `.txt`, and `_abs.html`. Crossref: `crossref_10_1103_PhysRevLett_124_101101.json`.
- **Parametrization.** The paper uses **Yukawa only**:
  > "constraining an additional Yukawa interaction  V(r) = V_N(r)[1 + α exp(−r/λ)]" (`.txt:35-37`)
- **Result:**
  > "limiting with 95% confidence any gravitational-strength Yukawa interactions to ranges < 38.6 µm." (`.txt:11`)
- **This paper gives no β_k (power-law) bounds.** I grepped for "power", "β" and "k−1". The only "power" hits refer to the torque power spectrum (`.txt:101,111`).
- **Newer work, 2021–2026.** I did one web search for candidates, then read each primary source.
  - `2605.18212` (Murata, Fujiie, Suzuki, "Short-Range Tests of the Gravitational Inverse-Square Law", arXiv 2026-05-18). This is a review.
    - Parametrization: V_power(r) = V_N(r)[1 + (Λ/r)^n], "(n, Λ : model parameters)" (`.txt:131-141`).
    - Here **n = k − 1**, and Λ plays the role of r0 with the strength absorbed into it.
    - Its n–Λ limits are **derived, not measured fits**: "Since most experiments do not report their results in terms of power-law parameters, we derive the corresponding power-law constraints by determining a representative δ(r) for each experiment that reproduces the published α–λ exclusion curve" (`.txt:474-478`). They are shown as a figure only; the one number stated is "For the case of n = 2, the upper limit on Λ has been tightened to 4 µm" (`.txt:641-642`).
    - It is **SECONDARY** for β_k.
  - `2406.13020` (Manley et al., microscale torsion resonators, 2024): no power-law bounds (grep empty).
  - `2305.02628` (Wu, Zhang, Yan 2023): reuses the **2007 Table I**; it does not produce a new β_k fit (see Section 5).
  - **Conclusion:** I found no newer direct β_k fit. **Adelberger 2007 Table I is still the primary β_k source.** This conclusion is limited to the search I ran; I did not survey the HUST papers, so a HUST power-law fit remains **PIN OWED** if one exists.

## 3. Goldberg & Nath, PRL 100, 031803 (2008), arXiv:0706.3898v3

- Files: `0706.3898.pdf`, `.txt`, and `_abs.html`. Rendered pages: `0706.3898_p3-03.png` (VT#2) and `0706.3898_p5-05.png` (VT#3).
- Crossref (`crossref_10_1103_PhysRevLett_100_031803.json`) gives the published title as "Scalar Modifications to Gravity from Unparticle Effects May Be Testable". The title in the brief ("…from unparticles") is slightly off.
- **I pinned the arXiv v3 text. The PRL typeset text has not been compared: PIN OWED/SECONDARY for the journal version.**
- **Coupling and its definitions.**
  - Tensor operator, Eq. (2): κ_* (1/Λ_U^{d_U−1}) √g T^{μν} O^U_{μν}, with κ_* = Λ_U^{−1}(Λ_U/M_U)^{d_UV} (`.txt:48-55`).
  - d_U is "an anomalous unparticle dimension" (abstract, `.txt:20`), "the fields of the hidden sector undergo dimensional transmutation at scale Λ_U generating scale invariant unparticle fields O with dimension d_U" (`.txt:35-37`).
- **The potential.** Text at `.txt:122-123`; Eq. (7) is garbled at `.txt:124-132`, so it was read visually (VT#2):
  > "for d_U different from unity the ungravity effects produce an r dependence of the form 1/r^{2d_u−1} … An explicit evaluation gives
  > V(r) = −(m1 m2 G / r)[1 + (R_G/r)^{2d_U−2}],
  > R_G = (1/(πΛ_U)) (M_Pl/M_*)^{1/(d_U−1)} · ( 2(2−α)/π × Γ(d_U+½)Γ(d_U−½)/Γ(2d_U) )^{1/(2d_U−2)}"   (7)
  - So **p = 2d_U − 2**, and the total r-exponent is −(2d_U−1).
  - **R_G** is "a characteristic length scale where the ungravity interactions become significant" (`.txt:20-21`).
  - α = 2/3 for the unparticle tensor projector (`.txt:92`). α = 1 is "the case of the graviton exchange" (`.txt:103-104`).
  - The same scaling is restated at `.txt:226`: "the correction from ungravity has the r dependence of the form 1/r^{2d_U−1} both at short as well as at large distances".
- **Prefactor, as the paper writes it** (verbatim, not reconstructed):
  - (R_G)^{2d_U−2} = (πΛ_U)^{−(2d_U−2)} (M_Pl/M_*)^2 · [2(2−α)/π] · Γ(d_U+½)Γ(d_U−½)/Γ(2d_U).
  - The π powers combine to **2(2−α)/π^{2d_U−1}**. That is **not** the "2/(π^{2d_U−1})" in the brief:
    - tensor case, (2−α) = 4/3: 8/(3π^{2d_U−1});
    - scalar case, (2−α) → 2: **4/π^{2d_U−1}**.
  - This is my own algebra on the pinned Eq. 7, not a quote.
- **Scalar (trace) coupling** (`.txt:144-148`):
  > "Let us now consider a spin zero unparticle operator with d_U ≥ 2 with coupling of the type κ_* √g T^μ_{;μ} O^U / Λ_U^{d_U−1}. In this case the modified Newtonian potential can be gotten from Eq.(7) by replacing (2 − α) by 2."
- **Unitarity ranges** (`.txt:143-144`):
  > "for a rank one tensor operator d_U > 2 and for a rank two d_U > 3."
  - **At d_U = 5/2 only the spin-0 trace coupling is allowed; the spin-2 tensor coupling is not (it needs d_U > 3).**
- **Internal inconsistencies, flagged but not resolved:**
  - The abstract (`.txt:20`) says "corrections of type (R_G/r)^{2dU−1}". Eq. 7 has exponent 2d_U−2 inside the bracket, times 1/r. The abstract is evidently quoting the total r-dependence.
  - `.txt:23` and `.txt:148` say "O(1/r^{(4+2δ)})" for d_U = 2+δ. By Eq. 7 the potential goes as 1/r^{3+2δ}; the force goes as 1/r^{4+2δ}.
  - **Eq. 7 and Fig. 1 are authoritative**, per the check below.
- **Bound.** The paper takes Table I of Adelberger 2007 and extrapolates it: "Instead, we extrapolate the power law limits in Table I of Ref. [10] to obtain an upper limit on R_G as a function of d_U" (`.txt:157-159`; Ref. [10] = PRL 98, 131104, `.txt:372`). Fig. 1 left (VT#3) reads R_G,max ≈ 0.038 mm at d_U = 2.5 (±0.003 by eye).
- **Check (my arithmetic).** Setting R_G^{k−1} = β_k (1 mm)^{k−1} with k = 2d_U−1 gives:

  | d_U | k | R_G = β_k^{1/(k−1)} mm | Fig. 1 read |
  |---|---|---|---|
  | 2 | 3 | 0.0114 | ≈ 0.013 |
  | 2.5 | 4 | **0.0366** | ≈ 0.038 |
  | 3 | 5 | 0.0622 | ≈ 0.063 |

  The figure matches **k = 2d_U − 1**. It does not match k = 2d_U: at d_U = 2 that would give 0.0366, against the ≈ 0.013 on the figure. The small offsets are consistent with their interpolation.

## 4. arXiv:0905.1602v2 — Bertolami, Páramos, Santos, "Astrophysical constraints on unparticle-inspired models of gravity", Phys. Rev. D 80, 022001 (2009)

- Files: `0905.1602.pdf`, `.txt`, and `_abs.html` (metadata: citation_doi 10.1103/PhysRevD.80.022001). Rendered page: `0905.1602_p-1.png` (VT#7).
- **Potential.** Text at `.txt:51-59`, confirmed visually:
  > "Considering tensor-type unparticle interactions with the stress-energy tensor of SM states leads to a modification to the Newtonian potential Φ(r), usually referred to as ungravity — a gravitational potential with a power-law addition [2], V(r) = −(G_U M/r)[1 + (R_G/r)^{2d_u−2}]"   (3)
  - [2] is Goldberg & Nath.
  - R_G in Eq. (4) is the same as Goldberg–Nath Eq. 7.
  - Eq. (6), used in their analysis, is printed as **−GM/(2r)[1 + (R_G/r)^{2d_u−2}]**, with a "2r" that looks like a typo (`.txt:44-45`, VT#7).
  - Exponent convention: 2d_U−2 inside the bracket, same as G-N.
- **Bounds.** These are stellar (solar central temperature, |ΔT_c/T_c| ≤ 0.06). They cover only **d_U near 1**: "1.0 < d_U < 1.06 for 0 < ξ_G < 1 and 0.94 < d_U < 1 for 10 < ξ_G < 10^4".
  > "We find that, for d_U ≳ 1 and Λ_U ≥ 1 TeV, lower bounds on M_* are in the range (10⁻² − 10⁻¹)M_Pl. For d_U ≲ 1 and Λ_U ≥ 1 TeV, M_* must lie in the range above (10⁻¹ − 10²)M_Pl." (`.txt:233-236`)
  - The paper says torsion balances "test a much smaller range of R_G [14], actually about 80 µm" (`.txt:237-239`).
  - **It gives no bound at d_U = 5/2.**

## 5. Other unparticle long-range-force papers

- **Deshpande, Hsu, Jiang, arXiv:0708.2735v2**, "Long range forces and limits on unparticle interactions", PLB (doi 10.1016/j.physletb.2007.12.018 per `_abs.html`). Rendered pages: VT#4.
  - Coupling: vector unparticle to the baryon current, Eq. (2), L = λ_B Λ_U^{1−d_U} B_μ O^μ_U.
  - "In the static limit this interaction generates the potential" (`.txt:54`):
    - Eq. (3): V_U = λ_B² Λ_U^{2−2d_U} (1/4π²)(1/r^{2d_U−1}) A_{d_U} Γ(2d_U−2) B1B2
    - Eq. (5): V_U = (1/2π^{2d_U}) λ_B² Λ_U^{2−2d_U} [Γ(d_U+½)Γ(d_U−½)/Γ(2d_U)] (1/r^{2d_U−1}) B1B2 (`.txt:56-73`)
  - It is repulsive; d_U = 1 gives λ_B²B1B2/(4πr).
  - Comparison with Adelberger, Eq. (10) (`.txt:116`), V^k_12 = −G(m1m2/r)β_k(1 mm/r)^{k−1}:
    > "The range of d_U we are interested in is 1 ≤ d_U ≤ 2 and it is related to k through equation 2d_U − 2 = k − 1." (`.txt:125-126`)
  - Table I (68% CL, `.txt:143,170-178`) reproduces Adelberger's k = 2 and 3 values at d_U = 1.5 (4.5 × 10⁻⁴) and d_U = 2.0 (1.3 × 10⁻⁴). **It does not cover d_U = 2.5.**
- **Liao & Liu, arXiv:0706.1284v2**, PRL 99, 191804. Electron-only couplings. Rendered page: VT#5.
  - Eq. (1) includes a direct scalar coupling C_S ψ̄ψ U_S (`.txt:110`).
  - Eq. (5), after "extracting the common factors A_d r^{1−2d}/(4π²)" (`.txt:87`):
    - U_non = (C_V² − C_S²)Γ(2(d−1)) + Γ(2d)/(4m²r²)[(2−d)C_V² − (3−d)C_S²]
  - **So a scalar with direct coupling gives an attractive leading term ∝ r^{1−2d}**, with a subleading term ∝ r^{−1−2d}. The paper says it will "retain only the leading term ∼ r^{1−2d}" (`.txt:149`), and later "(r^{1−2d} or r^{−1−2d} instead of r^{−3})" (`.txt:164`).
  - Its bounds are spin-spin bounds for 1.2 ≤ d ≤ 1.9. **No ISL (Eöt-Wash) bound.**
- **Freitas & Wyler, arXiv:0708.4339v3**, "Astro Unparticle Physics", JHEP 0712:033. Rendered page: VT#6.
  - > "By taking the Fourier transform of this propagator in the low-energy limit one obtains V_U = C α_U B_iB_j / r^{2d_U−1}" (8) (`.txt:108-111`)
  - Vector α_U is Eq. (9).
  - > "The scalar and pseudo-scalar interactions ∝ c_S2, c_P1, c_P2 do not contribute to long-range non-relativistic forces. However, the contribution from c_S1 gives α_U = π^{1/2}/(2π)^{2d_U} c_S1² (m_i m_j/M_Z^{2d_U}) Γ(d_U−½)/Γ(d_U)" (11) (`.txt:128-131`)
  - The c_S1 operator is (c_S1/M_Z^{d_U}) f̄ D̸ f O_U. It enters with the same 1/r^{2d_U−1} as Eq. 8.
  - Its bounds are Eötvös-type fifth-force limits (Fig. 1) for d_U = 1, 4/3, 5/3, 2 only. **Nothing at 5/2.**
- **Wu, Zhang, Yan, arXiv:2305.02628** (2023), "Exotic spin-dependent interactions through unparticle exchange".
  - Scalar–scalar potential, Eq. (8)/(A20): V_SS = −(A_{d_U}/4π²) C_S² r^{1−2d_U}{Γ(2d_U−2)(…) + …} (`.txt:202`, `.txt:541`).
  - Appendix B reuses Adelberger Table I. Eq. (B1) is quoted there as "V^k_ab(r) = G (M1M2/r) β_k (1 mm/r)^{k−1}", **with the minus sign dropped** (`.txt:552-554`).
  - It matches the VV term ∝ (1 mm/r)^{2d_U−1} (B4, `.txt:573-574`) "when k = 2d_U − 1" (`.txt:586`).
  - This is a second explicit statement of **k = 2d_U − 1**.
- **Mureika (PLB 660, 561 (2008); PRD 79, 056003 (2009))**: not fetched. The tensor ("ungravity") form is already pinned from Goldberg–Nath Eq. 7 with α = 2/3.

## 6. Nieto 1979, Am. J. Phys. 47, 1067

- **Identity is pinned from Crossref** (`crossref_10_1119_1_11976.json`): DOI 10.1119/1.11976, "Hydrogen atom and relativistic pi-mesic atom in N-space dimensions", Nieto, Am. J. Phys. 47, 1067–1072, issued 1979-12-01.
- **OSTI record** (`nieto_try_osti_5728264.json`, OSTI ID 5728264) has the abstract only: "We derive in simple analytic closed form the eigenfunctions and eigenenergies for the hydrogen atom in N dimensions. …". Its only link is a citation link; there is no purl or full text.
- **Full text: PIN OWED.** Tried:
  1. OSTI API search (`nieto_try_osti.json`): record found, no full text.
  2. OpenAlex (`nieto_try_openalex.json`): is_oa False, oa_status "closed", any_repository_has_fulltext False.
  3. Semantic Scholar (`nieto_try_s2.json`): openAccessPdf status CLOSED.
  4. archive.org advanced search, phrase and keyword (`nieto_try_archiveorg_meta*.json`): 0 hits for the phrase. The keyword query results were not itemized.
  5. Web search: publisher (pubs.aip.org) only, paywalled.
- Not tried: Google Scholar "all versions" (no scriptable access), LANL institutional repository beyond OSTI. Sci-hub was not used.

---

## Summary table

| coupling type | potential form (source's own convention) | total r-exponent at d_U = 5/2 | source file:line |
|---|---|---|---|
| ISL power-law parametrization (experiment) | V_k = −G M_aM_b/r · β_k (1 mm/r)^{k−1}; total r^{−k}; \|β_4\| < 4.9×10⁻⁵ (68% CL) | k = 4 ⇒ **r⁻⁴** | hep-ph_0611223.txt:179-190, 202-211; VT#1 |
| Tensor (spin-2, traceless) ↔ T^{μν} ("ungravity") | −Gm1m2/r [1+(R_G/r)^{2d_U−2}], α = 2/3 | formally r⁻⁴, **but d_U = 5/2 violates the paper's d_U > 3 for rank 2** | 0706.3898.txt:122-132, 143-144; VT#2 |
| Scalar ↔ trace T^μ_μ | Eq. 7 with (2−α)→2; requires d_U ≥ 2 | **r⁻⁴**; R_G ≲ 0.037 mm (Fig. 1 ≈ 0.038) | 0706.3898.txt:144-148, 157-159; VT#2, VT#3 |
| Tensor ungravity (astro reuse) | −G_U M/r [1+(R_G/r)^{2d_u−2}] (Eq. 6 printed with 2r) | r⁻⁴ (their bounds cover d_U≈1 only) | 0905.1602.txt:51-59, 44-45; VT#7 |
| Vector ↔ B (or L, B−L) current | V_U ∝ λ²Λ^{2−2d_U}/r^{2d_U−1}; 2d_U−2 = k−1 | r⁻⁴ (their table stops at d_U=2) | 0708.2735.txt:54-73, 116, 125-126; VT#4 |
| Scalar direct ↔ ψ̄ψ (electron) | U_non ⊃ −C_S² Γ(2d−2) A_d r^{1−2d}/(4π²) + O(r^{−1−2d}/m²) | leading **r⁻⁴** (subleading r⁻⁶) | 0706.1284.txt:87, 110, 149, 164; VT#5 |
| Scalar direct c_S1 f̄D̸f O_U (nucleon) | V_U = Cα_U B_iB_j/r^{2d_U−1}, α_U ∝ c_S1² m_im_j/M_Z^{2d_U} | **r⁻⁴** | 0708.4339.txt:108-111, 128-131; VT#6 |
| Scalar–scalar / vector (2023 reuse) | V_SS ∝ −C_S² r^{1−2d_U}; VV ∝ (1 mm/r)^{2d_U−1}, "k = 2d_U − 1" | r⁻⁴ | 2305.02628.txt:202, 541, 552-554, 573-586 |
| Review re-parametrization | V_N[1+(Λ/r)^n]; n = k−1; limits derived from Yukawa curves | n = 3 | 2605.18212.txt:131-141, 474-478 |

**Bottom line.**
- Every source uses one convention: an unparticle of dimension d_U exchanged between matter gives an extra potential ∝ r^{−(2d_U−1)}. That is k = 2d_U − 1 in Adelberger's β_k language, which puts d_U = 5/2 at **k = 4, total r⁻⁴**.
- The only primary β_4 bound is **|β_4| < 4.9 × 10⁻⁵ at 68% CL** (1 mm reference), from Adelberger et al. 2007. The Eöt-Wash 2020 paper gives Yukawa bounds only.
- Open items: the PRL typeset text of Goldberg–Nath and Nieto 1979 are **PIN OWED**. The exponent statements above do not depend on either.
