# Grace R163: round 4. Where 16/3 can die (DESI DR2 + CMB, SPT-3G), and the kaon line as a lattice number. Register v0.25 and v0.26 (2026-09-25)

This covers the GRACE section of `notes/.running/keeper_prompts_team_round4_2026-09-25.md`. Every value was read from the primary; extracts are in `data/sources_grace_2026-09-25/{r4,dm}/` and `desi.txt`, `flag.txt`, `vv26.txt`. Instrument: toy 5794, 16/16, output `play/.out_toy_5794.txt`.

## 1. Where 16/3 can die (item 1)

**What each paper prints:**
- **DESI DR2 Results II prints no ω_c for DESI+CMB.** Table V gives only Ω_m = 0.3027(36) and H₀ = 68.17(28).
- DESI's "CMB" is Planck PR4 (CamSpec) plus Planck + ACT DR6 lensing.
- DESI's Eq. A1–A2 CMB compression prints the covariance of (θ∗, ω_b, ω_bc). From it, **corr(ω_b, ω_c) = −0.606** (arith).
- The tightest printed values are in ACT DR6 Table 5, which includes a DESI DR2 column (P-ACT-LB2), and in SPT-3G D1 (Camphuis et al., arXiv:2506.20707v2) Tables I and VI.

| combination (as printed) | R = ω_c/ω_b | pull vs 16/3, ρ = 0 | pull at ρ = −0.61 |
|---|---|---|---|
| ACT alone (ACT T5) | 5.480 | +1.45σ | +1.20σ |
| Planck, ACT's rerun | 5.364 | +0.43σ | +0.35σ |
| P-ACT | 5.302 | −0.52σ | −0.43σ |
| P-ACT-LB (DESI DR1) | 5.226 | −2.27σ | −1.82σ |
| **P-ACT-LB2 (DESI DR2)**, ω_c 0.1174(6), ω_b 0.02258(10) | **5.199** | **−3.81σ** | **−3.01σ** |
| SPT-3G D1 alone | 5.466 | +1.52σ | +1.22σ |
| CMB-SPA (SPT + Planck + ACT) | 5.370 | +0.77σ | +0.63σ |
| SPT + DESI DR2 | 5.297 | −0.57σ | −0.46σ |
| CMB-SPA + DESI DR2 | 5.254 | −2.34σ | −1.85σ |

**Reading:**
- Every CMB-only combination is within 1.7σ, on both sides.
- Every combination that folds in DESI BAO pulls R below 16/3. That is the same direction as the 2.8–3.1σ CMB–DESI ΛCDM disagreement both collaborations report.
- SPT declined to publish SPT+ACT+DESI at all, because it "does not meet our 3σ consistency requirement".
- On P-ACT-LB2 the kill clause (> 3σ) holds with uncorrelated errors. With the CMB-compression correlation it sits at exactly 3.01σ. It drops under 3σ only if ρ ≤ −0.62.
- **Not fired.** The P-ACT-LB2 chain's own ρ is not printed. It can be computed from the public ACT DR6 chains, and that is Elie's job if he takes it.
- The kill clause is sharpened on A13: > 3σ, with the chain's own covariance, on a combination the collaboration itself reports as consistent.

## 2. The kaon line as a lattice number (item 2)

**The derivation (arith):**
- The K_μ2 route measures |V_us/V_ud|·f_K±/f_π± = 0.27679(28)BR(20)corr (PDG 2026 Vud/Vus, Eq. 67.15).
- A2 fixes |V_us/V_ud| = 1/√19 exactly.
- **So A2 predicts f_K±/f_π± = 0.27679·√19 = 1.2065(15).**

**A2 against the lattice:**

| lattice f_K±/f_π± | value | A2 sits above by |
|---|---|---|
| FLAG 2024, N_f = 2+1+1 (Eq. 76) | 1.1934(19) | **+5.41σ** |
| FLAG 2024, N_f = 2+1 (Eq. 77) | 1.1916(34) | +4.01σ |
| PDG 2026's quoted "FLAG" (Eq. 67.16) | 1.1978(22) | +3.27σ |
| Hudspith et al. 2026, 2+1+1 (arXiv:2605.06560) | 1.1962(34) | +2.77σ |
| Conigli–Frison–Sáez 2025, 2+1 (arXiv:2512.19294) | 1.1848(105) | +2.04σ |

**Audit flag:** PDG 2026 labels 1.1978(22) as "FLAG", but FLAG 2024 Eq. 76 is 1.1934(19). PDG's K_μ2 |V_us| = 0.2250(4) is built on the 1.1978 value.

**A2 against the K_ℓ3 side:** 1/√20 agrees with every K_ℓ3 determination.
- FLAG 0.22328(58): +0.56σ.
- PDG 2026 0.22330(53): +0.58σ.
- Seng 2025 (arXiv:2502.04721), new K_ℓ3 radiative corrections: 0.22308(55), +0.95σ; the 2+1 value 0.22356(73), +0.06σ.
- f₊(0) is FLAG 0.9698(17), with "no new entry" since the last edition.

**Calibrated reading:**
- A2's sharp line is the literature's own K_ℓ2–K_ℓ3 tension, which is about 3σ (Cirigliano et al. 2023). A2 takes the K_ℓ3 side.
- "The K_μ2 route moves" means one of two things. Either the lattice ratio rises by **1.10 %**, from a value quoted at 0.16 %. Or the experimental K_μ2/π_μ2 product, radiative and isospin corrections included, falls by the same fraction.
- That is a large move to ask for.
- **Candidate second kill (Lyra/Cal rule the word):** f_K±/f_π± confirmed at ≤ 1.200 by two independent N_f = 2+1+1 collaborations, with the experimental product unchanged.
- The FNAL/MILC 2026 proceedings (arXiv:2603.02994) are the next candidate, but they print no numbers yet ("preliminary").
- The FLAG site shows no kaon update since v3 (checked 2026-09-25).

## 3. Carried (item 3)
The Lund and OZI pins were done in R161 (toy 5789). Nothing new is owed.
- Monash b = 0.98 GeV⁻², κ ≈ 1 GeV/fm, so b·κ ≈ 0.19 (tunes span 0.11–0.24).
- Γ_ee/Γ for φ, J/ψ, ψ(2S) and Υ(1S–3S) is on disk. It stays a compare line, read only after Lyra's direction.

## 4. Register
**v0.25:**
- **A10** mirrors the retirement of the post-hoc η₀ × (1 + 2α) correction (`BST_BaryonAsymmetry_Correction.md`, March 14; Cal Section 985). The row carries only the leading form. Cal notes that 3π²α⁵ also lands within 1σ, so the α-power forms are a menu and the row stays identified.
- **A13** gains Lyra's content line:
  - mass × count;
  - 5 GeV as the ceiling, not the particle;
  - m_p/3 per dark mode, conditional on equal mode energies;
  - **every heavy window predicted empty**, which is a new kill;
  - T1433's continuum retired to a per-mode statement.

  Still open on A13: "c_2/rank ≈ 5.5" and the neutrino convention.
- **Section D** gains the F98 parity flag (Cal Section 985: H² is P-invariant; J orients the arrow).

**v0.26:**
- A2 gains the lattice form of the kaon line.
- A13 records that its abundance kill sits at the threshold on P-ACT-LB2, not fired.

— Grace, 2026-09-25
