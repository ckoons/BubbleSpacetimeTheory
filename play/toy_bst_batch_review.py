#!/usr/bin/env python3
"""
BST Batch Review Tool — Review notes/ files in batches of 50.

Usage:
    python3 play/toy_bst_batch_review.py status          # Show review progress
    python3 play/toy_bst_batch_review.py batch 1         # Review batch 1 (files 1-50)
    python3 play/toy_bst_batch_review.py batch 2         # Review batch 2 (files 51-100)
    python3 play/toy_bst_batch_review.py batch all       # Review all remaining batches
    python3 play/toy_bst_batch_review.py summary         # Summary of all reviewed files

Each file is checked for:
  - Parseable (not corrupted)
  - Theorem references (T_NNN) — checked against ac_graph_data.json
  - Toy references (Toy NNN, toy_NNN) — checked against play/ directory
  - File size and line count

Results are written to data/audit_log.json automatically.
"""

import os
import sys
import re
import json
import glob
from datetime import date

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES_DIR = os.path.join(REPO, "notes")
PLAY_DIR = os.path.join(REPO, "play")
AUDIT_LOG = os.path.join(REPO, "data", "audit_log.json")
GRAPH_FILE = os.path.join(REPO, "play", "ac_graph_data.json")
BATCH_SIZE = 50

# Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"


def load_graph_tids():
    """Load all theorem IDs from the AC graph."""
    with open(GRAPH_FILE) as f:
        g = json.load(f)
    return {t["tid"] for t in g["theorems"]}


def load_toy_files():
    """Load set of existing toy numbers and named toy files."""
    toys = set()
    named = set()
    for f in glob.glob(os.path.join(PLAY_DIR, "toy_*.py")):
        base = os.path.basename(f)
        named.add(base)
        m = re.match(r"toy_(\d+)_", base)
        if m:
            toys.add(int(m.group(1)))
    # Also check named toys that ARE numbered in their docstring (like toy_ac_classification.py = Toy 233)
    return toys, named


def load_audit_log():
    with open(AUDIT_LOG) as f:
        return json.load(f)


def save_audit_log(log):
    with open(AUDIT_LOG, "w") as f:
        json.dump(log, f, indent=2, ensure_ascii=False)


def get_unlogged_notes():
    """Get all notes/*.md files not yet in the audit log."""
    all_notes = sorted([
        f"notes/{f}" for f in os.listdir(NOTES_DIR)
        if f.endswith(".md") and not f.startswith(".")
    ])
    log = load_audit_log()
    logged_paths = {e["path"] for e in log["files"]}
    return [f for f in all_notes if f not in logged_paths]


def get_needs_review():
    """Get files with status 'new' or 'needs_review'."""
    log = load_audit_log()
    return [e for e in log["files"]
            if e.get("status") in ("new", "needs_review")
            and e["path"].startswith("notes/")]


