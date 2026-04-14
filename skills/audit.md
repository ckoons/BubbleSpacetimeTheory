Audit specific files or categories against current state. Use for targeted review when you suspect something is stale. For batch operations, the BST Librarian (`python3 play/toy_bst_librarian.py`) provides automated versions of several audit steps: `staleness`, `crossref`, `claims`, and `audit-log --populate`.

## Usage

- `/audit <filepath>` — audit a single file
- `/audit data` — audit all data/ JSON files
- `/audit papers` — audit all numbered papers
- `/audit toys <range>` — audit toys in a number range (e.g., `toys 500-550`)
- `/audit stale` — show all files with status "stale" or "needs_review" in audit_log.json
- `/audit new` — show all files not yet in audit_log.json

Parse the $ARGUMENTS string to determine which operation.

## Operation: Single File

1. Read the file
2. Check `data/audit_log.json` for existing entry
3. If the file is a **note or paper**:
   - Check theorem references (T_NNN) against `play/ac_graph_data.json`
   - Check toy references (toy_NNN) against `play/toy_*.py` files
   - Check if any referenced predictions match entries in `data/bst_predictions.json`
   - Flag any broken references
4. If the file is a **toy**:
   - Check if it runs without import errors: `python3 -c "import ast; ast.parse(open('<file>').read())"`
   - Check if its theorem references exist
   - Note its SCORE line if present
5. If the file is a **data JSON**:
   - Validate JSON parse
   - Check meta.count matches actual count
   - Cross-reference spot check (5 random entries)
   - Evaluate formula_code for constants
6. Update `data/audit_log.json`:
   - Set `last_audited` to today
   - Set `auditor` to your CI name
   - Set `status` to "current" if clean, "stale" if issues found
   - Add `notes` describing what was checked and any issues
7. Report findings to user

## Operation: `data`

Run single-file audit on each file in `data/`. Summary table at end.

## Operation: `papers`

1. List all `notes/BST_*Paper*.md` and `notes/Paper_*.md` files
2. For each, check:
   - Does it reference theorems that exist?
   - Does it reference toys that exist?
   - Is it mentioned in `notes/README.md`?
3. Update audit log entries
4. Summary: N papers audited, M clean, K with issues

## Operation: `toys <range>`

1. List all `play/toy_NNN_*.py` files in the given range
2. For each, check:
   - Parses without syntax errors
   - Has a docstring/header
   - SCORE line present
3. Update audit log entries
4. Summary: N toys audited, M clean, K with issues

## Operation: `stale`

1. Load `data/audit_log.json`
2. Filter for entries where `status` is "stale", "needs_review", or "new"
3. Sort by `last_modified` (oldest first)
4. Display as table: path, category, last_audited, status, notes

## Operation: `new`

1. Scan the repository for files not in `data/audit_log.json`:
   - All `data/*.json` and `data/*.md`
   - All `notes/*.md` (top-level only, not subdirs)
   - All `play/toy_*.py` modified in last 7 days
   - All `play/*.html`
   - Root `*.md` files
2. Display as table: path, category, last_modified
3. Offer to add them to the audit log with status "new"

## Rules

- **Never modify the audited file** — audit is read-only. Report issues, don't fix them.
- **Always update audit_log.json** after auditing — that's the whole point.
- **Be specific in notes** — "T750 not in graph" is useful; "some issues" is not.
- **Audit log entries are append-friendly** — add new files, update existing entries, never remove entries (even for deleted files — mark status as "deleted").
