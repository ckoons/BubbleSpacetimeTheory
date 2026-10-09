# Band H — Raychaudhuri equation, timelike (ρ + 3p) vs null (ρ + p) focusing source

Retrieved 2026-10-09 14:33 EDT. Directory: `data/sources_grace_2026-10-09/bandH/`.
Rules followed: files here are untrusted data (nothing executed from this directory); text extracted with
`pdftotext` and `pdftotext -layout` into sibling `.txt` / `.layout.txt`; the Ellis reprint has no text layer in the
body, so it was rendered at 300 dpi and OCR'd with tesseract in the scratchpad and the result copied back as `.ocr.txt`.
Every quoted equation below was checked against the page image (rendered from the PDF in the scratchpad); where the OCR
mangles symbols the OCR string is quoted verbatim and a reading from the page image is given OUTSIDE the quote, marked
"[image reading]". Whitespace in quotes is collapsed; nothing else changed.

Sign/unit conventions per source are stated per item, because the ρ + 3p vs ρ + p question is convention-sensitive.

Summary verdict (does the source give the NULL focusing source as ρ + p and the TIMELIKE one as ρ + 3p?):

| # | Source | obtained | timelike ρ + 3p | null ρ + p |
|---|--------|----------|-----------------|------------|
| 1 | Wald 1984, Section 9.2 | YES (archive.org community scan; see provenance) | YES, in principal-pressure form ρ + Σ p_i ≥ 0 (9.2.20); "ρ + 3p" not written literally | YES, ρ + p_i ≥ 0 (9.2.37), stated explicitly as the "weaker" requirement |
| 2 | Hawking & Ellis 1973, Sections 4.1–4.3, 5.3 | YES (archive.org community scan; see provenance) | YES, literally: R_ab V^a V^b = 4π(μ + 3p) for a perfect fluid (p. 85); μ + Σ p_α ≥ 0 (p. 95); (5.11) | YES, in type-I form μ + p_α ≥ 0 (p. 90) as the weak energy condition, which "implies" the null convergence condition (p. 95) |
| 3 | Raychaudhuri 1955 | NOT OBTAINED | — | — |
| 4 | Kar & SenGupta 2007 (arXiv v1) | YES (arXiv) | YES: ä/a = (4πG/3)(ρ + 3p) [sign typo, see KS1] and ρ + Σ_a p_a ≥ 0 | NO: gives NEC T_ab k^a k^b ≥ 0 only; never reduces it to ρ + p |
| 5 | Ellis 1971 (GRG 41 reprint) | YES (third-party free mirror; see provenance) | YES, literally, and LABELLED "active gravitational mass density ... μ + 3p" (p. 605) | NO as a null focusing source: μ + p > 0 appears only as a general restriction (3.8a) / energy condition; no null Raychaudhuri equation in the lectures |

Quote count: 34 numbered quotes (W1–W11, HE1–HE10, KS1–KS6, E1–E7).

---

## 1. Wald, General Relativity (1984), Section 9.2

**Files obtained:**
- `wald_1984_archiveorg_folkscanomy_text.pdf` (494 pp., "Additional Text PDF", 24 MB)
- `wald_1984_archiveorg_folkscanomy_djvu.txt` (archive.org OCR; quotes below are from this file)
- `wald_1984_archiveorg_folkscanomy_text.txt`, `wald_1984_archiveorg_folkscanomy_text.layout.txt` (pdftotext of the above)

**Provenance (flag):** archive.org item `general-relativity-r.-wald` (collection `folkscanomy`, uploader
said.siraj555@gmail.com, public date 2026-03-19). It is NOT a controlled-lending copy (no access restriction), but it is a
community-uploaded scan of a copyrighted book, not a publisher or university-course file. The library-lending copy
`generalrelativit0000wald` (Trent University, `printdisabled`/`inlibrary`) is access-restricted; its search-inside API
returned "Item not available", so it was NOT used. No university course PDF of Chapter 9 was found (three web searches).
Book page numbers below are the printed ones; PDF page = book page + 6.

**Bibliographic line:** Wald, R. M., *General Relativity*, University of Chicago Press, Chicago and London (1984),
Chapter 9 "Singularities", Section 9.2 "Timelike and Null Geodesic Congruences", pp. 216–224. Conventions: signature
(−+++), G = c = 1, Einstein's equation R_ab − ½ R g_ab = 8π T_ab, ξ^a unit timelike tangent, k^a affinely parametrised
null tangent.

**W1** (p. 218, eq. 9.2.11, djvu.txt line 12703–12704) — OCR verbatim:
> "Taking the trace of equation (9.2.10), we obtain EVE = d£ = -1e — Ono” + ww — Raft . (9.2.11)"

[image reading, PDF p. 224]: ξ^c ∇_c θ = dθ/dτ = −(1/3) θ² − σ_ab σ^ab + ω_ab ω^ab − R_cd ξ^c ξ^d . (9.2.11)
OCR artefacts: every symbol of the equation is garbled; the page image is unambiguous and matches the requested form.

**W2** (p. 218, djvu.txt 12728–12733) — OCR verbatim:
> "Equation (9.2.11) is known as Raychaudhuri’s equation and is the key equation used in the proof of the singularity theorems. We tum our attention, now, to investigate the positivity property of the last term on the right-hand side of this equation. Using Einstein’s equation, we may write this term as Rafe? = 87| Ta = Tea lee! = Bn] Tae + žr] - (9.2.15)"

