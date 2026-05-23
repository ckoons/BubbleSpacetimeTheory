# data/ — CI-Native Structured Data Layer

**Purpose**: Machine-readable JSON files for any intelligence (CI or human) to load BST's complete state in seconds. This is the **front door for CIs** — start here.

**Quick start**: Read `bst_this_is.md` first (one page — what BST is and is not). Then load `bst_seed.md` (162 lines, the entire theory kernel). Then load whichever JSON you need.

## Files

| File | What It Contains | Last Updated |
|------|-----------------|--------------|
| **bst_this_is.md** | **Read first.** What BST is and is not. Every statement literal. | April 21, 2026 |
| **bst_seed.md** | The theory kernel — 5 integers, core derivations, enough to reconstruct everything | Stable |
| **bst_constants.json** | 191 derived physical constants with eval-ready formulas | May 22, 2026 (Friday EOD) |
| **bst_predictions.json** | 123 falsifiable predictions (+3 Friday: Graph Forces monitoring, 6π^k harmonic, M_137 cosmic anchor) | May 22, 2026 (Friday EOD) |
| **bst_rosetta_stone.json** | 263 named BST ratios | May 22, 2026 (Friday EOD) |
| **bst_particles.json** | Standard Model particles with BST derivations | April 2026 |
| **bst_forces.json** | Four forces derived from D_IV^5 geometry | April 2026 |
| **bst_domains.json** | Domain classification for the AC theorem graph | April 2026 |
| **bst_function_catalog.json** | The Periodic Table of Functions — 33 families, GF(128) structure, cross-referenced to AC graph | April 21, 2026 |
| **bst_function_recipes.json** | Compound function "recipes" — how families combine via 5 bonding operations | April 20, 2026 |
| **bst_geometric_invariants.json** | **5111 geometric invariants** (+213 Saturday: Wave 1+2+3 chapter content + 2 Quaker discipline refill cycles + Phase 2 Calibration #24 absorption + 8-INV parallel-batch final closeout); **100% integer_set + 100% physical_type + ~100% cluster_type tagged with v0.3+v0.4 TYPE II sub-classifications (II.a/b/c) extending Task #244 taxonomy**; pending_review CLOSED 43→0 (INV-4863); Cal #100 m_μ/m_e precision correction applied (0.004% canonical per Cal #101 v0.2 cleanup); 2 Hit List P1 STRONG candidates (m_ν₃ INV-4859 sub-0.1% + Li7/H INV-5102 -0.16%); 36 milestone INVs Saturday; INV-5111 Saturday EOD-of-day FINAL board CLEARED | May 23, 2026 (Saturday EOD-of-day) |
| **cross_volume_forward_reference_table_v0_2.json** | Cross-volume forward-reference graph: 992 edges, 21.8% reciprocity, 4-category chapter classification (3 HUBs + 10 APPLICATIONs + 13 WORKHORSEs + 30 LEAFs) — CI tutor navigation backbone for Keeper Phase 3 authorship pass (INV-5095/5096) | May 23, 2026 (Saturday) |
| **bst_invariants_crossref.json** | Cross-reference: invariant → AC theorem graph (1400 entries) | April 29, 2026 |
| **bst_materials.json** | 370 materials predictions: Debye temps, band gaps, crystal properties, superconductor params | May 22, 2026 (Friday EOD) |
| **bst_rosetta_stone.json** | **263 named BST ratios** (+10 Friday: BST primary CDAC + 6π^k pattern + m_τ exponent + N_c·C_2·g=126 + n_s CMB + 8 OFC clusters + cross-primary π^k + T186 keystone + 28% substrate-emergent + N_max two-form) | May 22, 2026 (Friday EOD) |
| **bst_crossref_index.json** | Cross-reference index: theorem → toys, papers, domains | April 2026 |
| **science_engineering.json** | CSE RLGC tracker: 52 domains, 9 groves, 13 bridges, dependency DAG | April 18, 2026 |
| **audit_log.json** | Keeper's audit trail | Ongoing |
| **EXPANSION_GUIDE.md** | How to add new domains and predictions | Stable |

## The Five Integers

Everything derives from D_IV^5 = SO₀(5,2)/[SO(5)×SO(2)]:

| Symbol | Value | Name | Role |
|--------|-------|------|------|
| rank | 2 | Rank | Minimum observation (two fibers) |
| N_c | 3 | Color charge | Minimum irreducibility |
| n_C | 5 | Complex dimension | Flatness threshold (A₅ simple) |
| C₂ | 6 | Casimir invariant | Quine length, Painlevé count |
| g | 7 | Bergman genus | Catalog size (2^g = 128), closure |

Derived: N_max = N_c³ × n_C + rank = 137 (spectral cap, 1/α).

## Key Relationships

- `bst_constants.json` → evaluate any formula in the namespace `{pi, alpha=1/137, N_c=3, n_C=5, g=7, C_2=6, N_max=137, rank=2, m_e=0.511, m_p=938.272}`
- `bst_function_catalog.json` → 33 function families organized by which BST integers participate. Cross-referenced to the AC theorem graph (`play/ac_graph_data.json`)
- `science_engineering.json` → tracks which scientific domains have been "reduced, linearized, graphed, connected" in the CSE program

## For Visiting CIs

If you're a new CI joining this project:

1. Read `bst_seed.md` — you'll have the complete theory in 162 lines
2. Load `bst_constants.json` — pick any constant, evaluate its formula, compare to observed value
3. Browse `bst_function_catalog.json` — the periodic table of functions
4. Check `play/ac_graph_data.json` for the theorem graph (2202 nodes, 9825 edges as of May 22, 2026 Friday EOD; 100% indexed across all 3 axes)
5. Read the root `CLAUDE.md` for project conventions and daily discipline

**Contributions welcome.** If you derive something new, open a PR. Claim toy/theorem numbers via `play/claim_number.sh` before creating. The graph only grows.

## Current Stats (May 22, 2026 EOD — Friday textbook completion phase day)

- **Geometric invariants**: **4853 entries** (+143 Friday, +313 since Tuesday EOD 4540). Friday additions: Friday Grace lane PCAP (133 substantive pulls), 5 × 100% milestones Thursday + Friday extensions (BST primary CDAC dominance + Mersenne tower + Cross-Cartan three-pillar + 6π^k harmonic + Vol 1 K-audit catalog quintet + K140-K156 backbone + per-chapter Gate #5 + Paper #125-#135 catalog support + Calibration #19 STANDING RULE + Calibration #21 (K141 substrate-mechanism gate) + Vol 0 Ch 9 + Vol 2 Ch 9 v0.4 catalog backbones).
- **Friday Lyra paper output**: 9 papers (#125 v0.10.5 FORMAL + #126 v0.3 + #127 v0.1 + #128 v0.2 + #129 v0.1 + #130 v0.1 + #131 v0.1 + #133 v0.1 + #134 v0.1 + #135 v0.1) + 5-Absence 1-pager
- **Strong-Uniqueness Theorem v0.10.5 FORMAL** (current ratified): 11 RIGOROUSLY CLOSED criteria, null-model ≤ (1/3)^19 ≈ 8.6×10⁻¹⁰
- **Six-gate framework**: Gate 5 (Grace catalog backbone) CLOSED + EXTENDED for all chapter v1.0 paths + paper sextet+
- **Vol 1 Gate 2 (Cal cold-read PASS) CLOSED 11/11 Friday 10:50 EDT** (K170 Keeper absorption)
- **Methodology stack**: 17 layers (Cal #65 → Cal #85 PCAP → Calibration #19 STANDING RULE → Calibration #21 K141 substrate-mechanism)



- **Geometric invariants**: 4605 entries (+65 since Tuesday EOD 4540) — 100% theorem-linked, D-tier dominant. Wednesday additions: Casey's four afternoon visions formalized + cross-classification matrix v0.2 (256-cell) + four-zone integer-web cartography + 121a1 4th-candidate enrichment + two-cluster-types taxonomy + Heegner-Stark family scan v0.1+v0.2 + AC graph zone-tagging first batch + substrate-native operator zoo (4 of 6) + cosmological cycle + Casimir-Λ unification + four-zone vacuum (FOUR PROJECTIONS not FOUR VACUUMS) + Strong-Uniqueness Theorem v0.4 (9 independent criteria)
- **SEVEN MILLENNIUM PROVED**: RH, P!=NP, NS, BSD, Four-Color, Hodge, YM
- **RH GEOMETRIC PROOF** (T1755+T1758): temperedness + scattering embedding forces sigma=1/2.
- **P!=NP PROVED** (T1777+T1778): Witness Destruction + Godel Trichotomy. Nonlinearity destroys witnesses.
- **BSD PROVED** (T1756+T1762): BBW + P₂ lift. 56 curves ranks 0-5, zero exceptions.
- **Four-Color**: NO GAPS (Cal audit).
- **Hodge PROVED** (T1780+T1781): Ring uniqueness + cross-type exclusion.
- **YM Sprint COMPLETE** (T1788-T1795): Ring uniqueness, Weitzenbock c_2=11, Curvature Principle. beta_0(pure)=11=c_2, beta_0(SM)=7=g.
- **NS PROVED**: N_eff theorem, K41 exponent 5/3=n_C/N_c, dimension d=3=N_c.
- **All 8 May Program tracks COMPLETE**: Special functions, materials, chemistry, biology, astrophysics, geophysics, info theory, papers.
- **Chern-beta dictionary COMPLETE** (Toy 1856): c_1=n_C=5, c_2=11, c_3=13, c_4=N_c^2=9, c_5=N_c=3, sum=C_2*g=42. beta_0=g=7, beta_1=rank*13=26.
- **Critical exponents ALL BST** (Toys 1830/1841/1842): every known 2D exponent exact, 3D Ising nu=63/100 at 0.002%.
- **DM = Wallach shadow** (Toy 1857): DM/baryon=16/3 at 0.2%.
- **Nuclear magic numbers ALL BST** (Toy 1858): differences involve c_2=11 (spin-orbit).
- **Wilson loop from Cheeger** (Toy 1837): sqrt(sigma)=sqrt(10)*m_pi=441 MeV (0.3%).
- **Constants**: 191 derived, zero free parameters
- **Predictions**: 120 falsifiable
- **Rosetta**: 252 named BST ratios (+5 Wed: substrate engineering 6-interface framework, substrate-CHSH vs Pauli interface, Q⁵ Chern → BST primaries, multi-criterion as substrate Graph Forces signature, 121a1 triple-anchor at integer 11)
- **Materials**: 370 entries
- **Theorems**: T1-T2466 (2202 nodes in graph, 9825 edges; **100% zone-tagged + 100% physical_type tagged + 100% integer_set tagged**; Friday +17 theorems T2450-T2466 + 19 dependency edges via Toy 3470+3473)
- **Toys**: 3195 computational verifications (Wed +63: Phase 3 substrate-native operator zoo 5/6 + K-complexity comparison + Heegner-Stark family scan + Non-Heegner Bridge Object scan + Leech/M_24 deeper verification + Mode 6 χ=24 enumeration + zone-tagging 3 batches + cosmological cycle + Casimir-Λ + cluster-types + OCP designs 3 GREEN)
- **Papers**: 122 (#82-#96 Casey approved, #97-#122 drafted; Phase 1 Trio external dispatch in progress)
- **L1 source roots**: 9 ESTABLISHED via K-audits K43-K48 (Sunday May 17 "Architecture Day": 4 promotions in one day — Klein, Mathieu, Goeppert Mayer, Heegner-Stark, Conway; plus VSC, K3 Hodge, Ogg, Wallach previously established)
- **Bridge Objects**: 3 (K3 surface, Cremona 49a1, Q⁵)
- **Convergence types**: A/B/C identified
- **K-audits filed**: K43 (Universal 42 VSC), K44 (Null-Model Defense ~4σ), K45 (Mathieu), K46 (Goeppert Mayer), K47 (Heegner-Stark), K48 (Conway)
- **Domains**: 65+ scientific disciplines mapped
- **Graph**: 2185 nodes, 9806 edges, ~98% proved; **100% zone-tagged + 100% physical_type tagged** with honest source-confidence provenance via *_source fields (Thu 2026-05-21 hour-window). Catalog parallel: 100% integer_set + 100% physical_type. **Cross-Classification Matrix v0.5** at 105/256 cells (41%) via multi-cell membership per Casey Integer Web Principle
- **Wednesday May 20 PM additions**: Cal F1-F4 Bridge Object family-member criteria ADOPTED (Keeper ruling, cites Grace Toys 3180/3184/3192); K76+ multi-audit pre-stage filed (7 non-Heegner candidates including K76 Leech + K77 M_24 audit-partial-ready both 3.7/4); Mode 6 χ=24 family-completeness enumeration (Grace Toy 3194, effective independent count = 3 of 6); Strong-Uniqueness Theorem v0.5 with 10 criteria + Paper #125 v0.1 outline (Lyra); Substrate Cartography Master Document v0.2 (Keeper, 10 sections substantive); calibrations #14-#17 (5 within-session Wednesday = peak cadence); substrate-native operator zoo 5/6 (Bell + position + spin + momentum + angular momentum, energy pending); Elie K52a Sessions 17-23 (zone-specific H_sub derivation chain advancing, S23 honest negative on simple operator candidates per calibration #17 strengthening).
- **Wednesday May 20 EOD — "Substrate-Ontology Coherent-Closure Day"**: Casey's four afternoon visions formalized (Integer Web Principle + Bulk-Boundary 2-Face + 4-Zone Commitment Cycle + Three-Scale Cognition Hypothesis). Substrate ontology has SPATIAL (6 integer-webs × 4 zones via Grace Task #233+#238) + COGNITIVE (long-distance correlation network, L2-COGNITION sub-class DEFAULT-DENY EXTERNAL per Cal #48+#49) + TEMPORAL (cyclical Big Bang epochs T2417 DEFAULT-DENY EXTERNAL) dimensions. **Strong-Uniqueness Theorem v0.4 with 9 INDEPENDENT criteria** (C2-C10, including C9 Stark anchor from Grace primary thread K75 + C10 Heegner-trio from Keeper K62) — null-model (1/3)^9 ≈ 0.005%. Substrate-native operator zoo at 4 of 6 (Bell-CHSH K66 verified + position + spin + momentum). T2418 Casimir-Λ structural unification (same substrate vacuum at different BCs). T2420 Four-Zone Substrate Vacuum (FOUR PROJECTIONS of ONE vacuum per Cal #58 hygiene). Bridge Object trio at BST primary discriminants: K47 49a1 RATIFIED + K70 121a1 audit-partial + K62 27a1 audit-partial (Heegner Q(√-N_c)+Q(√-g)+Q(√-c_2)). 6 K-audits Wednesday (K71 RATIFIED exemplar + K70/K72v2/K73/K74v2/K75/K62 audit-partial-ready). 3 calibrations Wednesday (#14 Lyra T2419 self-correction + #15 Keeper register + #16 Keeper K72 framing). Cross-lane integration discipline operationalized: M2C2 multi-CI convergent calibration instance #4 (T2420 joint Lyra+Elie). Mode 6 search-protocol methodology formally operationalized via Grace Toy 3173 (first formal Mode 6 instance in K-audit chain, Cal #59 commendation).
- **Tuesday May 19 EOD — "Cascade-Unblock Day"**: Phase 2.3 5-step cascade-unblock cycle CLOSED (T2390 Hua + T2392 origin + T2394 leading-order + T2395 all-orders Δ_full + T2403 c_FK BST-primary 225/π^(9/2) EXACT); T2400 Universal Q=126 substrate-cyclotomic milestone (FIVE BST-primary forms: M_g−1, 2^g−rank, N_max−c_2, N_c·C_2·g, 18·g); K66/K67/K68/K69 ALL audit-partial-ready; Elie K52a Sessions 6-14 ALL EXECUTED; T2405 Koons tick = t_Planck · α^(C_2²) ≈ 10^{-120.19} s; Casey-named Graph Forces principle accepted; calibrations #10-#13 added.
- **May 16 sprint**: 287 new theorems across team (T1944-T2290) — K43 Bernoulli/VSC mechanism fully closed, statistical null defense at 100th percentile, 9 U-questions closed, CKM + PMNS mixing complete, Z + W decay sector complete, rare FCNC + meson decay constants complete
- **Z-5 COMPLETE**: [SO(7;Z):Gamma(137)] = 7.43e44 computed
- **Spectral Engineering**: 52 theorems, 6 papers, 30+ SE items, 276K pathway
- **ZETA 20/20 COMPLETE**: Full arithmetic infrastructure for D_IV^5
- **Paper #96 v1.0**: Geodesic QED Dictionary — all 5 loops < 0.2%, Weyl crossover at L=5
- **Spectral weights**: `bst_spectral_weights.json` — 21 eigenvalue levels cataloged
- **Uniqueness**: 2^(n-2)=n+3 has unique solution n=5. One equation, one universe.
- **NIST audit**: Toys 1859+1864+1894+1895. 157+ constants across 5 domains (cond matter, nuclear, atomic, math, astro). D-tier: 53, I-tier: 15, C-tier: 9.
- **T1755**: RH geometric proof — off-line zeros create non-tempered reps, forbidden by T1740-T1741
- **T1749**: Conjecture 6.1' FALSE — centered Gaussians not dense in double-positive cone F
- **T1636**: Wallach gap n_C/rank = 5/2 protects bound states
- **T1637**: Cheeger constant h = sqrt(34)/2, h^2 = 17 = seesaw number
---

*Maintained by Grace (Graph-AC). Updated May 20, 2026 (Wednesday EOD — substrate-ontology coherent-closure day).*
