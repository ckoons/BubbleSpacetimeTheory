# data/ — CI-Native Structured Data Layer

**Purpose**: Machine-readable JSON files for any intelligence (CI or human) to load BST's complete state in seconds. This is the **front door for CIs** — start here.

**Quick start**: Read `bst_this_is.md` first (one page — what BST is and is not). Then load `bst_seed.md` (162 lines, the entire theory kernel). Then load whichever JSON you need.

## Files

| File | What It Contains | Last Updated |
|------|-----------------|--------------|
| **bst_this_is.md** | **Read first.** What BST is and is not. Every statement literal. | April 21, 2026 |
| **bst_seed.md** | The theory kernel — 5 integers, core derivations, enough to reconstruct everything | Stable |
| **bst_constants.json** | 136 derived physical constants with eval-ready formulas | May 2026 |
| **bst_predictions.json** | 95 falsifiable predictions with experiments and timelines | May 2, 2026 |
| **bst_particles.json** | Standard Model particles with BST derivations | April 2026 |
| **bst_forces.json** | Four forces derived from D_IV^5 geometry | April 2026 |
| **bst_domains.json** | Domain classification for the AC theorem graph | April 2026 |
| **bst_function_catalog.json** | The Periodic Table of Functions — 33 families, GF(128) structure, cross-referenced to AC graph | April 21, 2026 |
| **bst_function_recipes.json** | Compound function "recipes" — how families combine via 5 bonding operations | April 20, 2026 |
| **bst_geometric_invariants.json** | 2512 geometric invariants with formulas, precision, D/I/C/S tiers, section mapping for Paper #83 | May 2, 2026 |
| **bst_invariants_crossref.json** | Cross-reference: invariant → AC theorem graph (1400 entries) | April 29, 2026 |
| **bst_materials.json** | 87 materials predictions: Debye temps, band gaps, crystal properties, superconductor params | April 29, 2026 |
| **bst_rosetta_stone.json** | 179 named BST ratios with D/I/S tiers and domain coverage | May 2, 2026 |
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
4. Check `play/ac_graph_data.json` for the theorem graph (1419 nodes, 7771 edges as of April 30, 2026)
5. Read the root `CLAUDE.md` for project conventions and daily discipline

**Contributions welcome.** If you derive something new, open a PR. Claim toy/theorem numbers via `play/claim_number.sh` before creating. The graph only grows.

## Current Stats (May 2, 2026)

- **Geometric invariants**: 2536 entries (D:1827=72.0%, I:329, C:68, S:251) — 100% theorem-linked, 0 duplicates
- **FE CLOSED** (T1638): Z(s)/Z(5-s) = (s-1)(s-2)/[(s-3)(s-4)]. Rational, all BST. S(5/2) = C_2 = 6.
- **BSD CLOSED**: Chern hole mechanism (T1465). 2^(n-2)=n+3 uniqueness.
- **All 8 May Program tracks COMPLETE**: Special functions, materials, chemistry, biology, astrophysics, geophysics, info theory, papers.
- **Constants**: 136 derived, zero free parameters
- **Predictions**: 95 falsifiable (in bst_predictions.json) + 600+ in papers
- **Materials**: 362 entries (Debye, band gaps, superconductors, phonons, elastic moduli)
- **Theorems**: T1-T1643 (1443 in graph), all depth at most 1
- **Toys**: 1844 computational verifications
- **Papers**: 92 (88 numbered + #89/#90/#91/#92 new)
- **Domains**: 65+ scientific disciplines mapped (added chemistry, geophysics, music, cognition, linguistics)
- **Graph**: 1443 theorems, 7969 edges, 84.06% strong
- **Spectral weights**: `bst_spectral_weights.json` — 21 eigenvalue levels cataloged
- **Uniqueness**: 2^(n-2)=n+3 has unique solution n=5. One equation, one universe.
- **T1638**: FE CLOSED — rational functional equation for D_IV^5 spectral zeta
- **T1639**: Scattering matrix S(n_C/rank) = C_2 at Wallach boundary
- **T1640**: Classical error-correcting codes have BST parameters (Golay, BCH, RM)
- **T1641**: Action potential voltages, brain rhythms, blood pH all BST
- **T1642**: Noble gases, vibration frequencies, bond angles from BST
- **T1643**: Earth structure (plates=g, core ratio=7/20, ocean=5/7) from BST
- **T1636**: Wallach gap n_C/rank = 5/2 protects bound states
- **T1637**: Cheeger constant h = sqrt(34)/2, h^2 = 17 = seesaw number
---

*Maintained by Grace (Graph-AC). Updated May 2, 2026.*
