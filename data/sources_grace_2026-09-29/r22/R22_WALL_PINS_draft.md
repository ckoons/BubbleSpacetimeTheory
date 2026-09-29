# R22: domain-wall pins (draft)

Grace, 2026-09-29 12:17 EDT. Every quote below comes from a file in this directory, cited as file:line. The text files come from `pdftotext -layout`, except the ZKO text, which is `pdftotext` raw from the JETP scan. Formulas garbled by OCR or text extraction were read off the rendered pages and are cited as `VISUAL_TRANSCRIPTIONS.txt [tag]` (PNGs in `png/`). Anything marked **COMPUTED (Grace)** is my own arithmetic on pinned formulas. It is not a pin.

## Retrieval ledger

| # | Source | Status | Local file |
|---|---|---|---|
| 1 | Zel'dovich, Kobzarev, Okun, Zh. Eksp. Teor. Fiz. 67 (1974) 3–11 [Sov. Phys. JETP 40 (1975) 1–5] | **PRIMARY PINNED.** The English translation is free from the JETP archive at http://www.jetp.ras.ru/cgi-bin/dn/e_040_01_0001.pdf (linked from the list page, saved as `jetp_40_1_p1_list.html`). INSPIRE 91696 lists both journal refs and 1158 citations (`inspire_zko.json`). Crossref has no DOI: two queries found nothing (`crossref_zko_query*.json`). | `zko_jetp_e_040_01_0001.pdf`, `zko_jetp_raw.txt`, `png/zko_p-1..5.png` |
| 2 | Saikawa, "A review of gravitational waves from cosmic domain walls", Universe 3 (2017) 40, DOI 10.3390/universe3020040, arXiv:1703.02576v2 | **PRIMARY PINNED** | `saikawa_1703.02576.{pdf,txt}`, `crossref_10.3390_universe3020040.json`, `inspire_saikawa.json` |
| 3 | Vilenkin & Shellard, *Cosmic Strings and Other Topological Defects* (CUP 1994; pbk 2000, ISBN 978-0-521-65476-0) | **PIN OWED (paywalled book, no open copy found).** Crossref has no book DOI; the ISBN filter returned 0 (`crossref_vilenkin_shellard_isbn.json`). Metadata comes from INSPIRE 1384873 (`inspire_vilenkin_shellard.json`) and a Crossref book-review record, DOI 10.1023/a:1022924010591, which gives the ISBNs of both editions (`crossref_vilenkin_shellard_query.json`). Nothing from Ch. 13 is quoted. | none |
| 4 | Battye, Pilaftsis, Viatic, "Domain wall constraints on two-Higgs-doublet models with Z2 symmetry", PRD 102 (2020) 123536, DOI 10.1103/PhysRevD.102.123536, arXiv:2010.09840 | **PRIMARY PINNED.** This is the electroweak-scale Z2 source. | `battye_pilaftsis_viatic_2010.09840.{pdf,txt}`, `png/bpv2020_p-07/08/09.png`, `crossref_10.1103_PhysRevD.102.123536.json` |
| 5 | Abel, Sarkar, White, Nucl. Phys. B 454 (1995) 663–681, DOI 10.1016/0550-3213(95)00483-9, hep-ph/9506359 | **PRIMARY PINNED** (NMSSM Z3 at the EW scale) | `abel_hep-ph9506359.{pdf,txt}`, `crossref_10.1016_0550-3213_95_00483-9.json` |
| 6 | Battye, Brawn, Pilaftsis, "Vacuum topology of the 2HDM", JHEP 08 (2011) 020, arXiv:1106.3482 | Supporting only (the topology of the Z2 vacuum manifold) | `battye_brawn_pilaftsis_1106.3482.{pdf,txt}` |
| X | arXiv:1102.3591 (the "Battye et al." ID in the brief) | **WRONG ID.** It is V. Berezinsky, "High Energy Neutrino Astronomy". It is kept under a WRONG_ID_ filename so the miss stays on record; no Battye paper has this number. The intended 2HDM domain-wall papers are #4 and #6. | `WRONG_ID_1102.3591_*` |

---

## 1. Zel'dovich–Kobzarev–Okun 1974 (primary)

### 1a. Conventions (quoted before any number)

