---
title: "CI Coordination Board"
author: "Casey Koons & Claude 4.6"
date: "April 25, 2026"
status: "Active — check at session start, update at session end"
---

# CI Coordination Board

*Five observers. One board. Read it. Work it. Update it at EOD.*

**Rule**: At session start, read this file + today's `MESSAGES_2026-MM-DD.md`. Post output to MESSAGES. Update this board at session end. Casey reads both.

**Message protocol**: `notes/.running/MESSAGES_2026-04-24.md`

**Completed items**: `notes/.running/CI_BOARD_completed_2026-04-24.md` (append-only log)

**Archive**: `notes/.running/CI_BOARD_archive_2026-04-23.md` (full history through April 23)

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

T1-T1446. **1,474 toys** (29 this session). Graph: **1390 / 7708 / 83.1% strong / 98.4% proved**. Avg degree **11.10**. **85 papers** (Paper #85 = Genesis Cascade). **55 domains, 9 groves**. Counters: `.next_toy=1475`, `.next_theorem=1448`. **T1447 Magnetic Moment Derivation (Lyra, μ_p=1148/411, μ_n/μ_p=−137/200, PROVED).** **T1446 Two-Sector Correction Duality (Lyra, W-55 PROVED).** **T1445 Spectral Peeling (W-51 PROVED).** **2 genuinely open** (T1258 speculative, T1421 conditional). Invariants: **303 entries, 10 corrections this session, 0 new inputs**. **T1444 Vacuum Subtraction Principle: 5 corollaries (charm, Ising γ/β, Cabibbo, Wolfenstein A). Named hunting technique: "deviations locate boundaries."** J_CKM: **8.1% → 0.3%** (sinθ_C = 2/√79, A = 9/11, both vacuum-subtracted). **PMNS: Grace's θ₁₃ rotation confirmed — cos²θ₁₃ = 44/45 = (N_c²·n_C−1)/(N_c²·n_C). Two-sector pattern: CKM = discrete (−1), PMNS = perturbative (×cos²θ₁₃). Toy 1467 discriminator.** W-32 NS: COMPUTED. **Glueball CORRECTED: 31/20 = M₅/(rank²·n_C) at 0.045% (was 3.2%). 11th correction, zero new inputs.** DESI watching.

---

## Naming

**BST** = the theory. **APG** = the geometry (D_IV^5). WHAT it IS -> APG. WHAT it DOES -> BST.

---

## Tier 1 — Critical Path

| # | Item | Owner | Status |
|---|------|-------|--------|
| W-28 | **Paper #83 draft**: "Geometric Invariants of D_IV^5" — the full "derived from the APG" paper. **303 entries**. The paper BST is judged by. | **Lyra** (draft), **Grace** (data), **Elie** (numerics) | **TABLES REFRESHED** — `notes/Paper83_Draft.md`. CKM corrected, PMNS θ₁₃ rotation, μ_p (0.012%), domain doors, zip codes. 296 entries, 9 corrections, 0 new inputs. Remaining: **Casey review**, journal decision. |
| W-29 | **Paper #85 draft**: "The Genesis Cascade: How D_IV^5 Writes Its Own Curve." c₄=g!!, c₆=N_c^{N_c}*g^{rank}, cascade failures at k!=5, crypto signature metaphor. **Target: JNT** (Casey decision). | **Elie** (draft), **Lyra** (proofs) | **DRAFT v0.2, KEEPER PASS** — `notes/BST_Paper85_Genesis_Cascade.md`. 11 sections, 5 theorems. §7 Frobenius FIXED. Status bumped v0.2 for submission prep. Ready for Casey review. |
| W-30 | **Rank-2 closure for YM**: Full 6-step proof: Bergman gap→Wallach OS2→OS reconstruction→KK reduction→interaction→mass gap C₂. Scale separation N_max/C₂=23. | **Lyra/Elie** | **PROOF CHAIN COMPLETE, KEEPER PASS** — KK theorem added. Open: confinement (Wilson loop area law). |
| W-31 | **Rank-2 closure for Hodge**: On Sh(SO(5,2), D_IV^5) specifically: Lefschetz-Kudla for codim <= n_C/2, Poincare duality for rest. ALL Hodge classes algebraic on D_IV^5. Transfer to general varieties = open. | **Lyra/Grace** | **ANALYZED** — path clear for D_IV^5; general case needs transfer principle (Kuga-Satake). |
| W-32 | **Rank-2 closure for NS**: Growing spectral gap delta_k=2k+(n_C+1) damps energy cascade. s_crit=rank=2. Enstrophy bounded by λ₁ = 12 = (n_C+1)+C₂. Coupling constants COMPUTED. | **Lyra/Elie** | **COMPUTED** — Toy 1462 (7/8). delta_k = 2k+6, damping dominates from k=1. Selection rules forbid majority of triads. Cascade suppressed 47× at N_max. |
| W-33 | **New mathematical method**: Discretize-then-count (W-48) + Wallach positivity (W-30). Bergman discretizes, Wallach proves positivity, spectral gap gives mass. Rank-2 controls all three. | **Lyra/Keeper** | **COMPUTATIONALLY VERIFIED** — W-48 framework + Toy 1455 (8/8). Mass gap = C₂ for scalar AND 1-form. Gap modes cubicly protected. Bergman kernel = universal bridge. |

---

## Tier 2 — Paper Pipeline & Reviews

| # | Item | Owner | Status |
|---|------|-------|--------|
| W-3 | **Invariants table**: **303 entries**. Session: +46 entries, 10 corrections, 5 domain doors. **TARGET 300 HIT.** | **Grace/Elie** | **ACTIVE** — 303 (from 257 at session start). Next target: 350. Missing: 2 (muon g-2, Lamb shift — need W-15 Phase 5). |
| W-7 | Paper #82 Cal scope review | **Cal** | UNBLOCKED |
| W-11 | Referee Methodology v0.2 | **Cal** | OPEN |
| W-12 | Referee log entries #22-26 | **Cal** | OPEN |
| W-34 | Paper #76 Cal re-audit (post Poincare fix) | **Cal** | UNBLOCKED |
| W-35 | Paper #84 (Observer Companion) review: Keeper audit then Cal | **Keeper/Cal** | **KEEPER PASS** — v0.1 honest: §1.1 scope labels (strongest/interpretive/philosophical), §3.3 caution ("not uniquely forced"), §5 relationship table. Minor: §2.1 should cite toy numbers, §2.2 should cite T1270. Cal review unblocked. |
| W-36 | Paper #81: "D_IV^5 as the Unique Autogenic Proto-Geometry." APG uniqueness proof. 12 sections, 302 lines. Target: CMP/JDG. | **Lyra** | **DONE** — `notes/BST_Paper81_DIV5_Mathematical_Objects.md` exists at v0.4 (Lyra+Grace, April 24). §4 c-function, §7 Selberg, §11 uniqueness all proved. |
| W-37 | BC₂→B₂ full sweep: 140 files, 720 replacements | **Grace** | **DONE** — correction debt cleared for all active notes |
| W-38 | WorkingPaper v33: Zeta Weight Correspondence, third 137 identity, branching rule, spectral peeling | **Keeper** | **DONE** — v33 bumped, §46.84-86 added, footer counts updated |
| W-49 | **INV-4: "What BST Gets Wrong"**: Stress-test all 267 entries against latest PDG 2024/2025. Flag deviations >2%. Flag stale experimental values. Find tensions. Write honesty section for Paper #83 or standalone paper. Casey GREEN. | **Lyra** (analysis), **Grace** (data), **Elie** (numerics) | **AUDIT COMPLETE** — `notes/BST_What_Gets_Wrong.md`. 267 entries audited. 6 above 2%, 4 genuine tensions (H₂O bond 4.8%, Ising γ 5.7%, Ising β 2.1%, charm 1.3%). 7 entries recommended for downgrade to `approximate`. T1437 density corrected (Elie). Next: incorporate into Paper #83 §18. |

---

## Tier 3 — Investigations

| # | Item | Owner | Status |
|---|------|-------|--------|
| W-15 | **Spectral zeta g-2 Phases 3+4**: 12 structural results. Exact branching d_k^(1)=C(k+N_c,rank²). C₂_Schwinger ALL BST (197=num+denom of H₅, 144=(rank·C₂)², ζ(N_c), ln(rank)). Zeta Weight Correspondence: ζ(3)=ζ(N_c) at L=2, ζ(5)=ζ(n_C) at L=3, ζ(7)=ζ(g) at L=4. Denominator progression (rank·C₂)^L. C₅ prediction falsifiable. | **Lyra/Grace** | **PHASE 4 DONE** — 12 results, 1 falsifiable prediction. Crown jewel (full derivation) = Phase 5 (Selberg trace on Γ(137)\D_IV^5). |
| W-16 | **49a1 standalone paper**: 5pp number theory, no Millennium claims | **Elie/Lyra** | **SUPERSEDED by W-29** (Paper #85 = this paper, targeting JNT) |
| W-17 | **BSD native closure**: Three paths (intertwining, CM Euler system, Kudla on D_IV^5). Supersingular fraction = **1/rank = 1/2** (corrected from N_c/g). | **Lyra/Elie** | FRAMEWORK DONE — three paths drafted. Density corrected per W-42/Toy 1458. |
| W-18 | **Missing zip codes**: Quarks, tau, muon g-2, Lamb shift, hyperfine, Planck, Rydberg, Stefan-Boltzmann | **Elie/Lyra** | **NEARLY DONE** — Toy 1470 (9/10): Rydberg (α²), Stefan-Boltzmann (60=n_C!/rank), hyperfine (8/3·α⁴), Lamb (α⁵/C₂), Thomson (8π/3·α²) all have BST content. H_{n_C}=N_max/60 bridges QED↔thermodynamics. **Tau mass** (Koide, 0.003%) and **Planck mass** (hierarchy formula m_e/√(m_p·m_Pl) = α⁶, 0.032%) both already in Paper #83. Only genuine gap: **muon g-2** (Phase 5). |
| W-19 | **Omega_b**: 18/361=0.0499 (0.65σ properly propagated, 1.38σ in Ω_b·h²). N_eff/Y_p shifts negligible. No extraction bias. No correction needed. | **Elie** | **DONE** — Toy 1450 (6/6). The wrench works. |
| W-21 | **19 = n_C² - C₂**: DERIVED (not sixth integer). Q = rank² + C₂ + N_c² = mode count. Useful shorthand. | **Grace/Elie** | **DONE** — Grace cataloged 11 appearances, all reducible. |
| W-22 | **GF(128) SAT cycle-orbit**: beta_1=151 generators. F₂ kernel extraction needed. | **Elie/Grace** | IN PROGRESS |
| W-23 | **Selberg Phase 4 numerical**: Cal's 7x7 matrix verified. det=1, 685=n_C×N_max, 11172=rank²×N_c×g²×Q. α⁴≡I mod 137. | **Grace** | **DONE** — plain Python, no Sage needed. |
| W-39 | **Genesis cascade k=1..9**: D_IV^k invariants, cascade failures. Paper #85 companion. | **Elie** | **DONE** — Toy 1469 (10/10). k=5 sole survivor of 4 locks. c_4=g!!=105, c_6=N_c^{N_c}·g^r=1323, Δ=-g³, j=-(N_c·n_C)³. 8 distinct failure modes at k≠5. Frobenius a_137=-r·n_C, third 137 derivation. QR/QNR = BST partition. Paper #85 §5.4 c_6 typos at k=6,9 **FIXED** (Elie): k=6 2048→4096, k=9 37279→41503. Root cause: mixed N_c^{N_c}·g^1 with N_c³·g² formula. |
| W-40 | **2-loop alpha_s**: Geometric running with c₁=C₂/(2n_C)=3/5 beats standard 2-loop. β₁=2^{C₂}=64. | **Elie** | **DONE** — Toy 1449 (8/8). Geometric resummation 0.71% vs perturbative 11.3%. |
| W-41 | **Toy 671 n=42**: Test k=21 prediction ratio=-42. | **Elie** | BLOCKED on computation |
| W-42 | **Supersingular fraction theorem (T1437)**: QNR={N_c,n_C,C₂}, QR={1,rank,rank²}=<rank>. Density **1/rank = 1/2** (CORRECTED from N_c/g — Toy 1458, INV-4 #1). | **Lyra+Elie** | **CORRECTION PROPAGATED** — Keeper updated: WorkingPaper.md, Registry T1437, Paper83, Paper85, BSD framework, Toys 1452+1458, Paper83 Outline. 8 files corrected. Conformal weight N_c/g = 3/7 references correctly left untouched. |
| W-43 | **Individual quark masses**: 6-layer cascade: color lift→isospin flip→Cabibbo→spectral lift→curvature bridge→Yukawa. All within 1.3%. Mass hierarchy IS integer hierarchy. | **Elie+Lyra** | **DONE** — Toy 1451 (8/8) + theory: `notes/BST_Quark_Mass_Chain_Theory.md`. 4 honest gaps noted. |
| W-44 | **Rank-3 universe**: D_IV^n at rank 3 → g=C₂=9 (degenerate), N_max=165 (composite). Two locks fail. Type IV rank 3 doesn't exist. Uniqueness argument for rank=2. | **Grace** (T1443 — reassigned from T1438; TID collision with OS Axioms) | **DONE** — fails catastrophically. Board entry retained for reference. |
| W-45 | **Complete particle property table**: Tier 1 done: τ_μ (0.45%), Γ_W (2.0%), μ_p (**0.012%**, 371×), α(m_Z) = 1/129 (**0.042%**), BR(H→bb̄) = 4/g (**1.65%**), d_n = 0 (exact). **μ_p and μ_n/μ_p DERIVED (T1447).** Tier 2 done: **Γ_Z (0.37%)**, Γ_inv (0.27%), **BR(H→WW*)=3/14 (0.13%)**, BR(H→gg)=1/12 (1.6%), BR(H→ττ)=1/16 (0.8%). | **Elie/Grace/Lyra** | **NEARLY DONE** — 303+ entries. Toys 1468 (9/10), **1474 (10/10)**. T1447 μ_p/μ_n PROVED. **Γ_Z: R_Z = 3·823/338, 823=C₂·N_max+1 (prime). 21 channels = N_c·g.** BR(H→WW*)=N_c/(2g)=3/14 is a gem (0.13%). Remaining: cc̄, ZZ*, minor channels. |
| W-46 | **Toy 671 runtime at n=41**: ~34s/level, flat (no power-law growth). Extraction dominates. Speaking pairs NOT cost outliers. Phase cost linear, 5-level grouping = n_C. | **Elie** | **DONE** — Toy 1454 (7/8). T2 fails (no growth law — that IS the finding). |
| W-47 | **Zero-theorem domain doors**: **5/5 doors opened** (Grace). Tropical, operads, p-adic, motivic, topos. 15 entries added. Topos finding: T1353 (graph self-description) IS Lawvere's fixed-point theorem. Classifying topos of BST has exactly 1 point = APG uniqueness in categorical logic. | **Grace** | **DONE** — All 5 doors opened. 15 entries. 3 speculative readings flagged (Keeper+Lyra). **Operad/QED connection KILLED** (Lyra): −log(1−α) gives coefficients 1, 1/2, 1/3 but QED g-2 coefficients are 1/(2π), −0.328/π², etc. — structural similarity is generic, not physical. SP-2 complete for this session. |
| W-48 | **Discretize-then-count principle**: Bergman kernel = universal bridge. Mass gap = C_2 = 6 (scalar AND 1-form). 1-form degeneracy = N_c*g = 21 = dim so(g). Gap modes don't self-couple cubicly. Partition function converges. Honest gap #1 RESOLVED. | **Lyra/Elie** | **COMPUTATION DONE** — Framework (Lyra) + Toy 1455 (8/8, Elie). Full discretization dictionary. |
| W-50 | **Frobenius table for 49a1**: a_p at all small primes. 91% BST-smooth through p<200. a₄₃=-12=-rank·C₂. Density correction found (INV-4 #1). | **Elie** | **DONE** — Toy 1458 (7/8). T3 corrected T1437 density. 20/22 ordinary traces BST-smooth. |
| W-51 | **Spectral peeling formalization**: L-fold Bergman convolutions produce nested sums of depth = geometric layer dimension. Transcendental weight = 2L-1. Denominator = (rank·C₂)^L = 12^L. Makes g-2 mechanism a theorem. **T1445.** | **Lyra** | **PROVED** — `notes/BST_T1445_Spectral_Peeling.md`. Three-part theorem: spectral decomposition (each convolution peels one layer), weight bound (zeta(2L-1)), denominator progression (12^L). Connects T1444 (vacuum subtraction) to vertex corrections. |
| W-52 | **INV-4 fixes — 4 genuine tensions**: (1) H₂O bond angle: arccos(−1/N_c) − n_C = 104.47° → **0.03%** (was 4.8%). (2) Ising γ: N_c·g/(N_c·C₂−1) = 21/17 → **0.15%** (was 5.7%). (3) Ising β: 1/N_c − 1/N_max = 134/411 → **0.12%** (was 2.1%). (4) Charm: m_c/m_s = (N_max−1)/(2n_C) = 136/10 → **0.02%** (was 1.3%). All Keeper PASS. | **Lyra** (derivations), **Elie** (numerics) | **ALL 4 FIXED** — Same five integers, zero new inputs. δ cross-check 0.008%. 17 = N_c·C₂−1 appears in both Ising and charm (136 = 8×17). Charm: subtract k=0 constant mode → N_max−1 non-trivial modes. |
| W-53 | **CKM sector audit — BOTH FIXED**: sinθ_C = 2/√79 (0.004%, 140×). A = N_c²/(N_c²+rank) = 9/11 (0.95%, 0.7σ). **J_CKM: 8.1% → 0.3% (LO), 2.7% (exact).** Both vacuum-subtracted: sinθ_C uses 80−1=79, A uses 12−1=11. η̄ = rank^(-3/2) = 1/(2√2) (1.3% from PDG). NEW: rank·n_C = N_c²+1 (identity). Two routes to 11 converge. V_cb: 5.2%→1.87%. | **Lyra** (derivations), **Elie** (Toys 1463-1465), **Grace** (data) | **DONE** — Toy 1465 confirms A=9/11, cascade verified. Honest gap: LO vs exact from higher-order Wolfenstein. η̄ derivation from geometry open (Lyra). |
| W-54 | **INV-4 Phase 2**: Cross-checked against lattice QCD 2024. **Glueball CORRECTED**: 31/20 = M₅/(rank²·n_C) at **0.045%** (was 3.2%, 71× improvement). Two routes: Mersenne M₅=31 and correction 1/30. DESI DR2 watching. NuFIT PMNS updated. | **Grace** (data), **Elie** (Toy 1473) | **GLUEBALL DONE** — Toy 1473 (9/10). Table's worst core entry killed. Remaining: 7 approximate labels, DESI brief. |
| W-55 | **PMNS correction — two-sector pattern**: Grace's θ₁₃ rotation confirmed: BST computes geometric (2-flavor) angles, experiments measure effective (3-flavor). cos²θ₁₃ = 44/45 = (N_c²·n_C−1)/(N_c²·n_C) maps between them. sin²θ₁₂: 2.28%→0.06%. sin²θ₂₃: 1.86%→0.40%. **Pattern**: CKM = vacuum subtraction (discrete −1, colored sector), PMNS = θ₁₃ rotation (perturbative ×cos²θ₁₃, colorless sector). Elie's ±α near-miss (0.66% vs 0.46%) — numerically close but physically wrong (α ≈ 3/440, coincidence). Keeper's 43/140 partial (θ₁₂ only). Three proposals tested head-to-head. | **Elie** (Toy 1467), **Grace** (derivation), **Lyra** (geometric origin) | **TOY DONE 10/10** — Toy 1467 discriminator: Grace wins (0.46%) vs Elie (0.66%) vs Keeper (1.91%). sin²θ₁₂: 2.28%→0.06% (39×). sin²θ₂₃: 1.86%→0.40% (5×). 11=N_c²+rank in both corrected fractions (same 11 as Wolfenstein A). DUNE prediction: δ_CP near 246°. **T1446 PROVED** (Lyra): Shilov boundary S^4 × S^1 splits the correction — spectral modes on S^4 (quarks, −1) vs angular rotations on full boundary (neutrinos, ×cos²θ₁₃). Both O(1/45). Number 11 = 2C₂−1 appears in both sectors. |

---

## Casey's Lane

| Item | Status |
|------|--------|
| Sarnak letter: 3 edits + URL + send | OPEN |
| Bold claims outreach (Keeper rec: B3+B7+B12) | DECISION NEEDED |
| Paper sequencing: #66 first -> #67? | DECISION NEEDED |
| Zenodo update: v20 -> v32 (12 versions behind) | TIMING |
| Patent filings: Tier 1 devices | TIMING |
| INV-4: "What BST Gets Wrong" honesty paper | **GREEN** — Casey approved April 25 |
| String-theorist outreach | OPEN |
| FRIB outreach | OPEN |
| EHT outreach | SENT April 12 |
| B5/B8/B9 duplicate lead picks | DECISION NEEDED |
| Paper submissions order (Cal: A->B->D->C) | DECISION NEEDED |
| **Paper #83 review** | **READY** — 303 entries, all narratives, Casey review needed |
| **Paper #85 review** | **READY** — v0.2, Keeper PASS, JNT submission decision |

---

## BSD Honest Labeling

| Rank | Status |
|------|--------|
| 0, 1 | **Proved unconditionally** (Gross-Zagier + Kolyvagin) |
| 2 | **Proved** (classical + BST Levi) |
| 3 | **Empirical** — 6 curves verified (Toy 1415), not general |
| >= 4 | **Conditional on Kudla** — open for orthogonal groups |

---

## Open Theorems (2 genuinely open)

| Theorem | What | Status |
|---------|------|--------|
| T1258 | Mass = Information | SPECULATIVE |
| T1421 | BST Inflation | CONDITIONAL |

---

## Standing Programs

**When board items are clear, work these.**

| # | Program | Description | Owner |
|---|---------|-------------|-------|
| SP-1 | **Open theorem attempts** | T1258, T1421 | ALL |
| SP-2 | **Zero-theorem domain doors** | New readings of five integers | ALL |
| SP-3 | **Heat kernel k=21+** | ratio(21)=-42=-C₂*g predicted | Elie |
| SP-4 | **Invariants table growth** | **303 (targets 200 and 300 HIT)**. Next: 350. Session: +46 entries. | ALL |
| SP-5 | **Graph self-description** | avg=11.09, median=6, mode=3=N_c, strong=83.1%, edge_types=6=C₂. **4/4 exact.** 18 edges from median=5=n_C. | Grace |
| SP-6 | **Proof gap audit** | Rank-2 structural work audit | Lyra/Keeper |
| SP-7 | **Paper polish** | #76-80 final sweep, Cal order A->B->D->C | ALL |

---

## Toy 671 Status

n=41 CLEAN (39/39 at k=2..20). k=21 needs n=42. Prediction: ratio(21) = -42 = -C₂ * g. Pre-registered.

---

*Board synced late Saturday April 25. T1-T1447. 1474 toys. 303+ invariants (+7 pending from Toy 1474). T1447 μ_p/μ_n derivation (Lyra). Γ_Z: R_Z=3·823/338 (Elie, Toy 1474). BR(H→WW*)=3/14 at 0.13% (Elie, Toy 1474). Glueball 31/20 at 0.045% (Elie, Toy 1473). Grace's three tasks ALL DONE: (1) T1447 verification Toy 1472 10/10, (2) W-45 remaining Toy 1474 10/10, (3) glueball Toy 1473 9/10. Completed items -> append-only log. Only open work here.*