[image reading]: R_ab ξ^a ξ^b = 8π [T_ab − ½ T g_ab] ξ^a ξ^b = 8π [T_ab ξ^a ξ^b + ½ T] . (9.2.15)
OCR artefacts: "tum" = "turn"; equation garbled.

**W3** (p. 218–219, djvu.txt 12737–12747) — OCR verbatim:
> "Now, Téng’ physically represents the energy density of matter as measured by an observer whose 4-velocity is £7. It is generally believed that for all physically reasonable classical matter this energy density is nonnegative, i.e., fe’ 20 (9.2.16) [page break: 9.2 Timelike and Null Geodesic Congruences 219] for all timelike °. This assumption is known as the weak energy condition."

[image reading]: T_ab ξ^a ξ^b ≧ 0 (9.2.16).

**W4** (p. 219, eq. 9.2.17, djvu.txt 12748–12758) — OCR verbatim:
> "However, it also seems physically reasonable that the stresses of matter will not become so large and negative as to make the right-hand side of equation (9.2.15) negative. This assumption that Totg = -3T (9.2.17) for all unit timelike ¿° is known as the strong energy condition."

[image reading]: T_ab ξ^a ξ^b ≧ −½ T (9.2.17). This is the requested "R_ab ξ^a ξ^b ≥ 0 ⇔ T_ab ξ^a ξ^b ≥ −T/2" sentence; the
equivalence is via (9.2.15) in W2.

**W5** (p. 219, djvu.txt 12770–12773 and footnote 12799–12800) — OCR verbatim:
> "In particular, the strong energy condition does not imply the weak energy condition.‘ It is “stronger” only in the sense that it appears to be a stronger physical requirement to assume equation (9.2.17) rather than (9.2.16)."
> "4. In some references, the terminology “weak energy condition” is defined to mean 7,,k°k° 2 0 for all null $°, With this definition, the strong energy condition does imply the weak energy condition."

[image reading of footnote]: T_ab k^a k^b ≧ 0 for all null k^a.

**W6** (p. 219–220, eqs. 9.2.18–9.2.20, djvu.txt 12786–12807) — OCR verbatim:
> "Ty = platy + PiXaXp + PrYaYo + Ps2Za%o , (9.2.18) where {t°, x°, y“, z°} is an orthonormal basis, with 4° timelike. The eigenvalue p may be interpreted as the rest energy density of the matter, while the eigenvalues p,, P2, ps ate called the principal pressures. For Ta of the form (9.2.18), the above energy conditions are equivalent to the following conditions. The weak energy condition will be satisfied if and only. if p20 and p+pm20 G=1,2,3) . (9.2.19) [page break: 220 Singularities] The<strong energy condition is equivalent to 3 p+ Spi =0 and pt+p,20 @=1,2,3) . (9.2.20) i=1 Thus, the weak and strong energy conditions will be satisfied provided only that p 20 and there do not exist negative pressures (i.e., tensions) comparable in magnitude or larger than p."

[image reading]: T_ab = ρ t_a t_b + p_1 x_a x_b + p_2 y_a y_b + p_3 z_a z_b (9.2.18); weak: ρ ≧ 0 and ρ + p_i ≧ 0 (i = 1, 2, 3)
(9.2.19); strong: ρ + Σ_{i=1}^{3} p_i ≧ 0 and ρ + p_i ≧ 0 (i = 1, 2, 3) (9.2.20). For a perfect fluid p_i = p this is ρ + 3p ≧ 0.
Wald does not write "ρ + 3p" anywhere in Section 9.2; the perfect-fluid specialisation is the reader's.

**W7** (p. 220, djvu.txt 12819–12826) — OCR verbatim:
> "Let us return now to Raychaudhuri’s equation (9,2.11). As discussed above, if Einstein’s equation holds, and the strong energy condition is satisfied by 7,,, then the last term of the right-hand side of equation (9.2.11) will be negative. This can be interpreted, physically, as a manifestation of the attractiveness of gravity. If the congruence is hypersurface orthogonal, we have w = 0, so the third term vanishes. The second term, —7,0”, is manifestly nonpositive."

**W8** (p. 220, Lemma 9.2.1, djvu.txt 12843–12849) — OCR verbatim:
> "Lemma 9.2.1. Let £* be the tangent field of a hypersurface orthogonal timelike geodesic congruence. Suppose Rak *k? = 0, as will be the case if Einstein’s equation holds in the spacetime and the strong energy condition is satisfied by the matter. If the expansion 6 takes the negative value 4 at any point on a geodesic in the congruence, then @ goes to —~ along that geodesic within proper time 7 = 3/| 6|."

[image reading]: R_ab ξ^a ξ^b ≧ 0; θ_0; θ → −∞; τ ≦ 3/|θ_0|. (OCR line numbers approximate; the lemma text is as on the image.)

**W9** (p. 222, eq. 9.2.32, djvu.txt 12966–12968) — OCR verbatim:
> "Finally, substituting our decomposition (9.2.26) for Bus and taking the trace, symmetric trace free, and antisymmetric parts of the equation, we obtain, respectively, dé č: A E | D = -3# - G38" + pP — Rak k? > (9.2.32)"

