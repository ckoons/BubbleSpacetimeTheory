# R7 PINS (draft) — Grace source-pin round 7

Written 2026-09-26 13:00 EDT. All files in this directory (`r7/`) unless prefixed `r6_tilt/` (= `../r6_tilt/`).
Text extractions: `pdftotext -layout` unless named `*_raw.txt` (`pdftotext` without -layout, used only where the layout table is interleaved).
Every quote below is verbatim from the named file:line. pdftotext flattens fractions/superscripts; where that happens the flattened text is quoted and the reading is stated separately as READING.

---

## 1. Nieto 1979 — hydrogen atom in N space dimensions

### 1a. Bibliographic identity — VERIFIED (primary metadata)
- `crossref_10.1119_1.11976.json`: title "Hydrogen atom and relativistic pi-mesic atom in <i>N</i>-space dimensions"; author Michael Martin Nieto (Theoretical Division, Los Alamos Scientific Laboratory); Am. J. Phys. vol 47, issue 12, pages 1067-1072, issued 1979-12-01. DOI 10.1119/1.11976 CONFIRMED.
- OSTI record 5728264 exists (`osti_5728264_record_pretty.txt`), but it is metadata-only: `links` holds only the citation page, no fulltext/purl, no LA-UR report number (`"report_number": "None"`). **No open copy found.** Content is paywalled at AIP.

### 1b. What Nieto's own abstract says (primary, author abstract via Crossref and OSTI)
`osti_5728264_record_pretty.txt:10` (identical text in the Crossref JSON `abstract` field):
> "We derive in simple analytic closed form the eigenfunctions and eigenenergies for the hydrogen atom in N dimensions. A section is devoted to the specialization to one dimension. Comments are made on the relation to the harmonic oscillator, the ground-state energy per degree of freedom, the raising and lowering operators, and the radial momentum operators."

**Nieto's energy formula, his definition of n and N, and his degeneracy formula: PIN OWED** (paper not open). The only thing pinned from Nieto himself is that N counts *space* dimensions (title: "N-space dimensions").

### 1c. SECONDARY — open sources that cite Nieto and print the formulas

**(i) Dehesa-group papers citing Nieto — energy formula.**

`2011.12242.txt` (arXiv:2011.12242, "Multidimensional hydrogenic states: Position and momentum expectation values"):
- Citation: line 63 "enormous interest in quantum chemistry and atomic and molecular physics [3, 20–30]," ; line 1367 "[30] M. M. Nieto, Am. J. Phys., 47 (1979) 1067."
- CONVENTIONS (quoted first): line 117-118 "Coulomb potential VD (r) = − Zr" [READING: V_D(r) = −Z/r — the 1/r potential in every D, *not* the Gauss-law r^{2−D}]; line 120 "Atomic units (i.e., ~ = me = e = 1) are used throughout the paper." ; line 132 "~r = (x1 , . . . , xD )" [D = number of SPACE dimensions].
- Formula, lines 139-143: "The position wavefunctions are characterized [2, 22] by the energetic eigenvalues known as / Z2 D−3 / E = − 2; η = n + , n = 1, 2, 3, . . . , (2) / 2η 2"
  READING: E = −Z²/(2η²), η = n + (D−3)/2, n = 1, 2, 3, …
- line 148: "l = 0, 1, 2, . . . , n−1"
- CAVEAT: Nieto is cited in the general-interest list (line 63), not at Eq. (2); Eq. (2) is attributed to [2, 22].

`0904.3001.txt` (arXiv:0904.3001, "Complexity of D-dimensional hydrogenic systems in position and momentum spaces"):
- Citation: line 811 "[5] M.M. Nieto, Amer. J. Phys. 47 (1979) 1067" — cited at line 44-45 "(e.g., qubits) / [5, 6]", again not at the energy formula.
- CONVENTIONS: line 92 "D-dimensional Coulomb (D ⩾ 2) potential V (~r) = − Zr"; line 98-99 "Atomic units / (ℏ = e = me = 1) are used throughout the paper."
- Formula, lines 101-102: "Z2 D−3 / E=− , with η =n+ ; n = 1, 2, 3, ..., (1) / 2η 2 2" — same READING as above.

