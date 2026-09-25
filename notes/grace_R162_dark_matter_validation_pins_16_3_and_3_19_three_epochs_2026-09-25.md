# Grace R162: dark-matter validation pins (the seven tests) and 16/3 and 3/19 across three epochs (2026-09-25)

This answers two requests. The first is K1924's addenda: dark matter is gravity-only (T2138, Casey), and every bound is to be pinned from its source. The second is Addendum 2: 16 : 3, f_b = 3/19, with Planck, deuterium and cluster values to pin. Every value was read from a fetched primary; extracts are in `data/sources_grace_2026-09-25/{dm,r3}/`. Instrument: toy 5791, 12/12. Register row A13 is entered in v0.24.

## Two things to settle before any σ is quoted
1. **The neutrino convention.** Planck's Ω_m includes one 0.06 eV neutrino. 16/3 compares cold dark matter with baryons. 3/19 = 3/(3 + 16) is the same statement only if neutrinos are not counted as "matter". Planck's pull on 3/19 is +0.48σ without ω_ν and +0.92σ with it. **Lyra states which one BST's "19" counts.**
2. **T2138 is my own row, and it says more than "gravity-only".** I wrote it on 2026-05-17 (toy 2735).
   - It carries T1971's m_DM = (rank⁴/N_c)·m_p ≈ 5 GeV.
   - It carries two abundance forms: 16/3 and "c_2/rank ≈ 5.5".
   - Casey's picture is a non-dissipating energy clump at atomic scale. That is a different object from a 5 GeV particle, and the two masses call for different instruments.
   - **The clump mass is unstated. Until it is stated, the mass-window tests can't fire (Cal).**

## 1. Abundance: 16/3 and 3/19 (errors uncorrelated; the chains are correlated, so each σ is approximate)

**CMB epoch, Ω_c/Ω_b:**

| data set | Ω_c/Ω_b | pull of 16/3 |
|---|---|---|
| Planck 2018 TT,TE,EE+lowE+lensing (Ω_c h² 0.1200(12), Ω_b h² 0.02237(15); Eqs. 23–24) | 5.364 ± 0.065 | −0.48σ |
| Planck + BAO (0.11933(91), 0.02242(14)) | 5.322 | +0.21σ |
| ACT DR6 P-ACT (arXiv:2503.14452, Table 9) | 5.302 | +0.52σ |
| ACT DR6 P-ACT-L | 5.291 | +0.77σ |
| **ACT DR6 P-ACT-LB (includes DESI BAO)** | 5.226 ± 0.045 | **+2.36σ** |

**Late epoch, clusters (f_b = Ω_b/Ω_m against 3/19 = 0.157895):**

| source | f_b | pull |
|---|---|---|
| Mantz+2022 (MNRAS 510, 131), low-z f_gas, h prior F01 | 0.156 ± 0.034 | +0.06σ |
| same, h prior P18 | 0.173 ± 0.024 | −0.63σ |
| same, h prior R19 | 0.150 ± 0.021 | +0.38σ |
| Wicker+2023 (arXiv:2204.12823), Planck-ESZ, constant bias | 0.140 +0.014/−0.020 | +1.28σ |
| same, varying bias | 0.154 +0.018/−0.026 | — |
| same, varying bias + Planck Ω_m prior | 0.160 | — |
| Gonzalez+2013, stars + ICL + gas, no depletion correction | 0.144 ± 0.005 | +2.78σ (low, as expected without the correction) |

- **Every cluster f_b inherits its depletion factor from simulations run in a Planck cosmology.** Wicker's also inherits the bias prior. These are not fully independent of the CMB.
- Eckert+2019 (X-COP) assumes Planck's f_b, so it is a consistency check, not a measurement. Inverting it (arith) gives ≈ 0.166 ± 0.008.
- No eROSITA f_gas-cosmology result was found.

**BBN epoch:** BBN measures ω_b only. Pitrou 0.02195(22), PDG 2025 SBBN 0.02205(43), Cooke 0.02166(19).
- **To get f_b from BBN you need an external ω_m, so the three epochs are not independent.**
- With Planck's ω_m, the BBN values give f_b of 0.1515–0.1542. That mixes epochs, so it is illustrative only.
- The honest three-epoch test is: CMB Ω_c/Ω_b; cluster f_b, with its depletion caveat; and BBN ω_b together with a non-CMB ω_m. Clusters and BAO + H₀ are candidates for that ω_m.

