# Exotic hadrons: masses, nearest two-hadron thresholds, offsets, widths (DRAFT)

Pinned 2026-09-26. Every number below was read from a text file in this directory
(`data/sources_grace_2026-09-26/exotics/`), except rho(770), taken from
`data/sources_grace_2026-09-25/meson_photon/rpp2026-tab-mesons-light.txt`. Each number is
cited as file:line. PDG = RPP 2026 (Takahashi et al., IJMPA 41, 2630011 (2026)), summary tables
(`rpp2026-tab-*`, `rpp2026-sum-*`) and Particle Listings (`rpp2026-list-*`), fetched from pdg.lbl.gov/2026.
Primary papers: arXiv PDFs run through `pdftotext -layout`.

Sign convention: offset = M(state) - threshold. **Negative means below threshold.**
Threshold errors are the two PDG mass errors added in quadrature, with no correlations
(see note T1).

## 1. Threshold inputs (PDG 2026 summary tables)

| hadron | mass (MeV) | file:line |
|---|---|---|
| D0 | 1864.84 ± 0.04 | rpp2026-tab-mesons-charm.txt:537 |
| D+ | 1869.66 ± 0.05 | rpp2026-tab-mesons-charm.txt:13 |
| D*(2007)0 | 2006.86 ± 0.05 (S=1.1) | rpp2026-tab-mesons-charm.txt:1519 |
| m(D*0) - m(D0) | 142.014 ± 0.030 | rpp2026-tab-mesons-charm.txt:1520 |
| D*(2010)+ | 2010.27 ± 0.04 | rpp2026-tab-mesons-charm.txt:1541 |
| m(D*+) - m(D0) | 145.4257 ± 0.0017 | rpp2026-tab-mesons-charm.txt:1543 |
| Ds*+ | 2112.2 ± 0.4 | rpp2026-tab-mesons-charm-strange.txt:526 |
| B+ | 5279.41 ± 0.07 | rpp2026-tab-mesons-bottom.txt:81 |
| B0 | 5279.72 ± 0.08 | rpp2026-tab-mesons-bottom.txt:1586 |
| B* (charge-unspecified) | 5324.75 ± 0.20 | rpp2026-tab-mesons-bottom.txt:3423 |
| m(B*+) - m(B+) | 45.34 ± 0.20 | rpp2026-tab-mesons-bottom.txt:3425 |
| Sigma_c(2455)+ | 2452.65 +0.22 -0.16 | rpp2026-sum-baryons.txt:2411-2412 |
| Sigma_c(2455)++ | 2453.97 ± 0.14 | rpp2026-sum-baryons.txt:2410 |
| Xi_c+ | 2467.79 ± 0.15 | rpp2026-sum-baryons.txt:2527 |
| Xi_c0 | 2470.50 ± 0.25 | rpp2026-sum-baryons.txt:2620 |
| K*(892)+ (hadroproduced) | 891.88 ± 0.23 | rpp2026-tab-mesons-strange.txt:503 |
| rho(770)+ (Breit-Wigner) | 775.11 ± 0.34 | ../../sources_grace_2026-09-25/meson_photon/rpp2026-tab-mesons-light.txt:190 |
| J/psi(1S) | 3096.900 ± 0.006 | rpp2026-tab-mesons-c-cbar.txt:108 |
| psi(2S) | 3686.097 ± 0.011 | rpp2026-tab-mesons-c-cbar.txt:1303 |

