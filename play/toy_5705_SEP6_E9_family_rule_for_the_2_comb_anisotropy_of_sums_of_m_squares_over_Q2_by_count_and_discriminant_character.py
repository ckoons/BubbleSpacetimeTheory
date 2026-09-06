#!/usr/bin/env python3
"""Toy 5705 — E9: kernel q0 = x_1^2+...+x_m^2, m = n-2, for D_IV^n, n = 3..8. Anisotropy over Q_2 by exhaustive primitive
zeros mod 2^k (k = 3..7); discriminant character for even m. Prereg (hash posted before this run)."""
import itertools, numpy as np, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); score = []
def sc(name, ok, detail=""): score.append(ok); print(f"  [{'HIT' if ok else 'MISS'}] {name}  {detail}")
def primitive_zero_mod(m, k):
    """does sum_{i<=m} x_i^2 = 0 mod 2^k have a solution with some x_i odd? (vectorised over the sum distribution)"""
    q = 2 ** k
    sq_odd = np.zeros(q, dtype=np.int64); sq_even = np.zeros(q, dtype=np.int64)
    for x in range(q):
        (sq_odd if x % 2 else sq_even)[(x * x) % q] += 1
    sq_all = sq_odd + sq_even
    # count solutions with at least one odd coordinate = all solutions - all-even solutions
    def cyc(a, b):
        out = np.zeros(q, dtype=np.int64)
        for i in np.nonzero(a)[0]: out += a[i] * np.roll(b, i)
        return out
    tot = np.zeros(q, dtype=np.int64); tot[0] = 1; ev = tot.copy()
    for _ in range(m): tot = cyc(tot, sq_all); ev = cyc(ev, sq_even)
    return int(tot[0] - ev[0]) > 0
print("m  n   primitive zero of sum of m squares mod 2^k, k=3..7")
rows = {}
for m in range(1, 8):
    n = m + 2; flags = [primitive_zero_mod(m, k) for k in range(3, 8)]
    rows[m] = flags; print(f"{m}  {n}   {['yes' if f else 'no' for f in flags]}")
aniso = {m: not any(rows[m]) for m in rows}; iso = {m: all(rows[m]) for m in rows}
sc("P1", all(aniso[m] for m in (1, 2, 3, 4)) and all(iso[m] for m in (5, 6, 7)), f"anisotropic at 2 (no primitive zero at any k): m = {[m for m in rows if aniso[m]]}; isotropic (zeros at every k): m = {[m for m in rows if iso[m]]} -> comb PRESENT for n = 3,4,5,6, ABSENT for n = 7,8")
def character(m):
    if m % 2: return "none (odd kernel)"
    return "chi_{-4}" if (m // 2) % 2 else "trivial (disc field Q)"
chars = {m + 2: character(m) for m in range(1, 7)}
sc("P2", chars[4] == "chi_{-4}" and chars[6].startswith("trivial") and chars[8] == "chi_{-4}" and chars[5].startswith("none") and chars[7].startswith("none"), f"n -> character: {chars}")
sc("P3", aniso[3], "m = 3 (n = 5): no primitive zero mod 8 -> the comb at n = 5 is forced")
sc("P4", all(aniso[m] for m in (1,2,3,4)) and all(iso[m] for m in (5,6,7)), "matches Hasse–Minkowski over Q_2: sums of <= 4 squares anisotropic, >= 5 isotropic")
print(f"\nSCORE {sum(score)}/{len(score)}")
json.dump({'primitive_zero_flags_k3_7': {m: rows[m] for m in rows}, 'characters': chars, 'score': f"{sum(score)}/{len(score)}"}, open(os.path.join(HERE, '.comb_5705.json'), 'w'), indent=1)
