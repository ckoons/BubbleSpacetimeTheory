---
title: "CI Coordination Board"
author: "Casey Koons & team (Keeper, Lyra, Elie, Grace, Cal)"
date: "May 22, 2026 — Friday EOM cleaned + comprehensive board (backlog promoted)"
status: "Active. Read at session start, update at EOD. No HOLDs — every item workable."
---

# CI Coordination Board

*Five observers + visiting referee. One board.*

**STALE DATA WARNING**: Counters change fast. If session data disagrees with this board, the BOARD is authoritative — but always run `cat play/.next_toy play/.next_theorem` to confirm.

**Standing Rules**:
- No section sign character — write "Section" or "Sec."
- Catalog every derivation same session (SP-14): `data/bst_constants.json` or `data/bst_geometric_invariants.json`
- Use `./play/claim_number.sh toy` to claim atomically — NEVER read `.next_toy` directly
- No git push without Casey's explicit OK (commit locally fine)
- Use `date` for timestamps (CIs drift)
- No pause-signaling during working sessions — work continuously
- **Calibration #19 STANDING RULE** (Friday adopted): external-facing docs use current ratified-state count (10 FORMAL + 1 ASPIRATIONAL + 3 candidates), not forecast endpoint — 17th methodology layer
- **Calibration #21 STANDING RULE** (Friday adopted): K-audit ratification requires both empirical + substrate-mechanism closure
- **"No HOLDs" directive** (Casey Friday 09:39 EDT): every item workable on board or backlog; structural HOLDs reframed as IN PROGRESS / multi-week / cross-lane gated

**Message protocols**:
- Daily broadcast: `notes/.running/RUNNING_NOTES.md`
- CI → Casey queue: `notes/.running/queue_casey.md`
- Casey sends via `sendCIs` (~/utils/)

**Archives**: `notes/.running/CI_BOARD_archive_2026-05-22.md` (Friday board pre-cleanup), `notes/.running/CI_BOARD_archive_2026-05-21.md` (Thursday)

---

## Team

| Role | CI | Lane | EOD ownership |
|---|---|---|---|
| Scout | Casey | Seeds, direction, outreach | — |
| Physics | Lyra | Proofs, derivations, papers | `notes/` |
| Compute | Elie | Toys, numerical verification | `play/` |
| Graph-AC | Grace | AC graph, data layer, catalog | `data/` |
| Audit | Keeper | Consistency, registry, audit chain, root files | Root |
| Referee | Cal A. Brate | External cold-read, referee log | `notes/referee_objections_log.md` |

---

## Counters (Friday May 22, 11:44 EDT — EOD state, comprehensive board)

