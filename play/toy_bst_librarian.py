#!/usr/bin/env python3
"""BST Librarian — Daily maintenance tool for the BST living library.

Scans for changes, checks counters, audits cross-references, and generates
daily digests. Used by /review and /audit skills.

Subcommands:
  scan [--since DATE] [--days N]    Walk data/, notes/, play/, root — categorize new/modified files
  counters                          Read .next_toy + .next_theorem, compare to actual highest, flag drift
  audit-log [--populate] [--update] Add new files to audit_log.json / update mtimes & flag stale
  staleness                         Check data/*.json cross-refs against filesystem mtimes
  crossref [--count N]              Random spot-check: theorem refs, toy files, formula_code eval
  readme-check                      Verify notes/README.md paper count, play/README.md toy count
  digest [--output PATH]            Generate notes/.running/DIGEST_YYYY-MM-DD.md from all checks
  claims                            Parse CLAIMS.md for stale/orphaned entries
  xref-index                        Build reverse cross-reference index (theorem→papers, topic→papers)
  impact <query>                    Query which files are affected by a theorem, toy, topic, or constant

Usage:
  python3 toy_bst_librarian.py                      # Interactive REPL
  python3 toy_bst_librarian.py scan --days 7        # Single command
  python3 toy_bst_librarian.py counters             # Check counter drift
  python3 toy_bst_librarian.py digest               # Generate daily digest
"""

import json
import glob
import math
import os
import random
import re
import sys
import time
from datetime import datetime, timedelta
from math import pi, sqrt, log, exp, sin, cos, tan, atan, asin, acos, factorial, comb
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────

REPO_ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
DATA_DIR = os.path.join(REPO_ROOT, 'data')
PLAY_DIR = os.path.join(REPO_ROOT, 'play')
NOTES_DIR = os.path.join(REPO_ROOT, 'notes')
RUNNING_DIR = os.path.join(NOTES_DIR, '.running')
AUDIT_LOG = os.path.join(DATA_DIR, 'audit_log.json')

# ── BST Evaluation Namespace (shared with explorer) ───────────────────────

rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7; N_max = 137
alpha = 1.0 / N_max; alpha_inv = N_max
pi5 = pi ** 5
m_e = 0.51099895000; m_p = 6 * pi5 * m_e
m_e_GeV = m_e / 1000.0; m_p_GeV = m_p / 1000.0
hbar_c = 197.3269804
ln = log
cbrt = lambda x: x ** (1.0/3.0)
Fraction = lambda a, b: a / b
inf = float('inf')

EVAL_NS = {
    'rank': rank, 'N_c': N_c, 'n_C': n_C, 'C_2': C_2, 'g': g, 'N_max': N_max,
    'alpha': alpha, 'alpha_inv': alpha_inv, 'pi': pi, 'pi5': pi5,
    'sqrt': sqrt, 'cbrt': cbrt, 'log': log, 'ln': ln, 'exp': exp,
    'sin': sin, 'cos': cos, 'tan': tan, 'atan': atan, 'asin': asin, 'acos': acos,
    'comb': comb, 'factorial': factorial, 'Fraction': Fraction,
    'abs': abs, 'pow': pow, 'float': float, 'inf': inf,
    'm_e': m_e, 'm_e_GeV': m_e_GeV, 'm_p': m_p, 'm_p_GeV': m_p_GeV,
    'hbar_c': hbar_c,
}

# ── Display Helpers ────────────────────────────────────────────────────────

BOLD = "\033[1m"
DIM = "\033[2m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

def ok(msg):    print(f"  {GREEN}OK{RESET}   {msg}")
def warn(msg):  print(f"  {YELLOW}WARN{RESET} {msg}")
def fail(msg):  print(f"  {RED}FAIL{RESET} {msg}")
def info(msg):  print(f"  {CYAN}INFO{RESET} {msg}")
def header(msg):
    print(f"\n{'='*60}")
    print(f"  {BOLD}{msg}{RESET}")
    print(f"{'='*60}")

# ── Utility ────────────────────────────────────────────────────────────────

def load_json(path):
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    f.close()

def file_mtime(path):
    try:
        return datetime.fromtimestamp(os.path.getmtime(path))
    except OSError:
        return None

def file_mtime_str(path):
    mt = file_mtime(path)
    return mt.strftime('%Y-%m-%d') if mt else None

def rel_path(path):
    return os.path.relpath(path, REPO_ROOT)

def categorize_file(path):
    rp = rel_path(path)
    if rp.startswith('data/'): return 'data'
    if rp.startswith('notes/') and 'Paper' in rp: return 'paper'
    if rp.startswith('notes/'): return 'note'
    if rp.startswith('play/toy_') and rp.endswith('.py'): return 'toy'
    if rp.startswith('play/') and rp.endswith('.html'): return 'tool'
    if rp.startswith('play/') and rp.endswith('.py'): return 'tool'
    if rp.endswith('.md'): return 'config'
    return 'other'

def parse_date_arg(args):
    """Parse --since DATE or --days N from args string."""
    since = None
    parts = args.strip().split()
    i = 0
    while i < len(parts):
        if parts[i] == '--since' and i + 1 < len(parts):
            try:
                since = datetime.strptime(parts[i+1], '%Y-%m-%d')
            except ValueError:
                warn(f"Invalid date: {parts[i+1]}. Use YYYY-MM-DD.")
            i += 2
        elif parts[i] == '--days' and i + 1 < len(parts):
            try:
                days = int(parts[i+1])
                since = datetime.now() - timedelta(days=days)
            except ValueError:
                warn(f"Invalid number: {parts[i+1]}")
            i += 2
        else:
            i += 1
    if since is None:
        since = datetime.now() - timedelta(days=1)
    return since