Threshold arithmetic (MeV):
- D0 + D*0bar = 1864.84 + 2006.86 = **3871.70 ± 0.06**. Via the mass difference, 2(1864.84) + 142.014 = 3871.694 ± 0.085. LHCb uses 3871.70 ± 0.11, with kaon-mass correlation: 2005.13419.txt:61, 2005.13422.txt:688.
- D*+ + D0 = 2010.27 + 1864.84 = **3875.11 ± 0.06**. Via the mass difference, 2(1864.84) + 145.4257 = 3875.106 ± 0.080.
- D+ + D*0bar = 1869.66 + 2006.86 = **3876.52 ± 0.07** (the lowest charged D Dbar* threshold after D*+ D0bar = 3875.11)
- D*+ + D*0bar = 2010.27 + 2006.86 = **4017.13 ± 0.06**
- B+ + B*0bar = 5279.41 + 5324.75 = **10604.16 ± 0.21**. B0bar + B*+ = 5279.72 + 5324.75 = 10604.47 ± 0.22. (PDG gives no separate B*0 mass; see T2.)
- B*+ + B*0bar = 2 × 5324.75 = **10649.50 ± 0.40**
- Sigma_c+ + D0bar = 2452.65 + 1864.84 = **4317.49 ± 0.22**. Sigma_c++ + D- = 2453.97 + 1869.66 = 4323.63 ± 0.15.
- Sigma_c+ + D*0bar = 2452.65 + 2006.86 = **4459.51 ± 0.23**
- Xi_c0 + D*0bar = 2470.50 + 2006.86 = **4477.36 ± 0.25**. Xi_c+ + D*- = 2467.79 + 2010.27 = 4478.06 ± 0.16.
- Xi_c+ + D- = 2467.79 + 1869.66 = **4337.45 ± 0.16**. LHCb quotes "4.337 GeV" at 2210.10346.txt:370. Xi_c0 + D0bar = 2470.50 + 1864.84 = 4335.34 ± 0.25.
- D*+ + K*+ = 2010.27 + 891.88 = **2902.15 ± 0.23** (the same value serves D*- K*+ for the c-bar states)
- Ds*+ + rho+ = 2112.2 + 775.11 = 2887.31 ± 0.52 (rho is broad, Gamma about 149 MeV)
- J/psi + J/psi = 2 × 3096.900 = **6193.800 ± 0.012**

## 2. Main table

