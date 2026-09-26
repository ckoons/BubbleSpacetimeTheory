# KAON HINGE — f_K±/f_π± falsifier inputs (draft)

Grace, 2026-09-26. Every number is read from a source text saved to disk; file:line given.
Path abbreviations:
- `S25/` = `data/sources_grace_2026-09-25/`
- `S26/` = `data/sources_grace_2026-09-26/kaon/`

Prediction under test: f_K+/f_π+ = **1.2065(15)**, described as the isospin-corrected charged ratio. No file in the repo contains "1.2065" or "0.27679" outside these source folders (grep run 09-26), so I could not check how the prediction was derived. **See the convention flag in Section 0 before you use any σ below.**

---

## 0. CONVENTION FLAG (read first)

Two conventions are in use, and the "discrepancy" between PDG 1.1978 and FLAG 1.1934 comes down to them.

| Quantity | Convention | Source (quote) |
|---|---|---|
| FLAG 2024 1.1934(19) | **charged, pure QCD with strong-isospin breaking (no QED)** | "Here, and in the following, fK± and fπ± are the isospin-broken decay constants in QCD." S25/flag.txt:3425. Table 17 caption: "fK/fπ is the pure QCD isospin-symmetric ratio, while fK±/fπ± is in pure QCD including the isospin-breaking correction" S25/flag.txt:3926-3928 |
| 1.1978(22) (Cirigliano et al. 2022) | **isospin-limit** F_K/F_π | "the N_f = 2+1+1 isospin-limit ratio of decay constants F_K/F_π = 1.1978(22) [93–96]" S25/r4/a2208.11707.txt:135-136 |
| PDG 2026 Vud/Vus review, same 1.1978(22) | **labelled** "isospin broken decay constants fK+/fπ+" | S25/vv26.txt:211-213 = S26/pdg26_rpp2026-rev-vud-vus.txt:211-213. This is a **label error in PDG**: the number is Cirigliano's isospin-limit average. It comes paired with 0.27679 from "A recent fit [14,25]" (S25/vv26.txt:207-209; [14] = arXiv:2208.11707, S25/vv26.txt:279), and 0.27679/1.1978 = 0.231082, which matches PDG's (67.17) 0.23108(51) (S25/vv26.txt:217) and Cirigliano's Eq. (7) 0.23108 (S25/r4/a2208.11707.txt:94-96, Eq. 7; Table 1 row :166). |
| 0.27679 = \|V_us/V_ud\| F_K/F_π | **isospin-limit** F_K/F_π (strong-IB correction moved to the experimental side) | Cirigliano et al. Table 1 (S25/r4/a2208.11707.txt:171). Formalism in Cirigliano–Neufeld Eq. (3.1): "(1 − δEM/2 − δSU(2)/2)", with F_K/F_π in the isospin limit (S26/a1102.0563.txt:296-301, 185-187) |
| 0.27599 = \|V_us/V_ud\| f_K+/f_π+ | **charged** | FLAG Eq. (65) S25/flag.txt:3421-3423; PDG leptonic review (71.9)/(71.12) S26/pdg26_rpp2026-rev-pseudoscalar-meson-decay-cons.txt:268, 283 |
| 0.27683(35) | **isospin-symmetric** (lattice δR_Kπ) | Di Carlo 2019 Eq. (107) S26/a1904.08731.txt:2579; FLAG Eq. (68) S25/flag.txt:3471 ("the ratio of the decay constants is the one corresponding to isosymmetric QCD", flag.txt:3474-3475) |

Arithmetic checks (mine):
- (0.27599/0.27679)² − 1 = −0.00577. This is the effective δSU(2) that separates the two conventions, in line with the lattice δSU(2) values −0.0054(14), −0.0052(9), −0.0073(6) (S25/flag.txt:4109-4110).
- 1.1978 × √(1 − 0.0073) = 1.19342, which is FLAG's 1.1934 to four decimals. So PDG 1.1978 and FLAG 1.1934 **agree** once the convention is matched. I found no source-level discrepancy between them.

