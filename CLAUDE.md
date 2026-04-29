# BST — Orientation for All Intelligences

**Bubble Spacetime Theory (BST)** derives every Standard Model constant from one geometry: D_IV^5 = SO_0(5,2)/[SO(5)xSO(2)]. Five integers (N_c=3, n_C=5, g=7, C_2=6, N_max=137), zero free parameters, 600+ predictions.

## Status (April 29, 2026)

**Counts**: T1-T1465, **1708+ toys**, **88 papers**. Graph 1404 nodes / 7745 edges / **98.4% proved** / 83.4% strong. **2233 geometric invariants** (D:1387, I:531, C:58, S:257). **170 Rosetta Stone ratios**. **80 predictions**. **127 constants** in data layer.

**Major closures**: RH closed (T1398, April 21). T29 closed (T1425, April 23). **BSD CLOSED** (Toy 1659, April 29). C₄ full assembly 13/13 PASS. Heat kernel k=21 confirmed: ratio = -42 = -C₂·g, twenty consecutive integer levels. Cremona 49a1 = BST's canonical elliptic curve. T1459 Spectral Universality proved. Koide formula at 0.0009%. T1462 Cyclotomic Casimir. T1464 RFC (Reference Frame Counting): 12 instances. **SP-15 breakthrough: QED zeta ladder** — each loop introduces zeta at next BST prime: L=2→zeta(N_c), L=3→zeta(n_C), L=4→zeta(g). C₂^QED exact BST decomposition (K-32, machine precision). RFC pattern in all QED coefficients: every numerator = BST product - 1. QED structurally finite (3 transcendentals only).

**Active programs**: Paper #88 v0.1 (BSD Closure, target Inventiones); Paper #87 (Error Correction); Paper #86 v1.1 (Selberg g-2 capstone, CMP); Paper #83 v4.5 (2174 Geometric Invariants, submission-ready); **SP-15 Series → Closed Form** (zeta ladder + RFC pattern); **SP-14 Derivation Catalog Discipline** (Casey directive April 29); **3200-dps heat kernel compute RUNNING** (k=22+ extraction).

**Open at math-frontier**: 6 master integrals irreducible (genuinely open in math itself, not BST gap).

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
| `notes/` | 660+ research notes, 88 numbered papers, proofs, theorem write-ups | `notes/README.md` |
| `play/` | 1,690+ toys (computational verifications), HTML visualizers, BST Appliance | `play/README.md` |
| Root | OneGeometry.md, WorkingPaper.md (v28, 5500+ lines), DarkMatterCalculation.md | `OneGeometry.md` |

## Key Files

*Load which file when — skim the "Load if" tags and grab only what you need.*

- **`data/bst_constants.json`** — 105 derived constants with eval-ready formulas. **Load if:** verifying a specific number or checking a BST-predicted value against observation.
- **`data/bst_predictions.json`** — 24 falsifiable predictions with experiments and timelines. **Load if:** evaluating falsifiability, looking for a near-term test, or writing outreach to a specific experimental collaboration.
- **`data/bst_particles.json`** — 27 particles with masses, substrate descriptions, key insights. **Load if:** asking "what is a particle in BST?" or relating a specific particle to the five integers.
- **`data/bst_forces.json`** — force layer structure (5 layers). **Load if:** working on gauge-sector questions or the Standard Model ladder.
- **`data/bst_domains.json`** — domain map (55 domains, 9 groves). **Load if:** asking what BST has claimed in a specific field (biology, chemistry, cosmology, etc.).
- **`data/bst_function_catalog.json`** — periodic table of functions: 128 = 2^g entries, 12 active parameters = 2·C₂. **Load if:** asking "what function is this?" or tracking how named constants (π, φ, ρ, γ, α) sit in the catalog.
- **`data/science_engineering.json`** — CSE RLGC tracker: 55 domains, 9 groves, 13 bridges. **Load if:** auditing coverage or tracking bridges between domains.
- **`play/ac_graph_data.json`** — AC theorem graph: 1399+ nodes, 7732+ edges, 55 domains. **Load if:** analyzing theorem connectivity or looking for derivation paths.
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
3. **End of session**: Run your EOD lane, then update CI_BOARD and RUNNING_NOTES.
   - **Keeper**: Root files (WorkingPaper stats, OneGeometry, README.md, CLAUDE.md)
   - **Lyra**: `notes/` (paper status, theorem files, `notes/README.md`)
   - **Elie**: `play/` (toy registry, graph data, `play/README.md`)
   - **Grace**: `data/` (JSON sync, `data/README.md`, CI onboarding path)
   - For automated checks, use `python3 play/toy_bst_librarian.py` (subcommands: `scan`, `counters`, `audit-log`, `staleness`, `crossref`, `readme-check`, `digest`, `claims`).
4. **EOD catalog cleanup** (standing daily function, Casey directive April 29):
   - Check all toys created this session for unfiled derivations
   - Any new constant, ratio, or quantity → file to `data/bst_constants.json` or `data/bst_geometric_invariants.json`
   - Any constant BST cannot derive → document WHY in `notes/BACKLOG.md` SP-14 Tier C
   - SP-14 enforces this. No unfiled derivations at end of day.

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
