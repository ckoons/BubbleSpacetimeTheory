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
# v1.2 -> v1.3 scope (K1903 §2): (i) x at the threshold; (ii) the vector-chi2 comparison; K1901 §3's §1 number; the declaration.
ITEMS_K1903 = {
 '(i) x at threshold':  r'x_i|threshold|selection limit|quadratic|derivative at|at the edge|0\.5 mag|local slope|2501\.06450|secant|tangent',
 '(ii) vector chi2':    r'χ²|chi2|\\chi\^2|vector|7\.815|14\.156|3 d\.o\.f|norm|debiased|tr\s*Σ|tr\s*\\Sigma|positional region|Siewert|2010\.08366|Δβ|\\Delta\\beta',
 '§1 number (K1901 §3)': r'443|149|σ_K|sigma_K|\\sigma_K|5758|5760|150 km',
 'declaration':         r'9b|K1903|v1\.3',
}
# v1.3 -> v1.4 scope (K1903 §6, board 12:41, K1905 §3-4, K1906 §1, Casey's word 12:5x): six declared items.
ITEMS_K1906 = {
 '§1 sentence (K1903 §6)':      r'149|170|250|415|5759|5760|redshift channel alone|joint',
 '§3.1 x-systematic':           r'x_i|secant|0\.2.mag|local slope|systematic|half.spread|curved counts|quadratic',
 '§2.1 sample (Casey)':         r'20\.5|20\.0|primary|robustness|brighter|magnitude limit|sample',
 '§4.4 clause (K1905 §4)':      r'sharp|smooth|sensitivity|outlier|×0\.5|×2|not determined|propagated uncertainty on',
 '§2.2 convention':             r'separation|great.circle|haversine|columns|\(l, b\)|mask',
 '§2.3 fallback (K1906 §1)':    r'selection function|NSIDE|weight|fallback|H5|released code|92eca506',
 'declaration':                 r'9c|K1905|K1906|v1\.4',
}
# v1.5.1 -> v1.5.2 scope (Cal §9f, declared; Elie 5765; Grace R153 G2 + 12:52; before any dipole): the LCDM prior on the intrinsic vector.
ITEMS_K1909 = {
 '(h) intrinsic term a vector; 4.2/4.3 linear unbounded': r'intrinsic vector|\\mathbf a|\ba_i\b|three components|unbounded|linear in|no bound|vector.*intrinsic|intrinsic.*vector',
 '(i) the prior + sensitivity fits':                    r'prior|D_\{?\\rm cls|D_cls|clustering dipole|Secrest 2021|908|L51|Gibelyou|zero.centred|zero-centered|√3|\\sqrt\{?3|factor (of )?ten|10 ?×|ten times|no-prior|without the prior|sensitivity',
 '(j) per-bin residual covariance':                     r'residual|covariance of the fitted|propagat|per-bin',
 '(k) §1 / 7.1(iii) paragraph':                         r'v1\.5\.2|capability|fractions|5765|false.fire|beyond ΛCDM|beyond LCDM|C by construction|405|352',
 '(l) design sigma re-evaluated':                       r'design|re-evaluated|σ_β|sigma_beta|135|160',
 '(m) §8 rescue clause':                                r'rescue|S3|null sky|prior sentence',
 'declaration':                                         r'9f|§974|Cal §974|K1909|referee.s objection|tuning channel',
}
# v1.5 -> v1.5.1 scope (K1908 §4 (a)-(g), board 11:01; declared before (vi)): seven items, each forced by a synthetic positive control.
ITEMS_K1908 = {
 '(a) region clause -> report':        r'region|25 ?%|quarter|sphere|2\.448|decisive|report',
 '(b) 185 design-level; H7':           r'185|β_\{\\rm CMB\}/2|beta_CMB/2|design|per.run|H7|175|band|mock mis|mis-specif',
 '(c) zeta column in 4.5':             r'ζ|zeta|intrinsic term|contaminant|mean redshift|⟨z⟩|\\langle z|p_i|z̃|ztilde|profile',
 '(d) A\' at this depth':              r"A′|C′|\\bA'(?!s)|\\bC'(?!s)|amplitude clause|count-only|cannot point|direction",
 '(e) response-corrected estimator':   r'response|R\^\{-1\}|R⁻¹|eigen|0\.72|1\.55|literal|second moment|unit-vector sum',
 '(f) S3 / negative control -> C':     r'S3|negative control|no boost|→ C|-> C|lands C|98',
 '(g) §1 recomputed':                  r'capability|A-capable|57|recomput|5763|5764|A_int|0\.005|0\.01',
 'declaration':                        r'9e|K1908|v1\.5\.1',
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
def changed_text(old, new):
    """K1908 fix (12:3x): classify the CHANGED substring only. These files are paragraph-long lines, so matching the whole
    line let any in-scope keyword already in the paragraph launder a sentence appended to it (negative control: 'Tolerance
    widened to 9 percent' passed under key (d) because the paragraph contained \"A's\"). Word-level diff; equal runs dropped."""
    if not old: return new
    if not new: return old
    a = re.findall(r'\S+|\s+', old); b = re.findall(r'\S+|\s+', new); out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag == 'equal': continue
        out.append(''.join(a[i1:i2]) + ' ' + ''.join(b[j1:j2]))
    return '\n'.join(out)
def classify(h):
    text = changed_text(h[1], h[2])
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
    # K1908 laundering case: an out-of-scope sentence APPENDED to a paragraph that already carries an in-scope keyword must be refused
    c = os.path.join(d, 'v12.md'); base2 = base[:]; base2[2] = 'tolerance 5 percent; prior art consistent: Wu & Xia 2026'
    open(a, 'w').write('\n'.join(base2)); open(c, 'w').write('\n'.join(base2[:2] + [base2[2] + ' Tolerance widened to 9 percent.'] + base2[3:]))
    cls2 = [bool(classify(h)) for h in hunks(a, c)]; ok2 = (cls2 == [False])
    print('SELFTEST', 'PASS' if (ok and ok2) else 'FAIL', cls, 'laundering refused:', ok2); return 0 if (ok and ok2) else 1
if __name__ == '__main__':
    if '--selftest' in sys.argv: sys.exit(selftest())
    if '--scope' in sys.argv:
        sc = sys.argv[sys.argv.index('--scope')+1].lower()
        ITEMS.clear(); ITEMS.update({'k1903': ITEMS_K1903, 'k1906': ITEMS_K1906, 'k1908': ITEMS_K1908, 'k1909': ITEMS_K1909}[sc])
    args = [a for a in sys.argv[1:] if not a.startswith('--') and a.lower() not in ('k1903', 'k1906', 'k1908', 'k1909')]
    sys.exit(audit(args[0], args[1]))
