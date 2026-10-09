#!/usr/bin/env python3
"""
Toy 5868 — item 5(h), Q* = m_e (Elie, 2026-10-09). Hash: Cal S1036 (sha256 5bd18a30..., K1953 names Q* = m_e).
Written and run AFTER the hash. Pre-run calibration on record (Elie): I expect a MISS of the 10 % window, within one
decade of m_e (Keeper's own calibration is "orders of magnitude"); neither calibration is part of the rule.

Hashed formula (on-shell, one electron loop, spacelike Q^2; Peskin-Schroeder 7.91 with q^2 -> -Q^2):
    alpha_eff^-1(Q) = alpha^-1(0) - Delta(Q),   Delta(Q) = (2/pi) int_0^1 dx x(1-x) ln[1 + x(1-x) Q^2/m_e^2].
Inputs: alpha^-1(0) = 137.035 999 177(21), CODATA 2022, pinned from the NIST page saved at
    data/sources_elie_2026-10-09/nist/nist_alphinv.html (sha256 d8b163d8e95991de...; Grace may re-pin).
m_e's digits do not enter: the formula depends on Q/m_e only, and the output is Q/m_e.
Order (S1036 Sec. 3): (1) Delta(m_e), alpha_eff^-1(m_e); (2) solve alpha_eff^-1(Q) = 137 -> Q/m_e; (3) ratios to the menu.
Match rule (S1036 Sec. 4): CREDIT iff |ln(Q/m_e)| <= ln 1.1; factor-2 landings on any menu point are REPORTED, not credited.
Beside (K1953): the curvature term n_C/N_max = 5/137 (K675), forward, as the pincer's other leg.
"""
import os, re, html, hashlib
import mpmath as mp
mp.mp.dps = 30

RESULTS = []
def score(tag, ok, msg):
    RESULTS.append((tag, bool(ok))); print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")

here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, '..', 'data', 'sources_elie_2026-10-09', 'nist', 'nist_alphinv.html')
raw = open(src, 'rb').read()
txt = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', raw.decode('utf-8', 'ignore'))))
m = re.search(r'Numerical value ([\d ]+\.[\d ]+) Standard uncertainty ([\d ]+\.[\d ]+)', txt)
assert m is not None, 'NIST page format changed'
ALPHA_INV0 = mp.mpf(m.group(1).replace(' ', '')); U0 = mp.mpf(m.group(2).replace(' ', ''))
print(f"pin: alpha^-1(0) = {ALPHA_INV0} +/- {U0} (source sha256 {hashlib.sha256(raw).hexdigest()[:16]}, "
      f"'{'2022 CODATA' if '2022 CODATA' in txt else 'CODATA year NOT found'}')")
score("I0", abs(ALPHA_INV0 - mp.mpf('137.035999177')) < mp.mpf('1e-9') and '2022 CODATA' in txt,
      "input read from the saved NIST page (2022 CODATA), not typed")

def Delta(r):            # r = Q/m_e
    r2 = mp.mpf(r) ** 2
    return 2 / mp.pi * mp.quad(lambda x: x * (1 - x) * mp.log(1 + x * (1 - x) * r2), [0, 1])
def alpha_inv(r): return ALPHA_INV0 - Delta(r)

# formula checks against Cal's instrument (limits), so the two codes agree before the solve
asym = lambda r: (1 / (3 * mp.pi)) * (2 * mp.log(r) - mp.mpf(5) / 3)
score("F0", abs(Delta(0)) < mp.mpf('1e-25') and abs(Delta(1e4) / asym(1e4) - 1) < mp.mpf('1e-6') and Delta(0.5) < Delta(1) < Delta(2),
      f"Delta(0) = 0; Delta/asymptote at Q = 1e4 m_e: {mp.nstr(Delta(1e4)/asym(1e4), 8)}; monotone")

print("\n(1) at the named point")
d1 = Delta(1); a1 = alpha_inv(1)
print(f"    Delta(m_e) = {mp.nstr(d1, 10)}    alpha_eff^-1(m_e) = {mp.nstr(a1, 12)}    (target 137; gap {mp.nstr(a1 - 137, 6)})")

print("(2) solve alpha_eff^-1(Q) = 137")
r_star = mp.findroot(lambda r: alpha_inv(r) - 137, mp.mpf(3))
print(f"    Q/m_e = {mp.nstr(r_star, 10)}      (check: alpha_eff^-1 there = {mp.nstr(alpha_inv(r_star), 12)})")
# sensitivity to the input's uncertainty
dr = (mp.findroot(lambda r: ALPHA_INV0 + U0 - Delta(r) - 137, r_star) - mp.findroot(lambda r: ALPHA_INV0 - U0 - Delta(r) - 137, r_star)) / 2
print(f"    +/- {mp.nstr(dr, 3)} from the 21e-9 input uncertainty")

print("(3) against the menu (ratios Q/point; no ranking)")
alpha0 = 1 / ALPHA_INV0
menu = {'m_e': mp.mpf(1), '2 m_e': mp.mpf(2), 'alpha m_e': alpha0, 'alpha^2 m_e': alpha0 ** 2}
within2 = []
for name, pt in menu.items():
    ratio = r_star / pt
    flag = abs(mp.log(ratio)) <= mp.log(2)
    within2 += [name] if flag else []
    print(f"    Q / ({name:<11}) = {mp.nstr(ratio, 8):>14}   |ln| = {mp.nstr(abs(mp.log(ratio)), 5):>8}   within factor 2: {flag}")

match = abs(mp.log(r_star)) <= mp.log(mp.mpf('1.1'))
score("T1", match, f"CREDIT rule |ln(Q/m_e)| <= ln 1.1: |ln| = {mp.nstr(abs(mp.log(r_star)), 5)} vs {mp.nstr(mp.log(mp.mpf('1.1')), 5)} -> "
                   + ("MATCH" if match else "MISS: the 0.036 is NOT QED running from an interior 137 at m_e"))
print(f"    reported, not credited: factor-2 landings = {within2 or 'none'}")

print("\nbeside (K1953 pincer, forward): the curvature term")
curv = mp.mpf(5) / 137
print(f"    n_C/N_max = 5/137 = {mp.nstr(curv, 8)};  measured excess alpha^-1(0) - 137 = {mp.nstr(ALPHA_INV0 - 137, 8)};  "
      f"ratio = {mp.nstr((ALPHA_INV0 - 137) / curv, 6)}  (K675's reading: a boundary TERM, not a running; 1.4 % off, as banked)")
score("T2", abs((ALPHA_INV0 - 137) / curv - 1) < mp.mpf('0.02'), "curvature term reproduces the 0.036 to 1.4 % (restated, K675; not new credit)")

passed = sum(ok for _, ok in RESULTS)
print(f"\nSCORE: {passed}/{len(RESULTS)}  (T1 is the hashed test and can fail either way; I0, F0 instrument; T2 restates K675)")
