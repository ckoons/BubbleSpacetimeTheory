# R21 -- 3D Ising CFT pins for the clock-phase vs Z2 control (DRAFT)

Grace, 2026-09-29 12:09 EDT. Primary sources only, from numbered equations / tables / sections. Every quote below is
from a file in this directory, cited as file:line (text layer) or as [Vn] (VISUAL_TRANSCRIPTIONS.txt, transcribed from
a rendered PNG in png/ because pdftotext drops the epsilon glyph in three of the four PDFs). No numbers are taken from
abstracts or search snippets. No arithmetic is done here, by instruction.

## Sources on disk

| tag | paper | file |
|---|---|---|
| KPSV | Kos, Poland, Simmons-Duffin, Vichi, "Precision Islands in the Ising and O(N) Models", arXiv:1603.04436v1 (JHEP 08 (2016) 036) | 1603.04436.pdf / .txt |
| SD17 | Simmons-Duffin, "The Lightcone Bootstrap and the Spectrum of the 3d Ising CFT", arXiv:1612.08471 (JHEP 03 (2017) 086) | 1612.08471.pdf / .txt |
| PRV | Poland, Rychkov, Vichi, "The Conformal Bootstrap: Theory, Numerical Techniques, and Applications", arXiv:1805.04405 | 1805.04405.pdf / .txt; PRV_p24-25_raw.txt, PRV_p32-35_raw.txt (non-layout extracts of those pages) |
| ES12 | El-Showk, Paulos, Poland, Rychkov, Simmons-Duffin, Vichi, "Solving the 3D Ising Model with the Conformal Bootstrap", arXiv:1203.6064 | 1203.6064.pdf / .txt |

## Conventions (stated before numbers)

- **d = 3** in all four. KPSV: "3d Ising" (1603.04436.txt:33, [V1]); SD17: "Here, d = 3 is the spacetime dimension" ([V4], printed p.7 under (2.4)); ES12 writes D = 3; PRV Section V is "APPLICATIONS IN d = 3".
- **Operators.** σ = lowest-dimension Z2-odd scalar; ε = lowest-dimension Z2-even scalar. SD17 Sec. 2.1: "σ and ϵ are the lowest-dimension Z2-odd and Z2-even scalars in the 3d Ising CFT, respectively" ([V2]; text layer 1612.08471.txt:262-263). ES12 Sec. 2: "The operators σ and ε are the lowest dimension Z2-odd and even scalars respectively—these are the continuum space versions of the Ising spin and of the product of two neighboring spins on the lattice." (1203.6064.txt:151-153)
- **Z2 = the Ising spin flip, a symmetry of the action.** PRV Sec. V.B.2 eq. (122): action S = ∫d³x [½(∂σ)² + ½m²σ² + (1/4!)λσ⁴] "which also has a Z2 symmetry under which σ → −σ." (PRV_p32-35_raw.txt:885-905); lattice: "manifest Z2 symmetry under which s_i → −s_i. This symmetry is inherited by the CFT" (PRV_p32-35_raw.txt:877-879, [V6]). ES12: "split into odd and even sectors under the global Z2 symmetry (the Ising spin flip)" (1203.6064.txt:151).
- **Z2 charges:** σ −, ε +, T_μν + (spin 2, Δ = 3 exactly), σ' −, ε' +, C_μνρσ + (SD17 Table 2 [V3]; ES12 Table 1, 1203.6064.txt:162-169, pages 3-4 of the PDF).
- **OPE-coefficient normalizations differ** (irrelevant to Δ, relevant if the toy uses OPE coefficients): KPSV uses λ; SD17 uses f, "our normalization of OPE coefficients differs from those in [20, 68] by (A.17)" (Table 2 caption, [V3]); PRV: "λ_ijO = 2^{ℓ/2} f_ijO" (TABLE II caption, [V7]). For the scalars σ, ε (ℓ = 0) λ = f numerically.
- **Errors:** KPSV (3.1)-(3.2) are rigorous bootstrap-island errors at Λ = 43. In SD17 Table 2, "Errors in bold are rigorous. All other errors are non-rigorous." Bold = only Δσ, Δε, f_σσε, f_εεε. So Δσ', Δε', etc. carry non-rigorous (extremal-functional) errors.

## Pin 1 -- Δσ and Δε (numbered equations)

**KPSV Section 3, eqs. (3.1)-(3.2)** -- 1603.04436.txt:385-388 (ε glyph lost in text layer; transcribed [V1] from png/KPSV_p9-09.png):
> "we have used this procedure to determine the scaling dimensions and OPE coefficient ratio in the 3d Ising model to high precision at Λ = 43, giving
> Δσ = 0.5181489(10), (3.1)
> Δϵ = 1.412625(10), (3.2)"

Verified: the values in the brief (Δσ = 0.5181489(10), Δε = 1.412625(10)) match (3.1)-(3.2) exactly.