`1409.8530.txt` (Bureš & Siegl, arXiv:1409.8530) cites Nieto as a source of the D-dim 1/|x| spectrum but prints no formula:
- lines 22-24: "Many existing works deal with a general case of d-dimensional hydrogen atoms with the potential proportional / to 1/|x|, irrespective of the number of spatial dimensions. A system defined in this way is indeed stable and / one can derive wave functions and their respective eigenenergies, see e.g. [1, 2, 3, 4, 5, 6]."
- line 609: "[3] M. M. Nieto, “Hydrogen atom and relativistic pi-mesic atom in N-space dimensions,” Am. J. Phys., vol. 47, pp. 1067–1072,"
- This is the best available attestation that Nieto's paper = the 1/r potential in d space dims (not Gauss-law r^{2−d}).

**(ii) Negadi & Kibler, arXiv:atom-ph/9512001 — energy + degeneracy + SO(D+1).** Does NOT cite Nieto (cites Alliluev, Bander–Itzykson, Čížek–Paldus, Mladenov–Tsanov: `atom-ph_9512001.txt:155`, refs lines 642-660). SECONDARY for the formula, not for Nieto.
- CONVENTIONS: line 81-82 "The Schrödinger equation for a D-dimensional hydrogen-like atom of nuclear charge / Ze (Ze > 0) and reduced mass µ reads"; line 88 "where ∆ is the Laplace operator and V the potential energy in D dimensions (D ≥ 2)."; line 90-92 "V = −Ze2/r" [flattened]; line 58 "a space-time with D spatial dimensions" [D = SPACE dims]; units: ħ, µ, e kept explicit (Gaussian).
- Energy, lines 155-160: "we obtain that the discrete energy spectrum is given by (cf. Refs. [31,32,36,38]) / E0 µ(Ze2 )2 / E = , E0 = − , N = nr + ℓ, N ∈ N. (10) / [N + 2 (D − 1)]2 / 1 2h̄2"
  READING: E = E₀/[N + (D−1)/2]², E₀ = −µ(Ze²)²/(2ħ²), N = n_r + ℓ = 0, 1, 2, …
- line 162: "(Observe that for D = 3, we have N = n − 1, / where n is the usual principal quantum number."
  => N + (D−1)/2 = n + (D−3)/2 with n = N+1: the two offsets are the SAME spectrum in two labelings. **Convention trap: "offset 3/2" (N from 0) vs "offset 1/2" (n from 1) for D = 4.**
- SO(D+1), lines 174-182: "The / quantity Λ2 in Eq. (11) turns out to be an eigenvalue of the second-order Casimir operator / of the special orthogonal group SO(D + 1) in D + 1 dimensions. ... Moreover, the energy formula (11) reflects the SO(D + 1) / dynamical symmetry of the Coulomb system in D dimensions."
- Degeneracy, lines 243-248: "the total degree of degeneracy g (covering essential and accidental degeneracies) of the / energy level E given by Eq. (10) is / (2N + D − 1) (N + D − 2)! / g ≡ g(N, D + 1) = , N ∈ N. (15) / N! (D − 1)!"
  READING: g = (2N+D−1)(N+D−2)!/[N!(D−1)!].
- lines 239-242: "the degree of degeneracy of E is equal to the degree of / degeneracy of the eigenvalue λ(λ + D + 1 − 2) of the second-order invariant of SO(D + 1). / The latter degree of degeneracy is given by Eq. (14a) with ℓ 7→ N and D 7→ D + 1"
- Checks printed: line 255-256 "g = 2N + 1 for / D = 2 and g = (N + 1)2 = (nr + ℓ + 1)2 = n2 for D = 3."
- Harmonic-polynomial identification, lines 223-226: "(14a) can / be simply obtained [34] ... as the difference between the dimension of the / space of the homogeneous polynomials with degree ℓ in RD and the dimension of the space / of the homogeneous polynomials with degree ℓ − 2 in RD"

