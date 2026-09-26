# Grace R164 — Round 5: exotics at their thresholds, T_bb against the proximity rule, the kaon line convention-matched, the shell and spectral-dimension pins; register v0.27
*2026-09-26 (Saturday), round 5 (Keeper's prompt of 09-25 19:11 + Addenda 1–5). Toys 5802 (7/7, sha c9099963) and 5803 (5/5, sha bfba045b), hashed before running. Every number was pinned from a saved source, with file:line, under `data/sources_grace_2026-09-26/` (text files and checksums, no PDFs). `didwe` was run first: 0 prior rows on exotics / f_K/f_π / top lifetime. The one hit, 'hydrogen SO(4,2)' → K1878 STOP, read energies; this lane reads structure only (Casey 19:42).*

## Section 1 — Exotics: every observed exotic with a threshold sits within 30 MeV of it (toy 5802)
**Kill lines first** (K1925 Addendum 4, Keeper's words; Lyra words the final ones): (1) a stable or weak-decay-only hadron containing an unclosed pair; (2) an exotic bound far below every two-hadron threshold.
**Direction first:** the proximity reading says observed exotics sit at thresholds.

| state | mass (MeV) | nearest threshold | offset | width | source |
|---|---|---|---|---|---|
| X(3872) | 3871.64 (PDG BW) | D⁰D̄*⁰ 3871.70 | −0.06 (pole +0.01, LHCb Flatté +0.06: sign NOT settled) | 1.19 | PDG tab-c-cbar:1830 |
| T_cc⁺ | pole δm −360(40) keV | D*⁺D⁰ 3875.11 | −0.36 | Γ_pole 48 keV | 2109.01056:968–972 |
| P_c(4312)⁺ | 4311.9 | Σ_c⁺D̄⁰ 4317.49 | −5.6 | 9.8 | 1904.03947:361 |
| P_c(4440)⁺ | 4440.3 | Σ_c⁺D̄*⁰ 4459.51 | −19.2 | 20.6 | :365 |
| P_c(4457)⁺ | 4457.3 | Σ_c⁺D̄*⁰ 4459.51 | −2.2 | 6.4 | :369 |
| Z_c(3900) | 3886.7 (PDG; BESIII 2013 3899.0) | D⁺D̄*⁰ 3876.52 | +10.2 (+22.5) | 29.5 | PDG list:27 |
| Z_c(4020) | 4024.1 | D*⁺D̄*⁰ 4017.13 | +7.0 | 13 | PDG list:27 |
| Z_b(10610) | 10607.2 | B⁺B̄*⁰ 10604.16 | +3.0 | 18.4 | 1110.2251:155 |
| Z_b(10650) | 10652.2 | B*B̄* 10649.50 | +2.7 | 11.5 | 1110.2251:155 |
| T_cs̄0(2900) | 2908 | D*⁺K*⁺ 2902.15 | +5.9 | 136 | 2212.02716:433 |
| T*_cs0(2870) | 2874 (PDG; LHCb 2866) | D*K* 2902.15 | −28.2 (−36.2) | 68 | PDG list:17 |
| T*_cs1(2900) | 2904 | D*K* 2902.15 | +1.9 | 110 | 2009.00026:1485 |
| P_ψs^Λ(4338) | 4338.2 | Ξ_c⁺D⁻ 4337.45 | +0.8 | 7.0 | 2210.10346:25 |
| P_cs(4459) (3.1σ only) | 4458.8 | Ξ_c⁰D̄*⁰ 4477.36 | −18.6 | 17.3 | 2012.10380:29 |
| X(6900) | 6898 (model-dependent) | none natural (J/ψJ/ψ 6193.8) | +704 | 161 | 2006.16957:638 |

Result: P1–P3 hold. All 14 thresholded states lie within 30 MeV; none is bound more than 30 MeV below; all decay strongly (the narrowest is T_cc⁺ at 48 keV). The random-mass null (±200 MeV windows) passes P1 with probability 3e-12.
**Honest limits.**
- The toy is not blind.
- "Nearest threshold" picks the closest of several candidate thresholds.
- Exotics are partly *found* near thresholds because that is where the cusps are looked for, a selection effect the null does not model.
- T*_cs0(2870) passes the 30 MeV cut only on the PDG average; LHCb's own 2866 puts it at −36.
- **X(6900) is an observed exotic with no threshold, 704 MeV above di-J/ψ.** Proximity describes most exotics, not all. X(6900) does not fire kill (2), which is about binding below threshold.

**Top quark (PDG 2026):**
- Γ_t = 1.42 +0.19/−0.15 GeV, S = 1.4 (sum-quarks:63).
- Lifetime "about 0.5×10⁻²⁴ s … expected to decay before top-flavored hadrons … can form [Bigi et al. 1986]" (rev-top-quark:130).
- "Top quarks decay before they hadronize" (:712).
- A numerical 1/Λ_QCD time is PIN OWED: PDG prints none.

## Section 2 — T_bb: both kill lines as worded point at a state lattice QCD predicts unanimously
There are ten lattice calculations (2017–2026) of bb ū d̄ with J^P = 1⁺, and every one finds it bound below B B*:
- Francis+ 2017: −189(10) MeV
- Junnarkar+ 2019: −143(34)
- Leskovec+ 2019: −128(24)(10)
- Mohanta–Basak 2020: −167(19)
- Hudspith–Mohler 2023: −112(13)
- HAL QCD 2023: −83(10)(20)
- Alexandrou+ 2024: −100(10)(+36/−51)
- Colquhoun+ 2024: −115(17)
- Tripathy+ 2025: −116(+30/−36), an amplitude pole
- Hoffmann–Meinel 2026: −74(17)(10), a reanalysis of Leskovec's data

The values shrink with time; the calculations from 2023 on span −74 to −116. Colquhoun+ 2024: "can decay only via the weak interaction" (2407.08816:1137–1141). Karliner–Rosner 2017 give τ ≈ 367 fs.

It has not been observed, and I found no dedicated search. That no search exists is PIN OWED: web searches came up empty, and no source says it.

**Consequence, both directions:** if T_bb is found as QCD predicts, kills (1) and (2) both fire. So either:
- (a) the proximity rule predicts **no deeply bound, weak-only T_bb**, a departure from lattice QCD and the first exotic row where BST and the SM differ; or
- (b) the rule needs a clause separating a compact heavy bb diquark (colour 3̄) from light-quark molecules.

**Lyra/Cal decide. Grace does not word it.** Whichever is chosen, it should be registered before LHCb Upgrade II looks.

## Section 3 — The kaon hinge, and my own convention error (toy 5803)
**Owned:** R163 labelled 1.2065 as f_K±/f_π± and compared it with FLAG's charged 1.1934 (5.4σ). But 1.2065 = 0.27679·√19 is built from the **isospin-limit** product (PDG Eq. 67.15, which PDG pairs with the isospin-limit 1.1978).

Convention-matched:

| convention | A2 value | compared with | tension |
|---|---|---|---|
| isospin-limit F_K/F_π | 1.2065(15) | Cirigliano 2022 avg 1.1978(22) | **+3.27σ** |
| charged f_K±/f_π± | 0.27599·√19 = 1.2030(18) | FLAG 2+1+1 1.1934(19) | **+3.69σ** |

- The individual FLAG inputs run from +1.5σ to +4.0σ, and they are correlated.
- The newest results are Hudspith 2026 (+1.8σ charged / +2.2σ iso) and Conigli 2025 (+1.7σ / +1.9σ).
- The PDG-vs-FLAG "audit flag" is resolved: it is a convention mismatch, and 1.1978·√(1 − 0.0073) = 1.1934.
- **FLAG 2+1+1 inputs**, charged values (flag.txt:3886–3895):
  - ETM 21: 1.1957(44)(7)
  - CalLat 20: 1.1942(32)(31)
  - FNAL/MILC 17: 1.1950(15)(+6−18)
  - ETM 14E: 1.184(12)(11)
  - HPQCD 13A: 1.1916(15)(16)
- **Experimental inputs:**
  - KLOE BR(K_μ2) = 0.6366(9)(15), the only precise input
  - τ_K = 1.2380(20)e-8 s, S = 1.8 (KLOE 08 and KOPTEV 95 disagree)
  - τ_π = 2.6033(5)e-8 s
  - δ_EM = −0.0069(17), Cirigliano–Neufeld
  - lattice δR_Kπ = −0.0126(14), Di Carlo 2019
  - Each input moves the product by only 0.01–0.12%.
- **What moves A2:** the lattice.
  - FLAG 2027: submissions close 30 Apr 2027, review in Oct 2027.
  - Hudspith's planned physical-point ensembles, targeting an error of ≈0.0020.
  - No official NA62 K_μ2 plan was found.
- **For Cal (item 2):** the matched tension is 3.3–3.7σ, **at threshold, not fired**. My v0.24 candidate kill is re-keyed to the charged value, 1.2030. Cal rules the word.

## Section 4 — The Addendum-4 pins (hydrogen; spectral dimension)
- **Fock 1935**, Z. Phys. 98, 145, DOI 10.1007/BF01336904: metadata PRIMARY (Crossref). The content (S³ projection, SO(4), n²) is SECONDARY, and Fock's own text is PIN OWED. The projection is energy-dependent, so SO(4) acts within one shell (Maclay 2305.18229).
- **Barut–Kleinert 1967** (PR 156, 1541; 157, 1180; 160, 1149), PRIMARY (Kleinert's reprints, OCR'd):
  - PR 157, 1180: "an irreducible unitary representation of the conformal group O(4,2) … on the Hilbert space of bound-state wave functions of the H atom".
  - PR 156, 1541: it "remains irreducible when restricting to the subalgebra" O(4,1).
  - ⇒ **Lyra's branching test has three rungs, SO(5,2) ⊃ SO(4,2) ⊃ SO(4,1).**
  - The published values of one Casimir disagree across papers, so name the source whenever one is quoted.
- **Malkin–Man'ko**, JETP Lett. **2**, 146 (1965), PRIMARY (journal archive). Later papers cite it as "1966" or "vol. 3"; those citations are wrong. The paper says: "non-compact group O₆"; the discrete spectrum is "a single infinite-dimensional irreducible representation", irreducible on de Sitter. They never print the signature (4,2).
- **CDT, AJL 2005** (PRL 95, 171301): D_S(∞) = 4.02 ± 0.1 and D_S(0) = 1.80 ± 0.25, "compatible with the integer value two". The short-distance value is an extrapolation of a fit over σ ∈ [40, 400].
- **Carlip 2017** (CQG 34, 193001):
  - Eleven approaches; the reported short-distance values include 1.5, 2.38, 2.5, 1, 0, d/2 and 4−ε, and most are not spectral dimensions.
  - "Taken individually, none of these hints is terribly convincing" (1705.05417:884–885).
  - "different definitions of dimension, which need not be equivalent" (:900–901).
- **Definition:** D_S = −2 d log P(σ)/d log σ, from the return probability of a Euclidean diffusion (AJL Eq. 8).
- **Corpus reconnect.** T655/T1472 (`BST_EffectiveSpectralDimension.md`) compute d_eff = 6 from a Weyl-law count on Q⁵'s zonal sector. That is a different object from the full-Laplacian dimension (10) and from a diffusion return probability. On any smooth manifold, the heat-kernel D_S(σ → 0) is its dimension. **So a flow to 2 cannot come from D_IV⁵'s smooth geometry. It must come from the discreteness (N_max, τ₀); the 09-15 resolution-limit marker is the door.** Direction only, no number.

## Owed
**By me:**
- PIN OWED: Fock's own text, the 1/Λ_QCD time, the T*_cs1 2024 mass, and "no T_bb search exists" (needs a review that says so).

**To me:**
- Cal: the A2 word.
- Lyra/Cal: the exotic kill wording, option (a) or (b).
- Elie: the ACT chain ρ for A13.
