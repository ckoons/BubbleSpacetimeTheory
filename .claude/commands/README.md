# BST Skills (Slash Commands)

**Purpose**: Slash commands any CI can invoke during a session. Each `.md` file in this directory defines one skill. Type `/<name>` to run it.

## Available Skills

| Command | File | What It Does |
|---------|------|-------------|
| `/ac0` | `ac0.md` | Apply AC(0) thinking — reduce to counting at bounded depth. Use when stuck. |
| `/audit` | `audit.md` | Audit specific files against current repo state. Cross-check claims, references, consistency. |
| `/katra-update` | `katra-update.md` | Persist CI identity state via katra system (sunrise/sundown cycle). |
| `/pdf` | `pdf.md` | Build PDFs from markdown files. Single file, directory scan, or batch. Every paper .md needs a .pdf. |
| `/review` | `review.md` | Daily review — scan changes, update data layer, flag stale references, generate digest. |
| `/theorem` | `theorem.md` | Claim theorem IDs and register to the AC graph databank. Prevents collisions. |
| `/toy` | `toy.md` | Claim toy numbers and register completed toys. MUST be called before creating any toy file. |

## How Skills Work

Each `.md` file contains:
1. A description of what the skill does
2. Usage patterns (e.g., `/toy claim`, `/toy register NNN "Title" X/Y`)
3. Step-by-step instructions the CI follows when the skill is invoked
4. Rules and edge cases

When you type `/<name>` or `/<name> arguments`, the system loads the corresponding `.md` and the CI follows its instructions.

## Adding a New Skill

1. Create `<name>.md` in this directory
2. Follow the pattern: description, usage, operations, rules
3. Update this README
4. Update `CLAUDE.md`'s Skills table
5. Test it in a session

## Daily Use

| When | Skills |
|------|--------|
| Start of session | `/review` (see what changed) |
| Creating a toy | `/toy claim` (BEFORE writing the file) |
| Creating a theorem | `/theorem claim` (BEFORE writing the file) |
| End of session | `/pdf check` (find missing PDFs), `/pdf <dir>` (build them) |
| When stuck | `/ac0` (simplify) |
| Auditing | `/audit <file>` (check consistency) |

## PDF Pipeline Quick Reference

```bash
pandoc INPUT.md -o OUTPUT.pdf --pdf-engine=xelatex -H notes/bst_pdf_header.tex -V geometry:margin=1in
```

Requirements: `pandoc` + `xelatex` + STIX Two Text font. All installed on this system.
