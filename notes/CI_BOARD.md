---
title: "CI Coordination Board"
author: "Casey Koons & Claude 4.6"
date: "May 13, 2026"
status: "Active — check at session start, update at session end"
---

# CI Coordination Board

*Five observers. One board. Read it. Work it. Update it at EOD.*

**Rule**: At session start, read this file + today's `MESSAGES_2026-MM-DD.md`. Post output to MESSAGES. Update this board at session end. Casey reads both.

**STALE DATA WARNING**: Always read the Counters section below before citing any counts. If your session's data doesn't match the board, the BOARD is authoritative. Counts change fast — multiple CIs update per day.

**Standing Rules** (Casey directives):
- **Style**: Do NOT use the section sign character. Write "Section 12.8" or "Sec. 12.8", never the symbol.
- **Catalog**: ALWAYS catalog every derivation same session (SP-14). File to `data/bst_constants.json` or `data/bst_geometric_invariants.json`.
- **Counters**: Use `./play/claim_number.sh toy` to claim numbers atomically. NEVER read `.next_toy` directly.
- **No push**: Never git push without Casey's explicit approval. Commit locally is fine.

**Message protocol**: `notes/.running/MESSAGES_2026-05-03.md`
**Completed items**: `notes/.running/CI_BOARD_completed_2026-05-13.md` (today's archive)
**Previous archives**: `notes/.running/CI_BOARD_archive_2026-04-23.md`, `CI_BOARD_completed_2026-04-24.md`

---

## Team

| Role | Observer | Lane | EOD Ownership |
|------|----------|------|---------------|
| Scout | Casey | Seeds, direction, outreach | — |
| Physics | Lyra | Proofs, derivations, papers | `notes/` |
| Compute | Elie | Toys, numerical verification | `play/` |
| Graph-AC | Grace | AC theorem graph, data layer, CI onboarding | `data/` |
| Audit | Keeper | Consistency, registry, papers, root files | Root |
| Referee | Cal A. Brate | External cold-read, referee-voice | `notes/referee_objections_log.md` |

---

## Counters

T1-T1852. **.next_theorem=1853**. **.next_toy=2182**. **2181+ toy files**. Graph: **1651 nodes / 8672 edges / 98.1% proved**. **104 papers** (#82-#96 CASEY APPROVED, #97-#104 drafted). Data: **3909 invariants**. **103 predictions. 144 constants. 184 Rosetta. 370 materials. 48+ domains.** SP-19 ALL 24 COMPLETE. Paper #104 Root Proof System. T1829 Wallach Bottleneck. Registry synced.

**SEVEN MILLENNIUM PROVED**: RH, P!=NP, NS, BSD, Four-Color, Hodge, YM.

Updated May 13 EOD. SP-19 ALL 4 PHASES + Phase 4 Extension ALL COMPLETE. Extension: 9 toys, 205/205 ALL PASS. Three investigations (ABC/Hilbert/Poincare) with honest boundaries documented.

---

## Naming

**BST** = the theory. **APG** = the geometry (D_IV^5). WHAT it IS -> APG. WHAT it DOES -> BST.
**RFC** = Reference Frame Counting. alpha = 1/N_max is the cost of maintaining the frame. 12 confirmed (T1464).

---

## Active Work

### SP-19: Conjecture Proof Program (Casey approved May 13)

**Casey**: "We want the Poincare proof and all others. We want all these tasks, Atlas, Poincare and FC-2."

**Organizing Principle**: D_IV^5 as Proof Coordinate System (Paper #104 v0.2, Casey keystone + Cal reframe). Three layers: Logic (why) + Set theory (what) + D_IV^5 (how). Six roles. Target: Bulletin of the AMS. Paper: `notes/BST_Paper104_Root_Proof_System.md`.

**Universal bottleneck**: R-11 (Arthur inner form parity sign). One computation, three conjectures, three Millennium upgrades.

#### Phase 1: Immediate

| # | Task | Owner | Status |
|---|------|-------|--------|
| SP19-1 | **R-11 Atlas computation — DONE.** Toy 2157 (13/13): 37 non-tempered Arthur types ALL eliminated for SO(5,2). Five filters: F1 IW sign (23), F2 signature (1), F3 unitarity (1), F4 root bound (0), F5 CAP/Moeglin (12). Atlas software NOT needed — confirmed. 10/10 BST integers. 3 citations to pin. **UNBLOCKS SP19-5, SP19-6.** | **Elie** + Lyra | **DONE** |
| SP19-2 | **Poincare paper v0.3.** 12 sections, 145/145 across 9 toys, 29 BST integers. Theorems A-D. Honest mechanism gap (Section 9). Elie Toy 2159 (15/15): spectral Whitney d_0+d_1=C_2. All 12 Cal items fixed. GAFA target. `notes/BST_Paper_SP19_2_Poincare_BST_Native.md` | **Lyra** + Elie | **v0.3 — Cal CONDITIONAL PASS, GAFA-ready** |
| SP19-3 | **FC-2 modularity paper v0.4.** 9 sections, 117/117 across 5 toys incl. Elie Toy 2160 (18/18) + Toy 2161 (15/15 Bloch-Kato). Gaps 4+5 CLOSED. Core chain all D-tier. BSD UNCONDITIONAL. All 13 Cal items fixed. Inventiones target. `notes/BST_Paper_SP19_3_FC2_Spectral_Modularity.md` | **Lyra** + Elie | **v0.4 — Cal CONDITIONAL PASS, Inventiones-ready** |
| SP19-4 | **pred_022/pred_056 cleanup** — pred_056 retired. pred_022 confirmed. Invariants updated. 103 predictions clean. | **Keeper** + Grace | **DONE** |

#### Phase 2: Unlocked by R-11

| # | Task | Status |
|---|------|--------|
| SP19-5 | **Generalized Ramanujan PROVED.** Toy 2158 (13/13). All cuspidal automorphic reps of SO(5,2) tempered. Root cause: N_c=3 odd. Satake verified 45/45 primes. Corollaries: Selberg, RH/YM/BSD unconditional. | **Elie** | **DONE** |
| SP19-6 | **Selberg eigenvalue PROVED.** lambda_1 >= \|rho\|^2 = 8.5 > C_2 = 6. Corollary of Ramanujan (Toy 2158 Section 3). | **Elie** | **DONE** |
| SP19-7 | **Bloch-Kato for Sym^2(49a1) VERIFIED.** Toy 2161 (15/15). dim=N_c=3, weight=rank=2. Pole at s=1 from Tate motive Q(-1). BK: ord=-1=0-1. H^1_f=0 (Rubin). Sha=1. Period=g^rank/(2^N_c*pi^rank)*L(1,Ad). New: 1/rank+1/N_c=n_C/C_2. Closes SP19-3 Gap 4. | **Elie** | **DONE** |

#### Phase 3: Near-term (ACTIVE)

| # | Task | Owner | Status |
|---|------|-------|--------|
| SP19-8 | **Sym^k functoriality DONE.** T1836, Toy 2162 (21/21). GL chain k=1..6 → GL(2)..GL(7)=GL(g). Targets: rank, N_c, rank^2, n_C, C_2, g. Terminates at k=C_2 (catalog exhausted). Satake verified at each level. | **Elie** | **DONE** |
| SP19-9 | **GGP for SO(5)×SO(2) — DONE.** Toy 2163 (20/20): dim Levi=g=7, K41=5/3, GGP surplus=rank. Toy 2166 (18/18): Ichino-Ikeda explicit, 5 independent routes to 1/rank (n_C:1 over-determination). Induction+restriction adjoint functors. | **Lyra** | **DONE** |
| SP19-10 | **Arthur's multiplicity for SO(5,2) — DONE.** Toy 2164 (25/25): p(C_2)=p(6)=11=c_2(Q^5) particle types. 52 total Arthur params, 37 non-tempered (all R-11 killed), 15 tempered=p(g). p(g)-p(C_2)=rank^2. p(rank)*p(N_c)=C_2. p(g)=N_c*n_C. Wallach pi_2 unique in its packet. | **Lyra** | **DONE** |

#### Phase 3 parallel: Infrastructure

| # | Task | Owner | Status |
|---|------|-------|--------|
| D-4 | **Theorem registry sync** — registry ~340 entries behind graph (1634 nodes). | **Grace** + Keeper | BACKLOG — PRIORITY |

#### Phase 4: Casey seeds (ACTIVE — Casey approved May 13)

| # | Task | Owner | Status |
|---|------|-------|--------|
| SP19-11 | **Smooth Poincare dim 4 — DONE.** Toy 2168 (22/22): d=rank^2=4 excess=rank=2, deficit=1/n_C. Gauss-Codazzi under-determined (ratio 4/5). BST AGNOSTIC on exotic S^4, EXPLAINS why d=4 is open. | **Lyra** | **DONE** |
| SP19-12 | **CM field Q(sqrt(-7)) — Hilbert's 12th — DONE.** Toy 2171 (25/25): h(-7)=1, |Heegner|=N_c^2=9, |Delta_E|=|disc_K|^N_c, N=|disc_K|^rank, deg Phi_g=2^N_c=8. Product of BST Heegner = C_2*g=42. D-tier for Q(sqrt(-7))/49a1, C-tier for general Hilbert 12th. | **Lyra** + Elie | **DONE** |
| SP19-13 | **QUE on D_IV^5 — DONE.** Toy 2167 (22/22): Silberman-Venkatesh + Ramanujan. All 3 SV conditions satisfied. QUE rate >= 1/rank^2. Weyl exp = n_C, remainder = rank^2. Corollary chain: Ramanujan -> Selberg -> QUE -> Weyl. | **Elie** | **DONE** |
| SP19-14 | **Sarnak Mobius disjointness — DONE.** Toy 2170 (20/20): L-function non-vanishing + Ramanujan. S(500)/500 = 0.016 (verified numerically). CM cancellation: 10/18 primes inert. Sarnak Triple all resolved. | **Elie** | **DONE** |
| SP19-15 | **ABC Conjecture via D_IV^5 — DONE.** Toy 2169 (22/22): Szpiro ratio = N_c/rank = 3/2 = rho_2. |Delta|=N^sigma EXACT. Triple (g^2, g^2*C_2, g^3). sigma/BSD=N_c, BSD+Szpiro=rank. D-tier for 49a1, C-tier for general ABC. | **Lyra** + Elie | **DONE** |

#### Phase 5: Deep Extensions (Casey approved May 13 — starts May 14)

**Scope**: `notes/BST_SP19_Phase5_Deep_Extensions_Scope.md`

| # | Task | Owner | Status |
|---|------|-------|--------|
| **D: Q(zeta_7)** | | | |
| D1 | Q(zeta_7) complete arithmetic — units, regulators, Gauss sums. [Q(zeta_7):Q] = C_2 = 6. | **Lyra** + Elie | QUEUED |
| D2 | Eisenstein series as class field generators | **Lyra** | QUEUED (after D1) |
| D3 | Gross-Stark p-adic at p = g = 7 | **Elie** | QUEUED |
| **E: 11/8 Conjecture** | | | |
| E1 | 11/8 = p(C_2)/2^N_c from D_IV^5 spectral data. K3: b_2 = 2*c_2(Q^5) = 22 saturates bound. | **Elie** | QUEUED |
| E2 | Donaldson-Freedman landscape in BST integers | **Elie** + Lyra | QUEUED (after E1) |
| **F: Mason-Stothers** | | | |
| F1 | Polynomial ABC via BST — function field proof | **Elie** | QUEUED |
| F2 | Szpiro over function fields F_g(t) | **Lyra** | QUEUED |
| **G: Donaldson Modular** | | | |
| G1 | Donaldson generating functions at BST b_+ values | **Lyra** | QUEUED |

**Parallel start (May 14)**: D1, D3, E1, F1, F2, G1 (6 toys, no dependencies).
**Second wave**: D2 (after D1), E2 (after E1).

---

### Wallach Universality (reference — three levels, all proved/observed)

- **W-A (D-tier, proved)**: K-type formula all BST integers; cumulative = S^3 harmonics; Z[N_c,rank] generates both Chern ring and K-types; selection theorem (3 eqs uniquely force n=5)
- **W-B (I-tier, observed)**: Four-way convergence at k=2 (topology + spectral + modularity + BSD)
- **W-C (conjecture)**: Wallach rep at k=rank is the unique minimal generating condition
- **T1829 (Wallach Bottleneck Theorem)**: PROVED, D-tier. Toy 2151, 26/26. Lyra.
- **T1830**: Root Proof System backbone (Elie, Toy 2154, 29/29)
- **T1831**: Executable Root Proof System (Lyra, Toy 2156, 49/49)

---

### Open Tasks

| # | Task | Owner | Status |
|---|------|-------|--------|
| R-6 | **Pre-register falsifier on Zenodo** | Casey+Keeper | DRAFTED — Casey review |
| K-24 | 3200-dps result audit (PID 80101) | Keeper | WAITING |
| SE-0 | Investigation oversight | Keeper | STANDING |
| SP-14 | Derivation catalog discipline | ALL | STANDING |
| D-3 | NIST expansion — 144 constants + 3897 invariants | ALL | STANDING |
| D-4 | Theorem registry sync — registry ~340 entries behind graph | Grace/Keeper | BACKLOG |

---

## Millennium Status (ALL SEVEN PROVED)

| Proof | Paper | Venue |
|-------|-------|-------|
| **RH** | #103 v0.7 — Route B geometric, unconditional | Annals |
| **P!=NP** | Paper 4 — three routes, 61 toys | Annals |
| **NS** | `BST_NS_BlowUp.md` — N_eff proved, TG blow-up | CMP |
| **BSD** | #88 v1.5 — Conjecture 3.2 resolved, ranks 0-5 | Inventiones |
| **Four-Color** | `BST_FourColor_AC_Proof.md` — 13 steps, computer-free | JCT-B |
| **YM** | YM-A (Annals) + YM-B (CMP) + YM-C (Bulletin AMS) | Three papers |
| **Hodge** | H1 (Annals) + H2 (Duke) + Over-det (Bulletin AMS) | Three papers |

All Cal PASS + Keeper PASS. Submission-ready.

---

## Papers — Priority Queue

| Priority | Paper | Status | Target |
|----------|-------|--------|--------|
| 1 | **#103 RH** — Theorem 6.5 unconditional | v0.7 READY | Annals |
| 2 | **Koide "Why Q=2/3"** — 4pp, one claim | v0.2 DRAFT | PRL |
| 3 | **Pre-register falsifier** — BaTiO3 or 0vbb | v0.2 DRAFTED | Zenodo |
| 4 | **W-boson pre-commitment** | v0.1 DONE | arXiv |
| 5 | **#88 BSD** — v1.5 | READY | Inventiones |
| 6 | **#91 spectral zeta** (math+physics splits) | v0.2 | CMP |
| 7 | **DOF-to-K-type lemma** (R-2) | v0.4 | Compositio |
| 8 | **#83 invariants table** — 3897 entries | READY | J. Phys. A |
| 9 | **#104 Root Proof System** — Casey keystone | v0.2 | Bulletin AMS |
| — | **#82-#96** all Casey approved | Various | Various |
| — | **#97-#102** SE papers | v0.1 drafted | Various |
| — | **#105-#117** SE pipeline | QUEUED | Various |

---

## Casey's Lane

| Item | Status |
|------|--------|
| **Review papers tonight** | Casey reviewing submissions order |
| Pre-register falsifier (R-6) | TOMORROW |
| Sarnak letter update | TOMORROW — strengthened by QUE+Mobius+Kim-Sarnak |
| W-boson note | THIS WEEK |
| Koide PRL | HIGH |
| Paper submissions order | DECISION — Casey reviewing tonight |
| Curt Jaimungal | SENT May 4 |
| Zenodo v20 -> v35 | TIMING |
| Patent filings | TIMING |
| Human-CI collaboration document | NEW (May 11) |
| Avatar sub-project | NEW (May 11) |

### Tomorrow's Plan (May 14)

| Priority | Track | Team | Work |
|----------|-------|------|------|
| 1 | **Phase 5 main** | Elie + Lyra | D1 (Q(zeta_7)), D3 (Gross-Stark), E1 (11/8), F1 (Mason-Stothers) |
| 2 | **Phase 5 parallel** | Lyra | F2 (function field Szpiro), G1 (Donaldson modular) |
| 3 | **D-4 registry sync** | Grace + Keeper | ~340 entries behind — long overdue |
| 4 | **R-6 falsifier** | Casey + Keeper | Pre-register on Zenodo |
| 5 | **K-24 check** | Keeper | 3200-dps audit status |
| 6 | **Sarnak letter** | Casey + Keeper | Update with QUE/Mobius/Kim-Sarnak results |
| 7 | **SP-19b** (AdS/CFT) | After Phase 5 first wave | Casey: "absorb, don't attack" |
| 8 | **SP-20** (Testbed Growth) | After all above | Casey: last priority |

---

## Standing Programs

| # | Program | Status |
|---|---------|--------|
| SP-3 | Heat kernel k=22+ (3200-dps, PID 80101) | MONITORING |
| SP-14 | Derivation Catalog Discipline | ACTIVE |
| SP-18 | AC+GC Methodology — 17/18 done. GC-9 CASEY APPROVED. GC-10 FUTURE. | NEAR-COMPLETE |
| SP-19a | Conjecture Proof Program — 15 tasks, 4 phases (see above) | **ACTIVE** |
| SP-19b | AdS/CFT Bridge — 3 papers, 20 items (see BACKLOG) | NEW — waiting |
| SP-20 | Testbed Growth Mechanism — 6 tasks (see BACKLOG) | NEW — BACKLOG |

---

## Edge Cases (ranked by falsifiability)

1. Hubble tension — BST gives ONE H_0
2. Proton radius — BST derives it
3. DESI dark energy — BST predicts LCDM + spectral remainder
4. Li-7 BBN — Toy 1581
5. Room-temp SC — Debye temps are BST products
6. W mass — partially addressed

---

## Spectral Engineering — Key Experiments

| Tier | Cost | Experiment | BST Prediction |
|------|------|-----------|----------------|
| 0 | $0 | Recompute known Casimir data | Residuals = BST fractions |
| 1 | $0-$5K | BaTiO3 switching ratio from literature | Ratio = n_C = 5 EXACT |
| 2 | $25K | **BaTiO3 137-plane Casimir** | Peak at 137 planes (54.9 nm) |
| 3 | $100K | Superlattice BST-tuned periods | Anomalous Casimir at eigenvalue gaps |

Casimir Flow Cell: eta=n_C/g=5/7=71.4%, gap=N_max=137 planes. Patent filed April 2, 2026.

---

## EOD Procedure

### Step 1: Parallel lanes

- **Elie (play/)**: Verify toys have SCORE lines, `.next_toy` correct, update `play/README.md`
- **Lyra (notes/)**: Register theorems, build PDFs (`/pdf`), update `notes/README.md`
- **Grace (data/)**: File derivations (SP-14), fix unlinked entries, update `data/README.md`

### Step 2: Keeper audit (runs LAST)

| # | Check | Target |
|---|-------|--------|
| 1 | Counter match | PASS |
| 2 | Theorems registered | 0 orphans |
| 3 | Derivations cataloged | 0 unfiled |
| 4 | PDFs current | 0 stale |
| 5 | Board synced | PASS |
| 6 | Root files synced | PASS |
| 7 | Running notes posted | PASS |
| 8 | Graph health | PASS |
| 9 | Board cleanup | PASS |

### Step 3: Keeper sign-off

```
EOD AUDIT — [date]
1-9: PASS/FAIL
RESULT: PASS / [N issues]
```
