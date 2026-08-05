# SM-Derivation Corpus Reconnect Index — item-3 launch map (2026-08-05)

**Purpose (Casey directive, 2026-08-05):** QM-from-D_IV⁵ is complete; **item-3 (the ~26 SM parameters) is the one real frontier left.** The corpus already contains a great deal of SM-derivation material — reconnect to it before grinding fresh. This index maps what BST already derives, its tier, its source, and the honest open frontier. Frame everything as **linear algebra on D_IV⁵** (build the operators, read invariants off the fixed operators, compute).

**Discipline caveat (Elie, verifier seat):** the tiers below are **as-cataloged in the corpus** (data/bst_constants.json + K-audits). This is a *reconnect map, not a re-verification*. Before any external citation, re-verify the load-bearing rows against the live notes/K-audits and grep the retraction log (per the corpus-reconnect standing rule). Known retractions/demotions are flagged in the Caveats section — respect them.

Five integers: **rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137.**

---

## A. DERIVED / IDENTIFIED (the banked SM side)

| Parameter | BST form | Tier | Precision | Source |
|---|---|---|---|---|
| α (fine structure) | α⁻¹ = N_max = 137 | **I** (demoted, see caveats) | 0.0001% | const_002 / T198 |
| θ_QCD (strong CP) | 0 (D_IV⁵ contractible, π₁=0) | **D** | exact | const_005 / T201 |
| m_p/m_e | 6π⁵ = C_2·π^{n_C} | **D** | 0.002% | const_001 / T187 |
| m_μ/m_e | (24/π²)⁶ | **D** | 0.003% | const_010 / T190 |
| m_τ/m_e | (24/π²)⁶·(7/3)^{10/3} | **I** | 0.19% | const_039 / T2043 |
| Higgs VEV v | m_p²/(7 m_e) = 36π¹⁰ m_e/7 | **D** | 0.046% | const_007 / T225 |
| m_H | two routes (√(2/√120)·v ; (π/2)(1−α)m_W) | **D** | 0.07–0.11% | const_008/009 / T230/231 |
| λ_H | √(2/5!) = 1/√60 | **D** | exact | const_008 / T230 |
| m_W | n_C·m_p/(8α) | **D** | 0.02% | const_012 / T281 |
| m_Z | m_W/√(10/13) | **D** | 0.5% | const_013 / T283 |
| sin²θ_W | N_c/(N_c+2n_C) = 3/13 | **S** (demoted, see caveats) | 0.2% | const_011 / T280 |
| sin²θ₁₂ (solar) | (3/10)·(44/45) | **D** | 0.06% | const_022 / T1446 |
| **sin²θ₂₃ (atm)** | **(4/7)·(44/45)** [4/7 = rank²/g] | **D** | 0.40% | const_023 / T1446 |
| sin²θ₁₃ (reactor) | 1/(n_C(2n_C−1)) = 1/45 | **D** | 0.9% | const_024 / T332 |
| sin θ_C (Cabibbo) | 2/√79 [vacuum subtraction] | **D** | 0.004% | const_020 / T1444 |
| J_CKM (Jarlskog) | A²λ⁶η̄, A=9/11, λ=2/√79 | **I** | 0.3% | const_077 |
| N_gen | N_c = 3 (Z₃ orbifold fixed pts) | **D** | exact | const_004 / T200 |
| m_e/m_Pl (hierarchy) | α^{n_C+1} = α⁶ | **D** | 0.017% | const_006 / T397 |
| Ω_DM/Ω_b | 2^{2·rank}/N_c = 16/3 | **D** | 0.58% | const_015 / T194 |

**Quark mass RATIOS (D-tier); absolute values S-tier (anchored to m_e ↔ the tick):**
m_s/m_d = (N_c+1)(N_c+2) = 20 · m_d/m_u = 13/6 · m_c/m_s = 136/10 · m_b/m_τ = 7/3. Absolute m_u = N_c√rank·m_e (0.4%), m_t = (1−α)v/√2 (y_t=1 saturation, 0.8%). **Charm second route** m_c = α·v/√2 (const_158/T2560, 0.05%) — pending Cal cold-read.