def extract_toy_number(filename):
    """Extract number from toy_NNN_*.py filename."""
    m = re.match(r'toy_(\d+)_', os.path.basename(filename))
    return int(m.group(1)) if m else None

def extract_theorem_refs(text):
    """Find all T_NNN or TNNN references in text."""
    return set(re.findall(r'\bT(\d+)\b', text))

def extract_toy_refs(text):
    """Find Toy NNN or toy_NNN references in text."""
    nums = set()
    for m in re.findall(r'[Tt]oy[_ ](\d+)', text):
        nums.add(int(m))
    return nums

# ── Subcommand: scan ──────────────────────────────────────────────────────

def cmd_scan(args=''):
    """Walk data/, notes/, play/, root — categorize new/modified files."""
    since = parse_date_arg(args)
    header(f"File Scan (since {since.strftime('%Y-%m-%d')})")

    categories = {'data': [], 'paper': [], 'note': [], 'toy': [], 'tool': [], 'config': [], 'other': []}

    # Walk directories
    for dirpath in [REPO_ROOT, DATA_DIR, NOTES_DIR, PLAY_DIR]:
        if not os.path.isdir(dirpath):
            continue
        for entry in os.scandir(dirpath):
            if entry.name.startswith('.') or entry.is_dir():
                continue
            if not entry.name.endswith(('.py', '.md', '.json', '.html')):
                continue
            try:
                mt = datetime.fromtimestamp(entry.stat().st_mtime)
            except OSError:
                continue
            if mt >= since:
                cat = categorize_file(entry.path)
                categories[cat].append((rel_path(entry.path), mt.strftime('%Y-%m-%d %H:%M')))

    # Report
    total = sum(len(v) for v in categories.values())
    print(f"\n  Found {total} files modified since {since.strftime('%Y-%m-%d')}:\n")

    for cat, label in [('toy', 'Toys'), ('paper', 'Papers'), ('note', 'Notes'),
                       ('data', 'Data'), ('tool', 'Tools'), ('config', 'Config'), ('other', 'Other')]:
        files = categories[cat]
        if files:
            print(f"  {BOLD}{label}{RESET} ({len(files)}):")
            for path, mtime in sorted(files, key=lambda x: x[1], reverse=True)[:15]:
                print(f"    {mtime}  {path}")
            if len(files) > 15:
                print(f"    ... and {len(files)-15} more")
            print()

    return categories

# ── Subcommand: counters ──────────────────────────────────────────────────

def cmd_counters(args=''):
    """Read .next_toy + .next_theorem, compare to actual highest, flag drift."""
    header("Counter Check")

    results = {}

    # .next_toy
    toy_counter_path = os.path.join(PLAY_DIR, '.next_toy')
    if os.path.exists(toy_counter_path):
        with open(toy_counter_path) as f:
            next_toy = int(f.read().strip())
    else:
        next_toy = None
        warn(".next_toy file not found")

    # Find actual highest numbered toy
    highest_toy = 0
    toy_count = 0
    for fname in os.listdir(PLAY_DIR):
        n = extract_toy_number(fname)
        if n is not None:
            toy_count += 1
            highest_toy = max(highest_toy, n)

    # Total toy count (including named)
    total_toys = len(glob.glob(os.path.join(PLAY_DIR, 'toy_*.py')))

    if next_toy is not None:
        print(f"\n  .next_toy counter:      {next_toy}")
        print(f"  Highest numbered toy:   {highest_toy}")
        print(f"  Numbered toys:          {toy_count}")
        print(f"  Total toys (toy_*.py):  {total_toys}")
        if next_toy <= highest_toy:
            fail(f"Counter drift! .next_toy={next_toy} but highest toy is {highest_toy}")
            results['toy_drift'] = True
        else:
            ok(f"Counter consistent (gap: {next_toy - highest_toy - 1} unused numbers)")
            results['toy_drift'] = False
    results['next_toy'] = next_toy
    results['highest_toy'] = highest_toy
    results['total_toys'] = total_toys

    # .next_theorem
    thm_counter_path = os.path.join(PLAY_DIR, '.next_theorem')
    if os.path.exists(thm_counter_path):
        with open(thm_counter_path) as f:
            next_thm = int(f.read().strip())
    else:
        next_thm = None
        warn(".next_theorem file not found")

    # Check graph for highest theorem
    graph_path = os.path.join(PLAY_DIR, 'ac_graph_data.json')
    graph = load_json(graph_path)
    highest_graph_thm = 0
    if graph and 'theorems' in graph:
        for t in graph['theorems']:
            tid = t.get('tid', 0)
            if isinstance(tid, int):
                highest_graph_thm = max(highest_graph_thm, tid)
            elif isinstance(tid, str) and tid.isdigit():
                highest_graph_thm = max(highest_graph_thm, int(tid))

    if next_thm is not None:
        print(f"\n  .next_theorem counter:  {next_thm}")
        print(f"  Highest in graph:       {highest_graph_thm}")
        if next_thm <= highest_graph_thm:
            fail(f"Counter drift! .next_theorem={next_thm} but graph has T{highest_graph_thm}")
            results['thm_drift'] = True
        else:
            ok(f"Counter consistent (gap: {next_thm - highest_graph_thm - 1})")
            results['thm_drift'] = False
    results['next_theorem'] = next_thm
    results['highest_graph_thm'] = highest_graph_thm

    return results

# ── Subcommand: audit-log ─────────────────────────────────────────────────