[image reading, PDF p. 228]: dθ/dλ = −½ θ² − σ̂_ab σ̂^ab + ω̂_ab ω̂^ab − R_cd k^c k^d , (9.2.32).
Also on p. 222 (image): "The change in the numerical factor in the term ½ θ ĥ_ab (as compared with ⅓ θ h_ab in the timelike
case) arises simply because the relevant vector space is now two-dimensional rather than three-dimensional."

**W10** (p. 223, eqs. 9.2.35–9.2.37, djvu.txt 12985–13008) — OCR verbatim:
> "The nature of equation (9.2.32) for the expansion of null geodesics is very similar to that of Raychaudhuri’s equation (9.2.11). The only significant change is that, using Einstein’s equation, we now obtain Rapk*k? = 8aTyk*k? . (9.2.35) Thus, all that is needed to ensure that the last term of equation (9.2.32) is nonpositive is that for all null k*, Takk’ Z0 . (9.2.36) If the strong energy condition, equation (9.2.17), holds, then for all timelike £* we have 7,£°¢° — 3T€*é, = 0, and by continuity equation (9.2.36) will hold for all null k*. Similarly, if the weak energy condition (9.2.16) holds, then by continuity equation (9.2.36) also will be satisfied. For a diagonalizable T}, equation (9.2.18), the necessary and sufficient requirement for satisfying equation (9.2.36) for all null k* is i ptp ž0 G@=1,2,3) . (9.2.37) Thus, the requirements on 7, needed to ensure that the last term of equation (9.2.32) is nonpositive are weaker than the corresponding requirements in the timelike case."

[image reading]: R_ab k^a k^b = 8π T_ab k^a k^b (9.2.35); T_ab k^a k^b ≧ 0 (9.2.36); T_ab ξ^a ξ^b − ½ T ξ^a ξ_a ≧ 0;
ρ + p_i ≧ 0 (i = 1, 2, 3) (9.2.37). For a perfect fluid this is ρ + p ≧ 0.

**W11** (p. 223, Lemma 9.2.2, djvu.txt 13012–13018) — OCR verbatim:
> "Lemma 9.2.2, Let £* be the tangent field of a hypersurface orthogonal null geodesic congruence. Suppose Rak *k? = 0, as will be the case if Einstein’s equation holds in the spacetime and the weak or strong energy condition is satisfied by the mattter. If the expansion 6 takes the negative value 4 at any point on a geodesic in the congruence, then @ goes to —~ along that geodesic within affine"

[image reading]: R_ab k^a k^b ≧ 0; ... within affine length λ ≦ 2/|θ_0|. ("mattter" sic in the original print.)

**Wald verdict.** Timelike: the focusing source is R_ab ξ^a ξ^b = 8π(T_ab ξ^a ξ^b + ½T), nonnegative iff the strong energy
condition, which for diagonalisable T_ab is ρ + Σp_i ≥ 0 and ρ + p_i ≥ 0 (9.2.20); perfect fluid ⇒ ρ + 3p ≥ 0 (not written
literally). Null: R_ab k^a k^b = 8π T_ab k^a k^b, nonnegative iff ρ + p_i ≥ 0 (9.2.37); perfect fluid ⇒ ρ + p ≥ 0; Wald says
explicitly the null requirement is "weaker than the corresponding requirements in the timelike case".

---

## 2. Hawking & Ellis, The Large Scale Structure of Space-Time (1973)

**Files obtained:**
- `hawking_ellis_1973_archiveorg_2025upload.pdf` (400 pp. scan with Acrobat text layer, 15 MB)
- `hawking_ellis_1973_archiveorg_2025upload_djvu.txt` (archive.org OCR; quotes below are from this file)
- `hawking_ellis_1973_archiveorg_2025upload.txt`, `.layout.txt` (pdftotext of the above)
- `hawking_ellis_1973_archiveorg_2024upload_djvu.txt` (OCR of a second, independent upload; kept as a cross-check only)

**Provenance (flag):** archive.org item `the-large-scale-structure-of-spacetime-1973-hawking-ellis` (collection
`opensource`, uploader hmsto@proton.me, 2025-10-17, description "Textbook"); the 2024 text is from item
`the-large-scale-structure-of-space-time-hawking-ellis` (uploader venkxg@gmail.com). Both are community uploads of a
copyrighted CUP book, unrestricted (not lending copies). The library-lending copies (`largescalestruct0000hawk`,
`largescalestruct0000unse_c8w2`) were not used. Book page = PDF page − 9.

**Bibliographic line:** Hawking, S. W. and Ellis, G. F. R., *The Large Scale Structure of Space-Time*, Cambridge Monographs
on Mathematical Physics, Cambridge University Press (1973). Chapter 4 "The physical significance of curvature": 4.1
Timelike curves (pp. 78–85), 4.2 Null curves (pp. 86–88), 4.3 Energy conditions (pp. 88–96); Chapter 5.3 Robertson–Walker
spaces (pp. 134–142). Conventions: signature (−+++), G = c = 1, field equations R_ab − ½ g_ab R + Λ g_ab = 8π T_ab, energy
density μ, pressure p; θ = expansion, s = proper time, v = affine parameter, V^a unit timelike, K^a null.

**HE1** (p. 84, eq. 4.26, djvu.txt 4691–4697) — OCR verbatim:
> "The trace of (4.25) is d i 6 = — Ry, VV? + 2u* — 202-462 + V2, , (4.26) where 2u? = w,,0" > 0, 207 = o,0% > 0."

