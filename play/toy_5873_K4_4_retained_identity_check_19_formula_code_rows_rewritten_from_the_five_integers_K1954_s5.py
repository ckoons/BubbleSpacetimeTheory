#!/usr/bin/env python3
"""
Toy 5873 — Round K4-4, Lane C item 2 (Grace, 2026-10-09). RETAINED INSTRUMENT for the K1954 Section 5 ledger pass.

On 2026-10-09 (commit 54787d5f) 19 rows of data/bst_constants.json had their formula_code rewritten from a bare
literal to an expression in the five integers (+ namespace constants hbar_c, m_e), each per the row's OWN
formula_display / derivation_chain. Every rewritten row carries the key `k1954_bare_literal_2026_10_09` whose text
holds the OLD code verbatim ("Old code: '...'"). This toy re-evaluates old and new in the explorer's namespace and
fails if any pair differs. It also re-counts Elie 5867's bare-literal detector so the number on the board (42 -> 29)
is a measurement with a retained instrument, not a memory.

Can fail: P1 (any of the 19 pairs differs), P2 (fewer than 19 rows carry an old code), P3 (the detector count
drifts from 29 without a dated note). P4 is a report line.
"""
import json, os, re, sys
from math import pi, sqrt, log, exp, sin, cos, tan, atan, asin, acos, factorial, comb

here = os.path.dirname(os.path.abspath(__file__))
rows = json.load(open(os.path.join(here, '..', 'data', 'bst_constants.json')))['constants']
ids = [c.get('id') or f"pos_{n:03d}" for n, c in enumerate(rows)]
TAG = 'k1954_bare_literal_2026_10_09'

# the explorer's namespace (play/toy_bst_explorer.py EVAL_NS), plus the SI exacts const_128 uses
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
alpha = 1.0 / N_max; alpha_inv = N_max; pi5 = pi ** 5
m_e = 0.51099895000; m_p = 6 * pi5 * m_e; hbar_c = 197.3269804
ln = log; cbrt = lambda x: x ** (1.0 / 3.0); Fraction = lambda a, b: a / b
NS = dict(rank=rank, N_c=N_c, n_C=n_C, C_2=C_2, g=g, N_max=N_max, alpha=alpha, alpha_inv=alpha_inv, pi=pi, pi5=pi5,
          sqrt=sqrt, cbrt=cbrt, log=log, ln=ln, exp=exp, sin=sin, cos=cos, tan=tan, atan=atan, asin=asin, acos=acos,
          comb=comb, factorial=factorial, Fraction=Fraction, abs=abs, pow=pow, float=float,
          m_e=m_e, m_p=m_p, hbar_c=hbar_c, k_B=1.380649e-23, h=6.62607015e-34, c=2.99792458e8)

RESULTS = []
def score(tag, ok, msg):
    RESULTS.append((tag, bool(ok))); print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")

pairs, worst = [], 0.0
for i, c in zip(ids, rows):
    note = c.get(TAG, '')
    m = re.search(r"Old code: '(.*?)'\. Identity check", note)
    if not m:
        continue
    old, new = m.group(1), c['formula_code']
    vo, vn = eval(old, {}, dict(NS)), eval(new, {}, dict(NS))
    rel = abs(vo - vn) / max(abs(vo), 1e-300)
    worst = max(worst, rel); pairs.append((i, rel))
    print(f"    {i:<10} old={vo:<22.15g} new={vn:<22.15g} |d|/|old|={rel:.1e}")
score('P1', worst < 1e-12, f"all {len(pairs)} rewritten rows evaluate to their previous value (worst {worst:.1e})")
score('P2', len(pairs) == 19, f"{len(pairs)} rows carry an old code (expected 19)")

SMALL = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 30, 60, 100, 1000, 1e6, 0.5}   # Elie 5867's set
lit = r'(?<![\w.])(\d+\.?\d*(?:[eE][+-]?\d+)?)(?![\w.])'
left = [i for i, c in zip(ids, rows) if (c.get('formula_code') or '').strip()
        and sorted({float(x) for x in re.findall(lit, c['formula_code'])} - SMALL)]
score('P3', len(left) == 29, f"Elie-5867 bare-literal detector: {len(left)} rows (board 10-09 says 29; was 42)")
classes = {}
for i, c in zip(ids, rows):
    if i in left:
        k = re.search(r'\. (NAMED|VALUE|UNIT|MEASURED|SI|IDENTIFIED|INPUT|TEXTBOOK|REWRITTEN)', c.get(TAG, '. UNCLASSIFIED')).group(1)
        classes[k] = classes.get(k, 0) + 1
print(f"    classes of the {len(left)}: {classes}")
score('P4', all(i in [j for j, _ in pairs] or rows[ids.index(i)].get(TAG) for i in left),
      "every remaining literal row carries a dated class note (report line)")

n_ok = sum(ok for _, ok in RESULTS)
print(f"\nSCORE: {n_ok}/{len(RESULTS)}  (3 can fail: P1 P2 P3; P4 is a report line)")
sys.exit(0 if n_ok == len(RESULTS) else 1)
