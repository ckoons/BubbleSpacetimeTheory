# R12 — Compact-circle pins: is a circle of radius ħ/(m_e c) excluded, and by how much?

Draft, 2026-09-27 11:29 EDT. Primary sources only, saved in this directory. Each pin gives file:line, from `pdftotext -layout` output unless marked PNG/VT, which means a transcription in `VISUAL_TRANSCRIPTIONS.txt`. The convention is quoted before each number.

Target: R_BST = ħ/(m_e c) = 3.8616e-13 m, so 1/R = 0.51100 MeV. That makes the first KK level m_1 = 1/R = 0.511 MeV, if R is the **radius** (y ~ y + 2πR).

## 0. Two corrections to the brief

- **arXiv:1606.04084 is not Deutschmann–Flacke–Kim.** It is Choudhury & Ghosh, "Bounds on Universal Extra Dimension from LHC Run I and II data", PLB, doi 10.1016/j.physletb.2016.10.010 (`1606.04084_abs.html`, citation_title/author meta). Deutschmann, Flacke, Kim, "Current LHC Constraints on Minimal Universal Extra Dimensions" is **arXiv:1702.00410**, PLB 771, 515 (2017) (`1702.00410_abs.html`). PDG cites 1702.00410 as its ref [171] for the 1.4–1.5 TeV mUED bound (`pdg2026_extra_dimensions.txt:892`). Both papers are saved and pinned.
- **The PDG 2026 R < 30 µm (δ = 2, 95% CL) sentence cites Ref. [23] = Tan et al., PRL 116, 131101 (2016)** (`pdg2026_extra_dimensions.txt:715`). It does not cite Lee et al. 2020. Lee 2020 is Ref. [24].

## 1. KK kinematics convention (the general rule)

**PDG 2026 RPP, "84. Extra Dimensions"** (rev. Aug 2025, Demiragli & Pomarol; `pdg2026_extra_dimensions.pdf`; citation line `:51`: "F. Takahashi et al. (Particle Data Group), Int. J. Mod. Phys. A 41, 2630011 (2026)").

- Convention, R is the radius. `:64-65`: "Let us now consider that the fifth dimension is compact with the topology of a circle S 1 of radius R, which corresponds to the identification of y with y + 2πR." Eq. (84.2) is the Fourier series e^{iny/R}.
- Mass. Eq. (84.5) (`:83-94`) gives the KK mass term (n/R)^2 |φ^(n)|^2, so m_n = |n|/R. `:100`: "At energies smaller than 1/R, the KK modes can be neglected".
- **Appelquist–Cheng–Dobrescu, PRD 64, 035002, hep-ph/0012100** (`hep-ph_0012100.txt`):
  - `:589`: "We consider first the case of a single extra dimension. Then Dj = 1 and Mj = j/R".
  - Universal case, KK-number conservation, `:59-65`: "The key element is the conservation of momentum in the universal dimensions. In the equivalent four-dimensional theory this implies KK number conservation. In particular there are no vertices involving only one non-zero KK mode, and consequently there are no tree-level contributions to the electroweak observables. Furthermore, non-zero KK modes may be produced at colliders only in groups of two or more."
  - **LEP rule (item 4)**, Sec. 4.1, `:747-749`: "Because of the KK number conservation, the KK states have to be produced in pairs or higher numbers. They can only be produced at LEP if their masses are less than ECM /2, ∼ 100 GeV."
  - At 1/R = 0.511 MeV, a KK electron pair has threshold ≈ 2·sqrt(m_e² + 1/R²) ≈ 1.45 MeV. That is 5 orders below LEP's reach (my arithmetic, not a source statement).
  - EW-precision bound (universal, 5D), Eq. (3.18), `:595-599`: "The current upper bound on isospin breaking effects, T ≲ 0.4, yields a lower bound on the compactification scale: 1/R ≳ 300 GeV." (2001 value.)
- **Not pinned.** No source found with a sentence of the form "UED with 1/R ~ MeV is excluded by LEP". The exclusion follows from the ACD pair-production rule plus kinematics. That step is our inference.

## 2. Universal extra dimension (all SM fields in the bulk): collider bound on 1/R

Convention (PDG 2026 `:661-663`): "Universal Extra Dimensions (UED) ... assumes that all SM fields propagate universally in a flat orbifold S 1 /Z2 with an extra Z2 parity, called KK-parity". R is the radius (Sec. 1). The paper's convention is the same: `1702.00410.txt:35` "universal in the sense that all Standard Model (SM) fields are promoted to fields which propagate on the full space-time M × X" and `:50` "compactification on the orbifold X = S 1 /Z2".

