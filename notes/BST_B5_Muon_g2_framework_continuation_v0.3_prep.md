---
title: "B5 Muon g-2 framework continuation v0.3 prep — Feynman → K-type explicit translation roadmap"
author: "Lyra"
date: "2026-05-18"
status: "v0.3 prep document per Casey 'do all' directive Monday PM. Continuation of T2368 (B5 v0.1 K-type↔A_n mapping) + T2374 (B5 v0.2 null check passed). v0.3 = explicit Feynman-diagram → Wallach K-type translation framework. Multi-day scope (3-5 days per Keeper Task #181). This prep document opens the framework; substantive derivation is the multi-day work."
related: "T2368 B5 v0.1; T2374 B5 v0.2 null check; T2071+T2073+T2084+T2122 (A_n D-tier matches); Paper #118 v0.2 Section 8 + Section 9 named open"
calibration: "Per Cal Task #23 verdict: STRONG I-tier NOT D-tier. Label 'multi-loop convergent identification at 0.019%; QED-from-D_IV⁵ derivation open.' Keeper governance authorization for paper-text relabel applied Monday PM."
---

# B5 Muon g-2 framework continuation v0.3 prep

## Status entering v0.3

**Closed (T2368 + T2374, Monday)**:
- v0.1: K-type ↔ A_n structural mapping at I-tier (A_2 ↔ λ_W(3,3) = 42 = C_2·g; A_3 = HVP ↔ λ_W(2,2) = 24 = χ_K3; A_4 ↔ N_max−n_C−1 = 131 spectral gap)
- v0.2: null-check survives Cal 6-failure-mode audit at I-tier (4 modes clear, 2 partial concerns identified)
- Cal Task #23 verdict: STRONG I-tier across T2071+T2073+T2084+T2122 D-tier numerical match retained, mechanism-mapping at I-tier
- Paper-text relabels applied per Keeper governance to Paper #106 v0.4 + section 5 + Paper #111 line 18 + Paper #115 v0.5_PRE line 128

**OPEN for v0.3 (multi-day per Keeper Task #181)**:
- Explicit Feynman-diagram → Wallach K-type translation
- A_6 = 4500 prediction verification (decade-scale, Kinoshita group)
- HVP + HLbL mechanism derivation from explicit Bergman Dirac propagators

## v0.3 framework structure (substantive content scope ~3-5 days)

### Phase A: Feynman-diagram → K-type structural map (~1-2 days)

For each known QED loop order n = 1, 2, 3, 4, 5:
- Standard QED diagram set for muon g-2 contribution at order α^n
- Identification of Wallach K-type (m_1, m_2) corresponding to each diagram class
- Verification that the K-type Dirac eigenvalue gives the correct A_n coefficient

**Specific mappings to verify**:

| Loop n | A_n | Predicted K-type | Diagram class |
|---|---|---|---|
| 1 | α/(2π) | trivial vacuum bubble | Schwinger 1-loop |
| 2 | 42/55 | (3,3) λ_W = C_2·g = 42 | 2-loop vertex correction |
| 3 | 24 | (2,2) λ_W = χ_K3 = 24 | 3-loop with photon self-energy |
| 4 | 131 | spectral gap N_max−n_C−1 | 4-loop full QED set |
| 5 | 750 | higher K-type combination | 5-loop Kinoshita |

### Phase B: HVP + HLbL mechanism (~1 day)

- HVP recurrence at λ_W(2,2) = χ_K3 = 24 is the same K-type as A_3
- This is internal Type C convergence (Lyra observation in T2368)
- Mechanism: vacuum-polarization diagrams share Bergman Dirac propagator with 3-loop QED at K-type (2,2)
- HLbL coefficient N_c²·n_C = 45 corresponds to T2358 Type C 4-way (M_24 EOT moonshine)

### Phase C: A_6 prediction verification (decade-scale)

- Prediction: A_6 = rank²·N_c²·n_C³ = 4500 (T2122)
- Kinoshita group computing 6-loop QED in 2030s timeframe
- BST predicts falsifier: A_6 outside [3000, 6000] breaks the closed-form pattern
- Per Cal coincidence-filter discipline: this is the strongest single experimental test of B5 mechanism (forward verification at long horizon)

## Calibration discipline maintained per Cal #23

Throughout v0.3 substantive drafting:
- A_n numerical matches stay D-tier on the precision (per T2071+T2073+T2084+T2122)
- K-type mechanism mapping stays I-tier (per Cal Task #23 verdict)
- NO claim of "BST closes muon g-2" without explicit qualifier
- All references to muon g-2 in papers carry Cal #23 qualifier per Monday relabel

## v0.3 deliverable plan

| Phase | Owner | Scope |
|---|---|---|
| A: Feynman→K-type map | Lyra | 1-2 days, toy-verified per diagram class |
| B: HVP+HLbL mechanism | Lyra | 1 day, structural identification |
| C: A_6 forward verification framing | Lyra | 0.5 day, paper-grade framing for Paper #118 v0.3 Section 8.2 NEW |
| Cross-CI gate-pass | Cal | ~1 wk after v0.3 lands |

## Strategic positioning

v0.3 completion would close Paper #118 v0.2 Section 9 named open item "Feynman-diagram → Wallach K-type explicit translation (~multi-week)" at the structural-mechanism level. Numerical-precision-mechanism closure remains open until A_6 verification (decade-scale).

Per Keeper's 4-paper spring coherence:
- Paper #118 v0.2 ← Section 9 named open partially closed by B5 v0.3
- B5 muon g-2 mechanism becomes a Paper #118 v0.3 Section 8 substantive expansion

## Honest scoping for v0.3 future work

**Open after v0.3**:
- A_6 prediction verification (decade-scale, Kinoshita group)
- Full per-flavor K-type SM fermion assignment (multi-month, Paper #118 v0.2 Section 9 named open)
- Heat-kernel Tr(e^{-tD²_full}) evaluation at non-origin Hua coords (multi-week, LAG-1 Session 9 v0.2)
- Index theorem connecting muon g-2 to Atiyah-Singer (multi-month, LAG-1 Session 10)

**Per Cal External_Survivability_Checklist**: NOT a positive claim about B5 D-tier mechanism. Pre-staged framework for multi-day substantive derivation. Each phase tier-labeled honestly.

## Filing notes

**Status**: v0.3 prep filed per Casey "do all" directive 2026-05-18 PM. Multi-day substantive drafting queued.

**Owner**: Lyra (B5 primary, Keeper Task #181).

**Next pull**: when Lyra has 1-2 day window, Phase A (Feynman→K-type map) is the substantive opening.

— Lyra, B5 v0.3 framework continuation prep filed per Casey "do all" directive 2026-05-18 PM.