**Consequence for the falsifier.** If 1.2065 came from 0.27679 divided by a predicted \|V_us/V_ud\|, it is an **isospin-limit** prediction and should be compared with the iso column in Table 2 (e.g. 1.1978(22): 3.27σ). If it truly is the charged ratio, compare it with the charged column (FLAG 1.1934(19): 5.41σ) and pair it with 0.27599, not 0.27679. Implied \|V_us/V_ud\| for 1.2065 (my arithmetic): 0.27599/1.2065 = 0.22875 (charged pairing) versus 0.27679/1.2065 = 0.22942 (iso pairing). **Convention pin owed on the theory side.**

---

## 1. FLAG 2024 N_f = 2+1+1 average f_K±/f_π± = 1.1934(19)

Source: FLAG Review 2024, arXiv:2411.04268v3 (S25/flag.txt:1-10 header: "arXiv:2411.04268v3 [hep-lat] 6 Feb 2026").

Average line: "direct, Nf = 2+1+1: fK±/fπ± = 1.1934(19) Refs. [20, 42–45]" (S25/flag.txt:4119). Also in the summary table (S25/flag.txt:479).

### Table 1: inputs to the average (refs [20, 42–45])

| Label | arXiv | f_K/f_π (iso), FLAG Tab.17 | f_K±/f_π± (charged), FLAG Tab.17 | Primary-paper pin |
|---|---|---|---|---|
| ETM 21 [45] | 2104.06747 (flag.txt:21761-21762) | 1.1995(44)(7) (flag.txt:3886) | 1.1957(44)(7) (flag.txt:3886) | iso 1.1995(44) S26/a2104.06747.txt:180; charged 1.1957(44) S26/a2104.06747.txt:190 |
| CalLat 20 [44] | 2005.04795 (flag.txt:21758-21759) | 1.1964(32)(30) (flag.txt:3887) | 1.1942(32)(31) (flag.txt:3887) | iso 1.1964(44) S26/a2005.04795.txt:126-128; charged 1.1942(45) S26/a2005.04795.txt:133-135 |
| FNAL/MILC 17 [20] | 1712.09262 (flag.txt:21668-21669) | 1.1980(12)(+5−15) (flag.txt:3888-3889) | 1.1950(15)(+6−18) (flag.txt:3888-3889) | charged 1.1950(15)stat(+4−17)syst(3)fπ,PDG[3]EM S26/a1712.09262.txt:1961-1962; iso 1.1980(12)(+3−14)(3)[3] :1963-1964; difference 0.00305(50) :1966 |
| ETM 14E [43] | 1411.7908 (flag.txt:21754-21756) | 1.188(11)(11) (flag.txt:3891) | 1.184(12)(11) (flag.txt:3891) | charged 1.184(16) S26/a1411.7908.txt:121; iso 1.188(15) :352 |
| HPQCD 13A [42] | 1303.1670 (flag.txt:21750-21752) | 1.1948(15)(18) (flag.txt:3895) | 1.1916(15)(16) (flag.txt:3895) | charged 1.1916(21) S26/a1303.1670.txt:652 |

Not in the average (not in refs [20,42–45]): FNAL/MILC 14A 1.1956(10)(+26−18) (flag.txt:3892; superseded), MILC 13A, ETM 13F, MILC 11, ETM 10E.

FLAG averaging notes:
- Correlations: "Because CalLat 20, FNAL/MILC 17 and HPQCD 13A partly share their gauge ensembles, we assume a 100 % correlation among their statistical errors. A 100 % correlation on the total systematic uncertainty is also assumed between FNAL/MILC 17 and HPQCD 13A" (flag.txt:4002-4010).
- Asymmetric errors: "we have symmetrized the asymmetric systematic error and shifted the central value by half the difference" (flag.txt:4004-4005, footnote 22).