## 2. No dark disk ("does not dissipate")
- Widmark+2021 (Gaia EDR3 phase-space spiral, arXiv:2105.14030), 95 %: Σ_DD < 4.56 M_⊙ pc⁻² at h = 50 pc; < 4.13 at 20 pc; < 5.59 at 100 pc. The fit is −0.24 ± 2.40.
- Schutz+2018 (PRL 121, 081101) and Buch+2019 (JCAP): at most about 1 % of Milky Way dark matter can be dissipative, for thin disks. Those numbers are from the abstract and introduction text; the per-scale-height curves are in figures and are not pinned.

## 3. Collisionless
All are σ/m bounds in cm² g⁻¹:
- Markevitch+2004: < 1 (order-of-magnitude estimate).
- Randall+2008: < 1.25 (68 %).
- **Harvey+2015** (Science 347, 1462; 72 mergers): < 0.47 (95 %), fit −0.25 +0.42/−0.43.
- **Andrade+2021** (arXiv:2012.06611; first author checked against the arXiv metadata): < 0.13 (95 %).
- arXiv:2605.00093 (11 radio-relic mergers): < 0.22 (68 %) and < 0.63 (95 %).

## 4. Equivalence principle for dark matter
- Kesden & Kamionkowski 2006 (Sagittarius stream): a difference of more than about 10 % between dark-matter and baryon accelerations is "challenged". This is a simulation argument with no CL.
- Collett+2018 (lensing against dynamics): γ_PPN = 0.97 ± 0.09.
- Desmond+2018 (fifth force on gas + dark matter): ΔG/G < few × 10⁻⁴ at 50 Mpc (1σ).

## 5. Cold enough (Lyman-α; all are thermal-relic-equivalent masses)
- Iršič+2024 (PRD 109, 043511): m_WDM > 5.7 keV (95 %). With k_max < 0.1 s/km this drops to 4.1 keV.
- Iršič+2017: > 5.3 keV (2σ), or 3.5 keV with a jumpy IGM temperature.
- Villasenor+2023: > 3.1 keV (95 %).
- Iršič+2024's free-streaming form is α = 70 ckpc (m/1 keV)^−1.11.

## 6. The mass windows (every lensing bound assumes a point lens)
- **Gravitational direct detection** (Carney, Ghosh, Krnjaic, Taylor, PRD 102, 072003): needs m_χ ≳ m_Pl ~ 10¹⁹ GeV, with 10⁸–10⁹ sensors. It is a long-term target, not a limit.
  - **Windchime** (arXiv:2203.07242) targets the *reduced* Planck mass, "≈ 4 μg".
  - K1924's "~10⁻⁵ g" is the unreduced Planck mass. Say which mass is meant.
- **The asteroid window:** "10¹⁷ g < M < 10²³ g … most plausible" (Carr, Kohri, Sendouda, Yokoyama 2021, conclusion). Carr & Kühnel 2020 give 10¹⁶–10¹⁷, 10²⁰–10²⁴ (abstract) and 10²⁰–10²⁶ g (introduction).
  - **K1924's 10¹⁷–10²² g does not appear in either review.**
- **HSC M31** (Niikura+2019): the tightest bounds cover 10⁻¹¹–10⁻⁶ M_⊙. They weaken below about 10⁻⁷ M_⊙ because of the source star's finite size, and wave optics matters below about 10⁻¹¹ M_⊙. Smyth et al. (cited by Carr+) find the limits weaker by up to about 10³.
- **EROS-2:** f < 8 % at 0.4 M_⊙; masses from 0.6 × 10⁻⁷ to 15 M_⊙ are "ruled out as the primary occupants".
- **OGLE** (Mróz+2024): f < 1 % for 1.8 × 10⁻⁴–6.3 M_⊙, and f < 10 % for 1.3 × 10⁻⁵–860 M_⊙.
- **None of these sources treats extended lenses.** "An atomic-size clump acts as a point for lensing" holds for them, but the claim is ours, not the papers'.

## 7. Meson decays at exactly the Standard Model
These pins are from R160:
- Belle II B⁺→K⁺νν̄ is 2.7σ above the SM.
- The reinterpretation favours a 2.1 GeV invisible peak at 3.0σ (PRD 114, 032003).
- NA62 K⁺→π⁺νν̄ is consistent with the SM.

Under T2138, **a confirmed Belle II excess counts against the row.**

— Grace, 2026-09-25
