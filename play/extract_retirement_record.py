#!/usr/bin/env python3
"""Extract the DISTINCT retired readings from the corpus into a machine-readable record.

WHY THIS EXISTS (Lyra's catch, R66): a hand-maintained RETIRED_READINGS list means
detector coverage silently narrows on every retirement nobody remembers to append.
Coverage must be DERIVED from the retirement record, not TRANSCRIBED into a checker.
This builds the record; detectors read it.

WHAT IT IS NOT: a retirement count.  1092 files contain retirement TEXT; that is a
file count, not a reading count, and quoting it as one would be the same error as
reading a pool size instead of an in-window count.

CONTROLS ARE COPIED FROM THE CORPUS, NEVER AUTHORED (R66): a control written in the
checker's own notation validates the checker's notation.  The must-catch strings below
were pasted from the registry, including their Unicode.
"""
import json, os, re, sys, collections

# --- controls, copied verbatim from the corpus (NOT retyped) ---
MUST_CATCH = [
    'A²=rank',        # registry T2516, U+00B2 -- an ASCII 'A^2=rank' control MISSES this
    'T2198',          # retired CKM integer-ratio row
]
MUST_REJECT = [
    'ET-A2 = rank/g', # false positive that fired on the earlier hand-written control
]
# Copied from the corpus: the tail that produced the T201 false positive.  The object
# next to the verb was KEPT; something else was retired.  Proximity cannot tell them
# apart, so this is a control on the BUCKETING, not on the regex.
POLARITY_CONTROL = '(K1675), the canonical **T201 kept** — the drop-Γ pattern done RIGHT (retire t'
# Contrast markers meaning "the nearby object is NOT the retirement subject".
NEGATION = re.compile(r'\b(kept|KEPT|withdrawn|not retired|over-claim|flag withdrawn|stands|survives)\b')

RETIRE = re.compile(
    r'(?P<verb>RETIRED|Retired|retired|RETRACTED|Retracted|retracted)'
    r'(?P<tail>[^.\n|]{0,120})')
KCITE = re.compile(r'\bK\d{2,4}\b')
TID = re.compile(r'\bT\d{1,4}\b')
# a "reading" is a named object: a formula-ish token, or a quoted form
FORMULA = re.compile(r'[A-Za-zα-ωΑ-Ω_][A-Za-z0-9_α-ωΑ-Ω²³⁵⁴]*\s*=\s*[^\s,;)]+')

def scan(root):
    notes = os.path.join(root, 'notes')
    readings = collections.defaultdict(lambda: {'citations': set(), 'theorems': set(),
                                                'files': set(), 'quotes': [],
                                                'bare_id': False, 'negated': False})
    files = 0
    for dirpath, _, names in os.walk(notes):
        for nm in names:
            if not nm.endswith('.md'):
                continue
            path = os.path.join(dirpath, nm)
            try:
                txt = open(path, encoding='utf-8', errors='replace').read()
            except OSError:
                continue
            hit = False
            for m in RETIRE.finditer(txt):
                tail = m.group('tail')
                forms = FORMULA.findall(tail)
                tids = TID.findall(tail)
                ks = KCITE.findall(tail)
                # a reading needs a NAMED OBJECT -- a formula or a theorem id
                bare_id_only = not forms
                negated = bool(NEGATION.search(tail))
                for key in [f.strip() for f in forms] + tids:
                    if len(key) < 3:
                        continue
                    r = readings[key]
                    if bare_id_only and re.fullmatch(r'T\d{1,4}', key):
                        r['bare_id'] = True
                    if negated:
                        r['negated'] = True
                    r['citations'].update(ks)
                    r['theorems'].update(tids)
                    r['files'].add(os.path.relpath(path, root))
                    if len(r['quotes']) < 2:
                        r['quotes'].append(tail.strip()[:110])
                    hit = True
            files += hit
    return readings, files