Isospin treatment (quotes):
- The N_f = 2+1+1 inputs already include strong IB: "For Nf = 2+1+1, HPQCD [42], FNAL/MILC [20] and ETM [366] estimate a value for δSU(2) equal to −0.0054(14), −0.0052(9) and −0.0073(6)" (flag.txt:4109-4110).
- A χPT correction is applied **only** to the N_f = 2+1 iso-only results: "we apply the strong-isospin correction individually to all those results that have been published only in the isospin-symmetric limit, i.e., BMW 10, HPQCD/UKQCD 07 and RBC/UKQCD 14B at Nf = 2+1 … NLO SU(3) χPT … fK±/fπ± = fK/fπ √(1+δSU(2))" (flag.txt:4071-4079, Eq. 74), with "a 100% error to the correction" (flag.txt:4115). The δSU(2) values are about −0.0039(6) (Table 18, flag.txt:4099-4101).
- Result: "for QCD with broken isospin" (flag.txt:4121). **No QED correction is applied** to f_K±/f_π±: "QED effects cannot be ignored, and a consistent lattice treatment … becomes mandatory" (flag.txt:4124-4125). QED enters only through δEM on the experimental side (Eq. 65).
- Derived: \|V_us\|/\|V_ud\| = 0.23126(50) from Eq. (76) with (65) (flag.txt:4157); iso-route 0.23131(45) (flag.txt:4166).
- Hudspith et al. restate that FLAG's "1.1934(19)" is F_K±/F_π± (S25/r4/a2605.06560.txt:65-67).

---

## 2. Newest lattice determinations (2025–2026) and σ from 1.2065(15)

| Result | arXiv | N_f | f_K±/f_π± (charged) | f_K/f_π (iso) | file:line |
|---|---|---|---|---|---|
| Hudspith et al. 2026 (CalLat-type MDWF, 4-flavor DWF sea) | 2605.06560 | 2+1+1 | **1.1962(34)** | 1.1984(23)s(07)χ(17)a(17)M = [34] | S25/r4/a2605.06560.txt:40 (abstract), :147 (iso), :161 (charged, Eq. 1) |
| Conigli, Frison, Sáez 2025 (v2 Apr 2026) | 2512.19294 | 2+1 | **1.1848(59)stat(84)χ−cont(24)SU(2) [105]** | 1.1872(59)(84) [103] | S25/r4/a2512.19294.txt:800 (Eq. 5.7), :918 (Eq. 6.2), :915 (Eq. 6.1) |

Other 2025–2026 lattice work I found and read. None gives a new final f_K/f_π:
- FNAL/MILC, Merino et al., LATTICE2025 proceeding, arXiv:2603.02994. It reports the "status of a new analysis of light-meson decay constant data … present some preliminary results" (S25/r4/a2603.02994.txt:36-42). There is **no final number** (grep for 1.19x found nothing).
- BMW, Cotellucci & Giusti, arXiv:2604.19430 (LATTICE2025): IB effects in f_π, preliminary (S26/a2604.19430.txt:18-23). No f_K/f_π.
- arXiv:2603.24420 (strong-IB method via truncated polynomials): methodology only. No f_K/f_π value (grep).
- Conigli also compares with "ALPHA 25" f_K (S25/r4/a2512.19294.txt:783, Fig. 6 caption :786-791). That is not an f_K/f_π ratio result, so it is not pinned.

### Table 2: σ distance from 1.2065(15)

σ = (1.2065 − x) / √(σ_x² + 0.0015²).

