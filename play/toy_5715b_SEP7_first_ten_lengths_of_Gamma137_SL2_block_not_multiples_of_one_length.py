#!/usr/bin/env python3
"""Toy 5715b — K1872 §4 item for Elie: the first ten primitive lengths of Gamma(137) in the SL2 block. Traces t ≡ 2 (mod 137²)
with |t| > 2 (5715 P1); existence per trace from 5715 P2's matrix counts (k = 1..6 > 0) and the sign symmetry t -> -t
(negate the matrix; -gamma ∈ Gamma(137)? no: -1 ≢ 1 mod 137 — so negative traces need a ≡ d ≡ 1 mod 137 with a + d < -2,
i.e. i + j = -137k: the same divisibility argument, same counts). Primitive: t < 18771² so not a power. Lengths 2 log λ(t)."""
import math, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); q2 = 137 * 137
traces = []
for k in range(1, 6):
    traces += [2 + q2 * k, -(2 + q2 * k) + 4]      # t = 2 + 137² k and t = 2 - 137² k (both ≡ 2 mod 137²); |t| > 2
traces = sorted(set(abs(t) for t in traces))
lengths = [2 * math.log((t + math.sqrt(t * t - 4)) / 2) for t in traces][:10]
print("first ten primitive lengths in the SL2 block of Gamma(137):")
for t, L in zip(traces[:10], lengths): print(f"  |trace| = {t:7d}   length = {L:.6f}   ratio to the first = {L/lengths[0]:.6f}")
mult = all(abs(L / lengths[0] - round(L / lengths[0])) < 1e-6 for L in lengths)
print(f"\nmultiples of one length: {mult} — the spectrum is 2 log(137² k ± ...), logarithmic in k, not n·ℓ₀; T1448's 'families indexed by winding n' is refuted by exhibit.")
json.dump({'traces': traces[:10], 'lengths': lengths}, open(os.path.join(HERE, '.hterm_5715b.json'), 'w'), indent=1)