def cmd_audit_log(args=''):
    """Add new files to audit_log.json / update mtimes & flag stale."""
    populate = '--populate' in args
    update = '--update' in args or populate
    header("Audit Log" + (" — POPULATE" if populate else " — UPDATE" if update else " — STATUS"))

    audit = load_json(AUDIT_LOG)
    if not audit:
        fail(f"Cannot read {AUDIT_LOG}")
        return None

    existing_paths = {f['path'] for f in audit['files']}
    print(f"\n  Current entries: {len(audit['files'])}")

    if populate:
        # Tier A: root .md files, play/*.html, utility scripts, graph data
        new_files = []

        # Root .md files
        for f in glob.glob(os.path.join(REPO_ROOT, '*.md')):
            rp = rel_path(f)
            if rp not in existing_paths:
                new_files.append((rp, 'config', f))

        # play/*.html
        for f in glob.glob(os.path.join(PLAY_DIR, '*.html')):
            rp = rel_path(f)
            if rp not in existing_paths:
                new_files.append((rp, 'tool', f))

        # play/ utility scripts (non-toy .py files)
        for f in glob.glob(os.path.join(PLAY_DIR, '*.py')):
            if os.path.basename(f).startswith('toy_'):
                continue
            rp = rel_path(f)
            if rp not in existing_paths:
                new_files.append((rp, 'tool', f))

        # play/ac_graph_data.json
        gf = os.path.join(PLAY_DIR, 'ac_graph_data.json')
        if os.path.exists(gf) and rel_path(gf) not in existing_paths:
            new_files.append((rel_path(gf), 'data', gf))

        # play/bst_appliance/ key files
        for f in glob.glob(os.path.join(PLAY_DIR, 'bst_appliance', '*.py')):
            rp = rel_path(f)
            if rp not in existing_paths:
                new_files.append((rp, 'tool', f))

        # data/ files
        for f in glob.glob(os.path.join(DATA_DIR, '*')):
            rp = rel_path(f)
            if rp not in existing_paths:
                new_files.append((rp, 'data', f))

        # Tier B: numbered papers in notes/
        for f in glob.glob(os.path.join(NOTES_DIR, 'BST_Paper*')):
            rp = rel_path(f)
            if rp not in existing_paths:
                new_files.append((rp, 'paper', f))
        for f in glob.glob(os.path.join(NOTES_DIR, 'Paper_*')):
            rp = rel_path(f)
            if rp not in existing_paths:
                new_files.append((rp, 'paper', f))

        # Skills
        skills_dir = os.path.join(REPO_ROOT, 'skills')
        if os.path.isdir(skills_dir):
            for f in glob.glob(os.path.join(skills_dir, '*')):
                rp = rel_path(f)
                if rp not in existing_paths:
                    new_files.append((rp, 'config', f))

        # Add new entries
        added = 0
        for rp, cat, fullpath in new_files:
            if rp not in existing_paths:
                entry = {
                    "path": rp,
                    "category": cat,
                    "last_audited": None,
                    "auditor": None,
                    "status": "new",
                    "last_modified": file_mtime_str(fullpath),
                    "notes": f"Added by librarian --populate on {datetime.now().strftime('%Y-%m-%d')}"
                }
                audit['files'].append(entry)
                existing_paths.add(rp)
                added += 1
                info(f"Added: {rp} ({cat})")

        print(f"\n  Added {added} new entries")

    if update:
        # Update mtimes and flag stale entries
        stale_count = 0
        for entry in audit['files']:
            fullpath = os.path.join(REPO_ROOT, entry['path'])
            if os.path.exists(fullpath):
                current_mtime = file_mtime_str(fullpath)
                if current_mtime and entry.get('last_modified') != current_mtime:
                    old = entry.get('last_modified', 'unknown')
                    entry['last_modified'] = current_mtime
                    if entry.get('status') == 'current' and entry.get('last_audited'):
                        if current_mtime > entry['last_audited']:
                            entry['status'] = 'needs_review'
                            stale_count += 1
            else:
                if entry.get('status') != 'deleted':
                    entry['status'] = 'deleted'
                    warn(f"Deleted: {entry['path']}")

        audit['meta']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
        save_json(AUDIT_LOG, audit)
        print(f"\n  Updated mtimes. {stale_count} entries flagged stale.")

    # Status summary
    status_counts = {}
    cat_counts = {}
    for entry in audit['files']:
        s = entry.get('status', 'unknown')
        status_counts[s] = status_counts.get(s, 0) + 1
        c = entry.get('category', 'unknown')
        cat_counts[c] = cat_counts.get(c, 0) + 1

    print(f"\n  Total entries: {len(audit['files'])}")
    print(f"  By status:  {', '.join(f'{s}: {n}' for s, n in sorted(status_counts.items()))}")
    print(f"  By category: {', '.join(f'{c}: {n}' for c, n in sorted(cat_counts.items()))}")

    return audit

# ── Subcommand: staleness ─────────────────────────────────────────────────

def cmd_staleness(args=''):
    """Check data/*.json cross-refs against filesystem mtimes."""
    header("Data Staleness Check")

    issues = []

    # Load all data files
    for fname in sorted(os.listdir(DATA_DIR)):
        if not fname.endswith('.json'):
            continue
        fpath = os.path.join(DATA_DIR, fname)
        data = load_json(fpath)
        if not data:
            continue

        data_mtime = file_mtime(fpath)
        print(f"\n  {BOLD}{fname}{RESET} (modified: {data_mtime.strftime('%Y-%m-%d') if data_mtime else '?'})")

        # Check meta.count vs actual count
        meta = data.get('meta', {})
        if 'count' in meta:
            # Find the main list
            for key in ['constants', 'particles', 'layers', 'predictions', 'domains', 'files']:
                if key in data:
                    actual = len(data[key])
                    expected = meta['count']
                    if actual != expected:
                        fail(f"  meta.count={expected} but actual {key} count={actual}")
                        issues.append(f"{fname}: count mismatch ({expected} vs {actual})")
                    else:
                        ok(f"  meta.count={expected} matches {key} count")
                    break

        # Check last_updated
        if 'last_updated' in meta:
            lu = meta['last_updated']
            print(f"    Last updated: {lu}")

        # Check for references to external files
        content = json.dumps(data)
        toy_refs = extract_toy_refs(content)
        thm_refs = extract_theorem_refs(content)

        if toy_refs:
            missing_toys = []
            for tn in sorted(toy_refs)[:20]:
                matches = glob.glob(os.path.join(PLAY_DIR, f'toy_{tn}_*.py'))
                if not matches:
                    missing_toys.append(tn)
            if missing_toys:
                warn(f"  {len(missing_toys)} toy refs not found: {missing_toys[:5]}")
                issues.append(f"{fname}: missing toy files for {missing_toys[:5]}")
            else:
                ok(f"  All {len(toy_refs)} toy references valid")

    if not issues:
        print(f"\n  {GREEN}All data files consistent.{RESET}")
    else:
        print(f"\n  {RED}{len(issues)} issues found.{RESET}")

    return issues