[image reading, PDF p. 93]: (d/ds) θ = −R_ab V^a V^b + 2ω² − 2σ² − ⅓ θ² + V̇^a_{;a} , (4.26) where 2ω² = ω_ab ω^ab ≥ 0,
2σ² = σ_ab σ^ab ≥ 0. (HE's 2σ² equals Wald's σ_ab σ^ab, so the two forms agree.)

**HE2** (pp. 84–85, djvu.txt 4701–4712) — OCR verbatim:
> "This equation, which was discovered by Landau and independently by Raychaudhuri, will be of great importance later. From it one sees that vorticity induces expansion as might be expected by analogy with [page break: 4.1] TIMELIKE CURVES 85] centrifugal force while shear induces contraction. By the field equa- tions, the term R,, V°V® = 47(u+ 3p) for a perfect fluid whose flow lines have tangent vectors V*. Thus one would expect this term also to induce contraction. We shall give a general discussion of the sign of this term in §4.3."

[image reading, PDF p. 94]: "By the field equations, the term R_ab V^a V^b = 4π(μ + 3p) for a perfect fluid whose flow lines
have tangent vectors V^a." — this is the literal timelike ρ + 3p statement.

**HE3** (p. 88, eq. 4.35, djvu.txt 4904) — OCR verbatim:
> "<9 = — Ry, K*K® + 26? — 26% — 462, (4.35)"

[image reading, PDF p. 97]: (d/dv) θ̂ = −R_ab K^a K^b + 2ω̂² − 2σ̂² − ½ θ̂² , (4.35).

**HE4** (p. 88, djvu.txt 4909–4915) — OCR verbatim:
> "Equation (4.35) is the analogue of the Raychaudhuri equation for timelike geodesics. One sees again that vorticity causes expansion while shear causes contraction. We shall show in the next section that the Ricci tensor term — R,,K°K® will normally be negative, and so cause focussing. As before the Wey] tensor does not affect the expan- sion directly but causes distortion which in turn causes contraction (cf. Penrose (1966))."

**HE5** (p. 89, "The weak energy condition", image reading; the djvu OCR of this paragraph is intact except symbols):
> "The energy–momentum tensor at each p ∈ M obeys the inequality T_ab W^a W^b ≥ 0 for any timelike vector W ∈ T_p. By continuity this will then also be true for any null vector W ∈ T_p. To an observer whose world-line at p has unit tangent vector V, the local energy density appears to be T_ab V^a V^b. Thus this assumption is equivalent to saying that the energy density as measured by any observer is non-negative."

