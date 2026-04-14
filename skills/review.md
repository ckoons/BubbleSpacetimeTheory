Daily review of the BST living library. Run at end of session to keep everything current.

## What This Does

Scans for changes since last review, updates the data layer incrementally, flags stale references, and generates a daily digest. Each step maps to a `toy_bst_librarian.py` subcommand.

## Steps

### 1. Scan for Changes

```bash
python3 play/toy_bst_librarian.py scan --days 1
```

Categorize changes:
- **New toys** (play/toy_*.py not in previous count)
- **New notes** (notes/*.md)
- **Modified papers** (notes/Paper_* or notes/BST_*Paper*)
- **Modified data** (data/*.json)
- **Modified tools** (play/*.py non-toy, play/*.html)

Report: "Today: N new toys, M modified notes, K modified papers."

### 2. Check Counters

```bash
python3 play/toy_bst_librarian.py counters
```

Read `play/.next_toy` and `play/.next_theorem`. Compare to actual highest. Flag drift.

### 3. Update Audit Log

```bash
python3 play/toy_bst_librarian.py audit-log --update
```

Load `data/audit_log.json`. For each file modified today:
- If already in the log: update `last_modified`, set `status` to `needs_review` if content changed significantly
- If new: add entry with `status: "new"`, `last_audited: null`

Save the updated log. For first-time population (adds ~200 entries), use `--populate`.

### 4. Data Layer Staleness Check

```bash
python3 play/toy_bst_librarian.py staleness
```

Check `data/*.json` cross-refs against filesystem. Verify meta.count matches actual counts. Flag missing toy/theorem references.

### 5. Cross-Reference Spot Check

```bash
python3 play/toy_bst_librarian.py crossref --count 5
```

Pick 5 random entries from `data/bst_constants.json`:
- Verify theorem refs exist in `play/ac_graph_data.json`
- Verify source toy files exist in `play/`
- Evaluate `formula_code` and compare to observed values

Report pass/fail counts.

### 6. README Currency Check

```bash
python3 play/toy_bst_librarian.py readme-check
```

Check if `play/README.md` toy count matches actual. Check `notes/README.md` paper count. Check `CLAUDE.md` counts. Report any drift.

### 7. Generate Digest

```bash
python3 play/toy_bst_librarian.py digest
```

Runs all checks and writes summary to `notes/.running/DIGEST_YYYY-MM-DD.md`.

### 8. Update RUNNING_NOTES

Append a brief "Library status" section to `notes/.running/RUNNING_NOTES.md` so the next CI session sees the current state.

## When to Run

- **Always** at end of a productive session (new toys, theorems, or papers created)
- **Optionally** at start of session to see what changed overnight
- **Weekly**: do a fuller review — audit 10 random files from the log instead of 5

## Arguments

- `/review` — full daily review (all 8 steps)
- `/review quick` — steps 1-3 only (scan + counters + audit log)
- `/review data` — steps 4-5 only (staleness + cross-refs)
- `/review digest` — step 7 only (generate digest from existing data)