- **Units:** "We utilize units with ħ = c = 1." (footnote 2; `VISUAL_TRANSCRIPTIONS.txt [Z-V4]`; the OCR reads "I'! = c = I" at `zko_jetp_raw.txt:589`)
- **Which symmetry is broken:** a discrete, sign-type symmetry of a pseudoscalar. ZKO frame it as spontaneous CP violation, not as a named "Z2". The Lagrangian is L = ½(∂φ)² − λ²(φ² − η²)² + ψ̄(i∂̸ − m − igγ₅φ)ψ: "Here φ is a pseudoscalar field, ψ is the baryon field and λ and η are real parameters." The vacuum has "⟨φ⟩ = ση, where σ = ±1" (`[Z-V1]`; `zko_jetp_raw.txt:64-69`).
  - **Convention collision:** ZKO's **σ is the vacuum sign**. Their wall tension is **μ**. Their quartic is **λ²**(φ²−η²)², where Saikawa writes (λ/4)(φ²−v²)².
- **Wall tension and its units:** "the thickness of a boundary layer at rest (we shall call this layer a wall) is Δ ~ 1/m_χ ~ 1/λη, and its surface density is μ ~ λη³" (`zko_jetp_raw.txt:135-137`; exact form from `[Z-V2]`). The exact result is μ = √2 λη³ ∫(ch ξ)⁻⁴ dξ = (4√2/3) λη³ (`[Z-V2]`). "The quantity μ could be called surface tension." (`zko_jetp_raw.txt:166`). Units: energy per area, i.e. mass³ in ħ = c = 1. ZKO's observational bound is given in CGS as g/cm² (see 1b).
- **When the walls form:** "Such a structure does not exist near a cosmolgical singularity, when the temperature is above the Curie point, but this structure must appear later during the cosmological expansion and cooling down." (abstract, `zko_jetp_raw.txt:7-10`). ZKO predate inflation (1974), so the paper contains **no statement relative to inflation**. The formation time used is "The domains are formed at the time t₀: T = m ..." with t₀ ~ 10⁻⁵ sec (`[Z-V3]`; `zko_jetp_raw.txt:332-357`).

### 1b. Main conclusion (pinned)

- The observational argument, using the CMB isotropy limit of the time: "the change of potential within a cell of size L is of the order δΦ = GμL ... Observations show that this radiation does not depend on the direction (δT/T < 10⁻³). The gravitational redshift should yield δT/T ~ αδΦ ... Thus it is necessary that GμL ≪ 1." (`[Z-V3]`; `zko_jetp_raw.txt:340-347, 316`)
- "The observable picture of the Universe (its visible isotropy and homogeneity) is incompatible with the assumption of a coarse domain structure with domains having dimensions of the order of or larger than today's t. Either the parameters of the walls are such that at the present time ... one can place a large number of walls over a distance of ct = 2 × 10²⁸ cm (for this it is necessary that the superficial density of walls be μ < 0.1 g/cm², which seems unrealistic from the viewpoint of the theory of elementary particles ...), or ... the domains disappeared at some time t₂ < t₁" (`zko_jetp_raw.txt:361-373`; `[Z-V3]`)
- Section 7, "CONCLUSIONS": "2. For λ ≲ 1 the walls of the domains are so heavy that their existence would lead to a radical change of the cosmological evolution of the Universe. 3. If there is no mechanism that leads to the disappearance of domains at a sufficiently early stage of the evolution of the Universe, the domains would lead to conclusions which are in contradiction with experiment. Thus, either the model of spontaneous breakdown of CP-symmetry discussed by us is false, or there must exist mechanisms which facilitate the disappearance of the domains." (`zko_jetp_raw.txt:492-508`; `png/zko_p-4.png`)
- On the escape route: "For this one obviously must first violate the symmetry of the two solutions φ = ±η. On the other hand, the symmetry breakdown should not be contained in the Lagrangian." (`zko_jetp_raw.txt:563-566`; `png/zko_p-4.png`)
- Wall-dominated expansion (Sec. 5): walls have the equation of state p = −2ε/3 and ε = 3/(2πGt²), so b ∝ t² (`[Z-V3]`).

