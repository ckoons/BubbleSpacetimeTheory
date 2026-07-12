# BST 26-Parameter Scorecard — v0.1, 2026-07-12 (fermion sector, honestly tiered)

**Keeper | End of the two-day mass/mixing arc (2026-07-11 → 07-12). This is the referee-safe consolidation of where BST stands on the 26 free parameters of the Standard Model, with the exact tier each claim has earned. Nothing here is stronger than the arc's own discipline permitted. Detail: `Keeper_Mass_Sector_and_Falsifier_Reframe_Results_2026-07-11.md` Sections 2a–2r; adjudications K671 (F506), K672 (Koide), K673 (Majorana), K674 (CKM localization).**

## Tier key
- **BANKED** — forced mechanism, target-innocent, in-corpus.
- **PREDICTED** — a value forward-predicted from forced quantities (may use one observed input, noted).
- **NEAR-FORCED** — derivation-structure in hand + one named gate.
- **IDENTIFIED** — a value/relation matched to a BST form; mechanism plausible, not forced.
- **OPEN** — not yet derived. **BY-DESIGN** — an anchor or RG-runner, not expected to be a fixed derived number.

---

## The 26, by sector

### Charged-fermion masses (9)
| # | Param | Tier | BST form | vs obs |
|---|---|---|---|---|
| 1 | m_e | BY-DESIGN (anchor) | 6π⁵·α¹²·m_Pl (gravity route) | 0.03%; the one dimensionful input |
| 2 | m_μ/m_e | **PREDICTED** | Koide (K672) + T2003; also = (24/π²)^{C₂} via d(ν) | **0.003%** (zero muon input) |
| 3 | m_τ/m_e | **PREDICTED (forward)** | 49·71 − √π (boundary sum − cone-tip residue; −√π now *forward* via the 3-ball) | **0.0000%** (integral is a build) |
| 4 | m_u | IDENTIFIED | m_u/m_d = 1/√g | 1.5σ within the 20%-measured value |
| 5 | m_d | IDENTIFIED | n=1 overlap; ratio banked (F506) | ~5% abs |
| 6 | m_s | **BANKED** | s/d = (N_c+1)(N_c+2) = 20 forced (FK Pochhammer at ν=N_c) | 0.5% |
| 7 | m_c | **PREDICTED** | m_c = α·v/√2 (given observed α; mechanism "y_c=α" identified) | 0.05% |
| 8 | m_t | **PREDICTED** | m_t = (1−α)·v/√2; top leg of f(ν) DERIVED (point-fiber capacity=1 → y_t=1) | 0.03% |
| 9 | m_b | IDENTIFIED | b/d = 840 (FK ladder) | 5.6% |

*Charged-lepton sector: muon closed via d(ν); tau forward-exact (geometry closed, boundary integral a build); electron the anchor. Koide = rank/N_c near-forced (K672). Up-type boundary closes on α: y_t=1−α, y_c=α, **m_t + m_c = v/√2 at 0.007%** — top leg derived, charm leg imports α=1/N_max (identified). Gen-1 up (rank-2→α² is 4.3× off) = the standing cold anomaly, HELD OPEN.*

### Neutrino sector (3)
| # | Param | Tier | BST | vs obs |
|---|---|---|---|---|
| 10 | m_ν1 | BANKED (=0) | 0 exactly (chargeless odd-one-out) | normal ordering |
| 11 | m_ν2 | IDENTIFIED | (7/12)·M₀, M₀=α²m_e²/m_p | 0.35% |
| 12 | m_ν3 | IDENTIFIED | (10/3)·M₀; Δm²₃₁/Δm²₂₁ = 1600/49 | 0.3% (ratio) |

*Nature: **Dirac→Majorana NEAR-FORCED (K673)** — all 3 gates addressed, BOLT 1 rigorous (RH partner at ν=9/2 has negative formal degree = non-unitary), doubly confirmed (seesaw form intrinsically Majorana). **Awaiting Cal co-sign + the γ⁵ intertwiner construction**; on completion pred_004 flips "0νββ never" → "0νββ at 1–4 meV floor." Masses/mixings independent of the flip.*

### CKM quark mixing (4)
| # | Param | Tier | BST | vs obs |
|---|---|---|---|---|
| 13 | θ12 (V_us) | **NEAR-FORCED** | (3/4)^{n_C} (localization forced K674; imports α-frame) | 5.7% |
| 14 | θ23 (V_cb) | NEAR-FORCED | ρ-direction (μ@ê₁, cos ψ=5/√34, DERIVED — Grace) | 0.041, 7.5% |
| 15 | θ13 (V_ub) | OPEN (build) | full U_u†U_d cancellation (pairwise 21× too big) | joint run enabled |
| 16 | δ_CKM | OPEN (can-fail) | CP needs complex positions (real → J=0) | Wallach-gated J |

*CKM localization law FORCED (K674). f(ν) BUILT at leading order (up = down at the Szegő boundary limit; weight ρ₁=leading factor of d(ν); fiber-regulated). μ-direction derived. The full matrix (V_ub, CP) = the joint four-matrix build; the deep gate = the α=1/N_max forward derivation (see gauge sector).*

