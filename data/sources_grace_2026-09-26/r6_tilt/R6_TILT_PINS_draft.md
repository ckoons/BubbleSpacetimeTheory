# R6 tilt / unparticle / carried pins: DRAFT

Written 2026-09-26 11:46 EDT (from `date`). Every pin is a verbatim quote from a file in this directory (or in `../shells/`), cited as file:line. The `.txt` files come from `pdftotext -layout` of the PDFs saved beside them, except the OCR files, which are marked. Quotes keep the extraction exactly as it came out, including garbled sub/superscripts. Where the OCR is garbled, the page was rendered to PNG and read by eye, and the reading is given as "[render: ...]". Anything that is my own arithmetic or inference is labelled **NOT A PIN**.

---

## 1. so(2,1) tilting treatment of the Coulomb problem

### 1a. arXiv:nucl-th/9801051: the tilt equations (PINNED, but note the scope)

- **Identity.** `nucl-th_9801051.txt:1` "Algebraic treatment of the hypercoulomb problem". Authors at :2–:14: "R. Bijker", "F. Iachello", "E. Santopinto". Published as J. Phys. A 31, 9041–9054 (1998), per `crossref_10_1088_0305_4470_31_45_004.json`.
- **Scope caveat (load-bearing).** This paper treats the **six-dimensional** hypercoulomb problem with dynamical group SO(7,2). It does **not** treat the 3-D hydrogen atom. `:56` "We consider the hypercoulomb potential in six dimensions". The SO(2,1) tilt mechanics carry over to 3-D, but the degeneracy labels (n = ω + 5/2) are the 6-D ones.

**Conventions, quoted before any formula.**
- Hamiltonian, `:58–:61`: "H = p²/2µ − τ/r" [layout-split], "with p² = Σ_{j=1}^6 p_j² and r² = Σ_{j=1}^6 r_j²".
- SO(2,1) generators, `:84` "L79 = ½ (rp² − r)", `:78–:82` "L78 = Σ_{k=1}^6 r_k p_k − 5i/2" [layout-split over lines 78–82], `:90` "L89 = ½ (rp² + r)". So **T3 − T1 = r and T3 + T1 = rp²** (this follows by reading the definitions at :140).
- `:140` "SO(2, 1) : T1 = L79 , T2 = L78 , T3 = L89     T² = T3² − T1² − T2²".
- Commutators, `:95` "[Lij , Lkl ] = −i (gik Ljl + gjl Lik − gil Ljk − gjk Lil )". Metric, `:99–:100`: "gij = −δij for j = 1, . . . , 7", "+δij for j = 8, 9". So the two time-like directions are 8 and 9, and T3 = L89 is the compact generator.
- Units: the paper states no ħ convention. ħ does not appear in eqs. (1)–(2), so ħ = 1 implicitly (**NOT A PIN**, this is an inference).
- Representation, `:158–:159`: "T² |ψ̃⟩ = q(q + 1) |ψ̃⟩ , (q real and < 0)", "T3 |ψ̃⟩ = q0 |ψ̃⟩ , (q0 = −q + s , with s = 0, 1, . . .)". This is the positive discrete series D⁺ (`:153–:154` "span the discrete rep- resentation D+ of SO(2, 1)").