**Honest scope note.** ZKO **do not write "σ^{1/3} ≲ 1 MeV"**. Their own numbers are δT/T < 10⁻³ (the 1974 limit) and μ < 0.1 g/cm².
- **COMPUTED (Grace):** 0.1 g/cm² × c² = 9.0 × 10¹⁹ erg/cm² = 2.2 × 10⁴ MeV³, so μ^{1/3} ≈ 28 MeV. The O(MeV) form under the name "Zel'dovich–Kobzarev–Okun bound" comes from the modern secondary (Saikawa, 2b), which uses δρ/ρ ≲ 10⁻⁵. Quote the MeV figure as Saikawa's statement, citing ZKO. Do not quote it as ZKO's own number.

---

## 2. Modern statement: Saikawa, Universe 3 (2017) 40 (primary, arXiv v2)

### 2a. Conventions

- **Units:** no explicit ħ = c = 1 sentence was found (grep for "natural units", "ħ", "units" returned nothing). ħ = c = 1 is implicit: tensions are in TeV³/MeV³ and times in GeV⁻¹ ↔ sec. **Flag:** implicit convention, not quoted. The reduced Planck mass is used: "M_Pl ≃ 2.435 × 10¹⁸ GeV is the reduced Planck mass" (`saikawa_1703.02576.txt:240-243`).
- **Symmetry:** "V(φ) = λ/4 (φ² − v²)². Note that the potential V(φ) has two degenerate minima at φ = ±v. In this theory there is a discrete Z2 symmetry, under which the field transforms as φ → −φ. This discrete symmetry is spontaneously broken when the scalar field acquires a vacuum expectation value (VEV), ⟨φ⟩ = ±v." (Eq. (2.2), Sec. 2.1; `saikawa_1703.02576.txt:110-117`)
- **Tension:** "Integrating T₀₀ over the direction perpendicular to the wall, we obtain its surface energy density, σ = ∫dz T₀₀ = (4/3)√(λ/2) v³ ... σ is also referred to as the tension of domain walls." (Eq. (2.6); `saikawa_1703.02576.txt:142-151`; `[S-V3]`). The general estimate is "σ ∼ δ · V₀" (Eq. (2.11), `:183-187`).
- **When the walls form relative to inflation** (Sec. 2.2, `saikawa_1703.02576.txt:202-217`): "Suppose that the toy model scalar field φ ... stayed at a certain vacuum before the inflationary period. In such a setup, we naively expect that domain walls do not exist in the present universe, since a domain on which ⟨φ⟩ takes an uniform value exponentially glows during inflation ... However, such a naive expectation is not necessarily true. During inflation, the field φ acquires vacuum fluctuations of order δφ ∼ H_inf/2π if its effective mass m_φ [m_φ² = 2λv²] is smaller than H_inf ... Furthermore, ... it can thermalize ... due to the reheating after inflation. If this is the case, the discrete symmetry is thermally restored when the maximum temperature after inflation T_max becomes larger than m_φ. After that, domain walls are formed when the universe cools below some critical temperature. Therefore, we expect that the formation of domain walls can happen if either the Hubble parameter during inflation H_inf or the maximum temperature after inflation T_max is sufficiently larger than the mass m_φ of the field φ." Footnote 1 (`:246-248`): "the condition is not robust ... if the φ field never thermalizes, domain walls may not be formed even when T_max > m_φ is satisfied."

### 2b. The domain-wall problem (numbers)