- **PDG 2026** `:670-673`: "A lower bound 1/R > 1.4 − 1.5 TeV was derived for ΛR in the range 5 − 35 [171]. A recent analysis is given in Ref. [173] where it is shown that the minimal UED model is ruled out when LHC data is combined with Dark Matter relic density data." The PDG 2024 wording is identical (`pdg2024_extra_dimensions.txt:651`, Sec. 85.3.4).
- **Deutschmann–Flacke–Kim 1702.00410**, CL 95%:
  - `:277-278`: "The mass scale up to R−1 = 1500 GeV can be excluded at 95% confidence level."
  - Conclusions `:324`, `:329`: "R−1 ≈ 1400 GeV excluded for Λ R ∼ 10. This limit is conservative in the sense that it does not include and K factor. For a K factor of 1.5, the limit would be increased to R−1 ≈ 1500 GeV."
  - Source: Fig. 3, whose caption (`:240-243`) reads "95% confidence level limit on the R−1 – Λ R plane from ATLAS and CMS searches performed at ... s = 13 TeV".
  - Resonant level-2 channel, `:70-71`: "KK photon mass of mA(2) ≳ 1.4 TeV, which corresponds to R−1 ≳ 715 GeV".
- **Choudhury–Ghosh 1606.04084**, 95% CL:
  - `:188-193`: "they exclude, at 95% CL ... for large ΛR ∼ 35, any R−1 below about 950 GeV is ruled out. However, for small ΛR ∼ 3 ... the lower bound on R−1 is only about 860 GeV".
  - 13 TeV, `:322-323`: "the strongest bound (R−1 ≳ 1110 GeV)" (Fig. 2, 95%).

## 3. Gauge bosons only in the bulk (fermions on a boundary): KK W, Z, γ

Convention (PDG 2026 `:650-652`): "assume that the SM gauge bosons propagate in a flat five-dimensional orbifold S 1 /Z2 of radius R, with the fermions localized on a 4D boundary. The KK gauge bosons behave as sequential SM gauge bosons with a coupling to fermions enhanced by a factor √2 [159]."

- Direct and LEP2 bounds, `:654-656`: "Such an interpretation of the ATLAS 7 TeV dilepton analysis [160] yielded the bound 1/R > 4.16 TeV, while a CMS 8 TeV search with a lepton and missing transverse energy in the final state [161] give 1/R > 3.4 TeV. Indirect bounds from LEP2 require however 1/R ≳ 6 TeV [86, 162]". PDG states no CL here.
- EWPT (Sec. 84.3.1.2, stated for 1/TeV-sized, mainly warped), `:454-460`: "Models in which the SM gauge bosons propagate in 1/TeV-sized extra dimensions give generically large corrections to electroweak observables ... the most relevant parameter is T̂, which gives the bound mKK ≳ 10 TeV [71]. When a custodial symmetry is imposed [80], the main constraint comes from the Ŝ parameter, requiring mKK ≳ 3 TeV".
- ACD's cross-reference for this class, `hep-ph_0012100.txt:50-53`: "if standard model fields propagate in extra dimensions, then they must be compactified at a scale 1/R above a few TeV [5]. These studies refer, however, to theories in which some of the quarks and leptons are confined to flat four-dimensional slices (branes)."

## 4. Gravity only in the bulk (Eöt-Wash and PDG)

Convention: a Yukawa-modified Newtonian potential. PDG `:169-176`: "V(r) = −GN m1 m2 /r [1 + α e−r/λ]. (84.12) For a 2-torus compactification, α = 16/3 and λ = R." Lee 2020 uses the same form (`2002.11761.txt:37`): "V (r) = VN (r)[1 + α exp(−r/λ)]". Its applicability, `:41-44`: "a reasonable approximation for the effects of extra dimensions as long as the minimum separation attained in the experiment is greater than the size of the largest extra dimension".

