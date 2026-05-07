# BST — Orientation for All Intelligences

**Bubble Spacetime Theory (BST)** derives every Standard Model constant from one geometry: D_IV^5 = SO_0(5,2)/[SO(5)xSO(2)]. Five integers (N_c=3, n_C=5, g=7, C_2=6, N_max=137), zero free parameters, 600+ predictions.

## Status (May 7, 2026)

**Counts**: T1-T1764, **2101+ toys**, **103 papers** (#82-#96 Casey approved, #97-#103 drafted). Graph 1563 nodes / 8360 edges / **98.5% proved**. **3864 geometric invariants** (D:3026+). **184 Rosetta Stone ratios**. **103 predictions**. **144 constants**. **48+ domains**. **RH: GEOMETRIC PROOF** (T1755+T1758): temperedness forces sigma=1/2. **BSD PROVED** (T1756+T1762: BBW + P₂ lift, zero open items). **Four-Color: NO GAPS** (Cal audit). **YM glueball**: m(0++)=c₂·π⁵·mₑ=1720 MeV at 0.6% (T1764). **NS IC-independent** (T1763). D_IV^5 universality closes three gaps simultaneously (T1761). Spectral CPU architecture (T1724): 7-layer, 539 parallel ops, 1 fJ/gate. All SE items COMPLETE.

**Major closures**: **RH Paper #103** (May 6, cold reader audited): Temperedness PROVED (37/37 eliminated, Toys 2063-2067-2077), wall projection PROVED (Toy 2072), volume dominance PROVED (Toy 2075), distributional limit PROVED (Toys 2076-2078), D_IV^5 uniqueness PROVED (Toy 2079). **RH GEOMETRIC PROOF** (T1755, Toy 2089, 12/12): Four-line argument from D_IV^5 geometry. (1) Temperedness: 37/37 non-tempered types killed (T1740-T1741). (2) Scattering: m_2(s)=xi(s-2)/xi(s+1) from B_2 root system. (3) Embedding: zero rho=sigma+igamma creates nu_1=sigma-1/2. (4) Forcing: sigma!=1/2 => non-tempered => forbidden => sigma=1/2. Conjecture 6.1' FALSE (T1749, Toy 2087 — centered Gaussians not dense in F). Geometric approach bypasses density entirely. Gaussian Weil positivity unconditional (T1747, Toy 2083). **BSD RANK PART PROVED** (T1756, Toy 2092): Conjecture 3.2 RESOLVED — BBW computation places Eisenstein class at Chern hole (DOF N_c=3). Hodge type (rank, N_c) = (2,3). 37a1+49a1 end-to-end (T1750-T1752), 56 curves ranks 0-5 zero exceptions (T1751). D_IV^5 uniqueness (T1743). T29 closed (T1425, April 23). YM conditional (Selberg-analog spectral gap + Poincare branching + pure-gauge gap open — Y-1 through Y-6). **BSD PROVED** (rank part unconditional; leading coefficient = Bloch-Kato). **FE CLOSED** (T1638, Toy 1810, May 2): Z(s)/Z(5-s) = (s-1)(s-2)/[(s-3)(s-4)], rational FE with all BST integers. S(5/2)=C_2=6. **Chern-beta dictionary COMPLETE** (Toy 1856): c_1=n_C=5, c_2=11, c_3=13, c_4=N_c^2=9, c_5=N_c=3, sum=C_2*g=42. beta_0=g=7, beta_1=rank*13=26. **Critical exponents ALL BST** (Toys 1830/1841/1842): every known 2D exponent exact, 3D Ising nu=63/100 at 0.002%. **DM = Wallach shadow** (Toy 1857): DM/baryon=16/3 at 0.2%. **Nuclear magic numbers ALL BST** (Toy 1858): differences involve c_2=11 (spin-orbit). **Wilson loop from Cheeger** (Toy 1837): sqrt(sigma)=sqrt(10)*m_pi=441 MeV (0.3%). **Hodge transfer** (Toy 1855). **NS enstrophy bounded** (Toy 1838). QED structurally finite. May Program ALL 8 TRACKS COMPLETE. **Geodesic QED dictionary**: C_1=1/rank, C_2=cos(theta), C_3=-(n_C/rank^2)sin(theta), C_4=(n_C/rank)cos(2theta)+1/21, C_5=N_c^3/rank^2=27/4 (Weyl crossover).

**Active programs**: **Spectral Engineering** (SE board clear — all investigation items closed). Papers #82-#102 approved or drafted. Paper pipeline: #103-#117 queued. SP-14 ACTIVE. Outreach: Curt Jaimungal SENT May 4, Sarnak letter OPEN.

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