- Intro (`saikawa_1703.02576.txt:73-78`): "In general, the formation of domain walls is regarded as a problem in cosmology [23], since their energy density soon dominates the total energy density of the universe, which conflicts with the present observational results. However, we can consider the possibility that domain walls are unstable and collapse before they overclose the universe [24–26]. Their unstability might be guaranteed if the discrete symmetry is only approximate and explicitly broken by a small parameter in the theory." Here [23] is ZKO (`:1139`).
- Scaling, Eqs. (2.17)–(2.18) (`:275-284`): ρ_wall(t) = 𝒜 σ/t, with "𝒜 ≃ 0.8 ± 0.1" for the Z2 model.
- Domination time, Eq. (2.19) (`:292-300`; `[S-V1]`): "From the condition ρ_c(t) = ρ_wall(t), we estimate the time at which the wall domination occurs, t_dom = 3M_Pl²/(4𝒜σ) ≃ 2.93 × 10³ sec 𝒜⁻¹ (σ/TeV³)⁻¹."
- Eq. (2.20) (`:312-318`; `[S-V2]`): "The equation of state for an isotropic gas of non-relativistic domain walls is given by w = −2/3 [36], which implies that the scale factor in the wall dominated universe evolves as R(t) ∝ t². Such a rapid expansion is incompatible with standard cosmology."
- **The bound**, Eqs. (2.21)–(2.22) (`:320-335`; `[S-V2]`): "Since their typical curvature radius is comparable to the Hubble radius, they introduce large scale density fluctuations, whose magnitude is estimated as δρ/ρ ∼ ρ_wall/ρ_c ∼ Gσt₀ ∼ 10¹² (σ/TeV³), ... The observation of the cosmic microwave background radiation implies δρ/ρ ≲ O(10⁻⁵), from which we obtain the following condition σ^{1/3} ≲ O(MeV). (2.22) This constraint was first discussed in Ref. [23], and it is referred to as the Zel'dovich-Kobzarev-Okun bound. We see that domain walls with a tension as large as σ > O(MeV³) must not exist in the universe at the present time."
- **Secondary citation of ZKO** (`saikawa_1703.02576.txt:1139`): "[23] Y. B. Zeldovich, I. Y. Kobzarev and L. B. Okun, Zh. Eksp. Teor. Fiz. 67, 3 (1974) [Sov. ..."

### 2c. The standard escapes

- Explicit breaking (bias), Sec. 2.3 (`:337-352`; `[S-V2]`): "One possible solution to the domain wall problem is to introduce an energy bias in the potential, which lifts the degenerate minima [24–26]." The paper then gives "ΔV(φ) = εvφ(φ²/3 − v²)" (2.23) and "V_bias ≡ V(−v) − V(+v) = (4/3)εv⁴" (2.24), and continues: "Because of this energy difference, domain walls become unstable and eventually collapse. Note that the additional term (2.23) explicitly breaks the discrete Z2 symmetry. Therefore, this solution works if the discrete symmetry is not exact, but holds only approximately."
- Lower bound on the bias for collapse before domination, Eq. (2.29) (`:419-426`): "Requiring that their collapse occurs before they overclose the universe t_ann < t_dom ..., we obtain the lower bound on the magnitude of the energy bias, V_bias > 4C_ann𝒜²σ²/3M_Pl²". The BBN bound, Eq. (2.32), is at `:453-456`.
- Footnote 3 (`:363-365`): the asymmetric-initial-distribution escape. "It is also possible to avoid the domain wall problem by assuming an asymmetric probability distribution for initial field fluctuations [49] instead of introducing the energy bias".
- Escape by breaking before or during inflation: see 2a (`:202-217`). It is stated as the "naive expectation" and then qualified: it fails if H_inf > m_φ or T_max > m_φ.
- **Scope caveat:** Saikawa Sec. 4.1, "Standard Model Higgs field" (`:699-745`), is about **Higgs walls between the EW vacuum and a high-scale (φ_f ≫ v) minimum** under a φ⁶/Λ² term. It is **not** a Z2 under which the Higgs is odd, so it is not the R22 case. Do not cite 4.1 for an EW-scale Z2.

---

## 3. Electroweak-scale Z2 walls

### 3a. Battye–Pilaftsis–Viatic, PRD 102 (2020) 123536 (primary; the direct case)

