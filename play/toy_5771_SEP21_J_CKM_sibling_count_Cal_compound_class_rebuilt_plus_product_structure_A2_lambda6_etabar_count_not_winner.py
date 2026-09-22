#!/usr/bin/env python3
"""Toy 5771 — J_CKM = √2/50000 sibling count: (I) Cal's compound class rebuilt (K1809-B/§705), (II) the product structure A²λ⁶η̄.
Prereg: notes/Elie_PREREG_5771_..._2026-09-21.md. Report the count, not the winner: no in-band form is printed; lists go to the record only.
Elie, 2026-09-21."""
import math, itertools, json, os, sys
from fractions import Fraction as F
import numpy as np
score, cf = [], []
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
V = [2, 3, 5, 6, 7, 137]; NAMES = {2: 'rank', 3: 'N_c', 5: 'n_C', 6: 'C_2', 7: 'g', 137: 'N_max'}
DMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 5   # Cal may amend at the hash; default 0..5 (contains 2^4·5^5)
# ---- pins (PDG 2024 CKM review) ----
JT, Jp, Jm = 3.12e-5, 0.13e-5, 0.12e-5
Jpub = math.sqrt(2) / 50000
lam, slam = 0.22501, 0.00068; A_, sAp, sAm = 0.826, 0.016, 0.015; eta, sep, sem = 0.3523, 0.0073, 0.0071
K1809_band = (2.77e-5 - 0.11e-5, 2.77e-5 + 0.11e-5)
tol = abs(Jpub - JT) / JT
print("=" * 100 + f"\nTOY 5771 — J sibling count. T = {JT:.3g} (+{Jp:.2g}/−{Jm:.2g}); published √2/50000 = {Jpub:.6g}, {100*tol:.2f} % off, z = {(Jpub-JT)/Jm:+.2f}σ\n" + "=" * 100)
# ---- Instrument I: compound class ----
nums = {}
nums[1.0] = "1"
for a in V:
    nums.setdefault(float(a), NAMES[a]); nums.setdefault(math.sqrt(a), f"√{NAMES[a]}")
    for b in V: nums.setdefault(float(a * b), f"{NAMES[a]}·{NAMES[b]}")
dens = {}
for c in V:
    for d in range(0, DMAX + 1):
        for e in V:
            for f in range(0, DMAX + 1):
                dens.setdefault(c ** d * e ** f, f"{NAMES[c]}^{d}·{NAMES[e]}^{f}")
poolI = {}
for n, ns in nums.items():
    for d, ds in dens.items():
        v = n / d; k = round(math.log(v), 11)
        if k not in poolI or len(ns + ds) < len(poolI[k][1]): poolI[k] = (v, f"{ns}/({ds})")
valsI = sorted(v for v, _ in poolI.values()); tagI = {round(math.log(v), 11): t for v, t in poolI.values()}
PI = len(valsI)
print(f"\n(I) compound class: numerator {{1, a, √a, a·b}}, denominator c^d·e^f, d,f ∈ 0..{DMAX}: |P| = {PI} (Cal reported 5,458; his script not retained)")
EPS = 1e-9
def inb(vals, lo, hi): return [v for v in vals if lo * (1 - EPS) <= v <= hi * (1 + EPS)]
def chance(vals, T, lo, hi, w=2): return sum(1 for v in vals if T / w <= v <= T * w) * math.log(hi / lo) / (2 * math.log(w))
bands = {"(a) PDG2024 1σ": (JT - Jm, JT + Jp), "(a') K1809 band": K1809_band, "(b) row tol": (JT * (1 - tol), JT * (1 + tol))}
resI = {}
for lab, (lo, hi) in bands.items():
    ib = inb(valsI, lo, hi); ch = chance(valsI, JT, lo, hi)
    surp = len(ib) > ch + 2 * math.sqrt(max(ch, 1e-9))
    print(f"   {lab:16} [{lo:.4g}, {hi:.4g}]: N = {len(ib):3d} of {PI}   chance {ch:.1f}   surprising: {'YES' if surp else 'no'}")
    resI[lab] = dict(N=len(ib), chance=ch, surprising=surp, forms=[tagI[round(math.log(v), 11)] for v in ib])
c0 = any(abs(v - Jpub) < 1e-12 for v in valsI)
sc("P1 C0 must-catch: √2/(rank⁴·n_C⁵) in pool I", c0, False)
NK = resI["(a') K1809 band"]["N"]  # amendment 09-22 08:3x: the f-string key was mistyped as (a'') and raised KeyError after the (I) counts printed; scoring line only
sc("P2 reproduction by convention: N on K1809's band in [25, 60] (Cal 41)", 25 <= NK <= 60, False, f"N = {NK}")
sc("P3 N(b) ≥ 2 ⟹ FAIL ⟹ IDENTIFIED", resI["(b) row tol"]["N"] >= 2, True, f"N(b) = {resI['(b) row tol']['N']}")
sc("P4 N(a) ≥ 2 at the PDG 2024 1σ band", resI["(a) PDG2024 1σ"]["N"] >= 2, True, f"N(a) = {resI['(a) PDG2024 1σ']['N']}")
sc("P5 density control: nothing surprising", not any(r["surprising"] for r in resI.values()), False)
# ---- Instrument II: product structure on the 5755 menu ----
prods = {}
for k in range(0, 4):
    for m in itertools.combinations_with_replacement(V, k):
        prods.setdefault(math.prod(m) if m else 1, '·'.join(NAMES[x] for x in m) or '1')