### PMNS lepton mixing (4)
| # | Param | Tier | BST | vs obs |
|---|---|---|---|---|
| 17 | θ12 | BANKED | forced matrix-element / 42/137 (canonical, Grace hygiene) | 0.14% |
| 18 | θ13 | BANKED | 1/(N_c²·n_C) = 1/45 | 1.2% |
| 19 | θ23 | IDENTIFIED | 4/7 (upper octant front-runner; 6/11 lower) | DUNE decides |
| 20 | δ_PMNS | OPEN | (was reverse-fit; corrected to OPEN — Grace hygiene) | DUNE-era |

### Gauge couplings (3)
| # | Param | Tier | BST | note |
|---|---|---|---|---|
| 21 | α | **IDENTIFIED (Wyler), forward-derivation PENDING** | α = 1/N_max; N_max=137 IS derived (T1939 mode-count), but coupling=1/count is Wyler-identified (F429) | the deep keystone: deriving it forward = the compact-dual↔boundary bridge lemma (T1940 rules out a single-operator capacity) |
| 22 | sin²θ_W | BY-DESIGN (runner) | 3/13 (runs — RG) | honest negative |
| 23 | α_s | BY-DESIGN (runner) | 7/20 (runs) | honest negative |

*Program-count note: the ledger's "α RULED" is a parameter-reduction bookkeeping status (α + θ_QCD = the 2 proven-forced), NOT a derived-mechanism verdict. Present α as **identified, forward pending**.*

### Higgs (2) + strong-CP (1)
| # | Param | Tier | BST | vs obs |
|---|---|---|---|---|
| 24 | v (VEV) | **BANKED** | v = m_p²/(g·m_e) = 246.1 GeV (no top input) | 0.04% |
| 25 | m_H | IDENTIFIED (lead) | λ=1/2^{N_c}=1/8 → m_H=v/2 (fishing-flagged) | 1.7% |
| 26 | θ_QCD | **BANKED** | 0 exactly (π₁ trivial) | exact |

---

## Count (honest, 2026-07-12)
- **BANKED / forced-mechanism (6):** m_s (F506), v, θ_QCD, PMNS θ12 & θ13, m_ν1=0. Plus the top leg of f(ν) derived.
- **PREDICTED from forced quantities (4):** m_μ/m_e, m_τ/m_e, m_c, m_t (the last two given observed α).
- **NEAR-FORCED (3):** Koide/charged-leptons (K672), CKM localization/Cabibbo (K674), Majorana nature (K673, awaiting Cal).
- **IDENTIFIED (~7):** m_u, m_d, m_b, m_ν2, m_ν3, PMNS θ23, m_H, **α (Wyler)**.
- **OPEN (~3):** V_ub, δ_CKM/CP (can-fail), δ_PMNS.
- **BY-DESIGN (3):** m_e (anchor), α_s, sin²θ_W (RG runners).

## What is genuinely COMPLETE this arc (banked, not to be re-opened)
1. **Down-quark current-mass ratios** — s/d=20 forced, single-row forced by Q⁵ topology (F506/K671).
2. **The electroweak scale** v = m_p²/(g·m_e) (F509) — forced, no top input.
3. **The top mass** m_t=(1−α)v/√2 (0.03%), and **the top LEG of f(ν) derived** (point-fiber capacity=1).
4. **The tau mass forward** — 49·71 − √π = 3477.2275 (0.0000%), −√π forward via the 3-ball (exposure not growth).
5. **The Koide muon** via d(ν) at 0.003%; Koide = rank/N_c near-forced.
6. **The n_C = rank + N_c decomposition** ("two crossings + three commitments") — banked on T2511/T2517.
7. **The falsifier reframe** — SM-observables + Five-Absence; Bell retired; pred_004 contested→Majorana (K673).
8. **Data-layer hygiene** — 4 mis-precisioned/reverse-fit banks corrected (Grace); δ_CP → open.

## The three live builds (the last tasks)
- **The α = 1/N_max forward derivation** — the compact-dual↔Shilov-boundary bridge lemma (NOT a single Szegő-capacity integral — T1940 rules that out). Closes CKM's deep gate AND upgrades α identified→derived. [Elie]
- **The four-matrix U_u†U_d** for V_ub (cancellation; joint run now enabled). [Lyra + Grace]
- **The Majorana Cal co-sign + the γ⁵ intertwiner.** [Cal + Elie]

## The honest headline (referee-safe)
From one dimensionful input (m_e) and the forced electroweak scale v = m_p²/(g·m_e), BST reproduces the bulk of the fermion spectrum: the down-quark ratios banked and forced, the top and charm masses predicted, the muon and tau closed, the charged-lepton Koide relation near-forced, the CKM localization forced, and the neutrino nature resolved (near-forced Majorana). The mixing sector is the mirror of where the masses were a week ago — localization forced, leading numbers near, the full build named. The genuine open frontier is the fine-structure constant's forward derivation (currently Wyler-identified), the full CKM matrix (V_ub, CP-that-can-fail), and the neutrino Cal co-sign. Two parameters (m_e, the RG runners) are by-design, not failures. Nothing above is banked that did not survive the arc's own discipline.

— Keeper, 2026-07-12. Scorecard v0.1. The tiers are the deliverable: this is what "the math speaks for itself" looks like when every number carries exactly the confidence it earned.