- **Symmetry**, Eq. (2.1) (`battye_pilaftsis_viatic_2010.09840.txt:131-133`): "Under a Z2 transformation the complex scalar Higgs doublets, Φ₁ and Φ₂, transform as Φ₁ → Φ₁, Φ₂ → −Φ₂." On exactness (`:141-144`): "The field bilinear Φ₁†Φ₂ violates the Z2 symmetry and hence this model possesses an approximate Z2 symmetry for small values of the coefficient m₁₂². Moreover, in the limit m₁₂² = 0 (2.2) possesses an exact Z2 symmetry."
- **Units:** "H₀ = 72 km s⁻¹ Mpc⁻¹ = 1.54 × 10⁻⁴² GeV in natural units" (`:409`). They use the non-reduced M_pl ≃ 1.2 × 10¹⁹ GeV (`[B-V2]`). **Convention collision:** Saikawa uses the reduced M_Pl.
- **Tension (energy per unit area):** Eqs. (3.1)–(3.3) (`[B-V1]`; `:374-392`). The dimensionless form is defined on pdf p.9 (`png/bpv2020_p-09.png`; `:506-508`): "recalling that in our dimensionless system the energy per unit area, E = M_h v²_SM Ê where M_h = 125 GeV and v_SM = 246 GeV".
- **Statement that the walls form at the EW scale**, from the abstract (`:23-26`): "The Two Higgs Doublet Model (2HDM) with spontaneously broken Z2 symmetry predicts a production of domain walls at the electroweak scale. We derive cosmological constraints on model parameters ... from the requirement that domain walls do not dominate the Universe by the present day. For Type-I 2HDMs, we deduce the lower bound on the key parameter tan β > 10⁵ for a wide range of Higgs-boson masses ∼ 100 GeV or greater close to the Standard Model alignment limit."
- **The bound**, Eqs. (3.6)–(3.7) (`[B-V2]`; `:409-422`): "For Ω_dw < 1 at present day, we obtain the limit 8πAÊM_h v²_SM/(3H₀²t₀M²_pl) < 1. Therefore, for t₀ ≃ 6.6×10⁴¹ GeV⁻¹ and M_pl ≃ 1.2×10¹⁹ GeV, we obtain the dimensionless inequality, AÊ < 3H₀²t₀M²_pl/(8πM_h v²_SM) ≃ 3.6 × 10⁻¹²."
- **Exclusion unless the symmetry is broken or the vev is tiny** (`png/bpv2020_p-08.png`; `:424-448`): "agreement with this limit can always be obtained for sufficiently large or small values of tan β ... domain walls do indeed become ultra-light in large and small limits of tan β where the VEV of the Z2 odd doublet becomes vanishingly small ... In lower tan β regimes one cannot evade the constraints placed on the Z2-symmetric 2HDM by domain wall domination without unreasonably low values of the scalar masses. It should be made clear that these results only pertain to scenarios where the 2HDM possess an exact discrete symmetry and, hence, a domain wall problem. These stringent constraints suggest that in order to have cosmologically viable 2HDM domain walls in experimentally viable parameter regimes a means of modifying the scaling behaviour of these domain walls will be required."
- Intro (`:75-82`): "domain walls will come to dominate the Universe at late times [6–8]. This is the so-called domain wall problem ... Alternatively, one could have the domain walls decay before they come to dominate the Universe by making the discrete symmetry approximate." Here [6] is ZKO (`:913`).
- Escape bound, abstract (`:34-35`): "For a 2HDM with softly-broken Z2 symmetry, we relate the size of this exponential suppression to the soft-breaking bilinear parameter m₁₂ allowing limits to be placed on this parameter of order µeV, such that domain wall domination can be avoided." See Eq. (4.7), `:646`.
- **Figure-read (not a printed number):** at tan β = 1, Fig. 1 (right) has Ê in 0.28–0.44 (`png/bpv2020_p-09.png`).
  - **COMPUTED (Grace):** with Ê ≈ 0.3, AÊ exceeds the (3.7) limit by ~10¹¹ for A ~ 1. The wall energy is E ≈ 0.3 × 125 × 246² GeV³ ≈ 2.3 × 10⁶ GeV³, so E^{1/3} ≈ 130 GeV.

### 3b. Abel–Sarkar–White, NPB 454 (1995) 663 (primary; NMSSM Z3, EW scale)

- **Symmetry:** "By invoking a Z3 symmetry under which every chiral superfield Φ transforms as Φ → e^{2πi/3}Φ" (`abel_hep-ph9506359.txt:59-60`). "The Z3 of the model is broken during the phase transition associated with electroweak symmetry breaking in the early universe." (`:77-78`)
- **Exclusion statement** (`:78-87`): "such spontaneously broken discrete symmetries lead to the formation of domains of different degenerate vacua separated by domain walls [7, 8]. These have a surface energy density σ ∼ ν³ where ν is a typical vacuum expectation value (vev) of the fields, here the electroweak scale of O(10²) GeV. Such walls would come to dominate the energy density of the universe and create unacceptably large anisotropies in the cosmic microwave background radiation unless their energy scale is less than a few MeV [9]. Therefore cosmology requires the Z3 walls to disappear well before the present era. Following the original suggestion by Zel'dovich et al [7], this may be achieved by breaking the degeneracy of the vacua". Here [7] is ZKO, Sov. Phys. JETP 40 (1975) 1, and [9] is Vilenkin, Phys. Rep. 121 (1985) 263, together with Vilenkin–Shellard CUP 1994 (`:786-790`).
- Numbers: Eq. (2), σ ≃ 5 × 10⁷ GeV³ (k/0.1)(x/5ν)³ (`:168-172`, text legible). The Fig. 1 caption gives "Total surface energy density is 8.6 × 10⁸ GeV³" (`:856`). "the surface energy is approximately M_W³ as expected on dimensional grounds" (`:102-104`).
- Convention: "ν = √(ν₁² + ν₂²) = 174 GeV" (`:163-164`). **Convention collision:** 174 GeV = 246/√2.

