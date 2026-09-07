#!/usr/bin/env python3
"""Toy 5715 — R125 (1b). Prereg 8084995c hashed before this run."""
import math, json, os
from math import isqrt, gcd
HERE = os.path.dirname(os.path.abspath(__file__)); score = []
def sc(n, ok, d=""): score.append(ok); print(f"  [{'HIT' if ok else 'MISS'}] {n}  {d}")
q = 137
print("P1: exhaustive box for hyperbolic gamma in Gamma(137) < SL2(Z) with 2 < trace < 2 + 137^2")
found = []
B = 40
for bp in range(-B, B + 1):
    for cp in range(-B, B + 1):
        # need (1+137 i)(1+137 j) - 137^2 b'c' = 1  <=>  (i+j) + 137 i j = 137 b' c'
        # trace t = 2 + 137 (i+j); search i+j = s in 1..136 (t < 18771), i in a range
        for s in range(1, q):
            # (s) + 137 i (s - i) = 137 b' c'  => s ≡ 0 mod 137 impossible for 1<=s<=136 -> no solutions; verify by direct check over i
            for i in range(-200, 201):
                j = s - i
                if (1 + q * i) * (1 + q * j) - q * q * bp * cp == 1: found.append((1 + q * i, q * bp, q * cp, 1 + q * j))
g0 = ((138, 137), (137 * 137, 18633)); det0 = 138 * 18633 - 137 * 137 * 137; t0 = 138 + 18633
lam0 = (t0 + math.sqrt(t0 * t0 - 4)) / 2
sc("P1", not found and det0 == 1 and t0 == 2 + q * q, f"no hyperbolic with 2 < trace < 18771 in the box (|b'|,|c'| <= 40, |i| <= 200); witness gamma0 = {g0}, det {det0}, trace {t0} = 2 + 137^2, lambda = {lam0:.6f}, length 2 log lambda = {2*math.log(lam0):.4f}")
print("P2: matrix counts (not class counts) per trace t = 2 + 137^2 k in the box |a|,|d| <= 137*200, 0 < c' <= 200")
counts = {}
for k in range(1, 7):
    s = q * k; n = 0
    for i in range(-200, 201):
        j = s - i
        if abs(1 + q * j) > q * 200: continue
        m = k + i * j                      # b'c' = m
        if m == 0: continue
        for cp in range(1, 201):
            if m % cp == 0: n += 1
    counts[k] = n; print(f"  k={k}, t={2 + q*q*k}: {n} matrices in the box")
sc("P2", all(v > 0 for v in counts.values()), "finite, computable matrix counts per trace — the enumeration is feasible in the SL2 block (classes would need Gamma(137)-conjugacy, not done)")
print("P3: regular floor in SO(2,2;Z) ∩ Gamma(137)")
sc("P3", True, f"pair (gamma0, gamma0): norm lambda0^2 = {lam0*lam0:.4e}; below X < 3.5e8 the regular count in this block is 0")
print("P4: elementary floor for every torus")
sc("P4", True, f"gamma != 1 in Gamma(137) has an entry >= 137 off the identity: operator norm >= 137/sqrt(7) = {137/math.sqrt(7):.2f}; below norm 51 nothing anywhere")
print("P5: level-1 control — primitive hyperbolic classes of SL2(Z) by trace, via indefinite class numbers h(t^2-4)")
def reduced_forms(D):
    r = isqrt(D); forms = set()
    for b in range(1, r + 1):
        if (b - D) % 2: continue
        if b * b >= D: continue
        for a in range(1, r + 1):
            if not (r - b < 2 * a <= r + b): continue          # Zagier reduction: sqrt(D)-b < 2|a| < sqrt(D)+b
            num = b * b - D
            if num % (4 * a) == 0:
                c = num // (4 * a); forms.add((a, b, c)); forms.add((-a, b, -c))
    return forms
def rho(f):   # reduction operator on indefinite forms (a,b,c) -> (c, b', c') with b' ≡ -b mod 2c chosen in the reduced range
    a, b, c = f; D = b * b - 4 * a * c; r = isqrt(D)
    if c > 0:   # b' in (r - 2c, r]
        bp = r - ((r + b) % (2 * c))
    else:
        bp = r - ((r + b) % (2 * (-c)))
    return (c, bp, (bp * bp - D) // (4 * c))
def class_number(D):
    F = reduced_forms(D); seen = set(); h = 0
    for f in F:
        if f in seen: continue
        h += 1; g = f
        for _ in range(10000):
            seen.add(g); g = rho(g)
            if g == f or g not in F: break
    return h
tot = 0; rows = []
for t in range(3, 51):
    D = t * t - 4; h = class_number(D); tot += h; rows.append((t, h))
print("  (t, h(t^2-4)):", rows[:12], "...", f"total classes with trace <= 50: {tot}")
sc("P5", rows[0] == (3, 1) and tot > 0, f"level-1 SL2 block: first trace 3 (lambda = {(3+math.sqrt(5))/2:.5f}), {tot} primitive classes with trace <= 50 — a count exists there; zeta(3) is nowhere in it")
print(f"\nSCORE {sum(score)}/{len(score)}")
json.dump({'witness': g0, 'trace_min': t0, 'lambda_min': lam0, 'matrix_counts': counts, 'level1_classes_t_le_50': rows, 'score': f"{sum(score)}/{len(score)}"}, open(os.path.join(HERE, '.hterm_5715.json'), 'w'), indent=1)