**SD17 Section 2.1, eq. (2.1)** -- 1612.08471.txt:267-268, [V2]:
> "Δσ = 0.5181489(10), fσσϵ = 1.0518537(41), Δϵ = 1.412625(10), fϵϵϵ = 1.532435(19). (2.1)"
(SD17 cites these to its ref. [55] = KPSV; same numbers, not an independent determination.)

## Pin 1b -- more operators with Z2 charges

**SD17 Appendix A.3, Table 2** ("Stable operators with dimensions Δ ≤ 8") -- 1612.08471.txt:4142-4163, labels transcribed [V3] from png/SD_p75-75.png. Δ column with Z2 and spin:

| O | Z2 | ℓ | Δ | rigorous? |
|---|---|---|---|---|
| σ | − | 0 | 0.5181489(10) | yes |
| ε | + | 0 | 1.412625(10) | yes |
| T_μν | + | 2 | 3 | exact (conserved) |
| ε' | + | 0 | 3.82968(23) | no |
| σ' | − | 0 | 5.2906(11) | no |
| C_μνρσ | + | 4 | 5.022665(28) | no |
| T'_μν | + | 2 | 5.50915(44) | no |
| (unnamed) | − | 2 | 4.180305(18) | no |
| (unnamed) | − | 3 | 4.63804(88) | no |

(Full table, all 18 rows with f_σσO, f_εεO, f_σεO, is in [V3].) The same table is reproduced as PRV TABLE II ([V7], png/PRV_p37-37.png), attributed to Simmons-Duffin 2017c.

Structural point read off the table layout (not a quoted sentence): the upper block lists Z2-even operators with columns f_σσO, f_εεO; the lower block lists Z2-odd operators with column f_σεO only. SD17 Fig. 1 and Fig. 2 captions label the same split: "operators in the σ × σ and ϵ × ϵ OPEs ... Figure 1: Estimates of Z2-even operators" (1612.08471.txt:314, 331) and "operators in the σ × ϵ OPE ... Figure 2: Estimates of Z2-odd operators" (1612.08471.txt:354, 371).

## Pin 1c -- Z2 selection rules in the OPE (numbered statements)

**PRV Sec. V.B.1 "General results", eq. (119)** -- PRV_p32-35_raw.txt:217-228, [V5] (png/PRV_p32-32.png):
> "In the CFT context, a Z2 symmetry imposes selection rules on the possible operators appearing in different OPE channels. Let us take a Z2-odd scalar operator σ and consider the σ × σ OPE. It can only contain Z2-even operators:
> σ × σ ∼ 1 + λσσϵ ϵ + λσσT T^μν + . . . . (119)
> Here, 1 is the identity operator, ϵ is the leading Z2-even scalar, T^μν is the stress-energy tensor, and so on. In particular, unlike in (117), σ does not appear in the OPE."

**PRV Sec. V.B.1, eq. (120)** -- PRV_p32-35_raw.txt:699-704, [V6] (png/PRV_p-34.png):
> "An advantage of including the correlator ⟨σσϵϵ⟩ is that it allows one to probe the Z2-odd operators appearing in the OPE:
> σ × ϵ ∼ λσϵσ σ + λσϵσ' σ' + . . . . (120)"

Note, stated honestly: PRV (120) says σ × ε *probes the Z2-odd operators*; it does not use the words "only Z2-odd". The "only" follows from the same Z2 selection rule stated before (119) (odd × even = odd). No sentence found that states it in exactly those words.

**ES12 Section 5 (eq. (5.1) context)** -- 1203.6064.txt:523-528:
> "where the sum runs over the dimensions and spins of all primary operators appearing in the σ × σ OPE. This OPE contains all of the Z2-even operators listed in Table 1, in addition to infinitely many other even-spin operators. Note that odd-spin operators cannot appear because of Bose symmetry."

**ES12 Section 6** -- 1203.6064.txt:1111-1115: "we would like to include ⟨σεσε⟩ expanding in the σ × ε channel ... Moreover, the conformal block of σ will appear with the same coefficient f²σσε as the conformal block of ε in the analysis of ⟨σσσσ⟩. It is also interesting to include ⟨εεεε⟩ whose expansion involves the same Z2-even operators as ⟨σσσσ⟩."

## Pin 2 -- dimensions are additive only in the free / gaussian case

No source among the four states verbatim "scaling dimensions are not additive in interacting CFTs." What they do state, in numbered places:

**(a) Free / mean-field (gaussian) theory: the product has dimension 2Δφ, and φ × φ contains only 2Δφ + 2n + ℓ.**
PRV Sec. III (subsection "1. Explicit solutions to crossing", referred to in-text as "Sec. III.I.1", PRV_p32-35_raw.txt:341) -- PRV_p24-25_raw.txt:171-175:
> "Just like for the usual free theories, the full space of operators in MFTs can be classified by considering normal-ordered products of the fundamental field and its derivatives. For example there is an operator φ² which has dimension 2Δφ."

