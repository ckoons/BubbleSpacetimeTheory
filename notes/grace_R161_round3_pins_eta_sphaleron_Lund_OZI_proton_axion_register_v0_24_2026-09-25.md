# Grace R161: round-3 pins (η, sphaleron, Barabash 2007, Lund, OZI, proton/dinucleon/trinucleon, axion) and register v0.24 (2026-09-25)

This covers the GRACE section of `notes/.running/keeper_prompts_team_round3_2026-09-25.md`. The rule for this round was no number from memory and no number from a search summary. Every value below was read from a fetched primary, and the extracts are retained in `data/sources_grace_2026-09-25/r3/`. Where only a secondary source was available, it says so.

Instrument: toy 5789, 11/11, output `play/.out_toy_5789.txt`. It covers η, Lund b·κ and Γ_ee/Γ, and it grep-checks each source string.

## 1. Sphaleron and η (item 1)

### The sphaleron statement
The three original papers are paywalled; only their DOIs are pinned (Crossref):
- 't Hooft, PRL 37, 8 (1976), doi:10.1103/PhysRevLett.37.8
- Klinkhamer & Manton, PRD 30, 2212 (1984), doi:10.1103/PhysRevD.30.2212
- Kuzmin, Rubakov & Shaposhnikov, PLB 155, 36 (1985), doi:10.1016/0370-2693(85)91028-7

The physics is pinned from the full text of Rubakov & Shaposhnikov, Phys. Usp. 39, 461 (1996), hep-ph/9603208:
- **Eq. 2.5:** "ΔN_e = ΔN_μ = ΔN_τ = N[A], ΔB = (1/3)·3·3·N[A]", "the factor 3·3 is due to colour and number of generations". So (B − L) is conserved and (B + L) is violated.
- **Eq. 2.8:** σ_inst ∝ exp(−4π/α_W) ~ 10⁻¹⁷⁰.
- **Eq. 2.11:** E_sph = (2m_W/α_W)·B, with B between 1.56 and 2.72, "of order 10 TeV".

### η against every pinned baryon density
BST's value is **η₁₀ = 2α⁴/(3π) × 10¹⁰ = 6.0176**, using α⁻¹ = 137.035999177 (CODATA 2022). The conversion is η₁₀ = 273.754 Ω_b h² (Fields–Olive–Yeh–Young, JCAP 03 (2020) 010, Eq. A24). Cooke's 273.78 changes each pull by ≤ 0.02.

| determination | Ω_b h² | η₁₀ | pull |
|---|---|---|---|
| Planck 2018, TT,TE,EE+lowE+lensing (Eq. 24) | 0.02237(15) | 6.124(41) | **−2.59σ** |
| Planck 2018, +BAO (Table 2) | 0.02242(14) | 6.138(38) | **−3.13σ** |
| Pitrou et al. 2021, BBN (MNRAS 502, 2474, Eq. 9) | 0.02195(22) | 6.009(60) | **+0.14σ** |
| PDG 2025, SBBN (Eq. 24.6; Yeh et al. 2022) | 0.02205(43) | 6.036(118) | −0.16σ |
| Cooke–Pettini–Steidel 2018, D/H (ApJ 855, 102, Eq. 12) | 0.02166(19) | 5.930(51) | +1.73σ |

**Reading:** η sits on the deuterium side of the known CMB–BBN baryon gap. Pitrou calls that gap 1.6σ (CMB) and 1.84σ (CMB+BAO). K1924's "−2.6σ from Planck" is correct, but it is half the picture, and quoting only the BBN half would be the other half. **The register row carries the pair.**

## 2. Barabash, Dolgov, Dvorničký, Šimkovic, Smirnov 2007 (item 2, which Elie was blocked on)
This paper has five authors, not four. NPB 783, 90 (2007), doi:10.1016/j.nuclphysb.2007.05.033, arXiv:0704.2944.

**The formalism:**
- The neutrino state is |ν⟩ = c_δ|f⟩ + s_δ|b⟩ (Eqs. 2–3).
- The amplitude is A = cos²χ A_f + sin²χ A_b (Eq. 7).
- **The rate is W_tot = cos⁴χ W_f + sin⁴χ W_b**. The f–b interference vanishes after phase-space integration (Eqs. 8, 15).
- The spectrum is P = [cos⁴χ dω_f + sin⁴χ r₀ dω_b]/[cos⁴χ + sin⁴χ r₀] (Eqs. 14, 16).

**Phase-space weights:**
- 0⁺ transition: f^b = [3(E_ν2 − E_ν1)² + (E_e2 − E_e1)²]/(48 m_e²), against f^f = 1 (HSD, Eqs. 31–32; the SSD form is Eqs. 38–39).
- 2⁺ transition: f^f = (E_e1−E_e2)²(E_ν1−E_ν2)²/(2m_e⁶) and f^b = (E_e1−E_e2)²/(4m_e²).

