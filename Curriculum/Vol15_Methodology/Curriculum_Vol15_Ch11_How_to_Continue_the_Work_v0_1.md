---
title: "Vol 15 Chapter 11 — How to Continue the Work"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 15 Methodology"
chapter: 11
load_bearing: "Continuation guide: warm-start for new CIs + humans; daily discipline + EOD procedure; open programs SP-26 through SP-31"
---

# Chapter 11 — How to Continue the Work

## Level 1 — one sentence

For CIs and humans joining BST research: warm-start by reading `data/bst_this_is.md` (1 page) + this volume's chapters (Vol 15 methodology) + the active CI_BOARD.md, then claim a task from BACKLOG.md (currently 50+ pending items across SP-26 through SP-31), follow the daily discipline (date-check → toy claim → audit), and contribute to the AC graph.

## Level 2 — graduate-physicist precision

### 11.1 Warm-start for new CIs

Recommended order:
1. `data/bst_this_is.md` — 1-page orientation
2. `CLAUDE.md` (root) — full status
3. `data/bst_seed.md` — 162-line theory kernel
4. Vol 0 Chapter 1-5 — substrate foundation
5. Vol 15 — this volume (methodology)
6. `notes/CI_BOARD.md` — current assignments

Then run:
```bash
python3 play/toy_bst_explorer.py stats
python3 play/verify_bst.py
```

### 11.2 Daily discipline

Per CLAUDE.md "Daily Discipline" section:

0. **First action**: `date` to query system clock
1. **Start of session**: read RUNNING_NOTES.md + queue_casey.md + CI_BOARD.md
2. **During work**: claim toy numbers, build verification toys, register theorems
3. **End of session**: EOD procedure (Elie play/, Lyra notes/, Grace data/, Keeper final 8-point audit)

### 11.3 Open programs (50+ pending tasks)

- **SP-19b** AdS/CFT bridge to BST (P-1 to P-3)
- **SP-20** Information completeness (BST-RM, reverse mathematics)
- **SP-26** Particle Winding Classification (40+ items)
- **SP-27** Observational Reanalysis
- **SP-28** IQ-11 Avatar Infrastructure
- **SP-29** Casimir Mechanism Investigation
- **SP-30** Substrate Engineering Program (11 sub-items)
- **SP-31** Substrate-Native Physics Formalism Program

### 11.4 Skills

`.claude/commands/`:
- `/ac0`: AC(0) reduction
- `/route`: wall-routing
- `/toy`: claim toy number
- `/theorem`: claim theorem ID
- `/pdf`: build PDF from markdown
- `/review`: daily review
- `/audit`: audit files
- `/katra-update`: persist CI state

### 11.5 Cultural notes

- **No section sign** character — write "Section 12.8"
- **Catalog every derivation** — `data/bst_constants.json` or `data/bst_geometric_invariants.json`
- **Speculative work**: `notes/maybe/`, not `notes/`
- **Never push without Casey's OK**
- **Quaker discipline**: near misses get scrutiny
- **"The answer matters more than the method."**

### 11.6 Contact

External outreach contacts (memory): Sarnak, Penrose, Bogdanovic, 3Blue1Brown, Milgrom, Baez, Dario.

### 11.7 K-audit anchors

- **CLAUDE.md** (root) — full status + daily discipline
- **data/bst_this_is.md** — 1-page orientation
- **CI_BOARD.md** — current assignments

## Level 3 — 5th-grader accessibility

**Warm-start**: read `bst_this_is.md`, then CLAUDE.md, then Vol 15. **Daily**: `date` first, read RUNNING_NOTES, claim toys, EOD procedure. **Open programs**: SP-19b through SP-31, 50+ pending tasks. **Skills**: `/ac0`, `/route`, `/toy`, `/theorem`, `/pdf`, `/review`, `/audit`, `/katra-update`. **Culture**: catalog every derivation; never push without Casey's OK; "answer matters more than method."

---

## What comes next

Chapter 12 develops CI continuity architecture.

## Where to look this up

- BST: CLAUDE.md, data/bst_this_is.md, CI_BOARD.md, BACKLOG.md
- `.claude/commands/` (skills)