**Hadrons (18 constants, 0.002–0.86%):** m_K, m_ρ, m_φ, m_η'=m_p·49/48, m_π, f_π, Γ_W — all π^{n_C}·m_e × integer envelopes.

---

## B. THE ITEM-3 OPEN FRONTIER (not yet forced)

**Highest leverage first (Keeper's pivot order):**
1. **O7 / mixing** — the 3×3 CKM+PMNS structure is N_c=3-forced, but the off-diagonals (V_us, V_cb, V_ub; PMNS δ_CP) are NOT all independently forced. One insight (the generation K-type ladder {1,3,5}, my toy 5046) unlocks ~7 mixing params + the θ₂₃ octant (4/7 upper = DUNE prediction). **Gated on the ℤ₂=Shilov selection-rule verdict (Lyra/Grace).**
2. **Koide** — A² = rank form identified but **NOT banked** (K2040 "composite-overlap"; naive product-reading FALSIFIED, K1158). Real open problem; route = Faraut-Koranyi rank-2 boundary computation.
3. **up-quark m_u** — derived form (N_c√rank·m_e, 0.4%) but the K-type overlap mechanism is structural, not proven forced (F603 O=SO(5) vector is Higgs; u sits at a different K-type — prove the equivalence).

**Harder / QFT-not-BST:** α_s running (β₀=11/3 universal — BST forces the coefficient not the running); PMNS δ_CP (Engine B / Majorana-condensate quadrant, K682 open); neutrino absolute scale (seesaw Λ_R open; BST forces m₁=0 + ratios, Σm_ν≈0.059 eV falsifier).

---

## C. CAVEATS / RETRACTIONS (respect these — do not re-inflate)

- **α → I** (K684): α⁻¹=137 is reverse-fit / value-identified, not forced forward. Upgrade = first-principles gauge quantization (open).
- **sin²θ_W = 3/13 → S** (K739): a running coincidence at m_p scale, ~0.2% from the RGE MS-bar value at M_Z. Not a primary observable.
- **m_τ/m_e → I** (structural 7/3 exponent, not forced).
- **Ω_Λ = 13/19, n_s = 1−5/137 → PD** (Partially Derived): numerators/mode-counts forced; the denominator-19 combination and per-mode tilt magnitude are open.
- **G → "Derived-given-the-tick"** (K1118): the a₁=(1/6)R form is UNIVERSAL (Seeley-DeWitt) — reproducing it is consistency, not distinctive; BST's marble is the coupling coefficient. Never externally "BST derives Einstein-Hilbert"; say "BST forces the gravity coefficient."
- **muon second route** (24=Γ(5) via F323): does NOT close; muon stays D via e=n, gains no second derivation. Parked.
- **Absolute masses are Derived-given-anchor** (m_e ↔ Planck tick t_B, ANCHOR #9): BST forces the dimensionless structure with zero dimensionless free params; one dimensionful anchor stated GR-plainly.

---

## D. READING LIST (get up to speed on SM derivations)

1. `data/bst_constants.json` — the full SM library (144+ constants, eval-ready formulas + tiers). Read `meta` first.
2. `notes/BST_26_Scoreboard_current_tiers_2026-07-18.md` — the 26-parameter tier reconciliation (Grace).
3. `notes/BACKLOG.md` SP-14 (the honest gap registry).
4. `notes/BST_ElectronMass_CanonicalProof.md` (K992) — why 6π⁵ is Derived (C_2=Casimir, π-measure not count).
5. `notes/BST_Referee_Methodology.md` App. D — tier definitions (D/I/C/S).
6. `notes/Lyra_F573_sin2thetaW...` — the running-vs-static demarcation.

*Compiled by Elie (corpus survey, verifier-framed) for the item-3 pivot. Tiers as-cataloged; re-verify load-bearing rows + grep retractions before external.*