**Numbers for ¹⁰⁰Mo (SSD):**
- r₀(0⁺g.s.) = 0.076, so T^b/T^f ≈ 13 (Eqs. 40–41).
- r₀(2⁺₁) = 7.1 (Eqs. 42–43).
- For ⁷⁶Ge, r₀ ≈ 10⁻³, so "purely bosonic neutrino is certainly excluded".

**Angular correlation:** dW/dcosθ = (W/2)(1 + κ cosθ), with **κ_f = −0.627, κ_b = −0.344** (Eqs. 45–46). This is the angular-correlation coefficient that NEMO-3 never published. Here it is a *prediction per statistics*, not a measurement.

**How the shapes shift:**
- The energy-sum spectrum shifts to lower energies with sin²χ.
- The single-electron spectrum has a fixed point at 0.3 MeV.

**Bounds:**
- The main bound is **sin²χ < 0.6, "conservative", with no confidence level**. It was read by eye from the shift of the sum-spectrum maximum ("will not perform detailed statistical analysis").
- Rate bounds: < 0.50 (⁷⁶Ge), < 0.34 (¹⁰⁰Mo), < 0.06 (¹¹⁶Cd, "requires further checks").
- The best fit is "sin²χ ~ 0.4–0.5".
- Internal inconsistencies: r₀ is 0.086 in Eq. 54 against 0.076 in Eq. 41, and the Conclusions give both 0.5 and 0.6.
- NEMO-3 2019's sin²χ < 0.27 (90 %, R160) supersedes it.

## 3. Lund (item 3)
**Monash 2013** (Skands, Carrazza, Rojo, EPJC 74, 3024, arXiv:1404.5630, Table 4), Monash value with the prior default in brackets:
- StringZ:aLund = 0.68 (0.3)
- StringZ:bLund = **0.98 GeV⁻²** (0.8)
- StringPT:sigma = 0.335 GeV (0.304)

Monash quotes no κ. Its Section 2 implies κ = π(0.25 GeV)² = 0.196 GeV² (arith).

**Pythia 8.3 manual** (arXiv:2203.11601, Section 7.1):
- κ: "κ ≈ 1 GeV/fm".
- Eq. 311: dP ∝ … exp(−bA), "A is the area covered by the string before breakup in units of κ". Fig. 14(b) is labelled A/κ², so A is in GeV².
- Eq. 312: f(z) ∝ (1−z)^a/z · exp(−b m⊥²/z).
- "the string tension κ does not enter explicitly into the PYTHIA implementation".

**The Professor LEP tune** (arXiv:0907.2973, Table 3) has b = 0.6 (Q²) or 1.2 (p⊥), against a P6.418 default of 0.58.

**b·κ (arith)**, with κ = 1 GeV/fm × ħc = 0.19733 GeV²:

| tune | b·κ |
|---|---|
| Monash | **0.193** |
| Pythia 8 pre-Monash | 0.158 |
| Professor Q² | 0.118 |
| Professor p⊥ | 0.237 |
| P6.418 default | 0.114 |

**The target's honest width is the tune spread, 0.11–0.24**, a factor of two. A BST value inside it is not evidence, and one outside it is a miss only if it misses by more than that factor.

## 4. OZI: leptonic and total widths (item 4; compare line only, after Lyra's direction)

PDG 2026 (IJMPA 41, 2630011). Γ is from the Summary Tables; Γ_ee is from the Listings (OUR EVALUATION / AVERAGE / FIT).

| state | Γ | Γ_ee | Γ_ee/Γ (arith) |
|---|---|---|---|
| φ(1020) | 4.249(13) MeV | 1.27(4) keV | 2.99 × 10⁻⁴ |
| J/ψ(1S) | 92.6(1.7) keV | 5.53(10) keV | 5.97 × 10⁻² |
| ψ(2S) | 293(9) keV | 2.33(4) keV | 7.95 × 10⁻³ |
| Υ(1S) | 54.02(1.25) keV | 1.340(18) keV | 2.48 × 10⁻² |
| Υ(2S) | 31.98(2.63) keV | 0.612(11) keV | 1.91 × 10⁻² |
| Υ(3S) | 20.32(1.85) keV | 0.443(8) keV | 2.18 × 10⁻² |

Υ(1S): the listed B(e⁺e⁻) is 2.39(8) %, about 1σ under Γ_ee/Γ. That is PDG's own inconsistency, not a misreading.

## 5. Wu–Shaknov 1950 (item 6): primary text still UNVERIFIED
- DOI 10.1103/PhysRev.77.136 is confirmed.
- APS returned 403. ADS, the Internet Archive and Semantic Scholar all have no full text.
- Five fetched secondaries agree on **2.04 ± 0.08**, measured against a geometry-corrected theory value of 2.00 (the ideal maximum is 2.85). One of them (arXiv:2504.16978) prints "2.4", evidently a typo.
- No source gives 2.00 ± 0.10.
- Someone with APS access should pull the one-page letter.

## 6. Proton, dinucleon, trinucleon and axion bounds (for the new rows)

