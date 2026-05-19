#!/usr/bin/env python3
"""
toy_wp_search.py — search the BST Working Paper library by keyword / regex.

Usage:
    python3 play/toy_wp_search.py "Bergman kernel"
    python3 play/toy_wp_search.py --regex "Tr\\(D\\^\\{2k\\}\\)"
    python3 play/toy_wp_search.py --volume 4 "Heegner"
    python3 play/toy_wp_search.py --context 3 "eigentone"
    python3 play/toy_wp_search.py --list-volumes

Returns file:line:context for every match across the volume:chapter library
(WP_Vol1_Journey/ through WP_Vol6_Frontier/, plus root WorkingPaper.md).

Companion to the curated master TOC in WorkingPaper.md and per-volume INDEX.md
files. The TOC is the entry-point index (curated, opinionated, "start here").
This toy is the search-and-find tool (every occurrence, machine-readable).

Builds on the same library structure documented in WorkingPaper.md.
"""

import re, argparse
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

VOLUMES = [
    ("WP_Vol1_Journey",     "Vol 1 — The Journey"),
    ("WP_Vol2_Framework",   "Vol 2 — The Framework"),
    ("WP_Vol3_Physics",     "Vol 3 — The Physics"),
    ("WP_Vol4_Mathematics", "Vol 4 — The Mathematics"),
    ("WP_Vol5_Predictions", "Vol 5 — The Predictions"),
    ("WP_Vol6_Frontier",    "Vol 6 — The Frontier"),
]


def chapters_in(voldir):
    """Return all chapter .md files in a volume (excluding INDEX.md), sorted."""
    p = REPO / voldir
    if not p.is_dir():
        return []
    return sorted(p.glob("Ch*.md"))


def search_file(path, pattern, ignore_case=True, context=1):
    """Return list of (line_number, matched_line, context_before, context_after)."""
    flags = re.IGNORECASE if ignore_case else 0
    matches = []
    try:
        with open(path, "r") as f:
            lines = f.readlines()
    except (UnicodeDecodeError, IOError):
        return matches
    for i, line in enumerate(lines):
        if re.search(pattern, line, flags):
            before = lines[max(0, i-context):i]
            after = lines[i+1:min(len(lines), i+1+context)]
            matches.append((i+1, line.rstrip(), [b.rstrip() for b in before], [a.rstrip() for a in after]))
    return matches


def main():
    ap = argparse.ArgumentParser(description="Search the BST Working Paper library.")
    ap.add_argument("pattern", nargs="?", help="Keyword or regex to search for.")
    ap.add_argument("--regex", action="store_true", help="Treat pattern as regex (default is plain substring; both work, regex enables special chars).")
    ap.add_argument("--volume", type=int, default=None, help="Restrict search to one volume (1-6).")
    ap.add_argument("--context", type=int, default=0, help="Lines of context before/after each match (default 0).")
    ap.add_argument("--case-sensitive", action="store_true", help="Case-sensitive search.")
    ap.add_argument("--list-volumes", action="store_true", help="List volumes and chapters, then exit.")
    ap.add_argument("--include-root", action="store_true", help="Also search root WorkingPaper.md (master TOC).")
    args = ap.parse_args()

    if args.list_volumes:
        for voldir, title in VOLUMES:
            print(f"\n{title}  ({voldir}/)")
            for ch in chapters_in(voldir):
                print(f"  - {ch.name}")
        return

    if not args.pattern:
        ap.print_help()
        return

    pattern = args.pattern if args.regex else re.escape(args.pattern)
    ignore_case = not args.case_sensitive

    total_files_with_hits = 0
    total_matches = 0
    results_by_volume = {}

    targets = VOLUMES
    if args.volume:
        targets = [VOLUMES[args.volume - 1]] if 1 <= args.volume <= len(VOLUMES) else []

    if args.include_root:
        # Search root WorkingPaper.md
        wp = REPO / "WorkingPaper.md"
        if wp.exists():
            ms = search_file(wp, pattern, ignore_case=ignore_case, context=args.context)
            if ms:
                results_by_volume["Root (WorkingPaper.md)"] = [(wp, ms)]
                total_files_with_hits += 1
                total_matches += len(ms)

    for voldir, voltitle in targets:
        vol_results = []
        for ch in chapters_in(voldir):
            ms = search_file(ch, pattern, ignore_case=ignore_case, context=args.context)
            if ms:
                vol_results.append((ch, ms))
                total_files_with_hits += 1
                total_matches += len(ms)
        if vol_results:
            results_by_volume[voltitle] = vol_results

    if not results_by_volume:
        print(f"No matches found for: {args.pattern!r}")
        if args.volume:
            print(f"(restricted to volume {args.volume})")
        return

    for voltitle, vol_results in results_by_volume.items():
        print(f"\n=== {voltitle} ===")
        for fp, ms in vol_results:
            rel = fp.relative_to(REPO)
            print(f"\n  {rel}  ({len(ms)} match{'es' if len(ms) != 1 else ''})")
            for lineno, line, before, after in ms:
                for b in before:
                    print(f"    {lineno - len(before)}: {b}")
                print(f"  > {lineno}: {line}")
                for a in after:
                    print(f"    {lineno + 1}: {a}")

    print(f"\n--- Summary: {total_matches} match{'es' if total_matches != 1 else ''} in {total_files_with_hits} file{'s' if total_files_with_hits != 1 else ''} ---")


if __name__ == "__main__":
    main()