### 3c. Supporting: Battye–Brawn–Pilaftsis, JHEP 08 (2011) 020

- `battye_brawn_pilaftsis_1106.3482.txt:1420-1429`: "the Z2 invariant 2HDM, where the two VEVs are non-zero, can lead to non-trivial topological solutions, such as domain walls. The vacuum manifold ... M ≃ Z2 × S³ ... Π₀[Z2 × S³] ≠ I ... This leaves the possibility for the formation of domain walls in the Z2 symmetric 2HDM".

### 3d. The R22 electroweak estimate

**COMPUTED (Grace) — none of this is a pin.** Take Saikawa's single-field formula (2.6), σ = (4/3)√(λ/2) v³, with v = 246.22 GeV and λ = m_h²/(2v²) = 0.129 for m_h = 125.1 GeV. This uses Saikawa's convention m_φ² = 2λv².
- σ ≈ 5.1 × 10⁶ GeV³, so σ^{1/3} ≈ 172 GeV.
- Against (2.22), σ^{1/3} ≲ 1 MeV: over by 1.7 × 10⁵ in σ^{1/3} and 5 × 10¹⁵ in σ.
- (2.21) gives δρ/ρ ~ 10¹² × 5.1 × 10⁻³ ≈ 5 × 10⁹, against 10⁻⁵.
- (2.19) with 𝒜 = 0.8 gives t_dom ≈ 2.93 × 10³ s / (0.8 × 5.1 × 10⁻³) ≈ 7 × 10⁵ s, about a week. That is before recombination and well before today.
- Consistent with the brief's "σ ~ (100 GeV)³, ~10⁵ in σ^{1/3}, ~10¹⁵ in σ". The exact factor depends on the model's quartic and on which field is odd.
- **No single source found states this exact one-Higgs-odd-under-Z2 arithmetic.** The closest primary statements of "EW-scale discrete-symmetry walls are excluded unless explicitly broken" are BPV 2020 (Z2, 2HDM) and Abel–Sarkar–White (Z3, NMSSM).

## 4. Caveats for the R22 use

1. **Formation.** The walls form only if the Z2 was restored after inflation: T_max > m_φ, or H_inf > m_φ (Saikawa `:202-217`). For an EW-scale Z2 this is the standard assumption, since reheating above ~100 GeV is needed for EW baryogenesis/sphalerons. **Flag:** this is not proved by these sources. The "not diluted" claim holds only under that condition, and fn 1 (`:246-248`) lists loopholes.
2. **The ZKO/Saikawa bound applies only to walls that are stable to today.** Every source gives the same escapes: explicit breaking or bias, a biased initial distribution, or breaking before inflation with no restoration. An **exact** Z2 of the action rules out the bias escape by definition. ZKO themselves note the tension ("the symmetry breakdown should not be contained in the Lagrangian"; `zko_jetp_raw.txt:565-566`).
3. **Is the Higgs actually odd?** If the Higgs is odd under a Z2 of the full action, that Z2 must be compatible with the SM Yukawas; BPV avoid the problem by making Φ₂ odd, not Φ₁. If the Higgs doublet is odd under a Z2 that acts on it as −1, the transformation lies in the U(1)_Y (or SU(2)) gauge orbit, and the vacua ±v are then gauge-equivalent. **This is standard lore, not pinned here.** A single-doublet "Higgs → −Higgs" is the hypercharge rotation e^{iπ}, so it gives no disconnected vacua, and BBP 2011 show Π₀ ≠ I needs the second doublet (`:1420-1429`). **Blind-pin owed** before R22 asserts that a one-doublet Higgs-odd Z2 makes walls at all. This is the most important caveat for the R22 argument.
