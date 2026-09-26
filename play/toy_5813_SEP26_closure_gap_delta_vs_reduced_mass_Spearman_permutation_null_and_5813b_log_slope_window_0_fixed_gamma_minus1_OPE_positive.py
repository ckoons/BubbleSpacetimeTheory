#!/usr/bin/env python3
"""
Toy 5813 (+5813b) — Casey's winding closure gap: is |δ| mass-independent (a window) or does it track μ? (Elie, 2026-09-26)
5813 prereg bc903cb1 (Cal hashed, S993 (3)); 5813b prereg 3223914b (the slope test Cal named as owed; hashed before δ read).
Class, thresholds and masses: Grace's toy 5810, reused verbatim (exec'd up to its checks). δ = M − M_thr (nearest V_OPEN pair);
μ = reduced mass of THAT pair. The 3 Tcccc states have NO V_OPEN threshold in 5810's class definition → μ undefined → reported,
excluded by the frozen definition (not by choice): N = 14 for 5813.
"""
import glob, math, random
import numpy as np
from itertools import product, combinations_with_replacement
src = open(glob.glob('play/toy_5810_*.py')[0]).read()
ns = {}; exec(src[:src.index("score = total = 0")], ns)
M, CLASS = ns['M'], ns['CLASS']
Dq = ns['Dq']
OPEN_PAIRS = {
 "ccbar":  [(x, y) for x, y in product(Dq, Dq)] + list(combinations_with_replacement(["Ds", "Ds*"], 2)),
 "ccbars": [(x, y) for x, y in product(["Ds", "Ds*"], Dq)],
 "cc":     [(x, y) for x, y in product(Dq, Dq)],
 "cccc":   [],
 "bbbar":  [(x, y) for x, y in product(["B+", "B0", "B*"], ["B+", "B0", "B*"])],
}
# consistency with 5810's threshold lists
assert all({M[a]+M[b] for a, b in OPEN_PAIRS[s]} == set(ns['TH'][s]['open']) for s in OPEN_PAIRS)
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
rows = []
for name, m, sec, _ in CLASS:
    if not OPEN_PAIRS[sec]:
        print(f"  {name:16s} {m:8.1f}  no V_OPEN threshold -> excluded by definition"); continue
    a, b = min(OPEN_PAIRS[sec], key=lambda p: abs(m - M[p[0]] - M[p[1]]))
    thr = M[a] + M[b]; mu = M[a]*M[b]/(M[a]+M[b]); d = m - thr
    rows.append((name, m, a, b, thr, mu, d))
    print(f"  {name:16s} {m:8.1f}  {a:>4s}+{b:<4s} thr {thr:8.2f}  μ = {mu:7.1f}  δ = {d:+7.1f}")
N = len(rows); mu = np.array([r[5] for r in rows]); ad = np.abs([r[6] for r in rows]); dd = np.array([r[6] for r in rows])
def spearman(x, y):
    rx = np.argsort(np.argsort(x)); ry = np.argsort(np.argsort(y))
    return np.corrcoef(rx, ry)[0, 1]
rs = spearman(ad, mu)
rng = np.random.default_rng(5813)
perm = np.array([spearman(rng.permutation(ad), mu) for _ in range(100000)])
p_pos = np.mean(perm >= rs); p_two = np.mean(np.abs(perm) >= abs(rs))
print(f"\n5813: N = {N}; Spearman ρ_s(|δ|, μ) = {rs:+.3f}; permutation p(ρ ≥ obs) = {p_pos:.3f}, two-sided p = {p_two:.3f}")
check("5813 KILL (ρ_s > 0 at p < 0.05: |δ| tracks μ like OPE) NOT fired", not (rs > 0 and p_pos < 0.05))
check("5813 DIRECTION: no significant correlation either sign (two-sided p > 0.05)", p_two > 0.05)
# power: what ρ_s would |δ| ∝ μ (OPE-like) produce with the observed scatter? scale |δ| by μ/mean(μ) keeping residual order
pw = np.mean([ (lambda y: spearman(y, mu))(np.abs(rng.permutation(ad)) * mu/mu.mean()) for _ in range(20000)])
pw_p = np.mean([spearman(np.abs(rng.permutation(ad)) * mu/mu.mean(), mu) > np.quantile(perm, 0.95) for _ in range(20000)])
print(f"   power: an |δ| ∝ μ law with the observed scatter gives mean ρ_s = {pw:+.3f}; detected at p<0.05 in {100*pw_p:.0f}% of draws")
# ---- 5813b: slope on the below-threshold subset ----
below = [r for r in rows if r[6] < 0]
print(f"\n5813b: below-threshold subset N = {len(below)}: {[r[0] for r in below]}")
if len(below) < 4:
    check("5813b: at least 4 below-threshold states (else 'no test')", False)
else:
    x = np.log([r[5] for r in below]); y = np.log([abs(r[6]) for r in below])
    b, a0 = np.polyfit(x, y, 1)
    rng2 = np.random.default_rng(5813); bs = []
    idx = np.arange(len(below))
    for _ in range(10000):
        s = rng2.choice(idx, len(idx), replace=True)
        if np.ptp(x[s]) > 0: bs.append(np.polyfit(x[s], y[s], 1)[0])
    lo, hi = np.quantile(bs, [0.025, 0.975])
    res = y - (a0 + b*x); se = math.sqrt(np.sum(res**2)/(len(x)-2)/np.sum((x-x.mean())**2))
    from scipy.stats import t as tdist
    tq = tdist.ppf(0.975, len(x)-2)
    print(f"   slope b = {b:+.3f}; 95% bootstrap [{lo:+.2f}, {hi:+.2f}]; OLS t-interval [{b-tq*se:+.2f}, {b+tq*se:+.2f}]; leverage sd(log μ) = {x.std():.3f}")
    win_out = not (lo <= 0 <= hi); fg_out = not (lo <= -1 <= hi); ope_out = hi <= 0
    print(f"   disfavoured (value outside 95%): window(0) {win_out}, fixed-γ(−1) {fg_out}, OPE-deep(>0) {ope_out}")
    check("5813b DIRECTION: no discrimination — the 95% interval contains both 0 and −1", (not win_out) and (not fg_out))
    xa = np.log(mu); ya = np.log(np.maximum(ad, 0.05))
    print(f"   secondary (all {N}, |δ| floored at 0.05 MeV): slope {np.polyfit(xa, ya, 1)[0]:+.3f}, sd(log μ) = {xa.std():.3f}")
print(f"\nSCORE: {sum(score)}/{len(score)}")