| Result | x | σ_x (how combined) | √(σ_x²+0.0015²) | Δ | σ |
|---|---|---|---|---|---|
| **Charged column** | | | | | |
| FLAG24 2+1+1 avg | 1.1934 | 0.0019 | 0.00242 | 0.0131 | **5.41** |
| FLAG24 2+1 avg (flag.txt:4120) | 1.1916 | 0.0034 | 0.00372 | 0.0149 | 4.01 |
| Hudspith 26 | 1.1962 | 0.0034 | 0.00372 | 0.0103 | **2.77** |
| Conigli 25 (2+1) | 1.1848 | √(59²+84²+24²)e-4 = 0.01054 | 0.01065 | 0.0217 | **2.04** |
| ETM 21 | 1.1957 | √(44²+7²)e-4 = 0.00446 | 0.00470 | 0.0108 | 2.30 |
| CalLat 20 | 1.1942 | 0.0045 | 0.00474 | 0.0123 | 2.59 |
| FNAL/MILC 17 (upward error: √(15²+4²+3²+3²)e-4) | 1.1950 | 0.00161 | 0.00220 | 0.0115 | 5.23 |
| FNAL/MILC 17 (FLAG-symmetrised: 1.1950−0.0006, √(15²+12²)e-4) | 1.1944 | 0.00192 | 0.00244 | 0.0121 | 4.96 |
| HPQCD 13A | 1.1916 | 0.0021 | 0.00258 | 0.0149 | 5.77 |
| ETM 14E | 1.184 | 0.016 | 0.01607 | 0.0225 | 1.40 |
| **Iso-limit column** (use only if 1.2065 is iso-convention) | | | | | |
| Cirigliano22 / PDG26 avg | 1.1978 | 0.0022 | 0.00266 | 0.0087 | 3.27 |
| FLAG-4 iso avg quoted by ETM21 / Di Carlo (a2104.06747.txt:196; a1904.08731.txt:2584) | 1.1966 | 0.0018 | 0.00234 | 0.0099 | 4.23 |
| Hudspith 26 iso | 1.1984 | √(23²+7²+17²+17²)e-4 = 0.00340 | 0.00372 | 0.0081 | 2.18 |
| Conigli 25 iso | 1.1872 | √(59²+84²)e-4 = 0.01026 | 0.01037 | 0.0193 | 1.86 |
| ETM 21 iso | 1.1995 | 0.0044 | 0.00465 | 0.0070 | 1.51 |
| CalLat 20 iso | 1.1964 | 0.0044 | 0.00465 | 0.0101 | 2.17 |
| FNAL/MILC 17 iso (upward: √(12²+3²+3²+3²)e-4) | 1.1980 | 0.00131 | 0.00199 | 0.0085 | 4.27 |

The caller's "2.8σ / 2.0σ" for Hudspith and Conigli is reproduced as 2.77σ and 2.04σ (charged column). Caveats: the FLAG-average inputs are correlated (Section 1), so their σ values are **not independent**. Conigli is N_f = 2+1 with no charm sea; the PDG review estimates about 0.7% for a charm-sea effect on decay constants but notes the 3- and 4-flavor f_K+ averages "agree to much better" (S26/pdg26_rpp2026-rev-pseudoscalar-meson-decay-cons.txt:357-365).

Hudspith on direction: "more recent determinations, including this one, indicate a slightly larger value of FK±/Fπ±", and "The HPQCD determination introduces some tension in the average" (S25/r4/a2605.06560.txt:421-423). Adding Hudspith to FLAG "reduces the quoted uncertainty by a modest 10%" (S25/r4/a2605.06560.txt:427-429).

---

## 3. Where PDG 2026's 1.1978 comes from

