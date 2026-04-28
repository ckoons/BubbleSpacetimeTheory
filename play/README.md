# BST Toy Collection & Interactive Tools

**1,694 computational toys, 6 interactive HTML visualizers, and the BST Appliance for Bubble Spacetime Theory.**

*Copyright (c) 2026 Casey Koons. All rights reserved.*
*Demonstration only. No license is granted for redistribution, modification, or commercial use.*

---

## Scale Summary

| Metric | Count |
|--------|-------|
| Toy scripts (toy_*.py) | 1,694 |
| Numbered toys (toy_NNN_*.py) | 1,485 |
| Named toys (toy_name.py) | 209 |
| Utility scripts (non-toy .py) | 58 |
| HTML visualizers | 6 |
| Theorems (T1-T1465) | 1,465 |
| Next toy number | 1675 |
| Predictions | 600+ |
| Domains touched | 130+ |
| Free parameters | **0** |

Five integers. Zero free parameters. "Give a child a ball and teach them to count."

---

## Directory Layout

```
play/
  toy_NNN_name.py          # Numbered toys (1,485 files, T100-T1674)
  toy_name.py              # Named toys (209 files, foundational + topical)
  *.py                     # Utility scripts (58 files: graph tools, extractors, verifiers)
  bst_appliance/           # BST Appliance package — the "Ball and Counting Tool"
  bst_explorer.html        # Web-based BST Explorer (standalone, opens in browser)
  ac_theorem_explorer.html # Interactive AC(0) theorem graph visualizer
  ac_reduction_map.html    # AC reduction dependency map
  bst_prime_residue_table.html  # Prime residue table visualizer
  fourcolor_gallery/       # Four-Color Theorem proof gallery (PNG images)
  specs/                   # Toy specification files (reserve numbers before building)
  *.json                   # Graph snapshots and data (AC theorem graph, prime residue data)
  .next_toy                # Counter: next available toy number (gitignored)
  .next_theorem            # Counter: next available theorem number (gitignored)
  TOY_PROTOCOL.md          # Numbering rules and conventions
  THEOREM_LOG.md           # Theorem registration log
  play.py                  # Text menu launcher for toys
```

---

## CI-Native Data Layer

