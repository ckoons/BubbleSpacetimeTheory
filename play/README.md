# BST Toy Collection & Interactive Tools

**1,322+ computational toys, 4 interactive HTML visualizers, and the BST Appliance for Bubble Spacetime Theory.**

*Copyright (c) 2026 Casey Koons. All rights reserved.*
*Demonstration only. No license is granted for redistribution, modification, or commercial use.*

---

## Scale Summary

| Metric | Count |
|--------|-------|
| Toy scripts (toy_*.py) | 1,322+ |
| Numbered toys (toy_NNN_*.py) | 1,091+ |
| Named toys (toy_name.py) | 209 |
| Utility scripts (non-toy .py) | 56 |
| HTML visualizers | 4 |
| Theorems (T1-T1347) | 1,347 |
| Next toy number | 1323 |
| Predictions | 600+ |
| Domains touched | 130+ |
| Free parameters | **0** |

Five integers. Zero free parameters. "Give a child a ball and teach them to count."

---

## Directory Layout

```
play/
  toy_NNN_name.py          # Numbered toys (986 files, T200-T1181)
  toy_name.py              # Named toys (208 files, foundational + topical)
  *.py                     # Utility scripts (56 files: graph tools, extractors, verifiers)
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
| `bst_predictions.json` | 507+ testable predictions with status and precision |
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
| `.next_toy` | 1323 | Next available toy number |
| `.next_theorem` | 1348 | Next available theorem number |

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

The 208 named toys include the original foundational collection and topical deep-dives. These are the toys described in detail below under "Foundational Toys."

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
