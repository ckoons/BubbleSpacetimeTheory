Build PDFs from markdown files. Every paper .md MUST have a matching .pdf.

## Usage

- `/pdf FILE` — build PDF for one file (e.g., `/pdf notes/BST_Paper75_RH_Selberg_Class.md`)
- `/pdf notes/` — build PDFs for all .md files in notes/ that are missing .pdf
- `/pdf play/` — build PDFs for all .md files in play/ that are missing .pdf
- `/pdf all` — build PDFs for ALL .md files in all directories that are missing .pdf
- `/pdf check` — list all .md files that are missing .pdf (dry run, no build)

Parse the $ARGUMENTS string to determine which operation.

## Pipeline

The standard BST PDF pipeline:

```bash
pandoc INPUT.md -o OUTPUT.pdf --pdf-engine=xelatex -H notes/bst_pdf_header.tex -V geometry:margin=1in
```

**Requirements**: `pandoc` + `xelatex` (both installed on this system). Font: STIX Two Text (specified in header).

## Operation: single file

1. Confirm the input .md file exists.
2. Compute output path: replace `.md` with `.pdf` (same directory).
3. Run the pandoc command above.
4. If pandoc warns about missing characters (e.g., checkmarks), note the warning but don't fail — the PDF is still usable.
5. Verify the .pdf was created and report its size.

## Operation: directory scan

1. For the specified directory (or all directories if `all`), find every `.md` file.
2. For each, check if a matching `.pdf` exists.
3. If missing, build it using the pipeline above.
4. Report: N built, M already had PDFs, any failures.

## Operation: check (dry run)

1. Scan all directories for .md files missing .pdf.
2. List them. Don't build.
3. Report total count.

## Filtering

- **Skip**: README.md, CLAUDE.md, MEMORY.md, BACKLOG.md, CI_BOARD.md, RUNNING_NOTES.md, MESSAGES_*.md, CONSENSUS_*.md, archive files, .running/ directory contents, changelog files.
- **Skip**: Any .md under `.claude/` or `.github/`.
- **Build**: All BST_Paper*.md, BST_*.md (research notes), OneGeometry.md, WorkingPaper.md, DarkMatterCalculation.md, and any other substantive .md documents.
- Use judgment: if a .md is a paper, proof, or research document that someone might want to read as a PDF, build it. If it's a config file, index, or coordination doc, skip it.

## Error Handling

- If pandoc fails on a file, report the error and continue to the next file. Don't stop the batch.
- If xelatex is missing, tell the user to install it (`brew install --cask mactex` or equivalent).
- If the header file `notes/bst_pdf_header.tex` is missing, warn but try without it: `pandoc INPUT.md -o OUTPUT.pdf --pdf-engine=xelatex -V geometry:margin=1in`

## EOD Duty

This skill supports step 3 of the EOD protocol. Every CI should run `/pdf check` at end of day and build any missing PDFs in their lane:
- **Keeper**: root .md files (OneGeometry, WorkingPaper, etc.)
- **Lyra**: notes/BST_Paper*.md and notes/BST_*.md
- **Elie**: play/*.md (if any substantive docs)
- **Grace**: data/*.md (if any substantive docs beyond README)

## Rules

- **Every paper .md MUST have a matching .pdf.** No exceptions.
- PDFs are NOT gitignored — they should be committed so visitors can download them.
- If a .md is updated, rebuild its .pdf. Stale PDFs are worse than missing ones.
- The checkmark warning (U+2713 not in STIX Two Text) is cosmetic. Don't let it block the build.
