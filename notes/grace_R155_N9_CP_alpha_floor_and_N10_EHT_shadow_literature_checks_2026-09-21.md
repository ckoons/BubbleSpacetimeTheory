# Grace R155 — N9 (CP = α floor at black-hole horizons) and N10 (EHT shadow deviation): register rows and same-day literature checks (2026-09-21)

**Written 2026-09-21 07:49–07:51 EDT (clock). On Keeper's science priorities of 09-20 (items 1 and 4), handed out by Casey this morning. Register v0.19: N9 and N10 added to Section N, no other row touched. Keeper gates. `didwe` run first: "circular polarization", "black hole shadow", "Kerr deviation", "EHT" — 0 rows each; "Stokes" — 4 rows, all Millennium/Navier–Stokes, not this ground. New lane.**

## 1. N9 — the CP floor

### 1.1 The claim as the volume states it
`Guide/Vol5_Predictions/Ch01_Predictions_Program.md:325`: "CP_geometric = α × 2GM/(Rc²). At any black hole horizon: CP = α = 0.730 %, independent of mass. Frequency-independent. The observed CP is |α + A sin(RM/ν² + φ₀)| (signed addition of geometric floor + oscillatory Faraday). The signed model fits Sgr A* multi-frequency data …" Falsifier table :342 "CP floor at BH horizon | CP = α = 0.730 %, mass-independent | EHT Stokes V | Data exists"; :361 kill-condition "No frequency-independent CP floor; floor differs between BH masses". Source: `notes/BST_CP_Alpha_Paper.md` (2026-03-12), never audited, no toy, no T-row, no K.

### 1.2 What the source actually does
- Fixes α at the horizon (:134), then fits eight Sgr A* points (4.8–345 GHz) with |α + A sin(RM_eff/ν² + φ₀)| — A, RM_eff, φ₀ free: three parameters against eight points, reported as χ²_red = 0.22 and "zero free parameters for the geometric component".
- Its own radial table (:147–153) puts the EHT emission region (2–3 R_s) at 0.24–0.49 %, then says the observed ∼1 % is "slightly above" α "consistent with residual Faraday contribution … combined with lensing enhancement" (:303–308). The floor is stated at R = R_s; no photon from R = R_s is observed. Recorded for Lyra and Cal, not ruled.
- Its 4.8 GHz entry "0.31 ± 0.13 (Bower et al. 1999)" is not the primary's number (1.3 below).

### 1.3 The primaries (DOIs resolved through Crossref today; text read where marked)
| Object | ν | CP | epoch | source |
|---|---|---|---|---|
| Sgr A* | 4.8 GHz | m_c = −0.36 ± 0.05 %; CP spectral index −0.6 ± 0.3 over 4.8–8.4 GHz | 1999 | Bower, Falcke & Backer, ApJL 523, L29 (1999), doi:10.1086/312246 — arXiv astro-ph/9907215 abstract read |
| Sgr A* | 230 / 345 GHz | −1.2 ± 0.3 % / −1.6 ± 0.3 %, LCP as at all lower frequencies; CP spectrum ∝ ν^{0.35 ± 0.03} | 2005–2007 SMA | Muñoz, Marrone, Moran & Rao, ApJ 745, 115 (2012), doi:10.1088/0004-637X/745/2/115 — PDF read |
| Sgr A* | 225 GHz | mean −1.1 ± 0.2 %; in-band change up to 25 %; sign of the frequency slope time-variable; handedness stable > 11 yr | 2016 ALMA | Bower et al., ApJ 868, 101 (2018), doi:10.3847/1538-4357/aae983 — PDF read |
| Sgr A* | 1.3 mm / 3 mm | −1.0 to −1.6 % / ∼0.7–1.1 % | 2017 ALMA (EHT campaign) | Goddi et al., ApJL 910, L14 (2021), doi:10.3847/2041-8213/abee6a — PDF read |
| Sgr A* | 230 GHz | daily averages −0.41 % to −1.0 %; CP variability ∼50 %; "tentative detections … below the official CP accuracy threshold guaranteed by the ALMA observatory" | 2018 ALMA | Albentosa-Ruiz et al., A&A 708, A179 (2026), doi:10.1051/0004-6361/202556759 — PDF read (arXiv:2604.10287) |
| Sgr A* | 230 GHz, resolved | v_net fixed to ALMA mean −1.5 %; ring CP dipole ∼5–10 %, negative in the west | 2017 EHT | EHT Collaboration, Sgr A* Paper VII, ApJL 964, L25 (2024), doi:10.3847/2041-8213/ad2df0 — PDF read |
| M87* | 230 GHz, resolved | ⟨|v|⟩ < 3.7 %; ALMA image-integrated |v_int| < 1 % | 2017 EHT | EHT Collaboration, M87* Paper IX, ApJL 957, L20 (2023), doi:10.3847/2041-8213/acff70 — PDF read |
| M87* | 1.3 mm | CP ∼0.3 % (tentative) | 2017 ALMA | Goddi et al. 2021 (above), Table 12 |