**The tilt, verbatim** (`:237–:297`):
- `:237–:238` "The Schrödinger equation can be expressed in terms of the generators of SO(2, 1) by introducing"
- `:240` "O |ψ⟩ ≡ r(H − E) |ψ⟩ = 0 , (17)"
- `:244` "O = (1/2µ − E) T3 + (1/2µ + E) T1 − τ . (18)"
- `:246` "This equation can be simplified further by performing a rotation about a tilting angle θ"
- `:252–:255` "|ψ̃⟩ = N e^{−iθT2} |ψ⟩ , Õ = e^{−iθT2} O e^{iθT2} = (1/2µ − E) (T3 cosh θ + T1 sinh θ) + (1/2µ + E) (T1 cosh θ + T3 sinh θ) − τ . (20)"
- `:257–:258` **"The tilting angle may be chosen to diagonalize either the compact generator T3 for the bound states, or the noncompact generator T1 for the continuous states."** "The discrete spectrum is obtained by the choice"
- `:261` "tanh θ = (E + 1/2µ)/(E − 1/2µ) , (21)"
- `:263–:266` "which reduces Eqs. (19) and (20) to an eigenvalue equation of T3   ( √(−2E/µ) T3 − τ ) |ψ̃⟩ = 0 . (22)"
- `:270–:271` "E = − µτ²/2n² , (n = q0 = ω + 5/2) . (23)"
- `:275` "θ = − ln(n/µτ ) . (24)"
- `:284` "(note that the group metric is 1/r [15])"; `:289` "⟨ψ̃| e^{i ln(n/µτ) T2} (T3 − T1 ) e^{−i ln(n/µτ) T2} |ψ̃⟩"
- `:299` normalised states: "|ψ⟩ = (√(µτ)/n) e^{−i ln(n/µτ) T2} |ψ̃⟩ (27)"

**What the paper does NOT write out.** It gives no explicit E > 0 tilt angle and no T1 eigen-equation. The only continuum statement is the clause at `:257–:258`.
**NOT A PIN (my algebra):** setting the T3 coefficient of (20) to zero gives tanh θ = (E − 1/2µ)/(E + 1/2µ). For E > 0 its magnitude is below 1, so it can be realised. Eq. (21), by contrast, has magnitude above 1 for E > 0 and cannot be realised. The result is Õ ∝ (√(2E/µ) T1 − τ), a noncompact generator with continuous spectrum. This is consistent with the paper's sentence at :257, but the paper does not display it.

### 1b. Maclay, Symmetry 12(8) 1323 (2020): the SO(2,1) subgroup and the scale change (PINNED; no "tilt" word)

