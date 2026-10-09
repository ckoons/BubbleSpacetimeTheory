# Band I primary source — Jacobson 1995, verbatim quotes

Retrieved 2026-10-09 14:54 EDT (system clock) by a retrieval subagent for Grace.

## File obtained

- `jacobson_1995_gr-qc9504004.pdf` — arXiv:gr-qc/9504004v2 (6 Jun 1995), downloaded from `https://arxiv.org/pdf/gr-qc/9504004`; 9 pages, 90623 bytes, PDF 1.4 (Ghostscript re-render dated 2024-11-26 by arXiv).
  - sha256: `85ed65e912baf62c27923dbf0e4b420ed444c4a253cb33f0a7763285b1271c4c`
- `jacobson_1995_gr-qc9504004.txt` — `pdftotext` (reading order) extraction.
- `jacobson_1995_gr-qc9504004_layout.txt` — `pdftotext -layout` extraction (used for the quotes below; page numbers are the arXiv version's printed page numbers, 1–8).

Untrusted data: nothing in this directory is executed.

## Bibliographic line

Jacobson, Ted. "Thermodynamics of Spacetime: The Einstein Equation of State." *Physical Review Letters* **75**, 1260–1263 (1995). arXiv:gr-qc/9504004v2 (6 Jun 1995); preprint UMDGR-95-114, Department of Physics, University of Maryland, College Park. DOI: 10.1103/PhysRevLett.75.1260.

Note: PRL page numbers are NOT printed in the arXiv version; all page numbers below are the arXiv preprint's own pagination. Equation numbers (1)–(6) are as printed in the arXiv version.

## Extraction artefact conventions

Whitespace collapsed only. The PDF-to-text extractor renders the sub/superscripts flat: `Tab` = T_ab, `ka` = k^a, `kb` = k^b, `χa` = χ^a, `dΣb` = dΣ^b, `θ 2` = θ², `σ 2` = σ², `σ ab σab` = σ^{ab} σ_{ab}, `η −1/2` = η^{−1/2}, `(h̄G)1/2` = (ħG)^{1/2}, `T −1` = T^{−1}, `lc2` = l_c². The display-integral sign comes out as a stray `Z` on the line above the equation and the integration domain `H` comes out as a separate line below; the fraction 1/2 in eqs (4) and (6) comes out as a `1` above and `2` below the line. Rendered (de-artefacted) readings are given outside each quote.

---

## Quote 1 — Abstract (p. 1)

> "The Einstein equation is derived from the proportionality of entropy and horizon area together with the fundamental relation δQ = T dS connecting heat, entropy, and temperature. The key idea is to demand that this relation hold for all the local Rindler causal horizons through each spacetime point, with δQ and T interpreted as the energy flux and Unruh temperature seen by an accelerated observer just inside the horizon. This requires that gravitational lensing by matter energy distorts the causal structure of spacetime in just such a way that the Einstein equation holds. Viewed in this way, the Einstein equation is an equation of state. This perspective suggests that it may be no more appropriate to canonically quantize the Einstein equation than it would be to quantize the wave equation for sound in air."

Artefacts: none.

## Quote 2a — Heat-flux definition, eq. (1) (p. 4)

> "Consider now any local Rindler horizon through a spacetime point p. (See Fig. 1.) Let χa be an approximate local boost Killing field generating this horizon, with the direction of χa chosen to be future pointing to the "inside" past of P. We assume that all the heat flow across the horizon is (boost) energy carried by matter. This heat flux to the past of P is given by Z δQ = Tab χa dΣb . (1) H (In keeping with the thermodynamic limit, we assume the quantum fluctuations in Tab are negligible.) The integral is over a pencil of generators of the "inside" past horizon H of P."

Artefacts: `Z` = integral sign; `H` on its own = the subscript of the integral (integration over the horizon H). Rendered: δQ = ∫_H T_ab χ^a dΣ^b.  (1)

## Quote 2b — Killing-vector form, eq. (2) (p. 4)

> "If ka is the tangent vector to the horizon generators for an affine parameter λ that vanishes at P and is negative to the past of P, then χa = −κλka and dΣa = ka dλdA, where dA is the area element on a cross section of the horizon. Thus the heat flux can also be written as Z δQ = −κ λ Tab ka kb dλdA. (2) H"

Artefacts: as in 2a. Rendered: χ^a = −κλ k^a, dΣ_a = k_a dλ dA; δQ = −κ ∫_H λ T_ab k^a k^b dλ dA.  (2)

Context (same page, p. 4, on the temperature and the heat current, verbatim): "the Minkowski vacuum state of quantum fields—or any state at very short distances— is a thermal state with respect to the boost hamiltonian at temperature T = h̄κ/2π, where κ is the acceleration of the Killing orbit on which the norm of χa is unity (and we employ units with the speed of light equal to unity.) The heat flow is to be defined by the boost-energy current of the matter, Tab χa , where Tab is the matter energy-momentum tensor."

## Quote 3a — Area-change equation, eq. (3) (pp. 4–5)

> "Assume now that the entropy is proportional to the horizon area, so the entropy variation associated with a piece of the horizon satisfies dS = η δA, where δA is the area variation of a cross section of a pencil of generators of H. The dimensional constant η is undetermined by anything we have said so far (although given a microscopic theory of spacetime structure one may someday be able to compute η in terms of a fundamental length scale.) The area variation is given by Z δA = θ dλdA, (3) H where θ is the expansion of the horizon generators."

Artefacts: as above. Rendered: δA = ∫_H θ dλ dA.  (3)  (Sentence begins on p. 4, "Assume now that the entropy is proportional to the horizon area, so the"; continues on p. 5.)

## Quote 3b — Raychaudhuri equation, eq. (4), and its integration into eq. (5) (p. 5)

> "The equation of geodesic deviation applied to the null geodesic congruence generating the horizon yields the Raychaudhuri equation dθ 1 = − θ 2 − σ 2 − Rab ka kb , (4) dλ 2 where σ 2 = σ ab σab is the square of the shear and Rab is the Ricci tensor. We have chosen the local Rindler horizon to be instantaneously stationary at P, so that θ and σ vanish at P. Therefore the θ 2 and σ 2 terms are higher order contributions that can be neglected compared with the last term when integrating to find θ near P. This integration yields θ = −λ Rab ka kb for sufficiently small λ. Substituting this into the equation for δA we find Z δA = − λ Rab ka kb dλdA. (5) H"

Artefacts: the fraction 1/2 is split (`1` above, `2` below); `θ 2`, `σ 2` = θ², σ². Rendered: dθ/dλ = −(1/2)θ² − σ² − R_ab k^a k^b  (4); θ = −λ R_ab k^a k^b; δA = −∫_H λ R_ab k^a k^b dλ dA  (5).

## Quote 4 — The result: Clausius relation forces the Einstein equation; Λ as undetermined constant (pp. 5–6)

> "With the help of (2) and (5) we can now see that δQ = T dS = (h̄κ/2π)η δA can only be valid if Tab ka kb = (h̄η/2π) Rab ka kb for all null ka , which implies that (2π/h̄η)Tab = Rab + f gab for some function f . Local conservation of energy and momentum implies that Tab is divergence free and therefore, using the contracted Bianchi identity, that f = −R/2 + Λ for some constant Λ. We thus deduce that the Einstein equation holds: 1 2π Rab − Rgab + Λgab = Tab . (6) 2 h̄η"

(p. 5; eq. (6) is the last display on p. 5.)

> "The constant of proportionality η between the entropy and the area determines Newton's constant as G = (4h̄η)−1 , which identifies the length η −1/2 as twice the Planck length (h̄G)1/2 . The undetermined cosmological constant Λ remains as enigmatic as ever."

(p. 6, first paragraph.)

Artefacts: in eq. (6) the fraction 1/2 and 2π/ħη are split across lines (`1 2π` above, `2 h̄η` below); `(4h̄η)−1` = (4ħη)^{−1}. Rendered: R_ab − (1/2) R g_ab + Λ g_ab = (2π/ħη) T_ab  (6), i.e. 8πG T_ab with G = (4ħη)^{−1}. Note for the caller: the paper does NOT literally use the words "integration constant" for Λ; the exact wording is "f = −R/2 + Λ for some constant Λ" (p. 5) and "The undetermined cosmological constant Λ remains as enigmatic as ever." (p. 6). Also the paper's own statement of the result is T_ab k^a k^b = (ħη/2π) R_ab k^a k^b, not written as 1/8πG; the 1/8πG form follows only after the identification G = (4ħη)^{−1} on p. 6.

## Quote 5 — Null energy flux drives the horizon area change (p. 5)

> "The content of δQ = T dS is essentially to require that the presence of the energy flux is associated with a focussing of the horizon generators. At P the local Rindler horizon has vanishing expansion, so the focussing to the past of P must bring an expansion to zero at just the right rate so that the area increase of a portion of the horizon will be proportional to the energy flux across it. This requirement imposes a condition on the curvature of spacetime as follows."

Artefacts: none ("focussing" is the paper's spelling).

Supporting statement of the same point, p. 4 (verbatim): "The fundamental principle at play in our analysis is this: The equilibrium thermodynamic relation δQ = T dS, as interpreted here in terms of energy flux and area of local Rindler horizons, can only be satisfied if gravitational lensing by matter energy distorts the causal structure of spacetime in just such a way that the Einstein equation holds. We turn now to a demonstration of this claim."

And p. 3 (verbatim): "So far we have argued that energy flux across a causal horizon is a kind of heat flow, and that entropy of the system beyond is proportional to the area of that horizon."

## Supplementary — scope caveats stated by the author (useful for a Band I audit)

p. 6, verbatim: "Changing the assumed entropy functional would change the implied gravitational field equations. For instance, if the entropy density is given by a polynomial in the Ricci scalar α0 + α1 R + ..., then δQ = T dS will imply field equations arising from a Lagrangian polynomial in the Ricci scalar[9]."

p. 6, verbatim: "Our thermodynamic derivation of the Einstein equation of state presumed the existence of local equilibrium conditions in that the relation δQ = T dS only applies to variations between nearby states of local thermodynamic equilibrium."

p. 3, verbatim: "Different accelerated observers will obtain different results. In the limit that the accelerated worldline approaches the horizon the acceleration diverges, so the Unruh temperature and energy flux diverge, however their ratio approaches a finite limit. It is in this limit that we analyse the thermodynamics, in order to make the arguments as local as possible."

Figure 1 caption (p. 8, verbatim): "FIGURE 1: Spacetime diagram showing the heat flux δQ across the local Rindler horizon H of a 2-surface element P. Each point in the diagram represents a two dimensional spacelike surface. The hyperbola is a uniformly accelerated worldline, and χa is the approximate boost Killing vector on H."

## Quote count

Requested items 1–5: 7 primary verbatim quotes (1; 2a; 2b; 3a; 3b; 4 as two paragraphs; 5), plus 7 supplementary verbatim passages (context for 2b, two supporting statements under 5, three scope caveats, figure caption). All taken from `jacobson_1995_gr-qc9504004_layout.txt`, page numbers as printed in the arXiv v2 PDF.
