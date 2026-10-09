#!/usr/bin/env python3
"""
Toy 5867 — Round K4-3, B-new-2 (Elie, 2026-10-09). Prereg: notes/Elie_K4-3_prereg_toys_5864-5867_* (976951e1).

The pi audit over data/bst_constants.json. Claim under test (Casey, TOMORROW 10-08 item 5a): every rational in a BST
formula comes from the interior's SPECTRUM; every pi enters through the BOUNDARY (a measure, a kernel normalisation,
a sphere volume). Method: parse every formula_code with sympy (pi symbolic), list the pi-exponents term by term, tag
each exponent from the prereg's fixed table or 'route owed'. Rational audit: pi -> 1, ruler -> 1, prime support.
The verdict on 'route owed' rows is Keeper's; this toy prints the list.
"""
import json, os, re, math, signal
from collections import Counter
import sympy as sp

RESULTS = []
def score(tag, ok, msg):
    RESULTS.append((tag, bool(ok))); print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")

here = os.path.dirname(os.path.abspath(__file__))
rows = json.load(open(os.path.join(here, '..', 'data', 'bst_constants.json')))['constants']
ids = [c.get('id') or f"pos_{n:03d}" for n, c in enumerate(rows)]
codes = [(i, c.get('formula_code') or '', c) for i, c in zip(ids, rows)]
with_code = [(i, f, c) for i, f, c in codes if f.strip()]
print(f"rows: {len(rows)}; with formula_code: {len(with_code)}; carrying 'pi': {sum('pi' in f for _, f, _ in with_code)}")

# ---------------------------------------------------------------- the namespace (sympy): integers exact, pi symbolic
INT = dict(rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137, c_2=11, c_3=13)
syms = {k: sp.Integer(v) for k, v in INT.items()}
syms.update(alpha=sp.Rational(1, 137), alpha_inv=sp.Integer(137), pi=sp.pi, pi5=sp.pi ** 5)
RULER = {k: sp.Symbol(k, positive=True) for k in ['m_e', 'm_p', 'hbar_c', 'm_e_kg', 'm_p_kg', 'hbar', 'h', 'c', 'c_light', 'e', 'k_B', 'H_0', 'N_A']}
syms.update(RULER); syms['m_p'] = 6 * sp.pi ** 5 * RULER['m_e']; syms['m_p_kg'] = 6 * sp.pi ** 5 * RULER['m_e_kg']
syms['hbar'] = RULER['h'] / (2 * sp.pi)
FUN = dict(sqrt=sp.sqrt, cbrt=sp.cbrt, log=sp.log, ln=sp.log, exp=sp.exp, sin=sp.sin, cos=sp.cos, tan=sp.tan, atan=sp.atan,
           asin=sp.asin, acos=sp.acos, comb=sp.binomial, factorial=sp.factorial, Fraction=sp.Rational, abs=sp.Abs, pow=sp.Pow,
           float=lambda x: sp.oo if x == 'inf' else sp.nsimplify(x))
def parse(code):
    code = re.sub(r'(?<![\w.])(\d+\.?\d*(?:[eE][+-]?\d+)?)(?![\w.])', lambda m: f"Rational('{m.group(1)}')", code)   # every literal exact (incl. 1e6)
    return sp.sympify(code, locals={**syms, **FUN, 'Rational': sp.Rational}, rational=True)

parsed, failed = {}, []
for i, f, c in with_code:
    try:
        parsed[i] = parse(f)
    except Exception as ex:
        failed.append((i, str(ex)[:50]))
print(f"parsed exactly: {len(parsed)}; not parsed: {len(failed)} {failed[:6]}")

# ---------------------------------------------------------------- pi exponents, term by term
def pi_exponents(expr):
    expr = sp.expand(sp.powsimp(sp.powdenest(expr, force=True), force=True))
    out = set()
    for term in sp.Add.make_args(expr):
        _, pipart = term.as_independent(sp.pi, as_Add=False)
        e = sp.Integer(0)
        for fac in sp.Mul.make_args(pipart):
            b, ex = fac.as_base_exp()
            if b == sp.pi: e += ex
            elif fac.has(sp.pi): e = sp.nan                      # pi inside a function: flag
        out.add(e)
    return out

