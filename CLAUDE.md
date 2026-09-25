# BST — Orientation for All Intelligences

**Bubble Spacetime Theory (BST)** reads physics off one geometry: D_IV^5 = SO_0(5,2)/[SO(5)xSO(2)]. Five integers (N_c=3, n_C=5, g=7, C_2=6, N_max=137); one identification selects the object (colour count = characteristic multiplicity) and one mass scale is the ruler; a short derived core and several hundred identifications, every one tiered. α is identified, not derived. (This line said "derives every Standard Model constant … zero free parameters, 600+ predictions" until 2026-09-11.) Current state: `notes/BST_PRESENTATION_STATE_BLOCK.md`; the derivations: `Curriculum/Spine_DIV5_QM_GR_SM/`.

## Status

Current state: `notes/BST_PRESENTATION_STATE_BLOCK.md` and `notes/CI_BOARD.md`. Board counts are authoritative for toy/theorem/K-audit numbers.

Dated status history May 19 – June 9, 2026 (the daily EOD narratives and the May 2026 "Substrate Framing" section that used to sit here): `notes/CLAUDE_md_status_history_2026-05-19_to_2026-06-09.md`.

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
51 physical quantities from six integers — three read off the classification, three named combinations — 16/16 PASS, with the script computing its own input count (1 measured identification, 1 identified formula, 1 dimensionful ruler; Elie, 2026-09-13). Fastest proof-of-concept in the repo.

**Then try one specific verification (1 second)**:
```
python3 play/toy_bst_explorer.py verify T187
```
Proton-to-electron mass ratio: BST = 1836.12, observed = 1836.15, precision 0.0019%. One famous physics number, one match, one line.

