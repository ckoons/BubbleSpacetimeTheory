# Grace R159: A2 CKM first-row pins, the C1 δ_CP table, Lane 1 early-dark-energy bound forms, and the K1922 register row (2026-09-25)

This covers the GRACE block of Keeper's team wake prompt (`notes/.running/keeper_prompts_team_wake_2026-09-25.md`). No BST number was adjusted, and no register row's word has changed. Keeper gates the A2 table before any row word moves. No w-direction is printed anywhere in this note.

**Instrument:** `play/toy_5780_grace_A2_CKM_first_row_and_C1_delta_CP_pins_2026-09-25.py`, SCORE 12/12, output `play/.out_toy_5780.txt`. Every printed value it uses is grep-checked against pdftotext extracts of the fetched primaries. Those extracts are retained in `data/sources_grace_2026-09-25/`, which also holds NuFIT 6.1's own 1D δ_CP χ² projections and its parameter table PDF. Primaries were fetched today, and nothing below is from memory. Where I did arithmetic on the sources' own numbers, it is marked (arith).

## 1. A2: CKM first row (the row's λ = 1/√20, |V_ud| = √(19/20))

### Where the row's inputs came from
The register cell has λ = 0.22501 ± 0.00068 (−2.06σ) and a direct sum of 0.9984 ± 0.0007 (2.3σ). Both come from the PDG CKM review, Revised April 2024 (Ceccucci, Ligeti, Sakai), in Navas et al., PRD 110, 030001 (2024), doi:10.1103/PhysRevD.110.030001. The PDG 2025 update repeats that text unchanged.