(PDF p. 98. Type I: T^ab = diag(p_1, p_2, p_3, μ) in an orthonormal basis with E_4 timelike; "The eigenvalue μ represents the
energy-density ... and the eigenvalues p_α (α = 1, 2, 3) represent the principal pressures".)

**HE6** (p. 90, djvu.txt 5024–5025) — OCR verbatim:
> "For type I, the weak energy condition will hold if 4 2 0, u+p, 2 0 (a = 1, 2, 3). For type IT it will hold if py, > 0,9, 20,K20,v=+1."

[image reading, PDF p. 99]: "For type I, the weak energy condition will hold if μ ≥ 0, μ + p_α ≥ 0 (α = 1, 2, 3)." For a
perfect fluid: μ + p ≥ 0. This is HE's null-side source condition (via HE7).

**HE7** (pp. 94–95, djvu.txt 5218–5236) — OCR verbatim:
> "For our consideration of singularities, the importance of the weak energy condition is that it implies that matter always has a converging (or more strictly nondiverging) effect on congruences of null geodesics. If the vorticity vanishes, the expansion 0 obeys the equation: d P 50 = — Bay Kok? — 26% 460. [page break: 4.3] ENERGY CONDITIONS 95] Thus in this case 6 will monotonically decrease along the null geodesic if R,, W*W® 2 0 for any null vector W. We shall call this the null convergence condition. From the Einstein equations, Rap — hap R+Agay = 87T iy, it follows that this condition is implied by the weak energy condition, independent of the value of A."

[image reading, PDF pp. 103–104]: (d/dv) θ̂ = −R_ab K^a K^b − 2σ̂² − ½ θ̂²; "if R_ab W^a W^b ≥ 0 for any null vector W. We shall
call this the null convergence condition. From the Einstein equations, R_ab − ½ g_ab R + Λ g_ab = 8π T_ab, it follows that
this condition is implied by the weak energy condition, independent of the value of Λ."

**HE8** (p. 95, djvu.txt 5238–5262) — OCR verbatim:
> "From (4.26) it can be seen that the expansion 6 of a timelike geodesic congruence with zero vorticity will monotonically decrease along a geodesic if R,, W*W® > 0 for any timelike vector W. We shall call this the timelike convergence condition. By the Einstein equation, this condi- tion will be satisfied if the energy-momentum tensor obeys the inequality, 1 T., WeW? > wow, (AP — = A). This will hold for type I if 1 H+P, 20, p+ p,—-Z A> 0, and for type II if v=+i, x20, p, 20, pp2O0 and Pit Pez 2 0. We shall say that the energy-momentum tensor satisfies the strong energy condition if it obeys the above inequality for A = 0. This is a stricter requirement than the weak energy condition but it is still physically reasonable for the total energy~momentum tensor. For the general case, type I, it would be violated only by a negative energy density or a large negative pressure (e.g. for a perfect fluid with density 1 gm cm it can only be violated if p < — 10 atmospheres)."

[image reading, PDF p. 104]: T_ab W^a W^b ≥ W^a W_a (½ T − (1/8π) Λ). "This will hold for type I if μ + p_α ≥ 0,
μ + Σ p_α − (1/4π) Λ ≥ 0, and for type II if ν = +1, κ ≥ 0, p_1 ≥ 0, p_2 ≥ 0 and p_1 + p_2 − (1/4π) Λ ≥ 0." ... "(e.g. for a
perfect fluid with density 1 gm cm⁻³ it can only be violated if p < −10¹⁵ atmospheres)". With Λ = 0 and p_α = p the type-I
condition is μ + 3p ≥ 0 — the timelike (strong) condition in perfect-fluid form; HE write it as μ + Σ p_α ≥ 0.

**HE9** (p. 136, eqs. 5.10–5.11, djvu.txt 7598–7602) — OCR verbatim:
> "The equation of conservation of energy (3.9) in these spaces takes the form f= —3(u+p)S']/8. (5.10) The Raychaudhuri equation (4.26) takes the form 4n(u+3p)—A = ~38"'/8. (5.11)"

[image reading, PDF p. 145]: μ̇ = −3(μ + p) Ṡ/S (5.10); 4π(μ + 3p) − Λ = −3 S̈/S (5.11). This is the Friedmann acceleration
form, i.e. S̈/S = −(4π/3)(μ + 3p) + Λ/3 with G = 1.

**HE10** (p. 137, djvu.txt 7652–7656) — OCR verbatim:
> "This singularity is the most striking feature of the Robertson— Walker solutions. It occurs in all models in which 4 + 3p is positive and A is negative, zero, or with not too large a positive value. It would imply that the universe (or at least that part of which we can have any physical knowledge) had a beginning a finite time ago."

[image reading, PDF p. 146]: "in all models in which μ + 3p is positive and Λ is negative, zero, or with not too large a
positive value."

**Hawking–Ellis verdict.** Timelike ρ + 3p: YES, literally (HE2: R_ab V^a V^b = 4π(μ + 3p) for a perfect fluid; HE8 general
form μ + Σp_α ≥ 0; HE9–HE10 the Friedmann form). Null ρ + p: YES in the sense that the null convergence condition
R_ab K^a K^b ≥ 0 "is implied by the weak energy condition" (HE7), whose type-I form is μ + p_α ≥ 0 (HE6), i.e. μ + p ≥ 0 for a
perfect fluid; HE do not write "μ + p" for the null case literally, nor R_ab K^a K^b = 8π(μ + p)(K·V)².

---

## 3. Raychaudhuri, A. (1955), "Relativistic Cosmology. I", Phys. Rev. 98, 1123–1126

**NOT OBTAINED.** Reason: APS paywall (DOI 10.1103/PhysRev.98.1123; ADS bibcode 1955PhRv...98.1123R). Searched: archive.org
(no scan), INSPIRE record 8888 (no document attached), three web searches for a course-site or mirrored scan
("PhysRev.98.1123", "Raychaudhuri_1955", "Relativistic Cosmology. I" + pdf) — only secondary sources returned. No
libgen-style mirror was tried, per the rules.

**Bibliographic line:** Raychaudhuri, A., "Relativistic Cosmology. I", *Physical Review* **98** (4), 1123–1126 (15 May 1955).

Secondary description of its content (Kar & SenGupta 2007, Section I.A, arXiv p. 3, from `kar_sengupta_gr-qc0611123.txt`),
quoted so the reader knows what the original contains without a pin:
> "(c) The quantity R44 (spacetime coordinates in the 1955 paper are labeled as x1 , x2 , x3 , x4 with the fourth one being time), is evaluated in two ways–once using the Einstein equations (with a cosmological constant Λ) and, again, using the geometric definition of R44 in terms of the metric and its derivatives. In the second way of writing this quantity, Raychaudhuri introduces the definitions of shear and rotation. (d) Finally, equating the two ways of writing R44 the equation for the evolution of the expansion rate is obtained."

The (ρ + 3p) term of the 1955 paper therefore remains PIN-OWED.

---

## 4. Kar, S. & SenGupta, S., "The Raychaudhuri equations: a brief review" (2007)

**Files obtained:**
- `kar_sengupta_gr-qc0611123.pdf` (arXiv:gr-qc/0611123v1, 23 Nov 2006, 35 pp.)
- `kar_sengupta_gr-qc0611123.txt`, `kar_sengupta_gr-qc0611123.layout.txt` (pdftotext)

The published Pramana PDF was NOT obtained (ias.ac.in returns HTTP 403 to non-browser clients; Springer copy paywalled), so
the sign typo in KS1 could not be checked against the journal version. Page numbers below are the arXiv v1 page numbers.

**Bibliographic line:** Kar, S. and SenGupta, S., "The Raychaudhuri equations: a brief review", *Pramana – J. Phys.* **69**
(1), 49–76 (2007); arXiv:gr-qc/0611123. Conventions: Θ expansion, λ affine parameter, v^a timelike tangent, k^a null tangent,
σ² = σ_ab σ^ab, ω² = ω_ab ω^ab (p. 11), Einstein equations written with 8πG = 1 in (12)–(17) and with 8πG explicit in (21).

**KS1** (p. 10, Section II.B(iii), `.txt` line 499–502; layout file 387–391) — verbatim:
> "It may be mentioned here that the equation for the expansion reduces to the equation for aä = 4πG (ρ + 3p). 3"

[image reading, PDF p. 10]: ä/a = (4πG/3)(ρ + 3p). FLAG: the arXiv v1 prints this WITHOUT the minus sign; the correct
Friedmann acceleration equation is ä/a = −(4πG/3)(ρ + 3p) (cf. HE9, E3). Treat as a typo; do not cite KS1 for the sign.
Preceding eq. (10) on the same page: "Θ = 3 ȧ/a = (1/√a⁶) d/dt √a⁶" (layout line 380).

**KS2** (p. 10, eq. 12, layout file 423–425) — verbatim (layout extraction, two lines merged):
> "dΘ 1 2 + Θ + σ 2 − ω 2 = −Rab v a v b (12) dλ 3"

[image reading]: dΘ/dλ + (1/3) Θ² + σ² − ω² = −R_ab v^a v^b (12). Followed on p. 11 by: "where σ 2 = σab σ ab , ω 2 = ωab ω ab ,
Ccbad is the Weyl tensor".

**KS3** (p. 11, `.txt` ~line 586–600) — verbatim:
> "There are a few points to note here. Firstly, one must realise that these are not equations but, essentially, identitites. Hence, in some references [22, 23, 24] we find the usage Raychaudhuri identity or Codazzi–Raychaudhuri identity ... The identities, however become equations once we use the Einstein equations or any other geometric property (e.g. Einstein space, or vacuum, etc.) as an extra input."

("identitites" sic.)

**KS4** (pp. 11–12, eq. 16 and SEC, `.txt` lines 620–650) — verbatim:
> "Using the well-known Sturm comparison theorems in the theory of differential equations one can show that convergence occurs if : Rab v a v b + σ 2 − ω 2 ≥ 0 (16) Thus, rotation defies convergence, while shear assists it. The equation for the evolution of the rotation ωab , has a trivial solution ωab = 0. The criterion for convergence then becomes particularly simple for such hypersurface orthogonal congruences (zero rotation) : Rab v a v b ≥ 0. This leads to geodesic focusing. If we make use of the Einstein field equations and rewrite the Ricci tensor in terms of the energy–momentum tensor Rab = Tab − 12 gab T the the so–called timelike convergence condition becomes a condition on matter stress energy. This, given as, Tab − 21 gab T v a v b ≥ 0 is known as the Strong Energy Condition (SEC). For a diagonal Tab (with T00 = ρ, Taa = pa ) we must have ρ + pa ≥ 0, ρ + P a pa ≥ 0 if the SEC is to be obeyed. In other words, geodesic focusing encodes the simple statement that if matter is attractive, geodesics must be eventually drawn towards each other."

[image reading]: R_ab = T_ab − ½ g_ab T (8πG = 1); (T_ab − ½ g_ab T) v^a v^b ≥ 0; ρ + p_a ≥ 0, ρ + Σ_a p_a ≥ 0. Artefacts: "12"/"21"
= ½; "P a" = Σ_a; "the the" is in the original. Perfect fluid ⇒ ρ + 3p ≥ 0 (not written literally).

**KS5** (p. 13, Section II.D, eq. 17, layout file 549–551 and `.txt` lines 680–686) — verbatim:
> "dΘ̂ 1 2 + Θ̂ + σ̂ 2 − ω̂ 2 = −Rab k a k b (17) dλ 2 where the hatted quantitites are the expansion, rotation and shear for the null geodesic congruence. The focusing theorem for null geodesic congruences follows in the same way as for timelike congruences, with the null convergence condition Rab k a k b ≥ 0 being the requirement. Using Einstein equations one can obtain the so–called Null Energy Condition Tab k a k b ≥ 0."

[image reading]: dΘ̂/dλ + ½ Θ̂² + σ̂² − ω̂² = −R_ab k^a k^b (17). ("quantitites" sic.) No perfect-fluid reduction (ρ + p) is given.

**KS6** (p. 17, Section III.A, eq. 21, layout file 691–694) — verbatim:
> "In GR, the SEC follows from the use of Einstein’s equations through the relation: Rab v a v b = 8πG Tab − T gab v a v b ≥ 0 (21) for all timelike v a . This, as mentioned before, leads to focussing."

[image reading]: R_ab v^a v^b = 8πG (T_ab − ½ T g_ab) v^a v^b ≥ 0 (21); the "½" fell out of the extraction.

**Kar–SenGupta verdict.** Timelike ρ + 3p: YES — the Friedmann form ä/a ∝ (ρ + 3p) (with a sign typo, KS1) and the SEC in
diagonal form ρ + Σ_a p_a ≥ 0 (KS4). Null ρ + p: NO — only the covariant NEC T_ab k^a k^b ≥ 0 is given (KS5); the perfect-fluid
reduction ρ + p ≥ 0 is never written (the "ρ + p_a ≥ 0" of KS4 is listed as part of the SEC, not the NEC).

---

## 5. Ellis, G. F. R., "Relativistic cosmology" (Varenna 1969/1971), reprinted GRG 41 (2009) 581

**Files obtained:**
- `ellis_1971_relativistic_cosmology_GRG41_581_isidore.pdf` (80 pp., Springer Golden Oldie PDF; body pages are scanned
  images of the 1971 Academic Press print, so pdftotext yields only running heads)
- `ellis_1971_relativistic_cosmology_GRG41_581_isidore.txt`, `.layout.txt` (pdftotext; headers/page numbers only)
- `ellis_1971_relativistic_cosmology_GRG41_581_isidore.ocr.txt` (tesseract OCR, 300 dpi, all 80 pages, with
  `===== PDF PAGE n (GRG 41 p. 580+n) =====` markers; quotes below are from this file)

**Provenance (flag):** isidore.co, "Physics papers and books/Cosmology/Relativistic Cosmology (Ellis)/" — a third-party free
mirror of the Springer reprint (not arXiv; the lectures are not on arXiv). Springer's own PDF (doi:10.1007/s10714-009-0760-7)
is paywalled. The file carries Springer's header and DOI and is complete (pp. 581–660). Note the lectures were given at
VARENNA (Enrico Fermi School, Course 47), not Cargèse, as the prompt had it.

**Bibliographic line:** Ellis, G. F. R., "Relativistic cosmology", in: Sachs, R. K. (ed.), *Proceedings of the International
School of Physics "Enrico Fermi", Course 47: General relativity and cosmology*, pp. 104–182, Academic Press, New York and
London (1971); republished as Golden Oldie, *Gen. Relativ. Gravit.* **41** (3), 581–660 (2009), DOI 10.1007/s10714-009-0760-7.
Conventions (p. 582/583 of reprint): signature (−+++); "The general-relativity notation and units we use are the same as
those used by Ehlers in this volume; in particular, note that we use units in which the speed of light is unity." The
coefficient ½ in front of (μ + 3p) in (4.12)–(4.13) is 4πG with 8πG = 1 (Ehlers' κ = 1). Throughout, Ellis prints the GR
equation on the left and its Newtonian analogue (primed number) on the right: μ = GR energy density, ρ = Newtonian/rest-mass
density, ε = specific internal energy, so μ = ρ + ερ.

**E1** (p. 595, Section 3.3.1, ocr.txt lines 699–713) — OCR verbatim:
> "33.1. General restrictions. A general restriction one would nor- mally put on the matter is that its energy density be positive. The restrictions of this kind we shall require the fluid to obey are (3.8a) w+ p>o, (3.8’) o>0. (3.8b) w+ 3p>0. (These restrictions will be used in Sect. 3°4 and 571.1). One would not expect (3.8') to be violated under any circumstances; (3.8a) and (3.8b) can only be violated, assuming yu is positive, if the pressure takes extremely large negative values. Thus if u is 1 g/cm’, (3.8a), (3.8b) can only be violated if p <— 10 atm (Gerocs [24])."

[image reading, PDF p. 15]: (3.8a) μ + p > 0, (3.8b) μ + 3p > 0 [GR, left column]; (3.8′) ρ > 0 [Newtonian, right column];
"(These restrictions will be used in Sect. 3·4 and 5·1.1)"; "p < −10¹⁵ atm (Geroch [24])".

**E2** (p. 605, Section 4.2.1, eq. 4.12, ocr.txt 1198–1205) — OCR verbatim:
> "42.1. Raychaudhuri’s equation. Contracting eqs. (4.10), (4.11) we obtain propagation equations for 6. g” X (4.10), (3.5) and (4.5) implies he” x (4.11) and (4.5’) implies (4.12) 6°+ 26?— a, +2(0?— 2) + (4.12') 6°+40?—a’, + 2(6?—wt) + +4(4+3p)—A=0, +te—-A=0, which is Raychaudhuri’s equation (RAYCHAUDHURI (38, 39])."

[image reading, PDF p. 25]: "4·2.1. Raychaudhuri's equation. Contracting eqs. (4.10), (4.11) we obtain propagation equations
for θ. g^ab × (4.10), (3.5) and (4.5) implies (4.12) θ̇ + ⅓ θ² − u̇^a_{;a} + 2(σ² − ω²) + ½(μ + 3p) − Λ = 0 ; [Newtonian:]
h^μν × (4.11) and (4.5′) implies (4.12′) θ̇ + ⅓ θ² − a^ν_{,ν} + 2(σ² − ω²) + ½ ρ − Λ = 0 , which is Raychaudhuri's equation
(Raychaudhuri [38, 39])." Here u̇^a_{;a} is the divergence of the 4-acceleration (the non-geodesic term); for geodesic flow
and with R_ab u^a u^b = ½(μ + 3p) − Λ this is HE1/W1.

**E3** (p. 605, eq. 4.13 and comment, ocr.txt 1206–1217) — OCR verbatim:
> "By (2.14), 6°+ 46? = 31°" /l, so we can rewrite this equation in the form (4.13) 31°" /l = 2(@* — 0?) + a, — (4.13’) 31°" /l = 2(w* 0?) + a”, — —4t(ut3p)+A. —tetA. This shows how the second derivative of the curve l(t) is determined directly at each space-time point by the matter density at that point, with the A-term acting as a constant repulsive force; rotation tends to hold the matter apart (as we might expect, representing a «centrifugal» effect); a pure distortion tends to pull the world-lines together; and acceleration affects the average distance of the world lines through its divergence."

[image reading]: θ̇ + ⅓ θ² = 3 l̈/l; (4.13) 3 l̈/l = 2(ω² − σ²) + u̇^a_{;a} − ½(μ + 3p) + Λ ; (4.13′) 3 l̈/l = 2(ω² − σ²) + a^ν_{,ν}
− ½ ρ + Λ. With l = a this is the Friedmann acceleration form ä/a = −(4πG/3)(μ + 3p) + Λ/3 (8πG = 1), with the correct minus
sign (contrast KS1).

**E4** (p. 605, ocr.txt 1219–1224) — OCR verbatim:
> "The main difference between the Newtonian and general-relativistic cases lies in the fact that while the active gravitational mass density is @ in Newto- nian mechanics, it is 4+ 3p = @ + e0+ 3p in general relativity. It is this additional pressure and internal energy contribution to the gravitational force which is the major cause of the problem of gravitational collapse in general relativity."

[image reading]: "while the active gravitational mass density is ρ in Newtonian mechanics, it is μ + 3p = ρ + ερ + 3p in
general relativity." — Ellis DOES use the label "active gravitational mass density" for μ + 3p.

**E5** (p. 605, static star, ocr.txt 1224–1232) — OCR verbatim:
> "Thus if we consider a static star model filled with a perfect fluid and take 1=0, (4.12) becomes iu, = 4(u + 3p), | a’,=te, where the acceleration is determined from the pressure gradient by (3.15). The extra terms in the relativistic case show that the pressure which tries to balance the star through acceleration tends to defeat itself, since it contributes directly to the gravitational field which tends to cause the star to collapse."

[image reading]: "take Λ = 0, (4.12) becomes u̇^a_{;a} = ½(μ + 3p), | a^ν_{,ν} = ½ ρ".

**E6** (p. 616, Fig. 3 caption, ocr.txt 1756–1757) — OCR verbatim:
> "Fig. 3. — If qgg>0 and the energy conditions n.+p>0, n+ 3p>0 are always ful- filled, then the age t, of an isotropic universe is less than 1/H)."

[image reading]: "If q_0 > 0 and the energy conditions μ + p > 0, μ + 3p > 0 are always fulfilled, then the age t_0 of an
isotropic universe is less than 1/H_0."

**E7** (p. 617, Fig. 4 caption, ocr.txt 1805–1807) — OCR verbatim:
> "Fig. 4. — The possible characteristics of the function 1(¢) in Robertson-Walker universes in which p+ p>0, w+ 3p>0 at all times. a) when A=0; 6) when 4<0; o) when A>O. The time reverses of these solution are also solutions."

[image reading]: "the function l(t) in Robertson-Walker universes in which μ + p > 0, μ + 3p > 0 at all times. a) when Λ = 0;
b) when Λ < 0; c) when Λ > 0."

