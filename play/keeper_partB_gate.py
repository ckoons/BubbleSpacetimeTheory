#!/usr/bin/env python3
"""Keeper — the Part B gate (Round 145 K1). Three checks, each with a control, run BEFORE any catalogue is opened:
 1. HASH: the frozen protocol file's SHA256 equals the hash posted on the board (pass both; the script computes, never trusts).
 2. NO CATALOGUE BEFORE THE HASH: no file in the tree matching the named catalogues (Quaia, CatWISE, NVSS, RACS, VLASS)
    has an mtime earlier than the frozen file's; nothing in play/ or data/ larger than 5 MB with those names at all.
 3. CONTROLS BLIND: Elie's estimator toy carries a prereg line whose hash predates its SCORE line (the toy's own record).
Positive/negative controls on synthetic files gate every real run: a decoy catalogue must fire check 2; a wrong hash must fire check 1.
Usage: keeper_partB_gate.py --frozen <file> --hash <sha256> [--toy <toy.py>]   |   --selftest"""
import sys, os, re, hashlib, glob, time, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATS = re.compile(r'quaia|catwise|nvss|racs|vlass|secrest', re.I)
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
def check_hash(frozen, posted):
    h = sha(frozen); ok = h.lower().startswith(posted.lower()) and len(posted) >= 8
    return ok, 'HASH %s (%s posted=%s)' % ('OK' if ok else 'FAIL', h[:12], posted[:12])
def check_no_catalogue(frozen_mtime, root=ROOT):
    hits = []
    for base in ('play', 'data', 'notes', '.'):
        for p in glob.glob(os.path.join(root, base, '**', '*'), recursive=True):
            if os.path.isfile(p) and CATS.search(os.path.basename(p)) and not p.endswith(('.md', '.py', '.txt')):
                hits.append((p, os.path.getmtime(p), os.path.getsize(p)))
    early = [h for h in hits if h[1] < frozen_mtime]
    big = [h for h in hits if h[2] > 5_000_000]
    ok = not early and not big
    return ok, 'NO-CATALOGUE %s (%d catalogue-like files; %d before the freeze; %d over 5 MB)' % ('OK' if ok else 'FAIL', len(hits), len(early), len(big))
def check_controls_blind(toy):
    t = open(toy, encoding='utf-8', errors='replace').read()
    pre = re.search(r'prereg\W{0,10}([0-9a-f]{8,})', t, re.I); score = re.search(r'^SCORE', t, re.M | re.I)
    ok = bool(pre) and (score is None or (score and pre.start() < score.start()))
    return ok, 'CONTROLS-BLIND %s (prereg hash %s; SCORE line %s)' % ('OK' if ok else 'FAIL', pre.group(1)[:8] if pre else 'MISSING', 'after it' if (pre and score and pre.start() < score.start()) else ('absent' if not score else 'BEFORE the prereg — not blind'))
def selftest():
    d = tempfile.mkdtemp(); fz = os.path.join(d, 'frozen.md'); open(fz, 'w').write('frozen protocol v1\n')
    h = sha(fz); r = []
    r.append(check_hash(fz, h)[0] is True)                      # must pass
    r.append(check_hash(fz, 'deadbeefdeadbeef')[0] is False)     # must fail
    os.makedirs(os.path.join(d, 'data'), exist_ok=True); decoy = os.path.join(d, 'data', 'quaia_v1.fits'); open(decoy, 'wb').write(b'0' * 10)
    os.utime(decoy, (time.time() - 3600, time.time() - 3600))    # older than the freeze
    r.append(check_no_catalogue(os.path.getmtime(fz), root=d)[0] is False)  # decoy must fire
    os.remove(decoy); r.append(check_no_catalogue(os.path.getmtime(fz), root=d)[0] is True)
    toy = os.path.join(d, 'toy.py'); open(toy, 'w').write('# prereg abcdef12\nSCORE 4/4\n'); r.append(check_controls_blind(toy)[0] is True)
    open(toy, 'w').write('SCORE 4/4\n# prereg abcdef12\n'); r.append(check_controls_blind(toy)[0] is False)
    print('SELFTEST', 'PASS' if all(r) else 'FAIL', r); return 0 if all(r) else 1
if __name__ == '__main__':
    a = sys.argv[1:]
    if '--selftest' in a: sys.exit(selftest())
    frozen = a[a.index('--frozen')+1]; posted = a[a.index('--hash')+1]
    res = [check_hash(frozen, posted), check_no_catalogue(os.path.getmtime(frozen))]
    if '--toy' in a: res.append(check_controls_blind(a[a.index('--toy')+1]))
    for ok, msg in res: print(('[OK]   ' if ok else '[FAIL] ') + msg)
    print('GATE', 'OPEN — a catalogue may be opened' if all(o for o, _ in res) else 'CLOSED')
    sys.exit(0 if all(o for o, _ in res) else 1)