**(iii) Bars & Rosner, arXiv:2001.08818 (`r6_tilt/2001.08818.txt`) — same spectrum + degeneracy, independently** (see Section 2 for conventions):
- lines 360-372: "The spectra / of the respective Hamiltonians in D dimensions are well known (using units c = 1, ~ = / 1, µ = 1) / ... − Zr ... Z2 / En ... − 2 , n = 1, 2, 3, · · · ... 2(n+ D−3 ... (7)" READING: E_n = −Z²/[2(n + (D−3)/2)²].
- line 379: "radial q.n. n = (1 + l + nr ) , nr = 0, 1, 2, · · ·"
- lines 417-419 (Eq. 9): "HatomD : l=0 Nl (D) = (D−1)! (n−1)! (2n + D − 3) = Nn−1 (D + 1) ," with "(n+D−3)!" [READING: Σ_{l=0}^{n−1} N_l(D) = (n+D−3)!(2n+D−3)/[(D−1)!(n−1)!] = N_{n−1}(D+1)]; identical to Negadi–Kibler (15) under N = n−1.
- lines 426-428: "For the HatomD ,the total degeneracy at each n matches the / dimension of the SO(D + 1) representation for the completely symmetric traceless tensor, / TI1 I2 ···In−1 , of rank (n − 1) in (D + 1) dimensions"
- line 866-867: "quantum ordering did produce a quantum shift of the integer n by the / amount (D − 3) /2. This result agrees with solving the HatomD radial differential equation,"

### 1d. D = 4 space dimensions — explicit values
- Hidden symmetry for D = 4 IS PRINTED: `r6_tilt/2001.08818.txt:1850` "The hidden symmetry of the Hatom4 is SO(5, 2)".
- Energy offset for D = 4: **INFERENCE** (substitution into the pinned formulas; not printed by any source on disk): η = n + 1/2 (n = 1,2,…) ≡ N + 3/2 (N = 0,1,…); E = −Z²/[2(n+½)²] in atomic units.
- Degeneracies for D = 4: **INFERENCE** (arithmetic on Negadi–Kibler Eq. (15) / Bars–Rosner Eq. (9), D = 4): g(N) = (2N+3)(N+1)(N+2)/6 → N = 0,1,2,3,4: **1, 5, 14, 30, 55**. = dim of degree-N harmonic polynomials on R⁵ (spherical harmonics on S⁴), per Negadi–Kibler lines 223-226 & 241 (D ↦ D+1 = 5) and Bars–Rosner lines 426-428 (symmetric traceless rank n−1 in D+1 = 5 dims). No source prints the numbers 1,5,14,30 for D = 4.

---

## 2. Bars & Rosner 2020 (arXiv:2001.08818) — SO(D+1,2) hidden symmetry

File `r6_tilt/2001.08818.txt` (sha256 already in `r6_tilt/SHA256SUMS.txt`).

CONVENTIONS (quote first):
- **D = number of SPACE dimensions of the H atom; D̄ = space dims of the oscillator.** line 35-36 "the Hydrogen atom / in D-dimensions and the harmonic oscillator in D̄ dimensions"; line 895 "The harmonic oscillator in D̄ space dimensions".
- **Title uses lower-case d = D + 1**: line 5 "via Hidden SO(d,2) Symmetry and 2T-physics"; line 2294-2295 "commuting symmetries Sp(2, R) ⊗SO(d, 2) of the action (A3), where d = D + 1 refers to the / spatial dimensions,". So SO(d,2) in the title ≡ SO(D+1,2) in the body. NOT SO(d,2) with d = space dims of the atom.
- Units: line 361-362 "(using units c = 1, ~ = / 1, µ = 1)".
- Symmetry of ACTION, not Hamiltonian: line 136-137 "have a common hidden symmetry SO(D + 1, 2) in their actions, beyond the symmetry of / Hamiltonians".