| state (PDG 2026 name) | mass (MeV) | nearest 2-hadron threshold (MeV) | offset M - thr (MeV) | width (MeV) | observed decays | primary source |
|---|---|---|---|---|---|---|
| chi_c1(3872) = X(3872) | **PDG avg 3871.64 ± 0.06** (BW; tab-c-cbar:1830; list:76). LHCb JHEP: 3871.59 ± 0.06 ± 0.03 ± 0.01 (2005.13422:668); LHCb combined 3871.64 ± 0.06 ± 0.01 (2005.13422:678). LHCb PRD: 3871.695 ± 0.067 ± 0.068 ± 0.010 (2005.13419:444). Flatte mode 3871.69 +0.00-0.04 +0.05-0.13 (2005.13419:34). **PDG T-matrix pole** (3871.70 ± 0.15 +0.07-0.08) - i(0.19 ± 0.08 +0.14-0.19) (list:52; BESIII 24C) | D0 D*0bar = 3871.70 ± 0.06 | PDG avg: **-0.06 ± 0.09**. LHCb δE = thr - m = +0.12 ± 0.13 (this analysis) and +0.07 ± 0.12 (LHCb average) (2005.13422:684-685), i.e. M - thr = -0.07 ± 0.12. PDG pole relative to threshold: Re = +0.01 ± 0.15 +0.07-0.08 ± 0.07 (tab-c-cbar:1821-1823; list:31). LHCb Flatte pole E_II = (0.06 - 0.13i) (2005.13419:836); second pole E_III = (-3.58 - 1.22i) (2005.13419:840) | PDG avg Γ = **1.19 ± 0.21** (S=1.1) (tab:1831; list:213). Γ_BW = 1.39 ± 0.24 ± 0.10 (2005.13419:29). Γ_BW = 0.96 +0.19-0.18 ± 0.21 (2005.13422:46,655-656). Flatte FWHM 0.22 +0.07-0.06 +0.11-0.13 (2005.13419:35-36). Pole: -2 Im = 0.38 | D0 D0bar π0 (55 ± 28)% (tab:1843); D*0 D0bar (46 ± 16)% (tab:1844); π+π- J/psi (4.3 ± 1.4)% (tab:1837); ω J/psi (5.0 ± 1.9)% (tab:1841); γ J/psi (10 ± 4)e-3 (tab:1870); π0 χc1 (3.8 +1.9-1.7)% (tab:1849-1850) | LHCb, arXiv:2005.13419, PRD 102 (2020) 092005 (2005.13419:44); LHCb, arXiv:2005.13422, JHEP 08 (2020) 123 (2005.13422:51); PDG chi_c1(3872) listing |
| T_cc(3875)+ | **PDG pole** Re = 3874.75 ± 0.10 (list-T-cc:40), from δm_pole + threshold | D*+ D0 = 3875.11 ± 0.06 | δm_BW = **-273 ± 61 ± 5 +11-14 keV** (2109.01038:265-266). δm_U = **-359 ± 40 +9-6 keV** (2109.01056:942-943). δm_pole = **-360 ± 40 +4-0 keV** (2109.01056:968; list-T-cc:18). Mode: FU -361 ± 40 keV vs FBW -279 ± 59 keV (2109.01056:266-268; see flag F3) | Γ_BW = **410 ± 165 ± 43 +18-38 keV** (2109.01038:267-268). Γ_pole = **48 ± 2 +0-14 keV** (2109.01056:972; PDG width 0.048 list-T-cc:47). FWHM 47.8 ± 1.9 keV vs 409 ± 163 keV (2109.01056:267-268). **No separate "Γ_U" is quoted.** The unitarised width comes out as Γ_pole, plus the coupling limit abs(g) > 5.1 (4.3) GeV at 90 (95)% CL (2109.01056:950) | D0 D0 π+ seen (list-T-cc:62) | LHCb, arXiv:2109.01038, Nature Phys. 18 (2022) 751 (text line 34 says "Nature Physics (2021)"; volume/page from PDG list-T-cc:81). LHCb, arXiv:2109.01056, Nature Commun. 13 (2022) 3351 (2109.01056:45; list-T-cc:82) |
| P_cc̄(4312)+ (was P_c(4312)+) | 4311.9 ± 0.7 +6.8-0.6 (1904.03947:361-362; PDG list-P-4312:13, no average) | Sigma_c+ D0bar = 4317.49 ± 0.22 | **-5.6** (+0.7/+6.8 on M). The paper says "approximately 5 MeV below" (1904.03947:460-461) | 9.8 ± 2.7 +3.7-4.5; < 27 at 95% CL (1904.03947:362) | J/psi p seen (list-P-4312:27). Λc+ D0bar, Λc π D not seen (list-P-4312:28-33) | LHCb, arXiv:1904.03947, PRL 122 (2019) 222001 (text line 33 says "Accepted by PRL"; journal ref from PDG list-P-4312:80) |
| P_cc̄(4440)+ | 4440.3 ± 1.3 +4.1-4.7 (1904.03947:365-366; list-P-4440:14) | Sigma_c+ D*0bar = 4459.51 ± 0.23 | **-19.2**. The paper says "about 20 MeV of binding energy" (1904.03947:463) | 20.6 ± 4.9 +8.7-10.1; < 49 (1904.03947:366; list:21) | J/psi p seen. Sigma_c(2455)++ D-, Sigma_c(2520)++ D- not seen (list-P-4440:28,34-35) | as above |
| P_cc̄(4457)+ | 4457.3 ± 0.6 +4.1-1.7 (1904.03947:369-370; list-P-4457:24) | Sigma_c+ D*0bar = 4459.51 ± 0.23 | **-2.2**. The paper says "approximately ... 2 MeV below" (1904.03947:460-461) | 6.4 ± 2.0 +5.7-1.9; < 20 (1904.03947:370; list:34) | J/psi p seen (list-P-4457:45) | as above |
| T_cc̄1(3900) = Z_c(3900) | BESIII 2013: **3899.0 ± 3.6 ± 4.9** (1303.5949:162; list-Tcc1-3900:51). **PDG 2026 avg 3886.7 ± 2.3** (S=1.7) (list-Tcc1-3900:27) | charged: D+ D*0bar = 3876.52 ± 0.07 (D*+ D0bar = 3875.11) | BESIII 2013: **+22.5 ± 6.1**. PDG avg: **+10.2 ± 2.3** (above threshold) | BESIII 2013: 46 ± 10 ± 20 (1303.5949:165). **PDG avg 29.5 ± 2.4** (list:98) | J/psi π seen; (D D*)± seen; D0 D*- + c.c. seen; D- D*0 + c.c. seen; η_c ρ seen; h_c π, ωπ, J/psi η not seen (list-Tcc1-3900:144-154) | BESIII, arXiv:1303.5949, PRL 110 (2013) 252001 (journal ref from PDG list-Tcc1-3900:282) |
| T_cc̄(4020) = Z_c(4020) | BESIII 2013: **4022.9 ± 0.8 ± 2.7** (1309.1896:183). PDG avg **4024.1 ± 1.9** (list-Tcc-4020:27) | D*+ D*0bar = 4017.13 ± 0.06 | BESIII: **+5.8 ± 2.8**. PDG: **+7.0 ± 1.9** | BESIII: 7.9 ± 2.7 ± 2.6 (1309.1896:183). PDG avg 13 ± 5 (S=1.7) (list:42) | h_c π seen; D* D*bar seen; D Dbar* not seen; J/psi π not seen (list-Tcc-4020:78-83) | BESIII, arXiv:1309.1896, PRL 111 (2013) 242001 (journal ref from PDG list-Tcc-4020:151) |
| T_bb̄1(10610)± = Z_b(10610) | **10607.2 ± 2.0** (1110.2251:155; PDG list-Tbb-10610:19, value used as the PDG number) | B Bbar*: B+ B*0bar = 10604.16 ± 0.21 (B0bar B*+ = 10604.47) | **+3.0 ± 2.0** (+2.7 vs B0bar B*+) | **18.4 ± 2.4** (1110.2251:155; list:52) | B B*bar + c.c. (85.6 +2.1-2.9)% (list-Tbb-10610:104-105); Υ(1S,2S,3S)π, h_b(1P,2P)π seen (list:90-101) | Belle, arXiv:1110.2251, PRL 108 (2012) 122001 (journal ref from PDG list-Tbb-10610:270) |
| T_bb̄1(10650)+ = Z_b(10650) | **10652.2 ± 1.5** (1110.2251:155; list-Tbb-10650:18) | B*+ B*0bar = 10649.50 ± 0.40 | **+2.7 ± 1.6** | **11.5 ± 2.2** (1110.2251:155-156; list:45) | B*+ B*0bar (74 +4-6)% (list-Tbb-10650:100-101); B B*bar not seen (list:99); Υ(nS)π, h_b(mP)π seen (list:89-97) | Belle, arXiv:1110.2251 (as above) |
| T*_cs̄0(2900)0 / ++ (LHCb "T_cs̄(2900)") | isospin-combined **2908 ± 11 ± 20** (2212.02716:433). Separate PDG: 0-charge 2892 ± 14 ± 15 (list-Tcs-2900:21); ++ 2921 ± 17 ± 20 (list:31) | D*+ K*+ = 2902.15 ± 0.23 (Ds*+ rho+ = 2887.31) | **+5.9 ± 23** vs D*K* (+20.7 vs Ds* rho) | combined **136 ± 23 ± 13** (2212.02716:434). 0: 119 ± 26 ± 13 (list:44); ++: 137 ± 32 ± 17 (list:55) | Ds+ π- (0) and Ds+ π+ (++) (2212.02716 abstract; list-Tcs-2900:74-77); 8.0σ and 6.5σ (list:16) | LHCb, arXiv:2212.02716, PRL 131 (2023) 041902 (2212.02716:34) |
| T*_cs0(2870)0 (was X0(2900)) | LHCb 2020: **2866 ± 7 ± 2** (2009.00026:1484). **PDG 2026 avg 2874 ± 11** (S=1.8, CL = 0.044) (list-Tcs-2870:17). LHCb 2024: 2914 ± 11 ± 15 (list:20) | D*- K*+ = 2902.15 ± 0.23 | 2020: **-36.2 ± 7.3**. PDG avg: **-28.2 ± 11**. Not near any threshold | 2020: 57 ± 12 ± 4 (2009.00026:1484). PDG avg 68 ± 17 (list:57). 2024: 128 ± 22 ± 23 (list:61) | D- K+ seen; D0bar K0S seen (list-Tcs-2870:93-94) | LHCb, arXiv:2009.00026, PRD 102 (2020) 112003 (2009.00026:35); arXiv:2009.00025, PRL 125 (2020) 242001 (2009.00025:34) |
| T*_cs1(2900)0 (was X1(2900)) | LHCb 2020: **2904 ± 5 ± 1** (2009.00026:1485; list-Tcs1:18). LHCb 2024: "2887 +- 8 + 7" (text is garbled; list:17). **No PDG average on disk** | D*- K*+ = 2902.15 ± 0.23 | 2020: **+1.9 ± 5.1**. 2024: -15 ± ~11 (value garbled, see F7) | 2020: 110 ± 11 ± 4 (2009.00026:1485). PDG avg 106 ± 10 (list:28) | D- K+ seen (list-Tcs1:41) | same as the row above |
| P_cc̄s(4338)0 = P_psi s^Λ(4338) | **4338.2 ± 0.7 ± 0.4** (2210.10346:25,440). PDG 4338.2 ± 0.8 (sum-baryons:3860) | Xi_c+ D- = 4337.45 ± 0.16 (Xi_c0 D0bar = 4335.34) | **+0.75 ± 0.8** (+2.9 vs Xi_c0 D0bar) | **7.0 ± 1.2 ± 1.3** (2210.10346:26). PDG 7.0 ± 1.8 (sum-baryons:3861) | J/psi Λ seen; Λc+ Ds- not seen (sum-baryons:3865-3870; list-Pccs-4338:27-28) | LHCb, arXiv:2210.10346, PRL 131 (2023) 031901 (2210.10346:34) |
| P_cc̄s(4459)0 (EVIDENCE only, 3.1σ) | LHCb **4458.8 ± 2.9 +4.7-1.1** (2012.10380:29). PDG avg 4466 +6-5 (S=1.8, with Belle 4471.7 ± 4.8 ± 0.6) (list-Pccs-4459:13-15) | Xi_c0 D*0bar = 4477.36 ± 0.25 | LHCb: **-18.6**. The paper says "about 19 MeV below" (2012.10380:362). PDG avg: -11.4 | LHCb 17.3 ± 6.5 +8.0-5.7 (2012.10380:29-30). PDG avg 19 +8-7 (list:29) | J/psi Λ seen (list:44) | LHCb, arXiv:2012.10380, Sci. Bull. 66 (2021) 1278 (2012.10380:43). Significance 3.1σ (list-Pccs-4459:22) |
| T_cccc̄c̄(6900)0 = X(6900) | LHCb: **6905 ± 11 ± 7** (no interference) / **6886 ± 11 ± 11** (interference) (2006.16957:638,648). **PDG avg 6898 ± 12** (S=1.2) (list-T4c:17) | no nearby two-hadron threshold. For reference, J/psi J/psi = 6193.80 | vs J/psi J/psi: +711 / +692 / +704 (PDG) | LHCb 80 ± 19 ± 33 / 168 ± 33 ± 69 (2006.16957:640,651). PDG avg 161 ± 26 (list:42) | J/psi J/psi seen (list-T4c:76); J/psi ψ(2S) (ATLAS, list:25) | LHCb, arXiv:2006.16957, Sci. Bull. 65 (2020) 1983 (2006.16957:35); JPC = 2++ (CMS) (list-T4c:10) |