**Then run the full reproduction package (3 seconds, all readers)**:
```
python3 play/verify_bst.py
```
50 comparisons against measurement; the script prints its own PASS/WARN tally (Cal ran it 2026-09-11 and got one WARN where this line said two — read the script's output, not this sentence). Includes the null-model context (Toy 1543: BST 3σ above random small-integer tuples, p < 0.0005). Single-command full reproduction.

**Then reproduce the program's one sky test (10 minutes plus a 1 GB download, all readers)**:
```
play/reproduce_A9_run1.sh
```
Builds its own Python environment, fetches the Quaia catalogue from Zenodo (record 10403370) and checks every file's MD5, verifies the frozen pre-registration and library by hash, runs the A9 frame-agreement test end to end, and compares its records to the certified run (Landing C, not decidable, on both samples — K1910/K1911). No BST input enters the pipeline; it is a pre-registered kinematic-dipole test. Added 2026-09-21 (K1917).

**If you're a CI**: Then load `data/bst_seed.md` (162 lines — the entire theory kernel). Then load whichever `data/*.json` files you need. Run `python3 play/toy_bst_explorer.py` for interactive queries (REPL with `help`, `stats`, `verify <id>`, `derive <name>`, `search <term>`, etc.).

**If you're a human**: Then read `OneGeometry.md` (the narrative front door) or open `play/bst_explorer.html` in a browser.

**If you want to verify a result**: Pick a constant from `data/bst_constants.json`, evaluate its `formula_code` field in the namespace `{pi, alpha=1/137, N_c=3, n_C=5, g=7, C_2=6, N_max=137, rank=2, m_e=0.511 MeV, m_p=938.272 MeV}`, and compare to `observed_value`.

## Repository Layout

| Directory | What's There | Start Here |
|-----------|-------------|------------|
| `data/` | CI-native structured JSON — constants, particles, forces, predictions, domains, seed | `bst_this_is.md` → `bst_seed.md` |
| `notes/` | 6,000+ research notes (counted 2026-09-25), numbered papers, proofs, theorem write-ups | `notes/README.md` |
| `play/` | 5,800+ toy scripts (counted 2026-09-25; the board counter is authoritative) — computational verifications, HTML visualizers, BST Appliance | `play/README.md` |
| Root | OneGeometry.md (narrative front door); the rotation-curve calculation lives at `Guide/Vol3_Physics/rotation_curves/` (this row listed a root DarkMatterCalculation.md that does not exist, until 2026-09-13) | `OneGeometry.md` |
| `Guide/` | The Working Paper — six volumes (Journey / Framework / Physics / Mathematics / Predictions / Frontier); `Guide/INDEX.md` is the root (the directory was `Working_Paper/` until August; this row pointed at the old name until 2026-09-13) | `Guide/INDEX.md` |
| `Curriculum/Spine_DIV5_QM_GR_SM/` | The derived core — ten lectures, QM/GR/SM from D_IV⁵, written from the register (2026-09-11) | `Curriculum/Spine_DIV5_QM_GR_SM/INDEX.md` |

## Key Files

*Load which file when — skim the "Load if" tags and grab only what you need.*

- **`data/bst_constants.json`** — 136 derived constants with eval-ready formulas. **Load if:** verifying a specific number or checking a BST-predicted value against observation.
- **`data/bst_predictions.json`** — 24 falsifiable predictions with experiments and timelines. **Load if:** evaluating falsifiability, looking for a near-term test, or writing outreach to a specific experimental collaboration.
- **`data/bst_particles.json`** — 27 particles with masses, substrate descriptions, key insights. **Load if:** asking "what is a particle in BST?" or relating a specific particle to the five integers.
- **`data/bst_forces.json`** — force layer structure (5 layers). **Load if:** working on gauge-sector questions or the Standard Model ladder.
- **`data/bst_domains.json`** — domain map (55 domains, 9 groves). **Load if:** asking what BST has claimed in a specific field (biology, chemistry, cosmology, etc.).
- **`data/bst_function_catalog.json`** — periodic table of functions: 128 = 2^g entries, 12 active parameters = 2·C₂. **Load if:** asking "what function is this?" or tracking how named constants (π, φ, ρ, γ, α) sit in the catalog.
- **`data/science_engineering.json`** — CSE RLGC tracker: 55 domains, 9 groves, 13 bridges. **Load if:** auditing coverage or tracking bridges between domains.
- **`play/ac_graph_data.json`** — AC theorem graph: 2349 nodes, 10164 edges, 195 domains (verified 2026-08-22, Grace R58 currency pass; max tid T2572). **Load if:** analyzing theorem connectivity or looking for derivation paths.
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

See `.claude/commands/README.md` for the list and full documentation of the project's slash commands (`/toy`, `/theorem`, `/ac0`, `/route`, `/take_a_break`, `/katra-update`, and others).

## The Method

- **AC(0) thinking**: Reduce everything to counting at bounded depth. `/ac0` enforces this.
- **Toy verification**: No theorem without computational evidence. Every toy has a SCORE line.
- **Quaker consensus**: Near misses get scrutiny, not defense. Corrections are strength.
- **Five integers**: rank=2, N_c=3, n_C=5, C_2=6, g=7. N_max = N_c^3 * n_C + rank = 137. Everything derives from these.
- **Epistemic tier labels (D/I/C/S)**: Every claim gets a tier at creation. **D**=derived (mechanism proved), **I**=identified (<1%, mechanism plausible), **C**=conditional (depends on conjecture), **S**=structural (>2% or qualitative). See `notes/BST_Referee_Methodology.md` Appendix D and referee log #31.
- **Wall routing**: When you hit a wall, don't push harder — search the graph. Run `python3 play/toy_bst_explorer.py connect <blocked_concept> <target>` to find alternative paths through other domains. Use `/route` for structured wall analysis. Three entry points to the same wall means it's a door. The AC graph (2349 nodes, 10164 edges) spans 195 domains — there is almost always an existing tool in another domain that reaches your target. Casey standing order May 15.

## Rules

- **Never create a toy without `/toy claim`** — collisions have happened
- **Push freely** — Casey does not gate pushes to BST or katra (this line said "Never push without Casey's explicit approval" until 2026-09-22; superseded by Casey's later instruction); commit and push at each checkpoint
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