# ── Subcommand: crossref ──────────────────────────────────────────────────

def cmd_crossref(args=''):
    """Random spot-check: theorem refs, toy files, formula_code eval."""
    count = 5
    parts = args.strip().split()
    for i, p in enumerate(parts):
        if p == '--count' and i + 1 < len(parts):
            try:
                count = int(parts[i+1])
            except ValueError:
                pass

    header(f"Cross-Reference Spot Check ({count} samples)")

    constants = load_json(os.path.join(DATA_DIR, 'bst_constants.json'))
    if not constants or 'constants' not in constants:
        fail("Cannot load bst_constants.json")
        return {'passed': 0, 'failed': 0, 'total': 0}

    # Load theorem graph for validation
    graph = load_json(os.path.join(PLAY_DIR, 'ac_graph_data.json'))
    graph_tids = set()
    if graph and 'theorems' in graph:
        for t in graph['theorems']:
            tid = t.get('tid')
            if tid is not None:
                graph_tids.add(str(tid))

    samples = random.sample(constants['constants'], min(count, len(constants['constants'])))
    passed = 0
    failed = 0

    for c in samples:
        name = c.get('name', '?')
        tid = c.get('theorem_id', '?')
        print(f"\n  {BOLD}[{tid}] {name}{RESET}")

        checks_ok = True

        # Check theorem ref exists in graph
        tid_num = re.search(r'T(\d+)', str(tid))
        if tid_num and graph_tids:
            if tid_num.group(1) in graph_tids:
                ok(f"Theorem {tid} found in graph")
            else:
                warn(f"Theorem {tid} NOT in graph")
                checks_ok = False

        # Check formula_code evaluates
        code = c.get('formula_code', '')
        if code and code != '1' and 'inf' not in code.lower():
            try:
                bst_val = eval(code, {"__builtins__": {}}, EVAL_NS)
                obs_val = c.get('observed_value')
                if isinstance(obs_val, (int, float)) and obs_val != 0:
                    pct = abs(bst_val - obs_val) / abs(obs_val) * 100
                    if pct < 5:
                        ok(f"Formula: BST={bst_val:.6g} vs Obs={obs_val:.6g} ({pct:.4f}%)")
                    else:
                        fail(f"Formula: BST={bst_val:.6g} vs Obs={obs_val:.6g} ({pct:.2f}%) > 5%")
                        checks_ok = False
                else:
                    ok(f"Formula evaluates to {bst_val:.6g} (no numeric observed value)")
            except Exception as e:
                fail(f"Formula eval error: {e}")
                checks_ok = False
        else:
            info("No evaluable formula_code")

        # Check source_toys files exist
        source_toys = c.get('source_toys', [])
        if source_toys:
            for st in source_toys[:3]:
                toy_num = re.search(r'(\d+)', str(st))
                if toy_num:
                    matches = glob.glob(os.path.join(PLAY_DIR, f'toy_{toy_num.group(1)}_*.py'))
                    if matches:
                        ok(f"Toy {toy_num.group(1)} exists")
                    else:
                        warn(f"Toy {toy_num.group(1)} not found")

        if checks_ok:
            passed += 1
        else:
            failed += 1

    total = passed + failed
    print(f"\n  Result: {GREEN}{passed}{RESET}/{total} passed" +
          (f", {RED}{failed}{RESET} failed" if failed else ""))

    return {'passed': passed, 'failed': failed, 'total': total}

# ── Subcommand: readme-check ──────────────────────────────────────────────