## 3. Top quark (no hadronization)

| quantity | value | file:line |
|---|---|---|
| Γ_t, PDG 2026 average | **1.42 +0.19 -0.15 GeV** (S = 1.4) | rpp2026-sum-quarks.txt:63-64; rpp2026-list-t-quark.txt:744-745 |
| Γ_t, SM NLO at m_t = 172.5 GeV | 1.326 GeV | rpp2026-rev-top-quark.txt:129 |
| lifetime, as quoted by PDG | "about 0.5×10−24 s" | rpp2026-rev-top-quark.txt:130 |
| D0 direct lifetime | τ_t = (3.29 +0.90 -0.63) × 10^-25 s (from Γ_t = 2.00 +0.47 -0.43 GeV) | rpp2026-rev-top-quark.txt:2804-2806 |
| "decays before it hadronizes" (sentence 1) | "Top quarks decay before they hadronize, and their presence is inferred from detecting their decay products." | rpp2026-rev-top-quark.txt:712 |
| sentence 2 | "Its lifetime is shorter than the timescale of non-perturbative strong interactions, which prevents hadronization and preserves properties such as its spin" | rpp2026-rev-top-quark.txt:14-15 |
| sentence 3 | "With its correspondingly short lifetime of about 0.5×10−24 s, the top quark is expected to decay before top-flavored hadrons or tt quarkonium-like bound states can form [12]" (ref [12] = Bigi et al., PLB 181, 157 (1986), line 4237) | rpp2026-rev-top-quark.txt:130-131 |
| hadronization time 1/Λ_QCD | **PIN OWED.** The PDG 2026 top review gives no numerical 1/Λ_QCD or hadronization time. It says only "timescale of non-perturbative strong interactions" (line 14) and, for the mass, "Q0 · αs(Q0) with Q0 ∼ 1 GeV, i.e., of order 0.5 GeV" (line 104). The original source, Bigi et al. 1986, is not on arXiv and has not been opened | — |