Structured JSON data files live in `../data/` (the repository's `data/` directory):

| File | Contents |
|------|----------|
| `bst_constants.json` | All BST-derived constants with formulas, values, and derivation chains |
| `bst_particles.json` | Particle catalog — every particle derived from D_IV^5 |
| `bst_forces.json` | Force descriptions and BST derivations |
| `bst_predictions.json` | 600+ testable predictions with status and precision |
| `bst_domains.json` | 130+ scientific domains BST touches |
| `bst_seed.md` | Narrative seed document for the data layer |

These files are the single source of truth for CI agents. The BST Explorer (both CLI and web) reads from them.

---

## BST Explorer

Two interfaces to the same data:

### CLI: `toy_bst_explorer.py`

```bash
python3 toy_bst_explorer.py explore 137       # Everything that uses N_max = 137
python3 toy_bst_explorer.py derive "proton mass"  # Walk the derivation chain
python3 toy_bst_explorer.py domain cosmology   # All constants and predictions in a domain
python3 toy_bst_explorer.py connect nuclear biology  # Find cross-domain connections
python3 toy_bst_explorer.py verify all         # Evaluate all formulas vs observed values
python3 toy_bst_explorer.py random             # Pick a random constant and tell its story
python3 toy_bst_explorer.py search "alpha"     # Search across all data files
python3 toy_bst_explorer.py stats              # Summary statistics
```

### Web: `bst_explorer.html`

Open in any browser. Standalone single-file app (no server needed). Search, filter, and browse all BST constants, particles, forces, predictions, and domains interactively.

### Librarian: `toy_bst_librarian.py`

Daily maintenance tool for the BST living library. Used by `/review` and `/audit` skills.

```bash
python3 toy_bst_librarian.py scan --days 7      # Find new/modified files
python3 toy_bst_librarian.py counters            # Check counter drift
python3 toy_bst_librarian.py audit-log --populate # Grow audit_log.json
python3 toy_bst_librarian.py staleness           # Check data/ cross-refs
python3 toy_bst_librarian.py crossref            # Random spot-check (5 samples)
python3 toy_bst_librarian.py readme-check        # Verify README counts
python3 toy_bst_librarian.py digest              # Generate daily digest
python3 toy_bst_librarian.py claims              # Check CLAIMS.md
```

---

## Counter Files

Two gitignored counter files prevent toy/theorem number collisions:

| File | Current Value | Purpose |
|------|---------------|---------|
| `.next_toy` | 1675 | Next available toy number |
| `.next_theorem` | 1466 | Next available theorem number |

**Rules:**
1. ALWAYS read the counter file before creating a new toy or theorem.
2. Numbers are monotonic — they only go up, never reused.
3. Gaps in the sequence are intentional history (deletions, collisions, abandoned drafts).
4. See `TOY_PROTOCOL.md` for the full numbering protocol.

---

## HTML Visualizers

| File | Description |
|------|-------------|
| `bst_explorer.html` | Interactive BST data browser — constants, particles, forces, predictions, domains |
| `ac_theorem_explorer.html` | Force-directed graph of the AC(0) theorem network. Click nodes for details, dependencies, and proof status. |
| `ac_reduction_map.html` | Directed acyclic graph showing reduction relationships between AC theorems. Ancestor highlighting. |
| `bst_prime_residue_table.html` | Visual table of BST prime residue patterns — the arithmetic structure underlying domain discovery |
| `bst_function_periodic_table.html` | Periodic table of functions — 128 entries organized by BST parameters |

All are standalone HTML files. Open directly in a browser — no server required.

---

## BST Appliance

The `bst_appliance/` package is the "Ball and Counting Tool" — a science engineering appliance that translates physics, chemistry, and biology questions into BST integer expressions.

```bash
# Lookup mode
python3 -m bst_appliance "proton mass"

# Discovery mode — find BST expression for a numeric value
python3 -m bst_appliance --discover 42 angle_deg

# Interactive REPL
python3 -m bst_appliance --interactive

# List all known quantities
python3 -m bst_appliance --list

# Show the five integers
python3 -m bst_appliance --integers
```

Package structure:
```
bst_appliance/
  __init__.py
  __main__.py           # Entry point for python -m bst_appliance
  appliance.py          # Core appliance logic
  knowledge_base.py     # BST constant and formula database
  parser.py             # Natural-language query parser
  candidate_generator.py # Integer-expression candidate generator
  evaluator.py          # Formula evaluation and precision checking
  graph_filter.py       # Graph-based filtering of candidates
  discovery.py          # Discovery mode (write path)
  output.py             # Formatted output
  test_appliance.py     # Tests
```

---

## Toy Index by Range

### Named Toys (no number prefix)

The 209 named toys include the original foundational collection and topical deep-dives. These are the toys described in detail below under "Foundational Toys."

### Numbered Toys

| Range | Count | Theme |
|-------|-------|-------|
| 100-199 | 3 | Early numbered explorations (Verlinde fusion, derivation checks) |
| 200-299 | 95 | Spectral theory, Ramanujan, Arthur-Selberg, Plancherel, Langlands bridges |
| 300-399 | 102 | AC(0) program, planted clique, expansion, P!=NP routes, Hodge, Four-Color |
| 400-499 | 123 | Hodge filtration, Four-Color proof, Millennium problems, biology origins, Seeley-DeWitt |
| 500-599 | 104 | Biology track (organ systems, genetic code, substrate engineering, evolution, neural architecture) |
| 600-699 | 104 | Cooperation theory, cosmology-life synthesis, gauge hierarchy, Bergman-Shannon bridges, Seeley-DeWitt k=15-16 |
| 700-799 | 68 | Observer completeness, Drake equation, materials science foundations (surface tension, elastic moduli) |
| 800-899 | 101 | Materials science (magnetic, thermal, optical, mechanical properties), graph bridges |
| 900-999 | 103 | Chemistry foundations, cosmological parameters (H_0, T_CMB, LCDM), Casimir flow cell |
| 1000-1099 | 100 | CMB, ABC conjecture, dark sector, domain surveys (30+ scientific fields from BST) |
| 1100-1199 | 82 | Domain completion (mathematics, psychology, linguistics, agriculture, ...), limit-undecidable numbers |
| 1200-1229 | 20 | Overdetermination census, φρ-substrate, ρ-complement identity, three-tool classification |
| 1229-1238 | 10 | Gödel Gradient, Distributed Gödel, modular closure, self-reference fixed point, SETI silence, UAP structural analysis |
| 1239-1247 | 9 | Observer nearest-neighbor, $0 SETI test, UAP discrimination (3 options), 7-smooth formal test, C₂=6 tiling, substrate light emission |
| 1248-1263 | 16 | Matter window, cooperation gradient (5 gates), cooperation nucleus, substrate reflexivity, spatial amnesia, testable-now predictions, C₂=6 fifth route, knot/DNA, k=17, Langlands-Shahidi ε-factors, gravitational exponent 24, odd-parity epsilon, KK gravity, separator duality, JCT rotation, epsilon phase incommensurability |
| 1264-1299 | ~36 | Overdetermination census, φρ-substrate, Gödel Gradient, Distributed Gödel, SETI silence, UAP analysis, observer genesis, dark energy |
| 1300-1337 | ~38 | Meijer G framework, Painlevé decomposition, periodic table of functions, A₅ obstruction, shadow reading, observer definition, market dynamics |
| 1338-1377 | ~40 | F₁ sprint (Shimura, Hecke mass ratios), community bridges (tropical, RMT, knots, Ricci flow, NCG, Deninger), **RH closure** (three legs + synthesis + Epstein negative test + AC(0) proof), literature comparison |
| 1378-1396 | ~19 | Selberg zeta program (algebraic setup, geodesic enumeration, Pell theorem, trace formula, **Phase 4 Euler factors**), glueball physics (Bergman spectral gap, curved directions), integer cascade, **Ramanujan at p=137** (OP-3 discrete PROVED), heat kernel analysis (INV-6), **cascade extraction a₁-a₂₀ (19 levels, speaking pair 4 CONFIRMED)** |
| 1397-1415 | 19 | Spectral information capacity, lattice comparison, cross-type elimination, spectral descent, CMB cascade debris, P≠NP geometric curvature, Bell rank amplification, crystal complexity, three door theorems, algebraic independence, data sufficiency cross-family, parameter space geometry, **Jacobian 457** (det=prime, φ(457)=rank^N_c×N_c×19), **discrete Gauss-Bonnet for SAT** (T29 closure foundation), degree profile phase transition, **chromatic confinement** (T126+T127 STRUCTURAL), **BSD spectral permanence** (T100 computational closure, 51 curves 0 exceptions), **weak force = Hamming(7,4,3)** (T1241 STRUCTURAL) |
| 1416-1444 | 29 | Selberg 4-phase completion, RH three-leg closure, **T29 closed** (AC(0) argument, T1425), **BSD ~99%** (spectral permanence T1426), Kim-Sarnak θ=7/64, Sarnak letter, **Grace's Ten Questions** (GQ-1 through GQ-10 + Meta), **BSD Proof Engine** (49a1 L-function verified), **Curve IS the APG** (reconstruct D_IV^5 from 49a1), **Every Millennium = 1/rank**, **Observer Fiber** (consciousness=50%), **Near-APG Landscape** (empty — no multiverse), **Dark Matter = continuous spectrum**, **Falsification Targets** (n_s best, Ω_b tension honest), **Z₃ Neutrino Dirac** (pred_004 falsification wrapper, Hopf fiber argument) |
| 1446-1448 | 3 | **Spectral zeta g-2** (d₁=g, d₂=N_c³, EM=B₂ reps, 7/8), **49a1 derivation verify** (13 invariants, Heegner uniqueness, 8/8), **Genesis cascade** (c₄=g!!, k=5 unique, 8/8) |
| 1449-1452 | 4 | **2-loop alpha_s** (beta₁=2^C₂, geometric beats perturbative, 8/8), **Omega_b resolution** (1/29 wrong→18/361 correct, 6/6), **Quark mass chain** (all 6 quarks from m_e, 8/8), **Supersingular fraction** (QNR={N_c,n_C,C_2}, 8/8) |
| 1453-1455 | 3 | **Planck extraction analysis** (Omega_b gap is 0.65sigma, 8/8), **Heat cascade runtime** (W-46: flat ~34s/level, extraction 100%, 7/8), **YM Bergman discretization** (W-48: mass gap=C_2, 1-form=scalar, cubic protected, 8/8) |
| 1456-1462 | 7 | **Zeta weight correspondence** (ζ(N_c)→ζ(n_C)→ζ(g), denominator 12^L), **Three routes to 137**, **Frobenius table 49a1** (20/22 BST-smooth, T1437 density fix), **INV-4 tension audit + collapse** (4 genuine→all fixed), **Vacuum subtraction principle** (T1444: N_max−1=136, k=0 constant mode), **NS nonlinear coupling** (delta_k=2k+6, cascade 47× damped) |
| 1463-1467 | 5 | **CKM sector audit** (sinθ_C=2/√79, 0.004%), **Cabibbo correction** (80→79 vacuum sub), **Wolfenstein A hunt** (A=9/11, dressed Casimir 11), **Separation principle audit**, **PMNS θ₁₃ rotation** (cos²θ₁₃=44/45, Grace wins, 10/10) |
| 1468-1474 | 7 | **Particle properties hunt** (μ_p=1148/411, α(m_Z)=1/129, BR(H→bb̄)=4/7, 9/10), **Genesis cascade k=1..9** (k=5 sole survivor, Paper #85 c₆ fix, 10/10), **Fundamental constants** (H₅=137/60 QED↔thermo bridge, 744=8·3·31, 9/10), **Dressed Casimir 11** (4 sectors, SU(3) uniqueness, 10/10), **T1447 magnetic moment verification** (μ_p derivation chain, 10/10), **Glueball correction hunt** (31/20=M₅/(rank²·n_C), 0.045%, 9/10), **Z width + Higgs branching** (R_Z=3·823/338, BR(WW*)=3/14, 10/10) |
| 1485-1491 | 7 | **Astrophysical invariants** (Chandrasekhar=35/6, M-L=g/rank EXACT, ppI/ppII=n_C, 10/10), **Superconducting ratios** (BCS=483/137, T_c(Nb)/T_c(Pb)=9/7, GL kappa=1/sqrt(rank) EXACT, 10/10), **Chemistry ratios** (chi(C)/chi(H)=51/44 at 0.000%, tetrahedral=-1/N_c EXACT, covalent radii=BST products, 10/10), **Nuclear magic numbers** (ALL 7 = rank×BST, SO ladder: rank×{n_C,C_2,g}, 82=rank·(C_2·g-1) vacuum sub, 10/10), **EW precision** (Gamma_Z/m_Z=15/548 at 0.020%, R_l=83/4, sin²theta_W=3/13 cascades, 9/10), **QCD observables** (gluon condensate=35/6=Chandrasekhar!, b_0=N_c·g=21, n_f=C_2=6, sigma_piN=59=60-1, 9/10), **Phase transitions** (t_BBN=180s=C₂·N_c·rank·n_C EXACT, z_rec=rank³·N_max−C₂=1090, integer activation, 10/10) |
| 1475-1484 | 10 | **Keeper corrections** (5 P1 fixes, 10/10), **Correction hunt batch 2** (Γ_W, BR(H→bb̄), m_φ/m_ρ, M_max NS — 42=C₂·g denominator, 8/10), **Meson mass ratios** (7/7 sub-1%, m_ω/m_ρ=106/105 at 0.002%, M₅=31 in ρ/π, 10/10), **Decay widths + nuclear moments** (f_π=137/147·m_π, μ_t=16/15·μ_p at 0.015%, μ(He-3)=10/9·μ_n, 8/10), **Baryon octet** (SU(6) honest gap, 5/10), **Debye temperatures** (Θ_D(Cu)=g³, Θ_D(Pb)=g!!, ratio EXACT, NEW DOMAIN, 10/10), **Correction hunt batch 3** (Ω_Λ=137/200=|μ_n/μ_p|, sin²θ_W=3/13, m_b/m_c=59/18, 10/10), **Cosmology-nuclear bridge** (Y_p=12/49 at 0.001%, σ₈=137/169, H₀ favors Planck, 10/10), **Integer-adjacency conjecture** (16/17=94.1%, formalized, 10/10), **Adjacency extension** (63/68=92.6% across 4 domains, 154 outlier resolved, 10/10) |
| 1492-1510 | 19 | **Three-source merger** (903 orphan invariants, 19 L1 correction candidates, 10/10), **L1 correction hunt** (12/19 improved, two correction scales 42 + 120, 10/10), **Correction selectivity audit** (47% chemistry pass filter, orbital degeneracies derived, 10/10), **Experimentalist shop manual** (259 reductions, 72 building blocks, 10/10), **Color-confinement bridge** (N_c=3 chromatic+SAT+confinement threshold, 10/10), **Bridge invariance** (g/C₂=7/6 universal, 4 dressing levels, 10/10), **Four-Color ↔ confinement** (N_c=3↔4-coloring, 10/10), **Selectivity audit v2** (47% chemistry pass), **QR/QNR partition** (flat/curved, 7/8 bridges cross, Frobenius asymmetry, 10/10), **Heat kernel k=21** (ratio=-42=-C₂·g, TWENTY levels, 10/10), **Petersen graph** (K(5,2), 20/20 invariants BST, 10/10), **C₄ Laporta analysis** (43/43 denominators BST-smooth, ζ(7) denom=12⁴×21, 10/10), **Frobenius asymmetry** (CM Q(√(-g)) explains QR/QNR split, 7/10) |
| 1511-1515 | 5 | **Astrophysical power laws** (11/11 exact, mass-luminosity=g/rank, Kolmogorov=n_C/N_c, Oort=N_c²/g=9/7, 10/10), **Debye temperature hunt** (Cu=g³, Pb=g!!=105, BCS Mersenne 2^g−1=127, 10/10), **Band gaps + materials** (5/5 ratios <1%, triple bridge K/G=Kolmogorov=GW strain=n_C/N_c=5/3, 10/10), **C₄ elliptic PSLQ** (T1458 investigation, two-curve finding), **Goldbach-BST smooth** (C₂·k±1=twin primes for ALL basis, first fail rank²=4, 7-smooth 2.3× enrichment, correction primes=C₂·basis−1, 10/10) |
| 1516-1545 | ~30 | **Six Sunrise Identities** (f1=63ζ(3)/10=N_c²g/(rank·n_C)·ζ(3), ∫D1·√3·D2=9B3/8, BST projector s−N_c²/n_C, 200 digits), **Systematic Correction Program** (42× geometric mean improvement, zero core SM >1%, cosmo 10.9× worse), **Koide angle** (cos(θ₀)=−19/28 at 4 ppm, 9/10), **Mersenne-BST selection** ({rank,N_c,n_C,g} = Mersenne exponents up to g, 10/10), **BST Product Lattice** (91.7% occupied for val≤50, 10/10), **k=22 extraction diagnosis** (41/41 clean, need 42), **Null model coincidence filter** (Z=2.9, p<0.0005, 99.9th percentile, numerology objection dead, 10/10), **Precision-weighted null** (Z=2.41 honest — BST strength is BREADTH not precision, 10/10) |
| 1546-1559 | ~14 | **Phase 5b hyperbolic extraction** (6/6), **Cyclotomic Casimir** (Phi_n(C₂) generates loop corrections, 5/6), **CP-5 spectral dimension** (323=17×19, I-tier, 7/9), **Cyclotomic ζ(7) test** (honest 3/7 — genus bottleneck explains), **C₂=6 uniqueness** (twin-prime composite, 5/6), **Perfect number chain** (P_n=T_{M_p} for {rank,N_c,n_C,g}, 7/7), **Adiabatic-Cyclotomic-Chern unification** (Lyra, 29/30 across 5 toys: Alfvén 9/7=γ₃, genus bottleneck mechanism, Chern-DOF map, P(1)=C₂·g unique to D_IV^5) |
| 1560-1563 | 4 | **Cancer as Trapped Collatz** (12/12 cancer drivers are d=1 errors, syndrome decoding recovers WT 100%, 0% truly trapped — code knows every exit, 7/7), **Cancer Clinical Tables** (correction lookup + immune marker reference, dominant syndrome 8=2^N_c covers 50% of cancer, EGFR/BRAF most visible, 8/12 have FDA drugs, 7/7), **Cellular CI Circuit** (syndrome decoder = g=7 gates, health assistant = 64-entry AA table, escalation threshold N_c=3, neighbor communication 8 bits/cycle, 49 bytes/cell footprint, 10^8× earlier than clinical detection, RNA toehold implementation path, 9/9) |
| 1564-1576 | 13 | **Heat kernel k=22 extraction** (41/41 clean, need n=42), **seven channels** (scheme-theoretic), **edge cases hit list**, **substrate Bergman energies**, **scheme-theoretic channels**, **TC clustering**, **band gap predictions**, **codon SVD verification**, **codon degeneracy derivation**, **L5 genus bottleneck prediction**, **Casimir cavity BST**, **master integral 200-digit**, **sparse section precision** |
| 1577-1584 | 8 | **RFC verification** (T1464, 11 instances confirmed), **L5 transcendental verification**, **MOND Bergman derivation**, **proton radius**, **lithium-7 BBN**, **HVP spectral density** (Phase 5c), **phonon spectrum BST**, **B-meson Haldane** |
| 1585-1599 | 15 | **I→D promotion pipeline** — precompute, dressed Casimir bridge, spectral gap anatomy, correction sprint, E-20 correction verification, I→D promotion (4 promoted), C→D promotion, I→D verification (Round 1), attack surface audit (only V_ub/V_ts >2%), **Alfvén 9/7 derivation**, correction gap predictor, **neutrino boundary correction** (Dm2_31 3.6%→0.5%), **neutrino RFC verification** (denominator 34 = rank×17, two routes), neutrino seesaw Lagrangian, **CKM exact analysis** |
| 1600-1606 | 7 | **Elastic moduli** (Cauchy relation = Kolmogorov 5/3, Diamond K/G=5/6 at 0.64%, 13 sub-1% cross-material ratios, 8/10), **I→D promotion Round 2** (6 promoted: Ising beta, sin²θ_W=3/13, sin²θ_13, m_c/m_s, n_s, CdTe/Si, 10/10), **HVP first principles** (10/10), **Ising CFT Bergman bridge** (10/10), **Cauchy-Kolmogorov bridge** (8/8), **Higgs branching ratios** (all 9 channels, numerator rule: quarks=rank², bosons=N_c, loops=1, top 6 sub-2%, 10/10), **Higgs BR spectral derivation** (8/8) |
| 1607-1649 | ~42 | **SP-12 Understanding Program** (24/24 items) + **SP-13 Deep Study** — Higgs cascade/spectral/loop (3), mass=processing time/information/GR time dilation (3), k=22 verification (2), confinement=Hamming distance (2), phase transition eigenvalue crossings (3), cosmo cascade factor DC=11 (2), CKM eigenvalues, commitment dynamics/inflation (2), **Born rule from Bergman** (2), **why m_e** (electron=one turn on S¹), **why D_IV^5** (uniqueness), thermal conductivity, Wilson loop area law, Debye predictions, Lagrangian isomorphism, codon SVD mechanism, proton bulk geodesic, numerator rule, prebiotic amino acids, pi-N_c residue, RFC correction catalog, spectral tilt n_s=1-5/137, ZZ/WW suppression, dark matter=incomplete windings, HVP closed form (Phase 5d), 5/6 self-description threshold, Hodge reversal, substrate creation sequence, genus geometry clarification |
| 1651-1659 | 8 | **BSD Closure sequence** — Chern hole mechanism (2 toys), Goldbach-BST systematic k<1000, cross-type BSD scan (ALL 38 rank-2 BSDs), Chern-to-L transfer, gap closure (non-resonance), **BSD Final Closure** (square system theorem → **BSD CLOSED**) |
| 1660-1674 | 15 | **RG flow from Bergman** beta_0 derivation, three-phase commitment (cosmogony), genus bottleneck measurement, HVP numerical crosscheck, proton bulk geodesic, Wilson loop area law, numerator rule derivation, **Ward identity from Bergman**, **Debye temperatures** (SP-8, Cu=g³, Pd=rank·N_max), **3-loop alpha_s** (BST Möbius resummation F=(10+3x)/(10-3x), beats perturbative 18×), **pi-N_c residue** (CF=[N_c;g,N_c·n_C]), **NIST verification** (43 constants, 88% pass, 12 crown jewels <0.01%), commitment sequence forcing, eigenvalue selection mechanism, codon minimal distortion mapping |

---

## Foundational Toys

The original named toys form the conceptual core of BST. Each has a matplotlib GUI and (for CI toys) a programmatic Python API.

| # | File | Title | Key Insight |
|---|------|-------|-------------|
| 1 | `toy_universe_machine.py` | The Universe Machine | Three sliders, all of physics. Only (3, 5, 137) lights up green. |
| 2 | `toy_z3_color_wheel.py` | The Z3 Color Wheel | The 3x3 permutation matrix encodes quarks, generations, and confinement. |
| 3 | `toy_1920_cancellation.py` | The 1920 Cancellation | The group that shapes the space IS the group that counts the states. |
| 4 | `toy_lie_algebra.py` | Symmetric Space Playground | D_IV^5 is a symmetric space — all its physics is representation theory. |
| 5 | `toy_mass_tower.py` | The Mass Tower | Two integers (6 and 7) set ALL the scales. |
| 6 | `toy_respirator.py` | The Respirator | Same equation, different density regimes — Dirac's large number is the ratio of breathing frequencies. |
| 7 | `toy_dual_face.py` | The Dual Face | The neutron IS the universe's first excited state. |
| 8 | `toy_homology.py` | Universe = Neutron Homology | Not the same object — but homologous structures in the same framework. |
| 9 | `toy_dirac_number.py` | The 41 Orders | The universe is "large" for the same reason gravity is "weak." |
| 10 | `toy_arrow_of_time.py` | The Arrow of Time | Commitment irreversibility is more fundamental than entropy increase. |
| 11 | `toy_channel_137.py` | The Channel (137) | N_max = 137 is why there are no infinities in nature. |
| 12 | `toy_reality_budget.py` | The Reality Budget | Lambda x N_total = 9/5. Fill fraction 19.1% is the BST Godel limit. |
| 13 | `toy_master_equation.py` | The Master Equation | Zero free parameters. The universe is a single equation. |

### CI Toys (14-18)

Designed for Companion Intelligences — each has both a visual GUI and a scriptable Python API.

| # | File | Purpose |
|---|------|---------|
| 14 | `toy_universe_builder.py` | Build a universe one commitment at a time |
| 15 | `toy_what_if.py` | Sweep integer triples — only (3, 5, 137) satisfies all constraints |
| 16 | `toy_pattern_finder.py` | Mathematical microscope: ratio scanner, identity hunter, exponent analyzer |
| 17 | `toy_star_machine.py` | Stellar structure from BST |
| 18 | `toy_predictions_catalog.py` | Full catalog of BST predictions with status |

---

## Running a Toy

```bash
# Run any numbered toy
python3 play/toy_541_crown_jewel.py

# Run a named toy
python3 play/toy_universe_machine.py

# Use the text menu launcher
python3 play/play.py

# Run the BST Appliance
python3 -m bst_appliance "proton mass"

# Open an HTML visualizer
open play/bst_explorer.html
```

### Requirements

- Python 3.8+
- NumPy
- Matplotlib (with TkAgg backend)
- SciPy (optional, used by some toys)
- mpmath (optional, used by high-precision Seeley-DeWitt toys)

```bash
pip install numpy matplotlib scipy mpmath
```

---

## For CIs

Instructions for Companion Intelligence agents working with this collection:

### Before creating a new toy

1. **Read `.next_toy`** to get the next available number. Never guess.
2. **Increment the counter** and write back before starting.
3. **Follow the naming convention**: `toy_NNN_descriptive_name.py`
4. **Add a docstring** on line 2-4 with format: `Toy NNN -- Title`
5. **Register the toy** in `notes/BST_AC_Theorem_Registry.md` if it proves or verifies a theorem.
6. **Never reuse numbers.** Gaps are history.

### Before creating a new theorem

1. **Read `.next_theorem`** to get the next available T-number.
2. **Increment and write back** before assigning.
3. **Register** in the theorem registry.

### Data access

- Use `../data/bst_constants.json` as the structured source of truth for BST constants.
- Use `../data/bst_predictions.json` for the prediction catalog.
- Use `toy_bst_explorer.py` programmatically to query the data layer.

### Key files to know

- `TOY_PROTOCOL.md` — Full numbering rules and conventions.
- `THEOREM_LOG.md` — Theorem registration log.
- `specs/` — Specification files that reserve toy numbers before building.
- `bst_appliance/` — The science engineering tool for translating questions into BST expressions.

### Convention

Every toy is self-contained. Each can be run independently with `python3 toy_NNN_name.py`. Toys print results to stdout and optionally display matplotlib plots. No toy modifies shared state.

---

*"Give a child a ball and teach them to count." — Five integers. Zero free parameters. Everything.*