def cmd_readme_check(args=''):
    """Verify notes/README.md paper count, play/README.md toy count, CLAUDE.md counts."""
    header("README Currency Check")

    issues = []

    # play/README.md toy count
    play_readme = os.path.join(PLAY_DIR, 'README.md')
    if os.path.exists(play_readme):
        with open(play_readme) as f:
            content = f.read()
        # Look for toy count
        m = re.search(r'Toy scripts.*?\|\s*(\d[\d,]*)', content)
        if m:
            readme_count = int(m.group(1).replace(',', ''))
            actual_count = len(glob.glob(os.path.join(PLAY_DIR, 'toy_*.py')))
            if readme_count == actual_count:
                ok(f"play/README.md toy count: {readme_count} (matches)")
            else:
                warn(f"play/README.md toy count: {readme_count}, actual: {actual_count}")
                issues.append(f"play/README.md: toy count {readme_count} vs actual {actual_count}")
        # Check next_toy
        m2 = re.search(r'Next toy number\s*\|\s*(\d+)', content)
        if m2:
            readme_next = int(m2.group(1))
            try:
                with open(os.path.join(PLAY_DIR, '.next_toy')) as f:
                    actual_next = int(f.read().strip())
                if readme_next == actual_next:
                    ok(f"play/README.md next_toy: {readme_next} (matches)")
                else:
                    warn(f"play/README.md next_toy: {readme_next}, .next_toy: {actual_next}")
                    issues.append(f"play/README.md: next_toy {readme_next} vs .next_toy {actual_next}")
            except (FileNotFoundError, ValueError):
                pass

    # notes/README.md paper count
    notes_readme = os.path.join(NOTES_DIR, 'README.md')
    if os.path.exists(notes_readme):
        with open(notes_readme) as f:
            content = f.read()
        # Count paper entries (look for "Paper #N" or "## N." patterns)
        paper_refs = re.findall(r'(?:Paper\s*#|##\s+)\d+', content)
        if paper_refs:
            paper_nums = set()
            for ref in paper_refs:
                m = re.search(r'(\d+)', ref)
                if m:
                    paper_nums.add(int(m.group(1)))
            if paper_nums:
                highest = max(paper_nums)
                info(f"notes/README.md references papers up to #{highest} ({len(paper_nums)} unique)")
        # Count actual paper files
        paper_files = (glob.glob(os.path.join(NOTES_DIR, 'BST_Paper*')) +
                      glob.glob(os.path.join(NOTES_DIR, 'Paper_*')))
        info(f"  Actual paper files in notes/: {len(paper_files)}")

    # CLAUDE.md counts
    claude_md = os.path.join(REPO_ROOT, 'CLAUDE.md')
    if os.path.exists(claude_md):
        with open(claude_md) as f:
            content = f.read()
        # Check toy count mention
        m = re.search(r'(\d[\d,]*)\+?\s*toys', content)
        if m:
            claude_toys = int(m.group(1).replace(',', ''))
            actual_toys = len(glob.glob(os.path.join(PLAY_DIR, 'toy_*.py')))
            if abs(claude_toys - actual_toys) <= 10:
                ok(f"CLAUDE.md toy count: {claude_toys} (actual: {actual_toys})")
            else:
                warn(f"CLAUDE.md toy count: {claude_toys}, actual: {actual_toys}")
                issues.append(f"CLAUDE.md: toy count {claude_toys} vs actual {actual_toys}")

    if not issues:
        print(f"\n  {GREEN}All README counts consistent.{RESET}")
    else:
        print(f"\n  {YELLOW}{len(issues)} drift issues found.{RESET}")

    return issues

# ── Subcommand: digest ─────────────────────────────────────────────────────

def cmd_digest(args=''):
    """Generate notes/.running/DIGEST_YYYY-MM-DD.md from all checks."""
    today = datetime.now().strftime('%Y-%m-%d')

    output_path = None
    parts = args.strip().split()
    for i, p in enumerate(parts):
        if p == '--output' and i + 1 < len(parts):
            output_path = parts[i+1]

    if not output_path:
        os.makedirs(RUNNING_DIR, exist_ok=True)
        output_path = os.path.join(RUNNING_DIR, f'DIGEST_{today}.md')

    header(f"Generating Daily Digest → {rel_path(output_path)}")

    # Run all checks quietly (capture results)
    import io
    old_stdout = sys.stdout

    # Scan
    sys.stdout = io.StringIO()
    scan_results = cmd_scan(f'--since {today}')
    sys.stdout = old_stdout
    scan_counts = {k: len(v) for k, v in (scan_results or {}).items()}

    # Counters
    sys.stdout = io.StringIO()
    counter_results = cmd_counters()
    sys.stdout = old_stdout

    # Crossref
    sys.stdout = io.StringIO()
    xref_results = cmd_crossref('--count 5')
    sys.stdout = old_stdout

    # Staleness
    sys.stdout = io.StringIO()
    stale_issues = cmd_staleness()
    sys.stdout = old_stdout

    # README check
    sys.stdout = io.StringIO()
    readme_issues = cmd_readme_check()
    sys.stdout = old_stdout

    # Audit log status
    audit = load_json(AUDIT_LOG)
    audit_status = {}
    if audit:
        for entry in audit['files']:
            s = entry.get('status', 'unknown')
            audit_status[s] = audit_status.get(s, 0) + 1

    # Build digest
    lines = [
        f"# BST Daily Digest — {today}",
        "",
        "## Changes",
        f"- {scan_counts.get('toy', 0)} toys modified",
        f"- {scan_counts.get('paper', 0)} papers modified",
        f"- {scan_counts.get('note', 0)} notes modified",
        f"- {scan_counts.get('data', 0)} data files modified",
        f"- {scan_counts.get('tool', 0)} tools modified",
        "",
        "## Counters",
    ]

    if counter_results:
        lines.append(f"- .next_toy: {counter_results.get('next_toy', '?')}")
        lines.append(f"- .next_theorem: {counter_results.get('next_theorem', '?')}")
        lines.append(f"- Total toys: {counter_results.get('total_toys', '?')}")
        drift = []
        if counter_results.get('toy_drift'):
            drift.append('toy counter')
        if counter_results.get('thm_drift'):
            drift.append('theorem counter')
        if drift:
            lines.append(f"- **DRIFT**: {', '.join(drift)}")
        else:
            lines.append(f"- No counter drift")

    lines.extend([
        "",
        "## Data Layer Status",
    ])

    # Load constants count
    constants = load_json(os.path.join(DATA_DIR, 'bst_constants.json'))
    predictions = load_json(os.path.join(DATA_DIR, 'bst_predictions.json'))
    lines.append(f"- Constants: {len(constants['constants']) if constants else '?'}")
    lines.append(f"- Predictions: {len(predictions['predictions']) if predictions else '?'}")
    lines.append(f"- Staleness issues: {len(stale_issues) if stale_issues else 0}")

    if audit_status:
        status_str = ', '.join(f'{s}: {n}' for s, n in sorted(audit_status.items()))
        lines.append(f"- Audit log: {sum(audit_status.values())} entries ({status_str})")

    lines.extend([
        "",
        "## Spot Check",
        f"- Cross-refs: {xref_results.get('passed', '?')}/{xref_results.get('total', '?')} passed",
    ])

    if readme_issues:
        lines.append(f"- README drift: {len(readme_issues)} issues")
        for issue in readme_issues:
            lines.append(f"  - {issue}")
    else:
        lines.append("- README counts: all consistent")

    lines.extend([
        "",
        "## Notes",
        f"Generated by BST Librarian on {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
    ])

    digest_content = '\n'.join(lines)

    with open(output_path, 'w') as f:
        f.write(digest_content)

    print(f"\n  Digest written to {rel_path(output_path)}")
    print(f"\n{DIM}{digest_content}{RESET}")

    return output_path