## 4. Flags (BW vs pole; disagreements; extraction artefacts)

- **F1 X(3872): BW vs pole vs Flatte.** The PDG "Mass m = 3871.64" is a Breit-Wigner average from the J/psi X mode (list:74-76). It is dominated by LHCb 20S (list:79). PDG 2026 also gives a T-matrix pole (from BESIII 24C alone), OUR ESTIMATE (list:52). LHCb says a BW is questionable because thr - m < Γ_BW (2005.13419:474-475). Its Flatte analysis puts the pole on sheet II at E = +0.06 - 0.13i MeV relative to threshold, "compatible with a quasi-bound D0 D*0 state but a quasi-virtual state is still allowed at 2σ" (2005.13419:37-39). **The sign of the offset is therefore not settled:** BW gives -0.06 to -0.07 ± 0.1, the PDG pole Re gives +0.01 ± 0.15, and LHCb Flatte gives +0.06.
- **F2 X(3872) PDG label.** The PDG pole header reads "relative to D 0 D ∗+ threshold" (tab-mesons-c-cbar.txt:1821; list:27), but the footnote says "D ∗0 D 0 channel" (list:41). The numbers only work for D0 D*0bar: 3871.70 - 0.01 = 3871.69, while D0 D*+ = 3875.11. This is either a PDG typo or a lost overbar in pdftotext. It needs checking against the HTML/pdgLive page.
- **F3 T_cc: BW vs unitarised, and label order in 2109.01056:266-268.** As extracted, the text gives "for the FBW profile ... δm = −361, w = 47.8 keV" and "for the FU profile ... δm = −279, w = 409 keV". The numbers match the other way round: FU goes with the pole (Γ_pole = 48 keV) and FBW with Γ_BW = 410 keV. Either the arXiv v4 text swaps the labels or the subscripts were mis-extracted, so check against the journal PDF. The BW (Nature Phys) and unitarised (Nature Comm) masses differ by about 86 keV (-273 vs -359). The widths differ by about 8× (410 keV BW vs 48 keV pole). The Nature Comm paper says the BW parameters are biased, and PDG repeats this (list-T-cc:55-56).
- **F4 Z_c(3900): the papers disagree.** The 2013 discovery BW gives 3899.0 ± 6.1 and Γ = 46 ± 22. The PDG 2026 average (S = 1.7) is 3886.7 ± 2.3 with Γ = 29.5 ± 2.4. BESIII 25BU gives 3884.6 ± 0.7 ± 3.3 and Γ = 37.2 (list:28,99). The offset from the D Dbar* threshold shrinks from about +22 to about +10 MeV. All are BW fits that neglect interference (1303.5949:162).
- **F5 Z_b.** BONDAR 12 masses and widths are the channel-averaged BW values, and PDG uses them as its values (no "OUR AVERAGE" line). GARMASH 15 values are listed but not used (list-Tbb-10610:20-31). PDG gives the B* mass without a charge label, plus m(B*+) - m(B+). The B*0 mass is therefore not separately pinned, and B+ B*0bar uses m(B*) = 5324.75.
- **F6 P_c states:** BW masses only (relativistic BW amplitudes, 1904.03947:116). No pole positions are given. The Sigma_c+ mass error is asymmetric (+0.22/-0.16), and the threshold error above uses 0.22.
- **F7 T*_cs0(2870)0 / T*_cs1(2900)0: LHCb results disagree.** The 2870 mass ranges over 2866 / 2883 / 2914. The PDG average has CL = 0.044 and S = 1.8 (list-Tcs-2870:30-37). The 2870 width ranges over 57 / 87 / 128. For T*_cs1 the 2024 mass line reads "2887 +- 8 + 7" (list-Tcs1:17): the errors are garbled in extraction and there is no PDG average, so it is **PIN OWED** as a clean value.
- **F8 P_cs(4459)0 is evidence only.** It is 3.1σ at LHCb and 2.8σ at Belle (list-Pccs-4459:20-22). The LHCb paper says the structure "is also consistent with being due to two resonances", at 4454.9 ± 2.7 (Γ 7.5 ± 9.7) and 4467.8 ± 3.7 (Γ 5.2 ± 5.3), stat. errors only (2012.10380:430-431). It is not well-established and is included only for completeness.
- **F8b P_cs(4338)0 is the only exotic baryon in the PDG 2026 summary table** (sum-baryons.txt:3856-3861, "EXOTIC BARYONS"). The P_c states, T_cc, Z_c, Z_b, T_cs and X(6900) are all "OMITTED FROM SUMMARY TABLE" or appear only in the Listings.
- **F9 X(6900): model dependence.** The mass shifts by 19 MeV and the width doubles depending on the interference assumption (2006.16957:638-651). PDG averages LHCb (the interference model), ATLAS and CMS. All are BW parametrisations.
- **T1 Threshold errors** do not account for correlations between D masses (the kaon-mass correlation discussed in 2005.13419:58-61). The mass-difference route gives the same central values to within 0.006 MeV.
- **T2** "Nearest" means nearest among the S-wave two-hadron thresholds with matching flavour content. For Z_b(10610), B+ B*0bar and B0bar B*+ differ by 0.31 MeV, and both are given.