def main(root):
    readings, files = scan(root)
    out, unreliable = {}, {}
    for k, v in readings.items():
        rec = {'citations': sorted(v['citations']), 'theorems': sorted(v['theorems']),
               'n_files': len(v['files']), 'files': sorted(v['files'])[:5],
               'quotes': v['quotes'],
               'review_status': 'CANDIDATE — extracted, NOT hand-verified'}
        # A bare theorem id next to a retirement verb may be the SUBJECT of the
        # retirement, or an object explicitly KEPT while something else was retired
        # (the T201 case: "the canonical T201 kept -- ... (retire ...)").  Proximity
        # cannot tell those apart, and no regex can: the information is in the prose,
        # not in the structure.  So the class is bucketed and labelled, NOT patched.
        if v['bare_id']:
            rec['review_status'] = ('UNRELIABLE BY CONSTRUCTION — a bare theorem id near a '
                                    'retirement verb; proximity cannot identify the SUBJECT')
            if v['negated']:
                rec['contrast_marker'] = ('a "kept"/"withdrawn"/"stands" marker appears in the same '
                                          'clause — the id is probably NOT the retired object')
            unreliable[k] = rec
        else:
            if v['negated']:
                rec['contrast_marker'] = 'a contrast marker appears in the same clause — verify polarity'
            out[k] = rec

    blob = json.dumps({**out, **unreliable}, ensure_ascii=False)
    failed = [c for c in MUST_CATCH if c not in blob]
    fired = [c for c in MUST_REJECT if c in out]

    print(f"files containing a retirement statement with a named object: {files}")
    print(f"DISTINCT candidate retired readings (formula-named): {len(out)}")
    print(f"  ...of which cite a K-audit: {sum(1 for v in out.values() if v['citations'])}")
    print(f"BUCKETED AS UNRELIABLE (bare theorem id, subject undecidable): {len(unreliable)}")
    t201 = unreliable.get('T201')
    print(f"  polarity control -- T201 bucketed as unreliable: "
          f"{'PASS' if t201 else 'FAIL'}"
          f"{' (contrast marker detected)' if t201 and 'contrast_marker' in t201 else ''}")
    print(f"\nCONTROLS (corpus-sourced):")
    for c in MUST_CATCH:
        print(f"  must-catch {c!r}: {'PASS' if c not in failed else 'FAIL'}")
    for c in MUST_REJECT:
        print(f"  must-reject {c!r}: {'PASS' if c not in fired else 'FAIL — fired'}")
    if failed:
        print("\nINSTRUMENT NOT VALIDATED — a must-catch case was missed. Record NOT written.")
        return 1

    dest = os.path.join(root, 'data', 'bst_retirements.json')
    json.dump({'meta': {
        'purpose': 'Derived retirement record. Detector coverage READS this; it is never transcribed.',
        'built_by': 'play/extract_retirement_record.py',
        'built': '2026-08-23',
        'warning': ('Every entry is a CANDIDATE until hand-verified. This is an extraction, not a '
                    'ruling. n_files is a file count and is NOT a retirement count.'),
        'controls': {'must_catch': MUST_CATCH, 'must_reject': MUST_REJECT,
                     'note': 'Copied from the corpus, not authored. A control written in the '
                             "checker's notation validates the checker's notation."},
        'distinct_candidate_readings': len(out),
        'unreliable_bucket_size': len(unreliable),
        'bucketing_note': ('Bare theorem ids adjacent to a retirement verb are bucketed separately '
                           'and are UNRELIABLE BY CONSTRUCTION. The subject of a retirement lives in '
                           'the prose, not in the structure, so no regex resolves this -- it is a '
                           'type (C) limit and is labelled rather than patched.')},
        'readings': out, 'unreliable_bare_theorem_ids': unreliable},
        open(dest, 'w'), indent=1, ensure_ascii=False)
    print(f"\nwrote {dest}")
    return 0

if __name__ == '__main__':
    sys.exit(main(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