# ── Subcommand: claims ─────────────────────────────────────────────────────

def cmd_claims(args=''):
    """Parse CLAIMS.md for stale/orphaned entries."""
    header("Claims Check")

    claims_path = os.path.join(REPO_ROOT, 'CLAIMS.md')
    if not os.path.exists(claims_path):
        info("No CLAIMS.md found in repo root. Nothing to check.")
        return []

    with open(claims_path) as f:
        content = f.read()

    issues = []

    # Find toy claims
    toy_claims = re.findall(r'[Tt]oy\s+(\d+)\s*[-—:]\s*(.+)', content)
    for num_str, desc in toy_claims:
        num = int(num_str)
        matches = glob.glob(os.path.join(PLAY_DIR, f'toy_{num}_*.py'))
        if not matches:
            warn(f"Claimed toy {num} not found: {desc.strip()}")
            issues.append(f"Toy {num}: claimed but no file found")
        else:
            ok(f"Toy {num}: exists ({os.path.basename(matches[0])})")

    # Find theorem claims
    thm_claims = re.findall(r'T(\d+)\s*[-—:]\s*(.+)', content)
    graph = load_json(os.path.join(PLAY_DIR, 'ac_graph_data.json'))
    graph_tids = set()
    if graph and 'theorems' in graph:
        for t in graph['theorems']:
            tid = t.get('tid')
            if tid is not None:
                graph_tids.add(str(tid))

    for num_str, desc in thm_claims:
        if num_str in graph_tids:
            ok(f"T{num_str}: in graph")
        else:
            warn(f"T{num_str}: claimed but not in graph — {desc.strip()}")
            issues.append(f"T{num_str}: claimed but not in graph")

    if not issues:
        if not toy_claims and not thm_claims:
            info("No parseable claims found in CLAIMS.md")
        else:
            print(f"\n  {GREEN}All claims verified.{RESET}")
    else:
        print(f"\n  {YELLOW}{len(issues)} orphaned/stale claims.{RESET}")

    return issues

# ── Subcommand: xref-index ────────────────────────────────────────────────

XREF_INDEX = os.path.join(DATA_DIR, 'bst_crossref_index.json')

# Keywords extracted from filenames and content — maps topic → search patterns
TOPIC_PATTERNS = {
    'proton_mass':    [r'proton\s+mass', r'm_p\b', r'938\.27'],
    'cosmic_age':     [r'cosmic\s+age', r'age.*universe', r'13\.79', r'13\.78'],
    'hubble':         [r'H_?0\b', r'[Hh]ubble', r'67\.3'],
    'CKM':            [r'CKM', r'Cabibbo', r'Wolfenstein', r'V_\{?[ucdstb][ucdstb]'],
    'PMNS':           [r'PMNS', r'neutrino.*mix', r'theta_\{?1[23]'],
    'magic_number':   [r'magic\s+number', r'shell\s+closure', r'kappa_ls'],
    'dark_energy':    [r'dark\s+energy', r'Omega_?[Ll]ambda', r'cosmological\s+constant'],
    'dark_matter':    [r'dark\s+matter', r'Omega_?[Mm]', r'MOND'],
    'higgs':          [r'[Hh]iggs', r'125\s*GeV', r'Fermi\s+scale'],
    'strong_cp':      [r'strong\s+CP', r'theta.*QCD', r'CP\s+violation'],
    'fine_structure':  [r'fine\s+struct', r'alpha\s*=\s*1/137', r'\b137\b.*channel'],
    'mass_gap':       [r'mass\s+gap', r'Yang.Mills', r'Wightman'],
    'riemann':        [r'[Rr]iemann\s+[Hh]ypothesis', r'critical\s+line', r'zeta\s+function'],
    'four_color':     [r'[Ff]our.?[Cc]olor', r'planar\s+graph', r'chromatic'],
    'p_np':           [r'P\s*[!≠]\s*=?\s*NP', r'AC\(0\)', r'complexity.*lower'],
    'CMB':            [r'\bCMB\b', r'power\s+spectrum', r'spectral\s+index', r'n_s\b'],
    'heat_kernel':    [r'[Hh]eat\s+kernel', r'Seeley.DeWitt', r'a_\{?\d+\}?.*coefficient'],
    'biology':        [r'genetic\s+code', r'amino\s+acid', r'DNA', r'evolution'],
    'cooperation':    [r'cooperation', r'game\s+theory', r'Nash'],
    'observer':       [r'observer', r'consciousness', r'interstasis'],
    'bottom_quark':   [r'bottom\s+quark', r'm_b\b', r'4\.18\s*GeV'],
    'SEMF':           [r'SEMF', r'semi.empirical', r'liquid\s+drop', r'nuclear\s+binding'],
    'jarlskog':       [r'[Jj]arlskog', r'J_\{?CKM'],
    'casimir':        [r'[Cc]asimir', r'vacuum\s+energy', r'flow\s+cell'],
    'superconductivity': [r'BCS', r'superconducti', r'Cooper\s+pair', r'critical.*temp'],
    'neutron_star':   [r'neutron\s+star', r'Chandrasekhar', r'TOV'],
    'meson':          [r'meson', r'pion', r'kaon', r'rho\s+meson'],
    'lepton':         [r'muon', r'tau.*mass', r'lepton.*ratio'],
    'gravity':        [r'Newton.*G\b', r'gravitational\s+const', r'Einstein.*equat'],
}