### Newer edition
PDG 2026 (Int. J. Mod. Phys. A 41, 2630011, dated 1 June 2026) has a CKM review Revised March 2026 and a V_ud/V_us review (Blucher, D'Ambrosio, Marciano) Revised August 2025.

### Inputs as printed

| quantity | value | source (locator) |
|---|---|---|
| \|V_ud\| superallowed | 0.97367(11)exp(13)ΔR(27)NS(32)total | PDG 2026 Vud/Vus Eq. 67.4. Still built on Hardy & Towner, PRC 102, 045501 (2020). No newer survey exists. |
| \|V_ud\| superallowed, lattice γW box | 0.97386(11)(9)(27) | Ma, Feng, Gorchtein, Seng et al., PRL 132, 191901 (2024), arXiv:2308.16755. Abstract: "reducing the previous 2.1σ tension … to 1.8σ". |
| \|V_ud\| superallowed, new δ_C shell model | 0.97359(33) | Xayavong, Smirnova, Nowacki, arXiv:2508.18189 (2025-08-25), PRC doi:10.1103/pwl4-7y27 |
| Ft long-distance O(Zα²) shift | 3072.1 → 3073.0 ± 0.6 s | Cao, Hill, Plestid, Vander Griend, arXiv:2511.05446 (2025-11-07). "exacerbates the first-row CKM unitarity deficit". The paper quotes no \|V_ud\|. |
| \|V_ud\| neutron, best values | 0.97413(20)τn(35)λ(13)ΔR(42)TOT | PDG 2026 Eq. 67.8. Inputs: τ_n from UCNτ 877.82 ± 0.22 s (arXiv:2409.05560, PRC 111, 045501 (2025)) and λ from PERKEO III −1.27641(45)(33) (PRL 122, 242501). |
| \|V_ud\| neutron, averages | 0.97441(28)(82)(13)(88) | PDG 2026 Eq. 67.7 |
| f₊(0), N_f = 2+1+1 | 0.9698(17) | FLAG 2024, arXiv:2411.04268v3, PRD 113, 014508 (2026). Unchanged from FLAG 2021. |
| f_K±/f_π± | 1.1934(19) | FLAG 2024 Eq. 76 |
| \|V_us\| from K_ℓ3 / from K_μ2 / average | 0.22330(53) / 0.2250(4) / 0.22431(85) with S = 2.5 | PDG 2026 |
| Row sum | 0.9984(7), "a 2.3 σ tension" | PDG 2026 CKM review (same as 2024) |
| Row sum | 0.9983(7): "2 sigma … increases to 3 sigma if nuclear structure uncertainties are ignored" | PDG 2026 Vud/Vus Eq. 67.21 |
| Row sums | 0.99802(66) ≈ 3.0σ (K_ℓ3 route); 0.99888(67), 1.7σ (K_μ2 route) | FLAG 2024 Section 5.4 |
| λ, global fit | 0.22501(68) in 2024 → **0.22517(68)** in 2026 | PDG CKM review Eq. 12.26. UTfit went 0.22497(70) → 0.22519(68); tree-level-only went 0.22509(68) → 0.22528(69). |

### λ against 1/√20 = 0.2236068 (toy 5780)

| λ input | 2024 | 2026 |
|---|---|---|
| CKMfitter | +2.06σ | **+2.30σ** |
| UTfit | +1.95σ | +2.33σ |
| tree-level | +2.18σ | +2.42σ |

The direct kaon inputs have not moved:
- |V_us| average: +0.83σ
- K_ℓ3: −0.58σ
- K_μ2: +3.48σ

### |V_ud| = √(19/20) = 0.974679 against the |V_ud| pins (arith)
The row prints this value but carries no σ for it.

| |V_ud| pin | tension |
|---|---|
| superallowed, Hardy–Towner | +3.15σ |
| superallowed, lattice box | +2.64σ |
| superallowed, Xayavong | +3.30σ |
| neutron, best values | +1.31σ |
| neutron, averages | +0.31σ |

### Growing or fading
1. **The global-fit λ tension GREW: 2.06σ → 2.30σ.** The σ is unchanged and the central value moved up by 0.00016. The same happens on all three fits (UTfit 1.95 → 2.33σ).
2. **The first-row deficit is FLAT in PDG's headline: 2.3σ in 2024 and 2026, same inputs.** The 2024–2025 corrections pull in both directions:
   - the lattice box raises |V_ud|, giving 1.77σ (arith);
   - the δ_C shell model lowers it, giving 2.40σ (arith);
   - the Zα² Ft shift lowers it (the authors' word: "exacerbates").
   Which kaon route you take spans 1.7σ to 3.0σ (FLAG).

### Flag for Keeper (a question, not an edit)
The A2 cell reads "direct first-row sum … 2.3σ short of unitary — currently in BST's favor". The row fixes the first row as exactly unitary, so a deficit is a tension with the row, not support for it. The phrase needs its reason on the face of the cell, or it should go.

The one reading under which it holds is this: the direct |V_us| (0.83σ from 1/√20) sits closer to 1/√20 than the unitarity-imposed fit λ does (2.30σ). But that reading moves the tension onto |V_ud|, and the superallowed |V_ud| is 3.15σ from √(19/20).

So the row has two faces: λ at 2.3σ on the fit, and |V_ud| at 3.15σ on the superallowed value. Its kill clause ("the Wolfenstein tension growing well past 3σ") is written only on the first face. **The second face is already past 3σ on the superallowed |V_ud|, and at 1.3σ on the neutron.** I am laying this out. Whether √(19/20) against superallowed is a can-fail line the row owns is a Keeper/Lyra ruling.

## 2. C1: δ_CP, the three corpus claims (309° / 77° / ~197°) laid out, not picked

For the |sin δ| = 2/7 claim, 197° is the root the corpus names (196.6°). Its partner root in the same half, 163°, is shown beside it.

**Conventions:**
- σ = √Δχ² with 1 dof.
- NuFIT Δχ² values are read from NuFIT's own 1D projections, relative to the GLOBAL minimum, which is in NO. The IO file minima are 1.49 (IC23) and 5.91 (IC24), and they match the table headers "Inverted Ordering (Δχ² = 1.5 / 5.9)".
- T2K+NOvA and NOvA intervals are Bayesian HPD credible intervals, so each value is only in or out.

| source | ord. | best fit | 309° | 77° | 197° | 163° |
|---|---|---|---|---|---|---|
| NuFIT 6.1, IC23 without SK-atm | NO | 207° | 3.51 (1.87σ) | 11.28 (3.36σ) | 0.28 (0.53σ) | 1.80 (1.34σ) |
| same | IO | 283° | 2.64 (1.62σ) | 48.3 (6.95σ) | 11.9 (3.44σ) | 24.7 (4.97σ) |
| NuFIT 6.1, IC24 with SK-atm | NO | 212° | 3.36 (1.83σ) | 15.44 (3.93σ) | 0.52 (0.72σ) | 2.03 (1.42σ) |
| same | IO | 274° | 8.53 (2.92σ) | 59.1 (7.69σ) | 16.6 (4.07σ) | 30.6 (5.53σ) |
| T2K+NOvA joint (with reactor θ13) | NO | −0.87π = 203° | in 3σ, out of 1σ | **out of 3σ** | in 1σ | in 3σ, just out of 1σ |
| same | IO | −0.47π = 275° | in 3σ, just out of 1σ | out of 3σ | in 3σ (edge 194.4°) | **out of 3σ** |
| NOvA 10-yr (1D, conditional) | NO | 0.93π = 167° | out of 1σ | out of 1σ | in 1σ | in 1σ |
| same | IO | 1.50π = 270° | just out of 1σ | out of 1σ | out of 1σ | out of 1σ |
| Capozzi et al. 2025 (Bari) | NO | 1.20π = 216° | in 2σ | **out of 3σ** | in 1σ | in 2σ |
| same | IO | 1.48π = 266° | in 2σ (edge 309.6°) | out of 3σ | **out of 3σ** (edge 202°) | out of 3σ |

**Which ordering each fit prefers:**
- NuFIT 6.1: NO, with IO at Δχ² 1.5 / 5.9.
- Capozzi: NO at 2.2σ.
- NOvA alone: NO (IO disfavoured at 1.4σ).
- T2K+NOvA joint: no significant preference, with a Bayes factor of 1.3 (2.5) for IO with (without) the reactor constraint.

So each claim's standing is ordering-conditional. That condition belongs in the C1 cell beside any σ.

**Sources:**
- **NuFIT 6.1** (data November 2025): www.nu-fit.org, with Esteban et al., JHEP 12 (2024) 216, arXiv:2410.05380. The site's table caption still reads "as of September 2024", but the release notes date the release November 2025.
- **T2K+NOvA joint:** Nature 646, 818–824 (2025), doi:10.1038/s41586-025-09599-3, arXiv:2510.19888. Numbers from the main text and Extended Data Table III.
- **NOvA:** arXiv:2509.04361, PRL 136, 011802 (2026). Journal DOI unverified. Numbers from Table S1.
- **Capozzi, Giarè, Lisi, Marrone, Melchiorri, Palazzo:** PRD 111, 093006 (2025), arXiv:2503.07752, Table I.
- **Not found:** no peer-reviewed T2K-alone update after 2023; no Valencia fit after 2021.

**Change from the row:** the row's pin is NuFIT 6.0 (212° +26/−41) with 309° ~3.7σ, 77° ~3.3σ and 197° ~0.4σ. NuFIT 6.1 moves 309° to under 2σ in NO (1.83–1.87σ). The row's 3.7σ does not survive the newer release on the NuFIT 6.1 projection. 77° stays past 3σ in NO, and past 3σ on T2K+NOvA in both orderings. The corpus ruling on which claim is live stays Lyra/Cal's.

## 3. Lane 1: early-dark-energy bounds, in the form each source states them

| bound | form as stated | CL | epoch | source |
|---|---|---|---|---|
| Doran–Robbers Ω_e (constant early fraction) | Ω_e < 0.0036 (TT,TE,EE+lowP+BSH); < 0.0070 (other combination) | 95% | constant fraction until recent times | Planck 2015 XIV, A&A 594, A14 (2016), arXiv:1502.01590. Sect. 5.1.4, Eq. (26), Table 3. Planck 2018 gives no Ω_e (Sect. 7.4 defers to PDE15). |
| EDE switched on at z_e | "bounds on Ωe can be weaker if DE is present only over a limited range of redshifts" | 95% | z_e = 10–1000 | same, Eq. (27), Fig. 11 (bars only) |
| axion-like EDE f_EDE (max fraction, at z_c) | n = 3: f_EDE < 0.088 (ACT), < 0.12 (P-ACT), < 0.10 (P-ACT-LB-BOSS). n = 2: < 0.091 (ACT). Prior log₁₀ z_c ∈ [3.0, 4.3]. | 95% | peak at z_c ~ 10³–10^4.3 | Calabrese, Hill et al., ACT DR6, JCAP 11 (2025) 063, doi:10.1088/1475-7516/2025/11/063, arXiv:2503.14454, Sect. 5.1, Eqs. (11), (16) |
| extra radiation at BBN | N_ν − 3 < 0.168 (BBN+CMB) | 95% | T ~ MeV | Fields, Olive, Yeh, Young, JCAP 03 (2020) 010, doi:10.1088/1475-7516/2020/03/010, Eq. (44). As a fraction of radiation at g* = 10.75: (7/4)(0.168)/10.75 = 0.027 (arith). |
| N_eff at recombination | 2.86 ± 0.13 (ACT DR6); 2.89 ± 0.11 with BBN | 68% | recombination | ACT DR6, abstract |
| w = −1/3 fluid as its own component (not curvature) | Ω_s < 0.0465 (CMB); < 0.00824 (CMB+DESI); "ρ_s ∝ a⁻²" | 95% | today, flat | Cheng, Di Valentino, Visinelli, JHEAP 53, 100610 (2026), arXiv:2505.22066, Table 2 |
| the same scaling as curvature (background-degenerate) | 10³ Ω_K = 2.3 ± 1.1 (DESI+CMB, ΛCDM+Ω_K) | 68% | late | DESI DR2 Results II, PRD 112, 083515 (2025), **doi:10.1103/tr6y-kpc6**. Table V. |

**On DESI DR2 Results II:** the old-style DOI 10.1103/PhysRevD.112.083515 does NOT resolve (404). APS registered the new-style DOI above, which Crossref confirms (published 2025-10-06). This closes R158's "DOI check UNRESOLVED".

**Reach against Lyra's item (iii):** Lyra's FILLING_LAW Section (iii) puts Ω_DE(a_eq) at about 5 × 10⁻¹¹, falling as a² before equality. The closest-shaped pinned bound is ACT's f_EDE < 0.088–0.12 at a peak z_c ~ 10³–10^4.3. It sits about nine orders above that value, and BBN's 0.027 sits further still. So Lyra's "can fail in principle, will not fail in practice" is right on the pinned forms. Her "~10⁻² near z ~ 3000–5000" should cite ACT DR6's f_EDE < 0.088 (95%, prior z_c ∈ 10³–10^4.3), not a rounded 10⁻². No pinned bound is parametrized as "fraction grows as a² through radiation, then freezes". The Doran–Robbers Ω_e assumes a constant fraction, so it is the wrong shape to quote as a test.

**Re-resolved (Crossref today):**
- Hsu, Phys. Lett. B 594, 13–16 (2004), doi:10.1016/j.physletb.2004.05.020. Confirmed.
- Li, Phys. Lett. B 603, 1–5 (2004), doi:10.1016/j.physletb.2004.10.014. Confirmed.
- Luciano, Paliathanasis, Saridakis, J. High Energy Astrophys. 49, 100427, doi:10.1016/j.jheap.2025.100427. Confirmed. Crossref gives the print date as **January 2026**. Cite "(2026)", with arXiv:2506.03019 (2025).

## 4. Register rows

**K1922 row (Approaches Register):** built by Keeper's instrument (`play/keeper_approaches_register.py`, full corpus, cached). It drafted K1922 as:
- outcome: CONDITIONAL
- lane: "filling law exponent D=3"
- evidence (verbatim, verify clean): "The reading works only if each 3D cell is one commitment costing one Landauer bit"

**Mismatch for Keeper:** the model drafted the rubric cell as "Ext-3 Derive SM params". K1922's own header says External 4 / Internal C. I did not hand-edit the derived file. The next build would overwrite a hand edit anyway, so the fix belongs in the instrument (a rubric-cell override or a control).

**Instrument finding for Keeper:** the nightly default model `qwen3:30b-a3b` is not installed on this machine. Local Ollama has gpt-oss:20b/120b, gemma4, qwen3.6:35b, qwen3.8:27b and qwen3-coder-next. So 29 rows since 09-19 had been written with `model_error: HTTP 404`, K1921 among them. I ran with `--model qwen3.6:35b`. Those 29 rows now carry model drafts, and exactly one row is new (K1922). The model field on those rows now reads qwen3.6:35b. Keeper chooses the nightly default.

**Lane 2 row:** held until Lyra's F473 kill-first paragraph lands. F473 goes in its reason column: "the descent keeps the 3 colour/base directions — never shown", CONDITIONAL, 07-05. F474's signature bug (07-05, OPEN) is the neighbour row.

— Grace, 2026-09-25
