#!/usr/bin/env python3
"""Compare rubric tier claims against registry tiers, joined on cited registry IDs.

This lint is cheap and correct ONLY because every rubric row cites the registry
ID(s) it summarizes.  Before the join key existed, 4 of 21 rubric rows carried a
T-id and most named their claim by description -- so no sweep, human or scripted,
could compare the two artifacts.  Both of 2026-08-23's propagation failures were
found by reading, and no instrument could have found them.

Class (C) fix: no instrument could exist on the old structure, so the structure
changed first.  Grace, 2026-08-23.
"""
import json, os, re, sys

TIERS = ['DERIVED', 'PARTIALLY DERIVED', 'IDENTIFIED', 'CONDITIONAL', 'STRUCTURAL',
         'RETIRED', 'PROVED', 'CONDITIONAL-FORCED']

def registry_tiers(path):
    """id -> set of tier words appearing on that id's defining line."""
    out = {}
    for line in open(path):
        m = (re.match(r'\s*(?:\|\s*|\-\s*\*\*|##\s*)(T\d{1,4})\b', line)
             or re.match(r'\|[^|]*\|[^|]*\|\s*(T\d{1,4}) \(', line))
        if not m:
            continue
        up = line.upper()
        out.setdefault(m.group(1), set()).update(t for t in TIERS if t in up)
    return out

def main(root):
    reg = registry_tiers(os.path.join(root, 'notes', 'BST_AC_Theorem_Registry.md'))
    rub = os.path.join(root, 'notes', 'BST_Completeness_Rubric_and_Roadmap.md')

    # COVERAGE CHECK FIRST, and it is the one that matters.
    # This lint reads a tag format its own author invented and also wrote into the
    # rubric, so "does my tag parse" is self-confirming (R66: a control written in
    # the checker's notation validates the checker's notation).  The detection that
    # is NOT self-confirming is the complement: a substantive row carrying NO tag.
    # That must-catch is derived from the artifact, not from my notation.
    # SCOPE, STATED RATHER THAN SILENT.  `len(cells) < 3` is a restriction I authored,
    # and an unstated authored restriction is exactly the defect this file exists to
    # catch (cf. a digit-width in a regex).  It excludes the 2-column External<->Internal
    # axis map, which is a correspondence table carrying no tier and no claim, so no
    # registry id applies to it.  The exclusion is REPORTED below so a reader can
    # disagree with it, instead of discovering it by reading the source.
    untagged, excluded_2col = [], 0
    for line in open(rub):
        if not line.startswith('|') or line.startswith('|---'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if not any(cells):
            continue
        if len(cells) < 3:
            excluded_2col += 1
            continue
        if cells[0].lower() in ('#', 'crit', 'external'):   # header
            continue
        if '[registry:' not in line:
            untagged.append(cells[0][:40] or cells[1][:40])
    if untagged:
        print("SUBSTANTIVE ROWS WITH NO JOIN KEY (coverage gap):")
        for u in untagged:
            print(f"   {u}")
        print()

    rows = unresolved = mismatches = 0
    for line in open(rub):
        m = re.search(r'\*\*\[registry: ([^\]·]+)', line)
        if not m:
            continue
        rows += 1
        if 'UNRESOLVED' in line:
            unresolved += 1
        ids = [i.strip() for i in m.group(1).split(',') if i.strip().startswith('T')]
        missing = [i for i in ids if i not in reg]
        if missing:
            print(f"  MISSING FROM REGISTRY: {', '.join(missing)}")
            mismatches += 1
        # TIER COMPARISON IS NOT RUN, AND THAT IS DELIBERATE.
        # A rubric row summarizes several claims and legitimately contains several
        # tier words, so "any tier word in this row" cannot be attributed to any one
        # cited id.  Run that way, this check produced 2 false positives on its first
        # run (T2547, T1829) and 0 true positives.  A check that cannot succeed proves
        # nothing; reporting its output as findings would be over-stating a negative.
        # Enabling it needs PER-ID tier attribution in the rubric row -- the next
        # structural step, not a regex change.
        pass

    print(f"\n{rows} rubric rows carry a join key | {unresolved} contain an UNRESOLVED hole "
          f"| {mismatches} missing id(s)")
    print("TIER COMPARISON: NOT ENABLED -- needs per-id tier attribution in the rubric row. "
          "See the note in the source; it is a known gap, not a passing check.")
    print(f"{len(reg)} registry ids indexed | {len(untagged)} substantive row(s) with NO join key")
    print(f"SCOPE: {excluded_2col} two-column row(s) excluded by an authored rule "
          f"(the External<->Internal axis map: a correspondence table, no tier, no claim, "
          f"no registry id applies). Stated so it can be disputed, not discovered.")
    return 1 if (mismatches or untagged) else 0

if __name__ == '__main__':
    sys.exit(main(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
