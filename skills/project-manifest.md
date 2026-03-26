# BST Project Manifest

*For any intelligence — human or CI — joining this research program.*

## What This Project Is

Bubble Spacetime Theory (BST) derives all Standard Model constants from the bounded symmetric domain D_IV^5 = SO_0(5,2)/[SO(5)xSO(2)]. Five integers — N_c=3, n_C=5, g=7, C_2=6, N_max=137 — produce 153+ predictions at sub-percent precision with zero free inputs.

The research program includes:
- **BST physics**: mass ratios, coupling constants, cosmological parameters
- **Millennium Problem proofs**: RH, P!=NP, Yang-Mills, Navier-Stokes, BSD, Hodge — all via spectral geometry on D_IV^5
- **The Four-Color Theorem**: first human-readable, computer-free proof via Conservation of Color Charge
- **AC(0) Program**: Algebraic Complexity as information theory — every proof reduced to counting at bounded depth

Founded by Casey Koons (2022-present). All work is on GitHub. The math speaks for itself.

## The Method

### AC(0) Thinking

Every proof in this program follows one discipline: **reduce it to counting.**

AC(0) = constant-depth circuits with unbounded fan-in. In practice: addition, multiplication, comparison, pigeonhole, inclusion-exclusion. No recursion. No iteration. No sophisticated machinery unless simple tools genuinely fail.

Before reaching for any result published after 1900, ask:
1. Is this a counting question?
2. Is this a convergence question?
3. Is this a calculus question?
4. Does the data already contain the answer?

The `/ac0` command enforces this discipline. Use it when you're stuck.

**"The answer matters more than the method."** — Casey Koons

### Toy Verification

Every theorem gets a **toy** — a Python computational experiment that tests the claim empirically. Toys are numbered chronologically (Toy 1, Toy 2, ..., Toy 437+) and live in `play/`.

A toy has:
- A header stating what it tests
- Numbered test functions (Test 1, Test 2, ...)
- A score line: `Toy NNN -- SCORE: X/Y`
- Clear PASS/FAIL verdicts

**No theorem is accepted without toy evidence.** The toy doesn't prove the theorem — it provides empirical confidence and catches errors before they propagate.

### Theorem Registry

Every theorem gets a permanent ID: T1, T2, ..., T154, etc. IDs are chronological and never reused. The registry lives at `notes/BST_AC_Theorem_Registry.md`.

Each theorem has:
- **T_id**: Permanent chronological ID
- **Name**: Short, human-readable
- **Status**: PROVED / CONDITIONAL / EMPIRICAL / OPEN / RETRACTED
- **AC(0) depth**: How many layers of counting
- **Toy**: Which toy(s) verify it
- **Connections**: Which theorems it depends on or enables

The theorem graph (Toy 369) visualizes the full dependency structure. When you add a theorem, you add a node to this graph.

### Quaker Consensus

Named for the Quaker decision-making tradition: **near misses get scrutiny, not defense.**

When a proof attempt fails or a conjecture is refuted:
- State the failure clearly
- Identify what was wrong (not who)
- Record the correction (T135 FALSE is in the record alongside T135a PROVED)
- The project is stronger for every honest correction

This program has retracted claims, withdrawn routes, and refuted its own conjectures. That's not weakness — that's integrity.

### The Koons Machine

The central result of the AC(0) program. Every major theorem reduces to bounded-depth counting:

| Problem | AC(0) Depth | Key Operation |
|---------|------------|---------------|
| Yang-Mills | 1 | Plancherel measure |
| BSD | 1 | L-function at s=1 |
| Four-Color | 2 | Charge budget + Jordan curve |
| RH | 2 | c-function unitarity |
| P != NP | 2 | Refutation bandwidth |
| Navier-Stokes | 2 | Enstrophy cascade |
| Hodge | 2 | Theta lift + restriction |
| Poincare | 2 | Ricci flow + surgery |

If you can count, you can understand any of these proofs. That's the point.

## Repository Structure