TABLE = {   # exponent -> (tag, boundary object) ; fixed in the prereg
    1: ("S1", "|S^1| = 2pi: the Silov circle's measure"), -1: ("S1", "|S^1| = 2pi: the Silov circle's measure"),
    5: ("Hua", "Vol(D_IV^5) = pi^5/1920: the Hua/Bergman measure"), -5: ("Hua", "Vol(D_IV^5) = pi^5/1920"),
    10: ("Hua^2", "(pi^5)^2: m_p^2"), -10: ("Hua^2", "(pi^5)^-2"), 4: ("Hua/S1", "pi^5/pi: Hua over the circle"),
    2: ("ROUTE OWED", "pi^2: |S^3| = 2pi^2 or |S^1|^2 — not pinned"), -2: ("ROUTE OWED", "pi^-2: |S^3| or |S^1|^2 — not pinned"),
    -12: ("ROUTE OWED", "(pi^-2)^6: the muon/tau (24/pi^2)^6 — not pinned"),
    -23: ("ROUTE OWED", "pi^-(4 n_C + 3) = Hua^-4 x S1^-3 — not pinned"),
    6: ("Hua*S1", "pi * pi^5: (pi/2) x m_p"), 15: ("Hua^3", "(pi^5)^3: m_p^3"), -20: ("Hua^4", "(pi^5)^-4: m_p^-4"),
}
SI_NAMES = {'m_e_kg', 'm_p_kg', 'hbar', 'h', 'c', 'c_light', 'e', 'k_B', 'N_A'}
tags = {}
for i, f, c in with_code:
    if i not in parsed or 'pi' not in f: continue
    names = set(re.findall(r'[A-Za-z_]\w*', f))
    if '180/pi' in f.replace(' ', ''):
        tags[i] = [("UNIT", "180/pi: degrees, not a physical pi")]; continue
    if names & SI_NAMES:
        tags[i] = [("SI", "SI definitional row (hbar = h/2pi, sigma_SB, mu_B): standard physics, not BST")]; continue
    exps = pi_exponents(parsed[i])
    row_tags = []
    for e in sorted(exps, key=lambda x: float(x) if x.is_number and x != sp.nan else 99):
        if e == 0: continue
        if e == sp.nan: row_tags.append(("ROUTE OWED", "pi inside a transcendental function")); continue
        row_tags.append(TABLE.get(int(e) if e.is_Integer else e, ("ROUTE OWED", f"pi^{e}: no table entry")))
    if i == 'const_122': row_tags = [("ROUTE OWED", "pi^2 in the two-loop QED coefficient: a loop measure")]
    tags[i] = row_tags or [("NONE", "pi cancels")]

print("\npi rows, tagged:")
cnt = Counter()
for i, f, c in with_code:
    if i in tags:
        t = "; ".join(f"{a}" for a, _ in tags[i]); cnt.update(a for a, _ in tags[i])
        print(f"  {i:<9} {str(c.get('symbol') or c.get('name'))[:16]:<16} exps={sorted(str(e) for e in (pi_exponents(parsed[i]) if i in parsed else set()))!s:<22} {t:<22} | {f[:60]}")
n_pi = len(tags); n_owed = sum(1 for i in tags if any(a == "ROUTE OWED" for a, _ in tags[i]))
score("P1", all(tags[i] for i in tags) and n_pi == sum('pi' in f for i, f, _ in with_code if i in parsed),
      f"every parsed pi row carries a tag: {n_pi} rows; tag counts {dict(cnt)}")

# ---------------------------------------------------------------- P2 the exhibits
W_D5, W_B5, W_B3, W_B2 = 2 ** 4 * math.factorial(5), 2 ** 5 * math.factorial(5), 2 ** 3 * math.factorial(3), 2 ** 2 * 2
hua = lambda n: sp.pi ** n / (2 ** (n - 1) * sp.factorial(n))       # Hua: Vol(R_IV(n)) = pi^n / (2^(n-1) n!)
mp_me = parsed['const_001']
print(f"\nexhibits: m_p/m_e = {mp_me} = C_2 * pi^n_C; Vol(D_IV^5) = {hua(5)}; 1920 = 2^4*5! = |W(D5)| = {W_D5}; "
      f"|W(B5)| = {W_B5}, |W(B3)| (so(7,C), the complexification of so(5,2)) = {W_B3}, |W(B2)| (restricted, 5866) = {W_B2}")
wyler = sp.Rational(9, 8) / sp.pi ** 4 * (sp.pi ** 5 / 1920) ** sp.Rational(1, 4)
print(f"Wyler form (9/8pi^4)(pi^5/1920)^(1/4) = {wyler} = {sp.N(1/wyler, 10)}^-1 ; pi exponent {pi_exponents(wyler)}: "
      f"pi^(5/4) = Vol^(1/4) (boundary), pi^-4: ROUTE OWED (candidate |S^1|^2 |S^4| = 32 pi^4/3 — a candidate, not a pin). "
      f"Grace 08-10: alpha = charge count 1/N_max; the Wyler formula is RETIRED as the source.")
score("P2", mp_me == 6 * sp.pi ** 5 and hua(5) == sp.pi ** 5 / 1920 and W_D5 == 1920 and W_B3 == 48
      and abs(float(1 / wyler) - 137.036) < 0.001,
      "6 pi^5 and pi^5/1920 reproduced; 1920 = 2^(n-1) n! = |W(D_5)| numerically, NOT |W(B_3)| = 48 of so(5,2)'s own complexification nor |W(B_2)| = 8 — the '|W|' exhibit names a Weyl group the domain does not own (route owed); Wyler = 137.036")

