# Grace R160: round-2 pins (neutron, meson and dark sector, photon record, 2νββ) and register v0.23 (2026-09-25)

This covers the GRACE section of Keeper's round-2 consolidated prompt. Primaries were fetched today, and pdftotext extracts are retained in `data/sources_grace_2026-09-25/{neutron,meson_photon,dbd}/`. Instrument: toy 5785, 13/13, output `play/.out_toy_5785.txt`. It grep-checks every K it uses and recomputes every neutron σ below. Arithmetic on sources' numbers is marked (arith). Nothing below is from memory.

## 0. The finding first: K1923's master-formula constant is mis-attributed, and the σ depends on K

**What K1923 said.** Section 2 uses K = 4905.7(1.7) s and cites arXiv:2501.17916. It also names "4908(4) s (CMS 2018)".

**What the sources print:**
- **arXiv:2501.17916** (Vander Griend, Cao, Hill, Plestid, *The Fermi function and the neutron's lifetime*) prints no K and does not contain 4905.7.
  - Its Eq. 28 is τ_n|V_ud|²(1+3λ²)(1+Δ_R)(1+27.04(7)×10⁻³) = 5263.284(17) s, with Δ_R = 45.37(27)×10⁻³. That gives **K = 4902.3(1.3) s** (arith).
  - Its own neutron value is |V_ud| = 0.97393(41) (Eq. 29), from UCNτ 877.82(30) s and PERKEO III.
- **4905.7(1.7)** appears in Wietfeldt, Symmetry 16, 956 (2024), Eq. 3. That is a secondary source, and it credits Czarnecki–Marciano–Sirlin PRD 100, 073008 (2019). The arXiv v1 of that paper (1907.06737, Eq. 49) prints **4906.4(1.7)**. The published PRD is paywalled and unread.
- **"4908(4)" appears nowhere.** CMS 2018 (PRL 120, 202002, Eq. 2) prints **4908.6(1.9)**.
- **Other K values:** Gorchtein–Seng 2021 (arXiv:2106.09185, Eq. 2) gives 4903.1(1.1). PDG 2026 Eq. 67.5 gives 5099.33 s/(1+Δ_R) with Δ_R = 0.03983(27), which is 4904.0(1.3) (arith).

**What A2's product does under each K.** The prediction is τ_n(1+3λ²) = 20K/19. It is compared with 5168.3 ± 4.2 s, which is UCNτ all-data 877.82(30) with PERKEO III λ = 1.27641(56).

| K | 20K/19 | σ |
|---|---|---|
| 4902.3 (2501.17916) | 5160.3 | **+1.83σ** |
| 4903.1 (Gorchtein–Seng) | 5161.2 | +1.66σ |
| 4904.0 (PDG 2026) | 5162.1 | +1.42σ |
| 4905.7 (K1923) | 5163.9 | +0.98σ (+0.87σ on UCNτ 2021, K1923's number, reproduced) |
| 4906.4 (CMS 2019) | 5164.6 | +0.81σ |
| 4908.6 (CMS 2018) | 5166.9 | +0.30σ |

With PDG 2026's λ = 1.2753(13) (S = 2.7), the σ runs from −0.67 to +0.06 on every K. The beam lifetime is excluded on every K.

**Calibrated reading, both directions.**
- The free-neutron agreement holds under 2σ on every pinned K. That part of K1923 stands.
- But "0.87σ" is the second-most favourable value in the table, taken from a misattributed secondary number. The newest K on the newest lifetime gives 1.83σ, the same as 2501.17916's own |V_ud| against √(19/20).
- The K1923 sentence and the Section 2 pre-registration should carry the K range, not one value. The prediction's σ is set by the radiative-correction choice, so the choice of K belongs in Lyra's pre-registration as a named input. I'm handing that ruling to Keeper, and I have not edited K1923.

## 1. Neutron pins (item 1)

**Lifetime, bottle (UCN) method:**
- UCNτ 2021: 877.75 ± 0.28 (stat) +0.22/−0.16 (syst) s, combined 0.34 s. Gonzalez et al., PRL 127, 162501. PDG lists it as superseded.
- UCNτ all-data: **877.82 ± 0.22 (stat) +0.20/−0.17 (syst) s**. Musedinovic et al., PRC 111, 045501 (2025), arXiv:2409.05560.
- PDG 2026 τ_n average: **878.3 ± 0.4 s (S = 1.8)**, from 8 UCN results. Including Yue 2013 it becomes 878.6 ± 0.6 (S = 2.2). PDG states no separate bottle-only average.

**Lifetime, beam method:**
- NIST (Yue 2013, PRL 111, 222501): 887.7 ± 1.2 ± 1.9 s.
- J-PARC 2020 (PTEP 2020 123C02): 898 ± 10 +15/−18 s.
- J-PARC 2024 (arXiv:2412.19519, no journal ref found): 877.2 ± 1.7 +4.0/−3.6 s.
- Beam average: 888.0(2.0) s (CMS 2018 abstract; J-PARC 2024 quotes the same, beside a bottle average of 878.4 ± 0.5 and a "9.5-s (4.6σ)" gap).

**New lifetime experiments:**
- τSPECT: no lifetime published. It is commissioning at PSI, with a "sensitivity reach of σ ≤ 0.3 s" (Auler et al., EPJA, doi:10.1140/epja/s10050-025-01673-8, arXiv:2503.15239).
- UCNτ+: no result. A factor-4 statistics improvement is UNVERIFIED (seen only in a search snippet).

**λ = g_A/g_V:**
- PERKEO III: λ = −1.27641(45)(33). Märkisch et al., PRL 122, 242501 (2019), Eq. 4.
- UCNA: −1.2772(20). PRC 97, 035505.
- aSPECT: |λ| = 1.2677(28) (PRC 101, 055506, 2020). The reanalysis gives −1.2668(27), and −1.2724(13) combined with PERKEO III, with b = −0.0181(65) (arXiv:2308.16170v2; journal ref UNVERIFIED).
- PDG 2026: **−1.2753 ± 0.0013 (S = 2.7)**. It still uses aSPECT 2020, not the reanalysis. The Vud/Vus review's Eq. 67.6 carries 1.2756(13) from PDG 2022.

**Future precision:**
- Nab projects δλ/λ = 0.03 % (EPJ WoC 219, 04002). Its first physics result (PRC 113, 035501 (2026), doi:10.1103/ksmp-zxsl) is the Dalitz plot and phase space only, with no a and no λ yet.
- PERC projects correlations at 10⁻⁴ (arXiv:1905.10249). No first-result date found.

## 2. Meson and dark-sector pins (item 2)

**Belle II B⁺→K⁺νν̄** (arXiv:2311.14647, PRD 109, 112006 (2024)):
- Combined B = 2.3 ± 0.5 +0.5/−0.4 × 10⁻⁵. This is 3.5σ evidence, and "2.7 standard deviations above the standard model expectation".
- By analysis: ITA 2.7 ± 0.5 ± 0.5 × 10⁻⁵ (2.9σ vs SM); HTA 1.1 +0.9/−0.8 +0.8/−0.5 × 10⁻⁵ (0.6σ vs SM).
- SM prediction used: 5.58 ± 0.37 × 10⁻⁶, which includes the τ contribution (Eq. 1).
- **Where the excess sits:** "a deficit … for q²_rec < 3 GeV²/c⁴ and an excess for 3 GeV²/c⁴ < q²_rec < 5 GeV²/c⁴" (Figs. 17–18). Separate fits below and above 4 GeV² "are consistent within 1.4 standard deviations".

**Invisible-X reinterpretation:** Gärtner, Krug, Kuhr, Schmidt, Stefkova, Yabsley, PRD 114, 032003 (2026-08-07), doi:10.1103/ggtk-gkx4, arXiv:2602.09666.
- Fitted **m_X = 2.1 +0.2/−0.1 GeV**, with B(B⁺→K⁺X)·P_X,inv = 9.2 +1.8/−3.4 × 10⁻⁶.
- It "favors the Standard Model plus resonance hypothesis by 3.0σ".
- An earlier reinterpretation (Altmannshofer et al., PRD 109, 075008 (2024), arXiv:2311.14629) found m_X ≈ 2 GeV, 3.6σ, "localized around q² = 4 GeV²".

**⚠ For Lyra's item 1 (continuum vs peak): the published answer is already a PEAK at 2.1 GeV, at 3.0σ over SM.** A pre-registration written after today is target-aware. It should say so on its face, and it should name what distinguishes a continuum from a 2.1 GeV two-body peak in Belle II's binning. That second part is Elie's item 3.

**Other B→K(*)νν̄ results:**
- No dedicated 2025–26 Belle II K*⁰νν̄ result was found.
- Belle II's first inclusive B→X_sνν̄ upper limit is 3.2 × 10⁻⁴ at 90 % CL (arXiv:2511.10980).
- Belle 2017 (arXiv:1702.03224): K⁺νν̄ < 1.9 × 10⁻⁵, K*⁰νν̄ < 1.8 × 10⁻⁵.
- BaBar 2013 (arXiv:1303.7465): K*⁰νν̄ < 9.3 × 10⁻⁵.

**NA62 K⁺→π⁺νν̄:**
- 2016–2024 (arXiv:2604.12649v3, **preliminary proceedings**): 9.6 +1.9/−1.8 × 10⁻¹¹, over 6σ above background, "good agreement with SM".
- The SM predictions it quotes are 8.4 ± 1.0, 8.60 ± 0.42 and 7.86 ± 0.61 × 10⁻¹¹.
- The journal result for 2016–2022 is 13.0 +3.3/−3.0 × 10⁻¹¹ (arXiv:2412.12015).

**Strong widths, PDG 2026 Summary Tables** (Takahashi et al., IJMPA 41, 2630011):

| state | mass (MeV) | Γ (MeV) |
|---|---|---|
| ρ(770)⁰ (BW) | 775.26 ± 0.23 | 147.4 ± 0.8 (S 2.0) |
| ρ± | 775.11 ± 0.34 | 149.1 ± 0.8 |
| ω(782) | 782.66 ± 0.13 | 8.68 ± 0.13 |
| K*(892)± (hadroprod.) | 891.88 ± 0.23 | 48.5 ± 1.2 (S 2.1) |
| K*(892)⁰ | 895.56 ± 0.20 | 47.1 ± 0.5 (S 2.0) |
| φ(1020) | 1019.460 ± 0.016 | 4.249 ± 0.013 |
| a₂(1320) | 1318.2 ± 0.6 | 107 ± 5 |
| f₂(1270) | 1275.4 ± 0.8 | 186.6 +2.8/−2.2 (S 1.5) |

The widths are pinned here for the compare line. Lyra's ordering comes first, direction before numbers.

## 3. Photon-record pins (item 3)

**π⁰→γγ (PrimEx-II):** Larin et al., Science 368, 506 (2020), doi:10.1126/science.aay6641.
- Γ = 7.798 ± 0.056 (stat) ± 0.109 (syst) eV. PrimEx I+II combined: 7.802 ± 0.052 ± 0.105 eV, "1.50%", which "confirms the prediction based on the chiral anomaly".
- Only the abstract was read (OSTI), because science.org returned 403.

**The anomaly formula:**
- From arXiv:2608.31024, Eq. 1: Γ_ABJ = π m_π³ α² K₀² /(4F_π²) = 7.743(16) eV, with **K₀ = N_c(Q_u² − Q_d²)/(4π²)**.
- The N_c² form in the prompt, Γ = α² m_π³ N_c² /(576 π³ F_π²), is (arith) from K₀² = N_c²/(144π⁴). It is a derivation, not a quote.
- The same paper notes the measurement is in "a 1.8-σ tension with the NNLO ChPT prediction". So "the photons count the colours" holds at the percent level for N_c = 3 against N_c = 2 or 4 (a factor of 4/9 or 16/9 in rate). The NNLO comparison is a separate question.

**π⁰ parity (double Dalitz decay):** KTeV, arXiv:0802.2064, PRL 100, 182001 (2008), 30,511 candidates. "We confirm the negative π⁰ parity, and place a limit on scalar contributions … of less than 3.3%".

**Wu & Shaknov 1950:** Phys. Rev. 77, 136, doi:10.1103/PhysRev.77.136, confirmed via Crossref. **The primary text is UNVERIFIED** (APS blocked). The asymmetry ratio "2.04 ± 0.08 … theoretical value 2.00" comes from secondary sources (arXiv:2502.06458, 2507.13582). Pin it from the primary before any external quote.

## 4. 2νββ pins (item 4)

**NEMO-3 ¹⁰⁰Mo:** EPJC 79, 440 (2019), doi:10.1140/epjc/s10052-019-6948-4, arXiv:1903.08084.
- T½ (SSD) = 6.81 ± 0.01 +0.38/−0.40 × 10¹⁸ y.
- HSD excluded: single-electron χ²/ndf 1159/27 and 1508/27, against SSD 41.5/27 and 39/27.
- **Bosonic-neutrino admixture: "sin² χ < 0.27 (90% C.L.)"** (Eq. 7). This is built on W_tot = cos⁴χ W_f + sin⁴χ W_b (Eq. 5) and T½^b(0⁺g.s.) > 1.2 × 10²¹ y. It is the only bosonic-ν limit found. The earlier Barabash bound was not fetched.
- **Lorentz violation: "−4.2 × 10⁻⁷ GeV < å_of < 3.5 × 10⁻⁷ GeV (90% C.L.)"** (Eq. 8).

**CUPID-Mo ¹⁰⁰Mo:** PRL 131, 162501 (2023), arXiv:2307.14086. The journal ref is confirmed by CUORE 2025's reference list.
- T½ = 7.07 ± 0.02 ± 0.11 × 10¹⁸ yr.
- **ξ₃,₁ = 0.45 ± 0.03 (stat) ± 0.05 (syst)** (Eq. 6). This is obtained with a Gaussian prior on ξ₅,₁/ξ₃,₁ at the SSD value 0.367, 5 % width. The unconstrained ratio is < 40 (90 %), and ρ(ξ₃₁, ξ₅₁) = −0.92.
- g_A,eff (ISM) = 1.11 ± 0.03 ± 0.05.

**KamLAND-Zen ¹³⁶Xe:** PRL 122, 192501 (2019), arXiv:1901.03871. ξ₃₁ = −0.26 +0.31/−0.25, **ξ₃₁ < 0.26 (90 % CL)**.

**CUORE ¹³⁰Te:**
- 2021 (PRL 126, 171801): T½ = 7.71 +0.08/−0.06 +0.12/−0.15 × 10²⁰ yr.
- 2025 (arXiv:2503.24137, PRL 135, doi:10.1103/jdhf-hn4l): T½ (SSD) = 9.32 +0.05/−0.04 ± 0.07 × 10²⁰ yr. It gives ξ₃₁ "0.01 +0.31 −0.01", with a 90 % CI limit of 0.55, and ξ₅₁ = 1.46 +0.33/−0.62. SSD predicts ξ₃₁ = 0.35 and ξ₅₁ = 0.123. The paper states the HSD is ruled out at > 5σ.
- ⚠ The ξ₃₁ error bars read from the text layout. Check Fig. 3 before quoting.

**Other results:**
- GERDA ⁷⁶Ge (arXiv:2209.01671; journal ref UNVERIFIED): å_of ∈ (−2.7, 6.2) × 10⁻⁶ GeV at 90 %. Its Table 2 lists EXO-200, AURORA, CUPID-0 and KATRIN (|å| < 3 × 10⁻⁸).
- NEMO-3 ⁸²Se (EPJC 78, 821 (2018)): SSD 9.39 ± 0.17 ± 0.58 × 10¹⁹ y, preferred over HSD (χ² 12.3/16 vs 35.3/16).
- **Two-electron angular correlation coefficient:** neither NEMO-3 paper states one; both show cos θ distributions only. There is no number to pin, and Lyra's map should know that before it names the observable.

## 5. Register v0.23 (the ruled edits, applied)

- **A2:** now carries both faces, (i) λ and (ii) |V_ud|.
  - It adds (iii) the g_A-free neutron product with all six K values and their σ.
  - (iv) Kill clauses are now on both faces. The superallowed face is already past 3σ, and the row's reading is that the gap resolves on the binding side. That reading is Lyra's to pre-register.
  - (v) "Currently in BST's favor" is left as written for Keeper's ruling (the R159 flag).
- **A1:** the no-crossing clause gains the once-only-commit mechanism. F799/T2559's late-time clause is marked UNSUPPORTED BY THE LEDGER (not refuted), and both DESI directions are stated before the next release.
  - **My own 09-22 bracket sentence is WITHDRAWN.** It said "DESI's w₀ > −1, wₐ < 0 is the direction a growing commitment fraction gives". That is the direction-leak K1921 owned on the boundary paragraph, sitting on my row, and it was never computed.
  - F755's retirement stands on its own reason. The late-time −1 returns by a different mechanism, which Keeper may want named on F755's head.
- **E7 (NEW, CANDIDATE, NOT CERTIFIED):** g_A = 4/π.
  - Against PERKEO III: 5.66σ. Against PDG 2026's 1.2753(13): 1.58σ.
  - Jointly with A2 on UCNτ all-data: +5.9σ to +7.5σ across the six K values.
  - The Vol 3 presentation drift is named. Cal decides fired or tension; Keeper certifies.
- **Dark-matter rows:** waiting on Lyra's ruling among T1433, T1971 and Vol 5's May text.

— Grace, 2026-09-25