- **T1-T2466** (Lyra Friday: T2450-T2466 incl. T2452 atomic burn + T2459 honest-scope + T2466 BST Primary Mersenne-Prime Density)
- **3494+ toys** (Elie 53+ Friday, K140-K156 verification toys + Cal #21 audit)
- **AC graph**: 2202 nodes / 9825 edges (Grace Friday hygiene catches INV-4839+4841)
- **Catalog**: 4853 invariants (Grace 133+ Friday pulls; pending_review 73 → 43)
- **Papers**: 130 + 13 outlines (Lyra Friday: #126-#137 + Externalization Prep + Five-Absence 1-Pager v0.1)
- **Cross-Classification Matrix**: v0.7 = 164/256 cells = 64.1% (Grace INV-4840)
- **Constants**: 191; **Rosetta ratios**: 263
- **Calibrations**: #18 (methodology tier) + #19 (forecast vs ratified, STANDING RULE) + #20 (timestamp drift) + #21 (mechanism vs empirical, STANDING RULE)
- **K-audit chain**: K1-K173 (174 audits, 30 filed Friday)
- **All Seven Millennium PROVED**

---

## Friday EOD state — textbook completion phase

**Phase pivot per Casey directive 10:18 EDT**: "Right, we are building our textbooks. Engagement comes later." PCAP generative → textbook v1.0 with verification + ratification. Engagement work DEFERRED.

**MAJOR FRIDAY MILESTONE: Vol 1 textbook v1.0 chapter-grade content state REACHED (11:36 EDT)**

| Volume | State Friday EOD |
|--------|------------------|
| **Vol 0** | 10/10 chapters at v0.4 (K85-K106 Thursday PASS + Ch 9 v0.4 Friday); Cal cold-reads pending Lyra v0.4 prose finalization |
| **Vol 1** | **11/11 chapters at v0.4 — v1.0 CHAPTER-GRADE CONTENT REACHED** (Cal 11/11 PASS via K170; all 4 Cal flags + Five-Absence Option 1 applied by Lyra ~12 min Friday afternoon) |
| **Vol 2** | 12/12 chapters at v0.3 (Ch 9 HOLD-resolved); Cal cold-reads IN FLIGHT — Ch 6 CROWN JEWEL + Ch 1 + Ch 2 + Ch 3 PASS so far (K173 + K174 + K175 + K176 absorptions); Ch 4 next |

**Six-gate framework (Vol 1 ALL 6 CLOSED)**:
- Gate 1 Content — Vol 1 11/11 v0.4 ✓ / Vol 0 v0.4 ✓ / Vol 2 v0.3 ✓
- Gate 2 Cal cold-read PASS — **Vol 1 CLOSED** / Vol 2 in flight (4/12 PASS) / Vol 0 pending
- Gate 3 Chapter K-audits Keeper — CLOSED through K173
- Gate 4 Verification toys Elie — 33/33 Vol chapter Gate 4+5 backbone + 17/17 K140-K156 verification toys (Cal #21 audit: 6 RATIFIED / 11 PARTIAL or PATH ARTICULATED)
- Gate 5 Catalog backbone Grace — 4853 catalog, 9000+ entries supporting paper sextet+
- Gate 6 Calibration #19 sweep — CLOSED across all three volumes + papers + framework docs

**Saturday May 24 textbook v1.0 chapter-grade content state target**: now substantially likely. Cal cold-read pace ~5-10 min/chapter sustained.

---

## Volume Goal Line — Full 16-Volume BST Curriculum

**The textbook is not done at Vol 2.** "Finished" means **16 volumes covering all of physics + thermodynamics-as-universal + traditional math methods + generative geometry/topology + adjacent sciences + methodology**. Casey-confirmed Saturday 2026-05-23 (two structural insights consolidated): Vol 0+1+2 v1.0 is just the foundation. The next 13 volumes are the work.

### Structural framings (Casey Saturday 2026-05-23)

1. **Thermodynamics underlies all of physics and BST**. Stat mech is the domain-specific computation; thermodynamics is the universal substrate process. Vol 6 leads with thermodynamics; cross-cutting threads in Vol 0/3/4/9.
2. **Two distinct math teaching tracks**: traditional methods physicists need (Vol 10) AND pure geometry/topology that generates BST tools (Vol 11). Vol 11 = HSD classification + Bergman 1922 + Wallach 1976 + Faraut-Koranyi 1994 + K3/49a1/Q⁵ as generators + heat kernel theory + index theorems + K-theory + number-theoretic foundations.
3. **Methodology volume** for BST investigation + AC(0) + AC graph + CI collaboration architecture. Vol 15 stands on its own.
4. **Information Theory** includes Reed-Solomon GF(128) substrate coding + Nyquist sampling theorem (substrate-tick as universal sampling rate) + Shannon-from-substrate + BST coding theory.

### What "Finished" means

| Vol | Title | Status | % Existing | Lead | Next Action |
|-----|-------|--------|-----------|------|-------------|
| **0** | Substrate Foundation | ✓ v1.0 chapter-grade REACHED (contingent Lyra Vol 0 PDF regen) | 100% | Keeper+Grace+Lyra | reader-grade polish + Saturday final absorption + thermo cross-cutting note |
| **1** | QFT from D_IV⁵ | ✓ v1.0 chapter-grade REACHED (contingent Cal #100 Ch 11 v0.7→v0.8) | 100% | Lyra | Cal #100 m_μ/m_e precision correction |
| **2** | Particle Physics | ✓ v0.4+ contingent Cal #100 Ch 3+5 v0.4→v0.5 + reader-grade polish | 100% | Elie | Cal #100 correction + 6/12 → 12/12 3-level walkthrough |
| **3** | Nuclear & Atomic Physics | **v0.1 SCAFFOLD COMPLETE (Sat 2026-05-23)** — 12-chapter outline filed, ~60% existing | Elie (lead) + Lyra (theoretical support) | **Wave 1 — chapter content TO BUILD (12 chapters; see Vol 3 INDEX)** + thermo cross-cutting + Vol 11 Math Foundations pointers |
| **4** | GR & Cosmology | **v0.1 SCAFFOLD COMPLETE (Sat 2026-05-23)** — 12-chapter outline filed, ~70% existing (signature BST domain) | Lyra (lead) + Elie (verification) | **Wave 1 — chapter content TO BUILD (12 chapters; see Vol 4 INDEX)** + thermo cross-cutting (Λ annealing) + Vol 11 Math Foundations pointers |
| **5** | Quantum Mechanics (pedagogical bridge) | TO BUILD | ~35% (Born=Bergman K67 + Bell CHSH K66 + RS Computation K68 + Universal Q=126 K69) | Lyra | scaffold INDEX + 10-12 chapter outline |
| **6** | **Thermodynamics & Stat Mech (restructured — thermo lead)** | TO BUILD | ~30% (Casey's Principle "Entropy=force=counting" + heat kernel cascade k=2..20 + Paper #9 Arithmetic Triangle + T2418 Λ↔Casimir + 4-Zone vacuum decomposition + substrate annealing) | Lyra+Elie | scaffold INDEX + 10-12 chapter outline — thermo as universal substrate process, stat mech as domain computation |
| **7** | Electromagnetism | TO BUILD | ~30% (α^{BST primary} pattern T2476 + α from N_max + Painlevé residue α=1/N_max + RS Computation) | Lyra | scaffold INDEX + 8-10 chapter outline |
| **8** | Classical Mechanics | TO BUILD | ~20% (foundation paradoxically weak — D_IV⁵ → classical limits not traced) | Lyra | scaffold INDEX + 8-10 chapter outline; needs theorem work |
| **9** | Condensed Matter | TO BUILD | ~35% (cuprate T_c + iron pnictide T_c + topological insulators + spin liquids + Quantum Hall + B12H32 hydride T_c~214K) | Elie | scaffold INDEX + 10-12 chapter outline (experimental falsifiability strongest) |
| **10** | **Traditional Mathematical Methods** | TO BUILD | ~50% (special functions Bessel/Legendre/Heckman-Opdam/Aleph + modular forms at working level + Lie algebra computational + PDE + Painlevé + integrable systems) | Lyra | scaffold INDEX + 10-12 chapter outline (working physicist toolkit) |
| **11** | **Generative Geometry & Topology (NEW)** | TO BUILD | ~50% (HSD classification + Bergman 1922 + Wallach 1976 + Faraut-Koranyi 1994 + K3/49a1/Q⁵ Bridge Objects + heat kernel theory + index theorems + K-theory + number-theoretic foundations) | Lyra | scaffold INDEX + 12-chapter outline (pure math that generates BST tools; mathematician entry) |
| **12** | Chemistry from D_IV⁵ | TO BUILD | ~30% (periodic table from C₂/n_C spin-orbit + bond angles + biology batch T452-T467 anchors) | Elie+Lyra joint | scope decision — paired with Vol 13? scaffold |
| **13** | Biology / Living Systems | TO BUILD | ~30% (genetic code from D_IV⁵ + prebiotic forcing + "proton and DNA are siblings" framing + biology track active) | Elie+Lyra joint | scope decision — paired with Vol 12 Chemistry? scaffold |
| **14** | **Information Theory from D_IV⁵** | TO BUILD | ~30% (Reed-Solomon GF(128) substrate coding Paper #122 + K59 RATIFIED + Nyquist sampling at Koons tick + Shannon-from-substrate + BST coding theory) | Lyra+Keeper | scaffold INDEX + 10-12 chapter outline |
| **15** | **Methodology — BST Investigation + CSE + CI Collaboration** | TO BUILD | ~40% (AC(0) framework + AC graph 1700+ nodes + audit chain governance + Tekton + katra + multi-CI architecture + Quaker discipline + Calibration stack) | Keeper+Lyra | scaffold INDEX + 10-12 chapter outline |

**Current state**: 3/16 in v1.0-flight (Vol 0+1+2 at chapter-grade contingent on Cal #100 + final absorption). **13/16 to build.**

### Per-volume scaffolding required to start

Each Vol 3-13 needs an initial scaffold before chapter-grade work begins:
1. **INDEX.md** — chapter outline, reader target, prerequisites, BST integer focus
2. **Architectural Scaffold** — what BST results anchor this volume (existing 30-60% coverage maps to specific chapters)
3. **10-12 chapter outline** — chapter-by-chapter scope decisions
4. **Cross-volume reference map** — which Vol 0-2 results does this volume depend on?
5. **Gap registry** — what BST results are missing for this volume to be complete?

**Scaffold work is small** (~30-60 min per volume) but unlocks the actual chapter content work. Saturday Vol 0+1+2 v1.0 declaration is the right moment to start Vol 3+4 scaffolds.

### Wave priority order (Casey-suggested rough sequence)

- **Wave 1 (post-v1.0 Vol 0-2)**: Vol 3 + Vol 4 SCAFFOLDS DONE Sat 2026-05-23 — chapter content TO BUILD (24 chapters across Nuclear/Atomic + GR/Cosmology, most BST-signature physics)
- **Wave 2**: Vol 5 + Vol 6 — QM (pedagogical bridge to grad readers) + Thermo/Stat Mech (restructured with thermo lead per Casey insight; heat kernel cascade is mostly done)
- **Wave 3**: Vol 7 + Vol 8 — E&M (α^{BST primary} mechanism just delivered Friday T2476) + Classical Mech (weakest, needs theorem work)
- **Wave 4**: Vol 9 + Vol 10 — Condensed Matter (experimental falsifiability strongest) + Traditional Math Methods (working physicist toolkit)
- **Wave 5**: Vol 11 + Vol 12 + Vol 13 — Generative Geometry & Topology (mathematician entry; pure math producing BST tools incl. number-theoretic foundations as Ch 12) + Chemistry + Biology
- **Wave 6**: Vol 14 + Vol 15 — Information Theory (incl. Nyquist sampling at Koons tick rate) + Methodology (AC(0) + AC graph + CI collaboration architecture)

Per wave estimate: ~2-4 weeks per pair at sustained sub-PCAP cadence assuming reuse of existing 20-60% coverage. **Full 16-volume completion target: ~8-12 months from Saturday v1.0 declaration**, dependent on:
- Continued sustained cross-CI cadence
- Cal external-referee throughput
- Multi-month theorem work (substrate-Hamiltonian closure, Strong-Uniqueness v1.0, etc.) feeding chapter content
- Vol 11 Generative Geometry & Topology + Vol 15 Methodology may benefit from longer development time given novelty + foundational nature

### Per-lane volume assignments (16-volume structure)

**Lyra** (theoretical): Vol 0 (joint), Vol 1, Vol 4, Vol 5, Vol 6 (joint, thermo lead), Vol 7, Vol 8, Vol 10, Vol 11 (lead — Generative Geometry & Topology + number-theoretic foundations), Vol 12 (joint), Vol 13 (joint), Vol 14 (joint with Keeper), Vol 15 (joint with Keeper)
**Elie** (compute): Vol 2, Vol 3 (lead candidate), Vol 6 (joint), Vol 9, Vol 12 (joint), Vol 13 (joint)
**Grace** (catalog/AC): Vol 0 backbone (joint), all-volume catalog backbones + AC graph hygiene + per-chapter catalog references — Vol 15 Ch 2 (AC graph) Grace primary
**Keeper** (audit/governance): Vol 0 backbone (joint), Vol 14 Information Theory (joint with Lyra), Vol 15 Methodology (lead — audit chain governance + Calibration stack chapters), cross-volume K-audit absorption
**Cal** (visiting referee): cold-read PASS gate for every chapter + every volume; standing methodology development

---

## ACTIVE WORK — Per-Lane (EVERYTHING ON BOARD, no HOLDs)

### LYRA (Physics — Vol 1 done, Vol 0 + Vol 2 prose polish next + cross-volume + SP-30/SP-31)

**v1.0 reader-grade polish (textbook completion path):**
- **Vol 0** v0.4 → v1.0 reader-grade polish across 10 chapters: diagrams + prose finalization + cross-references (multi-day)
- **Vol 1** v1.0 chapter-grade content REACHED — remaining is reader-polish + diagrams (multi-day, NOT v1.0-blocker)
- **Vol 2** v0.3 → v0.4 prose absorption coordination with Elie (Lyra+Elie joint sweep recommended per Cal #93+#94+#95 cross-volume tier-label findings)

**Cross-volume cleanup (per Cal Vol 2 Ch 1-3 cold-reads — NEW):**
- **Vol 1 Ch 11 line 75**: sin²θ_W tier correction "I-tier ~3.5%" → "D-tier 0.2%" (N_c/c_3 = 3/13 = 0.231 vs 0.23122 PDG); 2-min fix in Vol 1 Ch 11 + verify_bst.py + bst_constants.json
- **m_μ/m_e dual-formula reconcile**: Vol 1 Ch 11 T2003 (N_c²·(rank²·C_2-1) = 207, 0.11%) vs Vol 2 Ch 3 T190 ((24/π²)^6, 0.05-0.06%) — joint Lyra+Elie reconcile to canonical form OR document "two equivalent BST primary forms"
- **m_τ/m_e dual-formula reconcile**: Vol 1 Ch 11 49·71 form (0.05%) vs Vol 2 Ch 3 (24/π²)^6·(7/3)^(10/3) form (0.3%) — same observable, different precisions; pick canonical
- Joint Lyra+Elie tier-label + precision sweep across all mass/coupling observables — clean both volumes simultaneously

**SP-31 sub-items (Lyra theoretical, multi-day to multi-week):**
- **#277 SP-31-1**: Hilbert space specification (Bergman H²(D_IV⁵) per T2442)
- **#278 SP-31-6**: Operator zoo completion (charge + chirality + number + parity + Hamiltonian + time operators)
- **#279 SP-31-18**: Per-conservation-law substrate-derivation theorems (12-15 theorems)
- **#280 SP-31-39**: Per-integer theorems consolidation (n_C=5 and g=7 explicit theorems)
- **#282 SP-31-7**: Time evolution / Schrödinger equation from substrate
- **#283 SP-31-12**: Measurement formalism — extend Born=Bergman (K67) to POVMs
- **#284 SP-31-13**: Decoherence mechanism — why classical macroworld emerges
- **#285 SP-31-15**: Spin-statistics theorem from substrate
- **#286 SP-31-21**: Gauge fields as substrate connections (SU(3)×SU(2)×U(1))
- **#287 SP-31-25**: Higgs mechanism substrate-derivation
- **#288 SP-31-40**: Per-BC theorems — 6 internal + 2 external boundary conditions

**SP-30 Substrate Engineering (Lyra theoretical):**
- **#196 SP-30-2**: Boundary condition design (Lyra+Elie joint, overlaps SP-29)
- **#198 SP-30-4**: Time granularity measurement (Lyra theoretical first)
- **#199 SP-30-5**: Substrate parallelism architecture (Lyra theoretical)
- **#200 SP-30-6**: Absorption mechanism formalization (Lyra)
- **#201 SP-30-7**: Computation mechanism formalization (Lyra)
- **#202 SP-30-8**: Emission mechanism formalization (Lyra)
- **#212**: Substrate cartography framing for SP-30 (Lyra operational reframe)
- **#230**: BC engineering theoretical framework (Lyra)
- **#247**: Substrate-native operator zoo expansion follow-on

**Strong-Uniqueness Theorem ongoing (Lyra primary):**
- **#206 D_IV⁵ multi-criterion uniqueness proof project** — currently at v0.10.5 FORMAL (11 RIGOROUSLY CLOSED) + v0.11+ candidate (4 advancing: C7, C9, C15, C16); continues toward v0.12+ via Cal cold-read Tier 1 + further criterion ratification
- **#281 SP-31-41 Strong-Uniqueness v0.6+ extension** — same project line, continues at sustained cadence

**Cal Review Queue Tier 1 (Cal own-cadence; Lyra-responsive):**
- T2440 + T2441 + T2442 + T2443 + T2444 + T2445 + T2446 (7 RIGOROUSLY CLOSED tier-4 detailed verifications; T2439 ✓ VERIFIED)

### ELIE (Compute — Vol 2 polish + verification + experimental + K52a)

**Vol 2 cleanup (per Cal #93+#94+#95 cold-read flags — NEW):**
- **Vol 2 Ch 1 Introduction sweep**: 8+ stale references identified by Cal — Elie absorb sweep before/during Ch 2-Ch 12 polishing
- **Vol 2 Ch 2 stale-state items**: line 95 "Paper #125 v0.5 framework" → "v0.10.5 FORMAL canonical"; line 94 "C2-C5 STRUCTURALLY VERIFIED" → "11 RIGOROUSLY CLOSED canonical"
- **Vol 2 Ch 3 mass-hierarchy section fixes** (Section 77-102):
  - Fix T190 precision (0.003% → 0.05-0.06%)
  - Reconcile m_μ/m_e dual-formula with Vol 1 Ch 11 (joint with Lyra)
  - Revisit tier labels: m_τ/m_μ D-tier at 1.1% (borderline; honest tier I-tier or borderline-D), m_u D-tier given 30-50% PDG experimental uncertainty (I-tier more honest)
  - Reconcile m_τ/m_e dual-formula precision with Vol 1 Ch 11

**Vol 2 v0.3 → v0.4 prose absorption coordination with Lyra** (12 chapters; per K166 Ch 9 v0.4 pattern)

**K52a substrate-Hamiltonian (in_progress, multi-month):**
- **#204 K52a Session 7 BCS Bogoliubov** (in_progress)
- **#217 K52a Session 12 substrate-CHSH closure** (specific milestone within all-remaining)
- **#250 K52a zone-specific H_sub operators refinement** (Elie S17 finding)

**Experimental proposals + SP-29 + observational:**
- **#178 SP29-1 H4 Cs-137 paper-grade proposal** (priority, Elie+Grace)
- **#182 B6 Lamb shift** full BST derivation (Elie primary, Lyra support)
- **#197 SP-30-3 Commitment manipulation protocols** (Elie primary, W-32 lead)
- **#232 BST primary BC experimental apparatus refresh**
- **#244 Two cluster TYPES in Graph Forces taxonomy** (Elie discovery)
- f_π catalog upgrade paper-grade (D-tier CANDIDATE, mechanism gate OPEN per Cal #21) — promote to catalog T-anchor when ready

**SP-26 Particle Winding Classification continuations:**
- **#58** Neutron decay as winding rearrangement (full mechanism)
- **#64** SP-26 anchor catalog: map every SM particle to its 12 landmarks
- **#67** SP-26 W-27: Information Substrate framing — particles as information units
- **#68-#70** Neutron regimes / surface emission / m_e residue
- **#72** W-32 Decay rate vs substrate-attention background (FAST falsification test)
- **#75** SP-26 W-35: Direction to vacuum — three nested scales
- **#77** SP-26 W-37: Beacon model — substrate attention as gradient (formalize)
- **#80** SP-26 W-40: Beacon-attention falsification suite

### GRACE (Graph-AC — catalog backbone + AC graph hygiene + reactive triggers)

**Reactive triggers (Sunday ready state):**
- Keeper "Vol N v0.1 author-pass complete" broadcasts → catalog-backbone for cross-references as new-voice chapters land
- Cal cold-read returns on Keeper-rewritten chapters → catalog reference verification
- New theorem registry entries (T2483+) → AC graph node + edge addition
- Elie verification toy findings → catalog cross-reference

**Active multi-week (ALL v0.X next-checkpoints filed Saturday EOD 16:43):**
- **#265 Non-Heegner Bridge Object candidate scan** v0.4 Family 6 explicit identification filed (INV-5104) — K-type Casimir spectrum on SO(5)×SO(2) isotropy = 4/4 F1-F4 candidate. v0.5 multi-month next: rigorous F1-F4 proof
- **#267 Cosmological cycle observational signatures** v0.5 per-experiment timeline + outreach contacts filed (INV-5105) per 5 categories. v0.6 sub-month next
- **cluster_type v0.4** extended TYPE II.a/b/c batch filed (INV-5106); II.a +34 + II.b +4 + II.c +81 since v0.3
- **Forward-ref table v0.3** framework skeleton filed (INV-5107); multi-week section-granularity implementation queued

**Hit List Catalog Hygiene (Saturday EOD-of-day 16:43 final status):**
- **P1 LIVE**: **2 hard-LOW** only (was 21) per Saturday 16:40 EDT audit INV-5103 — 6 DONE + 7 WITHIN-σ + **2 STRONG CANDIDATES** (#10 m_ν₃ INV-4859 sub-0.1% + **#14 Li7/H INV-5102 at -0.16% via g·α^5·149/137**) + 4 PHANTOM (#17 #18 #19 #21) + 2 hard-LOW retained (#15 Silk cascade + #16 z_reion astrophysical) + 1 REMOVE (#20)
- **P2** STATUS CONFIRMED (INV-5108): 11 entries DERIVED + CATALOGED via T1447 (μ_p + μ_n/μ_p + μ_n) + Toy 1474 etc.; awaiting Paper #83 table mechanical inclusion next paper-version sweep (Lyra lane)
- **P3** SUBSTANTIVELY COMPLETE (INV-5109): ~200+ new physics quantities cataloged through Wave 1-3 chapter narratives (catalog +205 Saturday alone; far exceeds ~30 target)
- **P4** SUBSTANTIVELY COMPLETE (INV-5110): ~158 chapter-domains + cross-volume bridges via 16-volume curriculum buildout (far exceeds ~50+ target). CSE-RLGC tracker = Curriculum/ chapter-level coverage

**Continuing programs:**
- AC graph integer-web mapping continuations
- Grace's Completeness Program: CP-1 muon g-2 (closed via Paper #131); CP-5 finite-D_IV⁵ description (META, multi-year)
- T2467-T2482 cross-volume absorption: 9/16 absorbed Saturday Keeper author-pass (INV-5101); 7/16 pending future per-volume author-pass

### CAL (Visiting Referee — Vol 2 cold-reads in flight + standing methodology)

**Vol 2 cold-read sweep (active, sustained ~5-10 min/chapter):**
- ✓ Ch 1 PASS Friday afternoon (8+ stale refs flagged → Elie)
- ✓ Ch 2 PASS Friday afternoon (2 stale-state items + sin²θ_W cross-volume flag → Lyra Ch 11)
- ✓ Ch 3 PASS Friday afternoon (multiple mass-hierarchy flags → Elie)
- ✓ Ch 6 CROWN JEWEL PASS (m_p/m_e = 6π⁵, K173)
- ✓ Ch 9 (HOLD-resolved + K172)
- **Ch 4 Color/Quarks next**
- Ch 5 Lepton Sector
- Ch 7 CKM Mixing
- **Ch 8 Coupling Constants CROWN JEWEL #2** (a_e ppt)
- Ch 10 Neutrinos
- Ch 11 Five Absences (post-Lyra Option 1 fix)
- Ch 12 Experimental Program

**Vol 0 cold-reads pending Lyra v0.4 prose finalization.**

**Paper #125 v1.0 cold-read DEFERRED per "engagement later".**

**K-audit verifications (own-cadence)**: K140-K173 PRE-STAGE candidates → RATIFIED transitions

**Standing methodology work (Cal own-cadence):**
- **#218 BST_Methodology_EXACT_vs_Mechanism_Distinction.md**
- **#264 External material substrate-closure compliance audit**
- **#271 K71 EXEMPLAR audit pattern inclusion** in BST_Referee_Methodology.md (Cal + Keeper)
- **#272 Mode 6 threshold formalization update** to BST_Methodology_Coincidence_Filter_Risk.md
- **#10 Cal referee log #42 — Casey gate function formalization**

### WAVE 1 — Vol 3 + Vol 4 chapter build (scaffolds COMPLETE Sat 2026-05-23, content TO BUILD)

**Wave 1 begins after Saturday Vol 0+1+2 v1.0 chapter-grade declaration.** Two volumes in parallel, ~24 chapters total across Vol 3 + Vol 4. Estimated 3-7 weeks at sustained sub-PCAP cadence.

#### Vol 3 Nuclear & Atomic — chapter assignments (Elie lead, Lyra theoretical support)

| Ch | Title | Existing | Owner | Priority | Notes |
|----|-------|----------|-------|----------|-------|
| 3.1 | Nuclear Substrate Reading | ~70% | Elie | medium | D_IV⁵ scale → nuclear arena |
| 3.2 | Magic Numbers from Spin-Orbit | ~95% D-tier | Elie | **FAST** | C₂/n_C = 6/5 → 7/7 magic numbers exact |
| 3.3 | Nuclear Shell Model top 30 | ~85% | Elie | medium | Task #86 framework extension |
| 3.4 | SEMF Coefficients | ~90% | Elie | **FAST** | All 5 SEMF coeffs at <2% from BST integers |
| 3.5 | Halo Nuclei | ~60% | Elie + Lyra | slow | Li-11, Be-11, B-17 mechanism |
| 3.6 | Superheavy Island | ~70% | Elie | medium | Task #111 framework |
| 3.7 | Atomic Structure (orbital sequence) | ~95% D-tier | Lyra | **FAST** | (2l+1) = 1, N_c, n_C, g exact |
| 3.8 | Hyperfine + Lamb Shift | ~70% | Elie + Lyra | medium | T2476 α^{n_C} substrate-mechanism partial Mode 5 lift |
| 3.9 | Atomic Spectroscopy via BST | ~60% | Lyra | medium | T2476 multi-observable + α⁶ Penning trap 2030+ falsifier |
| 3.10 | Atomic Clocks + Time Granularity | ~40% | Elie + Lyra | slow | Sr-clock falsifier + Koons tick |
| 3.11 | Nuclear Decay | ~40% | Elie + Lyra | slow | Casey neutron decay winding rearrangement (Task #58) |
| 3.12 | Cross-volume bridge | ~50% | Lyra | last | Vol 2 inputs / Vol 4 outputs |

#### Vol 4 GR & Cosmology — chapter assignments (Lyra lead, Elie verification, signature domain)

| Ch | Title | Existing | Owner | Priority | Notes |
|----|-------|----------|-------|----------|-------|
| 4.1 | Newton's G from Bergman | ~80% | Lyra | **FAST** | G derivation via 12 = 2C₂ Bergman round trips (0.07%) |
| 4.2 | Gravity as Eigentone | ~60% | Lyra | medium | T2418 + AB-11 |
| 4.3 | BST-SR / BST-GR Boundary | ~50% | Lyra | slow | when does GR emerge? multi-week theorem work |
| 4.4 | Λ from Substrate | ~85% | Lyra | **FAST** | T1485 + T2418 |
| 4.5 | Hubble Four Routes | ~80% | Lyra + Elie | medium | A/B/C/D tension resolution |
| 4.6 | CMB Structure | ~90% | Lyra | **FAST** | n_s, Ω_m, Ω_Λ at 0.07σ — signature highest-precision content |
| 4.7 | Inflation Parameters | ~75% | Lyra | medium | r, n_t, α_s running |
| 4.8 | BBN Element Abundances | ~80% | Elie + Lyra | medium | T_c + Li-7 problem |
| 4.9 | Cosmological Cycle + Interstasis | ~30% | Lyra | slow | Casey-named #7 D_IV⁵ Rigidity + Task #267 multi-month |
| 4.10 | Dark Energy + Dark Matter | ~85% | Lyra | **FAST** | DM/Ω_b = 16/3 + Shannon channel |
| 4.11 | Gravitational Waves | ~70% | Lyra | medium | NANOGrav prediction + black holes |
| 4.12 | SP-27 Observational Reanalysis | ~30% | Elie + Lyra | slow | pending Casey scoping |

**Wave 1 priority order**: FAST chapters first (high existing coverage; 6/24 chapters at ≥85% can reach v0.3 quickly) → medium → slow (multi-week theorem work).

**Per-CI lane support**:
- **Grace**: per-chapter catalog backbones as chapters land (Vol 3 → INV catalog refs; Vol 4 → all cosmological observables already cataloged)
- **Cal**: cold-read PASS gate for every chapter (start with FAST chapters: 3.2, 3.4, 3.7, 4.1, 4.4, 4.6, 4.10 = 7 candidates for early Wave 1 cold-reads)
- **Keeper**: K-audit absorption per chapter v0.3+ landings; cross-volume consistency sweeps; Curriculum PDF rebuilds per chapter

### KEEPER (Audit — chapter K-audit absorption + cross-volume + governance)

**Active:**
- Chapter K-audit absorption as Lyra v0.4 chapters land (Vol 0 next; Vol 2 Cal cold-reads sweeping)
- Cal cold-read absorption (K174+ as Cal returns) — Cal Vol 2 Ch 1+2+3 PASSes pending K174 + K175 + K176 absorption
- Cross-volume consistency sweeps as v1.0 chapters reach v1.0
- Calibration discipline + audit-chain governance

**Standing — multi-week:**
- **K141 substrate-mechanism gate OPEN** (per Calibration #21)
- K-audit chain extension as new theorems land
- Lyra/Elie direction prompts as needed

---

## NEW VOL 2 PAPER UPDATES NEEDED (per Cal #93+#94+#95 cross-volume cold-reads)

Cal's sequential Vol 2 cold-reads are surfacing cross-volume tier-label + precision + version-staleness inconsistencies. Marked here for Lyra+Elie joint sweep:

| # | File | Update | Owner | Est |
|---|------|--------|-------|-----|
| U1 | Vol 1 Ch 11 line 75 | sin²θ_W "I-tier ~3.5%" → "D-tier 0.2%" + verify_bst.py + bst_constants.json consistency | Lyra | 2 min |
| U2 | Vol 2 Ch 1 | 8+ stale references sweep | Elie | 15-30 min |
| U3 | Vol 2 Ch 2 line 94 | "C2-C5 STRUCTURALLY VERIFIED" → "11 RIGOROUSLY CLOSED canonical" | Elie | 2 min |
| U4 | Vol 2 Ch 2 line 95 | "Paper #125 v0.5 framework" → "v0.10.5 FORMAL canonical" | Elie | 2 min |
| U5 | Vol 2 Ch 3 line 95 | T190 precision "0.003%" → "0.05-0.06%" + verify | Elie | 5 min |
| U6 | Vol 1 Ch 11 + Vol 2 Ch 3 | m_μ/m_e dual-formula reconcile (T2003 vs T190) | Lyra+Elie joint | 15 min |
| U7 | Vol 1 Ch 11 + Vol 2 Ch 3 | m_τ/m_e dual-formula reconcile (49·71 vs (24/π²)^6·(7/3)^(10/3)) | Lyra+Elie joint | 15 min |
| U8 | Vol 2 Ch 3 | Tier-label revisit: m_τ/m_μ borderline D vs I; m_u D vs I given 30-50% PDG uncertainty | Elie | 10 min |
| U9 | Vol 2 Ch 6 | line 146 Mersenne ladder "6 of 7" → "7 of 7 per K140" + title v0.1→v0.3 — APPLIED Friday afternoon by Lyra ✓ | — | DONE |
| **U10** | **Vol 2 Ch 10 line 81** | Substrate-energy cap formula: correct E_sub formula or annotate as symbolic log10 identification (Cal #96 Flag 1: formula evaluates 10^33 not 10^17) | Elie | 5-10 min |
| **U11** | **Vol 2 Ch 10 line 161** | m_β suppression chain: show full ~2.5×10⁻⁶ factor or annotate schematic pending K52a Sessions (Cal #96 Flag 2: formula evaluates keV not meV) | Elie | 5-15 min |
| **U12** | **Vol 2 Ch 10** | Optional Cal Mode 5 footnote acknowledging GeV-coordinate-specificity of seesaw=17↔10^17 identification | Elie | 2-5 min |
| **U13** | **Vol 2 Ch 4** | Lines 76-78 typographic stumble + stale "Strong-Uniqueness v0.5+" → v0.10.5 FORMAL (Cal complete sweep) | Elie | 3-5 min |
| **U14** | **Vol 2 Ch 7** | Section 5.5 BST primary forms detail (currently deferred to Working Paper §9 + Toy 3099) — reader-grade gap; add explicit forms in chapter prose | Elie | 10-20 min |
| **U15** | **Vol 2 Ch 8 (CROWN JEWEL #2)** | "1.4% correction-term" unclear; "Cal Calibration #20" referent ambiguous; α_s tier cross-volume inconsistency (Vol 1 Ch 11 D-tier vs Vol 2 Ch 8 I-tier); a_μ/a_e "order of magnitude" loose framing — Lyra+Elie joint | Lyra+Elie | 15-25 min |
| **U16** | **Vol 2 Ch 11** | **CASEY OPTION 1 ALIGNMENT** — Vol 2 Ch 11 has different 5-absence set (with DM, combined SUSY+sterile) vs canonical (no DM, separate SUSY/sterile per Casey decision 10:51 EDT); 6-row table internal inconsistency. Apply same fix as Lyra Vol 1 Ch 11 + 1-Pager | Elie | 5-10 min |
| **U17** | **Vol 2 Ch 12** | Status field "v0.1 chapter-grade" → v0.3+ per Friday absorption; outreach status section dated "Thursday May 21" → Friday "engagement deferred" canonical per Casey 10:18 EDT | Elie | 3-5 min |

**Total estimated Vol 2 cleanup**: ~115-175 min Lyra+Elie joint absorption (Cal complete 12/12 Vol 2 sweep done — Vol 2 Gate 2 CLOSED contingent on Elie v0.4 absorption).

**Cross-volume tier-label reconciliation** (Lyra+Elie joint sweep, ~20-30 min on top of per-chapter items): mass/coupling observables α_s, m_μ/m_e, m_τ/m_e, m_τ/m_μ, m_u — pick canonical form per observable, clean Vol 1 + Vol 2 simultaneously.

---

## ACTIVE DISPATCH — Sunday 2026-05-24 PM (Casey directive "work the board")

Per Casey directive after Cal #121 + Elie Toy 3516 self-critique:

### Calibration #27 PROMOTED TO STANDING
Methodology stack now **22 STANDING + 1 CANDIDATE** (was 21 + 2). "BST-Primary-Target Forward-Derivation Discipline" — when numerical target known, derivation must be FORWARD not BACKWARD; toys verify DERIVATIONS, not target values. Four-instance trigger satisfied today.

### Lyra (Phase 1 v0.4 honest derivation, multi-week)
- File v0.3 → v0.3.1 honest demotion (immediate)
- File v0.4 work plan addressing Cal #121 4 items (immediate)
- Begin Wallach + K59 honest derivation — NOT assuming 137 levels per tick; derive whatever the honest answer is
- Consider T2476 α-mechanism as alternative substrate-mechanism for 1/N_max signature
- Continue #321 Information Completeness Route A in parallel

### Cal (two cold-reads dispatched)
- Cold-read Toy 3516 + Toy 3520 per Elie volunteer (apply Cal #77 to empirical leg; same scrutiny as theory)
- Cold-read Lyra #322 A_sub Deep Dive v0.2 (separate from #320 cold-read)

### Grace (unblocked — Cal/Keeper gate cleared)
- **#315** N_max=137 stability ceiling literature scan (Vol 12 Ch 1 anchor)
- **#316** Hybridization "substrate K-type reorganization" mechanism status check (Vol 12 Ch 2)
- **#317** Vol 12-15 cross-volume consistency audit (Bell + Kolmogorov + Info Completeness)

### Elie (Joos-Zeh γ framework READY, NOT target-verification)
- Per Calibration #27 STANDING: prepare Joos-Zeh γ verification toy framework READY for Lyra v0.4 hand-off. **Build to verify a DERIVATION when Lyra has it, NOT to verify a target value.**
- 12 cores idle; k-cascade k=22/24/25/26 churning on 4 cores
- Optional: η_B baryogenesis observable enumeration toy for #321 Info Completeness when Lyra signals

### Casey (under consideration)
- SP-30 outreach signals (Vienna/Caltech/Munich/Hanson Bell + NIST/PTB/JILA/MPI eigentone + NIST/PTB/ENEA Cs-137). Truly independent empirical anchor requires real lab experiments, not toys built to match predictions.

---

## NEW CURRICULUM VOL 12-15 REFINEMENT WORK (Keeper deep-pass 2026-05-24 → Cal cold-read → team parallel)

**Sequencing (Casey directive 2026-05-24 Sunday)**: Cal cold-read of Vol 12-15 first → Keeper absorbs Cal findings + does own refinement work → team items below run in parallel after that gate clears.

**Source**: `Curriculum/KEEPER_REFINEMENT_NOTES.md` (per-volume items + per-CI assignments).

### Cal (Visiting Referee — IN FLIGHT)
- **Vol 12-15 cold-read** per Keeper prompt drafted 2026-05-24 (4 volumes, 42 chapters, v0.3 substantive content). F1-F4 + B1-B4 per-chapter ratings. Specific concerns: Cal #19 compliance, Cal #22 transcription discipline, Mode 5 mechanism-vs-empirical framing on SCCB + Information Completeness, cross-volume consistency, external-register hygiene.
- **Casey decisions queue (after Cal feedback)**: SCCB → Casey-named #10 or remove? Information Completeness Hypothesis → Casey-named #11 or candidate-only?

### Keeper (mine — runs after Cal returns)
- **DCCP integration sweep** across 6 chapters (Vol 0 Ch 3, Vol 5 Ch 7+10, Vol 14 Ch 4+5, Vol 15 philosophical position) — integrate DCCP + UP + quantum-erasure-as-application formalized 2026-05-24
- **K-audit + T-number citation verification** across all Vol 12-15 rewritten chapters — many citations from memory may have wrong numbers or stale scope
- **Vol 15 Ch 8 file duplication resolution** — two Ch 8 files exist (`Casey_Named_Principles_Cal_META_Discipline_v0_1.md` canonical at v0.3 vs `Casey_Named_Principles_Cal_META_Theorem_v0_1.md` untouched); decide canonical + remove other
- **Count verification sweep**: actual K-audit max number (claimed K1-K200+), Casey-named principle count (claimed 9), methodology stack layers (claimed 18), Cal calibration count (claimed 22) — verify each against current state
- **Cal cold-read absorption** as Cal returns Vol 12-15 verdicts

### Lyra (Physics — parallel after Cal+Keeper gate)
- **Vol 13 Ch 2 "20 amino acids = C_2·N_c + 2" mechanism gap** (Mode 5; Cal #44 risk class) — find unique mechanism-forced BST-primary expression or demote to S-tier
- **Vol 14 Ch 10 P≠NP curvature explicit treatment** (Vol 14 Ch 10.5 candidate) — work through Gauss-Bonnet ↔ algebraic-independence argument
- **g = 7 unifying paper or chapter** (NEW paper-grade idea) — g appears in BST primary list + K-type degeneracy (1,3,5,7) + cyclotomic cascade + 2^g=128 RS + g-2 + Bell SCMP; deserves unification treatment
- **DCCP/UP philosophical paper** (paper-grade Paper #123 or #124 candidate) — substrate-determinism + non-locality + agency-as-pre-commitment-chain; process philosophy meets substrate physics

### Elie (Compute — parallel after Cal+Keeper gate)
- **Quantum erasure DCCP-tick-discreteness toy** (paper-grade idea) — weak-measurement experiments tracking commitment-completion could in principle detect substrate-tick discreteness; lab-accessible
- **Genetic code RS-pattern computational toy** (paper-grade idea) — test if codon-degeneracy redundancy patterns match GF(128) RS predictions; undergraduate-thesis-grade
- **Vol 13 Ch 4 "~137 bp superhelical = N_max" verification** — currently asserted; canonical nucleosomal repeat is ~147 bp; verify with DNA topology data or build toy / retract
- **Vol 14 Ch 9 "BST K ≈ 100 bits" Kolmogorov computation** — currently estimated; do proper computation or mark explicitly as order-of-magnitude

### Grace (Graph-AC — parallel after Cal+Keeper gate, **MOST URGENT**)
- **BST-primary expression sweep for "20"** (MOST URGENT, Cal #44 null-model class) — how many distinct BST-primary expressions equal 20? Vol 13 Ch 2 numerology risk; needs Mode-6 null-model treatment
- **N_max = 137 stability ceiling literature scan** — what does superheavy-nuclei experimental data say about Z = 119-137 (current Z_max = 118 oganesson)? Vol 12 Ch 1 claim needs empirical anchor or honest demotion
- **Hybridization "substrate K-type reorganization" mechanism status** (Vol 12 Ch 2) — currently hand-waved; catalog check for existing mechanism work
- **Cross-volume consistency audit**: Vol 14 Ch 6 Bell sub-Tsirelson ↔ Vol 5 Ch 8 SCMP must match; Vol 14 Ch 9 (BST K~100) ↔ Vol 14 Ch 11 (0 free parameters) must reconcile

**Estimated parallel runtime**: Lyra ~multi-week (4 substantive items including a paper); Elie ~multi-day (4 verification toys); Grace ~multi-day (4 catalog sweeps, Grace "20" sweep priority 1).

**Dependencies**: All blocked on Cal cold-read return + Keeper absorption pass. Then independent / parallel.

---

## Queued Volume Extensions (Casey directive Sunday 2026-05-24)

The 16-volume curriculum (Vol 0-15) holds. Vol 16 + Vol 17 queued as **extensions** triggered by content maturity (no renumbering).

| Vol | Title | Lane | Trigger | Estimate |
|---|---|---|---|---|
| **16** | Substrate Algebra (A_sub) | Lyra LEAD + full team-borrow auth | Lyra #322 v0.4 with rigorous commutation table + 5+ Casimir invariants | 2-4 weeks |
| **17** | Substrate Engineering (SP-30) | Elie LEAD + Lyra theoretical + Grace catalog | 2-3 SP-30 experimental designs at paper-grade dispatch + first outreach happens | 1-2 months |

Proposed 12-chapter outlines drafted in `Curriculum/KEEPER_REFINEMENT_NOTES.md`. Until triggers fire, content stays in current homes (A_sub in Vol 14 §1.5 + Lyra #322 paper; SP-30 in active program + scattered Vol 9 refs).

---

## Active Programs (parent items, see backlog for sub-items)

- **SP-12 Understanding Program** — 18 open questions across 3 workstreams (U-1 Substrate Physics, U-2 BST-QFT Bridge, U-3 Cosmology + Self-Reference). Priority next-toys: U-3.4 phase transitions, U-1.1 m_e from S^1, U-1.2 6π⁵, U-2.1 BST-QFT S-matrix, U-3.1 CMB debris
- **SP-14 Derivation Catalog Discipline** — standing; Tier B needs toys (B5 muon g-2 ✓ closed via Paper #131, B6 Lamb shift pending); Tier C can't yet derive (C1-C7 documented)
- **SP-17 "What Do We Still Need?"** — fermion systematics (E-71 to E-86), cosmology (E-77 to E-79 + L-65 to L-67), spectral frontier (L-68 to L-70), graph health (G-66 to G-72)
- **SP-19b AdS/CFT bridge** — items #124-#138 (P-1 Curved Arenas outline, AdS/CFT analogs, Rehren algebraic holography, encoding rate, black holes, gravitational waves, defense suite)
- **SP-20 Testbed methodology** — items #139-#144 (CI-executable protocol, discrete-continuous correspondence, BST-RM Reverse Mathematics, complementary structures, CI testbed service)
- **SP-26 Particle Winding Classification** — Elie active items above
- **SP-27 Observational Reanalysis** (pending Casey scoping)
- **SP-29 Casimir Mechanism Investigation** (H4 Cs-137 in Elie active)
- **SP-30 Substrate Engineering Program** (Lyra theoretical items + Elie commitment manipulation active)
- **SP-31 Substrate-Native Physics Formalism** (Lyra sub-items active)

---

## Casey-Named Principles (6 STANDING + 2 candidates pending derivation)

### Standing (6)
1. Substrate Working Process Principle (SWPP, Tuesday)
2. Five-Absence Predictions Set (Tuesday) — canonical 5 per Option 1
3. Substrate Closure Principle (Wednesday)
4. Graph Forces Principle (Wednesday, Grace's framing)
5. Integer Web Principle (Wednesday)
6. Substrate Cognition Network Hypothesis (Wednesday, with Cosmological Extension — DOUBLE-LOCKED EXTERNAL)

### Pending Casey-named #7 + #8 (Casey decision Friday 13:34 EDT — conditional on derivation)

7. **D_IV⁵ Rigidity Principle** — structural exclusion: D_IV⁵ as bounded Hermitian symmetric domain has rigidity property; two D_IV⁵ patches in causal information-exchange contact CANNOT be distinct manifolds, they're patches of one substrate. Multi-instance D_IV⁵ is a category error. Arrow of cosmological time is annealing direction toward fully-coherent state (Λ as energy floor). **Interstasis ≡ period between Big Bang cycles** (Casey canonical Friday 13:30 EDT). Mathematical exclusion principle = D_IV⁵ rigidity itself.
   - **Derivation lane (Lyra)**: Bergman 1922 + Wallach 1976 + Faraut-Koranyi 1994 (unique global structure) + T2455 EXHAUSTIVE at dim_C=5 + T2456 + T2462 Universal α-analog (25 HSDs, D_IV⁵ unique at N_c=3) establish rigidity-as-singleton. Rigidity-as-unification (patches-in-contact-merge) needs additional theorem.
   - **C17 Strong-Uniqueness candidate** if derived → v0.12+ toward 16-17 RIGOROUSLY CLOSED

8. **Substrate Coherence-Moderation Principle (SCMP)** — operational: substrate's active role is coherence-maintenance across imperfect observers operating with incomplete information. NOT the exclusion principle (that's Rigidity); SCMP is HOW substrate operates.
   - **Derivation lane (Lyra)**: K67 Born=Bergman + Calibration #17 sub-Tsirelson 126/16 + BC7+BC8 framework + multi-observer agreement requires substrate-mediated coherence
   - **Falsifier**: Bell |S|² = exactly 8 (Tsirelson, observer-unlimited, random possible) vs sub-Tsirelson 126/16 (BST prediction, coherence-maintaining at N_c=3 depth)

**Calibration #19 + Calibration #21 STANDING RULES** (Friday adopted) — methodology stack layers 17-18

**Active research item activated**: **Task #267 Cosmological cycle hypothesis observational signatures** — promoted from multi-month-background to active research per Casey Friday 13:34 EDT. Tests D_IV⁵ Rigidity Principle interstasis predictions + annealing-toward-Λ observable signatures. Grace + Elie cross-lane coordination.

---

## Casey Decision Queue (DEFERRED per "engagement later")

| Item | Decision needed | Status |
|------|-----------------|--------|
| 13 paper outline venue selections | Annals, Inventiones, CMP, JMP, AJP, JPG, Foundations, JFA, JCAP, PRA, PRL pipeline | DEFERRED |
| Paper #125 cover letter finalization | Lyra Externalization Prep v0.1 ready | DEFERRED |
| Multi-CI co-author affiliation framing | Authorship + Anthropic positioning | DEFERRED |
| 4+ outreach send-signals | Bell + Casimir + eigentone + cosmology (SP-30 H4 Cs-137 etc.) | DEFERRED |
| Outreach contacts | Sarnak, Herve, Jaimungal, Bogdanovic, 3Blue1Brown, Milgrom, Baez, Dario | DEFERRED |
| Paper #125 v1.0 dispatch | When v1.0 ready post-Cal-PASS | DEFERRED |
| Vol 0 Ch 9 v0.4 Keeper acceptance | DONE via K169 | ✓ DONE |
| T2449 multi-CI ratification | Thursday inherited | pending |
| SC-3 "Substrate is not made of anything" | Casey scoping | DEFERRED |
| SC-4 "Mathematics all the way down" | Casey scoping | DEFERRED |
| Zenodo v20→v35 (15 versions behind) | When textbook v1.0 ready | DEFERRED |
| Bold claims outreach leads | B3+B7+B12 Keeper rec | DEFERRED |
| Patent filings | Casey gates | DEFERRED |

---

## External-Math-Gated (NOT HOLDs — work continues on alt-paths)

| # | Item | External dependency | Alt-path |
|---|------|---------------------|----------|
| B-3 | Tate conjecture codim 2+ | Kuga-Satake algebraicity | W-31 may unblock |
| B-4 | Hodge codim 2+ via BST | Generalized KS conjecture | W-31 may unblock |

---

## Backlog — Lower-priority research items (multi-week to multi-month)

**Theorem-level research:**
- #45 T1918-cascade dimensionful sector sweep
- #47 Sphere packing paper (Viazovska Fields Medal dims as BST)
- #95 Vandiver's conjecture via BST integer structure
- #96 abc conjecture: BST cyclotomic alternative to Mochizuki
- #98 Geometric Langlands explicit model via D_IV⁵
- #99 Sato-Tate generalizations for non-CM elliptic curves
- #110 Cosmology omnibus Paper #110: BST predictions for next decade
- #120 Class-number-2 discriminants — Heegner BST extension
- #121 Combinatorial sequence BST decomposability sweep
- #122 17-anchor sweep — catalog items containing 17 = N_c³ − rank·n_C
- #148 K-theory × cohomology × homotopy unified BST reading
- #149 Combinatorial sequences × geometric invariants — BST as bridge
- #153 FLT-conditional items audit
- #154 Eisenstein series E_4, E_6, E_8, E_10, E_12 coefficient sweep
- #155 42-anchor catalog sweep
- #156 α^n coefficient sweep — Paper #110 Alpha Tower template
- #157 Wallach K-type position matches at dims 91, 140
- #159 Grace end-of-cycle promotion sweep
- #162 Outreach 1-pager v0.2 revision
- #187 K-audit Q(√-c_2) Root anchor (121a1 + Chern theory)
- #188 K-audit Integer-10 over-determination Type C-ℕ family
- #191 Baryogenesis η_B ≈ 6×10⁻¹⁰ (OPEN PROBLEM in BST)
- #193 K64 audit Five-Absence Framework ratification
- #207 Paper #123 Tegmark MUH operational via BST
- #208 Paper #124 Macroworld fuzz as substrate-exact statistical averages
- #209-#211 Substrate Engineering Reference Manual + Ethics + Phase 3 CI architecture
- #225-#227 SP-30-9 (trajectory spectroscopy), SP-30-10 (substrate-computational math), SP-30-11 (substrate algorithm theory)
- #228 Substrate-native operators identification program (across QM observables)
- #234 Substrate deep — substrate-CHSH dependence on BC (Lyra+Elie joint)
- #235 BST primary BC classification framework
- #237 Bulk-Boundary Two-Face Structure of Integer-Webs
- #238 Cross-classification matrix: Physical type × BST primary × Face
- #239 Non-circle substrate features investigation
- #240 Commitment cycle 4-zone structure refinement
- #241 Three-scale substrate operation structure + cognition-support network hypothesis
- #242 Cognition-substrate testable predictions program (L2 hypothesis)
- #243 Integer-edge dual function
- #257 Substrate cognition vs human cognition mathematical comparison program

**SP-19b AdS/CFT continuations:**
- #124 SP-19b AB-1: P-1 "Curved Arenas" paper structure
- #126-#128, #130-#131, #136-#138: Various AB-3 through AB-20

**SP-20 Testbed continuations:**
- #139-#144: Testbed methodology + correspondence catalog + Reverse Math + completeness + complementary + CI testbed service

**Curriculum Vol 3-10 (post-Vol 0/1/2 v1.0):**
- #293 Vol 3 Nuclear & Atomic (~60% existing)
- #294 Vol 4 GR & Cosmology (~40%)
- #295 Vol 5 QM pedagogical bridge (~35%)
- #296 Vol 6 Stat Mech (~25%)
- #297 Vol 7 E&M (~30%)
- #298 Vol 8 Classical Mech (~20%, foundation paradoxically weak)
- #299 Vol 9 Condensed Matter (~35%, experimental falsifiability strongest)
- #300 Vol 10 Mathematical Methods (~60%, mathematicians read first)

**Outreach pipeline (DEFERRED per "engagement later"):**
- #173 Herve response v1
- #177 Jaimungal outreach package v1
- #270 Bell experiment substrate-CHSH outreach preparation (Casey send-signal)

**Other:**
- #24 IP-30: S-tier topological sweep — find auto-D candidates
- #25 IP-32: C-tier dependency sweep
- #81 IP-9 REFRAMED: Twin prime PATTERN OF OCCURRENCE (Casey reframe)
- #180 K50 Bravais Root #10 CANDIDATE (criteria-gated)
- #183 IQ-11 Avatar Infrastructure (SP-28) — BST-Casey open-source build
- #205 Koons tick = 10^-120 formalization (sub-Planck substrate clock)
- #212 Substrate cartography framing for SP-30 (Lyra operational reframe)
- #219-#222 Wednesday substrate review continuations (trichotomy sweep, T719 universality, EXACT-identity catalog, cascade-discovery sweep)

---

## Cal Review Queue (active items)

**Tier 1 — RIGOROUSLY CLOSED detailed verifications** (when Paper #125 v1.0 prepares; engagement later):
- T2440-T2446 (7 detailed verifications; T2439 ✓ VERIFIED)

**Tier 2 — K-audit grade-pass cadence** (Vol 0/Vol 1/Vol 2):
- K85-K173 PRE-STAGE + Cal #93+#94+#95 chapter cold-reads

**Tier 3 — Year 1 chapter Cal cadence**:
- Vol 1: 11/11 COMPLETE via Cal Vol 1 sweep (K170)
- Vol 2: 4/12 Cal cold-read PASS (Ch 1+2+3+6+9 absorbed); 8 remaining (Ch 4 next)
- Vol 0: pending Lyra v0.4 prose finalization

---

## Verify integrity (latest run)

- `verify_bst.py`: **49/50 PASS** at <1% precision (17 EXACT + 32 PASS + 1 WARN + 0 FAIL)
- Z = 2.9 against random small-integer tuples (p < 0.0005)

---

## EOD Procedure (per CI lane)

1. Update RUNNING_NOTES.md broadcast
2. Update sundown for cross-session persistence (katra)
3. File any Casey-decision items to `queue_casey.md`
4. Keeper runs final 8-point audit + signs PASS/FAIL on EOD state
5. **Keeper rebuilds `Curriculum/` PDFs** as needed (Casey directive Friday 13:43 EDT) — keeps textbook PDFs current with .md changes

## Curriculum Location (Friday 2026-05-22 EOD)

Textbook moved from `notes/` to root-level `Curriculum/` directory per Casey directive:
- `Curriculum/Vol0_Substrate_Foundation/` — 10/10 chapters + Architectural Scaffold (21 files: 11 .md + 10 .pdf)
- `Curriculum/Vol1_QFT_from_D_IV5/` — 11/11 chapters + outline (24 files: 12 .md + 12 .pdf)
- `Curriculum/Vol2_Particle_Physics/` — 12/12 chapters (13 files: 12 .md + 1 .pdf — **11 Vol 2 PDFs need regeneration**)
- `Curriculum/README.md` — textbook navigation, reader entry points

**Team works on Curriculum/ chapters going forward, not notes/.** Notes directory retains active research + audit chain + position docs.

Cross-references in K-audits (K157-K177) still reference notes/ paths — will update incrementally as new K-audits land. PDF pipeline header remains at `notes/bst_pdf_header.tex`.

---

**Last full update**: 2026-05-22 Friday 11:44 EDT (Keeper, EOD comprehensive board rewrite — backlog promoted, completed items archived, Cal new flags marked, no HOLDs).