- **Identity.** `maclay_2020_symmetry_12_1323.txt:2–:7` "Dynamical Symmetries of the H Atom, One of the Most Important Tools of Modern Physics: SO(4) to SO(4,2), Background, Theory, and Use in Calculating Radiative Shifts" by "G. Jordan Maclay". Crossref: `crossref_10_3390_sym12081323.json`, DOI 10.3390/sym12081323.
- **Provenance.** mdpi.com returned "Access Denied" (Akamai) for both /htm and /pdf. The PDF was fetched from MDPI's own asset host `mdpi-res.com/d_attachment/symmetry/symmetry-12-01323/article_deploy/symmetry-12-01323.pdf` and saved as `maclay_2020_symmetry_12_1323.pdf`. This is the publisher's version of record.
- **The word "tilt" appears 0 times** in the paper (grep). Maclay's equivalent operation is the **scale change generated by S**.
- **Units**, `:3635` (ref. note 17): "We employ natural Gaussian units so h̄ = 1, c = 1, and α = (e²/h̄c) ≈ 1/137."
- **Compact vs noncompact, general**, `:583` "SO(4) and SO(3) are both compact groups, while SO(4,1) and SO(4,2) are non-compact".
- **Scattering states**, `:888–:889` "The scattering states with E > 0 form an infinite dimensional representation of the non-compact group SO(3,1)." This is in the classical Kepler/SO(4) section after eq. (39).
- **Schrödinger → Γ0 eigen-equation**, `:3008` "Γ0 = [K1(a)]⁻¹ = (1/2)(√r p² √r / a + ar)" [layout-split], `:3013` "(Γ0 − n) |nlm) = 0. (253)", `:3015` "This last equation is the Schrodinger equation expressed in our language of SO(4,2): our states |nlm) are eigenstates of Γ0 with eigenvalue n."
- `:3029` "Γ0 − Γ4 = ar     Γ0 + Γ4 = √r p² √r / a (255)". This is the same pattern as Bijker et al. T3 ∓ T1, with Maclay's ar ↔ r.
- **SO(2,1) subgroup**, `:3105` "2. Γ4 , S = S40 , Γ0 , forming a SO(2,1) subgroup. These operators commute with L but not with Γ0 , hence then can change n but not L or m." `:3112` "j1 = Γ4   j2 = S   j3 = Γ0 (267)"; `:3115` "[ j1 , j2 ] = −ij3 [ j2 , j3 ] = ij1 [ j3 , j1 ] = ij2 (268)"; `:3129` "Γ0 |nlm) = n|nlm)   (Γ4 ± iS)|nlm) = √(n(n ± 1) − l(l + 1)) |n ± 1 lm) (271)".
- **The scale change (Maclay's tilt)**, `:3136–:3139` "the operator S generates scale changes as shown in Equation (257), where the value of a is changed. We can also express the action of S equivalently as transforming Γ0 into Γ4   e^{iSλ} Γ0 e^{−iSλ} = Γ0 cosh λ − Γ4 sinh λ   e^{iSλ} Γ4 e^{−iSλ} = Γ4 cosh λ − Γ0 sinh λ. (273)"
- Dilation, `:1559` "D(λ) = e^{i ½ (p·r + r·p) λ} (109)".
- **Maclay's framework has no continuum, by construction**, `:1537–:1541` "(1) Because of the boundedness of K, there is no continuum portion in the eigenvalue spectrum of (Zα)⁻¹, the eigenvalues are discrete. … This feature leads to a unified treatment of all states of the hydrogenlike atom as opposed to the treatment in terms of energy eigenstates in which we must consider separately the bound states and the continuum of scattering states." Also `:646` "the kernel is bounded, which means that there are no states with E > 0, no scattering states".
- **Consequence for the brief.** Maclay does **not** state which SO(2,1) generator the scattering states diagonalise; the brief's "compact for bound / noncompact for scattering" is pinned from Bijker et al. :257, not from Maclay.

### 1c. Barut–Kleinert, Phys. Rev. 156, 1541 (1967), OCR on disk (PINNED: no tilt, has a dilatation)

- `../shells/kleinert_site_article_9.OCR.txt:5–:7` "Transition Probabilities of the Hydrogen Atom from Noncompact Dynamical Groups*", "A. O. Barut AND HAGEN KLEINERT".
- **No "tilt"/"tilting"** in this paper (grep 0 hits). It works with a dilatation operator:
  - `:246–:248` "where D, is defined as the dilatation operator by a, i.e.,   Daf (x)= fax). (15)" [OCR; reads D_a f(x) = f(ax)].
  - `:318–:320` "The dilatation operator is the one which causes transitions in » over the whole spectrum" [OCR "»" = n].
  - **SO(2,1)**, `:324–:326` "We also note that the operators Bt, B-, N occurring in the magnitude of the dipole operators generate an algebra isomorphic to SU (1,1)~O(2,1)." [OCR "Bt" = B⁺]
  - `:16` "becomes particularly simple by the introduction of a one-parameter family of representations of O(4,2)."
  - `:527–:529` "It is not clear yet how the dilatation operator can be found within the framework of a purely group-theoretical approach to dynamics."
- **The "tilting" operator is in Kleinert 1968** ("Group Dynamics of the Hydrogen Atom", lectures), `../shells/kleinert_1968_group_dynamics_H_atom.OCR.txt`:
  - `:802–:808` "The connection of the states Φ_nlm(ξ) with a Φ(ξ) can be given by the "tilting" operation (IV.45) with (IV.46)". The OCR is garbled; the equations are **[render: `kleinert_1968_page17_IV45-48_render110dpi.png`, printed p. 443] "T_n Φ̄_nlm(ξ) = Φ_nlm (IV.45)  with  T_n = e^{iθ_n L45}, θ_n = ℓn na. (IV.46)"**. The render also shows "e^{iθ_n L45} Φ̄_n(ξ) = (ch ℓn na − sh ℓn na ξ4)^{-2} Φ̄_n(ξ^{T_n})".
  - `:826–:827` "Observe that the tilter dilates the p in the wave function by p_n/a."
  - `:946–:948` "3) The physical states are given by the tilted and renormal- ized basis states of the representation. **A tilter is a non-compact rotational invariant group operation.**"

### 1d. arXiv:2001.08818, Bars & Rosner: hydrogen ↔ oscillator duality (PINNED; KS is NOT named)

- **Identity.** `2001.08818.txt:4–:5` "Duality Between Hydrogen Atom and Oscillator Systems via Hidden SO(d,2) Symmetry and 2T-physics", `:7` "Itzhak Bars† and Jonathan L. Rosner‡". Published J. Phys. A 53, 234001 (2020), per `crossref_10_1088_1751_8121_ab87ba.json`.
- **Units**, `:361–:362` "(using units c = 1, ħ = 1, µ = 1)".
- **Main statement**, `:135–:140` "2T-physics predicts that these systems (and many other shadows) have a common hidden symmetry SO(D + 1, 2) in their actions, beyond the symmetry of Hamiltonians, and despite having different 1T Hamiltonians and different 1T actions, the spectra of the respective Hamiltonians fit into the same unitary representations of the hidden SO(D + 1, 2), with the same fixed Casimir eigenvalues".
- **Dimension map**:
  - `:211–:215` "we established conclusively a one-to-one correspondence between a subset of quantum states of the HOsc_D̄ and all the quantum states of the Hatom_D. Based on this experience we conjecture the full duality satisfies D̄ = 2 (D − 1) for all D ≥ 2, with the same form of canonical transformation and dual quantum states. However, there is room for the formula for D̄ to be more general as we indicate for D ≥ 6".
  - `:1970–:1972` "D̄ = 2 (D − 1) , for 2 ≤ D ≤ 5, except for the case of D = 1 for which D̄ = 4. The pattern l̄ = 2l, along with D̄ = 2 (D − 1), may be taken as a conjecture for further investigations to determine D̄ once D ≥ 6 is given".
  - Table (76), `:1952–:1957`: "1 4 … Sp(8,R) ⊃ SO(2,2) ⊗ SU(2)"; "2 2 … Sp(4,R) ⊃ SO(3,2) ⊗ discrete"; "3 4 2complex Sp(8,R) ⊃ SO(4,2) ⊗ U(1)"; "4 6 4complex plus one constraint Sp(12,R) ⊃ SO(5,2) ⊗ U(1) ⊗ U(1)"; "5 8 4complex Sp(16,R) ⊃ SO(6,2) ⊗ SU(2)".
- **The 3 → 4 spinor map (KS-type).** `:1294–:1297` "we must take D̄ = 4 for the phase space vectors (r̄, p̄) of the HOsc4. This suggests to rearrange the 4 real components of r̄, which is a vector of SO(4), into two complex numbers of an SO(3) spinor". `:1311` eq. (50) **[render: `bars_rosner_2001.08818_page26_eq50-54_render100dpi.png`] "r^i = Z† (σ^i/2) Z, with z1 = r̄4 + i r̄3, z2 = −r̄2 + i r̄1"; "The second line yields |r| = |r̄|²/2, consistent with radial duality (1)"**.
- **Naming caveat.** The strings "Kustaanheimo", "Stiefel" and "KS" appear **0 times** in the paper (grep). The paper does not call this the KS transformation. The identification with KS is ours (**NOT A PIN**).
- **Dimension-convention caveat.** The paper's hydrogen dimension is D and the oscillator dimension is D̄. The brief's "d-dim hydrogen ↔ 2(d−1)-dim oscillator" matches D̄ = 2(D−1), which is **proved for D = 2, 3, 5** (`:1819–:1820`: "In the D = 2, 3, 5 cases we also note that we find D̄ = 2 (D − 1)"), **constructed with a constraint for D = 4**, and **conjectured for D ≥ 6**. The title's "SO(d,2)" is SO(D+1,2) in the body.

---

## 2. Georgi's unparticles and Stephanov's deconstruction (PINNED)

### 2a. Georgi, "Unparticle Physics", PRL 98, 221601 (2007), arXiv:hep-ph/0703260
File `hep-ph_0703260.txt`. DOI 10.1103/PhysRevLett.98.221601 (`crossref_10_1103_PhysRevLett_98_221601.json`).
- `:20–:21` (abstract) "I find that in the appropriate low energy limit, unparticle stuff with scale dimension dU looks like a non-integral number dU of invisible particles."
- `:37–:38` "Scale invariant stuff cannot have a definite mass unless that mass is zero. A scale transformation multiplies all dimensional quantities by a rescaling factor raised to the mass dimension so a nonzero mass is not scale invariant."
- `:46–:48` "In such an interacting scale invariant sector in four space-time dimensions, there are no particles because there can be no particle states with a definite nonzero mass. Scale invariant stuff, if it exists, is made of unparticles."
- `:111` "where dU is the scaling dimension of the unparticle operator OU".
- **Phase space**, `:157–:163` "Because of scale invariance, the matrix element (4) scales with dimension 2dU, which requires that |⟨0| OU(0) |P⟩|² ρ(P²) = A_dU θ(P⁰) θ(P²) (P²)^{dU−2} (5). This is the appropriate phase space for unparticle stuff. (5) should remind you of the phase space for n massless particles," followed by eq. (6), "… = A_n θ(P⁰) θ(P²) (P²)^{n−2}", and `:175` eq. (7) "A_n = 16π^{5/2} Γ(n + 1/2) / ((2π)^{2n} Γ(n − 1) Γ(2n))".
- **Boxed statement**, `:189–:191` "Unparticle stuff with scale dimension dU looks like a non-integral number dU of invisible particles. (9)"
- Normalisation convention: the paper adopts (7) for non-integral n as the normalisation of A_dU and calls this "purely conventional" (`:193–:195`).

### 2b. Georgi, "Another Odd Thing About Unparticle Physics", PLB 650, 275 (2007), arXiv:0704.2457
File `0704.2457.txt`. DOI 10.1016/j.physletb.2007.05.037.
- **Continuous-mass spectral representation**, `:74–:83` "In the notation of [1], the transverse 4-vector unparticle propagator is given by ∫ e^{iPx} ⟨0| T(O_U^µ(x) O_U^ν(0)) |0⟩ d⁴x = i (A_dU/2π) ∫_0^∞ (M²)^{dU−2} (−g^{µν} + P^µP^ν/P²)/(P² − M² + iε) dM² = i (A_dU/2) (−g^{µν} + P^µP^ν/P²)/sin(dU π) (−P² − iε)^{dU−2}" (eq. 3). `:85` gives A_dU as in 2a.
- `:108–:112` "while the discontinuity across the cut is not singular for integer dU > 1, the propagator (3) is singular because of the sin(dU π) in the denominator. I believe that this is a real effect. These integer values describe multiparticle cuts and the mathematics is telling us that we should not be trying to describe them with a single unparticle field. For this reason we will focus on 1 < dU < 2".
- Georgi does not use the words "continuous" or "continuum" in either paper (grep). The continuum is carried by the ∫_0^∞ dM² in eq. (3).

### 2c. Stephanov, "Deconstruction of Unparticles", PRD 76, 035008 (2007), arXiv:0705.3049 (the tower pin)
File `0705.3049.txt` (two-column; the text below is the column read in order, with the starting line of each fragment given). DOI 10.1103/PhysRevD.76.035008.
- Abstract, `:5–:7` "We discuss properties of hypothetical scale invariant (unparticle) matter by viewing it as a tower of massive particles. We show how peculiar properties of unparticles emerge in the limit when the mass spacing parameter ∆ vanishes. We explain why unparticle cannot decay in this limit".
- `:46–:47` "we deconstruct the unparticle and view it as an infinite tower of particles of different masses."
- `:55–:56` "We shall think of the unparticle as a limiting case in which the spacing ∆² of the (squared) masses in the tower of particles goes to zero."
- Spectral function, `:67` "ρ_O(M²) = A_dU (M²)^{dU−2}, (2)"; eq. (3) is ρ_O(M²) = 2π Σ_λ δ(M² − M_λ²) |⟨0|O(0)|λ⟩|².
- **Continuum statement**, `:79–:86` "The unparticle spectral function means that the spectrum of the operator O is continuous, i.e., the sum in Eq. (3) is in fact an integral. Let us imagine that the scale invariance is broken in the system in a controllable way, so that, instead of a continuous spectrum of states λ, there is a discrete tower of states with the spacing controlled by parameter ∆."
- **Tower**, `:89` "M_n² = ∆² n. (4)"; `:119` "In the limit ∆ → 0 the sum over n in Eq. (6) becomes an integral, which must match Eq. (2)."; `:124` "F_n² = (A_dU/2π) ∆² (M_n²)^{dU−2} (8)". Eq. (9) generalises to M_n² = ∆² n^{1/γ}.
- Coupling vs density, `:119–:121` (right column) "each of the deconstructing particles λn couples weaker and weaker as ∆ → 0 but their number in a fixed interval of energies dEu is increasing inversely proportionally to their coupling leading to finite dΓ/dEu in the scaling limit ∆ → 0."
- `:187` "a true (∆ = 0) unparticle, once produced, never decays."
- **Verbatim oddity (keep as printed).** `:90` has "which in the limit ∆ → ∞ merge into the continuum distribution". Given :56 and :119, this reads as a typo for ∆ → 0. **Do not cite :90 for the limit direction.**
- AdS realisation, `:24–:26` "the tower of deconstructing particles appears naturally as a Kaluza-Klein tower, once the extra dimension is compactified/truncated."

---

## 3. Carried pins

### 3a. Hadronisation time ~ 1/Λ_QCD with a number (PINNED from the preprint of the requested paper)
- Paper: Bigi, Dokshitzer, Khoze, Kühn, Zerwas, "Production and decay properties of ultra-heavy quarks", PLB 181 (1986) 157–163, DOI 10.1016/0370-2693(86)91275-X (`crossref_10_1016_0370-2693_86_91275-X.json`, 5 authors confirmed).
- Open copy: the preprint **SLAC-PUB-4021 / CERN-TH.4494/86 (July 1986)**, "Submitted to Physics Letters B", from INSPIRE record 231393 (`https://inspirehep.net/files/2d32cb89541dfcad0a7dc0134b537bb6`, saved as `slac-pub-4021.pdf`). **This is the preprint, not the journal typeset.** The text layer is OCR (garbled), so the quotes below were read from page renders.
- **Abstract**, `slac-pub-4021.txt:39–:41` [OCR "A$* - 1O-23 set"] **[render `slac-pub-4021_page02_render120dpi.png`]: "If the lifetimes become much shorter than the typical strong interaction time scale Λ_QCD⁻¹ ∼ 10⁻²³ sec, then open-flavor hadrons and quarkonium bound states cannot be formed any more."**
- **Hadronisation time, explicit**, `:242–:244` **[render `slac-pub-4021_page07_render120dpi.png`, p. 7]: "above which no more open-flavor hadrons can exist, i.e. Q decays before it can form a meson by picking up a light quark q: τ_Q < t_Had ∼ Λ_QCD⁻¹ ∼ 10⁻²³ sec."**
- `:255–:257` [render p. 7]: "the typical strong interaction time characterized by the confinement radius R_conf ∼ Λ_QCD⁻¹ ∼ 10⁻²³ sec".
- Convention: order of magnitude only ("∼"). No value of Λ_QCD is stated in these sentences. (**NOT A PIN**, arithmetic: ħ/(200 MeV) ≈ 3.3×10⁻²⁴ s ≈ 1 fm/c, which is consistent with "∼10⁻²³ sec".)

### 3b. T_bb (b b ū d̄) experimental status (PINNED as "prospects / ongoing", NOT as "no search published")
No primary source found that states verbatim "no dedicated search has been published". The closest primary statements:
- **PDG 2026, "78. Heavy Non-qq̄ Mesons"** (`rpp2026-rev-non-qqbar-mesons.pdf` from pdg.lbl.gov/2026/reviews/; `:6` "Revised October 2025 by T. Gutsche (Tübingen U.), C. Hanhart (FZ Jülich) and R.E. Mitchell (Indiana U.)"), `:551–:557`: "All those papers agree that a Tbb should be bound for the I = 0 and J^P = 1⁺ channel, but there is no consensus about the binding energy relative to the lowest open bottom threshold (BB*), which ranges from values near zero to 500 MeV. … no strong decay channels are accessible for the heavier partner states of the Tcc(3875) and they could only decay weakly. Accordingly, **once found**, they would provide an exciting laboratory". The phrase "once found" implies it has not been observed; the review cites no search.
- **PDG 2026, "Spectroscopy of mesons containing two heavy quarks"** (`rpp2026-rev-heavy-quarkonium-spectroscopy.txt`): its T_bb̄ entries are the hidden-bottom Z_b states (T_bb̄1(10610/10650), `:706–:711`), **not** the bb ū d̄ state. This review has no bbq̄q̄ entry.
- **LHCb Upgrade II Physics Case**, arXiv:1808.08865 (CERN-LHCC-2018-027), `1808.08865.txt:6248–:6254`: "Prompt production at LHC remains the best hope for unambiguously establishing the existence of stable, weakly decaying bbud tetraquark predicted by both lattice QCD and phenomenological models, which accurately predicted the mass of the recently detected Ξcc++ baryon [262]. However, the inclusive reconstruction efficiencies for such states are tiny due to the small branching fractions of B and D mesons decays to low multiplicity final states (Fig. 9.2, right)." Fig. 9.2 (right), `:6170`: "Xbbud → B D π decays".
- **Johnson, Polyakov, Skwarnicki, Wang, "Exotic Hadrons at LHCb"**, Ann. Rev. Nucl. Part. Sci. 74, 583 (2024), arXiv:2403.04051, `2403.04051.txt:1434–:1439`: "Run 3 and 4 will also make it possible to do detailed study of doubly-charmed exotic states, namely the Tcc+ and resonances in J/ψJ/ψ system, and to search for analogous states with beauty quarks. … and searches for other types of exotic states like tetra/pentaquarks decaying only weakly".
- **Most recent, Dai, Jia, Nefediev, Nieves, Shen, Zhang, "Exotic hadrons associated with b-quark"**, Phys. Rep. 1191 (2026) 1–62, arXiv:2603.09315v2 (18 Jun 2026), `2603.09315.txt:3213–:3215`: "LHCb is pursuing searches for open-bottom (bqqq), hidden-bottom (bb̄qq), and doubly-bottom (bbq̄q̄) candidates, as well as their pentaquark analogues, in prompt production. This program will continue throughout Run 3, Run 4, and into the HL-LHC era."
- **Honest form of the claim:** as of PDG 2026 and the June 2026 Phys. Rep. review, T_bb is unobserved ("once found"). LHCb describes doubly-bottom searches as **ongoing** ("is pursuing"), and none of these reviews cites a published result. "No published search" therefore has a **secondary basis only (absence from reviews)**. The supporting instrument is an INSPIRE query, `inspire_cnLHCb_t_tetraquark.json` (q = `cn LHCb and t tetraquark`, 7 hits, all charm or χc1(3872), no bb). It is a metadata search, **not a pin**. Also `inspire_search_tetraquark_bb_query.json` (1 hit, a lattice paper).

### 3c. Fock 1935, Z. Phys. 98, 145 (FOUND: open scan, PINNED from OCR)
- Crossref (already on disk): `../shells/crossref_10_1007_BF01336904.json` gives "Zur Theorie des Wasserstoffatoms", Z. Phys. 98 (3–4), 145–154, Fock.
- **Open copy.** Internet Archive item `sim_zeitschrift-fuer-physik-a-atoms-and-nuclei_1936_98` ("Zeitschrift für Physik 1936: Vol 98", microfilm serials collection, not access-restricted; metadata `ia_zphys_vol98_metadata.json`). Its full-text OCR is saved as `ia_zphys_vol98_1935-36_djvu.txt`. The 240 MB PDF was not downloaded; it is at archive.org/download/<id>/<id>.pdf if a render is wanted.
- Table of contents, `:163` "V. Fock, Zur Theorie des Wasserstoffatoms. (Eingegangen am 5. August 1935) 145".
- Title and header, `:12356–:12358` "Zur Theorie des Wasserstoffatoms¹). Von V. Foek [sic OCR] in Leningrad. (Eingegangen am 5. August 1935.)"; page footer `:12425` "Zeitschrift für Physik. Bd. 98. 10".
- **Abstract**, `:12361–:12364` "Die Schrödinger-Gleichung für das Wasserstoffatom im Impulsraum erweist sich als identisch mit der Integralgleichung für die Kugelfunktionen der vierdimensionalen Potentialtheorie. Die Transformationsgruppe der Wasserstoffgleichung ist also die vierdimensionale Drehgruppe; dadurch wird die Entartung der Wasserstoffniveaus in bezug auf die Azimutalquantenzahl l erklärt." (OCR errors silently normalised here: "Schrédinger", "fiir", "-ich", "limensionalen", "vleichung". The raw OCR is at the cited lines.)
- `:12385–:12386` "In dieser Arbeit wollen wir zeigen, daß diese Gruppe mit der vierdimensionalen Drehgruppe äquivalent ist."
- Convention, `:12416` "p0 = √(−2mE). (2)" [OCR "Po = V—2mE"]. "den mittleren quadratischen Impuls" (the mean-square momentum), with p/p0 used as stereographic coordinates on the unit 4-sphere.
- `:12705` "diese Gruppe ist offenbar mit der vierdimensionalen Drehgruppe identisch."
- **Continuum = hyperboloid (directly relevant to the tilt: compact for bound, noncompact for scattering)**, `:12916–:12937`: "5. Wir haben die geometrische Deutung der Integralgleichung für den Fall des Punktspektrums gegeben. Im Falle des Streckenspektrums (E > 0) hat man statt der Hyperkugel ein zweimanteliges Hyperboloid im pseudoeuklidischen Raume zu betrachten … **Im Falle des Punktspektrums herrscht im Impulsraum die Geometrie von Riemann mit konstanter positiver Krümmung, während im Falle des Streckenspektrums dort die Geometrie von Lobatschewski mit konstanter negativer Krümmung gilt.**" [OCR reads "(i > 0)" for (E > 0), and has "Hyperboloic", "Krimmung"; normalised here, raw at the cited lines.]
- Status: **PINNED (OCR of the journal scan)**. The quotes are OCR-normalised German; a page render from the IA PDF is still owed if byte-exact wording is needed.

---

## Retrieval log (where tried)
- MDPI Symmetry 12/1323: www.mdpi.com /htm and /pdf returned 403 "Access Denied". Wayback had no snapshots. **mdpi-res.com asset URL worked.** arXiv has no preprint of this review (the Maclay arXiv listing shows 1908.07343, 2306.01000 and 2305.18229, all different papers).
- The arXiv API (export.arxiv.org) returned empty bodies. arXiv abs/pdf pages worked.
- Fock: neo-classical-physics.info (Delphenich translations) has several Fock papers but not this one. Internet Archive advancedsearch found the Z. Phys. vol. 98 serial scan.
- Bigi et al.: the INSPIRE record carried the SLAC-PUB-4021 scan.

## Files (this directory)
PDFs+txt: nucl-th_9801051, maclay_2020_symmetry_12_1323, 2001.08818, hep-ph_0703260, 0704.2457, 0705.3049, 1808.08865, 2403.04051, 2603.09315, slac-pub-4021, rpp2026-rev-non-qqbar-mesons, rpp2026-rev-heavy-quarkonium-spectroscopy. OCR text: ia_zphys_vol98_1935-36_djvu.txt. Renders: slac-pub-4021_page02/07, kleinert_1968_page17, bars_rosner page26. Metadata: arxivabs_*.html, crossref_*.json, ia_zphys_vol98_metadata.json, inspire_*.json. Checksums: SHA256SUMS.txt.