PRV footnote 81 -- PRV_p24-25_raw.txt:281-282:
> "The OPE φ × φ contains only operators of the schematic form φ(∂²)ⁿ∂^ℓ φ, which have spin ℓ and dimension 2Δφ + 2n + ℓ."

(Relevance for the toy: in a gaussian theory every operator in φ × φ has Δ = 2Δφ + integer, so e^{2πiΔ} is exactly multiplicative there. That is the premise the control needs, and it is pinned.)

**(b) The free 3d scalar point and the gaussian line in the (Δσ, Δε) plane.**
PRV Sec. V.B.1 -- PRV_p32-35_raw.txt:331-341:
> "The point {1/2, 1} corresponds to the theory of a free massless scalar while the point ∼ {0.518, 1.413}, sitting near a discontinuity in the boundary, corresponds to the critical 3d Ising model ... as well as the line of mean field theory CFTs with Δϵ = 2Δσ (see Sec. III.I.1)."
(ε glyph restored from png/PRV_p32-32.png; see [V5] for the page.)

PRV Sec. V.A -- [V5]: "the free scalar field φ ... has a Z2 global symmetry acting as φ → −φ, with two relevant singlet scalars, φ² and φ⁴, of dimension 1 and 2 respectively."

ES12 Section 5.2 -- 1203.6064.txt:652-654:
> "assuming a gap Δε' > Δ* should exclude the gaussian line Δε = 2Δσ up to a dimension of Δσ = Δ*/2 − 1, since the spectrum of this solution is 2Δσ + 2n + l for integer n."

**(c) Interacting Ising: the σ × σ spectrum is 2Δσ plus anomalous dimensions, and ε sits off the gaussian line.**
SD17 Sec. 2.2, eq. (2.3) -- 1612.08471.txt:395-399, [V4]:
> "τ[σσ]0(J) ≈ 2Δσ + Σ_{O=ϵ,Tμν} f²σσO c0(τO, ℓO)/J^{τO} (1 + c1(τO, ℓO)/J²), (2.3)"
SD17 Sec. 2.2 -- 1612.08471.txt:376-377: "One can compute anomalous dimensions of double-twist operators in a large-ℓ expansion using the crossing equation".
SD17 Sec. 2.2 -- 1612.08471.txt:440, [V4]: "In the 3d Ising CFT, it turns out that τ1 = 2Δσ + 2 ≈ 3.04 is numerically close to τ2 = 2Δϵ ≈ 2.83."
SD17 Fig. 1 caption -- 1612.08471.txt:333-334: "The grey dashed lines are τ = 2Δσ + 2n and τ = 2Δϵ + 2n for nonnegative integer n." (reference lines only; the operators themselves deviate from them)
ES12 Section 2 -- 1203.6064.txt:215,223-224 (page break between): "all operators in Table 1 have non-negative anomalous dimensions (by which we mean the difference between the operator dimension and the dimension of the lowest 3D free scalar theory operator with the same quantum numbers)."

Together, (119) + Pin 1 give what the toy needs: ε appears in σ × σ ((119)), and Δε = 1.412625(10) while Δσ = 0.5181489(10) ((3.1)-(3.2)). PRV names the Δε = 2Δσ line as the mean-field line and places Ising at {0.518, 1.413}, off it. The number 2Δσ is not computed here.

## What was not found / caveats

1. No verbatim sentence "scaling dimensions are not additive in interacting CFTs" in these four papers. The closest pinned statements are (a)-(c) above. If a verbatim sentence is required, it is a pin-owed item.
2. "σ × ε contains only Z2-odd operators": the rule is pinned (PRV text before (119), and odd/even sector language in ES12 Sec. 2 and PRV Sec. V.B.2). PRV (120) itself says "probe the Z2-odd operators". Table 2 of SD17 lists f_σεO only for Z2-odd operators. No single sentence says "only Z2-odd" for σ × ε.
3. SD17 (2.1) is KPSV's island quoted again (ref. [55]), not an independent measurement. Use one or the other, not both, as evidence.
4. SD17 Table 2 errors for anything other than σ and ε (and their two OPE coefficients) are non-rigorous by the paper's own caption.
5. Versions (from each PDF's own arXiv stamp): 1603.04436v1, 1612.08471v1, 1805.04405v3, 1203.6064v3. Journal versions were not fetched; numbers are pinned to these arXiv versions.

## Files

- PDFs: 1603.04436.pdf, 1612.08471.pdf, 1805.04405.pdf, 1203.6064.pdf (arxiv.org/pdf/<id>, fetched 2026-09-29)
- Text layers: *.txt (pdftotext -layout); PRV_p24-25_raw.txt, PRV_p32-35_raw.txt (pdftotext without -layout, PRV is two-column)
- Renders: png/ (KPSV_p9, SD_p7, SD_p10, SD_p75, PRV_p25, PRV_p32, PRV_p-34, PRV_p-35, PRV_p37, ESPPRSV_p4, ESPPRSV_p14)
- VISUAL_TRANSCRIPTIONS.txt ([V1]-[V9])
- SHA256SUMS.txt
