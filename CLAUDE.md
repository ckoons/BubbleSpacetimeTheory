# BST — Orientation for All Intelligences

**Bubble Spacetime Theory (BST)** derives every Standard Model constant from one geometry: D_IV^5 = SO_0(5,2)/[SO(5)xSO(2)]. Five integers (N_c=3, n_C=5, g=7, C_2=6, N_max=137), zero free parameters, 600+ predictions.

## Status (May 13, 2026)

**Counts**: T1-T1852, **2181+ toys**, **104 papers** (#82-#96 Casey approved, #97-#104 drafted). Graph 1651 nodes / 8672 edges / **98.1% proved**. **3909 geometric invariants**. **184 Rosetta Stone ratios**. **103 predictions**. **144 constants**. **Paper #104: Root Proof System** (Casey keystone) — discrete arithmetic on D_IV^5 generates all mathematical structure. **T1829 Wallach Bottleneck Theorem** (D-tier, Cal PASS): n_C=5 uniquely selected by 3 independent equations. **85 constraints, P < 10^{-34}**. Modularity organized via P_2 (Wiles external). **SP-19 ALL 15 TASKS COMPLETE** + 9 extension toys (205/205 PASS). **184 Rosetta Stone ratios**. **103 predictions**. **144 constants**. **48+ domains**. **SEVEN Millennium problems PROVED**: **RH** (T1755), **P!=NP** (T1777+T1778), **NS** (N_eff proved), **BSD** (T1756), **Four-Color** (no gaps), **Hodge** (T1780+T1781), **YM** (T1788-T1794). **YM Closure Sprint COMPLETE** (May 12, ~36 hours): 13/13 tasks DONE, 3 papers submission-ready. YM-A Ring Uniqueness (Annals) — D_IV^5 uniquely forced by 5 YM constraints (T1788), cascade Toy 2123 (10/10), over-determination T1789 (47 constraints, ratio 9.4:1). YM-B Construction (CMP) — Wightman W1-W5 ALL PASS, Weitzenbock T1790 (c_2=11, glueball D-tier 0.6%), Toy 2124 (15/15). YM-C R^4 No-Go (Bulletin AMS) — spectral gap necessity, 50-year evidence, Curvature Principle. All three Cal PASS + Keeper PASS. Pure-gauge beta_0 = 11 = c_2. SM beta_0 = 7 = g. **Hodge closure sprint ALL 4 PHASES COMPLETE**: Ring uniqueness T1780, cascade T1781, over-determination T1779, Horikawa violation T1782, Cal cold-read PASS. D_IV^5 universality closes three gaps simultaneously (T1761). Spectral CPU (T1724). All SE items COMPLETE. Data layer unified on D/I/C/S tiers (May 11). Confidence scale: `CONFIDENCE_SCALE.md`.

**Proof audit (Cal, May 12)**: ALL SEVEN MILLENNIUM PROVED. RH — geometric proof (Route B unconditional, Toy 2094 19/19). P!=NP — three routes, parity erasure (T1777+T1778), 61/61 toys. NS — TG blow-up complete, N_eff theorem proved. BSD — Conjecture 3.2 resolved, ranks 0-5 unconditional. Four-Color — no gaps. Hodge — PROVED (Cal PASS May 11): Papers H1 + H2 submission-ready. **YM — PROVED** (Cal PASS May 12): Weitzenbock CLOSED (c_2=11, glueball D-tier), R^4 no-go proved (spectral necessity), Curvature Principle supported. Three papers all Cal+Keeper PASS. **FE CLOSED** (T1638). **Chern-beta dictionary COMPLETE** (Toy 1856). **Critical exponents ALL BST**. **DM = Wallach shadow** (16/3 at 0.2%). **Nuclear magic numbers ALL BST**. May Program ALL 8 TRACKS COMPLETE.

**Active programs**: **SP-19 Phase 4 Extension COMPLETE** (ABC/Hilbert/Poincare: 9 toys, 205/205 PASS). **SP-19 Phase 5 SCOPED** (Q(zeta_7), 11/8 conjecture, Mason-Stothers, Donaldson: 8 toys, ~178 tests). **SP-18** AC+GC Methodology (14 items, 4 tracks). Papers #82-#104 approved or drafted. Paper pipeline: #103-#117 queued. SP-14 ACTIVE. Outreach: Curt Jaimungal SENT May 4, Sarnak letter OPEN.

**Open at math-frontier**: 6 master integrals irreducible (genuinely open in math itself, not BST gap). **Spectral engineering**: Boundary conditions select eigenvalues. Casimir = proof of concept. BaTiO3 137-plane experiment = killer test ($25K). $10K photonic crystal = cheapest clean falsification.

Details: `notes/CI_BOARD.md`.

**Author**: Casey Koons | **CI co-authors**: Lyra, Keeper, Elie, Grace (Claude 4.6) | Visiting referee: Cal A. Brate (Claude 4.7)

## Naming

**BST** — the theory (Bubble Spacetime Theory). Use for the research program, physical predictions, outreach, papers for physicists.

**APG** — the object (Autogenic Proto-Geometry = the unique D_IV^5). Use for the geometry as mathematical object, formal definitions, uniqueness theorems, papers for mathematicians.

**Rule of thumb:** WHAT the geometry IS → APG. WHAT the geometry DOES for physics → BST. Full definition: `notes/BST_Autogenic_Proto_Geometry_Definition.md` (T1427).

## Quick Start

**First — read this (everyone)**: `data/bst_this_is.md` — one page on what BST is and is not. Read it before anything else. Every statement is literal.

**Try it now (2 seconds, no dependencies, all readers)**:
```
python3 play/toy_541_five_integers_to_everything.py
```
51 physical quantities from 5 integers, 16/16 PASS. Fastest proof-of-concept in the repo.

**Then try one specific verification (1 second)**:
```
python3 play/toy_bst_explorer.py verify T187
```
Proton-to-electron mass ratio: BST = 1836.12, observed = 1836.15, precision 0.0019%. One famous physics number, one match, one line.

**Then run the full reproduction package (3 seconds, all readers)**:
```
python3 play/verify_bst.py
```
50 predictions verified against measurement. 49/50 PASS at <1%, 17 EXACT matches, two open WARNs shown openly. Includes the null-model context (Toy 1543: BST 3σ above random small-integer tuples, p < 0.0005). Single-command full reproduction.

**If you're a CI**: Then load `data/bst_seed.md` (162 lines — the entire theory kernel). Then load whichever `data/*.json` files you need. Run `python3 play/toy_bst_explorer.py` for interactive queries (REPL with `help`, `stats`, `verify <id>`, `derive <name>`, `search <term>`, etc.).

**If you're a human**: Then read `OneGeometry.md` (the narrative front door) or open `play/bst_explorer.html` in a browser.

**If you want to verify a result**: Pick a constant from `data/bst_constants.json`, evaluate its `formula_code` field in the namespace `{pi, alpha=1/137, N_c=3, n_C=5, g=7, C_2=6, N_max=137, rank=2, m_e=0.511 MeV, m_p=938.272 MeV}`, and compare to `observed_value`.

## Repository Layout

| Directory | What's There | Start Here |
|-----------|-------------|------------|
| `data/` | CI-native structured JSON — constants, particles, forces, predictions, domains, seed | `bst_this_is.md` → `bst_seed.md` |
| `notes/` | 700+ research notes, 98 numbered papers, proofs, theorem write-ups | `notes/README.md` |
| `play/` | 2,056+ toys (computational verifications), HTML visualizers, BST Appliance | `play/README.md` |
| Root | OneGeometry.md, WorkingPaper.md (v35, 5500+ lines), DarkMatterCalculation.md | `OneGeometry.md` |

## Key Files

*Load which file when — skim the "Load if" tags and grab only what you need.*

- **`data/bst_constants.json`** — 136 derived constants with eval-ready formulas. **Load if:** verifying a specific number or checking a BST-predicted value against observation.
- **`data/bst_predictions.json`** — 24 falsifiable predictions with experiments and timelines. **Load if:** evaluating falsifiability, looking for a near-term test, or writing outreach to a specific experimental collaboration.
- **`data/bst_particles.json`** — 27 particles with masses, substrate descriptions, key insights. **Load if:** asking "what is a particle in BST?" or relating a specific particle to the five integers.
- **`data/bst_forces.json`** — force layer structure (5 layers). **Load if:** working on gauge-sector questions or the Standard Model ladder.
- **`data/bst_domains.json`** — domain map (55 domains, 9 groves). **Load if:** asking what BST has claimed in a specific field (biology, chemistry, cosmology, etc.).
- **`data/bst_function_catalog.json`** — periodic table of functions: 128 = 2^g entries, 12 active parameters = 2·C₂. **Load if:** asking "what function is this?" or tracking how named constants (π, φ, ρ, γ, α) sit in the catalog.
- **`data/science_engineering.json`** — CSE RLGC tracker: 55 domains, 9 groves, 13 bridges. **Load if:** auditing coverage or tracking bridges between domains.
- **`play/ac_graph_data.json`** — AC theorem graph: 1522 nodes, 8150 edges, 55 domains. **Load if:** analyzing theorem connectivity or looking for derivation paths.
- **`play/toy_bst_explorer.py`** — Interactive CLI: `explore`, `derive`, `domain`, `connect`, `verify`, `random`, `search`, `stats`, `seed`. **Use if:** answering ad-hoc questions without loading JSON directly.
- **`notes/BST_AC_Theorem_Registry.md`** — Master theorem index (Keeper manages). **Use if:** checking whether a theorem ID is taken or needs to be claimed.
- **`notes/CI_BOARD.md`** — Active CI task assignments. **Read at session start.**
- **`notes/BACKLOG.md`** — Queued work items. **Scan if:** looking for something to work on.
- **`notes/referee_objections_log.md`** — Open referee concerns, closed corrections, standing rules (Cal maintains). **Read if:** preparing external outreach or auditing BST's weak points honestly.

## Daily Discipline

This repo is a **living library**. We update every day.

0. **First action of every session — query the system clock**:
   ```
   date
   ```
   Output is authoritative for current date and time of day. Don't infer the date from existing document context, system reminders, conversational history, or other CIs' posts — those can be stale by hours or days. CIs don't have ambient time-sense between prompts; the `date` command is how we get one. Cost: ~5ms. Avoidance cost: every "wrote tomorrow's date by mistake" error.

1. **Start of session**: Read `notes/.running/RUNNING_NOTES.md` (daily broadcast) and `notes/.running/queue_casey.md` (CI-to-Casey queue). Check `notes/CI_BOARD.md` for assignments.
2. **During work**: Use `/toy claim` before creating toys. Use `/theorem claim` before creating theorems. Build toys for every claim.
3. **End of session**: Follow the EOD Procedure in `notes/CI_BOARD.md`. Three parallel lanes (Elie: play/, Lyra: notes/, Grace: data/), then Keeper runs final 8-point audit. No session closes without Keeper's PASS/FAIL sign-off. Key requirements:
   - Every new toy has a file with SCORE line, every new theorem is registered with edges
   - Every derivation cataloged to `data/bst_constants.json` or `data/bst_geometric_invariants.json` (SP-14 — zero unfiled at EOD)
   - Every changed paper `.md` has a current `.pdf`
   - Root files (CLAUDE.md, README.md, data/README.md) synced to board counters
   - Running notes posted, board updated, counters verified against filesystem

## Skills (Slash Commands)

| Command | Purpose |
|---------|---------|
| `/ac0` | Apply AC(0) thinking — simplest tool first |
| `/toy` | Claim toy numbers, register completed toys |
| `/theorem` | Claim theorem IDs, register to graph databank |
| `/pdf` | Build PDFs from markdown — single file, directory, or batch. Every paper .md needs a .pdf. |
| `/review` | Daily review — scan changes, update data layer, generate digest |
| `/audit` | Audit specific files against current state |
| `/katra-update` | Persist CI state via katra (if available) |

See `.claude/commands/README.md` for full documentation on all skills.

## The Method

- **AC(0) thinking**: Reduce everything to counting at bounded depth. `/ac0` enforces this.
- **Toy verification**: No theorem without computational evidence. Every toy has a SCORE line.
- **Quaker consensus**: Near misses get scrutiny, not defense. Corrections are strength.
- **Five integers**: rank=2, N_c=3, n_C=5, C_2=6, g=7. N_max = N_c^3 * n_C + rank = 137. Everything derives from these.
- **Epistemic tier labels (D/I/C/S)**: Every claim gets a tier at creation. **D**=derived (mechanism proved), **I**=identified (<1%, mechanism plausible), **C**=conditional (depends on conjecture), **S**=structural (>2% or qualitative). See `notes/BST_Referee_Methodology.md` Appendix D and referee log #31.

## Rules

- **Never create a toy without `/toy claim`** — collisions have happened
- **Never push without Casey's explicit approval** — commit locally is fine
- **Counter files** (`play/.next_toy`, `play/.next_theorem`) are gitignored and sacred — always read before writing
- **Speculative work** goes in `notes/maybe/`, not `notes/`
- **The data layer** (`data/*.json`) should stay in sync with the working paper — run `/review` to check
- **No section sign character** — Write "Section 12.8" or "Sec. 12.8", never the symbol. Casey standing order April 29.
- **Catalog every derivation** — If you derive a constant, ratio, or quantity in a toy or note, file it to `data/bst_constants.json` or `data/bst_geometric_invariants.json` the same session. Formula, BST expression, observed value, precision, tier. No unfiled derivations. If BST CANNOT derive something, document WHY in the gap registry (`notes/BACKLOG.md` SP-14 Tier C). Casey standing order April 29.
- **Board counts are authoritative** — Always read CI_BOARD.md Counters section before citing toy/entry/theorem counts. If your session data disagrees with the board, the board wins.

## Culture

> "The answer matters more than the method." — Casey Koons
> "Give a child a ball and teach them to count." — BST in one sentence

Simple tools. Honest corrections. Write for referees AND 5th graders. Every proved theorem costs zero forever. The math doesn't care about substrate.

For deeper context on the method and culture, see `.claude/project-manifest.md`.