**Ellis verdict.** Timelike ρ + 3p: YES, literally, in the Raychaudhuri equation (E2, E3) and labelled "active gravitational
mass density ... μ + 3p" (E4). Null ρ + p: NO as a null focusing source — the lectures contain no null Raychaudhuri equation
(Section 6.4.1 "The area law", p. 627, only quotes Sachs' d(dS)/dv = dS k^a_{;a}); μ + p > 0 appears as a general restriction
(3.8a) and in the Figure 3/4 captions as an "energy condition", never tied to R_ab k^a k^b.

---

## Cross-source consistency notes

1. Timelike equation: W1 (Wald 9.2.11), HE1 (4.26 with V̇^a_{;a} = 0), KS2 (12), E2 (4.12 with u̇^a_{;a} = 0) agree:
   dθ/dτ = −⅓θ² − σ_ab σ^ab + ω_ab ω^ab − R_ab ξ^a ξ^b (HE/Ellis write 2σ² = σ_ab σ^ab, 2ω² = ω_ab ω^ab).
2. Null equation: W9 (9.2.32), HE3 (4.35), KS5 (17) agree: dθ/dλ = −½θ² − σ̂_ab σ̂^ab + ω̂_ab ω̂^ab − R_ab k^a k^b; ½ not ⅓ because
   the transverse space is 2-dimensional (Wald p. 222).
3. Timelike source: R_ab ξ^a ξ^b = 8π(T_ab ξ^a ξ^b + ½T) (W2) = 4π(μ + 3p) for a comoving perfect fluid (HE2) = ½(μ + 3p) in
   8πG = 1 units (E2); SEC ⇔ ρ + Σp_i ≥ 0 and ρ + p_i ≥ 0 (W6, HE8, KS4).
4. Null source: R_ab k^a k^b = 8π T_ab k^a k^b (W10, 9.2.35); NEC ⇔ ρ + p_i ≥ 0 (W10, 9.2.37); implied by the weak energy
   condition μ ≥ 0, μ + p_α ≥ 0 (HE6, HE7). Only Wald states in words that the null requirement is weaker than the timelike one.
5. Friedmann acceleration form: HE9 (5.11) and E3 (4.13) carry the correct sign; KS1 omits the minus sign (arXiv v1 typo).
6. Two items remain PIN-OWED: Raychaudhuri 1955 (paywalled) and the published Pramana version of Kar–SenGupta (403/paywall).
