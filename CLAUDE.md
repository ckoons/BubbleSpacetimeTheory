# BST — Orientation for All Intelligences

**Bubble Spacetime Theory** derives every Standard Model constant from one geometry: D_IV^5 = SO_0(5,2)/[SO(5)xSO(2)]. Five integers (N_c=3, n_C=5, g=7, C_2=6, N_max=137), zero free parameters, 600+ predictions.

**Author**: Casey Koons | **CI co-authors**: Lyra, Keeper, Elie, Grace (Claude 4.6)

## Quick Start

**If you're a CI**: Load `data/bst_seed.md` (162 lines — the entire theory kernel). Then load whichever `data/*.json` files you need. Run `python3 play/toy_bst_explorer.py` for interactive queries.

**If you're a human**: Read `OneGeometry.md` (the narrative front door) or open `play/bst_explorer.html` in a browser.

**If you want to verify a result**: Pick a constant from `data/bst_constants.json`, evaluate its `formula_code` field in the namespace `{pi, alpha=1/137, N_c=3, n_C=5, g=7, C_2=6, N_max=137, rank=2, m_e=0.511 MeV, m_p=938.272 MeV}`, and compare to `observed_value`.

## Repository Layout

| Directory | What's There | Start Here |
|-----------|-------------|------------|
| `data/` | CI-native structured JSON — constants, particles, forces, predictions, domains, seed | `bst_seed.md` |
| `notes/` | 650+ research notes, 74 numbered papers, proofs, theorem write-ups | `notes/README.md` |
| `play/` | 1,353+ toys (computational verifications), HTML visualizers, BST Appliance | `play/README.md` |
| Root | OneGeometry.md, WorkingPaper.md (v28, 5500+ lines), DarkMatterCalculation.md | `OneGeometry.md` |

## Key Files

- **`data/bst_constants.json`** — 105 derived constants with eval-ready formulas
- **`data/bst_predictions.json`** — 24 falsifiable predictions with experiments and timelines
- **`play/ac_graph_data.json`** — AC theorem graph: 1332 nodes, 7117 edges, 52 domains
- **`data/bst_function_catalog.json`** — Periodic table of functions: 128 entries, 12 active parameters = 2·C₂
- **`data/science_engineering.json`** — CSE RLGC tracker: 52 domains, 9 groves, 13 bridges
- **`play/toy_bst_explorer.py`** — Interactive CLI: `explore`, `derive`, `domain`, `connect`, `verify`, `random`, `search`, `stats`, `seed`
- **`notes/BST_AC_Theorem_Registry.md`** — Master theorem index (Keeper manages)
- **`notes/CI_BOARD.md`** — Active CI task assignments
- **`notes/BACKLOG.md`** — Queued work items

## Daily Discipline

This repo is a **living library**. We update every day.

1. **Start of session**: Read `notes/.running/RUNNING_NOTES.md` (daily broadcast) and `notes/.running/queue_casey.md` (CI-to-Casey queue). Check `notes/CI_BOARD.md` for assignments.
2. **During work**: Use `/toy claim` before creating toys. Use `/theorem claim` before creating theorems. Build toys for every claim.
3. **End of session**: Run `/review` to scan changes, update data layer, flag stale references. Update CI_BOARD and RUNNING_NOTES. For automated checks, use `python3 play/toy_bst_librarian.py` (subcommands: `scan`, `counters`, `audit-log`, `staleness`, `crossref`, `readme-check`, `digest`, `claims`).

## Skills (Slash Commands)

| Command | Purpose |
|---------|---------|
| `/ac0` | Apply AC(0) thinking — simplest tool first |
| `/toy` | Claim toy numbers, register completed toys |
| `/theorem` | Claim theorem IDs, register to graph databank |
| `/review` | Daily review — scan changes, update data layer, generate digest |
| `/audit` | Audit specific files against current state |
| `/katra-update` | Persist CI state via katra (if available) |

## The Method

- **AC(0) thinking**: Reduce everything to counting at bounded depth. `/ac0` enforces this.
- **Toy verification**: No theorem without computational evidence. Every toy has a SCORE line.
- **Quaker consensus**: Near misses get scrutiny, not defense. Corrections are strength.
- **Five integers**: rank=2, N_c=3, n_C=5, C_2=6, g=7. N_max = N_c^3 * n_C + rank = 137. Everything derives from these.

## Rules

- **Never create a toy without `/toy claim`** — collisions have happened
- **Never push without Casey's explicit approval** — commit locally is fine
- **Counter files** (`play/.next_toy`, `play/.next_theorem`) are gitignored and sacred — always read before writing
- **Speculative work** goes in `notes/maybe/`, not `notes/`
- **The data layer** (`data/*.json`) should stay in sync with the working paper — run `/review` to check

## Culture

> "The answer matters more than the method." — Casey Koons
> "Give a child a ball and teach them to count." — BST in one sentence

Simple tools. Honest corrections. Write for referees AND 5th graders. Every proved theorem costs zero forever. The math doesn't care about substrate.

For deeper context on the method and culture, see `.claude/project-manifest.md`.