def review_file(filepath, graph_tids, toy_numbers, toy_names):
    """Review a single notes/ file. Returns (status, notes)."""
    full_path = os.path.join(REPO, filepath)
    if not os.path.exists(full_path):
        return "deleted", "File not found"

    try:
        with open(full_path, encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return "stale", f"Read error: {e}"

    lines = content.split("\n")
    issues = []

    # Check theorem references
    thm_refs = set(re.findall(r"\bT(\d{3,4})\b", content))
    broken_thms = []
    for t in thm_refs:
        tid = int(t)
        if tid > 10 and tid not in graph_tids:  # skip small numbers that might not be theorem refs
            broken_thms.append(f"T{t}")
    if broken_thms:
        issues.append(f"Broken thm refs: {', '.join(sorted(broken_thms)[:5])}"
                      + (f" +{len(broken_thms)-5} more" if len(broken_thms) > 5 else ""))

    # Check toy references
    toy_refs = set(re.findall(r"[Tt]oy[\s_](\d{3,4})", content))
    broken_toys = []
    for t in toy_refs:
        tnum = int(t)
        if tnum not in toy_numbers:
            # Check if it's a named toy with that number in its docstring
            pattern = f"toy_{t}_"
            if not any(pattern in name for name in toy_names):
                broken_toys.append(f"Toy {t}")
    if broken_toys:
        issues.append(f"Broken toy refs: {', '.join(sorted(broken_toys)[:5])}"
                      + (f" +{len(broken_toys)-5} more" if len(broken_toys) > 5 else ""))

    # Build notes string
    note_parts = []
    note_parts.append(f"{len(lines)} lines")
    note_parts.append(f"{len(thm_refs)} thm refs")
    note_parts.append(f"{len(toy_refs)} toy refs")
    if issues:
        note_parts.extend(issues)

    status = "needs_review" if issues else "current"
    return status, ". ".join(note_parts)


def cmd_status():
    """Show review progress."""
    unlogged = get_unlogged_notes()
    needs = get_needs_review()
    log = load_audit_log()
    notes_in_log = [e for e in log["files"] if e["path"].startswith("notes/")]
    current = [e for e in notes_in_log if e.get("status") == "current"]

    total_notes = len([f for f in os.listdir(NOTES_DIR) if f.endswith(".md") and not f.startswith(".")])

    print(f"\n{BOLD}Notes Review Progress{RESET}")
    print(f"{'='*50}")
    print(f"  Total notes/*.md files:  {total_notes}")
    print(f"  {GREEN}Reviewed (current):{RESET}      {len(current)}")
    print(f"  {YELLOW}In log (needs_review):{RESET}  {len([e for e in notes_in_log if e.get('status')=='needs_review'])}")
    print(f"  {YELLOW}In log (new):{RESET}            {len([e for e in notes_in_log if e.get('status')=='new'])}")
    print(f"  {RED}Not yet in log:{RESET}          {len(unlogged)}")
    print()

    batches = (len(unlogged) + BATCH_SIZE - 1) // BATCH_SIZE
    print(f"  Batches remaining:       {batches} (of {BATCH_SIZE} files each)")
    if unlogged:
        print(f"  Next batch starts at:    {unlogged[0]}")
    print()


def cmd_batch(batch_num):
    """Review a batch of files."""
    unlogged = get_unlogged_notes()
    if not unlogged:
        print(f"{GREEN}All notes/ files are in the audit log!{RESET}")
        return

    total_batches = (len(unlogged) + BATCH_SIZE - 1) // BATCH_SIZE

    if batch_num == "all":
        batches_to_run = list(range(1, total_batches + 1))
    else:
        batch_num = int(batch_num)
        if batch_num < 1 or batch_num > total_batches:
            print(f"{RED}Invalid batch {batch_num}. Valid range: 1-{total_batches}{RESET}")
            return
        batches_to_run = [batch_num]

    # Load resources once
    graph_tids = load_graph_tids()
    toy_numbers, toy_names = load_toy_files()
    log = load_audit_log()
    logged_paths = {e["path"] for e in log["files"]}

    total_reviewed = 0
    total_clean = 0
    total_issues = 0

    for bn in batches_to_run:
        start = (bn - 1) * BATCH_SIZE
        end = min(start + BATCH_SIZE, len(unlogged))
        batch_files = unlogged[start:end]

        print(f"\n{BOLD}Batch {bn}/{total_batches} — {len(batch_files)} files{RESET}")
        print(f"{'='*60}")

        for filepath in batch_files:
            status, notes = review_file(filepath, graph_tids, toy_numbers, toy_names)

            # Determine category
            basename = os.path.basename(filepath)
            if re.match(r"BST_Paper\d+_", basename) or re.match(r"Paper_", basename):
                category = "paper"
            elif re.match(r"BST_T\d+_", basename):
                category = "note"
            else:
                category = "note"

            # Color output
            if status == "current":
                sym = f"{GREEN}OK{RESET}"
                total_clean += 1
            elif status == "needs_review":
                sym = f"{YELLOW}!!{RESET}"
                total_issues += 1
            else:
                sym = f"{RED}XX{RESET}"
                total_issues += 1

            short_name = basename[:50] + ("..." if len(basename) > 50 else "")
            print(f"  {sym}  {short_name}")
            if status != "current":
                # Print issue details
                for part in notes.split(". "):
                    if "Broken" in part:
                        print(f"       {YELLOW}{part}{RESET}")

            # Add to audit log
            if filepath not in logged_paths:
                try:
                    mtime = os.path.getmtime(os.path.join(REPO, filepath))
                    mod_date = date.fromtimestamp(mtime).isoformat()
                except:
                    mod_date = str(date.today())

                log["files"].append({
                    "path": filepath,
                    "category": category,
                    "last_audited": str(date.today()),
                    "auditor": "batch_review",
                    "status": status,
                    "last_modified": mod_date,
                    "notes": notes
                })
                logged_paths.add(filepath)
            total_reviewed += 1

        print(f"\n  Batch {bn}: {total_clean} clean, {total_issues} with issues")

    # Save updated log
    log["meta"]["last_updated"] = str(date.today())
    save_audit_log(log)
    print(f"\n{BOLD}Total: {total_reviewed} reviewed, {total_clean} clean, {total_issues} with issues{RESET}")
    print(f"Audit log updated ({len(log['files'])} total entries)")


def cmd_summary():
    """Show summary of all reviewed files with issues."""
    log = load_audit_log()
    notes = [e for e in log["files"] if e["path"].startswith("notes/")]

    by_status = {}
    for e in notes:
        s = e.get("status", "unknown")
        by_status.setdefault(s, []).append(e)

    print(f"\n{BOLD}Review Summary — notes/{RESET}")
    print(f"{'='*50}")
    for status in ["current", "needs_review", "new", "stale", "deleted"]:
        entries = by_status.get(status, [])
        if entries:
            color = GREEN if status == "current" else YELLOW if status in ("needs_review", "new") else RED
            print(f"\n  {color}{status}: {len(entries)}{RESET}")
            if status in ("needs_review", "stale"):
                for e in sorted(entries, key=lambda x: x["path"])[:20]:
                    print(f"    {e['path']}")
                    if e.get("notes") and "Broken" in e["notes"]:
                        for part in e["notes"].split(". "):
                            if "Broken" in part:
                                print(f"      {YELLOW}{part}{RESET}")
                if len(entries) > 20:
                    print(f"    ... +{len(entries)-20} more")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1]
    if cmd == "status":
        cmd_status()
    elif cmd == "batch":
        if len(sys.argv) < 3:
            print("Usage: batch <number|all>")
            sys.exit(1)
        cmd_batch(sys.argv[2])
    elif cmd == "summary":
        cmd_summary()
    else:
        print(f"Unknown command: {cmd}")
        print("Commands: status, batch <N|all>, summary")