**Proton decay (ΔB = 1), Super-K:**
- p → e⁺π⁰: τ/B > 2.4 × 10³⁴ yr (90 %, PRD 102, 112011 (2020)).
- p → ν̄K⁺: > 5.9 × 10³³ yr (PRD 90, 072005 (2014)). Whether a newer result exists is unchecked.

**Dinucleon decay (ΔB = 2), Super-K:**
- ¹⁶O(pp) → π⁺π⁺: > 7.22 × 10³¹ yr (arXiv:1504.01041; the journal ref is unverified).
- ¹⁶O(nn) → π⁰π⁰: > 4.04 × 10³² yr.
- n–n̄ in ¹⁶O: > 3.6 × 10³² yr, with a free-equivalent τ > 4.7 × 10⁸ s (PRD 103, 012008 (2021), arXiv:2012.02607).
- Free n–n̄ (ILL 1994): > 0.86 × 10⁸ s, secondary only (cited in the Super-K paper).

**Trinucleon decay (ΔB = 3):**
- Super-K ¹⁶O(ppp) → ¹³C π⁺π⁺e⁺: > 4.2 × 10³² yr (arXiv:2609.25681, submitted **2026-09-22**, a preprint).
- Majorana ⁷⁶Ge(ppp)/(ppn): > 1.83 × 10²⁶ yr (arXiv:2412.16047, doi:10.1103/2pgp-hvst; supersedes PRD 99, 072004 (2019)).
- EXO-200 ¹³⁶Xe, inclusive: ppp > 3.3 × 10²³ yr, npp > 1.9 × 10²³ yr (PRD 97, 072007 (2018)).

**nEDM and θ̄:**
- Abel et al., PRL 124, 081803 (2020): d_n = (0.0 ± 1.1 ± 0.2) × 10⁻²⁶ e·cm, |d_n| < 1.8 × 10⁻²⁶ e·cm (90 %).
- PDG 2026 review 89: "|Θ̄| ≲ 10⁻¹⁰".
- n2EDM status is UNVERIFIED (search snippets only).

**Axion searches:**
- ADMX: DFSZ excluded at 3.27–3.34 μeV (PRL 134, 111002 (2025)). KSVZ is excluded at 4.54–5.41 μeV, and DFSZ was "not reached" there (PRL 135, 191001 (2025)).
- CAST: |g_aγγ| < 5.8 × 10⁻¹¹ GeV⁻¹ (95 %, PDG 2026 Eq. 89.20).
- PDG 2026 has no QCD-axion detection claim. It also has no explicit "none" sentence.

## 7. Register v0.24 (applied)
- **A2:**
  - (vi) The sharp line is the kaons. 1/√20 sits at −0.58σ on K_ℓ3 and +3.48σ on K_μ2, so the row predicts the K_μ2 route moves. **Kill: K_ℓ3 settling near 0.2250.**
  - (vii) The neutron split is demoted to consistency (Cal Section 984), and 0.87σ is withdrawn as K-dependent.
- **E7:** g_A = 4/π is FIRED (Cal Section 984, accepted in the K1923 Amendment). Keeper certification of the row is owed.
- **A5:** carries Casey's two residue branches, recorded and not adopted:
  - (a) same-sign residues ⇒ no 0νββ. This branch **contradicts the Majorana bank the row stands on.**
  - (b) complementary residues ⇒ 0νββ. This branch is consistent with the bank.
- **A10 (NEW), η = 2α⁴/(3π):** IDENTIFIED, carrying the two-sided pulls. The candidate kill (Lyra/Cal to rule the word) is the CMB–BBN gap closing on the CMB side at ≥ 3σ from 6.018.
- **A11 (NEW), no QCD axion (F786):**
  - The kill is a QCD axion on the QCD line. An ALP off that line does not fire it.
  - The nEDM floor clause names the SM CKM floor (~10⁻³² e·cm), which is **not pinned today**.
- **A12 (NEW), ΔB ≡ 0 (mod 3):**
  - Kill: any ΔB = 1 or ΔB = 2 process.
  - The rule's ΔB = 3 pattern is a shape, not a rate.
  - **Seam flagged:** K1699(b) called the asymmetry an initial condition, while K1924/A10 read it as dynamical over-winding. Lyra reconciles.
  - **Also flagged:** K1924 cites "K1700 (baryon number = winding number mod 3)", but K1700b corrected K1700's mechanism. The row cites K1700b.
- **Dark matter (T2138, gravity-only, settled by Casey):** the row waits on the validation pins, which are in progress, and on one seam.
  - **T2138 is mine** (Grace, 2026-05-17, toy 2735), and as written it carries more than "gravity-only".
  - It also carries T1971's m_DM = (rank⁴/N_c)·m_p ≈ 5 GeV, and two abundance forms: rank⁴/N_c = 16/3 (T1966) and "c_2/rank ≈ 5.5".
  - Casey's picture (energy clumped at atomic scale) and a 5 GeV particle are different masses, and a different mass means a different instrument.
  - Lyra states which content stands before the row is written.

— Grace, 2026-09-25
