#!/usr/bin/env python3
"""Toy 5769 — sin²θ₁₃ = 1/45 through the K1809 sibling count: the rule as text, with two controls (Cal §978 (B)). Elie, 2026-09-21.
Prereg: notes/Elie_PREREG_5769_..._2026-09-21.md. Menu = toy 5755's (products/ratios of <= 3 of V, with and without sqrt).
Rule: N(b) = distinct pool values inside the row's own tolerance band; PASS iff N(b) = 1; FAIL (identified) iff N(b) >= 2."""
import itertools, math, json, os, hashlib
from fractions import Fraction as F
score, cf = [], []
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
V = [2, 3, 5, 6, 7, 137]; NAMES = {2: 'rank', 3: 'N_c', 5: 'n_C', 6: 'C_2', 7: 'g', 137: 'N_max'}
prods = {}
for k in range(0, 4):
    for m in itertools.combinations_with_replacement(V, k):
        prods.setdefault(math.prod(m) if m else 1, []).append('·'.join(NAMES[x] for x in m) or '1')
pool = {}
for a, na in prods.items():
    for b, nb in prods.items():
        q = F(a, b); lab = f"{na[0]}/{nb[0]}" if b != 1 else na[0]
        for val, tag in ((float(q), lab), (math.sqrt(q), f"√({lab})")):
            key = round(val, 12)
            if key not in pool or len(tag) < len(pool[key]): pool[key] = tag
vals = sorted(pool); P = len(vals)
print(f"pool |P| = {P} distinct values (5755's menu)")
EPS = 1e-9
def inband(lo, hi): return [(v, pool[v]) for v in vals if lo * (1 - EPS) <= v <= hi * (1 + EPS)]
def chance(T, lo, hi, win=2): return sum(1 for v in vals if T / win <= v <= T * win) * math.log(hi / lo) / (2 * math.log(win))
rows = [("theta13", 2.19e-2, 0.07e-2, 1 / 45, "1/(N_c²·n_C) = 1/45", "target"),
        ("eta_bar", 0.3523, 0.0071, 1 / (2 * math.sqrt(2)), "1/(2√2)", "positive control (K1809 retired; must FAIL)"),
        ("lambda", 0.22431, 0.00085, 1 / math.sqrt(20), "1/√20", "negative control (T2530 blind; must PASS)")]
res = {}
for nm, T, sT, pub, form, role in rows:
    tol = abs(pub - T) / T; z = (pub - T) / sT
    print(f"\n{nm} [{role}]: T = {T:.6g} ± {sT:.2g}; published {form} = {pub:.6g}, {100*tol:.2f} % off, {z:+.1f}σ")
    out = {}
    for lab, lo, hi in (("(a) 1σ", T - sT, T + sT), ("(b) row tol", T * (1 - tol), T * (1 + tol))):
        ib = inband(lo, hi); ch = chance(T, lo, hi)
        print(f"   {lab:12} [{lo:.6g}, {hi:.6g}]: N = {len(ib):2d} of {P}   chance {ch:.2f}   surprising: {'YES' if len(ib) > ch + 2*math.sqrt(max(ch,1e-9)) else 'no'}   forms: " + ", ".join(f"{t}={x:.5g}" for x, t in ib[:12]))
        out[lab] = (len(ib), ch, [t for _, t in ib])
    if nm == "eta_bar":
        ib = inband(0.349 - 0.010, 0.349 + 0.010); print(f"   (a') K1809's band 0.349 ± 0.010: N = {len(ib)}  {[t for _, t in ib]}")
    c0 = any(abs(x - pub) < 1e-9 * pub for x, _ in inband(pub * 0.999, pub * 1.001))
    res[nm] = dict(T=T, sT=sT, pub=pub, tol=tol, z=z, Na=out["(a) 1σ"][0], Nb=out["(b) row tol"][0], cha=out["(a) 1σ"][1], chb=out["(b) row tol"][1],
                   forms_b=out["(b) row tol"][2], C0=c0, rule="PASS" if out["(b) row tol"][0] == 1 else "FAIL")
print()
sc("C0 must-catch: every published form is in the pool", all(r["C0"] for r in res.values()), False, str({k: r["C0"] for k, r in res.items()}))
sc("P1 reproduction of 5755: θ13 N(b) = 4, N(a) = 9", res["theta13"]["Nb"] == 4 and res["theta13"]["Na"] == 9, False, f"N(b) = {res['theta13']['Nb']}, N(a) = {res['theta13']['Na']}")
sc("P2 positive control: η̄ FAILS the rule (N(b) ≥ 2)", res["eta_bar"]["Nb"] >= 2, True, f"N(b) = {res['eta_bar']['Nb']}: {res['eta_bar']['forms_b']}")
sc("P3 negative control: λ = 1/√20 PASSES the rule (N(b) = 1)", res["lambda"]["Nb"] == 1, True, f"N(b) = {res['lambda']['Nb']}: {res['lambda']['forms_b']}")
surp = [nm for nm, r in res.items() for N, ch in ((r["Na"], r["cha"]), (r["Nb"], r["chb"])) if N > ch + 2 * math.sqrt(max(ch, 1e-9))]
sc("P4 density control: no row surprising", not surp, False, f"surprising = {surp or 'none'}")
decidable = res["lambda"]["Nb"] == 1
print("\nVERDICT (rule: PASS iff N(b) = 1; FAIL ⟹ IDENTIFIED iff N(b) ≥ 2; band (b) = the row's own tolerance):")
for nm, r in res.items():
    print(f"   {nm:8}: N(b) = {r['Nb']} of |P| = {P} (chance {r['chb']:.2f}); N(a) = {r['Na']} (chance {r['cha']:.2f}); rule {r['rule']}")
th = res["theta13"]
word = ("IDENTIFIED" if th["rule"] == "FAIL" else "stays") if decidable else "NOT DECIDABLE BY THIS INSTRUMENT (negative control failed)"
print(f"   θ13 = 1/45: N(b) = {th['Nb']} of {P}; rule {th['rule']}; word {word}")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s, c in zip(score, cf) if c and s)}/{sum(cf)} can-fail hit")
here = os.path.dirname(os.path.abspath(__file__))
json.dump({"pool_size": P, "rows": res, "word": word}, open(os.path.join(here, ".record_5769.json"), "w"), indent=1)