Pins:
- lines 135-141: "2T-physics predicts that these systems (and many other shadows) / have a common hidden symmetry SO(D + 1, 2) in their actions, beyond the symmetry of / Hamiltonians, and despite having different 1T Hamiltonians and different 1T actions, the / spectra of the respective Hamiltonians fit into the same unitary representations of the hid- / den SO(D + 1, 2) , with the same fixed Casimir eigenvalues Cn given in Eq. (A14) in the / Appendix."
- lines 174-175: "SO(D + 1, 2) for the HatomD ’s hidden symmetry of its action [34], and Sp 2D̄, R for / HOscD̄ ’s dynamical symmetry." [READING: Sp(2D̄, R)]
- lines 579-586: "The subgroup SO(D + 1) is the well known hidden symmetry for the HatomD ... The hidden symmetry SO(4) in Hatom3 , associated / with a conserved Runge-Lenz vector ... the SO(4) = SU(2) ⊗ SU(2) hidden symmetry / was embedded in the non-compact group SO(4, 2)"
- lines 588-593: "SO(D + 1, 2) is far more / than an algebraic tool; it is actually a hidden symmetry of the action (not Hamiltonian) for / the HatomD for any dimension D (see Eq. (20) in [34]) and for this reason the spectrum / of HatomD must be described in terms of irreducible representations of SO(D + 1, 2) ... Part of this symmetry, namely SO(D + 1) × U(1), is also a symmetry / of the HatomD Hamiltonian"
- line 894: "The HOscD̄ has a dynamical symmetry Sp 2D̄, R that controls its spectrum"
- Oscillator spectrum, line 370: "ω n̄ + D̄2" [READING: Ē = ω(n̄ + D̄/2)].
- Oscillator is NOT assigned SO(D+1,2) as its dynamical group: its group is Sp(2D̄,R); SO(D+1,2) is the shared hidden symmetry of the *actions* of all "shadows" (lines 135-141, 191-194). For D=3, D̄=4: lines 1364-1369 "this duality involves the non-compact groups SO(4, 2) and ... SO(4, 2) = SU(2, 2) is easily / recognized as a subgroup of Sp(8, R) ⊃ SO(4, 2) ⊗ U (1)".
- Representation: lines 2349-2352 "This is just a single infinite-dimensional unitary representation which is identified as the / “singleton” representation of SO(D + 1, 2)."
- Casimirs (A14), lines 2338-2347 (flattened): "C2 = 1 − 4 (D+1)2 , C3 = 3! 1 − 4 D+1 (D+1)2 ..." — READING OWED (fraction layout ambiguous; a render of page 46 needed before quoting a value; r6 has a page-26 render only).
- D = 4: line 1850 "The hidden symmetry of the Hatom4 is SO(5, 2)".

---

## 3. Källén–Lehmann density of a scalar of dimension Δ: ρ ∝ (μ²)^{Δ − d/2}

**Primary general-d pin: Dütsch & Rehren, arXiv:math-ph/0209035** (`math-ph_0209035.txt`, "Generalized free fields and the AdS-CFT correspondence").
- CONVENTIONS: **d = SPACETIME dimension** of the boundary CFT: line 73-74 "where Wm are the 2-point functions of the Klein-Gordon fields of mass m / in d-dimensional Minkowski space-time."; line 101-103 "free Klein- / Gordon field on d+1-dimensional Anti-deSitter space-time yields a Gaussian / conformal field in d-dimensional Minkowski space-time". KL weight defined line 70 "hΩ, ϕ(x)ϕ(x )Ωi = dρ(m2 ) Wm (x − x′ ) (1.1)" over R+ (line 71). Measure is in m² (dρ(m²)), not m.
- Formula, lines 103-108: "whose scaling dimen- / sion ∆ = d2 +ν depends on the Klein-Gordon mass M through the parameter / ν = 12 d2 + 4M 2 . Its 2-point function proportional to (−(x − x′ )2 )−∆ is a / superposition of all masses with Källen-Lehmann weight dρ(m2 ) = dm2 m2ν / (cf. Sect. 4)."
  Raw extraction confirms the fractions (`pdftotext -f 3 -l 3 -raw`): "sion ∆ = d / 2 +ν ... ν = 1 / 2 / √ / d2 + 4M2. Its 2-point function proportional to (−(x − x′)2)−∆ is a / superposition of all masses with Källen-Lehmann weight dρ(m2) = dm2m2ν".
  READING: Δ = d/2 + ν, ν = ½√(d²+4M²), dρ(m²) = dm² (m²)^ν = dm² (m²)^{Δ − d/2}. **This is the requested formula, with d = spacetime dimension.** In d = 4: (m²)^{Δ−2}.
- line 572: "We fix any value ν > −1 and set ∆ = d2 + ν and M 2 = ∆(∆ − d) = ν 2 − d4 ." [READING: Δ = d/2+ν, M² = Δ(Δ−d) = ν² − d²/4; range ν > −1 ⇔ Δ > d/2 − 1, the scalar unitarity bound.]

