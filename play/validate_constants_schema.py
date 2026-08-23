#!/usr/bin/env python3
"""Validate data/bst_constants.json against the REQUIRED_FIELDS_CONTRACT.

The error bar is the DETECTOR, not a nicety: a target with no error bar cannot be
compared to another target, so duplicate rows never surface as contradictions --
only as two independently plausible numbers.  That is how four tier-D rows
disagreed by 1.5% on one angle with nothing tripping.

Run before any pass that lands pinned values.  Exit 1 if a contested group is
still unpinned.  Grace, 2026-08-23.
"""
import json, math, sys, os

REL = {'identity': lambda x: x,
       'sqrt(1-x**2)': lambda x: math.sqrt(1 - x * x),
       'sqrt(x)': lambda x: math.sqrt(x)}
VAGUE = {'pdg 2024', 'pdg', 'pdg2024', 'codata', 'codata 2022', 'pdg 2022', ''}

def main(path):
    d = json.load(open(path))
    rows = d['constants']
    no_bar = [r for r in rows
              if r.get('observed_uncertainty') is None and r.get('observed_error') is None]
    vague = [r for r in rows if (r.get('observed_source') or '').strip().lower() in VAGUE]

    groups = {}
    for r in rows:
        if r.get('relation_to_canonical'):
            groups.setdefault(r['observable_key'], []).append(r)

    print(f"{len(rows)} rows | {len(no_bar)} with NO error bar | {len(vague)} with an underspecified source")
    print(f"{len(groups)} hand-assigned observable groups\n")

    bad = 0
    for key, grp in sorted(groups.items()):
        implied = []
        for r in grp:
            try:
                implied.append(REL[r['relation_to_canonical']](float(r['observed_value'])))
            except (TypeError, ValueError, KeyError):
                pass
        spread = (100 * (max(implied) - min(implied)) / min(implied)) if len(implied) > 1 else 0.0
        unpinned = sum(1 for r in grp if r.get('observed_uncertainty') is None)
        flag = 'CONTRADICTION' if spread > 0.05 else 'ok'
        if spread > 0.05 or unpinned:
            bad += 1
        print(f"  {key:22s} n={len(grp)} spread={spread:6.3f}%  unpinned={unpinned}/{len(grp)}  {flag}")

    print(f"\n{bad} group(s) still unpinned or self-contradictory.")
    return 1 if bad else 0

if __name__ == '__main__':
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1
                  else os.path.join(here, 'data', 'bst_constants.json')))