### 1.4 Verdict, property by property
1. **A 0.73 % floor.** Published values below it exist on both objects: Sgr A* −0.36 % at 4.8 GHz (1999), Sgr A* daily −0.41 % at 230 GHz (2018), M87* < 1 % and ∼0.3 % tentative. The corpus model absorbs any sub-floor value by signed cancellation with a three-parameter term, so the floor cannot fire in either direction. **NOT TESTABLE AS STATED.**
2. **Frequency-independent.** The primaries measure a rising spectrum (ν^{0.35}, Muñoz) with a time-variable slope (Bower 2018). Fitting that with A, RM_eff, φ₀ is not a test of α. **UNDECIDABLE**, and the "frequency-independent" word is contradicted by every multi-frequency primary unless the Faraday term is invoked.
3. **Mass-independent.** Sgr A* ∼1 % vs M87* < 1 % (∼0.3 % tentative) — consistent with any common value from 0 to ∼1 %. **UNDECIDABLE** at current precision; a real test needs M87* CP detected, not bounded.
4. **The radius.** Nothing at R = R_s is observed; the EHT ring is emission at several GM/c², where the corpus formula gives 0.24–0.49 % — below the measured ∼1 %. The paper reads this both ways. **For Lyra and Cal.**
5. **Handedness.** Sgr A* is LCP at every frequency for > 11 yr; a compactness formula gives a magnitude and says nothing about sign. Not a fire, a gap in the claim.

Kill-condition if the row is ever re-stated: a fixed-epoch ring CP with the Faraday term independently constrained from the LP rotation measure, sitting below the geometric value at the emission radius.

## 2. N10 — the EHT shadow deviation

### 2.1 Source hunt
`Guide/Vol1_Journey/Ch01_The_Journey.md:1374`: "BST predicts a specific deviation in the black hole shadow shape from the Kerr metric." Corpus-wide grep (Guide, Curriculum, notes, play, registry, board): the only number is **"(27/2)(1 + rank/N_max)"** at `notes/BST_What_Gets_Wrong.md:254` (INV-4; first commit 1dec7de3, 2026-04-24, "v34 … 303 invariants") and `notes/Paper83_Draft.md:979`, whose :990 lists it as "EHT shadow diameter". No unit, no derivation, no toy, no T-row, no board discussion. **No shape anywhere.**

### 2.2 The check
(27/2)(1 + 2/137) = 13.697. Schwarzschild shadow diameter 2√27 = 10.392 GM/c²; Kerr 9.6–10.4 by spin and inclination.
- **Reading (a), literal diameter 13.70 GM/c²:** δ = +0.318. M87* 2017: δ = −0.01 ± 0.17 (68 %, stellar prior) — EHT M87* Paper VI, ApJL 875, L6 (2019), doi:10.3847/2041-8213/ab1141 (PDF read) → 1.9σ high. Sgr A* 2017: δ = −0.08 +0.09/−0.09 (VLTI), −0.04 +0.09/−0.10 (Keck), "within ∼10 % of the Kerr predictions" — EHT Sgr A* Paper VI, ApJL 930, L17 (2022), doi:10.3847/2041-8213/ac6756 (PDF read) → 4.4σ / 4.0σ high. **EXCLUDED.**
- **Reading (b), fractional δ_BST = +rank/N_max = +0.0146:** an order of magnitude inside every band. **UNDECIDABLE**; needs ∼1 % shadow-size precision with a mass-to-distance prior at the same level.
- The base 27/2 matches no Kerr observable (√27 = shadow radius, 27 = critical impact parameter squared).

### 2.3 Verdict
A sentence, not a prediction: the "shape" claim has no source; the number has no unit or derivation and is excluded under its literal reading. Vol1 :1374 goes to Lyra's head-note pass as retired, no instrument. The INV-4 / Paper 83 line stays an unsourced number until its author states the observable and unit or retires it.

## 3. Pins owed / not done
- Goddi 2021 M87 CP ∼0.3 % taken from the PDF's summary sentence (p. line 982) — Table 12 not transcribed.
- EHT Sgr A* Paper VIII (ApJL 964, L26, doi:10.3847/2041-8213/ad2df1) DOI pinned, not read; Paper VII's v_net is the ALMA-fixed value, not an EHT measurement.
- Bower et al. 2002 (8.4/15/22 GHz entries in the corpus table) not re-pinned.

## 4. What I did not do
Did not edit the CP paper, INV-4, Paper 83, or any volume. Did not rule on the radius. No toy (arithmetic on the rows only). Nothing pushed.

— Grace, 2026-09-21