- PDG CKM review (Ceccucci, Ligeti, Sakai, rev. March 2026): "combined with the lattice QCD result, fK/fπ = 1.1978 ± 0.0022 [10], leads to |Vus| = 0.2250 ± 0.0004" (S25/pdg2026.txt:141-143). [10] = Blucher, D'Ambrosio, Marciano review (S25/pdg2026.txt:838). KLOE BR is ref [20] = hep-ex/0509045 (S25/pdg2026.txt:860).
- PDG Vud/Vus review (Blucher, D'Ambrosio, Marciano, rev. Aug 2025, dated 1 June 2026): "A recent fit [14, 25] gives |Vus|fK+/|Vud|fπ+ = 0.27679(28)BR(20)corr (67.15). Employing the FLAG [59] lattice QCD averages for the isospin broken decay constants fK+/fπ+ = 1.1978(22) Nf = 2+1+1 (67.16)" (S26/pdg26_rpp2026-rev-vud-vus.txt:207-213; identical at S25/vv26.txt:207-213).
  - Ref [59] = FLAG 2019 (arXiv:1902.08191) plus primaries including HPQCD 13, FNAL/MILC 17, ETM 16, RBC/UKQCD, BMW, QCDSF (S25/vv26.txt:348-360). It does **not** cite FLAG 2024.
  - The number actually matches Cirigliano–Crivellin–Hoferichter–Moulson 2022, "isospin-limit ratio … F_K/F_π = 1.1978(22) [93–96]" (S25/r4/a2208.11707.txt:135-136). Refs [93–96] = HPQCD 13 (1303.1670), FNAL/MILC 17 (1712.09262), CalLat 20 (2005.04795), ETM 21 (2104.06747) (S25/r4/a2208.11707.txt:594-601). The average "accounts for statistical and systematic correlations" (:136-138).
  - Radiative/IB corrections in that fit: "We use the isospin-breaking corrections from Ref. [92]" = Di Carlo et al. 2019 (S25/r4/a2208.11707.txt:134, :591).
- PDG's *own* leptonic-decay review (Briere et al., upd. Aug 2025) instead adopts FLAG 2024 charged: "fK+/fπ+ = 1.193(2) … simply the four-flavor FLAG 2024 averages" (S26/pdg26_rpp2026-rev-pseudoscalar-meson-decay-cons.txt:368-371). Its table lists FLAG 24 1.1934(19) (:231).
- **Conclusion:** PDG 2026 carries two numbers under the same "fK+/fπ+" label: 1.1978 (Vud/Vus and CKM reviews, isospin-limit in origin) and 1.193(2) (leptonic review, charged). They differ by convention (Section 0), not by data.

---

## 4. Experimental inputs to Γ(K→μν(γ))/Γ(π→μν(γ))

| Input | Value | file:line |
|---|---|---|
| BR(K+→μ+ν(γ)), KLOE 2006 | 0.6366 ± 0.0009stat ± 0.0015syst (total 0.0017, my quadrature) | S26/ahep-ex_0509045.txt:387 (Eq. 2), abstract :80 |
| BR(K+→μ+ν), PDG 2026 fit | 63.56 ± 0.11 % OUR FIT (S=1.2); OUR AVERAGE 63.60 ± 0.16; KLOE 06A 63.66 ± 0.09 ± 0.15 (865k); CHIANG 72 63.24 ± 0.44 | S26/pdg26_rpp2026-list-K-plus-minus.txt:558-561; summary :365 |
| BR(K+→μ+ν), Cirigliano 22 global fit | 63.58(11) % (S=1.1) | S25/r4/a2208.11707.txt:151-152 |
| τ(K±), PDG 2026 | 1.2380 ± 0.0020 ×10⁻⁸ s OUR FIT (S=1.8). Inputs: KLOE 08 1.2347(30), KOPTEV 95 1.2451(30) & 1.2368(41), OTT 71 1.2380(16), LOBKOWICZ 69 1.2272(36), FITCH 65B 1.2443(38) | S26/pdg26_rpp2026-list-K-plus-minus.txt:291-300 |
| τ(K±), Cirigliano 22 fit | 12.384(15) ns (S=1.2) | S25/r4/a2208.11707.txt:163-164 |
| Γ(K+→μ+ν[γ]), PDG review | 5.134(12)×10⁷ s⁻¹ (from 63.56(11)% and 12.380(20) ns) | S26/pdg26_rpp2026-rev-pseudoscalar-meson-decay-cons.txt:198-199 |
| τ(π±), PDG 2026 | 2.6033 ± 0.0005 ×10⁻⁸ s OUR AVERAGE (S=1.2) | S26/pdg26_rpp2026-list-pi-plus-minus.txt:153 |
| BR(π+→μ+ν) | 99.98770 ± 0.00004 % | S26/pdg26_rpp2026-list-pi-plus-minus.txt:204 |
| Γ(π→μν[γ]) | 3.8408(7)×10⁷ s⁻¹ | S26/pdg26_rpp2026-rev-pseudoscalar-meson-decay-cons.txt:179-180 |
| Γ ratio R_A | **1.3367(32)** (PDG review); 1.3367(32) (Conigli, citing PDG); 1.3367(25) (PIONEER 2022) | pdg26 rev :265; S25/r4/a2512.19294.txt:868; S26/a2203.01981.txt:378 |
| δEM (χPT), Cirigliano–Neufeld 2011 | δEM = δEM^K − δEM^π = −0.0069(17) ("25% uncertainty … higher order") | S26/a1102.0563.txt:151-162, 166-167; summary :404 |
| δSU(2) (χPT), Cirigliano–Neufeld 2011 | −0.0043(5)(11) = −0.0043(12) | S26/a1102.0563.txt:288 (Eq. 2.23), :404 |
| δK/π used by PDG review | −0.0069(17) | S26/pdg26_rpp2026-rev-pseudoscalar-meson-decay-cons.txt:175 |
| δR_Kπ lattice, Di Carlo et al. 2019 (RM123S) | −0.0126(14) (= QED + strong IB, GRS scheme) | S26/a1904.08731.txt:2574 (Eq. 106) |
| δR_Kπ lattice, RBC/UKQCD 2022 | −0.0086(3)stat(+11−4)fit(5)disc(5)quench(39)vol | S26/a2211.12865.txt:216 (Eq. 1.4). χPT comparison −0.0112(21) :225 |
| δR_Kπ, Conigli (χPT, conservative) | −0.0112(40)SU(2)(14)EM | S25/r4/a2512.19294.txt:854 (Eq. 5.12) |

Resulting \|V_us/V_ud\| × f_K/f_π:

| Value | Convention | Source |
|---|---|---|
| **0.27679(28)BR(20)corr** | isospin-limit (Cirigliano 22 fit) | S26/pdg26_rpp2026-rev-vud-vus.txt:209; S25/r4/a2208.11707.txt:171 (0.27679(34) "current fit") |
| 0.27683(29)exp(20)th = 0.27683(35) | iso (Di Carlo δR_Kπ) | S26/a1904.08731.txt:2579; FLAG S25/flag.txt:3471 |
| **0.27599(33)(24)** | charged (δK/π = −0.0069) | S26/pdg26_rpp2026-rev-pseudoscalar-meson-decay-cons.txt:268, 283 ("These values are unchanged since the last reviews", :286); FLAG (65) 0.27599(41) S25/flag.txt:3423 |
| 0.27604(33)exp(19)EM | charged (Conigli, δEM = −0.0072(14)) | S25/r4/a2512.19294.txt:873 |
| 0.2763(5) | iso (Cirigliano–Neufeld 2011, older widths) | S26/a1102.0563.txt:311 |

**0.27679 is still the current value in PDG 2026** (Vud/Vus review, Eq. 67.15). The charged-convention current value is 0.27599 (leptonic review).

**Sensitivity (my arithmetic).** These experimental inputs do **not** enter lattice f_K/f_π at all; they enter only the \|V_us/V_ud\| extraction. \|V_us/V_ud\|·f_K/f_π ∝ √R_A, so relative errors are halved:

| Input | Relative error on the product |
|---|---|
| R_A (0.24%) | 0.12% |
| BR(Kμ2) (0.17%) | 0.09% |
| τ_K (0.16%) | 0.08% |
| τ_π (0.02%) | 0.01% |
| δK/π (±0.0017) | 0.085% |

Moving 0.27679 by 1% would take a 2% shift in R_A, which is about 8× its current error.

---

## 5. What could move each input (only where I found a primary/official statement)

| Input | Candidate mover | Statement found | file:line |
|---|---|---|---|
| Lattice f_K/f_π (2+1+1) | Hudspith/CalLat MDWF follow-up | "further ensembles at the physical point are planned"; with more computing, "significantly reducing the uncertainty of our final result to match that of Refs. [23, 24]" (i.e. ~0.0020) | S25/r4/a2605.06560.txt:409-410; :430 → :396-398 (column continuation) |
| Lattice f_K/f_π (2+1+1) | FNAL/MILC new correlated SChPT analysis | "status of a new analysis of light-meson decay constant data … preliminary results" (no date or target precision) | S25/r4/a2603.02994.txt:36-42 |
| Lattice f_K/f_π (2+1) | Conigli et al. | "Increased statistics … further ensembles at the physical point for finer lattice spacings … expected to substantially help" | S25/r4/a2512.19294.txt:927-934 |
| Lattice IB/QED | BMW f_π IB programme | ongoing, "next steps and plans" | S26/a2604.19430.txt:18-23 |
| FLAG average | **FLAG 2027** | "deadline for publications to be included in the next review is 30 April 2027. We expect to make the next FLAG Review public in October that year." It covers "kaon and pion decay constants" | S26/flag_submission_form_2026-09-26.txt:44-50 (page last updated 2026-07-02, :42) |
| BR(Kμ2) / Kμ3/Kμ2 | NA62 | **Official NA62 statement: not found.** A theorist proposal exists: "a measurement of the Kμ3/Kμ2 branching fraction at the level of 0.2% … as possible for example at NA62", and "the data base for Kℓ2 is completely dominated by a single experiment [35]" (= KLOE 2006). The 2026 NA62 status talk (arXiv:2605.02415) covers K→πνν̄ and dump mode only, with no Kμ2 result. Table 1 of the proposal shows that a 0.2% Kμ3/Kμ2 at ±2σ moves the product by ±0.00047/−0.00045, i.e. **~0.17%**, not 1%. | S25/r4/a2208.11707.txt:22-25, 120-122, 171; S25/r4/a2605.02415.txt (no Kμ2 content, grep) |
| BR(Kμ2), KLOE-2 / J-PARC | — | not found | — |
| τ(K±) | — | not found. The listing carries S=1.8 with KLOE 08 1.2347(30) vs KOPTEV 95 1.2451(30) scatter (pdg K± list :291-296) | — |
| τ(π±), BR(πμ2) | PIONEER | PIONEER (PSI proposal R-22-01.1) does **not** remeasure the πμ2 rate. It targets R_e/μ and pion β decay. Its Phase-2 goal gives an *independent* vector-channel \|V_us/V_ud\| at 0.2% via R_V, to "match the precision of the current extraction … from the axial channels", R_A = 1.3367(25). Pion lifetime is "presently known to 0.02% precision" | S26/a2203.01981.txt:1 (header), :360-380, :1995 |
| δEM / δR_Kπ | Lattice QED programmes | RM123S −0.0126(14) and RBC/UKQCD −0.0086(…)(39)vol differ by about 1σ; FLAG: "can be readily improved by more realistic simulations and higher statistics" (S25/flag.txt:4169-4170). No scheduled run with a date was found | as cited |

---

## Sources on disk (all read)

S25 (reused): `flag.txt` (arXiv:2411.04268v3), `pdg2026.txt` (PDG CKM review rev. Mar 2026), `vv26.txt` (PDG Vud/Vus review), `r4/a2605.06560.txt` (Hudspith), `r4/a2512.19294.txt` (Conigli v2), `r4/a2208.11707.txt` (Cirigliano et al. 2022), `r4/a2603.02994.txt` (FNAL/MILC LAT25), `r4/a2605.02415.txt` (NA62 2026), `r4/flag_web_mainpage_2026-09-25.txt`.

S26 (fetched 2026-09-26, arXiv PDFs → `pdftotext -layout`): `ahep-ex_0509045` (KLOE 2006), `a1102.0563` (Cirigliano–Neufeld), `a1904.08731` (Di Carlo 2019), `a1711.06537` (Giusti 2018), `a2211.12865` (RBC/UKQCD δR_Kπ), `a2104.06747` (ETM 21), `a2005.04795` (CalLat 20), `a1712.09262` (FNAL/MILC 17), `a1303.1670` (HPQCD 13A), `a1411.7908` (ETM 14E), `a1509.02220` (Rosner–Stone–Van de Water 2015), `a2203.01981` (PIONEER), `a2604.19430` (BMW IB f_π), `a2603.24420`; PDG 2026 from pdg.lbl.gov/2026: `pdg26_rpp2026-rev-pseudoscalar-meson-decay-cons`, `pdg26_rpp2026-rev-vud-vus`, `pdg26_rpp2026-list-K-plus-minus`, `pdg26_rpp2026-list-pi-plus-minus`, `pdg26_rpp2026-sum-mesons`; `flag_submission_form_2026-09-26.txt` (flag.unibe.ch/2024/Submission form).

PIN OWED / not found: an official NA62 Kμ2 or Kμ3/Kμ2 plan; any new K± lifetime or Kμ2 BR experiment; a derivation file for 1.2065 in this repo (to settle its convention).
