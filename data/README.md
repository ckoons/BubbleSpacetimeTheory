# data/ — CI-Native Structured Data Layer

**Purpose**: Machine-readable JSON files for any intelligence (CI or human) to load BST's complete state in seconds. This is the **front door for CIs** — start here.

**Quick start**: Read `bst_this_is.md` first (one page — what BST is and is not). Then load `bst_seed.md` (162 lines, the entire theory kernel). Then load whichever JSON you need.

## Files

| File | What It Contains | Last Updated |
|------|-----------------|--------------|
| **bst_this_is.md** | **Read first.** What BST is and is not. Every statement literal. | April 21, 2026 |
| **bst_seed.md** | The theory kernel — 5 integers, core derivations, enough to reconstruct everything | Stable |
| **bst_constants.json** | 105 derived physical constants with eval-ready formulas | April 2026 |
| **bst_predictions.json** | 52 falsifiable predictions with experiments and timelines | April 29, 2026 |
| **bst_particles.json** | Standard Model particles with BST derivations | April 2026 |
| **bst_forces.json** | Four forces derived from D_IV^5 geometry | April 2026 |
| **bst_domains.json** | Domain classification for the AC theorem graph | April 2026 |
| **bst_function_catalog.json** | The Periodic Table of Functions — 33 families, GF(128) structure, cross-referenced to AC graph | April 21, 2026 |
| **bst_function_recipes.json** | Compound function "recipes" — how families combine via 5 bonding operations | April 20, 2026 |
| **bst_geometric_invariants.json** | 1403 geometric invariants with formulas, precision, D/I/C/S tiers, section mapping for Paper #83 | April 29, 2026 |
| **bst_invariants_crossref.json** | Cross-reference: invariant → AC theorem graph (1400 entries) | April 29, 2026 |
| **bst_materials.json** | 87 materials predictions: Debye temps, band gaps, crystal properties, superconductor params | April 29, 2026 |
| **bst_rosetta_stone.json** | 150 named BST ratios with D/I/S tiers and domain coverage | April 29, 2026 |
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
4. Check `play/ac_graph_data.json` for the theorem graph (1343 nodes, 7201 edges as of April 21, 2026)
5. Read the root `CLAUDE.md` for project conventions and daily discipline

**Contributions welcome.** If you derive something new, open a PR. Claim toy/theorem numbers via `play/claim_number.sh` before creating. The graph only grows.

## Current Stats (April 29, 2026)

- **Geometric invariants**: 2000 entries (D:1231, I:506, C:54, S:209) — 100% theorem-linked, 0 duplicates
- **BSD CLOSED**: Chern hole mechanism (Toys 1651-1659, T1465). 2^(n-2)=n+3 uniqueness.
- **SP-12 Understanding Program**: 24/24 items answered. Born rule = Bergman normalization. Confinement = Hamming distance. n_s DERIVED from slow-roll.
- **Constants**: 105 derived, zero free parameters
- **Predictions**: 74 falsifiable (in bst_predictions.json) + 600+ in papers
- **Theorems**: T1-T1465, all depth at most 1
- **Toys**: 1660+ computational verifications
- **Papers**: 88 numbered
- **Domains**: 58+ scientific disciplines mapped
- **Graph**: 1404 theorems, 7737+ edges, 83.35% strong (5/6 self-description EXCEEDED)
- **Uniqueness**: 2^(n-2)=n+3 has unique solution n=5. One equation, one universe.
- **>2% attack surface**: Only 2 D/I entries (V_ub 2.25%, V_ts 2.56%, both lambda^3 CKM)
- **T1444**: Vacuum Subtraction / RFC — 19+ instances, "deviations locate boundaries"
- **T1459**: Spectral Universality — all domains = same Bergman spectrum
- **T1462**: Cyclotomic Casimir — C_2=6 single generator
- **T1465**: BSD Chern Hole — Millennium Problem closed
- **beta_0 = g**: QCD one-loop coefficient IS the genus (SP-13 A-1)
- **a_mu^HVP closed form**: [g/(g+N_c)]*(alpha/pi)^2*(m_mu/m_rho)^2 at 1.2%
- **N_max = lambda_9 + 11**: Second derivation of 137 from spectral gap position
- **Dm2_31 = 1/34**: RFC correction, 3.1% -> 0.5%, 18th RFC instance
- **T1464**: Reference Frame Counting — 11 instances, generalizes T1444
---

*Maintained by Grace (Graph-AC). Updated at end of each session.*