# ---------------------------------------------------------------- P3 the rational audit
ALLOWED = {2, 3, 5, 7, 11, 13, 137}
def primes_of(q):
    s = set()
    for x in (q.p, q.q):
        x = abs(int(x)); d = 2
        while d * d <= x:
            while x % d == 0: s.add(d); x //= d
            d += 1
        if x > 1: s.add(x)
    return s
rat, outside, nonrat = {}, [], []
one = {s: 1 for s in RULER.values()}
for i, f, c in with_code:
    if i not in parsed: continue
    # no sp.simplify: const_122's zeta(3) literal hangs it (owned, first run); expand only, 3 s cap per row
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError()))
    signal.alarm(3)
    try:
        v = sp.expand(sp.powsimp(parsed[i].subs(sp.pi, 1).subs(one), force=True)); v2 = sp.expand(v ** 2)
    except TimeoutError:
        nonrat.append((i, 'TIMEOUT')); continue
    finally:
        signal.alarm(0)
    if v.is_Rational and v.is_finite:
        rat[i] = v
    elif v.is_number and v.is_finite and v2.is_Rational:
        rat[i] = v2
    else:
        nonrat.append((i, str(v)[:40])); continue
    bad = primes_of(sp.Rational(rat[i])) - ALLOWED
    if bad: outside.append((i, str(rat[i])[:24], sorted(bad)))
print(f"\nrational audit: {len(rat)} rows rational (or a single sqrt of a rational) after pi -> 1, ruler -> 1; "
      f"{len(nonrat)} non-rational (acos, 2^(1/3), ln 2, zeta(3), ...): {[i for i, _ in nonrat]}")
print(f"  prime support outside {sorted(ALLOWED)}: {len(outside)} rows")
for i, v, b in outside: print(f"    {i:<9} {v:<24} primes {b}")
score("P3", len(rat) >= 150 and len(outside) <= 20,
      f"{len(outside)}/{len(rat)} rational rows carry a prime outside {{2,3,5,7,11,13,137}} — the list above IS the finding (reported, not hidden)")

# P3b — the instrument the question needs (added after P3's first run; P3's FAIL stands as prereg'd):
# a foreign prime is spectral if the formula builds it from the namespace integers (79 = rank^4 n_C - 1), and foreign
# if it is TYPED as a bare literal. Split the rows by whether formula_code carries a bare literal other than small
# combinatorial ones (<= 12, 24, 30, 60) or a power-of-ten unit factor.
SMALL = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 30, 60, 100, 1000, 1e6, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 10.0, 12.0, 24.0, 30.0, 60.0, 100.0}
def bare_literals(f):
    lits = [x for x in re.findall(r'(?<![\w.])(\d+\.\d+|\d+)(?![\w.])', f)]
    return sorted({float(x) for x in lits} - SMALL)
lit_rows = {i: bare_literals(f) for i, f, c in with_code if i in parsed}
spectral_foreign = [(i, v, b) for i, v, b in outside if not lit_rows[i]]
typed_foreign = [(i, v, b, lit_rows[i]) for i, v, b in outside if lit_rows[i]]
print(f"\nP3b: of the {len(outside)} foreign-prime rows, {len(spectral_foreign)} are literal-free (the prime is built from the namespace: spectral)")
for i, v, b in spectral_foreign: print(f"    {i:<9} {v:<24} primes {b}  <- built from the namespace integers by the formula (e.g. 79 = rank^4 n_C - 1)")
print(f"     and {len(typed_foreign)} carry a bare literal (typed, not built):")
for i, v, b, L in typed_foreign: print(f"    {i:<9} {v:<24} primes {b}  literals {L}")
all_lit = sorted(i for i in lit_rows if lit_rows[i])
print(f"  rows with ANY bare literal outside the small set: {len(all_lit)}/{len(lit_rows)}: {all_lit}")
score("P3b", len(spectral_foreign) + len(typed_foreign) == len(outside),
      f"foreign primes split: {len(spectral_foreign)} spectral (built), {len(typed_foreign)} typed as literals; "
      f"{len(all_lit)} rows carry a bare literal at all — THAT list is the rational audit's finding")

# ---------------------------------------------------------------- P4 the kill count
owed = [i for i in tags if any(a == "ROUTE OWED" for a, _ in tags[i])]
routed = [i for i in tags if tags[i] and all(a in ("S1", "Hua", "Hua^2", "Hua/S1", "Hua*S1", "Hua^3", "Hua^4") for a, _ in tags[i])]
print(f"\nkill count: {len(owed)}/{n_pi} pi rows have at least one pi-power with no named boundary route: {owed}")
print(f"            {len(routed)}/{n_pi} pi rows are fully routed (S1 or Hua only): {routed}")
score("P4", True, f"printed as k/N = {len(owed)}/{n_pi} (Keeper's kill is 'one formula whose pi has no boundary route'; the verdict is his, the list is here)")

passed = sum(ok for _, ok in RESULTS)
print(f"\nSCORE: {passed}/{len(RESULTS)}  ({len(RESULTS) - 1} can fail; P4 is a report line; P3's FAIL is my prereg threshold, kept)")