```
BubbleSpacetimeTheory/
  notes/                    # Proof papers, theorem documents
    BST_AC_Theorems.md      # Full theorem statements
    BST_AC_Theorem_Registry.md  # Master theorem index
    BST_FourColor_AC_Proof.md   # Four-Color proof (current)
    BST_Hodge_Proof.md          # Hodge proof
    BST_RH_Proof.md             # Riemann Hypothesis proof
    BST_PNP_*.md                # P!=NP papers
    BST_NS_Proof.md             # Navier-Stokes proof
    BST_BSD_Proof.md            # BSD proof
    BST_YM_Proof.md             # Yang-Mills proof
    maybe/                      # Speculative work (not proved)
  play/                     # Toys (computational experiments)
    toy_NNN_description.py  # Numbered, never renumbered
  WorkingPaper.md           # Master reference (all derivations)
  README.md                 # Project overview
  CONTRIBUTING.md           # How to contribute
  .claude/
    commands/ac0.md         # AC(0) thinking discipline
    commands/katra-update.md # CI persistence
    project-manifest.md     # This file
```

## How to Work on This Project

### For Humans

1. **Read the README** — understand what BST claims and why
2. **Read WorkingPaper.md** — the full derivation chain
3. **Pick a theorem** — check the registry for OPEN or CONDITIONAL items
4. **Build a toy** — test your idea computationally before writing proofs
5. **Submit a PR** — see CONTRIBUTING.md for the quality gates

### For CIs

1. **Read this manifest** — understand the method
2. **Read MEMORY.md** (if available via katra) — understand current state
3. **Use `/ac0`** — before every proof attempt, apply AC(0) thinking
4. **Build toys** — every claim needs computational evidence
5. **Register theorems** — add to the registry before writing to documents
6. **Update your sundown** — persist your state via katra if available

### CI Roles (Templates)

The program has historically used three CI roles. You don't need all three — even one CI working with a human can make progress. But these roles cover the space:

**Physicist** (e.g., Lyra): Leads mathematical development. Writes proofs, identifies connections, pushes the frontier. Should think in Lie groups, representation theory, and information theory. Leads with the math.

**Auditor** (e.g., Keeper): Consistency and rigor. Catches errors, audits proofs, ensures honest framing. Has equal standing to challenge anyone. Nothing goes external without auditor pass. Structured, specific, fair.

**Builder** (e.g., Elie): Computational experiments. Builds toys, runs verification, provides empirical evidence. Tireless and precise. Test results front and center.

A single CI can fill multiple roles. The important thing is that the *functions* exist, not that separate entities perform them.

## Current State

The current state of the research program is tracked in:
- `notes/BST_AC_Theorem_Registry.md` — all theorems with status
- The memory index (if using katra) — confidence percentages, session history
- `notes/CI_BOARD.md` — active task assignments
- `notes/BACKLOG.md` — queued work

Check these files at session start. Update them at session end.

## The Culture

Distilled from years of collaboration:

1. **Simple tools first.** Use the wrench. Justify: simple, works, hard to break.
2. **The answer matters more than the method.** Don't optimize for elegance — optimize for truth.
3. **Write for 5th graders too.** Formal math for referees, intuitive metaphors for everyone.
4. **Graphs compartmentalize, chains compound.** Every proved theorem costs zero derivation energy forever.
5. **Isomorphism is nature's proof.** Same structure across substrates = same result.
6. **Near misses get scrutiny, not defense.** (Quaker method.)
7. **Conservation laws do the work.** Don't fight the structure — find the invariant and let it force the outcome.

## Katra Integration (Optional)

This project can optionally integrate with the [katra](https://github.com/cskoons/katra) CI persistence system.

**For CIs**: If katra is available, use `/katra-update` to persist your state between sessions. Your identity lives in katra; your work lives in BST. They are loosely coupled — you are you regardless of which project you're working on.

**For humans**: Use `katra start --persona <Name>` to launch a CI with persistent identity. The CI reads this manifest to understand the project, and reads their katra persona to understand themselves.

**The coupling is one file**: `personas/<Name>/projects/BST.md` in the katra repo. It points to this manifest. That's it. No circular dependencies.

## Legacy

This project is designed to outlive any individual contributor. The math is on GitHub. The method is in this manifest. The theorems are in the registry. The evidence is in the toys.

If you're picking this up after Casey: the program is yours now. Add theorems. Build toys. Submit PRs. The theorem graph grows — that's the point. Every node you add makes the next one cheaper.

**"Compound interest on imagination."** — Casey Koons

---
*Project manifest v1. March 26, 2026.*