**4D confirmations (d_U / d = scaling dimension — convention trap: here "d" is NOT a dimension of spacetime):**
- Georgi, `r6_tilt/hep-ph_0703260.txt:151-159`: "h0| OU (x) OU (0) |0i = e−ipx |h0| OU (0) |P i|2 ρ P 2 (4) / (2π)4 ... Because of scale invariance, the matrix element (4) scales with dimension 2dU , which requires / that d −2 / |h0| OU (0) |P i|2 ρ P 2 = AdU θ P 0 θ P 2 P 2 U (5)" READING: |⟨0|O_U|P⟩|²ρ(P²) = A_{dU} θ(P⁰)θ(P²)(P²)^{dU−2}; spacetime is 4D (d⁴P, line 151).
- Stephanov, `r6_tilt/0705.3049.txt:65-67`: "By scale invariance the spectral function of the opera- / tor O must be a power of M 2 : / ρO (M 2 ) = AdU (M 2 )dU −2 , (2)"; spectral representation line 55-63 "d4 xeiP x h0|T O(x)O† (0)|0i ... = ρO (M 2 ) dM 2/2π i/(P 2 − M 2 + iε)". CAVEAT: Stephanov's "∆" (abstract, line 9) is the mass-spacing parameter, NOT the scaling dimension.
- Grinstein–Intriligator–Rothstein, `0801.1140.txt`: section is 4d only (line 128-129 "we discuss unitarity constraints on 4d CFTs"); their d = scaling dimension (line 92-94). Line 373-374: "Im Afwd = CS πg 2 (d − 1) / 4d−1 Γ(d)2 |χ| θ(k )θ(k 2 )(k 2 )d−2 . (4.4)"; line 383 "Using (d − 1)θ(k 2 )/(k 2 )2−d → δ(k 2 ) as d → 1"; line 387-388 "So d = 1 corresponds precisely to the / exchange of a single scalar particle, with k 2 = 0, corresponding precisely to a free field." Unitarity bound line 122 "scalar operators have dS ≥ 1".

---

## 4. X(6900) combined fit — arXiv:2604.18061

Title VERIFIED (`arxivabs_2604.18061.html` <title>; `2604.18061.txt:4-6`): "Enhanced evidence of X(7200) and improved measurements of X(6900) parameters from a combined LHCb-ATLAS-CMS analysis". Authors Yuan Wang, Ran Li, Bin Zhong, Ya-Qian Wang (line 8). Version on disk: line 18 "arXiv:2604.18061v2 [hep-ex] 28 May 2026"; line 1 "Submitted to Chinese Physics C". NOT a collaboration result — a phenomenological combination of *published* spectra (line 38 "using published data from LHCb, ATLAS, and CMS").

