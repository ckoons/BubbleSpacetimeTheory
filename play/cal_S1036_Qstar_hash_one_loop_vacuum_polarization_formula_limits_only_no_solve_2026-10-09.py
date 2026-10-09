#!/usr/bin/env python3
"""Cal Section 1036 (2026-10-09) — the α running test, item 5(h): FORMULA CHECK ONLY.
This instrument verifies the hashed one-loop formula's two limits. It does NOT
solve α_eff^{-1}(Q) = 137 and prints no value near m_e. Elie solves after the hash.

Hashed formula (on-shell scheme, one electron loop, spacelike Q^2 = -q^2 > 0;
Peskin–Schroeder 7.91 with q^2 -> -Q^2):
    α_eff^{-1}(Q) = α^{-1}(0) - Δ(Q),
    Δ(Q) = (2/π) ∫_0^1 dx x(1-x) ln[1 + x(1-x) Q^2/m_e^2]        (independent of α)
Limits: Δ(0) = 0;  Δ(Q >> m_e) -> (1/3π)[ln(Q^2/m_e^2) - 5/3].
"""
import numpy as np
from math import pi, log

def Delta(r2, n=200001):
    """r2 = Q^2/m_e^2. Simpson on [0,1]."""
    x = np.linspace(0.0, 1.0, n)
    f = x*(1-x)*np.log1p(x*(1-x)*r2)
    h = x[1]-x[0]
    return (2/pi) * h/3 * (f[0] + f[-1] + 4*f[1:-1:2].sum() + 2*f[2:-1:2].sum())

score = 0; total = 0
def check(name, ok, detail=""):
    global score, total
    total += 1; score += bool(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {detail}" if detail else ""))

check("Δ(0) = 0", abs(Delta(0.0)) < 1e-15)
for r2 in (1e4, 1e6, 1e8):
    asym = (1/(3*pi))*(log(r2) - 5/3)
    d = Delta(r2)
    check(f"Δ -> (1/3π)[ln(Q²/m²) − 5/3] at Q²/m² = {r2:.0e}", abs(d/asym - 1) < 2e-2*1e4/r2**0.5 + 1e-3, f"ratio {d/asym:.5f}")
check("Δ is monotone increasing in Q (α^{-1} falls with Q: screening direction)",
      all(Delta(a) < Delta(b) for a, b in ((0.01, 0.1), (0.1, 1.0), (10.0, 100.0))))
print("  (no value of Δ at or near Q = m_e is printed; Elie solves)")
print(f"\nSCORE: {score}/{total}")