poolII = {}
for a, na in prods.items():
    for b, nb in prods.items():
        q = F(a, b); lab = f"{na}/{nb}" if b != 1 else na
        for val, tag in ((float(q), lab), (math.sqrt(q), f"√({lab})")):
            key = round(val, 12)
            if key not in poolII or len(tag) < len(poolII[key]): poolII[key] = tag
valsII = np.array(sorted(poolII)); PII = len(valsII)
def band_set(T, lo, hi): return valsII[(valsII >= lo * (1 - EPS)) & (valsII <= hi * (1 + EPS))]
S_l = band_set(lam, lam - slam, lam + slam); S_A = band_set(A_, A_ - sAm, A_ + sAp); S_e = band_set(eta, eta - sem, eta + sep)
print(f"\n(II) product structure J_W = A²λ⁶η̄ on the 5755 menu (|P| = {PII}): |S_λ| = {len(S_l)}, |S_A| = {len(S_A)}, |S_η̄| = {len(S_e)}  (1σ bands, PDG 2024 eq. 12.26)")
corp = (1 / math.sqrt(20), 0.8, 1 / (2 * math.sqrt(2)))
print(f"   corpus triple (1/√20, 4/5, 1/(2√2)): z_λ = {(corp[0]-lam)/slam:+.2f}σ, z_A = {(corp[1]-A_)/sAm:+.2f}σ, z_η̄ = {(corp[2]-eta)/sep:+.2f}σ; J_W = {corp[1]**2*corp[0]**6*corp[2]:.6g}")
def count_tri(Sl, SA, Se, lo, hi):
    if len(Sl) == 0 or len(SA) == 0 or len(Se) == 0: return 0, []
    J = (SA[:, None, None] ** 2) * (Sl[None, :, None] ** 6) * Se[None, None, :]
    m = (J >= lo) & (J <= hi); idx = np.argwhere(m)
    return int(m.sum()), [(float(Sl[j]), float(SA[i]), float(Se[k])) for i, j, k in idx[:200]]
resII = {}
for lab in ("(a) PDG2024 1σ", "(b) row tol"):
    lo, hi = bands[lab]; n, trip = count_tri(S_l, S_A, S_e, lo, hi); resII[lab] = dict(N_tri=n, triples=trip)
    print(f"   N_tri{lab[:3]} = {n}  of {len(S_l)*len(S_A)*len(S_e)} all-in-band triples")
L_l = band_set(lam, lam / 2, 2 * lam); L_A = band_set(A_, A_ / 2, 2 * A_); L_e = band_set(eta, eta / 2, 2 * eta)
lo, hi = bands["(a) PDG2024 1σ"]; nloose, _ = count_tri(L_l, L_A, L_e, lo, hi)
print(f"   saturation: N_loose = {nloose} triples from ×2-loose factor ranges ({len(L_l)}·{len(L_A)}·{len(L_e)} = {len(L_l)*len(L_A)*len(L_e)}) land in J's 1σ band")
in_sets = (any(abs(S_l - corp[0]) < 1e-9)) and (any(abs(S_A - corp[1]) < 1e-9)) and (any(abs(S_e - corp[2]) < 1e-9))
sc("P6 the corpus's triple is NOT in S_λ×S_A×S_η̄", not in_sets, True, f"in-band: λ {bool(any(abs(S_l-corp[0])<1e-9))}, A {bool(any(abs(S_A-corp[1])<1e-9))}, η̄ {bool(any(abs(S_e-corp[2])<1e-9))}")
sc("P7 N_tri(a) ≥ 1", resII["(a) PDG2024 1σ"]["N_tri"] >= 1, True, f"N_tri(a) = {resII['(a) PDG2024 1σ']['N_tri']}")
Nb = resI["(b) row tol"]["N"]
print(f"\nVERDICT: J = √2/50000: N(b) = {Nb} of |P| = {PI}; rule {'PASS' if Nb == 1 else 'FAIL'}; word {'stays' if Nb == 1 else 'IDENTIFIED (K1809: retire; count reported, winner not named)'}")
print(f"         product: N_tri(a) = {resII['(a) PDG2024 1σ']['N_tri']}, N_tri(b) = {resII['(b) row tol']['N_tri']}, N_loose = {nloose}")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s, c in zip(score, cf) if c and s)}/{sum(cf)} can-fail hit")
here = os.path.dirname(os.path.abspath(__file__))
json.dump(dict(DMAX=DMAX, pool_I=PI, pool_II=PII, I=resI, II={k: dict(N_tri=v["N_tri"], triples=v["triples"]) for k, v in resII.items()}, N_loose=nloose,
               S_sizes=[len(S_l), len(S_A), len(S_e)]), open(os.path.join(here, ".record_5771.json"), "w"), indent=1)