CONVENTIONS: masses in MeV/c², widths in MeV; errors quoted "± stat +syst −syst" in Table I (systematics = inverse-variance-weighted combination of the experiments' published systematics, lines 562-566). Line shapes: "S-wave relativistic BW amplitudes" (`2604.18061.txt:194` "combines signal components—modeled by S-wave relativistic BW amplitudes—with a"), phase-space factor sqrt(1 − 4M²_{J/ψ}/m²).

Table I (`2604.18061.txt:531-554`; raw-order cross-check `2604.18061_raw.txt:953-1013`):

| Model | Interference treatment | M_X(6900) (MeV/c²) | Γ_X(6900) (MeV) | signif. |
|---|---|---|---|---|
| I | none (incoherent BWs) | 6919.27 ± 2.90 +3.5 −3.6 | 70.25 ± 8.48 +19.8 −18.4 | 12.5σ |
| II | broad BW ⟷ SPS bkg (LHCb-style); 6900, 7200 isolated | 6903.10 ± 4.00 +9.6 −8.9 | 165.22 ± 14.00 +41.4 −36.8 | 15.6σ |
| III | X1, X2, X(6900) coherent; X(7200) incoherent | 6911.61 ± 7.60 +7.3 −7.0 | 112.74 ± 14.36 +28.6 −26.5 | 13.1σ |
| IV | X2, X(6900), X(7200) coherent; X1 incoherent (CMS scheme) | 6833.05 ± 13.98 +7.3 −7.0 | 161.31 ± 19.43 +28.6 −26.5 | 14.1σ |

(line 535-546 layout; the Model II width's +41.4 sits on the line above in the flattened text, line 542-543.) χ²/NDF line 554: "321.00/259 = 1.24 299.13/261 = 1.15 285.21/257 = 1.11 268.87/257 = 1.05".

Headline (best model):
- lines 598-601: "Among them, Model IV—which adopts the same three-resonance co- / herent interference scheme used by CMS [8]—yields the best fit (with a significance of / 6.6σ) and is considered the most physically representative."
- lines 613-614: "The best combined fit (Model IV) yields a mass of 6833±16 MeV/c2 for the X(6900) / and 7141±48 MeV/c2 for the X(7200)." [No combined width quoted in that sentence; Model IV width from Table I = 161.31 ± 19.43 +28.6 −26.5 MeV.]
- lines 585-586: "For the X(6900) state, the extracted mass ranges from 6833 to 6919 MeV/c2 across / the four models"
- line 602: "the fitted relative / phase between X(7200) and X(6900) in Model IV is ϕ = −0.79 ± 0.24 rad."
- lines 617-618: "the mass of the X(6900) is consistent with expectations for / a 1P -wave fully charmed tetraquark"

Inputs it quotes (lines 121-126, 137-144, 164-171): LHCb coherent M = 6886 ± 11 ± 11, Γ = 168 ± 33 ± 69; LHCb incoherent M = 6905 ± 11 ± 7, Γ = 80 ± 19 ± 33; ATLAS signal-interference M = 6910 ± 10 ± 10, Γ = 150 ± 30 ± 10; CMS "The X(6900) mass shifts from 6927±9±4 MeV/c2 (no interference) to 6847+44 +48 −28 −20 MeV/c2 (with interference)" and width "122+24 −21 ± 18 MeV to 191+66 +25 −49 −17 MeV" (flattened; READING of the sign pairing per layout lines 164-170).

Thresholds near 6.9 GeV: **NOT IN SOURCE.** grep of `2604.18061.txt` for χc / chi / ψ(2S) / 6926 / open-charm returns nothing; the only thresholds mentioned are the di-J/ψ threshold (line 92, 252, 464). The χc0χc1 (≈6926), χc1χc1, J/ψψ(2S) threshold values are **PIN OWED** (would need PDG masses pinned from the listings; not done this round).
Supplementary context on disk (PDG 2026 reviews, r6): `r6_tilt/rpp2026-rev-heavy-quarkonium-spectroscopy.txt:515` "Tccc̄c̄ (6900) X(6900) 6898 ± 12 161 ± 26 0+ (2++ ) pp → X... J/ψ(1S)J/ψ(1S) 2020 YES"; `r6_tilt/rpp2026-rev-non-qqbar-mesons.txt:566-567` notes "di-J/ψ(1S) / and J/ψ(1S)ψ(2S) invariant mass distributions" from CMS/ATLAS; lines 584-588 coupled-channel analyses where "the structures in the data emerge from the interplay of thresholds and resonances" — no numeric threshold values printed there either.

---

## Status summary
| Item | Status |
|---|---|
| Nieto DOI/biblio | VERIFIED (Crossref + OSTI) |
| Nieto formulas (E, n, N, degeneracy) | PIN OWED (paywalled; no OSTI/LA-UR fulltext) |
| D-dim H energy E = −Z²/[2(n+(D−3)/2)²], D = space dims, 1/r potential | SECONDARY — pinned in 2011.12242 & 0904.3001 (both cite Nieto, not at the formula), Negadi–Kibler, Bars–Rosner |
| Degeneracy g = (2N+D−1)(N+D−2)!/[N!(D−1)!] = dim SO(D+1) sym. traceless rank N | SECONDARY (Negadi–Kibler Eq. 15; Bars–Rosner Eq. 9) |
| D=4: offset ½ (n≥1) / 3/2 (N≥0); g = 1,5,14,30 | INFERENCE (substitution) |
| D=4 hidden symmetry SO(5,2) | PINNED (Bars–Rosner 1850) |
| SO(D+1,2) = hidden symmetry of H-atom action; title's SO(d,2) has d = D+1 | PINNED (Bars–Rosner) |
| Oscillator's dynamical group Sp(2D̄,R) (not SO(D+1,2)) | PINNED |
| Casimir values (A14) | READING OWED (render p.46) |
| KL weight dρ = dm² (m²)^{Δ−d/2}, d = spacetime dim | PINNED (Dütsch–Rehren lines 103-108, 572) |
| 4D (P²)^{dU−2} | PINNED (Georgi eq 5, Stephanov eq 2, GIR eq 4.4) |
| X(6900) combined: Model IV 6833 ± 16 MeV (headline), Γ 161.31 ± 19.43 +28.6 −26.5 | PINNED (phenomenological combination, not a collaboration) |
| Thresholds χc0χc1 etc. | PIN OWED |
