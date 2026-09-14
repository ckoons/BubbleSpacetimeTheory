#!/usr/bin/env python3
"""Keeper — v1→v1.1 diff audit for the Part B freeze (Round 146 K1). A re-freeze is scoped BEFORE the file is reopened
(K1898 §6, six items). This script diffs the two frozen files and classifies every changed hunk into a declared item by
keyword; any hunk matching no item is OUT OF SCOPE and the re-freeze is refused. Self-test: a synthetic pair with one
in-scope and one out-of-scope hunk must classify both correctly.
Usage: keeper_partB_diff_audit.py v1.md v1_1.md   |   --selftest"""
import sys, difflib, re, tempfile, os
FRONT = re.compile(r'^(title:|date:|status:|# |— Cal|\s*$)')  # front matter, headers, signature, blank: not substance
ITEMS = {
 '(1) narrowings':      r'common velocity|best-measured|assigns to the exterior|local flow',
 '(2) bin-membership':  r'bin.membership|edge|observed redshift|Hausegger|Dalang|boost(ed|ing) of the redshift|B_i|boundary term|f_i = 2',
 '(3) prior art':       r'prior art|Wu|Xia|2608\.30914|DESI|replication',
 '(4) evolution':       r'evolution|Dalang|Bonvin|Guandalin|luminosity function|2404\.07929|2212\.04925|2111\.03616',
 '(5) power':           r'power|sigma_K|σ_K|150 km|450 km|3σ Landing B|3\\sigma',
 '(6) P3':              r'P3|redshift.dipole|clock|Rac|ℓ = 1|\\ell = 1',
}
def hunks(a, b):
    """Per changed LINE, not per opcode hunk: adjacent in-scope and out-of-scope edits merge into one hunk and the
    in-scope keyword would launder the other (the self-test's first failure). Each inserted/replaced line stands alone."""
    A = open(a, encoding='utf-8').read().splitlines(); B = open(b, encoding='utf-8').read().splitlines()
    out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, A, B).get_opcodes():
        if tag == 'equal': continue
        removed = A[i1:i2]; added = B[j1:j2]
        if tag == 'delete':
            for l in removed: out.append(('delete', l, ''))
        else:
            for k, l in enumerate(added):
                out.append((tag, removed[k] if k < len(removed) else '', l))
    return out
def classify(h):
    text = h[1] + '\n' + h[2]
    hits = [k for k, rx in ITEMS.items() if re.search(rx, text, re.I)]
    return hits
def audit(a, b, verbose=True):
    hs = hunks(a, b); out_of_scope = []
    for h in hs:
        if FRONT.match((h[2] or h[1]).strip()) and not (h[2] and h[1] and h[2].strip() and not FRONT.match(h[2].strip())):
            if verbose: print('  [--] front matter / blank :: %s' % (h[2] or h[1]).strip()[:60])
            continue
        hits = classify(h)
        if verbose: print('  [%s] %s :: %s' % ('OK ' if hits else 'OUT', ', '.join(hits) or 'no declared item', (h[2] or h[1]).strip().replace('\n', ' ')[:90]))
        if not hits: out_of_scope.append(h)
    print('%d hunk(s), %d OUT OF SCOPE -> %s' % (len(hs), len(out_of_scope), 'REFUSED' if out_of_scope else 'in scope'))
    return 1 if out_of_scope else 0
def selftest():
    d = tempfile.mkdtemp(); a = os.path.join(d, 'v1.md'); b = os.path.join(d, 'v11.md')
    base = ['# frozen', 'bins fixed', 'tolerance 5 percent', 'hatch H1..H6', 'the end']
    open(a, 'w').write('\n'.join(base))
    new = base[:]; new.insert(2, 'prior art consistent: Wu & Xia 2026, DESI DR1'); new[3] = 'tolerance 7 percent'  # second edit is out of scope
    open(b, 'w').write('\n'.join(new))
    hs = hunks(a, b); cls = [bool(classify(h)) for h in hs]
    ok = (cls == [True, False]) if len(cls) == 2 else False
    print('SELFTEST', 'PASS' if ok else 'FAIL', cls); return 0 if ok else 1
if __name__ == '__main__':
    if '--selftest' in sys.argv: sys.exit(selftest())
    sys.exit(audit(sys.argv[1], sys.argv[2]))