- **Lee et al., PRL 124, 101101 (2020), arXiv:2002.11761** (copied from `../../sources_grace_2026-09-26/r8_force/`; CL 95%, "2σ"). Body `:280-286`: "We find that any gravitational-strength Yukawa interaction must have λ < 38.6 µm. This implies that the dilaton or heavy graviton mass, and the radion unification mass must be greater than 5.1 meV and 7.1 TeV, respectively, and that the largest extra dimension[2] must have a toroidal radius less than 30 µm." "Gravitational strength" means α = 1. The 30 µm is a **toroidal radius** for the ADD case of their ref. [2] (Adelberger, Heckel, Nelson review, `:315`). Abstract `:11`: "limiting with 95% confidence any gravitational-strength Yukawa interactions to ranges < 38.6 µm."
- **PDG 2026** `:177-178`: "From Ref. [23] we have the constraint R < 30µm at 95% CL for δ = 2, corresponding to MD > 4.0 TeV." Here R is the torus radius (λ = R, α = 16/3).
- **Eöt-Wash web pages** (fetched 2026-09-27):
  - `eotwash_results.txt:28`: "This plot shows the 95% confidence level constraints on a Yukawa violation of the gravitational inverse-square law (as of 1/17/02)."
  - `eotwash_results.txt:32`: "The results constrain extra dimensions to be smaller than 150 um, for the particular case that there are two large extra dimensions of equal size". **This page is stale (2002).** The current number is the 2020 paper's.
  - `eotwash_isl_fresh.txt:21` is qualitative only: "these extra dimensions could be as big as a millimeter and no experiment would have detected them!" That sentence is historical framing, not a bound. The inverse-square-law page states no current number.
- **Relevance.** The gravity-only bound is 1/R > ħc/30 µm = 6.6 meV. R_BST is 7.8e7 times *smaller* than 30 µm, so this class does **not** exclude the BST circle. It also does not apply, because photon-sourcing fields in the bulk take the scenario out of "gravity only".

## 5. KK photon as a massive photon-like vector at 0.5 MeV with coupling of EM strength

Coupling convention (dark-photon literature). Fabbrichesi et al. (`2005.01515.txt:1772-1775`), Eq. (3.1): "L = −εeJ µ A0µ , where J µ is the electromagnetic current. The strength of this interaction is modulated by the parameter ε." For a KK photon with brane-localized charges, ε = √2 (PDG `:652`), so ε² = 2. **Caveat:** in the *universal* case, KK number conservation (ACD `:60-63`) forbids the tree-level γ^(1) e^(0) e^(0) vertex. In that case the Sec. 5 bounds, which all assume tree-level single-vector exchange, do not directly apply. The universal case falls to pair production (Sec. 1) and loops.

### 5a. Coulomb's law (Williams–Faller–Hill 1971)

- Metadata from `crossref_10_1103_PhysRevLett_26_721.json`: "New Experimental Test of Coulomb's Law: A Laboratory Upper Limit on the Photon Rest Mass", Williams, Faller, Hill, PRL 26, 721-724 (1971). The PRL itself is paywalled; the APS page `wfh1971_aps.html` is saved, but its body was not obtained.
- Convention (Fulcher, PRA 33, 759 (1986); VT V1; `png/fulcher1986-1.png`): "a parameter δ, which is introduced as a (possible) violation of Coulomb's law in the scale invariant form r^{−2+δ}."
- Number: Fulcher Table I, row "Williams, Faller, and Hill (1971) | Five concentric icosahedrons | (2.7 ± 3.1) × 10^−16". Fulcher's reanalysis, abstract and Eq. (9): "The new upper limit for δ is (1.0 ± 1.2) × 10^−16."
- Photon-mass form: Goldhaber & Nieto RMP 82, 939 (`0809.1003.txt:837-845`), Eq. (36): "the 35-year-old result of Williams, Faller, and Hill (83) remains the landmark test of Coulomb's Law. Their limit of λ̄C ≳ 2 × 10^7 m, or µ ≲ 10^−14 eV". PDG 2026 photon listing (`pdg2026_photon_listing.txt:58`): "< 1 × 10−14 [eV] ... WILLIAMS 71 Tests Coulomb's Law"; note 26 (`:153`): "WILLIAMS 71 is landmark test of Coulomb's law."
- **Relevance: none.** WFH probes a power-law δ, or a Yukawa of range ≳ 10^7 m, on a ~1 m apparatus. A 0.511 MeV KK photon has Yukawa range 3.86e-13 m. The factor e^{−r/R} at r ~ 0.5 m is e^{−1.3e12}, so WFH has no sensitivity. The number is recorded for completeness only.

### 5b. Hydrogen spectroscopy (Coulomb law at atomic scales)

- **Jaeckel & Roy, PRD 82, 125020, arXiv:1008.3536.**
  - Convention, Eq. (2.3) (`1008.3536.txt:108-111`): "the addition of a new Yukawa-type term to the Coulomb potential, V (r) = −Zα/r (1 + e−mγ′ r χ2 )". This is exactly the single-KK-mode potential with χ² → ε² (= 2 for n = 1 with brane charges).
  - Fig. 3 (2σ; VT V5): at m = 0.5 MeV, log10 χ ≈ −2.5 (**APPROX read-off**), so χ² ≲ 1e-5. ε² = 2 is excluded by roughly 2 × 10^5 in χ² (read-off grade).
  - Fig. 1 (VT V4) shows the 0.5 MeV column shaded up to χ = 1.