## 5. Sources (files in this directory; lines used)

| file | origin | lines used |
|---|---|---|
| 2005.13419.txt | arXiv:2005.13419v3, LHCb, PRD 102 (2020) 092005 | 28-29, 34-39, 44, 61, 444, 474-475, 836, 840 |
| 2005.13422.txt | arXiv:2005.13422v4, LHCb, JHEP 08 (2020) 123 | 45-46, 51, 655-656, 668, 678, 682-688 |
| 2109.01038.txt | arXiv:2109.01038v4, LHCb, Nature Phys. | 34, 80, 200-201, 265-268 |
| 2109.01056.txt | arXiv:2109.01056v4, LHCb, Nature Commun. 13, 3351 | 45, 247, 266-268, 667-672, 942-943, 950, 968-972 |
| 1904.03947.txt | arXiv:1904.03947v2, LHCb, PRL 122 222001 | 27, 33, 116, 358-370, 460-463 |
| 1303.5949.txt | arXiv:1303.5949v2, BESIII, PRL 110 252001 | 162, 165 |
| 1309.1896.txt | arXiv:1309.1896, BESIII Z_c(4020), PRL 111 242001 | 183, 520-521 |
| 1110.2251.txt | arXiv:1110.2251, Belle, PRL 108 122001 | 155-156 |
| 2009.00025.txt | arXiv:2009.00025v3, LHCb, PRL 125 242001 | 34 |
| 2009.00026.txt | arXiv:2009.00026v3, LHCb, PRD 102 112003 | 35, 1484-1485 |
| 2212.02716.txt | arXiv:2212.02716v3, LHCb, PRL 131 041902 | 23-24, 34, 433-434 |
| 2210.10346.txt | arXiv:2210.10346v2, LHCb, PRL 131 031901 | 25-26, 34, 370, 440 |
| 2012.10380.txt | arXiv:2012.10380v2, LHCb, Sci. Bull. 66 1278 | 29-30, 43, 362, 430 |
| 2006.16957.txt | arXiv:2006.16957v2, LHCb, Sci. Bull. 65 1983 | 35, 638-651 |
| rpp2026-tab-mesons-charm.txt | PDG 2026 summary table | 13, 537, 1519-1520, 1541-1543 |
| rpp2026-tab-mesons-charm-strange.txt | PDG 2026 | 526 |
| rpp2026-tab-mesons-bottom.txt | PDG 2026 | 81, 1586, 3423-3425 |
| rpp2026-tab-mesons-strange.txt | PDG 2026 | 503 |
| rpp2026-tab-mesons-c-cbar.txt | PDG 2026 | 108, 1303, 1817-1870 |
| rpp2026-sum-baryons.txt | PDG 2026 baryon summary | 2410-2412, 2527, 2620, 3856-3870 |
| rpp2026-sum-quarks.txt | PDG 2026 quark summary | 63-64 |
| rpp2026-rev-top-quark.txt | PDG 2026 review 61 "Top Quark" (rev. Sept 2025) | 14-15, 104, 129-131, 712, 2804-2806, 4237 |
| rpp2026-list-t-quark.txt | PDG 2026 listing | 741-745 |
| rpp2026-list-chi-c1-3872.txt | PDG 2026 listing | 27-52, 74-100, 213, 863-864 |
| rpp2026-list-T-cc-3875-plus.txt | PDG 2026 listing | 13-62, 81-82 |
| rpp2026-list-P-c-cbar-4312-plus.txt, -4440-plus, -4457-plus | PDG 2026 listings | 13, 14, 21, 24, 27-35, 80 |
| rpp2026-list-T-c-cbar-1-3900.txt | PDG 2026 listing | 27-51, 98-99, 144-154, 282 |
| rpp2026-list-T-c-cbar-4020.txt | PDG 2026 listing | 27, 42, 78-83, 151 |
| rpp2026-list-T-b-bbar-1-10610.txt, rpp2026-list-T-b-bbar-1-10650-plus.txt | PDG 2026 listings | 18-19, 45, 52, 89-105, 270 |
| rpp2026-list-T-star-c-sbar-0-2900.txt | PDG 2026 (T*cs0(2900)) | 16, 21, 31, 44, 55, 74-77 |
| rpp2026-list-T-star-cbar-sbar-0-2870-zero.txt | PDG 2026 (was X0(2900)) | 17-37, 57-62, 93-94 |
| rpp2026-list-T-star-cbar-sbar-1-2900-zero.txt | PDG 2026 (was X1(2900)) | 17-18, 28, 41 |
| rpp2026-list-P-c-cbar-s-4338-zero.txt, rpp2026-list-P-c-cbar-s-4459-zero.txt | PDG 2026 | 13-44 |
| rpp2026-list-T-c-c-cbar-cbar-6900-zero.txt | PDG 2026 | 10, 17-25, 42, 76 |
| ../../sources_grace_2026-09-25/meson_photon/rpp2026-tab-mesons-light.txt | PDG 2026 (pre-existing) | 190 |

The PDFs are kept next to their .txt files. Other downloaded listings (D, B, Sigma_c, Lambda_c, J/psi, K) are on disk but were not needed; the summary-table values were used.
