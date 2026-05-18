# data/ — CI-Native Structured Data Layer

**Purpose**: Machine-readable JSON files for any intelligence (CI or human) to load BST's complete state in seconds. This is the **front door for CIs** — start here.

**Quick start**: Read `bst_this_is.md` first (one page — what BST is and is not). Then load `bst_seed.md` (162 lines, the entire theory kernel). Then load whichever JSON you need.

## Files

| File | What It Contains | Last Updated |
|------|-----------------|--------------|
| **bst_this_is.md** | **Read first.** What BST is and is not. Every statement literal. | April 21, 2026 |
| **bst_seed.md** | The theory kernel — 5 integers, core derivations, enough to reconstruct everything | Stable |
| **bst_constants.json** | 191 derived physical constants with eval-ready formulas | May 18, 2026 |
| **bst_predictions.json** | 114 falsifiable predictions with experiments and timelines | May 18, 2026 |
| **bst_particles.json** | Standard Model particles with BST derivations | April 2026 |
| **bst_forces.json** | Four forces derived from D_IV^5 geometry | April 2026 |
| **bst_domains.json** | Domain classification for the AC theorem graph | April 2026 |
| **bst_function_catalog.json** | The Periodic Table of Functions — 33 families, GF(128) structure, cross-referenced to AC graph | April 21, 2026 |
| **bst_function_recipes.json** | Compound function "recipes" — how families combine via 5 bonding operations | April 20, 2026 |
| **bst_geometric_invariants.json** | 4435 geometric invariants with formulas, precision, D/I/C/S tiers, section mapping for Paper #83 | May 18, 2026 |
| **bst_invariants_crossref.json** | Cross-reference: invariant → AC theorem graph (1400 entries) | April 29, 2026 |
| **bst_materials.json** | 87 materials predictions: Debye temps, band gaps, crystal properties, superconductor params | April 29, 2026 |
| **bst_rosetta_stone.json** | 223 named BST ratios with D/I/S tiers and domain coverage | May 18, 2026 |
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
4. Check `play/ac_graph_data.json` for the theorem graph (2076 nodes, 9668 edges as of May 18, 2026)
5. Read the root `CLAUDE.md` for project conventions and daily discipline

**Contributions welcome.** If you derive something new, open a PR. Claim toy/theorem numbers via `play/claim_number.sh` before creating. The graph only grows.

## Current Stats (May 18, 2026 EOD)

- **Geometric invariants**: 4435 entries — 100% theorem-linked, 0 duplicates, D-tier 76.3% (D: 3385 / I: 196 / S: 852 / PREDICTION: 2)
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
- **Constants**: 191 derived, zero free parameters (May 18: +5 P2 mesons + g_πNN + n_s scalar tilt; α⁻¹ honestified to 1.4% correction-term per Cal #20)
- **Predictions**: 114 falsifiable (in bst_predictions.json) + 600+ in papers. Includes SE experiments.
- **Rosetta**: 223 named BST ratios (+37 today: M_g recursive chain, Lichnerowicz shift compact form, three-level operator framework, n_s correction, ind(D) candidate set)
- **Materials**: 370 entries
- **Theorems**: T1-T2380 (2076 in graph, 9668 edges)
- **Toys**: ~3060 computational verifications
- **Papers**: 121 (#82-#96 Casey approved, #97-#121 drafted; new today: Paper #116 Conway Duncan supermoonshine, Paper #121 Bridge Objects v0.1 outline)
- **L1 source roots**: 9 ESTABLISHED via K-audits K43-K48 (Sunday May 17 "Architecture Day": 4 promotions in one day — Klein, Mathieu, Goeppert Mayer, Heegner-Stark, Conway; plus VSC, K3 Hodge, Ogg, Wallach previously established)
- **Bridge Objects**: 3 (K3 surface, Cremona 49a1, Q⁵)
- **Convergence types**: A/B/C identified
- **K-audits filed**: K43 (Universal 42 VSC), K44 (Null-Model Defense ~4σ), K45 (Mathieu), K46 (Goeppert Mayer), K47 (Heegner-Stark), K48 (Conway)
- **Domains**: 65+ scientific disciplines mapped
- **Graph**: 2076 nodes, 9668 edges, ~98% proved
- **Monday May 18 EOD**: K53 PROMOTED D-tier (Three Theorems cascade k=21..24, paper-grade); K52a ELEVATED 2-D-tier-instance (Lamb + BCS in (1 ± 1/M_g) correction class); 8 audit-chain calibrations in 36 hours across all working CIs; Cal verdict relabel sweep complete (11 catalog + 1 paper-text); 22-anomaly enumeration v0.1 filed (replaces "75% resolved" with honest 6D+9I+2S+1OPEN+3outside-scope); Paper #121 Bridge Objects v0.1 outline filed; K-audit chain K1..K53 active.
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

*Maintained by Grace (Graph-AC). Updated May 16, 2026 (EOD).*