def extract_topics(text, filename):
    """Extract topic keywords from file content and name."""
    topics = set()
    # From filename
    name_lower = filename.lower()
    for topic, patterns in TOPIC_PATTERNS.items():
        for pat in patterns:
            if re.search(pat, name_lower):
                topics.add(topic)
                break
    # From content (case-insensitive)
    for topic, patterns in TOPIC_PATTERNS.items():
        if topic in topics:
            continue
        for pat in patterns:
            if re.search(pat, text, re.IGNORECASE):
                topics.add(topic)
                break
    return topics

def extract_file_summary(text, filename):
    """Get a one-line summary from the file."""
    # Try first markdown heading
    m = re.search(r'^#\s+(.+)', text, re.MULTILINE)
    if m:
        return m.group(1).strip()[:100]
    # Try first non-empty line
    for line in text.split('\n')[:10]:
        line = line.strip()
        if line and not line.startswith('---') and not line.startswith('```'):
            return line[:100]
    return filename

def cmd_xref_index(args=''):
    """Build reverse cross-reference index from all notes/ files."""
    header("Building Cross-Reference Index")

    by_theorem = {}   # tid_str → [{"path": ..., "summary": ...}, ...]
    by_toy = {}       # toy_num_str → [...]
    by_topic = {}     # topic_name → [...]
    by_constant = {}  # constant_id → [...]

    # Load constant names for matching
    constants_data = load_json(os.path.join(DATA_DIR, 'bst_constants.json'))
    const_names = {}
    if constants_data:
        for c in constants_data.get('constants', []):
            cid = c.get('id', '')
            name = c.get('name', '')
            const_names[cid] = name.lower()

    # Scan all notes/*.md files
    files_scanned = 0
    notes_files = sorted([
        f for f in os.listdir(NOTES_DIR)
        if f.endswith('.md') and not f.startswith('.')
    ])

    for fname in notes_files:
        fpath = os.path.join(NOTES_DIR, fname)
        rel = f"notes/{fname}"
        try:
            with open(fpath, encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue

        files_scanned += 1
        summary = extract_file_summary(content, fname)
        entry = {"path": rel, "summary": summary}

        # Theorem refs
        thm_refs = extract_theorem_refs(content)
        for t in thm_refs:
            tid = int(t)
            if tid > 10:  # skip small numbers
                by_theorem.setdefault(t, []).append(entry)

        # Toy refs
        toy_refs = extract_toy_refs(content)
        for t in toy_refs:
            by_toy.setdefault(str(t), []).append(entry)

        # Topic keywords
        topics = extract_topics(content, fname)
        for topic in topics:
            by_topic.setdefault(topic, []).append(entry)

        # Constant references (by name match)
        content_lower = content.lower()
        for cid, cname in const_names.items():
            if len(cname) > 5 and cname in content_lower:
                by_constant.setdefault(cid, []).append(entry)

    # Also scan play/ toy files (just headers, not full content)
    toy_files = sorted(glob.glob(os.path.join(PLAY_DIR, 'toy_*.py')))
    for tpath in toy_files:
        fname = os.path.basename(tpath)
        rel = f"play/{fname}"
        try:
            with open(tpath, encoding='utf-8') as f:
                # Read just first 30 lines for speed
                head_lines = []
                for i, line in enumerate(f):
                    if i >= 30:
                        break
                    head_lines.append(line)
                head = ''.join(head_lines)
        except Exception:
            continue

        files_scanned += 1
        summary = extract_file_summary(head, fname)
        entry = {"path": rel, "summary": summary}

        # Theorem refs from header
        thm_refs = extract_theorem_refs(head)
        for t in thm_refs:
            tid = int(t)
            if tid > 10:
                by_theorem.setdefault(t, []).append(entry)

    # Deduplicate entries within each list
    def dedup(mapping):
        for key in mapping:
            seen = set()
            unique = []
            for e in mapping[key]:
                if e['path'] not in seen:
                    seen.add(e['path'])
                    unique.append(e)
            mapping[key] = unique

    dedup(by_theorem)
    dedup(by_toy)
    dedup(by_topic)
    dedup(by_constant)

    index = {
        "meta": {
            "version": 1,
            "built": datetime.now().strftime('%Y-%m-%d'),
            "files_scanned": files_scanned,
            "theorem_keys": len(by_theorem),
            "toy_keys": len(by_toy),
            "topic_keys": len(by_topic),
            "constant_keys": len(by_constant),
            "description": "Reverse cross-reference index. Query with: impact <theorem|toy|topic|constant>"
        },
        "by_theorem": by_theorem,
        "by_toy": by_toy,
        "by_topic": by_topic,
        "by_constant": by_constant,
    }

    save_json(XREF_INDEX, index)

    print(f"\n  Files scanned: {files_scanned}")
    print(f"  Theorem keys:  {len(by_theorem)} (unique theorem IDs referenced)")
    print(f"  Toy keys:      {len(by_toy)} (unique toy numbers referenced)")
    print(f"  Topic keys:    {len(by_topic)} ({', '.join(sorted(by_topic.keys())[:10])}...)")
    print(f"  Constant keys: {len(by_constant)} (constants mentioned by name)")
    print(f"\n  Index written to {rel_path(XREF_INDEX)}")

    return index

# ── Subcommand: impact ────────────────────────────────────────────────────

def cmd_impact(args=''):
    """Query cross-reference index: which papers are affected by a change?

    Usage:
      impact T891                  — files referencing theorem T891
      impact toy 541               — files referencing Toy 541
      impact topic cosmic_age      — files discussing cosmic age
      impact topic CKM             — files discussing CKM matrix
      impact const cosmic_age      — files mentioning the cosmic age constant
      impact <any string>          — search across all categories
    """
    query = args.strip()
    if not query:
        print("  Usage: impact <T891|toy 541|topic cosmic_age|const name|any string>")
        print("  Run 'xref-index' first to build the index.")
        return

    # Load index
    index = load_json(XREF_INDEX)
    if not index:
        print(f"  {YELLOW}No cross-reference index found. Run 'xref-index' first.{RESET}")
        return

    header(f"Impact Analysis: {query}")

    results = []

    # Parse query type
    parts = query.split(None, 1)
    qtype = parts[0].lower() if parts else ''
    qval = parts[1].strip() if len(parts) > 1 else ''

    if qtype == 'topic' and qval:
        # Direct topic lookup
        entries = index.get('by_topic', {}).get(qval, [])
        if not entries:
            # Try fuzzy match
            for key in index.get('by_topic', {}):
                if qval.lower() in key.lower():
                    entries.extend(index['by_topic'][key])
                    print(f"  Matched topic: {key}")
        results = entries

    elif qtype == 'toy' and qval:
        results = index.get('by_toy', {}).get(qval, [])

    elif qtype == 'const' and qval:
        # Search constant keys
        for key, entries in index.get('by_constant', {}).items():
            if qval.lower() in key.lower():
                results.extend(entries)
                print(f"  Matched constant: {key}")

    elif re.match(r'^T\d+$', query, re.IGNORECASE):
        # Theorem lookup
        tid = re.search(r'(\d+)', query).group(1)
        results = index.get('by_theorem', {}).get(tid, [])

    elif re.match(r'^toy\s*\d+$', query, re.IGNORECASE):
        # Toy lookup (without explicit "toy" prefix in qtype)
        tnum = re.search(r'(\d+)', query).group(1)
        results = index.get('by_toy', {}).get(tnum, [])

    else:
        # General search — check all categories
        q_lower = query.lower()
        seen = set()

        # Check theorems
        for tid, entries in index.get('by_theorem', {}).items():
            if q_lower in f"t{tid}":
                for e in entries:
                    if e['path'] not in seen:
                        results.append(e)
                        seen.add(e['path'])

        # Check topics
        for topic, entries in index.get('by_topic', {}).items():
            if q_lower in topic.lower():
                for e in entries:
                    if e['path'] not in seen:
                        results.append(e)
                        seen.add(e['path'])

        # Check constants
        for cid, entries in index.get('by_constant', {}).items():
            if q_lower in cid.lower():
                for e in entries:
                    if e['path'] not in seen:
                        results.append(e)
                        seen.add(e['path'])

    # Deduplicate
    seen = set()
    unique = []
    for r in results:
        if r['path'] not in seen:
            seen.add(r['path'])
            unique.append(r)
    results = unique

    if not results:
        print(f"\n  No files found for '{query}'.")
        print(f"  Available topics: {', '.join(sorted(index.get('by_topic', {}).keys()))}")
        return

    # Group by category
    papers = [r for r in results if 'Paper' in r['path']]
    theorems = [r for r in results if '_T' in r['path'] and 'Paper' not in r['path']]
    notes = [r for r in results if r not in papers and r not in theorems and r['path'].startswith('notes/')]
    toys = [r for r in results if r['path'].startswith('play/')]

    print(f"\n  {BOLD}{len(results)} files affected{RESET}\n")

    for label, group in [("Papers", papers), ("Theorem notes", theorems),
                          ("Research notes", notes), ("Toys", toys)]:
        if group:
            print(f"  {BOLD}{label} ({len(group)}):{RESET}")
            for r in sorted(group, key=lambda x: x['path'])[:25]:
                print(f"    {r['path']}")
                if r.get('summary'):
                    print(f"      {DIM}{r['summary'][:80]}{RESET}")
            if len(group) > 25:
                print(f"    ... +{len(group)-25} more")
            print()

    return results

    return issues

# ── REPL ───────────────────────────────────────────────────────────────────

COMMANDS = {
    'scan': cmd_scan,
    'counters': cmd_counters,
    'audit-log': cmd_audit_log,
    'staleness': cmd_staleness,
    'crossref': cmd_crossref,
    'readme-check': cmd_readme_check,
    'digest': cmd_digest,
    'claims': cmd_claims,
    'xref-index': cmd_xref_index,
    'impact': cmd_impact,
}

def cmd_help():
    print(__doc__)

def run_command(line):
    parts = line.strip().split(None, 1)
    if not parts:
        return True
    cmd = parts[0].lower()
    args = parts[1] if len(parts) > 1 else ''

    if cmd in ('quit', 'exit', 'q'):
        return False
    elif cmd == 'help':
        cmd_help()
    elif cmd in COMMANDS:
        COMMANDS[cmd](args)
    else:
        print(f"  Unknown command: {cmd}. Type 'help' for usage.")
    return True

def main():
    print(f"\n{BOLD}BST Librarian{RESET} — Daily maintenance for the BST living library")
    print(f"Eight tools for keeping 1,194+ toys, 64 papers, and 7 data files honest.\n")

    # Single command mode
    if len(sys.argv) > 1:
        line = ' '.join(sys.argv[1:])
        run_command(line)
        return

    # Interactive REPL
    try:
        import readline
    except ImportError:
        pass

    print("Type 'help' for commands, 'quit' to exit.\n")
    while True:
        try:
            line = input(f"{BOLD}lib>{RESET} ")
            if not run_command(line):
                break
        except (EOFError, KeyboardInterrupt):
            print()
            break

    print("\nThe library is tended. The math endures.")

if __name__ == '__main__':
    main()