- **Fabbrichesi et al.**
  - Sec. 3.1.3 (`2005.01515.txt:2234-2239`, `:2332-2333`): "Atomic and nuclear experiments: These experiments aim to detect modifications of the Coulomb force ... Corrections in Rydberg atoms, Lamb shift and hyperfine splitting in atomic hydrogen have been translated into bounds on the massive dark photon mixing parameter [239]." Here [239] is Jaeckel–Roy (`:3504`).
  - Fig. 3.7 (VT V3): exclusion reaches the plot's top edge (ε = 1e-2) at 0.1–1 MeV.

### 5c. Electron g−2 (extra vector exchange), the cleanest numbered chain

- **Pospelov, PRD 80, 095002, arXiv:0811.1030** (Fabbrichesi's (g−2)_e reference [194], `:3397`).
  - Eq. (4) (`0811.1030.txt:115-123`): "a_l^V = (α/2π) × κ² ∫0^1 dz 2m_l² z(1−z)² / [m_l²(1−z)² + m_V² z] = (ακ²/2π) × {1 for m_l ≫ m_V ; 2m_l²/(3m_V²) for m_l ≪ m_V}". The coupling is κeJ_µV_µ (Eq. (3), `:101`), so κ ≡ ε.
  - Eq. (6) (`:175`): "κ² × F(m_e²/m_V²) < 15 × 10^−9", from α(g−2) vs α(Cs,Rb) at 15 ppb. This is the 2009 input.
- **Fan et al., PRL 130, 071801 (2023), arXiv:2209.13084.**
  - Eq. (6) (`2209.13084.txt:258`): "−µ/µB = g/2 = 1.001 159 652 180 59 (13) [0.13 ppt]".
  - Body (`:252-255`): "the best that can be said is that the predicted and measured µ/µB agree to about δ(g/2) = 0.7 × 10−12, half of the α discrepancy."
- **Fabbrichesi Eq. (2.33)** (`2005.01515.txt:1166-1168`): "The uncertainty on this difference (at 1σ) is given by [114] δ∆ae < 8.1 × 10−13."
- **Evaluation (my computation; integral of Pospelov Eq. (4) done numerically).**
  - At m_V = m_e: F = 0.2092. For the n = 1 mode with ε² = 2, a_e^V = (α/2π)·2·0.2092 = 4.86e-4.
  - Summing the tower m_n = n·m_e gives ΣF = 0.514, so a_e^V ≈ 1.19e-3.
  - Against δ(g/2) = 0.7e-12, **excess ≈ 7e8 (n = 1) to 1.7e9 (tower)**. Against Pospelov's Eq. (6) (15e-9), the excess is 2.8e7.
  - For ε² = 1: 3.5e8 and 1.4e7.

## Summary table

| Scenario (what propagates in the bulk) | Bound (convention) | CL | Source file:line | Bound ÷ 0.511 MeV (or R_BST vs bound) |
|---|---|---|---|---|
| mUED, all SM fields, S¹/Z₂, R = radius | 1/R > 1.4–1.5 TeV (ΛR 5–35) | 95% (paper) | pdg2026_extra_dimensions.txt:671; 1702.00410.txt:277-278, :324, :329 | 2.7e6 – 2.9e6 |
| mUED, 8 TeV soft dimuon | R⁻¹ ≳ 950 GeV (ΛR~35), 860 GeV (ΛR~3) | 95% | 1606.04084.txt:188-193 | 1.9e6 / 1.7e6 |
| mUED, 13 TeV multijet (early Run 2) | R⁻¹ ≳ 1110 GeV (low ΛR) | 95% | 1606.04084.txt:322-323 | 2.2e6 |
| UED, EW precision (T), 2001 | 1/R ≳ 300 GeV | T≲0.4 at 95% (`:474`) | hep-ph_0012100.txt:595-599 | 5.9e5 |
| UED, LEP pair-production reach (rule) | KK masses < E_CM/2 ~ 100 GeV producible | kinematic | hep-ph_0012100.txt:747-749 | ~2e5 (KK pair threshold 1.45 MeV ≪ 200 GeV) |
| Gauge bosons only (fermions on brane), direct | 1/R > 4.16 TeV (ATLAS 7 TeV); > 3.4 TeV (CMS 8 TeV) | not stated in PDG | pdg2026_extra_dimensions.txt:654-656 | 8.1e6 / 6.7e6 |
| Gauge bosons only, LEP2 indirect | 1/R ≳ 6 TeV | not stated | pdg2026_extra_dimensions.txt:656 | 1.2e7 |
| Gauge bosons in 1/TeV (mainly warped) ED, EWPT | m_KK ≳ 10 TeV (T̂); ≳ 3 TeV (custodial, Ŝ) | not stated | pdg2026_extra_dimensions.txt:458-460 | 2.0e7 / 5.9e6 |
| Gravity only (ADD δ=2, torus radius) | R < 30 µm (1/R > 6.6 meV) | 95% | pdg2026_extra_dimensions.txt:177-178 (Ref. [23] Tan 2016); 2002.11761.txt:286 | R_BST = 3.86e-13 m is 7.8e7× *below* the bound: **not excluded** |
| Gravity-strength Yukawa (α=1) | λ < 38.6 µm | 95% | 2002.11761.txt:11, :282 | 1.0e8× below: not excluded |
| Eöt-Wash web (stale, 2002, two equal EDs) | < 150 µm | 95% | eotwash_results.txt:28, :32 | n/a (superseded) |
| KK photon, brane charges, Coulomb law (WFH) | δ = (2.7±3.1)e-16 in r^{−2+δ}; µ_γ ≲ 1e-14 eV | 1σ quoted | VT V1 (fulcher Table I); 0809.1003.txt:837-845; pdg2026_photon_listing.txt:58 | **no sensitivity** at range 3.9e-13 m |
| KK photon, brane charges, H spectroscopy | χ ≲ ~3e-3 at 0.5 MeV (χ² ≲ 1e-5) | 2σ | 1008.3536.txt:108-111 (Eq. 2.3); VT V5 (Fig. 3, APPROX) | ε²=2 excluded by ~2e5 in χ² (read-off) |
| KK photon, brane charges, electron g−2 | a_e^V = (αε²/2π)F; data: δ(g/2) ≈ 0.7e-12 | ~1σ | 0811.1030.txt:115-123 (Eq. 4), :175 (Eq. 6); 2209.13084.txt:255, :258 | predicted/allowed ≈ 7e8 (n=1) – 1.7e9 (tower) |

## Verdict, stated as pins support it

- **What propagates decides it.** If all SM fields propagate on a circle of radius ħ/(m_e c), which is what "the photon's charged sources propagate" means, that is the UED class. It is excluded, and the bound on 1/R sits a factor **~3 × 10^6** above 0.511 MeV (PDG 1/R > 1.4–1.5 TeV, 95%). The earlier and weaker EW-precision (300 GeV) and LEP-kinematic (~100 GeV) statements still give factors of 2 × 10^5 to 6 × 10^5.
- If only the gauge field propagates and charges sit on a brane, the KK photon couples at √2 e. The direct and indirect bounds are 3.4–6 TeV, a factor of **~10^7**. A 0.5 MeV tower of that strength is excluded at low energy by electron g−2, overshooting by **~10^9**, and by hydrogen spectroscopy by ~10^5 in χ².
- **Only the gravity-only class permits a circle this small.** It bounds R from above, at 30 µm, not from below. That class does not describe a photon tower.
- **Open (not pinned):**
  - Explicit literature statement excluding MeV-scale UED at LEP.
  - The running of α from KK charged modes above 0.5 MeV. Power-law running would be a further, probably very strong, bound; no source is saved.
  - Exact reading of Jaeckel–Roy Fig. 3 at 0.5 MeV. The value is read-off grade.

## Files

- PDFs, with `.txt` from pdftotext -layout: 1606.04084, 1702.00410, 2002.11761, 2005.01515, 2105.04565, 0809.1003, 0811.1030, hep-ph_0012100, 1008.3536, 2209.13084, pdg2026_extra_dimensions, pdg2024_extra_dimensions, pdg2026_photon_listing, fulcher1986_PRA33_759.
- Abstract pages: `*_abs.html`.
- `crossref_10_1103_PhysRevLett_26_721.json` and `wfh1971_aps.html`.
- Eöt-Wash pages: `eotwash_results.html/.txt`, `eotwash_isl.html/.txt` (09-26 copy), `eotwash_isl_fresh.html/.txt` (09-27).
- `VISUAL_TRANSCRIPTIONS.txt` and `png/`.
- 2105.04565 (Caputo et al. handbook) was fetched but not pinned. Its scope is ultralight/haloscope DPs, and it has no statement at 0.5 MeV with ε ~ 1.
